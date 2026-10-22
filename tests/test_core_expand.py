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
    from test_out_of_sample import _rows, _sign
    cons = S.run(S.load(ROOT / "cases" / case / loop / "situation.json"))
    keys = {(a, v, _sign(c.model_dump()), c.window) for c in cons if c.reported for a in (c.actor_group or [c.actor_class]) for v in (c.group or [c.variable])}
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


def test_blind_loop_runs_on_mandates_after_fixed_prices_and_readings():
    """Blind mandate runs after fixed prices, unclear provisions and capped payers (a522291): a third WE-036 run and first runs
    on WE-031 and WE-059. All three writers report reading slips beyond section 1 (section headings, the closing check
    paragraph; on WE-059 the start of sections 2 and 3), recorded in their notes.md."""
    cases = [
        ("we036_quenby", "loop_r3", "WE-036_employer_health_cover_mandate.md",
         {"insurers": "insurers.health", "workers.uncovered": "workers.at_bound_firms", "workers.at_players": "workers.at_offering_firms",
          "workers.min_wage": "workers.at_bound_firms", "employers.near_50": "employers.near_line", "workers.near_30": "workers.near_30_hours",
          "insurers.group": "insurers.health", "employers.small": "employers.unbound", "sellers.contract_services": "employers.staffing",
          "general_fund": "officials.revenue"},
         {}, 17, 60),                                                                              # 16 before the in-kind receiver was a chooser; r2 18; pattern engine 29
        ("we031_westmere", "loop", "WE-031_building_energy_code.md",
         {"builders": "builders.homes", "officials.enforcement": "officials.building_departments",
          "owners.buildable_lots": "landowners.buildable_lots", "input_suppliers.efficiency": "makers.efficiency_products",
          "workers.residential_construction": "workers.construction", "taxpayers.current": "taxpayers"},
         {"announcement window": "announcement"}, 12, 47),                                         # pattern engine 9
        ("we059_kestrava", "loop", "WE-059_right_to_repair.md",
         {"lobbying groups": ["makers.ag", "makers.phone", "dealers.ag", "owners.ag"]}, {}, 9, 47),  # pattern engine 9
    ]
    for case, loop, example, short, windows, k, n in cases:
        produced, total = _loop_score(case, example, short, windows, loop)
        assert (case, len(produced), total) == (case, k, n)


def test_the_proposer_is_given_the_controlled_names():
    from praxeo import vocabulary as V
    text = X.vocabulary_text()
    assert all(f"- {v}:" in text for v in V.variables()) and "buyers.current" in text
    assert "controlled list" in X.PROPOSER_SYSTEM and "subclass" in X.PROPOSER_SYSTEM
    # a blind run on an example is not shown the names only that example's table supports
    assert set(V.actor_classes(exclude=("WE-036",))) <= set(V.actor_classes())


def test_off_list_names_are_flagged():
    sit = S.Situation(name="t", exchanges=[], assumptions={},
                      links=[{"source_actor": "buyers.current", "source_variable": "quantity_traded", "relation": "substitute",
                              "actor": "zzz.unknown", "variable": "homes_listed"}])
    msgs = X.off_list(sit)
    assert any("homes_listed" in m for m in msgs) and any("zzz" in m for m in msgs)


def test_blind_loop_runs_with_the_controlled_names():
    """Runs whose proposer was given the controlled names and the subclass guidance (10e031e), reading only extracted files
    (section 1 and the four allowed assumption columns), so without the reading slips of earlier runs."""
    cases = [
        ("we036_quenby", "loop_r4",
         {"workers.uncovered": ["workers.at_paying_firms", "workers.at_offering_firms"], "workers.at_players": "workers.at_offering_firms",
          "employers.players": "employers.offering", "employers.payers_midsize": "employers.paying",
          "employers.near_50": "employers.near_threshold", "workers.capped_firms": "workers.at_capped_firms",
          "general_fund": ["treasury", "officials.revenue"], "sellers.contract_services": "contractors", "insurers.group": "insurers"},
         {}, 19),
        ("we036_quenby", "loop_r5",
         {"workers.uncovered": "workers.fulltime_bound", "workers.at_players": "workers.at_offering_firms",
          "employers.near_50": "employers.near_threshold", "workers.near_30": "workers.near_hours_line",
          "workers.full_time": "workers.fulltime_bound", "insurers.group": "insurers", "general_fund": ["treasury", "officials.revenue"],
          "providers.medical": "sellers.health_care", "sellers.contract_services": "contractors"},
         {}, 21),     # runs 1 to 3 without the names: 13, 18, 16; pattern engine 29 (of 60)
        ("we020_tamberlay", "loop_r2",
         {"buyers.first_time": "homebuyers.first_time", "owners.entry_level": ["owners.under_cap", "sellers.entry_level"],
          "owners": ["owners.under_cap", "sellers.entry_level"], "buyers.other": "homebuyers.repeat",
          "construction_labor": "construction_workers", "taxpayers": "taxpayers.current"},
         {"March to June": "announcement", "before end of Year 4": "deadline"}, 16),   # r1 13; pattern engine 15 (of 33)
    ]
    examples = {"we036_quenby": "WE-036_employer_health_cover_mandate.md", "we020_tamberlay": "WE-020_first_time_buyer_grant.md"}
    for case, loop, short, windows, k in cases:
        produced, _ = _loop_score(case, examples[case], short, windows, loop)
        assert (case, loop, len(produced)) == (case, loop, k)


