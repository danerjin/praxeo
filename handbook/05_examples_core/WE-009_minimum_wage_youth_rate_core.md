# WE-009 / Analysis: Minimum wage increase with a lower youth rate (core-only re-run)

Analyst: core-only re-run (Handbook 0.4)  |  Rules: core rules CR-1 to CR-12 only  |  Status: awaiting comparison

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


Horizons used below: short = from passage (Year 1) through Year 2 (first step); medium = Year 3 (second step) and the following years; long = later, as the unindexed floor is overtaken by the wage trend. This is a contested case; the analysis states only what the core rules license given the case assumptions, and records group or ambiguous signs where the rules license no more.

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | Core rules applied |
|---|---|---|---|
| K1 Adult minimum | triangular (forbids employment of adults at less than $12, then $14) | Yes for an identifiable group of adults (A-1, p 0.9); complied with by most employers (A-3, p 0.75) | CR-1, CR-4, CR-5a, CR-6, CR-7, CR-9, CR-10 |
| K2 Youth rate | triangular (a lower floor for workers under 20) | Yes for some workers under 20 (A-2, p 0.8); used by a meaningful number of employers (A-12, p 0.8) | CR-1 (op 1 against the old $10 floor; op 2 against K1), CR-4 |
| K3 Anti-displacement rule | triangular (restricts a contract term: dismissal or hours cuts to replace with youth) | Hard to prove; deters dismissals more than hiring (record) | CR-1 (op 3), CR-4 |
| K4 Enforcement | binary on the budget side; attaches back pay and damages to violation | Complaint-driven; some evasion undetected (A-6, p 0.65) | CR-1 (op 3), CR-8 |

**CR-1: what each component does to each actor class.** Operations: 1 remove an option, 2 add an option, 3 change what an option brings, 4 transfer means. A dash means no direct effect; indirect effects are traced with CR-9.

| Actor class | K1 Adult minimum | K2 Youth rate | K3 Anti-displacement | K4 Enforcement |
|---|---|---|---|---|
| employers (restaurants, retail, recreation and other low-wage employers in Larrow) | 1: employing adults below the floor removed | 1: employing youth below 85% of the floor removed; 2 relative to K1: youth may be paid less than adults | 3: risk attached to dismissing or cutting hours of adults in order to hire youth | 3: back pay, equal damages, lawsuits attached to violation |
| workers.adult_low_wage (aged 20 and over, valued near or below the floor) | 1: working below the floor removed; 3: the job, where kept, pays more | — | 3: some protection against replacement | 2: a right to sue |
| workers.youth (under 20) | — | 1: working below the youth floor removed; 3: pay rises where bound | — | 2 |
| workers.prospective (adult and youth job seekers) | 1: offering to work below the floor removed | 1 (youth) | — | — |
| buyers.current (customers of low-wage-intensive services) | — | — | — | — |
| neighboring_jurisdictions (Port Dorran sellers and workers) | — | — | — | — |
| input_suppliers (sellers of labor-saving equipment) | — | — | — | — |
| officials.enforcement (Labor Department) | — | — | — | 2: duties; 4: means from the general budget |
| taxpayers | — | — | — | 4 |

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| employers | Low-wage-intensive firms in Larrow | Labor of bound groups costs more per hour (A-14); youth cheaper than adults (K2); dismissing adults for youth risky (K3) |
| workers.adult_low_wage | Adults earning under $12 or $14 | Higher wage where employed; fewer hours, jobs or non-wage terms for at least some |
| workers.youth | Workers under 20 | Higher wage where bound (A-2); relatively cheaper than adults (A-13) |
| workers.prospective | Job seekers in low-wage work | More applicants per job at the floor |
| buyers.current | Customers of restaurants, retail and recreation in Larrow | Face employers' higher costs (CR-9) |
| neighboring_jurisdictions | Port Dorran sellers and workers, ten minutes across the river | Receive Larrow Falls shoppers (A-11) |
| input_suppliers | Sellers of kiosks, self-checkout and similar equipment (A-7) | More demand from employers |
| factor_owners.specific | Owners of fit-outs and leases tied to low-wage-intensive businesses | Expected yield cut |
| officials.enforcement | Labor Department (about 40 investigators) | More complaints |
| taxpayers | General budget | Fund enforcement |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | workers.adult_low_wage (employed adults paid below the new floor) | wage_rate | increase | short | CR-1 (K1 op 1) | A-1, A-3 |
| C-2 | workers.youth (paid below the youth floor) | wage_rate | increase | short | CR-1 (K2 op 1) | A-2, A-3 |

