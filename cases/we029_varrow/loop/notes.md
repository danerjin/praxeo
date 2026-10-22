# WE-029 Varrow Healthy Workplaces Act: expand loop, blind run

Inputs read: section 1 of the policy record, the assumption table (ID | Statement | Type | p), the core rules, the engine files, and the
worked situations we001, we009 and we013 (only we009 and we001 in detail). Not read: handbook/05_examples*, tests/, any existing
file under cases/we029_varrow/. Slip to report: I ran `ls cases/we029_varrow` once while checking the folder existed and saw three file
names (answers.json, policy.txt, record.json); I did not open them.

Result: DONE in 3 rounds, 30 node visits, 17 questions (13 answered from the table, 4 judged). No `off-list:` lines.

## Seed (policy's own facts, CR-1)

- Exchanges (employment contract): e1 employers.covered / workers.uncovered (uncovered, wage above the floor); e2 employers.covered /
  workers.min_wage (uncovered at the floor); e3 employers.pto_gap / workers.pto_gap (existing PTO that fails the K2 conditions, K4).
  Seller price variable wage_rate; buyer price variable price_paid (the employer's full hourly cost including the term).
- charges: k1 (accrual and pay, mandated term paid in kind to the worker, receipt non_wage_compensation) on e1 and e2; k3 (carry-over) on
  e1 and e2; k2 (conditions of use, as the price of K4's deemed compliance) on e3. `quantity_premises` A-6 (the term is worth less to
  the worker than it costs the employer). `branch_premises` carry the binding and enforcement premises (A-1, A-2 for k1/k3; A-12 for k2).
- fixed: e1 and e3 seller short, A-3 (pay scales, annual raises, collective agreements); e2 seller long, A-7 (the minimum wage R1).
- moves: buyer's price takes the wedge short (A-3 on e1/e3; A-7 on e2, long); seller's wage takes it medium (A-5 on e1/e3).
- thresholds (K5): reading U2-a employers.near_threshold, employment (headcount); reading U2-b workers.part_time, hours_worked, chosen by
  employers.near_threshold. Premise A-10 (and A-8 for the hours route). announced K5 with A-25; announced K1.
- unclear U1 (k3 applies under U1-a only) and U2 (k5_headcount under U2-a, k5_hours under U2-b).
- compliance (k1 employers.covered, k2 employers.pto_gap), enforcer (k6 officials.enforcement), funded (k6 by taxpayers, A-20).
  No fixed_budget (A-20: new money). No held line, grant, cap, ban, backstop, expiry or qualifies: the Act has none.

## Round 1 (depth 1): 9 nodes

Nodes: employers.covered, employers.near_threshold, employers.pto_gap, officials.enforcement, taxpayers, workers.min_wage,
workers.part_time, workers.pto_gap, workers.uncovered.

Proposed:
- employers.covered: adjust margins on workers.uncovered (e1) and workers.min_wage (e2) over employment, hours_worked,
  non_wage_compensation (wages fixed by A-3/A-7, so the payer adjusts the terms it controls; premise judged); outside margin
  legal_breach on e1 and e2 (A-16: "on complaint only", complaints unlikely for some workers); alternatives: reclassification
  (A-11, Independent-contractor exemption and R2), quantity_substitute (A-19, agencies and on-call staff), seasonal turnover before the
  90-day wait (A-23, K2); stake in k1 (A-14); links: price_paid output to consumers (A-17), cost to producers.tradable
  quantity_supplied (A-18, Pellam), reclassification same_act to workers.contractor employment (A-11), quantity_substitute input to
  intermediaries.staffing (A-19); asset owners.labor_intensive (A-24); yields on e1 (A-3) and e2 (A-7).
- employers.pto_gap: adjust margin on workers.pto_gap, link price_paid to consumers (A-17), yield (A-3).
- employers.near_threshold: alternatives under U2-a (reclassification A-11, quantity_substitute A-19) and U2-b (more part-timers, A-8);
  timing carry_over of employment in the announcement window (A-10 with the announced premise A-25); stakes (A-14).
- workers.min_wage: job_changes alternative (A-15). workers.uncovered: hours_worked alternative (A-4); job_changes (A-15);
  jobs at employers.small (judged); jobs in Pellam as workers.border (judged, "40,000 people commute across the river"); stake (A-14);
  incidence on k1/e1 with side seller (A-22).
- Empty lists: officials.enforcement, taxpayers, workers.part_time, workers.pto_gap.

Answers (14 questions): from the table: A-16 .8, A-11 .55, A-19 .65, A-23 .4, A-14 .85, A-17 .7, A-18 .65, A-24 .7, A-15 .55, A-4 .9,
A-22 .6. Judged: "Employers can adjust at least one of hiring, hours, schedules, breaks, training or benefits." .9 (not in the table;
same wording as the WE-009 record); "Some uncovered workers can take jobs at firms with fewer than six employees." .8;
"Some uncovered workers can take jobs in Pellam across the river." .7.

## Round 2 (depth 2): 14 node visits

Nodes: consumers, employers.covered#2, employers.near_threshold#2, employers.pto_gap#2, employers.small, intermediaries.staffing,
owners.labor_intensive, producers.tradable, workers.border, workers.contractor, workers.min_wage#2, workers.part_time#2,
workers.pto_gap#2, workers.uncovered#2.

Proposed:
- consumers (price_paid up): substitute to consumers.border cross_border_purchases (judged, Fenmouth on the river); own_price to
  quantity_demanded (CR-4c, no premise); quantity_demanded input to workers.uncovered employment,hours_worked (CR-6 1.1, no premise);
  substitute to employers.small and employers.compliant quantity_traded (A-13).
- producers.tradable (quantity_supplied down): substitute to sellers.foreign (A-18); input to workers.uncovered employment,hours_worked.
- employers.near_threshold#2: employment same_act to workers.prospective (A-10); reclassification and quantity_substitute links
  (A-11, A-19); `parts`: near_threshold is part of employers.small (CR-12, so small-firm employment combines the held-back hiring and
  the workers arriving).
- employers.covered#2: adjust margin on workers.prospective employment (A-9: employers infer expected use from applicants and cannot
  set pay worker by worker, so hiring is the margin I had missed in round 1).
