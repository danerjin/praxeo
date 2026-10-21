"""Out-of-sample check of the prohibition rules (praxeo/rules/prohibition.lp, written from WE-017) on WE-018, the plastic bag ban.

Same shape as test_prohibition.py::test_consistent_with_worked_example_we017. The rules were not changed for this example:
every engine consequence is a row of the example's consequence list or sits in EXCEPTIONS with its reason, and every table
row the engine does not produce sits in NOT_PRODUCED with its reason. The run is described in
cases/we018_brennick/out_of_sample.md. K2, the paper-bag charge, is also read by the price-floor rules
(floors.lp, commit 5944604; the K2 role fields are in record.json); the section of the report on the floor rules describes that run.
"""
from pathlib import Path

from test_out_of_sample import _check, _engine, _rows

ROOT = Path(__file__).resolve().parents[1]
WE18 = ROOT / "cases" / "we018_brennick"

# the table's "retailers" (C-11, lobbying) is the record's bound sellers
SHORT = {"retailers": "retailers.brennick"}
WINDOWS = {"announcement window": "announcement"}
EXCEPTIONS = {
    ("retailers.brennick", "informal_activity", "increase", None):
        "defensible: RS-3 on the floor's complier (the retailers who must charge it); C-8 names the small retailers, a subclass; after the rule changes",
    ("retailers.small", "reclassification", "increase", None):
        "defensible: RS-5 signs reclassification on the record's informal-seller role; the table puts it on retailers.brennick (C-7), who sell the thick bags",
    ("sellers.substitutes", "reclassification", "increase", None):
        "defensible: section 8 has bag makers designing cheap bags that just meet the 4 mil and 125-use line; the table lists only the retailers' sales (C-7)",
    ("retailers.brennick", "excess_supply", "increase", None):
        "defensible: PC-9 on the sellers' side of K2 (binding and cost_not_offset); the example lists no surplus of bags, but at 10 cents against a cost of a few cents retailers would sell more paper bags than shoppers take",
    ("taxpayers", "resources_available_other_uses", "at_least_one_decrease", None):
        "OC-1 (who pays) as a group; the table gives taxpayers alone a plain decrease (C-19)",
    ("taxpayers.future", "resources_available_other_uses", "at_least_one_decrease", None):
        "member of the OC-1 group; the table assumes a budget that rises with the task, so the cost falls on current taxpayers (C-19)",
    ("recipients.other_spending", "resources_available_other_uses", "at_least_one_decrease", None):
        "member of the OC-1 group; the table assumes a budget that rises with the task (C-19)",
}
NOT_PRODUCED = {
    "C-4": "missing record fact: the household class and the secondary_use relation to bin liners; RS-1 is applied to the buyers of the banned good only",
    "C-7": "role: RS-5 signs reclassification on the informal-seller and substitute-seller roles, not on the bound sellers who sell the thick bags",
    "C-8": "role: the floor's RS-3 (evasion, A-5) signs informal_activity on the complier, retailers.brennick (after the floor fixes); the table names the small stores that waive the fee; the prohibition's RS-3 is a hidden market gated on demand_persists (0.2)",
    "C-13": "missing record fact and rule: Brennick edge stores have no role; the mirror of the neighbours' gain (RS-4 with RS-9) is not encoded",
    "C-14": "missing rule: OC-5 (staffing follows sales), and no edge-store role",
    "C-15": "combiner: retailers' resources, (+) bag savings against (-) compliance and lost sales; no declared comparison (CR-8b, CR-8c, CR-12b)",
    "C-16": "combiner and missing rule: RS-14 pass-through of compliance costs and bag savings to shelf prices; no declared comparison",
    "C-17": "missing rule: OC-1 for the buyers' spending on paper-bag fees and reusable bags (K2 and RS-1)",
    "C-18": "missing record fact: the household class; RS-1 spending on liners",
    "C-19": "sign form: the engine signs OC-1 as a group (at_least_one_decrease over taxpayers, future taxpayers, other spending), the table a plain decrease",
    "C-20": "missing rule: OC-5 and the neighbours' staffing; Fallow Creek mirror of C-14",
}
PRODUCED = {f"C-{i}" for i in range(1, 23)} - set(NOT_PRODUCED)


def test_consistent_with_worked_example_we018():
    pred, keys = _engine(WE18)
    rows = _rows("WE-018_plastic_bag_ban.md", SHORT, WINDOWS, {})
    assert len(rows) == 22
    _check(rows, keys, EXCEPTIONS, NOT_PRODUCED, PRODUCED)
    assert len(PRODUCED) == 11  # 10 after the floor run; C-5 after the floor fixes (the complier role)
    # KNOWN WRONG and masked by a key of the table: K2's PC-9 "fewer units traded" (fl_fewer) is merged into the consequence of
    # K1 with the same key (shoppers and retailers.brennick quantity_traded decrease, C-1, thin bags). For the paper bags the
    # example says the opposite: they are bought more (C-3, C-21), and paper use stays above the counterfactual (section 8).
    derived = {(c["actor_class"], c["variable"]): {d["conclusion"] for d in c["derivation"]} for c in pred["consequences"] if c["reported"]}
    for actor in ("shoppers", "retailers.brennick"):
        assert "fl_fewer(k2)" in derived[(actor, "quantity_traded")]
    known_wrong = {k for k, v in EXCEPTIONS.items() if v.startswith("KNOWN WRONG")}
    assert known_wrong == set()  # 2 after the floor run (OC-2 and RS-3 on the shoppers); gone with the complier role
