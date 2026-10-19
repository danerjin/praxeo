# Out-of-sample run of the mandate rules on WE-034 (Teravel Freedom to Work Act)

Rules as they were at commit 96d60b0 (PC-17 developed on WE-029; PC-18 `term_prohibition` and EN-14 written from the catalog alone). Nothing under `praxeo/` was changed. Record: `record.json`, two components. K1 is a `term_prohibition` (bound `employers.restraining`, freed party `workers.bound`, `restrains_mobility`, `voids_existing`, enforcer `officials.enforcement`, no `general_budget` because the Act makes no new appropriation). K2 is the K4 notice as a `disclosure_mandate`, which no rule reads. The exemptions (K2, K3 of the example) and the private suits (K5) have no instrument and are not components; the exemptions appear only in the policy text. U1 (garden leave) and U2 (training repayment) change no Component field, so they carry readings and no `reading_fields`; the engine ran once. Answers: `answers.json`, four questions, all with a probability from the example's assumption table (`binding` A-1, `term_valued` A-5, `substitute_terms` A-4, `can_organize` A-13); no probability was judged. Run: `python3 -m praxeo cases/we034_teravel --out cases/we034_teravel/sample_run` (verifier and citation problems empty). Key: (actor class, variable, sign, window). No table actor name is mapped to a record role: the table's `employers.net_trainers` is a subclass of the record's bound class `employers.restraining`.

Summary: the table has 39 rows (C-1 to C-39). The engine reports 6 consequences, which give 7 keys (the CR-6 entry is a group over two variables). Table rows produced by key: 2 (C-1, C-23). Rows not produced: 37. Engine rows classified WRONG: 1 consequence (2 keys: `workers.bound` wage_rate and non_wage_compensation, `at_least_one_decrease`).

## Engine rows (reported)

| Engine row | Class | Why |
|---|---|---|
| workers.bound job_changes increase | in table | C-1 (CR-4b, CR-7 mobility). Only the 2026-on window; no window rows |
| officials.enforcement enforcement_cost increase | in table | C-23 (OC-3) |
| employers.restraining asset_value decrease | defensible | CR-8 voiding on the whole bound class; the table signs it for the net trainers (C-16) and the class's resources (C-38) |
| employers.restraining lobbying_effort increase | defensible | RS-7 on the bound class; the table has net trainers and associations (C-13) |
| employers.restraining term_prevalence increase | defensible | substitute terms (A-4), on the bound class; the table has the net trainers (C-4) |
| **workers.bound wage_rate at_least_one_decrease** | **WRONG** | The group (CR-5c, CR-6: the employer who valued the term offers less on other terms) is put on the workers whose existing contracts are voided. The table has their wage_rate rising (C-8) and non_wage_compensation rising (C-26), and says the opposing chain on their pay was checked and not found (final check 1). The group belongs to the would-be hires, `workers.trainees` (C-7) |
| **workers.bound non_wage_compensation at_least_one_decrease** | **WRONG** | Member of the same group; contradicted by C-26 |

## Table rows

