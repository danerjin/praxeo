"""The patterns as checks (step 5): each catalog pattern is a derived result (04a_core_rules.md: "a pattern is a shortcut,
never an independent source of truth"), so the core rules must derive its conclusion on a small situation that meets its
If-clause. One test per pattern; the situation names no instrument, only what the policy does in CR-1's terms."""
from praxeo.core import situation as S

P = {"text": "premise", "p": 0.9}


def _run(**parts):
    sit = {"name": "check", "exchanges": [], **parts}
    used = {p for v in parts.values() if isinstance(v, list) for x in v if isinstance(x, dict)
            for p in x.get("premises", []) + x.get("quantity_premises", []) + x.get("branch_premises", [])}
    sit["assumptions"] = {k: P for k in used | {"a1"}}
    return {(c.actor_class, c.variable if not c.group else ",".join(c.group), c.sign, c.window)
            for c in S.run(S.Situation(**sit)) if c.reported}


CEILING = dict(exchanges=[{"id": "e", "buyer": "buyers.served", "seller": "sellers", "unsatisfied_buyer": "buyers.unserved",
                           "buyer_price_var": "price_paid", "seller_price_var": "net_price_received",
                           "criteria_for": "buyers.unserved", "criteria": ["wait_time", "search_cost", "allocation_by_non_price_criteria"]}],
               held=[{"component": "k", "exchange": "e", "direction": "below", "premises": ["a1"]}])
FLOOR = dict(exchanges=[{"id": "e", "buyer": "employers", "seller": "workers", "unsatisfied_seller": "workers.seeking",
                         "seller_price_var": "wage_rate", "criteria_for": "workers.seeking",
                         "criteria": ["allocation_by_non_price_criteria", "search_cost", "wait_time"]}],
             held=[{"component": "k", "exchange": "e", "direction": "above", "premises": ["a1"]}])
TAX = dict(exchanges=[{"id": "e", "buyer": "buyers", "seller": "sellers", "buyer_price_var": "price_paid", "seller_price_var": "net_price_received"}],
           charges=[{"component": "k", "exchange": "e", "payer_side": "seller", "receiver": "officials.revenue",
                     "receipt_variable": "tax_revenue", "projection_variable": "tax_revenue_vs_static_projection"}],
           moves=[{"exchange": "e", "side": "buyer", "premises": ["a2"]}, {"exchange": "e", "side": "seller", "premises": ["a3"]}])


def test_pc_1_binding_ceiling_excess_demand():
    assert ("buyers.unserved", "excess_demand", "increase", None) in _run(**CEILING)


def test_pc_2_shortage_rationed_by_other_means_as_a_group():
    assert ("buyers.unserved", "wait_time,search_cost,allocation_by_non_price_criteria", "at_least_one_increase", None) in _run(**CEILING)


def test_pc_3_insiders_pay_the_controlled_price():
    got = _run(**CEILING)
    assert ("buyers.served", "price_paid", "decrease", None) in got and ("sellers", "net_price_received", "decrease", None) in got


def test_pc_4_quality_falls_under_a_ceiling():
    m = [{"exchange": "e", "kind": "adjust", "side": "seller", "actor": "buyers.served", "variables": ["quality_per_unit"], "premises": ["a2"]}]
    assert ("buyers.served", "quality_per_unit", "decrease", None) in _run(**CEILING, margins=m)


def test_pc_5_supply_shrinks_under_a_ceiling():
    m = [{"exchange": "e", "kind": "adjust", "side": "seller", "actor": "sellers", "variables": ["quantity_supplied"], "premises": ["a2"]}]
    assert ("sellers", "quantity_supplied", "decrease", None) in _run(**CEILING, margins=m)


def test_pc_6_trade_outside_the_ceiling():
    m = [{"exchange": "e", "kind": "outside", "actor": "buyers.unserved", "variables": ["informal_activity"], "premises": ["a2"]}]
    assert ("buyers.unserved", "informal_activity", "increase", None) in _run(**CEILING, margins=m)


def test_pc_7_holders_move_less():
    alt = [{"component": "k", "chooser": "buyers.served", "actor": "buyers.served", "variables": ["turnover"], "premises": ["a2"]}]
    assert ("buyers.served", "turnover", "decrease", None) in _run(**CEILING, alternatives=alt)


