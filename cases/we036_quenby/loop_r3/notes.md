# WE-036 Quenby, expand-loop blind run (loop_r3)

Inputs read: section 1 of the example (saved as `policy.txt`) and the ID / Statement / Type / p columns of its assumption table. Nothing else of the example, no `05_examples_core/`, no existing file for this case. Ids `a<n>` in the files are the table's `A-<n>`; classes are the table's Type column.

Result: DONE in 3 rounds (round 3 reached only nodes already proposed for, so it added nothing), 19 nodes proposed for (10 in round 1, 9 in round 2), 19 premise questions asked, 32 assumptions in the final situation (13 in the seed, 19 from the loop). Engine output: `final_output.txt` (40 reported consequences, none unreported).

## Seed (CR-1: the policy's own facts)

One exchange `e_work` (employers.bound buy full-time labour from workers.at_bound_firms; seller price `wage_rate`). Components: k1_play, k1_pay (the two branches of K1), k3 (50 FTE line), k1_hours (30-hour line), k3_seasonal (U1-a only), k5 (enforcement), k2 (certification).

- `charges`: k1_play is the mandated term paid in kind, so its receiver is `workers.at_offering_firms` (non_wage_compensation), `branch_premises` a2 (some bound firms that offer nothing now choose to offer), `quantity_premises` a7 (cover at 30% is worth less to the marginal worker than it costs). k1_pay is the $3,000 charge to the Department of Revenue (`officials.revenue`, non_tax_receipts), `branch_premises` a4 (some bound firms pay), `capped_payers` employers.capped (K4, $300,000 cap).
- `fixed` on the seller side of e_work, twice with one premise each (a9: the minimum wage R1 binds for some; a3: wages are sticky in the short run), because they are independent grounds. `moves` on the seller side with a6 (raises can adjust over the medium horizon) and a37 (workers cannot all move to unbound work, the response is partial).
- `thresholds`: k3 (employers.near_line, employment, a14), k1_hours (workers.near_30_hours, hours_worked, chosen by employers.bound, a10), k3_seasonal (employers.seasonal, a33 and a14).
- `unclear` U1: U1-a lists k3_seasonal, U1-b lists nothing (the text gives no operation to record under "seasonal workers are left out").
- `announced` k3 (a15), k1_play and k1_pay (a21). `compliance` k5 on employers.bound; `enforcers` k5 officials.revenue and k2 officials.insurance; `funded` k5 taxpayers (a29).
- Not in the seed because the policy does none of it: held, capped, banned, grants, backstops, means, expires (the Act has no expiry), qualifies, discretion, transfers.

First run: 10 nodes pending (employers.bound, employers.capped, employers.near_line, employers.seasonal, officials.insurance, officials.revenue, taxpayers, workers.at_bound_firms, workers.at_offering_firms, workers.near_30_hours).

## Round 1 (10 nodes)

- employers.bound (compliance cost up, trades down, means down). Alternatives to paying for each uncovered full-timer: extra hours from existing full-timers (alt to workers.at_bound_firms hours_worked, a11), contracting out and franchising (reclassification, a17, "Firms under common control are counted together"), shortening engagements below the 60-day offer rule (reclassification, a30), agency workers (alt to staffing.agencies, a34, "Agency workers count for the agency"). Margin `outside` legal_breach (a18, misreported offer status). Margin `adjust` on workers.at_bound_firms (employment, hours_worked, non_wage_compensation) because the wage is fixed, with a judged premise. Stake k1_pay (a19). Asset owners.bound_firms (a21, introduced Nov 2026, takes effect 2028). Yield of employers.bound (a3: sticky wages leave the charge with the employer in the short run). Link `input` from labour hired to quantity_supplied (judged premise).
- employers.capped: stake only (a19). A-12 and A-13 say the cap binds and does not decide staying, so no alternative; the cap is the seed's `capped_payers`.
- employers.near_line: reclassification (a17), asset owners.near_line_firms (a16, a14), timing carry_over of employment in 2027 (judged premise; `announced` k3 with a15), link `same_act` to workers.at_near_line_firms employment (no premise, an identity).
- employers.seasonal: reclassification under k3_seasonal (a17).
- officials.revenue: link non_tax_receipts to taxpayers' means (no premise: "Charges are paid into the general fund").
- taxpayers: `dominance` increase on resources_available_other_uses, kind arithmetic, premise a36. It rests on the funded appropriation against charges paid into the same fund, and on the income tax lost (CR-8 1.0, CR-12e).
- workers.at_bound_firms: alternative to workers.at_unbound_firms employment (a8, Tarnley commuters), stake k1_play (a19, unions), link wage_rate to officials.revenue tax_revenue (judged premise: R2 excludes cover from the 4.5% income tax).
- workers.at_offering_firms: `parts` (offering part of bound workers); links to insurers.individual_market (substitute, a20), providers.health_care (complement, a27), officials.icp (substitute, a28 and a32), insurers.group (same_act, judged premise); alternative job_changes (a35, see "could not hold").
- officials.insurance: empty. workers.near_30_hours: I first proposed an alternative on hours_worked; it made the class ambiguous against the threshold already in the seed (a10), so I removed it before the final run and left an empty list (the threshold is the rescheduling).

