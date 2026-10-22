# WE-036 Quenby, expand-loop blind run (loop_r7)

Branch `loop_r7-we036_quenby` from 7890e0e. Read only section 1 and the assumption table (ID, Statement, Type, p); did not open handbook/05_examples*, any other file under cases/we036_quenby/, or tests/. Names were taken from `--vocab --exclude WE-036`. Final output: `final_output.txt`; final situation: `situation.json`.

Result: DONE in 3 rounds (the depth limit), 42 node visits (30 first visits, 12 revisits), 50 proposals, 25 loop questions (plus 14 seed assumptions).

## Seed (CR-1, the policy's own facts)

- Exchanges (employment of full-timers at bound firms), split where the policy treats parts differently: e1 employers.mid_size / workers.uncovered (offered nothing or less than K1; the ~73,000 at ~2,050 mid-size firms); e2 employers.mid_size / workers.min_wage (R1 binds); e3 employers.capped / workers.at_capped_firms (the 45 large firms, K4); e4 employers.seasonal / workers.at_seasonal_firms (the ~380 firms, U1).
- Charges: `k1_offer` (the mandated term, paid in kind to `workers.at_offering_firms`, receipt non_wage_compensation, `quantity_premises` A-7, branch premises A-1+A-2, further set A-1+A-5 for upgraders) and `k1_pay` (the $3,000 alternative to the Department of Revenue, non_tax_receipts, branch A-1+A-4; on e3 also A-12 and `capped_payers` employers.capped for K4). The seasonal-firm versions `k1_offer_seasonal`, `k1_pay_seasonal` (and compliance `k5_seasonal`) belong to reading U1-a only.
- `fixed` (wages above the minimum short, A-3; the minimum wage long, A-9) and `moves` (buyer short A-3, seller medium A-6; e2 buyer long A-9).
- `thresholds`: k3 at 50 FTE for employers.near_threshold (A-14); k1_hours at 30 hours for workers.near_hours_line with employers.mid_size choosing (A-10). `announced` k1 (no premise) and k3 (A-15).
- `unclear` U1 (seasonal workers in the count): U1-a applies the seasonal-firm components, U1-b none. `compliance`/`enforcers` for K5 (Revenue) and K2 (Insurance), `funded` K5 by taxpayers (A-29).
- Left empty: held, grants, capped, banned, expires, qualifies, incidence, alternatives, links, margins, stakes, assets, yields, timing, parts, dominance. Not used: `held` (no price line), `qualifies` (no right allocated by history), `expires` (no expiry).

## Round 1 (13 nodes, 19 questions)

Nodes: employers.mid_size, employers.capped, employers.near_threshold, employers.seasonal, officials.insurance, officials.revenue, taxpayers, workers.uncovered, workers.at_capped_firms, workers.at_offering_firms, workers.at_seasonal_firms, workers.min_wage, workers.near_hours_line.

Proposed:
- employers.mid_size: `adjust` margins on workers.uncovered (e1) and workers.min_wage (e2), because wages are fixed (A-3, R1) and the charge must go to terms the payer controls; `outside` legal_breach on e1, e2 (K5 reporting, "Misreporting: twice the unpaid charge", A-18; none on e3 because a capped firm gains nothing at the margin by misreporting). Alternatives: quantity_substitute via agency workers (A-34), more hours from existing full-timers (A-11, workers.uncovered hours_worked), shorter seasonal engagements (A-30, job_changes). Stakes (A-19). Links: agency input to intermediaries.staffing (A-34); substitute to employers.small (A-22); output to consumers (A-24); cost to producers.tradable (A-26, the Tarnley sentence). Asset e1 owners.mid_size_firms (A-21). Yields e1 (A-3) and e2 (A-9).
- employers.capped: a stake only (A-19). No margin or alternative: A-13 says the cap does not decide operating, and K4 fixes the sum at the margin.
- employers.near_threshold: alternative reclassification (contracting out, A-17); an alternative open only under U1-b (seasonal workers outside the count, premise that 30 to 49 FTE firms can staff seasons with seasonal workers; `reading: "U1-b"`); timing carry_over (K3 status from the 2027 average, A-14, with announced premise A-15); asset e1 owners.near_threshold (A-16); link to workers.prospective employment; a stake.
- employers.seasonal: adjust margin on e4, alternative shorter engagements (A-30), a stake on k3.
- officials.revenue: links paid_from (enforcement cost, appropriation, A-29) and paid_into (charges) to treasury fund_balance, from "A new appropriation of $4.1 million" and "Charges are paid into the general fund".
- workers.uncovered / at_capped_firms: alternatives to employers.small employment and workers.border employment (A-8), job_changes (A-35); incidence on seller side for k1_pay, k1_offer (A-23); link wage_rate yield to treasury tax_revenue (R2).
- workers.at_offering_firms: links to sellers.care (A-27), insurers.individual (substitute, A-20), insurers (same_act, premise that employers buy plans from insurers).
- Empty lists: officials.insurance, taxpayers, workers.at_seasonal_firms, workers.min_wage, workers.near_hours_line (nothing in section 1 or the assumptions says what they can do instead).

Answers: from the table (p as given): A-19 .85, A-18 .55, A-34 .55, A-11 .65, A-30 .4, A-22 .65, A-24 .4, A-26 .65, A-21 .7, A-17 .55, A-16 .6, A-8 .85, A-23 .6, A-27 .75, A-20 .7, A-35 .6. Judged from section 1 (no table row): "Employers can adjust at least one of hiring, hours, schedules, breaks, training or benefits." .9; "Firms with 30 to 49 year-round FTE can staff their seasons with seasonal workers." .8 (the policy describes them as using seasonal workers); "Employers meet the offer with plans bought from insurers." .9 (K2 names insurers and self-insured employers); "Wages are taxed under the 4.5% income tax while employer contributions to health premiums are excluded." .97 (R2 states it).