def test_pc_8_spillover_to_uncontrolled_substitutes():
    link = [{"source_actor": "buyers.unserved", "source_variable": "quantity_traded", "relation": "substitute",
             "actor": "buyers.unserved", "variable": "price_substitute", "premises": ["a2"]}]
    assert ("buyers.unserved", "price_substitute", "increase", None) in _run(**CEILING, links=link)


def test_pc_9_binding_floor_excess_supply():
    assert ("workers.seeking", "excess_supply", "increase", None) in _run(**FLOOR)


def test_pc_10_fewer_hires_hours_or_benefits_under_a_wage_floor():
    m = [{"exchange": "e", "kind": "adjust", "side": "buyer", "actor": "workers",
          "variables": ["employment", "hours_worked", "non_wage_compensation"], "premises": ["a2"]}]
    got = _run(**FLOOR, margins=m)
    assert ("workers", "employment,hours_worked,non_wage_compensation", "at_least_one_decrease", None) in got
    assert ("workers", "wage_rate", "increase", None) in got


def test_pc_11_non_price_selection_under_a_floor():
    assert ("workers.seeking", "allocation_by_non_price_criteria,search_cost,wait_time", "at_least_one_increase", None) in _run(**FLOOR)


def test_sb_9_buyer_of_last_resort_holds_the_floor():
    got = _run(**FLOOR, backstops=[{"component": "k", "exchange": "e", "buyer": "board", "outlay_variable": "subsidy_outlay", "premises": []}])
    assert ("board", "inventory_held", "increase", None) in got and ("workers", "quantity_supplied", "increase", None) in got
    assert ("workers.seeking", "excess_supply", "increase", None) not in got          # PC-9 Unless


def test_tx_1_and_tx_2_a_tax_takes_resources_opens_a_wedge_and_shrinks_the_market():
    got = _run(**TAX)
    assert {("officials.revenue", "tax_revenue", "increase", None), ("buyers", "price_paid", "increase", None),
            ("sellers", "net_price_received", "decrease", None), ("buyers", "quantity_traded", "decrease", None),
            ("sellers", "resources_available_other_uses", "decrease", None)} <= got


def test_tx_9_revenue_falls_short_of_a_static_projection():
    assert ("officials.revenue", "tax_revenue_vs_static_projection", "decrease", None) in _run(**TAX)


def test_tx_7_a_tariff_raises_the_protected_sellers_price_and_output():
    link = [{"source_actor": "buyers", "source_variable": "price_paid", "relation": "substitute", "actor": "sellers.domestic",
             "variable": v, "premises": ["a4"]} for v in ("net_price_received", "quantity_supplied")]
    got = _run(**TAX, links=link)
    assert ("sellers.domestic", "net_price_received", "increase", None) in got and ("sellers.domestic", "quantity_supplied", "increase", None) in got


def test_tx_8_import_restriction_lowers_exports():
    link = [{"source_actor": "buyers", "source_variable": "quantity_traded", "relation": "currency", "actor": "exporters",
             "variable": "quantity_supplied", "premises": ["a4"]}]
    assert ("exporters", "quantity_supplied", "decrease", None) in _run(**TAX, links=link)


def test_rs_14_input_cost_passed_to_the_output_price():
    link = [{"source_actor": "buyers", "source_variable": "price_paid", "relation": "output", "actor": "buyers.downstream",
             "variable": "price_paid", "premises": ["a4"]}]
    assert ("buyers.downstream", "price_paid", "increase", None) in _run(**TAX, links=link)


def test_rs_1_rs_4_rs_5_responses_of_those_a_tax_burdens():
    alt = [{"component": "k", "chooser": "buyers", "actor": "buyers", "variables": [v], "premises": ["a4"]}
           for v in ("quantity_substitute", "cross_border_purchases", "reclassification")]
    got = _run(**TAX, alternatives=alt)
    assert {("buyers", v, "increase", None) for v in ("quantity_substitute", "cross_border_purchases", "reclassification")} <= got


