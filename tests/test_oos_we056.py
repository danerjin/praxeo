"""Out-of-sample run of the subsidy rules (and the ceiling rules) on WE-056: consistency with the example's consequence list.

Same shape as tests/test_subsidies.py::test_consistent_with_worked_example_we019. WE-056 was not used to write any rule.
The record (cases/we056_tarrenmoor/record.json) was written from policy.txt alone: K1 as a price_ceiling on what pharmacies
collect, K2 as a mandated_contract_term (no rules), K3 as a purchase_rebate. The classification and the gaps are in
cases/we056_tarrenmoor/out_of_sample.md. Engine rows that contradict the example are marked "KNOWN WRONG:".
"""
from test_out_of_sample import ROOT, _check, _engine, _rows

WE56 = ROOT / "cases" / "we056_tarrenmoor"

# the table's class totals are matched to the record's subclasses; "lobbying groups" to the roles the record has for them
SHORT = {
    "covered_residents": ["covered_residents.uninsured", "covered_residents.paying_above_cap"],
    "lobbying groups": ["pharmacies.in_state", "covered_residents.paying_above_cap", "plans.state_regulated"],  # A-17 names insurers
    # the OC-1 payer group's members, written in prose
    "recipients of other state spending": "recipients.other_spending", "future taxpayers": "taxpayers.future",
}
WINDOWS = {"Nov–Dec 2027": "announcement", "Jan–Feb 2028": "first_months"}

