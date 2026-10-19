% Licensing and quotas (handbook catalog 1.4, family EN): EN-1 to EN-3, EN-5, EN-6 and EN-11, with RS-1, RS-3, RS-7, RS-10,
% OC-1, OC-3, OC-4, SB-4 and TX-8 where they bring them in. Licensing was developed on WE-003; the quota rules were written
% from EN-6's text alone. EN-4 (quality, ambiguous by default), EN-7 to EN-10 and EN-12 to EN-15 are not encoded.
% Input facts, written by praxeo/engine.py from the policy record:
%   licensing(C). quota(C).          component C is a licensing_requirement or a quota
%   bound(C, A).                     who must hold a license to sell, or whose quantity is capped (sellers, importers)
%   en_buyer(C, A).                  buyers of the licensed or capped good
%   en_holder(C, A).                 those who hold the license or quota right (default the bound actor)    (EN-2, EN-6)
%   en_trainer(C, A).                sellers of the training or exam the license requires                    (EN-1)
%   transferable(C).                 licenses or quota rights may be sold or leased                          (EN-2, SB-4)
%   import_quota(C).                 the quota caps imports; the tariff roles are written too (EN-6, TX-7, TX-8)
%   en_informal_buyer(C, A).         buyers of the unlicensed or unrecorded trade (default the buyers)      (RS-3, RS-10)
%   allocation_by_history(C).        the right is allocated in proportion to past activity in a base period  (EN-12)
%   base_after_announcement(C).      the base period runs after the measure was announced                  (EN-12)
%   en_entrant(C, A). en_worker(C, A). en_supplier(C, A).  would-be entrants; the bound sellers' workers and suppliers
%   price_fixed(C).                  a rule in force without the measure too fixes the price               (EN-6, PC-1)
%   seller_cap(C).                   the cap is on the number of sellers (licenses), not on quantity         (EN-6 1.0)
%   wider_market(C).                 the capped good's price is set in a wider market                        (EN-6 Unless)
%   enforcer(C, A). general_budget(C). en_payer_group(C, "a,b,c"). tax_named(C). taxpayer(C, A).  (OC-3, OC-1)
% Every rule is monotone in holds/1: it negates only plain facts.

{ holds(A) } :- assumption(A).

en(C) :- licensing(C).
en(C) :- quota(C).

% ---------------------------------------------------------------- licensing (EN-1, EN-2, EN-3, EN-5, EN-11)

% EN-1: a requirement that goes beyond what some would-be sellers already meet (binding), and is enforced, removes the option
% of selling without a license: fewer sellers and less entry, less supplied and a higher price (CR-1, CR-4, CR-6).
lic_binds(C) :- licensing(C), holds(binding(C)), holds(enforced(C)), not exception(en_1, C).
fired(en_1, lic_binds(C), binding(C)) :- lic_binds(C).
fired(en_1, lic_binds(C), enforced(C)) :- lic_binds(C).
effect(lic_binds(C), B, "share_of_sellers_licensed", increase, short, visible, "B") :- lic_binds(C), bound(C, B).
effect(lic_binds(C), B, "number_of_sellers", decrease, short, invisible, "B")       :- lic_binds(C), bound(C, B).
effect(lic_binds(C), B, "entry_rate", decrease, short, invisible, "B")              :- lic_binds(C), bound(C, B).
effect(lic_binds(C), X, "price_paid", increase, short, invisible, "B")              :- lic_binds(C), en_buyer(C, X), not price_fixed(C).
% CR-8b: what the buyers pay above the old price is lost to their other uses.
effect(lic_binds(C), X, "resources_available_other_uses", decrease, short, invisible, "B") :- lic_binds(C), en_buyer(C, X), not price_fixed(C).
% OC-4: the exchanges the higher price prices out are not made; both sides lose them.
lic_prevented(C) :- lic_binds(C), not exception(oc_4, C).
fired(oc_4, lic_prevented(C), lic_binds(C)) :- lic_prevented(C).
effect(lic_prevented(C), X, "quantity_traded", decrease, short, invisible, "B") :- lic_prevented(C), en_buyer(C, X).
effect(lic_prevented(C), B, "quantity_traded", decrease, short, invisible, "B") :- lic_prevented(C), bound(C, B).

