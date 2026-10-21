% Thin-slice rule base: per-unit taxes and tariffs (handbook catalog 1.4, family TX, plus RS-14).
% Input facts, written by praxeo/engine.py from the policy record:
%   tax(C).                         component C is a per-unit tax
%   tariff(C).                      component C is a tariff
%   bound(C, Actor).                who must pay (the importers, for a tariff)
%   buyer(C, A). seller(C, A).      buyers and sellers of the taxed good
%   domestic_seller(C, A).          domestic producers of the good a tariff protects
%   importer(C, A). revenue(C, A).  importers, and the agency that collects
%   exporter(C, A). exporter_worker(C, A).  export industries and their workers (TX-8)
%   downstream(C, A, B, K).         A use the good as an input, sell to B; K is `same` when their
%                                   competitors face the same cost, `exempt` when competitors do not (RS-14)
%   domestic_seller_worker(C, A).   employees of the protected domestic producers (optional)
%   downstream_worker(C, A, W).     employees W of the downstream users A (optional)
%   rate_rise(C).                   the measure raises the rate of an existing tax (TX-1, 1.1)
%   announced(C).                   the measure was announced before it takes effect (RS-8; see timing.lp)
%   assumption(A).                  an assumption the decider estimated
% The choice over assumptions is repeated here so that the file stands alone; the same rule in
% price_controls.lp adds no answer sets. Signs are relative to the no-policy counterfactual.

{ holds(A) } :- assumption(A).

% TX-1: a tax that is imposed and collected takes resources and yields revenue (Tier A, given collection).
collected(C) :- tax(C), not exception(tx_1, C).
collected(C) :- tariff(C), not exception(tx_1, C).
fired(tx_1, collected(C), tax(C))    :- collected(C), tax(C).
fired(tx_1, collected(C), tariff(C)) :- collected(C), tariff(C).
% A new tax yields revenue (Tier A). A rise in the rate of an existing tax (rate_rise) yields more revenue only if the base does
% not fall enough to offset it: Tier B, with that premise (TX-1, 1.1).
effect(collected(C), R, "tax_revenue", increase, short, visible, "A") :- collected(C), revenue(C, R), not rate_rise(C).
revenue_rises(C) :- collected(C), rate_rise(C), holds(revenue_base_holds(C)).
fired(tx_1, revenue_rises(C), collected(C))          :- revenue_rises(C).
fired(tx_1, revenue_rises(C), revenue_base_holds(C)) :- revenue_rises(C).
effect(revenue_rises(C), R, "tax_revenue", increase, short, visible, "B") :- revenue_rises(C), revenue(C, R).
% TX-5: whoever must record, file or collect bears a compliance cost (Tier A, given positive compliance work).
tx_files(C) :- collected(C), not exception(tx_5, C).
fired(tx_5, tx_files(C), collected(C)) :- tx_files(C).
effect(tx_files(C), B, "compliance_cost", increase, short, invisible, "A") :- tx_files(C), bound(C, B).
% Who bears it: the importers pay a tariff outright; the buyers and sellers of a taxed good bear it as TX-2 / TX-7 say.
effect(collected(C), B, "resources_available_other_uses", decrease, short, invisible, "A") :- collected(C), tariff(C), bound(C, B).
bears_buyer(C) :- collected(C), tax(C), holds(buyers_bear(C)).
fired(tx_1, bears_buyer(C), collected(C))   :- bears_buyer(C), tax(C).
fired(tx_2, bears_buyer(C), buyers_bear(C)) :- bears_buyer(C), tax(C).
bears_buyer(C) :- collected(C), tariff_bites(C).
fired(tx_1, bears_buyer(C), collected(C))     :- bears_buyer(C), tariff(C).
fired(tx_7, bears_buyer(C), tariff_bites(C))  :- bears_buyer(C), tariff(C).
bears_seller(C) :- collected(C), tax(C), holds(sellers_bear(C)).
fired(tx_1, bears_seller(C), collected(C))    :- bears_seller(C).
fired(tx_2, bears_seller(C), sellers_bear(C)) :- bears_seller(C).
effect(bears_buyer(C),  X, "resources_available_other_uses", decrease, short, invisible, "A") :- bears_buyer(C), buyer(C, X).
effect(bears_seller(C), X, "resources_available_other_uses", decrease, short, invisible, "A") :- bears_seller(C), seller(C, X).

% TX-2: a per-unit tax opens a wedge; at least one side responds by trading less.
% Who bears it is not fixed by the rule (its Note): the two incidence premises stand in for DM-1.
wedge(C) :- tax(C), holds(quantity_responds(C)), not exception(tx_2, C).
fired(tx_2, wedge(C), tax(C))               :- wedge(C).
fired(tx_2, wedge(C), quantity_responds(C)) :- wedge(C).
buyers_pay(C) :- wedge(C), holds(buyers_bear(C)).
fired(tx_2, buyers_pay(C), wedge(C))        :- buyers_pay(C).
fired(tx_2, buyers_pay(C), buyers_bear(C))  :- buyers_pay(C).
sellers_lose(C) :- wedge(C), holds(sellers_bear(C)).
fired(tx_2, sellers_lose(C), wedge(C))        :- sellers_lose(C).
fired(tx_2, sellers_lose(C), sellers_bear(C)) :- sellers_lose(C).
effect(buyers_pay(C),   X, "price_paid", increase, short, visible, "B")             :- buyers_pay(C), buyer(C, X).
effect(sellers_lose(C), X, "net_price_received", decrease, short, invisible, "B")   :- sellers_lose(C), seller(C, X).
effect(wedge(C),        X, "quantity_traded", decrease, short, invisible, "B")      :- wedge(C), bound(C, X).

