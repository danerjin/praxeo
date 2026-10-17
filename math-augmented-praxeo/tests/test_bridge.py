"""The annex pass and its guards: sizes are attached, nothing praxeological is changed."""
import copy
import json
import sys
from pathlib import Path

import pytest

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))  # praxeo

from mathpraxeo.bridge import (AnnexInputs, GuardError, annex_pass, premise_evidence,  # noqa: E402
                               settle_by_arithmetic)
from mathpraxeo.interval import Interval  # noqa: E402
from mathpraxeo.result import Result  # noqa: E402

PRED = HERE.parent / "cases" / "sf_1994" / "sample_run" / "prediction.json"
INPUTS = HERE / "examples" / "sf_1994" / "annex_inputs.json"


def test_pass_attaches_and_changes_nothing():
    pred = json.loads(PRED.read_text())
    before = copy.deepcopy(pred)
    atts = annex_pass(pred, AnnexInputs.load(INPUTS))
    assert pred == before
    by_var = {a.variable: a for a in atts}
    assert by_var["quantity_supplied"].sign_check == "agrees"
    assert by_var["price_paid"].actor_class == "tenants.controlled" and by_var["price_paid"].sign_check == "agrees"
    assert all(a.sources for a in atts)


def test_pass_skips_unreported_and_unmapped():
    pred = json.loads(PRED.read_text())
    for c in pred["consequences"]:
        c["reported"] = False
    assert annex_pass(pred, AnnexInputs.load(INPUTS)) == []


def _r(lo, hi, rung):
    return Result("x", Interval(lo, hi), rung)


def test_premise_evidence_proposes_but_never_applies():
    ev = premise_evidence("keepers_dominate(c1)", 0.6, _r(-0.3, -0.2, "M1"), _r(0.01, 0.05, "M1"))
    assert ev.proposed_p == 0.9 and ev.current_p == 0.6 and not ev.accepted and ev.rung == "M1"
    ev = premise_evidence("keepers_dominate(c1)", 0.6, _r(-0.1, -0.02, "M1"), _r(0.01, 0.05, "M1"))
    assert ev.proposed_p == 0.6  # ranges overlap: no change proposed


def test_m1_cannot_settle_cr12():
    inp = AnnexInputs({"a": Interval(1, 1)}, {"a": "case"}, {"a": True})
    with pytest.raises(GuardError):
        settle_by_arithmetic({"favoured_sign": "decrease"}, _r(-0.3, -0.2, "M1"), _r(0.01, 0.05, "M0"), inp, ["a"])


def test_m0_settles_only_on_case_figures():
    total = {"favoured_sign": "decrease"}
    case = AnnexInputs({"a": Interval(1, 1)}, {"a": "case record"}, {"a": True})
    outside = AnnexInputs({"a": Interval(1, 1)}, {"a": "illustrative"}, {"a": False})
    assert settle_by_arithmetic(total, _r(-300, -200, "M0"), _r(10, 50, "M0"), case, ["a"]) == "decrease"
    assert settle_by_arithmetic(total, _r(-30, -2, "M0"), _r(10, 50, "M0"), case, ["a"]) == "ambiguous"
    with pytest.raises(GuardError):
        settle_by_arithmetic(total, _r(-300, -200, "M0"), _r(10, 50, "M0"), outside, ["a"])


def _pred(instrument, conss, **actors):
    comp = {"id": "k1", "instrument": instrument, "bound_actor": actors.get("bound", "sellers.current"),
            "protected_actor": actors.get("protected"), "excluded_actor": actors.get("excluded")}
    return {"record": {"name": "t", "components": [comp]},
            "consequences": [{"id": f"C-{n}", "actor_class": a, "variable": v, "sign": s, "reported": True}
                             for n, (a, v, s) in enumerate(conss, 1)]}


def _inputs(actors=None, **vals):
    return AnnexInputs({k: Interval.of(v) for k, v in vals.items()}, {k: "test" for k in vals},
                       {k: False for k in vals}, actors or {})


def test_tariff_handlers():
    pred = _pred("tariff", [("steel_users", "price_paid", "increase"),
                            ("steelmakers.domestic", "quantity_supplied", "increase"),
                            ("importers", "quantity_traded", "decrease"),
                            ("steel_users", "quantity_traded", "decrease"),
                            ("officials.enforcement", "tax_revenue_vs_static_projection", "decrease"),
                            ("buyers.construction", "price_paid", "increase")])
    inp = _inputs({"buyers": "steel_users", "domestic_sellers": "steelmakers.domestic", "importers": "importers",
                   "downstream": "buyers.construction"},
                  tax_rate=0.25, import_share=(0.38, 0.42), demand_elasticity=(-0.6, -0.2),
                  supply_elasticity=(0.2, 1.0), pass_through=(0.6, 1.0), input_price_change=(0.15, 0.25),
                  cost_share=(0.03, 0.1))
    atts = {a.consequence_id: a for a in annex_pass(pred, inp)}
    assert [atts[f"C-{i}"].handler for i in range(1, 7)] == [
        "tariff_domestic_price", "tariff_domestic_output", "tariff_imports", "tariff_use",
        "tariff_revenue_shortfall", "cost_pass_through"]
    assert all(atts[f"C-{i}"].sign_check == "agrees" for i in range(1, 6))
    assert atts["C-6"].sign_check == "indeterminate"  # a bound that includes zero


