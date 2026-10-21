"""Out-of-sample check of the price-floor rules (praxeo/rules/floors.lp, written from WE-009) on WE-008, the raw milk floor
with state purchase of the surplus.

Same shape as test_oos_we018.py. The rules were not changed for this example: every engine consequence is a row of the
example's consequence list or sits in EXCEPTIONS with its reason (each classified "defensible" or "KNOWN WRONG"), and every
table row the engine does not produce sits in NOT_PRODUCED with its reason. The run is described in
cases/we008_velmora/out_of_sample.md.
"""
from pathlib import Path

from test_out_of_sample import _check, _engine, _rows

ROOT = Path(__file__).resolve().parents[1]
WE8 = ROOT / "cases" / "we008_velmora"

# the table's "Dairy Board" is the record's enforcer and outlay actor
SHORT = {"Dairy Board": "officials.enforcement"}
EXCEPTIONS = {
    ("plants.commodity", "legal_breach", "increase", None):
        "defensible: RS-3 with open_breach: false certification of origin is a breach within the legal market; the table records the same act as reclassification (C-11); after the rule changes",
    ("plants.commodity", "price_paid", "increase", None):
        "defensible: the floor raises the price every Velmora plant pays; the table gives it to the specialty plants (C-6), and section 5 says the commodity plants also pay $21 and recover it from the Board",
    ("officials.enforcement", "subsidy_outlay", "increase", None):
        "defensible: SB-9's outlay of the Board's purchases (K2 is treated as a per_unit_subsidy); the table records the cost as stocks (C-20), taxpayers' loss (C-22) and audits (C-23), not as a variable of its own",
    ("taxpayers", "resources_available_other_uses", "at_least_one_decrease", None):
        "defensible: OC-1 as a group (SB-9 outlay and OC-3 funding); the table gives taxpayers a plain decrease (C-22)",
    ("recipients.other_spending", "resources_available_other_uses", "at_least_one_decrease", None):
        "defensible: member of the OC-1 group; the table names taxpayers alone as payers (C-22)",
}
NOT_PRODUCED = {
    "C-2": "missing rule: the state's purchase (SB-2 for the Board's quantity_demanded) is not signed by the state_buys branch, which gives stocks and outlay only",
    "C-6": "role: a floor has one bound_actor; the record names commodity plants (C-10, C-13), so the specialty plants have no role",
    "C-7": "role and missing rule: no specialty-plant role; RS-14 for a floor is written for rivals who face the same floor (price rise), not for exempt rivals (quantity effect)",
    "C-8": "role: plants.market, who switch to out-of-state milk, are bound buyers too, but a floor has one bound_actor; substitute_seller_actor and mobile_buyer_actor name sellers and buyers of the output, not another bound class",
    "C-9": "missing rule: SB-2 with CR-9 for plants that expand to process the extra milk; the engine's TS-2 row says the opposite (see EXCEPTIONS)",
    "C-12": "missing rule: RS-4 widened (entry across the boundary, SB-5) with a prospective-sellers role",
    "C-14": "missing rule: SB-9's withdrawal of product into stocks raises the consumers' price; the engine's route to the same key is RS-14, gated off by rivals_bound (0.15, reported False)",
    "C-15": "missing rule and role: PC-8 for a floor (plants switch to neighbors' milk); no neighbor-seller role for a floor",
    "C-16": "missing rule and role: PC-8 and LW-4 for the neighbors' supply",
    "C-17": "missing rule: SB-3 for the input suppliers; input_supplier_actor is not a floor role",
    "C-19": "missing rule: SB-3 for land and labour kept in dairy (substitute uses)",
    "C-21": "missing rule: SB-9's disposal by donation displaces suppliers' sales",
    "C-22": "sign form: the engine signs OC-1 as a group (at_least_one_decrease over taxpayers and other spending), the table a plain decrease",
    "C-24": "missing rule: OC-4 for the quantity traded in the regional market when the Board withdraws product; floors.lp signs fewer units traded only where the state does not buy (fl_fewer)",
    "C-25": "combiner: ambiguous; no declared comparison, and the entry and neighbor-supply chains are not rules",
    "C-26": "combiner: ambiguous; no declared comparison, and SB-9's resale and PC-8 chains are not rules",
    "C-27": "missing rule: SB-3 with CR-9 for the farm labour group (employment, hours_worked at_least_one_increase)",
    "C-28": "missing rule: SB-8 and SB-9 for the food programs' freed budgets",
}
PRODUCED = {f"C-{i}" for i in range(1, 29)} - set(NOT_PRODUCED)


def test_consistent_with_worked_example_we008():
    pred, keys = _engine(WE8)
    rows = _rows("WE-008_milk_price_floor.md", SHORT, {}, {})
    assert len(rows) == 28
    _check(rows, keys, EXCEPTIONS, NOT_PRODUCED, PRODUCED)
