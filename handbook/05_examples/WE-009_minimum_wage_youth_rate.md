# WE-009 Minimum wage increase with a lower youth rate

Analyst: draft (Handbook 0.3)  |  Rule catalog version: 0.3  |  Status: awaiting expert review

A stylized policy in a fictional state. This is a designated contested case (PC-10, note; `06_gaps.md`, Q2): the empirical size of minimum-wage employment effects is disputed. The analysis therefore uses the weaker form of PC-10 ("employment, hours or non-wage compensation decrease, in some combination") and does not claim that any one of them falls. Earnings are left ambiguous wherever no dominance rule applies. The probabilities are illustrative; the evidence column says what a real analysis would cite.

## 1. Policy record

**Larrow Fair Wage Act.** Larrow is a state of about five million people, with a minimum wage of $10 an hour. Wages for low-paid work have been rising about 3% a year. About 15% of Larrow workers earn under $12 and about 22% under $14. Workers under 20 are about 5% of the workforce but about 20% of those earning under $12; most work in restaurants, retail and recreation. The neighboring state of Dorran keeps a $10 minimum. The border cities of Larrow Falls (Larrow) and Port Dorran face each other across a river, ten minutes apart by three bridges.

The bill was introduced in December of Year 0 and passed in March of Year 1. It takes effect in two steps, on January 1 of Year 2 and Year 3. It is not indexed after the second step.

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Adult minimum | `price_floor` (minimum wage) | Hourly wage of employees aged 20 and over | All employers in Larrow | $12 from January 1, Year 2; $14 from January 1, Year 3. No indexing after. | As under the existing law (family members on family farms; certain apprentices). No tip credit, before or after. |
| K2 Youth rate | `price_floor` (a lower floor for a group) | Hourly wage of employees under 20 | All employers in Larrow | Employers may pay at least 85% of the adult minimum: $10.20 in Year 2, $11.90 in Year 3. | As K1 |
| K3 Anti-displacement rule | Restriction on contract terms | Dismissals and hours cuts | Employers | An employer may not dismiss an employee aged 20 or over, or cut their hours, in order to replace them with a worker paid the youth rate. | None |
| K4 Enforcement | Administration and enforcement | K1 to K3 | State Labor Department; private lawsuits | Complaint-driven investigations (about 40 investigators); back pay plus an equal amount in damages; workers may sue. Funded from the general budget. | None |

Unclear provisions: how K3 is proved. The text requires intent to replace; no guidance yet says what evidence suffices. Assumed hard to prove, so it deters dismissals more than it affects hiring (see A-9).

## 2. Classification

| Component | Rothbard type | Binding? | Rule families |
|---|---|---|---|
| K1 | Triangular: prohibits employment of workers aged 20 and over at wages below the floor | Yes, for an identifiable group of adult workers whose wages would otherwise be below $12 in Year 2 and $14 in Year 3, even after the 3% trend (A-1). Becomes less binding after Year 3 as wages rise and the floor stays fixed (TS-3). | PC, RS, TS |
| K2 | Triangular: a lower floor for workers under 20 | Yes, for some young workers whose wages would otherwise be below $10.20 and $11.90 (A-2). It also creates a boundary at age 20, where the floor jumps by about 18%. | PC, RS-1 |
| K3 | Triangular | Partly; it limits dismissals, not hiring choices | RS-3 |
| K4 | Binary: funded by taxpayers | Yes | OC-3 |

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `workers.adult_low_wage` | Employees aged 20 and over who would earn under $14 | Higher wage floor; employers may change their hours, terms or numbers. |
| `workers.youth` | Employees and job seekers under 20 | Higher floor, but now cheaper to employ than adults at the minimum. |
| `workers.prospective` | Job seekers, including adults aged 20 and over with little experience | Employers have more applicants per vacancy at the floor and can choose more strictly. |
| `employers.low_wage` | Restaurants, shops, care providers and others paying near the minimum | Labor at the floor costs more; youth labor less so. |
| `consumers` | Buyers of goods and services made with much low-wage labor | Possibly higher prices. |
| `consumers.border` | Larrow Falls residents | Can buy in Port Dorran. |
| `input_suppliers` (labor-saving equipment) | Sellers of ordering kiosks, self-checkouts and similar equipment | More demand. |
| `officials.enforcement`, `taxpayers` | Labor Department and its funders | More complaints and investigations. |

