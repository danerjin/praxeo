% Mandates (handbook catalog 1.4): PC-17 (a mandated contract term), PC-18 (a prohibited contract term) and EN-14 (a standard
% on new units, with the stock exempt), with RS-4, RS-5, RS-7, RS-11, RS-14, RS-17, RS-18, RS-20, RS-23, PC-10, CR-7, CR-9,
% OC-1, OC-2 and OC-3 where a mandate brings them in. PC-17 was developed on WE-029 (paid sick leave); PC-18 and EN-14 are
% written from the catalog alone. Input facts, written by praxeo/engine.py from the policy record:
%   mandate(C).                    a mandated_contract_term: every contract of a kind must carry a term
%   employment(C).                 the contract is an employment contract (Component.contract_kind); the wage, hours, jobs
%                                  and earnings chains apply only then (found out of sample on WE-059: a sale contract)
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
%   disclosure(C). (st_buyer: the buyers the disclosure informs; mc_rival: exempt sellers)   EN-15
%   mc_player_recipient(C, A).     play or pay: the recipients who get the term
%   mc_charge_payer(C, A). mc_charge_payer_worker(C, A). mc_charge_capped(C, A). mc_charge_receiver(C, A).  play or pay
%   fixed_cost_per_item(C).        RS-24
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
effect(mc_binds(C), R, "non_wage_compensation", increase, short, visible, "B") :- mc_binds(C), mc_term_holder(C, R).
% Who holds the term: the recipients, or under play or pay only those at firms that provide it (found out of sample on WE-036).
mc_has_players(C) :- mc_player_recipient(C, _).
mc_term_holder(C, R) :- mc_player_recipient(C, R).
mc_term_holder(C, R) :- mc_recipient(C, R), not mc_has_players(C).

% The cost stays with the providers while the other terms are fixed (wages_sticky, short run; CR-6 0.8) or, after they
% adjust, where the term is worth less to the recipient than it costs the provider (worth_less; CR-2 0.7, CR-12e).
mc_cost_stays(C) :- mc_binds(C), holds(wages_sticky(C)).
mc_cost_stays(C) :- mc_binds(C), holds(worth_less(C)).
fired(cr_6, mc_cost_stays(C), mc_binds(C))     :- mc_cost_stays(C).
fired(cr_6, mc_cost_stays(C), wages_sticky(C)) :- mc_cost_stays(C), holds(wages_sticky(C)).
fired(cr_12, mc_cost_stays(C), worth_less(C))  :- mc_cost_stays(C), holds(worth_less(C)).
% The provider's cost per unit is recorded as price_paid only for labour; for a sale the price is a member of the adjusting
% group (PC-17 1.1), not a cost (found out of sample on WE-059).
effect(mc_cost_stays(C), B, "price_paid", increase, short, visible, "B") :- mc_cost_stays(C), employment(C), bound(C, B).
% The cost that stays after the other terms adjust, as a chain of its own: later chains rest on it, never on the group
% (CR-12 1.1: a group is not a chain; found out of sample on WE-059).
mc_cost_after(C) :- mc_binds(C), holds(worth_less(C)).
fired(cr_12, mc_cost_after(C), mc_binds(C))   :- mc_cost_after(C).
fired(cr_2, mc_cost_after(C), worth_less(C))  :- mc_cost_after(C).

% PC-17 Then: the bargaining range moves, so the other terms adjust, at least one: jobs, hours, other benefits. Short run
% while the wage is fixed; medium run where the term is worth less than it costs.
mc_others_short(C) :- mc_binds(C), employment(C), holds(wages_sticky(C)).
fired(pc_17, mc_others_short(C), mc_binds(C))     :- mc_others_short(C).
fired(cr_6, mc_others_short(C), wages_sticky(C))  :- mc_others_short(C).
group_effect(mc_others_short(C), R, "employment,hours_worked,non_wage_compensation", at_least_one_decrease, short, invisible, "B") :- mc_others_short(C), mc_recipient(C, R).
mc_others_medium(C) :- mc_binds(C), employment(C), holds(worth_less(C)).
fired(pc_17, mc_others_medium(C), mc_binds(C))  :- mc_others_medium(C).
fired(cr_2, mc_others_medium(C), worth_less(C)) :- mc_others_medium(C).
group_effect(mc_others_medium(C), R, "employment,hours_worked,non_wage_compensation", at_least_one_decrease, medium, invisible, "B") :- mc_others_medium(C), mc_recipient(C, R).

