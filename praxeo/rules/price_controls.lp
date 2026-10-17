% Thin-slice rule base: price ceilings (handbook catalog 1.4, family PC).
% Input facts, written by praxeo/engine.py from the policy record:
%   ceiling(C).                     component C is a price ceiling
%   decontrol(C).                   the price of a new contract is free (vacancy decontrol)
%   bound(C, Actor). protected(C, Actor). excluded(C, Actor).
%   assumption(A).                  an assumption the decider estimated
%   enforcer(C, Actor).             who administers and enforces the cap (OC-3)
%   neighbor(C, Actor).             buyers in a neighbouring market outside the cap's reach (RS-4), if the record names one
%   taxpayer(C, Actor).             who funds new administration, written only if the record says enforcement is funded
%                                   from the general budget (OC-3, OC-1)
%   announced(C).                   the measure was announced before it takes effect (RS-8; see timing.lp)
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

% PC-7 (1.4), RS-5 and CR-9: holders displaced by conversion or withdrawal are a subclass whose turnover rises
% (the owner's exit ends the lease). The class total of turnover is a CR-12 comparison that the handbook's worked example
% does not settle (it lists the keepers' fall as C-5 and this rise as C-10), so the combiner forms no total.
displaced_move(C) :- reclassify(C), not exception(cr_9, C).
fired(rs_5, displaced_move(C), reclassify(C)) :- displaced_move(C).
effect(displaced_move(C), @displaced(P), "turnover", increase, medium, invisible, "B") :- displaced_move(C), protected(C, P).

% PC-21 (1.4) subclass split: insiders displaced by conversion or withdrawal leave more
% (their next-best home may be outside the area: the mobility premise).
displaced_leave(C) :- reclassify(C), holds(would_leave(C)), not exception(pc_21, C).
fired(rs_5,  displaced_leave(C), reclassify(C))  :- displaced_leave(C).
fired(pc_21, displaced_leave(C), would_leave(C)) :- displaced_leave(C).
effect(displaced_leave(C), @displaced(P), "relocation_out_of_area", increase, long, invisible, "B") :- displaced_leave(C), protected(C, P).

% ---- Widened in this version: the rest of the ceiling family and the generic patterns a ceiling uses. ----
% Signs are against the no-policy counterfactual. Where a pattern's Then lists more members than are encoded
% here, the comment says which ones are left out.

% PC-2 (1.4): a shortage is rationed by other means. Not met where the price of a new contract is free
% (excess_demand is not derived then). Each member of the group is signed on its own only with a premise
% that its margin is open and used in this market.
search_rationing(C) :- excess_demand(C), holds(search_open(C)), not exception(pc_2, C).
fired(pc_2, search_rationing(C), excess_demand(C)) :- search_rationing(C).
fired(pc_2, search_rationing(C), search_open(C))   :- search_rationing(C).
effect(search_rationing(C), X, "search_cost", increase, short, invisible, "B") :- search_rationing(C), excluded(C, X).

selection_rationing(C) :- excess_demand(C), holds(selection_open(C)), not exception(pc_2, C).
fired(pc_2, selection_rationing(C), excess_demand(C)) :- selection_rationing(C).
fired(pc_2, selection_rationing(C), selection_open(C)) :- selection_rationing(C).
effect(selection_rationing(C), X, "allocation_by_non_price_criteria", increase, short, invisible, "B") :- selection_rationing(C), excluded(C, X).
% PC-2's other members: wait_time is not signed (no queue premise); side_payments comes from PC-6 below.

% PC-4 with RS-2: sellers cut unregulated quality and maintenance. Insiders receive less quality per unit;
% sellers spend less on maintenance.
quality_falls(C) :- binding_cap(C), holds(quality_adjustable(C)), not exception(pc_4, C).
fired(pc_4, quality_falls(C), binding_cap(C))        :- quality_falls(C).
fired(rs_2, quality_falls(C), quality_adjustable(C)) :- quality_falls(C).
effect(quality_falls(C), P, "quality_per_unit", decrease, short, invisible, "B") :- quality_falls(C), protected(C, P).
effect(quality_falls(C), B, "maintenance_spending", decrease, short, invisible, "B") :- quality_falls(C), bound(C, B).

% PC-6 with RS-3: some exchanges happen above the ceiling, disguised or illegal. Seekers pay side payments.
informal(C) :- binding_cap(C), holds(evasion(C)), not exception(pc_6, C).
fired(pc_6, informal(C), binding_cap(C)) :- informal(C).
fired(rs_3, informal(C), evasion(C))     :- informal(C).
effect(informal(C), X, "side_payments", increase, short, invisible, "B") :- informal(C), excluded(C, X).

% PC-6, sublet form: where the protected buyers' right cannot be assigned, they sublet at the market price.
% (PC-6 signs informal_activity without naming who; only this form is encoded.)
sublet(C) :- informal(C), holds(nontransferable(C)), not exception(pc_6, C).
fired(pc_6, sublet(C), informal(C))          :- sublet(C).
fired(pc_6, sublet(C), nontransferable(C))   :- sublet(C).
effect(sublet(C), P, "informal_activity", increase, short, invisible, "B") :- sublet(C), protected(C, P).

% RS-10: trade driven into the informal market has no recourse to the courts. Encoded for the buyers in that
% trade; the pattern's other members (quality_information, quality_variability, search_cost) are not encoded.
no_recourse(C) :- informal(C), not exception(rs_10, C).
fired(rs_10, no_recourse(C), informal(C)) :- no_recourse(C).
effect(no_recourse(C), X, "disputes_settled_outside_courts", increase, short, invisible, "B") :- no_recourse(C), excluded(C, X).

% RS-11 (with PC-7): a benefit lost by moving makes insiders turn down opportunities that require a move.
job_lock(C) :- turnover_falls(C), holds(opportunities_need_move(C)), not exception(rs_11, C).
fired(rs_11, job_lock(C), turnover_falls(C))            :- job_lock(C).
fired(rs_11, job_lock(C), opportunities_need_move(C))   :- job_lock(C).
effect(job_lock(C), P, "job_changes", decrease, medium, invisible, "B") :- job_lock(C), protected(C, P).

% RS-7: a gain concentrated on the protected buyers that rests on later decisions of the rule-maker, and a loss
% concentrated on the bound sellers: both groups spend to keep or to change the cap. Unless the counterfactual
% has the same lobbying (exception). The developers of WE-001 are not encoded (they need an exemption fact).
lobbying(C) :- binding_cap(C), holds(can_organize(C)), not exception(rs_7, C).
fired(rs_7, lobbying(C), binding_cap(C))  :- lobbying(C).
fired(rs_7, lobbying(C), can_organize(C)) :- lobbying(C).
effect(lobbying(C), P, "lobbying_effort", increase, medium, invisible, "B") :- lobbying(C), protected(C, P).
effect(lobbying(C), B, "lobbying_effort", increase, medium, invisible, "B") :- lobbying(C), bound(C, B).

% PC-16: a binding ceiling is a transfer. The sellers receive less by what the insiders pay less (PC-3, insider_gain).
transfer(C) :- insider_gain(C), not exception(pc_16, C).
fired(pc_16, transfer(C), insider_gain(C)) :- transfer(C).
effect(transfer(C), B, "net_price_received", decrease, medium, invisible, "B") :- transfer(C), bound(C, B).

% CR-8b with PC-16: every payment is a receipt. The sellers' rent forgone is one item of their resources for other uses
% (a fall); the buyers keep the same amount (a rise). Side payments take back part of it (key money, below), so the sellers'
% resources are a CR-12 comparison of two items, formed by the combiner (rent_forgone against key_money).
rent_forgone(C) :- transfer(C), not exception(cr_8, C).
fired(cr_8, rent_forgone(C), transfer(C)) :- rent_forgone(C).
effect(rent_forgone(C), B, "resources_available_other_uses", decrease, medium, invisible, "B") :- rent_forgone(C), bound(C, B).
item(rent_forgone(C), "rent_forgone") :- rent_forgone(C).
rent_kept(C) :- insider_gain(C), not exception(cr_8, C).
fired(cr_8, rent_kept(C), insider_gain(C)) :- rent_kept(C).
effect(rent_kept(C), P, "resources_available_other_uses", increase, medium, visible, "B") :- rent_kept(C), protected(C, P).

% CR-8b with PC-6 (RS-3): sellers who sell above the ceiling receive the side payment the seekers make (C-7). The item is
% signed at the medium horizon so that it can be compared with the rent forgone (CR-12g: one horizon per comparison).
key_money(C) :- informal(C), not exception(cr_8, C).
fired(cr_8, key_money(C), informal(C)) :- key_money(C).
effect(key_money(C), B, "resources_available_other_uses", increase, medium, invisible, "B") :- key_money(C), bound(C, B).
item(key_money(C), "key_money") :- key_money(C).

% OC-4: exchanges that supply withdrawn from the covered stock (PC-5) no longer allows are prevented;
% both sides lose them.
prevented(C) :- supply_falls(C), not exception(oc_4, C).
fired(oc_4, prevented(C), supply_falls(C)) :- prevented(C).
effect(prevented(C), X, "quantity_traded", decrease, medium, invisible, "B") :- prevented(C), excluded(C, X).
effect(prevented(C), B, "quantity_traded", decrease, medium, invisible, "B") :- prevented(C), bound(C, B).

% SB-4: a lasting cap lowers the return on a durable asset in slowly expandable supply; its value falls from
% the time the cap is expected. Owners at that time bear the loss.
capitalized(C) :- binding_cap(C), holds(durable_assets(C)), holds(expected_to_last(C)), not exception(sb_4, C).
fired(sb_4, capitalized(C), binding_cap(C))      :- capitalized(C).
fired(sb_4, capitalized(C), durable_assets(C))   :- capitalized(C).
fired(sb_4, capitalized(C), expected_to_last(C)) :- capitalized(C).
effect(capitalized(C), B, "asset_value", decrease, short, invisible, "B") :- capitalized(C), bound(C, B).

% OC-3: the policy must be administered and enforced, so enforcement cost rises for the enforcing body.
% (Who bears it depends on funding; OC-3 and OC-1 sign a general-budget payer only as a group, so none is encoded.)
% Enforcement activity is positive only where the cap binds and is enforced, so the rule rests on binding_cap (Tier A given that).
administered(C) :- binding_cap(C), not exception(oc_3, C).
fired(oc_3, administered(C), binding_cap(C)) :- administered(C).
effect(administered(C), E, "enforcement_cost", increase, short, invisible, "A") :- administered(C), enforcer(C, E).

% OC-3 with OC-1, first funding case: where the record says the board is funded from the general budget and the budget rises
% with the new task, taxpayers bear the cost. (From a fixed budget, or with no tax named, OC-1 and OC-3 give a group over
% payers; these examples take the raised-budget case, so no group is signed.)
ceiling_funded(C) :- administered(C), taxpayer(C, _), holds(enforcement_budget_raised(C)).
fired(oc_3, ceiling_funded(C), administered(C))                 :- ceiling_funded(C).
fired(oc_3, ceiling_funded(C), enforcement_budget_raised(C))    :- ceiling_funded(C).
fired(oc_1, ceiling_funded(C), administered(C))                 :- ceiling_funded(C).
effect(ceiling_funded(C), T, "resources_available_other_uses", decrease, short, invisible, "B") :- ceiling_funded(C), taxpayer(C, T).

% RS-4 with PC-3: buyers shut out of the covered units can buy in a neighbouring market outside the cap's
% reach, where the extra demand raises the price.
cross_boundary(C) :- binding_cap(C), holds(commutable(C)), neighbor(C, _), not exception(rs_4, C).
fired(pc_3, cross_boundary(C), binding_cap(C)) :- cross_boundary(C).
fired(rs_4, cross_boundary(C), commutable(C))  :- cross_boundary(C).
effect(cross_boundary(C), N, "price_paid", increase, medium, invisible, "B") :- cross_boundary(C), neighbor(C, N).

% PC-5 (keeping units off the market is one of its alternative uses) with RS-5 and CR-4: where re-letting a
% vacated unit makes the later move to an alternative use harder, owners hold vacated units empty instead.
held_vacant(C) :- reclassify(C), holds(relet_obstructs(C)), not exception(pc_5, C).
fired(pc_5, held_vacant(C), reclassify(C))        :- held_vacant(C).
fired(pc_5, held_vacant(C), relet_obstructs(C))   :- held_vacant(C).
effect(held_vacant(C), B, "units_held_vacant", increase, medium, invisible, "B") :- held_vacant(C), bound(C, B).

% OC-2: where the route to an alternative use runs through a permit or board process, using it costs time
% and effort that buy nothing the owner values for its own sake.
process_cost(C) :- reclassify(C), holds(exit_process(C)), not exception(oc_2, C).
fired(oc_2, process_cost(C), reclassify(C))   :- process_cost(C).
fired(oc_2, process_cost(C), exit_process(C)) :- process_cost(C).
effect(process_cost(C), B, "compliance_cost", increase, medium, invisible, "B") :- process_cost(C), bound(C, B).

#show holds/1.
#show fired/3.
#show effect/7.
#show group_effect/7.
#show window/2.
#show item/2.
