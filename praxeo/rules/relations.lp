% Related markets (catalog 1.4): CR-9 with LW-10 (derived demand for an input or factor), SB-3 with CR-7a (a factor in slow
% supply is bid away from its other users), and RS-12 (complements in use move together). Each relation is a record fact:
%   related(C, R, Kind, Sellers, PriceVar, OtherUsers).  Kind is input or complement; Sellers sell the related good (the
%       input's suppliers, a factor's workers, the complement's sellers); PriceVar is the variable for their price
%       (wage_rate for labour, net_price_received otherwise); OtherUsers are its other buyers ("" if none named).
%   rel_premise(C, R, Name, Atom).  the assumption atom of the relation's premise Name (close, slow), asked per relation.
% The target market's change comes from the other rule files (target_qty/2). Ceilings are not covered: PC-12 handles
% their inputs. Every rule is monotone in holds/1.

target_qty(C, increase) :- sb_expands(C).
target_qty(C, decrease) :- wedge(C).
fired(sb_2, target_qty(C, increase), sb_expands(C)) :- target_qty(C, increase), sb_expands(C).
fired(tx_2, target_qty(C, decrease), wedge(C))      :- target_qty(C, decrease), wedge(C).

% CR-9: the input's suppliers sell more (less) as the target market expands (shrinks).
rel_derived(C, R, D) :- target_qty(C, D), related(C, R, input, _, _, _), not exception(cr_9, C).
fired(cr_9, rel_derived(C, R, D), target_qty(C, D)) :- rel_derived(C, R, D).
effect(rel_derived(C, R, D), S, "quantity_traded", D, short, invisible, "B") :- rel_derived(C, R, D), related(C, R, input, S, _, _).

% SB-3 with CR-7a: where the input's supply is slow to expand (premise slow), more demand raises its price, and its other users
% pay more and use less; less demand lowers its price, and they pay less and use more.
rel_scarce(C, R, D) :- rel_derived(C, R, D), rel_premise(C, R, slow, A), holds(A).
fired(sb_3, rel_scarce(C, R, D), rel_derived(C, R, D)) :- rel_scarce(C, R, D).
fired(cr_7, rel_scarce(C, R, D), A) :- rel_scarce(C, R, D), rel_premise(C, R, slow, A).
opposite(increase, decrease). opposite(decrease, increase).
effect(rel_scarce(C, R, D), S, V, D, short, invisible, "B")                  :- rel_scarce(C, R, D), related(C, R, input, S, V, _).
effect(rel_scarce(C, R, D), O, "price_paid", D, short, invisible, "B")       :- rel_scarce(C, R, D), related(C, R, input, _, _, O), O != "".
effect(rel_scarce(C, R, D), O, "quantity_traded", E, short, invisible, "B")  :- rel_scarce(C, R, D), related(C, R, input, _, _, O), O != "", opposite(D, E).

% RS-12: a complement in use sells more (less) as the target's quantity rises (falls), if the relation is close and the
% complement has few other uses (premise close); where its supply is slow to adjust (slow), its price moves the same way.
rel_complement(C, R, D) :- target_qty(C, D), related(C, R, complement, _, _, _), rel_premise(C, R, close, A), holds(A), not exception(rs_12, C).
fired(rs_12, rel_complement(C, R, D), target_qty(C, D)) :- rel_complement(C, R, D).
fired(rs_12, rel_complement(C, R, D), A)                :- rel_complement(C, R, D), rel_premise(C, R, close, A).
effect(rel_complement(C, R, D), S, "quantity_traded", D, short, invisible, "B") :- rel_complement(C, R, D), related(C, R, complement, S, _, _).
rel_complement_price(C, R, D) :- rel_complement(C, R, D), rel_premise(C, R, slow, A), holds(A).
fired(rs_12, rel_complement_price(C, R, D), rel_complement(C, R, D)) :- rel_complement_price(C, R, D).
fired(rs_12, rel_complement_price(C, R, D), A) :- rel_complement_price(C, R, D), rel_premise(C, R, slow, A).
effect(rel_complement_price(C, R, D), S, V, D, short, invisible, "B") :- rel_complement_price(C, R, D), related(C, R, complement, S, V, _).

#show holds/1.
#show fired/3.
#show effect/7.
#show group_effect/7.
#show window/2.
#show item/2.