## 4. Direct effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | `workers.adult_low_wage` who keep their jobs | `wage_rate` | increase | short to medium | K1, PC-10 | A-1, A-3 |
| C-2 | `workers.youth` who keep their jobs | `wage_rate` | increase | short to medium | K2, PC-10 | A-2, A-3 |

The visible effect: workers paid near the minimum get a raise in each of the two years, smaller for those under 20. Compared with the counterfactual, the raise is the gap between the new floor and the wage each worker would have earned with the 3% trend, not the gap from $10.

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-3 | `workers.adult_low_wage` | `employment`, `hours_worked`, `non_wage_compensation` (group consequence) | `at_least_one_decrease` | short to medium | PC-10, PC-9, RS-2, RS-1 | A-1, A-3, A-4, A-12, A-13 |
| C-4 | `workers.youth` | `employment`, `hours_worked`, `non_wage_compensation` (group consequence) | ambiguous (section 7) | short to medium | PC-10 vs RS-1 | A-2, A-3, A-12, A-13 |
| C-5 | `workers.prospective` | `excess_supply` (of labor at the floor) | increase | short to medium | PC-9 | A-1, A-3, A-14 |
| C-6 | `workers.prospective` aged 20 and over with little experience | `allocation_by_non_price_criteria` (employers select on experience, references, credentials, and prefer applicants under 20 who cost less) | increase | short to medium | PC-11, RS-1 | A-1, A-3, A-12, A-14 |
| C-7 | `employers.low_wage` | `reclassification` (workers recast as independent contractors) | increase | short to medium | RS-5 | A-1, A-5 |
| C-8 | `employers.low_wage` | `informal_activity` (cash wages below the floor) | increase | short | RS-3 | A-1, A-6 |
| C-9 | `employers.low_wage` | `quantity_substitute` (labor-saving equipment in place of low-wage labor) | increase | medium to long | RS-1, TS-1 | A-1, A-7 |
| C-10 | `employers.low_wage` | `investment_target` (new low-wage-intensive outlets in Larrow) | decrease | short (from the bill's introduction) to medium | TS-2, RS-6 | A-1, A-8, A-14 |
| C-11 | `employers.low_wage`, unions, advocacy groups | `lobbying_effort` (to delay the second step, to index the floor, to abolish or widen the youth rate) | increase | medium | RS-7 | A-1 |

C-3 is the weaker form of PC-10, recorded as a group consequence (`02_ontology.md`, 2.5). Employers facing a higher price for some labor can respond on several margins: fewer hires, fewer hours, fewer paid breaks, less training, less flexible schedules, or none of these for some employers. PC-10 says that, for workers whose labor employers value below the floor, at least one of these margins moves down. It does not say which; that is an empirical question, and the evidence on it is disputed. The sign `at_least_one_decrease` is scored as correct if at least one of the three falls and none rises; writing each as its own "decrease" would overclaim.

Two chains push the adult group's margins down, and they agree: the higher adult floor (PC-10), and the youth rate, which makes workers under 20 about 15% cheaper than adults at the minimum, so employers who can use either shift some hiring toward the young (RS-1, A-13).

C-5 and C-6: where the floor raises employers' labor cost per hour for the bound group (A-14: it is not fully offset by cutting non-wage terms), more people seek work at the floor than employers wish to hire there (PC-9). C-5 does not say that employment falls, or by how much: the surplus can come as much from more applicants at the higher wage as from fewer vacancies, and C-3 leaves open which margin employers adjust. An adult aged 20 to 24 seeking a first job now competes, at the margin, with applicants under 20 who cost 15% less. Employers with more applicants than vacancies at the floor can afford to be selective (PC-11).

C-10: decisions to open new outlets are made years ahead. From December of Year 0, when the bill was introduced and expected to pass, employers planning outlets in Larrow took both steps into account (TS-2). This is the earliest response, a year before the first step.

Not reported: dismissals of workers when they turn 20 (RS-1 at the age boundary). K3 forbids dismissal to replace an adult with a youth-rate worker; A-9 is below the cut-off (p = 0.4). The substitution in C-3 and C-4 works mainly through whom employers hire, which K3 does not reach.

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-12 | `workers.prospective` | `search_cost` (longer job searches) | increase | short to medium | PC-11, OC-2 | | A-1, A-3, A-14 |
| C-13 | `consumers` | `price_paid` (restaurant meals and other low-wage-intensive services) | increase | short to medium | RS-14 | low-wage labor: `input_to` these services | A-1, A-10, A-14 |
| C-14 | `consumers.border` | `cross_border_purchases` (meals and shopping in Port Dorran) | increase | short to medium | RS-14, RS-4 | Larrow Falls and Port Dorran: `across_border`, close | A-1, A-11, A-14 |
| C-15 | `input_suppliers` (labor-saving equipment) | `quantity_traded` | increase | medium to long | RS-1 | labor and equipment: `substitute`, partial | A-1, A-7 |

C-13 applies RS-14 (input cost pass-through). Low-wage labor is a large part of the cost of restaurant meals and similar local services. Where it raises labor cost per hour (A-14), buyers pay more and/or less is supplied. Most sellers of these services compete with other Larrow sellers who face the same floor (A-10), so RS-14 says the price effect dominates. C-14: at the border the competitors ten minutes away in Port Dorran are exempt, so for Larrow Falls sellers RS-14 gives mainly the quantity effect (RS-6: fewer or smaller outlets); either way, some Larrow Falls residents eat and shop in Port Dorran instead (RS-4). RS-9 was checked: those who cross for meals buy other things on the same trip, but that chain reaches diffuse bystanders at depth 4, so it is pruned.

RS-10 is recorded with C-8: workers paid in cash below the floor cannot take pay disputes to the Labor Department without exposing the arrangement. RS-11 was checked and does not apply: no benefit is tied to a place. Pruned at depth 3: Dorran workers who commute to Larrow for the higher wage, and the wages Dorran employers must then pay to keep staff (RS-4 in its widened form would carry it; diffuse).

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `workers.adult_low_wage`, `employment` / `hours_worked` / `non_wage_compensation` as a group, short to medium (C-3) | None. | Higher adult floor (PC-10); hiring shifted toward cheaper workers under 20 (RS-1). | None needed | **at_least_one_decrease**. Both chains point the same way; which margin moves is not determined. |
| `workers.youth`, the same group, short to medium (C-4) | Employers shift hiring from adults to workers under 20, whose relative cost has fallen (RS-1, A-13). | The youth floor itself rises from $10 to $10.20 and then $11.90 (PC-10). | None | **ambiguous**. Which chain is stronger depends on how close a substitute young workers are for adults in each job, and on how far the youth floor binds. |
| `workers.adult_low_wage`, `earnings`, short to medium | Higher wage per hour (C-1). | If the adjustment in C-3 falls on employment or hours, fewer hours are paid. If it falls only on non-wage terms, earnings are unaffected by it. | None | **ambiguous**. This is PC-10's note: earnings of the low-wage group combine opposite chains, and no dominance rule applies. |
| `workers.youth`, `earnings`, short to medium | Higher wage per hour (C-2); more hires shifted from adults (RS-1). | Youth floor binds for the least productive young workers (PC-10). | None | **ambiguous**. |

## 8. Time structure

- **Announcement (December of Year 0 to January of Year 2).** The bill gave a year's notice of the first step and two years' notice of the second. Long-lived decisions respond first: plans for new outlets (C-10, TS-2). Wages, hours and staffing do not change before the first step, because the floor applies to existing workers as well as new hires, so there is nothing to gain by acting early (RS-8 does not apply).
- **Year 2 and Year 3.** In each step, the margins that are cheapest for employers to change move first: schedules, hours, paid breaks, training (C-3, RS-2). Staffing changes come mostly through hiring and not replacing those who leave, which takes months. The two steps mean the second step's effects are anticipated during the first year.
- **Medium to long run.** Labor-saving equipment is adopted as existing equipment comes up for replacement and as new outlets are designed (C-9, TS-1). Effects that work through capital therefore grow over several years after the wage effects have appeared.
- **Erosion after Year 3 (TS-3).** The floor is fixed at $14 in money. If low-wage pay keeps rising about 3% a year in the counterfactual, the group for whom the floor binds shrinks each year, and both the wage gains (C-1, C-2) and the adjustments (C-3) shrink relative to the counterfactual. The youth rate is a fixed fraction of the adult floor, so the gap between the two groups stays at 15% while both erode together. If indexing is later won through lobbying (C-11), this erosion stops; that would be a new policy.
- **The age boundary over time.** Each cohort crosses age 20. Under the youth rate, employers who hire mostly under-20 workers face a cost jump as each worker turns 20. The K3 rule limits dismissals at that point (A-9, below the cut-off), so the effect appears mainly in who is hired, not in who is let go.

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-16 | `employers.low_wage` using the youth rate | `compliance_cost` (proof of age, payroll records, documenting reasons for dismissals under K3) | increase | Staff time that would otherwise have gone to running the business. | OC-2 |
| C-17 | `taxpayers` | `resources_available_other_uses` | decrease | What the Labor Department's added investigations would otherwise have funded. | OC-3, OC-1 |

Job seekers' longer searches are recorded as C-12. Prevented exchanges (OC-4) are not listed separately: the exchanges that the floor prohibits, jobs at wages below it, are either replaced by jobs at the floor or not, and which of these happens is exactly what C-3 leaves open. Listing them as `quantity_traded` decrease would overclaim.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | For an identifiable group of adults, employers value their labor below the new floor, even after the 3% wage trend. | binding | 0.9 | Wage distribution by industry and age; projected wages in Year 2 and Year 3. | Most consequences fail. |
| A-2 | Some workers under 20 would earn less than $10.20 in Year 2 or $11.90 in Year 3. | binding | 0.8 | Wage distribution for workers under 20. | C-2 fails; C-4 reduces to the + chain (more youth hiring). |
| A-3 | Most employers comply with the floor. | enforcement | 0.75 | Investigator numbers; damages; private lawsuits. | C-1 and C-2 shrink; C-8 grows. |
| A-4 | Employers can adjust at least one margin: hiring, hours, schedules, breaks, training or benefits. | other | 0.9 | Labor contracts in low-wage industries; scheduling practices. | C-3 fails; earnings rise without offset. |
| A-5 | Recasting some workers as independent contractors is feasible. | other | 0.55 | Legal tests for contractor status; platform work in Larrow. | C-7 not reported. |
| A-6 | Some cash payment below the floor goes undetected. | enforcement | 0.65 | Complaint-driven enforcement; small cash-based employers. | C-8 not reported. |
| A-7 | Labor-saving equipment exists for some low-wage tasks. | alternative_uses | 0.75 | Adoption of ordering kiosks and self-checkout elsewhere. | C-9, C-15 not reported. |
| A-8 | Employers planning outlets expected both steps to take effect. | expectations | 0.85 | Bill sponsors; legislative majority; polls. | C-10 starts later or is smaller. |
| A-9 | Employers dismiss workers as they turn 20, despite K3. | enforcement | 0.4 | Turnover by age at youth-rate employers; complaints under K3. | Below cut-off; not reported. |
| A-10 | Most sellers of low-wage-intensive services compete mainly with other Larrow sellers who face the same floor (RS-14: competitors' exposure). | other | 0.8 | Local nature of restaurant, retail and recreation services; share of their sales made to Larrow residents; price changes after past minimum-wage steps. | C-13 weakens: the quantity effect (fewer or smaller outlets) dominates instead of the price effect. |
| A-11 | Larrow Falls residents can easily shop and eat in Port Dorran. | mobility | 0.7 | Ten-minute bridge crossings; existing cross-river shopping. | C-14 not reported. |
| A-12 | A meaningful number of employers use the youth rate. | other | 0.8 | Use of youth rates where they exist; share of under-20 workers. | The RS-1 chains in C-3, C-4 and C-6 fail; C-16 shrinks. |
| A-13 | Workers under 20 and adults are substitutes in many low-wage jobs. | substitutability | 0.8 | Job tasks in restaurants and retail; age mix by job. | The RS-1 chains weaken; C-4 becomes `at_least_one_decrease`. |
| A-14 | The floor raises employers' labor cost per hour for the bound group: they cannot offset it fully by cutting non-wage terms, or by replacing the labor with equipment or other workers at the old cost. | substitutability | 0.8 | Non-wage compensation in minimum-wage jobs (small: few benefits to cut); cost of equipment against the wage it replaces. | C-5, C-6, C-12, C-13, C-14 and C-10 not reported: if the whole adjustment fell on non-wage terms, labor cost would not rise, and C-3 would hold through `non_wage_compensation` alone. |

## 11. Report

**The policy.** Larrow raises its minimum wage from $10 to $12 and then $14 an hour over two years, with no indexing after. Employers may pay workers under 20 at 85% of the adult rate. Employers may not dismiss adults to replace them with youth-rate workers.

**Visible consequences.** Low-paid workers who keep their jobs earn more per hour (C-1), and those under 20 somewhat less so (C-2).

**Invisible consequences.**
- *Adult low-wage workers* face some combination of fewer jobs, fewer hours, or less training, fewer benefits and less flexible schedules (C-3). The method says at least one of these happens for workers whose labor employers value below the floor; it does not say which, or how much.
- *Job seekers* find more applicants competing for each vacancy at the floor (C-5), search longer (C-12), and face employers who select more strictly; adults with little experience also compete with cheaper applicants under 20 (C-6).
- *Employers* recast some workers as contractors (C-7), pay some workers in cash below the floor (C-8), adopt more labor-saving equipment over time (C-9), and open fewer new outlets in Larrow, starting from when the bill was introduced (C-10). Those using the youth rate keep more records (C-16). Sellers of labor-saving equipment sell more (C-15).
- *Consumers* pay more for low-wage-intensive services (C-13), and residents of Larrow Falls eat and shop more in Port Dorran, where sellers do not face the floor (C-14).
- *Interested groups* lobby over the second step, indexing and the youth rate (C-11). *Taxpayers* fund enforcement (C-17).

**Ambiguous effects.** Whether employment, hours and non-wage terms for workers under 20 rise or fall: the youth floor rises, but the young also become cheaper relative to adults (C-4). Whether total earnings of adult and young low-wage workers rise or fall: wages rise, but the method cannot say whether the adjustment falls on hours and jobs or on non-wage terms (section 7).

**Key conditions.** The floor must bind for an identifiable group (A-1, p = 0.9). The youth-rate effects depend on employers using it (A-12, p = 0.8) and on young and adult workers being substitutes (A-13, p = 0.8). The effects on job seekers, prices and new outlets rest on the floor raising labor cost per hour rather than being absorbed wholly by cuts in non-wage terms (A-14, p = 0.8). After Year 3, effects of every kind shrink as wages rise past a floor fixed in money.

**What this analysis cannot say.** Which margin employers adjust and by how much; whether employment of any group falls, and by how many jobs; whether the total earnings of low-wage workers rise or fall; effects on poverty, health or schooling (out of scope for version 1); whether the policy is desirable. The size of minimum-wage effects is disputed in the empirical literature (PC-10, note), and this analysis takes no side in that dispute.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | workers.adult_low_wage (employed) | wage_rate | increase | short–medium | visible | B | K1, PC-10 | A-1, A-3 |
| C-2 | workers.youth (employed) | wage_rate | increase | short–medium | visible | B | K2, PC-10 | A-2, A-3 |
| C-3 | workers.adult_low_wage | employment, hours_worked, non_wage_compensation (group) | at_least_one_decrease | short–medium | invisible | B | PC-9, PC-10, RS-2, RS-1 | A-1, A-3, A-4, A-12, A-13 |
| C-4 | workers.youth | employment, hours_worked, non_wage_compensation (group) | ambiguous | short–medium | invisible | B | PC-10 vs RS-1 | A-2, A-3, A-12, A-13 |
| C-5 | workers.prospective | excess_supply (labor at the floor) | increase | short–medium | invisible | B | PC-9 | A-1, A-3, A-14 |
| C-6 | workers.prospective (20+, inexperienced) | allocation_by_non_price_criteria | increase | short–medium | invisible | B | PC-9, PC-11, RS-1 | A-1, A-3, A-12, A-14 |
| C-7 | employers.low_wage | reclassification | increase | short–medium | invisible | B | RS-5 | A-1, A-5 |
| C-8 | employers.low_wage | informal_activity | increase | short | invisible | B | RS-3, RS-10 | A-1, A-6 |
| C-9 | employers.low_wage | quantity_substitute (equipment) | increase | medium–long | invisible | B | RS-1, TS-1 | A-1, A-7 |
| C-10 | employers.low_wage | investment_target (new outlets) | decrease | short–medium | invisible | B | TS-2, RS-6 | A-1, A-8, A-14 |
| C-11 | employers, unions, advocacy groups | lobbying_effort | increase | medium | invisible | B | RS-7 | A-1 |
| C-12 | workers.prospective | search_cost | increase | short–medium | invisible | B | PC-9, PC-11, OC-2 | A-1, A-3, A-14 |
| C-13 | consumers | price_paid (low-wage-intensive services) | increase | short–medium | invisible | B | PC-10, RS-14 | A-1, A-10, A-14 |
| C-14 | consumers.border | cross_border_purchases | increase | short–medium | invisible | B | RS-14, RS-6, RS-4 | A-1, A-11, A-14 |
| C-15 | input_suppliers (equipment) | quantity_traded | increase | medium–long | invisible | B | RS-1 | A-1, A-7 |
| C-16 | employers.low_wage (youth rate) | compliance_cost | increase | short | invisible | B | OC-2 | A-12 |
| C-17 | taxpayers | resources_available_other_uses | decrease | short | invisible | A | OC-3, OC-1 | none |
| — | workers.adult_low_wage | earnings | ambiguous | short–medium | invisible | B | C-1 vs C-3 | A-1, A-3, A-4 |
| — | workers.youth | earnings | ambiguous | short–medium | invisible | B | C-2 vs C-4 | A-2, A-3, A-12, A-13 |

## Gaps found

- GAP-009-1 (closed in catalog 0.3: group consequences, `02_ontology.md` 2.5). C-3 is now a group consequence with sign `at_least_one_decrease`; C-4 is the same group with sign `ambiguous`. Neither claims that any one member falls.
- GAP-009-2 (closed in catalog 0.3: RS-14). C-13 and C-14 are now Tier B. RS-14's assumptions are covered by A-10 (rewritten to state the competitors' exposure, instead of assuming the pass-through itself) and the new A-14 (labor cost per hour rises; not fully offset by non-wage cuts or replacement), which the job-seeker consequences C-5, C-6 and C-12 and the outlet consequence C-10 now also cite.
