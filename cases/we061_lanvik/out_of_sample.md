# Out-of-sample run of the mandate rules on WE-061 (Lanvik App-Based Work Act 2027)

Rules as they were at commit 96d60b0 (`praxeo/rules/mandates.lp`: PC-17 developed on WE-029, PC-18 and EN-14 written from the catalog). Nothing under `praxeo/` was changed. Record: `record.json`, three components. K1 is the `mandated_contract_term` (the employee presumption, section 3): bound `platforms`, recipient, floor-held and applicant role all `drivers.employee`, output buyer `riders`, rivals `sellers.small_platform` and `sellers.substitutes` (taxis), outside actor `drivers.contractor`, `definition_line`, `size_threshold` with `below_threshold_actor` `sellers.small_platform`, enforcer `officials.enforcement`, `general_budget` (payer group left at the default of taxpayers, recipients of other spending and future taxpayers, which is the example's group). K2 (the floor on engaged time, `price_floor`) and K5 (the buy-out, `mandate_with_charge`) are recorded but no rule reads them. K3 (overtime) and K4 (contributions) are not recorded: K3 would be a second mandated term with the same roles as K1 and repeat its rows, and K4 is a `per_unit_tax` on wages, which belongs to the tax rules, not to the rules under test. K6 (enforcement) is folded into K1's `enforcer_actor` and `general_budget`. No `tradable_actor` and no `complaint_only`: the example's Selvane mechanism is workers moving hours, there is no named rival provider across the river, and it says RS-20 does not apply because enforcement is by audit as well as by complaint. U1 (does waiting time count as engaged time) changes no Component field, so it has two readings and no `reading_fields`. Answers: `answers.json`, 15 questions, all on k1. Probabilities come from the assumption table of WE-061 where a row matches (enforced A-1, wages_sticky A-29, wages_adjust A-28, valued_on_earnings A-11, can_organize and recipients_organize A-16, floor_binds A-3, can_screen A-31, rivals_bound A-4 loosely, compete_with_bound A-10, reshaping_pays A-8, staying_small_pays A-15); `binding`, `worth_less` and `alternatives_worse` have no matching row and were judged from the text. Run: `python3 -m praxeo cases/we061_lanvik --out cases/we061_lanvik/sample_run` (verifier and citation problems empty). Key: (actor class, variable, sign, window); the table's "lobbying groups" (C-22) is matched to `platforms` and `drivers.employee`, and its payer group (C-37) to the record's three payer roles. Sign cells given per reading of U1 are collapsed where both readings agree; the rows where they differ (C-24, C-40, C-41) are not produced.

Summary: the table has 43 rows (C-1 to C-45, without C-32 and C-39). The engine reports 23 consequences (of 24 derived; the incidence row `tax_share_borne` is below the cut-off), which give 27 keys (the recipients' group over three variables and the OC-1 group over three actor classes give one key per member). Table rows produced by key: 13 (C-3, C-5, C-6, C-7, C-8, C-9, C-11, C-15, C-16, C-21, C-22, C-36, C-37); C-7 for the riders only and C-16 for the contractors only. Rows not produced: 30. Engine rows classified WRONG: 2.

## Engine rows (reported)

| Engine row | Class | Why |
|---|---|---|
| drivers.employee non_wage_compensation increase | in table | C-3 (PC-17, CR-1) |
| platforms compliance_cost increase | in table | C-5 (OC-2, Tier A) |
| riders price_paid increase; riders quantity_traded decrease | in table | C-6, C-7 (RS-14 with CR-4c); employees and contractors not signed on trips |
| drivers.employee employment, hours_worked, non_wage_compensation at_least_one_decrease | in table | C-8 (PC-10 through the floor); the table's group has a fourth member, wage_rate above the floor |
| drivers.employee allocation_by_non_price_criteria increase | in table | C-9 (RS-23 as the rule has it, PC-11 in the example) |
| platforms price_paid increase | in table | C-11 (the cost stays with the platforms while fare shares hold) |
| platforms reclassification increase | in table | C-15 (RS-5) |
| drivers.contractor reclassification increase | in table | C-16 (RS-5; the table has the employees too) |
| sellers.small_platform number_of_sellers increase | in table | C-21 (RS-17 notch at 100 workers) |
| platforms lobbying_effort increase; drivers.employee lobbying_effort increase | in table | C-22 (RS-7) |
| officials.enforcement enforcement_cost increase | in table | C-36 (OC-3) |
| taxpayers, recipients.other_spending, taxpayers.future resources_available_other_uses at_least_one_decrease | in table | C-37 (OC-1 group) |
| platforms asset_value decrease | defensible | CR-7c on the bound actor; the table puts the fall on `owners.platforms` (C-27) |
| platforms return_on_capital decrease | defensible | CR-7b; C-27 rests on the same fall in expected yield |
| platforms resources_available_other_uses decrease | defensible | CR-8b. The final check (item 4) signs this variable only for riders whose trips do not fall (C-38), but does not say the platforms' means do not fall |
| sellers.small_platform quantity_supplied increase | defensible | CR-9, exempt rivals gain sales; the table has their number rise (C-21), not their sales |
| sellers.small_platform asset_value increase | defensible | CR-7c on the exempt rivals; not in the table, not contradicted |
| sellers.substitutes quantity_supplied increase | defensible | CR-9 for taxis; the table has the same gain as `quantity_substitute` (C-25, RS-1) |
| sellers.substitutes asset_value increase | defensible | CR-7c; the table puts the gain on the medallion owners (C-26) |
| **drivers.employee wage_rate decrease** | **WRONG** | PC-17 with CR-6 (`wages_adjust`) lowers the wage of all employees. The example has the section 5 floor hold the pay of workers below 16 (C-1: increase) and puts only the pay above the floor among the margins that give, as one member of a group (C-8). A plain decrease for the class contradicts C-1 |
| **drivers.employee earnings decrease** | **WRONG** | Fewer jobs and hours and a lower wage are reported as the only chain. The example has the floor (C-1) as the opposing chain and signs earnings `ambiguous` (C-33). The engine's opposing chain exists only for a paid absence |

## Table rows

| Row | Produced? | Reason |
|---|---|---|
| C-1 employee wage_rate increase | no | missing rule: the floor's direct effect on workers below it (PC-10). K2 is a `price_floor`, which has no rules; the engine signs `wage_rate` the other way |
| C-2 contractor net_price_received (premium) increase | no | unsupported form: K5 is a `mandate_with_charge`, which has no rules |
| C-3 employee non_wage_compensation increase | yes | |
| C-4 state_insurance_fund tax_revenue increase | no | missing record fact: K4 not recorded (tax family) |
| C-5 platforms compliance_cost increase | yes | |
| C-6 riders price_paid increase | yes | |
| C-7 riders, employee, contractor quantity_traded decrease | yes (part) | riders only |
| C-8 employee hours, employment, non_wage, wage_rate at_least_one_decrease | yes | three of four members |
| C-9 employee allocation_by_non_price_criteria increase | yes | |
| C-10 low_fare term_prevalence increase | no | missing rule: RS-23's selection into the term by workers; the rule signs only the provider's choice among applicants |
| C-11 platforms price_paid increase | yes | |
| C-12 contractor net_price_received (fare share) decrease | no | unsupported form: K5, a premium added to a free term undone through that term (CR-6 0.8) |
| C-13 contractor net_price_received (total) increase | no | unsupported form: K5, two items of one variable (CR-12 0.8) |
| C-14 contractor net_price_received (total) ambiguous | no | unsupported form: K5 |
| C-15 platforms reclassification increase | yes | |
| C-16 contractor, employee reclassification increase | yes (part) | contractors only (the outside role); the employees are the recipients, which RS-5 does not sign |
| C-17 platforms, employee legal_breach increase | no | missing rule: RS-3 is not in the mandate rules; RS-20's breach chain needs `complaint_only`, and enforcement here is by audit as well |
| C-18 employee hours_worked just below 40 increase | no | unsupported form: RS-17 is encoded for a size threshold only, not a kink in hours; K3 not recorded |
| C-19 employee reclassification (hours split) increase | no | unsupported form: same |
| C-20 part-time employee hours_worked at 150 increase | no | unsupported form: a notch in weekly wages (K4) |
| C-21 small_platform number_of_sellers increase | yes | |
| C-22 lobbying groups lobbying_effort increase | yes | |
| C-23 neighboring_jurisdictions quantity_supplied ambiguous | no | missing record fact: RS-4 here needs providers selling against unbound rivals across the boundary; the example moves workers' hours (CR-7a) and names no rival provider |
| C-24 riders wait_time (U1-a decrease; U1-b ambiguous) | no | combiner and missing rule: CR-12e's response argument; the sign differs by reading |
| C-25 taxis quantity_substitute increase | no | missing rule: RS-1; the engine's CR-9 gain is `quantity_supplied` |
| C-26 owners.medallions asset_value increase | no | role: CR-7c signs the rivals' own value; no owners role for rivals |
| C-27 owners.platforms asset_value decrease | no | role: the rule signs the bound actor (platforms), not its owners |
| C-28 restaurants quantity_traded decrease | no | missing rule: RS-12 (complement) |
| C-29 in-house couriers employment, hours at_least_one_increase | no | missing rule: RS-1 with CR-6 labor demand |
| C-30 state_insurance_fund subsidy_outlay increase | no | missing record fact: K4's fund; CR-8b |
| C-31 state_insurance_fund fund_balance ambiguous | no | combiner: contributions against benefits; no K4 |
| C-33 employee earnings ambiguous | no | combiner: the engine reports one chain, as decrease (a WRONG row) |
| C-34 contractor wait_time ambiguous | no | combiner and missing rule: CR-12e second chains; K5 |
| C-35 contractor wage_rate (per logged-in hour) ambiguous | no | combiner and missing rule: same |
| C-36 officials.enforcement enforcement_cost increase | yes | |
| C-37 taxpayers, other spending, future taxpayers resources_available_other_uses at_least_one_decrease | yes | |
| C-38 riders (trips not falling) resources_available_other_uses decrease | no | missing rule: OC-1 for the buyers who keep paying a higher price (CR-3's note) |
| C-40 employee hours_worked (paid waiting) (U1-a no_change; U1-b decrease) | no | missing rule, and the reading: U1 changes no field, so the engine cannot tell the readings apart |
| C-41 employee non_wage_compensation total (U1-a increase; U1-b ambiguous) | no | combiner: cover (+) against flexibility (-) as two items (CR-12 0.8); only the cover is signed |
| C-42 contractor term_prevalence increase | no | unsupported form: K5 |
| C-43 prospective entry_rate ambiguous | no | missing rule: no rule signs entry |
| C-44 riders home_production increase | no | missing rule: RS-1 |
| C-45 owners.medallions right_lease_price increase | no | missing rule: CR-6 for the price of a legal right |

## Patterns for the rule writer

1. **A floor that comes with the mandate (PC-10 inside PC-17).** The mandate rule derives the recipients' wage decrease (`mc_wage`, `wages_adjust`) and the earnings decrease (`mc_earn_down`) with no condition on a floor, and the floor group (`mc_floor`) is derived beside them. Where the same Act sets a floor under the recipients (section 5), the example signs the wage of those below the floor as an increase (C-1), puts the give on the other margins as a group (C-8), and has the floor as the opposing chain for earnings (C-33, ambiguous). The engine contradicts it twice (two WRONG rows) and cannot produce C-1 or C-33. The question `floor_binds` and the field `floor_bound_actor` are worded for an existing floor, which the example does not have (the old minimum wage does not reach these workers); the floor is K2, a `price_floor` that no rule reads. A general fix: a wage-down chain should exclude recipients held by a floor, and a floor on the pay for the mandated term should itself raise the pay per hour for those below it and oppose the earnings-down chain. Rows: C-1, C-33, engine wage_rate and earnings.
2. **A second term in the same mandate, paid to the counterparty (`mandate_with_charge`, the buy-out).** K5 has no rules. The premium, the fare share it is added to, the total per trip, the contractors' term prevalence, waits and hourly earnings all hang on it. The pattern has two parts: a mandated add-on to a price the payer still sets is undone through that price once it can move (CR-6 0.8), and the two items of one variable are recorded and combined per horizon (CR-12 0.8). Rows: C-2, C-12, C-13, C-14, C-34, C-35, C-42. This is the largest cluster (seven rows).
3. **Companion instruments recorded but unread.** `price_floor` and `mandate_with_charge` have no rules, and a wage tax with a notch (K4) belongs to the tax family. Hours lines (a kink at 40 hours, a notch in weekly wages) are not in RS-17, which the mandate rules encode for a size threshold only. Rows: C-4, C-18, C-19, C-20, C-30, C-31.
4. **Selection into the term by recipients.** RS-23 is encoded as the provider's choice among applicants (`can_screen`, `allocation_by_non_price_criteria`). The example's use is the opposite side: recipients with different costs choose between the uniform term and an alternative, so some classes take it (`term_prevalence`, C-10, C-42). Rows: C-10, C-42.
5. **Owners of the bound and of rivals.** CR-7c puts the bound providers' fall (and the rivals' rise) on the providers themselves; the example puts it on their owners and on holders of a fixed right (shareholders, medallion owners). A record has no owners role for the bound actor or for rivals, so the same sign lands on a different class. Rows: C-26, C-27 (and the three defensible `asset_value` rows).
6. **RS-4 as workers' mobility.** The mandate rules encode RS-4 for providers selling against unbound rivals across a boundary and sign output moving. The example uses it for labor supply moving to trips on the other side (CR-7a) and signs it `ambiguous`, because the premium and the higher fares oppose. The rules have no ambiguous output of their own and no role for mobile workers. Row: C-23.
7. **Neighbouring markets of a mandate.** Riders leaving the apps (taxi trips, home cooking, restaurants' own couriers, delivery orders, the taxi lease price) are RS-1, RS-12, LW-10 and CR-6 on a right's price; the mandate rules reach only the rivals' `quantity_supplied`, which is the same event under another variable name. Rows: C-25, C-28, C-29, C-44, C-45.
8. **Breach under audit enforcement.** RS-3 breach (workers treated as contractors without a valid agreement, unpaid engaged time) has no route in the mandate rules. RS-20's breach chain is gated on `complaint_only`, and a mandate enforced by audit as well as by complaint has no equivalent that rests on imperfect enforcement alone (A-19). Row: C-17.
9. **A reading that changes no record field.** U1 says whether waiting time counts as engaged time. It changes the hours the floor binds on and the margins the company uses, but no Component field, so the engine runs once and cannot give a sign per reading; the rows signed per reading (C-24, C-40, C-41) are not produced. A field such as "the floor covers time between jobs" would let a reading carry it. Rows: C-24, C-40, C-41.
10. **One-sided combiners and "who keeps paying".** Where two chains are signed in opposite directions for one variable (earnings, total non-wage terms, the insurance fund's balance, hourly earnings), the engine reports a sign only when a single chain is derived, which is how the WRONG earnings row arises. The mandate rules also sign the providers' means (`resources_available_other_uses`, `return_on_capital`) but not the means of the buyers who keep paying the higher price (CR-3's note, C-38), while the example signs it for those buyers only. Rows: C-31, C-33, C-35, C-38, C-41, and the platforms' `resources_available_other_uses` row.


## After the rule changes

General fixes from the out-of-sample runs on WE-031, WE-034, WE-036, WE-059 and WE-061 (`rules/mandates.lp`): a contract-kind field (`contract_kind`: employment or sale), so the wage, hours, jobs and earnings chains apply only to employment contracts (PC-17 1.1); later chains (unbound rivals, relocation, the cost above a per-head cap, earnings) rest on their own premise, never on a group conclusion (CR-12 1.1); no wage-down or earnings-down chain for recipients a floor holds, whether the floor exists or the measure sets it; a term ban's adjusting group falls on the prospective counterparties of new contracts (`applicant_actor`), the holders of voided contracts are bid up where they were paid below rivals (`paid_below_rivals`), and voiding is recorded on both sides (CR-8b); EN-14's Unless clause also opposes the stock's age and the fall in new units, and its question is asked of every standard. The record and answers are unchanged (the recipients are the floor-held class already). Rows produced: 13 of 43 (unchanged). WRONG: 0 (was 2): the drivers' wage-down and earnings-down rows are gone.


## After the second round of rule changes

Second round of general fixes (`rules/mandates.lp`): play or pay (PC-17 0.9: firms that pay the charge face TX-2 on their labour, the state receives the charge, payers above a cap per firm bear a fixed cost, and the term itself and lock-in go to the recipients at firms that provide it, `player_recipient_actor`); inputs a standard or mandate requires (`related` kind `required`: more demand, and with slow supply a higher price for them and their other users); EN-15 for `disclosure_mandate` (compliance cost; buyers' choices on two premises, ignorance and direction; voluntary disclosure by exempt sellers); RS-24 (`fixed_cost_per_item`). K5 (`mandate_with_charge`, a premium paid to the worker, not a charge to the state) names no recipient or payer, so only OC-2, OC-3 and RS-7 apply; its three answers come from A-2 and A-16 or the text. Rows produced: 13 of 43 (unchanged). WRONG: 0.
