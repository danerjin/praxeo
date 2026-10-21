# WE-029 / Analysis: Varrow Healthy Workplaces Act (paid sick leave mandate)

Analyst: core-only re-run (Handbook 0.7)  |  Rules: core rules CR-1 to CR-12 only  |  Status: compared

## 1. Policy record

**Varrow Healthy Workplaces Act.** The State of Varrow has about 6.2 million people and 2.7 million private-sector employees. Its largest city, Fenmouth, lies on the river that forms the border with the State of Pellam, which has no paid sick leave law; about 40,000 people commute across the river each day. Varrow's minimum wage is $13.50 an hour, indexed each year to consumer prices; about 9% of private employees earn at or near it. About 62% of private employees already receive paid sick leave, or PTO usable for illness; about 38% (about 1.0 million) do not. The uncovered are concentrated in food service, retail, personal care, agriculture and construction, and about 55% of them work part time. About 9% of private employees are covered by collective agreements that fix wages for one to three years.

| Field | Value | Source sentence |
|---|---|---|
| Jurisdiction (and what lies just outside) | State of Varrow, private employers. Just outside: the State of Pellam across the river from Fenmouth, with no paid sick leave law; about 40,000 daily cross-river commuters. | "Its largest city, Fenmouth, lies on the river that forms the border with the State of Pellam, which has no paid sick leave law" |
| Announced / enacted / effective / expires | Introduced 12 January 2026 with the governor's support; passed 28 April 2026; signed 15 May 2026; effective 1 January 2027; K3 enforced from 1 January 2028; no expiry. | "The bill was introduced on 12 January 2026 ... takes effect on 1 January 2027. It has no expiry." |
| Enforcement (who, penalties, resources) | Department of Labor Standards; on complaint only, within two years; back pay plus an equal sum as damages; civil penalty up to $1,000 for retaliation; notices and three-year records; $3.4 million a year from the general fund for 25 investigators. | K6 |

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Accrual and pay | `mandated_contract_term` (the employment contract) | Paid sick time | Covered employers | One hour per 30 hours worked, from the first hour (existing employees from 1 January 2027), up to 40 hours accrued a year; paid at the regular hourly rate. | K4, K5; independent contractors (R2 test); public employers. |
| K2 Use | Part of K1 | Conditions of use | Covered employers | Own or family member's illness, injury or medical care; usable after 90 days (existing employees from 1 April 2027); one-hour increments; notice "as soon as practicable"; documentation only for absences over three consecutive scheduled workdays; no replacement requirement; not counted under attendance policies. | As K1 |
| K3 Carry-over | Part of K1 | Unused hours | Covered employers | Unused hours carry over; employer may cap balance at 80 and use at 40 a year; no payout at separation; balance restored on rehire within six months. Enforced from 1 January 2028. | As K1 |
| K4 Equivalent policies | Exemption from K1 to K3 | Employers with existing PTO | Covered employers | Deemed compliant if at least 40 hours a year usable for K2 purposes on K2 conditions. | - |
| K5 Small employers | Exemption from K1 to K3 | Employers with fewer than six employees | - | Size is the average number of employees during the previous calendar year. | - |
| K6 Enforcement | Enforcement | K1 to K3 | DLS | As in the field table above. | - |
| R1 Minimum wage (existing) | `price_floor` | Wages | Employers | $13.50 an hour, indexed yearly. | - |
| R2 Classification test (existing) | Rule on contracts | Employee or contractor | Employers | Three-part test; enforced on complaint and in tax audits. | - |

Unclear provisions:
- **U1, carry-over in the first year.** U1-a: hours accrued in 2027 and unused on 31 December 2027 must carry into 2028; only enforcement waits. U1-b: K3 applies only to hours accrued from 2028, so 2027 hours may lapse.
- **U2, counting employees for K5.** U2-a: every person on the payroll counts as one. U2-b: only employees averaging 20 or more hours a week count.

Counterfactual: Varrow without the Act, with the same minimum wage (R1) and classification rule (R2). In the counterfactual law no term obliges a private employer to pay for sick time, so K1 attaches an obligation that did not exist (CR-1, recording note).

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | CR-1 operations | Core rules applied |
| --- | --- | --- | --- | --- |
| K1 Accrual and pay | triangular (forces a term into a private exchange) | Yes for employers of the 38% uncovered (A-1); no for employers already meeting K4 | Employers: op 3 (a payment for absent hours attached to the option 'employ a worker'); op 1 (the option 'employ without paid sick time' removed where enforced, a risk attached where not, A-16). Workers: op 2 (the option 'take a paid absence' added) | CR-4, CR-5c, CR-6, CR-7b, CR-8b, CR-9 |
| K2 Use | triangular (part of K1) | Yes for workers at bound employers after 90 days; also for PTO policies that fail K2 conditions (A-12) | Employers: op 1 (documentation for short absences, replacement requirements and attendance points removed as options). Workers: op 2 (use in one-hour increments without proof for short absences) | CR-4, CR-5c |
| K3 Carry-over | triangular (part of K1) | Yes from 2028; for 2027 hours per reading (U1) | Employers: op 3 (a carried liability); workers: op 3 (a balance lost on leaving, CR-4 for job changes). U1-a: op 3 applies to 2027 hours; U1-b: it does not | CR-4, CR-10a, CR-10b |
| K4 Equivalent policies | exemption | - | Op 2 for employers whose PTO meets K2 conditions (no change); op 3 for those whose PTO does not (A-12): they must change it | CR-1, CR-5c |
| K5 Small employers | exemption (creates a boundary) | Boundary at six employees; who counts per reading (U2) | Op 2 for firms below six; a boundary that attaches op 3 to the option 'grow to six' (A-10) | CR-4, CR-7a, CR-10a |
| K6 Enforcement | binary (appropriation from the general fund) and triangular (damages paid by employers to workers) | Complaint-based (A-16, A-21) | DLS: op 4 ($3.4 million a year); employers: op 3 (risk of back pay, damages, retaliation penalty; notice and records duty); taxpayers: op 4 | CR-4 (x: comply, y: violate), CR-8b, CR-8c |

## 3. Actor classes

