"""The annex pass and its guards: sizes are attached, nothing praxeological is changed."""
import copy
import json
import sys
from pathlib import Path

import pytest

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))

from mathpraxeo.bridge import (AnnexInputs, GuardError, annex_pass, premise_evidence,  # noqa: E402
                               settle_by_arithmetic)
from mathpraxeo.interval import Interval  # noqa: E402
from mathpraxeo.result import Result  # noqa: E402

PRED = HERE.parent / "cases" / "sf_1994" / "sample_run" / "prediction.json"
INPUTS = HERE / "examples" / "sf_1994" / "annex_inputs.json"


def test_pass_attaches_and_changes_nothing():
    pred = json.loads(PRED.read_text())
    before = copy.deepcopy(pred)
    atts = annex_pass(pred, AnnexInputs.load(INPUTS), "tenants.controlled")
    assert pred == before
    by_var = {a.variable: a for a in atts}
    assert by_var["quantity_supplied"].sign_check == "agrees"
    assert by_var["price_paid"].actor_class == "tenants.controlled" and by_var["price_paid"].sign_check == "agrees"
    assert all(a.sources for a in atts)


def test_pass_skips_unreported_and_unmapped():
    pred = json.loads(PRED.read_text())
    for c in pred["consequences"]:
        c["reported"] = False
    assert annex_pass(pred, AnnexInputs.load(INPUTS), "tenants.controlled") == []


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