def test_blind_loop_runs_with_incidence_and_horizons():
    """Runs after incidence (CR-7b) and horizons on moves and fixed (86c9546), from extracted files only. WE-012 and WE-029
    were used to write the pattern rules (taxes, mandates), so the pattern engine's counts there are in sample."""
    cases = [
        ("we036_quenby", "loop_r6", "WE-036_employer_health_cover_mandate.md",
         {"workers.uncovered": ["workers.at_paying_firms", "workers.at_offering_firms"], "workers.at_players": "workers.at_offering_firms",
          "employers.players": "employers.offering", "employers.payers_midsize": "employers.paying",
          "employers.near_50": "employers.near_threshold", "workers.capped_firms": "workers.at_capped_firms",
          "workers.near_30": "workers.near_30_hours", "general_fund": ["treasury", "officials.revenue"],
          "sellers.contract_services": "contractors", "insurers.group": "insurers", "insurers.individual": "insurers.individual_market",
          "neighboring_jurisdictions": "producers.tarnley", "providers.medical": "sellers.hospital_care"},
         {}, 24),     # runs 1 to 5: 13, 18, 16, 19, 21; pattern engine 29 (of 60)
        ("we012_payroll", "loop", "WE-012_employer_payroll_tax.md",
         {"employers.formal": "employers.covered", "workers.formal": "workers.covered", "workers.below_ceiling": "workers.covered",
          "officials.enforcement": ["officials.enforcement", "officials.revenue"], "buyers.labor_intensive": "consumers",
          "government.general_budget": "general_fund"},
         {"announcement window": "announcement"}, 18),                                  # of 33
        ("we029_varrow", "loop", "WE-029_paid_sick_leave_mandate.md",
         {"employers.uncovered": "employers.covered", "associations": "employers.covered", "unions": "workers.uncovered",
          "neighboring_jurisdictions": "sellers.foreign", "employers.tradable": "producers.tradable",
          "buyers.local_services": "consumers"},
         {}, 18),                                                                       # of 42; pattern engine 40, in sample
    ]
    for case, loop, example, short, windows, k in cases:
        produced, _ = _loop_score(case, example, short, windows, loop)
        assert (case, loop, len(produced)) == (case, loop, k)


def test_blind_loop_runs_after_the_last_mandate_forms():
    """Runs after branch premise sets, link horizons, fund links and reading-tied exempt alternatives (7890e0e)."""
    cases = [
        ("we036_quenby", "loop_r7", "WE-036_employer_health_cover_mandate.md",
         {"workers.at_players": "workers.at_offering_firms", "employers.payers_midsize": "employers.mid_size",
          "employers.bound": ["employers.mid_size", "employers.capped"], "employers.near_50": "employers.near_threshold",
          "workers.capped_firms": "workers.at_capped_firms", "workers.near_30": "workers.near_hours_line",
          "general_fund": ["treasury", "officials.revenue", "officials.icp"],
          "sellers.contract_services": ["contractors", "intermediaries.staffing"], "insurers.group": "insurers",
          "employers.tradable": "producers.tradable", "neighboring_jurisdictions": "sellers.foreign", "providers.medical": "sellers.care"},
         {}, 26),     # runs 1 to 6: 13, 18, 16, 19, 21, 24; pattern engine 29 (of 60)
        ("we059_kestrava", "loop_r2", "WE-059_right_to_repair.md",
         {"owners.ag": "growers", "makers.ag": "manufacturers.farm", "makers.phone": ["manufacturers.phone", "manufacturers.phone_other"],
          "dealers.ag": "retailers.dealers", "independents": ["repair_shops.independent_farm", "repair_shops.independent_phone"],
          "authorized_providers.phone": "repair_shops.authorized_phone",
          "lobbying groups": ["manufacturers.farm", "manufacturers.phone", "retailers.dealers", "growers"],
          "buyers of stolen parts": "sellers.stolen_parts"},
         {}, 11),     # r1 9; pattern engine 9 (of 47)
        ("we029_varrow", "loop_r2", "WE-029_paid_sick_leave_mandate.md",
         {"employers.uncovered": "employers.covered", "associations": "employers.covered", "unions": "workers.uncovered",
          "neighboring_jurisdictions": "sellers.foreign", "employers.tradable": "producers.tradable", "buyers.local_services": "consumers"},
         {}, 19),     # r1 18 (of 42); pattern engine 40, in sample
    ]
    for case, loop, example, short, windows, k in cases:
        produced, _ = _loop_score(case, example, short, windows, loop)
        assert (case, loop, len(produced)) == (case, loop, k)


