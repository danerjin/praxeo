# WE-036 Quenby, expand loop, blind run loop_r5

Branch `loop_r5-we036_quenby` (from 10e031e). Files: `seed.json`, `proposals.json`, `answers.json`, `situation.json`, `policy.txt` (section 1 as given). Result: DONE in 3 rounds, 39 node visits, 22 questions asked (5 judged, 17 taken from the assumption table). No `off-list:` lines in the final run.

## Seed (the policy's own facts, CR-1)

- Exchanges: e1 employers.bound / workers.fulltime_bound (K1 target, wage_rate on the seller side); e2 employers.bound / workers.min_wage (R1 binds); e3 employers.seasonal / workers.at_seasonal_firms (the ~380 firms of 30 to 49 year-round FTE, who are bound only if seasonal hours count).
- Charges, one pair per exchange, K1 being a choice between two branches: `k1_offer` (the mandated term paid in kind, receiver workers.at_offering_firms, non_wage_compensation, `quantity_premises` A-7, `branch_premises` A-1, A-2) and `k1_pay` (the $3,000 charge to officials.revenue, non_tax_receipts with the static-projection shortfall, `branch_premises` A-1, A-4, `capped_payers` employers.capped for K4). On e3 the components are `k1_offer_seasonal` / `k1_pay_seasonal` (branch premise A-33 for the pay branch).
- `fixed`: e1 seller (A-3 sticky pay), e2 seller (A-9 minimum wage R1), e3 seller (A-3). `moves`: e1, e3 seller (A-6, A-37).
- `thresholds`: k3 (employers.near_threshold, employment, A-14); k3_seasonal (employers.seasonal, A-14); k1_hours (the 30-hour line: workers.near_hours_line, hours_worked, chooser employers.bound, A-10).
- `unclear` U1: U1-a lists the seasonal-firm components (k1_offer_seasonal, k1_pay_seasonal, k3_seasonal, k5_seasonal); U1-b lists none (the firms are not bound).
- `announced`: k3 (A-15), k1_offer and k1_pay (A-21). `compliance`: k5 employers.bound, k5_seasonal employers.seasonal, k2 insurers. `enforcers`: k5 officials.revenue, k2 officials.insurance. `funded`: k5 by taxpayers (A-29).
- Not in the seed because the section has no such fact: held, grants, capped, banned, expires ("no expiry"), qualifies, backstops, discretion, means, early_price, transfers, fixed_budget. R2 to R4 were left to the loop (they are existing rules, not components).

## Round 1 (13 nodes)

