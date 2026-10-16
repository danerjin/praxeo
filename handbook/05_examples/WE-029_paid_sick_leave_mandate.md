# WE-029 Paid sick leave mandate

Analyst: draft (Handbook 0.6, corrected under 0.8)  |  Rule catalog version: 0.8  |  Status: awaiting expert review

A stylized policy in a fictional state. It resembles real paid sick leave laws but is not modeled on any one of them. It was chosen to probe a kind of policy the first 25 examples did not contain: a term the law writes into every private contract of a kind (here, employment), with no tax, subsidy or price control. The analysis works through CR-5c (the term moves the range of terms both sides accept), CR-7b (who pays, between wages and employment), group signs for the margins employers can adjust, workers for whom the term does not bind, the timing of sick-hour use, the hours at which accrual stops, a small-employer exemption and enforcement that waits for complaints. Health effects, including the spread of illness at work, are outside the scope of version 1. The probabilities are illustrative; the evidence column says what a real analysis would cite.

## 1. Policy record

**Varrow Healthy Workplaces Act.** The State of Varrow has about 6.2 million people and 2.7 million private-sector employees. Its largest city, Fenmouth, lies on the river that forms the border with the State of Pellam, which has no paid sick leave law; about 40,000 people commute across the river each day. Varrow's minimum wage is $13.50 an hour, indexed each year to consumer prices; about 9% of private employees earn at or near it. A survey by the state labor department found that about 62% of private employees already receive paid sick leave, or paid time off (PTO) that can be used for illness, and about 38% (about 1.0 million) do not. The uncovered are concentrated in food service, retail, personal care, agriculture and construction, and about 55% of them work part time. About 9% of private employees are covered by collective agreements that fix wages for one to three years.

The bill was introduced on 12 January 2026 with the governor's support, passed on 28 April 2026, signed on 15 May 2026, and takes effect on 1 January 2027. It has no expiry.

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Accrual and pay | `mandated_contract_term` (`contract`: the employment contract) | Paid sick time | Covered employers | Every employee accrues one hour of paid sick time for every 30 hours worked, from the first hour of work or from 1 January 2027 for existing employees, up to 40 hours accrued in a calendar year. Paid at the employee's regular hourly rate. | K4, K5. Independent contractors, as defined by the state's existing classification test. Public employers. |
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
| K1 to K3 | Triangular: forces a term into private employment contracts. By CR-1: for employers, removes the option of employing without paid sick time (operation 1) and attaches a cost to every hour of work (operation 3); for workers, removes the option of selling labor without it for a higher wage (operation 1) and adds the option of a paid absence (operation 2). The counterfactual law leaves sick pay to the contract. | For the 38% without equivalent leave (A-1). Not binding on pay for the 62% already covered, though some must change their policy's conditions (A-12). | PC-17, CR-5, CR-4, CR-6, CR-7b, PC-10 (through R1), RS-1 to RS-8, RS-11, RS-14, RS-18 (the accrual cap) |
| K4 | Exemption: a boundary between compliant and non-compliant leave policies | Yes | RS-5 |
| K5 | Exemption: a boundary at six employees | Yes | RS-17, RS-5 |
| K6 | Binary: funded by a new appropriation from the general fund (A-20). Enforcement only on complaint, so for many employers the Act attaches a risk to non-compliance rather than removing the option (CR-1, Premises). | Yes | OC-3, OC-1 (payers from the general budget are a group), RS-3 |

The Act collects no revenue and pays no subsidy. Every paid sick hour is paid by an employer to a worker (CR-8b): C-1 and C-2 are the two sides of that payment, and C-42 records the payer's means while wages are fixed. Back pay and damages under K6 are likewise transfers from employers to complainants (C-40, C-41).

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
| `workers.pto_noncompliant` | Employees whose existing PTO does not meet the K2 conditions | Get the K2 conditions of use. |
| `workers.size_ambiguous` | Employees of firms with six or more on the payroll but fewer than six employees averaging 20 hours a week | Covered under U2-a only. |
| `workers.complainants`, `employers.violating` | Workers who complain and win; employers found in breach | Back pay and an equal sum as damages pass from the second to the first. |
| `contractors` | Independent contractors | Outside the Act. |
| `staffing_agencies` (`intermediaries`) | Temporary and on-call staffing firms | Cover absent shifts; are themselves bound as employers. |
| `buyers.local_services` | Buyers of restaurant meals, retail, personal care, home care | Sellers' labor costs rise. |
| `neighboring_jurisdictions` | Pellam employers near Fenmouth | Not bound. |
| `officials.enforcement` | DLS | Investigations on complaint. |
| `taxpayers`, recipients of other general-fund spending | Those who fund the $3.4 million appropriation | One or more of them gives up what it would otherwise have funded. |

## 4. Direct effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | `workers.uncovered` | `non_wage_compensation` (paid sick time) | increase | short (from 2027) | CR-1, CR-5c | A-1, A-2 |
| C-2 | `employers.uncovered` | `price_paid` (labor cost per hour worked: wage plus accrued sick pay) | increase | short | CR-1, CR-5c, CR-8b | A-1, A-2, A-3 |