% EN-2: with entry restricted, the gain from the higher price settles on those who hold licenses (CR-6, CR-7b); where
% licenses can be sold and are expected to last, their value rises (SB-4).
lic_holders_gain(C) :- lic_binds(C), not exception(en_2, C).
fired(en_2, lic_holders_gain(C), lic_binds(C)) :- lic_holders_gain(C).
effect(lic_holders_gain(C), H, "net_price_received", increase, short, invisible, "B") :- lic_holders_gain(C), en_holder(C, H), not price_fixed(C).

% EN-1 with CR-1 and CR-8c: those who choose to qualify (some_qualify) pay for the training and exam, and its sellers sell more.
lic_qualify(C) :- lic_binds(C), holds(some_qualify(C)), not exception(en_1, C).
fired(en_1, lic_qualify(C), lic_binds(C))     :- lic_qualify(C).
fired(cr_8, lic_qualify(C), some_qualify(C))  :- lic_qualify(C).
effect(lic_qualify(C), B, "compliance_cost", increase, short, invisible, "B")  :- lic_qualify(C), bound(C, B).
effect(lic_qualify(C), T, "quantity_demanded", increase, short, invisible, "B") :- lic_qualify(C), en_trainer(C, T).
% CR-4b with CR-12b: where the training was already commonly taken before the requirement (training_common), those who would
% have taken it may be put off by the license's further conditions (hours, exams), so the trainers' demand is the sum of two
% opposite chains, ambiguous without a premise (found out of sample on WE-016, C-7). The engine keeps the sign of the
% reported chains, so the row is an increase where the premise is below the cut-off.
lic_training_deterred(C) :- lic_qualify(C), en_trainer(C, _), holds(training_common(C)), not exception(cr_4, C).
fired(cr_4, lic_training_deterred(C), lic_qualify(C))      :- lic_training_deterred(C).
fired(cr_4, lic_training_deterred(C), training_common(C))  :- lic_training_deterred(C).
effect(lic_training_deterred(C), T, "quantity_demanded", decrease, short, invisible, "B") :- lic_training_deterred(C), en_trainer(C, T).

% EN-3 with OC-4: would-be sellers who do not qualify move to their next-best occupation, so paid work in the licensed trade
% falls for them (their money earnings fall only with a further premise, not encoded).
lic_excluded(C) :- lic_binds(C), not exception(en_3, C).
fired(en_3, lic_excluded(C), lic_binds(C)) :- lic_excluded(C).
effect(lic_excluded(C), B, "employment", decrease, short, invisible, "B") :- lic_excluded(C), bound(C, B).

% EN-3 with RS-1: buyers priced out turn to doing it themselves or to other substitutes (buyer_substitutes).
lic_substitute(C) :- lic_binds(C), holds(buyer_substitutes(C)), not exception(rs_1, C).
fired(rs_1, lic_substitute(C), lic_binds(C))          :- lic_substitute(C).
fired(rs_1, lic_substitute(C), buyer_substitutes(C))  :- lic_substitute(C).
effect(lic_substitute(C), X, "quantity_substitute", increase, short, invisible, "B") :- lic_substitute(C), en_buyer(C, X).

% EN-3 with RS-3 and RS-10: some keep selling without a license and are not caught (evasion); their buyers search more, can
% judge quality less, and settle disputes outside the courts.
en_informal(C) :- lic_binds(C), holds(evasion(C)), not exception(rs_3, C).
en_informal(C) :- quota_binds(C), holds(evasion(C)), not exception(rs_3, C).
fired(rs_3, en_informal(C), lic_binds(C))   :- en_informal(C), lic_binds(C).
fired(rs_3, en_informal(C), quota_binds(C)) :- en_informal(C), quota_binds(C).
fired(rs_3, en_informal(C), evasion(C))     :- en_informal(C).
effect(en_informal(C), B, "informal_activity", increase, short, invisible, "B")               :- en_informal(C), bound(C, B).
% These fall on the buyers of the unlicensed or unrecorded trade (en_informal_buyer: informal_buyer_actor, default the
% buyers), not on every buyer (found out of sample on WE-055 and WE-028).
effect(en_informal(C), X, "search_cost", increase, short, invisible, "B")                     :- en_informal(C), en_informal_buyer(C, X).
effect(en_informal(C), X, "quality_information", decrease, short, invisible, "B")             :- en_informal(C), en_informal_buyer(C, X).
effect(en_informal(C), X, "disputes_settled_outside_courts", increase, short, invisible, "B") :- en_informal(C), en_informal_buyer(C, X).

