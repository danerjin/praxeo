# WE-029 Varrow Healthy Workplaces Act, expand loop, blind run (loop_r2)

Branch `loop_r2-we029_varrow` (from 7890e0e). Files: `seed.json`, `proposals.json`, `answers.json`, `policy.txt` (section 1 as given), `situation.json` (grown situation), `final_output.txt` (engine output of the last run).
Read: section 1 and the assumption table (ID, Statement, Type, p), the core rules, situation.py, expand.py, core.lp, the vocabulary list, WE-009/WE-013/WE-001 records and the WE-012 loop seed and notes (style for `capped_payers`, `fixed`/`moves`). Not opened: handbook/05_examples*, anything else under cases/we029_varrow, tests/.

Result: `DONE in 3 rounds, 15 questions`; 28 node visits (8 + 13 + 7); no `off-list:` lines. The situation holds 27 assumptions (12 in the seed, 15 asked). 40 proposed facts (12 alternatives, 20 links, 3 margins, 3 stakes, 1 asset, 1 yield, 2 timing, 0 dominance). Process note: I wrote each round's proposals after reading the PENDING list of the round before, but kept them in one generator script and regenerated the two files each time, so every round's answers were written together with its proposals (the statements are the table's own wording).

## Seed (CR-1: the policy's own facts)

- Exchanges. `e1`: employers.covered buy labour from workers.uncovered (employees above the minimum; buyer `price_paid`, seller `wage_rate`). `e2`: employers.covered buy from workers.min_wage (R1, a rule in force, "about 9% earn at or near" it; A-7). The split follows the text: the minimum wage cannot move; other wages can move when raises are set. No held price, no unsatisfied side, no criteria (no price line).
- `charges` K1 on e1 and e2 (payer buyer; receiver the workers, `non_wage_compensation`: the mandated term is paid in kind to the counterparty). `quantity_premises` A-6 (the fall in trades rests on the term being worth less to the worker than it costs). `branch_premises` A-1, A-2 (binding and compliance), and a second set A-12, A-2 (employers whose PTO falls short of K2 and must upgrade): the K4 exemption gives the payer a choice (own equivalent policy or K1). `capped_payers` employers.full_time: accrual stops at 40 hours a year, so for staff past about 1,200 hours the employer pays a fixed sum (CR-1 0.9).
- Charge `k3_2027` (same payers and receivers, same premises): carry-over of 2027 hours into 2028. It is the component only U1-a applies (U1-b: it does not).
- `unclear`. U1 (carry-over in the first year): U1-a applies `k3_2027`, U1-b does not. U2 (counting for K5): U2-a applies `k5a`, U2-b applies `k5b` (below).
- `thresholds`. `k5a` (every person counts): employers.near_threshold hold `employment` below the line, premise A-10. `k5b` (only those averaging 20 hours count): the line is on part-timers' `hours_worked` (workers.part_time), and the employers set them (`chooser` employers.near_threshold), premises A-10, A-8.
- `fixed`: e1 seller short (A-3: pay scales, annual raises and agreements); e2 seller long (A-7: the minimum wage binds). `moves`: e1 buyer short (A-3: employers' cost takes the term while wages are fixed), e1 seller medium (A-5: raises get set), e2 buyer long (A-7).
- `incidence`: k1 on e1, workers (seller) side, A-22 (their alternatives are clearly worse).
- `announced`: k1 (signed May 2026, effective January 2027; no premise, as in WE-012/013), k5a and k5b (A-25: firms near six employees know the 2026 average decides).
- `compliance` k6 employers.covered (notice, three years of records); `enforcers` k6 officials.enforcement; `funded` k6 taxpayers (A-20: new money from the general fund).
- Not seeded, with reason: held (the policy fixes no price; R1 is `fixed`), grants, capped, banned, backstops, discretion, means, qualifies (no right allocated by history), expires ("no expiry"), early_price, transfers, `basis: operating`.

## Round 1 (8 nodes at depth 1)

- employers.covered: adjust margins on e1 and e2 (employment, hours_worked; A-8, since the wage is fixed) ; outside margin `legal_breach` on e1 (A-16, complaint-only enforcement, K6); alternatives under k1: `reclassification` (A-11; K1 exempts contractors, R2 enforced on complaint), `quantity_substitute` (A-19; K2: no replacement requirement, shifts covered via agencies), full-time `hours_worked` (A-8; the 40-hour cap makes full-time hours cheaper than part-time), workers.uncovered `job_changes` (A-23; ending engagements before the 90 days), workers.uncovered `allocation_by_non_price_criteria` (A-9; screening applicants by expected use); links: quantity_substitute input to intermediaries (A-19), price_paid output to consumers (A-17), price_paid cost to export_industries `quantity_supplied` (A-18, Pellam), price_paid substitute to employers.small `quantity_supplied` (A-13, K4/K5 exempt firms), `legal_breach` same_act to officials.enforcement `non_tax_receipts` (A-21, K6 penalty) and to workers.uncovered `resources_available_other_uses` (A-21, K6 back pay plus equal damages); stake in k1 (A-14); asset on e1 buyer side held by `owners` (A-24); yield for employers.covered on e1 (A-3, A-6).
- employers.near_threshold: `reclassification` under k5a and under k5b (A-11); under k5b an alternative open only under U2-b (`reading: "U2-b"`): more part-timers, `employment` of workers.part_time (A-8); timing carry_over of `employment` under k5a and k5b (A-10; announced in the seed with A-25); link `employment` input to workers.prospective `employment,hours_worked` (A-10).
- workers.min_wage: alternatives job_changes (A-15) and hours_worked (A-4); link non_wage_compensation same_act to `earnings` (A-26: unpaid absences become paid); stake (A-14, unions).
- workers.uncovered: the same two alternatives and the A-26 link, stake; link wage_rate same_act to earnings (no premise: earnings are wage times hours times employment), which sets the money wage fall against the A-26 gain.
- workers.part_time: link hours_worked substitute to workers.full_time hours_worked (A-8).
- Empty lists: employers.full_time (a capped payer: a fixed sum, and it is not a party, so it is no chooser), officials.enforcement (funded and enforcing; nothing more in section 1), taxpayers.

## Round 2 (13 nodes at depth 2)

- consumers: price_paid substitute to consumers.border `cross_border_purchases` (judged premise, below).
- employers.covered#2: return_on_capital yield to `investment_target` (A-24); reclassification same_act to workers.contractors `employment` (A-11).
- employers.near_threshold#2: reclassification same_act to workers.contractors employment (A-11).
- employers.small: quantity_supplied input to workers.small_firms `employment,hours_worked` (A-13).
- export_industries: quantity_supplied input to workers.export_industries (A-18).
- intermediaries: quantity_traded input to workers.agency_on_call (A-19).
- officials.enforcement#2: enforcement_cost paid_from general_fund `fund_balance` (A-20).
- Empty: owners, workers.full_time, workers.min_wage#2, workers.part_time#2, workers.prospective, workers.uncovered#2 (terminal effects; nothing in section 1 or the table to carry them on).

## Round 3 (7 nodes at depth 3)

- consumers.border: cross_border_purchases substitute to retailers `quantity_traded` (judged premise).
- Empty: employers.covered#3, general_fund, workers.agency_on_call, workers.contractors, workers.export_industries, workers.small_firms.

## Answers

14 of the 15 asked statements are the table's own wording and took its p: A-16 0.8, A-11 0.55, A-19 0.65, A-23 0.4, A-9 0.55, A-17 0.7, A-18 0.65, A-13 0.6, A-21 0.85, A-14 0.85, A-24 0.7, A-15 0.55, A-4 0.9, A-26 0.95. The 12 seed premises (A-1, A-2, A-3, A-5, A-6, A-7, A-8, A-10, A-12, A-20, A-22, A-25) took the table's p and were not asked again.
Judged (1): "Fenmouth residents can buy goods and services across the river in Pellam." p 0.6, from section 1 (Fenmouth lies on the river border with Pellam, no sick leave law there; about 40,000 commute across daily), lowered because A-17 says most local service competitors are bound too.
Table statements not used: A-20 is in the seed; none left over.
A-23 (0.4) is below the 0.5 cut-off, yet `job_changes` of workers.uncovered is reported `ambiguous`: the engine counts the chain with a premise set that clears (A-15 down, and the workers' own alternative opened by their wage fall, see below) against A-23's.

## Final output (signs of note)

- Per reading: employers.near_threshold `employment` ambiguous overall, U2-a decrease / U2-b none; workers.part_time `employment` U2-b increase, `hours_worked` U2-b decrease; workers.prospective `employment,hours_worked` U2-a at_least_one_decrease. U1 gives no sign difference: `k3_2027` repeats the chains k1 already derives.
- Ambiguous (opposite chains, no dominance premise proposed): workers.uncovered `earnings` (A-26 paid absences against the fall in the money wage), `hours_worked` (A-4: paid absence lowers hours, against the same workers' alternative opened by their medium-run wage fall, where the engine makes a seller whose wage fell a chooser who is made worse), `job_changes` (A-15 down against A-23 and the same wage-fall chooser).

## What the format could not hold

- A charge has no binding or enforcement premise of its own: A-1/A-2 sit in `branch_premises`, which is meant for "some payers take the branch". The branch reading is true here (K4 lets the employer provide its own policy), but the premise set mixes binding and enforcement into it.
- Dating. K3 is enforced only from 1 January 2028, K2 use opens after 90 days (existing staff from 1 April 2027), K1 accrues from 1 January 2027: the format has one `announced` date and no per-component start, so U1 shows up only as a component that repeats k1. The U1-b exempt alternative (let 2027 hours lapse) has no variable in the controlled list that measures it, so it was not proposed; U1 therefore gives no sign difference.
- The 40-hour accrual cap: `capped_payers` loses means only and leaves `quantity_traded` down for the exchange's parties; it cannot say that full-time staff cost the employer nothing more per hour past the cap. The part-time/full-time split needs separate seller classes on the exchange, which I did not make (e1 mixes them), so the cap reaches the exchange only through employers.full_time and the A-8 alternative.
- Exempt-form choices. K4 (own equivalent policy) is a branch of the charge, K5 a threshold; neither gives an exempt exchange of its own, so the small and equivalent-PTO employers appear only as link targets (employers.small).
- Employees below the line under U2 are counted by headcount (k5a) or by hours (k5b); the threshold actor/variable pair differs by reading, but the `unclear` components list is the only place that ties them.
- Cross-border labour and employers' move to Pellam (A-22, 40,000 commuters) have no variable (`relocation_out_of_area` is for members' homes), so only the incidence rank (A-22) carries it.
- Worker classes reached through a link (contractors, small firms, agency staff, export workers) get an `employment,hours_worked` group or a single `employment`, never a wage.
- Retailers and consumers: the supply response of exempt small firms (a price-restraining chain against the consumers' price rise) would need a dominance premise of kind `response` and a "cost per unit does not fall" statement, absent from the table; I left the consumers' price rise unopposed.
- Hard-to-police use (A-4) and unpaid absences (A-26) are two different responses of a worker to a paid term (work while ill; absence that was unpaid); the controlled list has no variable for "working while ill" or "unpaid absence", so A-4 is on `hours_worked` and A-26 on `earnings`.
