"""Step 4 of the core layer: the expand-as-you-go loop (praxeo/core/expand.py). Given the same facts, the loop must give the
one-shot result while asking only about actors the reasoning reaches; a file-driven run stops and lists what it needs."""
import json
from pathlib import Path

import pytest

from praxeo.core import expand as X
from praxeo.core import situation as S

ROOT = Path(__file__).resolve().parents[1]


def _key(cons):
    return {(c.actor_class, c.variable, c.sign, c.window, tuple(c.group)) for c in cons if c.reported}


@pytest.mark.parametrize("case", ["we001_riverton", "we009_larrow", "we013_halvern"])
def test_the_loop_reproduces_the_one_shot_record(case, tmp_path):
    full = S.load(ROOT / "cases" / case / "situation.json")
    seed, props = X.split(full)
    (tmp_path / "p.json").write_text(json.dumps(props))
    run = X.expand(seed, X.FixtureProposer(tmp_path / "p.json"), X.TextDecider({v["text"]: v["p"] for v in full.assumptions.values()}))
    assert _key(S.run(run.situation)) == _key(S.run(full))
    asked = {e["node"] for e in run.log}
    assert set(props) <= asked                       # every proposing actor was reached
    assert run.rounds <= X.MAX_DEPTH


def test_a_file_driven_run_lists_what_it_needs(tmp_path):
    full = S.load(ROOT / "cases" / "we009_larrow" / "situation.json")
    seed, props = X.split(full)
    prop, dec = X.FileProposer(tmp_path / "none.json"), X.FileDecider(tmp_path / "none.json")
    X.expand(seed, prop, dec)
    assert {n.actor for n in prop.missing} >= {"employers.low_wage", "workers.adult_low_wage"}   # the first round's nodes
    assert all(n.depth == 1 for n in prop.missing)   # nothing deeper is reached without their facts


def _loop_score(case, example, short, windows=None, loop="loop"):
    from test_out_of_sample import _rows
    cons = S.run(S.load(ROOT / "cases" / case / loop / "situation.json"))
    keys = {(a, v, c.sign, c.window) for c in cons if c.reported for a in (c.actor_group or [c.actor_class]) for v in (c.group or [c.variable])}
    rows = _rows(example, short, windows or {}, {})
    return {r for r, ks in rows.items() if ks & keys}, len(rows)


def test_blind_loop_runs():
    """Blind: a stand-in for the LLM proposer and the decider wrote the seed and answered the loop node by node from the
    policy section and the assumption statements only (cases/<case>/loop/notes.md). Names mapped only where the class is
    the same."""
    produced, n = _loop_score("we006_coralia", "WE-006_price_gouging_law.md",
                              {"buyers.served": "buyers.local", "residents.declared": ["buyers.unserved", "guests.unserved"],
                               "hotels.declared": "sellers.lodging", "evacuees.in_rooms": "guests.local",
                               "repair_contractors.outside": "sellers.repair_outside"})
    assert (len(produced), n) == (17, 26)          # pattern engine: 15 after its fixes
    produced, n = _loop_score("we062_saldria", "WE-062_plastic_packaging_tax.md",
                              {"state budget": "officials.enforcement", "converters": "converters.domestic",
                               "sellers.foreign": ["converters.foreign", "sellers.foreign.packaged_goods"],
                               "recyclers": "recyclers.domestic", "buyers.packaged_goods": "consumers.packaged_goods",
                               "exporters": "exporters.packaged_goods", "converter_workers": "workers.converters",
                               "recycler_workers": "workers.recyclers", "workers of sellers.substitutes": "workers.substitute_makers",
                               "sellers.substitutes": "sellers.substitute_packaging", "converters.owners": "owners.converters",
                               "importers.packaged_goods": "importers.goods",
                               "small_importers": ["importers.small_goods", "importers.small_packaging"], "taxpayers.other": "taxpayers"})
    assert (len(produced), n) == (26, 68)          # pattern engine: 12 after its fixes; 23 before r2 and the response argument


