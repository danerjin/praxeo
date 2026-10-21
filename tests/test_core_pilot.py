"""Core-rule pilot: WE-001 and WE-009 derived from the core rules alone (praxeo/core/core.lp), with no pattern file
loaded, from a situation record in CR-1's terms (cases/<case>/situation.json). Scored against the handbook tables with
the same harness as the pattern engine's tests. The pilot report is PILOT_CORE_RULES.md.
"""
from pathlib import Path

from praxeo.core import situation as S
from test_out_of_sample import _rows

ROOT = Path(__file__).resolve().parents[1]


def _keys(case: str) -> set:
    cons = S.run(S.load(ROOT / "cases" / case / "situation.json"))
    return {(a, v, c.sign, c.window) for c in cons if c.reported for a in (c.actor_group or [c.actor_class])
            for v in (c.group or [c.variable])}


def _score(rows, keys):
    table = set().union(*rows.values())
    produced = {rid for rid, ks in rows.items() if ks & keys}
    return produced, sorted(k for k in keys if k not in table)


WE001_SHORT = {"landlords": "landlords.controlled", "tenants": "tenants.controlled"}
WE001_NOT_PRODUCED: dict = {}   # C-21 came with CR-12h (the first months: the price set before the line against the line)
WE001_EXTRA = {
    ("landlords.controlled", "net_price_received", "increase", "announcement"): "CR-10a: the landlords' side of C-17 (rents raised at renewal before the freeze)",
    ("landlords.controlled", "net_price_received", "ambiguous", "first_months"): "CR-12h: the landlords' side of C-21",
    ("landlords.controlled", "lobbying_effort", "increase", None): "C-11 names landlords (mapped); kept as a key the table has",
    ("tenants.prospective", "wait_time", "at_least_one_increase", None): "CR-6's group over the criteria; the table signs three members alone (C-3, C-4, C-7)",
    ("tenants.prospective", "search_cost", "at_least_one_increase", None): "member of the CR-6 group (see above)",
    ("tenants.prospective", "side_payments", "at_least_one_increase", None): "member of the CR-6 group (see above)",
    ("tenants.prospective", "allocation_by_non_price_criteria", "at_least_one_increase", None): "member of the CR-6 group (see above)",
}

WE009_SHORT = {"unions": "workers.adult_low_wage"}
WE009_EXTRA = {
    ("employers.low_wage", "quantity_traded", "decrease", None): "CR-5a on the burdened side: hires prevented at the floor; the table records them in the group C-3",
    ("workers.prospective", "quantity_traded", "decrease", None): "CR-5a on the unsatisfied side; the table records it as excess supply (C-5)",
    ("employers.low_wage", "resources_available_other_uses", "decrease", None): "CR-8c: what employers spend on complying (records, the youth-rate checks) is used up; the table records the compliance cost",
}


def test_we001_from_the_core_rules_alone():
    rows = _rows("WE-001_rent_freeze.md", WE001_SHORT, {"renewing before": "announcement", "first months": "first_months"},
                 {"converted buildings": ".converted"})
    produced, extra = _score(rows, _keys("we001_riverton"))
    assert set(rows) - produced == set(WE001_NOT_PRODUCED)
    assert len(produced) == 30 and len(rows) == 30   # 28 before CR-10a, 29 before CR-12h
    assert set(extra) <= set(WE001_EXTRA)


def test_we009_from_the_core_rules_alone():
    rows = _rows("WE-009_minimum_wage_youth_rate.md", WE009_SHORT, {}, {})
    produced, extra = _score(rows, _keys("we009_larrow"))
    assert produced == set(rows) and len(rows) == 19
    assert set(extra) <= set(WE009_EXTRA)


def test_the_core_rules_name_no_instrument():
    text = (ROOT / "praxeo" / "core" / "core.lp").read_text()
    code = "\n".join(l.split("%")[0] for l in text.splitlines())
    for word in ("ceiling", "floor", "tax", "tariff", "subsidy", "license", "quota", "mandate", "rent", "wage"):
        assert word not in code, word


# Blind runs: situation records written by a subagent from section 1 of the example and the assumption statements only,
# without the analysis or the consequence list. Actor names are mapped to the table's names only where they denote the
# same class (no class is merged into another).
WE005_BLIND_SHORT = {"drivers.served": "drivers.current", "stations": "stations.retail",
                     "drivers": ["drivers.current", "drivers.unserved"], "suppliers": "refiners.corvane"}
