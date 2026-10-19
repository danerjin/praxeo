# Out-of-sample run of the mandate rules on WE-031 (Westmere Residential Energy Performance Act)

Rules as they were at commit 96d60b0 (`rules/mandates.lp`: PC-17 developed on WE-029; PC-18 and EN-14 written from the catalog alone). Nothing under `praxeo/` was changed. This case tests EN-14, the product standard with the stock exempt. Record: `record.json`, one `product_standard` component (K1: bound `builders`, buyers `buyers.new_homes`, `stock_exempt` with owners `owners.existing_homes`, `definition_line` with `outside_actor` `homeowners.renovating`, `announcement_window`, `general_budget`, payers `taxpayers.current`, `taxpayers.future` and the default `recipients.other_spending`, enforcer `officials.enforcement`). K3 (verification and enforcement) is folded into K1's `enforcer_actor` and `general_budget`. K2 (vesting, a timing rule) and the existing rebate are not components: the ontology has no instrument for a timing rule, and the rebate is an existing rule the Act moves, not a provision of the Act. U1 (size adjustment) and U2 (which code the rebate means) change no Component field, so they have two readings each and no `reading_fields`; the engine gives the same result under each. No related markets are recorded: the policy text (section 1) names raters but not the suppliers of efficiency products or other inputs, and raters are a required service, not a derived-demand input (see pattern 2). Answers: `answers.json`, five questions. Four take their probability from WE-031's assumption table (`binding` A-4 0.7, `enforced` A-2 0.9, `can_organize` A-17 0.9, `stock_competes` A-7 0.8); `buyers_value_standard` has no matching row and was judged from the text (no, 0.3). Run: `python3 -m praxeo cases/we031_westmere --out cases/we031_westmere/sample_run` (verifier and citation problems empty). Key: (actor class, variable, sign, window); no table actor needed renaming.

Summary: the table has 47 rows (C-1 to C-47). The engine reports 9 consequences (all that it derives; none is below the cut-off), which give 11 keys (the OC-1 entry is a group of three actor classes). Table rows produced by key: 7 (C-1, C-3, C-4, C-5, C-18, C-21, C-30). Rows not produced: 40. Engine rows classified WRONG: 0 by key. One row, `buyers.new_homes price_paid increase`, is in the table as C-4 (medium to long) but the engine gives it over short to long, and C-35 says the price is ambiguous in Years 1 to 3; its short horizon is contradicted (pattern 5).

## Engine rows (reported)

| Engine row | Class | Why |
|---|---|---|
| builders compliance_cost increase | in table | C-1 (OC-2, CR-8c) |
| officials.enforcement enforcement_cost increase | in table | C-3 (OC-3) |
| buyers.new_homes price_paid increase | in table, horizon too wide | C-4 (EN-14, CR-1). The engine gives short to long; C-4 is medium to long and C-35 is ambiguous in Years 1 to 3 |
| builders quantity_supplied decrease | in table | C-5 (EN-14, CR-4c). Engine horizon medium to long, as C-5 |
| builders lobbying_effort increase | in table | C-18 (RS-7) |
| owners.existing_homes asset_value increase | in table | C-21 (CR-7c). The engine starts at medium; C-21 is short to long, from the enactment (CR-10c) |
| taxpayers.current, recipients.other_spending, taxpayers.future resources_available_other_uses at_least_one_decrease | in table | C-30 (OC-3, OC-1, CR-8b), the same group |
| buyers.new_homes specification_level increase | defensible | EN-14 puts specification_level on the buyers of the new units; the table has it on the builders (C-2). Section 4 says it records the mandated specification of the homes |
| owners.existing_homes stock_age increase | defensible | Section 5 says the existing stock is kept in use longer; the example folds it into C-5 and C-11 for want of a variable (Gaps found, item 4) |

## Table rows

