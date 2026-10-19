% Prohibitions (handbook catalog 1.4): EN-7 (trade moves underground), EN-8 (concentrated forms), EN-10 (penalty records),
% with RS-1, RS-3, RS-4, RS-5, RS-7, RS-8, RS-10, OC-1, OC-3, OC-4, SB-4 and TX-10 where a ban brings them in. Developed on
% WE-017. Input facts, written by praxeo/engine.py from the policy record:
%   prohibition(C).                   component C bans making, selling or possessing a good
%   bound(C, A).                      the legal sellers until now (shops)
%   pr_buyer(C, A).                   its current buyers (users)
%   pr_informal_seller(C, A). pr_informal_buyer(C, A).   who sells and buys it outside the law (defaults: the buyers for
%                                     the informal buyers; no informal-seller row without the role)
%   pr_importer(C, A). pr_prospective(C, A). pr_convicted(C, A).  legal importers; would-be users; those convicted
%   mobile_buyer(C, A). neighbor_seller(C, A).            buyers who can buy where it stays legal, and the sellers there
%   pr_substitute_seller(C, A).       sellers of goods just outside the ban's definitions (RS-5)
%   definition_line(C). announced(C). volume_penalties(C). stocks_destroyed(C). taxed_before(C). practice_ban(C).
%   fees_to_budget(C).                fees or fines from the measure are paid into the budget that funds its enforcement
%   enforcer(C, A). general_budget(C). tax_named(C). taxpayer(C, A). pr_payer_group(C, "a,b,c"). revenue(C, A).
% Every rule is monotone in holds/1: it negates only plain facts.

{ holds(A) } :- assumption(A).

% EN-7 with CR-1: legal trade stops where the legal sellers comply (enforced): legal sales, legal sellers, legal imports and
% the staff and value of the legal sellers' businesses, where the businesses cannot turn to other products (no_other_use).
pr_legal_stops(C) :- prohibition(C), holds(enforced(C)), not exception(en_7, C).
fired(en_7, pr_legal_stops(C), enforced(C)) :- pr_legal_stops(C).
effect(pr_legal_stops(C), B, "quantity_traded", decrease, short, visible, "B")   :- pr_legal_stops(C), bound(C, B).
effect(pr_legal_stops(C), X, "quantity_traded", decrease, short, visible, "B")   :- pr_legal_stops(C), pr_buyer(C, X).
effect(pr_legal_stops(C), I, "quantity_traded", decrease, short, invisible, "B") :- pr_legal_stops(C), pr_importer(C, I).
pr_specific(C) :- pr_legal_stops(C), holds(no_other_use(C)), not exception(sb_4, C).
fired(cr_1, pr_specific(C), pr_legal_stops(C)) :- pr_specific(C).
fired(sb_4, pr_specific(C), no_other_use(C))   :- pr_specific(C).
% Fewer legal sellers only where they cannot turn to other products (found out of sample on WE-018 and WE-050, where shops
% and importers keep selling the rest of their range).
effect(pr_specific(C), B, "number_of_sellers", decrease, short, visible, "B") :- pr_specific(C), bound(C, B).
effect(pr_specific(C), B, "employment", decrease, short, invisible, "B")  :- pr_specific(C), bound(C, B).
effect(pr_specific(C), B, "asset_value", decrease, short, invisible, "B") :- pr_specific(C), bound(C, B).
% OC-1: stocks that must be destroyed without compensation are a loss to their owners (Tier A, given the ban).
pr_stocks_lost(C) :- prohibition(C), stocks_destroyed(C), not exception(oc_1, C).
fired(oc_1, pr_stocks_lost(C), stocks_destroyed(C)) :- pr_stocks_lost(C).
effect(pr_stocks_lost(C), B, "resources_available_other_uses", decrease, short, invisible, "A") :- pr_stocks_lost(C), bound(C, B).
% RS-8 with the destruction rule: compliant sellers run their stock down by the effective date.
pr_run_down(C) :- pr_legal_stops(C), stocks_destroyed(C).
fired(rs_8, pr_run_down(C), pr_legal_stops(C)) :- pr_run_down(C).
effect(pr_run_down(C), B, "inventory_held", decrease, short, invisible, "B") :- pr_run_down(C), bound(C, B).

