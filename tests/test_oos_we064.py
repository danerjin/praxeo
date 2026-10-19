"""Out-of-sample run of the quota rules (praxeo/rules/licensing.lp: EN-6, EN-12, EN-13) on WE-064, an auction of spectrum licenses.

EN-6 was written from the catalog text, EN-12 and EN-13 from WE-028 only. WE-064 is a right created by the policy and sold at
auction, not allocated by history, with a cap on holdings per bidder, a build-out obligation and receipts into the budget.
Same shape as tests/test_oos_we028.py: every reported engine consequence is a row of the example's consequence list (key:
actor class, variable, sign, window) or sits in EXCEPTIONS with its reason (prefixed "KNOWN WRONG:" when it contradicts the
example); every table row the engine does not produce sits in NOT_PRODUCED with the reason. The record and answers are in
cases/we064_tarnesse/, the write-up in cases/we064_tarnesse/out_of_sample.md. Nothing under praxeo/ was changed for this run.

The record has three components: K1 (`rights_allocation`, the auction), K2 (`mandated_contract_term`, the build-out) and K3
(`quota`, the cap on holdings). Only a quota gets rules and questions, so every engine row comes from K3. K4 (receipts) and K5
(administration) have no instrument in the ontology; K5 is the quota's general_budget and K4 has no component.
"""
from pathlib import Path

from test_out_of_sample import _check, _engine, _rows

ROOT = Path(__file__).resolve().parents[1]
WE64 = ROOT / "cases" / "we064_tarnesse"