def test_blind_loop_runs_on_the_families_left_on_the_pattern_engine():
    """First core runs on cases that had only pattern-engine inputs, one per family, after the no-payment terms operation
    and costs per item offered (57f997f): private rules, disclosure, a transfer of means, a licence cap, a ban on a
    contract term, a congestion charge."""
    cases = [
        ("we066_campus", "WE-066_campus_ebike_ban.md",
         {"students.throttle": "members.current.throttle", "students.pedal_assist": "members.current.pedal_assist",
          "students.ebike": ["members.current.throttle", "members.current.pedal_assist"], "parents.driving": "drivers.school_run",
          "students.offsite": "riders.off_site", "coach_riders": "customers.coach", "school_bus_contractor": "contractors.coach",
          "bike_shops": ["retailers.ebikes", "retailers.pedal_bicycles", "retailers.escooters"],
          "parking_sellers": ["sellers.driveway_space", "sellers.yard_storage"], "parade_shops": "retailers.neighbors",
          "dunnock_news": "retailers.news_agent", "public_bus_operator": "sellers.route14",
          "members.current": ["members.current.throttle", "members.current.pedal_assist", "members.current.non_riders"]},
         {}, 18),     # of 64; no pattern-engine run
        ("we035_menu", "WE-035_menu_calorie_labels.md",
         {"chains.covered": "sellers.covered", "buyers.covered_chains": "buyers", "chains.near_threshold": "firms.near_threshold",
          "restaurants.exempt": "sellers.exempt"}, {}, 8),                                  # of 26; no pattern-engine run
        ("we033_kestland", "WE-033_household_cash_rebate.md",
         {"officials.enforcement": "officials.revenue", "households.recipients": "households",
          "borrowers.private": ["borrowers.business", "borrowers.mortgage", "borrowers.households"],
          "households.splittable": "households.separate_filers", "public_spending_recipients.later": "recipients.other_spending"},
         {}, 4),      # of 31; pattern engine 6
        ("we015_porthalden", "WE-015_taxi_license_cap.md",
         {"riders": "customers.taxi", "taxi operators": "licensees", "medallion_owners.initial": "licensees",
          "medallion_holders": "licensees", "medallion_buyers.later": "licensees.bought_near_peak",
          "private_hire": "drivers.private_hire", "drivers.unlicensed": "drivers.prospective", "drivers.taxi": "drivers.licensed"},
         {"announcement window": "announcement"}, 15),                                     # of 34; pattern engine 6
        ("we034_teravel", "WE-034_noncompete_ban.md",
         {"employers.net_trainers": "employers.trainers", "employers.rivals": "employers.hiring",
          "employers.restraining": "employers.trainers", "practices.professional": "employers.trainers.practices"}, {}, 13),  # of 39; pattern 7
        ("we046_calderford", "WE-046_congestion_charge.md",
         {"goods_vehicle_operators": ["distributors.longer_visits", "distributors.short_visits"], "drivers.nonresident": "customers.drivers",
          "residents.zone": "drivers.resident", "businesses.zone": "retailers.zone", "bus_riders": "riders",
          "ride_hail_drivers": "customers.ride_hail", "owners.parking.zone": "owners.garages_zone",
          "owners.parking.edge": "owners.garages_ringside", "transit_workers": "workers.transit", "transit_operator": "sellers.transit",
          "ring_road_users": "drivers.through", "owners.zone_commercial": "owners.property_zone",
          "owners.zone_residential": "owners.property_zone", "officials.enforcement": ["officials.enforcement", "officials.revenue"],
          "businesses.edge": "retailers.neighbors"}, {}, 18),                               # of 71; pattern engine 53
    ]
    for case, example, short, windows, k in cases:
        produced, _ = _loop_score(case, example, short, windows)
        assert (case, len(produced)) == (case, k)