% PC-17 with CR-4 on each side and CR-6: where the wage can adjust (wages_adjust), it falls; both sides push it the same way,
% so no comparison of value and cost is needed.
mc_wage(C) :- mc_binds(C), employment(C), holds(wages_adjust(C)), not exception(pc_17, C).
fired(pc_17, mc_wage(C), mc_binds(C))     :- mc_wage(C).
fired(cr_6, mc_wage(C), wages_adjust(C))  :- mc_wage(C).
% Not for recipients whose wage a floor holds, whether the floor exists or the measure sets it (found out of sample on WE-061).
effect(mc_wage(C), R, "wage_rate", decrease, medium, invisible, "B") :- mc_wage(C), mc_recipient(C, R), not mc_floor_recipient(C, R).
mc_wage_moves(C) :- mc_wage(C), mc_recipient(C, R), not mc_floor_recipient(C, R).

% CR-7b: who bears the term's gross cost. Where the recipients' alternatives are worse than the providers' (alternatives_worse),
% the recipients bear the larger share as the wage adjusts.
mc_incidence(C) :- mc_wage(C), holds(alternatives_worse(C)), not exception(cr_7, C).
fired(cr_7, mc_incidence(C), mc_wage(C))             :- mc_incidence(C).
fired(cr_7, mc_incidence(C), alternatives_worse(C))  :- mc_incidence(C).
effect(mc_incidence(C), R, "tax_share_borne", increase, medium, invisible, "B") :- mc_incidence(C), mc_recipient(C, R), not mc_floor_recipient(C, R).

% PC-10 through a floor (existing, or set by the same measure): where the wage cannot fall (floor_binds), the cost stays with providers at every horizon
% and the other terms of the recipients at the floor adjust, at least one.
mc_floor(C) :- mc_binds(C), employment(C), mc_floor_recipient(C, _), holds(floor_binds(C)), not exception(pc_10, C).
fired(pc_10, mc_floor(C), mc_binds(C))      :- mc_floor(C).
fired(pc_10, mc_floor(C), floor_binds(C))   :- mc_floor(C).
group_effect(mc_floor(C), R, "employment,hours_worked,non_wage_compensation", at_least_one_decrease, short, invisible, "B") :- mc_floor(C), mc_floor_recipient(C, R).

% CR-7b, CR-7c: while the cost stays with providers, their returns and their means fall (CR-8b: the term is paid to the
% recipients); owners of businesses valued on expected earnings (valued_on_earnings) see the value fall when the mandate
% becomes expected.
mc_returns(C) :- mc_binds(C), employment(C), holds(wages_sticky(C)).
fired(cr_7, mc_returns(C), mc_binds(C))     :- mc_returns(C).
fired(cr_7, mc_returns(C), wages_sticky(C)) :- mc_returns(C).
effect(mc_returns(C), B, "return_on_capital", decrease, short, invisible, "B") :- mc_returns(C), bound(C, B).
effect(mc_returns(C), B, "resources_available_other_uses", decrease, short, invisible, "B") :- mc_returns(C), bound(C, B).
mc_capitalized(C) :- mc_returns(C), holds(valued_on_earnings(C)), not exception(cr_7, C).
fired(cr_7, mc_capitalized(C), mc_returns(C))           :- mc_capitalized(C).
fired(cr_7, mc_capitalized(C), valued_on_earnings(C))   :- mc_capitalized(C).
effect(mc_capitalized(C), B, "asset_value", decrease, short, invisible, "B") :- mc_capitalized(C), bound(C, B).

