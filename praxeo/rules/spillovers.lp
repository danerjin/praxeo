% Wider tax and tariff patterns (handbook catalog 1.4): TX-4, TX-9, OC-3, OC-4, RS-1, RS-4, RS-5, RS-6, RS-7,
% RS-15 (with OC-2), SB-4, TS-1, TS-2, CR-4c and CR-9 (derived demand). They build on the conclusions in taxes.lp
% (collected, wedge, tariff_bites, protected_sellers, passes_down, exempt_squeeze) and share its input facts.
% Further input facts, written by praxeo/engine.py from the policy record (all optional unless noted):
%   taxpayer(C, A).                 who funds new administration (default taxpayers)       (OC-3)
%   foreign_seller(C, A).           foreign sellers of the tariffed good (default sellers.foreign)  (OC-4)
%   input_supplier(C, A).           suppliers of inputs to the protected domestic producers  (CR-9)
%   seller_owner(C, A).             owners of the protected domestic producers               (SB-4)
%   downstream_owner(C, A, O).      owners of the downstream users A                         (SB-4)
%   downstream_exporter(C, A, E).   the exporting part E of the downstream users A           (RS-6)
%   renewable(C).                   the gain depends on a later decision (renewal, review)   (RS-7, TS-2)
%   definition_line(C).             the definitions or exemptions draw a line between covered and uncovered goods  (RS-5)
%   relief_applicant(C, A).         who may apply for discretionary relief (exclusion, waiver)  (RS-15)
%   downstream_worker(C, A, W).     employees W of the downstream users A                    (RS-6, group sign)
% Signs are relative to the no-policy counterfactual. Each rule has an exception/2 default.

% The burden bites: a per-unit tax with a wedge (TX-2), or a tariff that foreign sellers do not absorb (TX-7).
tx_burden(C) :- wedge(C).
tx_burden(C) :- tariff_bites(C).
fired(tx_2, tx_burden(C), wedge(C))        :- tx_burden(C), tax(C).
fired(tx_7, tx_burden(C), tariff_bites(C)) :- tx_burden(C), tariff(C).

% OC-3: a tax or tariff must be administered; the cost falls on the enforcement agency (Tier A). If the budget rises
% with the new task, taxpayers fund it and OC-1 applies. From a fixed budget the pattern gives a group sign, so
% nothing is derived for that funding.
tx_administered(C) :- collected(C), not exception(oc_3, C).
fired(oc_3, tx_administered(C), collected(C)) :- tx_administered(C).
effect(tx_administered(C), R, "enforcement_cost", increase, short, invisible, "A") :- tx_administered(C), revenue(C, R).
tx_budget_funded(C) :- tx_administered(C), holds(enforcement_budget_raised(C)).
fired(oc_3, tx_budget_funded(C), tx_administered(C))              :- tx_budget_funded(C).
fired(oc_3, tx_budget_funded(C), enforcement_budget_raised(C)) :- tx_budget_funded(C).
fired(oc_1, tx_budget_funded(C), tx_administered(C))              :- tx_budget_funded(C).
effect(tx_budget_funded(C), T, "resources_available_other_uses", decrease, short, invisible, "B") :- tx_budget_funded(C), taxpayer(C, T).

% OC-4: exchanges that the burden prices out are not made, and both parties lose them. Unless the exchange is lost to
% a better offer the policy creates elsewhere (exception).
tx_prevented(C) :- tx_burden(C), not exception(oc_4, C).
fired(oc_4, tx_prevented(C), tx_burden(C)) :- tx_prevented(C).
effect(tx_prevented(C), X, "quantity_traded", decrease, short, invisible, "B") :- tx_prevented(C), buyer(C, X), not importer(C, X).
effect(tx_prevented(C), X, "quantity_traded", decrease, short, invisible, "B") :- tx_prevented(C), tariff(C), foreign_seller(C, X).
effect(tx_prevented(C), X, "quantity_traded", decrease, short, invisible, "B") :- tx_prevented(C), tax(C), seller(C, X), not bound(C, X).

% TX-9: when the taxed quantity falls (TX-2), revenue is less than the rate times the pre-tax base. Unless the tax is
% ad valorem on a price the tax itself pushes up, or the revenue is returned to the same buyers (exception).
tx_short_of_static(C) :- tx_burden(C), not exception(tx_9, C).
fired(tx_9, tx_short_of_static(C), tx_burden(C)) :- tx_short_of_static(C).
effect(tx_short_of_static(C), R, "tax_revenue_vs_static_projection", decrease, short, invisible, "B") :- tx_short_of_static(C), revenue(C, R).

