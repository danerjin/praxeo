# WE-061 Lanvik, expand loop, blind run (notes)

Inputs read: section 1 and the assumption table only. Branch `loop-we061_lanvik` from c2e834f. Final engine output: `final_output.txt` (DONE in 3 rounds, 23 questions, 62 reported lines, 0 off-list). Seed ids are lower-case `a<N>` for table rows A-N and `j1` for one judged premise (clingo needs lower-case atom ids).

## Seed (policy's own facts, CR-1)
- Exchanges: `e_min` (platforms.covered buy engaged time from workers.min_wage, the employees the floor binds on; unsatisfied: workers.prospective; criteria allocation_by_non_price_criteria, wait_time), `e_emp` (same buyer, workers.employees: the rest of the employees), `e_con` (contractors.agreement), `e_off` (contractors.no_agreement: the contractor form without a valid agreement), `e_svc` (customers buy rides/deliveries from platforms.covered).
- K1 as `banned` on `e_off` (a1: enforced); K5 restores the option through the agreement. `threshold` k1 for platforms.near_threshold (employment; a15).
- K2 as `held` above on `e_min`, one component per reading: k2_a (a3, a1), k2_b (j1, a1); `unclear` U1 maps readings to them. `fixed` e_min seller long (a3); `transfers` e_min; criterion margin (a31).
- K3 overtime: charge on `e_emp` paid to workers.full_time (receipt wage_rate; quantity premise a17) and threshold at 40 hours (chooser platforms.covered). K4: charge on `e_min` and `e_emp` to officials.revenue (tax_revenue), threshold on earnings for workers.part_time (chooser platforms.covered; a18). K5: charge on `e_con`, receiver contractors.agreement, non_wage_compensation, quantity premise a4, branch premise a2.
- Fare shares: `fixed` seller short (a29) and `moves` seller medium (a28) on e_emp and e_con. `announced` k4, k5 (a11). K6: enforcers, funded (taxpayers, a26), compliance k1, k5.
- Table premises used in the seed: a1, a2, a3, a4, a11, a15, a17, a18, a26, a28, a29, a31 (p from the table). Judged: j1 ("Some hours logged in pay below 16 per hour logged in (about three quarters)", 0.95: section 1 arithmetic for U1-b).

## Round 1 (12 nodes)
- platforms.covered: alternatives k1 reclassification (a8, §3 conditions); k4 steering to contractors (a7); k2_b scheduling cuts paid waiting, `inverse`, reading U1-b (a6); outside margin e_off legal_breach (a19); links to customers and retailers.restaurants price_paid (output; a4), to officials.enforcement non_tax_receipts (a19, a1); stake k1 (a16); yield e_emp (j4); asset owners.shares (a11).
- contractors.agreement: alternative to employee status (j3); adjust margin e_con (j2); three same_act links into earnings (identity, no premise) and a dominance fact (a25).
- contractors.no_agreement: alternatives sign the agreement (a2), become employees (a5), one-person companies (a9).
- officials.enforcement: paid_from general_fund (a26). officials.revenue: paid_into treasury (j5). platforms.near_threshold: reclassification (a15). taxpayers: [].
- workers.employees: adjust margin (j2); Selvane hours (a14); benefit claims as an `inverse` alternative on treasury fund_balance (a20); stake (a16). workers.full_time: substitute link to other companies' hours (j6). workers.min_wage: adjust margin (j2); contractor choice per reading (a5; a23 under U1-b). workers.part_time: split hours over companies (j7). workers.prospective: entry as contractors (a24) and Selvane (a14), per reading.
- From table: a5, a6, a7, a8, a9, a14, a16, a19, a20, a23, a24, a25 (as given). Judged from section 1: j2 dispatch controls hours 0.9; j3 some prefer the agreement (premium about 3.00 an hour on a trip, flexibility kept) 0.85; j4 platforms do not recover all added cost (a4 says "part") 0.85; j5 contributions go to the insurance funds (§7) 0.95; j6 capped workers take hours from another company (45% multi-home) 0.7; j7 split hours to stay under 150 (45% multi-home, 24,000 earn under 150 from a platform) 0.65.

## Round 2 (13 nodes)
customers (own_price to quantity_demanded, same_act to platforms.covered quantity_traded, taxi and home-production and small-courier alternatives, same_act to customers.no_substitute: a4, a10, a15, a30); retailers.restaurants (own_price a12; own couriers a13); contractors.agreement#2 (entry same_act employment a24; entry `supply` earnings j8; stake a16); platforms.covered#2 (input links to the three worker classes' employment,hours_worked a4; yield to investment_target a11). Empty: general_fund, owners.shares, treasury, officials.enforcement#2, platforms.near_threshold#2, contractors.no_agreement#2, workers.employees#2, workers.min_wage#2, workers.uncovered. Table: a4, a10, a12, a13, a15, a16, a24, a30, a11; judged: j8 (new contractors share the same requests) 0.8.

## Round 3 (10 nodes)
drivers.taxi: yield link to owners.medallions asset_value (a10, a11). The other nine nodes: [] (nothing needed that section 1 supports).

## Corrections made during the run
- The three earnings links were first written with a25 as their premise (a mistake: the dominance premise belongs on the dominance fact); with p 0.35 the chain was cut and earnings read `decrease`. Fixed to no premise; earnings is now ambiguous (a25 below 0.5 settles nothing).
- The U1-b scheduling alternative first had no `inverse`, which made hours_worked rise; fixed (scheduling cuts paid hours).

## What the format could not hold
- Exchanges can only be seeded, so taxis (fares fixed by the city, medallion cap) and restaurants as a payer of fees could not be exchanges: no `fixed`/`capped` on the taxi fare, no `asset` on medallions (a link `yield` stands in), and no charge on `e_svc` to carry the pass-through (done by an `output` link) or to put incidence (a30) on riders against platforms.
- K1's two operations (option removed, restored at the worker's election) are only a `banned` exchange plus the K5 branch; the worker's election and the "default screen" duty have no field. Overtime (a premium rate on hours above 40) is a charge plus a threshold, not a rate.
- Benefit eligibility from insured wages (a20) is only an `inverse` alternative; no relation says "claims rise when hours fall".
- A wage notch (K4 at 150 in a week) is a threshold on `earnings`, with no cost-of-crossing size.
- Table rows A-10 (taxi idle capacity), A-24 (a four-to-six-week lag) and A-29 (30 days' notice) carry timing the format only holds as horizons.
- Premises answered 0.5 or lower leave their facts cut off (a8 at 0.5 counts as held; a25 at 0.35 does not).
