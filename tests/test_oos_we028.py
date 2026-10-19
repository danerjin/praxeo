"""Out-of-sample run of the quota rules (praxeo/rules/licensing.lp, EN-6) on WE-028, a catch cap with transferable shares.

The quota rules were written from EN-6's text alone (no example). Same shape as
tests/test_licensing.py::test_consistent_with_worked_example_we003: every reported engine consequence is a row of the
example's consequence list (key: actor class, variable, sign, window) or sits in EXCEPTIONS with its reason (prefixed
"KNOWN WRONG:" when it contradicts the example); every table row the engine does not produce sits in NOT_PRODUCED with
the reason. The record and answers are in cases/we028_kallmark/, the write-up in cases/we028_kallmark/out_of_sample.md.
Nothing under praxeo/ was changed for this run.

EN-12 (allocation by history) and EN-13 (consolidation) are not encoded, so most of the table is out of reach. The table's
"(2026–2027)" cells are the announcement window; the engine signs no quota row there.
"""
from pathlib import Path

from test_out_of_sample import _check, _engine, _rows

ROOT = Path(__file__).resolve().parents[1]
WE28 = ROOT / "cases" / "we028_kallmark"

# C-3's "all vessels fishing ridge cod" is the record's right-holder role; the OC-1 payer group's second member is prose
SHORT = {"all vessels fishing ridge cod": "share_recipients", "recipients of other public spending": "recipients.other_spending"}
WINDOWS = {"2026–2027": "announcement"}
EXCEPTIONS = {
    ("vessel_owners.history", "number_of_sellers", "decrease", None):
        "EN-13 (consolidation, added after the first run): C-9 signs it for operators.high_cost, a subclass the record has no role for",
    ("vessel_owners.history", "asset_value", "increase", "announcement"):
        "the race of EN-12 (added after the first run): vessels with history gain value in the window; C-8 signs it for vessel_owners.at_announcement, a subclass",
    ("buyers.fresh_domestic", "search_cost", "increase", None):
        "RS-3 with RS-10 for the buyers of unrecorded fish, sold fresh at home (`informal_buyer_actor`, added after the first run); not in the table",
    ("buyers.fresh_domestic", "disputes_settled_outside_courts", "increase", None):
        "RS-10, as above",
    ("buyers.fresh_domestic", "quality_information", "decrease", None):
        "RS-10, as above",

    ("buyers.regional", "resources_available_other_uses", "decrease", None):
        "CR-8b, the mirror of C-49 (what the buyers pay above the old price); the table lists the price only",
}
NOT_PRODUCED = {
    "C-7": "missing rule and question: entry under a cap that must be bought or leased (EN-6 signs entry_rate only for seller_cap); no A-27 question; no entrant role",
    "C-8": "missing rule and role: CR-7c claims before creation (the claim rides on vessels sold in the window); no vessel_owners.at_announcement role",
    "C-9": "missing rule: EN-13 (consolidation under tradable rights) is not encoded; no operators.high_cost role",
    "C-11": "missing rule and role: CR-1/CR-4 on the condition for holding a right (only vessel owners may hold shares); no holders.non_fishing role",
    "C-12": "missing rule: physical-unit quota on heterogeneous output (high-grading; CR-4 on land-or-discard) is not encoded; no A-9 question",
    "C-13": "same as C-12 (and the discard ban as an RS-3 margin)",
    "C-16": "missing rule and role: RS-5 for vessels bought to hold shares (A-14); no processors role in a quota record",
    "C-20": "missing rule: RS-6/CR-7a, displaced boats move to the open saithe and ling fisheries; the quota record has no substitute-seller role",
    "C-21": "missing record fact: one buyer role per quota; the record names the regional buyers (C-49), and the fresh domestic buyers (EN-6 Unless: the home part is rationed by its own price) have no second role",
    "C-22": "missing rule: EN-6's Unless clause signs the lease price only and suppresses the holders' net_price_received; the processors competing for fish (CR-9, A-17, A-18) are not modeled",
    "C-23": "missing record fact and rule: CR-9 for the plants as buyers of the capped good; no processors role",
    "C-24": "same as C-23 (CR-7b)",
    "C-25": "same as C-23, with RS-6 for plant workers",
    "C-27": "missing record fact and rule: RS-12 for the suppliers of fuel, ice and repairs (section 1 does not name them as complements); EN-12 for the race window",
    "C-28": "missing record fact and rule: RS-12 for the complements; `related` is not read for quotas",
    "C-29": "missing rule and combiner: CR-12b over vessels without shares (RS-13, CR-7c against CR-1, CR-4); no vessel-market roles",
    "C-30": "case-specific provision: the crew settlement rule (K3, term_prohibition) has no rules; CR-5c, CR-12b, and the per-reading sign cell",
    "C-31": "missing rule: OC-2 and CR-8c for the owners' costs of the register, fees and monitor fee are not encoded for quotas (EN-1's compliance cost needs some_qualify)",
    "C-34": "missing rule: OC-7 and CR-8b for the shares sold (A-23); no question for trade in the rights",
    "C-35": "same as C-34, and no share_buyers.later role",
    "C-36": "missing rule: RS-16 and RS-13 for the price of substitutes; ambiguous combiner",
    "C-37": "missing rule: CR-9 and CR-12b for the processing ports; no ports roles",
    "C-38": "missing rule and role: CR-7c for the plants (asset_value of processors), owners' role absent",
    "C-40": "missing rule: EN-13 (catch per remaining vessel); no operators.low_cost role",
    "C-41": "missing record fact and rule: RS-7 for the firms near the 8% limit; the limit is not a field and there is no vessel_owners.large role",
    "C-42": "case-specific provision: U1 is on K3 (term_prohibition, no rules); the per-reading sign cell cannot be produced and reading_fields has no Component field for it",
    "C-43": "missing rule: OC-3 with CR-8b/CR-8e, the enforcer's non_tax_receipts from fees (A-23) and fines (A-2 with A-10 or A-11)",
    "C-44": "missing rule: CR-8e/CR-8b for detected violators; the evasion question asks about trade not caught, not about those caught",
    "C-45": "missing rule: EN-12 with CR-9 for the race window",
    "C-46": "missing rule: RS-1 and RS-16 for buyers who turn to substitutes under a quota (the substitute question exists for licensing only)",
    "C-47": "missing rule: EN-12 (race window) with CR-9",
    "C-48": "same as C-47",
    "C-50": "missing rule: RS-1 for the foreign sellers of substitutes (supply premise A-29); no question for it under a quota",
    "C-51": "case-specific provision: the crew share term (K3) has no rules (CR-5c, CR-7b)",
    "C-52": "missing rule: EN-13 and CR-7a for vessels sold abroad",
    "C-53": "missing rule and role: CR-8b/OC-7 for buyers of vessels in the window; no vessel_buyers.window role",
    "C-54": "same as C-53 (the sellers' side)",
    "C-55": "missing record fact and rule: CR-8b and CR-9 for the monitors hired; K4 is folded into K1 and the monitors have no role",
}
PRODUCED = {"C-1", "C-2", "C-3", "C-4", "C-5", "C-6", "C-10", "C-14", "C-17", "C-18", "C-19", "C-26", "C-32", "C-33", "C-39", "C-49"}


def test_consistent_with_worked_example_we028():
    pred, keys = _engine(WE28)
    rows = _rows("WE-028_fishing_quota_shares.md", SHORT, WINDOWS, {})
    assert len(rows) == 54
    _check(rows, keys, EXCEPTIONS, NOT_PRODUCED, PRODUCED)
    # EN-6 Unless: the lease price of the right rations the cap, so the holders' net price received is not signed
    assert ("share_recipients", "net_price_received", "increase", None) not in keys
    # the table's "from the announcement" asset value (C-2) is the capitalized right; the engine's has no window
    assert ("share_recipients", "asset_value", "increase", None) in keys
    # the example has the enforcement cost as Tier A (no assumption); the engine gates it on binding and enforced (Tier B)
    by = {(c["actor_class"], c["variable"]): c for c in pred["consequences"]}
    assert by[("officials.enforcement", "enforcement_cost")]["tier"] == "B"