| Actor class | Role | How its options change (CR-1) |
| --- | --- | --- |
| workers.uncovered | Employees of covered employers who had no paid leave usable for illness (about 1.0 million, A-1) | Op 2: paid absence for illness; through CR-5c, wages and other terms may move. Split below. |
| workers.uncovered.minimum_wage | Those at or near $13.50 (A-7) | As above; R1 stops the wage from falling to offset the term. |
| workers.uncovered.above_minimum | Those above the minimum | As above; wage can adjust as raises are set (A-5). |
| workers.part_time | Part-time employees of covered employers (about 55% of the uncovered) | Accrue the full 1 per 30 rate without reaching the 40-hour cap, so each of their hours carries more cost than a full-timer's (arithmetic). |
| workers.full_time | Full-time employees of covered employers | Accrual capped at 40 hours (reached at 1,200 hours worked). |
| workers.pto_noncompliant | Employees whose PTO fails the K2 conditions (A-12) | Op 2: conditions of use loosened. |
| workers.size_ambiguous | Employees of firms with six or more on the payroll but fewer than six averaging 20+ hours | U2-a: op 2 as for workers.uncovered; U2-b: none. |
| workers.prospective | Job applicants, including those who appear likely to use sick time (A-9) | Through CR-6: employers choose among them by non-price criteria. |
| workers.family_carers | Uncovered workers with ill family members | Op 2: paid time to give care (gift relation). |
| employers.bound_uncovered | Covered employers that did not offer qualifying leave | Op 3 and op 1 as in K1 to K3; op 3 from K6. |
| employers.pto_noncompliant | Covered employers whose PTO fails K2 (A-12) | Op 3: rewrite PTO to K2 conditions. |
| employers.covered | All covered employers, including those already compliant | Op 3: notices and records (K6). |
| employers.near_threshold | Firms with four to six employees (A-10) | Op 3 attached to the option 'grow to six'. |
| employers.small_exempt | Firms below six employees | Op 2 (exempt); through CR-9 their bound rivals' costs rise (A-13). |
| employers.already_offering | Firms that already met K4 | No operation except notices; through CR-9 their bound rivals' costs rise (A-13). |
| owners.labor_intensive_businesses | Owners of bound labor-intensive firms | Through CR-7c, CR-10c: expected earnings change (A-24). |
| buyers.local_services | Customers of bound restaurants, shops, care agencies | Through CR-9 (labor input_to their services). |
| producers.tradable_varrow | Bound Varrow producers of tradable goods | Through CR-9 (across_border): compete with unbound Pellam producers (A-18). |
| sellers.foreign | Pellam producers | Through CR-9 (across_border). |
| input_suppliers.agency_on_call | Staffing agencies and on-call workers | Through CR-9: cover absent shifts (A-19). |
| intermediaries | Payroll vendors, HR and compliance consultants | Through CR-9: input_to compliance (A-2). |
| sellers.complements.medical | Medical providers | Through CR-9 (complement: paid time off for visits, A-N3). |
| sellers.substitutes.paid_care | Paid sitters and carers for ill family members | Through CR-9 (substitute for a worker's own care, A-N4). |
| workers.complainants | Workers who file complaints (A-21) | Op 4 via K6: back pay plus equal damages. |
| employers.violating | Employers found in breach (A-16, A-21) | Op 4 via K6: pay back pay plus damages. |
| officials.enforcement | DLS | Op 4: $3.4 million a year; investigation tasks. |
| taxpayers | Payers into the general fund, and recipients of other general-fund spending | Op 4: fund K6 (A-20). |
| lobby_groups | Small-business and restaurant associations, unions, compliant employers (A-14) | CR-4 (x: accept, y: lobby) on amendments, readings U1 and U2, enforcement funding. |
| workers.public_and_contractors | Public employees and independent contractors | Excluded: no operation (except through C-23, contractor conversions). |

## 4. Direct effect

CR-1 and CR-2: the immediate change for those whose options K1 to K6 alter.

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-1 | workers.uncovered | term_prevalence (paid sick time in employment contracts) | increase | short; medium; long | CR-1 (op 1, op 2), CR-2 | A-1, A-2 |
| C-2 | workers.uncovered | non_wage_compensation (paid sick time) | increase | short | CR-1 (op 2), CR-5c, CR-8b | A-1, A-2, A-3 |
| C-3 | employers.bound_uncovered | price_paid (labor per hour worked, including sick pay) | increase | short | CR-1 (op 3), CR-5c | A-1, A-2, A-3 |
| C-4 | workers.pto_noncompliant | non_wage_compensation (conditions of use of existing PTO) | increase | short | CR-1 (op 2), CR-5c | A-12, A-2 |
| C-5 | employers.covered | compliance_cost (notices, records, accrual tracking, PTO rewrites) | increase | short | CR-1 (op 3), CR-8c | A-2 |
| C-6 | officials.enforcement | enforcement_cost | increase | short; medium; long | CR-1 (op 4), CR-8c | none |
| C-7 | workers.size_ambiguous | term_prevalence (paid sick time) | U2-a: increase; U2-b: no_change | short; medium; long | CR-1 (op 2, per reading) | A-1, A-2 |

## 5. Responses

CR-4 applied to every pair of options each actor class has; CR-6 where a price is held (R1, existing pay scales); CR-5 for exchanges that stop or change terms; CR-10a for timing.

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-8 | workers.uncovered | hours_worked | decrease | short; medium; long | CR-4 (x: work while ill or attend to other ends unpaid, y: paid absence), CR-4c | A-4, A-2 |
| C-9 | workers.uncovered.minimum_wage | employment (−), hours_worked (−), non_wage_compensation other than sick time (−) | at_least_one_decrease | short; medium; long | CR-6, CR-5c, CR-4c | A-7, A-1, A-2 |
| C-10 | workers.uncovered.above_minimum | wage_rate | no_change | short | CR-6 (existing contracts count as regulated), CR-5c | A-3, A-1 |
| C-11 | workers.uncovered.above_minimum | wage_rate | decrease | medium; long | CR-5c, CR-3b, CR-6, CR-7b | A-5, A-1, A-2 |
| C-12 | workers.uncovered.above_minimum | employment (−), hours_worked (−) | at_least_one_decrease | medium; long | CR-5c, CR-5a, CR-4c | A-6, A-5, A-1, A-2 |
| C-13 | workers.uncovered.above_minimum | employment (−), hours_worked (−), non_wage_compensation other than sick time (−) | at_least_one_decrease | short | CR-6, CR-4c | A-3, A-1, A-2 |
| C-14 | employers.bound_uncovered | tax_share_borne (gross cost of the term) | increase | short | CR-7b, CR-6 | A-3, A-1, A-2 |
| C-15 | workers.uncovered | tax_share_borne (cost of the term) | increase | medium; long | CR-7b | A-22, A-5, A-1, A-2 |
| C-16 | employers.bound_uncovered | price_paid (labor per hour worked, including sick pay) | increase | medium; long | CR-5c, CR-4c, CR-12e | A-6, A-5, A-1, A-2 |
| C-17 | workers.part_time | hours_worked | decrease | medium | CR-4 (x: part-time staffing, y: full-time), CR-4c, arithmetic | A-8, A-1, A-2 |
| C-18 | workers.full_time | hours_worked | ambiguous | medium | CR-12b | A-8, A-1, A-2, A-4 |
| C-19 | workers.prospective | allocation_by_non_price_criteria (hiring against apparent high users) | increase | short; medium | CR-6, CR-4 | A-9, A-1, A-2 |
| C-20 | employers.near_threshold | employment (employees averaging 20+ hours a week) | decrease | short (from mid-2026); medium | CR-4 (x: sixth employee, y: stay below six), CR-10a | A-10, A-N2 |
| C-21 | employers.near_threshold | employment (employees under 20 hours a week) | U2-a: decrease; U2-b: increase | short (from mid-2026); medium | CR-4 per reading, CR-10a | A-10, A-N2 |
| C-22 | employers.small_exempt | number_of_sellers (firms with fewer than six employees) | increase | medium; long | CR-4, CR-7a | A-10 |
| C-23 | employers.bound_uncovered | reclassification (work engaged as independent contracting) | increase | medium | CR-4 (x: employee, y: contractor), CR-1 (op 2) | A-11, A-1 |
| C-24 | employers.bound_uncovered | legal_breach (sick time denied or unpaid) | increase | short; medium; long | CR-4 (x: comply, y: violate), CR-1 | A-16 |
| C-25 | employers.bound_uncovered | legal_breach (2027 balances not carried into 2028) | U1-a: increase; U1-b: no_change | medium (2028) | CR-4 (x: carry over, y: lapse), CR-1 per reading | A-16 |
| C-26 | workers.uncovered | job_changes | decrease | medium; long | CR-4 (x: move, y: stay), CR-10b | A-15, A-1, A-2 |
| C-27 | employers.bound_uncovered | investment_target (labor-saving equipment) | increase | medium; long | CR-4 (x: labor, y: equipment), CR-7a, LW-9 | A-N1, A-6, A-5, A-1 |
| C-28 | lobby_groups | lobbying_effort | increase | short; medium; long | CR-4 (x: accept, y: lobby), CR-8c | A-14, A-1 |
| C-29 | owners.labor_intensive_businesses | asset_value (bound labor-intensive firms) | decrease | short (from January to May 2026) | CR-7c, CR-10c, CR-10a | A-24, A-1, A-3 |
| C-30 | workers.family_carers | home_production (care for ill family members) | increase | short; medium; long | CR-4 (x: work and arrange other care, y: paid time to care), CR-5 (gift) | A-N4, A-1, A-2 |

## 6. Second-order effects

CR-9 along named relations, then CR-5 to CR-7 in each market reached. Depth limit 4. Chains through Pellam labor markets (commuters) and through customers of firms that buy from bound firms are stopped at depth 3 as diffuse. The proximity relation (illness spreading between coworkers and customers) is a health effect, out of scope. No currency relation is reached: Varrow and Pellam share a currency.

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C-31 | buyers.local_services | price_paid (bound restaurants, shops, care services) | increase | short; medium | CR-9, LW-10, CR-6, CR-7a | labor input_to local services (close) | A-17, A-1, A-2 |
| C-32 | buyers.local_services | quantity_traded (bound restaurants, shops, care services) | decrease | short; medium | CR-4c | as above | A-17, A-1, A-2 |
| C-33 | employers.small_exempt, employers.already_offering | quantity_traded (their goods and services) | increase | short; medium | CR-9, CR-4 (buyers: x bound seller, y unbound seller) | substitute (same_market_other_segment) | A-13, A-1, A-2 |
| C-34 | employers.small_exempt, employers.already_offering | asset_value (their firms) | increase | short (from announcement) | CR-7c, CR-10c | as above | A-13, A-24, A-1 |
| C-35 | producers.tradable_varrow | quantity_traded (tradable goods) | decrease | medium; long | CR-9, CR-7a, CR-4c | across_border (Varrow and Pellam producers, partial) | A-18, A-1, A-2 |
| C-36 | sellers.foreign | quantity_traded (Pellam tradable goods) | increase | medium; long | CR-9, CR-4 (buyers: x Varrow producer, y Pellam producer) | across_border | A-18, A-1, A-2 |
| C-37 | input_suppliers.agency_on_call | quantity_traded (agency and on-call labor) | increase | short; medium | CR-9, LW-10 | agency and on-call labor substitute for absent staff (close) | A-19, A-4, A-2 |
| C-38 | intermediaries | quantity_traded (payroll compliance services) | increase | short | CR-9, LW-10 | compliance services input_to compliance (close) | A-2, A-1 |
| C-39 | sellers.complements.medical | quantity_traded (medical visits by covered workers) | increase | short; medium | CR-9, LW-10 | paid time off complement to medical visits | A-N3, A-1, A-2 |
| C-40 | sellers.substitutes.paid_care | quantity_traded (paid care for ill family members) | decrease | short; medium | CR-9, CR-4 | worker's own care substitute for paid care; gift relation to the family member | A-N4, A-1, A-2 |
| C-41 | workers.uncovered | earnings | ambiguous | short | CR-12b | contract (employment) | A-1, A-2, A-3, A-7, A-N5 |
| C-42 | workers.uncovered | earnings | ambiguous | medium; long | CR-12b | contract (employment) | A-1, A-2, A-5, A-6, A-7, A-N5 |
| C-43 | workers.complainants | resources_available_other_uses | increase | short; medium; long | CR-8b | contract (employment); K6 | A-21, A-16 |
| C-44 | employers.violating | resources_available_other_uses | decrease | short; medium; long | CR-8b, CR-3c | as above | A-21, A-16 |

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance premise | Combined sign |
| --- | --- | --- | --- | --- |
| workers.uncovered, earnings, short | Absences that would have been unpaid are now paid (CR-1 op 2, CR-8b; A-N5, A-3) | Employment and hours cut at the margin where the wage cannot fall (C-9, C-13; A-7, A-3); part-time hours cut (C-17, medium) | None | ambiguous (C-41) |
| workers.uncovered, earnings, medium; long | Paid absences (as above) | Wage below the counterfactual (C-11); employment or hours lower (C-9, C-12, C-17) | None | ambiguous (C-42) |
| workers.full_time, hours_worked, medium | Employers move hours from part-time to full-time staff, whose hours carry less accrual per hour above 1,200 (C-17; A-8) | Paid absences (C-8; A-4); labor dearer per hour overall (C-12, C-16) | None | ambiguous (C-18) |
| workers.part_time, hours_worked, medium | - | Shift to full-time staff (A-8); paid absences (C-8); dearer labor (C-12) | Not needed | decrease (C-17) |
| employers.bound_uncovered, price_paid (labor), medium; long | Cost of the term (CR-5c) | Wage falls (C-11) | CR-12e (a response cannot reverse its cause): with A-6, some exchanges stop (C-12), and along the employer's own ranking fewer hours are bought only at a higher total cost per hour (CR-4c) | increase (C-16) |
| employers.bound_uncovered vs workers.uncovered, tax_share_borne | Short: employers (wages fixed, A-3; C-14) | Medium and long: workers (A-22; C-15) | Different horizons, not combined (CR-12g) | employers bear more (short); workers bear more (medium; long) |
| workers.uncovered.above_minimum, wage_rate | - | Medium; long: C-11 | Short: no_change (C-10) | no_change (short); decrease (medium; long) |
| workers.uncovered, non_wage_compensation | Paid sick time (C-2) | Other non-wage terms (C-9, C-13) | Different named items, not netted (CR-12c); see Gaps (b) | increase (paid sick time); members of group signs (other terms) |
| employers.near_threshold, employment, short and medium | - | Holding counted staff below six (A-10) | - | decrease (C-20); per reading for part-timers (C-21) |
| employers.small_exempt, number_of_sellers | Firms that stay below six (C-22); rivals' costs rise (C-33) | - | - | increase |

No chains cancel exactly by construction (CR-12f).

## 8. Time structure

- **Announcement (12 January to 15 May 2026).** The bill was introduced with the governor's support, so its probability of passing rose through the spring. The value of bound labor-intensive firms falls part of the way as the probability rises and the rest at signing (CR-7c, CR-10c; C-29); the value of exempt small firms and already-compliant rivals rises in the same way (C-34). The loss is borne by those who owned the firms in that period, not by later buyers.
- **Size measured in 2026 (K5).** K5 counts the "average number of employees during the previous calendar year", so status in 2027 is set by staffing in 2026. Firms near six respond from the time they learn this (CR-10a; A-N2), in the second half of 2026: C-20 and C-21 start in 2026, before the Act takes effect. Each later year's status is set by the year before, so the response repeats.
- **2027 phase-in.** Existing employees accrue from 1 January 2027 but can use hours only from 1 April 2027; new hires from 90 days. Paid absences (C-8), agency cover (C-37) and medical visits (C-39) start in April 2027 for existing staff. Whether some workers postpone medical visits from January to March 2027 into April (a timing shift, which would be a decrease in the first window and an increase in the second against the counterfactual) needs a premise no case assumption supplies; it is not signed.
- **End of 2027 and U1.** Under U1-b, unused 2027 hours lapse, so workers who expect to lose them use them before 31 December (CR-10a, CR-4 with x: keep, y: use now); paid absences then bunch in late 2027. Against the counterfactual, hours worked are lower in every window under both readings (C-8), so the bunching is a path note (CR-12h). Under U1-a, 2027 balances raise 2028 balances (up to the 80-hour cap) and K3 lapses become breaches (C-25).
- **Wages.** Pay scales, annual raises and collective agreements (9% of employees, one to three years) fix wages in 2027 (A-3), so employers bear the cost at first (C-14) and the pressure goes to hours, jobs and other terms (C-9, C-13). As raises are reset in 2028 and 2029, raises above the minimum are smaller than they would have been (C-11), and the burden shifts toward workers (C-15). For minimum-wage workers R1 (indexed yearly) holds the wage, so the pressure stays on hours, jobs and other terms in every horizon (C-9).
- **Stocks.** Firms kept below six, conversions to contracting and labor-saving equipment (C-22, C-23, C-27) are stocks that change only through flows (CR-10b). Accrued balances are a stock held by the worker that is lost on leaving, which slows job changes more as balances build (C-26). The policy has no expiry; `persistence` (for repeals) does not apply.
- **Enforcement.** Complaints may be filed up to two years after a violation, so back-pay awards (C-43, C-44) lag violations (C-24) by up to two years.

## 9. Opportunity costs

Each is written as a signed change in a variable.

| ID | Actor class | Variable | Sign | What is given up | Rules |
| --- | --- | --- | --- | --- | --- |
| C-5 | employers.covered | compliance_cost (notices, records, accrual tracking, PTO rewrites) | increase | Staff time and payroll fees that would have served other ends | CR-1 (op 3), CR-8c |
| C-6 | officials.enforcement | enforcement_cost | increase | $3.4 million a year: 25 investigators' work and the means taxpayers would otherwise have kept or other programs used | CR-1 (op 4), CR-8c |
| C-28 | lobby_groups | lobbying_effort | increase | Members' dues and staff time | CR-4, CR-8c |
| C-32 | buyers.local_services | quantity_traded (bound restaurants, shops, care services) | decrease | Meals, purchases and care services not bought at the higher price | CR-4c, CR-5a |
| C-45 | employers.bound_uncovered | resources_available_other_uses | decrease | Sick pay, cover for absent shifts and compliance spending that would have gone to investment, owners' consumption or saving; they keep paying because the term cannot be avoided for workers they keep | CR-8a, CR-8b, CR-3c |
| C-46 | taxpayers, recipients of other general-fund spending | resources_available_other_uses | at_least_one_decrease | The $3.4 million a year appropriated for K6 | CR-8b, CR-8a |
| C-12 | workers.uncovered.above_minimum | employment (−), hours_worked (−) | at_least_one_decrease | Employment contracts that both sides would have accepted without the term but not with it (A-6) | CR-5c, CR-5a |

CR-8b is applied to every transfer: sick pay paid by employers (C-45) is received by workers as paid sick time (C-2); back pay and damages paid by violating employers (C-44) are received by complainants (C-43); the appropriation paid by taxpayers (C-46) is spent by DLS (C-6), and is used up in enforcement (CR-8c). The wage reduction in the medium run (C-11) is the means by which part of the employer's payment returns to the employer (C-15).

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
| --- | --- | --- | --- | --- | --- |
| A-1 | About 38% of private employees lack paid leave usable for illness, so the term binds for them. | binding | 0.9 | State labor department survey; benefit surveys by industry. | Nearly every consequence fails; only C-5, C-6, C-46 remain. |
| A-2 | Most bound employers comply: payroll vendors build in accrual, and some workers complain. | enforcement | 0.7 | Payroll vendors' compliance features; complaint rates under comparable laws. | The term becomes a risk rather than a cost: C-1 to C-5, C-7 to C-9, C-11 to C-19, C-26, C-30 to C-42, C-45 weaken or fail. |
| A-3 | Money wages are fixed in the short run by pay scales, annual raises and collective agreements. | other | 0.8 | Raise cycles; collective agreements cover 9%. | C-2, C-3, C-10, C-13, C-14, C-29, C-41, C-45 fail or lose this chain. |
| A-4 | Some uncovered workers would have worked while ill, or will use paid hours for other ends, and documentation rules make this hard to police. | other | 0.9 | Surveys on working while ill; K2's three-day documentation rule. | C-8, C-18, C-37 fail or lose this chain. |
| A-5 | Wages above the minimum can adjust over the medium horizon, as raises are set. | other | 0.8 | Wage growth in these industries is well above zero. | C-11, C-12, C-15, C-16, C-27, C-42 fail. |
| A-6 | For the marginal worker and employer, the term is worth less to the worker than it costs the employer. | other | 0.6 | The term was absent for 38%; against this, selection of high users by employers who alone offer it. | C-12, C-16, C-27 fail; C-42 loses a chain. |
| A-7 | The minimum wage binds for some uncovered workers. | binding | 0.85 | 9% of private employees earn at or near $13.50, mostly in uncovered industries. | C-9 fails; C-41, C-42 lose a chain. |
| A-8 | Employers can move hours between part-time and full-time staff. | other | 0.7 | Shift scheduling in retail and food service. | C-17, C-18 fail. |
| A-9 | Employers can infer expected use of sick time from what they see of applicants, and cannot set pay worker by worker to match it. | other | 0.55 | Hiring practice; posted pay scales; anti-discrimination law. | C-19 fails. |
| A-10 | Some firms near six employees value staying exempt more than an extra hire. | other | 0.6 | Count of firms with four to six employees; their margins. | C-20, C-21, C-22 fail. |
| A-11 | The classification test is weakly enforced in some occupations, so contractor arrangements are open to some employers. | enforcement | 0.55 | Audit rates; occupations where contracting is common. | C-23 fails. |
| A-12 | Some existing PTO policies do not meet the K2 conditions. | other | 0.8 | Sample of employee handbooks. | C-4 fails. |
| A-13 | Compliant and small firms compete in product markets with uncovered firms. | substitutability | 0.6 | Industry overlap. | C-33, C-34 fail. |
| A-14 | Small-business and restaurant associations, unions and compliant employers can organize at a cost below their stake. | other | 0.85 | Existing associations and their activity on the bill. | C-28 fails. |
| A-15 | Some job changes are marginal enough that losing a balance and waiting 90 days decides them. | mobility | 0.55 | Job-to-job moves; the size of the balance compared with a wage gain. | C-26 fails. |
| A-16 | Complaints are unlikely for some workers: short tenure, unaware of the law, fearing retaliation, or owed small sums. | enforcement | 0.8 | Complaint-based enforcement elsewhere; tenure in these industries. | C-24, C-25 fail; C-43, C-44 lose their violations. |
| A-17 | Most competitors of local service sellers are bound too. | other | 0.7 | Size distribution of restaurants, shops and care agencies. | C-31, C-32 fail (the cost would fall on sellers rather than buyers). |
| A-18 | Varrow's tradable producers compete with Pellam producers, who are not bound. | mobility | 0.65 | Plants on both sides of the river; shipping costs. | C-35, C-36 fail. |
| A-19 | Shift-based employers cover absent shifts, partly through agencies and on-call staff. | other | 0.65 | Staffing practice in care, retail and food service. | C-37 fails. |
| A-20 | The $3.4 million is new money from the general fund. | revenue_use | 0.9 | K6. | C-46 becomes a reallocation within DLS: its payers are DLS's other programs. |
| A-21 | Complaints are filed in meaningful numbers. | enforcement | 0.85 | Complaint volumes under comparable laws. | C-43, C-44 fail. |
| A-22 | Over the medium to long run, workers' alternatives to bound employment are clearly worse than employers' alternatives. | mobility | 0.6 | Share of employment in bound firms; commuting to Pellam is open only near Fenmouth. | C-15 fails: the medium-run split is unsigned. |
| A-23 | Employers end seasonal and temporary engagements before 90 days to avoid use. | other | 0.4 | Replacement costs compared with 40 hours of sick pay. | No reported consequence rests on it (see Not reported). |
| A-24 | Labor-intensive businesses are valued on expected earnings, and buyers expect the short-run cost before wages adjust. | expectations | 0.7 | Business sale prices as multiples of earnings. | C-29, C-34 fail. |
| A-N1 | Some bound employers can substitute equipment or self-service for labor at the margin. | substitutability | 0.7 | NEW. Self-ordering kiosks, self-checkout and scheduling software in food service and retail. | C-27 fails. |
| A-N2 | Owners of firms near six employees know from mid-2026 that the 2026 average decides their 2027 status. | expectations | 0.7 | NEW. Act signed 15 May 2026; associations' guidance (A-14); payroll vendors' notices. | C-20, C-21 start in 2027 rather than 2026; their 2026 window fails. |
| A-N3 | Some uncovered workers forgo or delay medical visits during working hours because the time is unpaid. | other | 0.6 | NEW. Surveys on care delayed for lost wages; K2 names medical care. | C-39 fails. |
| A-N4 | Some uncovered workers with an ill family member would have kept working and arranged other care (relatives, paid sitters). | other | 0.6 | NEW. Surveys of working parents; K2 covers family members. | C-30, C-40 fail. |
| A-N5 | Some uncovered workers would have taken unpaid absences for illness without the Act. | other | 0.95 | NEW. Absence rates in uncovered industries. | C-41, C-42 lose their (+) chain and become decreases or no change. |

**Not reported** (an assumption below 0.5, or a premise missing):
- Seasonal and temporary engagements ended before 90 days (CR-4, x: keep past 90 days, y: replace before): needs A-23 (p 0.4). Its direction is a priori (no employer keeps a worker longer because of K2's 90-day threshold), its scale is not.
- Civil penalties for retaliation received by the state (`non_tax_receipts`): needs a premise that retaliation is found and penalized, which no case assumption gives.
- Firms that already offered leave attracted the workers who expect to use it most; spreading the term to all bound firms would lower expected use at those firms. The selection is mentioned only as evidence against A-6, not as an assumption; recorded as a Tier C note.
- Service quality at bound firms falls on days with absences (CR-6, quality as an open margin): no premise says this margin is used rather than agency cover (A-19); Tier C note.
- Cross-river commuters: whether more Pellam residents seek Varrow jobs (term added) or fewer (wages lower in the medium run) is unsigned; the chain is stopped at depth 3.

### Final check before the report

1. **Uncombined chains.** Every (class, variable, horizon) reached by more than one chain is in section 7. Hours worked (C-8, C-9, C-12, C-13, C-17, C-18) all push down except the full-time shift, which makes C-18 ambiguous. Earnings combine to ambiguous in both horizons (C-41, C-42). Employer labor cost in the medium run is signed only with the CR-12e argument and A-6 (C-16).
2. **Group signs.** Where CR-6 licenses only "at least one margin" (C-9, C-13) or CR-5c licenses only that fewer hours of labor are traded (C-12), the group sign is used. C-46 is a group over payers.
3. **Baseline.** All signs are against Varrow without the Act. Legal breach (C-24) is from zero. Wage decrease (C-11) is against the counterfactual path of raises, not a nominal cut.
4. **Worse off is not poorer.** `resources_available_other_uses` is signed only for employers who keep paying an unavoidable term (C-45), payers of the appropriation (C-46), and the two sides of K6 awards (C-43, C-44). It is not signed for buyers of local services, who may buy less (C-32).
5. **Timing shifts.** Size counting in 2026, the April 2027 start of use, and U1 bunching at end-2027 are in section 8; each window is signed against the counterfactual where a premise allows; the January to March 2027 postponement of medical visits is left unsigned for lack of a premise.
6. **Both sides of every transfer.** Sick pay (C-45 / C-2), K6 awards (C-44 / C-43), appropriation (C-46 / C-6), and the medium-run wage offset (C-11 / C-15).
7. **Every actor class, every core rule.** CR-4 applied to comply/violate (C-24, C-25), employee/contractor (C-23), grow/stay small (C-20 to C-22), part/full time (C-17), labor/equipment (C-27), here/Pellam (C-35, C-36), move/stay (C-26), accept/lobby (C-28), work/absent (C-8), work/care (C-30). CR-6 for R1 and fixed pay scales (C-9, C-13). CR-7 including capitalization (C-29, C-34) and incidence (C-14, C-15). CR-9 along input_to, substitute, complement, across_border, contract and gift relations (C-31 to C-44). Enforcement costs (C-6) and the payer's side (C-46) included.
8. **Unstated premises.** Five added (A-N1 to A-N5), each in the table above.

## 11. Report

**The policy:** From 1 January 2027, private employers in Varrow with six or more employees must let each employee accrue one hour of sick time per 30 hours worked, up to 40 hours a year, paid at the regular rate and usable after 90 days (existing staff from April 2027) for their own or a family member's illness or medical care, in one-hour steps, without documentation for short absences. Unused hours carry over (enforced from 2028). Employers whose existing PTO meets these terms are deemed compliant. Enforcement is by complaint, with back pay plus equal damages, funded by $3.4 million a year from the general fund.

**Visible consequences:** About a million employees who had no paid sick time now have it (C-1, C-2), and some whose PTO had stricter conditions get looser ones (C-4). Their employers pay more per hour worked at first (C-3), and every covered employer bears notice and record costs (C-5). The state spends on investigators (C-6). Who is covered at employers with many part-timers depends on how the size rule is read (C-7).

**Invisible consequences:**
- *Workers:* They work fewer hours, because some who would have worked while ill now take paid time, and some use it for other ends (C-8). Where the minimum wage stops the wage from falling, and in 2027 while pay scales are fixed, employers cut at least one of jobs, hours or other terms (C-9, C-13). From 2028, raises above the minimum are smaller than they would have been (C-10, C-11), and if the term is worth less to workers than it costs, fewer hours of work are bought (C-12). Part-timers, whose hours carry the most accrual per hour, lose hours (C-17). Applicants who look likely to use sick time are passed over (C-19). Workers change jobs less, since moving loses the balance and restarts the 90-day wait (C-26). Workers caring for ill family members give more care themselves (C-30). Over the medium run workers bear more of the cost than employers (C-15); in 2027 employers bear more (C-14).
- *Employers:* Their labor costs per hour remain higher in the medium run (C-16), and they have less to spend elsewhere (C-45). Some move work to contractors (C-23) or to equipment (C-27). Firms near six employees hold down their counted staff from 2026 (C-20, C-21), so more firms stay small (C-22). Some do not comply, especially with workers unlikely to complain (C-24); under one reading of the carry-over rule, letting 2027 hours lapse is a breach (C-25). Owners of labor-intensive bound firms lost value from the spring of 2026 (C-29); owners of exempt and already-compliant rivals gained (C-34).
- *Other markets:* Customers of bound restaurants, shops and care agencies pay more and buy less (C-31, C-32), and some shift to exempt or already-compliant sellers (C-33). Varrow producers of tradable goods lose sales to Pellam producers (C-35, C-36). Agencies and on-call workers fill more absent shifts (C-37); payroll and compliance vendors sell more (C-38); medical visits rise (C-39); paid care for ill relatives falls (C-40).
- *The state:* Taxpayers or recipients of other spending fund the investigators (C-46); complainants receive back pay and damages from violating employers (C-43, C-44); interest groups spend on lobbying over amendments and readings (C-28).

**Ambiguous effects:** Total earnings of the uncovered, short and medium run (C-41, C-42): paid absences push them up; fewer jobs and hours, and smaller raises, push them down. Hours of full-time staff (C-18): employers move hours to them from part-timers, while paid absences and dearer labor push hours down. What would decide each: the size of the employment and hours response against the value of sick pay received.

**Key conditions:** The term binds for the uncovered (A-1, 0.9) and most employers comply (A-2, 0.7). Wages are fixed in 2027 (A-3, 0.8) and adjust later (A-5, 0.8), which decides who bears the cost when (C-14, C-15, with A-22, 0.6). The term is worth less to workers than it costs (A-6, 0.6), which is what makes employment fall above the minimum and keeps labor costs higher in the medium run. The selection premise A-9 (0.55), the contracting premise A-11 (0.55) and the lock-in premise A-15 (0.55) are close to the cut-off. Five premises were added (A-N1 to A-N5).

**What this analysis cannot say:** How large any effect is; whether earnings of the uncovered rise or fall; whether workers value the leave more than any wage and job losses; whether the policy is good. Health effects, including the spread of illness at work and the health of workers who now stay home or see a doctor, are out of scope in version 1, as are safety effects.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C-1 | workers.uncovered | term_prevalence (paid sick time in employment contracts) | increase | short; medium; long | visible | B | CR-1 (op 1 for the employer where enforced: contracts without paid sick time removed; op 2 for the worker); CR-2 (employers who comply choose the term over violation, A-2) | A-1, A-2 |
| C-2 | workers.uncovered | non_wage_compensation (paid sick time) | increase | short | visible | B | CR-1 (op 2: paid absence added); CR-5c (the terms include everything either party gives, money or not); CR-8b (the employer's payment is the worker's receipt); wages fixed (A-3), so the term is added on top | A-1, A-2, A-3 |
| C-3 | employers.bound_uncovered | price_paid (labor per hour worked, including sick pay) | increase | short | visible | B | CR-1 (op 3: a payment for absent hours attached to each hour worked, 1/30 of an hour up to 40 hours a year); CR-5c (what one party must give rises; wage fixed, A-3) | A-1, A-2, A-3 |
| C-4 | workers.pto_noncompliant | non_wage_compensation (conditions of use of existing PTO) | increase | short | invisible | B | CR-1 (op 2: K2 removes documentation for short absences, replacement requirements and attendance points from PTO that relied on them, A-12); CR-5c | A-12, A-2 |
| C-5 | employers.covered | compliance_cost (notices, records, accrual tracking, PTO rewrites) | increase | short | invisible | B | CR-1 (op 3: K6 notice and three-year records; K1 accrual tracking; K4 rewrite for A-12 firms); CR-8c (resources spent complying are used up) | A-2 |
| C-6 | officials.enforcement | enforcement_cost | increase | short; medium; long | visible | A | CR-1 (op 4: $3.4 million a year for 25 investigators); CR-8c (resources spent enforcing are used up) | none |
| C-7 | workers.size_ambiguous | term_prevalence (paid sick time) | U2-a: increase; U2-b: no_change | short; medium; long | invisible | B | CR-1 per reading: U2-a counts every payroll member, so firms with six or more heads are bound (op 2 for their workers); U2-b counts only 20+ hour employees, so firms with fewer than six such employees stay exempt (no operation) | A-1, A-2 |
| C-8 | workers.uncovered | hours_worked | decrease | short; medium; long | invisible | B | CR-4 (x: work while ill, or forgo other ends, unpaid; y: take a paid absence; y made better by K1, so workers for whom x ranked narrowly above y switch); CR-4c (the last hour worked, valued least, is the first given up); K2's documentation rule keeps y open (A-4) | A-4, A-2 |
| C-9 | workers.uncovered.minimum_wage | employment (−), hours_worked (−), non_wage_compensation other than sick time (−) | at_least_one_decrease | short; medium; long | invisible | B | CR-5c (the employer's maximum acceptable wage falls by the cost of the term); CR-6 (R1 holds the wage, A-7, so the pressure goes to open margins: hours, jobs, other terms); CR-4c (fewer units of labor bought at a higher cost per unit). Which margin is used needs a premise per margin, so a group | A-7, A-1, A-2 |
| C-10 | workers.uncovered.above_minimum | wage_rate | no_change | short | invisible | B | CR-6 (terms fixed by existing contracts count as regulated while they last: pay scales, raise cycles and collective agreements, A-3); CR-5c (the range moves but the fixed term does not) | A-3, A-1 |
| C-11 | workers.uncovered.above_minimum | wage_rate | decrease | medium; long | invisible | B | CR-5c (the employer's maximum acceptable wage falls by the cost of the term); CR-3b (the added option cannot make workers less willing to work at a given wage); CR-6 (with fewer hours wanted and no fewer offered at each wage, the wage moves toward a lower clearing level as raises are set, A-5); CR-7b (each side bears part) | A-5, A-1, A-2 |
| C-12 | workers.uncovered.above_minimum | employment (−), hours_worked (−) | at_least_one_decrease | medium; long | invisible | B | CR-5c (the employer's maximum wage falls by the cost, the worker's minimum by the term's value to them; with A-6 the cost exceeds the value, so the range of acceptable terms narrows for every pair); CR-5a (pairs whose range was narrower than the gap no longer exchange); CR-4c. Whether jobs or hours are given up is not said, so a group | A-6, A-5, A-1, A-2 |
| C-13 | workers.uncovered.above_minimum | employment (−), hours_worked (−), non_wage_compensation other than sick time (−) | at_least_one_decrease | short | invisible | B | CR-6 (wages fixed by existing contracts, A-3, so the employer's higher cost per hour goes to open margins); CR-4c (fewer units bought at a higher cost per unit) | A-3, A-1, A-2 |
| C-14 | employers.bound_uncovered | tax_share_borne (gross cost of the term) | increase | short | invisible | B | CR-7b (the burden settles on the side that cannot move: in 2027 the wage cannot move, A-3, so employers bear the gross cost of the term except where they cut hours or jobs); CR-6 (existing contracts count as regulated) | A-3, A-1, A-2 |
| C-15 | workers.uncovered | tax_share_borne (cost of the term) | increase | medium; long | invisible | B | CR-7b (where both sides have alternatives, the side whose alternatives are clearly worse bears more: workers' alternatives (small firms, contracting, Pellam) are clearly worse than employers' (automation, redeployment, Pellam), A-22; the wage adjusts, A-5). Gross share, before the term's value to workers | A-22, A-5, A-1, A-2 |
| C-16 | employers.bound_uncovered | price_paid (labor per hour worked, including sick pay) | increase | medium; long | invisible | B | CR-5c (+: the term's cost; −: the lower wage, C-11); CR-12e (a response cannot reverse its cause: with A-6 employers buy fewer hours, C-12, and by CR-4c they buy fewer only at a higher total cost per hour, so the wage fall is smaller than the cost) | A-6, A-5, A-1, A-2 |
| C-17 | workers.part_time | hours_worked | decrease | medium | invisible | B | Arithmetic on K1: accrual is 1/30 of each hour worked up to 40 hours, reached at 1,200 hours a year, so an hour of a part-timer below 1,200 hours carries more accrual than an hour of a full-timer above it; CR-4 (x: staff with part-timers, y: with full-timers; y made relatively better, A-8); CR-4c; plus C-8 and C-12, also down | A-8, A-1, A-2 |
| C-18 | workers.full_time | hours_worked | ambiguous | medium | invisible | B | CR-12b: (+) CR-4 (hours moved from part-time to full-time staff, A-8, C-17); (−) CR-4 (paid absences, A-4, C-8); (−) CR-4c (dearer labor overall, C-12, C-13). No premise says which dominates | A-8, A-1, A-2, A-4 |
| C-19 | workers.prospective | allocation_by_non_price_criteria (hiring against apparent high users) | increase | short; medium | invisible | B | CR-6 (the wage cannot be set worker by worker to match expected use, A-9, so the pressure goes to the criteria by which employers choose among applicants); CR-4 (x: hire an applicant who appears likely to use the time, y: another applicant) | A-9, A-1, A-2 |
| C-20 | employers.near_threshold | employment (employees averaging 20+ hours a week) | decrease | short (from mid-2026); medium | invisible | B | CR-4 (x: hire a sixth counted employee, which binds K1 to K3 the next year; y: stay below six; x made worse, so firms that rank staying exempt above the hire switch, A-10); CR-10a (status in 2027 depends on the 2026 average, A-N2, so the response starts in 2026). Such employees count under both readings of U2 | A-10, A-N2 |
| C-21 | employers.near_threshold | employment (employees under 20 hours a week) | U2-a: decrease; U2-b: increase | short (from mid-2026); medium | invisible | B | CR-4 per reading. U2-a: every head counts, so firms near six hold down part-time heads too, and spread hours over fewer staff. U2-b: under-20-hour employees do not count, so firms replace a counted hire with uncounted part-timers (x: counted hire, y: uncounted hires). CR-10a for the 2026 start (A-N2) | A-10, A-N2 |
| C-22 | employers.small_exempt | number_of_sellers (firms with fewer than six employees) | increase | medium; long | invisible | B | CR-4 (x: grow past five, y: stay below six; A-10); CR-7a (owners who would have grown a firm past five start a second small firm or stay small where the yield is higher net of the term) | A-10 |
| C-23 | employers.bound_uncovered | reclassification (work engaged as independent contracting) | increase | medium | invisible | B | CR-1 (op 2: the contractor exemption is an option without the term); CR-4 (x: employ, y: engage as a contractor; y made relatively better; open where R2 is weakly enforced, A-11) | A-11, A-1 |
| C-24 | employers.bound_uncovered | legal_breach (sick time denied or unpaid) | increase | short; medium; long | invisible | B | CR-1 (an unenforced obligation attaches a risk rather than removing an option; enforcement is on complaint only); CR-4 (x: comply, y: violate; for workers unlikely to complain, A-16, the expected penalty is small, so some employers violate) | A-16 |
| C-25 | employers.bound_uncovered | legal_breach (2027 balances not carried into 2028) | U1-a: increase; U1-b: no_change | medium (2028) | invisible | B | CR-1 per reading: U1-a makes the 2027 carry-over an obligation enforced from 2028; some employers let balances lapse anyway, by CR-4 (x: carry over, y: lapse), where complaints are unlikely (A-16). U1-b: lapse is lawful | A-16 |
| C-26 | workers.uncovered | job_changes | decrease | medium; long | invisible | B | CR-4 (x: move to another job, y: stay; moving loses the accrued balance, not paid out, and restarts the 90-day wait, so x is made worse; A-15); CR-10b (balances are a stock that builds, up to 80 hours, so the effect grows) | A-15, A-1, A-2 |
| C-27 | employers.bound_uncovered | investment_target (labor-saving equipment) | increase | medium; long | invisible | B | CR-4 (x: hire labor, y: buy equipment that replaces it; labor dearer per hour, C-16, A-6, A-5; equipment available, A-N1); CR-7a; LW-9 (the proportion of means is changed toward the one made cheaper) | A-N1, A-6, A-5, A-1 |
| C-28 | lobby_groups | lobbying_effort | increase | short; medium; long | invisible | B | CR-4 (x: accept the Act and its readings, y: lobby for amendment, repeal, a reading of U1 or U2, or enforcement funding; each group's stake changed by K1 to K6, A-1; organizing costs below stakes, A-14); CR-8c (resources spent lobbying are used up) | A-14, A-1 |
| C-29 | owners.labor_intensive_businesses | asset_value (bound labor-intensive firms) | decrease | short (from January to May 2026) | invisible | B | CR-10c (value reflects expected earnings, A-24); CR-7c (the expected fall in earnings while wages are fixed, A-3, is borne by whoever owns the firm when it becomes expected, part of the way as passage became more likely from 12 January and the rest by signing on 15 May); CR-10a | A-24, A-1, A-3 |
| C-30 | workers.family_carers | home_production (care for ill family members) | increase | short; medium; long | invisible | B | CR-4 (x: keep working and arrange other care, y: take paid time to give care; y made better by K2, A-N4); CR-5 gift clarification (the worker's care is a gift to the family member, who receives more of it) | A-N4, A-1, A-2 |
| C-31 | buyers.local_services | price_paid (bound restaurants, shops, care services) | increase | short; medium | invisible | B | CR-9 (relation: labor input_to local services; sellers' cost per unit rises, C-3, C-16); LW-10; CR-6 (less offered at each price moves the price up); CR-7a (since most competitors are bound too, A-17, buyers cannot move to sellers without the cost) | A-17, A-1, A-2 |
| C-32 | buyers.local_services | quantity_traded (bound restaurants, shops, care services) | decrease | short; medium | invisible | B | CR-4c (at a higher price the last unit, valued least, is given up; LW-3); CR-5a | A-17, A-1, A-2 |
| C-33 | employers.small_exempt, employers.already_offering | quantity_traded (their goods and services) | increase | short; medium | invisible | B | CR-9 (relation: same_market_other_segment; their rivals' costs and prices rise, C-31); CR-4 (buyers: x bound seller, y exempt or already-compliant seller; y made relatively better; A-13) | A-13, A-1, A-2 |
| C-34 | employers.small_exempt, employers.already_offering | asset_value (their firms) | increase | short (from announcement) | invisible | B | CR-10c (value reflects expected yields, A-24); CR-7c (the expected rise in their sales, C-33, is captured by whoever owns them when it becomes expected) | A-13, A-24, A-1 |
| C-35 | producers.tradable_varrow | quantity_traded (tradable goods) | decrease | medium; long | invisible | B | CR-9 (relation: across_border; Pellam rivals are not bound, A-18); CR-7a (the price of a tradable good is held in line with Pellam's, so the higher cost cannot be passed on, and output moves to where yields are higher); CR-4c | A-18, A-1, A-2 |
| C-36 | sellers.foreign | quantity_traded (Pellam tradable goods) | increase | medium; long | invisible | B | CR-9 (relation: across_border); CR-4 (buyers: x Varrow producer, y Pellam producer; y made relatively better as Varrow producers supply less, C-35) | A-18, A-1, A-2 |
| C-37 | input_suppliers.agency_on_call | quantity_traded (agency and on-call labor) | increase | short; medium | invisible | B | CR-9 (relation: agency and on-call labor substitute for staff absent on paid time, C-8, A-4); LW-10 (demand for the means that cover a shift follows the shifts left uncovered); employers cover shifts partly this way (A-19) | A-19, A-4, A-2 |
| C-38 | intermediaries | quantity_traded (payroll compliance services) | increase | short | invisible | B | CR-9 (relation: compliance services input_to compliance, C-5); LW-10 (demand for the input follows the compliance it serves; payroll vendors build in accrual, A-2) | A-2, A-1 |
| C-39 | sellers.complements.medical | quantity_traded (medical visits by covered workers) | increase | short; medium | invisible | B | CR-9 (relation: paid time off complement to medical visits during working hours); CR-4 (workers: x: forgo or delay a visit, y: make it on paid time; y made better, A-N3); LW-10 | A-N3, A-1, A-2 |
| C-40 | sellers.substitutes.paid_care | quantity_traded (paid care for ill family members) | decrease | short; medium | invisible | B | CR-9 (relation: the worker's own care substitute for paid care; gift relation to the family member); CR-4 (x: pay for care and work, y: give care on paid time; C-30, A-N4) | A-N4, A-1, A-2 |
| C-41 | workers.uncovered | earnings | ambiguous | short | invisible | B | CR-12b: (+) CR-1 op 2 and CR-8b (absences that would have been unpaid, A-N5, are paid at the fixed wage, A-3); (−) CR-6 and CR-4c (jobs or hours cut where the wage cannot fall, C-9, C-13, A-7, A-3). No premise says which dominates | A-1, A-2, A-3, A-7, A-N5 |
| C-42 | workers.uncovered | earnings | ambiguous | medium; long | invisible | B | CR-12b: (+) paid absences (CR-8b, A-N5); (−) smaller raises (C-11, A-5); (−) fewer jobs or hours (C-9, C-12, A-7, A-6). No premise says which dominates | A-1, A-2, A-5, A-6, A-7, A-N5 |
| C-43 | workers.complainants | resources_available_other_uses | increase | short; medium; long | invisible | B | CR-8b (back pay plus an equal sum as damages adds to the complainant exactly what it takes from the employer; violations occur, A-16, and complaints are filed in meaningful numbers, A-21) | A-21, A-16 |
| C-44 | employers.violating | resources_available_other_uses | decrease | short; medium; long | invisible | B | CR-8b (the other side of C-43); CR-3c (a sum they cannot avoid once awarded) | A-21, A-16 |
| C-45 | employers.bound_uncovered | resources_available_other_uses | decrease | short | invisible | B | CR-8b (sick pay paid is received by workers, C-2); CR-8a and CR-3c (means used for sick pay, cover and compliance are not available for other uses; the term cannot be avoided for workers they keep, and wages are fixed, A-3) | A-1, A-2, A-3 |
| C-46 | taxpayers, recipients of other general-fund spending | resources_available_other_uses | at_least_one_decrease | short; medium; long | invisible | B | CR-8b (payers from the general budget: someone pays, but not who, so a group); CR-8a ($3.4 million a year of new money, A-20, withdrawn from other uses) | A-20 |

## Gaps found

**(a) Steps no core rule covers.**
- GAP-029-C1: The asymmetric cost per hour between part-time and full-time staff (C-17) rests on arithmetic on the 40-hour cap, then CR-4. No core rule says how a cap on a per-unit obligation changes the relative cost of units at different volumes; the step was done by arithmetic, which CR-12e names only as a dominance premise. Not a calculus gap in the strict sense, but the rules do not state where arithmetic on policy parameters is admissible outside CR-12e.
- GAP-029-C2: The medium-run total labor cost (C-16) needed the argument that, along the employer's own ranking, fewer hours are bought only at a higher total cost per hour. CR-12e's "a response cannot reverse the change that causes it" was stretched to cover it; no core rule states the mandated-term case (cost to one side against value to the other) directly. CR-5c gives the movement of both ends of the range, but not the result for the quantity traded unless the two movements are compared (A-6).

**(b) Core-rule wording that was hard to apply.**
- CR-12c: "different variables are never netted". Paid sick time and other non-wage terms are both `non_wage_compensation`. It is unclear whether two named items of one variable count as one variable (to be combined, giving ambiguous) or two (kept apart). Treated as two.
- CR-7b: the rule ranks shares by comparing alternatives, but for a mandated term the burden is gross or net of the worker's valuation (0.7 clarification), and the case assumption A-22 does not say which. C-15 is stated as a gross share.
- CR-6 "existing contracts count as regulated": used to sign the short-run wage as `no_change` (C-10). The rule does not say whether a pay scale or a habit of annual raises, as distinct from a written contract, counts.
- CR-10a and timing shifts: for the April 2027 start of use, the normal form asks for per-window signs, but whether medical visits are postponed into April needs a premise no case assumption gives; recorded as an unsigned path note.
- CR-1 recording rule: K1 is at once op 1 for employers (the old contract form removed) and op 2 for workers. The rule says to record both, which was done, but the link to `term_prevalence` as a variable is not stated anywhere.

**(c) Vocabulary missing from the ontology.**
- No variable for an employer's total labor cost per hour; `price_paid (labor ...)` was used for the employer as buyer of labor.
- No variable for absences or paid leave taken; `hours_worked` and `non_wage_compensation` were used.
- No variable for a size-class count of firms; `number_of_sellers (firms with fewer than six employees)` was used.
- No relation type for workers who share shifts at one employer (cover for an absent coworker); recorded through `substitute` for agency labor.
- No variable for accrued but unpaid balances (an employer liability and a worker asset that is lost on leaving).

## Comparison with the pattern-based analysis

**Summary.** The two versions agree on the structure of the sick leave case: paid sick time for the uncovered and a higher labor cost per hour at first, fewer hours present, at least one of jobs, hours or other benefits cut while wages are fixed and at the minimum wage, smaller raises above the minimum once raises are reset, fewer jobs or hours after that only on the premise that the term is worth less to workers than it costs (A-6), part-timers losing hours to full-timers with full-timers' hours ambiguous, hiring screened on expected use, the per-reading response at the size threshold, contractor arrangements, breach where complaints are unlikely, lock-in, lobbying, higher prices for local services, tradable production moving to Pellam, more agency cover, a capital loss for owners, workers bearing more of the cost in the medium run (gross of the term's value), and ambiguous earnings. No key is signed in opposite directions. The differences are of coverage and recording. The core version followed more relations (exempt rivals' asset values, buyers' quantities, medical visits, family care, payroll vendors), recorded both sides of every transfer the pattern version left in prose (sick pay, K6 awards), and signed per reading where the pattern version's 0.6 vocabulary had no `no_change`. The pattern version recorded three derivable claims the core version lacks: employers' short-run return on capital, workers' time spent on complaints, and an ambiguous total for non-wage compensation (a judgment call under CR-12c). The one core-only claim that is not valid as stated is employers' larger short-run share (C-14), which ranks shares under CR-7b without a premise, although CR-6 itself says the cost is pushed onto at least one open margin that workers bear. Both versions omit A-6 on the medium horizon of the local-services price, and the core version also omits it on its other medium-run product-market consequences. Many 0.7 clarifications the core version relied on were drawn from this very example's pattern version (CR-2 on the absence of an exchange, CR-6 on existing contracts, CR-7b on gross and net burdens, CR-12 on actions paid differently, `legal_breach`, `no_change`, `tax_share_borne` for mandates), so on those points the two versions are not independent, and pattern-version records that 0.7 has since superseded are counted as V, not as errors.

Counts: M 18, V 10, S 0, OP 19, OC 3.

### Pattern version → core version

| Pattern ID | Matched core ID(s) | Class | Cause | Note |
| --- | --- | --- | --- | --- |
| C-1 | C-2 | M | | Core also records `term_prevalence` (C-1), listed below. |
| C-2 | C-3 | M | | |
| C-3 | C-8 | M | | Pattern: hours present, short. Core: `hours_worked` for all horizons, with no qualifier separating presence from schedule. Same sign and premise (A-4). |
| C-4 | C-13, C-9 | V | | Pattern: one short-run group for all uncovered workers. Core splits it by wage: above the minimum (C-13, short) and at the minimum (C-9, all horizons). Core cites CR-6's 0.7 sentence on existing contracts, which was drawn from the pattern version's gap (b2). |
| C-5 | C-11 | M | | Core adds CR-3b for the worker side, as the pattern's section 5 also argues. |
| C-6 | C-12 | V | | Pattern group: employment, hours or other benefits (CR-5b, CR-12e, A-6). Core group: employment or hours only (CR-5c, CR-5a, A-6). The core's narrower group is valid and stronger. If the term costs more than it is worth, each pair's joint gain falls whatever term adjusts, so some marginal pairs stop exchanging. Both treat "could have agreed and did not" as a premise, as the 0.7 clarification to CR-2 now requires. |
| C-7 | C-9 | M | | Pattern cites PC-10; core derives the same group from CR-6 and CR-5c and extends it to the long run. |
| C-8 | C-17 | V | | Pattern: employment or hours of part-timers, as a group. Core: the class's `hours_worked`, single sign. This is valid if read as the class's total hours, which fall whether heads or hours are cut. The core mixes hours present (C-8) into the chain, which the pattern version deliberately kept apart. |
| C-9 | C-18 | M | | Both ambiguous. Different (+) and (−) lists: the pattern counts covering absent colleagues as a (+) chain (A-19), which the core omits, and the core counts paid absences as a (−) chain, which concern hours present rather than scheduled. The sign is unaffected. |
| C-10 | C-19 | M | | Core adds the short horizon. |
| C-11 | C-21 | M | | |
| C-12 | C-23 | M | | Pattern's classes include `employers.small`, which bear no term to avoid except through the threshold (covered by C-11 and core C-20 to C-22); the core's single class is the sounder one. |
| C-13 | C-5 | V | | Merged with pattern C-27 into one compliance-cost row for all covered employers. |
| C-14 | C-26 | M | | |
| C-15 | C-24 | V | | Pattern: `informal_activity` (the 0.6 list had nothing better; its gap (d5) proposed a new variable). Core: `legal_breach`, added in 0.7 from that proposal. |
| C-16 | C-28 | M | | |
| C-17 | C-31 | M | | Both omit A-6 on the medium horizon: once wages adjust, the price rise rests on part of the cost staying with employers. The pattern version says so in its text but does not list A-6. The core cites C-16 in the derivation but not its premises. |
| C-18 | C-35 | V | | `quantity_supplied` (long) against `quantity_traded` (medium; long). Pattern correctly lists A-6; core omits it (core-version error, sign unchanged). |
| C-19 | C-36 | V | | As C-18. |
| C-20 | C-33 | V | | `quantity_supplied` (medium) against `quantity_traded` (short; medium). Core's short horizon is valid on A-3; its medium horizon needs A-6, which it omits. |
| C-21 | C-37 | M | | |
| C-22 | C-29 | M | | Core dates the fall from introduction in January 2026, as CR-7c's probability clause implies. The pattern's "from passage" is narrower but has the same sign. |
| C-23 | none | OC | E | Employers' `return_on_capital` decrease, short (CR-7b: with wages fixed, A-3, the cost falls on means that cannot move). The core records the capitalized loss (C-29) and employers' means (C-45), but not the return. Core-version omission. |
| C-24 | C-15 | M | | Both gross shares, before the term's value to workers. The 0.7 clarification to CR-7b ("say whether gross or net") was drawn from the pattern version's gap (b3). |
| C-25 | none | OC | J | Pattern combines paid sick time and other benefits within `non_wage_compensation` to `ambiguous`. The core keeps the two named items apart under CR-12c and records no total (its gap (b)). CR-12c does not say whether named items of one variable are one variable, so both readings are defensible. |
| C-26 | C-42 | M | | Core extends it to the long run. |
| C-27 | C-5 | V | | As C-13. Pattern Tier A with no premise; core Tier B with A-2. Notices and records are owed whether or not employers comply with accrual, so the pattern's tier is defensible for that part. |
| C-28 | C-6 | M | | |
| C-29 | C-46 | V | | Pattern signs `taxpayers` alone (OC-3, OC-1). The core records taxpayers and recipients of other general-fund spending as a group with `at_least_one_decrease`, as the 0.7 clarification to CR-8 on payers from the general budget requires. The pattern version predates that clarification and overclaims for taxpayers alone. |
| C-30 | none | OC | E | Complainants' `compliance_cost` (time spent filing and pursuing complaints) increase (CR-8c with A-21). The core records complainants' receipts (C-43) but not their time. Core-version omission. |
| C-31 | C-16 | M | | Pattern: A-6 as an arithmetic dominance premise. Core: CR-12e (fewer hours are bought only at a higher full cost per hour, CR-4c) with A-6. Same sign and premise. |

### Core-only consequences

| Core ID | Class | Cause | Note |
| --- | --- | --- | --- |
| C-1 | OP | J | `term_prevalence` increase. Pattern recorded the term only as `non_wage_compensation` (its C-1). Recording choice. |
| C-4 | OP | E | Workers whose PTO failed the K2 conditions get looser conditions (CR-1 op 2, A-12). The pattern version recorded the employer's side (C-13) but not the worker's. Pattern-version omission. |
| C-7 | OP | E | Coverage at firms with six heads but fewer than six counted employees, `U2-a: increase; U2-b: no_change` (CR-1 per reading). Derivable. The pattern version's 0.6 vocabulary had no per-reading `no_change` (its gap (d6)), which partly explains the omission. |
| C-10 | OP | J | Above-minimum wage `no_change` in the short run (CR-6, existing contracts; A-3). The pattern version stated this in prose (section 4, A-3) without recording it, and 0.6 had neither `no_change` nor the CR-6 sentence. Recording choice. |
| C-14 | OP | E | Employers' `tax_share_borne` increase, short. Core-version error. CR-7b ranks shares only with a premise comparing alternatives. A-3 fixes the wage, but CR-6 (which the core cites) says the cost is pushed to at least one open margin (jobs, hours, other benefits; C-13), and workers bear those cuts. The core's own derivation ("except where they cut hours or jobs") names the missing premise. The pattern version said only that employers bear the cost "at first" and did not rank shares. |
| C-20 | OP | E | Near-threshold firms hire fewer employees of 20+ hours a week, under both readings (CR-4, CR-10a; A-10, A-N2). Valid. The pattern version recast C-11 on part-timers and dropped this. Pattern-version omission. |
| C-22 | OP | E | More firms with fewer than six employees (CR-4 with A-10). Derivable from the pattern's own premise. Pattern-version omission. |
| C-25 | OP | E | Breach by letting 2027 balances lapse, `U1-a: increase; U1-b: no_change` (CR-1 per reading, CR-4; A-16). The pattern version noted the risk in section 8 but did not record it, partly for want of `no_change`. Pattern-version omission. |
| C-27 | OP | A | Investment in labor-saving equipment increase. Rests on the new premise A-N1 (p 0.7) and A-6. The pattern version mentions automation only as an alternative in C-24. Valid given the premise. `investment_target` is defined for the target good, so the variable is stretched here. |
| C-30 | OP | A | Workers give more care to ill family members (`home_production`; CR-4, CR-5 gift clarification). Rests on new premise A-N4. Valid given it. |
| C-32 | OP | E | Buyers of local services buy less (CR-4c on C-31). RS-14 gives "price up and/or quantity down" and the pattern version recorded only the price. Pattern-version omission. Medium horizon needs A-6, as C-31. |
| C-34 | OP | E | Exempt and already-compliant rivals' asset values rise (CR-7c, CR-10c; A-13, A-24). Pattern-version omission: it applied capitalization to bound firms only (final check item 7). |
| C-38 | OP | J | Payroll compliance services sold increase. The pattern version stopped this chain as diffuse at depth 2. Depth choice. |
| C-39 | OP | A | Medical visits by covered workers increase (complement relation; new premise A-N3). The pattern version stopped it as health behavior, out of scope. The core treats it as an exchange through the complement relation, which CR-9 allows. Valid given the premise. |
| C-40 | OP | A | Paid care for ill relatives decreases (substitute relation; A-N4). As C-30. |
| C-41 | OP | E | Earnings of the uncovered, short, `ambiguous` (CR-12b). The pattern version recorded only the medium horizon. Pattern-version omission (CR-12g asks for one key per horizon). |
| C-43 | OP | E | Complainants' means rise by back pay and damages (CR-8b; A-16, A-21). The pattern version named the transfer in section 9 and declined to record it. Final check item 6 requires both sides. Pattern-version omission. |
| C-44 | OP | E | Violating employers' means fall (CR-8b, CR-3c). Other side of C-43. Pattern-version omission. |
| C-45 | OP | E | Bound employers' `resources_available_other_uses` decrease, short. CR-3's note is met: wages are fixed (A-3) and the term cannot be avoided for workers kept. The payer's side of sick pay, which the pattern version mentioned in section 2 without recording. Pattern-version omission. |

### Findings

- **Pattern overclaims or hidden premises.**
  1. C-29 signs `taxpayers` alone, which presumes the appropriation is met by taxes. CR-8b gives only a group of taxpayers and recipients of other spending, which is what the 0.7 clarification now records. The pattern version predates that clarification.
  2. C-17's medium horizon rests on A-6 (the pattern version's own text says the later price rise depends on part of the cost staying with employers), but A-6 is not in its assumption list.
  3. C-12 names `employers.small` among the classes that reclassify, although exempt firms bear no term to avoid except at the threshold.
- **Errors in the core version.**
  1. C-14 ranks employers' short-run share above workers' on A-3 alone. CR-7b needs a premise comparing the two sides, and CR-6 places part of the cost on workers through the open margins (C-13).
  2. A-6 (and A-5) are missing from the medium horizons of C-31, C-32, C-33, C-35 and C-36, all of which rest on labor costing more per hour after wages adjust (C-16). The signs survive with the premise added.
  3. Omissions of derivable claims: employers' short-run return on capital (pattern C-23) and complainants' time (pattern C-30).
  4. Smaller points: C-17 and C-18 mix hours present with hours scheduled, which the pattern version kept apart. C-18 omits the (+) chain of full-timers covering absent colleagues. C-27 stretches `investment_target`.
- **Errors in the pattern version.** Omissions only:
  1. The workers' side of the PTO rewrite (core C-4).
  2. Coverage and lapse breach per reading (C-7, C-25), partly blocked by the 0.6 vocabulary.
  3. Near-threshold firms' counted employees and the number of small firms (C-20, C-22).
  4. Buyers' quantity (C-32) and exempt rivals' asset values (C-34).
  5. Short-run earnings (C-41).
  6. Both sides of the K6 awards and the payer's side of sick pay (C-43 to C-45).

  `informal_activity` (C-15) and the single-class taxpayer row (C-29) are superseded by 0.7 vocabulary and clarifications, not errors under 0.6.
- **Limits of the core rules.** None produced a difference: every pattern-version claim the core lacks is derivable from CR-1 to CR-12, and every core-only claim is either derivable or rests on a flagged premise. The core version's GAP-029-C1 is not a limit: the extra accrual an hour of part-time work carries is what K1's op 3 attaches to each hour (CR-1), read from the policy's terms, not a dominance premise. GAP-029-C2 is covered by CR-12e as the core version applied it. One genuine unclear point remains: CR-12c does not say whether two named items of one variable (the mandated term and the benefits it displaces) are combined or kept apart, the source of the one J difference on a key both versions reached (pattern C-25). CR-5c still does not state the direction of the other terms under a mandated term (pattern gap (b1)), but the core version derived it from CR-5c, CR-3b and CR-6 without difficulty. Because several 0.7 clarifications (CR-2, CR-6, CR-7b, CR-12, `legal_breach`, `no_change`) were drawn from the pattern version of this example, the agreement on those points is not an independent test of them.
