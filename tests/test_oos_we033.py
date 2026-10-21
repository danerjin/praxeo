"""Out-of-sample run of the subsidy rules on WE-033 (Kestland Household Support Payment Act 2027).

The subsidy rules were written from WE-019 only. Same shape as
tests/test_subsidies.py::test_consistent_with_worked_example_we019: every reported engine consequence is a row of the
example's consequence list (key: actor class, variable, sign, window), or sits in a dict of exceptions with its reason
(prefixed "KNOWN WRONG:" when the row contradicts the example); every table row the engine does not produce sits in a
dict with the reason. The write-up is cases/we033_kestland/out_of_sample.md.
"""
from pathlib import Path

from test_out_of_sample import _check, _engine, _rows

ROOT = Path(__file__).resolve().parents[1]
WE33 = ROOT / "cases" / "we033_kestland"

# the record uses the table's own actor names for every role it fills
SHORT: dict = {}
# no table cell carries a timing qualifier in its actor or variable cell (the windows are in the horizon column)
WINDOWS: dict = {}
EXCEPTIONS = {
    ('households.recipients', 'legal_breach', 'increase', None):
        'RS-3 (false claims, A-14): the table names the false claimants as their own class (C-27, claimants.false), which the record has no role for',
}
NOT_PRODUCED = {
    "C-3": "unsupported form: the bond sale (K2, government_borrowing) has no rule; the lenders' side of CR-5 is not derived",
    "C-4": "missing rule and question: CR-4 'A change in means alone' and 'Saving is a use' (a lump sum has no questions)",
    "C-6": "missing question: SB-5/RS-5 reclassification is gated on takeup, and a lump sum has no takeup question (A-7)",
    "C-7": "missing rule and question: RS-8 for credit taken against the announced payment (A-5); RS-8 is encoded for purchases only",
    "C-8": "missing rule: CR-4 timing shift in credit after the payment (A-6)",
    "C-9": "unsupported form: OC-8 (crowding out by public borrowing) and the per-reading sign cell; the record's readings carry no engine facts",
    "C-10": "same as C-9",
    "C-11": "same as C-9 (OC-1 'naming the forgone uses' also needs a role for the crowded-out sellers)",
    "C-12": "same as C-9 (OC-5 for the crowded-out sellers)",
    "C-13": "missing record fact (no role field for sellers of unnamed goods; seller_actor is null) and missing rule: CR-4 'A change in means alone'",
    "C-14": "same as C-13, with OC-5",
    "C-15": "unsupported form: OC-8, CR-7c for existing bonds; per-reading sign cell",
    "C-16": "same as C-15 (CR-7a)",
    "C-17": "same as C-15 (CR-7, CR-10b)",
    "C-18": "combiner: a CR-12b total over C-13 and C-11 is not declared",
    "C-23": "case-specific provision: CR-8 (a law that promises more than its budget can pay) under reading U1-b; the per-reading sign cell and the shortfall bearers have no encoding",
    "C-24": "missing rule and question: CR-4 'A change in means alone' with CR-12e against the rate chain (A-1, A-16, A-17)",
    "C-25": "missing rule: RS-8 with CR-4 for borrowers against the announced payment (A-5)",
    "C-26": "missing rule: CR-10b/CR-8b for loans not taken (A-6)",
    "C-27": "missing rule: CR-1 operation 3 / CR-4 (comply or violate) for false claims; the record has no `claimants.false` role",
    "C-28": "missing rule and record fact: CR-8b for what a diverted payment adds to the fraudsters",
    "C-29": "missing record fact (no role for the defrauded households) and missing rule: CR-8c, OC-2",
    "C-31": "case-specific provision: prosecution (a second agency) has no role field",
    "C-32": "unsupported form: OC-8, CR-7c for homes; per-reading sign cell",
    "C-33": "combiner: a CR-12b ambiguity across the sales chain and the discount-rate chain is not declared; unsupported form (OC-8)",
}
PRODUCED = {"C-1", "C-2", "C-5", "C-19", "C-22", "C-30"}


def test_consistent_with_worked_example_we033():
    pred, keys = _engine(WE33)
    rows = _rows("WE-033_household_cash_rebate.md", SHORT, WINDOWS, {})
    assert len(rows) == 31
    _check(rows, keys, EXCEPTIONS, NOT_PRODUCED, PRODUCED)
    by = {(c["actor_class"], c["variable"]): c for c in pred["consequences"]}
    # SB-1 with borrowing is Tier A from the medium horizon (as C-19 says: 2028 to 2037); OC-3 and the claims cost are Tier A
    payers = by[("taxpayers.later", "resources_available_other_uses")]
    assert payers["horizon"] == ["medium", "long"] and payers["sign"] == "at_least_one_decrease"
    assert payers["actor_group"] == ["taxpayers.later", "public_spending_recipients.later"]   # C-19
    # SB-1's receipt side is Tier A for a lump sum (C-1, C-22); false claims and their recovery rest on premises (C-30)
    assert {c["tier"] for c in pred["consequences"] if c["variable"] not in ("legal_breach", "non_tax_receipts")} == {"A"}
    # a lump sum has no questions, so nothing else is derived: no quantity, price or window rows
    assert len(pred["consequences"]) == 7
