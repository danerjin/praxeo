"""Out-of-sample check of the prohibition rules (praxeo/rules/prohibition.lp, written from WE-017) on WE-018, the plastic bag ban.

Same shape as test_prohibition.py::test_consistent_with_worked_example_we017. The rules were not changed for this example:
every engine consequence is a row of the example's consequence list or sits in EXCEPTIONS with its reason, and every table
row the engine does not produce sits in NOT_PRODUCED with its reason. The run is described in
cases/we018_brennick/out_of_sample.md.
"""
from pathlib import Path

from test_out_of_sample import _check, _engine, _rows

ROOT = Path(__file__).resolve().parents[1]
WE18 = ROOT / "cases" / "we018_brennick"

# the table's "retailers" (C-11, lobbying) is the record's bound sellers
SHORT = {"retailers": "retailers.brennick"}
WINDOWS = {"announcement window": "announcement"}
EXCEPTIONS = {
    ("retailers.small", "reclassification", "increase", None):
        "defensible: RS-5 signs reclassification on the record's informal-seller role; the table puts it on retailers.brennick (C-7), who sell the thick bags",
    ("sellers.substitutes", "reclassification", "increase", None):
        "defensible: section 8 has bag makers designing cheap bags that just meet the 4 mil and 125-use line; the table lists only the retailers' sales (C-7)",
    ("taxpayers", "resources_available_other_uses", "at_least_one_decrease", None):
        "OC-1 (who pays) as a group; the table gives taxpayers alone a plain decrease (C-19)",
    ("taxpayers.future", "resources_available_other_uses", "at_least_one_decrease", None):
        "member of the OC-1 group; the table assumes a budget that rises with the task, so the cost falls on current taxpayers (C-19)",
    ("recipients.other_spending", "resources_available_other_uses", "at_least_one_decrease", None):
        "member of the OC-1 group; the table assumes a budget that rises with the task (C-19)",
    ("retailers.brennick", "number_of_sellers", "decrease", None):
        "KNOWN WRONG: EN-7 reads a ban as driving legal sellers out; here the ban is on a free giveaway and every store keeps selling its goods",
    ("shoppers", "lobbying_effort", "increase", None):
        "KNOWN WRONG: RS-7 gives the banned good's buyers lobbying; the table has makers, substitute makers and retailers only (C-11), and shoppers have no concentrated stake in a 2-cent bag",
    ("shoppers.edge", "search_cost", "increase", None):
        "KNOWN WRONG: RS-4's crossing cost; section 9 says no separate travel cost is recorded, since edge shoppers find the other store about as convenient",
}
NOT_PRODUCED = {
    "C-2": "K2 is a price_floor, which has no rules; the engine's price_paid (the risk price) needs demand_persists, which is unreported at 0.2",
    "C-4": "missing record fact: the household class and the secondary_use relation to bin liners; RS-1 is applied to the buyers of the banned good only",
    "C-5": "missing rule: compliance cost of the bound sellers under a prohibition (CR-8c, Tier A)",
    "C-6": "unsupported form: K2, a price_floor, has no rule",
    "C-7": "role: RS-5 signs reclassification on the informal-seller and substitute-seller roles, not on the bound sellers who sell the thick bags",
    "C-8": "unsupported form: RS-3 is encoded as a hidden market gated on demand_persists (0.2); open non-compliance by small stores (A-5) is not that",
    "C-13": "missing record fact and rule: Brennick edge stores have no role; the mirror of the neighbours' gain (RS-4 with RS-9) is not encoded",
    "C-14": "missing rule: OC-5 (staffing follows sales), and no edge-store role",
    "C-15": "combiner: retailers' resources, (+) bag savings against (-) compliance and lost sales; no declared comparison (CR-8b, CR-8c, CR-12b)",
    "C-16": "combiner and missing rule: RS-14 pass-through of compliance costs and bag savings to shelf prices; no declared comparison",
    "C-17": "missing rule: OC-1 for the buyers' spending on paper-bag fees and reusable bags (K2 and RS-1)",
    "C-18": "missing record fact: the household class; RS-1 spending on liners",
    "C-19": "sign form: the engine signs OC-1 as a group (at_least_one_decrease over taxpayers, future taxpayers, other spending), the table a plain decrease",
    "C-20": "missing rule: OC-5 and the neighbours' staffing; Fallow Creek mirror of C-14",
    "C-21": "missing rule: CR-9 (input_to) for the paper-bag makers' sales",
}
PRODUCED = {f"C-{i}" for i in range(1, 23)} - set(NOT_PRODUCED)


def test_consistent_with_worked_example_we018():
    pred, keys = _engine(WE18)
    rows = _rows("WE-018_plastic_bag_ban.md", SHORT, WINDOWS, {})
    assert len(rows) == 22
    _check(rows, keys, EXCEPTIONS, NOT_PRODUCED, PRODUCED)