% TX-7: a tariff that is not absorbed by foreign sellers raises the buyers' price; with domestic substitutes
% the protected producers' price and quantity rise. Unless domestic output pays the same tax (exception).
tariff_bites(C) :- tariff(C), holds(binding(C)), not exception(tx_7, C).
fired(tx_7, tariff_bites(C), tariff(C))  :- tariff_bites(C).
fired(tx_7, tariff_bites(C), binding(C)) :- tariff_bites(C).
effect(tariff_bites(C), X, "price_paid", increase, short, invisible, "B") :- tariff_bites(C), buyer(C, X).
protected_sellers(C) :- tariff_bites(C), holds(domestic_substitutes(C)).
fired(tx_7, protected_sellers(C), tariff_bites(C))        :- protected_sellers(C).
fired(tx_7, protected_sellers(C), domestic_substitutes(C)) :- protected_sellers(C).
effect(protected_sellers(C), X, "net_price_received", increase, short, visible, "B") :- protected_sellers(C), domestic_seller(C, X).
effect(protected_sellers(C), X, "quantity_supplied", increase, short, visible, "B")  :- protected_sellers(C), domestic_seller(C, X).
% TX-7 with LW-4: mills that sell more use more labor. Spare capacity may be used first through shifts and overtime, so the rule
% licenses only that headcount or hours rise: the group at_least_one_increase.
group_effect(protected_sellers(C), W, "employment,hours_worked", at_least_one_increase, short, visible, "B") :- protected_sellers(C), domestic_seller_worker(C, W).

% TX-2 for a tariff: the tax on imports shrinks the quantity imported.
imports_fall(C) :- tariff_bites(C), not exception(tx_2, C).
fired(tx_2, imports_fall(C), tariff_bites(C)) :- imports_fall(C).
effect(imports_fall(C), X, "quantity_traded", decrease, short, invisible, "B") :- imports_fall(C), importer(C, X).

% TX-8: fewer imports mean foreigners earn less of the domestic currency, so they buy fewer of its exports.
% Assumes no offset by capital flows or other adjustments in the period.
exports_fall(C) :- imports_fall(C), holds(no_offset(C)), not exception(tx_8, C).
fired(tx_8, exports_fall(C), imports_fall(C)) :- exports_fall(C).
fired(tx_8, exports_fall(C), no_offset(C))    :- exports_fall(C).
effect(exports_fall(C), X, "quantity_supplied", decrease, medium, invisible, "B") :- exports_fall(C), exporter(C, X).
% TX-8 names employment; sellers that sell less may cut staff or hours, so WE-013 (C-32, OC-5) records the labor effect as the
% group at_least_one_decrease over employment and hours_worked, which says no more than the rule licenses.
group_effect(exports_fall(C), X, "employment,hours_worked", at_least_one_decrease, medium, invisible, "B") :- exports_fall(C), exporter_worker(C, X).

% RS-14: a higher cost of an input is passed down to the output, if the input cannot be replaced at the
% old cost. Where competitors face the same cost the output's price rises; where competitors are exempt
% (RS-6) the exposed sellers sell less.
input_cost_up(C) :- tariff_bites(C).
fired(tx_7, input_cost_up(C), tariff_bites(C)) :- input_cost_up(C), tariff(C).
input_cost_up(C) :- buyers_pay(C).
fired(tx_2, input_cost_up(C), buyers_pay(C))   :- input_cost_up(C), tax(C).
passes_down(C) :- input_cost_up(C), holds(input_not_replaceable(C)), not exception(rs_14, C).
fired(rs_14, passes_down(C), input_cost_up(C))          :- passes_down(C).
fired(rs_14, passes_down(C), input_not_replaceable(C))  :- passes_down(C).
effect(passes_down(C), B, "price_paid", increase, medium, invisible, "B") :- passes_down(C), downstream(C, _, B, same).
exempt_squeeze(C) :- passes_down(C), holds(competitors_exempt(C)), downstream(C, _, _, exempt).
fired(rs_14, exempt_squeeze(C), passes_down(C))          :- exempt_squeeze(C).
fired(rs_14, exempt_squeeze(C), competitors_exempt(C))   :- exempt_squeeze(C).
effect(exempt_squeeze(C), A, "quantity_supplied", decrease, medium, invisible, "B") :- exempt_squeeze(C), downstream(C, A, _, exempt).

#show holds/1.
#show fired/3.
#show effect/7.
#show group_effect/7.
#show window/2.
#show item/2.