| Row | Produced? | Reason |
|---|---|---|
| C-1 workers.bound job_changes increase | yes | |
| C-2 employers.restraining compliance_cost increase | no | unsupported form: K4 is a `disclosure_mandate`, which has no rules |
| C-3 founders.spinoff entry_rate increase | no | missing record fact and rule: no founders role; entry by the freed party not encoded |
| C-4 employers.net_trainers term_prevalence increase | no (role) | produced on `employers.restraining`, the bound class; with net_trainers mapped to it this row would count |
| C-5 net_trainers term_prevalence, per reading | no | unsupported form: signs per reading that change no Component field |
| C-6 net_trainers term_prevalence, per reading | no | unsupported form: same |
| C-7 workers.trainees wage_rate, non_wage_compensation, employment at_least_one_decrease | no | role: the engine puts this group on `workers.bound`; a term ban has no field for would-be counterparties. Employment is also not in the group |
| C-8 workers.bound wage_rate increase | no | missing rule: CR-7a, CR-9; the engine's group on the same class has the opposite sign |
| C-9 workers.bound job_changes decrease | no | missing rule: CR-4a, RS-11 (moves out of the field) |
| C-10 workers.bound job_changes ambiguous | no | combiner |
| C-11 workers.bound job_changes ambiguous (2025 window) | no | missing rule: RS-8 timing and the pending-cases clause |
| C-12 practices.professional reclassification increase | no | missing record fact and rule: exemptions have no field; RS-5 not applied to a term ban |
| C-13 net_trainers and associations lobbying_effort increase | no (role) | produced on `employers.restraining`; the associations have no role |
| C-14 net_trainers quantity_substitute increase | no | missing rule: RS-1 |
| C-15 employers.rivals search_cost decrease | no | missing record fact and rule |
| C-16 net_trainers asset_value decrease | no (role) | produced on `employers.restraining` |
| C-17 employers.rivals asset_value ambiguous | no | missing record fact and combiner |
| C-18 customers search_cost decrease | no | missing record fact and rule (CR-9) |
| C-19 customers price_paid ambiguous | no | combiner (RS-13 against RS-14); no customers role |
| C-20 intermediaries quantity_traded increase | no | missing record fact and rule (CR-9) |
| C-21 net_trainers investment_target decrease | no | missing rule: RS-4, CR-7a |
| C-22 officials.courts enforcement_cost ambiguous | no | combiner and role: no courts role |
| C-23 officials.enforcement enforcement_cost increase | yes | |
| C-24 officials.enforcement enforcement_cost decrease | no | missing rule: OC-3 fixed-budget case (CR-8a) |
| C-25 trainees, net_trainers quantity_traded decrease | no | missing rule: OC-4, CR-5a for a prevented exchange under a term ban |
| C-26 workers.bound non_wage_compensation increase | no | missing rule and question: retention pay (A-10); the engine's group on the same class has the opposite sign |
| C-27 employers.restraining quantity_traded decrease (buy-outs sold) | no | missing record fact and rule (CR-10a, CR-8b) |
| C-28 employers.rivals quantity_traded decrease (buy-outs bought) | no | same, with no rival role |
| C-29 employers.restraining quantity_traded decrease (client accounts) | no | missing rule: CR-9, CR-4 |
| C-30 intermediaries quantity_traded decrease | no | missing record fact and rule |
| C-31 intermediaries quantity_traded increase | no | missing record fact and rule |
| C-32 intermediaries quantity_traded ambiguous | no | combiner and role |
| C-33 officials.courts enforcement_cost decrease | no | missing record fact and rule: no courts role |
| C-34 officials.courts enforcement_cost increase | no | same |
| C-35 employers.rivals investment_target increase | no | missing record fact and rule (CR-4, CR-7a) |
| C-36 neighboring_jurisdictions investment_target increase | no | missing record fact and rule: a term ban has no neighbour field |
| C-37 neighboring_jurisdictions entry_rate decrease | no | same |
| C-38 employers.restraining resources_available_other_uses decrease | no | sign form: the engine signs the loss as `asset_value` only |
| C-39 workers.bound resources_available_other_uses increase | no | missing rule: the counterparty's side of the CR-8 voiding transfer |

Several rows carry two reasons; the table names the first. No row falls below the cut-off: the example's own assumptions below 0.5 (A-12, A-20, A-25, A-30) are not reported by the example either.

## Patterns for the rule writer

General, pattern-level problems the run shows. Rows are those of this table.

