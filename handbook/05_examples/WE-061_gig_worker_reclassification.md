# WE-061 App-based drivers and couriers deemed employees, with a per-trip buy-out at the worker's option

Analyst: draft (Handbook 1.0 held-out test, corrected under 1.1)  |  Rule catalog version: 1.1  |  Status: awaiting expert review

A stylized policy in a fictional state. Several real jurisdictions have tested app-based drivers against an employment test, and some have allowed a payment in place of employee status; this one is not modeled on any of them. It is a held-out test of catalog 1.0 on a case none of the 1.0 changes were drawn from. It probes PC-17 (a mandated contract term) and its 0.9 clause on a buy-out, here at the worker's option and paid to the worker rather than to the state; PC-10 (a minimum wage, here on "engaged time" only); RS-23 (selection under a uniform term, promoted in 1.0) and whether its conclusions are against the no-policy counterfactual; RS-22 (compensating differential); RS-17's 1.0 clauses on hours lines, notches and kinks; RS-5 (reclassification); CR-6's 0.9 clause on splitting a shift between price and quantity and its 0.8 note on terms that are free to change; and CR-12's 1.0 notes on what the response argument needs and on the baseline of patterns, with its 0.8 note on two items in one variable (a statutory premium up, a free fare share down). The unclear provision is whether time spent logged in and waiting counts as engaged time. The counterfactual throughout is **Lanvik without the Act**: app-based drivers and couriers working as independent contractors, under the existing minimum wage, overtime and insurance laws, which do not reach them. Effects on road safety and health are outside the scope of version 1. The probabilities are illustrative; the evidence column says what a real analysis would cite.

## 1. Policy record

**Lanvik App-Based Work Act 2027.** Lanvik is a state of about 9 million people. Most app-based work is in the Lanvik City metro area, whose eastern suburbs lie across the Tolvar River in the state of Selvane; about 8% of the metro area's app trips start in Selvane, which has no such law. Four network companies operate in Lanvik: two ride-hail platforms and two delivery platforms, each with well over 100 workers. A few local courier cooperatives have fewer than 100.

**Figures (last 12 months, before the Act).** About 140,000 people did at least one ride or delivery; in a typical week about 62,000 are active, about 45% of them on more than one platform. They log about 1.3 million hours a week, of which about 58% (about 754,000 hours) is time on a trip, from accepting a request to completing it. The platforms pay workers an average of 22.40 per hour on a trip (about 11.20 per trip, at about 2.0 trips per hour on a trip: 1.6 for rides, 2.4 for deliveries), or about 13.00 per hour logged in. Workers bear their own vehicle costs (about 4 per hour logged in). About 20% of hours on a trip pay less than 16 per hour on a trip (bicycle couriers on short orders, long low-fare rides). About 75% of hours logged in pay less than 16 per hour logged in. In a typical week about 600 workers spend more than 40 hours on trips for one platform, and about 5,000 are logged in to one platform for more than 40 hours. About 24,000 of those active in a week earn less than 150 from a given platform that week. Riders pay on average about 16.00 a trip; the platforms keep the difference. Platforms set and change workers' fare shares and bonuses unilaterally, usually several times a year, with 30 days' notice.

The state minimum wage is 16 an hour (indexed). Taxis in Lanvik City are licensed separately: the city caps medallions at 1,800 and sets metered fares; medallions trade at about 95,000.

**Statute.**
- §3. An app-based worker is an employee of the network company unless the company proves that (a) the worker is free from its control and direction in performing the work, (b) the work is outside the usual course of its business, and (c) the worker is customarily engaged in an independently established trade. §3 applies to natural persons who perform rides or deliveries through a network company with 100 or more app-based workers in Lanvik.
- §5. An employee shall be paid at least the state minimum wage for all engaged time. §5(2): "'Engaged time' means the time from when a worker accepts a request for a ride or delivery until the worker completes it, and any other time during which the worker is required by the network company to remain available to perform work."
- §6. Engaged time over 40 hours in a workweek with one network company is paid at 1.5 times the regular rate.
- §7. The network company pays unemployment insurance (2.7%) and state social insurance (8.3%) contributions, 11% in all, on all wages paid to an employee in any week in which the employee's wages from that company exceed 150. Insured wages count toward unemployment benefit eligibility (2,600 in a base year).
- §9. A network company may elect to offer its app-based workers in Lanvik a contractor agreement; an election applies to all its Lanvik workers. A worker who signs one is not an employee for the purposes of §5 to §7 for the following twelve months, and may revoke it at each anniversary. For every ride or delivery completed under a contractor agreement, the company shall pay the worker, "in addition to the agreed fare share", a premium of 1.50. Employee status must be offered as the default, on a separate screen, and the choice must be freely made.
- §11. The Department of Labor enforces the Act by audit; workers have a private right of action for double damages; the penalty for misclassification is 5,000 per worker. The Department's budget is raised by 4 million a year from the general fund.

**Arithmetic.** The premium is about 3.00 per hour on a trip (1.50 × 2.0 trips), about 1.74 per hour logged in, and about 9% of the average rider fare. Contributions on an employee paid the average fare share cost about 2.46 per hour on a trip (11% × 22.40). The §7 threshold is a notch: crossing 150 in a week adds about 16.50 of contributions on the first 150. Under U1-a, a worker on a trip at the average rate already earns more than 16 an hour on the trip; the minimum binds on about a fifth of trip hours. Under U1-b, the minimum applies to all logged-in time, and binds on about three quarters of logged-in hours.

The bill was introduced on 10 January 2027 and enacted on 15 March 2027; it takes effect on 1 October 2027, and contractor agreements may be offered from 1 September 2027. No expiry.

| Field | Value | Source sentence |
|---|---|---|
| Jurisdiction (and what lies just outside) | Lanvik. Just outside: Selvane (eastern suburbs of the metro area, about 8% of trips); companies with fewer than 100 workers in Lanvik. | §3. |
| Announced / enacted / effective / expires | Introduced 10 January 2027; enacted 15 March 2027; effective 1 October 2027; no expiry. | §1, §14. |
| Enforcement (who, penalties, resources) | Department of Labor audits; private suits for double damages; 5,000 per misclassified worker; +4 million a year from the general fund. | §11. |

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Employee presumption | `mandated_contract_term` | The status of app-based workers | Network companies with 100 or more Lanvik workers | Employee unless the three conditions are proved. | Non-natural persons; companies under 100 workers. |
| K2 Minimum wage on engaged time | `price_floor` | Engaged time of employees | Network companies | 16 an hour of engaged time (U1). | Contractors under K5. |
| K3 Overtime | `mandated_contract_term` | Engaged time over 40 hours a week with one company | Network companies | 1.5 times the regular rate. | Contractors under K5. |
| K4 Contributions | `per_unit_tax` (on wages, with a notch) | Employees' wages | Network companies | 11% of all wages in any week in which wages from the company exceed 150. | Weeks at or under 150; contractors under K5. |
| K5 Buy-out | `mandate_with_charge` | Status | The company elects; each worker chooses | Premium of 1.50 per completed trip, paid to the worker, "in addition to the agreed fare share"; twelve months, revocable at the anniversary. | — |
| K6 Enforcement | Enforcement | K1 to K5 | Department of Labor | +4 million a year, general fund. | — |

Unclear provision:
- **U1, waiting time.** Is time logged in and waiting for a request "time during which the worker is required by the network company to remain available"? Reading U1-a: no. A worker may log off at will, so only time on a trip, and any shift a company schedules, is engaged time. Reading U1-b: yes. The apps reduce the priority of workers who decline requests, so a logged-in worker is required to remain available; all logged-in time is engaged time. The Department's draft guidance quotes §5(2) without applying it, and the legislative record is silent.