WE008_BLIND_SHORT = {"farmers.prospective": "farmers.entrants", "farmers.neighbors": "farmers.neighboring",
                     "Dairy Board": "officials.enforcement"}


def test_blind_situation_records():
    # r2: the same writers added the facts CR-10a and the buyer of last resort can hold (12 and 9 rows before)
    rows = _rows("WE-005_gasoline_price_cap.md", WE005_BLIND_SHORT, {"Days 3–5": "announcement"}, {})
    produced, _ = _score(rows, _keys("we005_corvane"))
    assert produced == {"C-1", "C-2", "C-4", "C-5", "C-6", "C-9", "C-12", "C-15", "C-16", "C-18", "C-20", "C-21", "C-26"}
    rows = _rows("WE-008_milk_price_floor.md", WE008_BLIND_SHORT, {}, {})
    produced, _ = _score(rows, _keys("we008_velmora"))
    assert len(produced) == 11 and {"C-2", "C-20"} <= produced


def test_we013_a_charge_from_the_core_rules_alone():
    """CR-1 operation 3 (a payment attached to trading): the steel tariff, with no held price."""
    rows = _rows("WE-013_steel_tariff.md", {"owners of steel-using firms": "owners.steel_users"}, {"Jan–Mar": "announcement"}, {})
    produced, extra = _score(rows, _keys("we013_halvern"))
    assert set(rows) - produced == {"C-30"}   # CR-7a on other producers; C-8 came with CR-10a
    assert extra == []


def test_we002_and_we010_blind_charges():
    rows = _rows("WE-002_drinks_excise.md", {"buyers.lakeport": "buyers.households", "distributors": "distributors.registered",
                 "retailers": "retailers.lakeport", "retailers.neighbors": "retailers.neighboring", "town budget": "officials.town",
                 "officials.enforcement": "officials.revenue_dept", "approved providers": "providers.approved",
                 "families.preschool": "families.private_preschool"}, {}, {})
    produced, _ = _score(rows, _keys("we002_lakeport"))
    assert len(produced) == 9 and len(rows) == 26
    rows = _rows("WE-010_cigarette_tax_border.md", {"smokers": "smokers.marren", "stamping_agents": "wholesalers.stamping",
                 "border retailers": "retailers.border", "health groups": "health_groups",
                 "intermediaries.bootleggers": "intermediaries.smuggling", "intermediaries.smuggling_networks": "intermediaries.smuggling",
                 "retailers.neighbors": "sellers.neighboring", "factor_owners.specific": "factor_owners.border_sites"}, {}, {})
    produced, _ = _score(rows, _keys("we010_marren"))
    assert len(produced) == 16 and len(rows) == 33


def test_cr12_parts_and_dominance():
    """A class total combines its parts' chains (opposite: ambiguous); a dominance premise that holds settles the sign."""
    base = {"name": "t", "exchanges": [{"id": "e1", "buyer": "buyers.served", "seller": "sellers.s", "unsatisfied_buyer": "buyers.unserved"}],
            "held": [{"component": "k1", "exchange": "e1", "direction": "below", "premises": ["a1"]}],
            "alternatives": [{"component": "k1", "chooser": c, "actor": c, "variables": ["cross_border_purchases"], "premises": ["a2"]}
                             for c in ("buyers.served", "buyers.unserved")],
            "parts": [{"part": "buyers.served", "whole": "buyers.border"}, {"part": "buyers.unserved", "whole": "buyers.border"}],
            "assumptions": {"a1": {"text": "binds", "p": 0.9}, "a2": {"text": "can cross", "p": 0.8}, "a3": {"text": "the unserved dominate", "p": 0.7}}}
    by = lambda s: {(c.actor_class, c.variable): c.sign for c in S.run(S.Situation(**s)) if c.reported}
    got = by(base)
    assert got[("buyers.served", "cross_border_purchases")] == "decrease" and got[("buyers.unserved", "cross_border_purchases")] == "increase"
    assert got[("buyers.border", "cross_border_purchases")] == "ambiguous"
    dom = [{"actor": "buyers.border", "variable": "cross_border_purchases", "direction": "increase", "kind": "empirical", "premises": ["a3"]}]
    assert by({**base, "dominance": dom})[("buyers.border", "cross_border_purchases")] == "increase"
    base["assumptions"]["a3"]["p"] = 0.3
    assert ("buyers.border", "cross_border_purchases") not in by({**base, "dominance": dom})   # the settled sign rests on a3