% TX-4 with RS-5: where the definitions draw a line between covered and uncovered goods, goods are reshaped to fall on
% the uncovered side, if reshaping costs less than the burden for some actors.
tx_reshaped(C) :- tx_burden(C), definition_line(C), holds(reshaping_pays(C)), not exception(rs_5, C).
fired(rs_5, tx_reshaped(C), tx_burden(C))             :- tx_reshaped(C).
fired(rs_5, tx_reshaped(C), definition_line(C))    :- tx_reshaped(C).
fired(tx_4, tx_reshaped(C), reshaping_pays(C))     :- tx_reshaped(C).
effect(tx_reshaped(C), X, "reclassification", increase, short, invisible, "B") :- tx_reshaped(C), bound(C, X).
effect(tx_reshaped(C), X, "reclassification", increase, short, invisible, "B") :- tx_reshaped(C), buyer(C, X).

% RS-15 with OC-2: relief granted case by case, and worth more than its fee, is allocated by non-price criteria; applying
% costs time; applicants lobby, as do those who gain when relief is denied (the protected producers).
tx_rationed(C) :- tx_burden(C), relief_applicant(C, _), holds(relief_discretionary(C)), holds(relief_valuable(C)), not exception(rs_15, C).
fired(rs_15, tx_rationed(C), tx_burden(C))                :- tx_rationed(C).
fired(rs_15, tx_rationed(C), relief_discretionary(C))  :- tx_rationed(C).
fired(rs_15, tx_rationed(C), relief_valuable(C))       :- tx_rationed(C).
fired(oc_2, tx_rationed(C), relief_discretionary(C))   :- tx_rationed(C).
effect(tx_rationed(C), A, "allocation_by_non_price_criteria", increase, short, invisible, "B") :- tx_rationed(C), relief_applicant(C, A).
effect(tx_rationed(C), A, "compliance_cost", increase, short, invisible, "B")                  :- tx_rationed(C), relief_applicant(C, A).
tx_lobbies_users(C)   :- tx_rationed(C).
fired(rs_15, tx_lobbies_users(C), tx_rationed(C))   :- tx_lobbies_users(C), tx_rationed(C).
tx_lobbies_sellers(C) :- tx_rationed(C), protected_sellers(C).
fired(rs_15, tx_lobbies_sellers(C), tx_rationed(C)) :- tx_lobbies_sellers(C), tx_rationed(C), protected_sellers(C).

% RS-7: a gain concentrated on an identifiable group that depends on a later decision (renewal) draws lobbying; so does a
% concentrated harm (the users who cannot pass the cost on). Assumes each group can organize. Unless the question was
% contested in the counterfactual too (exception).
tx_lobbies_sellers(C) :- protected_sellers(C), renewable(C), holds(beneficiaries_organize(C)), not exception(rs_7, C).
fired(rs_7, tx_lobbies_sellers(C), protected_sellers(C))      :- tx_lobbies_sellers(C), protected_sellers(C), renewable(C), holds(beneficiaries_organize(C)), not exception(rs_7, C).
fired(rs_7, tx_lobbies_sellers(C), beneficiaries_organize(C)) :- tx_lobbies_sellers(C), protected_sellers(C), renewable(C), holds(beneficiaries_organize(C)), not exception(rs_7, C).
tx_lobbies_users(C) :- exempt_squeeze(C), renewable(C), holds(harmed_organize(C)), not exception(rs_7, C).
fired(rs_7, tx_lobbies_users(C), exempt_squeeze(C))   :- tx_lobbies_users(C), exempt_squeeze(C), renewable(C), holds(harmed_organize(C)), not exception(rs_7, C).
fired(rs_7, tx_lobbies_users(C), harmed_organize(C))  :- tx_lobbies_users(C), exempt_squeeze(C), renewable(C), holds(harmed_organize(C)), not exception(rs_7, C).
effect(tx_lobbies_sellers(C), S, "lobbying_effort", increase, medium, invisible, "B") :- tx_lobbies_sellers(C), domestic_seller(C, S).
effect(tx_lobbies_users(C), A, "lobbying_effort", increase, medium, invisible, "B")   :- tx_lobbies_users(C), relief_applicant(C, A).
effect(tx_lobbies_users(C), A, "lobbying_effort", increase, medium, invisible, "B")   :- tx_lobbies_users(C), exempt_squeeze(C), downstream(C, A, _, exempt).

% TS-2 with TX-7: if the protected producers expect the protection to be extended, they invest in capacity now.
tx_invests(C) :- protected_sellers(C), renewable(C), holds(expects_extension(C)), not exception(ts_2, C).
fired(ts_2, tx_invests(C), protected_sellers(C)) :- tx_invests(C).
fired(ts_2, tx_invests(C), expects_extension(C)) :- tx_invests(C).
effect(tx_invests(C), S, "investment_target", increase, medium, invisible, "B") :- tx_invests(C), domestic_seller(C, S).

% CR-9 (derived demand): protected producers that sell more buy more of their inputs.
tx_inputs_demanded(C) :- protected_sellers(C), input_supplier(C, _), not exception(cr_9, C).
fired(cr_9, tx_inputs_demanded(C), protected_sellers(C)) :- tx_inputs_demanded(C).
effect(tx_inputs_demanded(C), I, "quantity_demanded", increase, short, invisible, "B") :- tx_inputs_demanded(C), input_supplier(C, I).

