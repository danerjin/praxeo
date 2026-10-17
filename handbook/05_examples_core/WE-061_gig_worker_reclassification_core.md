# WE-061 / Analysis: App-based drivers and couriers deemed employees, with a per-trip buy-out at the worker's option

Analyst: core-only re-run (Handbook 1.0)  |  Rules: core rules CR-1 to CR-12 only  |  Status: compared

## 1. Policy record

**Lanvik App-Based Work Act 2027.** Lanvik has about 9 million people. Most app work is in the Lanvik City metro area, whose eastern suburbs lie in Selvane, a state with no such law; about 8% of the metro area's app trips start in Selvane. Four network companies (two ride-hail, two delivery) each have well over 100 Lanvik workers; a few courier cooperatives have fewer than 100.

**Figures before the Act (last 12 months).** About 140,000 people did at least one trip; about 62,000 are active in a typical week, about 45% of them on more than one platform. They log about 1.3 million hours a week, about 58% (754,000 hours) on a trip. Pay averages 22.40 per hour on a trip (about 11.20 per trip at about 2.0 trips an hour), about 13.00 per hour logged in; vehicle costs are about 4 per hour logged in. About 20% of trip hours pay below 16 per trip hour; about 75% of logged-in hours pay below 16 per logged-in hour. In a typical week about 600 workers spend more than 40 trip hours with one platform and about 5,000 are logged in to one platform for more than 40 hours; about 24,000 earn under 150 from a given platform. Riders pay about 16.00 a trip. Platforms change fare shares and bonuses unilaterally several times a year, with 30 days' notice. The state minimum wage is 16 an hour. Lanvik City taxis: 1,800 medallions, metered fares set by the city, medallions trade at about 95,000.

**Arithmetic.** The premium is about 3.00 per trip hour (1.74 per logged-in hour), about 9% of the average fare. Contributions on the average fare share cost about 2.46 per trip hour. The §7 threshold is a notch: crossing 150 in a week adds about 16.50 of contributions on the first 150. Under U1-a the minimum binds on about a fifth of trip hours; under U1-b on about three quarters of logged-in hours.

| Field | Value | Source sentence |
|---|---|---|
| Jurisdiction (and what lies just outside) | Lanvik. Just outside: Selvane (about 8% of metro trips); companies with fewer than 100 Lanvik workers. | §3. |
| Announced / enacted / effective / expires | Introduced 10 January 2027; enacted 15 March 2027; effective 1 October 2027 (contractor agreements may be offered from 1 September 2027); no expiry. | §1, §14. |
| Enforcement (who, penalties, resources) | Department of Labor audits; private suits for double damages; 5,000 per misclassified worker; +4 million a year from the general fund. | §11. |

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Employee presumption | `mandated_contract_term` | Status of app-based workers | Network companies with 100 or more Lanvik workers | Employee unless the company proves (a) freedom from control, (b) work outside the usual course of business, (c) an independent trade. | Non-natural persons; companies under 100 workers. |
| K2 Minimum wage on engaged time | `price_floor` | Engaged time of employees | Network companies | 16 an hour of engaged time (U1). | Contractors under K5. |
| K3 Overtime | `mandated_contract_term` | Engaged time over 40 hours a week with one company | Network companies | 1.5 times the regular rate. | Contractors under K5. |
| K4 Contributions | `per_unit_tax` (on wages, with a notch) | Employees' wages | Network companies | 11% (2.7% unemployment insurance, 8.3% social insurance) of all wages in any week in which wages from the company exceed 150; insured wages count toward unemployment benefit (2,600 a year). | Weeks at or under 150; contractors under K5. |
| K5 Buy-out | `mandate_with_charge` | Status | The company elects; each worker chooses | Premium of 1.50 per completed trip, "in addition to the agreed fare share"; twelve months, revocable at the anniversary; employee status the default, on a separate screen. | — |
| K6 Enforcement | Enforcement | K1 to K5 | Department of Labor | +4 million a year, general fund. | — |

Unclear provisions:
- **U1, waiting time.** U1-a: time logged in and waiting is not engaged time (a worker may log off at will); only trip time and any scheduled shift is. U1-b: the apps lower the priority of workers who decline requests, so a logged-in worker is "required to remain available", and all logged-in time is engaged time. Readings get no probability; signs that depend on U1 are given per reading.

Counterfactual law: app workers are independent contractors; no minimum wage, overtime or contributions apply to them; companies set fare shares freely; taxi medallion cap and metered fares unchanged.

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | CR-1 operations | Core rules applied |
| --- | --- | --- | --- | --- |
| K1 Employee presumption | triangular | Yes where enforced (A-1); evasion risk where not (A-19) | 1 (removes, for covered companies and workers, the option of a contractor relation without a §9 agreement); 3 (penalty and damages attached to misclassification) | CR-4 (x: comply, y: violate; x: covered form, y: reclassified form), CR-5b, CR-6 |
| K2 Minimum wage | triangular | U1-a: on about a fifth of trip hours (A-3); U1-b: on about three quarters of logged-in hours | 1 (removes the option of employing at less than 16 per engaged hour) | CR-5a, CR-6, CR-7b, CR-4 |
| K3 Overtime | triangular | On about 600 workers (U1-a) or about 5,000 (U1-b) (A-17) | 3 (a 50% higher payment attached to engaged hours over 40 with one company) | CR-4c, CR-6 |
| K4 Contributions | binary | On employees' weeks over 150 | 3 (a charge on employing for more than 150 a week); notch at 150 (CR-1 1.0) | CR-4, CR-7b, CR-8b |
| K5 Buy-out | triangular and binary | Yes if companies elect (A-2) | 2 (adds, for workers, the option of a contractor agreement under the Act); 3 (attaches a 1.50 payment per trip to that option, paid by the company) | CR-2, CR-3b, CR-4, CR-5c, CR-6 |
| K6 Enforcement | binary | Yes (A-26) | 4 (means transferred to the Department from the general fund) | CR-8b, CR-8c |

Interactions: K5 opens an exit from K1 to K4 for workers who prefer it; the premium is a charge the company pays for each worker who leaves K2 to K4. K4's notch interacts with K2 through weekly wages. K1 binds only companies with 100 or more Lanvik workers, creating a boundary at 100 (CR-4, x: covered, y: under 100).

## 3. Actor classes