Readings get no probability; where a sign depends on U1, one sign per reading is given.

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | Rule families |
|---|---|---|---|
| K1 | Triangular: removes, for both parties, the option of contracting as principal and independent contractor without the K5 premium (CR-1, operation 1). The counterfactual law is contractor status under the old common-law test, under which the platforms prevailed in the courts. | Yes: no worker is an employee now (A-1). | PC-17, RS-5, RS-3, RS-17 (1.0: firm threshold; 1.1: baseline) |
| K2 | Triangular: a floor on the price of an hour of engaged time; what an "hour" is depends on U1. | U1-a: on about 20% of trip hours (A-3). U1-b: on about 75% of logged-in hours. | PC-10, PC-11 (1.1: rationing already in the counterfactual), CR-6, PC-17 |
| K3 | Triangular: a higher price above a line on hours (a kink). | U1-a: about 600 workers; U1-b: about 5,000 (A-17). | RS-17 (1.0: kink; line on hours) |
| K4 | Binary: a tax on wages with a notch at 150 a week (CR-1, 1.0: notch). Receipts go to the state insurance fund, which pays benefits to employees who qualify. | Yes, for employees above 150 a week. | TX-1, RS-17 (1.0: notch, eligibility), CR-8 (1.0: receipts into the same budget) |
| K5 | Triangular: the option removed by K1 is recorded as removed, and the restoring option as operation 2 for the party who holds the election: first the company (to offer the agreement), then the worker (to sign it) (CR-1, 1.1). A mandated per-trip payment from the company to the worker is attached to the restored option (operation 3). The payment goes to the counterparty, not to the state, so TX-2 does not apply to it: it is a transfer within the exchange, added to a fare share the company can still set, and can be undone through it (PC-17, 1.1; CR-6). The buy-out is a legal exit the Act itself creates, and so one of the margins open to displaced pressure (CR-6, 1.1). | Yes, if elected (A-2). | PC-17 (0.9: buy-out; 1.1: a buy-out paid to the worker), RS-23 (1.1: baseline), CR-6 (0.8: free terms; 1.1: margins the policy creates), CR-12 (0.8: two items) |
| K6 | Binary: enforcement from the general budget. | Yes | OC-3, OC-1 |

