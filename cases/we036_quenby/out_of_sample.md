# Out-of-sample run of the mandate rules on WE-036 (Quenby Fair Share Health Cover Act)

Rules as they were at commit 96d60b0 (`praxeo/rules/mandates.lp`: PC-17 developed on WE-029, PC-18 and EN-14 written from the catalog alone). Nothing under `praxeo/` was changed. Record: `record.json`, two components. K1 is a `mandated_contract_term` (bound `employers.bound`, recipients `workers.uncovered`, floor-bound `workers.min_wage`, already-providers `employers.lean_plans` with recipients `workers.lean_plans`, `per_head_cap` read as the 30-hour line with `workers.near_30` below and `workers.full_time` above, output buyers `buyers.local_services`, tradable `employers.tradable` against `neighboring_jurisdictions`, rivals `employers.compliant` and `employers.small`, `definition_line` with the agencies and contractors outside, `forfeit_on_leaving` (the 60-day wait and cover lost on moving to unbound work), `size_threshold` with `employers.near_50` and `employers.small`, `threshold_staff_split` for the seasonal workers, `margin_recipient_actor` `workers.seasonal`, `general_budget` with no future taxpayers). K3, K4 and K5 are folded into K1 (the threshold, the cap per firm, and the enforcer and budget); the cap per firm has no field, and the buy-out charge has none either. K2 is a `product_standard` (makers `insurers.group`, buyers `employers.players`). U1 (seasonal workers in the count) changes two K1 fields per reading, so it has `reading_fields`: U1-a sets `margin_covered`, U1-b sets `threshold_partial_count`. Answers: `answers.json`, 21 questions; 19 take their probability from the example's assumption table (A-1, A-3, A-5, A-6, A-7, A-9, A-11, A-14, A-17, A-19, A-21, A-22, A-23, A-24, A-26, A-35; `rivals_bound` is answered no with P(yes) 0.4 from A-24, so its chain is unreported, as in the example), and `k1.enforced` and `k2.enforced` are judged from the text (0.9). Run: `python3 -m praxeo cases/we036_quenby --out cases/we036_quenby/sample_run` (verifier and citation problems empty). Key: (actor class, variable, sign, window); the table's "insurers" is `insurers.group`, its "unions" `workers.uncovered`, its "recipients of other general-fund spending" `recipients.other_spending`.

Summary: the table has 60 rows (C-1 to C-61, no C-6). The engine reports 37 consequences (of 39 derived), which give 43 keys (the OC-1 entry and the RS-18 and PC-17 groups give several keys each). Table rows produced by key: 23 (C-2, C-5, C-7, C-8, C-9, C-10, C-15, C-16, C-20, C-23, C-27, C-28, C-29, C-30, C-32, C-33, C-34, C-38, C-41, C-42, C-45, C-53, C-54); C-2 by a different derivation (see below), and C-20, C-23, C-32 in part. Rows not produced: 37. Engine rows classified WRONG: 5.

## Engine rows (reported)