def test_rs_7_lobbying_by_those_with_a_stake():
    assert ("sellers", "lobbying_effort", "increase", None) in _run(**TAX, stakes=[{"component": "k", "actor": "sellers", "premises": ["a4"]}])


def test_rs_8_actions_brought_forward_before_a_burden_takes_effect():
    t = [{"component": "k", "actor": "buyers", "variable": "quantity_traded", "mode": "bring_forward", "premises": ["a4"]}]
    got = _run(**TAX, announced=[{"component": "k", "premises": []}], timing=t)
    assert ("buyers", "quantity_traded", "increase", "announcement") in got
    assert ("buyers", "quantity_traded", "decrease", None) in got                    # outside the window, the market shrinks


def test_sb_4_capitalization_of_a_change_in_returns():
    assets = [{"exchange": "e", "side": "seller", "actor": "owners", "premises": ["a4"]}]
    assert ("owners", "asset_value", "decrease", None) in _run(**CEILING, assets=assets)


def test_oc_3_enforcement_and_its_funding():
    got = _run(**TAX, enforcers=[{"component": "k", "actor": "officials.enforcement"}],
               funded=[{"component": "k", "actor": "taxpayers", "premises": ["a4"]}])
    assert ("officials.enforcement", "enforcement_cost", "increase", None) in got and ("taxpayers", "resources_available_other_uses", "decrease", None) in got


def test_oc_4_prevented_exchanges_are_lost_to_both_sides():
    got = _run(**CEILING)
    assert ("sellers", "quantity_traded", "decrease", None) in got and ("buyers.unserved", "quantity_traded", "decrease", None) in got


def test_rs_15_relief_granted_case_by_case_is_rationed_by_other_criteria():
    got = _run(**TAX, discretion=[{"component": "k", "actor": "buyers", "premises": ["a4"]}])
    assert ("buyers", "allocation_by_non_price_criteria", "increase", None) in got and ("buyers", "compliance_cost", "increase", None) in got


GRANT = dict(exchanges=[{"id": "e", "buyer": "buyers", "seller": "producers", "buyer_price_var": "price_paid", "seller_price_var": "net_price_received"}],
             grants=[{"component": "k", "exchange": "e", "recipient_side": "seller", "payer": "agency"}],
             moves=[{"exchange": "e", "side": "buyer", "premises": ["a2"]}, {"exchange": "e", "side": "seller", "premises": ["a3"]}])
QUOTA = dict(exchanges=[{"id": "e", "buyer": "buyers", "seller": "sellers", "unsatisfied_seller": "sellers.excluded",
                         "buyer_price_var": "price_paid", "seller_price_var": "net_price_received"}],
             capped=[{"component": "k", "exchange": "e", "holders": ["licence_holders"], "premises": ["a1"]}])


def test_sb_1_and_sb_2_a_grant_transfers_means_and_expands_the_market():
    got = _run(**GRANT)
    assert {("producers", "resources_available_other_uses", "increase", None), ("agency", "subsidy_outlay", "increase", None),
            ("buyers", "quantity_traded", "increase", None), ("buyers", "price_paid", "decrease", None),
            ("producers", "net_price_received", "increase", None)} <= got


def test_sb_6_purchases_pulled_into_a_grant_fall_after_it_expires():
    t = [{"component": "k", "actor": "producers", "variable": "investment", "mode": "bring_forward", "premises": ["a4"]}]
    got = _run(**GRANT, timing=t, announced=[{"component": "k", "premises": []}], expires=[{"component": "k", "premises": ["a5"]}])
    assert ("producers", "investment", "decrease", "after_expiry") in got


def test_en_1_and_en_2_a_quantity_cap_raises_the_price_and_the_value_of_the_permission():
    got = _run(**QUOTA)
    assert {("buyers", "price_paid", "increase", None), ("buyers", "quantity_traded", "decrease", None),
            ("licence_holders", "asset_value", "increase", None), ("sellers.excluded", "quantity_traded", "decrease", None)} <= got


def test_en_6_a_cap_on_a_good_priced_in_a_wider_market_raises_the_permissions_price_not_the_goods():
    q = {**QUOTA, "capped": [{**QUOTA["capped"][0], "wider_price": True}]}
    got = _run(**q)
    assert ("licence_holders", "right_lease_price", "increase", None) in got
    assert ("buyers", "price_paid", "increase", None) not in got


