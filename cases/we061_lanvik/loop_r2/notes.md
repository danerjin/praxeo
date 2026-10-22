# WE-061 Lanvik App-Based Work Act 2027: blind expand-loop run (loop_r2)

Inputs: section 1 and the assumption table only. Assumption ids are written lower-case in the seed (a1, a3 ...) because clingo rejects `A-1`; `j1`, `j2` are statements judged by me.

## Seed (policy's own facts, CR-1)
- Exchanges: `e_emp` (platforms.large buy from workers.employees; unsatisfied workers.prospective; criteria allocation_by_non_price_criteria, wait_time) and `e_con` (platforms.large from workers.contractors). Classes split because the policy treats them differently (employee vs contractor; 100+ workers vs fewer: platforms.large / platforms.near_threshold / platforms.small).
- K2 floor as two held components under unclear U1: k2_a (U1-a, trip time; premises a3, a1) and k2_b (U1-b, all logged-in time; j1, a1). K3 overtime and K4 notch as `thresholds` (workers.full_time hours_worked, chooser platforms.large; workers.near_threshold earnings). K4 also a charge (tax_revenue) on e_emp. K5 premium as a charge on e_con paid in kind to workers.contractors (non_wage_compensation), `quantity_premises` a29, branch premises a2, j2. K1 as a threshold on platforms.near_threshold (employment), a15. K6: penalties (5,000 fine to officials.enforcement; double damages to workers.employees), enforcer, compliance, `funded` by taxpayers (a26). `fixed` (short, a29) and `moves` (medium, a28) on the fare share in both exchanges; `announced` (a11) for k2_a, k2_b, k3, k4, k5; criterion margin a31.
- Table answers: a1 a2 a3 a11 a15 a17 a18 a19 a26 a28 a29 a31. Judged: j1 "Many logged-in hours pay below 16 per logged-in hour (about three quarters)" 0.95 (section 1: 75%); j2 "Some workers sign a contractor agreement" 0.85 (section 1 is silent on take-up; A-5 implies some choose each way).

## Round 1 (10 nodes, depth 1)
platforms.large: links (output) of its price_paid to consumers.riders and retailers.restaurants (a4); adjust margins on e_emp (a18), e_con (a7), and a U1-b-only margin (a6, scheduling logged-in time); alternatives for k2_a/k2_b to contractors (a2, a7) and reclassification under k1 (a8); stakes k2_a, k2_b, k5 (a16); asset and yield for owners (a11). workers.employees: alternatives to contractor status (j2), one-person firms (a9), Selvane (a14); link to claimants' applications (a20); stakes. workers.contractors: alternative back to employee status (a5) and, under U1-b, (a23); stake. workers.full_time, workers.near_threshold: contractor alternative (j2). workers.prospective: contractors (a2, j2), Selvane (a14). platforms.near_threshold: shift to platforms.small (a15), stake. officials.enforcement, officials.revenue, taxpayers: empty.
Answers: all ten questions from the table (a4 a7 a6 a8 a16 a5 a23 a9 a14 a20).

## Round 2 (9 nodes)
consumers.riders: own_price to quantity_demanded (a4), substitute links to drivers.taxi (a10) and sellers.substitutes (a4), input links of quantity_demanded to the workers' employment,hours_worked. retailers.restaurants: own_price (a12), in-house couriers (a13), input links. owners: yield to investment_target (a11). platforms.large#2: link to consumers.diners (a4). platforms.small: input to workers.uncovered (a15). workers.contractors#2: same_act links of net_price_received and non_wage_compensation to earnings, and a dominance premise (a25, increase). neighboring_jurisdictions, platforms.near_threshold#2, workers.employees#2: empty. Answers from table: a10 a12 a13 a25.

## Round 3 (9 nodes)
consumers.diners: own_price, substitute to households home_production (home cooking, a4), input links. drivers.taxi: new exchange `e_taxi` with the city's fares `fixed` on both sides (a10), same_act to quantity_traded (idle capacity, a10), asset and yield for owners.medallion (a11, a10). Six nodes empty (consumers.riders#2, owners#2, retailers.restaurants#2, sellers.substitutes, workers.contractors#3, workers.couriers, workers.uncovered). No new questions.

Totals: 3 rounds, 28 node visits, 14 loop questions (all from the table; none judged in the loop; two judged in the seed), no `off-list:` lines.

## What the format could not hold
- K1 as a status presumption (a default status with the burden of proof on the company) has no part: only the 100-worker line (threshold) is recorded, not the three-condition test or the default screen of §9.
- The overtime rate (1.5 times) and the contribution on first 150 (a notch of about 16.50) have no cost field; `thresholds` records only that crossing is worse.
- The choice each worker makes between statuses is two exchanges with split classes; the engine has no "choose one of two statuses" link, so a5/a23 appear as alternatives and the net result on workers.employees (wage_rate, hours) stays ambiguous.
- A-25 (premium dominates entry and fewer trips on hourly earnings) needs one variable that nets a price and a quantity; I made `earnings` by same_act links. Dominance below the cut-off (0.35) leaves earnings ambiguous. "Hourly" earnings has no variable.
- A-24 (entry is partial for four to six weeks) and A-30 (some riders do not cut trips) are limits on a response, with no field; a24 and a30 not used. A-27 is absent from the table.
- Per-reading signs: the U1 readings changed only the contractor/employee hours group; the report prints no per-reading line, so I cannot tell from the output which signs depend on U1.
- Double damages (private suits) recorded as a penalty collected by workers.employees; the engine treats it as a fine.