**Split by response (CR-1, 0.7).** Every worker faces the same provisions, but they respond differently. Before the Act they differ in two ways that decide their choice: what they are paid per hour on a trip (`drivers.low_fare`: below 16) and how much of their logged-in time is spent waiting (`drivers.low_util`: utilization well under the average 58%). After it, they split into `drivers.employee` and `drivers.contractor` by choice.

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `platforms` | The four network companies: sellers of rides and deliveries, buyers of workers' time | Must treat workers as employees or, if they elect K5, pay contractors 1.50 a trip; may still set fare shares, fares and dispatch. |
| `drivers.employee` | Workers who are employees after 1 October 2027 | Paid at least 16 an hour of engaged time; overtime; contributions paid on them; the company may now schedule and direct them. |
| `drivers.contractor` | Workers who sign a contractor agreement | 1.50 a trip on top of the fare share, which the company may change; keep logging in at will. |
| `drivers.low_fare` | Workers whose pay per hour on a trip is below 16 (about a fifth of trip hours) | Gain most from employee status under either reading. |
| `drivers.low_util` | Workers who spend much of their logged-in time waiting | Under U1-b, paid 16 for every logged-in hour as employees. |
| `drivers.high_util` | Workers with many trips per logged-in hour | Gain most from the per-trip premium. |
| `drivers.prospective` (`sellers.prospective`) | People who might start app work as contractors | Higher pay per trip at first; fewer trips per hour. |
| `riders` | Riders and diners (`buyers.current`) | Fares and delivery fees; pickup and delivery waits. |
| `sellers.complements` | Restaurants that sell through delivery apps | Delivery fees charged to their customers. |
| `workers.inhouse_couriers` | Couriers employed directly by restaurants | Restaurants may deliver themselves. |
| `sellers.substitutes` | Taxi drivers and companies (fares set by the city; 1,800 medallions) | Riders who leave the apps. |
| `owners.medallions` (`factor_owners.specific`) | Owners of taxi medallions when the Act became expected | Values capitalize the change. |
| `owners.platforms` | Shareholders of the network companies | Values capitalize the change. |
| `sellers.small_platform` (`sellers.prospective`) | Delivery services with fewer than 100 Lanvik workers | Exempt from §3. |
| `neighboring_jurisdictions` | Selvane riders and drivers in the metro area | Drivers move between Lanvik and Selvane trips. |
| `state_insurance_fund` | Unemployment and social insurance funds | Receive contributions, pay benefits to app workers who qualify. |
| `officials.enforcement` | Department of Labor | New audits and cases. |
| `taxpayers`, recipients of other spending, future taxpayers | General fund | Pay the Department's 4 million. |
| `lobbying groups` | Platforms, drivers' groups, unions | Stakes in U1, the premium, and guidance on §3. |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | `drivers.employee` (hours paid below 16) | `wage_rate` (pay per hour of engaged time) | U1-a: increase; U1-b: increase | short (from October 2027) | PC-10, PC-17, CR-1 | A-1, A-3 |
| C-2 | `drivers.contractor` | `net_price_received` (the 1.50 premium per trip: item 1) | increase | short | PC-17 (1.1), CR-1 | A-1, A-2 |
| C-3 | `drivers.employee` | `non_wage_compensation` (unemployment and social insurance cover) | increase | short to medium | PC-17, CR-1, CR-8b | A-1, A-5 |
| C-4 | `state_insurance_fund` | `tax_revenue` (contributions on app workers' wages) | increase | short | TX-1, CR-8b | A-1, A-5 |
| C-5 | `platforms` | `compliance_cost` (classification, payroll, records of engaged time, the election) | increase | short | CR-8c, OC-2 | none |

**The mandate and the buy-out (PC-17).** Employee status with its terms (K2 to K4) is absent from every contract now: the mandate binds (A-1). PC-17 applies to those who become employees: the cost of the contract to the company rises, and the bargaining range moves, so the other terms adjust: for an employment term, a mixed group of the wage above the floor, non-wage terms and hours or jobs. PC-17's 0.9 clause splits the bound class by response: PC-17 for those who provide the term, TX-2 for those who pay the charge. Here the "charge" is paid to the worker, not to the state, and it is the worker who chooses (after the company elects). So TX-2 does not fit, as PC-17's 1.1 clause now says: a buy-out at the worker's option paid to the worker is a transfer within the exchange, and where it is added to a price the payer can still set freely, it can be undone through that price (CR-6). The terms that adjust are compared with no Act, not with the contract minus the term (PC-17, 1.1). C-2 is the premium as an item; whether contractors' pay per trip rises in total is section 7's question (C-12 to C-14).

**Who becomes an employee depends on U1.** Under U1-a, a worker paid above 16 per hour on a trip gains little in pay from employee status, while a contractor gains about 3.00 per hour on a trip; most workers sign the contractor agreement if it is offered, except those paid below 16 per hour on a trip (A-5). Under U1-b, an employee is paid at least 16 for every logged-in hour, against about 13.00 plus 1.74 for a contractor: workers who wait a lot gain from employee status too (A-23). C-1, C-3 and C-4 need at least some employees, which A-5 gives under both readings (and A-2's failure would make every worker an employee).

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-6 | `riders` | `price_paid` (fares and delivery fees) | increase | short to medium | RS-14, PC-17, CR-6 (0.9: splitting a shift), CR-5c | A-4, A-5 |
| C-7 | `riders`, `drivers.employee`, `drivers.contractor` | `quantity_traded` (rides and deliveries) | decrease | short to medium | PC-17, CR-4c, CR-6 (0.9), OC-4 | A-4, A-5 |
| C-8 | `drivers.employee` | `hours_worked` (−), `employment` (−), `non_wage_compensation` (flexibility, −), `wage_rate` (above the floor, −) | U1-a: at_least_one_decrease; U1-b: at_least_one_decrease | short to medium | PC-10, PC-17, CR-6 | A-1, A-3 |
| C-9 | `drivers.employee` | `allocation_by_non_price_criteria` (shifts and requests allotted by rating and acceptance, beyond the counterfactual's dispatch ranking) | U1-a: increase; U1-b: increase | short to medium | PC-11 (1.1), CR-6 | A-1, A-3, A-7, A-31 |
| C-10 | `drivers.low_fare` | `term_prevalence` (employee status) | increase | short | RS-23, CR-4 | A-1, A-5 |
| C-11 | `platforms` | `price_paid` (labor cost per engaged hour of employees; per trip of contractors) | U1-a: increase; U1-b: increase | short | RS-23 (re-signed, CR-12 1.0; RS-23 1.1: baseline), PC-17, CR-8b | A-1, A-5, A-29 |
| C-40 | `drivers.employee` | `hours_worked` (paid waiting time outside scheduled shifts) | U1-a: no_change; U1-b: decrease | short to medium | CR-4, CR-6, PC-10 | A-1, A-6 |
| C-42 | `drivers.contractor` | `term_prevalence` (contractor agreements with the premium) | increase | short | CR-1 (1.1), CR-12 (0.9: activities that exist only under the policy) | A-2 |
| C-43 | `drivers.prospective` | `entry_rate` (new contractors) | ambiguous | short to medium | CR-4, CR-12b | A-2, A-4 |
| C-15 | `platforms` | `reclassification` (services reshaped to meet the three conditions: workers set their own fares, carry several brands) | increase | medium | RS-5, CR-4 | A-8 |
| C-16 | `drivers.contractor`, `drivers.employee` | `reclassification` (work done through one-person companies, outside "natural person") | increase | short to medium | RS-5, CR-4 | A-9 |
| C-17 | `platforms`, `drivers.employee` | `legal_breach` (workers treated as contractors without a valid agreement; agreements not freely made; engaged time unpaid) | increase | short to medium | RS-3, CR-4 (x: comply, y: violate) | A-19 |
| C-18 | `drivers.employee` | `hours_worked` (worker-weeks just below 40 hours with one company: engaged under U1-a, logged in under U1-b) | U1-a: increase; U1-b: increase | short to medium | RS-17 (1.0: kink; a line on hours; 1.1: baseline), CR-4 | A-17 |
| C-19 | `drivers.employee` | `reclassification` (hours split across companies to stay under 40 with each) | U1-a: increase; U1-b: increase | short to medium | RS-17, RS-5 | A-17 |
| C-20 | `drivers.employee` (part-time) | `hours_worked` (worker-weeks with wages from one company just at or below 150) | increase | short to medium | RS-17 (1.0: notch), CR-1 (1.0: notch), CR-4 | A-18 |
| C-21 | `sellers.small_platform` | `number_of_sellers` (delivery services with fewer than 100 Lanvik workers) | increase | medium | RS-17 (1.0: notch), CR-4 | A-15 |
| C-22 | `lobbying groups` | `lobbying_effort` (on provisions that exist only under the Act: U1, the premium, guidance on §3) | increase | short to medium | RS-7 (1.0), CR-4 (1.0; 1.1: the same question), CR-12 (0.9) | A-16 |
| C-23 | `neighboring_jurisdictions` (Selvane drivers and riders) | `quantity_supplied` (worker-hours on trips starting in Selvane) | ambiguous | short to medium | RS-4, CR-7a, CR-12b | A-2, A-14 |

**Fares and trips (C-6, C-7).** Every platform in Lanvik faces the added cost of employees (contributions, top-ups, overtime: A-5) and of the premium while fare shares are slow to adjust (A-29). RS-14: where all competitors face the same cost, the price rises. The fixed costs of classification and payroll systems (C-5) are a cost per firm, not per trip (CR-4, 0.8), and are not counted toward the fare. The shift is in the cost of supply; CR-6's 0.9 clause says how it divides between price and quantity needs a premise about riders' response. A-4 (riders neither buy the same number of trips at any fare nor drop the apps at a small rise; taxis, transit and cooking at home are partial substitutes) gives both: fares up (C-6) and trips down (C-7). The trips not taken were exchanges both riders and workers expected to gain from (OC-4).

**Employees (C-8, C-9; PC-10).** For employees, the wage cannot adjust below the floor, so the pressure goes to the margins that remain open (CR-6; PC-17's group): the company cuts employee hours or jobs, sets shifts and acceptance rules that reduce flexibility, or pays less above the floor to employees whose fare share exceeded it. Recorded as a group, `at_least_one_decrease`, under both readings; under U1-b the floor binds on most logged-in time, so the company has a strong reason to schedule employees and limit their logged-in time (A-6). Those kept are paid at least the floor (C-1). With more workers seeking employee hours than the company wants at the floor, it chooses among them by rating and acceptance (C-9; PC-11), and steers low-fare requests to contractors where it can (A-7: the Act is silent on dispatch). Dispatch already ranks drivers by rating and acceptance without the Act, so under PC-11's 1.1 clause only the change in that rationing is signed: C-9 rests on A-31, that the floor's surplus of employee hours is rationed by stricter criteria than the counterfactual's ranking (shift allocation, acceptance thresholds). Under U1-b, paid waiting outside scheduled shifts is cut (C-40; A-6), which is signed on its own premise rather than taken from the group C-8; under U1-a waiting is unpaid in both worlds (no_change).

**Selection (C-10, C-11; RS-23).** The company's election is uniform (§9), and each worker then chooses the status that serves them better: a uniform term (employee status, with a floor per hour) against an alternative priced by each worker's output (the premium per trip). Workers paid below 16 per hour on a trip choose employee status under either reading (C-10; A-5). Under U1-b, workers who wait a lot choose it too (A-23); under U1-a they do not gain in pay from it, and their choice turns on how they value insurance cover against the premium and flexibility, which no premise settles (not recorded). RS-23 then says "the provider's cost per counterparty rises; under the alternative, the remaining pool is cheaper to serve". Its second clause compares the contractor pool with the average pool, not with Lanvik without the Act; it is re-signed (CR-12, 1.0): against no Act, the platform's labor cost rises for both pools, by the contributions and top-ups for employees and by the premium for contractors while fare shares hold (C-11). The selection itself says which workers end up in which pool; it is not a consequence against the counterfactual, where no one is an employee (RS-23, 1.1: the remaining pool is signed against no Act only with a premise on what it would have been). Contractor agreements themselves exist only under the Act and rise from none wherever a company elects (C-42; A-2).

**Reclassification and evasion (C-15 to C-17).** Some services can be reshaped to meet the three conditions (workers set their own fares and carry several brands), which takes them outside K1 entirely (C-15; RS-5; A-8). §3 applies to natural persons, so some workers operate through one-person companies (C-16; A-9). Some companies treat workers as contractors without a valid agreement, or press them to sign; some leave engaged time unpaid (C-17; RS-3; A-19). RS-20 does not apply: enforcement is by audit as well as by complaint.

**Hours lines (C-18 to C-21; RS-17).** Three lines, of two kinds. The overtime line (40 hours a week with one company) is a kink: only hours above it cost more (RS-17, 1.0). Companies keep employees under it, and employees who want more hours split them across companies (C-18, C-19). Under U1-a the line is on engaged time and touches about 600 workers; under U1-b it is on logged-in time and touches about 5,000. The contributions line (150 a week) is a notch: crossing it puts 11% on the whole week's wages (CR-1, 1.0; RS-17, 1.0). A company that controls dispatch keeps part-time employees at or just under 150 a week (C-20; A-18). The worker's side of the notch is the mirror: insured wages count toward unemployment benefit eligibility, so the worker gains from crossing (RS-17, 1.0, eligibility); the company decides, so the bunching follows the company's side. The firm-size line (100 workers) is a notch on the whole workforce: new delivery services stay under it (C-21; A-15). RS-17's first clause compares "just below relative to just above"; each sign here is re-signed against no Act (CR-12, 1.0): the count just below each line rises from those who would have been above it.

**Lobbying (C-22).** Whether app workers are employees was contested without the Act (suits under the old test were pending), so lobbying on that question, including repeal, is not signed (CR-4, 1.0; RS-7, 1.0). The reading of U1, the premium and the Department's guidance on the three conditions are provisions that exist only under the Act, and CR-4's 1.1 note says lobbying over such provisions (the reading of a new clause) is an increase, even though the field was contested.

**Entry of new contractors (C-43).** A higher pay per trip at first (C-13) makes contracting better for would-be entrants, but fewer trips (C-7) mean fewer trips per hour logged in; from the medium run the per-trip total is itself `ambiguous` (C-14). CR-4 signs neither way: entry is `ambiguous`, and it is not used as a signed chain anywhere (C-24, C-34, C-35).

**Selvane (C-23).** Drivers can choose trips that start in Selvane or in Lanvik (A-14) and move toward the side that yields more per hour (CR-7a; RS-4). For contractors, a Lanvik trip carries the premium; but Lanvik fares are higher and trips fewer (C-6, C-7), so hourly yield in Lanvik is itself ambiguous (C-14). Under U1-b, workers who cannot get employee shifts in Lanvik add hours in Selvane. No premise ranks these: `ambiguous`.

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-24 | `riders` | `wait_time` (pickup and delivery waits) | U1-a: decrease; U1-b: ambiguous | short | CR-6, CR-9, CR-7a, CR-12e (1.1: the response argument in every direction), CR-12b | workers' idle time and riders' waits: `same_market_other_segment` | A-2, A-4, A-6, A-29 |
| C-25 | `sellers.substitutes` (taxis) | `quantity_substitute` (taxi trips) | increase | short to medium | RS-1, RS-16 | taxis and app rides: `substitute` | A-4, A-10 |
| C-26 | `owners.medallions` | `asset_value` (taxi medallions) | increase | short (from January 2027) | CR-6 (a fixed quantity at a set fare), CR-7c, CR-10c, SB-4 | as C-25 | A-10, A-11 |
| C-45 | `owners.medallions` | `right_lease_price` (taxi medallions) | increase | short to medium | CR-6 (0.8: a free price's rise), CR-9 | as C-25 | A-10 |
| C-27 | `owners.platforms` | `asset_value` (shares, for the value of Lanvik operations) | decrease | short (from January 2027) | CR-7c, CR-10c | — | A-11 |
| C-28 | `sellers.complements` (restaurants) | `quantity_traded` (delivery orders) | decrease | short to medium | RS-12, CR-9 | delivery `complement` to restaurant meals sold through apps | A-4, A-12 |
| C-29 | `workers.inhouse_couriers` | `employment` (+), `hours_worked` (+) (couriers employed by restaurants) | at_least_one_increase | medium | RS-1, CR-9, LW-10, CR-6 (1.1: labor demand as a group) | in-house delivery `substitute` for app delivery | A-13 |
| C-44 | `riders` (diners) | `home_production` (meals cooked at home) | increase | short to medium | RS-1, CR-4, CR-9 | home cooking `substitute` for delivered meals | A-4, A-12 |
| C-30 | `state_insurance_fund` | `subsidy_outlay` (benefits paid to app workers) | increase | medium | CR-8b | contributions and cover: `contract` (statutory) | A-5, A-20 |
| C-31 | `state_insurance_fund` | `fund_balance` (contributions from app work less benefits paid to app workers) | ambiguous | medium | CR-8 (1.0: receipts into the same budget), CR-12b | as C-30 | A-5, A-20 |
| C-33 | `drivers.employee` | `earnings` | ambiguous | medium | PC-10 (note), CR-4c, CR-12b, CR-12c, CR-12 (1.1: group members are not chains) | — | A-1, A-3, A-4 |
| C-41 | `drivers.employee` | `non_wage_compensation` (total: insurance cover and flexibility) | U1-a: increase; U1-b: ambiguous | short to medium | PC-17 (gross and net), CR-12 (0.8: two items), CR-12b | — | A-1, A-5, A-6 |

**Waits (C-24).** Riders' waits fall as the fleet's trips per logged-in hour fall (more idle workers near any request). Under U1-a this follows without signing entry (C-43 is `ambiguous`). In the first months pay per trip is higher for contractors (C-13; A-29) and for employees on low-fare trips (C-1), and trips are fewer (C-7). If the fleet's logged-in hours rise or hold, trips per logged-in hour fall. Logged-in hours fall only if workers' hourly yield falls, and with pay per trip no lower for anyone that requires fewer trips per logged-in hour. Either way trips per logged-in hour fall: the response (logged-in hours) cannot reverse the change that drives it (CR-12e; CR-12, 1.1: the response argument in every direction, with a worker's cost per hour about constant). Dispatch steering under U1-a (A-7) moves requests between employees and contractors within the same fleet, so under CR-12's 1.1 note it is part of the response the argument bounds, not a second chain; under U1-a idle logged-in time costs the companies nothing, so they have no reason to cut it. `decrease`. Under U1-b, companies cut employees' paid waiting (C-40; A-6), which lengthens waits, while the fleet argument above shortens them: `ambiguous`. From the medium run, the per-trip total is `ambiguous` (C-14) and the argument no longer gives a sign; C-24 is signed for the short run only.

**Taxis (C-25, C-26, C-45).** Riders who leave the apps take some taxi trips (RS-1; A-10, which includes the premise that taxis have idle capacity at the fixed fare, since the cap binds on medallions, not on trips). Taxi fares are set by the city and the number of medallions is fixed, so more demand at the old fare cannot raise the fare: the pressure goes to the price of the right to operate (CR-6, 0.7, the price of a legal right is enough). The lease price of a medallion is a free price, and its rise satisfies CR-6 by itself (C-45; CR-6, 0.8); medallion values rise from the time the Act became expected (CR-7c, CR-10c; A-11). Owners at that time capture the gain.

**Platforms' shareholders (C-27).** The expected yield of the Lanvik operations falls with the costs above (CR-7c, CR-10c), from introduction in January 2027 in part and fully at enactment.

**Restaurants (C-28, C-29, C-44).** Delivery fees rise, so restaurants' delivery orders fall (RS-12; A-12); diners who order less cook more at home (C-44; A-4 names home cooking as a substitute). Some restaurants deliver with couriers of their own (RS-1; A-13). For restaurants starting in-house delivery that is a new activity (OC-5), but larger chains already employ couriers, and for them more delivery work can be more hours as well as more staff: the labor hired moves as a group (CR-6, 1.1: labor demand), `at_least_one_increase`.

**The insurance fund (C-30, C-31).** Contributions come in (C-4). Employees whose hours are cut, and who reach 2,600 of insured wages, claim benefits (A-20). Both go through the same fund, so they are recorded as two items, with the net separately (CR-8, 1.0); no figure in the case settles the net: `ambiguous`.

**Non-wage terms (C-41); RS-22 does not apply.** RS-22's 1.1 clause excludes terms the employer changes as a response to the policy: those are PC-17's adjusting terms. Flexibility is cut by the companies in response to the floor (C-8, C-40), and the value of the insurance cover to workers is recovered, if at all, through the other terms (PC-17, gross and net), which C-8 already carries. So no compensating-differential consequence is recorded. What remains is CR-12's 0.8 note on two items of one variable: insurance cover (C-3, +) and flexibility (−). Under U1-b flexibility falls on its own premise (A-6: companies schedule employees' logged-in time), and the total is `ambiguous`. Under U1-a nothing signs a cut in flexibility apart from its place as one member of the group C-8, and a group member is not a chain (CR-12, 1.1); the total is `increase`.

**Employees' earnings (C-33).** PC-10's note: the wage per engaged hour rises for some (C-1), while fewer trips at higher fares (C-7, signed with A-4) mean fewer engaged hours to pay. The group C-8 is not used as the opposing chain, since one of its members (flexibility) does not bear on earnings and no member is signed alone (CR-12, 1.1). Earnings combine the two signed chains and are `ambiguous` (CR-12b; CR-12c forbids netting the variables themselves).

Stopping points. The spending of workers whose earnings change, and of riders who pay more (depth 3, diffuse); the suppliers of vehicles and bicycles to app workers; transit ridership (a partial substitute, depth 2, recorded under A-4 only).

## 7. Combined effects

**Contractors' pay per trip: two items in one variable.** The premium is "in addition to the agreed fare share", and the fare share is set by the company, which changes it several times a year with 30 days' notice. Under CR-6's 0.8 note, a term that is free to change is regulated only for as long as changing it costs more than it gains: its stickiness is a premise. The pressure from the premium therefore goes to the fare share and bonuses (CR-6; PC-17: the other terms adjust). Under CR-12's 0.8 note, the premium (C-2) and the fare share (C-12) are two items of `net_price_received`, recorded separately, with the total separately (C-13).

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-12 | `drivers.contractor` | `net_price_received` (fare share and bonuses per trip: item 2) | decrease | medium | CR-6 (0.8: free terms), PC-17 (1.1: a buy-out added to a free price), RS-2 | A-2, A-28 |
| C-13 | `drivers.contractor` | `net_price_received` (total per trip: premium plus fare share) | increase | short (October 2027 to about March 2028) | CR-12 (0.8: two items), CR-12a | A-2, A-29 |
| C-14 | `drivers.contractor` | `net_price_received` (total per trip) | ambiguous | medium | CR-12 (0.8), CR-12b | A-2, A-28 |
| C-34 | `drivers.contractor` | `wait_time` (unpaid time between trips) | U1-a: ambiguous; U1-b: ambiguous | short | CR-6, CR-7a, CR-12e (1.1: the response argument in every direction), CR-12b | A-2, A-4, A-6, A-7, A-29 |
| C-35 | `drivers.contractor` | `wage_rate` (earnings per hour logged in) | U1-a: ambiguous; U1-b: ambiguous | short to medium | CR-12e (response argument), CR-12 (1.0; 1.1: the response argument in every direction), CR-12b | A-2, A-4, A-24 |

- *C-13.* In the first months, before fare shares are changed (A-29: platforms announce cuts with 30 days' notice and avoid them at launch, under the Department's scrutiny), the premium is added to unchanged fare shares: the total rises (CR-12a).
- *C-14.* Once fare shares can move, the company can cut them by up to the premium (A-28). Contractors' alternative is now employee status, which the company must offer as the default; a cut large enough to make that better for many workers raises the company's costs. No premise says whether the cut is smaller than the premium, equal to it or larger: `ambiguous` (CR-12b). The premium may thus be undone, in part or in full, without breaching §9, unless §9 is read as freezing the fare share (A-28 assumes it is not).
- *C-34 and C-35: the response argument (CR-12, 1.0).* A higher pay per trip draws more contractor hours (entry). CR-12e's response argument: entry is a response to the higher pay per trip and cannot push contractors' earnings per logged-in hour below their old level, since entry stops once hourly yields equal what workers can earn elsewhere. CR-12's 1.0 note says what the argument needs. (1) A premise that cost per unit does not fall as the activity expands: a worker's own cost per hour (vehicle, fuel) is about constant, so yes. (2) The total it bounds: contractors' earnings per logged-in hour, all platforms together, since workers move between them. (3) To give `increase` rather than "increase or no change", the response must be partial: onboarding takes four to six weeks (A-24). (4) The argument covers one response. A second response to the same change, riders taking fewer trips at higher fares (C-7), is not bounded by it: fewer trips per contractor push hourly earnings down. And from the medium run the per-trip total itself is ambiguous (C-14), so the entry chain is kind 3. CR-12's 1.1 note settles that riders' response, through the fare market, is a second chain, not part of the response the argument bounds. Under U1-b a third chain pushes up: companies cut employees' logged-in time, sending more requests to contractors; under both readings dispatch steering of low-fare requests to contractors (A-7) also adds trips. Combined: `ambiguous` under both readings (C-35); a premise that the premium dominates (A-25, p = 0.35) is below the cut-off. Entry itself is not signed (C-43) and is used here only as a response the argument bounds. On waiting (C-34), the fleet argument of C-24 gives fewer trips per logged-in hour for the fleet as a whole in the short run. For contractors alone, though, requests steered to them from employees (A-7, under both readings) and, under U1-b, requests no longer served by employees' cut waiting time come from outside the contractor total: they are second chains, pushing contractors' waits down. Combined: `ambiguous` under both readings.

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `drivers.contractor`, `net_price_received` (total), short | Premium (C-2) | — (fare shares sticky, A-29) | None needed | **increase** (C-13) |
| same, medium | Premium | Fare share cut (C-12, A-28) | None | **ambiguous** (C-14) |
| `drivers.contractor`, `wage_rate` per logged-in hour | Per-trip total (short); U1-b: requests moved from employees | Entry (bounded by the response argument); fewer trips (C-7, a second response) | None (A-25, p = 0.35) | **ambiguous** under both readings (C-35) |
| `drivers.contractor`, `wait_time`, short | Fewer trips per logged-in hour (fleet argument) | Requests steered from employees (A-7); U1-b: requests moved from employees' cut waiting | None | **ambiguous** under both readings (C-34) |
| `riders`, `wait_time`, short | U1-b: employees' paid waiting cut (C-40) | Fewer trips per logged-in hour for the fleet (response argument, CR-12e, 1.1) | U1-a: none needed | U1-a **decrease**; U1-b **ambiguous** (C-24) |
| `drivers.employee`, `non_wage_compensation` (total) | Insurance cover (C-3) | U1-b: flexibility cut by scheduling (A-6) | None | U1-a **increase**; U1-b **ambiguous** (C-41) |
| `drivers.employee`, `earnings` | Floor (C-1) | Fewer trips, so fewer engaged hours (C-7, A-4) | None | **ambiguous** (C-33) |
| `state_insurance_fund`, `fund_balance` | Contributions (C-4) | Benefits paid (C-30) | None | **ambiguous** (C-31) |
| `neighboring_jurisdictions`, worker-hours on Selvane trips | U1-b: workers without shifts | Premium on Lanvik trips | None; C-14 is itself ambiguous | **ambiguous** (C-23) |
| `riders`, fares and trips | Costs per trip (C-11) | — | Split by A-4 (CR-6, 0.9) | fares **increase** (C-6); trips **decrease** (C-7) |

**Final check** (`03_workflow.md`).
1. Uncombined chains: contractors' pay per trip combines the premium and the fare share (C-13, C-14); their hourly earnings and waits combine entry, fewer trips, dispatch steering and (U1-b) diverted requests (C-34, C-35); riders' waits combine the fleet's response with (U1-b) employees' cut waiting (C-24); employees' non-wage terms combine cover and flexibility (C-41); employees' earnings combine the floor with fewer trips (C-33).
2. Group signs: employees' margins (C-8) and restaurants' couriers (C-29, employment or hours under CR-6 1.1) are groups. No member of a group is used as a signed chain elsewhere (CR-12, 1.1): earnings (C-33) use the signed fall in trips (C-7), not C-8; the U1-b flexibility item in C-41 and the cut in paid waiting (C-40) rest on A-6; entry (C-43) is recorded as `ambiguous` and is not used as a signed chain.
3. Baseline: every sign is against Lanvik without the Act, in which no app worker is an employee and fare shares are set by the companies. RS-23's "cheaper pool" and RS-17's "below relative to above" are re-signed (C-11, C-18 to C-21; RS-23 and RS-17, 1.1). The premium is not compared with the mandate without a buy-out: CR-3b says the contractor option cannot leave a worker worse off than the mandate alone, but that is another policy, and against no Act contractors' pay per trip is signed in C-13 and C-14. PC-11's criteria (C-9) are signed only for the change against the counterfactual's dispatch ranking (A-31).
4. Worse off is not poorer: `resources_available_other_uses` is signed only for riders whose trips do not fall, who keep paying the higher fare (C-38; A-30).
5. Timing shifts: none signed; the announcement window carries asset values (C-26, C-27) and restructuring (C-15), which happen only because of the Act.
6. Both sides of every transfer: contributions (C-4) and benefits (C-30, C-31); the premium (C-2 to the worker, C-11 from the company); the floor (C-1 and C-11); enforcement (C-36, C-37); medallion leases (C-45: the lessees pay more, out of the extra yield that more riders at the fixed fare give them, so their net is not signed; CR-7b).
7. Every actor class, every core rule: CR-7c for medallions and platforms' shares; CR-6 for fares, the employee floor, the taxi fare and its lease price (C-45), and contractors' waits; CR-4 for entry (C-43) and home cooking (C-44); enforcement and its payers recorded. The insurance fund is not fed from the general budget in the record, so its items are netted on their own (CR-8, 1.1: a dedicated fund).
8. Unstated premises: the stickiness of fare shares (A-29) and whether they can be cut (A-28) are stated; so are dispatch steering (A-7), the company's election (A-2), the change in rationing (A-31), riders whose trips do not fall (A-30) and taxis' idle capacity (A-10).
9. Baseline of every pattern: PC-17, PC-10, PC-11, RS-1, RS-3, RS-5, RS-12, RS-14, RS-16, SB-4 conclude against no Act; PC-11 is signed on the change in rationing (1.1). RS-23 and RS-17 were re-signed (1.1). RS-22 is not used (its 1.1 clause excludes employers' responses); RS-20, RS-24, PC-20, EN-13 and EN-14 are not used.

## 8. Time structure

- **10 January to 15 March 2027: the bill.** Platform shares and medallion values begin to move as passage becomes likely, and fully at enactment (C-26, C-27; CR-7c, probability). Lobbying on U1 and the premium begins (C-22).
- **15 March to 30 September 2027.** Companies decide whether to elect K5 (A-2), build payroll and engaged-time records (C-5), and start reshaping some services to meet the three conditions (C-15). Contractor agreements are offered from 1 September; workers choose (C-10, C-42).
- **October 2027 to about March 2028: launch.** Employees are paid the floor (C-1) and covered (C-3); contractors receive the premium on unchanged fare shares (C-13). Fares rise and trips fall (C-6, C-7); riders wait less for a pickup under U1-a (C-24). Under U1-b, companies schedule employees and cut paid waiting (C-8, C-9, C-40, A-6). Medallion lease prices rise (C-45).
- **From about spring 2028.** Fare shares are reset (C-12), so contractors' total pay per trip becomes ambiguous (C-14). Contractors' entry is complete (A-24 no longer holds), and their hourly earnings move toward what they can earn elsewhere (CR-7a). Employees whose hours were cut and who qualify claim benefits (C-30). At the first anniversary (September 2028) workers can revoke their agreements, so the split between employees and contractors responds to the new fare shares.
- **Long run.** Restaurants' own delivery staff (C-29) and small exempt services (C-21) grow as investment allows (TS-1).

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-36 | `officials.enforcement` (Department of Labor) | `enforcement_cost` | increase | 4 million a year of audits and cases. | OC-3, CR-8c |
| C-37 | `taxpayers`, recipients of other spending, future taxpayers | `resources_available_other_uses` | at_least_one_decrease | The 4 million comes from the general fund, with no tax named. | OC-1 (who pays), OC-3, CR-8 (0.7) |
| C-38 | `riders` (whose trips do not fall) | `resources_available_other_uses` | decrease | What the higher fares would have bought, for riders who keep taking as many trips (A-30). | CR-3 (note), OC-1 |

The trips not taken (C-7) are prevented exchanges: both the riders and the workers who would have made them lose the gain they expected (OC-4). The resources used in reshaping services (C-15) and in evasion (C-17) are used up (CR-8c).

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | The Act is enforced: audits and private suits with double damages make treating workers as contractors without a valid agreement costly. | enforcement | 0.8 | 4 million budget; damages; the litigation record. | C-1 to C-4, C-8 to C-11 shrink; C-17 grows. |
| A-2 | Each company elects to offer contractor agreements. | other | 0.75 | Companies' statements during passage; the premium was the level they proposed; under U1-b the election saves most of the floor. | No contractors: C-2, C-12 to C-14, C-34, C-35 vanish; every worker is an employee and C-8 grows. |
| A-3 | Some hours on a trip pay below 16 per hour on a trip (about a fifth). | binding | 0.9 | Platform data in the record. | Under U1-a the floor does not bind: C-1, C-8, C-9 under U1-a are not reported. |
| A-4 | Platforms pass part of their added cost per trip into fares and fees, and some riders and diners take fewer trips at the higher price (taxis, transit and home cooking are partial substitutes). | substitutability | 0.8 | Effects of past fare and fee changes. | C-6, C-7, C-24 (U1-a), C-25, C-28, C-38 are not reported. |
| A-5 | Workers paid below 16 per hour on a trip mostly choose employee status (the top-up exceeds the premium and the flexibility they give up). | other | 0.65 | 16 against about 11 per hour on a trip for bicycle couriers, plus the premium of about 3. | C-3, C-4, C-10 rest on A-23 (U1-b) only; fares rest on the premium while fare shares hold. |
| A-6 | Under U1-b, companies schedule employees' logged-in time to cut paid waiting. | other | 0.85 | Practice of employers paying by the hour; 75% of logged-in hours below 16. | C-24 under U1-b becomes `decrease`; C-40 is not reported; C-41 under U1-b becomes `increase`. |
| A-7 | Companies can steer requests between employees and contractors through dispatch. | other | 0.6 | The Act is silent on dispatch; current dispatch uses ratings. | C-9 rests on shift allocation only; C-34 under U1-a becomes `increase`. |
| A-8 | Some services can be reshaped to meet the three conditions at a cost below the Act's burden. | other | 0.5 | Marketplace models elsewhere; legal opinions. | C-15 is not reported. |
| A-9 | Some workers can work through one-person companies, which §3 does not cover. | other | 0.55 | Incorporation cost; companies' contracting practice. | C-16 is not reported. |
| A-10 | Taxis are a substitute for some app rides, at fares fixed by the city, with the medallion cap binding; taxis have idle capacity at the fixed fare, so more riders mean more trips per medallion. | substitutability | 0.75 | Medallion prices; airport and downtown trips; taxis' share of time empty. | C-25, C-26, C-45 are not reported. |
| A-11 | Buyers of shares and medallions expect the Act to survive the court challenge and repeal campaign. | expectations | 0.7 | Legislative margins; legal commentary. | C-26 and C-27 shrink. |
| A-12 | Restaurants' delivery orders fall as delivery fees rise. | other | 0.8 | Order data after past fee changes. | C-28 and C-44 are not reported. |
| A-13 | Some restaurants hire their own couriers rather than pay the higher fees. | substitutability | 0.55 | Larger chains already do. | C-29 is not reported. |
| A-14 | Some workers can move hours between trips starting in Selvane and in Lanvik. | mobility | 0.65 | 8% of metro trips start in Selvane; workers' home locations. | C-23 is not reported. |
| A-15 | Some delivery services can operate with fewer than 100 Lanvik workers. | other | 0.5 | Cooperatives now; costs of scale. | C-21 is not reported. |
| A-16 | Companies, drivers' groups and unions can organize at a cost below their stakes. | other | 0.9 | Existing associations; the hearings. | C-22 is not reported. |
| A-17 | Some workers exceed 40 hours a week with one company (about 600 on trips; about 5,000 logged in), and companies can cap them. | other | 0.85 | Platform data. | C-18, C-19 are not reported. |
| A-18 | Companies control dispatch enough to keep part-time employees' weekly wages at or under 150. | other | 0.7 | About 24,000 workers a week earn under 150 from one company; dispatch control. | C-20 is not reported. |
| A-19 | Enforcement is imperfect: some misclassification and some pressure to sign occur. | enforcement | 0.65 | Audit rates; experience with similar laws. | C-17 is not reported. |
| A-20 | Some employees whose hours are cut qualify for and claim benefits. | other | 0.6 | Insured wages at 16 an hour reach 2,600 in about 160 hours. | C-30 is not reported; C-31 becomes `increase`. |
| A-23 | Under U1-b, workers who wait much of their logged-in time choose employee status. | other | 0.7 | 16 against about 13 plus 1.74 per logged-in hour. | Under U1-b fewer employees; C-8 and C-9 shrink. |
| A-24 | Onboarding of new contractors takes four to six weeks, so entry is partial in the first months. | durability | 0.6 | Background checks and vehicle inspections. | The response argument gives "increase or no change" for the entry chain; C-35 is unchanged (`ambiguous`). |
| A-25 | The premium dominates the effects of entry and fewer trips on contractors' hourly earnings. | other | 0.35 | No direct evidence. | Below the cut-off: C-35 stays `ambiguous`. |
| A-26 | The Department's 4 million is new money from the general fund. | revenue_use | 0.9 | §11. | C-37 becomes a fixed-budget case (OC-3, 0.9). |
| A-28 | §9 does not fix the fare share, and companies can cut fare shares and bonuses after launch. | other | 0.75 | §9's "agreed fare share" refers to the share in force at each trip; companies change shares routinely. | C-12 is not reported; C-14 becomes `increase`. |
| A-29 | Fare shares are not cut in the first months (30 days' notice; scrutiny at launch). | other | 0.6 | Companies' notice practice. | C-13 becomes `ambiguous`; C-11 for contractors rests on A-28 failing; C-24 under U1-a becomes `ambiguous`. |
| A-30 | Some riders do not cut their trips at the higher fares (airport, late-night and mobility-limited riders with no close substitute). | substitutability | 0.75 | Trip data by purpose after past fare changes. | C-38 is not reported. |
| A-31 | The floor's surplus of employee hours is rationed by stricter criteria than the counterfactual's dispatch ranking (shift allocation, acceptance thresholds). | other | 0.7 | Shifts do not exist without the Act; employers' practice where pay is by the hour. | C-9 is not reported. |

## 11. Report

**The policy.** From October 2027, app-based drivers and couriers in Lanvik are employees of the platform unless it proves three conditions. Employees must be paid at least 16 an hour of "engaged time", overtime above 40 hours a week, and the platform pays 11% insurance contributions in weeks when an employee earns over 150. A platform may instead offer a contractor agreement; workers who sign it stay contractors for a year and receive 1.50 a trip on top of their fare share. It is unclear whether time logged in and waiting counts as engaged time.

**Visible consequences.** Low-paid hours are paid at least 16 (C-1); contractors receive 1.50 a trip (C-2); employees gain insurance cover (C-3) and the fund collects contributions (C-4).

**Invisible consequences.**
- *Riders and restaurants.* Fares and fees rise and fewer trips are taken (C-6, C-7); riders who keep riding have less for other things (C-38). Restaurants sell fewer delivery orders (C-28); some hire their own couriers (C-29). Taxis carry more riders and medallions gain value (C-25, C-26).
- *Employees.* Their hours, jobs, flexibility or pay above the floor fall (C-8), and shifts and requests are allotted by rating (C-9). Workers paid below the floor choose employee status (C-10). Hours bunch below 40 a week with each company and below 150 a week in pay, and workers spread hours across companies (C-18 to C-20). Whether employees' earnings rise is open (C-33).
- *Contractors.* Their pay per trip rises at first (C-13); once fare shares are reset it may not (C-12, C-14). Under U1-a they wait longer between trips (C-34). Whether they earn more per hour logged in is open (C-35).
- *Companies.* Their labor cost rises for both kinds of worker (C-11); they spend on compliance (C-5); some reshape services or use one-person companies to fall outside the Act (C-15, C-16); some breach it (C-17). Small services stay under 100 workers (C-21). Their shares lost value when the Act became expected (C-27). Lobbying rises (C-22).
- *The state.* The Department of Labor spends more, paid by the general fund (C-36, C-37); the insurance fund pays benefits to app workers as well as collecting from them (C-30, C-31).

**Per reading of U1.** If waiting is not engaged time (U1-a), the floor binds on about a fifth of trip hours, overtime touches about 600 workers, and riders wait less (C-24). If it is (U1-b), the floor binds on most logged-in hours, companies schedule employees, workers who wait a lot become employees, overtime touches about 5,000 workers, and riders' waits may rise or fall (C-24).

**Ambiguous effects.** Contractors' pay per trip after the reset and their hourly earnings (C-14, C-35); employees' earnings (C-33); the RS-22 trade-off between flexibility and cover (C-32); the insurance fund's net (C-31); work in Selvane (C-23); and under U1-b, riders' and contractors' waits (C-24, C-34).

**Key conditions.** That the Act is enforced (A-1, p = 0.8); that companies elect the buy-out (A-2, p = 0.75); that fare shares can be reset after launch (A-28, p = 0.75), which decides whether the premium lasts.

**What this analysis cannot say.** Whether workers as a whole gain; how many jobs are lost or gained; whether the premium survives the reset in full or in part; road safety and health (out of scope for version 1).

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | drivers.employee (hours paid below 16) | wage_rate (per hour of engaged time) | U1-a: increase; U1-b: increase | short | visible | B | PC-10, PC-17, CR-1 | A-1, A-3 |
| C-2 | drivers.contractor | net_price_received (premium per trip) | increase | short | visible | B | PC-17, CR-1 | A-1, A-2 |
| C-3 | drivers.employee | non_wage_compensation (insurance cover) | increase | short–medium | visible | B | PC-17, CR-1, CR-8b | A-1, A-5 |
| C-4 | state_insurance_fund | tax_revenue (contributions) | increase | short | visible | B | TX-1, CR-8b | A-1, A-5 |
| C-5 | platforms | compliance_cost (classification, payroll, records) | increase | short | invisible | A | CR-8c, OC-2 | none |
| C-6 | riders | price_paid (fares and fees) | increase | short–medium | visible | B | RS-14, PC-17, CR-6, CR-5c | A-4, A-5 |
| C-7 | riders, drivers.employee, drivers.contractor | quantity_traded (rides and deliveries) | decrease | short–medium | invisible | B | PC-17, CR-4c, CR-6, OC-4 | A-4, A-5 |
| C-8 | drivers.employee | hours_worked (−), employment (−), non_wage_compensation (flexibility, −), wage_rate (above the floor, −) | U1-a: at_least_one_decrease; U1-b: at_least_one_decrease | short–medium | invisible | B | PC-10, PC-17, CR-6 | A-1, A-3 |
| C-9 | drivers.employee | allocation_by_non_price_criteria (shifts and requests) | U1-a: increase; U1-b: increase | short–medium | invisible | B | PC-11, CR-6 | A-1, A-3, A-7 |
| C-10 | drivers.low_fare | term_prevalence (employee status) | increase | short | invisible | B | RS-23, CR-4 | A-1, A-5 |
| C-11 | platforms | price_paid (labor cost per engaged hour of employees; per trip of contractors) | U1-a: increase; U1-b: increase | short | invisible | B | RS-23, PC-17, CR-8b, CR-12 | A-1, A-5, A-29 |
| C-12 | drivers.contractor | net_price_received (fare share and bonuses per trip) | decrease | medium | invisible | B | CR-6, PC-17, RS-2 | A-2, A-28 |
| C-13 | drivers.contractor | net_price_received (total per trip) | increase | short | invisible | B | CR-12, CR-12a | A-2, A-29 |
| C-14 | drivers.contractor | net_price_received (total per trip) | ambiguous | medium | invisible | B | CR-12, CR-12b | A-2, A-28 |
| C-15 | platforms | reclassification (services reshaped to meet the three conditions) | increase | medium | invisible | B | RS-5, CR-4 | A-8 |
| C-16 | drivers.contractor, drivers.employee | reclassification (one-person companies) | increase | short–medium | invisible | B | RS-5, CR-4 | A-9 |
| C-17 | platforms, drivers.employee | legal_breach (misclassification, pressure to sign, unpaid engaged time) | increase | short–medium | invisible | B | RS-3, CR-4 | A-19 |
| C-18 | drivers.employee | hours_worked (worker-weeks just below 40 hours with one company) | U1-a: increase; U1-b: increase | short–medium | invisible | B | RS-17, CR-4 | A-17 |
| C-19 | drivers.employee | reclassification (hours split across companies) | U1-a: increase; U1-b: increase | short–medium | invisible | B | RS-17, RS-5 | A-17 |
| C-20 | drivers.employee (part-time) | hours_worked (worker-weeks at or just under 150 in pay from one company) | increase | short–medium | invisible | B | RS-17, CR-1, CR-4 | A-18 |
| C-21 | sellers.small_platform | number_of_sellers (services with fewer than 100 Lanvik workers) | increase | medium | invisible | B | RS-17, CR-4 | A-15 |
| C-22 | lobbying groups | lobbying_effort (U1, the premium, guidance on §3) | increase | short–medium | invisible | B | RS-7, CR-4, CR-12 | A-16 |
| C-23 | neighboring_jurisdictions (Selvane) | quantity_supplied (worker-hours on Selvane trips) | ambiguous | short–medium | invisible | B | RS-4, CR-7a, CR-12b | A-2, A-14 |
| C-24 | riders | wait_time (pickup and delivery) | U1-a: decrease; U1-b: ambiguous | short | invisible | B | CR-6, CR-9, CR-12b | A-2, A-4, A-6, A-24 |
| C-25 | sellers.substitutes (taxis) | quantity_substitute (taxi trips) | increase | short–medium | invisible | B | RS-1, RS-16 | A-4, A-10 |
| C-26 | owners.medallions | asset_value (taxi medallions) | increase | short | invisible | B | CR-6, CR-7c, CR-10c, SB-4 | A-10, A-11 |
| C-27 | owners.platforms | asset_value (shares) | decrease | short | invisible | B | CR-7c, CR-10c | A-11 |
| C-28 | sellers.complements (restaurants) | quantity_traded (delivery orders) | decrease | short–medium | invisible | B | RS-12, CR-9 | A-4, A-12 |
| C-29 | workers.inhouse_couriers | employment (restaurant couriers) | increase | medium | invisible | B | RS-1, CR-9, LW-10 | A-13 |
| C-30 | state_insurance_fund | subsidy_outlay (benefits to app workers) | increase | medium | invisible | B | CR-8b | A-5, A-20 |
| C-31 | state_insurance_fund | fund_balance (app contributions less app benefits) | ambiguous | medium | invisible | B | CR-8, CR-12b | A-5, A-20 |
| C-32 | drivers.employee (positions) | wage_rate (above the floor) (+), employment (−) | ambiguous | medium | invisible | B | RS-22, CR-5c, CR-7a, CR-12b | A-6, A-21, A-22 |
| C-33 | drivers.employee | earnings | ambiguous | medium | invisible | B | PC-10, CR-12b, CR-12c | A-1, A-3 |
| C-34 | drivers.contractor | wait_time (unpaid time between trips) | U1-a: increase; U1-b: ambiguous | short | invisible | B | CR-6, CR-7a, CR-12, CR-12b | A-2, A-4, A-6, A-29 |
| C-35 | drivers.contractor | wage_rate (earnings per hour logged in) | U1-a: ambiguous; U1-b: ambiguous | short–medium | invisible | B | CR-12e, CR-12, CR-12b | A-2, A-4, A-24 |
| C-36 | officials.enforcement (Department of Labor) | enforcement_cost | increase | short–long | invisible | A | OC-3, CR-8c | none |
| C-37 | taxpayers, recipients of other spending, future taxpayers | resources_available_other_uses | at_least_one_decrease | short–long | invisible | B | OC-1, OC-3, CR-8 | A-26 |
| C-38 | riders (who keep riding) | resources_available_other_uses | decrease | short–medium | invisible | B | CR-3, OC-1 | A-4 |
| C-39 | drivers.contractor | compliance_cost (trip records for the premium) | increase | short | invisible | B | OC-2, CR-8c | A-2 |

## Gaps found

**(a) Calculus gaps (a step no core rule covers).** None. Every step was derived from CR-1 to CR-12.

**(b) Unclear core rules.**
1. *CR-6 0.8, free terms, applied to a payment mandated "in addition to" a free term.* The 0.8 note on at-will contracts says a term is regulated only as long as changing it costs more than it gains. That turned out to be the central fact about the buy-out: a premium added to a fare share the company sets can be undone by cutting the fare share (C-12 to C-14). The note is written for existing contracts and stickiness; it does not say that a mandated add-on to an unregulated price binds only on the add-on's floor (a fare share cannot fall below zero) and for as long as the base is sticky. A sentence saying so would make the move easy to find.
2. *CR-12e's response argument with a second response that is not a response to the same cause.* The 1.0 note says a second response to the same change is a second chain. Here riders' response is to higher fares, which the companies set in response to their costs, which include the premium: it is a response to the same policy, but through a different market. The note was read as covering it (C-35). Saying "a response by another class, through another market, is always a second chain" would remove the doubt.
3. *CR-1 for an option the policy removes and adds back at a price.* K1 removes the option of contracting as a contractor; K5 adds it back, at the company's election and the worker's choice, with a mandated payment. CR-1 records each operation; the 0.7 note on splitting by response worked, but CR-1 does not say how to record an option that exists only if the other party first elects to offer it.

**(c) Missing or wrong patterns.**
1. *PC-17's 0.9 buy-out clause assumes the charge goes to a third party.* It says "PC-17 applies to those who provide the term, TX-2 to those who pay the charge". Here the charge (the premium) is paid to the worker, and the worker chooses. TX-2 does not fit: the premium is not a wedge between a buyer's and a seller's price but a second mandated term, and it is added to a price the company still sets. Applied as written, the clause would have treated the premium as a tax and missed that it can be undone through the fare share. The clause should distinguish a charge paid to the state or a fund (TX-2) from one paid to the counterparty (PC-17 again, with CR-6 0.8 on the terms it is added to), and say whose option the buy-out is.
2. *RS-23's second conclusion is not against the counterfactual.* "Under the alternative, the remaining pool is cheaper to serve" compares the contractor pool with the average pool. Against no Act, the company's cost per contractor trip rises by the premium (while fare shares hold). The selection itself is a statement about who is in which pool, not a change against the counterfactual. Re-signed under CR-12 1.0 (C-11). The 1.0 promotion did not re-base this clause.
3. *RS-17's first clause.* As in other cases, "below relative to above" is re-signed against the counterfactual (C-18 to C-21). Its 1.0 clauses on notches, kinks, lines on hours and eligibility all fitted, including the mirror where the worker gains eligibility by crossing while the company bears the cost (C-20).
4. *RS-22 where two terms move in opposite directions.* Its precondition held, and its conclusion, applied to each term, gave opposite group signs (flexibility lost, cover added), so the combined sign is `ambiguous` (C-32). RS-22 does not say that the workers who would bear the worse term can choose the other contract (selection, RS-23), which acts on the same jobs. A note linking the two would help.
5. *PC-10 "on engaged time".* PC-10 is stated for a floor per hour of work. Where the floor applies to a defined part of the time (engaged time), the employer's open margins include the definition itself: what counts as engaged time (U1), dispatch, and scheduling. PC-10 worked through CR-6, but the unit of the floor (CR-4's units clause) matters more than PC-10 suggests.
6. No pattern gave a sign that I had to override apart from the re-signing in (c) 2 and (c) 3.

**(d) Vocabulary.**
1. No variable for utilization (the share of logged-in time spent on trips), which decides who chooses which status; it was described in the text.
2. `wait_time` serves both for workers' unpaid time between trips (C-34) and riders' pickup waits (C-24); they are opposite sides of the same idle capacity.
3. `term_prevalence` was used for the share choosing employee status (C-10); "status" is not quite a term of a contract.
4. No instrument type for a mandate whose buy-out is paid to the counterparty and chosen by them; `mandate_with_charge` was used with a note.

**(e) Test of 1.0.**
- *PC-17 (mandate) and its 0.9 buy-out clause.* The main clause worked as written for employees (C-8, group). The 0.9 clause failed as written: the buy-out is at the worker's option and paid to the worker, so TX-2 does not apply, and the premium is undone through a free term ((c) 1). The 1.0 clause on a charge refunded on the act is not relevant here (no refund).
- *PC-10.* Worked through CR-6 under both readings (C-1, C-8, C-33), with interpretation on the unit of the floor ((c) 5).
- *RS-23 (selection under a uniform term).* Needed interpretation and re-signing: selection held (C-10, and under U1-b low-utilization workers), but its second conclusion compares pools, not worlds ((c) 2). This case is a test of whether the 1.0 promotion carried a baseline problem with it: it did.
- *RS-22.* Worked as written per term; combined, `ambiguous` ((c) 4).
- *RS-17 1.0 (hours lines, notches, kinks, eligibility).* Worked as written on three lines (40 hours: kink; 150 a week: notch with an eligibility mirror; 100 workers: notch), after re-signing the first clause ((c) 3).
- *RS-5.* Worked as written (C-15, C-16, C-19).
- *CR-6 0.9, splitting a shift.* (The brief names it "CR-6 1.0"; the clause is 0.9.) Worked as written: fares and trips each signed only with A-4 on riders' response (C-6, C-7). CR-6's 1.0 clause on small effects was not needed.
- *CR-6 0.8, free terms.* Worked, and decided the buy-out (C-12 to C-14), but only when applied beyond the existing-contract case it is written for ((b) 1).
- *CR-12 0.8, two items in one variable.* Worked as written: premium (+) and fare share (−) recorded as items, total separately, per horizon (C-2, C-12 to C-14).
- *CR-12 1.0, what the response argument needs.* Worked as written for contractors' hourly earnings: constant cost per worker-hour, the total named (all platforms), partial entry (A-24), and the second response (fewer trips) kept as its own chain, giving `ambiguous` (C-35). Needed interpretation only on whether a response through another market counts as a second response ((b) 2).
- *CR-12 1.0, the baseline of patterns.* Worked: it caught RS-23 and RS-17 (C-11, C-18 to C-21). Without the final check's item 9, RS-23's "cheaper pool" would have been recorded as a decrease in cost against no Act, which is wrong.
- *CR-12 1.0, tiers and dominance.* Not exercised: no dominance premise was used.
- *Candidates from 06_gaps.md, 6.2e.* None needed. New candidate: "a mandated add-on to an unregulated price is undone through that price once it can move" (derived here from CR-6 0.8 and CR-12 0.8); its first use.