## Round 2 (9 nodes)

- insurers.group and insurers.individual_market: stake k1_play each (a19, insurers).
- officials.icp: link subsidy_outlay to taxpayers' means (same_act, no premise).
- workers.at_unbound_firms: link `supply` from employment to its wage_rate (a6, wages above the minimum adjust in the medium run).
- owners.bound_firms, owners.near_line_firms, providers.health_care, staffing.agencies, workers.at_near_line_firms: empty lists (nothing the policy text or the table supports without invention).

## Round 3

Frontier was revisits only (officials.revenue, taxpayers, workers.at_unbound_firms had new effects, all already keyed); no node lacked a proposal list, so the run printed DONE.

## Answers

From the table (p as given): the 13 seed assumptions a2, a3, a4, a6, a7, a9, a10, a14, a15, a21, a29, a33, a37, and 14 of the loop's 19 questions: a8, a11, a16, a17, a18, a19, a20, a27, a28, a30, a32, a34, a35, a36. The other 5 were judged. (Four table statements, a3, a6, a14 and a21, are used by both the seed and proposals and were not asked again.)

Judged (not in the table):
- "Employers whose cost of labour rises hold back hiring, hours or other benefits where the wage cannot be cut." 0.85 (CR-6 pressure goes to the terms the payer controls; fixed minimum wage).
- "Bound firms cannot replace the full-time labour they stop hiring with other inputs at the old cost." 0.75 (partial substitution, A-10, A-11, A-34 admit some).
- "Firms near 50 hold hiring back during 2027 to keep their 2027 average below 50." 0.7 (tracks a14 0.7 and a15 0.75).
- "Employer contributions to premiums are excluded from the employee's income tax while wages are taxed." 0.95 (stated in section 1, R2).
- "Most of the cover employers provide is bought from insurers." 0.8 (K2 names insurers and self-insured employers).

## What the format could not hold

1. A node reached again by a later effect cannot be given new proposals. `FileProposer` returns the same list for every visit of an actor and `expand` skips facts already added, and the PENDING listing only names nodes missing from the file. So follow-ups that a proposer called at the revisit would add are absent: employers.bound after "quantity_supplied decrease" (supply link to a local-services price with a24; substitute links to unbound firms with a22 and to Tarnley producers with a26), and officials.revenue after "tax_revenue decrease" (a link to taxpayers' means, which a36 needs to be a real netting). The first is left dangling (quantity_supplied falls and goes nowhere); the second is covered only by the receipts and ICP links plus the arithmetic dominance on taxpayers.
2. A charge receiver that is a subclass (workers.at_offering_firms) gets no "better" chooser, because `chooser(C, R, better)` needs R to be a party of the exchange. The a35 alternative (newly covered workers near the stay-or-move margin, job_changes) therefore never fires. The `parts` link to workers.at_bound_firms moves only the class total of non_wage_compensation, where the gross gain to offering firms' workers and the fall in other terms (the `adjust` group) are separate items; a wage fall that lands on the whole class and the in-kind gain that lands on a part cannot be netted for the part.
3. A reading that exempts (U1-b: seasonal workers left out) has no operation to record, so its components list is empty and the engine reports "none" for it. The exemption is an option added (CR-1 op 2) that no part can state.
4. The K2 benefit standard (a product standard on plans) and the 60-day wait have no part type; only the enforcer and certification cost of K2 is in the seed.
5. `capped_payers` carries no premise, so a12 ("the 45 capped firms stay above 100 uncovered full-timers") cannot be attached to the cap; the cap is unconditional in the engine.
6. Incidence shares (a23, workers' alternatives worse than employers' over the medium run; `tax_share_borne`) and delayed-not-lost growth (a31, persistence) have no part: dominance only settles a sign, not a ranking of shares.
7. `thresholds` for the hours line takes a chooser but the 30-hour line is also a notch on the whole base (cover for all hours above it); only the fall in hours near the line is derived.
8. Two charges on one exchange (play and pay) are run as additive wedges; the choice between them (the employer pays only the cheaper) is held only through `branch_premises`, not as one option set.
