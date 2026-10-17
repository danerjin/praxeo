"""Tests for Configuration B (plan 5.2): the price-ceiling steps run as typed questions, without the engine."""
import json
import re
from pathlib import Path

from praxeo import parser
from praxeo.config_b import STEPS, assumptions_from_log, compare_a_b, run_config_b
from praxeo.combiner import combine
from praxeo.decider import FixtureDecider
from praxeo.questions import ASSUMPTION_TEXT
from praxeo.verifier import verify

ROOT = Path(__file__).resolve().parents[1]
SF = ROOT / "cases" / "sf_1994"
ANSWERS = SF / "answers.json"

# The nine questions in the order Configuration B asks them on sf_1994.
ASKED = ["c1.binding", "c1.enforced", "c1.substitutes", "c1.alternative_uses", "c1.nontransferable",
         "c1.buyouts_limited", "c1.would_leave", "c1.lockin_dominates", "c1.keepers_dominate"]


def _record():
    return parser.parse_fixture(SF / "record.json")


def test_b_matches_a_on_sf_1994():
    res = compare_a_b(_record(), FixtureDecider(ANSWERS))
    assert res["only_a"] == [] and res["only_b"] == []
    assert res["agree"] == sorted([
        ("landlords.controlled", "quantity_supplied", "decrease"),
        ("landlords.controlled", "reclassification", "increase"),
        ("tenants.controlled", "price_paid", "decrease"),
        ("tenants.controlled", "relocation_out_of_area", "decrease"),  # CR-12 total
        ("tenants.controlled", "turnover", "decrease"),
        ("tenants.controlled.displaced", "relocation_out_of_area", "increase"),
        ("tenants.controlled.keepers", "relocation_out_of_area", "decrease"),
        ("tenants.prospective", "price_paid", "increase"),
        ("tenants.prospective", "price_substitute", "increase"),
    ])
    assert res["a_unreported"] == []


def test_low_binding_stops_every_chain(tmp_path):
    answers = json.loads(ANSWERS.read_text())
    for a in answers:
        if a["question_id"] == "c1.binding":
            a["probability"] = 0.3
    path = tmp_path / "answers.json"
    path.write_text(json.dumps(answers))
    cons, log = run_config_b(_record(), FixtureDecider(path))
    assert cons == []
    assert [e["question"]["id"] for e in log] == ["c1.binding"]  # nothing downstream was asked
    res = compare_a_b(_record(), FixtureDecider(path))
    assert res["agree"] == [] and res["only_a"] == [] and res["only_b"] == []
    assert res["a_unreported"]  # A derives the same chains but cannot report them


def test_log_records_each_question_asked():
    cons, log = run_config_b(_record(), FixtureDecider(ANSWERS))
    fixture = {a["question_id"]: a for a in json.loads(ANSWERS.read_text())}
    assert [e["question"]["id"] for e in log] == ASKED
    for e in log:
        qid = e["question"]["id"]
        assert e["question"]["kind"] == "noul" and e["answer"]["question_id"] == qid
        assert e["answer"]["probability"] == fixture[qid]["probability"]
        assert e["held"] == (e["answer"]["probability"] >= 0.5)


def test_steps_are_well_formed():
    ids = [s.id for s in STEPS]
    assert len(set(ids)) == len(ids)
    for i, s in enumerate(STEPS):
        assert set(s.needs) <= set(ids[:i]), s.id
        assert s.assumption is None or s.assumption in ASSUMPTION_TEXT, s.id
    assert {s.assumption for s in STEPS if s.assumption} == set(ASSUMPTION_TEXT)


LP_EFFECT = re.compile(r'effect\(\w+\(C\), (@keepers\(P\)|@displaced\(P\)|P|X|B), "(\w+)", (\w+), (\w+), (\w+), "(\w)"\)')
LP_ROLE = {"@keepers(P)": "keepers", "@displaced(P)": "displaced", "P": "protected", "X": "excluded", "B": "bound"}


def test_steps_carry_the_effects_of_price_controls_lp():
    lp = (ROOT / "praxeo" / "rules" / "price_controls.lp").read_text()
    in_lp = {(LP_ROLE[m[0]], *m[1:]) for m in LP_EFFECT.findall(lp)}
    in_steps = {(e.role, e.variable, e.sign, e.horizon, e.visibility, e.tier) for s in STEPS for e in s.effects}
    assert len(in_lp) == 9
    assert in_steps == in_lp


def test_chain_derivation_and_assumptions_match_engine_labels():
    cons, _ = run_config_b(_record(), FixtureDecider(ANSWERS))
    supply = next(c for c in cons if c.variable == "quantity_supplied")
    assert [s.rule for s in supply.derivation] == ["PC-1", "PC-5"]
    assert supply.assumptions == ["alternative_uses(c1)", "binding(c1)", "enforced(c1)"]
    assert supply.assumption_sets == [supply.assumptions] and supply.reported


def test_b_output_passes_verifier():
    record = _record()
    cons, log = run_config_b(record, FixtureDecider(ANSWERS))
    assumptions = assumptions_from_log(log)
    assert verify(combine(cons, assumptions), assumptions, record) == []


def test_vacancy_decontrol_switch_agrees():
    record = _record()
    record.components[0].vacancy_decontrol = False
    res = compare_a_b(record, FixtureDecider(ANSWERS))
    assert res["only_a"] == [] and res["only_b"] == []
    assert ("tenants.prospective", "excess_demand", "increase") in res["agree"]
    assert ("tenants.prospective", "price_paid", "increase") not in res["agree"]
