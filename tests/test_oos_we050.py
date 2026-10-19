"""Out-of-sample run of the prohibition rules (praxeo/rules/prohibition.lp) on WE-050, the end of sale of combustion cars.

The prohibition rules were written from WE-017 only. WE-050's handbook classification of the end-of-sale date is
`product_standard` (EN-14, which has no rules); the record uses `prohibition`, the nearest instrument with rules, for K1 and
K2, and `lump_sum_tax` (no rules) for the road charge K5. The run, the classification of every row and the general gaps are
in cases/we050_vessmark/out_of_sample.md.
"""
from pathlib import Path

from test_out_of_sample import _check, _engine, _rows

ROOT = Path(__file__).resolve().parents[1]
WE50 = ROOT / "cases" / "we050_vessmark"

# The record's bound role `importers` stands for the importers and dealers that K1 binds (the Act's section 3 binds both,
# and a component has one bound role), so the table's dealers are matched to it.
SHORT = {"dealers": "importers"}
WINDOWS = {"announcement window": "announcement"}
EXCEPTIONS = {
    ("buyers.new_combustion", "lobbying_effort", "increase", None):
        "RS-7 for the buyers; the table names the organized part of them, the motoring clubs, and the dealers and importers (C-18)",
    ("buyers.new_phev", "lobbying_effort", "increase", None):
        "RS-7 for the PHEV buyers; the table names the motoring clubs and the trade (C-18)",
    ("buyers.new_phev", "quantity_substitute", "increase", None):
        "RS-1: would-be PHEV buyers turn to BEVs and used cars; the table signs it for K1's buyers (C-5), not for K2's",
    ("buyers.new_phev", "quantity_demanded", "increase", "announcement"):
        "RS-8 for the 2038 date; the table keeps bunching inside the PHEV window as a path note (section 8, item 5) and signs C-8 instead",
    ("importers.used", "quantity_traded", "U1-a: decrease; U1-b: no_change", None):
        "the U1-a half is C-13; under U1-b the engine derives nothing where the table has an increase (RS-4 with A-20): an omission, not a contradiction",
    # produced and WRONG by the handbook
    ("buyers.new_combustion", "quantity_demanded", "increase", "announcement"):
        "KNOWN WRONG: RS-8's rush alone; the table's C-9 is ambiguous because the sellers' withdrawal of models (A-8) and the wait for pre-registered stock (A-29) run against it",
}
NOT_PRODUCED = {
    "C-3": "lump_sum_tax has no rules (TX-1 with CR-8b is not encoded for it): the road charge's loss to BEV owners",
    "C-4": "same: the charge's revenue to the general budget",
    "C-7": "needs a combiner over new cars plus imports (CR-12 with CR-12e) and a role for all buyers of new cars; none declared",
    "C-8": "RS-1 signs quantity_substitute on the bound buyers; PHEV purchases in 2035 to 2037 as a window of another class's quantity_traded are not encoded",
    "C-9": "RS-8's rush is encoded alone; the opposing chains (models withdrawn, A-8; wait for pre-registered stock, A-29) have no rule and no combiner",
    "C-10": "variety under a dated ban (CR-4, CR-10a) is not encoded",
    "C-11": "pre-registration of unsold stock (RS-8 with RS-5): the engine's run-down needs stocks_destroyed, the reverse case; and no dealers role",
    "C-12": "used imports before the date (RS-4, CR-7a, CR-7c): no rule for imports of the substitute durable good",
    "C-13": "the U1-b reading is silent: no rule signs rising imports of used cars when the used price rises (RS-4 with A-20)",
    "C-15": "EN-14 (a standard on new units, stock exempt) and CR-10b are not encoded; no owners.combustion role",
    "C-16": "same: scrapping falls as the cars are worth keeping (CR-10b, CR-12g)",
    "C-17": "same, combined over the two chains after 2040",
    "C-19": "EN-14 with CR-7c (revaluation of the durable stock held at enactment) is not encoded",
    "C-20": "EN-14 with RS-16 and CR-6: the price of used combustion cars of a given model is not encoded; no used-buyer role",
    "C-21": "same, the sellers' side (CR-8b)",
    "C-22": "same, after 2040 (CR-12b, TS-3)",
    "C-23": "RS-16 with CR-7c for used BEVs: not encoded",
    "C-24": "RS-12 (complements) needs related markets and target_qty, which a prohibition does not feed (relations.lp)",
    "C-25": "same: number of fuel stations",
    "C-26": "SB-4 with CR-7c for station businesses: not encoded for a ban",
    "C-27": "RS-6 with CR-9: station workers; no rule from a ban",
    "C-28": "RS-12 for charging: the complement of the substitute",
    "C-29": "CR-9 for repairs of the kept stock: not encoded",
    "C-30": "same, after 2040",
    "C-31": "RS-12: travel time to refuel; not encoded",
    "C-32": "TX-10 is encoded for a tax on the banned good itself (taxed_before); the fuel excise is a tax on a complement",
    "C-33": "combiner: fuel excise against the road charge; no declared comparison, and the charge is not encoded",
    "C-34": "dealers' pre-registration cost (CR-8c, OC-2): not encoded for a ban",
    "C-36": "OC-3's fixed-budget case (group of the Registry's other users) is not encoded",
    "C-37": "CR-8c for the import inspection under the readings: not encoded",
    "C-38": "CR-6 for a price that does not change (new BEVs, constant cost, A-5) is not encoded; the engine does not derive no_change",
    "C-39": "RS-8, TS-10 and CR-10a over 2026 to 2032 with CR-7c: not encoded",
    "C-40": "RS-8 for the substitute's purchases before the date: not encoded; no buyers.new_bev role",
    "C-41": "CR-7 with CR-7c for dealers' stock at the date: no dealers role; the run-down rule is for destroyed stocks",
    "C-42": "RS-13 with EN-6 for the wider market (Drevland's used price): the prohibition rules have no wider-market clause",
    "C-43": "CR-6 for the inspection queue under U1-b: not encoded",
    "C-44": "CR-9 for mechanics of the kept stock: not encoded",
    "C-45": "same, after 2040",
    "C-46": "CR-7c for repair businesses: not encoded",
    "C-47": "RS-16 with CR-6 for used BEVs' price: not encoded",
    "C-48": "EN-14 with CR-10b (the fleet ages): not encoded",
}
PRODUCED = {"C-1", "C-2", "C-5", "C-14", "C-18", "C-35"}


def test_out_of_sample_we050():
    pred, keys = _engine(WE50)
    rows = _rows("WE-050_combustion_car_sales_ban.md", SHORT, WINDOWS, {})
    assert len(rows) == 47
    _check(rows, keys, EXCEPTIONS, NOT_PRODUCED, PRODUCED)
    assert len(PRODUCED) == 6 and len(NOT_PRODUCED) == 41
    assert sum(1 for v in EXCEPTIONS.values() if v.startswith("KNOWN WRONG")) == 1   # 4 in the first run; three fixed (the risk price needs an informal trade; fewer sellers needs no_other_use)
    # the road charge (lump_sum_tax) yields nothing, and K1's and K2's readings differ only for the used importers
    assert not any(k[0] == "owners.bev" for k in keys)
    assert {c["actor_class"] for c in pred["consequences"] if c["sign_by_reading"]} == {"importers.used"}
