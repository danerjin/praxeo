"""The patterns as checks (step 5): each catalog pattern is a derived result (04a_core_rules.md: "a pattern is a shortcut,
never an independent source of truth"), so the core rules must derive its conclusion on a small situation that meets its
If-clause. One test per pattern; the situation names no instrument, only what the policy does in CR-1's terms."""
from praxeo.core import situation as S

P = {"text": "premise", "p": 0.9}


def _run(**parts):
    sit = {"name": "check", "exchanges": [], **parts}
    used = {p for v in parts.values() if isinstance(v, list) for x in v if isinstance(x, dict)
            for p in x.get("premises", []) + x.get("quantity_premises", [])}
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
