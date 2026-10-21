% Core rules as engine rules (pilot). CR-4, CR-5a, CR-6, CR-7 (b, c), CR-8 (b, c) and CR-9, over a situation described in
% CR-1's terms (praxeo/core/situation.py). No rule names an instrument, a good or a market: what is specific to a case is in
% the situation facts (who trades, which price is held and which way, which terms are left free, which alternatives and
% links exist), and every sign below comes from a core rule. Each empirical fact carries up to three premise atoms
% (P1, P2, P3; `none` when unused, which ok/1 always grants), which are assumptions estimated per case.
%
% Situation facts:
%   held(C, E, Dir, P1, P2, P3).            CR-1 op 1: component C removes trading in exchange E beyond a price line;
%                                           Dir is below (a maximum) or above (a minimum)
%   party(E, Side, A). unsatisfied(E, Side, A).  who trades on each side; who would trade at the line but cannot
%   price_var(E, Side, Var).                the variable in which a side's price is measured
%   criteria(E, A, "v1,v2,...").            the criteria by which the scarce side can choose among A (CR-6, a group)
%   criterion(E, A, Var, P1, P2, P3).       one of them, with its own premise
%   adjust(E, Side, A, "v1,...", P1, P2, P3).  the terms and quantities Side controls that fall on A (CR-6, a group)
%   adjust_one(E, Side, A, Var, P1, P2, P3). one of them, with its own premise
%   outside(E, A, Var, P1, P2, P3).         trade outside the rule (CR-6 third margin, CR-4: comply against violate)
%   alt(C, Chooser, A, Var, Kind, P1, P2, P3).  CR-4: an alternative of Chooser to an option C changes; its use is
%                                           measured by Var on A; Kind is plain or group (Var a comma list)
%   stake(C, A, P1, P2, P3).                CR-4 (accept against lobby): A has a stake in C
%   link(A0, V0, Rel, A, V, P1, P2, P3).    CR-9: a change in A0's V0 reaches A's V through relation Rel
%   asset(E, Side, Owner, P1, P2, P3). yield(E, Side, A, P1, P2, P3).   CR-7c, CR-7b: assets and returns tied to a side
%   transfer(E, P1, P2, P3).                CR-8b: the held price is a transfer between those who still trade
%   compliance(C, A). enforcer(C, A). funded(C, A, P1, P2, P3). fixed_budget(C, A, P1, P2, P3).   CR-8c
%   charge(C, E, Side, Receiver).           CR-1 op 3: C attaches a payment to trading in E, paid by Side, to Receiver
%   receipt_var(C, V). projection_var(C, V). the vocabulary's names for the receipt and its shortfall against a static
%                                           projection (a tax's revenue, a fee's receipts)
%   moves(E, Side, P1, P2, P3).             CR-6 0.9: with this premise on the other side's response, Side's price takes
%                                           the change (both sides may have one)
%   discretion(C, A, P1, P2, P3).           CR-1 op 2 granted case by case: an option A may apply for, at no price
%   means(C, A, Dir).                       CR-1 op 4: a transfer of means (Dir out or in) that no choice avoids
%   link(..., V, ...) with V a comma list:  a group over those variables (CR-6 1.1: labour moves as a group)
% Every rule is monotone in holds/1.

{ holds(A) } :- assumption(A).
ok(none).
ok(A) :- holds(A).

% ---------------------------------------------------------------- CR-6: a price held off the clearing level
h(C, E, D) :- held(C, E, D, P1, P2, P3), ok(P1), ok(P2), ok(P3).
fired(cr_6, h(C, E, D), P) :- h(C, E, D), held(C, E, D, P1, P2, P3), P = (P1; P2; P3), P != none.

% Which side the line burdens, and which side is left unsatisfied (long). A maximum burdens sellers and leaves buyers
% wanting more; a minimum the reverse (CR-6, symmetry).
burdens(below, seller). burdens(above, buyer).
long(below, buyer).     long(above, seller).
opp(increase, decrease). opp(decrease, increase).
line_dir(below, decrease). line_dir(above, increase).
burdened(E, S) :- h(_, E, D), burdens(D, S).
favored(E, S)  :- h(_, E, D), burdens(D, T), S != T, side(S), side(T).
side(buyer). side(seller).