% CR-12: recipients' earnings. A paid absence that replaces an unpaid one (unpaid_absence_before) raises them; a lower wage
% lowers them. The group of C-4 is not a chain here: its benefits member does not move earnings (CR-12 1.1). Both chains are kept; where both are reported the sign is ambiguous (_resolve).
mc_earn_up(C) :- mc_binds(C), employment(C), paid_absence(C), holds(unpaid_absence_before(C)).
fired(cr_8, mc_earn_up(C), mc_binds(C))               :- mc_earn_up(C).
fired(cr_8, mc_earn_up(C), unpaid_absence_before(C))  :- mc_earn_up(C).
effect(mc_earn_up(C), R, "earnings", increase, short, invisible, "B") :- mc_earn_up(C), mc_recipient(C, R).
mc_earn_down(C) :- mc_wage_moves(C).
fired(cr_12, mc_earn_down(C), mc_wage(C)) :- mc_earn_down(C).
effect(mc_earn_down(C), R, "earnings", decrease, medium, invisible, "B") :- mc_earn_down(C), mc_recipient(C, R), not mc_floor_recipient(C, R).

% A paid absence (CR-3b, CR-4): absence is now cheaper than unpaid absence, so where some recipients use it (absence_used)
% hours present fall; where providers cover absent shifts (absences_covered), sellers of cover sell more.
mc_absence(C) :- mc_binds(C), employment(C), paid_absence(C), holds(absence_used(C)), not exception(cr_4, C).
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
mc_cap_shift(C) :- mc_binds(C), employment(C), per_head_cap(C), holds(hours_shift(C)), not exception(rs_18, C).
fired(rs_18, mc_cap_shift(C), per_head_cap(C)) :- mc_cap_shift(C).
fired(rs_18, mc_cap_shift(C), hours_shift(C))  :- mc_cap_shift(C).
group_effect(mc_cap_shift(C), R, "employment,hours_worked", at_least_one_decrease, medium, invisible, "B") :- mc_cap_shift(C), mc_below_cap(C, R).
effect(mc_cap_shift(C), R, "hours_worked", increase, medium, invisible, "B") :- mc_cap_shift(C), mc_above_cap(C, R).
mc_cap_cover(C) :- mc_cover(C), per_head_cap(C).
fired(rs_18, mc_cap_cover(C), mc_cover(C)) :- mc_cap_cover(C).
effect(mc_cap_cover(C), R, "hours_worked", increase, medium, invisible, "B") :- mc_cap_cover(C), mc_above_cap(C, R).
mc_cap_cost(C) :- mc_cost_after(C), employment(C), per_head_cap(C).
fired(cr_4, mc_cap_cost(C), mc_cost_after(C)) :- mc_cap_cost(C).
effect(mc_cap_cost(C), R, "hours_worked", decrease, medium, invisible, "B") :- mc_cap_cost(C), mc_above_cap(C, R).

% RS-23: the term's cost differs by recipient while its terms are uniform; where providers can tell (can_screen), they choose
% among applicants by non-price criteria.
mc_screen(C) :- mc_binds(C), employment(C), mc_applicant(C, _), holds(can_screen(C)), not exception(rs_23, C).
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
mc_pass(C) :- mc_cost_stays(C), employment(C), mc_output_buyer(C, _), holds(rivals_bound(C)), not exception(rs_14, C).
fired(rs_14, mc_pass(C), mc_cost_stays(C))  :- mc_pass(C).
fired(rs_14, mc_pass(C), rivals_bound(C))   :- mc_pass(C).
effect(mc_pass(C), X, "price_paid", increase, short, invisible, "B")       :- mc_pass(C), mc_output_buyer(C, X).
effect(mc_pass(C), X, "quantity_traded", decrease, short, invisible, "B")  :- mc_pass(C), mc_output_buyer(C, X).

% RS-4, RS-6: providers selling against unbound rivals across a boundary (rivals_unbound) lose output to them over time,
% where the cost stays after the wage adjusts (worth_less).
mc_relocate(C) :- mc_cost_after(C), mc_tradable(C, _), holds(rivals_unbound(C)), not exception(rs_4, C).
fired(rs_4, mc_relocate(C), mc_cost_after(C)) :- mc_relocate(C).
fired(rs_4, mc_relocate(C), rivals_unbound(C))   :- mc_relocate(C).
effect(mc_relocate(C), T, "quantity_supplied", decrease, long, invisible, "B") :- mc_relocate(C), mc_tradable(C, T).
effect(mc_relocate(C), N, "quantity_supplied", increase, medium, invisible, "B") :- mc_relocate(C), neighbor_seller(C, N).

