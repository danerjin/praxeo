# WE-029 Paid sick leave mandate

Analyst: draft (Handbook 0.6)  |  Rule catalog version: 0.6  |  Status: awaiting expert review

A stylized policy in a fictional state. It resembles real paid sick leave laws but is not modeled on any one of them. It was chosen to probe a kind of policy the first 25 examples did not contain: a term the law writes into every private contract of a kind (here, employment), with no tax, subsidy or price control. The analysis works through CR-5c (the term moves the range of terms both sides accept), CR-7b (who pays, between wages and employment), group signs for the margins employers can adjust, workers for whom the term does not bind, the timing of sick-hour use, the hours at which accrual stops, a small-employer exemption and enforcement that waits for complaints. Health effects, including the spread of illness at work, are outside the scope of version 1. The probabilities are illustrative; the evidence column says what a real analysis would cite.

## 1. Policy record

**Varrow Healthy Workplaces Act.** The State of Varrow has about 6.2 million people and 2.7 million private-sector employees. Its largest city, Fenmouth, lies on the river that forms the border with the State of Pellam, which has no paid sick leave law; about 40,000 people commute across the river each day. Varrow's minimum wage is $13.50 an hour, indexed each year to consumer prices; about 9% of private employees earn at or near it. A survey by the state labor department found that about 62% of private employees already receive paid sick leave, or paid time off (PTO) that can be used for illness, and about 38% (about 1.0 million) do not. The uncovered are concentrated in food service, retail, personal care, agriculture and construction, and about 55% of them work part time. About 9% of private employees are covered by collective agreements that fix wages for one to three years.

The bill was introduced on 12 January 2026 with the governor's support, passed on 28 April 2026, signed on 15 May 2026, and takes effect on 1 January 2027. It has no expiry.

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Accrual and pay | Mandated contract term (`contract`: the employment contract; no type in 2.3) | Paid sick time | Covered employers | Every employee accrues one hour of paid sick time for every 30 hours worked, from the first hour of work or from 1 January 2027 for existing employees, up to 40 hours accrued in a calendar year. Paid at the employee's regular hourly rate. | K4, K5. Independent contractors, as defined by the state's existing classification test. Public employers. |
| K2 Use | Part of K1 | Conditions of use | Covered employers | For the employee's own illness, injury or medical care, or a family member's. Usable after 90 days of employment (existing employees: from 1 April 2027). In increments of one hour. Notice "as soon as practicable". The employer may require documentation only for absences of more than three consecutive scheduled workdays, may not require the employee to find a replacement, and may not count sick time as an absence under an attendance policy. | As K1 |
| K3 Carry-over | Part of K1 | Unused hours | Covered employers | Unused accrued hours carry over to the next calendar year. The employer may cap the balance at 80 hours and use at 40 hours a year. Unused hours are not paid out at separation; an employee rehired within six months gets the balance back. **K3 is enforced from 1 January 2028.** | As K1 |
| K4 Equivalent policies | Exemption from K1 to K3 | Employers with existing PTO | Covered employers | An employer whose policy provides at least 40 hours a year of paid time usable for the K2 purposes on the K2 conditions is deemed compliant. | — |
| K5 Small employers | Exemption from K1 to K3 | Employers with fewer than six employees | — | Size is the "average number of employees during the previous calendar year". | — |
| K6 Enforcement | Enforcement | K1 to K3 | Department of Labor Standards (DLS) | On complaint only, within two years of the violation; no routine audits. Remedies: back pay for sick time denied or unpaid, plus an equal sum as damages to the employee; civil penalty up to $1,000 for retaliation. Employers must post a notice and keep records for three years. A new appropriation of $3.4 million a year from the general fund pays for 25 investigators. | — |

Existing rules (in force in the counterfactual too):

| Rule | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| R1 Minimum wage | `price_floor` | Wages | Employers | $13.50 an hour, indexed yearly. | None relevant |
| R2 Classification test | Rule on contracts | Who is an employee and who an independent contractor | Employers | Existing three-part test; enforced on complaint and in tax audits. | — |

