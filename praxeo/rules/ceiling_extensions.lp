% Price-ceiling patterns added after the out-of-sample runs on WE-005, WE-006 and WE-067 (cases/we0*/out_of_sample.md).
% Each is a general pattern of handbook/04_rules.md that the first rule base left out; none is fitted to one example.
% Same input facts as price_controls.lp, plus
%   input_supplier(C, Actor).       suppliers of the input that the capped sellers buy (PC-12), written only if the record names them
% Every rule is monotone in holds/1 and negates only plain facts (exception/2, decontrol/1).

% LW-3 with PC-1: at the lower price the buyers want more. Where excess demand is derived (so not under vacancy decontrol),
% the buyers the cap leaves outside want to buy more than before.
demand_rises(C) :- excess_demand(C), not exception(lw_3, C).
fired(lw_3, demand_rises(C), excess_demand(C)) :- demand_rises(C).
effect(demand_rises(C), X, "quantity_demanded", increase, short, invisible, "B") :- demand_rises(C), excluded(C, X).

% PC-2 in its group form (handbook PC-2 Then): the shortage is rationed by at least one of waiting, searching, side payments and
% non-price selection, with no premise on which. The members are signed on their own only with their own premises (price_controls.lp).
rationing(C) :- excess_demand(C), not exception(pc_2, C).
fired(pc_2, rationing(C), excess_demand(C)) :- rationing(C).
group_effect(rationing(C), X, "wait_time,search_cost,side_payments,allocation_by_non_price_criteria", at_least_one_increase, short, invisible, "B") :- rationing(C), excluded(C, X).

% PC-6: exchanges above the ceiling are informal activity for both parties. price_controls.lp signs the protected buyers' sublets;
% here the buyers who pay the side payments (the excluded buyers). Not under vacancy decontrol, where the excluded buyers'
% initial price is free and the informal trade is the sitting tenants' sublets.
informal_buyers(C) :- informal(C), not decontrol(C), not exception(pc_6, C).
fired(pc_6, informal_buyers(C), informal(C)) :- informal_buyers(C).
effect(informal_buyers(C), X, "informal_activity", increase, short, invisible, "B") :- informal_buyers(C), excluded(C, X).

% PC-12: a binding ceiling on a good passes up to the inputs. The capped sellers are the main buyers of a named input (the record
% names its suppliers). Price branch: the input has few uncapped outlets, so its suppliers receive less for what they sell into the
% capped market. Quantity branch: the suppliers have other outlets, so they send less into it, and the prevented exchanges
% (OC-4) are lost to both sides. The two branches can hold together (different suppliers, or one supplier's different loads).
input_price(C) :- binding_cap(C), input_supplier(C, _), holds(input_few_outlets(C)), not exception(pc_12, C).
fired(pc_12, input_price(C), binding_cap(C))          :- input_price(C).
fired(pc_12, input_price(C), input_few_outlets(C))    :- input_price(C).
effect(input_price(C), S, "net_price_received", decrease, short, invisible, "B") :- input_price(C), input_supplier(C, S).

input_quantity(C) :- binding_cap(C), input_supplier(C, _), holds(input_other_outlets(C)), not exception(pc_12, C).
fired(pc_12, input_quantity(C), binding_cap(C))          :- input_quantity(C).
fired(pc_12, input_quantity(C), input_other_outlets(C))  :- input_quantity(C).
effect(input_quantity(C), S, "quantity_supplied", decrease, short, invisible, "B") :- input_quantity(C), input_supplier(C, S).

input_prevented(C) :- input_quantity(C), not exception(oc_4, C).
fired(oc_4, input_prevented(C), input_quantity(C)) :- input_prevented(C).
effect(input_prevented(C), S, "quantity_traded", decrease, short, invisible, "B") :- input_prevented(C), input_supplier(C, S).
effect(input_prevented(C), X, "quantity_traded", decrease, short, invisible, "B") :- input_prevented(C), excluded(C, X).

#show holds/1.
#show fired/3.
#show effect/7.
#show group_effect/7.
#show window/2.
#show item/2.
