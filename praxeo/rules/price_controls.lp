% Thin-slice rule base: price ceilings (handbook catalog 1.2, family PC).
% Input facts, written by praxeo/engine.py from the policy record:
%   ceiling(C).                     component C is a price ceiling
%   bound(C, Actor). protected(C, Actor). excluded(C, Actor).
%   assumption(A).                  an assumption the decider estimated
% The engine adds a choice over assumptions and enumerates answer sets,
% so each conclusion is labelled with the minimal assumption sets it needs
% (an ATMS label, plan 4.4).

{ holds(A) } :- assumption(A).

% PC-1 (plan sketch PR-017): binding, enforced ceiling -> excess demand.
% Unless: not binding (the binding assumption), or an explicit exception.
excess_demand(C) :- ceiling(C), holds(binding(C)), holds(enforced(C)),
                    not exception(pc_1, C).
fired(pc_1, excess_demand(C), binding(C))  :- excess_demand(C).
fired(pc_1, excess_demand(C), enforced(C)) :- excess_demand(C).
fired(pc_1, excess_demand(C), ceiling(C))  :- excess_demand(C).
effect(excess_demand(C), X, "excess_demand", increase, short, invisible, "B") :- excess_demand(C), excluded(C, X).

% PC-3: insiders who obtain the good at the controlled price pay less.
insider_gain(C) :- excess_demand(C), not exception(pc_3, C).
fired(pc_3, insider_gain(C), excess_demand(C)) :- insider_gain(C).
effect(insider_gain(C), P, "price_paid", decrease, medium, visible, "B") :- insider_gain(C), protected(C, P).

% PC-3 (outsiders) with RS-4: excluded seekers bid up uncovered substitutes.
outsider_price(C) :- excess_demand(C), holds(substitutes(C)), not exception(pc_3, C).
fired(pc_3, outsider_price(C), excess_demand(C)) :- outsider_price(C).
fired(rs_4, outsider_price(C), substitutes(C))   :- outsider_price(C).
effect(outsider_price(C), X, "price_paid", increase, long, invisible, "B") :- outsider_price(C), excluded(C, X).

% PC-5: resources move to uncontrolled uses -> quantity supplied falls.
% Unless: the resources have no other use (the alternative_uses assumption).
supply_falls(C) :- excess_demand(C), holds(alternative_uses(C)), not exception(pc_5, C).
fired(pc_5, supply_falls(C), excess_demand(C))    :- supply_falls(C).
fired(pc_5, supply_falls(C), alternative_uses(C)) :- supply_falls(C).
effect(supply_falls(C), B, "quantity_supplied", decrease, long, invisible, "B") :- supply_falls(C), bound(C, B).

% RS-5: owners move units out of the rule's reach (conversion, sale to owner-occupiers).
reclassify(C) :- excess_demand(C), holds(alternative_uses(C)), not exception(rs_5, C).
fired(rs_5, reclassify(C), excess_demand(C))    :- reclassify(C).
fired(rs_5, reclassify(C), alternative_uses(C)) :- reclassify(C).
effect(reclassify(C), B, "reclassification", increase, long, invisible, "B") :- reclassify(C), bound(C, B).

% PC-7: the benefit is tied to holding the tenancy and cannot be sold -> insiders move less.
turnover_falls(C) :- excess_demand(C), holds(nontransferable(C)), not exception(pc_7, C).
fired(pc_7, turnover_falls(C), excess_demand(C))   :- turnover_falls(C).
fired(pc_7, turnover_falls(C), nontransferable(C)) :- turnover_falls(C).
effect(turnover_falls(C), P, "turnover", decrease, medium, invisible, "B") :- turnover_falls(C), protected(C, P).

#show holds/1.
#show fired/3.
#show effect/7.