% EN-11: where the requirement tests something buyers value but cannot easily judge (tests_valued_quality), the license tells
% the licensed sellers' buyers something about quality (CR-11c).
lic_signal(C) :- lic_binds(C), holds(tests_valued_quality(C)), not exception(en_11, C).
fired(en_11, lic_signal(C), lic_binds(C))             :- lic_signal(C).
fired(en_11, lic_signal(C), tests_valued_quality(C))  :- lic_signal(C).
effect(lic_signal(C), X, "quality_information", increase, short, visible, "B") :- lic_signal(C), en_buyer(C, X).

% ---------------------------------------------------------------- quotas (EN-6)

% EN-6: a quota below the quantity that would otherwise be traded (binding), and enforced, cuts the quantity traded and raises
% the price buyers pay; holders of the rights gain. A cap on the number of sellers (seller_cap) cuts quantity only where the
% cap holds quantity down, which is what `binding` asks there (EN-6 1.0); it also cuts the number of sellers and their entry.
quota_binds(C) :- quota(C), holds(binding(C)), holds(enforced(C)), not exception(en_6, C).
fired(en_6, quota_binds(C), binding(C)) :- quota_binds(C).
fired(en_6, quota_binds(C), enforced(C)) :- quota_binds(C).
effect(quota_binds(C), B, "quantity_traded", decrease, short, invisible, "B")   :- quota_binds(C), bound(C, B).
effect(quota_binds(C), X, "quantity_traded", decrease, short, invisible, "B")   :- quota_binds(C), en_buyer(C, X).
effect(quota_binds(C), H, "net_price_received", increase, short, invisible, "B") :- quota_binds(C), en_holder(C, H), not wider_market(C), not price_fixed(C).
effect(quota_binds(C), B, "number_of_sellers", decrease, medium, visible, "B")  :- quota_binds(C), seller_cap(C), bound(C, B).
effect(quota_binds(C), B, "entry_rate", decrease, medium, invisible, "B")       :- quota_binds(C), seller_cap(C), bound(C, B).
% The buyers' price rises where the good is priced at home. Where its price is set in a wider market (EN-6 Unless), the
% lease price of the right rations the capped quantity, and the buyers' price rises only by as much as the capped quantity
% matters there (price_effect_material).
quota_price(C) :- quota_binds(C), not wider_market(C), not price_fixed(C).
fired(en_6, quota_price(C), quota_binds(C)) :- quota_price(C).
quota_price(C) :- quota_binds(C), wider_market(C), holds(price_effect_material(C)).
fired(en_6, quota_price(C), price_effect_material(C)) :- quota_price(C), wider_market(C).
effect(quota_price(C), X, "price_paid", increase, short, invisible, "B") :- quota_price(C), en_buyer(C, X).
effect(quota_price(C), X, "resources_available_other_uses", decrease, short, invisible, "B") :- quota_price(C), en_buyer(C, X).
quota_lease(C) :- quota_binds(C), wider_market(C), transferable(C), not exception(cr_6, C).
fired(cr_6, quota_lease(C), quota_binds(C)) :- quota_lease(C).
effect(quota_lease(C), H, "right_lease_price", increase, short, invisible, "B") :- quota_lease(C), en_holder(C, H).