% CR-9, CR-7c: unbound rivals of the providers (exempt or already offering the term) gain sales where they compete with them
% (compete_with_bound) and the cost stays after the wage adjusts; the expected gain is capitalized where firms are valued on
% expected earnings.
mc_rivals(C) :- mc_cost_after(C), mc_rival(C, _), holds(compete_with_bound(C)), not exception(cr_9, C).
fired(cr_9, mc_rivals(C), mc_cost_after(C))       :- mc_rivals(C).
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
mc_lockin(C) :- mc_binds(C), employment(C), forfeit_on_leaving(C), holds(move_marginal(C)), not exception(rs_11, C).
fired(rs_11, mc_lockin(C), forfeit_on_leaving(C)) :- mc_lockin(C).
fired(rs_11, mc_lockin(C), move_marginal(C))      :- mc_lockin(C).
effect(mc_lockin(C), R, "job_changes", decrease, medium, invisible, "B") :- mc_lockin(C), mc_term_holder(C, R).

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
mc_rule_binds(C) :- disclosure(C), holds(enforced(C)).
fired(rs_7, mc_rule_binds(C), binding(C))  :- mc_rule_binds(C), holds(binding(C)).
fired(rs_7, mc_rule_binds(C), enforced(C)) :- mc_rule_binds(C), disclosure(C).
mc_lobby(C) :- mc_rule_binds(C), holds(can_organize(C)), not exception(rs_7, C).
fired(rs_7, mc_lobby(C), mc_rule_binds(C)) :- mc_lobby(C).
fired(rs_7, mc_lobby(C), can_organize(C))  :- mc_lobby(C).
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
mc_rule(C) :- disclosure(C).
mc_administered(C) :- mc_rule(C), enforcer(C, _), not exception(oc_3, C).
fired(oc_3, mc_administered(C), mandate(C))  :- mc_administered(C), mandate(C).
fired(oc_3, mc_administered(C), standard(C)) :- mc_administered(C), standard(C).
fired(oc_3, mc_administered(C), term_ban(C)) :- mc_administered(C), term_ban(C).
fired(oc_3, mc_administered(C), disclosure(C)) :- mc_administered(C), disclosure(C).
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
% CR-7 (a means made mobile) with CR-6: where some holders were paid less than a rival would pay (paid_below_rivals), their
% pay rises as rivals can bid for them (found out of sample on WE-034, C-8).
tb_bid(C) :- tb_mobile(C), employment(C), holds(paid_below_rivals(C)).
fired(cr_7, tb_bid(C), tb_mobile(C))           :- tb_bid(C).
fired(cr_6, tb_bid(C), paid_below_rivals(C))   :- tb_bid(C).
effect(tb_bid(C), F, "wage_rate", increase, short, invisible, "B") :- tb_bid(C), tb_freed(C, F).
% CR-5c, CR-6: the party who valued the term offers less on the other terms of new contracts (wage, training it funds,
% hires), at least one, where it valued the term (term_valued). The group falls on the prospective counterparties
% (mc_applicant), not on holders of voided contracts, whose terms move the other way (found out of sample on WE-034, C-7, C-8).
% Shifts to substitute terms where they exist (substitute_terms).
tb_others(C) :- tb_binds(C), employment(C), mc_applicant(C, _), holds(term_valued(C)), not exception(pc_18, C).
fired(pc_18, tb_others(C), tb_binds(C))     :- tb_others(C).
fired(cr_6, tb_others(C), term_valued(C))   :- tb_others(C).
group_effect(tb_others(C), P, "wage_rate,non_wage_compensation,employment", at_least_one_decrease, medium, invisible, "B") :- tb_others(C), mc_applicant(C, P).
tb_substitute(C) :- tb_binds(C), holds(substitute_terms(C)), not exception(pc_18, C).
fired(pc_18, tb_substitute(C), substitute_terms(C)) :- tb_substitute(C).
effect(tb_substitute(C), B, "term_prevalence", increase, short, invisible, "B") :- tb_substitute(C), bound(C, B).
% CR-8 (voiding): where existing contracts are voided, the right voided passes from its holder to the other party.
tb_voided(C) :- tb_binds(C), voids_existing(C).
fired(cr_8, tb_voided(C), voids_existing(C)) :- tb_voided(C).
effect(tb_voided(C), B, "asset_value", decrease, short, invisible, "B") :- tb_voided(C), bound(C, B).
% CR-8b: both sides of the transfer (found out of sample on WE-034, C-38 and C-39).
effect(tb_voided(C), B, "resources_available_other_uses", decrease, short, invisible, "B") :- tb_voided(C), bound(C, B).
effect(tb_voided(C), F, "resources_available_other_uses", increase, short, invisible, "B") :- tb_voided(C), tb_freed(C, F).

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
effect(st_valued(C), O, "stock_age", decrease, long, invisible, "B")     :- st_valued(C), st_stock_owner(C, O).
% The same demand opposes "fewer new units built", with or without an exempt stock (found out of sample on WE-059, C-30).
st_drawn(C) :- st_binds(C), holds(buyers_value_standard(C)), not exception(en_14, C).
fired(en_14, st_drawn(C), buyers_value_standard(C)) :- st_drawn(C).
effect(st_drawn(C), B, "quantity_supplied", increase, medium, invisible, "B") :- st_drawn(C), bound(C, B).