def test_en_7_a_ban_stops_the_legal_trade_for_both_sides():
    got = _run(exchanges=QUOTA["exchanges"], banned=[{"component": "k", "exchange": "e", "premises": ["a1"]}])
    assert ("buyers", "quantity_traded", "decrease", None) in got and ("sellers", "quantity_traded", "decrease", None) in got


def test_pc_17_a_mandated_term_is_a_charge_paid_in_kind_to_the_counterparty():
    x = [{"id": "e", "buyer": "employers", "seller": "workers", "buyer_price_var": "labor_cost", "seller_price_var": "wage_rate"}]
    ch = [{"component": "k", "exchange": "e", "payer_side": "buyer", "receiver": "workers",
           "receipt_variable": "non_wage_compensation", "quantity_premises": ["a2"]}]
    got = _run(exchanges=x, charges=ch, moves=[{"exchange": "e", "side": "seller", "premises": ["a3"]}])
    assert {("workers", "non_wage_compensation", "increase", None), ("workers", "wage_rate", "decrease", None),
            ("employers", "quantity_traded", "decrease", None)} <= got


def test_en_3_a_fee_fixed_per_seller_bears_on_entry_not_on_each_trade():
    ch = [{**TAX["charges"][0], "basis": "operating", "receipt_variable": "non_tax_receipts", "projection_variable": None}]
    got = _run(exchanges=TAX["exchanges"], charges=ch)
    assert ("sellers", "number_of_sellers", "decrease", None) in got
    assert ("buyers", "quantity_traded", "decrease", None) not in got


def test_sb_3_more_offered_lowers_the_price_against_a_grants_rise():
    link = [{"source_actor": "producers", "source_variable": "quantity_traded", "relation": "supply", "actor": "producers",
             "variable": "net_price_received", "premises": ["a4"]}]
    assert ("producers", "net_price_received", "ambiguous", None) in _run(**GRANT, links=link)


def test_oc_1_complying_uses_up_means():
    assert ("buyers", "resources_available_other_uses", "decrease", None) in _run(**TAX, compliance=[{"component": "k", "actor": "buyers"}])


JOBS = [{"id": "e", "buyer": "employers", "seller": "workers", "buyer_price_var": "labor_cost", "seller_price_var": "wage_rate"}]


def test_en_14_play_or_pay_each_branch_needs_its_premise():
    ch = [{"component": "k_offer", "exchange": "e", "payer_side": "buyer", "receiver": "workers.at_players",
           "receipt_variable": "non_wage_compensation", "branch_premises": ["a2"]},
          {"component": "k_pay", "exchange": "e", "payer_side": "buyer", "receiver": "officials.revenue",
           "receipt_variable": "non_tax_receipts", "branch_premises": ["a3"]}]
    got = _run(exchanges=JOBS, charges=ch)
    assert ("workers.at_players", "non_wage_compensation", "increase", None) in got
    assert ("officials.revenue", "non_tax_receipts", "increase", None) in got
    sit = {"name": "check", "exchanges": JOBS, "charges": ch,
           "assumptions": {"a2": {"text": "Some offer", "p": 0.3}, "a3": {"text": "Some pay", "p": 0.9}}}
    got = {(c.actor_class, c.variable, c.sign) for c in S.run(S.Situation(**sit)) if c.reported}
    assert ("workers.at_players", "non_wage_compensation", "increase") not in got
    assert ("officials.revenue", "non_tax_receipts", "increase") in got


def test_a_capped_charge_takes_means_but_bears_on_no_margin():
    ch = [{"component": "k", "exchange": "e", "payer_side": "buyer", "receiver": "officials.revenue",
           "receipt_variable": "non_tax_receipts", "capped_payers": ["employers.capped"]}]
    assert ("employers.capped", "resources_available_other_uses", "decrease", None) in _run(exchanges=JOBS, charges=ch)
    x = [{"id": "e", "buyer": "employers.capped", "seller": "workers", "buyer_price_var": "labor_cost", "seller_price_var": "wage_rate"}]
    got = _run(exchanges=x, charges=[{**ch[0], "capped_payers": ["employers.capped"]}])
    assert ("employers.capped", "quantity_traded", "decrease", None) not in got


