# Out-of-sample run of the subsidy and ceiling rules on WE-056 (Tarrenmoor Insulin Affordability Act)

Rules as they were at commit 59d879f (subsidies SB-1 to SB-6 developed on WE-019 only; ceilings PC-1 to PC-21), handbook catalog 1.4. Nothing under `praxeo/` was changed. Record: `record.json`, written from `policy.txt` alone: K1 as a `price_ceiling` (bound `pharmacies.in_state`, protected `covered_residents.paying_above_cap`, enforcer `officials.enforcement`, announcement window, no general-budget flag because the Board is fee-funded), K2 as a `mandated_contract_term` (plans pay the balance; no rules, no questions), K3 as a `purchase_rebate` (recipients `covered_residents.uninsured`, sellers and claim handler `pharmacies.in_state`, other buyers `buyers.noncovered_cash`, substitute sellers `sellers.substitutes`, criteria, announcement window, general-revenue funded). The worked example itself says K1 is not a ceiling (section 2: PC-20); a parser reading only the text has no other ceiling-like type to use, so K1 tests what the rules do with a cap that a third party makes up. Answers: `answers.json`, 30 questions; 8 taken from the assumption table (A-1, A-3, A-8, A-11, A-16, A-17, A-25, A-30), 22 judged from the text. Run: `python3 -m praxeo cases/we056_tarrenmoor --out cases/we056_tarrenmoor/sample_run`; verifier and citation problems: none. Key: (actor class, variable, sign, window).

Summary: the table has 51 rows (C-1 to C-51). The engine reports 25 consequences (46 derived; the others are below the cut-off). Rows produced by key: 7 (C-1, C-5, C-17, C-24, C-39, C-40, C-41), of which C-5, C-17 and C-24 for some of the classes the row names. Rows not produced: 44. Engine rows classified WRONG: 11 of 25, all from K1 being treated as a ceiling.

## Engine rows (reported)

| Engine row | Class | Why |
|---|---|---|
| covered_residents.paying_above_cap price_paid decrease | in table | C-1 (by PC-3's insider gain; the example's mechanism is CR-8b / SB-2) |
| covered_residents.paying_above_cap resources_available_other_uses increase | in table | C-39 |
| covered_residents.paying_above_cap lobbying_effort increase; pharmacies.in_state lobbying_effort increase | in table (part) | C-24 (patient groups and pharmacies; no PBM or insurer roles) |
| covered_residents.uninsured quantity_traded increase | in table (part) | C-5 (SB-2; the state-plan members are not a recipient role) |
| covered_residents.uninsured quantity_traded decrease, window announcement | in table (part) | C-17 (RS-8 with A-11) |
| pharmacies.in_state compliance_cost increase | in table | C-40 (CR-8c claims) |
| officials.enforcement enforcement_cost increase | in table | C-41 (OC-3; the record has one enforcer for both the Board and the Department) |
| covered_residents.uninsured price_paid decrease | defensible | SB-2 for the Fund's recipients; a subclass of C-1's paying_above_cap, which the example says includes the uninsured cash buyers |
| covered_residents.paying_above_cap price_paid decrease, window first_months | defensible | same sign as C-1 |
| covered_residents.paying_above_cap quality_adjusted_price decrease | defensible | price falls with the product unchanged; the table signs the product (C-10, C-11) |
| pharmacies.in_state resources_available_other_uses increase (item key_money) | defensible | PC-6 on A-16: some pharmacies collect more than $35; the table has the breach (C-23) |
| sellers.substitutes quantity_traded decrease (item unsubsidized_goods) | defensible | SB-3 / RS-1 on A-8; the table has the buyers' side (C-12) and the chains' price and stocks (C-29) |
| taxpayers resources_available_other_uses decrease | defensible | SB-1 with OC-1, Tier A; C-37 has the same class inside an at_least_one_decrease group, so it does not count by key |
| **pharmacies.in_state net_price_received ambiguous** | **WRONG** | PC-16 (transfer from the sellers) against SB-2's increase. The example: the pharmacy receives the contract rate or the Fund's payment, so C-4 is no_change and C-6 an increase |
| **pharmacies.in_state quantity_traded ambiguous** | **WRONG** | SB-2's increase against PC-5 (supply falls through alternative_uses, answered 0.15). The example has an increase under both readings (C-26) |
| **pharmacies.in_state resources_available_other_uses decrease (item rent_forgone, and the total)** | **WRONG** | CR-8 with PC-16 takes the patients' saving from the pharmacies; the example has it paid by plans, the Fund and, through them, premium payers and taxpayers (CR-8b, C-37, C-38). Two engine rows |
| **buyers.prospective excess_demand increase** | **WRONG** | PC-1 where no shortage forms (section 2: PC-1 and PC-16 do not apply). The record has no excluded role; the engine fills `buyers.prospective` |
| **buyers.prospective quantity_demanded increase** | **WRONG** | same |
| **buyers.prospective wait_time / search_cost / side_payments / allocation_by_non_price_criteria at_least_one_increase** | **WRONG** | the PC-2 rationing group; the example removes rationing |
| **buyers.prospective search_cost increase; side_payments increase** | **WRONG** | PC-2 members |
| **buyers.prospective informal_activity increase** | **WRONG** | PC-6 with RS-3 for shut-out buyers |
| **buyers.prospective disputes_settled_outside_courts increase** | **WRONG** | RS-10 for the same informal trade |