| Engine row | Class | Why |
|---|---|---|
| workers.uncovered wage_rate decrease | in table | C-7 |
| workers.uncovered, workers.min_wage: employment, hours_worked, non_wage_compensation at_least_one_decrease | in table | C-8, C-9, C-10 (PC-17, PC-10) |
| workers.uncovered tax_share_borne increase | in table | C-30 (CR-7b) |
| workers.uncovered lobbying_effort increase | in table | C-23, "unions" |
| workers.lean_plans non_wage_compensation increase | in table | C-5 (conditions_differ, enforced) |
| employers.bound price_paid increase | in table | C-45 |
| employers.bound return_on_capital decrease; asset_value decrease | in table | C-29; C-27 |
| employers.bound compliance_cost increase | in table | C-42 (OC-2, Tier A) |
| employers.near_50 employment decrease | in table | C-15 and C-53 (same key; the engine's horizon is short only) |
| employers.near_50 employment, U1-a decrease / U1-b increase | in table | C-20, near_50 side, per reading |
| employers.small number_of_sellers increase; asset_value increase; quantity_supplied increase | in table | C-16; C-28; C-32 |
| employers.compliant quantity_supplied increase | in table | C-32 |
| employers.tradable quantity_supplied decrease; neighboring_jurisdictions quantity_supplied increase | in table | C-33; C-34 |
| insurers.group compliance_cost increase; lobbying_effort increase | in table | C-54; C-23 |
| officials.enforcement enforcement_cost increase | in table | C-41 (OC-3) |
| taxpayers, recipients.other_spending resources_available_other_uses at_least_one_decrease | in table | C-38 (OC-1 group, no future taxpayers) |
| employers.players price_paid increase | in table | C-2 by key. The engine derives it from K2 (EN-14: the buyers of covered plans pay more), the table from the contribution a player pays (CR-1, CR-5c). Same key, different claim |
| employers.bound lobbying_effort increase | defensible | the bound role; the table lists its subclasses (C-23) |
| employers.bound reclassification increase | defensible | RS-5 on the bound role; the table has mid-size payers (C-56) and firms near 50 (C-18) |
| employers.bound resources_available_other_uses decrease | defensible | CR-8b on the bound role; the table has capped, players and payers (C-14, C-43, C-46) |
| employers.lean_plans compliance_cost increase | defensible | CR-8c, firms that rewrite short plans (A-5); the table has all bound firms (C-42) |
| employers.players specification_level increase | defensible | buyers' side of C-25 (the table has the insurers) |
| sellers.contract_services reclassification increase | defensible | RS-5 on the actor outside the definitions; the table has the agencies' sales (C-60) |
| workers.near_30 employment, hours_worked at_least_one_decrease | defensible | RS-18 group below the line, true given C-11 |
| workers.uncovered earnings decrease | defensible | wage falls (C-7), hours or jobs fall (C-8, C-9) |
| workers.seasonal non_wage_compensation, U1-a increase / U1-b no_change | defensible | seasonal firms bound under U1-a only (C-19, C-61); gives all their workers cover, which holds only at players |
| **workers.uncovered non_wage_compensation increase** | **WRONG** | The class is workers at bound firms in both branches. The example gives cover only to those at players (C-1) and says nothing is added for the worker at payers (section 2); the total is ambiguous (C-44) |
| **employers.compliant asset_value increase** | **WRONG** | C-48 says ambiguous: rivals' costs help them (A-22), their own quarterly offer reporting (C-42) hurts. The engine has the gain only |
| **workers.full_time hours_worked ambiguous** | **WRONG** | C-12 says increase. The engine sets RS-18's shift against a general cost-rise chain (mc_cap_cost, via `worth_less`); section 7 calls that chain a suspected effect the rules do not derive (CR-12 kind 1, Tier C) |
| **workers.uncovered job_changes decrease** | **WRONG** | RS-11 lock-in at the medium horizon for the whole class. The example has decrease in the short run at players only (C-57), and ambiguous once wages adjust (C-58) |
| **insurers.group quantity_supplied decrease** | **WRONG** | EN-14 cuts the makers' output. The example has group plans meeting K2 sold in greater number (C-24) and lean plans still sold to payers (section 6) |

## Table rows

| Row | Produced? | Reason |
|---|---|---|
| C-1 workers.at_players non_wage_compensation increase | no | role: the cover is signed on the whole recipient class, not on players' workers (see the WRONG row) |
| C-2 employers.players price_paid increase | yes (by key) | derived from K2, not from K1's contribution |
| C-3 employers.payers_midsize price_paid increase | no | missing record fact: no field for the buy-out charge or the players/payers split; C-45 is produced on employers.bound |
| C-4 general_fund non_tax_receipts increase | no | missing record fact and rule: the charge paid to the state |
| C-5 workers.lean_plans non_wage_compensation increase | yes | |
| C-7 workers.uncovered wage_rate decrease | yes | |
| C-8 workers.uncovered employment, hours_worked, non_wage_compensation at_least_one_decrease (short) | yes | |
| C-9 same (medium) | yes | one engine row stands for both horizons |
| C-10 workers.min_wage same | yes | |
| C-11 workers.near_30 hours_worked decrease | no | sign form: group over employment and hours_worked |
| C-12 workers.full_time hours_worked increase | no | combiner: the engine says ambiguous (WRONG row) |
| C-13 workers.capped_firms employment, hours_worked at_least_one_increase | no | missing rule and record fact: cap per firm, sales won (CR-9, OC-5) |
| C-14 employers.capped resources_available_other_uses decrease | no | role: no capped class; signed on employers.bound |
| C-15 employers.near_50 employment decrease (2027) | yes | window ignored |
| C-16 employers.small number_of_sellers increase | yes | |
| C-17 employers.near_50 asset_value ambiguous | no | missing rule: value of firms near the line |
| C-18 employers.near_50 reclassification increase | no | role: RS-5 signs the bound role; these firms are below 50 |
| C-19 employers.seasonal price_paid, per reading | no | missing record fact: the 380 firms have no role |
| C-20 employers.seasonal, near_50 employment, per reading | yes (part) | near_50 side only |
| C-21 employers.near_50 employment ambiguous (flow) | no | missing rule: RS-8 timing chains at a threshold |
| C-22 employers.bound legal_breach increase | no | missing rule: breach under self-report with audit; mc_breach is for complaint-only enforcement |
| C-23 lobbying_effort increase | yes (part) | insurers.group and workers.uncovered; payers, capped, near_50 are not roles |
| C-24 insurers.group quantity_traded increase | no | missing rule: CR-9; EN-14 gives the opposite on quantity_supplied (WRONG row) |
| C-25 insurers.group specification_level increase | no | role: EN-14 signs the buyers |
| C-26 insurers.individual quantity_substitute decrease | no | missing rule: RS-1 for a mandate |
| C-27 employers.bound asset_value decrease | yes | |
| C-28 employers.small asset_value increase | yes | |
| C-29 employers.bound return_on_capital decrease | yes | |
| C-30 workers.uncovered tax_share_borne increase | yes | |
| C-31 payers_midsize, players quantity_supplied decrease | no | missing rule: RS-14 exempt-rival branch; the price branch (mc_pass) is below the cut-off at A-24 (0.4), as in the example |
| C-32 capped, small, compliant quantity_supplied increase | yes (part) | small and compliant; capped is bound, so not in `rival_actors` |
| C-33 employers.tradable quantity_supplied decrease | yes | |
| C-34 neighboring_jurisdictions quantity_supplied increase | yes | |
| C-35 providers.medical quantity_complement increase | no | missing rule: RS-12 for a mandate |
| C-36 general_fund subsidy_outlay decrease | no | missing rule: CR-9 along the insurance contract |
| C-37 general_fund tax_revenue decrease | no | missing rule: TX-10 |
| C-38 taxpayers, recipients of other spending at_least_one_decrease | yes | |
| C-39 same at_least_one_increase (charges received) | no | missing record fact and rule: no charge in the record |
| C-40 same at_least_one_increase (total, short) | no | missing rule and combiner |
| C-41 officials.enforcement enforcement_cost increase | yes | |
| C-42 employers.bound, compliant compliance_cost increase | yes (part) | bound only |
| C-43 employers.players resources_available_other_uses decrease | no | role: signed on employers.bound |
| C-44 workers.at_players non_wage_compensation ambiguous | no | combiner: two items in one variable, reported unreconciled on workers.uncovered |
| C-45 employers.bound price_paid increase | yes | |
| C-46 employers.payers_midsize resources_available_other_uses decrease | no | role |
| C-47 employers.capped asset_value ambiguous | no | role and missing rule |
| C-48 employers.compliant asset_value ambiguous | no | combiner: gain only (WRONG row) |
| C-49 taxpayers etc. ambiguous (medium) | no | combiner: no receipts side |
| C-50 workers.near_30 employment increase | no | missing rule: positions under the line |
| C-51 workers.full_time employment decrease | no | missing rule: RS-18 heads fall |
| C-52 employers.bound employment ambiguous | no | combiner: needs C-50 and C-51 |
| C-53 employers.near_50 employment decrease (stock) | yes (by key) | same key as C-15; the engine does not tell flow from stock |
| C-54 insurers.group compliance_cost increase | yes | |
| C-55 workers.uncovered employment etc. at_least_one_increase | no | unsupported form: one group over employment at three classes of employer |
| C-56 employers.payers_midsize reclassification increase | no | role and missing record fact |
| C-57 workers.at_players job_changes decrease | no | role (WRONG row is on workers.uncovered, medium) |
| C-58 workers.at_players job_changes ambiguous | no | combiner and missing rule: no opposing chain |
| C-59 workers.unbound wage_rate ambiguous | no | missing rule: CR-9 and CR-7a at unbound firms |
| C-60 sellers.contract_services quantity_traded increase | no | missing rule: CR-9 for the agencies' sales |
| C-61 employers.seasonal asset_value, per reading | no | missing record fact: no role |

## Patterns for the rule writer

General problems the run shows, ranked by the table rows they touch. The first two matter most.

1. **A mandate the bound party can buy off (play or pay).** The record has one recipient role and one bound role. The example splits the bound firms by response (players, payers, and the capped payers) and gives the term only to the players' workers; payers pay a charge to the state, which the workers do not value. With one recipient class, PC-17 gives cover to the payers' workers too (WRONG row, workers.uncovered non_wage_compensation) and lock-in to all of them (WRONG row, job_changes); it signs the cost on the bound role instead of on players and payers (C-3, C-43, C-46, C-14); and nothing signs the charge or the fund's receipts (C-4, C-39, C-40, C-49). PC-17 wants a record fact that the term can be bought off, a field for who offers and who pays, and a recipient role for the offering side. The term's effects (cover, lock-in, cost to the provider) should then run through the offering side only and the wage and hours effects through both. Rows: C-1, C-3, C-4, C-14, C-39, C-40, C-43, C-44, C-46, C-49, C-57, C-58 and the two WRONG rows on workers.uncovered.
2. **Fixed cost per firm and caps per firm.** `per_head_cap` is read as the 30-hour line here, and the firm-level cap has no field. The rules cannot say that capped firms pay a sum that does not vary with heads, win sales from mid-size payers (CR-9, OC-5), and supply agency labor that payers take in place of direct hires (RS-5 with A-34). Rows: C-13, C-14, C-32 (capped), C-47, C-56, C-60.
3. **A threshold on a worker's hours (RS-17 and RS-18 together).** `mc_cap_shift` gives a group below the line and one increase above it. The example signs each member of the single CR-4 switch: hours below the line fall, positions under the line rise, full-time heads fall, hours above the line rise, total heads ambiguous. The rule also adds a general cost-rise chain (`mc_cap_cost`) for the workers above the line. That makes the engine say ambiguous where WE-036 says increase (WRONG row), and WE-029 said ambiguous only because it also had the cover-for-absences chain. The cost chain should stand only with a second, independent chain, or be dropped. Rows: C-11, C-12, C-50, C-51, C-52.
4. **A size threshold: what the firms near it do besides hiring less.** `mc_threshold` signs hiring, the firms staying small, and the counted and uncounted staff. It does not sign the value of firms near the line (rivals' burden against lost growth), the timing of crossings (RS-8: held back in the measurement year, ambiguous flow afterward), contracting out by the firms near the line (RS-5 signs the bound role, but these firms are not bound), or the owners and price of firms whose status turns on a reading (the 380 seasonal firms; only the workers' margin is read). The measurement year before the effective date is not expressible, so C-15 and C-53 share a key. Rows: C-17, C-18, C-19, C-21, C-53, C-61.
5. **Opposing chains and the sums of two items in one variable.** Where the example is `ambiguous` the engine often has one side only. Rivals' gain is signed with no burden on the rivals themselves, although K5 puts reporting on every employer of 50 or more, compliant ones included (WRONG row, employers.compliant asset_value; C-48, C-47). Cover is signed up and the other terms down on the same variable, unreconciled (C-44), and total heads, charges against the appropriation and job changes lack their second chain (C-52, C-49, C-58). `mc_compliance` should reach every firm the measure makes report, not only those it binds. A rule that signs a gain to unbound rivals should look for the burden the measure puts on them. Rows: C-44, C-47, C-48, C-49, C-52, C-58, C-59.
6. **Related markets for a mandate.** Mandates have no `related` roles, so CR-9 (plans `input_to` compensation), RS-1 (individual plans as substitutes), RS-12 (care as a complement) and the fund's outlays and tax receipts are not signed. Rows: C-24, C-26, C-35, C-36, C-37, C-60, and the general-fund rows of pattern 1.
7. **EN-14 on a standard whose units are demanded because of another measure.** K2 sets the plans that count under K1. EN-14 gives the makers a fall in output and the buyers a higher price; the example has more compliant plans sold (C-24) and the buyers' specification rising (C-25 on the makers). The quantity decrease (WRONG row, insurers.group quantity_supplied) should need that the standard narrows a trade people would make anyway. The price row matches C-2 only by key. Rows: C-2, C-24, C-25.
8. **Enforcement by self-report with audit.** `mc_breach` needs complaint-only enforcement. The example has breach (offers reported but not made) from the gain of misreporting against the audit risk and a penalty of twice the charge. A second route to `legal_breach` under a mandate, gated on the cost saved and on weak verification, would fit; it also fits the prohibitions. Row: C-22.
9. **RS-14's exempt-rivals branch and workers' moves to unbound work.** `mc_pass` is the price branch (rivals bound). The branch where rivals are exempt or lightly bound, so the bound sellers lose sales and the rivals gain them, has the rivals' side only (mc_rivals); the bound sellers' quantity fall is missing. Nothing signs workers' moves to firms under the threshold, to part-time work or across the border, or the wage at unbound firms (opposing chains). Rows: C-31, C-55, C-59.
10. **Horizon of lock-in (RS-11).** `mc_lockin` signs job changes down at medium and long horizons. It holds while wages are fixed (`wages_sticky`); once wages adjust, the lower wage at the term's firms pushes job changes the other way. The rule should be short run on `wages_sticky`, and the second chain should give ambiguous at medium. Rows: C-57, C-58 and the WRONG row on job_changes.


## After the rule changes

General fixes from the out-of-sample runs on WE-031, WE-034, WE-036, WE-059 and WE-061 (`rules/mandates.lp`): a contract-kind field (`contract_kind`: employment or sale), so the wage, hours, jobs and earnings chains apply only to employment contracts (PC-17 1.1); later chains (unbound rivals, relocation, the cost above a per-head cap, earnings) rest on their own premise, never on a group conclusion (CR-12 1.1); no wage-down or earnings-down chain for recipients a floor holds, whether the floor exists or the measure sets it; a term ban's adjusting group falls on the prospective counterparties of new contracts (`applicant_actor`), the holders of voided contracts are bid up where they were paid below rivals (`paid_below_rivals`), and voiding is recorded on both sides (CR-8b); EN-14's Unless clause also opposes the stock's age and the fall in new units, and its question is asked of every standard. The answers gain `k2.buyers_value_standard` (0.3: firms buy plans meeting K2 because K1 counts only those, not because they value the standard). Rows produced: 23 of 60 (unchanged). WRONG: 5 (unchanged): cover for the payers' workers (play or pay is not split in the record or the rules), the compliant firms' value (K5's burden on them is an opposing chain no rule forms), full-timers' hours (an hours threshold recorded as a cap), lock-in at the medium horizon, and insurers' plan sales (units demanded because of another measure).
