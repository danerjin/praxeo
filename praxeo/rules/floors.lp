% Price floors (handbook catalog 1.4): PC-9 (excess supply), PC-10 (the least productive lose hires), PC-11 (non-price
% selection), written as CR-6 with the sides named: a price held above the clearing level leaves the sellers' side long and
% the buyers' side short; the pressure the floor stops moves to the terms it does not regulate and to the criteria by which
% the short side chooses. With RS-1, RS-3, RS-4, RS-5, RS-7, RS-14, SB-4, TS-2, OC-2 and OC-3 where a floor brings them in.
% Developed on WE-009 (a minimum wage with a youth rate). Input facts, written by praxeo/engine.py from the policy record:
%   floor(C).                      a price_floor
%   bound(C, A).                   the short side: buyers who must pay at least the floor (employers)
%   fl_seller(C, A).               the long side held at the floor: sellers whose price it raises (low-wage workers)
%   fl_excluded(C, A).             would-be sellers at the floor, who bear the surplus (job seekers)
%   employment(C).                 the floor is on a wage; otherwise on the price of a good
%   fl_lower_tier(C, A).           sellers under a lower floor whom buyers can hire in place of fl_seller (a youth rate)
%   fl_complier(C, A).             who must comply and can evade: the bound buyers unless the record names the sellers
%   open_breach(C).                evasion is within the legal market (legal_breach), not outside it
%   mc_output_buyer(C, A). mobile_buyer(C, A). fl_substitute_seller(C, A). fl_asset_owner(C, A).
%   definition_line(C). announced(C). general_budget(C). tax_named(C). fixed_budget(C). state_buys(C).
%   enforcer(C, A). fl_payer_group(C, "a,b,c"). fl_outlay(C, A).
% Every rule is monotone in holds/1: it negates only plain facts.

{ holds(A) } :- assumption(A).

% CR-6, CR-1: where the floor is above the price some sellers could command (binding) and buyers comply (enforced), the price
% of those sellers who keep selling rises (PC-10, Then: workers who keep their jobs at the floor).
fl_binds(C) :- floor(C), holds(binding(C)), holds(enforced(C)), not exception(pc_9, C).
fired(pc_9, fl_binds(C), binding(C))  :- fl_binds(C).
fired(pc_9, fl_binds(C), enforced(C)) :- fl_binds(C).
effect(fl_binds(C), S, "wage_rate", increase, short, visible, "B")          :- fl_binds(C), employment(C), fl_seller(C, S).
effect(fl_binds(C), S, "net_price_received", increase, short, visible, "B") :- fl_binds(C), not employment(C), fl_seller(C, S).
effect(fl_binds(C), B, "price_paid", increase, short, visible, "B")         :- fl_binds(C), not employment(C), bound(C, B).

% The floor raises the buyers' cost per unit where they cannot offset it fully by cutting the terms it does not regulate,
% or by replacing what they buy at the old cost (cost_not_offset). Every chain below rests on that.
fl_cost(C) :- fl_binds(C), holds(cost_not_offset(C)).
fired(cr_6, fl_cost(C), fl_binds(C))          :- fl_cost(C).
fired(cr_6, fl_cost(C), cost_not_offset(C))   :- fl_cost(C).

% PC-9: the long side has more than the short side takes at the floor. Unless the state buys the surplus (state_buys).
fl_surplus(C) :- fl_cost(C), not state_buys(C), not exception(pc_9, C).
fired(pc_9, fl_surplus(C), fl_cost(C)) :- fl_surplus(C).
effect(fl_surplus(C), X, "excess_supply", increase, short, invisible, "B") :- fl_surplus(C), fl_excluded(C, X).
effect(fl_surplus(C), S, "excess_supply", increase, short, invisible, "B") :- fl_surplus(C), not employment(C), fl_seller(C, S), not fl_excluded(C, _).
% PC-11 with PC-2's group form: the short side chooses among the long side by other criteria, and those who wait bear it
% as search, waiting or selection, at least one.
group_effect(fl_surplus(C), X, "allocation_by_non_price_criteria,search_cost,wait_time", at_least_one_increase, short, invisible, "B") :- fl_surplus(C), fl_excluded(C, X).
fired(pc_11, fl_surplus(C), fl_cost(C)) :- fl_surplus(C).

