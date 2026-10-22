# WE-036 Quenby Fair Share Health Cover Act: expand loop, blind run (loop_r6)

Files: `seed.json`, `proposals.json`, `answers.json`, `policy.txt` (section 1 as given), `situation.json` (final), `final_output.txt` (engine output).
Run: DONE in 3 rounds (depth limit), 51 node visits (14 + 21 + 16), 21 premise questions. No `off-list:` lines in any run.
Read only the two extracted files (section 1, assumption table). Nothing under `handbook/05_examples*`, `tests/` or an existing `cases/we036_quenby/` file was opened. Vocabulary came from `--vocab --exclude WE-036`.

## Seed (the policy's own facts, CR-1)

Classes split where the policy treats parts differently:
- Employers: `employers.offering` (take the in-kind branch), `employers.paying` (take the pay branch, below the cap), `employers.capped` (the 45 firms above 100 uncovered full-timers, K4), `employers.near_threshold` (the 40 to 60 FTE firms, K3), `employers.seasonal` (the 380 firms, U1). Workers: `workers.at_offering_firms`, `workers.at_paying_firms`, `workers.min_wage` (R1, at paying firms), `workers.at_capped_firms`, `workers.at_seasonal_firms`, `workers.near_30_hours` (the 30-hour line).
- Exchanges (all employment of a full-timer, seller price `wage_rate`): `e_off`, `e_pay`, `e_mw`, `e_cap`, `e_seas`.
- K1 offer branch: charge `k1_offer` on `e_off`, receiver `workers.at_offering_firms`, `non_wage_compensation`, `quantity_premises` a7 (cover at 30% is worth less to the worker than its cost: the mandated term is not fully recovered, so the fall in trades is not a priori), `branch_premises` a1 (K1 binds), a2 (some offer).
- K1 pay branch: charge `k1_pay` on `e_pay` and `e_mw`, receiver `officials.revenue`, `non_tax_receipts` (+ projection variable), `branch_premises` a1, a4 (some pay).
- K4 cap: `means` out for `employers.capped` (CR-1 0.9: operation 4 above the cap), not a charge (see limits).
- `fixed`: wage on `e_off`, `e_pay` fixed short (a3, pay scales); wage on `e_mw` fixed long (a9, minimum wage binds). `moves`: wage takes the charge in the medium run on `e_off`, `e_pay` (a6 raises can adjust, a37 response partial). `incidence`: workers' side on `e_off`, `e_pay` (a23, medium to long run).
- `thresholds`: k3 (`employers.near_threshold`, `employment`, a14); k3_a (`employers.seasonal`, a33); the 30-hour line on `workers.near_30_hours`, `hours_worked`, chosen by the employers (a10), once for each branch.
- `unclear` U1: reading U1-a applies `k3_a` and `k1_seas_a` (a charge on `e_seas`, branch premise a33); U1-b applies neither.
- `announced` k1_offer, k1_pay (a21), k3 (a15); `compliance` (offering, paying, capped employers; insurers for K2); `enforcers` k5 (`officials.revenue`, `officials.enforcement`); `funded` k5 by `taxpayers` (a29).
- Seed assumptions: a1, a2, a3, a4, a6, a7, a9, a10, a14, a15, a21, a23, a29, a33, a37, all from the table with its p (the ids a-n are the table's A-n).
- Left out of the seed: K2 (no operation slot, see limits), the 60-day tenure line, ICP and the tax exclusion (rules in force in both worlds; they enter through links and a7).

## Round 1 (14 nodes)

Proposed, with the sentence or assumption each rests on:
- `employers.paying`: alternatives quantity_substitute (A-34, agency workers), hours_worked of existing full-timers (A-11, with R4 overtime above 40), legal_breach (A-18, quarterly offer reporting, misreporting penalty); stake (A-19); asset `owners.paying` and yield (A-21, introduced 9 Nov 2026); links labor -> own output (input), output -> `employers.small` and `employers.capped` (substitute, A-22), -> `consumers` price_paid (supply, A-24), quantity_substitute -> `employers.capped` supply (same_act, A-34, staffing among the 45).
- `employers.offering`: alternative hours_worked (A-11); stake (A-19); asset and yield (A-21); links input -> output, substitute -> `employers.small` (A-22).
- `employers.capped`: stake (A-19).
- `employers.near_threshold`: alternative reclassification (A-17); timing carry_over of employment (A-31, the 2027 average decides 2028); links employment -> `owners.near_threshold` asset_value (yield, A-16), -> `workers.at_near_threshold_firms` (same_act).
- `employers.seasonal`: alternatives reclassification (A-17) and shortened engagements via hours_worked (A-30), both on k3_a.
- `insurers`: stake on k1_offer (A-19).
- `officials.revenue`: link non_tax_receipts -> `treasury` fund_balance (same_act, A-36).
- `workers.at_offering_firms`: alternatives employment at unbound firms (A-8, A-35), part-time, cross-border (A-8; 35,000 commute to Tarnley); margin adjust on `e_off` (new statement, see below); links cover -> individual plans (substitute, A-20), cover -> `sellers.hospital_care` care billed (complement, A-27), cover -> ICP outlay at `treasury` (substitute, A-28, A-32).
- `workers.at_paying_firms`: the same three alternatives (A-8); margin adjust on `e_pay`; stake of `unions` on k1_pay (A-19). The union stake is proposed here because `unions` is not a node until reached.
- `workers.min_wage`: margin adjust on `e_mw`. `workers.near_30_hours`: link hours_worked -> earnings.
- `officials.enforcement`, `taxpayers`, `workers.at_seasonal_firms`: empty (nothing the node needs: the staff are funded as new money, A-29; the seasonal workers' effect is already derived by reading).

Answers (18): 17 from the table (A-19, A-17, A-31, A-16, A-11, A-22, A-34, A-18, A-24, A-30, A-36, A-8, A-35, A-20, A-27, A-28, A-32) with the table p. Judged: "Employers can adjust at least one of hiring, hours, schedules or other benefits for full-timers at bound firms while the wage is fixed." 0.85 (section 1 says wages follow pay scales and the minimum wage; the statement is the margin premise used in WE-009-style records, no table row).

## Round 2 (21 nodes)

Revisits (`#2`) and new nodes reached by round 1 (`employers.small`, three `owners.*`, `sellers.hospital_care`, `treasury`, `unions`, `workers.at_near_threshold_firms`, `workers.at_unbound_firms`, `workers.cross_border`, `workers.part_time`).
- `employers.capped#2`: link output -> `workers.at_capped_firms` employment,hours_worked (input, A-12: they stay above 100 uncovered, so their marginal charge is nil).
- `employers.near_threshold#2`: stake on k3 (A-19); link reclassification -> `contractors` (same_act).
- `employers.offering#2`, `employers.paying#2`: return_on_capital -> investment_target (yield; judged premise "Firms expect the Act to stay in force, as it has no expiry." 0.9, from "It has no expiry."); output -> `input_suppliers` (input); output -> `producers.tarnley` (substitute, A-26); for payers also legal_breach -> `officials.revenue` non_tax_receipts (substitute, A-18).
- `employers.seasonal#2`: reclassification -> `contractors`. `employers.small`: output -> `workers.at_unbound_firms` (input).
- `treasury`: ICP outlay -> `taxpayers` means (substitute: ICP spending and other uses compete for the same funds, CR-8d); fund_balance -> `taxpayers` (same_act, A-36).
- `workers.at_offering_firms#2`: cover -> `insurers` quantity_traded (same_act); individual-plan purchases -> `insurers.individual_market` (same_act); wage_rate -> earnings (yield). `workers.at_paying_firms#2`: wage_rate -> earnings. `workers.min_wage#2`: quantity_traded -> earnings.
- Empty: `insurers#2`, `owners.*`, `sellers.hospital_care`, `unions`, `workers.at_near_threshold_firms`, `workers.at_unbound_firms`, `workers.cross_border`, `workers.part_time`, `workers.near_30_hours#2` (their effects are signed `ambiguous` or have no further market the policy text names; an ambiguous effect does not propagate).

Answers (3): from the table: A-12 (0.9), A-26 (0.65). Judged: the "stay in force" statement (0.9).

## Round 3 (16 nodes)

Dominance (CR-12e), all resting on A-36 (charges collected are not cut by misreporting below $13.5M less the short-run income tax lost, and that tax lost is smaller than the $9.4M by which the capped firms' charges exceed the appropriation): `officials.revenue` non_tax_receipts increase (empirical; opposes the misreporting chain), `treasury` fund_balance increase (arithmetic), `taxpayers` resources_available_other_uses increase (arithmetic; opposes the funded appropriation). Link `producers.tarnley` output -> `workers.cross_border` employment,hours_worked (input; the 35,000 commuters). All other depth-3 nodes: empty lists (diffuse chains, nothing named in section 1). No new questions.

## Where the format could not hold what the policy says

1. **Cap (K4).** `capped_payers` on a charge keeps the per-trade quantity effect (`c_qty` still lowers trades for a payer whose marginal charge is nil), and `basis: operating` signs `number_of_sellers` down, which A-13 denies. So the cap is a `means` fact; the 45 firms' payments to Revenue are then not counted as receipts.
2. **Two branches, one component.** Receipts and receivers are per component, so offer and pay are two components (`k1_offer`, `k1_pay`) and the pay charge is repeated on `e_pay` and `e_mw`. `branch_premises` is a conjunction: A-5 (upgraders) and A-2 (new offerers) are separate routes into the offer branch and cannot be "either/or"; only A-2 is used, and A-5 does not appear.
3. **Sharing a class between chains.** `workers.at_offering_firms` is both receiver (chooser `better`) and wage-loser (chooser `worse`), so its alternatives, and so `workers.at_unbound_firms` employment, come out `ambiguous`. No table row compares the two, so no dominance premise was proposed.
4. **Minimum-wage workers** need their own exchange (`e_mw`) to be fixed in the long run while other wages move in the medium run; they share the employer class with `e_pay`.
5. **Tenure line (60 days).** There is no variable for the length of an engagement; A-30 (p 0.4, so not reported) is carried as an alternative on `hours_worked`.
6. **Delay of growth (A-31).** `timing` signs only the announcement window; "delayed rather than lost" has no later-window consequence.
7. **K2.** The product standard has no operation slot (neither a ban nor a charge); only insurers' `compliance` is recorded, and no effect on plan quality or premiums.
8. **Budget side.** No relation turns `enforcement_cost` or an appropriation into a fall in `fund_balance`; the opposing chain at `taxpayers` is the funded outlay only, settled by a dominance fact on A-36. A fee's `projection_variable` is `tax_revenue_vs_static_projection`, a tax name.
9. **Cost pass-through.** `cost` and `own_price` links need a price as the source, so the employers' burden (`compliance_cost`, `resources_available_other_uses`) cannot be passed to the price of local services; the price chain goes through output instead (`supply`, gated by A-24, p 0.4, so not reported).
10. **Short-run income tax on wages vs the exclusion (R2)** and **Tarnley commuting** enter only as premises of other facts (A-7, A-8); no seed fact holds them.
