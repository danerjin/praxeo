"""Out-of-sample run of the subsidy rules (praxeo/rules/subsidies.lp) on WE-065, a deficiency payment to producers.

The subsidy rules were written from WE-019 only. Same shape as test_subsidies.py::test_consistent_with_worked_example_we019:
every reported engine consequence is a row of the example's consequence list or sits in EXCEPTIONS with its reason (a
reason that starts with KNOWN WRONG: marks a row that contradicts the example); every table row the engine does not produce
sits in NOT_PRODUCED with its reason. The record and answers are in cases/we065_brisklund/, the write-up in
cases/we065_brisklund/out_of_sample.md. Nothing under praxeo/ was changed for this run.

The table gives many signs by reading of the unclear provision U1 ("U1-a: increase; U1-b: no_change"). The parser's
readings carry no engine facts, so the engine runs the subsidy rules once, with the mechanism of actual output (U1-a). The
table's key is therefore its U1-a sign; the U1-b no_change halves are not checked.
"""
import re
from pathlib import Path

from test_out_of_sample import _check, _engine, _rows

ROOT = Path(__file__).resolve().parents[1]
WE65 = ROOT / "cases" / "we065_brisklund"

# the OC-1 payer group's members are written in prose in the table's actor cell
SHORT = {"recipients of other spending": "recipients.other_spending", "future taxpayers": "taxpayers.future"}
# the qualifiers in the table's cells are states of the world (years below or at Th 220) or scopes, not timing windows
WINDOWS = {}

EXCEPTIONS = {
    # the first run's two rows (growers' price_paid decrease, which was WRONG, and quantity_traded increase) are gone: SB-2
    # now signs a payment to producers as net_price_received and quantity_supplied (C-4, C-6, C-9)
    ("wheat_growers", "lobbying_effort", "U1-a: increase; U1-b: no_change", None):
        "KNOWN WRONG: RS-7 with the growers as the gaining sellers (renewal at the 2032 review). C-36 signs the lobbying over the "
        "level and continuation of support `ambiguous` by RS-7's Unless clause. The clause is now encoded (rules/lobbying.lp, "
        "`field_contested`), but the 2025 to 2026 farm-support campaign is not in the example's section 1, only in its analysis "
        "and A-8's evidence, so a record written from the policy text cannot set the flag (test_subsidies checks the flagged case)",
}

NOT_PRODUCED = {
    "C-1": "missing rule: SB-1 signs the payers' resources, not a subsidy_outlay variable for the treasury (CR-8b); the record has no treasury role",
    "C-2": "missing rule: CR-8's contingent payer (no payment in years at or above the line); the engine derives no no_change and has no state-of-the-world qualifier",
    "C-3": "missing rule: CR-8b mirror, the recipients' resources rise; SB-1 signs the funders only",
    "C-5": "missing rule and record fact: CR-6 and CR-9 small world-price effect; no foreign-sellers role and no rule for subsidies",
    "C-10": "missing rule: RS-6 (entry of new sellers) is not encoded for subsidies",
    "C-11": "missing record fact: the growers' alternative output (barley) is not a role field; SB-3 needs substitute_seller_actor, a different party",
    "C-12": "unsupported form: RS-16 (a payment per unit of one grade moves output toward the high-yield variety)",
    "C-13": "missing rule: RS-3 and RS-5 for overstated declarations; the engine has the claims cost only, and the penalty is not a record field",
    "C-14": "case-specific provision: hedges (put options, forwards) are a substitute for price cover (RS-1); no record field",
    "C-15": "missing rule and record fact: SB-5 with RS-7 needs sb_seller, but the recipients here are the sellers (seller_actor null); also `lobbying groups` is no role",
    "C-17": "missing record fact and rule: foreign buyers (no role), CR-6 and CR-9 chain through the world price",
    "C-18": "missing record fact and rule: foreign sellers (no subsidy field), as C-17",
    "C-19": "missing record fact and rule: foreign sellers, as C-17",
    "C-20": "missing record fact and rule: domestic buyers' price under the world-linked price (buyer_actor is a tax field), CR-6, RS-16",
    "C-21": "missing record fact and rule: grain exporters (no role), CR-4, CR-7a",
    "C-22": "missing rule: RS-16 and CR-6 chain on the outlay against a static projection; no subsidy_outlay variable",
    "C-23": "unsupported form: feed barley price, RS-13 and CR-12b, ambiguous; no role for feed buyers",
    "C-24": "missing record fact: input suppliers (no input_supplier_actor for subsidies); CR-9 and LW-10",
    "C-26": "missing record fact: one asset_owner_actor per component; the owners of land without wheat history are a second class (CR-7a)",
    "C-27": "missing rule and record fact: CR-7b and DM-1 between landowners and tenant growers; no tenants role in a subsidy",
    "C-28": "missing rule and record fact: CR-7b rent at renewal; no tenants role",
    "C-29": "missing record fact and rule: lenders (CR-7a, CR-7c)",
    "C-30": "missing rule and record fact: TX-8's mirror case through the currency for a subsidy; no industry roles",
    "C-31": "missing rule and record fact: as C-30",
    "C-35": "missing record fact: as C-11 (other output given up for wheat)",
    "C-36": "missing rule: RS-7's Unless clause (the farm-support question is contested without the Act); the engine has no lobbying row for this component",
    "C-37": "unsupported form: CR-9, LW-10 and CR-12b, ambiguous, input suppliers across crops",
    "C-38": "unsupported form: CR-12b, milling wheat ambiguous",
    "C-39": "missing record fact and rule: repayments and fines (the penalty is not a field; CR-8b non_tax_receipts)",
    "C-40": "combiner: the outlay net of repayments and fines (CR-8, CR-12e), no outlay variable",
    "C-41": "missing record fact: livestock farmers (no role); CR-9, CR-7a, CR-6",
    "C-42": "missing record fact and rule: neighboring sellers (no role); CR-9, CR-5",
    "C-43": "missing rule and record fact: import prices through the currency (TX-8 chain), no role",
}
PRODUCED = {"C-4", "C-6", "C-7", "C-8", "C-9", "C-16", "C-25", "C-32", "C-33", "C-34"}


def test_consistent_with_worked_example_we065():
    pred, keys = _engine(WE65)
    rows = _rows("WE-065_crop_deficiency_payments.md", SHORT, WINDOWS, {})
    assert len(rows) == 43
    _check(rows, keys, EXCEPTIONS, NOT_PRODUCED, PRODUCED)
    by = {(c["actor_class"], c["variable"], c["window"]): c for c in pred["consequences"]}
    # a payment to producers: no purchase to delay before the start (RS-8) and no dip after expiry (SB-6)
    assert not any(c["window"] for c in pred["consequences"])
    # U1-b (a fixed historical base) makes the payment a lump sum: no price or supply response (C-4, C-6, C-9), while the
    # land with a wheat history gains under both readings (C-25)
    assert by[("wheat_growers", "net_price_received", None)]["sign_by_reading"] == {"U1-a": "increase", "U1-b": "none"}
    assert by[("owners.wheat_land", "asset_value", None)]["sign"] == "increase"
    assert by[("taxpayers", "resources_available_other_uses", None)]["actor_group"] == [
        "taxpayers", "recipients.other_spending", "taxpayers.future"]                              # C-7 (OC-1)
