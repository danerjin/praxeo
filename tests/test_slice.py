"""Tests for the Phase 2 thin slice."""
import json
import os
import re
from pathlib import Path

import pytest

from praxeo import engine, parser, vocabulary
from praxeo.combiner import combine
from praxeo.context import ground
from praxeo.verifier import verify
from praxeo.decider import FixtureDecider
from praxeo.pipeline import predict, run_case
from praxeo.schema import Assumption, Consequence, Finding, OutcomeCard, PolicyRecord, Source, Unclear
from praxeo.scoring import f1_block, score

ROOT = Path(__file__).resolve().parents[1]
SF = ROOT / "cases" / "sf_1994"
WE1 = ROOT / "cases" / "we001_riverton"
WE13 = ROOT / "cases" / "we013_halvern"


def _assumptions(p=0.9, **over):
    out = {}
    for atom in ("binding", "enforced", "alternative_uses", "nontransferable", "buyouts_limited", "would_leave",
                 "lockin_dominates", "keepers_dominate", "substitutes"):
        out[f"{atom}(c1)"] = Assumption(id=f"{atom}(c1)", text=atom, assumption_class="other", p=over.get(atom, p))
    return out


def _record():
    return parser.parse_fixture(SF / "record.json")


def _by_var(cons):
    return {(c.actor_class, c.variable): c for c in cons}


def test_engine_derives_ceiling_consequences():
    cons, _ = engine.run(_record(), _assumptions())
    got = {(c.actor_class, c.variable, c.sign) for c in cons}
    assert ("landlords.controlled", "quantity_supplied", "decrease") in got
    assert ("tenants.controlled", "turnover", "decrease") in got
    assert ("tenants.controlled.keepers", "relocation_out_of_area", "decrease") in got
    assert ("tenants.controlled.displaced", "relocation_out_of_area", "increase") in got
    assert all(c.reported for c in cons)


def test_vacancy_decontrol_replaces_shortage_with_initial_price():
    """PC-1 1.4: with free initial rents there is no excess demand; seekers' initial price rises."""
    rec = _record()
    assert rec.components[0].vacancy_decontrol
    got = {(c.actor_class, c.variable, c.sign) for c in engine.run(rec, _assumptions())[0]}
    assert not any(v == "excess_demand" for _, v, _ in got)
    assert ("tenants.prospective", "price_paid", "increase") in got
    rec.components[0].vacancy_decontrol = False
    got = {(c.actor_class, c.variable, c.sign) for c in engine.run(rec, _assumptions())[0]}
    assert ("tenants.prospective", "excess_demand", "increase") in got
    assert ("tenants.prospective", "price_paid", "increase") not in got


def test_minimal_assumption_labels():
    cons = _by_var(engine.run(_record(), _assumptions())[0])
    supply = cons[("landlords.controlled", "quantity_supplied")]
    assert supply.assumption_sets == [["alternative_uses(c1)", "binding(c1)", "enforced(c1)"]]
    assert [s.rule for s in supply.derivation] == ["PC-1", "PC-5"]


def test_cutoff_blocks_reporting():
    cons, _ = engine.run(_record(), _assumptions(binding=0.3))
    assert cons and not any(c.reported for c in cons)
    cons = _by_var(engine.run(_record(), _assumptions(alternative_uses=0.4))[0])
    assert not cons[("landlords.controlled", "quantity_supplied")].reported
    assert cons[("tenants.controlled", "turnover")].reported
    cons = _by_var(engine.run(_record(), _assumptions(buyouts_limited=0.4))[0])
    assert not cons[("tenants.controlled", "turnover")].reported  # PC-7 1.4 buyout premise


def test_exception_defeats_rule():
    cons = _by_var(engine.run(_record(), _assumptions(), extra="exception(pc_5, c1).\n")[0])
    assert ("landlords.controlled", "quantity_supplied") not in cons
    assert ("landlords.controlled", "reclassification") in cons  # RS-5 has its own exception


def test_per_reading_signs():
    """An unclear provision whose second reading blocks PC-5: one sign per reading."""
    rec = _record()
    rec.unclear.append(Unclear(id="U9", text="whether conversions are barred",
                               readings=["U9-a: conversions allowed", "U9-b: conversions barred"],
                               reading_facts={"U9-b": "exception(pc_5, c1)."}))
    cons = _by_var(engine.run(rec, _assumptions())[0])
    supply = cons[("landlords.controlled", "quantity_supplied")]
    assert supply.sign == "ambiguous"
    assert supply.sign_by_reading == {"U9-a": "decrease", "U9-b": "none"}
    assert cons[("tenants.controlled", "turnover")].sign_by_reading == {}  # same under both readings


def test_combiner_total_needs_dominance_premise():
    a = _assumptions()
    cons = combine(engine.run(_record(), a)[0], a)
    total = next(c for c in cons if c.actor_class == "tenants.controlled" and c.variable == "relocation_out_of_area")
    assert total.sign == "decrease" and "keepers_dominate(c1)" in total.assumptions and len(total.combines) == 2
    a = _assumptions(keepers_dominate=0.4)
    cons = combine(engine.run(_record(), a)[0], a)
    total = next(c for c in cons if c.actor_class == "tenants.controlled" and c.variable == "relocation_out_of_area")
    assert total.sign == "ambiguous"
    a = _assumptions(alternative_uses=0.3)  # no displaced subclass reported: total takes the keepers' sign
    cons = combine(engine.run(_record(), a)[0], a)
    total = next(c for c in cons if c.actor_class == "tenants.controlled" and c.variable == "relocation_out_of_area")
    assert total.sign == "decrease" and len(total.combines) == 1