% Those who trade, trade at the line: the price moves toward it for both sides.
p_line(E, S) :- h(_, E, _), price_var(E, S, _).
fired(cr_6, p_line(E, S), h(C, E, D)) :- p_line(E, S), h(C, E, D).
effect(p_line(E, S), A, V, Dir, short, visible, "B") :- p_line(E, S), h(_, E, D), line_dir(D, Dir), price_var(E, S, V), party(E, S, A).

% The long side has more than the other side takes at the line.
p_excess(E) :- h(_, E, _).
fired(cr_6, p_excess(E), h(C, E, D)) :- p_excess(E), h(C, E, D).
excess_var(buyer, "excess_demand"). excess_var(seller, "excess_supply").
effect(p_excess(E), A, V, increase, short, invisible, "B") :- p_excess(E), h(_, E, D), long(D, S), excess_var(S, V), unsatisfied(E, S, A).

% The pressure goes to the margins still open. The scarce side chooses by other criteria, at least one (a group), and a
% criterion with its own premise is signed alone.
p_criteria(E) :- h(_, E, _), criteria(E, _, _).
fired(cr_6, p_criteria(E), h(C, E, D)) :- p_criteria(E), h(C, E, D).
group_effect(p_criteria(E), A, G, at_least_one_increase, short, invisible, "B") :- p_criteria(E), criteria(E, A, G).
p_criterion(E, A, V) :- h(_, E, _), criterion(E, A, V, P1, P2, P3), ok(P1), ok(P2), ok(P3).
fired(cr_6, p_criterion(E, A, V), P) :- p_criterion(E, A, V), criterion(E, A, V, P1, P2, P3), P = (P1; P2; P3), P != none.
effect(p_criterion(E, A, V), A, V, increase, short, invisible, "B") :- p_criterion(E, A, V).

% The burdened side gives less of what the line leaves free: its unregulated terms and the quantity it takes or offers.
p_adjust(E, S, A) :- burdened(E, S), adjust(E, S, A, G, P1, P2, P3), ok(P1), ok(P2), ok(P3).
fired(cr_6, p_adjust(E, S, A), P) :- p_adjust(E, S, A), adjust(E, S, A, _, P1, P2, P3), P = (P1; P2; P3), P != none.
group_effect(p_adjust(E, S, A), A, G, at_least_one_decrease, short, invisible, "B") :- p_adjust(E, S, A), adjust(E, S, A, G, _, _, _).
p_adjust_one(E, S, A, V) :- burdened(E, S), adjust_one(E, S, A, V, P1, P2, P3), ok(P1), ok(P2), ok(P3).
fired(cr_6, p_adjust_one(E, S, A, V), P) :- p_adjust_one(E, S, A, V), adjust_one(E, S, A, V, P1, P2, P3), P = (P1; P2; P3), P != none.
effect(p_adjust_one(E, S, A, V), A, V, decrease, short, invisible, "B") :- p_adjust_one(E, S, A, V).

% Trade outside the rule, where the expected gain exceeds the expected penalty (CR-6 with CR-4: comply against violate).
p_outside(E, A, V) :- h(_, E, _), outside(E, A, V, P1, P2, P3), ok(P1), ok(P2), ok(P3).
fired(cr_4, p_outside(E, A, V), P) :- p_outside(E, A, V), outside(E, A, V, P1, P2, P3), P = (P1; P2; P3), P != none.
effect(p_outside(E, A, V), A, V, increase, short, invisible, "B") :- p_outside(E, A, V).

% ---------------------------------------------------------------- CR-5a: exchanges prevented
% Trades that would have taken place beyond the line do not: both the burdened side and the unsatisfied lose them.
p_prevented(E) :- h(_, E, _).
fired(cr_5, p_prevented(E), h(C, E, D)) :- p_prevented(E), h(C, E, D).
effect(p_prevented(E), A, "quantity_traded", decrease, short, invisible, "B") :- p_prevented(E), burdened(E, S), party(E, S, A).
effect(p_prevented(E), A, "quantity_traded", decrease, short, invisible, "B") :- p_prevented(E), h(_, E, D), long(D, S), unsatisfied(E, S, A).

