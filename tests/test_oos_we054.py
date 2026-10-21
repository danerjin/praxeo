"""Out-of-sample run of the quota rules (praxeo/rules/licensing.lp: EN-6, EN-12, EN-13) on WE-054, a night curfew with a
daytime slot cap, slots allocated by history and tradable.

EN-6 was written from the catalog text; EN-12 and EN-13 from WE-028 only. WE-054 was not used for any rule. Same shape as
tests/test_oos_we028.py: every reported engine consequence is a row of the example's consequence list (key: actor class,
variable, sign, window) or sits in EXCEPTIONS with its reason (prefixed "KNOWN WRONG:" when it contradicts the example); every
table row the engine does not produce sits in NOT_PRODUCED with the reason. The record and answers are in
cases/we054_wexcombe/, the write-up in cases/we054_wexcombe/out_of_sample.md. Nothing under praxeo/ was changed.

The table's base-season cells ("in the base seasons") are the announcement window. K1 (the curfew, `prohibition`), K3 and K5
(`rights_allocation`) have no rules, so the night-side rows are out of reach.
"""
from pathlib import Path

from test_out_of_sample import _check, _engine, _rows

ROOT = Path(__file__).resolve().parents[1]
WE54 = ROOT / "cases" / "we054_wexcombe"

SHORT = {}
WINDOWS = {"base seasons": "announcement"}
EXCEPTIONS = {
    ("buyers.current", "quantity_substitute", "increase", None):
        "RS-1 (A-11, Pellham); prohibition rules (rules/prohibition.lp, added after the first run) on the curfew (k1): the buyers of night flights carry the default role name buyers.current, which the table does not use; it signs the travelers' moves to Pellham (C-22 to C-24)",
    ("buyers.current", "quantity_traded", "decrease", None):
        "EN-7: night trade stops; prohibition rules (rules/prohibition.lp, added after the first run) on the curfew (k1): the buyers of night flights carry the default role name buyers.current, which the table does not use; it signs the travelers' moves to Pellham (C-22 to C-24)",
    ("operators.night", "asset_value", "decrease", None):
        "KNOWN WRONG: EN-7 with SB-4 signs the loss on the sort hall (A-16) alone; C-45 signs the night operators' assets ambiguous, the hall's loss against the value of their priority claim to freed slots (C-44, A-31), a comparison no rule forms",
    ("operators.night", "employment", "decrease", None):
        "EN-7 with CR-1 (A-16): night work stops at WXI; the table records employment at WXI as a whole (C-25)",
    ("operators.night", "lobbying_effort", "increase", None):
        "RS-7 over provisions that exist only under the order, beside the contested-field row (C-46, A-32)",
    ("operators.night", "number_of_sellers", "decrease", None):
        "EN-7: night operators stop operating at night at WXI; not in the table",
    ("airlines.history", "quantity_traded", "decrease", None):
        "EN-6 for the capped movements; the same fact as C-2, which the table writes as quantity_supplied",
    ("airlines.history", "quantity_traded", "increase", "announcement"):
        "EN-12 race; the same fact as C-5, which the table writes as quantity_supplied",
    ("airlines.history", "resources_available_other_uses", "decrease", "announcement"):
        "EN-12 with CR-8c, the means used up in the race; the mirror of C-6, which the table writes as compliance_cost",
    ("airlines.history", "investment_target", "increase", "announcement"):
        "EN-12 (investment in the activity during the race); the table does not list it (A-5 speaks of added flights only)",
    ("airlines.history", "asset_value", "increase", "announcement"):
        "EN-12 with CR-7c, assets that carry history gain value in the window; the table has the slots' value (C-3) with no window",
    ("airlines.history", "capital_stock_target", "decrease", None):
        "EN-13 (long run); not in the table, and aircraft move between airports, so the WXI fleet is not a rule-derived sign against no order",
    ("workers.wxi", "employment", "at_least_one_increase", "announcement"):
        "EN-12 crews: employment follows the added base-season flights (A-25); the table lists no row for workers in the window",
    ("workers.wxi", "hours_worked", "at_least_one_increase", "announcement"):
        "same",
}
NOT_PRODUCED = {
    "C-1": "missing rule: K1 is a `prohibition` and no rule reads it (RS-8 per window, CR-1)",
    "C-2": "variable mismatch: the engine reports the fall as quantity_traded (EN-6) for airlines.history; the table writes quantity_supplied",
    "C-5": "variable mismatch: the engine reports the race as quantity_traded (EN-12); the table writes quantity_supplied",
    "C-6": "variable mismatch: EN-12 signs the means used up (resources_available_other_uses), not compliance_cost (CR-8c)",
    "C-7": "missing rule and roles: RS-4/RS-1/RS-16 for a prohibition; no integrator, cargo carriers or Pellham role",
    "C-8": "missing rule and role: RS-8 for flights moved into the shoulders; the curfew has no rules and operators.night is not the quota's bound role",
    "C-9": "same as C-8, with U1 (no Component field for a dispensation)",
    "C-10": "missing rule and role: nothing signs the buyers' purchases under EN-13 (the engine signs the sellers'); operators.night is not a holder role",
    "C-11": "missing rule and question: RS-21/CR-4c for larger aircraft under a cap in movements; no A-8 question",
    "C-13": "missing rule: entry into a capped market where rights must be bought (EN-6 signs entry only for seller_cap; EN-13 1.0 blocked entry)",
    "C-14": "missing rule: RS-3 for breaches of a prohibition; the evasion question is about the cap",
    "C-15": "case-specific provision: U1 on K1 (no rules); RS-5 reclassification",
    "C-17": "missing rule and role: RS-7 for the residents on a prohibition; the engine's contested-field row went to the slot holders",
    "C-18": "missing rule and role: CR-7c for the integrator's facility; K1 has no rules and no integrator role",
    "C-22": "missing rule and role: RS-4/CR-9/CR-3a for night travelers",
    "C-23": "missing rule and role: RS-1/RS-16 toward a neighbouring airport; no neighbour role for quotas",
    "C-24": "same as C-23 (CR-9)",
    "C-26": "missing rule and role: OC-5/CR-9 for Pellham workers",
    "C-27": "missing record fact and rule: CR-9/CR-7c for homes near the airport (proximity is not a record field); no neighbors role in a quota",
    "C-28": "same as C-27 (Tier C proximity chain, CR-12b)",
    "C-29": "same as C-27, for Pellham homes",
    "C-30": "same as C-27, for Pellham homes",
    "C-31": "missing rule and role: CR-9/CR-4 for shippers",
    "C-32": "missing record fact and rule: the WAA's cost-recovery charge method is an existing rule with no field; PC-15, CR-9 (1.0)",
    "C-33": "missing record fact and rule: concessions are not in section 1; RS-12 for quotas",
    "C-34": "missing rule: CR-8b for lessors' receipts; EN-13 signs only the lease price",
    "C-35": "missing rule and role: CR-8b for lessees and buyers; operators.night as a lessee is not a role",
    "C-36": "missing rule: CR-12b combiner over the airlines' operations as a whole (slot value against scarcity); the engine signs the slot value alone",
    "C-38": "missing rule: CR-9 over proximity for the noise office",
    "C-40": "missing rule: OC-2/CR-8c compliance cost for quotas is not encoded",
    "C-42": "missing rule: OC-3 with CR-8b for penalty receipts; no question for them",
    "C-44": "missing rule: K5 is a `rights_allocation` and no rule reads it (CR-1, CR-7c, CR-3b)",
    "C-45": "missing rule and role: CR-12b over night operators' businesses as a whole",
    "C-47": "missing rule: RS-13/CR-9 for off-peak fares in the race window (EN-12 signs no price)",
    "C-48": "missing rule and role: CR-9/LW-10 for hauliers",
    "C-50": "missing rule: CR-8b for the payers of penalties",
    "C-51": "missing rule and role: EN-6 1.0 with CR-9 for the national buyers of overnight parcels; K1 has no rules",
    "C-52": "missing rule: OC-1/CR-8b for the WAA's fund balance; funding from charges is not `general_budget`",
}
PRODUCED = {"C-3", "C-4", "C-12", "C-16", "C-19", "C-20", "C-21", "C-25", "C-37", "C-39", "C-41", "C-43", "C-46", "C-49"}


def test_consistent_with_worked_example_we054():
    pred, keys = _engine(WE54)
    rows = _rows("WE-054_airport_night_curfew.md", SHORT, WINDOWS, {})
    assert len(rows) == 52
    _check(rows, keys, EXCEPTIONS, NOT_PRODUCED, PRODUCED)
    # EN-6 without a wider market: the holders' net price is signed (C-21)
    assert ("airlines.history", "net_price_received", "increase", None) in keys
    # the example has the slot unit's enforcement cost as Tier A (no assumption); the engine gates it on binding and enforced
    by = {(c["actor_class"], c["variable"]): c for c in pred["consequences"]}
    assert by[("officials.enforcement", "enforcement_cost")]["tier"] == "B"