def test_verifier_clean_and_catches_problems():
    a = _assumptions()
    cons = combine(engine.run(_record(), a)[0], a)
    assert verify(cons, a, _record()) == []
    bad = cons[0].model_copy(update={"variable": "happiness", "reported": not cons[0].reported})
    problems = verify([bad], a, _record())
    assert any("happiness" in p for p in problems) and any("cut-off" in p for p in problems)


def test_vocabulary_shared_by_rules_and_cards():
    files = sorted((ROOT / "praxeo" / "rules").glob("*.lp"))
    assert {f.name for f in files} >= {"price_controls.lp", "taxes.lp"} and engine.RULES == files
    lp = "\n".join(f.read_text() for f in files)
    used = set(re.findall(r'effect\([^,]+, [^,]+, "([a-z_]+)"', lp))
    assert used and all(vocabulary.check_variable(v) is None for v in used), used
    for card in ROOT.glob("cases/*/outcome_card.json"):
        oc = OutcomeCard.model_validate_json(card.read_text())
        assert [f.variable for f in oc.findings if vocabulary.check_variable(f.variable)] == []


def test_context_grounding_holds_back_later_sources():
    srcs = [Source(id="s1", date="1994-06-01", text="Rents rose 4% last year.", citation="t"),
            Source(id="s2", date="1999-01-01", text="Rents rose 20% last year.", citation="t")]
    rec, held = ground(_record(), srcs)
    assert held == ["s2"] and any("4%" in c for c in rec.context) and not any("20%" in c for c in rec.context)
    undated = _record().model_copy(update={"enacted": "year 0"})
    assert ground(undated, srcs)[1] == ["s1", "s2"]


def test_no_ceiling_no_consequences():
    rec = _record()
    rec.components[0].instrument = "price_floor"  # no rule file covers it (a per_unit_tax now has rules in taxes.lp)
    assert engine.run(rec, _assumptions())[0] == []


def test_citation_check():
    rec = _record()
    text = (SF / "policy.txt").read_text()
    assert parser.check_citations(rec, text) == []
    rec.components[0].source_sentences.append("Landlords must paint every unit blue.")
    assert len(parser.check_citations(rec, text)) == 1


def _c(i, actor, var, sign, horizon=("long",)):
    return Consequence(id=i, actor_class=actor, variable=var, sign=sign, horizon=list(horizon),
                       visibility="invisible", tier="B", derivation=[], assumption_sets=[[]],
                       assumptions=[], reported=True)


def _card(findings):
    return OutcomeCard(case="t", written_by="t", findings=findings, assumption_status=[], confounders=[], verification="t")


def _f(i, actor, var, ftype, sign=None):
    return Finding(id=i, actor_class=actor, variable=var, finding_type=ftype, sign=sign, horizon=["long"], source="t")


def test_scoring_rules():
    card = _card([_f("F1", "landlords", "quantity_supplied", "effect", "decrease"),
                  _f("F2", "tenants.controlled", "quality_per_unit", "null"),
                  _f("F3", "tenants.prospective", "price_paid", "effect", "increase")])
    preds = [
        _c("C1", "landlords", "quantity_supplied", "decrease"),  # matches F1
        _c("C1b", "landlords", "quantity_supplied", "decrease"),  # duplicate, merged
        _c("C5", "landlords.controlled", "quantity_supplied", "increase"),  # subclass: not verifiable by F1
        _c("C2", "tenants.controlled", "quality_per_unit", "decrease"),  # null finding: false positive
        _c("C3", "tenants.prospective", "price_paid", "ambiguous"),  # excluded, not recalled
        _c("C4", "officials", "enforcement_cost", "increase"),  # unverifiable
    ]
    s = f1_block(preds, card)
    assert s["predictions"] == 5
    assert s["matched"] == ["C1"] and s["false_positives"] == ["C2"]
    assert s["ambiguous"] == 1 and s["unverifiable_ids"] == ["C5", "C4"]
    assert s["precision"] == 0.5 and s["recall"] == 0.5 and s["f1"] == 0.5
    assert s["missed_findings"] == ["F3"]


def test_brier_and_logic_accuracy():
    card = OutcomeCard.model_validate_json((SF / "outcome_card.json").read_text())
    a = _assumptions(0.8)
    cons, _ = engine.run(_record(), a)
    s = score(cons, a, card)
    assert s["brier"]["mean"] == pytest.approx(0.04)
    # only consequences whose assumptions the card shows all held stay in the logic score
    status = {x.assumption: x.held for x in card.assumption_status}
    kept = [c for c in cons if c.reported and all(status.get(x.split("(")[0]) is True for x in c.assumptions)]
    assert s["logic"]["predictions"] == len(kept) < s["headline"]["predictions"]


def test_end_to_end_fixture(tmp_path):
    record = parser.parse_fixture(SF / "record.json")
    result = run_case(SF, record, FixtureDecider(SF / "answers.json"), tmp_path)
    for name in ("prediction.json", "score.json", "report.md"):
        assert (tmp_path / name).exists()
    pred = json.loads((tmp_path / "prediction.json").read_text())
    assert "findings" not in json.dumps(pred)  # the frozen log holds no outcome data
    assert result["score"]["headline"]["precision"] is not None
    assert "Compared with no" in (tmp_path / "report.md").read_text()