def test_a_line_drawn_in_size_holds_those_near_it_below_it():
    alt = [{"component": "k", "chooser": "employers.near_line", "actor": "employers.near_line", "variables": ["reclassification"], "premises": ["a3"]}]
    got = _run(exchanges=JOBS, thresholds=[{"component": "k", "actor": "employers.near_line", "variable": "employment", "premises": ["a2"]}],
               alternatives=alt)
    assert ("employers.near_line", "employment", "decrease", None) in got
    assert ("employers.near_line", "reclassification", "increase", None) in got


def test_cr_7c_a_race_to_qualify_for_an_allocation_by_history():
    got = _run(exchanges=JOBS, qualifies=[{"component": "k", "actor": "vessel_owners", "variable": "quantity_supplied", "premises": ["a2"]}])
    assert ("vessel_owners", "quantity_supplied", "increase", "announcement") in got
    assert ("vessel_owners", "resources_available_other_uses", "decrease", None) in got


def test_rs_8_the_rush_before_a_grant_ends():
    t = [{"component": "k", "actor": "producers", "variable": "investment", "mode": "bring_forward", "premises": ["a4"]}]
    got = _run(**GRANT, timing=t, expires=[{"component": "k", "premises": ["a5"]}])
    assert ("producers", "investment", "increase", "deadline") in got and ("producers", "investment", "decrease", "after_expiry") in got


def test_a_line_another_actor_chooses_on():
    alt = [{"component": "k", "chooser": "employers", "actor": "employers", "variables": ["reclassification"], "premises": ["a3"]}]
    got = _run(exchanges=JOBS, alternatives=alt, thresholds=[{"component": "k", "actor": "workers.near_line", "variable": "hours_worked",
                                                            "chooser": "employers", "premises": ["a2"]}])
    assert ("workers.near_line", "hours_worked", "decrease", None) in got and ("employers", "reclassification", "increase", None) in got


def test_pc_17_a_mandated_cost_where_the_wage_cannot_fall_goes_to_hours_and_hiring():
    ch = [{"component": "k", "exchange": "e", "payer_side": "buyer", "receiver": "officials.revenue", "receipt_variable": "non_tax_receipts"}]
    m = [{"exchange": "e", "kind": "adjust", "side": "buyer", "actor": "workers.min_wage",
          "variables": ["employment", "hours_worked", "non_wage_compensation"], "premises": ["a3"]}]
    got = _run(exchanges=JOBS, charges=ch, margins=m, fixed=[{"exchange": "e", "side": "seller", "premises": ["a2"]}])
    assert ("workers.min_wage", "employment,hours_worked,non_wage_compensation", "at_least_one_decrease", None) in got
    assert ("workers.min_wage", "employment,hours_worked,non_wage_compensation", "at_least_one_decrease", None) not in _run(
        exchanges=JOBS, charges=ch, margins=m)


def test_an_unclear_provision_gives_a_sign_per_reading():
    sit = {"name": "check", "exchanges": JOBS,
           "thresholds": [{"component": "k_seasonal", "actor": "employers.seasonal", "variable": "employment", "premises": ["a2"]}],
           "unclear": [{"id": "U1", "text": "whether seasonal staff count", "readings": ["U1-a: they count", "U1-b: they do not"],
                        "components": {"U1-a": ["k_seasonal"], "U1-b": []}}],
           "assumptions": {"a2": P}}
    got = [c for c in S.run(S.Situation(**sit)) if c.actor_class == "employers.seasonal" and c.variable == "employment"]
    assert got and got[0].sign_by_reading == {"U1-a": "decrease", "U1-b": "none"}