C-1 is what the Act's supporters point to. C-2 is the other side of the same payment: a full-time worker who uses all 40 hours is paid for 2,080 hours and works 2,040, so the cost of each hour worked rises by about 2%; for a part-timer who uses all accrued hours, by 1/30, about 3.3%. Whether workers use all of it is part of C-3. In the short run, money wages are fixed by posted pay scales, annual raise cycles and collective agreements (A-3, `contract`), so employers bear this at first. Most of these contracts have no fixed term, so their stickiness is a premise with a probability, not a rule (CR-6, 0.8 clarification on existing contracts).

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-3 | `workers.uncovered` | `hours_worked` (hours present at work, net of paid sick hours used) | decrease | short | CR-3b, CR-4 | A-1, A-2, A-4 |
| C-4 | `workers.uncovered` | `employment`, `hours_worked` (hours scheduled), `non_wage_compensation` (benefits other than sick time) | at_least_one_decrease | short | PC-17, CR-5c, CR-4, CR-6 | A-1, A-2, A-3 |
| C-5 | `workers.uncovered` (above the minimum wage) | `wage_rate` | decrease | medium | PC-17, CR-4, CR-6, CR-7b | A-1, A-2, A-5 |
| C-6 | `workers.uncovered` | `employment`, `hours_worked` (hours scheduled), `non_wage_compensation` (benefits other than sick time) | at_least_one_decrease | medium | PC-17, CR-2, CR-5c, CR-4, CR-12e | A-1, A-2, A-6 |
| C-7 | `workers.min_wage` | `employment`, `hours_worked` (hours scheduled), `non_wage_compensation` (benefits other than sick time) | at_least_one_decrease | short to medium | PC-10, CR-6 | A-1, A-2, A-7 |
| C-8 | `workers.part_time` | `employment`, `hours_worked` (hours scheduled) | at_least_one_decrease | medium | RS-18, CR-4b, CR-4c | A-1, A-2, A-8 |
| C-9 | `workers.full_time` | `hours_worked` (hours scheduled) | ambiguous | medium | RS-18, CR-4b, CR-4c, CR-12b | A-1, A-8, A-19 |
| C-10 | `workers.prospective` | `allocation_by_non_price_criteria` (hiring screened on expected use of sick time) | increase | medium | CR-6, CR-4, CR-11 | A-1, A-9 |
| C-11 | `employers.near_threshold` | `employment` (employees working under 20 hours a week at firms with four to six employees) | U2-a: decrease; U2-b: increase | medium | RS-17, CR-4, CR-10a | A-10 |
| C-12 | `employers.uncovered`, `contractors` | `reclassification` (work engaged as independent contracts) | increase | medium | RS-5 | A-1, A-11 |
| C-13 | `employers.compliant` | `compliance_cost` (rewriting PTO policies to meet the K2 conditions) | increase | short | CR-1, CR-8c | A-12 |
| C-14 | `workers.uncovered` | `job_changes` | decrease | medium | RS-11 | A-1, A-15 |
| C-15 | `employers.uncovered` | `legal_breach` (employment in breach of the Act: sick time not accrued, not paid or penalized) | increase | short to medium | CR-4, CR-1, RS-3 | A-1, A-16 |
| C-16 | `employers.small`, employer associations, unions, `employers.compliant` | `lobbying_effort` (small firms and restaurant associations to raise the threshold or delay K3; unions and compliant employers to extend the Act to small firms and raise the cap) | increase | medium | RS-7 | A-14 |
| C-32 | `workers.pto_noncompliant` | `non_wage_compensation` (conditions of use of existing PTO: no documentation for short absences, no replacement requirement, no attendance points) | increase | short | CR-1, CR-5c | A-2, A-12 |
| C-33 | `workers.size_ambiguous` | `non_wage_compensation` (paid sick time) | U2-a: increase; U2-b: no_change | short | CR-1 | A-1, A-2 |
| C-34 | `employers.near_threshold` | `employment` (employees averaging 20 hours a week or more, at firms with four to six employees) | decrease | short (from mid-2026) to medium | RS-17, CR-4, CR-10a | A-10, A-25 |
| C-35 | `employers.small` | `number_of_sellers` (firms with fewer than six employees) | increase | medium | RS-17, CR-4, CR-7a | A-10 |
| C-36 | `employers.uncovered` | `legal_breach` (2027 balances not carried into 2028) | U1-a: increase; U1-b: no_change | medium (2028) | CR-1, CR-4, RS-3 | A-16 |

**What the term does to the bargain (C-4 to C-6).** Before the Act, any uncovered worker and employer could have agreed on paid sick time at a lower wage. For the employer, the term costs some amount per hour worked (c: the sick pay, plus covering the absent shift). For the worker, it is worth something (v), and v is not negative, because the term only adds an option: a paid absence (CR-3b). By CR-5c, the range of wages the employer accepts falls by c, and the range the worker accepts falls by v.
- **Wage (C-5).** Applying CR-4 to each side: at the old wage, employers want fewer hours of labor and workers offer at least as many. By CR-6, the wage falls. Both sides push it the same way, so the direction needs no comparison of v and c. It needs only that wages can move at the medium horizon, as raises are set (A-5).
- **Short run (C-4).** While wages are fixed (A-3), the whole of c falls on employers. They adjust the margins that are still open, at least one (CR-6, the terms that are not regulated): fewer hires, fewer scheduled hours, or less of other benefits (unpaid breaks rescheduled, bonuses, meal discounts, scheduling flexibility). Which ones is not licensed without a premise per margin, so they are recorded as a group.
- **Medium run (C-6).** Once wages adjust, employment and hours fall only if the wage falls by less than c, which holds if v is less than c for the marginal worker and employer. The Act's own record gives evidence for that: these pairs could have agreed on the term and did not. By the 0.7 clarification to CR-2, the absence of an exchange shows only that no pair found it worth agreeing on in the situation as it was; whether that reflects their rankings or an obstacle is a premise (A-6, p = 0.6). An employer who alone offers sick pay draws the applicants who expect to use it most, so its cost to that employer exceeds what it would cost under a rule that binds everyone (CR-11, CR-4). The dominance premise is therefore empirical (CR-12e). Without it, employment and hours are `ambiguous` and only C-5 stands.
- **Recording (PC-17).** PC-17 gives the adjustment of the other terms as a group; here every member moves the same way, so the group signs `at_least_one_decrease` (C-4, C-6, C-7), with the wage signed on its own where it can move (C-5).
- **At the minimum wage (C-7).** The wage cannot fall (R1), so all of c stays with employers at every horizon. PC-10 applies through the existing floor: employment, hours or other benefits, at least one, fall.

**Where accrual stops (C-8, C-9).** Accrual stops at 40 hours, which a worker reaches after 1,200 hours. A full-timer's hours beyond 1,200 carry no further sick-time cost, while every hour a part-timer works carries 1/30 of an hour. So, for employers, an extra hour from an existing full-timer has become cheaper than an hour from a new part-timer (CR-4b, x: hire another part-timer, y: give more hours to existing full-timers). Part-timers lose hours to full-timers, and the general rise in cost lowers hours too (CR-4c): both chains reduce part-timers' hours or jobs (C-8). For full-timers, the shift adds hours, and so does covering colleagues' absences (C-3, A-19), while the general cost rise subtracts them, so their scheduled hours are `ambiguous` (C-9; section 7). The same move appeared in WE-012, at the contribution ceiling.