% PC-10 (labour): for sellers whose labour buyers value below the floor, at least one of jobs, hours or other terms falls,
% where buyers can adjust some margin (margins). For a good (PC-9): fewer units are traded.
fl_margins(C) :- fl_cost(C), employment(C), holds(margins(C)), not exception(pc_10, C).
fired(pc_10, fl_margins(C), fl_cost(C))   :- fl_margins(C).
fired(pc_10, fl_margins(C), margins(C))   :- fl_margins(C).
group_effect(fl_margins(C), S, "employment,hours_worked,non_wage_compensation", at_least_one_decrease, short, invisible, "B") :- fl_margins(C), fl_seller(C, S).
fl_fewer(C) :- fl_cost(C), not employment(C), not state_buys(C).
fired(pc_9, fl_fewer(C), fl_cost(C)) :- fl_fewer(C).
effect(fl_fewer(C), B, "quantity_traded", decrease, short, invisible, "B") :- fl_fewer(C), bound(C, B).
effect(fl_fewer(C), S, "quantity_traded", decrease, short, invisible, "B") :- fl_fewer(C), fl_seller(C, S).

% PC-9 Unless, SB-9: where the state buys what the market does not take at the floor (state_buys), its stocks and outlay
% rise, paid as OC-1 says (the payer group unless a tax is named).
fl_bought(C) :- fl_binds(C), state_buys(C), holds(cost_not_offset(C)).
fired(sb_9, fl_bought(C), fl_binds(C))   :- fl_bought(C).
fired(sb_9, fl_bought(C), state_buys(C)) :- fl_bought(C).
effect(fl_bought(C), O, "inventory_held", increase, short, invisible, "B") :- fl_bought(C), fl_outlay(C, O).
effect(fl_bought(C), O, "subsidy_outlay", increase, short, invisible, "B") :- fl_bought(C), fl_outlay(C, O).
group_effect(fl_bought(C), G, "resources_available_other_uses", at_least_one_decrease, short, invisible, "B") :- fl_bought(C), fl_payer_group(C, G), not tax_named(C).

% A lower floor for one group of sellers (fl_lower_tier): where buyers use it (lower_tier_used) and the groups are
% substitutes (tiers_substitute), buyers shift toward the cheaper group (RS-1): the higher-floor sellers lose jobs or hours
% (agreeing with PC-10), the lower-tier sellers gain them, against that group's own PC-10 (its own component).
fl_tiers(C) :- fl_cost(C), employment(C), fl_lower_tier(C, _), holds(lower_tier_used(C)), holds(tiers_substitute(C)), not exception(rs_1, C).
fired(rs_1, fl_tiers(C), fl_cost(C))             :- fl_tiers(C).
fired(rs_1, fl_tiers(C), lower_tier_used(C))     :- fl_tiers(C).
fired(rs_1, fl_tiers(C), tiers_substitute(C))    :- fl_tiers(C).
group_effect(fl_tiers(C), S, "employment,hours_worked,non_wage_compensation", at_least_one_decrease, short, invisible, "B") :- fl_tiers(C), fl_seller(C, S).
group_effect(fl_tiers(C), Y, "employment,hours_worked,non_wage_compensation", at_least_one_increase, short, invisible, "B") :- fl_tiers(C), fl_lower_tier(C, Y).

% CR-7b, CR-3a: the buyers' return falls in the short run; TS-2: investment planned for when the floor is expected falls
% (announced, and expected_ahead); SB-4: the value of assets specific to the use falls where the floor is expected to last
% (expected_to_last).
% These are the short side's losses under a wage floor. Under a floor on a good that the state backs by buying the surplus,
% the long side gains instead (below): found out of sample on WE-008.
fl_returns(C) :- fl_cost(C), employment(C).
fired(cr_7, fl_returns(C), fl_cost(C)) :- fl_returns(C).
effect(fl_returns(C), B, "return_on_capital", decrease, short, invisible, "B") :- fl_returns(C), bound(C, B).
fl_invest(C) :- fl_cost(C), employment(C), announced(C), holds(expected_ahead(C)), not exception(ts_2, C).
fired(ts_2, fl_invest(C), announced(C))      :- fl_invest(C).
fired(ts_2, fl_invest(C), expected_ahead(C)) :- fl_invest(C).
effect(fl_invest(C), B, "investment_target", decrease, short, invisible, "B") :- fl_invest(C), bound(C, B).
fl_capitalized(C) :- fl_cost(C), employment(C), fl_asset_owner(C, _), holds(expected_to_last(C)), not exception(sb_4, C).
fired(sb_4, fl_capitalized(C), fl_cost(C))           :- fl_capitalized(C).
fired(sb_4, fl_capitalized(C), expected_to_last(C))  :- fl_capitalized(C).
effect(fl_capitalized(C), O, "asset_value", decrease, short, invisible, "B") :- fl_capitalized(C), fl_asset_owner(C, O).