# The first run recorded K1 as a price_ceiling, and the PC-1 shortage, its rationing group, PC-6, RS-10 and PC-16's transfer
# from the pharmacies came out (11 KNOWN WRONG rows). K1 is a cap on the buyer's share that a third party makes up (PC-20,
# `third_party_payer_actor`): the engine writes no ceiling fact for it, so none of those rules applies.
EXCEPTIONS = {
    ("plans.state_regulated", "compliance_cost", "increase", None):
        "OC-2 on K2 (mandates.lp, Tier A): plans must process the balance bills; the table records the outlay (C-2), not the processing",
    ('covered_residents.uninsured', 'resources_available_other_uses', 'increase', None):
        'SB-1 with CR-8b: what the recipients receive adds to their means; the example records the price they pay (C-1); C-39 is the same receipt for the insured',
    # defensible rows the table does not list
    ("covered_residents.uninsured", "price_paid", "decrease", None):
        "SB-2 for the Fund's recipients: a subclass of C-1's covered_residents.paying_above_cap, which section 3 of the example says includes the uninsured cash buyers",
    ("sellers.substitutes", "quantity_traded", "decrease", None):
        "SB-3 and RS-1 on A-8: recipients leave the unsubsidized good; the table has the buyers' side (C-12) and the chains' price and stocks (C-29)",
}
NOT_PRODUCED = {
    "C-4": "missing rule: PC-20's seller side (the receipt is set by the payer's terms, CR-6 1.1) is not encoded; PC-20 signs the buyers and the payer only",
    "C-6": "missing rule: SB-2 1.1 (a payment indexed to the seller's own price draws the posted price toward the limit); DM-1 needs seller_supply_slow, answered 0.1",
    "C-7": "missing rule: same mechanism (the cash buyers outside the Act pay the drawn-up usual price)",
    "C-8": "missing rule: RS-2 for sellers serving a payer-paid customer; PC-4 signs the protected buyers' quality only",
    "C-9": "unsupported form: K2; RS-2 for payers (prior authorization) has no rule",
    "C-10": "missing rule: RS-21 / RS-16 (price per unit of quality, product switching) is not encoded for subsidies",
    "C-11": "unsupported form: K2, and the same missing rule",
    "C-12": "missing record fact: SB-3 gives the substitute sellers' side only (an exception above); the buyers of the substitute have no role field",
    "C-13": "missing record fact and rule: no role for enrollees of private programs; CR-9 displacement of a private provider by a public payer is not encoded",
    "C-14": "missing record fact and rule: no role for upstream manufacturers; CR-9 / CR-12a not encoded for subsidies",
    "C-15": "missing record fact and rule: manufacturers' list price (CR-6 small effect in a wider market); no role",
    "C-16": "missing record fact and rule: buyers elsewhere in the country; no role",
    "C-18": "missing rule: RS-8 catch-up after the effective date for buyers; only the pull-back before it (C-17) is signed",
    "C-19": "unsupported form: K2; CR-9 pass-through of a mandated payment to premium payers has no rule",
    "C-20": "unsupported form: K2; RS-5 conversion to self-funding has no rule or role",
    "C-21": "unsupported form: K2; CR-4c on coverage has no rule",
    "C-22": "missing rule and record fact: RS-3 for false attestation (SB-5 with criteria signs no breach); no role for self-funded residents",
    "C-23": "missing rule: A-16 (evasion, 0.6) gives PC-6 key money for the pharmacies, not legal_breach (RS-3 as a breach is not encoded)",
    "C-25": "missing record fact: U1's readings carry no engine facts (parser leaves reading_facts empty) and no nonresident or mail-order role; RS-4 for mail order is not encoded",
    "C-27": "missing record fact: no role for the nonresident pharmacies; U1 not run by reading",
    "C-28": "missing record fact: no mail-order users role; U1 not run by reading",
    "C-29": "missing rule: RS-16 and CR-10b for the substitute sellers' price and stocks; SB-3 signs quantity only",
    "C-30": "missing rule: CR-12e / CR-7a over a long horizon for the substitute's cost per unit",
    "C-31": "missing record fact: no complements role in the subsidy record, and RS-12 is not encoded",
    "C-32": "missing record fact: same",
    "C-33": "case-specific provision: PBM contract renewals in 2029 (A-22); no rule for contract resets (CR-5c, RS-8 for contracts)",
    "C-34": "missing record fact and rule: shares of manufacturers; SB-4 needs asset_owner_actor and the record has none",
    "C-35": "combiner: CR-12b total of the premium tax chains is not a declared comparison; also TX-10 and the premium tax are case-specific",
    "C-36": "missing rule and record fact: fines paid into the fund (OC-3 own-revenue case with CR-8b); no fund role",
    "C-38": "unsupported form: K2; OC-1 for premium payers has no rule",
    "C-42": "missing rule: OC-3's absorbed-in-the-existing-budget case is not encoded for ceilings (the enforcement question is asked only with general_budget)",
    "C-43": "case-specific provision: deductible accounting in high-deductible plans (A-28); no hdhp role",
    "C-44": "case-specific provision: same",
    "C-45": "unsupported form: K2; RS-2 / OC-2 for plans' waiting times has no rule",
    "C-46": "missing record fact and rule: manufacturers' resources (CR-8b); no role",
    "C-47": "missing record fact: border residents have no role (neighbor_actor is for shut-out buyers, and the text names none)",
    "C-48": "missing rule: same as C-7 (CR-4c for cash buyers outside the Act is gated by seller_supply_slow in SB-2)",
    "C-49": "unsupported form: K2; no role for the national premium credits (CR-9)",
    "C-50": "missing record fact: no nonresident role; U1 not run by reading; CR-7c not encoded for subsidies",
    "C-51": "missing rule and record fact: CR-8b on the plans of false attesters; no role",
}
PRODUCED = {"C-1", "C-2", "C-3", "C-5", "C-17", "C-24", "C-26", "C-37", "C-39", "C-40", "C-41"}  # C-24: RS-7 for the plans bound by K2 (mandates.lp)


def test_consistent_with_worked_example_we056():
    pred, keys = _engine(WE56)
    rows = _rows("WE-056_insulin_price_cap.md", SHORT, WINDOWS, {})
    assert len(rows) == 51
    _check(rows, keys, EXCEPTIONS, NOT_PRODUCED, PRODUCED)
    assert not any(v.startswith("KNOWN WRONG") for v in EXCEPTIONS.values())
    # PC-20: no shortage from a cap on the buyer's share, so none of the ceiling rules' rows
    assert not any(k[0] == "buyers.prospective" for k in keys)
    assert ("plans.state_regulated", "subsidy_outlay", "increase", None) in keys                       # C-2