**Hours present (C-3).** A paid absence is now cheaper for the worker than an unpaid one (CR-4, x: work, y: take a paid sick hour). Some who would have worked while ill stay home, and since documentation may be asked only after three days, some hours are taken for other ends. Hours present fall. This is a different quantity from the hours employers schedule (C-4, C-6, C-8, C-9); section 7 says how they relate.

**Selection (C-10).** The term is the same for every worker, but its cost to the employer varies with how much sick time each will use. Pay cannot be set worker by worker to match (posted scales, anti-discrimination law), so the employer, choosing among applicants, uses other criteria (CR-6: the scarce side chooses by other criteria), screening on whatever predicts use (A-9).

**The size threshold (C-11, C-12).** K5 draws a line at six employees, averaged over the previous year. A firm at five that adds a sixth person takes on the term for everyone (CR-4, x: hire, y: stay exempt). Under U2-a every head counts, so firms near the line hire fewer part-timers; under U2-b, employees under 20 hours do not count, so firms near the line hire short-hour part-timers in place of a sixth longer-hour employee (C-11). Under either reading, employees of 20 hours or more count, so firms near the line hire fewer of them (C-34), starting in 2026, because the 2026 average decides 2027 status (RS-17, CR-10a; A-25); and some firms that would have grown past five stay below six (C-35). Under U2-a, workers at firms with six or more on the payroll but fewer than six counted employees are covered; under U2-b they are not, and nothing changes for them (C-33). Under either reading, some work is moved to contractor arrangements, outside the Act (C-12, RS-5), where the classification test is weakly enforced (A-11).

**Lock-in (C-14).** A balance of up to 80 hours is lost on leaving (K3), and a new job brings a 90-day wait (K2). Both make a job change cost more (RS-11). They apply from 2027, but carry-over raises the stake from 2028.

**Complaint-only enforcement (C-15).** DLS acts only on complaints. For an employer, breaking the Act brings back pay and equal damages only if a worker complains, so the expected penalty is the probability of a complaint times the remedy (CR-1: the rule attaches a risk; CR-4, x: comply, y: violate). That probability is lowest for workers who stay a short time, do not know the law, fear retaliation, or for whom the sums are small (A-16). Breach is therefore concentrated where workers are least able to complain, so the Act binds least where coverage was lowest. The trade stays in the legal labor market, so it is recorded as `legal_breach` (0.7), not `informal_activity`. Under U1-a, letting 2027 balances lapse at the end of the year is a further breach, and some employers do it where complaints are unlikely (C-36, A-16); under U1-b it is lawful, so there is no change.

**Existing PTO (C-13, C-32).** Where an employer's PTO relied on conditions K2 forbids (documentation for short absences, finding a replacement, attendance points), the employer rewrites it (C-13), and its workers gain the looser conditions (C-32, CR-1 operation 2).