| Actor class | Role | How its options change (CR-1) |
| --- | --- | --- |
| network_companies | Four platforms with over 100 Lanvik workers | Op 1 and 3: must employ or pay the premium; minimum wage, overtime, contributions on employees. |
| network_company_shareholders | Owners of the platforms | Through CR-7c. |
| workers.below_16_per_trip_hour | Bicycle couriers on short orders, long low-fare rides (about a fifth of trip hours) | New option of employee status with a floor; or contractor with premium. |
| workers.waiting | Workers who wait much of their logged-in time (U1-b) | Under U1-b, the floor covers waiting. |
| workers.contractors | Workers who sign contractor agreements | Op 2 and 3: premium of 1.50 per trip. |
| workers.employees | Workers who take employee status | Floor, overtime, insurance; shifts and acceptance rules. |
| workers.over_40_hours | About 600 (trip hours) or 5,000 (logged-in) | Overtime pay or a cap. |
| workers.part_time_under_150 | About 24,000 weekly earners under 150 from one company | The contribution notch at 150. |
| workers.prospective | Would-be app workers | Premium attracts; fewer trips repel. |
| riders, restaurants, diners | Buyers of rides and deliveries | Higher prices passed on (A-4). |
| buyers.substitutes (transit, home cooking), taxi_medallion_owners, taxi_drivers | Substitute markets | Through CR-9 (substitute). |
| restaurants.own_couriers | Restaurants that hire their own couriers | Through CR-9 (substitute). |
| courier_cooperatives (under 100 workers) | Exempt competitors | Through CR-9 (same_market_other_segment); option of staying under 100. |
| selvane_riders, workers' hours in Selvane | Across the river | Through CR-9 (across_border). |
| unemployment_insurance_fund, social_insurance_fund | Receive contributions; pay benefits | CR-8b. |
| officials.department_of_labor | Enforcer | Op 4: +4 million. |
| taxpayers or recipients of other spending | Fund the Department | CR-8 0.7. |
| drivers' groups, unions, companies | Lobbies | CR-4 (x: accept, y: lobby). |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-1 | workers.below_16_per_trip_hour (employees) | wage_rate (per engaged hour) | increase | short; medium; long | CR-1 op 1, CR-5c, CR-2 | A-1, A-3, A-5 |
| C-2 | workers.waiting (employees) | wage_rate (per logged-in hour) | U1-a: no_change; U1-b: increase | short; medium; long | CR-1 op 1, CR-2 | A-1, A-23 |
| C-3 | workers.contractors | net_price_received (premium item, per trip) | increase | short; medium; long | CR-1 op 2 and 3, CR-2 | A-2 |
| C-6 | riders, restaurants | price_paid (app rides and delivery fees) | increase | short; medium; long | CR-5c, CR-7b, CR-9 | A-4 |
| C-8 | unemployment_insurance_fund, social_insurance_fund | tax_revenue (contributions) | increase | short; medium; long | CR-1 op 3, CR-8b | A-1, A-5 |

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-4 | workers.contractors | net_price_received (fare share item, per trip) | decrease | medium; long | CR-6 (pressure to the unregulated term), CR-5c | A-2, A-28 |
| C-5 | workers.contractors | net_price_received (total per trip) | increase | short | CR-12a | A-2, A-29 |
| C-5b | workers.contractors | net_price_received (total per trip) | ambiguous | medium; long | CR-12 0.8 (two items), CR-12b | A-2, A-28 |
| C-11 | riders, diners | quantity_demanded (app rides and deliveries) | decrease | short; medium; long | CR-4c | A-4 |
| C-12 | network_companies | quantity_traded (trips) | decrease | short; medium; long | CR-4c, CR-5 | A-4 |
| C-13 | workers.employees | employment (−), hours_worked (−), non_wage_compensation (flexibility) (−) | at_least_one_decrease | short; medium; long | CR-6, CR-5a | A-1, A-3, A-5 |
| C-14 | workers.employees | hours_worked (paid logged-in time outside scheduled shifts) | U1-a: no_change; U1-b: decrease | short; medium | CR-4c, CR-6 | A-6 |
| C-17 | workers | term_prevalence (employee status) | increase | short; medium; long | CR-2, CR-4 | A-1, A-5 |
| C-18 | workers | term_prevalence (contractor agreements with premium) | increase | short; medium; long | CR-2, CR-12 0.9 | A-2 |
| C-20 | workers.prospective | entry_rate (as contractors) | ambiguous | short; medium | CR-4, CR-12b | A-2, A-4, A-24 |
| C-21 | workers.over_40_hours | hours_worked (with one company, above 40) | decrease | short; medium; long | CR-4c, CR-6 | A-17 |
| C-23 | workers.part_time_under_150 | hours_worked (with one company, in weeks near 150) | decrease | short; medium; long | CR-1 1.0 (notch), CR-4 | A-18 |
| C-25 | network_companies | reclassification (marketplace models; one-person companies) | increase | medium; long | CR-4 (x: covered form, y: uncovered form), CR-12d | A-8 |
| C-26 | network_companies | legal_breach (misclassification; pressure to sign) | increase | short; medium | CR-4 (x: comply, y: violate), CR-12 0.9 | A-19 |
| C-27 | network_companies | allocation_by_non_price_criteria (dispatch steering requests to contractors) | increase | short; medium | CR-6 (criteria margin), CR-4 | A-2, A-7 |
| C-28 | network_companies, unions, drivers' groups | lobbying_effort (over the reading of §5(2), the court challenge and repeal) | increase | short; medium | CR-4, CR-12 0.9, CR-8c | A-16 |
| C-7 | network_companies | compliance_cost | increase | short; medium | CR-1 op 3, CR-8c | none |
| C-9 | officials.department_of_labor | enforcement_cost | increase | short; medium; long | CR-1 op 4, CR-8c | A-26 |

## 6. Second-order effects