| Row | Produced? | Reason |
|---|---|---|
| C-1 builders compliance_cost increase | yes | |
| C-2 builders specification_level increase | no | role: EN-14 signs it on the buyers (the engine's row is above) |
| C-3 officials.enforcement enforcement_cost increase | yes | |
| C-4 buyers.new_homes price_paid increase | yes | |
| C-5 builders quantity_supplied decrease | yes | |
| C-6 builders.small number_of_sellers decrease | no | missing rule and record fact: lumpy fixed costs per plan (CR-4); no small-builders role, no question for A-8 |
| C-7 builders quantity_traded increase (permits before each step) | no | missing rule and record fact: RS-8 with a dated schedule of steps; no field for the steps |
| C-8 builders quantity_traded decrease (permits after each step) | no | missing rule: as C-7 |
| C-9 applicants.permits wait_time increase | no | missing rule and role: OC-3 with fixed review staff (A-10) |
| C-10 homeowners.renovating reclassification increase | no | missing rule: RS-5 is encoded for a mandated term only; `definition_line` and `outside_actor` are recorded but EN-14 does not read them |
| C-11 homeowners.renovating quantity_substitute increase | no | missing rule: RS-1 and RS-16 for the exempt substitutes |
| C-12 buyers.new_homes unit_size (U1-a increase; U1-b decrease) | no | missing rule and record fact: CR-4c on size under a per-square-foot index; U1 changes no Component field |
| C-13 buyers.new_homes, sellers.substitutes at_least_one_increase | no | missing record fact and rule: exempt new substitutes (manufactured homes) have no role |
| C-14 neighboring_jurisdictions quantity_supplied increase | no | missing rule: RS-4 is not in EN-14 |
| C-15 builders price_paid (ratings) increase | no | missing rule, role: raters, rating capacity (CR-6, CR-9) |
| C-16 raters entry_rate increase | no | missing rule, role |
| C-17 builders, raters legal_breach increase | no | missing rule, role: RS-3 for false certification |
| C-18 builders lobbying_effort increase | yes | |
| C-19 input_suppliers.efficiency lobbying_effort increase | no | role: RS-7 has no beneficiary role for a standard |
| C-20 builders net_price_received increase (rebates, Years 1 to 3) | no | unsupported form: an existing rule moved by the Act |
| C-21 owners.existing_homes asset_value increase | yes | |
| C-22 buyers.existing_homes price_substitute increase | no | missing rule, role: RS-16 on the price of the stock to its buyers |
| C-23 owners.buildable_lots asset_value decrease | no | missing rule, role: CR-7b, CR-7c for the factor specific to new units |
| C-24 input_suppliers.efficiency quantity_demanded increase | no | missing rule, role; derived demand through `target_qty` gives the opposite sign (pattern 2) |
| C-25 input_suppliers.other quantity_demanded (U1-a ambiguous; U1-b decrease) | no | missing record fact: not named in the policy text; relations.lp writes `quantity_traded`; signs depend on U1 |
| C-26 workers.residential_construction employment, hours_worked ambiguous | no | combiner and missing rule |
| C-27 renters price_paid increase | no | missing rule, role: RS-16 and CR-9 to rents |
| C-28 buyers.new_homes resources_available_other_uses ambiguous | no | combiner: DM-3, price against lower energy spending (A-24) |
| C-29 buyers.new_homes, builders quantity_traded decrease (homes below the standard) | no | missing rule: OC-4, CR-5a for prevented exchanges under a standard |
| C-30 taxpayers.current, taxpayers.future, recipients.other_spending at_least_one_decrease | yes | |
| C-31 officials.enforcement enforcement_cost decrease (other inspection work) | no | missing rule: OC-3's fixed-budget case (CR-8a) |
| C-32 builders net_price_received decrease (rebates, Years 4 to 10) | no | unsupported form: as C-20 |
| C-33 builders quantity_traded (late Year 0; U2-a ambiguous, U2-b increase) | no | unsupported form: RS-8 around the first step, per reading of a rebate rule |
| C-34 builders quantity_traded (early Year 1; U2-a ambiguous, U2-b decrease) | no | unsupported form: as C-33 |
| C-35 buyers.new_homes price_paid ambiguous (Years 1 to 3) | no | combiner and unsupported form: compliance chain against the looser rebate; the engine gives increase |
| C-36 builders quantity_supplied ambiguous (Years 1 to 3) | no | combiner and unsupported form: as C-35 |
| C-37 raters quantity_traded increase | no | missing rule, role; derived demand through `target_qty` gives the opposite sign (pattern 2) |
| C-38 raters asset_value increase | no | missing rule, role: CR-7c, CR-10c |
| C-39 builders.small variety decrease | no | missing rule, role |
| C-40 owners.buildable_lots tax_share_borne increase | no | missing rule, role: CR-7b pair |
| C-41 input_suppliers.efficiency asset_value increase | no | missing rule, role |
| C-42 buyers.home_energy_audits price_paid increase | no | missing rule, role: CR-6, CR-9 |
| C-43 utilities.rebate_program subsidy_outlay increase (Years 1 to 3) | no | unsupported form: the existing rebate under a moved threshold |
| C-44 utilities.rebate_program subsidy_outlay decrease (Years 4 to 10) | no | unsupported form: as C-43 |
| C-45 ratepayers, recipients.other_efficiency_programs at_least_one_decrease (Years 1 to 3) | no | unsupported form and role: the rebate budget's other side |
| C-46 ratepayers, recipients.other_efficiency_programs at_least_one_increase (Years 4 to 10) | no | unsupported form and role: as C-45 |
| C-47 buyers.commercial_construction price_paid (-), quantity_traded (+) | no | missing rule and sign form: RS-6; a mixed group no sign encodes |

No row is "below cut-off": the engine reports all 9 consequences it derives, so the 40 rows are missing for other reasons.

An experiment kept out of the committed run: with raters (`energy_ratings`) and the makers of efficiency products recorded as `related` inputs of K1, relations.lp derives `raters quantity_traded decrease` and `input_suppliers.efficiency quantity_traded decrease` (and a lower `net_price_received` for both, with the `slow` premise answered yes). C-37 and C-24 say increase. So recording them would have added WRONG rows. The scratch files were deleted.

## Patterns for the rule writer

1. **Existing rule moved by the measure (C-20, C-32, C-43, C-44, C-45, C-46, C-35, C-36, C-33, C-34; the opposing half of C-4 and C-5 in Years 1 to 3).** The Act changes the threshold of an existing rebate. The record has no way to say this, and no rule reads it. The effect is that the engine states the compliance chain alone for the short run (price up from Year 1, C-4's `short` horizon), where the example finds it ambiguous. A general pattern is needed for a measure that changes the terms of an existing subsidy, tax or standard: a record field naming the linked rule and its direction by window, and a combiner for the two chains. About 10 rows.
2. **Inputs the standard requires per unit versus derived demand (C-24, C-37, C-15, C-42, C-38, C-41, C-19).** EN-14 sets `target_qty(C, decrease)`, which makes CR-9 give every related input a lower `quantity_traded`. For a service or product the standard itself requires on every unit (ratings, insulation, heat pumps), demand rises per unit and the sign is the opposite. The experiment above shows two WRONG rows would follow from recording them. A third kind of relation is needed besides `input` and `complement`, such as `required`: its sellers sell more, their asset values rise (CR-7c, CR-10c), and they are the beneficiaries who lobby (RS-7, C-19). About 7 rows.
3. **Roles EN-14 does not read (C-10, C-11, C-13, C-14, C-22, C-23, C-27, C-40, C-47).** `_mandate_facts` emits `definition_line`, `outside_actor`, `neighbor_seller` and `mc_tradable` for any mandate, but the rules that read them (RS-5, RS-4, RS-6) require a mandated term. A standard has the same structure: exempt substitutes (renovation, manufactured homes, homes across the line), buyers of the exempt stock, and owners of the factor specific to new units. EN-14 needs the matching chains and roles. About 9 rows.
4. **Dated schedule of steps and vesting (C-7, C-8, C-33, C-34).** `announcement_window` is set but a standard does not read it. A schedule that tightens on known dates, with a filing date that fixes the standard (RS-8), needs a record field for the dated steps. U2 is a reading about another rule, which `reading_fields` cannot express (it names Component fields only). 4 rows.
5. **One `binding` question for two premises, and the horizon (C-4, C-5, C-35, C-36, C-21, C-38, C-41).** A-4 ("binds on some designs now", 0.7) and A-1 ("binds on a material share from Year 4", 0.8) are different premises. EN-14 asks the first and attaches `short` to the price rise. The example puts the price and quantity effects at medium to long (they need A-1 and A-5) and signs Years 1 to 3 ambiguous. EN-14 also starts the stock owners' gain at `medium`, where the example starts it at the enactment on the expectation that the schedule will be carried out (A-20, CR-10c). A growing binding (TS-3) needs a second question, and the expectation effects need a `short` horizon from the enactment. Rows affected: C-4, C-5, C-21, C-35, C-36 (and C-38, C-41 if produced).
6. **Verification and enforcement chains of a standard (C-9, C-29, C-31, C-17, C-6).** OC-4 (prevented exchanges of homes below the standard), OC-3's fixed-budget case (waiting and displaced other inspections), RS-3 for false certification, and fixed per-plan compliance costs for small makers are not derived from EN-14. EN-14 gives OC-2 and OC-3 (Tier A) correctly; the rest of the enforcement side is missing. 5 rows.
7. **Readings that change a measure, not a Component field (C-12, C-25, C-33, C-34).** U1 changes how the index is measured and U2 what another rule means. Neither can be written as `reading_fields`, so a reading-dependent row cannot be produced however the rules are extended. A schema field for the measure's form (for example `size_adjusted`) would be needed. 4 rows.
8. **Combiners and group forms (C-26, C-28, C-35, C-36, C-45, C-46, C-47).** Two chains for one variable (labor, buyers' means, Years 1 to 3 price) have no declared comparison, and the mixed group of C-47 (price -, quantity +) has no sign. 7 rows, most of them dependent on patterns 1 and 3.
9. **What worked.** EN-14 produced 7 table rows (compliance cost, price, quantity, lobbying, stock value, enforcement and its OC-1 payers) with no WRONG row; the stock gain and the price and quantity chains did not need the buyers-value premise, and `buyers_value_standard` at 0.3 kept the opposing chain out, as the example has it.


## After the rule changes

General fixes from the out-of-sample runs on WE-031, WE-034, WE-036, WE-059 and WE-061 (`rules/mandates.lp`): a contract-kind field (`contract_kind`: employment or sale), so the wage, hours, jobs and earnings chains apply only to employment contracts (PC-17 1.1); later chains (unbound rivals, relocation, the cost above a per-head cap, earnings) rest on their own premise, never on a group conclusion (CR-12 1.1); no wage-down or earnings-down chain for recipients a floor holds, whether the floor exists or the measure sets it; a term ban's adjusting group falls on the prospective counterparties of new contracts (`applicant_actor`), the holders of voided contracts are bid up where they were paid below rivals (`paid_below_rivals`), and voiding is recorded on both sides (CR-8b); EN-14's Unless clause also opposes the stock's age and the fall in new units, and its question is asked of every standard. The record and answers are unchanged. Rows produced: 7 of 47 (unchanged). WRONG: 0 (unchanged). The new-unit price's horizon (short, where C-4 starts at medium) is still flagged.


## After the second round of rule changes

Second round of general fixes (`rules/mandates.lp`): play or pay (PC-17 0.9: firms that pay the charge face TX-2 on their labour, the state receives the charge, payers above a cap per firm bear a fixed cost, and the term itself and lock-in go to the recipients at firms that provide it, `player_recipient_actor`); inputs a standard or mandate requires (`related` kind `required`: more demand, and with slow supply a higher price for them and their other users); EN-15 for `disclosure_mandate` (compliance cost; buyers' choices on two premises, ignorance and direction; voluntary disclosure by exempt sellers); RS-24 (`fixed_cost_per_item`). The record gains the raters as a required input (the policy text names their certificate; it does not name the efficiency-product makers, so they are not recorded), and the answers its supply premise (A-14, 0.7). Rows produced: 9 of 47 (was 7): C-37 and C-42. WRONG: 0. Two new rows are defensible: the raters' price, the sellers' side of C-15, and fewer audits bought by the raters' other users at the higher price.