NEW_ATOMS = ("search_open", "selection_open", "quality_adjustable", "evasion", "opportunities_need_move",
             "can_organize", "durable_assets", "expected_to_last", "commutable", "relet_obstructs", "exit_process")


def _all_assumptions(**over):
    """Every ceiling assumption at 0.9 (including those of the rules widened for WE-001), with overrides."""
    out = _assumptions(**{k: v for k, v in over.items() if k not in NEW_ATOMS})
    for atom in NEW_ATOMS:
        out[f"{atom}(c1)"] = Assumption(id=f"{atom}(c1)", text=atom, assumption_class="other", p=over.get(atom, 0.9))
    return out


def _wide_record():
    """The SF record without vacancy decontrol (so PC-1 and PC-2 apply) and with a neighbouring market (RS-4)."""
    rec = _record()
    rec.components[0].vacancy_decontrol = False
    rec.components[0].neighbor_actor = "renters.neighbors"
    return rec


def _reported(cons):
    return {(c.actor_class, c.variable, c.sign) for c in cons if c.reported}


# For each widened rule: the consequences it gives, the exception name that defeats it, and an assumption that,
# set low, stops the consequence being reported (a premise below the 0.5 cut-off).
WIDE_RULES = {
    "PC-2 search": ([("tenants.prospective", "search_cost", "increase")], "pc_2", "search_open"),
    "PC-2 selection": ([("tenants.prospective", "allocation_by_non_price_criteria", "increase")], "pc_2", "selection_open"),
    "PC-4 quality": ([("tenants.controlled", "quality_per_unit", "decrease"),
                      ("landlords.controlled", "maintenance_spending", "decrease")], "pc_4", "quality_adjustable"),
    "PC-6 side payments": ([("tenants.prospective", "side_payments", "increase")], "pc_6", "evasion"),
    "PC-6 sublet": ([("tenants.controlled", "informal_activity", "increase")], "pc_6", "nontransferable"),
    "RS-10 recourse": ([("tenants.prospective", "disputes_settled_outside_courts", "increase")], "rs_10", "evasion"),
    "RS-11 job lock": ([("tenants.controlled", "job_changes", "decrease")], "rs_11", "opportunities_need_move"),
    "RS-7 lobbying": ([("tenants.controlled", "lobbying_effort", "increase"),
                       ("landlords.controlled", "lobbying_effort", "increase")], "rs_7", "can_organize"),
    "PC-16 transfer": ([("landlords.controlled", "net_price_received", "decrease")], "pc_16", "binding"),
    "OC-4 prevented": ([("tenants.prospective", "quantity_traded", "decrease"),
                        ("landlords.controlled", "quantity_traded", "decrease")], "oc_4", "alternative_uses"),
    "SB-4 capitalization": ([("landlords.controlled", "asset_value", "decrease")], "sb_4", "expected_to_last"),
    "OC-3 enforcement": ([("officials.enforcement", "enforcement_cost", "increase")], "oc_3", "enforced"),
    "RS-4 neighbours": ([("renters.neighbors", "price_paid", "increase")], "rs_4", "commutable"),
    "PC-5 held vacant": ([("landlords.controlled", "units_held_vacant", "increase")], "pc_5", "relet_obstructs"),
    "OC-2 process": ([("landlords.controlled", "compliance_cost", "increase")], "oc_2", "exit_process"),
}


@pytest.mark.parametrize("name", sorted(WIDE_RULES))
def test_widened_rule_fires_and_is_blocked(name):
    keys, exception, premise = WIDE_RULES[name]
    rec = _wide_record()
    got = _reported(engine.run(rec, _all_assumptions())[0])
    for k in keys:
        assert k in got, (name, k)
    # the exception defeats it
    got = {(c.actor_class, c.variable, c.sign) for c in engine.run(rec, _all_assumptions(), extra=f"exception({exception}, c1).\n")[0]}
    for k in keys:
        assert k not in got, (name, "exception", k)
    # a premise below the cut-off stops it being reported
    got = _reported(engine.run(rec, _all_assumptions(**{premise: 0.3}))[0])
    for k in keys:
        assert k not in got, (name, "low premise", k)


def test_pc2_members_are_not_met_under_vacancy_decontrol():
    """PC-1/PC-2 1.4: no excess demand where the price of a new contract is free, so no rationing members."""
    rec = _wide_record()
    rec.components[0].vacancy_decontrol = True
    got = _reported(engine.run(rec, _all_assumptions())[0])
    assert ("tenants.prospective", "search_cost", "increase") not in got
    assert ("tenants.prospective", "allocation_by_non_price_criteria", "increase") not in got
    assert ("tenants.prospective", "side_payments", "increase") in got  # PC-6 does not depend on excess demand


def test_neighbour_effect_needs_a_neighbour_in_the_record():
    rec = _wide_record()
    rec.components[0].neighbor_actor = None
    got = _reported(engine.run(rec, _all_assumptions())[0])
    assert not any(a == "renters.neighbors" for a, _, _ in got)


def test_enforcer_role_comes_from_the_record():
    rec = _wide_record()
    rec.components[0].enforcer_actor = "officials.rent_board"
    got = _reported(engine.run(rec, _all_assumptions())[0])
    assert ("officials.rent_board", "enforcement_cost", "increase") in got


def test_widened_rules_pass_the_verifier():
    rec = _wide_record()
    a = _all_assumptions()
    cons, _ = engine.run(rec, a)
    assert verify(combine(cons, a), a, rec) == []