% ---------------------------------------------------------------- CR-4: response at the margin
% An actor whose option a component burdens (the burdened party, or those it leaves unsatisfied) uses its alternatives
% more; one whose option it improves (the favored party) uses its alternatives less.
chooser(C, A, worse)  :- h(C, E, _), burdened(E, S), party(E, S, A).
chooser(C, A, worse)  :- h(C, E, D), long(D, S), unsatisfied(E, S, A).
chooser(C, A, better) :- h(C, E, _), favored(E, S), party(E, S, A).
chooser(C, A, worse)  :- c_charged(C, E), charge(C, E, S, _), party(E, S, A).
alt_dir(worse, increase, at_least_one_increase). alt_dir(better, decrease, at_least_one_decrease).
p_alt(C, Ch, A, V) :- alt(C, Ch, A, V, _, P1, P2, P3), chooser(C, Ch, _), ok(P1), ok(P2), ok(P3).
fired(cr_4, p_alt(C, Ch, A, V), P) :- p_alt(C, Ch, A, V), alt(C, Ch, A, V, _, P1, P2, P3), P = (P1; P2; P3), P != none.
fired(cr_4, p_alt(C, Ch, A, V), h(C, E, D)) :- p_alt(C, Ch, A, V), h(C, E, D).
fired(cr_4, p_alt(C, Ch, A, V), c_charged(C, E)) :- p_alt(C, Ch, A, V), c_charged(C, E).
effect(p_alt(C, Ch, A, V), A, V, Dir, medium, invisible, "B")       :- p_alt(C, Ch, A, V), alt(C, Ch, A, V, plain, _, _, _), chooser(C, Ch, W), alt_dir(W, Dir, _).
group_effect(p_alt(C, Ch, A, V), A, V, G, medium, invisible, "B")   :- p_alt(C, Ch, A, V), alt(C, Ch, A, V, group, _, _, _), chooser(C, Ch, W), alt_dir(W, _, G).

% Accept against lobby: whoever has a stake in the component's outcome lobbies over it.
p_stake(C, A) :- stake(C, A, P1, P2, P3), c_acts(C), ok(P1), ok(P2), ok(P3).
c_acts(C) :- h(C, _, _).
c_acts(C) :- c_charged(C, _).
fired(cr_4, p_stake(C, A), P) :- p_stake(C, A), stake(C, A, P1, P2, P3), P = (P1; P2; P3), P != none.
effect(p_stake(C, A), A, "lobbying_effort", increase, medium, invisible, "B") :- p_stake(C, A).

% ---------------------------------------------------------------- CR-7: returns and asset values
% The burdened side's yield falls and the favored side's rises (b); assets tied to it are revalued when the change becomes
% expected (c).
side_dir(E, S, decrease) :- burdened(E, S).
side_dir(E, S, increase) :- favored(E, S).
p_yield(E, A) :- yield(E, S, A, P1, P2, P3), side_dir(E, S, _), ok(P1), ok(P2), ok(P3).
fired(cr_7, p_yield(E, A), P) :- p_yield(E, A), yield(E, _, A, P1, P2, P3), P = (P1; P2; P3), P != none.
effect(p_yield(E, A), A, "return_on_capital", D, short, invisible, "B") :- p_yield(E, A), yield(E, S, A, _, _, _), side_dir(E, S, D).
p_asset(E, A) :- asset(E, S, A, P1, P2, P3), side_dir(E, S, _), ok(P1), ok(P2), ok(P3).
fired(cr_7, p_asset(E, A), P) :- p_asset(E, A), asset(E, _, A, P1, P2, P3), P = (P1; P2; P3), P != none.
effect(p_asset(E, A), A, "asset_value", D, short, invisible, "B") :- p_asset(E, A), asset(E, S, A, _, _, _), side_dir(E, S, D).