% SB-2, SB-4 on the long side: where the state buys what the market does not take, the sellers are paid the floor for all
% they offer, so they supply more; where the floor is expected to last (expected_to_last), they invest, more of them enter,
% and the value of assets specific to selling rises.
fl_held(C) :- fl_binds(C), state_buys(C), not exception(sb_2, C).
fired(sb_2, fl_held(C), fl_binds(C))   :- fl_held(C).
fired(sb_2, fl_held(C), state_buys(C)) :- fl_held(C).
effect(fl_held(C), S, "quantity_supplied", increase, short, invisible, "B") :- fl_held(C), fl_seller(C, S).
fl_held_lasting(C) :- fl_held(C), holds(expected_to_last(C)).
fired(sb_4, fl_held_lasting(C), fl_held(C))           :- fl_held_lasting(C).
fired(sb_4, fl_held_lasting(C), expected_to_last(C))  :- fl_held_lasting(C).
effect(fl_held_lasting(C), S, "investment_target", increase, medium, invisible, "B") :- fl_held_lasting(C), fl_seller(C, S).
effect(fl_held_lasting(C), S, "number_of_sellers", increase, medium, invisible, "B") :- fl_held_lasting(C), fl_seller(C, S).
effect(fl_held_lasting(C), O, "asset_value", increase, short, invisible, "B") :- fl_held_lasting(C), fl_asset_owner(C, O).

% RS-14: where the buyers' rivals face the same floor (rivals_bound), their output's price rises; RS-4: buyers of that output
% who can cross to unbound sellers (cross_border_feasible) do so.
fl_pass(C) :- fl_cost(C), mc_output_buyer(C, _), holds(rivals_bound(C)), not exception(rs_14, C).
fired(rs_14, fl_pass(C), fl_cost(C))         :- fl_pass(C).
fired(rs_14, fl_pass(C), rivals_bound(C))    :- fl_pass(C).
effect(fl_pass(C), X, "price_paid", increase, short, invisible, "B") :- fl_pass(C), mc_output_buyer(C, X).
fl_cross(C) :- fl_cost(C), mobile_buyer(C, _), holds(cross_border_feasible(C)), not exception(rs_4, C).
fired(rs_4, fl_cross(C), fl_cost(C))                 :- fl_cross(C).
fired(rs_4, fl_cross(C), cross_border_feasible(C))   :- fl_cross(C).
effect(fl_cross(C), M, "cross_border_purchases", increase, short, invisible, "B") :- fl_cross(C), mobile_buyer(C, M).

% RS-1: where a substitute for what the floor makes dearer exists (substitute_exists: labour-saving equipment), buyers use
% more of it over time and its sellers sell more.
fl_substitute(C) :- fl_cost(C), holds(substitute_exists(C)), not exception(rs_1, C).
fired(rs_1, fl_substitute(C), fl_cost(C))            :- fl_substitute(C).
fired(rs_1, fl_substitute(C), substitute_exists(C))  :- fl_substitute(C).
effect(fl_substitute(C), B, "quantity_substitute", increase, medium, invisible, "B") :- fl_substitute(C), bound(C, B).
effect(fl_substitute(C), S, "quantity_traded", increase, medium, invisible, "B")     :- fl_substitute(C), fl_substitute_seller(C, S).

% RS-5: where the definitions draw a line (contractors are outside a minimum wage) and reshaping pays, trade moves outside it.
fl_reshaped(C) :- fl_binds(C), definition_line(C), holds(reshaping_pays(C)), not exception(rs_5, C).
fired(rs_5, fl_reshaped(C), definition_line(C)) :- fl_reshaped(C).
fired(rs_5, fl_reshaped(C), reshaping_pays(C))  :- fl_reshaped(C).
effect(fl_reshaped(C), B, "reclassification", increase, short, invisible, "B") :- fl_reshaped(C), bound(C, B).