def _we001_rows() -> dict[str, set[tuple[str, str, str]]]:
    """WE-001's normal-form table as {row id: {(actor class, variable, sign)}}. A cell naming several actor
    classes gives one key each; a qualifier in brackets is dropped; the table's bare `landlords` and `tenants`
    are the record's landlords.controlled and tenants.controlled."""
    md = (ROOT / "handbook" / "05_examples" / "WE-001_rent_freeze.md").read_text()
    table = md.split("## Consequence list (normal form)")[1].split("## Gaps found")[0]
    short = {"landlords": "landlords.controlled", "tenants": "tenants.controlled"}
    rows: dict[str, set[tuple[str, str, str]]] = {}
    for line in table.splitlines():
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) > 4 and re.match(r"C-\d+", cells[0]):
            actors = [re.sub(r"\s*\(.*", "", a).strip() for a in cells[1].split(",")]
            rows[cells[0]] = {(short.get(a, a), cells[2].split(" ")[0], cells[3]) for a in actors}
    return rows


# Engine consequences for WE-001 that are not rows of its table as written, each with the reason.
WE001_EXCEPTIONS = {
    ("tenants.controlled.keepers", "relocation_out_of_area", "decrease"): "PC-21 is newer than WE-001",
    ("tenants.controlled.displaced", "relocation_out_of_area", "increase"): "PC-21 is newer than WE-001",
    ("tenants.controlled", "relocation_out_of_area", "decrease"): "CR-12 total of the PC-21 subclasses",
    # PC-4 signs quality_per_unit and maintenance_spending. WE-001 section 5 (C-6) lists both; the normal-form
    # table keeps the quality row for the tenants who receive it and drops the landlords' spending.
    ("landlords.controlled", "maintenance_spending", "decrease"):
        "WE-001 section 5, C-6 lists it; the normal-form table omits the landlords' side",
}

# Rows of WE-001's table the engine does not produce, each with the reason (what it would need).
WE001_NOT_PRODUCED = {
    "C-10": "turnover increase for tenants in converted buildings: needs a CR-12 total of turnover (keepers against displaced) that the combiner does not form",
    "C-13": "developers' investment_target: needs the new-construction exemption and a combined sign of two opposing chains (LW-4, TS-2)",
    "C-14": "homebuyers' quantity_substitute: RS-5 signs reclassification only; the rental to owner-occupied market relation is a case fact",
    "C-17": "announcement-window price_paid: a per-window timing sign (RS-8)",
    "C-19": "taxpayers' resources_available_other_uses: OC-3 and OC-1 sign a general-budget payer as a group (at_least_one_decrease), which the engine cannot express",
    "C-21": "first-months price_paid: a per-window ambiguous sign (PC-3 against RS-8)",
    "C-28": "landlords' resources_available_other_uses: a CR-12 total (key money against rent forgone) with a dominance premise, not formed by the combiner",
    "C-29": "tenants' resources_available_other_uses: CR-8b, a core rule that has no pattern in the rule base",
    "C-30": "relocation payment under K3: a case-specific provision",
}
# Rows produced for only some of their actor classes.
WE001_PARTIAL = {"C-11": {("developers", "lobbying_effort", "increase")}}  # developers need the exemption fact


def test_consistent_with_worked_example_we001():
    """Every engine consequence for WE-001's record is a row of WE-001's consequence list, except those in
    WE001_EXCEPTIONS (each with its reason). The rows it does not produce are listed with a reason."""
    text = (WE1 / "policy.txt").read_text()
    record = parser.parse_fixture(WE1 / "record.json")
    pred = predict(text, record, FixtureDecider(WE1 / "answers.json"))
    assert pred["citation_problems"] == [] and pred["verifier_problems"] == []
    rows = _we001_rows()
    assert len(rows) == 30  # C-1 to C-30; the 31st table row (quality_adjusted_price) has no C id
    table_keys = set().union(*rows.values())
    produced = {(c["actor_class"], c["variable"], c["sign"]) for c in pred["consequences"] if c["reported"]}
    for key in produced:
        assert key in table_keys or key in WE001_EXCEPTIONS, key
    got = {rid for rid, keys in rows.items() if keys & produced}
    assert set(rows) - got == set(WE001_NOT_PRODUCED)
    for rid, missing in WE001_PARTIAL.items():
        assert rows[rid] - produced == missing
    assert len(got) == 21


def _we013_table() -> set[tuple[str, str, str]]:
    """(actor class, variable, sign) for every row of WE-013's normal-form table; a cell naming several
    actor classes or variables gives one row each."""
    md = (ROOT / "handbook" / "05_examples" / "WE-013_steel_tariff.md").read_text()
    table = md.split("## Consequence list (normal form)")[1].split("## Gaps found")[0]
    rows = set()
    for line in table.splitlines():
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) > 4 and re.match(r"C-\d+", cells[0]):
            for actor in cells[1].split(","):
                for var in cells[2].split("("[0])[0].split(","):
                    rows.add((actor.split("(")[0].strip(), var.split("(")[0].strip(), cells[3]))
    return rows


# Engine consequences for WE-013 that are not rows of its table as written, each with the reason.
WE013_EXCEPTIONS = {
    # TX-8 names `employment` for export industries; WE-013 records the labor effect as the group sign
    # at_least_one_decrease (employment or hours_worked), which the engine's sign set does not have.
    ("workers.export_industries", "employment", "decrease"):
        "TX-8 as written signs employment alone; the table's group sign at_least_one_decrease (C-32) is weaker",
    # C-22 names its actor in prose ("owners of steel-using firms"); the record's fixture gives the class a name.
    ("owners.steel_users", "asset_value", "decrease"):
        "C-22's actor is the prose 'owners of steel-using firms'; the record names that class owners.steel_users",
}