def test_tax_subsidy_floor_quota_handlers():
    tax = annex_pass(_pred("per_unit_tax", [("buyers.current", "price_paid", "increase"),
                                            ("sellers.current", "net_price_received", "decrease"),
                                            ("buyers.current", "quantity_traded", "decrease")]),
                     _inputs({"buyers": "buyers.current", "sellers": "sellers.current"},
                             tax_rate=0.1, demand_elasticity=-0.5, supply_elasticity=0.5))
    assert [a.sign_check for a in tax] == ["agrees"] * 3
    sub = annex_pass(_pred("per_unit_subsidy", [("buyers.current", "price_paid", "decrease")]),
                     _inputs({"buyers": "buyers.current"}, subsidy_rate=0.1, demand_elasticity=-0.5, supply_elasticity=0.5))
    assert sub[0].sign_check == "agrees"
    floor = annex_pass(_pred("price_floor", [("workers", "excess_supply", "increase"), ("workers", "employment", "decrease")]),
                       _inputs(floor_gap=0.1, demand_elasticity=(-0.5, -0.1), supply_elasticity=(0.0, 0.3)))
    assert [a.sign_check for a in floor] == ["agrees", "agrees"]
    quota = annex_pass(_pred("quota", [("license_holders", "asset_value", "increase")]),
                       _inputs({"holders": "license_holders"}, price_gap=(5, 10), units_per_right=1000,
                               discount_rate=(0.05, 0.08), expected_duration=10))
    assert quota[0].handler == "right_value" and quota[0].sign_check == "agrees"


def test_capitalized_value_handler():
    pred = _pred("price_ceiling", [("landlords.controlled", "asset_value", "decrease")], bound="landlords.controlled")
    atts = annex_pass(pred, _inputs(market_growth=(0.03, 0.07), cap_growth=0.02, gap_year=5,
                                    discount_rate=(0.04, 0.08), expected_duration=(5, 15)))
    assert atts[0].handler == "capitalized_value" and atts[0].sign_check == "agrees"


def test_wrong_actor_or_missing_inputs_gives_no_attachment():
    pred = _pred("per_unit_tax", [("someone_else", "price_paid", "increase")])
    assert annex_pass(pred, _inputs({"buyers": "buyers.current"}, tax_rate=0.1, demand_elasticity=-0.5, supply_elasticity=0.5)) == []
    pred = _pred("per_unit_tax", [("buyers.current", "price_paid", "increase")])
    assert annex_pass(pred, _inputs({"buyers": "buyers.current"}, tax_rate=0.1)) == []


# ---------------------------------------------------------------- premise step

def _sf_prediction(tmp_path, keepers_p):
    from praxeo import parser
    from praxeo.decider import FixtureDecider
    from praxeo.pipeline import predict
    case = HERE.parent / "cases" / "sf_1994"
    answers = json.loads((case / "answers.json").read_text())
    for a in answers:
        if a["question_id"] == "c1.keepers_dominate":
            a["probability"] = keepers_p
    f = tmp_path / "answers.json"
    f.write_text(json.dumps(answers))
    return predict((case / "policy.txt").read_text(), parser.parse_fixture(case / "record.json"), FixtureDecider(f))


class _Stub:
    name = "stub"

    def __init__(self, p):
        self.p = p
        self.asked = []

    def answer(self, q, record):
        from praxeo.schema import Answer
        self.asked.append(q.id)
        return Answer(question_id=q.id, value="yes", probability=self.p, rationale="stub", decider=self.name)


def _total(pred):
    return next(c for c in pred["consequences"]
                if c["actor_class"] == "tenants.controlled" and c["variable"] == "relocation_out_of_area")


def test_premise_step_accepted_changes_total_and_is_labelled(tmp_path):
    from mathpraxeo import premise_step
    pred = _sf_prediction(tmp_path, 0.4)
    before = copy.deepcopy(pred)
    assert _total(pred)["sign"] == "ambiguous"
    stub = _Stub(0.8)
    log, informed = premise_step.run(pred, AnnexInputs.load(INPUTS), stub)
    assert pred == before                                   # original untouched
    assert stub.asked == ["annex_premise.keepers_dominate(c1)"]  # lockin ranges overlap: not asked
    assert _total(informed)["sign"] == "decrease"
    diffs = informed["annex_informed"]["differences"]
    assert any(d["variable"] == "relocation_out_of_area" and "annex-informed" in d["label"] for d in diffs)
    assert informed["verifier_problems"] == []


def test_premise_step_decider_can_decline(tmp_path):
    from mathpraxeo import premise_step
    pred = _sf_prediction(tmp_path, 0.4)
    log, informed = premise_step.run(pred, AnnexInputs.load(INPUTS), _Stub(0.4))
    assert not any(r.evidence.accepted for r in log)
    assert _total(informed)["sign"] == "ambiguous" and informed["annex_informed"]["differences"] == []