## Round 2 (20 nodes, 4 new questions)

Nodes reached: employers.small, insurers, insurers.individual, intermediaries.staffing, owners.mid_size_firms, owners.near_threshold, producers.tradable, sellers.care, treasury, workers.border, workers.prospective, workers.seasonal, and the revisits employers.capped#2, mid_size#2, near_threshold#2, seasonal#2, workers.at_capped_firms#2, at_seasonal_firms#2, min_wage#2, uncovered#2.

Proposed: employers.mid_size#2 a link legal_breach substitute officials.revenue non_tax_receipts (misreporting against paying, A-18); employers.near_threshold#2 reclassification same_act contractors employment (A-17); employers.small a supply link to workers.at_small_firms wage_rate (A-37); stakes for insurers and insurers.individual (A-19); producers.tradable links to sellers.foreign (substitute) and workers.export_industries (input), both A-26; sellers.care a substitute link to officials.icp subsidy_outlay (A-28, A-32); treasury a paid_into link from tax_revenue to fund_balance and a dominance fact (fund_balance increase, arithmetic, A-36). Empty: the other nodes and all revisits except the two above.

Answers from the table: A-37 .9, A-28 .7, A-32 .6, A-36 .75.

## Round 3 (9 nodes, 1 new question)

Nodes: contractors, insurers#2, insurers.individual#2, officials.icp, officials.revenue#2, sellers.foreign, treasury#2, workers.at_small_firms, workers.export_industries. Proposed: officials.icp paid_from link to treasury fund_balance (outlay falls, so the balance rises); officials.revenue#2 a dominance fact (non_tax_receipts increase, kind `response`) so that charges against misreporting resolve. Answer judged: "Firms that misreport still pay the charge on some of their uncovered full-timers." .9. The run then stops at depth 3.

## What the output shows (for the caller)

Reported with signs: wage_rate down for workers.uncovered, at_capped_firms, at_small_firms; hours_worked up for workers.uncovered (A-11) and down for workers.near_hours_line; employment down at near-threshold firms (also in the announcement window); non_wage_compensation up for workers.at_offering_firms; treasury fund_balance up (dominance, A-36) and tax_revenue down; officials.revenue non_tax_receipts up; ICP subsidy_outlay down; seasonal-firm results `ambiguous` (they differ by reading). Unreported (`-`): consumers price_paid (A-24 .4) and workers.seasonal job_changes (A-30 .4).

## What the format could not hold

- **A cap that applies to one branch only.** `capped_payers` sits on a charge, so on e3 the offer branch (`k1_offer`) is still charged and employers.capped still shows quantity_traded decrease and price_paid increase, although at the K4 cap the marginal head costs nothing. The seed could not say "capped firms never take the offer branch at the margin".
- **Offsetting chains in one class.** workers.uncovered job_changes shows only increase: the better chain (newly covered workers staying, A-35) has no fact to ride on because the receiver `workers.at_offering_firms` is not a party of an exchange, so no `chooser(..., better)` is derived. The two directions of A-35 cannot both be recorded.
- **Subclass by response.** The charge splits workers into those offered and not offered, but exchanges are by employer, so the offered workers are a receiver class outside any exchange (no wage, no job_changes, no tax_share_borne for them).
- **Existing payer of last resort.** The ICP (R3) pays hospitals for uninsured care; `backstops` need a `held` line, and there is none, so ICP is only a node reached by a link with a `subsidy_outlay` variable invented through `officials.icp`.
- **A product standard (K2).** No operation fits "which plans count"; it is recorded only as an enforcer (officials.insurance), with no effect on insurers' plan design.
- **Lobbying by classes not reached.** A stake is proposed only at the node of the actor that has it; unions, employer associations and the large chains (A-19) are not nodes unless an effect reaches them.
- **Delay rather than loss.** A-31 (growth held back is partly delayed) has no home: `timing` has bring_forward and carry_over inside announcement and deadline windows, not a later catch-up. A-15/A-14 became a carry_over of employment only.
- **A history window that sets status.** 2027 average FTE decides 2028 status. `qualifies` is for an allocated right, so this was handled only through `announced`+`threshold`+`timing`.
- **Actors not in the vocabulary.** Care providers (`sellers.care`), the ICP administrator (`officials.icp`), individual-market insurers (`insurers.individual`), owners of mid-size and near-threshold firms and workers at small firms are role.qualifier names built from listed roles; `hospitals` was off-list and replaced.
- **Premises that need more than a yes or no.** A-36 mixes three figures ($13.5M, $9.4M, short-run tax lost) in one premise; it is used as one arithmetic dominance premise for fund_balance only, and a separate response premise was written for non_tax_receipts.
- **Size ratios.** The $2.49 and $3.32 per hour against the $1.44 and $1.92 penalty (play against pay) are not holdable; the loop uses only the existence of both branches (A-2, A-4, A-5).
- **Readings.** Only U1 is a reading. The alternative for firms near 50 under U1-b is tied to it; under U1-a the seasonal firms' components are the only difference, so the near-threshold count rule (seasonal hours push firms over 50) has no separate fact.
- **Judged answers.** Five of the 25 answers were judged, not taken from the table (listed above).