# Rows of the table the engine does not produce, each with the reason (kept so the gap stays visible).
WE013_NOT_PRODUCED = {
    "C-3": "group sign at_least_one_increase (employment or hours_worked)",
    "C-8": "RS-8: a sign per timing window (January to March against later)",
    "C-16": "group sign at_least_one_decrease",
    "C-30": "OC-1 on the factor market of the other domestic producers: needs CR-7a / CR-8a and a named class the record lacks",
    "C-32": "group sign at_least_one_decrease; the engine produces the weaker employment decrease (see WE013_EXCEPTIONS)",
}


def test_consistent_with_worked_example_we013():
    """Every engine consequence for WE-013's record appears in WE-013's consequence list (actor, variable, sign),
    except the listed exceptions. There is no outcome card for this fictional case."""
    text = (WE13 / "policy.txt").read_text()
    record = parser.parse_fixture(WE13 / "record.json")
    pred = predict(text, record, FixtureDecider(WE13 / "answers.json"))
    assert pred["citation_problems"] == [] and pred["verifier_problems"] == []
    rows = _we013_table()
    assert ("steelmakers.domestic", "quantity_supplied", "increase") in rows
    got = {(c["actor_class"], c["variable"], c["sign"]) for c in pred["consequences"] if c["reported"]}
    assert got
    for key in got:
        assert key in rows or key in WE013_EXCEPTIONS, key
    assert got & set(WE013_EXCEPTIONS) == set(WE013_EXCEPTIONS)  # an exception that no longer occurs is removed
    # the pieces of the table the rules in scope (TX-1, TX-2, TX-7, TX-8, RS-14 and spillovers.lp) cover
    for key in [("steelmakers.domestic", "net_price_received", "increase"), ("steel_users", "price_paid", "increase"),
                ("importers", "quantity_traded", "decrease"), ("officials.enforcement", "tax_revenue", "increase"),
                ("export_industries", "quantity_supplied", "decrease"), ("buyers.construction", "price_paid", "increase"),
                ("steel_users", "quantity_supplied", "decrease"),
                ("officials.enforcement", "enforcement_cost", "increase"), ("taxpayers", "resources_available_other_uses", "decrease"),
                ("steel_users", "quantity_traded", "decrease"), ("sellers.foreign", "quantity_traded", "decrease"),
                ("officials.enforcement", "tax_revenue_vs_static_projection", "decrease"),
                ("importers", "reclassification", "increase"), ("steel_users", "reclassification", "increase"),
                ("steel_users", "compliance_cost", "increase"), ("steel_users", "allocation_by_non_price_criteria", "increase"),
                ("steelmakers.domestic", "lobbying_effort", "increase"), ("steel_users", "lobbying_effort", "increase"),
                ("steelmakers.domestic", "investment_target", "increase"), ("input_suppliers", "quantity_demanded", "increase"),
                ("steelmakers.owners", "asset_value", "increase"), ("buyers.steel_goods", "quantity_substitute", "increase"),
                ("steel_users.exporters", "quantity_supplied", "decrease"), ("steel_users", "capital_stock_target", "decrease"),
                ("buyers.construction", "quantity_demanded", "decrease")]:
        assert key in got, key
    # every table row is either produced or listed with a reason
    section = (ROOT / "handbook" / "05_examples" / "WE-013_steel_tariff.md").read_text().split(
        "## Consequence list (normal form)")[1].split("## Gaps found")[0]
    table_ids = set(re.findall(r"^\| (C-\d+) \|", section, re.M))
    assert len(table_ids) == 32 and set(WE013_NOT_PRODUCED) <= table_ids
    assert len(got - set(WE013_EXCEPTIONS)) >= 25


def test_unscored_run_without_outcome_card(tmp_path):
    record = parser.parse_fixture(WE13 / "record.json")
    assert not (WE13 / "outcome_card.json").exists()
    result = run_case(WE13, record, FixtureDecider(WE13 / "answers.json"), tmp_path)
    assert result["score"] is None and not (tmp_path / "score.json").exists()
    assert "not scored" in (tmp_path / "report.md").read_text()


def _tariff_assumptions(p=0.9, extra=(), **over):
    atoms = ("binding", "domestic_substitutes", "no_offset", "input_not_replaceable", "competitors_exempt") + tuple(extra)
    return {f"{a}(k1)": Assumption(id=f"{a}(k1)", text=a, assumption_class="other", p=over.get(a, p)) for a in atoms}


def test_tariff_exception_and_cutoff():
    rec = parser.parse_fixture(WE13 / "record.json")
    cons = _by_var(engine.run(rec, _tariff_assumptions(no_offset=0.4))[0])
    assert not cons[("export_industries", "quantity_supplied")].reported  # TX-8 needs A-8 above the cut-off
    assert cons[("steelmakers.domestic", "quantity_supplied")].reported
    # TX-7 "Unless": domestic output pays the same tax, so there are no protected sellers and no pattern
    cons = _by_var(engine.run(rec, _tariff_assumptions(), extra="exception(tx_7, k1).\n")[0])
    assert ("steelmakers.domestic", "quantity_supplied") not in cons and ("steel_users", "price_paid") not in cons
    assert ("officials.enforcement", "tax_revenue") in cons  # TX-1 is unaffected