% ---------------------------------------------------------------- CR-8: conservation of means
% (b) the line is a transfer between those who still trade: the favored side keeps what the burdened side forgoes.
p_transfer(E) :- transfer(E, P1, P2, P3), h(_, E, _), ok(P1), ok(P2), ok(P3).
fired(cr_8, p_transfer(E), P) :- p_transfer(E), transfer(E, P1, P2, P3), P = (P1; P2; P3), P != none.
effect(p_transfer(E), A, "resources_available_other_uses", D, medium, invisible, "B") :- p_transfer(E), party(E, S, A), side_dir(E, S, D).
% (c) complying and enforcing use means up (Tier A given the policy); the enforcer is paid by those named, or its other
% work gives way where its budget is fixed.
p_comply(C, A) :- compliance(C, A).
fired(cr_8, p_comply(C, A), compliance(C, A)) :- p_comply(C, A).
effect(p_comply(C, A), A, "compliance_cost", increase, short, invisible, "A") :- p_comply(C, A).
p_enforce(C, A) :- enforcer(C, A).
fired(cr_8, p_enforce(C, A), enforcer(C, A)) :- p_enforce(C, A).
effect(p_enforce(C, A), A, "enforcement_cost", increase, short, invisible, "A") :- p_enforce(C, A).
p_funded(C, A) :- funded(C, A, P1, P2, P3), ok(P1), ok(P2), ok(P3).
fired(cr_8, p_funded(C, A), P) :- p_funded(C, A), funded(C, A, P1, P2, P3), P = (P1; P2; P3), P != none.
effect(p_funded(C, A), A, "resources_available_other_uses", decrease, short, invisible, "B") :- p_funded(C, A).
p_fixed(C, A) :- fixed_budget(C, A, P1, P2, P3), ok(P1), ok(P2), ok(P3).
fired(cr_8, p_fixed(C, A), P) :- p_fixed(C, A), fixed_budget(C, A, P1, P2, P3), P = (P1; P2; P3), P != none.
effect(p_fixed(C, A), A, "enforcement_cost", decrease, short, invisible, "B") :- p_fixed(C, A).
item(p_fixed(C, A), "other_work") :- p_fixed(C, A).

% ---------------------------------------------------------------- CR-9: propagation
% A change in one actor's variable reaches those linked to it. The direction follows the relation and whether the source is
% a price or a quantity (LW-10): what is used with a good or produces it moves with its use; a substitute moves against its
% use and with its price; a cost passes to the price of what it produces; investment follows the yield; `same_act` is the
% same act seen from another party (a conversion is the condo the buyer buys, the payment the tenant receives).
% price_kind(V): the variables that measure a price (vocabulary facts written by situation.py).
kind(V, price) :- moved(_, V, _), price_kind(V).
kind(V, quantity) :- moved(_, V, _), not price_kind(V).
rel_dir(complement, quantity, D, D) :- opp(D, _).
rel_dir(input,      quantity, D, D) :- opp(D, _).
rel_dir(substitute, quantity, D, E) :- opp(D, E).
rel_dir(substitute, price,    D, D) :- opp(D, _).
rel_dir(output,     price,    D, D) :- opp(D, _).
rel_dir(yield,      K,        D, D) :- opp(D, _), K = (price; quantity).
rel_dir(same_act,   K,        D, D) :- opp(D, _), K = (price; quantity).
% A cost: where a means it uses gets dearer (or cheaper) and rivals do not share the change, the user supplies less (more)
% and the value of what it owns falls (rises) (CR-4, CR-7c). Own price: an actor buys less of what costs it more (CR-4c).
% Currency: payments for imports are the means foreigners buy exports with (CR-9).
rel_dir(cost,       price,    D, E) :- opp(D, E).
rel_dir(own_price,  price,    D, E) :- opp(D, E).
rel_dir(currency,   quantity, D, D) :- opp(D, _).
moved(A, V, D) :- effect(_, A, V, D, _, _, _), opp(D, _).
p_link(A0, V0, R, A, V) :- link(A0, V0, R, A, V, P1, P2, P3), moved(A0, V0, _), ok(P1), ok(P2), ok(P3).
fired(cr_9, p_link(A0, V0, R, A, V), X) :- p_link(A0, V0, R, A, V), effect(X, A0, V0, D, _, _, _), opp(D, _).
fired(cr_9, p_link(A0, V0, R, A, V), P) :- p_link(A0, V0, R, A, V), link(A0, V0, R, A, V, P1, P2, P3), P = (P1; P2; P3), P != none.
effect(p_link(A0, V0, R, A, V), A, V, D2, medium, invisible, "B") :- p_link(A0, V0, R, A, V), not link_group(V), moved(A0, V0, D), kind(V0, K), rel_dir(R, K, D, D2).
group_sign(increase, at_least_one_increase). group_sign(decrease, at_least_one_decrease).
group_effect(p_link(A0, V0, R, A, V), A, V, G, medium, invisible, "B") :- p_link(A0, V0, R, A, V), link_group(V), moved(A0, V0, D), kind(V0, K), rel_dir(R, K, D, D2), group_sign(D2, G).