def test_an_alternative_only_one_reading_opens():
    sit = {"name": "check", "exchanges": JOBS,
           "thresholds": [{"component": "k", "actor": "employers.near_line", "variable": "employment", "premises": ["a2"]}],
           "alternatives": [{"component": "k", "chooser": "employers.near_line", "actor": "employers.near_line",
                             "variables": ["seasonal_engagements"], "premises": ["a2"], "reading": "U1-b"}],
           "unclear": [{"id": "U1", "text": "whether seasonal staff count", "readings": ["U1-a: they count", "U1-b: they do not"],
                        "components": {}}],
           "assumptions": {"a2": P}}
    got = [c for c in S.run(S.Situation(**sit)) if c.variable == "seasonal_engagements"]
    assert got and got[0].sign_by_reading == {"U1-a": "none", "U1-b": "increase"}


def test_dm_1_incidence_follows_the_alternatives():
    got = _run(**TAX, incidence=[{"component": "k", "exchange": "e", "side": "buyer", "premises": ["a4"]}])
    assert ("buyers", "tax_share_borne", "increase", None) in got and ("sellers", "tax_share_borne", "increase", None) not in got
    got = _run(**GRANT, incidence=[{"component": "k", "exchange": "e", "side": "seller", "premises": ["a4"]}])
    assert ("producers", "subsidy_share_received", "increase", None) in got


def test_a_sticky_price_takes_the_wedge_later_and_the_other_terms_first():
    ch = [{"component": "k", "exchange": "e", "payer_side": "buyer", "receiver": "officials.revenue", "receipt_variable": "non_tax_receipts"}]
    m = [{"exchange": "e", "kind": "adjust", "side": "buyer", "actor": "workers",
          "variables": ["employment", "hours_worked", "non_wage_compensation"], "premises": ["a3"]}]
    sit = {"name": "check", "exchanges": JOBS, "charges": ch, "margins": m,
           "fixed": [{"exchange": "e", "side": "seller", "horizon": "short", "premises": ["a2"]}],
           "moves": [{"exchange": "e", "side": "seller", "horizon": "medium", "premises": ["a4"]}],
           "assumptions": {k: P for k in ("a2", "a3", "a4")}}
    cons = {(c.actor_class, ",".join(c.group) or c.variable): c for c in S.run(S.Situation(**sit)) if c.reported}
    assert cons[("workers", "wage_rate")].sign == "decrease" and cons[("workers", "wage_rate")].horizon[0] == "medium"
    grp = cons[("workers", "employment,hours_worked,non_wage_compensation")]
    assert grp.sign == "at_least_one_decrease" and grp.horizon[0] == "short"


def test_signs_name_only_the_readings_they_depend_on():
    sit = {"name": "check", "exchanges": JOBS,
           "thresholds": [{"component": "k_seasonal", "actor": "employers.seasonal", "variable": "employment", "premises": ["a2"]}],
           "unclear": [{"id": "U1", "text": "x", "readings": ["U1-a: x", "U1-b: y"], "components": {"U1-a": ["k_seasonal"], "U1-b": []}},
                       {"id": "U2", "text": "z", "readings": ["U2-a: z", "U2-b: w"], "components": {"U2-a": [], "U2-b": []}}],
           "assumptions": {"a2": P}}
    got = [c for c in S.run(S.Situation(**sit)) if c.actor_class == "employers.seasonal" and c.variable == "employment"]
    assert got[0].sign_by_reading == {"U1-a": "decrease", "U1-b": "none"}


def test_a_branch_any_of_several_premise_sets_opens():
    ch = [{"component": "k_offer", "exchange": "e", "payer_side": "buyer", "receiver": "workers.at_offering_firms",
           "receipt_variable": "non_wage_compensation", "branch_premises": ["a2"], "branch_premise_sets": [["a3"]]}]
    sit = {"name": "check", "exchanges": JOBS, "charges": ch,
           "assumptions": {"a2": {"text": "new offerers", "p": 0.3}, "a3": {"text": "upgraders", "p": 0.8}}}
    got = {(c.actor_class, c.variable, c.sign) for c in S.run(S.Situation(**sit)) if c.reported}
    assert ("workers.at_offering_firms", "non_wage_compensation", "increase") in got