% EN-6 for an import quota: "as under TX-7". A binding import quota raises the domestic price as a tariff does, so it is
% the same conclusion as a tariff that bites (tariff_bites), and every chain the tariff rules draw from it applies: TX-7's
% protected domestic sellers, TX-8 for exporters, RS-14 for downstream users, OC-4, SB-4, RS-5, RS-7 and TS-2 (taxes.lp,
% spillovers.lp; found out of sample on WE-014). The engine writes the tariff roles for an import quota but not tariff/1,
% so TX-1's revenue, which a quota does not collect, does not fire.
% Through quota_price, so that a wider market (without a material price effect) or a fixed price stops it too.
tariff_bites(C) :- quota_price(C), import_quota(C).
fired(en_6, tariff_bites(C), quota_price(C)) :- tariff_bites(C), quota_price(C), import_quota(C).
% the tariff rules' burden step (spillovers.lp) names its rule for a tariff only
fired(en_6, tx_burden(C), tariff_bites(C)) :- tx_burden(C), quota(C).
fired(en_6, input_cost_up(C), tariff_bites(C)) :- input_cost_up(C), quota(C).

% EN-6 and EN-1 under an existing price rule (found out of sample on WE-015): where a rule in force without the measure too
% fixes the price (price_fixed: a council-set fare), the restriction cannot raise it. Buyers' price, the holders' net price
% and the buyers' CR-8b loss are not signed; the shortfall shows as excess demand at the fixed price instead (PC-1).
en_shortage(C) :- lic_binds(C), price_fixed(C).
en_shortage(C) :- quota_binds(C), price_fixed(C).
fired(pc_1, en_shortage(C), lic_binds(C))   :- en_shortage(C), lic_binds(C).
fired(pc_1, en_shortage(C), quota_binds(C)) :- en_shortage(C), quota_binds(C).
effect(en_shortage(C), X, "excess_demand", increase, medium, invisible, "B") :- en_shortage(C), en_buyer(C, X).

% ---------------------------------------------------------------- both

% EN-12: a right allocated in proportion to an activity over a base period. Where the base period ended before the measure
% became expected (history_before), the allocation is a windfall to those with history (CR-7c): the right's value rises for
% its holders. Where the base period runs after the announcement (base_after_announcement), and actors know the rule
% (allocation_known), they race to build history in that window (CR-10a): the capped activity, investment in it, entry and
% the work of their crews rise; the racing uses resources up (CR-8c); and assets that carry history gain value (CR-7c, SB-4).
en_windfall(C) :- quota_binds(C), allocation_by_history(C), not base_after_announcement(C), not exception(en_12, C).
fired(en_12, en_windfall(C), quota_binds(C)) :- en_windfall(C).
effect(en_windfall(C), H, "asset_value", increase, short, invisible, "B") :- en_windfall(C), en_holder(C, H).
en_race(C) :- quota(C), allocation_by_history(C), base_after_announcement(C), holds(allocation_known(C)), not exception(en_12, C).
fired(en_12, en_race(C), allocation_by_history(C)) :- en_race(C).
fired(cr_10, en_race(C), allocation_known(C))      :- en_race(C).
window(en_race(C), announcement) :- en_race(C).
effect(en_race(C), B, "quantity_traded", increase, short, invisible, "B")                  :- en_race(C), bound(C, B).
effect(en_race(C), B, "investment_target", increase, short, invisible, "B")                :- en_race(C), bound(C, B).
effect(en_race(C), B, "resources_available_other_uses", decrease, short, invisible, "B")   :- en_race(C), bound(C, B).
effect(en_race(C), B, "asset_value", increase, short, invisible, "B")                      :- en_race(C), bound(C, B).
effect(en_race(C), E, "entry_rate", increase, short, invisible, "B")                       :- en_race(C), en_entrant(C, E).
group_effect(en_race(C), W, "employment,hours_worked", at_least_one_increase, short, invisible, "B") :- en_race(C), en_worker(C, W).