% ---------------------------------------------------------------- CR-1 op 3: a payment attached to trading
% The payment is a wedge: the range both sides accept moves (CR-5c). Fewer trades take place (CR-4: the option is worse for
% the payer; CR-5a for the other side). Which side's price takes the change needs a premise on the other side's response
% (moves/5, CR-6 0.9); the payer's price rises, the other side's net price falls. The payment is the receiver's revenue and
% a sum the payers who keep trading cannot avoid (CR-8b, CR-3); with fewer trades, the revenue falls short of the payment
% times the old base (CR-4 with CR-8b).
c_charged(C, E) :- charge(C, E, _, _).
fired(cr_1, c_charged(C, E), charge(C, E, S, R)) :- c_charged(C, E), charge(C, E, S, R).
effect(c_charged(C, E), A, "quantity_traded", decrease, short, invisible, "B") :- c_charged(C, E), party(E, _, A).
p_moves(C, E, S) :- c_charged(C, E), moves(E, S, P1, P2, P3), ok(P1), ok(P2), ok(P3).
fired(cr_6, p_moves(C, E, S), P) :- p_moves(C, E, S), moves(E, S, P1, P2, P3), P = (P1; P2; P3), P != none.
fired(cr_5, p_moves(C, E, S), c_charged(C, E)) :- p_moves(C, E, S).
wedge_dir(S, increase) :- charge(_, _, S, _).
wedge_dir(S, decrease) :- charge(_, _, T, _), side(S), side(T), S != T.
effect(p_moves(C, E, S), A, V, D, short, invisible, "B") :- p_moves(C, E, S), price_var(E, S, V), party(E, S, A), charge(C, E, T, _), c_wedge(T, S, D).
c_wedge(T, T, increase) :- side(T).
c_wedge(T, S, decrease) :- side(T), side(S), S != T.
c_paid(C, E) :- c_charged(C, E).
fired(cr_8, c_paid(C, E), c_charged(C, E)) :- c_paid(C, E).
effect(c_paid(C, E), R, V, increase, short, visible, "A") :- c_paid(C, E), charge(C, E, _, R), receipt_var(C, V).
effect(c_paid(C, E), A, "resources_available_other_uses", decrease, short, invisible, "A") :- c_paid(C, E), charge(C, E, S, _), party(E, S, A).
effect(c_paid(C, E), R, V, decrease, short, invisible, "B") :- c_paid(C, E), charge(C, E, _, R), projection_var(C, V).

% ---------------------------------------------------------------- CR-1 op 2 at discretion, and op 4
% An option granted case by case at no price is scarce at that price: applicants spend means on applying (CR-8c), and
% officials choose among them by other criteria (CR-6, public supply at a set price).
p_discretion(C, A) :- discretion(C, A, P1, P2, P3), ok(P1), ok(P2), ok(P3).
fired(cr_6, p_discretion(C, A), P) :- p_discretion(C, A), discretion(C, A, P1, P2, P3), P = (P1; P2; P3), P != none.
effect(p_discretion(C, A), A, "compliance_cost", increase, short, invisible, "B") :- p_discretion(C, A).
effect(p_discretion(C, A), A, "allocation_by_non_price_criteria", increase, short, invisible, "B") :- p_discretion(C, A).
% A transfer of means alone: the actor's means change; which uses give way is not signed (CR-4, a change in means alone).
p_means(C, A) :- means(C, A, _).
fired(cr_8, p_means(C, A), means(C, A, D)) :- p_means(C, A), means(C, A, D).
means_dir(out, decrease). means_dir(in, increase).
effect(p_means(C, A), A, "resources_available_other_uses", D, short, invisible, "A") :- p_means(C, A), means(C, A, M), means_dir(M, D).

#show holds/1.
#show fired/3.
#show effect/7.
#show group_effect/7.
#show window/2.
#show item/2.
