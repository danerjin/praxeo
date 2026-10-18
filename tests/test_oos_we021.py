"""Out-of-sample run of the subsidy rules (praxeo/rules/subsidies.lp, developed on WE-019 only) on WE-021.

Same shape as tests/test_subsidies.py::test_consistent_with_worked_example_we019: every reported engine consequence is a row
of the example's consequence list (key: actor class, variable, sign, window; a group gives one key per member) or sits in
EXCEPTIONS with its reason; every table row the engine does not produce sits in NOT_PRODUCED with its reason. The rules and
the record schema were not changed for this run (see cases/we021_calvera/out_of_sample.md).
"""
from pathlib import Path

from test_out_of_sample import _check, _engine, _rows

ROOT = Path(__file__).resolve().parents[1]
WE21 = ROOT / "cases" / "we021_calvera"

# the table's actor names are the record's role names
SHORT: dict = {}
# C-10 is the September to December dip before the start; C-18 and C-32 are after the program ends. C-8 (sales before each
# step-down) would otherwise have the key of C-2's buyers' side, which the engine produces for another reason, so it gets a
# window of its own that no engine consequence has
WINDOWS = {"September to December": "announcement", "after program ends": "after_expiry",
           "before step-downs": "before_step_down"}
EXCEPTIONS = {
    ('officials.enforcement', 'subsidy_outlay', 'increase', None):
        "SB-1 with CR-8b (the receipt side, added after the out-of-sample runs): the paying agency's outlay; the example records the funders, not the outlay",
    ('buyers.commercial_solar', 'resources_available_other_uses', 'decrease', None):
        "CR-8b with OC-1: the excluded commercial buyers' higher price (C-28, C-29) is lost to their other uses; not in the table",
    ("electricians", "quantity_traded", "increase", None):
        "CR-9 (related input, `related`): installers hire more electrical work as installations rise; the table records the "
        "labour side as the installers' workers (C-31) and the electricians' wage (C-13)",
    ("buyers.adopters", "quantity_traded", "increase", None):
        "SB-2: the buyers' side of C-2 (an exchange has two sides); the table signs the installers' side only (C-8 is the pre-step-down surge)",
    ("installers", "reclassification", "increase", None):
        "SB-5 with RS-5 where the criteria bind the installers (K3 certification; `qualifier_actor`, added after the first run, "
        "which put the row on the recipients); the table records the installers' response as entry (C-6), not as reshaping",
    ("customers.electricity", "quantity_substitute", "increase", None):
        "TX-3 with RS-1: customers turn to untaxed own generation; the table covers only adopters' fall in grid purchases (C-16, A-10) "
        "and says the priced-out purchases are too few for an entry (A-3)",
    ("officials.enforcement", "tax_revenue_vs_static_projection", "decrease", None):
        "TX-9: the revenue falls short of the static projection because the quantity falls (quantity_responds); not in the table, "
        "which has the fund's receipt only (C-24)",
}
NOT_PRODUCED = {
    "C-6": "missing rule: the entry of installers drawn by the higher price (SB-3, LW-4); no question for A-5 on the sellers' side",
    "C-7": "missing record fact and rule: the per-building limit (10 kW) has no field, and CR-4 for the size of a unit is not encoded for subsidies",
    "C-8": "missing record fact and rule: the tiered payment that steps down with funded capacity (RS-8 is encoded for the announcement window only)",
    "C-9": "same as C-8 (backlogs at the thresholds); PC-2's group for the capped budget is not signed here (oversubscribed answered 0.45)",
    "C-11": "missing record fact: the text does not say the subsidy may be renewed (renewable false); panel suppliers and large users have no role",
    "C-12": "missing record fact (no role for the taxpayers who receive no payment) and rule (RS-1 with CR-1: the tax share borne by non-recipients)",
    "C-14": "missing record fact (the rule is now encoded, `related` with other_user_actor): the text does not name the other users of electrical work; buyers of the competing use of the scarce factor (other electrical work) have no role",
    "C-17": "combiner: the ambiguous total of the + chain (PC-15) and the - chain (RS-13) is not a declared CR-12 comparison; neither rule is encoded, and non-adopters have no role",
    "C-20": "same as C-14",
    "C-22": "combiner: DM-3 (entrants' earnings over the surge and the end) is not a declared comparison",
    "C-27": "missing record fact: the text names no asset in slow supply for the installers' businesses (asset_owner_actor), so SB-4 is not asked",
    "C-30": "missing record fact and rule: wholesale generators have no role, and RS-13 (lower midday wholesale price) is not encoded",
    "C-31": "missing record fact and rule: no worker role for subsidies and no LW-4 rule for the subsidized sellers' labor (CR-9, CR-7)",
    "C-32": "same as C-31, with SB-6 for the fall after the program",
}
PRODUCED = {"C-1", "C-2", "C-3", "C-4", "C-5", "C-10", "C-13", "C-15", "C-16", "C-18", "C-19", "C-21", "C-23", "C-24", "C-25", "C-26", "C-28", "C-29", "C-33"}


def test_consistent_with_worked_example_we021():
    pred, keys = _engine(WE21)
    rows = _rows("WE-021_solar_panel_subsidy.md", SHORT, WINDOWS, {})
    assert len(rows) == 33
    _check(rows, keys, EXCEPTIONS, NOT_PRODUCED, PRODUCED)
    by = {(c["actor_class"], c["variable"], c["window"], c["item"]): c for c in pred["consequences"]}
    # the funding is the surcharge itself (own revenue): SB-1 names no taxpayer, so C-4 comes from the tax rules (TX-1, TX-2)
    assert by[("customers.electricity", "resources_available_other_uses", None, None)]["tier"] == "A"
    assert not any(d["rule"] == "SB-1" for d in by[("customers.electricity", "resources_available_other_uses", None, None)]["derivation"])
    # the claims cost, the administration and the collection cost are Tier A (C-25, C-19, C-26)
    assert {by[k]["tier"] for k in [("installers", "compliance_cost", None, None), ("officials.enforcement", "enforcement_cost", None, None),
                                    ("utilities", "compliance_cost", None, None)]} == {"A"}
    # the announcement dip (C-10) and the dip after the program (C-18)
    assert by[("buyers.adopters", "quantity_traded", "announcement", None)]["horizon"] == ["short"]
    assert by[("installers", "quantity_traded", "after_expiry", None)]["sign"] == "decrease"
    # the first run's WRONG row: the price after expiry now rests on supply at that date (supply_slow_at_expiry, judged low
    # from A-4 and A-5), not on supply at the start
    assert not by[("installers", "net_price_received", "after_expiry", None)]["reported"]
