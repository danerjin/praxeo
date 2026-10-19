% Mandates (handbook catalog 1.4): PC-17 (a mandated contract term), PC-18 (a prohibited contract term) and EN-14 (a standard
% on new units, with the stock exempt), with RS-4, RS-5, RS-7, RS-11, RS-14, RS-17, RS-18, RS-20, RS-23, PC-10, CR-7, CR-9,
% OC-1, OC-2 and OC-3 where a mandate brings them in. PC-17 was developed on WE-029 (paid sick leave); PC-18 and EN-14 are
% written from the catalog alone. Input facts, written by praxeo/engine.py from the policy record:
%   mandate(C).                    a mandated_contract_term: every contract of a kind must carry a term
%   bound(C, A).                   who must provide it (employers without the term)
%   mc_recipient(C, A).            who receives it (their workers)
%   mc_floor_recipient(C, A).      recipients whose wage an existing floor holds (PC-10)
%   mc_applicant(C, A).            would-be recipients, among whom the provider chooses (RS-23)
%   mc_already(C, A). mc_already_recipient(C, A).   providers who already offer the term on other conditions, and their
%                                  recipients
%   mc_below_cap(C, A). mc_above_cap(C, A).          recipients below and above a per-head cap on the term (RS-18)
%   mc_cover_seller(C, A).         sellers of cover for absences (a paid absence)
%   mc_output_buyer(C, A).         buyers of the providers' output (RS-14)
%   mc_tradable(C, A). neighbor_seller(C, A).        providers selling against rivals across a boundary, and those rivals
%   mc_rival(C, A).                unbound rivals of the providers in their output market (CR-9)
%   mc_outside(C, A).              those engaged outside the mandate's definitions (contractors; RS-5)
%   mc_complainant(C, A). mc_violator(C, A).         recipients who complain and win; providers found in breach (RS-20)
%   mc_near_threshold(C, A). mc_below_threshold(C, A).  providers near a size threshold, and those below it (RS-17)
%   mc_margin_recipient(C, A).     recipients whose coverage turns on a reading (covered where margin_covered(C))
%   per_head_cap(C). paid_absence(C). forfeit_on_leaving(C). complaint_only(C). size_threshold(C). threshold_staff_split(C).
%   threshold_partial_count(C). margin_covered(C). definition_line(C). general_budget(C). tax_named(C).
%   term_ban(C). tb_freed(C, A). restrains_mobility(C). voids_existing(C).       PC-18
%   standard(C). st_buyer(C, A). stock_exempt(C). st_stock_owner(C, A).            EN-14
%   enforcer(C, A). taxpayer(C, A). mc_payer_group(C, "a,b,c").
% Every rule is monotone in holds/1: it negates only plain facts.

{ holds(A) } :- assumption(A).

% ------------------------------------------------------------------ PC-17: a mandated contract term