% RS-3: where trade below the floor goes undetected (evasion), those who must comply evade: outside the law, or within the
% legal market where the evasion is open (open_breach: pay below the floor on the books, false certification; found out of
% sample on WE-008 and WE-061).
fl_evaded(C) :- floor(C), holds(binding(C)), holds(evasion(C)), not exception(rs_3, C).
fired(rs_3, fl_evaded(C), binding(C)) :- fl_evaded(C).
fired(rs_3, fl_evaded(C), evasion(C)) :- fl_evaded(C).
effect(fl_evaded(C), B, "informal_activity", increase, short, invisible, "B") :- fl_evaded(C), not open_breach(C), fl_complier(C, B).
effect(fl_evaded(C), B, "legal_breach", increase, short, invisible, "B")      :- fl_evaded(C), open_breach(C), fl_complier(C, B).

% RS-7: those who bear the floor (can_organize) and those it raises (sellers_organize) lobby over it.
fl_lobby(C) :- floor(C), holds(binding(C)), holds(can_organize(C)), not exception(rs_7, C).
fired(rs_7, fl_lobby(C), binding(C))      :- fl_lobby(C).
fired(rs_7, fl_lobby(C), can_organize(C)) :- fl_lobby(C).
effect(fl_lobby(C), B, "lobbying_effort", increase, medium, invisible, "B") :- fl_lobby(C), bound(C, B).
fl_sellers_lobby(C) :- floor(C), holds(binding(C)), holds(sellers_organize(C)), not exception(rs_7, C).
fired(rs_7, fl_sellers_lobby(C), binding(C))          :- fl_sellers_lobby(C).
fired(rs_7, fl_sellers_lobby(C), sellers_organize(C)) :- fl_sellers_lobby(C).
effect(fl_sellers_lobby(C), S, "lobbying_effort", increase, medium, invisible, "B") :- fl_sellers_lobby(C), fl_seller(C, S).
lobby_concl(fl_lobby(C), C) :- fl_lobby(C).
lobby_concl(fl_sellers_lobby(C), C) :- fl_sellers_lobby(C).

% OC-2: complying takes resources (records of hours and pay), Tier A given the floor.
fl_compliance(C) :- floor(C), not exception(oc_2, C).
fired(oc_2, fl_compliance(C), floor(C)) :- fl_compliance(C).
effect(fl_compliance(C), B, "compliance_cost", increase, short, invisible, "A") :- fl_compliance(C), fl_complier(C, B).

% OC-3: enforcing the floor takes the agency's resources (Tier A). With a general budget, OC-1's payers bear it. With a budget
% that is not raised (fixed_budget, and budget_fixed), the agency's other work falls instead (OC-3 0.9), recorded as the item
% other_work.
fl_administered(C) :- floor(C), enforcer(C, _), not exception(oc_3, C).
fired(oc_3, fl_administered(C), floor(C)) :- fl_administered(C).
effect(fl_administered(C), E, "enforcement_cost", increase, short, invisible, "A") :- fl_administered(C), enforcer(C, E).
fl_funded(C) :- fl_administered(C), general_budget(C), not fixed_budget(C), not exception(oc_1, C).
fired(oc_1, fl_funded(C), general_budget(C)) :- fl_funded(C).
group_effect(fl_funded(C), G, "resources_available_other_uses", at_least_one_decrease, short, invisible, "A") :- fl_funded(C), fl_payer_group(C, G), not tax_named(C).
fl_crowded(C) :- fl_administered(C), fixed_budget(C), holds(budget_fixed(C)), not exception(oc_3, C).
fired(oc_3, fl_crowded(C), fixed_budget(C)) :- fl_crowded(C).
fired(oc_3, fl_crowded(C), budget_fixed(C)) :- fl_crowded(C).
effect(fl_crowded(C), E, "enforcement_cost", decrease, short, invisible, "B") :- fl_crowded(C), enforcer(C, E).
item(fl_crowded(C), "other_work") :- fl_crowded(C).

#show holds/1.
#show fired/3.
#show effect/7.
#show group_effect/7.
#show window/2.
#show item/2.
