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
    "lobbying groups": ["pharmacies.in_state", "covered_residents.paying_above_cap"],
}
WINDOWS = {"Nov–Dec 2027": "announcement", "Jan–Feb 2028": "first_months"}

_NO_SHORTAGE = ("PC-1 and PC-16 do not apply (section 2 of the example): the pharmacy receives the balance from the plan or "
                "the Fund, so no excess demand forms")
EXCEPTIONS = {
    # K1 recorded as a price_ceiling: the PC-1 shortage and its rationing group, for the engine's default excluded role
    ("buyers.prospective", "excess_demand", "increase", None): "KNOWN WRONG: " + _NO_SHORTAGE + "; the record has no excluded role and the engine fills buyers.prospective",
    ("buyers.prospective", "quantity_demanded", "increase", None): "KNOWN WRONG: PC-1 (as excess_demand)",
    ("buyers.prospective", "wait_time", "at_least_one_increase", None): "KNOWN WRONG: member of the PC-2 group; the example removes rationing",
    ("buyers.prospective", "search_cost", "at_least_one_increase", None): "KNOWN WRONG: member of the PC-2 group",
    ("buyers.prospective", "side_payments", "at_least_one_increase", None): "KNOWN WRONG: member of the PC-2 group",
    ("buyers.prospective", "allocation_by_non_price_criteria", "at_least_one_increase", None): "KNOWN WRONG: member of the PC-2 group",
    ("buyers.prospective", "search_cost", "increase", None): "KNOWN WRONG: PC-2 member (as above)",
    ("buyers.prospective", "side_payments", "increase", None): "KNOWN WRONG: PC-2 member and PC-6 for buyers shut out by a shortage",
    ("buyers.prospective", "informal_activity", "increase", None): "KNOWN WRONG: PC-6 with RS-3 for the shut-out buyers",
    ("buyers.prospective", "disputes_settled_outside_courts", "increase", None): "KNOWN WRONG: RS-10 for the informal trade of the shut-out buyers",
    # K1's PC-16 transfer from the pharmacies, and PC-5's supply fall
    ("pharmacies.in_state", "net_price_received", "ambiguous", None):
        "KNOWN WRONG: PC-16 puts the patients' saving on the pharmacies against SB-2's increase; the example has the pharmacy's receipt unchanged or higher (C-4, C-6)",
    ("pharmacies.in_state", "quantity_traded", "ambiguous", None):
        "KNOWN WRONG: SB-2's increase against PC-5's supply fall (alternative_uses answered 0.15); the example has an increase (C-26)",
    ("pharmacies.in_state", "resources_available_other_uses", "decrease", None):
        "KNOWN WRONG: CR-8 with PC-16 takes the patients' saving from the pharmacies (item rent_forgone, and the total); the transfer runs from plans and the Fund (CR-8b)",
    # defensible rows the table does not list
    ("pharmacies.in_state", "resources_available_other_uses", "increase", None):
        "item key_money (PC-6, RS-3, CR-8) on A-16: some pharmacies collect more than $35 and keep it; the table has the breach (C-23), not the receipt",
    ("covered_residents.uninsured", "price_paid", "decrease", None):
        "SB-2 for the Fund's recipients: a subclass of C-1's covered_residents.paying_above_cap, which section 3 of the example says includes the uninsured cash buyers",
    ("covered_residents.paying_above_cap", "price_paid", "decrease", "first_months"):
        "same sign as C-1: the combiner forms the first-months row from the cap chain when window_repricing is unreported",
    ("covered_residents.paying_above_cap", "quality_adjusted_price", "decrease", None):
        "price falls with the product unchanged; C-10 and C-11 sign the product, not this variable",
    ("sellers.substitutes", "quantity_traded", "decrease", None):
        "SB-3 and RS-1 on A-8: recipients leave the unsubsidized good; the table has the buyers' side (C-12) and the chains' price and stocks (C-29)",
    ("taxpayers", "resources_available_other_uses", "decrease", None):
        "SB-1 with OC-1 (Tier A): the engine signs the funders' decrease plainly; the table has the at_least_one_decrease group over three classes (C-37)",
}
NOT_PRODUCED = {
    "C-2": "unsupported form: K2 (a plan must pay the balance) is a mandated_contract_term; no rule signs the payer's outlay",
    "C-3": "missing record fact and rule: no role for the paying fund (taxpayer_actor is the funder); SB-1 signs the funders' resources, not subsidy_outlay",
    "C-4": "missing rule: PC-20 / CR-6 1.1 (a cap on the buyer's share made up by a third party) is not encoded; the engine's row for this key is the WRONG ambiguous",
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
    "C-26": "WRONG row instead: the engine signs pharmacies.in_state quantity_traded ambiguous (SB-2 against PC-5), not increase",
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
    "C-37": "sign form: the engine signs taxpayers alone with a plain decrease (SB-1, Tier A); the table signs three classes as at_least_one_decrease",
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
PRODUCED = {"C-1", "C-5", "C-17", "C-24", "C-39", "C-40", "C-41"}


def test_consistent_with_worked_example_we056():
    pred, keys = _engine(WE56)
    rows = _rows("WE-056_insulin_price_cap.md", SHORT, WINDOWS, {})
    assert len(rows) == 51
    _check(rows, keys, EXCEPTIONS, NOT_PRODUCED, PRODUCED)
    assert {k for k, v in EXCEPTIONS.items() if v.startswith("KNOWN WRONG")} >= {
        ("buyers.prospective", "excess_demand", "increase", None), ("pharmacies.in_state", "net_price_received", "ambiguous", None)}