def test_blind_loop_runs_on_the_remaining_families():
    """Blind runs after the grant, expiry, cap, ban and in-kind-charge operations (one per family). Counts are of table rows
    produced by key; names mapped only where the class is the same (cases/<case>/loop/notes.md has the records' choices)."""
    cases = [
        ("we020_tamberlay", "WE-020_first_time_buyer_grant.md",
         {"owners.entry_level": ["owners.entry_level_homes", "sellers.entry_level_homes"],
          "owners": ["owners.entry_level_homes", "sellers.entry_level_homes"], "buyers.other": "buyers.ineligible",
          "builders": "developers", "intermediaries": "agents.real_estate", "construction_labor": "workers.construction"},
         {"March to June": "announcement", "before end of Year 4": "deadline"}, 13, 33),     # pattern engine 15
        ("we016_arvane", "WE-016_interior_designer_license.md",
         {"clients.residential": "clients.design", "clients.commercial": ["clients.design", "applicants.permit"],
          "clients": "clients.design", "designers.recent": "designers.unlicensed", "designers.prospective": "students.interior_design",
          "designers": ["designers.licensed", "designers.grandfathered", "designers.unlicensed"],
          "schools.design": "schools.design_programs", "retailers.furniture": "retailers.furnishings",
          "officials.enforcement": "officials.board"},
         {"announcement window": "announcement", "first months": "first_months"}, 8, 36),      # pattern engine 16
        ("we028_kallmark", "WE-028_fishing_quota_shares.md",
         {"vessel_owners.history": "vessel_owners", "share_recipients": "vessel_owners", "all vessels fishing ridge cod": "vessel_owners",
          "crew": "crew.ridge_cod", "processors": "processors.ridge_cod", "buyers.fresh_domestic": "buyers.fresh_fish",
          "buyers.regional": "buyers.north_basin", "share_buyers.later": "vessel_owners.acquiring",
          "recipients of other public spending": "recipients.other_spending"},
         {"2026–2027": "announcement"}, 18, 54),     # pattern engine 16 (8 out of sample)
        ("we018_brennick", "WE-018_plastic_bag_ban.md", {"retailers": "retailers.brennick", "shoppers": "shoppers.brennick"},
         {"announcement window": "announcement"}, 10, 22),     # pattern engine 11; 9 before CR-8c on compliers
        ("we036_quenby", "WE-036_employer_health_cover_mandate.md",
         {"insurers": "insurers.health", "unions": "workers.full_time_bound", "workers.uncovered": "workers.full_time_bound",
          "workers.min_wage": "workers.minimum_wage_bound", "workers.full_time": "workers.full_time_bound",
          "general_fund": ["officials.enforcement", "officials.indigent_care"], "insurers.group": "insurers.health",
          "insurers.individual": "insurers.individual_market", "employers.small": "employers.unbound",
          "sellers.contract_services": "employers.staffing", "neighboring_jurisdictions": "sellers.foreign",
          "providers.medical": "hospitals.providers", "recipients of other general-fund spending": "recipients.other_spending"},
         {}, 13, 60),     # pattern engine 29
    ]
    for case, example, short, windows, k, n in cases:
        produced, total = _loop_score(case, example, short, windows)
        assert (case, len(produced), total) == (case, k, n)


def test_blind_loop_runs_after_the_family_forms():
    """Second blind runs (loop_r2, written without sight of the first) after per-seller charges, charge branches, capped
    payers, thresholds, races to qualify and the deadline window; WE-055 is a first run. The WE-028 r2 and WE-055 writers
    each saw part of the example beyond what was allowed (row starts; the closing check paragraph) and say so in notes.md."""
    cases = [
        ("we016_arvane", "loop_r2", "WE-016_interior_designer_license.md",
         {"designers.recent": "designers.unlicensed", "designers": ["designers.arvane", "designers.grandfathered", "designers.unlicensed"],
          "retailers.furniture": "retailers.furnishings", "officials.enforcement": "board.interior_design", "architects": "architects.arvane"},
         {"announcement window": "announcement", "first months": "first_months"}, 14, 36),       # r1 8; pattern engine 16
        ("we036_quenby", "loop_r2", "WE-036_employer_health_cover_mandate.md",
         {"insurers": "insurers.health", "workers.uncovered": "workers.full_time", "employers.near_50": "employers.near_threshold",
          "workers.near_30": "workers.near_hours_line", "insurers.group": "insurers.health", "employers.small": "employers.unbound",
          "providers.medical": "providers.health", "employers.tradable": "producers.tradable", "general_fund": "officials.enforcement"},
         {}, 18, 60),                                                                              # r1 13; pattern engine 29
        ("we028_kallmark", "loop_r2", "WE-028_fishing_quota_shares.md",
         {"vessel_owners.history": "vessel_owners", "all vessels fishing ridge cod": "vessel_owners", "share_buyers.later": "share_buyers",
          "entrants.prospective": "vessel_owners.prospective_entrants", "recipients of other public spending": "recipients.other_spending"},
         {"2026–2027": "announcement"}, 19, 54),                                                   # r1 18; pattern engine 16
        ("we055_aldenmoor", "loop", "WE-055_home_inspector_licensing.md",
         {"inspectors": ["inspectors.licensed", "inspectors.unlicensed", "inspectors.entrant"], "buyers.current": "buyers.homebuyers",
          "inspectors.prospective": "inspectors.entrant", "inspectors.near_line": "inspectors.nearline", "training_schools": "schools.training",
          "agents": "agents.realestate", "insurers": "insurers.liability", "officials.enforcement": "officials.board",
          "unlicensed inspectors": "inspectors.unlicensed"},
         {}, 11, 37),                                                                              # pattern engine 8
    ]
    for case, loop, example, short, windows, k, n in cases:
        produced, total = _loop_score(case, example, short, windows, loop)
        assert (case, len(produced), total) == (case, k, n)