## Table rows

| Row | Produced? | Reason |
|---|---|---|
| C-1 paying_above_cap price_paid decrease | yes | |
| C-2 plans.state_regulated subsidy_outlay increase | no | unsupported form: K2, a mandated payment |
| C-3 insulin_fund subsidy_outlay increase | no | missing record fact (no paying-fund role) and rule (SB-1 signs funders, not outlay) |
| C-4 pharmacies net_price_received no_change | no | missing rule: PC-20 / CR-6 1.1; the engine's row for this key is WRONG (ambiguous) |
| C-5 covered_residents quantity_traded increase | yes (part) | uninsured only |
| C-6 pharmacies net_price_received increase | no | missing rule: SB-2 1.1 (payment indexed to the seller's own price); DM-1 needs seller_supply_slow (0.1) |
| C-7 buyers.noncovered_cash price_paid increase | no | missing rule: same |
| C-8 pharmacies quality_per_unit / side_payments group | no | missing rule: RS-2 for a payer-paid customer |
| C-9 plans term_prevalence increase | no | unsupported form (K2) |
| C-10 uninsured quality_per_unit increase | no | missing rule: RS-21 / RS-16 for subsidies |
| C-11 state_plans quality_per_unit ambiguous | no | unsupported form (K2), same missing rule |
| C-12 buyers.otc_human_insulin quantity_substitute decrease | no | missing record fact: no role for the substitute's buyers (SB-3 gives the sellers' side only) |
| C-13 program_enrollees price_paid increase | no | missing record fact and rule (CR-9 displacement of a private program) |
| C-14 manufacturers quantity_traded increase | no | missing record fact (no upstream role) and rule |
| C-15 manufacturers net_price_received increase | no | missing record fact and rule (CR-6 small effect in a wider market) |
| C-16 buyers.other_states price_paid increase | no | same |
| C-17 covered_residents quantity_traded decrease (Nov-Dec 2027) | yes (part) | uninsured only |
| C-18 covered_residents quantity_traded increase (Jan-Feb 2028) | no | missing rule: RS-8 catch-up after the effective date for buyers |
| C-19 buyers.plan_premiums price_paid increase | no | unsupported form (K2) |
| C-20 employers.fully_insured reclassification increase | no | unsupported form (K2) |
| C-21 buyers.individual_market quantity_traded decrease | no | unsupported form (K2) |
| C-22 false attestations legal_breach increase | no | missing rule (RS-3 for attestation) and record fact |
| C-23 pharmacies legal_breach increase | no | missing rule: A-16 gives key money, not a breach |
| C-24 lobbying groups lobbying_effort increase | yes (part) | pharmacies and patients; no PBM, insurer roles |
| C-25 mail-order users, nonresident pharmacies cross_border_purchases | no | missing record fact: U1's readings carry no engine facts; no nonresident role; RS-4 for mail order |
| C-26 pharmacies.in_state quantity_traded increase | no | the engine signs it ambiguous (WRONG row) |
| C-27 nonresident compliance_cost | no | missing record fact: no nonresident role |
| C-28 mail_order_users travel_time | no | missing record fact |
| C-29 sellers.substitutes price_substitute, inventory_held | no | missing rule: RS-16, CR-10b |
| C-30 sellers.substitutes price_substitute ambiguous (long) | no | missing rule: CR-12e / CR-7a |
| C-31 clinics quantity_complement increase | no | missing record fact (no complements role for subsidies); RS-12 not encoded |
| C-32 pen needles, syringes quantity_complement increase | no | same |
| C-33 pharmacies net_price_received decrease (2029) | no | case-specific provision: PBM contract renewals |
| C-34 manufacturers asset_value increase | no | missing record fact (SB-4 needs asset_owner_actor) |
| C-35 general_fund tax_revenue ambiguous | no | combiner: CR-12b total not declared; premium tax is case-specific |
| C-36 insulin_fund non_tax_receipts increase | no | missing rule (OC-3 own-revenue case, fines) and record fact |
| C-37 taxpayers etc. resources at_least_one_decrease | no | sign form: the engine signs taxpayers with a plain decrease (a defensible row above) |
| C-38 buyers.plan_premiums resources decrease | no | unsupported form (K2) |
| C-39 paying_above_cap resources increase | yes | |
| C-40 pharmacies compliance_cost increase | yes | |
| C-41 officials.enforcement enforcement_cost increase | yes | |
| C-42 Board wait_time / enforcement_cost group | no | missing rule: OC-3's absorbed-in-budget case for ceilings (A-5) |
| C-43 hdhp resources ambiguous | no | case-specific provision: deductible accounting |
| C-44 hdhp price_paid increase | no | case-specific provision: same |
| C-45 state_plans wait_time increase | no | unsupported form (K2) |
| C-46 manufacturers resources increase | no | missing record fact and rule |
| C-47 border residents cross_border_purchases decrease | no | missing record fact: no role; `neighbor_actor` is for shut-out buyers |
| C-48 buyers.noncovered_cash quantity_traded decrease | no | missing rule: as C-7 |
| C-49 national_government subsidy_outlay increase | no | unsupported form (K2), no role |
| C-50 nonresident asset_value | no | missing record fact: no nonresident role |
| C-51 plans.self_funded price_paid decrease | no | missing rule and record fact |