% EN-7 with RS-3: where some buyers keep valuing the good (demand_persists) and enforcement is imperfect (evasion), trade moves
% outside the law; RS-10 applies to it: search, quality variability and information, disputes outside the courts.
% Only an enforced ban drives trade underground: unenforced, it carries on openly (found out of sample on WE-037). A ban on a
% practice of legal firms (practice_ban: hosting data abroad) makes evasion a legal breach by those firms, not an informal
% market (found out of sample on WE-053).
pr_underground(C) :- pr_legal_stops(C), holds(demand_persists(C)), holds(evasion(C)), not practice_ban(C), not exception(rs_3, C).
fired(en_7, pr_underground(C), pr_legal_stops(C))  :- pr_underground(C).
fired(en_7, pr_underground(C), demand_persists(C)) :- pr_underground(C).
fired(rs_3, pr_underground(C), evasion(C))         :- pr_underground(C).
effect(pr_underground(C), S, "informal_activity", increase, short, invisible, "B")               :- pr_underground(C), pr_informal_seller(C, S).
effect(pr_underground(C), X, "search_cost", increase, short, invisible, "B")                     :- pr_underground(C), pr_informal_buyer(C, X).
effect(pr_underground(C), X, "quality_variability", increase, short, invisible, "B")             :- pr_underground(C), pr_informal_buyer(C, X).
effect(pr_underground(C), X, "quality_information", decrease, short, invisible, "B")             :- pr_underground(C), pr_informal_buyer(C, X).
effect(pr_underground(C), X, "disputes_settled_outside_courts", increase, short, invisible, "B") :- pr_underground(C), pr_informal_buyer(C, X).
effect(pr_underground(C), S, "disputes_settled_outside_courts", increase, short, invisible, "B") :- pr_underground(C), pr_informal_seller(C, S).

pr_breach(C) :- pr_legal_stops(C), practice_ban(C), holds(evasion(C)), not exception(rs_3, C).
fired(rs_3, pr_breach(C), pr_legal_stops(C)) :- pr_breach(C).
fired(rs_3, pr_breach(C), evasion(C))        :- pr_breach(C).
effect(pr_breach(C), B, "legal_breach", increase, short, invisible, "B") :- pr_breach(C), bound(C, B).

% EN-7 with CR-7: where an informal trade exists and enforcement is a real risk to it (enforcement_risk), its price includes
% compensation for that risk: buyers pay more per unit, and fewer buy over time (CR-4, LW-3), current and would-be buyers.
% Without an informal trade there is no risk price (found out of sample on WE-050: a new car cannot be registered).
pr_risk_price(C) :- pr_underground(C), holds(enforcement_risk(C)), not exception(en_7, C).
fired(en_7, pr_risk_price(C), pr_underground(C))   :- pr_risk_price(C).
fired(cr_7, pr_risk_price(C), enforcement_risk(C)) :- pr_risk_price(C).
effect(pr_risk_price(C), X, "price_paid", increase, short, invisible, "B")         :- pr_risk_price(C), pr_buyer(C, X).
effect(pr_risk_price(C), X, "quantity_demanded", decrease, short, invisible, "B")  :- pr_risk_price(C), pr_buyer(C, X).
effect(pr_risk_price(C), P, "quantity_demanded", decrease, long, invisible, "B")   :- pr_risk_price(C), pr_prospective(C, P).

% EN-8: where penalties scale with bulk (volume_penalties) and concentrates are easy to make (concentrate_easy), the informal
% trade shifts toward concentrated forms.
pr_concentrate(C) :- pr_underground(C), volume_penalties(C), holds(concentrate_easy(C)), not exception(en_8, C).
fired(en_8, pr_concentrate(C), pr_underground(C))    :- pr_concentrate(C).
fired(en_8, pr_concentrate(C), concentrate_easy(C))  :- pr_concentrate(C).
effect(pr_concentrate(C), S, "share_concentrated_forms", increase, medium, invisible, "B") :- pr_concentrate(C), pr_informal_seller(C, S).

% EN-10: where convictions are recorded and checked by employers (records_checked), those convicted work less in the long run.
pr_records(C) :- pr_risk_price(C), pr_convicted(C, _), holds(records_checked(C)), not exception(en_10, C).
fired(en_10, pr_records(C), pr_risk_price(C))    :- pr_records(C).
fired(en_10, pr_records(C), records_checked(C))  :- pr_records(C).
effect(pr_records(C), V, "employment", decrease, long, invisible, "B") :- pr_records(C), pr_convicted(C, V).

% RS-1: buyers turn to legal substitutes they find acceptable (buyer_substitutes).
pr_substitute(C) :- prohibition(C), holds(buyer_substitutes(C)), not exception(rs_1, C).
fired(rs_1, pr_substitute(C), buyer_substitutes(C)) :- pr_substitute(C).
effect(pr_substitute(C), X, "quantity_substitute", increase, short, invisible, "B") :- pr_substitute(C), pr_buyer(C, X).