% SB-4: a lasting change in the return on assets in slow supply is capitalized in their value from the time it is
% expected. Owners of the protected producers gain; owners of the users whose return falls (no pass-through) lose.
tx_capitalized_gain(C) :- protected_sellers(C), holds(asset_supply_slow(C)), holds(expected_to_last(C)), not exception(sb_4, C).
fired(sb_4, tx_capitalized_gain(C), protected_sellers(C)) :- tx_capitalized_gain(C).
fired(sb_4, tx_capitalized_gain(C), asset_supply_slow(C)) :- tx_capitalized_gain(C).
fired(sb_4, tx_capitalized_gain(C), expected_to_last(C))  :- tx_capitalized_gain(C).
effect(tx_capitalized_gain(C), O, "asset_value", increase, short, invisible, "B") :- tx_capitalized_gain(C), seller_owner(C, O).
tx_capitalized_loss(C) :- exempt_squeeze(C), holds(asset_supply_slow(C)), holds(expected_to_last(C)), not exception(sb_4, C).
fired(sb_4, tx_capitalized_loss(C), exempt_squeeze(C))    :- tx_capitalized_loss(C).
fired(sb_4, tx_capitalized_loss(C), asset_supply_slow(C)) :- tx_capitalized_loss(C).
fired(sb_4, tx_capitalized_loss(C), expected_to_last(C))  :- tx_capitalized_loss(C).
effect(tx_capitalized_loss(C), O, "asset_value", decrease, short, invisible, "B") :- tx_capitalized_loss(C), downstream(C, A, _, exempt), downstream_owner(C, A, O).

% RS-1: users that cannot pass the cost on supply less; their buyers turn to the uncovered substitute, if its supply can expand.
tx_turn_to_substitutes(C) :- exempt_squeeze(C), holds(substitute_supply_expands(C)), not exception(rs_1, C).
fired(rs_1, tx_turn_to_substitutes(C), exempt_squeeze(C))            :- tx_turn_to_substitutes(C).
fired(rs_1, tx_turn_to_substitutes(C), substitute_supply_expands(C)) :- tx_turn_to_substitutes(C).
effect(tx_turn_to_substitutes(C), B, "quantity_substitute", increase, medium, invisible, "B") :- tx_turn_to_substitutes(C), downstream(C, _, B, exempt), B != "".

% RS-6 after RS-14: exporters among the users sell at world prices and cannot pass the cost on, so they supply less.
tx_exporters_squeezed(C) :- passes_down(C), downstream_exporter(C, _, _), holds(exporters_price_takers(C)), not exception(rs_6, C).
fired(rs_6, tx_exporters_squeezed(C), passes_down(C))            :- tx_exporters_squeezed(C).
fired(rs_6, tx_exporters_squeezed(C), exporters_price_takers(C)) :- tx_exporters_squeezed(C).
effect(tx_exporters_squeezed(C), E, "quantity_supplied", decrease, medium, invisible, "B") :- tx_exporters_squeezed(C), downstream_exporter(C, _, E).

% RS-4 with RS-6 and TS-1: users whose return falls and who can produce abroad when they next replace plant move capital
% out; durable capital wears out slowly, so the fall in the stock comes late.
tx_capital_moves(C) :- exempt_squeeze(C), holds(can_relocate_capital(C)), not exception(rs_4, C).
fired(rs_6, tx_capital_moves(C), exempt_squeeze(C))       :- tx_capital_moves(C).
fired(rs_4, tx_capital_moves(C), can_relocate_capital(C)) :- tx_capital_moves(C).
fired(ts_1, tx_capital_moves(C), exempt_squeeze(C))       :- tx_capital_moves(C).
effect(tx_capital_moves(C), A, "capital_stock_target", decrease, long, invisible, "B") :- tx_capital_moves(C), downstream(C, A, _, exempt).

% CR-4c: buyers whose price rises through RS-14 take fewer units.
tx_buyers_cut_back(C) :- passes_down(C), not exception(cr_4, C).
fired(cr_4, tx_buyers_cut_back(C), passes_down(C)) :- tx_buyers_cut_back(C).
effect(tx_buyers_cut_back(C), B, "quantity_demanded", decrease, medium, invisible, "B") :- tx_buyers_cut_back(C), downstream(C, _, B, same).

% RS-6 after RS-14: users that sell less may cut staff or hours, so their employees' sign is the group at_least_one_decrease
% over employment and hours_worked (a member alone would claim more than the rule licenses).
tx_workers_cut(C) :- exempt_squeeze(C), not exception(rs_6, C).
fired(rs_6, tx_workers_cut(C), exempt_squeeze(C)) :- tx_workers_cut(C).
group_effect(tx_workers_cut(C), W, "employment,hours_worked", at_least_one_decrease, medium, invisible, "B") :- tx_workers_cut(C), downstream_exempt_worker(C, W).
downstream_exempt_worker(C, W) :- downstream(C, A, _, exempt), downstream_worker(C, A, W).
