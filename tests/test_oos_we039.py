"""Out-of-sample run of the quota rules (praxeo/rules/licensing.lp: EN-6, EN-12, EN-13) on WE-039, a groundwater pumping cap
with tradable shares allocated by history.

EN-6 was written from the catalog text; EN-12 (allocation by history) and EN-13 (consolidation) from WE-028 only. Same shape
as tests/test_oos_we028.py: every reported engine consequence is a row of the example's consequence list (key: actor class,
variable, sign, window) or sits in EXCEPTIONS with its reason (prefixed "KNOWN WRONG:" when it contradicts the example);
every table row the engine does not produce sits in NOT_PRODUCED with the reason. The record and answers are in
cases/we039_sorrel/, the write-up in cases/we039_sorrel/out_of_sample.md. Nothing under praxeo/ was changed for this run.

The record has one quota (K1: cap, trading and enforcement folded in) and two rights_allocation components (K2, K3), which
have no rules. The base period (2017 to 2021) ended before the plan was proposed, so EN-12's windfall branch applies, not the
race. The record's right holder is `landholders.history`, who receive the shares; the table's lease price (C-4) is on `pumpers`.
"""
from pathlib import Path

from test_out_of_sample import _check, _engine, _rows

ROOT = Path(__file__).resolve().parents[1]
WE39 = ROOT / "cases" / "we039_sorrel"

