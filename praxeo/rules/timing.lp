% RS-8 (handbook catalog 1.4): a change of timing. Where a measure is announced before it takes effect, the same action is
% treated differently depending on when it is taken, and actors move it toward the favourable window.
% Input facts (written by praxeo/engine.py from the policy record):
%   announced(C).                   the record has an announcement window before the effective date
%   rolled_back(C).                 a reading of an unclear provision: the new rule is applied to cases already pending
%                                   (an increase made in the window is cancelled), so the earlier window is partly protected
% Every rule is monotone in holds/1: it negates only plain facts (exception/2, rolled_back/1).
% Each response is signed per window against the counterfactual (02_ontology.md 2.5, window/2 marks the window); the
% announcement window has horizon short. The other side of every shift (the action falls in the window it was taken
% from) is carried by the chains that already sign that window (PC-3 and PC-16 for the capped price; TX-2, OC-4 and TX-7
% for imports), so it is not repeated here. Their comparison with the announcement-window chain is the combiner's
% (rows "first_months" and the A-14 dominance premise on the capped price; see praxeo/combiner.py).

% Price ceiling: sellers reprice contracts that come up before the cap takes effect, which lifts the frozen base.
% Assumes the actors know the timing and can shift (window_repricing). Unless the measure also protects the earlier window
% (a pending-cases clause, the reading rolled_back): the two timing chains then oppose and the sign is ambiguous.
rush(C) :- ceiling(C), announced(C), holds(window_repricing(C)), not exception(rs_8, C).
fired(rs_8, rush(C), announced(C))         :- rush(C).
fired(rs_8, rush(C), window_repricing(C))  :- rush(C).
rush_pays(C) :- rush(C), not rolled_back(C).
rush_contested(C) :- rush(C), rolled_back(C).
window(rush_pays(C), announcement)      :- rush_pays(C).
window(rush_contested(C), announcement) :- rush_contested(C).
fired(rs_8, rush_pays(C), rush(C))      :- rush_pays(C).
fired(rs_8, rush_contested(C), rush(C)) :- rush_contested(C).
effect(rush_pays(C), P, "price_paid", increase, short, invisible, "B")                :- rush_pays(C), protected(C, P).
effect(rush_pays(C), B, "net_price_received", increase, short, invisible, "B")        :- rush_pays(C), bound(C, B).
effect(rush_contested(C), P, "price_paid", ambiguous, short, invisible, "B")          :- rush_contested(C), protected(C, P).
effect(rush_contested(C), B, "net_price_received", ambiguous, short, invisible, "B")  :- rush_contested(C), bound(C, B).

% Tax or tariff: buyers bring purchases forward into the window before the charge starts, if they can store the good or
% order ahead (stockpile_ahead).
bring_forward(C) :- tax(C), announced(C), holds(stockpile_ahead(C)), not exception(rs_8, C).
bring_forward(C) :- tariff(C), announced(C), holds(stockpile_ahead(C)), not exception(rs_8, C).
fired(rs_8, bring_forward(C), announced(C))        :- bring_forward(C).
fired(rs_8, bring_forward(C), stockpile_ahead(C))  :- bring_forward(C).
window(bring_forward(C), announcement) :- bring_forward(C).
effect(bring_forward(C), X, "quantity_traded", increase, short, invisible, "B") :- bring_forward(C), buyer(C, X).

#show holds/1.
#show fired/3.
#show effect/7.
#show group_effect/7.
#show window/2.
#show item/2.
