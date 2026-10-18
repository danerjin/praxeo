% Subsidies (handbook catalog 1.4, family SB): SB-1 to SB-6, with OC-3, CR-8c, DM-1, PC-2 (group form), RS-5, RS-7,
% RS-8 and RS-11 where a subsidy brings them in. Export subsidies (SB-10) are not encoded.
% Input facts, written by praxeo/engine.py from the policy record:
%   subsidy(C).                     component C is a per_unit_subsidy, purchase_rebate or lump_sum_subsidy (SB-1)
%   per_unit_sub(C).                the payment rises with the quantity bought or sold: per_unit_subsidy, purchase_rebate (SB-2)
%   sb_recipient(C, A).             who receives the payment (the record's bound_actor)
%   sb_seller(C, A).                sellers of the subsidized good, when they are not the recipients
%   sb_other_buyer(C, A).           buyers of the same good who receive no subsidy                         (DM-1, CR-4c)
%   sb_substitute_seller(C, A).     sellers of the unsubsidized goods the recipients would otherwise buy   (SB-3)
%   sb_asset_owner(C, A).           owners of an asset in slow supply whose return the subsidy raises      (SB-4)
%   sb_claim_handler(C, A).         who files or processes claims (default the recipients)                 (CR-8c)
%   enforcer(C, A). taxpayer(C, A). who administers the payments, and who funds them                       (OC-3, SB-1)
%   own_revenue(C).                 the payments come from a dedicated revenue, not from taxpayers' general funds
%   debt_funded(C).                 the payments are borrowed now and repaid from taxes later (SB-1)
%   criteria(C).                    the payment is conditional on eligibility criteria                     (SB-5)
%   renewable(C).                   the subsidy expires or is reviewed and may be renewed                  (RS-7)
%   budget_capped(C).               a fixed budget or number of payments, first come first served          (PC-2, LW-6)
%   temporary(C).                   available only during a limited window, then it expires                (SB-6)
%   announced(C).                   announced before it takes effect                                       (RS-8)
%   scrappage(C).                   the payment requires destroying a used good                            (SB-6)
%   sb_used_buyer(C, A). sb_used_owner(C, A). sb_scrapper(C, A).  buyers and other owners of used goods, and who
%                                   destroys the scrapped goods (SB-6)
%   repay_on_move(C).               the payment is repaid if the recipient moves within a period          (RS-11)
%   tax_named(C).                   the record names the tax that pays (OC-1, who pays); otherwise the payers are a group
%   sb_payer_group(C, "a,b,c").     that group: taxpayers, recipients of other spending, future taxpayers  (OC-1)
%   sb_recipients_sell(C).          the recipients are the sellers of the subsidized good (a payment to producers)
%   sb_payer_body(C, A).            who pays the money out (default the administering agency)            (SB-1, CR-8b)
%   claim_penalties(C).             the text sets penalties for false claims (clawback, fines)          (RS-3, CR-8b)
%   sb_qualifier(C, A).             who must meet the criteria (default the recipients)                   (SB-5)
% Every rule is monotone in holds/1: it negates only plain facts (exception/2, own_revenue/1, debt_funded/1, tax_named/1,
% sb_recipients_sell/1, per_unit_sub/1).
% Signs are relative to the no-policy counterfactual.

{ holds(A) } :- assumption(A).

% SB-1 with TX-1 and OC-1: the subsidy is funded by someone (Tier A, given payment). Not from a dedicated revenue
% (own_revenue): that reduces what the revenue does elsewhere, which the record does not name. OC-1, who pays: where the
% record names the tax that pays (tax_named), its payers lose; otherwise the means come from a general budget, and the
% payers are a group over actor classes (taxpayers, recipients of other spending, future taxpayers: sb_payer_group, one
% comma-separated string) with at_least_one_decrease. Borrowed now and repaid later (debt_funded): from the medium horizon.
sb_paid(C) :- subsidy(C), not exception(sb_1, C).
fired(sb_1, sb_paid(C), subsidy(C)) :- sb_paid(C).
sb_tax_funded(C) :- sb_paid(C), not own_revenue(C).
fired(oc_1, sb_tax_funded(C), sb_paid(C)) :- sb_tax_funded(C).
effect(sb_tax_funded(C), T, "resources_available_other_uses", decrease, short, invisible, "A")  :- sb_tax_funded(C), tax_named(C), taxpayer(C, T), not debt_funded(C).
effect(sb_tax_funded(C), T, "resources_available_other_uses", decrease, medium, invisible, "A") :- sb_tax_funded(C), tax_named(C), taxpayer(C, T), debt_funded(C).
group_effect(sb_tax_funded(C), G, "resources_available_other_uses", at_least_one_decrease, short, invisible, "A")  :- sb_tax_funded(C), sb_payer_group(C, G), not tax_named(C), not debt_funded(C).
group_effect(sb_tax_funded(C), G, "resources_available_other_uses", at_least_one_decrease, medium, invisible, "A") :- sb_tax_funded(C), sb_payer_group(C, G), not tax_named(C), debt_funded(C).

% OC-3: the payments must be administered; the cost falls on the agency that pays them (Tier A).
sb_administered(C) :- subsidy(C), not exception(oc_3, C).
fired(oc_3, sb_administered(C), subsidy(C)) :- sb_administered(C).
effect(sb_administered(C), E, "enforcement_cost", increase, short, invisible, "A") :- sb_administered(C), enforcer(C, E).

% CR-1 with CR-8c: claims must be filed and checked, which uses time that serves no other end (Tier A, given claims).
sb_claims(C) :- subsidy(C), not exception(cr_8, C).
fired(cr_8, sb_claims(C), subsidy(C)) :- sb_claims(C).
effect(sb_claims(C), H, "compliance_cost", increase, short, invisible, "A") :- sb_claims(C), sb_claim_handler(C, H).

% SB-2: a payment per unit bought or sold is a wedge in the other direction. Recipients take it up if it is worth more than
% what qualifying costs them (takeup). Buyers pay less net of it unless sellers capture all of it (not_fully_captured);
% the quantity traded rises if at least one side can expand (quantity_expands).
sb_takeup(C) :- per_unit_sub(C), holds(takeup(C)), not exception(sb_2, C).
fired(sb_2, sb_takeup(C), per_unit_sub(C)) :- sb_takeup(C).
fired(sb_2, sb_takeup(C), takeup(C))       :- sb_takeup(C).
sb_recipients_gain(C) :- sb_takeup(C), holds(not_fully_captured(C)).
fired(sb_2, sb_recipients_gain(C), sb_takeup(C))          :- sb_recipients_gain(C).
fired(sb_2, sb_recipients_gain(C), not_fully_captured(C)) :- sb_recipients_gain(C).
% Recipients who buy pay less; recipients who sell (a payment to producers per unit sold, sb_recipients_sell) receive more.
effect(sb_recipients_gain(C), R, "price_paid", decrease, short, visible, "B")         :- sb_recipients_gain(C), sb_recipient(C, R), not sb_recipients_sell(C).
effect(sb_recipients_gain(C), R, "net_price_received", increase, short, visible, "B") :- sb_recipients_gain(C), sb_recipient(C, R), sb_recipients_sell(C).
sb_expands(C) :- sb_takeup(C), holds(quantity_expands(C)).
fired(sb_2, sb_expands(C), sb_takeup(C))       :- sb_expands(C).
fired(sb_2, sb_expands(C), quantity_expands(C)) :- sb_expands(C).
effect(sb_expands(C), R, "quantity_traded", increase, short, visible, "B")   :- sb_expands(C), sb_recipient(C, R), not sb_recipients_sell(C).
effect(sb_expands(C), R, "quantity_supplied", increase, short, visible, "B") :- sb_expands(C), sb_recipient(C, R), sb_recipients_sell(C).
effect(sb_expands(C), S, "quantity_traded", increase, short, visible, "B") :- sb_expands(C), sb_seller(C, S).

% SB-1 with CR-8b, the receipt side (found out of sample on WE-033, WE-065, WE-021, WE-056): every payment is a receipt.
% The paying body's outlay rises (sb_payer_body: who pays out, default the administering agency), and what the recipients
% receive adds to their means: a lump sum on payment (Tier A); a payment per unit on take-up, and for recipients who buy
% only the part sellers do not capture (sb_recipients_gain).
sb_outlay(C) :- sb_takeup(C).
fired(sb_1, sb_outlay(C), sb_takeup(C)) :- sb_outlay(C), sb_takeup(C).
sb_outlay(C) :- sb_paid(C), not per_unit_sub(C).
fired(sb_1, sb_outlay(C), sb_paid(C))   :- sb_outlay(C), sb_paid(C), not per_unit_sub(C).
effect(sb_outlay(C), P, "subsidy_outlay", increase, short, visible, "B") :- sb_outlay(C), sb_payer_body(C, P), per_unit_sub(C).
effect(sb_outlay(C), P, "subsidy_outlay", increase, short, visible, "A") :- sb_outlay(C), sb_payer_body(C, P), not per_unit_sub(C).
sb_recipients_keep(C) :- sb_paid(C), not per_unit_sub(C).
fired(cr_8, sb_recipients_keep(C), sb_paid(C)) :- sb_recipients_keep(C), sb_paid(C), not per_unit_sub(C).
sb_recipients_keep(C) :- sb_recipients_gain(C).
fired(cr_8, sb_recipients_keep(C), sb_recipients_gain(C)) :- sb_recipients_keep(C), sb_recipients_gain(C).
effect(sb_recipients_keep(C), R, "resources_available_other_uses", increase, short, invisible, "A") :- sb_recipients_keep(C), sb_recipient(C, R), not per_unit_sub(C).
effect(sb_recipients_keep(C), R, "resources_available_other_uses", increase, short, invisible, "B") :- sb_recipients_keep(C), sb_recipient(C, R), per_unit_sub(C).

% CR-1 with RS-3: where the payment can be claimed falsely and the text sets penalties for it (claim_penalties), some claims
% are false or overstated if checks are partial (false_claims); where some are found (claims_recovered), the paying body
% takes in repayments and fines (CR-8b).
sb_false_claims(C) :- sb_outlay(C), claim_penalties(C), holds(false_claims(C)), not exception(rs_3, C).
fired(rs_3, sb_false_claims(C), sb_outlay(C))   :- sb_false_claims(C).
fired(rs_3, sb_false_claims(C), false_claims(C)) :- sb_false_claims(C).
effect(sb_false_claims(C), R, "legal_breach", increase, short, invisible, "B") :- sb_false_claims(C), sb_recipient(C, R).
sb_recovered(C) :- sb_false_claims(C), holds(claims_recovered(C)).
fired(cr_8, sb_recovered(C), sb_false_claims(C))  :- sb_recovered(C).
fired(cr_8, sb_recovered(C), claims_recovered(C)) :- sb_recovered(C).
effect(sb_recovered(C), P, "non_tax_receipts", increase, short, invisible, "B") :- sb_recovered(C), sb_payer_body(C, P).

% SB-2 with DM-1: where the sellers' supply cannot grow at once (seller_supply_slow), the added demand raises the price they
% receive, and buyers without the subsidy pay more for the same good and buy less of it (CR-4c). Which side receives the
% larger share is a comparison of their alternatives (DM-1), signed as subsidy_share_received only with that premise.
sb_sellers_capture(C) :- sb_takeup(C), holds(seller_supply_slow(C)), not exception(dm_1, C).
fired(sb_2, sb_sellers_capture(C), sb_takeup(C))         :- sb_sellers_capture(C).
fired(dm_1, sb_sellers_capture(C), seller_supply_slow(C)) :- sb_sellers_capture(C).
effect(sb_sellers_capture(C), S, "net_price_received", increase, short, invisible, "B") :- sb_sellers_capture(C), sb_seller(C, S).
effect(sb_sellers_capture(C), B, "price_paid", increase, short, invisible, "B")         :- sb_sellers_capture(C), sb_other_buyer(C, B).
% CR-8b with OC-1: what they pay above the old price is lost to their other uses (found out of sample on WE-020, C-25).
effect(sb_sellers_capture(C), B, "resources_available_other_uses", decrease, short, invisible, "B") :- sb_sellers_capture(C), sb_other_buyer(C, B).
sb_others_cut_back(C) :- sb_sellers_capture(C), sb_other_buyer(C, _), not exception(cr_4, C).
fired(cr_4, sb_others_cut_back(C), sb_sellers_capture(C)) :- sb_others_cut_back(C).
effect(sb_others_cut_back(C), B, "quantity_traded", decrease, short, invisible, "B") :- sb_others_cut_back(C), sb_other_buyer(C, B).
sb_sellers_share(C) :- sb_sellers_capture(C), holds(sellers_fewer_alternatives(C)).
fired(dm_1, sb_sellers_share(C), sb_sellers_capture(C))        :- sb_sellers_share(C).
fired(dm_1, sb_sellers_share(C), sellers_fewer_alternatives(C)) :- sb_sellers_share(C).
effect(sb_sellers_share(C), S, "subsidy_share_received", increase, short, invisible, "B") :- sb_sellers_share(C), sb_seller(C, S).

% SB-3 with RS-1: resources move into the subsidized activity from other uses. Recipients who would otherwise have bought an
% unsubsidized good buy less of it (substitutes_given_up). For a temporary subsidy the effect is signed for the window only
% (SB-3 Unless: a timing shift, not a lasting reduction); the after-window chains are SB-6's.
sb_drawn(C) :- sb_expands(C), sb_substitute_seller(C, _), holds(substitutes_given_up(C)), not exception(sb_3, C).
fired(sb_3, sb_drawn(C), sb_expands(C))           :- sb_drawn(C).
fired(rs_1, sb_drawn(C), substitutes_given_up(C)) :- sb_drawn(C).
% The unsubsidized goods are other goods than the subsidized one, so the effect is the item `unsubsidized_goods`: where
% their sellers also sell the subsidized good, their sales of it rise (SB-2) and of these fall, and no total is formed.
effect(sb_drawn(C), S, "quantity_traded", decrease, short, invisible, "B") :- sb_drawn(C), sb_substitute_seller(C, S).
item(sb_drawn(C), "unsubsidized_goods") :- sb_drawn(C).

% SB-4: a lasting rise in the return on an asset in slow supply is capitalized in its value from the time it is expected.
% For a payment per unit the rise comes through take-up; a lump sum attached to an asset (paid to whoever holds land with
% a production history) raises its return directly (found out of sample on WE-065, reading U1-b).
sb_asset_gain(C) :- sb_takeup(C).
fired(sb_2, sb_asset_gain(C), sb_takeup(C)) :- sb_asset_gain(C), sb_takeup(C).
sb_asset_gain(C) :- sb_paid(C), not per_unit_sub(C).
fired(sb_1, sb_asset_gain(C), sb_paid(C))   :- sb_asset_gain(C), sb_paid(C), not per_unit_sub(C).
sb_capitalized(C) :- sb_asset_gain(C), sb_asset_owner(C, _), holds(asset_supply_slow(C)), holds(expected_to_last(C)), not exception(sb_4, C).
fired(sb_4, sb_capitalized(C), sb_asset_gain(C))    :- sb_capitalized(C).
fired(sb_4, sb_capitalized(C), asset_supply_slow(C)) :- sb_capitalized(C).
fired(sb_4, sb_capitalized(C), expected_to_last(C))  :- sb_capitalized(C).
effect(sb_capitalized(C), O, "asset_value", increase, short, invisible, "B") :- sb_capitalized(C), sb_asset_owner(C, O).

% SB-5 with RS-5: a payment conditional on criteria draws reshaping to qualify, where qualifying costs less than the payment
% is worth (qualifying_pays).
sb_reshaped(C) :- sb_takeup(C), criteria(C), holds(qualifying_pays(C)), not exception(sb_5, C).
fired(sb_5, sb_reshaped(C), sb_takeup(C))       :- sb_reshaped(C).
fired(rs_5, sb_reshaped(C), qualifying_pays(C)) :- sb_reshaped(C).
% The criteria bind whoever must meet them (sb_qualifier: the recipients unless the record names another class, such as
% installers who must be certified).
effect(sb_reshaped(C), Q, "reclassification", increase, short, invisible, "B") :- sb_reshaped(C), sb_qualifier(C, Q).

% SB-5 with RS-7: a gain concentrated on the sellers that depends on a later decision (renewal or review) draws their
% lobbying, if they can organize at a cost below their stake (beneficiaries_organize).
% The sellers who gain are the recipients themselves where they sell.
sb_gaining_seller(C, S) :- sb_seller(C, S).
sb_gaining_seller(C, R) :- sb_recipient(C, R), sb_recipients_sell(C).
sb_lobbies(C) :- sb_takeup(C), renewable(C), sb_gaining_seller(C, _), holds(beneficiaries_organize(C)), not exception(rs_7, C).
fired(rs_7, sb_lobbies(C), sb_takeup(C))              :- sb_lobbies(C).
fired(rs_7, sb_lobbies(C), beneficiaries_organize(C)) :- sb_lobbies(C).
effect(sb_lobbies(C), S, "lobbying_effort", increase, medium, invisible, "B") :- sb_lobbies(C), sb_gaining_seller(C, S).

% PC-2 (group form) with LW-6: a payment handed out at a fixed price in a fixed number is rationed by other means than price
% when more want it than the budget allows (oversubscribed): claimants race and queue, or claims go by connections. Which
% margin is used is not established, so the sign is the group.
sb_rationed(C) :- sb_takeup(C), budget_capped(C), holds(oversubscribed(C)), not exception(pc_2, C).
fired(lw_6, sb_rationed(C), budget_capped(C))  :- sb_rationed(C).
fired(pc_2, sb_rationed(C), oversubscribed(C)) :- sb_rationed(C).
group_effect(sb_rationed(C), R, "wait_time,allocation_by_non_price_criteria", at_least_one_increase, short, invisible, "B") :- sb_rationed(C), sb_recipient(C, R).

% RS-8: recipients who mean to claim (takeup) and learn of the subsidy before it starts delay purchases they would have made
% in the meantime (can_delay).
% A purchase subsidy only: a payment to producers per unit sold is not a purchase the recipients can put off.
sb_delayed(C) :- sb_takeup(C), announced(C), not sb_recipients_sell(C), holds(can_delay(C)), not exception(rs_8, C).
fired(rs_8, sb_delayed(C), sb_takeup(C)) :- sb_delayed(C).
fired(rs_8, sb_delayed(C), announced(C)) :- sb_delayed(C).
fired(rs_8, sb_delayed(C), can_delay(C)) :- sb_delayed(C).
window(sb_delayed(C), announcement) :- sb_delayed(C).
effect(sb_delayed(C), R, "quantity_traded", decrease, short, invisible, "B") :- sb_delayed(C), sb_recipient(C, R).

% SB-6: a temporary purchase subsidy moves purchases into its window. After it expires, buyers who brought their purchase
% forward do not buy again (pulled_forward), so sellers sell less than they would have. The dip needs the payment to end
% as scheduled (ends_as_scheduled): a renewal or a repeat moves the purchases on again (found out of sample on WE-020,
% where non-renewal is below the cut-off). Where the sellers' supply still cannot adjust when the payment ends
% (supply_slow_at_expiry: a premise about that date, not the start; found out of sample on WE-021) the price they
% receive falls in that window (CR-6).
sb_dip(C) :- sb_expands(C), temporary(C), not sb_recipients_sell(C), holds(pulled_forward(C)), holds(ends_as_scheduled(C)), not exception(sb_6, C).
fired(sb_6, sb_dip(C), sb_expands(C))        :- sb_dip(C).
fired(sb_6, sb_dip(C), pulled_forward(C))    :- sb_dip(C).
fired(sb_6, sb_dip(C), ends_as_scheduled(C)) :- sb_dip(C).
window(sb_dip(C), after_expiry) :- sb_dip(C).
effect(sb_dip(C), S, "quantity_traded", decrease, short, invisible, "B") :- sb_dip(C), sb_seller(C, S).
sb_dip_price(C) :- sb_dip(C), holds(supply_slow_at_expiry(C)).
fired(sb_6, sb_dip_price(C), sb_dip(C))                :- sb_dip_price(C).
fired(cr_6, sb_dip_price(C), supply_slow_at_expiry(C)) :- sb_dip_price(C).
window(sb_dip_price(C), after_expiry) :- sb_dip_price(C).
effect(sb_dip_price(C), S, "net_price_received", decrease, medium, invisible, "B") :- sb_dip_price(C), sb_seller(C, S).

% SB-6, scrappage: the payment requires destroying a used good. The goods scrapped would otherwise have stayed in use
% (would_stay_in_use), so the stock of used goods falls for those who buy them, and the resales they would later have
% been sold in do not happen (OC-4). Where other supply cannot replace them quickly (used_supply_slow), used goods cost
% more and the owners who keep theirs hold a more valuable asset (SB-4).
sb_scrapped(C) :- sb_takeup(C), scrappage(C), not exception(sb_6, C).
fired(sb_6, sb_scrapped(C), sb_takeup(C)) :- sb_scrapped(C).
effect(sb_scrapped(C), D, "quantity_traded", increase, short, invisible, "B") :- sb_scrapped(C), sb_scrapper(C, D).
sb_stock_falls(C) :- sb_scrapped(C), holds(would_stay_in_use(C)).
fired(sb_6, sb_stock_falls(C), sb_scrapped(C))       :- sb_stock_falls(C).
fired(sb_6, sb_stock_falls(C), would_stay_in_use(C)) :- sb_stock_falls(C).
effect(sb_stock_falls(C), U, "quantity_substitute", decrease, short, visible, "B") :- sb_stock_falls(C), sb_used_buyer(C, U).
sb_resales_lost(C) :- sb_stock_falls(C), not exception(oc_4, C).
fired(oc_4, sb_resales_lost(C), sb_stock_falls(C)) :- sb_resales_lost(C).
effect(sb_resales_lost(C), U, "quantity_traded", decrease, medium, invisible, "B") :- sb_resales_lost(C), sb_used_buyer(C, U).
sb_used_dearer(C) :- sb_stock_falls(C), holds(used_supply_slow(C)).
fired(sb_6, sb_used_dearer(C), sb_stock_falls(C))   :- sb_used_dearer(C).
fired(sb_6, sb_used_dearer(C), used_supply_slow(C)) :- sb_used_dearer(C).
effect(sb_used_dearer(C), U, "price_substitute", increase, short, invisible, "B") :- sb_used_dearer(C), sb_used_buyer(C, U).
sb_used_revalued(C) :- sb_used_dearer(C), not exception(sb_4, C).
fired(sb_4, sb_used_revalued(C), sb_used_dearer(C)) :- sb_used_revalued(C).
effect(sb_used_revalued(C), O, "asset_value", increase, short, invisible, "B") :- sb_used_revalued(C), sb_used_owner(C, O).

% RS-11: a payment repaid if the recipient moves within a period ties it to staying put. Recipients turn down
% opportunities that would require a move (opportunities_need_move), so they change jobs and homes less.
sb_lockin(C) :- sb_takeup(C), repay_on_move(C), holds(opportunities_need_move(C)), not exception(rs_11, C).
fired(rs_11, sb_lockin(C), repay_on_move(C))          :- sb_lockin(C).
fired(rs_11, sb_lockin(C), opportunities_need_move(C)) :- sb_lockin(C).
effect(sb_lockin(C), R, "job_changes", decrease, short, invisible, "B") :- sb_lockin(C), sb_recipient(C, R).
effect(sb_lockin(C), R, "turnover", decrease, short, invisible, "B")    :- sb_lockin(C), sb_recipient(C, R).

#show holds/1.
#show fired/3.
#show effect/7.
#show group_effect/7.
#show window/2.
#show item/2.