1. **One freed-party role for two different groups.** PC-18 puts the CR-5c, CR-6 group (employers offer less on other terms) on `tb_freed`, the workers whose contracts are voided. The example puts the group on the would-be counterparties of new contracts (`workers.trainees`, C-7) and signs the voided-contract holders' pay and benefits upward (C-8, C-26). A term ban that applies to existing and new contracts needs two roles: the holders of voided existing contracts (their option widens, the other terms cannot be re-set until renewal) and the prospective counterparties (the other terms adjust). Affects C-7 (not produced), C-8, C-26 (not produced), and the two WRONG engine rows. The PC-18 text in the example (CR-5c: "where the contract can be ended or renegotiated at will ... where it cannot, they do not until renewal") already makes this split. The WRONG rows are a rule problem, not an answer problem: the answers did not select the group; `term_valued` only gates it.
2. **The bound class is a superclass of the class the example works with.** The record's bound class is every employer holding a non-compete; the table's effects on loss of asset value, lobbying and substitute terms sit on the net trainers, a subset. The rules sign the bound role only. A subclass field (like `trainer_actor` in licensing) or a rule that signs the class the premise names would settle C-4, C-13, C-16 (3 rows if net_trainers were mapped to the bound role, which this run did not do).
3. **CR-8 voiding is half a transfer.** The rule signs the holder's `asset_value` fall and not the counterparty's gain, nor the holder's `resources_available_other_uses` fall (the example's CR-8b form). C-38, C-39; and the comment in the rule file ("passes from its holder to the other party") says both sides. 2 rows.
4. **Mobility restraint removed: only the first consequence is encoded.** RS-11 (substitute retention devices lock in and oppose the rise in moves), CR-7a/CR-7b (the gain settles on the freed means: pay rises), CR-4a (fewer moves out of the field), entry by the freed party (CR-4b), and the retention pay that replaces the restraint have no rule. C-3, C-8, C-9, C-10, C-26. With the missing combiner for job_changes (all), 5 rows; this is the example's own "removing a mobility restraint" pattern (Gaps found (c)).
5. **Timing of a retroactive change.** A term ban with a pending-cases clause or announcement needs RS-8 on both sides (waiting to move, moving early). PC-18 has no window. C-11.
6. **Exemptions as routes (RS-5) are not read for a term ban.** The record cannot say which terms the law leaves untouched, and `definition_line` is asked only of mandates. C-12, and the per-reading signs of C-5 and C-6, which the reading mechanism cannot carry when the reading changes no Component field (the example's U1 and U2 change what `term_prevalence` means, not a record field).
7. **Companion instruments with no rules.** The notice (`disclosure_mandate`, C-2) and the fixed enforcement budget (OC-3's no-new-appropriation case, C-24) are not encoded; the ceiling and mandate families already have the second one for `general_budget` and nothing for its absence. 2 rows.
8. **Third-party classes absent from the record schema for a term ban.** Rival employers, customers, intermediaries, courts, and the neighbouring jurisdiction (C-15, C-17 to C-20, C-22, C-27 to C-37) have no field in a `term_prohibition`, although the mandate rules already take a neighbour, rivals and an output buyer. This is the largest group: about 19 rows, and also the reason most of the table is out of reach whatever the answers.


## After the rule changes

General fixes from the out-of-sample runs on WE-031, WE-034, WE-036, WE-059 and WE-061 (`rules/mandates.lp`): a contract-kind field (`contract_kind`: employment or sale), so the wage, hours, jobs and earnings chains apply only to employment contracts (PC-17 1.1); later chains (unbound rivals, relocation, the cost above a per-head cap, earnings) rest on their own premise, never on a group conclusion (CR-12 1.1); no wage-down or earnings-down chain for recipients a floor holds, whether the floor exists or the measure sets it; a term ban's adjusting group falls on the prospective counterparties of new contracts (`applicant_actor`), the holders of voided contracts are bid up where they were paid below rivals (`paid_below_rivals`), and voiding is recorded on both sides (CR-8b); EN-14's Unless clause also opposes the stock's age and the fall in new units, and its question is asked of every standard. The record gains `applicant_actor` = `workers.trainees` (the would-be counterparties of new contracts), and the answers gain `paid_below_rivals` (A-7, 0.75). Rows produced: 6 of 39 (was 2): C-7, C-8, C-38 and C-39 added. WRONG keys: 0 (was 2).


## After the second round of rule changes

Second round of general fixes (`rules/mandates.lp`): play or pay (PC-17 0.9: firms that pay the charge face TX-2 on their labour, the state receives the charge, payers above a cap per firm bear a fixed cost, and the term itself and lock-in go to the recipients at firms that provide it, `player_recipient_actor`); inputs a standard or mandate requires (`related` kind `required`: more demand, and with slow supply a higher price for them and their other users); EN-15 for `disclosure_mandate` (compliance cost; buyers' choices on two premises, ignorance and direction; voluntary disclosure by exempt sellers); RS-24 (`fixed_cost_per_item`). K4, the notice, is a `disclosure_mandate`; the answers gain its five questions (A-2, A-13; the two direction questions answered no: the notice changes no purchase). Rows produced: 7 of 39 (was 6): C-2, the employers' compliance cost. WRONG: 0.
