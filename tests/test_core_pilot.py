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
WE001_NOT_PRODUCED = {
    "C-17": "CR-10 (renewals brought into the announcement window) is not in the pilot",
    "C-21": "CR-12: the first-months total of C-1 against C-17 needs the CR-10 chain and a declared comparison",
}
WE001_EXTRA = {
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
}


def test_we001_from_the_core_rules_alone():
    rows = _rows("WE-001_rent_freeze.md", WE001_SHORT, {}, {"converted buildings": ".converted"})
    produced, extra = _score(rows, _keys("we001_riverton"))
    assert set(rows) - produced == set(WE001_NOT_PRODUCED)
    assert len(produced) == 28 and len(rows) == 30
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
    rows = _rows("WE-005_gasoline_price_cap.md", WE005_BLIND_SHORT, {}, {})
    produced, _ = _score(rows, _keys("we005_corvane"))
    assert produced == {"C-1", "C-2", "C-4", "C-5", "C-6", "C-9", "C-15", "C-16", "C-18", "C-20", "C-21", "C-26"}
    rows = _rows("WE-008_milk_price_floor.md", WE008_BLIND_SHORT, {}, {})
    produced, _ = _score(rows, _keys("we008_velmora"))
    assert produced == {"C-1", "C-6", "C-9", "C-10", "C-12", "C-13", "C-18", "C-22", "C-23"}