SHORT = {"recipients of other spending": "recipients.other_spending", "future taxpayers": "taxpayers.future"}
WINDOWS: dict = {}
EXCEPTIONS = {
    ("licensees", "lobbying_effort", "increase", None):
        "RS-7 for the holders of the rights; C-15 signs the same for lobbying groups (operators, entrants, town councils), a wider role the record has no field for",
    ("bidders", "informal_activity", "increase", None):
        "RS-3 for holdings beyond the cap that are not caught (A-5); C-8 records the same behavior as reclassification (stakes below the affiliate line, RS-17)",
    ("bidders", "search_cost", "increase", None):
        "RS-3 with RS-10 for the buyers of unrecorded trade; here the evasion is stakes below the affiliate line, not unrecorded trade in a good, so the buyers' "
        "search and quality chains do not fit; not in the table",
    ("bidders", "quality_information", "decrease", None): "RS-10, as above; not in the table",
    ("bidders", "disputes_settled_outside_courts", "increase", None): "RS-10, as above; not in the table",
}
NOT_PRODUCED = {
    "C-3": "missing rule: PC-17 for the build-out (`mandated_contract_term` has no rules or questions) and CR-1/CR-4 for investment in a created right; no A-1/A-3 question",
    "C-4": "missing rule: CR-9/LW-10 for customers of the service the right permits; no customers role is read for a quota on holdings",
    "C-5": "missing rule: PC-17 (mandated_contract_term) for service in towns",
    "C-6": "missing rule: CR-4 for applications to bid for a right the state creates (EN-1 asks for a licensing_requirement)",
    "C-7": "missing rule: OC-2/CR-8c for the bidders' preparation costs; EN-1's compliance_cost needs a licensing_requirement with some_qualify",
    "C-8": "missing rule: RS-17 (reclassification under a holding cap); evasion gives informal_activity, a different variable",
    "C-9": "missing rule: RS-17 and CR-5 for pooling of blocks by sharing agreements; no A-6 question",
    "C-10": "missing rule: CR-4/CR-9 for less densification in existing bands; no A-7 question and no substitute-use rule for a created right",
    "C-11": "missing rule: RS-3/RS-5 for breach of a mandated term (PC-17 and mandated_contract_term have no rules); no A-9 question",
    "C-12": "EN-13 is not reported (trade_cheap is below the cut-off) and signs no transfer-volume variable; a quantity of licenses transferred is not an EN-13 effect",
    "C-13": "missing rule: RS-5 for company sales and capacity leases in place of transfers; no A-11 question",
    "C-14": "missing rule and role: CR-4/CR-10a for bidders who plan to resell; no bidders.financial role and no A-12 question",
    "C-15": "role: the engine signs the holders (`licensees`) where the table has lobbying groups (see EXCEPTIONS)",
    "C-16": "missing rule: CR-1/CR-4 for entry by a winner of a created right; EN-6 signs entry only for seller_cap, and the entrant role is read only for EN-12's race",
    "C-17": "missing rule: EN-13's clause for a resource with no users without the policy (1.1) is not encoded; as encoded EN-13 signs fewer sellers and is not reported here",
    "C-18": "missing rule: CR-4/CR-9 for entrants' fixed wireless supply; no A-14/A-18 question",
    "C-19": "missing rule: RS-13/CR-6/CR-12 for quality-adjusted prices of the service; no customers role for a quota on holdings",
    "C-20": "missing rule and role: RS-13/CR-7c for the incumbents' licenses in existing bands; no owners.incumbents role",
    "C-21": "same as C-20 (CR-12b combiner over the shares' value)",
    "C-22": "missing rule and role: RS-16/CR-9 for the substitute seller's volume (DSL); no substitute-seller role for a quota",
    "C-23": "same as C-22 (RS-16, CR-6)",
    "C-24": "same as C-22 with CR-7c for the owners of the copper network",
    "C-25": "missing rule: CR-9/CR-6 for the demand of the build-out for sites; EN-13's supplier effect (tower_owners) has the opposite sign and is not reported",
    "C-26": "missing rule: CR-7c/SB-4 for towers and sites (no rule from a mandated term to its input suppliers)",
    "C-27": "missing rule: CR-4/CR-7a/CR-12b for new towers; EN-13's supplier effect is not reported",
    "C-28": "missing rule and role: CR-9/LW-10 for the riggers' wages; `worker_actor` is the bound sellers' workers, not the workers of the installation trade",
    "C-29": "same as C-28 (employment)",
    "C-30": "missing rule and role: CR-8a/RS-13 for other projects that compete for riggers and sites",
    "C-31": "same as C-30 (the long-run ambiguous cell)",
    "C-32": "missing rule and role: CR-9 for the foreign sellers of equipment",
    "C-33": "missing rule: CR-6 (small effects are signed) on the world price of equipment; no foreign buyers role",
    "C-34": "missing rule: OC-8/CR-8a for the loan market; no borrowers role and no A-26/A-27 question",
    "C-35": "group sign differs: the engine signs the budget payers a decrease from the TCA costs alone (see EXCEPTIONS)",
    "C-36": "role: CR-8b is signed for the bidders (the record's buyer role) where the table has the licensees paying; no OC-1 rule for the price of the created right",
    "C-40": "missing rule: CR-10a for investment moved in the window before an auction (EN-12's race is for history, and K3 has no base period)",
    "C-41": "missing rule: OC-1/CR-8a for the cost of a mandated term (PC-17 not encoded)",
    "C-42": "missing rule and role: CR-10b/CR-12b for riggers' wages after 2032",
    "C-43": "missing rule and role: CR-9/CR-6 for the price other projects pay for installation work",
    "C-44": "missing rule and role: CR-6 on the world price (small), foreign buyers of equipment",
}
PRODUCED = {"C-1", "C-2", "C-37", "C-38", "C-39"}  # C-39 from mandates.lp (OC-2 on a mandate with no named recipient)


def test_consistent_with_worked_example_we064():
    pred, keys = _engine(WE64)
    rows = _rows("WE-064_spectrum_auction.md", SHORT, WINDOWS, {})
    assert len(rows) == 44
    _check(rows, keys, EXCEPTIONS, NOT_PRODUCED, PRODUCED)
    # every reported row with premises traces to the quota (K3) or to the coverage obligation (K2, mandates.lp)
    by = {(c["actor_class"], c["variable"]): c for c in pred["consequences"] if c["reported"]}
    assert all(any(k in a for k in ("k2", "k3") for a in c["assumptions"]) for c in by.values() if c["assumptions"])
    # rights sold at auction: the treasury's receipts (C-38, rights_sold, added after the first run), and no payer group
    assert by[("treasury", "non_tax_receipts")]["sign"] == "increase"
    assert ("taxpayers", "resources_available_other_uses") not in by
    # EN-13 is not reported: trade_cheap (p 0.4) is below the cut-off; EN-12 does not apply to a right sold at auction
    assert not any(c["reported"] and c["variable"] in ("capital_stock_target", "right_lease_price", "number_of_sellers")
                   for c in pred["consequences"])
    # the example's enforcement cost is Tier A (no assumption); the engine gates it on binding and enforced (Tier B)
    assert by[("officials.enforcement", "enforcement_cost")]["tier"] == "B"