def test_per_unit_tax_wedge():
    rec = parser.parse_fixture(SF / "record.json")
    comp = rec.components[0]
    comp.instrument, comp.bound_actor, comp.buyer_actor, comp.seller_actor = "per_unit_tax", "sellers.current", "buyers.current", "sellers.current"
    a = {f"{x}(c1)": Assumption(id=f"{x}(c1)", text=x, assumption_class="other", p=0.8)
         for x in ("quantity_responds", "buyers_bear", "sellers_bear")}
    cons = engine.run(rec, a)[0]
    got = {(c.actor_class, c.variable, c.sign) for c in cons}
    assert {("buyers.current", "price_paid", "increase"), ("sellers.current", "net_price_received", "decrease"),
            ("sellers.current", "quantity_traded", "decrease"), ("officials.enforcement", "tax_revenue", "increase")} <= got
    assert verify(cons, a, rec) == []
    a["sellers_bear(c1)"] = a["sellers_bear(c1)"].model_copy(update={"p": 0.3})
    cons = _by_var(engine.run(rec, a)[0])
    assert not cons[("sellers.current", "net_price_received")].reported and cons[("buyers.current", "price_paid")].reported


@pytest.mark.skipif(not os.environ.get("ANTHROPIC_API_KEY"), reason="needs ANTHROPIC_API_KEY")
def test_llm_parser_live():
    text = (SF / "policy.txt").read_text()
    rec = parser.parse_llm(text)
    assert isinstance(rec, PolicyRecord)
    assert any(c.instrument == "price_ceiling" for c in rec.components)


def test_prose_reading_facts_are_ignored_and_reported():
    """A parser may write text where engine facts belong; the engine must not crash on it."""
    rec = _record()
    rec.unclear.append(Unclear(id="U8", text="t", readings=["U8-a: x", "U8-b: y"],
                               reading_facts={"U8-a": "no rent reset after involuntary departure"}))
    a = _assumptions()
    cons, _ = engine.run(rec, a)
    assert cons and all(c.sign_by_reading == {} for c in cons)
    assert any("U8" in p and "not valid clingo" in p for p in verify(cons, a, rec))


def test_card_matches_by_role_not_label():
    """A parser that calls the bound landlords `landlords.covered` is scored as the card's `landlords.controlled`."""
    card = OutcomeCard.model_validate_json((SF / "outcome_card.json").read_text())
    rec = _record()
    a = _assumptions()
    base = score(engine.run(rec, a)[0], a, card, rec)["headline"]
    renamed = rec.model_copy(deep=True)
    renamed.components[0].bound_actor = "landlords.covered"
    cons = engine.run(renamed, a)[0]
    assert any(c.actor_class == "landlords.covered" for c in cons)
    assert score(cons, a, card, renamed)["headline"]["matched"] == base["matched"]
    assert score(cons, a, card)["headline"]["recall"] < base["recall"]  # without the record, labels must match


# --- spillovers.lp: one test per pattern (fires; blocked by its exception or a low assumption) ---

def _wk(extra, p=0.9, exception="", **over):
    """Run WE-013's record with the base tariff assumptions plus `extra`; returns {(actor, variable): Consequence}."""
    rec = parser.parse_fixture(WE13 / "record.json")
    a = _tariff_assumptions(p, extra=extra, **over)
    cons = engine.run(rec, a, extra=exception)[0]
    assert verify(cons, a, rec) == []
    return {(c.actor_class, c.variable): c for c in cons}


def _fires(cons, key, sign=None):
    c = cons.get(key)
    return c is not None and c.reported and (sign is None or c.sign == sign)


def test_oc3_enforcement_cost_and_funding():
    cons = _wk(("enforcement_budget_raised",))
    assert _fires(cons, ("officials.enforcement", "enforcement_cost"), "increase")
    assert cons[("officials.enforcement", "enforcement_cost")].assumptions == []  # Tier A, no assumption
    assert _fires(cons, ("taxpayers", "resources_available_other_uses"), "decrease")
    low = _wk(("enforcement_budget_raised",), enforcement_budget_raised=0.4)
    assert not _fires(low, ("taxpayers", "resources_available_other_uses")) and _fires(low, ("officials.enforcement", "enforcement_cost"))
    off = _wk(("enforcement_budget_raised",), exception="exception(oc_3, k1).\n")
    assert ("officials.enforcement", "enforcement_cost") not in off and ("taxpayers", "resources_available_other_uses") not in off


def test_oc4_prevented_exchanges_name_both_sides():
    cons = _wk(())
    assert _fires(cons, ("steel_users", "quantity_traded"), "decrease") and _fires(cons, ("sellers.foreign", "quantity_traded"), "decrease")
    assert not _fires(_wk((), binding=0.4), ("sellers.foreign", "quantity_traded"))
    off = _wk((), exception="exception(oc_4, k1).\n")
    assert ("sellers.foreign", "quantity_traded") not in off and ("importers", "quantity_traded") in off  # TX-2 is separate


def test_tx9_revenue_short_of_static_projection():
    cons = _wk(())
    assert _fires(cons, ("officials.enforcement", "tax_revenue_vs_static_projection"), "decrease")
    assert not _fires(_wk((), binding=0.4), ("officials.enforcement", "tax_revenue_vs_static_projection"))
    assert ("officials.enforcement", "tax_revenue_vs_static_projection") not in _wk((), exception="exception(tx_9, k1).\n")
    assert _fires(cons, ("officials.enforcement", "tax_revenue"), "increase")  # TX-1 is not affected