% CR-1, CR-5c: where the term was absent from some contracts (binding) and providers comply (enforced), the recipients get it
% and the providers' cost per unit of the exchange rises.
% The contract chains need the counterparty: a record that names no recipient (an obligation owed to the state, such as a
% licence's coverage duty) gets only OC-2, OC-3 and RS-7 (found on WE-056 and WE-064).
mc_binds(C) :- mandate(C), mc_recipient(C, _), holds(binding(C)), holds(enforced(C)), not exception(pc_17, C).
fired(pc_17, mc_binds(C), binding(C))  :- mc_binds(C).
fired(pc_17, mc_binds(C), enforced(C)) :- mc_binds(C).
effect(mc_binds(C), R, "non_wage_compensation", increase, short, visible, "B") :- mc_binds(C), mc_recipient(C, R).

% The cost stays with the providers while the other terms are fixed (wages_sticky, short run; CR-6 0.8) or, after they
% adjust, where the term is worth less to the recipient than it costs the provider (worth_less; CR-2 0.7, CR-12e).
mc_cost_stays(C) :- mc_binds(C), holds(wages_sticky(C)).
mc_cost_stays(C) :- mc_binds(C), holds(worth_less(C)).
fired(cr_6, mc_cost_stays(C), mc_binds(C))     :- mc_cost_stays(C).
fired(cr_6, mc_cost_stays(C), wages_sticky(C)) :- mc_cost_stays(C), holds(wages_sticky(C)).
fired(cr_12, mc_cost_stays(C), worth_less(C))  :- mc_cost_stays(C), holds(worth_less(C)).
effect(mc_cost_stays(C), B, "price_paid", increase, short, visible, "B") :- mc_cost_stays(C), bound(C, B).

% PC-17 Then: the bargaining range moves, so the other terms adjust, at least one: jobs, hours, other benefits. Short run
% while the wage is fixed; medium run where the term is worth less than it costs.
mc_others_short(C) :- mc_binds(C), holds(wages_sticky(C)).
fired(pc_17, mc_others_short(C), mc_binds(C))     :- mc_others_short(C).
fired(cr_6, mc_others_short(C), wages_sticky(C))  :- mc_others_short(C).
group_effect(mc_others_short(C), R, "employment,hours_worked,non_wage_compensation", at_least_one_decrease, short, invisible, "B") :- mc_others_short(C), mc_recipient(C, R).
mc_others_medium(C) :- mc_binds(C), holds(worth_less(C)).
fired(pc_17, mc_others_medium(C), mc_binds(C))  :- mc_others_medium(C).
fired(cr_2, mc_others_medium(C), worth_less(C)) :- mc_others_medium(C).
group_effect(mc_others_medium(C), R, "employment,hours_worked,non_wage_compensation", at_least_one_decrease, medium, invisible, "B") :- mc_others_medium(C), mc_recipient(C, R).

% PC-17 with CR-4 on each side and CR-6: where the wage can adjust (wages_adjust), it falls; both sides push it the same way,
% so no comparison of value and cost is needed.
mc_wage(C) :- mc_binds(C), holds(wages_adjust(C)), not exception(pc_17, C).
fired(pc_17, mc_wage(C), mc_binds(C))     :- mc_wage(C).
fired(cr_6, mc_wage(C), wages_adjust(C))  :- mc_wage(C).
effect(mc_wage(C), R, "wage_rate", decrease, medium, invisible, "B") :- mc_wage(C), mc_recipient(C, R).

% CR-7b: who bears the term's gross cost. Where the recipients' alternatives are worse than the providers' (alternatives_worse),
% the recipients bear the larger share as the wage adjusts.
mc_incidence(C) :- mc_wage(C), holds(alternatives_worse(C)), not exception(cr_7, C).
fired(cr_7, mc_incidence(C), mc_wage(C))             :- mc_incidence(C).
fired(cr_7, mc_incidence(C), alternatives_worse(C))  :- mc_incidence(C).
effect(mc_incidence(C), R, "tax_share_borne", increase, medium, invisible, "B") :- mc_incidence(C), mc_recipient(C, R).

% PC-10 through an existing floor: where the wage cannot fall (floor_binds), the cost stays with providers at every horizon
% and the other terms of the recipients at the floor adjust, at least one.
mc_floor(C) :- mc_binds(C), mc_floor_recipient(C, _), holds(floor_binds(C)), not exception(pc_10, C).
fired(pc_10, mc_floor(C), mc_binds(C))      :- mc_floor(C).
fired(pc_10, mc_floor(C), floor_binds(C))   :- mc_floor(C).
group_effect(mc_floor(C), R, "employment,hours_worked,non_wage_compensation", at_least_one_decrease, short, invisible, "B") :- mc_floor(C), mc_floor_recipient(C, R).

% CR-7b, CR-7c: while the cost stays with providers, their returns and their means fall (CR-8b: the term is paid to the
% recipients); owners of businesses valued on expected earnings (valued_on_earnings) see the value fall when the mandate
% becomes expected.
mc_returns(C) :- mc_binds(C), holds(wages_sticky(C)).
fired(cr_7, mc_returns(C), mc_binds(C))     :- mc_returns(C).
fired(cr_7, mc_returns(C), wages_sticky(C)) :- mc_returns(C).
effect(mc_returns(C), B, "return_on_capital", decrease, short, invisible, "B") :- mc_returns(C), bound(C, B).
effect(mc_returns(C), B, "resources_available_other_uses", decrease, short, invisible, "B") :- mc_returns(C), bound(C, B).
mc_capitalized(C) :- mc_returns(C), holds(valued_on_earnings(C)), not exception(cr_7, C).
fired(cr_7, mc_capitalized(C), mc_returns(C))           :- mc_capitalized(C).
fired(cr_7, mc_capitalized(C), valued_on_earnings(C))   :- mc_capitalized(C).
effect(mc_capitalized(C), B, "asset_value", decrease, short, invisible, "B") :- mc_capitalized(C), bound(C, B).

% CR-12: recipients' earnings. A paid absence that replaces an unpaid one (unpaid_absence_before) raises them; fewer jobs
% and hours, or a lower wage, lower them. Both chains are kept; where both are reported the sign is ambiguous (_resolve).
mc_earn_up(C) :- mc_binds(C), paid_absence(C), holds(unpaid_absence_before(C)).
fired(cr_8, mc_earn_up(C), mc_binds(C))               :- mc_earn_up(C).
fired(cr_8, mc_earn_up(C), unpaid_absence_before(C))  :- mc_earn_up(C).
effect(mc_earn_up(C), R, "earnings", increase, short, invisible, "B") :- mc_earn_up(C), mc_recipient(C, R).
mc_earn_down(C) :- mc_others_short(C).
mc_earn_down(C) :- mc_wage(C).
fired(cr_12, mc_earn_down(C), mc_others_short(C)) :- mc_earn_down(C), mc_others_short(C).
fired(cr_12, mc_earn_down(C), mc_wage(C))         :- mc_earn_down(C), mc_wage(C).
effect(mc_earn_down(C), R, "earnings", decrease, short, invisible, "B") :- mc_earn_down(C), mc_recipient(C, R).

% A paid absence (CR-3b, CR-4): absence is now cheaper than unpaid absence, so where some recipients use it (absence_used)
% hours present fall; where providers cover absent shifts (absences_covered), sellers of cover sell more.
mc_absence(C) :- mc_binds(C), paid_absence(C), holds(absence_used(C)), not exception(cr_4, C).
fired(cr_4, mc_absence(C), mc_binds(C))       :- mc_absence(C).
fired(cr_4, mc_absence(C), absence_used(C))   :- mc_absence(C).
effect(mc_absence(C), R, "hours_worked", decrease, short, invisible, "B") :- mc_absence(C), mc_recipient(C, R).
mc_cover(C) :- mc_absence(C), holds(absences_covered(C)), not exception(cr_9, C).
fired(cr_9, mc_cover(C), mc_absence(C))         :- mc_cover(C).
fired(cr_9, mc_cover(C), absences_covered(C))   :- mc_cover(C).
effect(mc_cover(C), S, "quantity_traded", increase, short, invisible, "B") :- mc_cover(C), mc_cover_seller(C, S).

% RS-18: the term per head stops at a cap. Below the cap every hour carries it; above it, an extra hour from an existing
% recipient adds nothing. Where providers can move hours between them (hours_shift), those below the cap lose jobs or hours;
% those above it gain hours from the shift and from covering absences, and lose them to the general cost rise (worth_less):
% opposite chains, ambiguous where both are reported.
mc_cap_shift(C) :- mc_binds(C), per_head_cap(C), holds(hours_shift(C)), not exception(rs_18, C).
fired(rs_18, mc_cap_shift(C), per_head_cap(C)) :- mc_cap_shift(C).
fired(rs_18, mc_cap_shift(C), hours_shift(C))  :- mc_cap_shift(C).
group_effect(mc_cap_shift(C), R, "employment,hours_worked", at_least_one_decrease, medium, invisible, "B") :- mc_cap_shift(C), mc_below_cap(C, R).
effect(mc_cap_shift(C), R, "hours_worked", increase, medium, invisible, "B") :- mc_cap_shift(C), mc_above_cap(C, R).
mc_cap_cover(C) :- mc_cover(C), per_head_cap(C).
fired(rs_18, mc_cap_cover(C), mc_cover(C)) :- mc_cap_cover(C).
effect(mc_cap_cover(C), R, "hours_worked", increase, medium, invisible, "B") :- mc_cap_cover(C), mc_above_cap(C, R).
mc_cap_cost(C) :- mc_others_medium(C), per_head_cap(C).
fired(cr_4, mc_cap_cost(C), mc_others_medium(C)) :- mc_cap_cost(C).
effect(mc_cap_cost(C), R, "hours_worked", decrease, medium, invisible, "B") :- mc_cap_cost(C), mc_above_cap(C, R).

% RS-23: the term's cost differs by recipient while its terms are uniform; where providers can tell (can_screen), they choose
% among applicants by non-price criteria.
mc_screen(C) :- mc_binds(C), mc_applicant(C, _), holds(can_screen(C)), not exception(rs_23, C).
fired(rs_23, mc_screen(C), mc_binds(C))    :- mc_screen(C).
fired(rs_23, mc_screen(C), can_screen(C))  :- mc_screen(C).
effect(mc_screen(C), P, "allocation_by_non_price_criteria", increase, medium, invisible, "B") :- mc_screen(C), mc_applicant(C, P).

% PC-17 (not binding for those who already offer the term): where their conditions differ from the mandate's
% (conditions_differ), they rewrite them (CR-8c), and their recipients gain the mandated conditions (CR-1 operation 2).
mc_rewrite(C) :- mandate(C), mc_already(C, _), holds(conditions_differ(C)), holds(enforced(C)), not exception(pc_17, C).
fired(pc_17, mc_rewrite(C), conditions_differ(C)) :- mc_rewrite(C).
fired(pc_17, mc_rewrite(C), enforced(C))          :- mc_rewrite(C).
effect(mc_rewrite(C), A, "compliance_cost", increase, short, invisible, "B") :- mc_rewrite(C), mc_already(C, A).
effect(mc_rewrite(C), R, "non_wage_compensation", increase, short, invisible, "B") :- mc_rewrite(C), mc_already_recipient(C, R).

% CR-1: recipients whose coverage turns on a reading get the term only where the reading covers them (margin_covered).
mc_margin(C) :- mc_binds(C), margin_covered(C).
fired(cr_1, mc_margin(C), margin_covered(C)) :- mc_margin(C).
effect(mc_margin(C), R, "non_wage_compensation", increase, short, invisible, "B") :- mc_margin(C), mc_margin_recipient(C, R).

% RS-14 with CR-9: where the cost stays with providers and their rivals in the output market are bound too (rivals_bound),
% the price of the output rises and its buyers buy less (CR-4c).
mc_pass(C) :- mc_cost_stays(C), mc_output_buyer(C, _), holds(rivals_bound(C)), not exception(rs_14, C).
fired(rs_14, mc_pass(C), mc_cost_stays(C))  :- mc_pass(C).
fired(rs_14, mc_pass(C), rivals_bound(C))   :- mc_pass(C).
effect(mc_pass(C), X, "price_paid", increase, short, invisible, "B")       :- mc_pass(C), mc_output_buyer(C, X).
effect(mc_pass(C), X, "quantity_traded", decrease, short, invisible, "B")  :- mc_pass(C), mc_output_buyer(C, X).

% RS-4, RS-6: providers selling against unbound rivals across a boundary (rivals_unbound) lose output to them over time,
% where the cost stays after the wage adjusts (worth_less).
mc_relocate(C) :- mc_others_medium(C), mc_tradable(C, _), holds(rivals_unbound(C)), not exception(rs_4, C).
fired(rs_4, mc_relocate(C), mc_others_medium(C)) :- mc_relocate(C).
fired(rs_4, mc_relocate(C), rivals_unbound(C))   :- mc_relocate(C).
effect(mc_relocate(C), T, "quantity_supplied", decrease, long, invisible, "B") :- mc_relocate(C), mc_tradable(C, T).
effect(mc_relocate(C), N, "quantity_supplied", increase, medium, invisible, "B") :- mc_relocate(C), neighbor_seller(C, N).

% CR-9, CR-7c: unbound rivals of the providers (exempt or already offering the term) gain sales where they compete with them
% (compete_with_bound) and the cost stays after the wage adjusts; the expected gain is capitalized where firms are valued on
% expected earnings.
mc_rivals(C) :- mc_others_medium(C), mc_rival(C, _), holds(compete_with_bound(C)), not exception(cr_9, C).
fired(cr_9, mc_rivals(C), mc_others_medium(C))    :- mc_rivals(C).
fired(cr_9, mc_rivals(C), compete_with_bound(C))  :- mc_rivals(C).
effect(mc_rivals(C), V, "quantity_supplied", increase, medium, invisible, "B") :- mc_rivals(C), mc_rival(C, V).
mc_rivals_value(C) :- mc_capitalized(C), mc_rival(C, _), holds(compete_with_bound(C)), not exception(cr_7, C).
fired(cr_7, mc_rivals_value(C), mc_capitalized(C))      :- mc_rivals_value(C).
fired(cr_7, mc_rivals_value(C), compete_with_bound(C))  :- mc_rivals_value(C).
effect(mc_rivals_value(C), V, "asset_value", increase, short, invisible, "B") :- mc_rivals_value(C), mc_rival(C, V).

% RS-5: where the definitions draw a line (contractors outside the mandate) and reshaping pays, some work moves outside it.
mc_reshaped(C) :- mc_binds(C), definition_line(C), holds(reshaping_pays(C)), not exception(rs_5, C).
fired(rs_5, mc_reshaped(C), definition_line(C))  :- mc_reshaped(C).
fired(rs_5, mc_reshaped(C), reshaping_pays(C))   :- mc_reshaped(C).
effect(mc_reshaped(C), B, "reclassification", increase, medium, invisible, "B") :- mc_reshaped(C), bound(C, B).
effect(mc_reshaped(C), O, "reclassification", increase, medium, invisible, "B") :- mc_reshaped(C), mc_outside(C, O).

% RS-11: where something the term gives is lost on leaving (a balance, a waiting period), job changes at the margin
% (move_marginal) fall.
mc_lockin(C) :- mc_binds(C), forfeit_on_leaving(C), holds(move_marginal(C)), not exception(rs_11, C).
fired(rs_11, mc_lockin(C), forfeit_on_leaving(C)) :- mc_lockin(C).
fired(rs_11, mc_lockin(C), move_marginal(C))      :- mc_lockin(C).
effect(mc_lockin(C), R, "job_changes", decrease, medium, invisible, "B") :- mc_lockin(C), mc_recipient(C, R).

% RS-20: enforcement only on complaint. Where complaint is unlikely for some recipients (complaint_unlikely), breach rises
% from none (1.0 baseline); where complaints are filed (complaints_filed), recipients spend time on them, and awards pass
% from the providers found in breach to the complainants (CR-8b).
mc_breach(C) :- mandate(C), complaint_only(C), holds(complaint_unlikely(C)), holds(binding(C)), not exception(rs_20, C).
fired(rs_20, mc_breach(C), complaint_only(C))      :- mc_breach(C).
fired(rs_20, mc_breach(C), complaint_unlikely(C))  :- mc_breach(C).
fired(rs_20, mc_breach(C), binding(C))             :- mc_breach(C).
effect(mc_breach(C), B, "legal_breach", increase, short, invisible, "B") :- mc_breach(C), bound(C, B).
mc_complaints(C) :- mandate(C), complaint_only(C), holds(complaints_filed(C)), not exception(oc_2, C).
fired(oc_2, mc_complaints(C), complaint_only(C))   :- mc_complaints(C).
fired(oc_2, mc_complaints(C), complaints_filed(C)) :- mc_complaints(C).
effect(mc_complaints(C), R, "compliance_cost", increase, short, invisible, "B") :- mc_complaints(C), mc_recipient(C, R).
mc_awards(C) :- mc_breach(C), mc_complaints(C).
fired(cr_8, mc_awards(C), mc_breach(C))      :- mc_awards(C).
fired(cr_8, mc_awards(C), mc_complaints(C))  :- mc_awards(C).
effect(mc_awards(C), W, "resources_available_other_uses", increase, short, invisible, "B") :- mc_awards(C), mc_complainant(C, W).
effect(mc_awards(C), V, "resources_available_other_uses", decrease, short, invisible, "B") :- mc_awards(C), mc_violator(C, V).

% RS-17: a size threshold. Where staying below it pays (staying_small_pays), firms near it hire fewer of the staff it counts,
% and more firms stay below it. Where the record splits off a class of staff whose counting is at issue
% (threshold_staff_split), that class is hired less where it counts and more, in place of counted staff, where it does not
% (threshold_partial_count; CR-4, x: hire counted staff, y: uncounted staff).
mc_threshold(C) :- mandate(C), size_threshold(C), holds(staying_small_pays(C)), holds(binding(C)), not exception(rs_17, C).
fired(rs_17, mc_threshold(C), size_threshold(C))       :- mc_threshold(C).
fired(rs_17, mc_threshold(C), staying_small_pays(C))   :- mc_threshold(C).
fired(rs_17, mc_threshold(C), binding(C))              :- mc_threshold(C).
effect(mc_threshold(C), N, "employment", decrease, short, invisible, "B") :- mc_threshold(C), mc_near_threshold(C, N).
item(mc_threshold(C), "counted_staff") :- mc_threshold(C), threshold_staff_split(C).
mc_stay_small(C) :- mc_threshold(C), mc_below_threshold(C, _).
fired(rs_17, mc_stay_small(C), mc_threshold(C)) :- mc_stay_small(C).
effect(mc_stay_small(C), S, "number_of_sellers", increase, medium, invisible, "B") :- mc_stay_small(C), mc_below_threshold(C, S).
mc_threshold_other(C) :- mc_threshold(C), threshold_staff_split(C).
fired(rs_17, mc_threshold_other(C), mc_threshold(C)) :- mc_threshold_other(C).
item(mc_threshold_other(C), "other_staff") :- mc_threshold_other(C).
effect(mc_threshold_other(C), N, "employment", increase, medium, invisible, "B") :- mc_threshold_other(C), threshold_partial_count(C), mc_near_threshold(C, N).
effect(mc_threshold_other(C), N, "employment", decrease, medium, invisible, "B") :- mc_threshold_other(C), not threshold_partial_count(C), mc_near_threshold(C, N).

% OC-2 and CR-8c: complying takes resources (records, payroll, notices), Tier A given the mandate.
mc_compliance(C) :- mandate(C), not exception(oc_2, C).
fired(oc_2, mc_compliance(C), mandate(C)) :- mc_compliance(C).
effect(mc_compliance(C), B, "compliance_cost", increase, short, invisible, "A") :- mc_compliance(C), bound(C, B).

% RS-7: those who bear the mandate lobby to narrow it where they can organize (can_organize); its recipients lobby to widen
% it where they can (recipients_organize).
% Only where the measure binds: a rule that changes no contract imposes no stake to lobby over.
mc_rule_binds(C) :- mandate(C), holds(binding(C)).
mc_rule_binds(C) :- standard(C), holds(binding(C)).
mc_rule_binds(C) :- term_ban(C), holds(binding(C)).
mc_lobby(C) :- mc_rule_binds(C), holds(can_organize(C)), not exception(rs_7, C).
fired(rs_7, mc_lobby(C), binding(C))      :- mc_lobby(C).
fired(rs_7, mc_lobby(C), can_organize(C)) :- mc_lobby(C).
effect(mc_lobby(C), B, "lobbying_effort", increase, medium, invisible, "B") :- mc_lobby(C), bound(C, B).
mc_recipients_lobby(C) :- mandate(C), holds(binding(C)), holds(recipients_organize(C)), not exception(rs_7, C).
fired(rs_7, mc_recipients_lobby(C), binding(C))             :- mc_recipients_lobby(C).
fired(rs_7, mc_recipients_lobby(C), recipients_organize(C)) :- mc_recipients_lobby(C).
effect(mc_recipients_lobby(C), R, "lobbying_effort", increase, medium, invisible, "B") :- mc_recipients_lobby(C), mc_recipient(C, R).
lobby_concl(mc_lobby(C), C) :- mc_lobby(C).
lobby_concl(mc_recipients_lobby(C), C) :- mc_recipients_lobby(C).

% OC-3: an enforcing agency (Tier A); with a general budget, OC-1's payers bear it (the payer group unless a tax is named).
mc_rule(C) :- mandate(C).
mc_rule(C) :- standard(C).
mc_rule(C) :- term_ban(C), enforcer(C, _).
mc_administered(C) :- mc_rule(C), enforcer(C, _), not exception(oc_3, C).
fired(oc_3, mc_administered(C), mandate(C))  :- mc_administered(C), mandate(C).
fired(oc_3, mc_administered(C), standard(C)) :- mc_administered(C), standard(C).
fired(oc_3, mc_administered(C), term_ban(C)) :- mc_administered(C), term_ban(C).
effect(mc_administered(C), E, "enforcement_cost", increase, short, invisible, "A") :- mc_administered(C), enforcer(C, E).
mc_funded(C) :- mc_administered(C), general_budget(C), not exception(oc_1, C).
fired(oc_1, mc_funded(C), general_budget(C)) :- mc_funded(C).
effect(mc_funded(C), T, "resources_available_other_uses", decrease, short, invisible, "A") :- mc_funded(C), tax_named(C), taxpayer(C, T).
group_effect(mc_funded(C), G, "resources_available_other_uses", at_least_one_decrease, short, invisible, "A") :- mc_funded(C), mc_payer_group(C, G), not tax_named(C).

% ------------------------------------------------------------------ PC-18: a prohibited contract term

% CR-1: where the term was in use (binding), the option of buying its protection is removed for the party that used it (bound)
% and the option of breaking it added for the other (tb_freed). Where the term restrained the mobility of a means
% (restrains_mobility), its owner moves more (CR-7: the gain from mobility goes to the owner).
tb_binds(C) :- term_ban(C), holds(binding(C)), not exception(pc_18, C).
fired(pc_18, tb_binds(C), binding(C)) :- tb_binds(C).
tb_mobile(C) :- tb_binds(C), restrains_mobility(C).
fired(cr_7, tb_mobile(C), restrains_mobility(C)) :- tb_mobile(C).
effect(tb_mobile(C), F, "job_changes", increase, short, invisible, "B") :- tb_mobile(C), tb_freed(C, F).
% CR-5c, CR-6: the party who valued the term offers less on the other terms (wage, training it funds), at least one, where it
% valued the term (term_valued); and shifts to substitute terms where they exist (substitute_terms).
tb_others(C) :- tb_binds(C), holds(term_valued(C)), not exception(pc_18, C).
fired(pc_18, tb_others(C), tb_binds(C))     :- tb_others(C).
fired(cr_6, tb_others(C), term_valued(C))   :- tb_others(C).
group_effect(tb_others(C), F, "wage_rate,non_wage_compensation", at_least_one_decrease, medium, invisible, "B") :- tb_others(C), tb_freed(C, F).
tb_substitute(C) :- tb_binds(C), holds(substitute_terms(C)), not exception(pc_18, C).
fired(pc_18, tb_substitute(C), substitute_terms(C)) :- tb_substitute(C).
effect(tb_substitute(C), B, "term_prevalence", increase, short, invisible, "B") :- tb_substitute(C), bound(C, B).
% CR-8 (voiding): where existing contracts are voided, the right voided passes from its holder to the other party.
tb_voided(C) :- tb_binds(C), voids_existing(C).
fired(cr_8, tb_voided(C), voids_existing(C)) :- tb_voided(C).
effect(tb_voided(C), B, "asset_value", decrease, short, invisible, "B") :- tb_voided(C), bound(C, B).

% ------------------------------------------------------------------ EN-14: a standard on new units, the stock exempt

% CR-1, TS-3: where the standard binds on some designs (binding) and is enforced, the cheaper designs are removed: new units
% cost their buyers more, fewer are built (CR-4c), and their makers bear the cost of meeting it.
st_binds(C) :- standard(C), holds(binding(C)), holds(enforced(C)), not exception(en_14, C).
fired(en_14, st_binds(C), binding(C))  :- st_binds(C).
fired(en_14, st_binds(C), enforced(C)) :- st_binds(C).
effect(st_binds(C), X, "price_paid", increase, short, invisible, "B")           :- st_binds(C), st_buyer(C, X).
effect(st_binds(C), X, "specification_level", increase, short, visible, "B")    :- st_binds(C), st_buyer(C, X).
effect(st_binds(C), B, "quantity_supplied", decrease, medium, invisible, "B")   :- st_binds(C), bound(C, B).
effect(st_binds(C), B, "compliance_cost", increase, short, invisible, "B")      :- st_binds(C), bound(C, B).
target_qty(C, decrease) :- st_binds(C).
fired(en_14, target_qty(C, decrease), st_binds(C)) :- target_qty(C, decrease), st_binds(C).
% CR-7c, CR-10b: the exempt stock faces less competition from cheaper new units, so where the two compete (stock_competes) it
% rises in value and is kept in use longer. Unless (1.1): where buyers value the standard (buyers_value_standard), covered
% units draw demand from the stock, which opposes the rise in its value.
st_stock(C) :- st_binds(C), stock_exempt(C), holds(stock_competes(C)), not exception(en_14, C).
fired(en_14, st_stock(C), stock_exempt(C))    :- st_stock(C).
fired(cr_7, st_stock(C), stock_competes(C))   :- st_stock(C).
effect(st_stock(C), O, "asset_value", increase, medium, invisible, "B") :- st_stock(C), st_stock_owner(C, O).
effect(st_stock(C), O, "stock_age", increase, long, invisible, "B")     :- st_stock(C), st_stock_owner(C, O).
st_valued(C) :- st_binds(C), stock_exempt(C), holds(buyers_value_standard(C)), not exception(en_14, C).
fired(en_14, st_valued(C), buyers_value_standard(C)) :- st_valued(C).
effect(st_valued(C), O, "asset_value", decrease, medium, invisible, "B") :- st_valued(C), st_stock_owner(C, O).

#show holds/1.
#show fired/3.
#show effect/7.
#show group_effect/7.
#show window/2.
#show item/2.