def test_a_link_acts_at_its_horizon_and_funds_net_their_flows():
    link = [{"source_actor": "officials.revenue", "source_variable": "tax_revenue", "relation": "paid_into", "actor": "treasury",
             "variable": "fund_balance", "premises": ["a4"]},
            {"source_actor": "buyers", "source_variable": "price_paid", "relation": "output", "actor": "buyers.downstream",
             "variable": "price_paid", "horizon": "long", "premises": ["a4"]}]
    sit = {"name": "check", **TAX, "links": link, "assumptions": {k: P for k in ("a2", "a3", "a4")}}
    cons = {(c.actor_class, c.variable): c for c in S.run(S.Situation(**sit)) if c.reported}
    assert cons[("treasury", "fund_balance")].sign == "increase"
    assert cons[("buyers.downstream", "price_paid")].horizon == ["long"]
    spend = link[:1] + [{"source_actor": "officials.enforcement", "source_variable": "enforcement_cost", "relation": "paid_from",
                         "actor": "treasury", "variable": "fund_balance", "premises": ["a4"]}]
    got = _run(**TAX, links=spend, enforcers=[{"component": "k", "actor": "officials.enforcement"}])
    assert ("treasury", "fund_balance", "ambiguous", None) in got        # receipts against spending: CR-12 without dominance


def test_the_subclass_receiving_a_term_in_kind_holds_on_to_it():
    ch = [{"component": "k", "exchange": "e", "payer_side": "buyer", "receiver": "workers.at_offering_firms",
           "receipt_variable": "non_wage_compensation", "quantity_premises": ["a2"]}]
    alt = [{"component": "k", "chooser": "workers.at_offering_firms", "actor": "workers.at_offering_firms",
            "variables": ["job_changes"], "premises": ["a3"]}]
    assert ("workers.at_offering_firms", "job_changes", "decrease", None) in _run(exchanges=JOBS, charges=ch, alternatives=alt)


MENU = [{"id": "e", "buyer": "diners", "seller": "restaurants", "buyer_price_var": "price_paid", "seller_price_var": "net_price_received"}]


def test_cr_11_a_disclosure_that_shows_a_good_worse_than_believed():
    got = _run(exchanges=MENU, terms=[{"component": "k", "exchange": "e", "side": "buyer", "direction": "worse", "premises": ["a1"]}],
               moves=[{"exchange": "e", "side": "seller", "premises": ["a2"]}],
               alternatives=[{"component": "k", "chooser": "diners", "actor": "diners", "variables": ["quantity_substitute"], "premises": ["a3"]}])
    assert {("diners", "quantity_traded", "decrease", None), ("restaurants", "net_price_received", "decrease", None),
            ("diners", "quantity_substitute", "increase", None)} <= got


def test_cr_5_a_private_rule_that_worsens_the_members_bundle():
    x = [{"id": "e", "buyer": "members.current", "seller": "rule_maker.private", "buyer_price_var": "price_paid",
          "seller_price_var": "net_price_received"}]
    alt = [{"component": "k", "chooser": "members.current", "actor": "rival_providers", "variables": ["quantity_traded"], "premises": ["a3"]}]
    got = _run(exchanges=x, alternatives=alt, terms=[{"component": "k", "exchange": "e", "side": "buyer", "direction": "worse", "premises": ["a1"]}])
    assert ("members.current", "quantity_traded", "decrease", None) in got and ("rival_providers", "quantity_traded", "increase", None) in got


def test_cr_4_a_cost_per_item_offered_narrows_the_range():
    ch = [{"component": "k", "exchange": "e", "payer_side": "seller", "receiver": "testers", "receipt_variable": "non_tax_receipts", "basis": "item"}]
    got = _run(exchanges=MENU, charges=ch)
    assert ("restaurants", "variety", "decrease", None) in got and ("diners", "quantity_traded", "decrease", None) not in got


def test_an_alternative_measured_inversely():
    alt = [{"component": "k", "chooser": "restaurants", "actor": "restaurants", "variables": ["product_attribute"], "inverse": True, "premises": ["a3"]}]
    got = _run(exchanges=MENU, alternatives=alt,
               charges=[{"component": "k", "exchange": "e", "payer_side": "seller", "receiver": "testers", "receipt_variable": "non_tax_receipts", "basis": "item"}])
    assert ("restaurants", "product_attribute", "decrease", None) in got