def test_tx9_oc4_for_a_per_unit_tax():
    rec = parser.parse_fixture(SF / "record.json")
    comp = rec.components[0]
    comp.instrument, comp.bound_actor, comp.buyer_actor, comp.seller_actor = "per_unit_tax", "sellers.current", "buyers.current", "landlords.current"
    a = {f"{x}(c1)": Assumption(id=f"{x}(c1)", text=x, assumption_class="other", p=0.8) for x in ("quantity_responds", "buyers_bear", "sellers_bear")}
    got = {(c.actor_class, c.variable, c.sign) for c in engine.run(rec, a)[0] if c.reported}
    assert ("officials.enforcement", "tax_revenue_vs_static_projection", "decrease") in got
    assert {("buyers.current", "quantity_traded", "decrease"), ("landlords.current", "quantity_traded", "decrease")} <= got


def test_rs5_tx4_reclassification():
    cons = _wk(("reshaping_pays",))
    assert _fires(cons, ("importers", "reclassification"), "increase") and _fires(cons, ("steel_users", "reclassification"), "increase")
    assert not _fires(_wk(("reshaping_pays",), reshaping_pays=0.4), ("importers", "reclassification"))
    assert ("importers", "reclassification") not in _wk(("reshaping_pays",), exception="exception(rs_5, k1).\n")
    rec = parser.parse_fixture(WE13 / "record.json")
    rec.components[0].definition_line = False  # no line between covered and uncovered goods, no pattern
    assert ("importers", "reclassification") not in _by_var(engine.run(rec, _tariff_assumptions(extra=("reshaping_pays",)))[0])


def test_rs15_discretionary_relief_is_rationed():
    atoms = ("relief_discretionary", "relief_valuable")
    cons = _wk(atoms)
    for var in ("allocation_by_non_price_criteria", "compliance_cost", "lobbying_effort"):
        assert _fires(cons, ("steel_users", var), "increase"), var
    assert _fires(cons, ("steelmakers.domestic", "lobbying_effort"), "increase")  # those who gain when relief is denied
    for low in atoms:
        got = _wk(atoms, **{low: 0.4})
        assert not _fires(got, ("steel_users", "compliance_cost")) and not _fires(got, ("steel_users", "allocation_by_non_price_criteria"))
    assert ("steel_users", "compliance_cost") not in _wk(atoms, exception="exception(rs_15, k1).\n")


def test_rs7_lobbying_needs_renewal_and_organization():
    atoms = ("beneficiaries_organize", "harmed_organize")
    cons = _wk(atoms)
    assert _fires(cons, ("steelmakers.domestic", "lobbying_effort"), "increase") and _fires(cons, ("steel_users", "lobbying_effort"), "increase")
    low = _wk(atoms, beneficiaries_organize=0.4, harmed_organize=0.4)
    assert not _fires(low, ("steelmakers.domestic", "lobbying_effort")) and not _fires(low, ("steel_users", "lobbying_effort"))
    off = _wk(atoms, exception="exception(rs_7, k1).\n")
    assert ("steelmakers.domestic", "lobbying_effort") not in off
    rec = parser.parse_fixture(WE13 / "record.json")
    rec.components[0].renewable = False  # the gain does not depend on a later decision
    assert ("steelmakers.domestic", "lobbying_effort") not in _by_var(engine.run(rec, _tariff_assumptions(extra=atoms))[0])
    # builders pass the cost on, so their harm is diffuse and they are not named
    assert ("builders", "lobbying_effort") not in cons


def test_ts2_investment_follows_expected_extension():
    cons = _wk(("expects_extension",))
    assert _fires(cons, ("steelmakers.domestic", "investment_target"), "increase")
    assert not _fires(_wk(("expects_extension",), expects_extension=0.45), ("steelmakers.domestic", "investment_target"))
    assert ("steelmakers.domestic", "investment_target") not in _wk(("expects_extension",), exception="exception(ts_2, k1).\n")
    assert ("steelmakers.domestic", "investment_target") not in _wk(("expects_extension",), exception="exception(tx_7, k1).\n")


def test_cr9_derived_demand_for_inputs():
    assert _fires(_wk(()), ("input_suppliers", "quantity_demanded"), "increase")
    assert not _fires(_wk((), domestic_substitutes=0.4), ("input_suppliers", "quantity_demanded"))
    assert ("input_suppliers", "quantity_demanded") not in _wk((), exception="exception(cr_9, k1).\n")


def test_sb4_asset_values_capitalize_lasting_changes():
    atoms = ("asset_supply_slow", "expected_to_last")
    cons = _wk(atoms)
    assert _fires(cons, ("steelmakers.owners", "asset_value"), "increase") and _fires(cons, ("owners.steel_users", "asset_value"), "decrease")
    for low in atoms:
        got = _wk(atoms, **{low: 0.4})
        assert not _fires(got, ("steelmakers.owners", "asset_value")) and not _fires(got, ("owners.steel_users", "asset_value"))
    assert ("steelmakers.owners", "asset_value") not in _wk(atoms, exception="exception(sb_4, k1).\n")
    # owners of users that can pass the cost on do not lose (no squeeze): competitors not exempt
    assert not _fires(_wk(atoms, competitors_exempt=0.4), ("owners.steel_users", "asset_value"))


