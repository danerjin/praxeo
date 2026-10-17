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


def test_consistent_with_worked_example_we001():
    """Every engine consequence for WE-001's record should appear in WE-001's consequence list,
    except PC-21's consequences, which were added to the catalog after WE-001 was written."""
    text = (WE1 / "policy.txt").read_text()
    record = parser.parse_fixture(WE1 / "record.json")
    pred = predict(text, record, FixtureDecider(WE1 / "answers.json"))
    assert pred["citation_problems"] == []
    md = (ROOT / "handbook" / "05_examples" / "WE-001_rent_freeze.md").read_text()
    table = md.split("## Consequence list (normal form)")[1].split("## Gaps found")[0]
    rows = set()
    for line in table.splitlines():
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) > 4 and re.match(r"C-\d+", cells[0]):
            rows.add((cells[1].split(" ")[0], cells[2].split(" ")[0], cells[3]))
    known = {("tenants.controlled.keepers", "relocation_out_of_area", "decrease"),  # PC-21 is newer than WE-001
             ("tenants.controlled.displaced", "relocation_out_of_area", "increase"),
             ("tenants.controlled", "relocation_out_of_area", "decrease")}
    for c in pred["consequences"]:
        key = (c["actor_class"], c["variable"], c["sign"])
        assert key in rows or key in known, key


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
    # the pieces of the table the rules in scope (TX-1, TX-2, TX-7, TX-8, RS-14) cover
    for key in [("steelmakers.domestic", "net_price_received", "increase"), ("steel_users", "price_paid", "increase"),
                ("importers", "quantity_traded", "decrease"), ("officials.enforcement", "tax_revenue", "increase"),
                ("export_industries", "quantity_supplied", "decrease"), ("buyers.construction", "price_paid", "increase"),
                ("steel_users", "quantity_supplied", "decrease")]:
        assert key in got, key


def test_unscored_run_without_outcome_card(tmp_path):
    record = parser.parse_fixture(WE13 / "record.json")
    assert not (WE13 / "outcome_card.json").exists()
    result = run_case(WE13, record, FixtureDecider(WE13 / "answers.json"), tmp_path)
    assert result["score"] is None and not (tmp_path / "score.json").exists()
    assert "not scored" in (tmp_path / "report.md").read_text()


def _tariff_assumptions(p=0.9, **over):
    atoms = ("binding", "domestic_substitutes", "no_offset", "input_not_replaceable", "competitors_exempt")
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