% ------------------------------------------------------------------ PC-17 0.9: a mandate with a buy-out charge (play or pay)

% The bound class is split by response (CR-1 0.7): PC-17 applies to the firms that provide the term (bound, with their
% recipients); TX-2 to those that pay the charge to the state instead (some_pay). The charge is a wedge on the payers'
% labour: their cost per head rises, the quantity of labour they buy falls (employment or hours, at least one), and the
% state receives the charge (CR-8b). Above a cap per firm the charge no longer varies with heads (RS-18 0.9): a fixed cost,
% which lowers those payers' means but not their hiring. Found out of sample on WE-036.
mc_pays(C) :- mandate(C), mc_charge_payer(C, _), holds(binding(C)), holds(enforced(C)), holds(some_pay(C)), not exception(tx_2, C).
fired(pc_17, mc_pays(C), binding(C))  :- mc_pays(C).
fired(pc_17, mc_pays(C), enforced(C)) :- mc_pays(C).
fired(cr_4, mc_pays(C), some_pay(C))  :- mc_pays(C).
effect(mc_pays(C), P, "price_paid", increase, short, invisible, "B") :- mc_pays(C), employment(C), mc_charge_payer(C, P).
effect(mc_pays(C), P, "resources_available_other_uses", decrease, short, invisible, "B") :- mc_pays(C), mc_charge_payer(C, P).
effect(mc_pays(C), K, "resources_available_other_uses", decrease, short, invisible, "B") :- mc_pays(C), mc_charge_capped(C, K).
effect(mc_pays(C), R, "non_tax_receipts", increase, short, invisible, "B") :- mc_pays(C), mc_charge_receiver(C, R).
mc_pay_wedge(C) :- mc_pays(C), employment(C), mc_charge_payer_worker(C, _).
fired(tx_2, mc_pay_wedge(C), mc_pays(C)) :- mc_pay_wedge(C).
group_effect(mc_pay_wedge(C), W, "employment,hours_worked", at_least_one_decrease, medium, invisible, "B") :- mc_pay_wedge(C), mc_charge_payer_worker(C, W).

% ------------------------------------------------------------------ Inputs the measure requires (CR-9)