% RS-4: buyers who can reach a place where the good stays legal (cross_border_feasible) buy there, and the sellers there gain
% them; finding and carrying it costs them time (OC-2).
pr_cross(C) :- prohibition(C), mobile_buyer(C, _), holds(cross_border_feasible(C)), not exception(rs_4, C).
fired(rs_4, pr_cross(C), cross_border_feasible(C)) :- pr_cross(C).
effect(pr_cross(C), M, "cross_border_purchases", increase, short, invisible, "B") :- pr_cross(C), mobile_buyer(C, M).
pr_cross_trip(C) :- pr_cross(C), holds(crossing_extra_trip(C)).
fired(oc_2, pr_cross_trip(C), crossing_extra_trip(C)) :- pr_cross_trip(C).
% The time it costs, only where the crossing is a trip they would not otherwise make (found out of sample on WE-018).
effect(pr_cross_trip(C), M, "search_cost", increase, short, invisible, "B") :- pr_cross_trip(C), mobile_buyer(C, M).
effect(pr_cross(C), N, "quantity_traded", increase, short, invisible, "B")        :- pr_cross(C), neighbor_seller(C, N).

% RS-5: where the ban's definitions draw a line, goods just outside it are sold (reshaping_pays).
pr_reshaped(C) :- prohibition(C), definition_line(C), holds(reshaping_pays(C)), not exception(rs_5, C).
fired(rs_5, pr_reshaped(C), reshaping_pays(C)) :- pr_reshaped(C).
effect(pr_reshaped(C), S, "reclassification", increase, short, invisible, "B") :- pr_reshaped(C), pr_substitute_seller(C, S).
effect(pr_reshaped(C), S, "reclassification", increase, short, invisible, "B") :- pr_reshaped(C), pr_informal_seller(C, S).

% RS-8: buyers who know the date and can store the good (stockpile_ahead) buy more before it.
pr_stock_up(C) :- prohibition(C), announced(C), holds(stockpile_ahead(C)), not exception(rs_8, C).
fired(rs_8, pr_stock_up(C), announced(C))        :- pr_stock_up(C).
fired(rs_8, pr_stock_up(C), stockpile_ahead(C))  :- pr_stock_up(C).
window(pr_stock_up(C), announcement) :- pr_stock_up(C).
effect(pr_stock_up(C), X, "quantity_demanded", increase, short, invisible, "B") :- pr_stock_up(C), pr_buyer(C, X).

% TX-10: where the good was taxed (taxed_before), legal sales that stop no longer pay the tax.
pr_revenue(C) :- pr_legal_stops(C), taxed_before(C), not exception(tx_10, C).
fired(tx_10, pr_revenue(C), pr_legal_stops(C)) :- pr_revenue(C).
effect(pr_revenue(C), R, "tax_revenue", decrease, short, invisible, "B") :- pr_revenue(C), revenue(C, R).

% RS-7: a concentrated harm draws lobbying for repeal by those who can organize (can_organize): the former legal sellers.
pr_lobby(C) :- prohibition(C), holds(can_organize(C)), not exception(rs_7, C).
fired(rs_7, pr_lobby(C), can_organize(C)) :- pr_lobby(C).
effect(pr_lobby(C), B, "lobbying_effort", increase, medium, invisible, "B") :- pr_lobby(C), bound(C, B).
% The buyers lobby only where they too have a concentrated stake and can organize (buyers_organize; found out of sample on
% WE-018: nobody campaigns over a 2-cent bag).
pr_buyers_lobby(C) :- prohibition(C), holds(buyers_organize(C)), not exception(rs_7, C).
fired(rs_7, pr_buyers_lobby(C), buyers_organize(C)) :- pr_buyers_lobby(C).
effect(pr_buyers_lobby(C), X, "lobbying_effort", increase, medium, invisible, "B") :- pr_buyers_lobby(C), pr_buyer(C, X).

% OC-3: a ban must be enforced (Tier A); with a raised general budget, OC-1's payers bear it (the payer group unless a tax
% is named).
pr_administered(C) :- prohibition(C), not exception(oc_3, C).
fired(oc_3, pr_administered(C), prohibition(C)) :- pr_administered(C).
effect(pr_administered(C), E, "enforcement_cost", increase, short, invisible, "A") :- pr_administered(C), enforcer(C, E).
pr_funded(C) :- pr_administered(C), general_budget(C), not exception(oc_1, C).
fired(oc_1, pr_funded(C), general_budget(C)) :- pr_funded(C).
effect(pr_funded(C), T, "resources_available_other_uses", decrease, short, invisible, "A") :- pr_funded(C), tax_named(C), taxpayer(C, T).
% Not where fees or fines from the measure are paid into the same budget (fees_to_budget): the payers' net is then unsigned
% without a premise on which is larger (OC-1 1.0; found out of sample on WE-053).
group_effect(pr_funded(C), G, "resources_available_other_uses", at_least_one_decrease, short, invisible, "A") :- pr_funded(C), pr_payer_group(C, G), not tax_named(C), not fees_to_budget(C).

#show holds/1.
#show fired/3.
#show effect/7.
#show group_effect/7.
#show window/2.
#show item/2.
