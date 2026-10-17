% Thin-slice rule base: price ceilings (handbook catalog 1.4, family PC).
% Input facts, written by praxeo/engine.py from the policy record:
%   ceiling(C).                     component C is a price ceiling
%   decontrol(C).                   the price of a new contract is free (vacancy decontrol)
%   bound(C, Actor). protected(C, Actor). excluded(C, Actor).
%   assumption(A).                  an assumption the decider estimated
%   plus any facts a reading of an unclear provision adds (engine runs once per reading).
% The engine adds a choice over assumptions and enumerates answer sets,
% so each conclusion is labelled with the minimal assumption sets it needs
% (an ATMS label, plan 4.4).

{ holds(A) } :- assumption(A).

% A binding, enforced ceiling: the premise every pattern below starts from.
binding_cap(C) :- ceiling(C), holds(binding(C)), holds(enforced(C)).
fired(pc_1, binding_cap(C), binding(C))  :- binding_cap(C).
fired(pc_1, binding_cap(C), enforced(C)) :- binding_cap(C).

% PC-1 (plan sketch PR-017): excess demand for new contracts.
% Not where the price of a new contract is free (PC-1 1.4, vacancy decontrol).
excess_demand(C) :- binding_cap(C), not decontrol(C), not exception(pc_1, C).
fired(pc_1, excess_demand(C), binding_cap(C)) :- excess_demand(C).
effect(excess_demand(C), X, "excess_demand", increase, short, invisible, "B") :- excess_demand(C), excluded(C, X).

% PC-3: insiders who hold the good at the controlled price pay less.
insider_gain(C) :- binding_cap(C), not exception(pc_3, C).
fired(pc_3, insider_gain(C), binding_cap(C)) :- insider_gain(C).
effect(insider_gain(C), P, "price_paid", decrease, medium, visible, "B") :- insider_gain(C), protected(C, P).

% PC-3 (outsiders) with RS-4: buyers shut out turn to uncovered substitutes, whose price rises.
outsider_price(C) :- binding_cap(C), holds(substitutes(C)), not exception(pc_3, C).
fired(pc_3, outsider_price(C), binding_cap(C))  :- outsider_price(C).
fired(rs_4, outsider_price(C), substitutes(C))  :- outsider_price(C).
effect(outsider_price(C), X, "price_substitute", increase, long, invisible, "B") :- outsider_price(C), excluded(C, X).

% PC-5: resources move to uncontrolled uses -> quantity supplied falls.
supply_falls(C) :- binding_cap(C), holds(alternative_uses(C)), not exception(pc_5, C).
fired(pc_5, supply_falls(C), binding_cap(C))      :- supply_falls(C).
fired(pc_5, supply_falls(C), alternative_uses(C)) :- supply_falls(C).
effect(supply_falls(C), B, "quantity_supplied", decrease, long, invisible, "B") :- supply_falls(C), bound(C, B).

% RS-5: owners move units out of the rule's reach (conversion, sale to owner-occupiers).
reclassify(C) :- binding_cap(C), holds(alternative_uses(C)), not exception(rs_5, C).
fired(rs_5, reclassify(C), binding_cap(C))      :- reclassify(C).
fired(rs_5, reclassify(C), alternative_uses(C)) :- reclassify(C).
effect(reclassify(C), B, "reclassification", increase, long, invisible, "B") :- reclassify(C), bound(C, B).

% PC-7 (1.4): the benefit is tied to holding the tenancy and cannot be sold -> insiders move less,
% given that buyouts (handing the tenancy back for a payment) stay below the lock-in.
turnover_falls(C) :- binding_cap(C), holds(nontransferable(C)), holds(buyouts_limited(C)), not exception(pc_7, C).
fired(pc_7, turnover_falls(C), binding_cap(C))      :- turnover_falls(C).
fired(pc_7, turnover_falls(C), nontransferable(C))  :- turnover_falls(C).
fired(pc_7, turnover_falls(C), buyouts_limited(C))  :- turnover_falls(C).
effect(turnover_falls(C), P, "turnover", decrease, medium, invisible, "B") :- turnover_falls(C), protected(C, P).

% PC-1 1.4: under vacancy decontrol, seekers' price is signed through the fall in vacancies:
% initial prices of new covered contracts rise.
initial_price(C) :- turnover_falls(C), decontrol(C), not exception(pc_1, C).
fired(pc_1, initial_price(C), turnover_falls(C)) :- initial_price(C).
effect(initial_price(C), X, "price_paid", increase, medium, invisible, "B") :- initial_price(C), excluded(C, X).

% PC-21 (1.4): insiders who keep the unit leave the area less, given that the lock-in
% outweighs moves diverted out of the area by higher free prices.
stay_in_area(C) :- turnover_falls(C), holds(would_leave(C)), holds(lockin_dominates(C)), not exception(pc_21, C).
fired(pc_21, stay_in_area(C), turnover_falls(C))    :- stay_in_area(C).
fired(pc_21, stay_in_area(C), would_leave(C))       :- stay_in_area(C).
fired(pc_21, stay_in_area(C), lockin_dominates(C))  :- stay_in_area(C).
effect(stay_in_area(C), @keepers(P), "relocation_out_of_area", decrease, medium, invisible, "B") :- stay_in_area(C), protected(C, P).

% PC-21 (1.4) subclass split: insiders displaced by conversion or withdrawal leave more
% (their next-best home may be outside the area: the mobility premise).
displaced_leave(C) :- reclassify(C), holds(would_leave(C)), not exception(pc_21, C).
fired(rs_5,  displaced_leave(C), reclassify(C))  :- displaced_leave(C).
fired(pc_21, displaced_leave(C), would_leave(C)) :- displaced_leave(C).
effect(displaced_leave(C), @displaced(P), "relocation_out_of_area", increase, long, invisible, "B") :- displaced_leave(C), protected(C, P).

#show holds/1.
#show fired/3.
#show effect/7.