SHORT = {}
WINDOWS = {}
EXCEPTIONS = {
    ("pumpers", "quantity_supplied", "increase", None):
        "KNOWN WRONG: EN-13's 'more per remaining user' is put on the whole class `pumpers`; C-1 and C-47 have the same key, a decrease (total groundwater pumped falls)",
    ("pumpers", "quantity_traded", "decrease", None):
        "EN-6: the capped quantity falls; the table has this event as C-1 under `quantity_supplied` (a cap on the pumpers' own pumping, not an exchange)",
    ("growers.nuts", "quantity_traded", "decrease", None):
        "EN-6 for the buyers of the capped good (`buyer_actor`); the table has C-34 for growers.field and C-37 (leases, an increase) for the lessors, and nut growers' output is C-6; defensible only as pumped water, not as leased water",
    ("pumpers", "number_of_sellers", "decrease", None):
        "EN-13 (consolidation): C-7 signs the same fall for growers.field and growers.nuts, the farms that irrigate; the record has one class, `pumpers`",
    ("landholders.history", "right_lease_price", "increase", None):
        "EN-6 Unless (quota_lease) on the record's right holder; the table puts the lease price on `pumpers` (C-4), a role that also holds the shares in the handbook",
    ("landholders.history", "lobbying_effort", "increase", None):
        "RS-7 for the holders of the rights (A-11); C-14 names growers, landholders.no_history and local water groups, not the history holders",
    ("pumpers", "informal_activity", "increase", None):
        "RS-3 (A-10): the same over-pumping as C-13, which uses `legal_breach` because the trade stays inside a legal activity",
    ("growers.nuts", "search_cost", "increase", None):
        "RS-3 with EN-3 for 'buyers of unrecorded trade'; over-pumping is self-supply, so there are no such buyers (misattributed to the buyer role); not in the table",
    ("growers.nuts", "quality_information", "decrease", None):
        "as above (misattributed); not in the table",
    ("growers.nuts", "disputes_settled_outside_courts", "increase", None):
        "RS-10 for the same trade (misattributed); not in the table",
}
NOT_PRODUCED = {
    "C-1": "unsupported form: the capped quantity is signed as quantity_traded (EN-6), the table has quantity_supplied for a cap on the bound pumpers' own pumping (autistic, no exchange)",
    "C-3": "missing rule: the lottery branch of EN-12 (K3 rights_allocation, CR-7c) has no rule; no winners role",
    "C-4": "missing role: the engine signs the lease price on the record's right holder (`landholders.history`); the table has `pumpers`; one right-holder field cannot serve C-2 and C-4",
    "C-5": "missing record fact and rule: EN-6 Inputs clause (0.9), the output of the capped input falls; the record has no output relation and no growers.field role",
    "C-6": "missing record fact and rule: EN-6 Inputs clause with CR-12e (partial response), no output relation; nut growers are the record's buyers but the rule signs their quantity_traded",
    "C-7": "missing role: EN-13 signs number_of_sellers on `pumpers`; the table names growers.field and growers.nuts (see EXCEPTIONS)",
    "C-8": "missing record fact: groundwater pumped in South by nut growers; no sub-basin or South role, and the per-reading (U1) cell",
    "C-9": "missing rule: entry under a quota that must be bought or leased (EN-6 signs entry only for seller_cap; EN-12 signs entrants only in the race); the entrant role is set but nothing reads it for this case",
    "C-10": "missing rule: CR-10a for plantings from the announcement (EN-12's first branch signs only the holders' asset value); no question A-20",
    "C-11": "missing rule: the lottery branch of EN-12 (RS-5, RS-8, CR-7c competing to qualify); K3 has no rules, no A-13 and A-21 questions",
    "C-12": "missing rule: CR-8c for the lottery entry costs (K3)",
    "C-13": "unsupported form: the over-pumping is signed as informal_activity (RS-3, C-13 uses legal_breach: the trade stays within a legal activity)",
    "C-14": "missing role: RS-7 is signed for the rights holders only; growers, landholders.no_history and local water groups have no role in the quota record",
    "C-15": "missing rule and record fact: RS-1 for buyers of the capped input turning to a substitute (surface water); the substitute question exists for licensing only",
    "C-16": "missing rule and record fact: RS-4 for relocation to the uncapped Lowther Basin; neighbor_actor is for price ceilings",
    "C-17": "missing rule and record fact: RS-16 for the substitute's price; Related has no substitute kind, and `related` is not read for quotas",
    "C-18": "missing rule and record fact: RS-4 with CR-7c for land across the border; no neighbouring-jurisdiction role",
    "C-20": "missing record fact and rule: CR-9 for suppliers of farm inputs; section 1 does not name them, and `related` is not read for quotas",
    "C-21": "missing rule and record fact: CR-9 over a shared_facility relation (the aquifer), Tier C; no such relation kind in the record",
    "C-22": "same as C-21",
    "C-23": "same as C-21 (domestic well owners have no role)",
    "C-24": "same as C-21",
    "C-25": "same as C-21 (the county programme has no role; OC-3 with a right baseline)",
    "C-26": "missing rule and combiner: CR-9 shared_facility, CR-12 (Tier C against Tier B), A-15",
    "C-27": "missing rule and combiner: CR-7c with CR-12b for land and shares in one variable; no history-holder asset comparison",
    "C-28": "missing rule and role: CR-7c, CR-10c for eligible parcels without history; K3 has no rules; combiner CR-12b",
    "C-29": "missing rule and combiner: CR-6 for the full cost of water, CR-9 shared_facility, CR-12e",
    "C-31": "missing rule: OC-3 (own revenue) with CR-8b for the fee on shares held; own_revenue_funded is set but the quota rules use only general_budget",
    "C-32": "missing rule: OC-2 and CR-8c for the pumpers' meters and reporting under a quota (EN-1's compliance cost needs some_qualify)",
    "C-33": "case-specific provision: U1 has no Component field for a reading to set (reading_fields cannot express the sub-basin limit); per-reading sign cell",
    "C-34": "missing role: OC-4 prevented exchanges are signed for pumpers and growers.nuts only; growers.field, farm_workers and buyers.crops have no roles",
    "C-35": "missing rule: OC-3 with CR-8b for the enforcer's receipts from fees (K4, K5)",
    "C-36": "missing rule: CR-8b for the enforcer's receipts from penalties; the evasion question is about trade not caught",
    "C-37": "missing rule: EN-13 signs the lease price and consolidation but not the quantity of rights leased out by lessors (quantity_traded increase); no lessor role",
    "C-38": "missing rule: CR-8b for the lease receipts of the lessors (EN-6 Unless signs the lease price only); no lessor role",
    "C-39": "missing rule and combiner: CR-12b over lease receipts, fees and lost crop receipts",
    "C-40": "missing rule: CR-8b/CR-3 for the lease payments of the buyers; EN-6 signs the buyers' resources only when price_paid is signed (price_effect_material is below the cut-off)",
    "C-41": "missing rule and combiner: as C-40 with CR-9 shared_facility, CR-12e",
    "C-43": "missing record fact and rule: CR-9 for the sellers of meters; section 1 does not name them as a related market, and `related` is not read for quotas",
    "C-44": "missing record fact and rule: CR-7b for local input dealers; as C-20",
    "C-45": "missing rule and record fact: CR-9, CR-4c for other districts' buyers of surface water; as C-15",
    "C-46": "missing rule and record fact: CR-9 after a shared_facility link (well drillers), Tier C",
    "C-47": "unsupported form: the capped quantity is signed as quantity_traded (EN-6), the table has quantity_supplied; also CR-12 split of the Tier B sign",
    "C-48": "missing rule and record fact: EN-6 Inputs clause for the long run, CR-12e; as C-6",
    "C-49": "missing rule and combiner: CR-9 shared_facility, CR-10b, CR-12b",
    "C-50": "missing record fact and rule: EN-6 Inputs clause for field crops; as C-5",
    "C-51": "same as C-49",
    "C-53": "same as C-49 (farm workers, Tier C)",
    "C-54": "missing record fact, rule and combiner: as C-5 with CR-9 shared_facility and CR-12e",
    "C-55": "same as C-54 for tree nuts",
    "C-56": "same as C-54 for South",
    "C-57": "missing rule: CR-6 for the full cost per unit of the capped input (the lease price is a cost of each af); not encoded for quotas",
    "C-58": "missing rule and role: CR-1 with CR-7c for land without history (landholders.no_history.small); K2 and K3 have no rules",
    "C-59": "same as C-58 with the Tier C aquifer chain and CR-12e",
    "C-60": "missing rule and record fact: resource_stock of a shared facility (CR-9 shared_facility, CR-8), Tier C",
}
PRODUCED = {"C-2", "C-19", "C-30", "C-42", "C-52"}


def test_consistent_with_worked_example_we039():
    pred, keys = _engine(WE39)
    rows = _rows("WE-039_groundwater_pumping_allocation.md", SHORT, WINDOWS, {})
    assert len(rows) == 60
    _check(rows, keys, EXCEPTIONS, NOT_PRODUCED, PRODUCED)
    # the base period ended before the plan was proposed: EN-12's windfall branch, so no race (no announcement-window row)
    assert not any(c["window"] for c in pred["consequences"])
    assert ("landholders.history", "asset_value", "increase", None) in keys
    # EN-6 Unless: the water has no price of its own, the lease price rations it; the holders' net price received is not signed
    assert ("landholders.history", "net_price_received", "increase", None) not in keys
    # A-19 (p = 0.3) is below the cut-off: the national price effect is noted, not reported
    assert ("growers.nuts", "price_paid", "increase", None) not in keys
    # the example has the enforcement cost as Tier A (no assumption); the engine gates it on binding and enforced (Tier B)
    by = {(c["actor_class"], c["variable"]): c for c in pred["consequences"]}
    assert by[("officials.enforcement", "enforcement_cost")]["tier"] == "B"