% A standard or mandate that requires an input per unit (ratings, efficient windows, certified plans) raises the demand for
% it where the measure binds: its sellers sell more. relations.lp's derived demand (fewer units, less input) does not apply
% to it (found out of sample on WE-031). Where its supply is slow (related_slow_rN), its price rises and its other users pay
% more and use less (SB-3, CR-7a).
mc_measure_binds(C) :- st_binds(C).
mc_measure_binds(C) :- mc_binds(C).
fired(cr_9, mc_measure_binds(C), st_binds(C)) :- mc_measure_binds(C), st_binds(C).
fired(cr_9, mc_measure_binds(C), mc_binds(C)) :- mc_measure_binds(C), mc_binds(C).
rel_required(C, R) :- mc_measure_binds(C), related(C, R, required, _, _, _), not exception(cr_9, C).
fired(cr_9, rel_required(C, R), mc_measure_binds(C)) :- rel_required(C, R).
effect(rel_required(C, R), S, "quantity_traded", increase, short, invisible, "B") :- rel_required(C, R), related(C, R, required, S, _, _).
rel_required_scarce(C, R) :- rel_required(C, R), rel_premise(C, R, slow, A), holds(A).
fired(sb_3, rel_required_scarce(C, R), rel_required(C, R)) :- rel_required_scarce(C, R).
fired(cr_7, rel_required_scarce(C, R), A) :- rel_required_scarce(C, R), rel_premise(C, R, slow, A).
effect(rel_required_scarce(C, R), S, V, increase, short, invisible, "B") :- rel_required_scarce(C, R), related(C, R, required, S, V, _).
effect(rel_required_scarce(C, R), O, "price_paid", increase, short, invisible, "B") :- rel_required_scarce(C, R), related(C, R, required, _, _, O), O != "".
effect(rel_required_scarce(C, R), O, "quantity_traded", decrease, short, invisible, "B") :- rel_required_scarce(C, R), related(C, R, required, _, _, O), O != "".

% ------------------------------------------------------------------ EN-15: a disclosure mandate

% Covered sellers who comply (enforced) bear the cost of disclosing (CR-4 0.8). Buyers' choices change only where they did
% not already know and care (buyers_unaware, CR-11 0.7), and the direction is a premise of its own: fewer purchases where the
% disclosed fact deters (disclosed_deters), more where it attracts (disclosed_attracts); both reported gives ambiguous.
% Exempt sellers whose goods compare well disclose voluntarily (exempt_compare_well, CR-11 0.9).
ds_binds(C) :- disclosure(C), holds(enforced(C)), not exception(en_15, C).
fired(en_15, ds_binds(C), enforced(C)) :- ds_binds(C).
effect(ds_binds(C), B, "compliance_cost", increase, short, invisible, "B") :- ds_binds(C), bound(C, B).
ds_informs(C) :- ds_binds(C), holds(buyers_unaware(C)).
fired(cr_11, ds_informs(C), buyers_unaware(C)) :- ds_informs(C).
ds_less(C) :- ds_informs(C), holds(disclosed_deters(C)).
fired(en_15, ds_less(C), disclosed_deters(C)) :- ds_less(C).
effect(ds_less(C), X, "quantity_demanded", decrease, short, invisible, "B") :- ds_less(C), st_buyer(C, X).
ds_more(C) :- ds_informs(C), holds(disclosed_attracts(C)).
fired(en_15, ds_more(C), disclosed_attracts(C)) :- ds_more(C).
effect(ds_more(C), X, "quantity_demanded", increase, short, invisible, "B") :- ds_more(C), st_buyer(C, X).
ds_voluntary(C) :- ds_binds(C), mc_rival(C, _), holds(exempt_compare_well(C)), not exception(en_15, C).
fired(cr_11, ds_voluntary(C), exempt_compare_well(C)) :- ds_voluntary(C).
effect(ds_voluntary(C), V, "term_prevalence", increase, short, invisible, "B") :- ds_voluntary(C), mc_rival(C, V).

% ------------------------------------------------------------------ RS-24: a fixed cost per item

% Where the measure attaches a cost fixed per item, model or version (testing, labeling, parts per model) and some items
% sell in small numbers (small_items), sellers drop them: variety falls.
mc_items(C) :- mc_rule_binds(C), fixed_cost_per_item(C), holds(small_items(C)), not exception(rs_24, C).
fired(rs_24, mc_items(C), mc_rule_binds(C)) :- mc_items(C).
fired(rs_24, mc_items(C), small_items(C))   :- mc_items(C).
effect(mc_items(C), B, "variety", decrease, medium, invisible, "B") :- mc_items(C), bound(C, B).

#show holds/1.
#show fired/3.
#show effect/7.
#show group_effect/7.
#show window/2.
#show item/2.