Not reported: employers ending seasonal and temporary engagements before 90 days, so that workers never reach the point of using their hours (`turnover` increase). A-23 is below the cut-off (p = 0.4), because replacing a worker costs more than 40 hours of sick pay in most such jobs.

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-17 | `buyers.local_services` | `price_paid` (restaurant meals, retail service, personal and home care) | increase | short to medium | RS-14, CR-9 | labor `input_to` local services | A-1, A-2, A-3, A-6, A-17 |
| C-18 | `employers.tradable` | `quantity_supplied` (output produced in Varrow) | decrease | long | RS-14, RS-6, RS-4 | Varrow and Pellam producers: `across_border`, close near Fenmouth | A-6, A-18 |
| C-19 | `neighboring_jurisdictions` (Pellam employers) | `quantity_supplied` (goods and services sold into Varrow) | increase | medium to long | RS-4 | as C-18 | A-6, A-18 |
| C-20 | `employers.compliant`, `employers.small` | `quantity_supplied` | increase | medium | CR-9, CR-7a | their output and that of `employers.uncovered`: `substitute`, partial | A-6, A-13 |
| C-21 | `staffing_agencies` | `quantity_traded` (temporary and on-call staffing to cover absences) | increase | short | CR-9 | agency labor and absent employees' hours: `substitute`, close in shift work | A-1, A-4, A-19 |
| C-22 | `employers.uncovered` (owners) | `asset_value` (labor-intensive businesses employing uncovered staff) | decrease | short (from the bill's introduction, fully at signing) | CR-7c, CR-10c | — | A-1, A-3, A-24 |
| C-23 | `employers.uncovered` | `return_on_capital` | decrease | short | CR-7b | — | A-1, A-2, A-3 |
| C-24 | `workers.uncovered` | `tax_share_borne` (gross share of the term's cost borne, workers compared with employers) | increase | medium to long | CR-7b | `contract` (employment) | A-5, A-22 |
| C-37 | `buyers.local_services` | `quantity_traded` (restaurant meals, retail service, personal and home care from bound sellers) | decrease | short to medium | RS-14, CR-4c, CR-5a | as C-17 | A-1, A-2, A-3, A-6, A-17 |
| C-38 | `employers.compliant`, `employers.small` (owners) | `asset_value` (firms competing with bound, uncovered firms) | increase | short (from the bill's introduction) | CR-7c, CR-10c | as C-20 | A-3, A-13, A-24 |

C-17 and C-37: where the competitors of a local seller are also bound (A-17), the higher labor cost raises prices (RS-14), and buyers give up the units they value least (C-37, CR-4c). In the short run this rests on fixed wages (A-3); at the medium horizon, on part of the cost staying with employers after wages adjust (A-6). C-18 and C-19: where competitors are in Pellam, the quantity effect dominates instead, and production moves across the river over time (RS-4, RS-6). Both rest on A-6, that wages do not absorb the whole cost.

C-20 and C-38: compliant and exempt firms now face rivals with higher costs (CR-9). Their own costs are unchanged, so they gain sales, and the expected gain is capitalized in their value when the Act becomes expected (C-38, CR-7c), as the loss is for bound firms (C-22).

C-21: shift-based employers must fill absent shifts (C-3). Those who use agencies buy more agency labor. Agencies are themselves bound to provide sick time to their own workers (K1), which raises their price; that chain is not followed (depth 3).

C-22 and C-23: until wages adjust, the cost falls on employers' returns (C-23). Where a business's value rests on its expected earnings, the fall for the years before wages adjust is capitalized when the Act becomes expected, borne by owners at that time (CR-7c, a change of limited duration): part of the way from the bill's introduction in January 2026, as passage became likely, and the rest at signing. In the long run returns are equalized across uses (CR-7a), so no lasting change in return is signed.

C-24, who pays (CR-7b). Nearly every employer of six or more in Varrow is bound, so a worker cannot escape the term by changing employer. Their alternatives are exempt small firms, contracting, or a job in Pellam. Employers can redeploy capital, automate or move across the river over time. With the premise that workers' alternatives are clearly worse (A-22), workers bear more of the cost than employers, through the wage (C-5), and their share grows as capital redeploys. Here "bears" means the gross share, before counting what the term is worth to them (C-1), as the 0.7 clarification to CR-7 asks the analysis to say; the method does not compare that value with what they pay.

Stopping points: C-17 leads to the buyers' other spending (depth 3), a diffuse effect; stopped, because buyers' total spending on these services may rise or fall (CR-3, note). Medical providers seeing more patients during working hours: the link runs through health behavior, out of scope. Payroll software firms: depth 2, diffuse; stopped.

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `workers.full_time`, `hours_worked` (scheduled), medium | Hours beyond 1,200 carry no accrual, so hours shift from part-timers to them (CR-4b, A-8); covering absent colleagues (C-3, A-19). | The cost of labor as a whole rises (C-2, CR-4c); wages fall at most partly (A-6). | None | **ambiguous** (C-9). Decided by how much of employers' labor is part time, and how much of c the wage absorbs. |
| `workers.uncovered`, `hours_worked`, short to medium | None. | Hours present fall as paid sick hours are used (C-3); hours scheduled fall, in the group with employment and other benefits (C-4, C-6), and for part-timers (C-8). | None needed | The chains measure **different quantities**: hours at work net of absence (C-3) and hours on the schedule (C-4, C-6, C-8, C-9). The controlled list has only `hours_worked` (Gaps found, d). Read as hours present, the combined sign is a decrease for part-timers and for the class as a whole, and `ambiguous` for full-timers (C-9's + chains against C-3). |
| `workers.uncovered`, `non_wage_compensation` (total, including sick time), short to medium | Paid sick time (C-1). | Other benefits may be cut (C-4, C-6, C-7), at least as one member of a group. | CR-12b | **ambiguous** (C-25). Recorded as CR-12's 0.8 clarification on two items in one variable asks: each item as its own consequence (sick time in C-1; other benefits as members of the groups in C-4, C-6 and C-7), and the total separately, combined under (b). |
| `workers.uncovered`, `earnings`, short | Pay for sick hours that would otherwise have been unpaid absences (C-1, A-26). | Fewer jobs or hours while wages are fixed (C-4, C-7). | None | **ambiguous** (C-39). |
| `workers.uncovered`, `earnings`, medium | Pay for sick hours that would otherwise have been unpaid absences (C-1, A-26). | Lower wages (C-5); fewer jobs or hours (C-6, C-7, C-8). | None | **ambiguous** (C-26). |
| `employers.uncovered`, `price_paid` (labor cost per hour worked), medium | The mandated cost (C-2). | Lower wages (C-5). | A-6 (arithmetic once v is less than c: the wage falls by less than c) | **increase** (C-31), extending C-2 to the medium horizon under A-6 (p = 0.6). Without A-6, `ambiguous`. |
| `workers.min_wage`, `wage_rate`, medium | — | — | — | **Not signed.** The floor holds the wage (R1); the cost goes to C-7's margins. |
| `employers.uncovered`, `return_on_capital`, long | — | — | CR-7a | **Not signed**: returns are equalized across uses in the long run. |

## 8. Time structure

- **Announcement to effective date (January to December 2026).** Employers set their 2027 raises and benefit plans knowing the Act is coming (CR-10a), so wage restraint (C-5) can begin with the first pay round after passage, before any sick hour is accrued. Business values move from the bill's introduction, as passage becomes likely, and fully at signing (C-22, C-38). Firms near six employees manage their 2026 average, because K5 counts the previous year (C-11, C-34). Compliant employers rewrite policies (C-13).
- **2027: accrual ramps up.** Existing employees cannot use hours before 1 April 2027 and accrue one hour per 30 worked, so a full-timer has about 17 hours in April and reaches 40 hours around the end of July. Hours present (C-3) fall a little in the first quarter and more through the year. Agency demand (C-21) follows.
- **End of 2027, under each reading of U1.** Under U1-b, 2027 hours lapse on 31 December, so workers use them in November and December. Under U1-a, they carry over and the end-of-year bunching does not happen. Under both readings, hours present are below the counterfactual in every window (C-3), so the bunching moves use within the decrease and is a path note (CR-12h), not a separate signed consequence. The paid absence itself is a change in kind from the unpaid absence it replaces, recorded separately as C-1 (CR-12, 0.7 clarification). Employers who read the Act as U1-b and are wrong are in breach under U1-a (C-36) and face back-pay claims from 2028 within the two-year window.
- **2028 on: carry-over.** Balances of up to 80 hours raise the cost of leaving a job (C-14), and workers about to quit use their balance first, because it is not paid out. That again moves use in time within a decrease; it is a path note.
- **Wages adjust over years.** In the short run employers pay the higher cost per hour (C-2, C-23, C-42), while the open margins pass part of it to workers (C-4); no ranking of shares is made for this horizon. As raises are set lower (C-5), the burden moves toward workers (C-24), and further as capital redeploys (CR-7b, with CR-10b). Relocation to Pellam (C-18, C-19) and contractor arrangements (C-12) grow slowly.
- **Erosion.** The 40-hour cap and the 1/30 rate are not money amounts, so they do not erode with prices. The size threshold is a count of employees and does not move.

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-27 | `employers.uncovered` | `compliance_cost` (tracking accrual, payroll changes, records kept three years, notices, responding to complaints) | increase | What that staff time and software would otherwise have done. | OC-2, CR-8c |
| C-28 | `officials.enforcement` | `enforcement_cost` | increase | Investigating complaints. | OC-3 |
| C-29 | `taxpayers`, recipients of other general-fund spending | `resources_available_other_uses` | at_least_one_decrease | What the $3.4 million a year would otherwise have funded: lower taxes or other spending. The record names no tax, so the payers are a group. | OC-3, OC-1 |
| C-30 | `workers.uncovered` | `compliance_cost` (time spent filing and pursuing complaints) | increase | The other uses of that time. | OC-2, CR-8c |
| C-40 | `workers.complainants` | `resources_available_other_uses` | increase | Nothing given up: back pay plus an equal sum as damages is a receipt (CR-8b). | CR-8b |
| C-41 | `employers.violating` | `resources_available_other_uses` | decrease | What the back pay and damages would otherwise have bought; a sum they cannot avoid once awarded. | CR-8b, CR-3c |
| C-42 | `employers.uncovered` (those keeping their staff and hours) | `resources_available_other_uses` | decrease | What the sick pay and cover for absent shifts would otherwise have bought. With wages fixed (A-3), the term cannot be avoided for the workers and hours kept (CR-3, note). | OC-1, CR-8a, CR-8b, CR-3c |

The jobs and hours not exchanged under C-4, C-6 and C-7 are prevented exchanges (OC-4): workers and employers both lose the gain each expected from them. They are recorded in those groups, not again here.

Back pay and the equal damages paid after a successful complaint are transfers from employers to workers (CR-8b), recorded on both sides (C-40, C-41); they rest on violations (A-16) and complaints (A-21). Sick pay itself is recorded on both sides too: the workers' receipt within C-1 and earnings (C-39, C-26), the employers' outlay in C-2 and C-42. The appropriation is paid by the group in C-29.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | About 38% of private employees lack paid leave usable for illness, so the term binds for them. | binding | 0.9 | State labor department survey; benefit surveys by industry. | Most consequences shrink to the uncovered share that remains. |
| A-2 | Most bound employers comply: payroll vendors build in accrual, and some workers complain. | enforcement | 0.7 | Payroll vendors' compliance features; complaint rates under comparable laws. | C-1 to C-9, C-32, C-33 and C-42 are smaller; C-15 is larger. |
| A-3 | Money wages are fixed in the short run by pay scales, annual raises and collective agreements. | other | 0.8 | Raise cycles; collective agreements cover 9%. | C-2, C-4, C-17, C-22, C-23, C-37, C-38 and C-42 are smaller; the wage adjusts at once. |
| A-4 | Some uncovered workers would have worked while ill, or will use paid hours for other ends, and documentation rules make this hard to police. | other | 0.9 | Surveys on working while ill; K2's three-day documentation rule. | C-3 and C-21 are not reported. |
| A-5 | Wages above the minimum can adjust over the medium horizon, as raises are set. | other | 0.8 | Wage growth in these industries is well above zero, so raises can be smaller without nominal cuts. | C-5 and C-24 are not reported. |
| A-6 | For the marginal worker and employer, the term is worth less to the worker than it costs the employer: they could have agreed on it and did not. | other | 0.6 | The term was absent for 38%; against this, selection of high users by employers who alone offer it (section 5). | C-6, C-18 and C-19 are not reported, nor C-17 and C-37 at the medium horizon; the medium-run labor cost row in section 7 is `ambiguous`; employment and hours are `ambiguous`. |
| A-7 | The minimum wage binds for some uncovered workers. | binding | 0.85 | 9% of private employees earn at or near $13.50, mostly in uncovered industries. | C-7 is not reported; one (−) chain of C-39 weakens. |
| A-8 | Employers can move hours between part-time and full-time staff. | other | 0.7 | Shift scheduling in retail and food service. | C-8 weakens to the cost chain alone; the + chain in C-9 vanishes. |
| A-9 | Employers can infer expected use of sick time from what they see of applicants, and cannot set pay worker by worker to match it. | other | 0.55 | Hiring practice; posted pay scales; anti-discrimination law. | C-10 is not reported. |
| A-10 | Some firms near six employees value staying exempt more than an extra hire. | other | 0.6 | Count of firms with four to six employees; their margins. | C-11, C-34 and C-35 are not reported. |
| A-11 | The classification test is weakly enforced in some occupations, so contractor arrangements are open to some employers. | enforcement | 0.55 | Audit rates; occupations where contracting is common. | C-12 is not reported. |
| A-12 | Some existing PTO policies do not meet the K2 conditions (documentation, notice, increments, attendance points). | other | 0.8 | Sample of employee handbooks. | C-13 and C-32 are not reported. |
| A-13 | Compliant and small firms compete in product markets with uncovered firms. | substitutability | 0.6 | Industry overlap: many restaurants and shops in each class. | C-20 and C-38 are not reported. |
| A-14 | Small-business and restaurant associations, unions and compliant employers can organize at a cost below their stake. | other | 0.85 | Existing associations and their activity on the bill. | C-16 is not reported. |
| A-15 | Some job changes are marginal enough that losing a balance and waiting 90 days decides them. | mobility | 0.55 | Job-to-job moves in these industries; the size of the balance compared with a wage gain. | C-14 is not reported. |
| A-16 | Complaints are unlikely for some workers: short tenure, unaware of the law, fearing retaliation, or owed small sums. | enforcement | 0.8 | Complaint-based enforcement elsewhere; tenure in these industries. | C-15 and C-36 are not reported; C-40 and C-41 fail. |
| A-17 | Most competitors of local service sellers are bound too (in Varrow, six or more employees). | other | 0.7 | Size distribution of restaurants, shops and care agencies. | C-17 and C-37 weaken; small exempt rivals hold prices down. |
| A-18 | Varrow's tradable producers compete with Pellam producers, who are not bound. | mobility | 0.65 | Plants on both sides of the river near Fenmouth; shipping costs. | C-18 and C-19 are not reported. |
| A-19 | Shift-based employers cover absent shifts, partly through agencies and on-call staff. | other | 0.65 | Staffing practice in care, retail and food service. | C-21 is not reported; the second + chain in C-9 vanishes. |
| A-20 | The $3.4 million is new money from the general fund. | revenue_use | 0.9 | K6. | C-29 is not reported; other DLS work falls instead (OC-3, fixed budget). |
| A-21 | Complaints are filed in meaningful numbers. | enforcement | 0.85 | Complaint volumes under comparable laws. | C-30, C-40 and C-41 are not reported. |
| A-22 | Over the medium to long run, workers' alternatives to bound employment (small firms, contracting, Pellam) are clearly worse than employers' alternatives (automation, redeployment, Pellam). | mobility | 0.6 | Share of employment in bound firms; commuting to Pellam is open only near Fenmouth. | C-24 is not reported; the split is not signed. |
| A-23 | Employers end seasonal and temporary engagements before 90 days to avoid use. | other | 0.4 | Replacement costs compared with 40 hours of sick pay. | Below the cut-off; not reported. |
| A-24 | Labor-intensive businesses are valued on expected earnings, and buyers expect the short-run cost before wages adjust. | expectations | 0.7 | Business sale prices as multiples of earnings. | C-22 and C-38 are not reported. |
| A-25 | Owners of firms near six employees know from mid-2026 that the 2026 average decides their 2027 status. | expectations | 0.7 | Act signed 15 May 2026; associations' guidance; payroll vendors' notices. | C-34 and the 2026 part of C-11 start in 2027 instead. |
| A-26 | Some uncovered workers would have taken unpaid absences for illness without the Act. | other | 0.95 | Absence rates in uncovered industries. | The (+) chains of C-26 and C-39 fail, and earnings become a decrease. |

## 11. Report

**The policy.** From January 2027, Varrow requires every employer with six or more employees to give each employee one paid sick hour for every 30 hours worked, up to 40 hours a year, usable after 90 days, with documentation only for absences over three days. Unused hours carry over (enforced from 2028), up to a balance of 80 hours, and are not paid out on leaving. Employers whose leave policy already meets these terms are deemed compliant. Enforcement waits for workers' complaints.

**Visible consequences.** About a million workers who had no paid sick time now get it (C-1), and their employers pay for it (C-2).

**Invisible consequences.**
- *Wages and jobs.* As raises are set, wages of the newly covered grow less than they would have (C-5). Before wages adjust, employers cut at least one of hiring, scheduled hours or other benefits (C-4). If, as the absence of the term suggests, it was worth less to these workers than it costs, employers keep doing so after wages adjust (C-6). At the minimum wage, where the wage cannot fall, they must (C-7). Over time, workers bear more of the cost than employers do, before counting what the term is worth to them (C-24). Until wages adjust, employers who keep their staff and hours have less to spend on other things (C-42), and workers' total earnings may rise or fall (C-39, C-26).
- *Part-timers and full-timers.* Accrual stops after 1,200 hours, so an extra hour from a full-timer now costs an employer less than an hour from a part-timer. Part-timers lose hours or jobs (C-8); for full-timers the net effect on hours is ambiguous (C-9).
- *Hiring.* Employers screen applicants on how much sick time they are likely to use (C-10).
- *The threshold.* Near six employees, firms avoid crossing the line: they hire fewer employees of 20 hours or more, from 2026 (C-34), and more firms stay below six (C-35). Under one reading of how part-timers are counted they hire fewer of them; under the other they hire more short-hour ones (C-11), and workers at firms with six or more on the payroll but fewer than six counted employees are not covered (C-33). Some work moves to contractor arrangements (C-12).
- *Use and absence.* Workers are present for fewer hours (C-3), employers buy more temporary cover (C-21), and workers change jobs a little less, to keep their balances (C-14).
- *Enforcement.* Because only complaints trigger enforcement, breaches are concentrated among workers least able to complain (C-15); under one reading of the carry-over rule, letting 2027 balances lapse is a further breach (C-36). Workers who complain and win receive back pay and damages from the employers found in breach (C-40, C-41).
- *Other markets.* Local services cost more (C-17) and buyers buy less of them (C-37). Tradable production moves partly to Pellam over time (C-18, C-19). Compliant and exempt firms gain sales (C-20) and value (C-38). Owners of labor-intensive businesses see their value fall as passage becomes likely (C-22), and their returns fall until wages adjust (C-23).
- *Existing leave.* Workers whose PTO had conditions the Act forbids get looser conditions (C-32).
- *Costs.* Employers' record-keeping and handling of complaints (C-27), compliant employers' policy changes (C-13), enforcement (C-28) and its funding by taxpayers or recipients of other general-fund spending (C-29), workers' time spent on complaints (C-30), and lobbying over the threshold and the cap (C-16).

**Ambiguous effects.** Full-timers' scheduled hours (C-9); covered workers' total non-wage compensation (C-25) and total earnings, in the short run and after wages adjust (C-39, C-26). Per reading: coverage at firms whose size depends on how part-timers are counted (C-33) and breach by letting 2027 balances lapse (C-36). Not signed: the wage of minimum-wage workers, which the floor holds, and employers' long-run returns.

**Key conditions.** The term binds for about 38% (A-1, p = 0.9). Whether employment and hours fall after wages adjust rests on the term being worth less to the worker than it costs the employer (A-6, p = 0.6), the premise on which the most depends. Who bears the cost rests on workers' alternatives being worse than employers' (A-22, p = 0.6). Compliance rests on payroll practice and complaints (A-2, p = 0.7).

**What this analysis cannot say.** How large any effect is; whether the value of paid sick time to the workers who get it outweighs what they and others give up for it; how much each employer margin is used; any effect on health, including the spread of illness at work and in schools (out of scope for version 1); whether the policy is desirable.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | workers.uncovered | non_wage_compensation (paid sick time) | increase | short | visible | B | CR-1, CR-5c | A-1, A-2 |
| C-2 | employers.uncovered | price_paid (labor cost per hour worked) | increase | short | visible | B | CR-1, CR-5c, CR-8b | A-1, A-2, A-3 |
| C-3 | workers.uncovered | hours_worked (hours present) | decrease | short | invisible | B | CR-3b, CR-4 | A-1, A-2, A-4 |
| C-4 | workers.uncovered | employment, hours_worked (scheduled), non_wage_compensation (other benefits) | at_least_one_decrease | short | invisible | B | PC-17, CR-5c, CR-4, CR-6 | A-1, A-2, A-3 |
| C-5 | workers.uncovered (above minimum wage) | wage_rate | decrease | medium | invisible | B | PC-17, CR-4, CR-6, CR-7b | A-1, A-2, A-5 |
| C-6 | workers.uncovered | employment, hours_worked (scheduled), non_wage_compensation (other benefits) | at_least_one_decrease | medium | invisible | B | PC-17, CR-2, CR-5c, CR-4, CR-12e | A-1, A-2, A-6 |
| C-7 | workers.min_wage | employment, hours_worked (scheduled), non_wage_compensation (other benefits) | at_least_one_decrease | short–medium | invisible | B | PC-10, CR-6 | A-1, A-2, A-7 |
| C-8 | workers.part_time | employment, hours_worked (scheduled) | at_least_one_decrease | medium | invisible | B | RS-18, CR-4b, CR-4c | A-1, A-2, A-8 |
| C-9 | workers.full_time | hours_worked (scheduled) | ambiguous | medium | invisible | B | RS-18, CR-4b, CR-4c, CR-12b | A-1, A-8, A-19 |
| C-10 | workers.prospective | allocation_by_non_price_criteria (screening on expected use) | increase | medium | invisible | B | CR-6, CR-4, CR-11 | A-1, A-9 |
| C-11 | employers.near_threshold | employment (under 20 hours a week) | U2-a: decrease; U2-b: increase | medium | invisible | B | RS-17, CR-4, CR-10a | A-10 |
| C-12 | employers.uncovered, contractors | reclassification (contractor arrangements) | increase | medium | invisible | B | RS-5 | A-1, A-11 |
| C-13 | employers.compliant | compliance_cost (rewriting PTO policies) | increase | short | invisible | B | CR-1, CR-8c | A-12 |
| C-14 | workers.uncovered | job_changes | decrease | medium | invisible | B | RS-11 | A-1, A-15 |
| C-15 | employers.uncovered | legal_breach (employment in breach of the Act) | increase | short–medium | invisible | B | CR-4, CR-1, RS-3 | A-1, A-16 |
| C-16 | employers.small, associations, unions, employers.compliant | lobbying_effort | increase | medium | invisible | B | RS-7 | A-14 |
| C-17 | buyers.local_services | price_paid (local services) | increase | short–medium | invisible | B | RS-14, CR-9 | A-1, A-2, A-3, A-6, A-17 |
| C-18 | employers.tradable | quantity_supplied (in Varrow) | decrease | long | invisible | B | RS-14, RS-6, RS-4 | A-6, A-18 |
| C-19 | neighboring_jurisdictions | quantity_supplied (into Varrow) | increase | medium–long | invisible | B | RS-4 | A-6, A-18 |
| C-20 | employers.compliant, employers.small | quantity_supplied | increase | medium | invisible | B | CR-9, CR-7a | A-6, A-13 |
| C-21 | staffing_agencies | quantity_traded (temporary cover) | increase | short | invisible | B | CR-9 | A-1, A-4, A-19 |
| C-22 | employers.uncovered (owners) | asset_value (labor-intensive businesses) | decrease | short | invisible | B | CR-7c, CR-10c | A-1, A-3, A-24 |
| C-23 | employers.uncovered | return_on_capital | decrease | short | invisible | B | CR-7b | A-1, A-2, A-3 |
| C-24 | workers.uncovered | tax_share_borne (gross cost of the mandated term) | increase | medium–long | invisible | B | CR-7b | A-5, A-22 |
| C-25 | workers.uncovered | non_wage_compensation (total, including sick time) | ambiguous | short–medium | invisible | B | CR-12b | A-1, A-2 |
| C-26 | workers.uncovered | earnings | ambiguous | medium | invisible | B | CR-12b | A-1, A-2, A-5, A-26 |
| C-27 | employers.uncovered | compliance_cost (accrual tracking, records, complaints) | increase | short | invisible | A | OC-2, CR-8c | none |
| C-28 | officials.enforcement | enforcement_cost | increase | short | invisible | A | OC-3 | none |
| C-29 | taxpayers, recipients of other general-fund spending | resources_available_other_uses | at_least_one_decrease | short | invisible | B | OC-3, OC-1 | A-20 |
| C-30 | workers.uncovered | compliance_cost (filing complaints) | increase | short–medium | invisible | B | OC-2, CR-8c | A-21 |
| C-31 | employers.uncovered | price_paid (labor cost per hour worked) | increase | medium | invisible | B | CR-5c, CR-12e | A-1, A-2, A-6 |
| C-32 | workers.pto_noncompliant | non_wage_compensation (conditions of use of existing PTO) | increase | short | invisible | B | CR-1, CR-5c | A-2, A-12 |
| C-33 | workers.size_ambiguous | non_wage_compensation (paid sick time) | U2-a: increase; U2-b: no_change | short | invisible | B | CR-1 | A-1, A-2 |
| C-34 | employers.near_threshold | employment (employees of 20+ hours a week) | decrease | short–medium | invisible | B | RS-17, CR-4, CR-10a | A-10, A-25 |
| C-35 | employers.small | number_of_sellers (firms with fewer than six employees) | increase | medium | invisible | B | RS-17, CR-4, CR-7a | A-10 |
| C-36 | employers.uncovered | legal_breach (2027 balances not carried into 2028) | U1-a: increase; U1-b: no_change | medium | invisible | B | CR-1, CR-4, RS-3 | A-16 |
| C-37 | buyers.local_services | quantity_traded (local services from bound sellers) | decrease | short–medium | invisible | B | RS-14, CR-4c, CR-5a | A-1, A-2, A-3, A-6, A-17 |
| C-38 | employers.compliant, employers.small (owners) | asset_value (firms competing with bound firms) | increase | short | invisible | B | CR-7c, CR-10c | A-3, A-13, A-24 |
| C-39 | workers.uncovered | earnings | ambiguous | short | invisible | B | CR-12b | A-1, A-2, A-3, A-7, A-26 |
| C-40 | workers.complainants | resources_available_other_uses | increase | short–medium | invisible | B | CR-8b | A-16, A-21 |
| C-41 | employers.violating | resources_available_other_uses | decrease | short–medium | invisible | B | CR-8b, CR-3c | A-16, A-21 |
| C-42 | employers.uncovered (keeping staff and hours) | resources_available_other_uses | decrease | short | invisible | B | OC-1, CR-8a, CR-8b, CR-3c | A-1, A-2, A-3 |

## Corrections after the core-only comparison

- **Changed.** C-29: payers from the general fund recorded as a group with `at_least_one_decrease` (OC-1 and OC-3, 0.8). C-17: A-6 added, since its medium horizon rests on part of the cost staying with employers after wages adjust. C-12: `employers.small` dropped from the class; exempt firms have no term to avoid except at the threshold (C-11, C-34, C-35). C-15: variable now `legal_breach` (0.7). C-22: dated from the bill's introduction, part of the way, as CR-7c's probability clause implies. C-24: stated as a gross share (CR-7, 0.7). C-26: A-26 added, the premise its (+) chain needs. C-4 to C-6 cite PC-17, C-8 and C-9 cite RS-18, C-11 cites RS-17; C-6 cites CR-2's 0.7 clarification on the absence of an exchange instead of CR-5b. C-25 is kept as the total of two named items of one variable, now under CR-12's 0.8 clarification, which settles that J row in the pattern version's favor.
- **Added.** C-32 (workers' side of the PTO rewrite), C-33 (coverage per reading of U2, with `no_change`), C-34 (fewer employees of 20 or more hours near the threshold, from 2026; A-25 added), C-35 (more firms below six), C-36 (lapse of 2027 balances as breach per reading of U1), C-37 (buyers of local services buy less), C-38 (exempt and compliant rivals' asset values), C-39 (short-run earnings, ambiguous), C-40 and C-41 (both sides of K6 awards), C-42 (bound employers' means while wages are fixed, limited to those keeping their staff and hours, since CR-3's note signs means only where a sum cannot be avoided).
- **Rejected or not applied.** Core-version C-14 (employers bear the larger short-run share): the comparison itself finds it invalid, since CR-7b ranks shares only with a premise and CR-6 passes part of the cost to workers through the open margins; section 8 now says no ranking is made for the short run. Core C-27 (labor-saving investment), C-30 and C-40 (family care) and C-39 (medical visits) are A rows resting on new premises the 0.8 catalog does not settle, and C-39 runs through health behavior, out of scope; not added. Core C-1 (`term_prevalence`), C-10 (above-minimum wage `no_change` in the short run) and C-38 (payroll vendors) are J rows on recording and depth that 0.8 does not settle; not added. The narrower core group for C-6 (employment or hours only) is a V row; the pattern group stays, as PC-17 gives it.

## Gaps found

**(a) Calculus gaps (a step no core rule covers).** None. Every step was derived from CR-1 to CR-12 or from patterns whose preconditions held. The step closest to a gap was why a term the parties could have agreed on was missing (section 5, C-6). The core rules give two answers, demonstrated preference (CR-2) and selection by the better-informed side (CR-11 with CR-4), but no way to choose between them, so the choice is an empirical premise (A-6). That is the method working as intended, not a gap, and the 0.7 clarification to CR-2 now says so.

**(b) Unclear core rules.**
1. *CR-5c gives the range, not the direction of the terms.* (Closed in 0.7: PC-17 states the direction of the other terms under a mandated term, as a group.) CR-5c itself still states only that the range moves; the direction of the wage (C-5) comes from CR-4 on each side with CR-6.
2. *CR-6's "terms that are not regulated" in the short run.* (Closed in 0.7 and 0.8: CR-6 clarification "existing contracts"; in 0.8, for contracts without a fixed term, stickiness is a premise with a probability, here A-3.)
3. *CR-7b, "bears", for a term that benefits the side that pays.* (Closed in 0.7: CR-7 clarification "gross and net burdens"; C-24 is a gross share.) What counts as an alternative when every employer in reach is bound is still read from the boundaries (small firms, contracting, Pellam).
4. *CR-5b as a dominance premise.* (Closed in 0.7: CR-2 clarification "absence of an exchange": whether a missing term reflects the parties' rankings or an obstacle is a premise, here A-6.)
5. *CR-12h and 2.5, timing within a decrease.* (Closed in 0.7: CR-12 clarification that the same action at different times is "the same" only if paid the same way; the paid absence is recorded as a change in kind, C-1, and the bunching as a path note.)

**(c) Missing patterns.**
1. *Mandated contract term.* (Closed in 0.7: PC-17 and instrument `mandated_contract_term`.)
2. *A uniform term with costs that differ by counterparty (proposed here as RS-18; that ID is now the per-head cost with a cap).* Listed as the candidate "selection under a uniform term" in `06_gaps.md`, 6.2e; the derivation here (CR-4 for the provider, CR-6) stands until a second example needs it.
3. *A cost per head that stops at a cap.* (Closed in 0.7: RS-18; C-8, C-9.)
4. *Complaint-driven enforcement.* Listed as a candidate pattern in `06_gaps.md`, 6.2e. Derivation: CR-1 (a risk equal to the probability of a complaint times the remedy) and CR-4 (x: comply, y: violate), counterparty by counterparty (C-15, C-36).
5. *Size thresholds.* (Closed in 0.7: RS-17; C-11, C-34, C-35.)

**(d) Vocabulary.**
1. *Instrument type.* (Closed in 0.7: `mandated_contract_term`; K1.)
2. *Hours present and hours scheduled.* `hours_worked` cannot tell hours paid but not worked (absence) from hours scheduled. The analysis needed both (section 7); they are kept apart by qualifiers. Still open.
3. *The mandated term and the benefits it displaces.* (Closed in 0.8: CR-12 clarification "two items in one variable": each item recorded with a qualifier and the total combined separately, C-25.)
4. *Who bears a mandate's cost.* (Closed in 0.7: `tax_share_borne` now covers a mandate's burden; C-24.)
5. *Breach within the legal market.* (Closed in 0.7: variable `legal_breach`; C-15, C-36.)
6. *Per-reading "no change".* (Closed in 0.7: sign `no_change`, usable per reading; C-33, C-36.)