Proposals (each rests on the quoted part of section 1 or on the assumption named):
- employers.bound: adjust margins on e1 (workers.fulltime_bound) and e2 (workers.min_wage) over employment and non_wage_compensation (the payer's open terms when pay is fixed; hours_worked left out of the group because A-11 moves it up separately); outside margin `legal_breach` (K5 misreporting, A-18); alternatives under k1_pay to part-time work (A-10), agency workers (A-34), upgraded plans bought from insurers (A-5), shorter seasonal engagements (A-30); stake (A-19); yield (cannot pass the charge on, judged from A-22 against A-24); asset of owners.bound (A-21); links output to labour hired (judged), then substitute to employers.small (A-22) and neighboring_jurisdictions (A-26).
- employers.capped: stake (A-19, K4 cap).
- employers.near_threshold: alternative contracting out (A-17); timing carry_over of employment in 2027 (A-31, with k3 announced A-15); stake (A-19); asset of owners.near_threshold (A-16); same_act link to workers.prospective.
- employers.seasonal: adjust margin on e3; alternatives under k3_seasonal: contractors (A-17), cutting seasonal hours (A-14); stake (A-19).
- insurers: stake (A-19). workers.at_offering_firms: links to care sold (A-27), ICP outlay (A-28, A-32), individual plans (A-20), income tax revenue (R2 and A-6). workers.at_seasonal_firms and workers.fulltime_bound: alternatives to employers.small, workers.part_time, neighboring_jurisdictions (A-8); A-11 link of fewer full-time heads to more hours per head. workers.near_hours_line: earnings follow hours (A-3). officials.revenue: link of receipts to the treasury's fund_balance (K5, general fund).
- Empty lists: officials.insurance, taxpayers, workers.min_wage.

Pass-through: the officials.revenue link was first left out of round 1 and added on a later pass over round 1 (the files are replayed from the seed each run); the other round-1 lists were not changed after seeing round 2.

## Round 2 (22 nodes)

Real proposals only at: employers.bound#2 (misreporting lowers receipts, A-18); employers.small (more employment there lowers wages at workers.at_small_firms, supply relation, A-37); officials.indigent_care (lower outlay raises the fund balance, judged premise that ICP is paid from the general fund, section 1 R3); treasury (lost income tax lowers fund_balance, same_act); workers.agency (same_act with employers.capped). Empty for the rest (contractors, capped, near_threshold, seasonal, small insurers, owners, health care, part-time, prospective, seasonal workers, min-wage workers): terminal effects with nothing in section 1 to carry them on.

## Round 3 (4 nodes)

Two dominance facts, the only places the section gives a premise that one direction outweighs another: officials.revenue non_tax_receipts increase (kind response, A-36: misreporting does not cut collections below $13.5 million less the tax lost) and treasury fund_balance increase (kind arithmetic, A-36: tax lost is smaller than the $9.4 million by which capped firms' charges exceed the appropriation). employers.capped#3 and workers.at_small_firms: empty.

## Answers

Taken from the table (17 asked): A-5 0.7, A-8 0.85, A-11 0.65, A-16 0.6, A-17 0.55, A-18 0.55, A-19 0.85, A-20 0.7, A-22 0.65, A-26 0.65, A-27 0.75, A-28 0.7, A-30 0.4, A-31 0.6, A-32 0.6, A-34 0.55, A-36 0.75. The premises used by the seed facts (A-1 to A-4, A-6, A-7, A-9, A-10, A-14, A-15, A-21, A-29, A-33, A-37) carry their table values in the seed and were not asked again.
Judged (5), each from section 1:
- "Employers control the headcount and the non-wage terms of their full-timers." 0.9 (at-will employment; the mandated term).
- "Bound firms cannot pass the whole charge on to their customers." 0.65 (A-22 unbound rivals against A-24 at 0.4).
- "The output of bound firms moves with the labour they hire." 0.8.
- "Employer contributions to health premiums are excluded from taxable income, while wages are taxed." 0.95 (R2).
- "The Indigent Care Program is paid from the general fund." 0.95 (R3).

A-30 (0.4) and A-24 (0.4) fall below the 0.5 cut-off. A-30 sits under the alternative "shorter seasonal engagements", so workers.seasonal turnover is derived but not reported; A-24 was not usable (see below).

## What the format could not hold

- No horizon on `fixed` and `moves`: A-3 (pay fixed in the short run) and A-6 (wages adjust in the medium run) are both seeded for e1, so the run reports a wage fall and a squeeze on non-wage terms together, with no way to say which belongs to which period.
- `capped_payers` has no premise (A-12, A-13), and the engine still signs a fall in trades for the capped firms from the pay charge; a capped firm's marginal pay cost is zero, which the record cannot express except by a separate exchange.
- A charge's receiver subclass (workers.at_offering_firms) is not a party of the exchange, so no `chooser(better)` arises for it; A-35 (newly covered workers near the margin between staying and moving) cannot be used, and nothing says whether newly covered workers stay more.
- Only actors an effect reaches get a node: unions (named in A-19) are never reached, so their stake cannot be proposed.
- Assets are tied to an exchange side. The assets of firms near 50 (A-16) are tied to the e1 buyer side, which they are not yet on; the sign is the intended one.
- No price source for employers: with only `wage_rate` set as price variable, the product-price link (A-24: most competitors are bound) has no source effect, so I used a quantity chain (labour hired to output to rivals' output) instead; pass-through of cost to product prices is lost.
- Incidence shares (A-23 workers' alternatives worse than employers') have a variable (`tax_share_borne`) but no rule; nothing derives it.
- R2 (tax exclusion), R3 (ICP) and R4 (overtime) are existing rules with no slot: they entered only as premises of links (R2 via a judged statement, R3 via a judged statement, R4 only in the `source` of the A-11 link).
- The notch at 50 FTE and the 130-hours count are held as thresholds only; the 1,100 firms already at 50 to 60 are "those near the line" on the other side, which the threshold fact (actors below the line) does not distinguish.
- Under U1 the seasonal firms show `ambiguous` per reading in the printed output; the by-reading signs are in `situation.json` through the engine, not printed by the CLI.