Unclear provisions:
- U1, carry-over in the first year. K3 "is enforced from 1 January 2028". Reading U1-a: hours accrued in 2027 and unused on 31 December 2027 must carry into 2028; only enforcement waits. Reading U1-b: K3 applies only to hours accrued from 2028, so an employer may let 2027 hours lapse at the end of the year.
- U2, counting employees for K5. The Act does not say whether part-time employees count. Reading U2-a: every person on the payroll counts as one. Reading U2-b: only employees who average 20 hours a week or more count (the definition in the state's unemployment insurance code, which K5 does not cite).

Readings get no probability; where a sign depends on one, each reading's sign is reported.

The counterfactual is Varrow without the Act, with the same minimum wage and classification rules.

## 2. Classification

| Component | Rothbard type | Binding? | Rule families |
|---|---|---|---|
| K1 to K3 | Triangular: forces a term into private employment contracts. By CR-1: for employers, removes the option of employing without paid sick time (operation 1) and attaches a cost to every hour of work (operation 3); for workers, removes the option of selling labor without it for a higher wage (operation 1) and adds the option of a paid absence (operation 2). The counterfactual law leaves sick pay to the contract. | For the 38% without equivalent leave (A-1). Not binding on pay for the 62% already covered, though some must change their policy's conditions (A-12). | CR-5, CR-4, CR-6, CR-7b, PC-10 (through R1), RS-1 to RS-8, RS-11, RS-14 |
| K4 | Exemption: a boundary between compliant and non-compliant leave policies | Yes | RS-5 |
| K5 | Exemption: a boundary at six employees | Yes | RS-5, RS-4 (in the sense of the favored side of a boundary) |
| K6 | Binary: funded by a new appropriation (A-20). Enforcement only on complaint, so for many employers the Act attaches a risk to non-compliance rather than removing the option (CR-1, Premises). | Yes | OC-3, RS-3 |

The Act collects no revenue and pays no subsidy. Every paid sick hour is paid by an employer to a worker (CR-8b): C-1 and C-2 are the two sides of that payment.

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `employers.uncovered` | Employers with six or more employees and no equivalent leave | Each hour of work now carries 1/30 of a paid sick hour, up to 40 hours a year per worker. |
| `employers.compliant` | Employers whose leave already meets K4, or nearly | Little changes, except conditions of use. |
| `employers.small` | Employers with fewer than six employees | Exempt; compete with bound employers. |
| `employers.near_threshold` | Employers with four to six employees | Each hire may cross the threshold, depending on U2. |
| `employers.tradable` | Bound employers selling against out-of-state producers (food processing, light manufacturing) | Higher labor cost than Pellam rivals. |
| `workers.uncovered` (`sellers.current`) | Employees of `employers.uncovered` | Gain paid sick time; their wages and hours may adjust. |
| `workers.min_wage` | Uncovered employees at or near $13.50 | Their money wage cannot fall. |
| `workers.part_time` | Uncovered employees working under 1,200 hours a year | Every hour they work carries accrual. |
| `workers.full_time` | Uncovered employees working more than 1,200 hours a year | Accrual stops at 40 hours, after 1,200 hours worked. |
| `workers.prospective` (`sellers.prospective`) | Job seekers | Employers' expected cost of a hire now depends on how much sick time the hire will use. |
| `workers.compliant_firms` | Employees already covered | Little changes. |
| `contractors` | Independent contractors | Outside the Act. |
| `staffing_agencies` (`intermediaries`) | Temporary and on-call staffing firms | Cover absent shifts; are themselves bound as employers. |
| `buyers.local_services` | Buyers of restaurant meals, retail, personal care, home care | Sellers' labor costs rise. |
| `neighboring_jurisdictions` | Pellam employers near Fenmouth | Not bound. |
| `officials.enforcement`, `taxpayers` | DLS and the general fund | Investigations on complaint. |

## 4. Direct effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | `workers.uncovered` | `non_wage_compensation` (paid sick time) | increase | short (from 2027) | CR-1, CR-5c | A-1, A-2 |
| C-2 | `employers.uncovered` | `price_paid` (labor cost per hour worked: wage plus accrued sick pay) | increase | short | CR-1, CR-5c, CR-8b | A-1, A-2, A-3 |

C-1 is what the Act's supporters point to. C-2 is the other side of the same payment: a full-time worker who uses all 40 hours is paid for 2,080 hours and works 2,040, so the cost of each hour worked rises by about 2%; for a part-timer who uses all accrued hours, by 1/30, about 3.3%. Whether workers use all of it is part of C-3. In the short run, money wages are fixed by posted pay scales, annual raise cycles and collective agreements (A-3, `contract`), so employers bear this at first.

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-3 | `workers.uncovered` | `hours_worked` (hours present at work, net of paid sick hours used) | decrease | short | CR-3b, CR-4 | A-1, A-2, A-4 |
| C-4 | `workers.uncovered` | `employment`, `hours_worked` (hours scheduled), `non_wage_compensation` (benefits other than sick time) | at_least_one_decrease | short | CR-5c, CR-4, CR-6 | A-1, A-2, A-3 |
| C-5 | `workers.uncovered` (above the minimum wage) | `wage_rate` | decrease | medium | CR-4, CR-6, CR-7b | A-1, A-2, A-5 |
| C-6 | `workers.uncovered` | `employment`, `hours_worked` (hours scheduled), `non_wage_compensation` (benefits other than sick time) | at_least_one_decrease | medium | CR-5b, CR-4, CR-12e | A-1, A-2, A-6 |
| C-7 | `workers.min_wage` | `employment`, `hours_worked` (hours scheduled), `non_wage_compensation` (benefits other than sick time) | at_least_one_decrease | short to medium | PC-10, CR-6 | A-1, A-2, A-7 |
| C-8 | `workers.part_time` | `employment`, `hours_worked` (hours scheduled) | at_least_one_decrease | medium | CR-4b, CR-4c | A-1, A-2, A-8 |
| C-9 | `workers.full_time` | `hours_worked` (hours scheduled) | ambiguous | medium | CR-4b, CR-4c, CR-12b | A-1, A-8, A-19 |
| C-10 | `workers.prospective` | `allocation_by_non_price_criteria` (hiring screened on expected use of sick time) | increase | medium | CR-6, CR-4, CR-11 | A-1, A-9 |
| C-11 | `employers.near_threshold` | `employment` (employees working under 20 hours a week at firms with four to six employees) | U2-a: decrease; U2-b: increase | medium | CR-4, RS-5 | A-10 |
| C-12 | `employers.small`, `employers.uncovered`, `contractors` | `reclassification` (work engaged as independent contracts) | increase | medium | RS-5 | A-1, A-11 |
| C-13 | `employers.compliant` | `compliance_cost` (rewriting PTO policies to meet the K2 conditions) | increase | short | CR-1, CR-8c | A-12 |
| C-14 | `workers.uncovered` | `job_changes` | decrease | medium | RS-11 | A-1, A-15 |
| C-15 | `employers.uncovered` | `informal_activity` (employment in breach of the Act: sick time not accrued, not paid or penalized) | increase | short to medium | CR-4, CR-1, RS-3 | A-1, A-16 |
| C-16 | `employers.small`, employer associations, unions, `employers.compliant` | `lobbying_effort` (small firms and restaurant associations to raise the threshold or delay K3; unions and compliant employers to extend the Act to small firms and raise the cap) | increase | medium | RS-7 | A-14 |

**What the term does to the bargain (C-4 to C-6).** Before the Act, any uncovered worker and employer could have agreed on paid sick time at a lower wage. For the employer, the term costs some amount per hour worked (c: the sick pay, plus covering the absent shift). For the worker, it is worth something (v), and v is not negative, because the term only adds an option: a paid absence (CR-3b). By CR-5c, the range of wages the employer accepts falls by c, and the range the worker accepts falls by v.
- **Wage (C-5).** Applying CR-4 to each side: at the old wage, employers want fewer hours of labor and workers offer at least as many. By CR-6, the wage falls. Both sides push it the same way, so the direction needs no comparison of v and c. It needs only that wages can move at the medium horizon, as raises are set (A-5).
- **Short run (C-4).** While wages are fixed (A-3), the whole of c falls on employers. They adjust the margins that are still open, at least one (CR-6, the terms that are not regulated): fewer hires, fewer scheduled hours, or less of other benefits (unpaid breaks rescheduled, bonuses, meal discounts, scheduling flexibility). Which ones is not licensed without a premise per margin, so they are recorded as a group.
- **Medium run (C-6).** Once wages adjust, employment and hours fall only if the wage falls by less than c, which holds if v is less than c for the marginal worker and employer. The Act's own record gives evidence for that: these pairs could have agreed on the term and did not (CR-2, CR-5b). That is a premise, not a certainty (A-6, p = 0.6), because the term may have been missing for other reasons. An employer who alone offers sick pay draws the applicants who expect to use it most, so its cost to that employer exceeds what it would cost under a rule that binds everyone (CR-11, CR-4). The dominance premise is therefore empirical (CR-12e). Without it, employment and hours are `ambiguous` and only C-5 stands.
- **At the minimum wage (C-7).** The wage cannot fall (R1), so all of c stays with employers at every horizon. PC-10 applies through the existing floor: employment, hours or other benefits, at least one, fall.

**Where accrual stops (C-8, C-9).** Accrual stops at 40 hours, which a worker reaches after 1,200 hours. A full-timer's hours beyond 1,200 carry no further sick-time cost, while every hour a part-timer works carries 1/30 of an hour. So, for employers, an extra hour from an existing full-timer has become cheaper than an hour from a new part-timer (CR-4b, x: hire another part-timer, y: give more hours to existing full-timers). Part-timers lose hours to full-timers, and the general rise in cost lowers hours too (CR-4c): both chains reduce part-timers' hours or jobs (C-8). For full-timers, the shift adds hours, and so does covering colleagues' absences (C-3, A-19), while the general cost rise subtracts them, so their scheduled hours are `ambiguous` (C-9; section 7). The same move appeared in WE-012, at the contribution ceiling.

**Hours present (C-3).** A paid absence is now cheaper for the worker than an unpaid one (CR-4, x: work, y: take a paid sick hour). Some who would have worked while ill stay home, and since documentation may be asked only after three days, some hours are taken for other ends. Hours present fall. This is a different quantity from the hours employers schedule (C-4, C-6, C-8, C-9); section 7 says how they relate.

**Selection (C-10).** The term is the same for every worker, but its cost to the employer varies with how much sick time each will use. Pay cannot be set worker by worker to match (posted scales, anti-discrimination law), so the employer, choosing among applicants, uses other criteria (CR-6: the scarce side chooses by other criteria), screening on whatever predicts use (A-9).

**The size threshold (C-11, C-12).** K5 draws a line at six employees, averaged over the previous year. A firm at five that adds a sixth person takes on the term for everyone (CR-4, x: hire, y: stay exempt). Under U2-a every head counts, so firms near the line hire fewer part-timers; under U2-b, employees under 20 hours do not count, so firms near the line hire short-hour part-timers in place of a sixth longer-hour employee (C-11). Under either reading, some work is moved to contractor arrangements, outside the Act (C-12, RS-5), where the classification test is weakly enforced (A-11).

**Lock-in (C-14).** A balance of up to 80 hours is lost on leaving (K3), and a new job brings a 90-day wait (K2). Both make a job change cost more (RS-11). They apply from 2027, but carry-over raises the stake from 2028.

**Complaint-only enforcement (C-15).** DLS acts only on complaints. For an employer, breaking the Act brings back pay and equal damages only if a worker complains, so the expected penalty is the probability of a complaint times the remedy (CR-1: the rule attaches a risk; CR-4, x: comply, y: violate). That probability is lowest for workers who stay a short time, do not know the law, fear retaliation, or for whom the sums are small (A-16). Breach is therefore concentrated where workers are least able to complain, so the Act binds least where coverage was lowest. The trade stays in the legal labor market, and the only variable that fits is `informal_activity` (Gaps found, d).

Not reported: employers ending seasonal and temporary engagements before 90 days, so that workers never reach the point of using their hours (`turnover` increase). A-23 is below the cut-off (p = 0.4), because replacing a worker costs more than 40 hours of sick pay in most such jobs.

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-17 | `buyers.local_services` | `price_paid` (restaurant meals, retail service, personal and home care) | increase | short to medium | RS-14, CR-9 | labor `input_to` local services | A-1, A-2, A-3, A-17 |
| C-18 | `employers.tradable` | `quantity_supplied` (output produced in Varrow) | decrease | long | RS-14, RS-6, RS-4 | Varrow and Pellam producers: `across_border`, close near Fenmouth | A-6, A-18 |
| C-19 | `neighboring_jurisdictions` (Pellam employers) | `quantity_supplied` (goods and services sold into Varrow) | increase | medium to long | RS-4 | as C-18 | A-6, A-18 |
| C-20 | `employers.compliant`, `employers.small` | `quantity_supplied` | increase | medium | CR-9, CR-7a | their output and that of `employers.uncovered`: `substitute`, partial | A-6, A-13 |
| C-21 | `staffing_agencies` | `quantity_traded` (temporary and on-call staffing to cover absences) | increase | short | CR-9 | agency labor and absent employees' hours: `substitute`, close in shift work | A-1, A-4, A-19 |
| C-22 | `employers.uncovered` (owners) | `asset_value` (labor-intensive businesses employing uncovered staff) | decrease | short (from passage) | CR-7c, CR-10c | — | A-1, A-3, A-24 |
| C-23 | `employers.uncovered` | `return_on_capital` | decrease | short | CR-7b | — | A-1, A-2, A-3 |
| C-24 | `workers.uncovered` | `tax_share_borne` (share of the term's cost borne, workers compared with employers) | increase | medium to long | CR-7b | `contract` (employment) | A-5, A-22 |

C-17: where the competitors of a local seller are also bound (A-17), the higher labor cost raises prices (RS-14). In the short run this rests on fixed wages (A-3); later, on part of the cost staying with employers. C-18 and C-19: where competitors are in Pellam, the quantity effect dominates instead, and production moves across the river over time (RS-4, RS-6). Both rest on A-6, that wages do not absorb the whole cost.

C-20: compliant and exempt firms now face rivals with higher costs (CR-9). Their own costs are unchanged, so they gain sales.

C-21: shift-based employers must fill absent shifts (C-3). Those who use agencies buy more agency labor. Agencies are themselves bound to provide sick time to their own workers (K1), which raises their price; that chain is not followed (depth 3).

C-22 and C-23: until wages adjust, the cost falls on employers' returns (C-23). Where a business's value rests on its expected earnings, the fall for the years before wages adjust is capitalized when the Act becomes expected, borne by owners at that time (CR-7c, a change of limited duration). In the long run returns are equalized across uses (CR-7a), so no lasting change in return is signed.

C-24, who pays (CR-7b). Nearly every employer of six or more in Varrow is bound, so a worker cannot escape the term by changing employer. Their alternatives are exempt small firms, contracting, or a job in Pellam. Employers can redeploy capital, automate or move across the river over time. With the premise that workers' alternatives are clearly worse (A-22), workers bear more of the cost than employers, through the wage (C-5), and their share grows as capital redeploys. Here "bears" means pays, before counting what the term is worth to them (C-1); the method does not compare that value with what they pay (Gaps found, b).

Stopping points: C-17 leads to the buyers' other spending (depth 3), a diffuse effect; stopped, because buyers' total spending on these services may rise or fall (CR-3, note). Medical providers seeing more patients during working hours: the link runs through health behavior, out of scope. Payroll software firms: depth 2, diffuse; stopped.

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `workers.full_time`, `hours_worked` (scheduled), medium | Hours beyond 1,200 carry no accrual, so hours shift from part-timers to them (CR-4b, A-8); covering absent colleagues (C-3, A-19). | The cost of labor as a whole rises (C-2, CR-4c); wages fall at most partly (A-6). | None | **ambiguous** (C-9). Decided by how much of employers' labor is part time, and how much of c the wage absorbs. |
| `workers.uncovered`, `hours_worked`, short to medium | None. | Hours present fall as paid sick hours are used (C-3); hours scheduled fall, in the group with employment and other benefits (C-4, C-6), and for part-timers (C-8). | None needed | The chains measure **different quantities**: hours at work net of absence (C-3) and hours on the schedule (C-4, C-6, C-8, C-9). The controlled list has only `hours_worked` (Gaps found, d). Read as hours present, the combined sign is a decrease for part-timers and for the class as a whole, and `ambiguous` for full-timers (C-9's + chains against C-3). |
| `workers.uncovered`, `non_wage_compensation` (total, including sick time), short to medium | Paid sick time (C-1). | Other benefits may be cut (C-4, C-6, C-7), at least as one member of a group. | None | **ambiguous** (C-25). The variable cannot keep the mandated term apart from the benefits it may displace (Gaps found, d). |
| `workers.uncovered`, `earnings`, medium | Pay for sick hours not worked (C-1). | Lower wages (C-5); fewer jobs or hours (C-6, C-7, C-8). | None | **ambiguous** (C-26). |
| `employers.uncovered`, `price_paid` (labor cost per hour worked), medium | The mandated cost (C-2). | Lower wages (C-5). | A-6 (arithmetic once v is less than c: the wage falls by less than c) | **increase** (C-31), extending C-2 to the medium horizon under A-6 (p = 0.6). Without A-6, `ambiguous`. |
| `workers.min_wage`, `wage_rate`, medium | — | — | — | **Not signed.** The floor holds the wage (R1); the cost goes to C-7's margins. |
| `employers.uncovered`, `return_on_capital`, long | — | — | CR-7a | **Not signed**: returns are equalized across uses in the long run. |

## 8. Time structure

- **Announcement to effective date (January to December 2026).** Employers set their 2027 raises and benefit plans knowing the Act is coming (CR-10a), so wage restraint (C-5) can begin with the first pay round after passage, before any sick hour is accrued. Business values move at passage (C-22). Firms near six employees manage their 2026 average, because K5 counts the previous year (C-11). Compliant employers rewrite policies (C-13).
- **2027: accrual ramps up.** Existing employees cannot use hours before 1 April 2027 and accrue one hour per 30 worked, so a full-timer has about 17 hours in April and reaches 40 hours around the end of July. Hours present (C-3) fall a little in the first quarter and more through the year. Agency demand (C-21) follows.
- **End of 2027, under each reading of U1.** Under U1-b, 2027 hours lapse on 31 December, so workers use them in November and December. Under U1-a, they carry over and the end-of-year bunching does not happen. Under both readings, hours present are below the counterfactual in every window (C-3), so the bunching moves use within the decrease and is a path note (CR-12h), not a separate signed consequence. Employers who read the Act as U1-b and are wrong face back-pay claims from 2028 within the two-year window.
- **2028 on: carry-over.** Balances of up to 80 hours raise the cost of leaving a job (C-14), and workers about to quit use their balance first, because it is not paid out. That again moves use in time within a decrease; it is a path note.
- **Wages adjust over years.** In the short run employers bear the cost (C-2, C-4, C-23). As raises are set lower (C-5), the burden moves toward workers (C-24), and further as capital redeploys (CR-7b, with CR-10b). Relocation to Pellam (C-18, C-19) and contractor arrangements (C-12) grow slowly.
- **Erosion.** The 40-hour cap and the 1/30 rate are not money amounts, so they do not erode with prices. The size threshold is a count of employees and does not move.

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-27 | `employers.uncovered` | `compliance_cost` (tracking accrual, payroll changes, records kept three years, notices, responding to complaints) | increase | What that staff time and software would otherwise have done. | OC-2, CR-8c |
| C-28 | `officials.enforcement` | `enforcement_cost` | increase | Investigating complaints. | OC-3 |
| C-29 | `taxpayers` | `resources_available_other_uses` | decrease | What the $3.4 million a year would otherwise have funded. | OC-3, OC-1 |
| C-30 | `workers.uncovered` | `compliance_cost` (time spent filing and pursuing complaints) | increase | The other uses of that time. | OC-2, CR-8c |

The jobs and hours not exchanged under C-4, C-6 and C-7 are prevented exchanges (OC-4): workers and employers both lose the gain each expected from them. They are recorded in those groups, not again here.

Back pay and the equal damages paid after a successful complaint are transfers from employers to workers (CR-8b). How often they are paid depends on complaints (A-21), and they are not recorded as their own consequence.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | About 38% of private employees lack paid leave usable for illness, so the term binds for them. | binding | 0.9 | State labor department survey; benefit surveys by industry. | Most consequences shrink to the uncovered share that remains. |
| A-2 | Most bound employers comply: payroll vendors build in accrual, and some workers complain. | enforcement | 0.7 | Payroll vendors' compliance features; complaint rates under comparable laws. | C-1 to C-9 are smaller; C-15 is larger. |
| A-3 | Money wages are fixed in the short run by pay scales, annual raises and collective agreements. | other | 0.8 | Raise cycles; collective agreements cover 9%. | C-2, C-4, C-17, C-22 and C-23 are smaller; the wage adjusts at once. |
| A-4 | Some uncovered workers would have worked while ill, or will use paid hours for other ends, and documentation rules make this hard to police. | other | 0.9 | Surveys on working while ill; K2's three-day documentation rule. | C-3 and C-21 are not reported. |
| A-5 | Wages above the minimum can adjust over the medium horizon, as raises are set. | other | 0.8 | Wage growth in these industries is well above zero, so raises can be smaller without nominal cuts. | C-5 and C-24 are not reported. |
| A-6 | For the marginal worker and employer, the term is worth less to the worker than it costs the employer: they could have agreed on it and did not. | other | 0.6 | The term was absent for 38%; against this, selection of high users by employers who alone offer it (section 5). | C-6, C-18 and C-19 are not reported; the medium-run labor cost row in section 7 is `ambiguous`; employment and hours are `ambiguous`. |
| A-7 | The minimum wage binds for some uncovered workers. | binding | 0.85 | 9% of private employees earn at or near $13.50, mostly in uncovered industries. | C-7 is not reported. |
| A-8 | Employers can move hours between part-time and full-time staff. | other | 0.7 | Shift scheduling in retail and food service. | C-8 weakens to the cost chain alone; the + chain in C-9 vanishes. |
| A-9 | Employers can infer expected use of sick time from what they see of applicants, and cannot set pay worker by worker to match it. | other | 0.55 | Hiring practice; posted pay scales; anti-discrimination law. | C-10 is not reported. |
| A-10 | Some firms near six employees value staying exempt more than an extra hire. | other | 0.6 | Count of firms with four to six employees; their margins. | C-11 is not reported. |
| A-11 | The classification test is weakly enforced in some occupations, so contractor arrangements are open to some employers. | enforcement | 0.55 | Audit rates; occupations where contracting is common. | C-12 is not reported. |
| A-12 | Some existing PTO policies do not meet the K2 conditions (documentation, notice, increments, attendance points). | other | 0.8 | Sample of employee handbooks. | C-13 is not reported. |
| A-13 | Compliant and small firms compete in product markets with uncovered firms. | substitutability | 0.6 | Industry overlap: many restaurants and shops in each class. | C-20 is not reported. |
| A-14 | Small-business and restaurant associations, unions and compliant employers can organize at a cost below their stake. | other | 0.85 | Existing associations and their activity on the bill. | C-16 is not reported. |
| A-15 | Some job changes are marginal enough that losing a balance and waiting 90 days decides them. | mobility | 0.55 | Job-to-job moves in these industries; the size of the balance compared with a wage gain. | C-14 is not reported. |
| A-16 | Complaints are unlikely for some workers: short tenure, unaware of the law, fearing retaliation, or owed small sums. | enforcement | 0.8 | Complaint-based enforcement elsewhere; tenure in these industries. | C-15 is not reported. |
| A-17 | Most competitors of local service sellers are bound too (in Varrow, six or more employees). | other | 0.7 | Size distribution of restaurants, shops and care agencies. | C-17 weakens; small exempt rivals hold prices down. |
| A-18 | Varrow's tradable producers compete with Pellam producers, who are not bound. | mobility | 0.65 | Plants on both sides of the river near Fenmouth; shipping costs. | C-18 and C-19 are not reported. |
| A-19 | Shift-based employers cover absent shifts, partly through agencies and on-call staff. | other | 0.65 | Staffing practice in care, retail and food service. | C-21 is not reported; the second + chain in C-9 vanishes. |
| A-20 | The $3.4 million is new money from the general fund. | revenue_use | 0.9 | K6. | C-29 is not reported; other DLS work falls instead (OC-3, fixed budget). |
| A-21 | Complaints are filed in meaningful numbers. | enforcement | 0.85 | Complaint volumes under comparable laws. | C-30 is not reported. |
| A-22 | Over the medium to long run, workers' alternatives to bound employment (small firms, contracting, Pellam) are clearly worse than employers' alternatives (automation, redeployment, Pellam). | mobility | 0.6 | Share of employment in bound firms; commuting to Pellam is open only near Fenmouth. | C-24 is not reported; the split is not signed. |
| A-23 | Employers end seasonal and temporary engagements before 90 days to avoid use. | other | 0.4 | Replacement costs compared with 40 hours of sick pay. | Below the cut-off; not reported. |
| A-24 | Labor-intensive businesses are valued on expected earnings, and buyers expect the short-run cost before wages adjust. | expectations | 0.7 | Business sale prices as multiples of earnings. | C-22 is not reported. |

## 11. Report

**The policy.** From January 2027, Varrow requires every employer with six or more employees to give each employee one paid sick hour for every 30 hours worked, up to 40 hours a year, usable after 90 days, with documentation only for absences over three days. Unused hours carry over (enforced from 2028), up to a balance of 80 hours, and are not paid out on leaving. Employers whose leave policy already meets these terms are deemed compliant. Enforcement waits for workers' complaints.

**Visible consequences.** About a million workers who had no paid sick time now get it (C-1), and their employers pay for it (C-2).

**Invisible consequences.**
- *Wages and jobs.* As raises are set, wages of the newly covered grow less than they would have (C-5). Before wages adjust, employers cut at least one of hiring, scheduled hours or other benefits (C-4). If, as the absence of the term suggests, it was worth less to these workers than it costs, employers keep doing so after wages adjust (C-6). At the minimum wage, where the wage cannot fall, they must (C-7). Over time, workers bear more of the cost than employers do (C-24).
- *Part-timers and full-timers.* Accrual stops after 1,200 hours, so an extra hour from a full-timer now costs an employer less than an hour from a part-timer. Part-timers lose hours or jobs (C-8); for full-timers the net effect on hours is ambiguous (C-9).
- *Hiring.* Employers screen applicants on how much sick time they are likely to use (C-10).
- *The threshold.* Near six employees, firms avoid crossing the line. Under one reading of how part-timers are counted they hire fewer of them; under the other they hire more short-hour ones (C-11). Some work moves to contractor arrangements (C-12).
- *Use and absence.* Workers are present for fewer hours (C-3), employers buy more temporary cover (C-21), and workers change jobs a little less, to keep their balances (C-14).
- *Enforcement.* Because only complaints trigger enforcement, breaches are concentrated among workers least able to complain (C-15).
- *Other markets.* Local services cost more (C-17). Tradable production moves partly to Pellam over time (C-18, C-19). Compliant and exempt firms gain sales (C-20). Owners of labor-intensive businesses see their value fall at passage (C-22), and their returns fall until wages adjust (C-23).
- *Costs.* Employers' record-keeping and handling of complaints (C-27), compliant employers' policy changes (C-13), enforcement and its funding (C-28, C-29), workers' time spent on complaints (C-30), and lobbying over the threshold and the cap (C-16).

**Ambiguous effects.** Full-timers' scheduled hours (C-9); covered workers' total non-wage compensation (C-25) and total earnings (C-26). Not signed: the wage of minimum-wage workers, which the floor holds, and employers' long-run returns.

**Key conditions.** The term binds for about 38% (A-1, p = 0.9). Whether employment and hours fall after wages adjust rests on the term being worth less to the worker than it costs the employer (A-6, p = 0.6), the premise on which the most depends. Who bears the cost rests on workers' alternatives being worse than employers' (A-22, p = 0.6). Compliance rests on payroll practice and complaints (A-2, p = 0.7).

**What this analysis cannot say.** How large any effect is; whether the value of paid sick time to the workers who get it outweighs what they and others give up for it; how much each employer margin is used; any effect on health, including the spread of illness at work and in schools (out of scope for version 1); whether the policy is desirable.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | workers.uncovered | non_wage_compensation (paid sick time) | increase | short | visible | B | CR-1, CR-5c | A-1, A-2 |
| C-2 | employers.uncovered | price_paid (labor cost per hour worked) | increase | short | visible | B | CR-1, CR-5c, CR-8b | A-1, A-2, A-3 |
| C-3 | workers.uncovered | hours_worked (hours present) | decrease | short | invisible | B | CR-3b, CR-4 | A-1, A-2, A-4 |
| C-4 | workers.uncovered | employment, hours_worked (scheduled), non_wage_compensation (other benefits) | at_least_one_decrease | short | invisible | B | CR-5c, CR-4, CR-6 | A-1, A-2, A-3 |
| C-5 | workers.uncovered (above minimum wage) | wage_rate | decrease | medium | invisible | B | CR-4, CR-6, CR-7b | A-1, A-2, A-5 |
| C-6 | workers.uncovered | employment, hours_worked (scheduled), non_wage_compensation (other benefits) | at_least_one_decrease | medium | invisible | B | CR-5b, CR-4, CR-12e | A-1, A-2, A-6 |
| C-7 | workers.min_wage | employment, hours_worked (scheduled), non_wage_compensation (other benefits) | at_least_one_decrease | short–medium | invisible | B | PC-10, CR-6 | A-1, A-2, A-7 |
| C-8 | workers.part_time | employment, hours_worked (scheduled) | at_least_one_decrease | medium | invisible | B | CR-4b, CR-4c | A-1, A-2, A-8 |
| C-9 | workers.full_time | hours_worked (scheduled) | ambiguous | medium | invisible | B | CR-4b, CR-4c, CR-12b | A-1, A-8, A-19 |
| C-10 | workers.prospective | allocation_by_non_price_criteria (screening on expected use) | increase | medium | invisible | B | CR-6, CR-4, CR-11 | A-1, A-9 |
| C-11 | employers.near_threshold | employment (under 20 hours a week) | U2-a: decrease; U2-b: increase | medium | invisible | B | CR-4, RS-5 | A-10 |
| C-12 | employers.small, employers.uncovered, contractors | reclassification (contractor arrangements) | increase | medium | invisible | B | RS-5 | A-1, A-11 |
| C-13 | employers.compliant | compliance_cost (rewriting PTO policies) | increase | short | invisible | B | CR-1, CR-8c | A-12 |
| C-14 | workers.uncovered | job_changes | decrease | medium | invisible | B | RS-11 | A-1, A-15 |
| C-15 | employers.uncovered | informal_activity (employment in breach of the Act) | increase | short–medium | invisible | B | CR-4, CR-1, RS-3 | A-1, A-16 |
| C-16 | employers.small, associations, unions, employers.compliant | lobbying_effort | increase | medium | invisible | B | RS-7 | A-14 |
| C-17 | buyers.local_services | price_paid (local services) | increase | short–medium | invisible | B | RS-14, CR-9 | A-1, A-2, A-3, A-17 |
| C-18 | employers.tradable | quantity_supplied (in Varrow) | decrease | long | invisible | B | RS-14, RS-6, RS-4 | A-6, A-18 |
| C-19 | neighboring_jurisdictions | quantity_supplied (into Varrow) | increase | medium–long | invisible | B | RS-4 | A-6, A-18 |
| C-20 | employers.compliant, employers.small | quantity_supplied | increase | medium | invisible | B | CR-9, CR-7a | A-6, A-13 |
| C-21 | staffing_agencies | quantity_traded (temporary cover) | increase | short | invisible | B | CR-9 | A-1, A-4, A-19 |
| C-22 | employers.uncovered (owners) | asset_value (labor-intensive businesses) | decrease | short | invisible | B | CR-7c, CR-10c | A-1, A-3, A-24 |
| C-23 | employers.uncovered | return_on_capital | decrease | short | invisible | B | CR-7b | A-1, A-2, A-3 |
| C-24 | workers.uncovered | tax_share_borne (cost of the mandated term) | increase | medium–long | invisible | B | CR-7b | A-5, A-22 |
| C-25 | workers.uncovered | non_wage_compensation (total, including sick time) | ambiguous | short–medium | invisible | B | CR-12b | A-1, A-2 |
| C-26 | workers.uncovered | earnings | ambiguous | medium | invisible | B | CR-12b | A-1, A-2, A-5 |
| C-27 | employers.uncovered | compliance_cost (accrual tracking, records, complaints) | increase | short | invisible | A | OC-2, CR-8c | none |
| C-28 | officials.enforcement | enforcement_cost | increase | short | invisible | A | OC-3 | none |
| C-29 | taxpayers | resources_available_other_uses | decrease | short | invisible | B | OC-3, OC-1 | A-20 |
| C-30 | workers.uncovered | compliance_cost (filing complaints) | increase | short–medium | invisible | B | OC-2, CR-8c | A-21 |
| C-31 | employers.uncovered | price_paid (labor cost per hour worked) | increase | medium | invisible | B | CR-5c, CR-12e | A-1, A-2, A-6 |

## Gaps found

**(a) Calculus gaps (a step no core rule covers).** None. Every step was derived from CR-1 to CR-12 or from patterns whose preconditions held. The step closest to a gap was why a term the parties could have agreed on was missing (section 5, C-6). The core rules give two answers, demonstrated preference (CR-2, CR-5b) and selection by the better-informed side (CR-11 with CR-4), but no way to choose between them, so the choice is an empirical premise (A-6). That is the method working as intended, not a gap.

**(b) Unclear core rules.**
1. *CR-5c gives the range, not the direction of the terms.* CR-5c says that a change in what one party must give "moves that range", but not which way the remaining terms move when the law fixes one term for both sides. Getting the wage's direction (C-5) took three rules: CR-4 for each side's schedule, CR-6 for the price, and CR-12 for the quantity, which is ambiguous when both schedules move. A sentence in CR-5c would help: when a fixed term costs one party c and is worth v ≥ 0 to the other, the other terms move against the party it benefits, and the quantity exchanged falls only if v < c.
2. *CR-6's "terms that are not regulated" in the short run.* It was not obvious that CR-6 licenses C-4. The money wage is not regulated by the Act, but it is fixed in the short run by contract (A-3), so the pressure goes to other margins. CR-6 should say that terms fixed by existing contracts count, for their duration, as regulated terms (the `contract` relation).
3. *CR-7b, "bears", for a term that benefits the side that pays.* CR-7b ranks who bears a burden by comparing alternatives. With a mandated term, the side that pays through a lower wage (workers) also receives the term. C-24 records the share of the cost borne, not net of the term's value, and the rule does not say which is meant. It also does not say what counts as an alternative when every employer in reach is bound: here, only the boundaries (small firms, contracting, Pellam).
4. *CR-5b as a dominance premise.* CR-5b covers compelled transfers. Using "they could have agreed and did not" as evidence that v < c is an application of CR-2 (demonstrated preference) to an exchange that did not take place. The core rules do not say when the absence of an exchange counts as demonstrated preference, and when it reflects an obstacle (selection, information, the cost of negotiating terms one by one). A note under CR-2 or CR-5 is needed.
5. *CR-12h and 2.5, timing within a decrease.* Use of sick time bunches before the end of 2027 (under U1-b) and before quitting. Both shifts move a paid absence that would not exist without the Act, but absence as such does exist without it. Is that "an action that also takes place without the policy" (signed per window) or not (a path note)? Here every window has the same sign, so CR-12h settles it as a path note, but the test in 2.5 does not say how to identify "the same action" when the policy changes how it is paid.

**(c) Missing patterns.**
1. *Mandated contract term (proposed PC-17 or a new family).* If a policy requires a term in every contract of a kind that costs one party c per unit and is worth v ≥ 0 to the other, then: the money price moves against the party the term benefits (`wage_rate` decrease) where it can move; while it cannot (contracts, a floor), the party that pays adjusts the other open terms, as a group with `at_least_one_decrease`; once the price adjusts, quantity falls only with a premise that v < c, otherwise `ambiguous`; at a binding floor, PC-10 applies through the floor. Derivation: CR-1 (an option removed for both sides, one added for the beneficiary), CR-3b (v ≥ 0), CR-4 for each side, CR-5c, CR-6, CR-12b and CR-12e.
2. *A uniform term with costs that differ by counterparty (proposed RS-18).* If a policy fixes a term that must be the same for all counterparties, but its cost to the provider differs by counterparty and the price cannot be set to match, then the provider selects counterparties on whatever predicts cost: `allocation_by_non_price_criteria` increase. Derivation: CR-4 for the provider, CR-6 (the scarce side chooses by other criteria). It covers insurance rating bans and lending rules as well.
3. *A cost per head that stops at a cap (proposed RS-19).* If a policy's cost per counterparty rises with units up to a cap and then stops (a contribution ceiling, an accrual cap), units move toward counterparties already above the cap: more units per head for those, fewer heads, and the opposite for those below. Derivation: CR-4b, with x: add a head, y: add units to an existing head above the cap, against CR-4c for the general rise in cost. It recurred here (C-8, C-9) and in WE-012 (C-4).
4. *Complaint-driven enforcement (proposed RS-20).* If a rule is enforced only on complaint by the protected party, then breach is concentrated where complaint is least likely (short tenure, ignorance of the law, fear of retaliation, small sums), and the rule binds least for those parties. Derivation: CR-1 (the rule attaches a risk equal to the probability of a complaint times the remedy) and CR-4 (x: comply, y: violate), applied counterparty by counterparty.
5. *Size thresholds (proposed RS-5 clause).* An exemption by firm size, measured over a past period, gives firms near the line a reason to manage the measure (heads, hours, contractors) in that period. RS-5 covers this in general; a clause naming size thresholds and how the count is defined would prompt it. Derivation: CR-4 (x: cross the line, y: stay below) with CR-10a when the count is over a past period.

**(d) Vocabulary.**
1. *Instrument type.* 2.3 has no type for a mandated contract term (sick leave, notice periods, required insurance cover, warranty terms). K1 is recorded as "Mandated contract term (no type in 2.3)". Proposed: `mandated_contract_term`, triangular, with the `contract` relation it acts on.
2. *Hours present and hours scheduled.* `hours_worked` cannot tell hours paid but not worked (absence) from hours scheduled. The analysis needed both (section 7). Proposed: `absence_hours`, or a split into `hours_paid` and `hours_worked`.
3. *The mandated term and the benefits it displaces.* `non_wage_compensation` holds both the mandated sick time (C-1, up) and the other benefits employers may cut (C-4, C-6, down), which forced a separate ambiguous total (C-25).
4. *Who bears a mandate's cost.* `tax_share_borne` is defined for taxes. C-24 uses it for the cost of a mandated term. Proposed: widen it to "share of the burden of a tax or mandate borne", or add `cost_share_borne`.
5. *Breach within the legal market.* `informal_activity` means trade outside the legal market. Breach of a mandated term (C-15) takes place within legal employment. Proposed: `noncompliance`, the share of bound actors not complying.
6. *Per-reading "no change".* The first candidate for C-11 was hours per worker at firms near the threshold, which rise under U2-a (fewer heads, more hours each) and have no reason to change under U2-b. There is no per-reading sign for "no effect under this reading" (see WE-028, Gaps found, d4), so C-11 was recast on a variable with a sign under both readings.