def test_rs1_buyers_turn_to_uncovered_substitutes():
    cons = _wk(("substitute_supply_expands",))
    assert _fires(cons, ("buyers.steel_goods", "quantity_substitute"), "increase")
    assert not _fires(_wk(("substitute_supply_expands",), substitute_supply_expands=0.4), ("buyers.steel_goods", "quantity_substitute"))
    assert not _fires(_wk(("substitute_supply_expands",), competitors_exempt=0.4), ("buyers.steel_goods", "quantity_substitute"))
    assert ("buyers.steel_goods", "quantity_substitute") not in _wk(("substitute_supply_expands",), exception="exception(rs_1, k1).\n")


def test_rs6_exporting_users_who_take_world_prices_supply_less():
    cons = _wk(("exporters_price_takers",))
    assert _fires(cons, ("steel_users.exporters", "quantity_supplied"), "decrease")
    assert not _fires(_wk(("exporters_price_takers",), exporters_price_takers=0.4), ("steel_users.exporters", "quantity_supplied"))
    assert not _fires(_wk(("exporters_price_takers",), input_not_replaceable=0.4), ("steel_users.exporters", "quantity_supplied"))
    assert ("steel_users.exporters", "quantity_supplied") not in _wk(("exporters_price_takers",), exception="exception(rs_6, k1).\n")


def test_rs4_ts1_capital_moves_out_late():
    cons = _wk(("can_relocate_capital",))
    c = cons[("steel_users", "capital_stock_target")]
    assert c.reported and c.sign == "decrease" and c.horizon == ["long"]  # TS-1: the stock falls late
    assert {s.rule for s in c.derivation} >= {"RS-4", "RS-6", "TS-1"}
    assert not _fires(_wk(("can_relocate_capital",), can_relocate_capital=0.4), ("steel_users", "capital_stock_target"))
    assert not _fires(_wk(("can_relocate_capital",), competitors_exempt=0.4), ("steel_users", "capital_stock_target"))
    assert ("steel_users", "capital_stock_target") not in _wk(("can_relocate_capital",), exception="exception(rs_4, k1).\n")


def test_cr4c_buyers_cut_back_when_price_rises():
    assert _fires(_wk(()), ("buyers.construction", "quantity_demanded"), "decrease")
    assert not _fires(_wk((), input_not_replaceable=0.4), ("buyers.construction", "quantity_demanded"))
    assert ("buyers.construction", "quantity_demanded") not in _wk((), exception="exception(cr_4, k1).\n")


def test_questions_follow_the_record():
    from praxeo.questions import questions_for
    rec = parser.parse_fixture(WE13 / "record.json")
    atoms = [q.assumption for q, _ in questions_for(rec.components[0])]
    assert len(atoms) == len(set(atoms)) and {"enforcement_budget_raised", "reshaping_pays", "relief_discretionary", "relief_valuable",
        "beneficiaries_organize", "harmed_organize", "expects_extension", "expected_to_last", "asset_supply_slow",
        "can_relocate_capital", "substitute_supply_expands", "exporters_price_takers"} <= set(atoms)
    for q, _ in questions_for(rec.components[0]):
        if q.assumption not in {"binding", "domestic_substitutes", "no_offset", "input_not_replaceable", "competitors_exempt"}:
            assert " and " not in q.text.lower(), q.id  # one concept per question (the new ones)
    plain = rec.components[0].model_copy(update=dict(renewable=False, definition_line=False, relief_applicant_actor=None,
                                                    domestic_seller_owner_actor=None, input_supplier_actor=None, downstream=[]))
    assert {q.assumption for q, _ in questions_for(plain)} == {"binding", "domestic_substitutes", "no_offset", "enforcement_budget_raised"}


def test_minimal_sets_match_brute_force_enumeration():
    """The engine finds each conclusion's minimal assumption sets with clingo's subset-minimal enumeration.
    Check it against brute force (every answer set over every choice of assumptions, then minimal sets),
    on programs small enough to enumerate: the ceiling case with nine assumptions and a tariff with five."""
    import clingo
    from praxeo.engine import RULES

    def brute(program):
        ctl = clingo.Control(["0", "--warn=none"])
        for r in RULES:
            ctl.load(str(r))
        ctl.add("base", [], program)
        ctl.ground([("base", [])], context=engine._Context())
        sets = {}
        def on_model(m):
            syms = m.symbols(shown=True)
            held = frozenset(str(x.arguments[0]) for x in syms if x.name == "holds")
            for x in syms:
                if x.name == "effect":
                    sets.setdefault(str(x.arguments[0]), set()).add(held)
        ctl.solve(on_model=on_model)
        return {c: sorted({s for s in ss if not any(o < s for o in ss)}, key=lambda s: (len(s), sorted(s)))
                for c, ss in sets.items()}

    nine = ("binding", "enforced", "alternative_uses", "nontransferable", "buyouts_limited", "would_leave",
            "lockin_dominates", "keepers_dominate", "substitutes")
    ceiling = {f"{x}(c1)": Assumption(id=f"{x}(c1)", text=x, assumption_class="other", p=0.9) for x in nine}
    for rec, a in ((_record(), ceiling), (parser.parse_fixture(WE13 / "record.json"), _tariff_assumptions())):
        program = engine.facts(rec, a)
        expected = brute(program)
        derived = engine._derive(program, a)
        assert {d["concl"] for d in derived.values()} == set(expected)
        for d in derived.values():
            assert d["sets"] == expected[d["concl"]], d["concl"]