Depth limit 4. Diffuse effects on the customers of restaurants, and on employers in other low-wage work (who gain or lose applicants), are pruned at depth 3.

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C-19 | workers.contractors | earnings (per hour logged in) | ambiguous | short; medium | CR-12b | - | A-2, A-4, A-24 |
| C-22 | workers.over_40_hours | hours_worked (with other network companies) | increase | short; medium; long | CR-7a, CR-9 | same_market_other_segment (other platforms) | A-17, A-N1 |
| C-24 | unemployment_insurance_fund, social_insurance_fund | tax_revenue_vs_static_projection | decrease | short; medium | CR-4, CR-12e | - | A-2, A-18 |
| C-29 | workers | hours_worked (trips starting in Selvane) | ambiguous | short; medium | CR-7a, CR-12b | across_border | A-2, A-14 |
| C-30 | courier_cooperatives | quantity_traded (deliveries by services under 100 workers) | increase | medium; long | CR-9, CR-4 | same_market_other_segment | A-4, A-15 |
| C-31 | restaurants | quantity_traded (delivery orders) | decrease | short; medium; long | CR-9, CR-4c | complement (delivery is used with restaurant meals) | A-4, A-12 |
| C-32 | restaurants.own_couriers | employment (restaurants' own couriers) | increase | medium | CR-9, CR-4 | substitute | A-4, A-13 |
| C-33 | diners | home_production (meals cooked at home) | increase | short; medium | CR-9, CR-4 | substitute | A-4, A-12 |
| C-34 | taxi_medallion_owners | asset_value (medallions) | increase | short (from January 2027); medium | CR-9, CR-6, CR-7c, CR-10c | substitute (taxis for app rides) | A-4, A-10, A-11 |
| C-34b | taxi_drivers | right_lease_price (medallion lease) | increase | short; medium | CR-6 0.8 (a free price's rise) | substitute | A-4, A-10 |
| C-35 | network_company_shareholders | asset_value (shares) | decrease | short (from January 2027); medium | CR-7c, CR-10c | - | A-4, A-11 |
| C-36 | network_companies | net_price_received (per trip, net of worker pay and contributions) | decrease | short; medium | CR-7b | - | A-4 |
| C-37 | unemployment_insurance_fund | subsidy_outlay (unemployment benefits) | increase | medium; long | CR-9, CR-8b | contract (employment) | A-1, A-20 |
| C-38 | riders | wait_time | ambiguous | short; medium | CR-6, CR-12b | - | A-4, A-6 |
| C-39 | taxpayers or recipients of other spending | resources_available_other_uses | at_least_one_decrease | short; medium; long | CR-8b, CR-8 0.7 | - | A-26 |
| C-40 | workers.below_16_per_trip_hour (employees) | earnings | ambiguous | short; medium | CR-12b, CR-12c | - | A-1, A-3, A-5 |
| C-41 | workers.employees | non_wage_compensation (total: insurance cover against flexibility) | ambiguous | short; medium | CR-12 0.8 (two items), CR-12b | - | A-21, A-22 |
| C-15 | workers.employees | term_prevalence (unemployment and social insurance cover) | increase | short; medium; long | CR-1 op 3, CR-2 | contract (employment) | A-1, A-5 |

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance premise | Combined sign |
| --- | --- | --- | --- | --- |
| workers.contractors, net_price_received (total per trip), short | premium 1.50 (A-2) | fare share cut: not in the first months (A-29) | not needed | increase (C-5) |
| workers.contractors, same, medium; long | premium (C-3) | fare share cut (C-4, A-28) | none | ambiguous (C-5b); each item reported separately (C-3, C-4) |
| workers.contractors, earnings per hour logged in | premium per trip | fewer trips per hour (A-4); entry of new contractors, partial at first (A-24); fare share cut later (A-28) | A-25 would give dominance but has p 0.35 (not used) | ambiguous (C-19) |
| workers.prospective, entry_rate | premium per trip | fewer trips; fare share cut | none | ambiguous (C-20) |
| workers.below_16 (employees), earnings | wage rate up (C-1) | hours or employment down (C-13) | none | ambiguous (C-40) |
| workers.employees, non_wage_compensation | insurance cover (C-15; valued, A-22) | flexibility lost to shifts and acceptance rules (A-21) | none | ambiguous (C-41) |
| workers, hours in Selvane | employees displaced from Lanvik hours (C-13, C-21) move to Selvane trips (A-14) | contractors drawn to Lanvik trips by the premium (A-2, A-14) | none | ambiguous (C-29) |
| riders, wait_time | U1-b: companies schedule employees and cut paid waiting (A-6), so fewer idle drivers; under both readings, fewer employee hours (C-13) | fewer trips demanded (C-11) | none | ambiguous (C-38) |
| riders, price_paid | cost per trip up under both readings (premium, floor, contributions, overtime) | none | not needed | increase (C-6) |
| network_companies, net_price_received | none | part of the added cost not passed on (CR-7b, A-4) | not needed | decrease (C-36) |

The election (K5) and the default (K1 to K4) are alternatives for each worker, not chains on the same worker: the analysis splits workers by their choice (CR-1 0.7). Different variables (wage rate, hours, earnings) are not netted (CR-12c).

## 8. Time structure

- **Introduction (10 January 2027) to effect (1 October 2027).** Share prices and medallion values move as the Act becomes likely, part of the way before enactment on 15 March (CR-7c, CR-10c; C-34, C-35), given that buyers expect it to survive (A-11). Contractor agreements may be offered from 1 September (CR-10a): companies elect before the default applies.
- **Fare shares.** In the first months, fare shares are not cut (A-29; 30 days' notice and scrutiny), so contractors gain the full premium per trip (C-5). Later, companies may cut fare shares (A-28), so the total per trip becomes ambiguous (C-5b).
- **Entry.** Onboarding takes four to six weeks (A-24), so any entry of new contractors is partial at first; the sign of entry is ambiguous (C-20).
- **Twelve-month agreements.** A worker's choice is fixed for twelve months and revocable at each anniversary; responses to fare share cuts by moving back to employee status therefore come at anniversaries (CR-10b).
- **Insurance.** Insured wages build toward the 2,600 threshold over time, so unemployment benefit claims (C-37) arise from the medium term.
- **Reclassification.** Marketplace models and one-person companies take time to set up (C-25, medium and long).

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
| --- | --- | --- | --- | --- | --- |
| C-7 | network_companies | compliance_cost | increase | Payroll, scheduling, onboarding screens and legal work | CR-8c |
| C-9 | officials.department_of_labor | enforcement_cost | increase | 4 million a year of other public uses | CR-8c |
| C-39 | taxpayers or recipients of other spending | resources_available_other_uses | at_least_one_decrease | The 4 million taken from the general fund | CR-8b, CR-8 0.7 |
| C-28 | network_companies, unions, drivers' groups | lobbying_effort | increase | Staff time and money spent on the reading, the court challenge and repeal | CR-8c |
| C-11 | riders, diners | quantity_demanded (app rides and deliveries) | decrease | Trips not taken at the higher price (CR-5a for exchanges no longer made) | CR-5a, CR-4c |
| C-13 | workers.employees | employment (−), hours_worked (−), non_wage_compensation (flexibility) (−) | at_least_one_decrease | Exchanges below the floor no longer made: workers who would have worked those hours, and companies that would have bought them, lose an expected gain | CR-5a, CR-6 |

CR-8b symmetry: the premium (C-3) is paid by the companies (C-36) and in part by riders (C-6); contributions (C-8) are paid by the companies and, in part, by workers and riders (CR-7b, shares not ranked); unemployment benefits (C-37) are paid by the fund from contributions.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
| --- | --- | --- | --- | --- | --- |
| A-1 | The Act is enforced: audits and private suits with double damages make treating workers as contractors without a valid agreement costly. | enforcement | 0.8 | 4 million budget; damages; litigation record. | C-1, C-2, C-8, C-13, C-15, C-17, C-37, C-40 fail or weaken. |
| A-2 | Each company elects to offer contractor agreements. | other | 0.75 | Companies' statements; the premium was their proposal. | C-3 to C-5b, C-18 to C-20, C-24, C-27, C-29 fail; all workers become employees. |
| A-3 | Some hours on a trip pay below 16 per trip hour (about a fifth). | binding | 0.9 | Platform data. | C-1, C-13, C-40 fail under U1-a. |
| A-4 | Platforms pass part of their added cost per trip into fares and fees, and some riders and diners take fewer trips at the higher price. | substitutability | 0.8 | Past fare and fee changes. | C-6, C-11, C-12, C-30 to C-36 fail. |
| A-5 | Workers paid below 16 per trip hour mostly choose employee status. | other | 0.65 | 16 against about 11 plus a premium of about 3. | C-1, C-13, C-15, C-17 fail. |
| A-6 | Under U1-b, companies schedule employees' logged-in time to cut paid waiting. | other | 0.85 | Practice of hourly employers. | C-14 fails. |
| A-7 | Companies can steer requests between employees and contractors through dispatch. | other | 0.6 | The Act is silent on dispatch. | C-27 fails. |
| A-8 | Some services can be reshaped to meet the three conditions at a cost below the Act's burden. | other | 0.5 | Marketplace models elsewhere. | C-25 loses this chain. |
| A-9 | Some workers can work through one-person companies, which §3 does not cover. | other | 0.55 | Incorporation cost; contracting practice. | C-25 loses this chain. |
| A-10 | Taxis are a substitute for some app rides, at fares fixed by the city, with the medallion cap binding. | substitutability | 0.8 | Medallion prices. | C-34, C-34b fail. |
| A-11 | Buyers of shares and medallions expect the Act to survive the court challenge and repeal campaign. | expectations | 0.7 | Legislative margins. | C-34, C-35 smaller. |
| A-12 | Restaurants' delivery orders fall as delivery fees rise. | other | 0.8 | Order data. | C-31, C-33 fail. |
| A-13 | Some restaurants hire their own couriers rather than pay the higher fees. | substitutability | 0.55 | Larger chains already do. | C-32 fails. |
| A-14 | Some workers can move hours between trips starting in Selvane and in Lanvik. | mobility | 0.65 | 8% of trips; home locations. | C-29 has no chain. |
| A-15 | Some delivery services can operate with fewer than 100 Lanvik workers. | other | 0.5 | Cooperatives now. | C-30 fails. |
| A-16 | Companies, drivers' groups and unions can organize at a cost below their stakes. | other | 0.9 | Existing associations. | C-28 fails. |
| A-17 | Some workers exceed 40 hours a week with one company (about 600 on trips; about 5,000 logged in), and companies can cap them. | other | 0.85 | Platform data. | C-21, C-22 fail. |
| A-18 | Companies control dispatch enough to keep part-time employees' weekly wages at or under 150. | other | 0.7 | About 24,000 under 150 a week. | C-23, C-24 fail. |
| A-19 | Enforcement is imperfect: some misclassification and some pressure to sign occur. | enforcement | 0.65 | Audit rates. | C-26 fails. |
| A-20 | Some employees whose hours are cut qualify for and claim benefits. | other | 0.6 | 2,600 reached in about 160 hours at 16. | C-37 fails. |
| A-21 | Some workers who become employees value the flexibility they lose to shifts and acceptance rules. | other | 0.75 | Surveys. | C-41 becomes increase. |
| A-22 | Workers value insurance cover at more than nothing. | other | 0.7 | Take-up of voluntary cover. | C-41 becomes decrease. |
| A-23 | Under U1-b, workers who wait much of their logged-in time choose employee status. | other | 0.7 | 16 against about 13 plus 1.74. | C-2 fails under U1-b. |
| A-24 | Onboarding of new contractors takes four to six weeks, so entry is partial in the first months. | durability | 0.6 | Background checks. | C-19, C-20 lose the timing note. |
| A-25 | The premium dominates the effects of entry and fewer trips on contractors' hourly earnings. | other | 0.35 | No direct evidence. | Not used (below 0.5). |
| A-26 | The Department's 4 million is new money from the general fund. | revenue_use | 0.9 | §11. | C-9, C-39 change payers. |
| A-28 | §9 does not fix the fare share, and companies can cut fare shares and bonuses after launch. | other | 0.75 | Routine share changes. | C-4 fails; C-5b becomes increase. |
| A-29 | Fare shares are not cut in the first months. | other | 0.6 | Notice practice. | C-5 becomes ambiguous. |
| A-N1 | Some workers whose hours with one company are capped at 40 can work the extra hours for another network company. | substitutability | 0.75 | NEW. About 45% of active workers already work on more than one platform. Flagged: needed for C-22. | C-22 fails. |

**Not reported** (an assumption below 0.5):
- Contractors' hourly earnings rise: needs A-25 (p 0.35). Without it C-19 and C-20 are ambiguous (CR-12 0.8, kind 2 chains with p of at least 0.5 on the other side).
- If companies do not elect (A-2 false, p 0.25), every covered worker becomes an employee and the floor binds much more widely under U1-b; not reported.

### Final check before the report

1. Uncombined chains: contractors' total per trip, hourly earnings and entry; employees' earnings and non-wage terms; Selvane hours; riders' waiting were each combined in section 7, including the time-structure chains (fare share cuts, onboarding).
2. Group signs: C-13 (employment, hours or flexibility), C-39 (payers of the general fund).
3. Baseline: every sign is against Lanvik with contractor status and no Act, not against a version without the buy-out.
4. Worse off is not poorer: no resources consequence is claimed for riders; they buy fewer trips (C-11).
5. Timing: share and medallion values are dated from introduction; fare shares per window (C-5 short, C-5b medium and long).
6. Both sides: premium (paid by companies, partly riders), contributions (fund and payers), Department (general fund).
7. Every class, every rule: CR-7c on shares and medallions; CR-6 on the floor (group) and the medallion cap; CR-9 along substitute, complement, across_border, same_market_other_segment and contract relations; CR-4 (x: comply, y: violate) on companies.
8. Unstated premises: A-N1 added and flagged.
9. No pattern is cited.

## 11. Report

**The policy:** From 1 October 2027, app-based drivers and couriers working for a network company with 100 or more Lanvik workers are employees unless the company proves three conditions. Employees get at least 16 an hour of engaged time and overtime above 40 hours with one company. The company pays 11% contributions in weeks when an employee earns more than 150. A company may instead offer every worker a twelve-month contractor agreement, with a premium of 1.50 per trip on top of the fare share. It is unclear whether waiting time counts as engaged time (U1).

**Visible consequences:** Low-paid workers who become employees earn a higher wage per engaged hour (C-1). Under U1-b, so do workers who mostly wait (C-2). Contractors receive 1.50 more per trip (C-3), and in the first months more in total per trip (C-5). Riders and restaurants pay more (C-6). The insurance funds collect contributions (C-8).

**Invisible consequences:**
- *Employees:* employment, hours or flexibility fall (C-13). Under U1-b, paid waiting outside shifts is cut (C-14). Hours above 40 with one company are capped (C-21) and partly moved to other platforms (C-22). Part-time employees' wages are held at or under 150 a week (C-23). Employees gain insurance cover (C-15), and some claim unemployment benefit later (C-37).
- *Contractors:* fare shares are cut after the first months (C-4).
- *Companies:* compliance costs (C-7), a lower net price per trip (C-36) and lower share values from the Act's introduction (C-35). Some reshape services or contract with one-person companies (C-25), some misclassify or press workers to sign (C-26), and dispatch steers requests toward contractors (C-27). Lobbying over the reading and the repeal increases (C-28).
- *Markets nearby:* fewer trips and deliveries (C-11, C-12), fewer restaurant delivery orders (C-31), more restaurant-employed couriers (C-32), more home cooking (C-33), more business for services with fewer than 100 workers (C-30). Taxi medallions gain value, and their lease price rises (C-34, C-34b).
- *State:* the Department's enforcement costs (C-9) are paid from the general fund (C-39). Contributions fall short of a static projection (C-24).

**Ambiguous effects:** Contractors' total pay per trip after the first months (C-5b) and their hourly earnings (C-19). Entry of new contractors (C-20). Low-paid employees' total earnings (C-40). Employees' non-wage terms as a whole (C-41). Hours on trips starting in Selvane (C-29). Riders' waiting times (C-38). Section 7 says what would decide each.

**Key conditions:** Enforcement (A-1, 0.8). Companies elect the buy-out (A-2, 0.75). Low-paid workers choose employee status (A-5, 0.65). Costs are passed into fares (A-4, 0.8). Fare shares can be cut after launch (A-28, 0.75), but not in the first months (A-29, 0.6). Capped workers can work for another platform (A-N1, 0.75, added).

**What this analysis cannot say:** How large any effect is. Whether workers as a whole gain. How the burden is split between companies, workers and riders. Whether the policy is good. Safety and health effects of shifts and caps are out of scope.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C-1 | workers.below_16_per_trip_hour (employees) | wage_rate (per engaged hour) | increase | short; medium; long | visible | B | CR-1 (op 1: no employment below 16 per engaged hour, enforced, A-1); CR-2 (those below 16 choose employee status, A-5); binds on about a fifth of trip hours (A-3) | A-1, A-3, A-5 |
| C-2 | workers.waiting (employees) | wage_rate (per logged-in hour) | U1-a: no_change; U1-b: increase | short; medium; long | visible | B | U1-a: waiting is not engaged time, so K2 attaches nothing to it; U1-b: CR-1 op 1 on all logged-in time, and waiting workers choose employee status (CR-2, A-23) | A-1, A-23 |
| C-3 | workers.contractors | net_price_received (premium item, per trip) | increase | short; medium; long | visible | B | CR-1 (op 2: the contractor agreement; op 3: 1.50 per completed trip, A-2); CR-2 | A-2 |
| C-4 | workers.contractors | net_price_received (fare share item, per trip) | decrease | medium; long | invisible | B | CR-6 (the premium raises the cost of each contractor trip; the fare share is an unregulated term, A-28, and the pressure moves to it); CR-5c (any change in what one party must give moves the range) | A-2, A-28 |
| C-5 | workers.contractors | net_price_received (total per trip) | increase | short | visible | B | CR-12a: premium (C-3) and no fare share cut in the first months (A-29) | A-2, A-29 |
| C-5b | workers.contractors | net_price_received (total per trip) | ambiguous | medium; long | invisible | B | CR-12 0.8 (two items in one variable) and CR-12b: (+) C-3, (−) C-4; no dominance premise | A-2, A-28 |
| C-6 | riders, restaurants | price_paid (app rides and delivery fees) | increase | short; medium; long | visible | B | CR-5c (premium, floor, overtime and contributions raise the cost of each trip under both readings); CR-7b (part passed into fares and fees, A-4) | A-4 |
| C-7 | network_companies | compliance_cost | increase | short; medium | invisible | A | CR-1 (op 3: payroll, the separate screen, records, contributions); CR-8c | none |
| C-8 | unemployment_insurance_fund, social_insurance_fund | tax_revenue (contributions) | increase | short; medium; long | visible | B | CR-1 (op 3: 11% on employees' wages in weeks over 150); CR-8b; there are employees (A-5) and the Act is enforced (A-1) | A-1, A-5 |
| C-9 | officials.department_of_labor | enforcement_cost | increase | short; medium; long | invisible | A | CR-1 (op 4: +4 million); CR-8c (means used up in enforcing) | A-26 |
| C-11 | riders, diners | quantity_demanded (app rides and deliveries) | decrease | short; medium; long | invisible | B | CR-4c (the last trip, valued least, is given up at the higher price, A-4); CR-5a (exchanges no longer made lose both sides an expected gain) | A-4 |
| C-12 | network_companies | quantity_traded (trips) | decrease | short; medium; long | invisible | B | CR-4c and CR-5 (C-11) | A-4 |
| C-13 | workers.employees | employment (−), hours_worked (−), non_wage_compensation (flexibility) (−) | at_least_one_decrease | short; medium; long | invisible | B | CR-6 (a floor that binds, A-3, A-5, sends the pressure to every open margin: fewer employees, fewer hours, shifts and acceptance rules); CR-5a; under U1-b the floor binds far more widely | A-1, A-3, A-5 |
| C-14 | workers.employees | hours_worked (paid logged-in time outside scheduled shifts) | U1-a: no_change; U1-b: decrease | short; medium | invisible | B | U1-a: waiting is unpaid, so nothing changes on this margin; U1-b: CR-4c and CR-6 (each hour of waiting now costs 16; companies schedule and cut it, A-6) | A-6 |
| C-15 | workers.employees | term_prevalence (unemployment and social insurance cover) | increase | short; medium; long | invisible | B | CR-1 (op 3: contributions make wages insured); CR-2 (employees chosen, A-5); relation: contract (employment) | A-1, A-5 |
| C-17 | workers | term_prevalence (employee status) | increase | short; medium; long | visible | B | CR-2 (from none under the counterfactual; low-paid workers choose it, A-5); CR-4 | A-1, A-5 |
| C-18 | workers | term_prevalence (contractor agreements with premium) | increase | short; medium; long | visible | B | CR-2 and CR-12 0.9 (an agreement that exists only under the Act, offered by electing companies, A-2) | A-2 |
| C-19 | workers.contractors | earnings (per hour logged in) | ambiguous | short; medium | invisible | B | CR-12b: (+) premium per trip (C-3); (−) fewer trips per logged-in hour (C-11, A-4), entry (A-24), fare share cuts (C-4); A-25 (p 0.35) cannot be used for dominance | A-2, A-4, A-24 |
| C-20 | workers.prospective | entry_rate (as contractors) | ambiguous | short; medium | invisible | B | CR-4 (x: stay out, y: enter): y improved per trip, worsened by fewer trips (A-4); CR-12b; partial in the first months (A-24) | A-2, A-4, A-24 |
| C-21 | workers.over_40_hours | hours_worked (with one company, above 40) | decrease | short; medium; long | invisible | B | CR-1 op 3 (K3: 1.5 times the rate above 40); CR-4c and CR-6 (companies cap employees at 40, A-17); about 600 workers under U1-a, 5,000 under U1-b | A-17 |
| C-22 | workers.over_40_hours | hours_worked (with other network companies) | increase | short; medium; long | invisible | B | CR-7a (capped hours move to the next use where yields are equal); CR-9 (relation: same_market_other_segment, other platforms, A-N1) | A-17, A-N1 |
| C-23 | workers.part_time_under_150 | hours_worked (with one company, in weeks near 150) | decrease | short; medium; long | invisible | B | CR-1 1.0 (the 150 threshold is a notch: crossing it adds about 16.50 on the first 150); CR-4 (x: cross, y: stay at or under 150; dispatch control, A-18) | A-18 |
| C-24 | unemployment_insurance_fund, social_insurance_fund | tax_revenue_vs_static_projection | decrease | short; medium | invisible | B | CR-4 (workers choose contractor agreements, A-2; companies hold weeks at or under 150, A-18; caps and cuts in hours, C-13); CR-12e (responses can only reduce the base against a projection on all current earnings) | A-2, A-18 |
| C-25 | network_companies | reclassification (marketplace models; one-person companies) | increase | medium; long | invisible | B | CR-4 (x: covered form, y: uncovered form); CR-12d: two independent chains, marketplace models meeting the three conditions (A-8) and one-person companies outside §3 (A-9); either suffices | A-8 |
| C-26 | network_companies | legal_breach (misclassification; pressure to sign) | increase | short; medium | invisible | B | CR-4 (x: comply, y: violate; enforcement imperfect, A-19); CR-12 0.9 (the breach exists only under the Act) | A-19 |
| C-27 | network_companies | allocation_by_non_price_criteria (dispatch steering requests to contractors) | increase | short; medium | invisible | B | CR-6 (the criteria by which the scarce side chooses: each employee trip costs more than a contractor trip where the floor binds, so requests are steered, A-7); CR-4 | A-2, A-7 |
| C-28 | network_companies, unions, drivers' groups | lobbying_effort (over the reading of §5(2), the court challenge and repeal) | increase | short; medium | invisible | B | CR-4 (x: accept, y: lobby; U1 alone moves the floor from a fifth of trip hours to three quarters of logged-in hours); CR-12 0.9 (the dispute over §5(2) exists only under the Act); CR-8c; groups can organize (A-16) | A-16 |
| C-29 | workers | hours_worked (trips starting in Selvane) | ambiguous | short; medium | invisible | B | CR-7a and CR-9 (across_border, A-14): (+) employees' displaced hours move to Selvane; (−) contractors drawn to Lanvik trips by the premium (A-2); CR-12b | A-2, A-14 |
| C-30 | courier_cooperatives | quantity_traded (deliveries by services under 100 workers) | increase | medium; long | invisible | B | CR-9 (same_market_other_segment: covered companies' prices rise, A-4); CR-4 (x: covered service, y: service under 100, A-15) | A-4, A-15 |
| C-31 | restaurants | quantity_traded (delivery orders) | decrease | short; medium; long | invisible | B | CR-9 (complement: delivery is used with restaurant meals); CR-4c (higher fees, A-4, A-12) | A-4, A-12 |
| C-32 | restaurants.own_couriers | employment (restaurants' own couriers) | increase | medium | invisible | B | CR-9 (substitute: own couriers for platform delivery); CR-4 (x: platform, y: own couriers, A-13) | A-4, A-13 |
| C-33 | diners | home_production (meals cooked at home) | increase | short; medium | invisible | B | CR-9 (substitute); CR-4 (x: delivery, y: home cooking, A-12) | A-4, A-12 |
| C-34 | taxi_medallion_owners | asset_value (medallions) | increase | short (from January 2027); medium | invisible | B | CR-9 (substitute: taxis for app rides, A-10); CR-6 (the medallion cap fixes the quantity and fares are fixed, so the higher demand is rationed by the medallion's value); CR-7c and CR-10c (captured by holders as the Act becomes expected, A-11) | A-4, A-10, A-11 |
| C-34b | taxi_drivers | right_lease_price (medallion lease) | increase | short; medium | invisible | B | CR-6 0.8 (a free price's rise satisfies the margin conclusion: the lease price rations the capped medallions, A-10) | A-4, A-10 |
| C-35 | network_company_shareholders | asset_value (shares) | decrease | short (from January 2027); medium | invisible | B | CR-7c and CR-10c (expected yields fall with C-36; borne by holders when the Act becomes expected, part of the way from introduction, A-11) | A-4, A-11 |
| C-36 | network_companies | net_price_received (per trip, net of worker pay and contributions) | decrease | short; medium | invisible | B | CR-7b (each side bears part of the added cost; only part is passed on, A-4) | A-4 |
| C-37 | unemployment_insurance_fund | subsidy_outlay (unemployment benefits) | increase | medium; long | invisible | B | CR-9 (contract: insured wages qualify employees for benefit); CR-8b; hours cut (C-13) and claims made (A-20) | A-1, A-20 |
| C-38 | riders | wait_time | ambiguous | short; medium | invisible | B | CR-6 and CR-12b: (+) fewer employee hours (C-13), and under U1-b scheduled shifts cut idle drivers (A-6); (−) fewer trips demanded (C-11) | A-4, A-6 |
| C-39 | taxpayers or recipients of other spending | resources_available_other_uses | at_least_one_decrease | short; medium; long | invisible | A | CR-8b and CR-8 0.7 (payers from the general budget: the 4 million is new money, A-26) | A-26 |
| C-40 | workers.below_16_per_trip_hour (employees) | earnings | ambiguous | short; medium | invisible | B | CR-12b: (+) wage rate up (C-1); (−) employment or hours down (C-13) | A-1, A-3, A-5 |
| C-41 | workers.employees | non_wage_compensation (total: insurance cover against flexibility) | ambiguous | short; medium | invisible | B | CR-12 0.8 (two items): (+) insurance cover, valued (C-15, A-22); (−) flexibility lost to shifts and acceptance rules (A-21); CR-12b | A-21, A-22 |

## Gaps found

**(a) Steps no core rule covers.**
- GAP-061-C1: The worker's choice between employee status and the contractor agreement depends on the company's later freedom to cut the fare share, which the worker cannot observe when signing. CR-2 and CR-11 cover choice on beliefs, but no core rule says how to sign the effect of a term that one party can change after the other has chosen (A-28) beyond treating it as a premise.

**(b) Core-rule wording that was hard to apply.**
- CR-1 0.7 splitting by response versus by operation: K5 gives every worker the same option, but workers respond differently; splitting the class by the choice made (employees, contractors) made it hard to state counterfactual signs for "workers" as a whole.
- CR-6 on a floor with an exit option: the pressure from the floor goes partly to the buy-out (a margin that the policy itself creates). CR-6 lists unregulated terms, criteria and violations, but not a legal exit the policy offers; it was recorded under the criteria margin (C-27) and as term prevalence (C-18).
- CR-12 0.8 kind 2 with a premise below 0.5 (A-25): the rule says to report the derived sign and record the chain; here the derived chains themselves oppose each other, so there was no single derived sign to report (C-19).
- CR-4 1.0 (lobbying against the counterfactual contest): it is unclear whether lobbying over the reading of §5(2) should be compared with the pre-Act contest over classification; it was treated as an activity that exists only under the Act.

**(c) Vocabulary missing from the ontology.**
- No variable for the share of a group's work or sales across a border (hours on Selvane trips were recorded as `hours_worked` with a qualifier).
- No variable for worker status choice as distinct from `term_prevalence`; no variable for dispatch priority (used `allocation_by_non_price_criteria`).
- No generic actor class for social insurance funds (recorded as the insurance funds).

## Comparison with the pattern-based analysis

**Summary.** The two versions agree on the main structure of the Lanvik case. Low-paid workers who become employees are paid the floor, and contractors receive the premium. In the first months contractors' pay per trip rises; after fare shares are reset it is `ambiguous`, with the fare share item falling. Fares rise and trips fall. Employees lose employment, hours or flexibility as a group. Hours bunch at the 40-hour kink and the 150 notch, and work is reshaped outside the Act or evaded. Restaurants sell fewer delivery orders and employ more couriers, medallions and platform shares are revalued, and the insurance funds collect contributions and pay benefits. Contractors' hourly earnings, employees' earnings and hours in Selvane are `ambiguous` in both. Both versions sign against Lanvik without the Act, not against the mandate without a buy-out. Both treat the premium as a mandated term undone through the free fare share, the core from CR-6's main clause and CR-5c without the prompt of PC-17's 0.9 clause. There is one S row. On riders' waits under U1-a, the pattern gives `decrease` and the core `ambiguous`; both are defensible (J). The pattern version applies RS-22 to a term the employer changes in response to the floor (C-32). It also assumes contractors keep records (C-39), and its "riders who keep riding" class (C-38) does not meet CR-3's condition. The core version overclaims on contributions against the static projection (C-24), omitting that the floor and overtime raise the wage base. It omits taxi trips, the insurance fund's net balance and contractors' waiting. The pattern version omits the entry of new contractors, which it uses as a chain without signing, as well as paid waiting cut under U1-b, the medallion lease price, home cooking, the prevalence of contractor agreements and the total of employees' non-wage terms.

Counts: M 20, V 12, S 1, OP 7, OC 6.

### Pattern version → core version

| Pattern ID | Matched core ID(s) | Class | Cause | Note |
| --- | --- | --- | --- | --- |
| C-1 | C-1, C-2 | V | | The core splits by the unit of the floor: trip hours below 16 (C-1) and waiting workers per logged-in hour (C-2: U1-a no_change, U1-b increase). |
| C-2 | C-3 | M | | |
| C-3 | C-15 | V | | Recorded as `term_prevalence` of insurance cover rather than `non_wage_compensation`. |
| C-4 | C-8 | M | | |
| C-5 | C-7 | M | | |
| C-6 | C-6 | M | | |
| C-7 | C-11, C-12 | V | | Split by side (riders' demand; companies' trips). |
| C-8 | C-13 | V | | The pattern's group also includes `wage_rate` above the floor (−). The core's group has employment, hours and flexibility. |
| C-9 | C-27 | V | | Same variable, different content: the pattern records selection among employees by rating (PC-11), the core dispatch steering to contractors. Both need A-7 and the premise that rationing by criteria rises against a counterfactual in which dispatch already ranks drivers. |
| C-10 | C-17 | M | | |
| C-11 | C-36 | V | | Pattern: the platforms' labor cost per unit rises (RS-23 re-signed). Core: platforms' net price per trip falls (CR-7b), with the premium and contributions as the payer side of C-3 and C-8 (CR-8b symmetry note). Same chain, other variable. |
| C-12 | C-4 | M | | |
| C-13 | C-5 | M | | |
| C-14 | C-5b | M | | |
| C-15 | C-25 | M | | The core lists only A-8, though its CR-12d derivation runs on A-8 or A-9. CR-12d asks for each chain's premises to be listed. |
| C-16 | C-25 | V | | The core combines one-person companies into the companies' reclassification key. |
| C-17 | C-26 | M | | |
| C-18 | C-21 | V | | Pattern: worker-weeks just below 40 increase. Core: hours above 40 with one company decrease. |
| C-19 | C-22 | V | | Pattern: `reclassification` (hours split across companies). Core: `hours_worked` with other platforms increase (A-N1). |
| C-20 | C-23 | V | | Pattern: worker-weeks at or under 150 increase. Core: hours in weeks near 150 decrease. |
| C-21 | C-30 | V | | Pattern: `number_of_sellers` under 100 increase. Core: deliveries by services under 100 increase. Both rest on A-15. |
| C-22 | C-28 | M | | The core's key adds "the court challenge and repeal". Classification was contested without the Act (suits under the old test), so CR-4 1.0 signs lobbying on that question only against that contest. The core's `increase` holds for the U1 dispute, not for repeal lobbying. The core flagged this. |
| C-23 | C-29 | M | | |
| C-24 | C-38 | S | J | Pattern: riders' waits U1-a decrease (U1-b `ambiguous`). Core: `ambiguous` under both. The pattern argues from entry, whose sign its own C-35 leaves open (core C-20: `ambiguous`). The U1-a sign can be derived another way. With pay per trip up and hourly yields equalized (CR-7a), trips per logged-in hour fall, so idle capacity per request rises. The core's opposing chain is "fewer employee hours", which is only a member of the `at_least_one_decrease` group C-13 and not signed alone. Under U1-a, displaced employees can sign contractor agreements. Both defensible. |
| C-25 | none | OC | E | Taxi trips increase (CR-4, CR-9 substitute). Valid with a premise that taxis have spare capacity at the fixed fare (A-10 says the cap binds on medallions, not trips). Core-version omission: it records medallion values and lease prices only. |
| C-26 | C-34 | M | | |
| C-27 | C-35 | M | | |
| C-28 | C-31 | M | | |
| C-29 | C-32 | M | | |
| C-30 | C-37 | M | | |
| C-31 | none | OC | E | Insurance fund's net balance `ambiguous`. CR-8 1.0 asks for receipts and outlays of the same budget to be recorded as two items and a net. The core recorded both items (C-8, C-37) but not the net. Core-version omission. |
| C-32 | none | OC | P | RS-22 misapplied. Its precondition is a term changed by the policy. Flexibility is cut by the employer as a response to the floor (CR-6; pattern C-8). The insurance term's effect on other terms is PC-17's gross-and-net clause (CR-7 0.7), already in C-8. Recorded separately, the `wage_rate`-above-floor member duplicates C-8 with the opposite member sign. The core's C-41 (the non-wage total) is the correct key. Nothing scorable lost, since the result is `ambiguous`. |
| C-33 | C-40 | M | | |
| C-34 | none | OC | E | Contractors' waiting (U1-a increase; U1-b `ambiguous`). Core-version omission. On the pattern's sign: the CR-7a argument in C-24 supports `increase` once hourly yields settle. In the short run, though, dispatch steering of low-fare requests to contractors (A-7) also acts under U1-a and pushes the other way. The pattern lists it only under U1-b. |
| C-35 | C-19 | V | | `wage_rate` per logged-in hour against `earnings` per logged-in hour. Both `ambiguous`; the core gets there without the response argument. |
| C-36 | C-9 | M | | |
| C-37 | C-39 | M | | |
| C-38 | none | OC | J | Riders "who keep riding" have less for other uses. CR-3's note signs this only for those who keep spending on the burdened option, and riders who keep riding but take fewer trips may spend less. The core declined (final check, item 4). The pattern's class should be riders whose trips do not fall, with a premise. Both defensible on CR-3's wording. |
| C-39 | none | OC | E | Contractors' `compliance_cost` for trip records. No provision requires contractors to keep records; checking the premium is their own choice (CR-2). Pattern hidden premise: needs an assumption or should be dropped. |

### Core-only consequences

| Core ID | Class | Cause | Note |
| --- | --- | --- | --- |
| C-14 | OP | E | Employees' paid logged-in time outside shifts: U1-a no_change, U1-b decrease (A-6). The pattern states A-6 (p 0.85) but uses it only inside the group C-8. Pattern-version omission. |
| C-18 | OP | E | Contractor agreements with the premium: `term_prevalence` increase from none (CR-12 0.9, A-2). Pattern-version omission (trivial). |
| C-20 | OP | E | Entry of new contractors `ambiguous` (CR-4: better per trip, fewer trips per hour). The pattern's C-24 and C-34 use an entry chain as if signed, without recording it. Pattern-version omission. |
| C-24 | OP | E | Contributions against the static projection `decrease`. The core claims "responses can only reduce the base", but the floor (C-1, C-2) and overtime raise wages per engaged hour for employees who are kept, and under U1-b they pay for waiting time. Those chains enlarge the base. Without a dominance premise the sign is `ambiguous`. Core-version error. |
| C-33 | OP | E | Diners cook more at home (CR-9 substitute, A-4, A-12). The pattern names home cooking as a substitute under A-4 but records no key. Pattern-version omission. |
| C-34b | OP | E | Medallion lease price increase (CR-6 0.8: a free price's rise). Pattern-version omission. |
| C-41 | OP | E | Employees' non-wage terms in total `ambiguous` (CR-12 0.8 two items: cover +, flexibility −). The pattern records the items (C-3, and flexibility within C-8) but not the total the 0.8 note asks for. The core's (−) item is itself only a member of the group C-13, so it should cite A-6 or A-21 for it. |

### Findings

- **Pattern overclaims or hidden premises.** *PC-17's 0.9 buy-out clause* would treat the premium as a TX-2 wedge. The pattern version overrode it, and the core version, using CR-6's main clause (pressure to the unregulated fare share) and CR-5c, reached the same items and signs (C-3, C-4, C-5, C-5b). The clause is wrong for a charge paid to the counterparty. *RS-23*'s second clause ("the remaining pool is cheaper to serve") compares pools, not worlds. The core never made that comparison and recorded only `term_prevalence` and the companies' net price against no Act. *RS-17*'s first clause compares below with above; the core signed every line directly. *RS-22*'s If clause ("a policy changes a term of a job") does not exclude terms the employer changes in response to the policy. Applied to flexibility (C-32), it double-counts PC-17's adjustment. *PC-11* signs the criteria margin at Tier A "given the surplus". Where the counterfactual already rations by non-price criteria (app dispatch by rating), an `increase` needs a premise (C-9 uses A-7). C-39 (contractors' records) and the class in C-38 rest on unstated premises.
- **Errors in the core version.** Contributions against the static projection (C-24) omit the chains by which the floor and overtime raise the wage base. Lobbying (C-28) includes repeal and court lobbying, which CR-4 1.0 signs against the counterfactual contest over classification. The C-25 assumptions omit A-9, though the derivation uses it. Riders' waits (C-38) and the non-wage total (C-41) use a member of the group C-13 as a signed chain. Omissions: taxi trips (pattern C-25), the insurance fund's net (C-31, required by CR-8 1.0), contractors' waiting (C-34).
- **Errors in the pattern version.** RS-22 is applied to an employer's response (C-32). An entry chain is used without being signed (C-24, C-34; core C-20 is `ambiguous`). U1-a dispatch steering is left out of contractors' waits (C-34). C-38 and C-39 rest on unstated premises. Omissions: paid waiting cut under U1-b (core C-14), contractor-agreement prevalence (C-18), entry (C-20), home cooking (C-33), medallion lease price (C-34b), the non-wage total (C-41).
- **Test of 1.0 verdicts.** *PC-17 0.9 buy-out (failed as written):* confirmed. Without the pattern, the core treated the premium as an operation 3 on the worker's added option, with pressure to the unregulated fare share, not as a wedge. *PC-10 on engaged time (needed interpretation on the unit of the floor):* confirmed. The core had to split the floor's effect by unit and reading (C-1 against C-2, C-14). *RS-23 (needed re-signing):* confirmed: the core has no "cheaper pool" claim against no Act. *CR-6 0.8 on free terms (worked, but beyond the case it is written for):* partly contradicted. CR-6's main clause ("the terms that are not regulated") was enough for the core. The 0.8 note matters only for the stickiness premise (A-29), which both versions state. *CR-12 1.0, the response argument (needed interpretation on a second response through another market):* not tested by the core, which reached `ambiguous` for contractors' hourly earnings (C-19) by listing the chains under CR-12b without the argument. *RS-17's first clause (re-signed):* confirmed by core C-21 to C-23.
- **Limits of the core rules.** None produced a difference: no row has cause K. GAP-061-C1 (a term one party can change after the other has chosen) is not a gap: CR-6's main clause and CR-10a handle it with a premise (A-28), which is the right answer. Unclear core-rule wording: (1) CR-6 does not list a legal exit the policy itself creates (the buy-out) among the open margins. (2) CR-6 0.8's note on free terms is written for existing contracts; it could say that a mandated add-on to an unregulated price sends the pressure to that price. (3) CR-12e's 1.0 note does not say whether a response by another class, through another market, is a second response. (4) CR-12 0.8, kind 2, does not say what to report when the derived chains themselves oppose and the dominance premise is below 0.5 (core C-19). (5) CR-12 does not say whether a member of an `at_least_one` group can serve as a signed chain in another combination (core C-38, C-41). (6) CR-3's note "keep spending on the burdened option" does not say whether it means any purchase or an unchanged quantity (pattern C-38). (7) CR-4 1.0 on lobbying does not say whether a dispute over a new provision's reading is a new question when the underlying question was contested. (8) CR-1 does not say how to record an option removed and added back only if the other party first elects to offer it.