% EN-13: where the rights can be traded or leased at low cost (trade_cheap) and holders' costs or values differ (values_differ), rights move
% to those who value them most (CR-5, CR-7a): fewer users, and in the long run fewer vessels or plants; more per remaining
% user; lessors receive the lease price instead of producing; and the workers and suppliers of those who leave lose (CR-9).
en_consolidate(C) :- quota_binds(C), transferable(C), holds(values_differ(C)), holds(trade_cheap(C)), not exception(en_13, C).
fired(en_13, en_consolidate(C), quota_binds(C))    :- en_consolidate(C).
fired(en_13, en_consolidate(C), values_differ(C))  :- en_consolidate(C).
fired(en_13, en_consolidate(C), trade_cheap(C))    :- en_consolidate(C).
effect(en_consolidate(C), B, "number_of_sellers", decrease, medium, invisible, "B")    :- en_consolidate(C), bound(C, B).
effect(en_consolidate(C), B, "capital_stock_target", decrease, long, invisible, "B")   :- en_consolidate(C), bound(C, B).
effect(en_consolidate(C), B, "quantity_supplied", increase, medium, invisible, "B")    :- en_consolidate(C), bound(C, B).
effect(en_consolidate(C), H, "right_lease_price", increase, medium, invisible, "B")    :- en_consolidate(C), en_holder(C, H).
effect(en_consolidate(C), S, "quantity_traded", decrease, medium, invisible, "B")      :- en_consolidate(C), en_supplier(C, S).
group_effect(en_consolidate(C), W, "employment,hours_worked", at_least_one_decrease, medium, invisible, "B") :- en_consolidate(C), en_worker(C, W).

% EN-2 and EN-6 with SB-4: where licenses or quota rights can be sold, and the restriction is expected to last, the holders'
% gain is capitalized in the value of the right from the time it is expected.
en_capitalized(C) :- lic_holders_gain(C), transferable(C), holds(expected_to_last(C)), not exception(sb_4, C).
en_capitalized(C) :- quota_binds(C), transferable(C), holds(expected_to_last(C)), not exception(sb_4, C).
fired(sb_4, en_capitalized(C), lic_holders_gain(C)) :- en_capitalized(C), lic_holders_gain(C).
fired(sb_4, en_capitalized(C), quota_binds(C))      :- en_capitalized(C), quota_binds(C).
fired(sb_4, en_capitalized(C), expected_to_last(C)) :- en_capitalized(C).
effect(en_capitalized(C), H, "asset_value", increase, short, invisible, "B") :- en_capitalized(C), en_holder(C, H).

% EN-5 with RS-7: holders who gain from the restriction lobby to keep or tighten it, if they can organize (can_organize).
en_lobby(C) :- lic_holders_gain(C), holds(can_organize(C)), not exception(rs_7, C).
en_lobby(C) :- quota_binds(C), holds(can_organize(C)), not exception(rs_7, C).
fired(en_5, en_lobby(C), lic_holders_gain(C)) :- en_lobby(C), lic_holders_gain(C).
fired(rs_7, en_lobby(C), quota_binds(C))      :- en_lobby(C), quota_binds(C).
fired(rs_7, en_lobby(C), can_organize(C))     :- en_lobby(C).
effect(en_lobby(C), H, "lobbying_effort", increase, medium, invisible, "B") :- en_lobby(C), en_holder(C, H).

% OC-3: the rule must be administered and enforced; enforcement work is positive only where the rule binds and is enforced
% (as for ceilings). If the agency's budget rises with the task (enforcement_budget_raised) from a general budget, OC-1's
% payers bear it: the named tax's payers, or else the payer group.
en_administered(C) :- lic_binds(C), not exception(oc_3, C).
en_administered(C) :- quota_binds(C), not exception(oc_3, C).
fired(oc_3, en_administered(C), lic_binds(C))   :- en_administered(C), lic_binds(C).
fired(oc_3, en_administered(C), quota_binds(C)) :- en_administered(C), quota_binds(C).
effect(en_administered(C), E, "enforcement_cost", increase, short, invisible, "B") :- en_administered(C), enforcer(C, E).
en_funded(C) :- en_administered(C), general_budget(C), holds(enforcement_budget_raised(C)).
fired(oc_3, en_funded(C), en_administered(C))           :- en_funded(C).
fired(oc_1, en_funded(C), enforcement_budget_raised(C)) :- en_funded(C).
effect(en_funded(C), T, "resources_available_other_uses", decrease, short, invisible, "B") :- en_funded(C), tax_named(C), taxpayer(C, T).
group_effect(en_funded(C), G, "resources_available_other_uses", at_least_one_decrease, short, invisible, "B") :- en_funded(C), en_payer_group(C, G), not tax_named(C).

#show holds/1.
#show fired/3.
#show effect/7.
#show group_effect/7.
#show window/2.
#show item/2.