## General gaps

Ranked by the rows each would add or fix.

1. **A cap on the buyer's share that a third party makes up (PC-20, with the 1.1 clauses of PC-1, PC-16 and CR-6).** Fixes all 11 WRONG engine rows and adds C-4 (and, with item 5, C-6). Pattern-level change: a record fact on a `price_ceiling` (the balance is paid by someone else, so the sellers' receipt is not capped) that switches off the shortage chain (PC-1 excess demand, PC-2, PC-5, PC-6, PC-16 transfer from sellers) and leaves CR-1 / CR-8b (the payers bear it) and SB-2 for the buyers' price and quantity. Without it the parser's only available type produces the shortage the handbook says does not form. A related defect: a null `excluded_actor` still yields `buyers.prospective`; a record must be able to say there are none.
2. **The mandated payer (K2) and pass-through (CR-9, CR-7b, CR-8b, OC-1).** Adds C-2, C-9, C-11, C-19, C-20, C-21, C-38, C-45, C-49 and, with a fund role, C-3 (about 10 rows). One pattern: a `mandated_contract_term` / mandated payment makes the payer's outlay rise, the payer passes it to its premium payers, who pay more and have less to spend. Needs a payer and a premium-payer role field.
3. **Wider-market and substitute roles (CR-6 small effects, RS-16, RS-12, CR-9, SB-4 for shares).** Adds C-12 to C-16, C-29 to C-32, C-34, C-46 (about 11 rows). Subsidy records have `substitute_seller_actor` but no substitute buyers, complements, upstream suppliers or asset owners beyond SB-4's single field.
4. **Unclear provisions that decide who is bound (U1) with RS-4 for mail order.** Adds C-25 to C-28, C-47, C-50 (6 rows). Needs per-reading facts a parser can fill (the readings carry facts only if a person writes them) and a nonresident-seller role.
5. **SB-2 1.1: a payment indexed to the seller's own price.** Adds C-6, C-7, C-48 (3 rows). A question and a rule for the posted price drawn toward the limit; today DM-1 is gated on fixed supply, which does not hold for insulin.
6. **OC-3 with CR-8b for own-revenue fines and an absorbed budget; RS-3 for attestation and overcharges as breaches.** C-36, C-42; C-22, C-23, C-51 (5 rows).
7. **RS-8 catch-up for buyers after the effective date and RS-2 for payer-paid customers.** C-18, C-8, C-10 (3 rows).

C-33, C-35, C-43 and C-44 (PBM renewals, premium tax, deductible accounting) are case-specific and need no general fix.