- Empty: employers.pto_gap#2, employers.small, intermediaries.staffing, owners.labor_intensive, workers.border, workers.contractor,
  workers.min_wage#2, workers.part_time#2, workers.pto_gap#2, workers.uncovered#2.

Answers (3 new questions): A-13 .6 and A-9 .55 from the table; "Residents of Fenmouth and other border towns can easily buy goods and
services in Pellam." .6 judged.

## Round 3 (depth 3): 7 node visits

Nodes: consumers#2, consumers.border, employers.compliant, employers.small#2, sellers.foreign, workers.prospective, workers.uncovered#3.
Proposed: consumers.border same_act to sellers.foreign quantity_traded and substitute to employers.covered quantity_traded (the
Pellam premise); employers.compliant input to workers.with_leave employment,hours_worked (A-13); employers.small#2 input to its own
employment,hours_worked (A-13); sellers.foreign input to workers.border employment,hours_worked (A-18). Empty: consumers#2,
workers.prospective, workers.uncovered#3. No new questions. Stops at depth 3.

## Table statements not used, and why

A-21 (complaints filed in meaningful numbers) and A-26 (unpaid absences without the Act) have no place to attach. See below.

## What the format could not hold

1. Binding and enforcement premises on a mandated term. A charge has no `binding` premise; I put A-1/A-2 into `branch_premises`, which
   gates the charge, though K1 is not a choice between two branches.
2. A charge that is a choice for some payers only (K4 "deemed compliant if the PTO policy meets K2") is held as a separate exchange e3
   with a branch premise; the choice between keeping the old PTO and meeting K2 is not a modelled option.
3. Dated operations. "K3 is enforced from 1 January 2028", the 90-day wait (existing employees: 1 April 2027) and the two-year complaint
   window have no field. U1 can only switch k3 on or off by reading; k3 duplicates k1's effects (same exchange, receiver, variable) so
   no sign differs by reading. U2 is held as two thresholds on different variables, which does produce reading-dependent signs.
4. Enforcement strength. A-16 (complaints unlikely) and A-21 (complaints filed in numbers) pull legal_breach in opposite directions; the
   `outside` margin can only raise it. A-21 and A-26 cannot be used.
5. Subgroups with different horizons inside one exchange (the 9% under collective agreements fix wages for 1 to 3 years, others do not):
   one `fixed` horizon per exchange, so the agreement group is folded into A-3.
6. No variable for an employer's labour cost per hour: price_paid ("including taxes") stands for wage plus the mandated term.
7. An alternative is only signed as "used more" (worse) or "used less" (better), so an option such as automation, or an employer moving
   to Pellam, has no variable that falls when used; I left automation out, and the quirk that a receiver's option set is "better" made
   workers.min_wage alternatives unusable except job_changes.
8. A wage that falls in the medium run should undo the short-run rise in employers' price_paid and in consumers' price; links carry no
   horizon and `moves` fires both, so the consumer price rise stands as stated.
9. Staffing agencies, contractors and workers with existing leave are new classes (intermediaries.staffing, workers.contractor,
   workers.with_leave); seasonal workers (workers.seasonal) never clear the cut-off (A-23, p .4).
