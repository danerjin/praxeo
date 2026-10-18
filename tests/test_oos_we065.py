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

SHORT = {}  # the table's actor names are the record's role names (the payments office's parenthesis is dropped)
# the qualifiers in the table's cells are states of the world (years below or at Th 220) or scopes, not timing windows
WINDOWS = {}

EXCEPTIONS = {
    ("taxpayers", "resources_available_other_uses", "decrease", None):
        "SB-1 with OC-1 (C-7, C-8, C-32, C-34): the table signs the group of three classes at_least_one_decrease, per state of the world; "
        "the record names one taxpayer class and SB-1 gives it a plain decrease, in no state qualifier",
    ("wheat_growers", "price_paid", "decrease", None):
        "KNOWN WRONG: SB-2's price_paid decrease is for recipients who BUY the subsidized good. These recipients are the sellers; "
        "the example signs net_price_received increase (C-4, C-6), and price_paid for growers is not a row",
    ("wheat_growers", "quantity_traded", "increase", None):
        "SB-2: the growers sell more wheat; the table signs the same fact as quantity_supplied (C-9, U1-a) and as grain_exporters' "
        "quantity_traded (C-21)",
}

NOT_PRODUCED = {
    "C-1": "missing rule: SB-1 signs the payers' resources, not a subsidy_outlay variable for the treasury (CR-8b); the record has no treasury role",
    "C-2": "missing rule: CR-8's contingent payer (no payment in years at or above the line); the engine derives no no_change and has no state-of-the-world qualifier",
    "C-3": "missing rule: CR-8b mirror, the recipients' resources rise; SB-1 signs the funders only",
    "C-4": "missing rule: SB-2 for a payment to sellers (net_price_received increase); the engine gives price_paid decrease instead (the WRONG row)",
    "C-5": "missing rule and record fact: CR-6 and CR-9 small world-price effect; no foreign-sellers role and no rule for subsidies",
    "C-6": "missing rule: SB-2 for sellers, the expected price at sowing (CR-10a, CR-12e); as C-4",
    "C-7": "combiner: a group over three classes (OC-1); the record has the one role taxpayers, signed decrease (EXCEPTIONS)",
    "C-8": "combiner: as C-7, over the whole period (CR-12 total across states of the world not declared)",
    "C-9": "missing rule: SB-2's quantity rule signs quantity_traded; for a payment to producers the variable is quantity_supplied",
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
    "C-32": "combiner: as C-7 (OC-1, CR-8a)",
    "C-34": "combiner and missing rule: the group of three classes (as C-7); OC-3 funding of the administration is encoded only as the agency's cost",
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
PRODUCED = {"C-16", "C-25", "C-33"}


def test_consistent_with_worked_example_we065():
    pred, keys = _engine(WE65)
    rows = _rows("WE-065_crop_deficiency_payments.md", SHORT, WINDOWS, {})
    # the sign cell "U1-a: x; U1-b: y" becomes its U1-a sign, the mechanism the record's rules run (see the module docstring)
    rows = {rid: {(a, v, (re.match(r"U1-a:\s*(\w+)", s) or [None, s])[1], w) for a, v, s, w in ks} for rid, ks in rows.items()}
    assert len(rows) == 43
    _check(rows, keys, EXCEPTIONS, NOT_PRODUCED, PRODUCED)
    by = {(c["actor_class"], c["variable"], c["window"]): c for c in pred["consequences"]}
    # the announcement-window delay (RS-8) is built for buyers; for these growers it has no meaning and is below the cut-off
    assert not by[("wheat_growers", "quantity_traded", "announcement")]["reported"]
    # no lobbying row: SB-5 with RS-7 needs a seller class apart from the recipients
    assert not any(k[1] == "lobbying_effort" for k in by)