Supporters expect the wage of low-paid workers who keep their work to rise. It does where the floor binds and is complied with. The analysis does not claim that this is the only change for these workers: see C-4 and C-5.

## 5. Responses

**CR-2 to CR-5 by actor class.**

| Actor class | CR-2/CR-3: which chosen option is removed or burdened | CR-4 pairs (x made worse relative to y) | CR-5 |
|---|---|---|---|
| employers | Employing bound labor at the prior wage removed (CR-3a) | x: an hour of bound adult labor, y: equipment, a youth worker, or not producing that unit; x: hire adult, y: hire youth; x: employee, y: contractor; x: comply, y: pay cash below the floor; x: open an outlet in Larrow, y: elsewhere or not; x: accept, y: lobby | 5a: employment at wages below the floor prevented |
| workers.adult_low_wage | Working below the floor removed (worse off only for those whose job, hours or terms are lost, CR-3a) | x: leave a job paying the floor, y: keep it; mirror for working more hours (CR-4 exception: a higher wage also raises means, so hours offered by those employed are ambiguous) | 5a |
| workers.youth | Working below the youth floor removed | as for adults | 5a |
| workers.prospective | Offering to work below the floor removed | x: wait for a legal job, y: informal or contractor work | 5a |
| buyers.current | Paying prior prices (CR-9, via employers' costs) | x: buy in Larrow, y: buy in Port Dorran or buy less | — |

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-3 | employers | return_on_capital | decrease | short | CR-1 (K1 op 1) → CR-3a | A-1, A-3, A-14 |
| C-4 | workers.adult_low_wage | employment, hours_worked, non_wage_compensation | at_least_one_decrease | short | CR-6 (price of labor held above clearing; pressure displaced to unregulated terms) and CR-4c (x: the last hour of bound labor, y: equipment, other labor or not producing) → CR-12a | A-1, A-3, A-4, A-14 |
| C-6 | workers.prospective | excess_supply (labor at the floor) | increase | short | CR-6 | A-1, A-3, A-14 |
| C-7 | workers.prospective | search_cost, wait_time, allocation_by_non_price_criteria | at_least_one_increase | short | C-6 → CR-6 (criteria margin: employers choose among more applicants) | A-1, A-3, A-14 |
| C-8 | workers.adult_low_wage | job_changes | decrease | medium | C-6 → CR-4b (x: leave a job paying the floor, y: keep it) → CR-3 | A-1, A-3, A-14 |
| C-9 | workers.youth | employment | ambiguous | short | (+) CR-4b (x: hire adult, y: hire youth at 85%); (−) CR-1 (K2 op 1) → CR-4c; (−) C-11 → LW-10 → CR-12b | A-2, A-3, A-12, A-13, A-14 |
| C-10 | employers | quantity_substitute (labor-saving equipment: kiosks, self-checkout) | increase | medium | CR-4b (x: an hour of bound labor, y: equipment) → CR-10b (installed as equipment is replaced) | A-1, A-7, A-14 |
| C-17 | employers | reclassification (workers recast as independent contractors) | increase | short | CR-4b (x: employee form, y: contractor form) | A-1, A-5, A-14 |
| C-18 | employers | informal_activity (cash pay below the floor) | increase | short | CR-6 (exchanges outside the rule) → CR-4b (x: comply, y: violate) | A-1, A-6 |
| C-19 | employers | investment_target (new low-wage-intensive outlets in Larrow) | decrease | short | CR-10a (both steps expected from passage) → CR-4b (x: open in Larrow, y: elsewhere or not) | A-1, A-8, A-14 |
| C-21 | employers | compliance_cost (age records for the youth rate; documentation against K3 claims) | increase | short | CR-1 (K2 op 2, K3 op 3) → CR-8c | A-12 |
| C-24 | employers | lobbying_effort | increase | short | CR-4 (x: accept, y: lobby) | A-1, A-N1 |

Notes on the responses.
- C-4 is a group: CR-6 says the pressure moves to the unregulated terms (breaks, schedules, training, benefits), and CR-4c says employers give up the hours they value least once each hour costs more (A-14 says the cost cannot be fully offset). Which margin moves is empirical (A-4 says at least one is open). The core rules do not license a separate claim that employment falls, or that hours fall.
- C-6: those whose labor employers value below the floor (A-1) are not hired legally at the floor (CR-5a). The CR-4 exception (a higher wage raises means, so hours offered may fall) applies only to those who are employed at the higher wage, not to those who are not hired, so the excess supply at the floor is positive.
- C-9: the youth rate makes youth cheaper relative to adults (pushes youth employment up where youth and adults are substitutes, A-13), while the youth floor itself binds on some youth (A-2) and less output is produced (C-11). No premise says which dominates.
- K3 attaches risk to dismissing or cutting incumbent adults in order to hire youth, but not to hiring youth instead of adult applicants. So the substitution in C-9 runs mainly through new hires (CR-4: K3 burdens only the dismissal route). Dismissal of workers as they turn 20 (A-9, p 0.4) is not reported.

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-5 | workers.adult_low_wage | earnings | ambiguous | short | (+) C-1; (−) C-4 → CR-12b | — | A-1, A-3, A-4, A-14 |
| C-11 | employers | quantity_supplied (restaurant, retail and recreation services in Larrow) | decrease | medium | CR-9 (labor `input_to` services) → CR-4c (last units made costlier) | labor `input_to` services | A-1, A-3, A-14 |
| C-12 | buyers.current (Larrow customers) | price_paid (low-wage-intensive services) | increase | medium | C-11 → CR-5c (range of acceptable terms moved) with rivals facing the same floor (A-10) → CR-7a | labor `input_to` services | A-1, A-3, A-10, A-14 |
| C-13 | buyers.current (Larrow customers) | quantity_demanded (low-wage-intensive services) | decrease | medium | C-12 → CR-4c | — | A-1, A-3, A-10, A-14 |
| C-14 | buyers.current (Larrow Falls residents) | cross_border_purchases (shopping and eating in Port Dorran) | increase | medium | C-12 → CR-4b (x: buy in Larrow Falls, y: buy in Port Dorran) | Larrow Falls and Port Dorran services, `across_border`, close | A-1, A-3, A-10, A-11, A-14 |
| C-15 | neighboring_jurisdictions (Port Dorran sellers) | quantity_substitute (sales to Larrow residents) | increase | medium | C-14 → CR-9 | `across_border` | A-1, A-3, A-10, A-11, A-14 |
| C-16 | neighboring_jurisdictions (Port Dorran workers in low-wage services) | employment | increase | medium | C-15 → CR-9 (labor `input_to` services) → LW-10 | labor `input_to` services | A-1, A-3, A-10, A-11, A-14 |
| C-20 | factor_owners.specific (owners of fit-outs and leases of low-wage-intensive businesses) | asset_value | decrease | short | CR-10c → CR-7c (moves when the steps became expected); CR-7b (lasting loss settles on means that cannot move) | fit-outs `input_to` services | A-1, A-8, A-14 |
| C-22 | officials.enforcement | enforcement_cost | increase | short | C-18 and more bound workers → CR-1 (K4) → CR-8c | — | A-1 |
| C-23 | taxpayers | resources_available_other_uses | decrease | short | C-22 → CR-8a | — | A-1 |

Chains stopped: C-16 is at depth 4 (floor, employers' costs, customers crossing, Port Dorran sales, Port Dorran labor). Effects on wages in Port Dorran are ambiguous (more demand for their labor; some Port Dorran workers seek Larrow jobs at the higher wage but face rationed hiring) and are not reported. Suppliers of equipment (after C-10) are recorded only through C-10. Effects on landlords of commercial space and on Larrow customers' other spending are diffuse beyond depth 3; pruned.

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| workers.adult_low_wage, earnings, short | higher wage (C-1) | fewer hours, jobs or terms (C-4) | none: no premise establishes which dominates | ambiguous (C-5) |
| workers.youth, employment, short | youth cheaper than adults (K2, A-13) | youth floor binds (A-2); less output (C-11) | none | ambiguous (C-9) |
| workers.adult_low_wage, employment/hours/non-wage, short | none | own floor (CR-6, CR-4c); youth cheaper than adults (K2) | none needed (CR-12a) | at_least_one_decrease (C-4) |
| buyers.current, price_paid, medium | higher labor cost (C-11) with rivals bound alike (A-10) | none | none needed | increase (C-12) |

No dominance claim is made in this analysis.

## 8. Time structure

- December Year 0 to March Year 1: the bill becomes expected and passes. Employers planning outlets expect both steps (A-8), so new outlets in Larrow are held back from then (C-19), and the value of fixed assets tied to low-wage-intensive businesses falls when the steps become expected (C-20, CR-7c).
- Year 2 (first step, $12): C-1 to C-9 and C-17, C-18 begin. Changes to equipment and outlets come gradually as existing equipment and leases turn over (CR-10b): C-10 and C-11 are medium-run.
- Year 3 (second step, $14): the floor binds on a wider group (about 22% of workers earned under $14), so the same chains apply to more workers.
- Long run: the floor is not indexed; wages for low-paid work rise about 3% a year in the counterfactual, so the floor binds on a shrinking group after Year 3 (arithmetic). Signs are unchanged for those still bound; the number bound falls. Equipment installed and outlets not opened persist (CR-10b).

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-4 | workers.adult_low_wage | employment, hours_worked, non_wage_compensation | at_least_one_decrease | Jobs, hours or terms that both parties would have agreed to below the floor | CR-5a, CR-3a |
| C-7 | workers.prospective | search_cost, wait_time, allocation_by_non_price_criteria | at_least_one_increase | Time spent seeking scarcer jobs at the floor | CR-6, CR-8c |
| C-13 | buyers.current | quantity_demanded | decrease | Services forgone at higher prices | CR-3a, CR-4c |
| C-21 | employers | compliance_cost | increase | Staff time on age records and documentation | CR-8c |
| C-22 | officials.enforcement | enforcement_cost | increase | Investigator time | CR-8c |
| C-23 | taxpayers | resources_available_other_uses | decrease | Whatever the general budget would otherwise have funded | CR-8a |

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | For an identifiable group of adults, employers value their labor below the new floor, even after the 3% wage trend. | binding | 0.9 | Wage distribution by industry and age; projected wages in Year 2 and Year 3. | The adult floor does not bind; most consequences vanish. |
| A-2 | Some workers under 20 would earn less than $10.20 in Year 2 or $11.90 in Year 3. | binding | 0.8 | Wage distribution for workers under 20. | C-2 fails; C-9 loses its (−) own-floor chain. |
| A-3 | Most employers comply with the floor. | enforcement | 0.75 | Investigator numbers; damages; private lawsuits. | The floor becomes a risk rather than a removed option; C-1, C-4 weaken and C-18 grows. |
| A-4 | Employers can adjust at least one margin: hiring, hours, schedules, breaks, training or benefits. | other | 0.9 | Labor contracts in low-wage industries; scheduling practices. | C-4 fails. |
| A-5 | Recasting some workers as independent contractors is feasible. | other | 0.55 | Legal tests for contractor status; platform work in Larrow. | C-17 fails. |
| A-6 | Some cash payment below the floor goes undetected. | enforcement | 0.65 | Complaint-driven enforcement; small cash-based employers. | C-18 fails. |
| A-7 | Labor-saving equipment exists for some low-wage tasks. | alternative_uses | 0.75 | Adoption of ordering kiosks and self-checkout elsewhere. | C-10 fails. |
| A-8 | Employers planning outlets expected both steps to take effect. | expectations | 0.85 | Bill sponsors; legislative majority; polls. | C-19, C-20 move to the effective dates. |
| A-9 | Employers dismiss workers as they turn 20, despite K3. | enforcement | 0.4 | Turnover by age at youth-rate employers; complaints under K3. | (Below cut-off; used by no reported consequence.) |
| A-10 | Most sellers of low-wage-intensive services compete mainly with other Larrow sellers who face the same floor. | other | 0.8 | Local nature of restaurant, retail and recreation services; share of their sales made to Larrow residents; price changes after past minimum-wage steps. | C-12 to C-16 weaken; the burden settles more on employers (C-3, C-20). |
| A-11 | Larrow Falls residents can easily shop and eat in Port Dorran. | mobility | 0.7 | Ten-minute bridge crossings; existing cross-river shopping. | C-14 to C-16 fail. |
| A-12 | A meaningful number of employers use the youth rate. | other | 0.8 | Use of youth rates where they exist; share of under-20 workers. | C-9 loses its (+) chain; C-21 narrows. |
| A-13 | Workers under 20 and adults are substitutes in many low-wage jobs. | substitutability | 0.8 | Job tasks in restaurants and retail; age mix by job. | C-9 loses its (+) chain. |
| A-14 | The floor raises employers' labor cost per hour for the bound group: they cannot offset it fully by cutting non-wage terms, or by replacing the labor with equipment or other workers at the old cost. | substitutability | 0.8 | Non-wage compensation in minimum-wage jobs (small: few benefits to cut); cost of equipment against the wage it replaces. | C-3, C-6 to C-8, C-10 to C-16, C-19, C-20 fail; C-4 rests on CR-6 alone. |
| A-N1 | Employers' associations in restaurants, retail and recreation spend resources seeking changes (indexing rules, wider youth rate, exemptions) after passage. | other | 0.6 | Concentrated stake of low-wage-intensive industries; the bill passed over organized debate; review of the unindexed rate is likely. | C-24 fails. |

**Not reported (an assumption below 0.5).**
- Employers dismiss workers as they turn 20 (CR-4b, x: keep a worker at the adult rate, y: replace with a youth): needs A-9 (p 0.4).

## 11. Report

**The policy:** Larrow raises its minimum wage for workers aged 20 and over from $10 to $12 in Year 2 and $14 in Year 3, with no indexing after. Workers under 20 may be paid 85% of the adult minimum. Employers may not dismiss or cut the hours of adults in order to replace them with youth. The Labor Department enforces on complaint; workers may sue.

**Visible consequences:** Adults and youth who were paid below the new floors and keep their work receive a higher wage (C-1, C-2).

**Invisible consequences:**
- Adults paid near the floor: at least one of employment, hours or non-wage terms (breaks, training, schedules, benefits) falls (C-4). Those in jobs change jobs less often (C-8). Their total earnings may rise or fall (C-5).
- Job seekers: at the floor, more people seek low-wage work than employers wish to hire (C-6), and job seekers spend more time searching or waiting, or employers choose by other criteria (at least one, C-7).
- Employers: earn less on their capital (C-3), install more labor-saving equipment over time (C-10), offer less of their services (C-11), recast some workers as contractors (C-17), pay some workers in cash below the floor (C-18), open fewer new outlets in Larrow from the time the steps were expected (C-19), and spend more on records and on seeking changes to the law (C-21, C-24). Owners of fixed assets tied to these businesses lose value when the steps become expected (C-20).
- Customers in Larrow pay more for restaurant, retail and recreation services (C-12) and buy less (C-13). Larrow Falls residents shop and eat more in Port Dorran (C-14); Port Dorran sellers sell more and employ more (C-15, C-16).
- The state spends more on enforcement (C-22), drawn from other uses of the general budget (C-23).

**Ambiguous effects:**
- Earnings of low-paid adults (C-5): a higher wage against fewer hours, jobs or terms.
- Employment of workers under 20 (C-9): cheaper than adults under the youth rate, but their own floor rises and less is produced.

**Key conditions:** That the floor binds (A-1, p 0.9; A-2, p 0.8) and is complied with (A-3, p 0.75); that employers cannot fully offset the cost (A-14, p 0.8). Price and cross-border chains need A-10 (p 0.8) and A-11 (p 0.7). Contractor recasting rests on A-5 (p 0.55).

**What this analysis cannot say:** Whether employment of low-paid adults falls, or only their hours or non-wage terms; how large any change is; whether low-paid workers as a group gain or lose; whether the policy is good. Nor can it say how the gains of those who keep jobs at a higher wage compare with the losses of those who lose jobs, hours or terms. Health and well-being effects are out of scope for version 1 and are not analyzed.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | workers.adult_low_wage (employed adults paid below the new floor) | wage_rate | increase | short | visible | B | CR-1 (K1 op 1: employment below floor removed) | A-1, A-3 |
| C-2 | workers.youth (paid below the youth floor) | wage_rate | increase | short | visible | B | CR-1 (K2 op 1) | A-2, A-3 |
| C-3 | employers | return_on_capital | decrease | short | invisible | B | CR-1 (K1 op 1) → CR-3a (chosen option removed) | A-1, A-3, A-14 |
| C-4 | workers.adult_low_wage | employment, hours_worked, non_wage_compensation | at_least_one_decrease | short | invisible | B | CR-6 (pressure displaced to unregulated terms) and CR-4c (x: last hour of bound labor, y: equipment, other labor, not producing) → CR-12a | A-1, A-3, A-4, A-14 |
| C-5 | workers.adult_low_wage | earnings | ambiguous | short | invisible | B | (+) C-1; (−) C-4 → CR-12b | A-1, A-3, A-4, A-14 |
| C-6 | workers.prospective | excess_supply (labor at the floor) | increase | short | invisible | B | CR-6 (price held above clearing); CR-5a | A-1, A-3, A-14 |
| C-7 | workers.prospective | search_cost, wait_time, allocation_by_non_price_criteria | at_least_one_increase | short | invisible | B | C-6 → CR-6 (criteria by which employers choose among applicants) | A-1, A-3, A-14 |
| C-8 | workers.adult_low_wage | job_changes | decrease | medium | invisible | B | C-6 → CR-4b (x: leave a job paying the floor, y: keep it) → CR-3 | A-1, A-3, A-14 |
| C-9 | workers.youth | employment | ambiguous | short | invisible | B | (+) CR-4b (x: hire adult, y: hire youth at 85%); (−) CR-1 (K2 op 1) → CR-4c; (−) C-11 → LW-10 → CR-12b | A-2, A-3, A-12, A-13, A-14 |
| C-10 | employers | quantity_substitute (labor-saving equipment: kiosks, self-checkout) | increase | medium | invisible | B | CR-4b (x: an hour of bound labor, y: equipment) → CR-10b | A-1, A-7, A-14 |
| C-11 | employers | quantity_supplied (restaurant, retail and recreation services in Larrow) | decrease | medium | invisible | B | CR-9 (labor input_to services) → CR-4c (last units made costlier) | A-1, A-3, A-14 |
| C-12 | buyers.current (Larrow customers) | price_paid (low-wage-intensive services) | increase | medium | invisible | B | C-11 → CR-5c (range moved) with rivals bound alike → CR-7a | A-1, A-3, A-10, A-14 |
| C-13 | buyers.current (Larrow customers) | quantity_demanded (low-wage-intensive services) | decrease | medium | invisible | B | C-12 → CR-4c | A-1, A-3, A-10, A-14 |
| C-14 | buyers.current (Larrow Falls residents) | cross_border_purchases (shopping and eating in Port Dorran) | increase | medium | invisible | B | C-12 → CR-4b (x: buy in Larrow Falls, y: in Port Dorran) | A-1, A-3, A-10, A-11, A-14 |
| C-15 | neighboring_jurisdictions (Port Dorran sellers) | quantity_substitute (sales to Larrow residents) | increase | medium | invisible | B | C-14 → CR-9 (across_border) | A-1, A-3, A-10, A-11, A-14 |
| C-16 | neighboring_jurisdictions (Port Dorran workers in low-wage services) | employment | increase | medium | invisible | B | C-15 → CR-9 (labor input_to services) → LW-10 | A-1, A-3, A-10, A-11, A-14 |
| C-17 | employers | reclassification (workers recast as independent contractors) | increase | short | invisible | B | CR-4b (x: employee form, y: contractor form) | A-1, A-5, A-14 |
| C-18 | employers | informal_activity (cash pay below the floor) | increase | short | invisible | B | CR-6 (exchanges outside the rule) → CR-4b (x: comply, y: violate) | A-1, A-6 |
| C-19 | employers | investment_target (new low-wage-intensive outlets in Larrow) | decrease | short | invisible | B | CR-10a (steps expected from passage) → CR-4b (x: open in Larrow, y: elsewhere or not) | A-1, A-8, A-14 |
| C-20 | factor_owners.specific (owners of fit-outs and leases of low-wage-intensive businesses) | asset_value | decrease | short | invisible | B | CR-10c → CR-7c (moves when expected); CR-7b (lasting loss on immobile means) | A-1, A-8, A-14 |
| C-21 | employers | compliance_cost (age records; documentation against K3 claims) | increase | short | invisible | B | CR-1 (K2 op 2, K3 op 3) → CR-8c | A-12 |
| C-22 | officials.enforcement | enforcement_cost | increase | short | invisible | B | C-18 and more bound workers → CR-1 (K4) → CR-8c | A-1 |
| C-23 | taxpayers | resources_available_other_uses | decrease | short | invisible | B | C-22 → CR-8a | A-1 |
| C-24 | employers | lobbying_effort | increase | short | invisible | B | CR-1 (K1 op 1) → CR-4 (x: accept, y: lobby) | A-1, A-N1 |

## Gaps found

**(a) Calculus gaps.** None. Every step was derived from CR-1 to CR-12 and the foundations. The core rules were sufficient to license the contested core of the case only in its weak form (C-4 as a group; C-5 and C-9 ambiguous), which is what the task asks.

**(b) New premises.**
- A-N1 (p 0.6, other): CR-4 (x: accept, y: lobby) gives only the direction; that some employers' associations are at that margin is empirical and not among the case assumptions.

**(c) Unclear core rules.**
- CR-4 exception and labor supply (C-6): the exception (a change in total means can reverse the direction) is stated for buyers and savers; applying it to workers' hours offered at a higher wage, and seeing that it does not apply to those not hired, took a step the rule does not spell out.
- CR-6 versus CR-4c for C-4: CR-6 says pressure moves to unregulated terms (non-wage compensation), while CR-4c says the least-valued hours are given up. Each alone licenses a different member of the group; neither alone licenses "at least one of three". The group sign came from reading CR-6's "every margin that is still open" as covering hours and hiring as well as terms; CR-6 could say so explicitly.
- CR-7b in a market where customers also bear part of a cost (C-20 with C-12): CR-7b says lasting losses settle on the means that cannot move, but customers who cannot easily switch (A-10) are also "actors without alternatives". The rule does not say how to split the burden between immobile capital and immobile customers; the analysis gave only directions for each.
