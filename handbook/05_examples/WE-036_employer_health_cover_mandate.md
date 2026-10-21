# WE-036 Employer health cover mandate ("play or pay")

Analyst: draft (Handbook 0.8 held-out test, corrected under 0.9)  |  Rule catalog version: 0.9  |  Status: awaiting expert review

A stylized policy in a fictional state. It resembles real employer health cover mandates but is not modeled on any one of them. It is a held-out test of catalog 0.8: the 0.7 and 0.8 changes were tuned on WE-026 to WE-035, and this case was not among them. It probes a mandated contract term that the employer may escape by paying a charge per uncovered worker ("play or pay", so PC-17's If clause is only partly met), two thresholds at once (50 full-time equivalents per firm, 30 hours a week per worker: RS-17), a per-head cost that is fixed above the 30-hour line and a penalty capped per firm (RS-18, CR-4's 0.8 clause on fixed costs per firm), gross and net burdens (CR-7, 0.7), wage stickiness in at-will contracts (CR-6, 0.8), and payers and receivers in one general budget (OC-1 and OC-3, 0.8). Health outcomes, including the effect of insurance on anyone's health, are outside the scope of version 1. The probabilities are illustrative; the evidence column says what a real analysis would cite.

This version is corrected under catalog 0.9, after the blind core-only re-run (`05_examples_core/WE-036_employer_health_cover_mandate_core.md`). The changes are listed in "Corrections after the core-only comparison"; part (e) of "Gaps found" is the record of the 0.8 test and is kept as written.

## 1. Policy record

**Quenby Fair Share Health Cover Act.** The State of Quenby has about 5.1 million people and 2.2 million private-sector employees. Its largest city, Marisport, lies on the border with the State of Tarnley, which has no such law; about 35,000 people commute across the border each day. Quenby's minimum wage is $14.00 an hour, indexed to prices; about 11% of private employees earn at or near it, mostly in retail, food service, cleaning, security and care.

Firms with 50 or more full-time equivalents (FTE) employ about 1.45 million people, of whom about 1.15 million average 30 or more hours a week. A state insurance department survey found that, of those 1.15 million, about 79% (910,000) are already offered a plan that meets the Act's benefit standard with an employer share of at least 70%; about 9% (105,000) are offered a plan that falls short on benefits or on the employer's share; and about 12% (135,000) are offered nothing. The 135,000 work at about 2,100 firms: about 62,000 at 45 large firms (national retail and food chains, staffing, security) each with more than 100 such employees, and about 73,000 at about 2,050 mid-size firms, about 36 per firm on average. About 1,300 firms have 40 to 49 FTE, and about 1,100 have 50 to 60. About 380 firms (farms, food processing, ski and lake resorts, landscaping) have 30 to 49 year-round FTE and would reach 50 if the hours of their seasonal workers counted.

The average premium for an employee-only plan that meets the standard is $7,400 a year, so a 70% share is $5,180. For a full-time worker at the minimum wage (2,080 hours, $29,120), that is 17.8% of pay, or $2.49 per hour at 40 hours a week and $3.32 at 30. The penalty of $3,000 a year is $1.44 per hour at 40 hours and $1.92 at 30. For a capped firm with 1,500 uncovered full-timers, the $300,000 cap is $200 per head a year.

The bill was introduced on 9 November 2026 with the governor's support, signed on 4 January 2027, and takes effect on 1 January 2028. Status for 2028 is decided by the firm's average FTE over 2027. It has no expiry.

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Play or pay | `mandated_contract_term` (`contract`: the employment contract), with an alternative charge per head | Health cover for each employee averaging 30 or more hours a week (130 hours in a month) | Employers with 50 or more FTE (K3) | Either offer each such employee, from the first of the month after 60 days of employment, a plan meeting K2 with an employer contribution of at least 70% of the employee-only premium; or pay $250 a month ($3,000 a year) to the Department of Revenue for each such employee not so offered. An employee who is offered and declines counts as offered. | Public employers. Employees averaging under 30 hours. |
| K2 Benefit standard | `product_standard` | Plans that count under K1 | Insurers and self-insured employers | Hospital, physician, prescription and maternity care, deductible no higher than $2,500; list kept by the Department of Insurance. | — |
| K3 Size threshold | Exemption below 50 FTE | Employers | — | FTE = monthly average over the previous calendar year of (employees averaging 130 hours a month) plus (all other employees' hours ÷ 130). Firms under common control are counted together. Agency workers count for the agency. | U1 |
| K4 Cap | Part of K1 | The K1 charge | — | No firm pays more than $300,000 a year under K1 (reached at 100 uncovered employees). | — |
| K5 Enforcement | Enforcement | K1, K2 | Department of Revenue; Department of Insurance | Employers report each employee's offer status on quarterly withholding returns; the charge is assessed with them. Misreporting: twice the unpaid charge. The Department of Insurance certifies plans under K2. Charges are paid into the general fund. A new appropriation of $4.1 million a year from the general fund pays for 32 staff. | — |

Existing rules (in force in the counterfactual too):

| Rule | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| R1 Minimum wage | `price_floor` | Wages | Employers | $14.00 an hour, indexed yearly. | — |
| R2 Tax exclusion | Exemption from `income_tax` | Employer contributions to health premiums | — | Excluded from the employee's income for Quenby's 4.5% income tax; wages are taxed. | — |
| R3 Indigent Care Program (ICP) | `public_supply` (payment to hospitals) | Care for uninsured residents below 200% of the poverty line | Hospitals that claim | About $310 million a year from the general fund; about $9 million of that is administration. | — |
| R4 Overtime | `price_floor` on hours above 40 | Hours above 40 a week | Employers | 1.5 times the regular rate. | — |

Unclear provisions:
- U1, seasonal workers in the count. The Act defines a seasonal worker (employed no more than 120 days in a calendar year in work that recurs at the same season) but does not say whether seasonal workers count toward the 50. Reading U1-a: they count by their hours, like any other employee. Reading U1-b: they are left out of the count (as the state's unemployment insurance code leaves them out of its own small-employer test, which K3 does not cite). Under both readings, a seasonal worker who averages 30 or more hours at a bound firm is owed an offer after 60 days; that part of the text is clear.

Readings get no probability; where a sign depends on U1, each reading's sign is reported.

The counterfactual is Quenby without the Act, with the same minimum wage, tax exclusion, Indigent Care Program and overtime rule.

## 2. Classification

| Component | Rothbard type | Binding? | Rule families |
|---|---|---|---|
| K1, firms that offer ("players") | Triangular: a term written into the employment contract. By CR-1: for the employer, removes the option of employing a 30-hour worker without cover and without charge (operation 1) and attaches the contribution to the option of employing them (operation 3); for the worker, adds the option of enrolling at no more than 30% of the premium (operation 2). The counterfactual law leaves cover to the contract, with the tax exclusion (R2). | For the 135,000 offered nothing and the 105,000 offered less than K1 requires (A-1), at firms that choose to offer (A-2). | PC-17, CR-5c, CR-6, CR-7b, PC-10 (through R1), RS-14 |
| K1, firms that pay ("payers") | Binary: a charge per uncovered full-timer, paid to the state. A charge paid only when an option is taken (employing a full-timer without an offer) is operation 3 (CR-1, 0.7). Nothing is added for the worker. | For firms that choose to pay (A-4). | TX-1, TX-2 (on full-time labor), OC-1, CR-7b |
| K1 as a whole | Each bound firm chooses between the two branches (CR-4, x: offer, y: pay), so the class is split by response, not by operation (CR-1, 0.7), as PC-17's 0.9 clause on a mandate with a buy-out charge now prescribes. | Yes | CR-1, CR-4, PC-17 (0.9) |
| K2 | Triangular: a standard on the plans that count. Removes, for bound firms, the option of meeting K1 with a lean plan. A firm that pays the charge may keep its lean plan: K1 charges it either way. Insurers and self-insured employers submit plans for certification (operation 3). | For firms whose plans fall short and that choose to upgrade (A-5). | CR-1, CR-4, TS-3 (product standards) |
| K3 | Exemption: a boundary at 50 FTE, measured over the previous year. | Yes | RS-17, RS-5, CR-10a |
| 30-hour line (in K1) | Exemption: a boundary in each worker's monthly hours. | Yes | RS-17 (0.9: a line on hours), RS-18, CR-4 |
| K4 | The charge stops at $300,000 per firm. Below the cap the charge is operation 3 on the option of employing a full-timer without an offer; above it, for a payer above 100 uncovered full-timers, it no longer varies with the number of heads and is operation 4, a sum no choice of heads avoids (CR-1, 0.9: operation per range). It is a fixed cost per firm (CR-4, 0.8). | Yes, for the 45 large payers (A-12) | CR-1 (0.9), CR-4 (fixed cost per firm), RS-18 (0.9: caps per firm) |
| K5 | Binary: funded by a new appropriation from the general fund (A-29); charges paid into the same fund. Every employer of 50+ FTE reports offer status, including those already compliant (operation 3). | Yes | OC-3, OC-1, CR-8b, CR-8d |

Every contribution is paid by an employer to an insurer for a worker's cover (CR-8b): C-2 and C-43 record the employers' side, C-1 and C-5 the workers' side, C-24 the insurers' sales. Every charge is paid by an employer to the general fund: C-3 and C-14 on the payers' side, C-4 and C-39 on the receiving side.

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `employers.bound` | Firms with 50+ FTE whose full-timers are offered no plan, or a plan short of K1 | Must offer, or pay $3,000 per uncovered full-timer, capped at $300,000. Split by response into players and payers. |
| `employers.players` | Bound firms that choose to offer | Pay 70% of a premium for each full-timer who enrolls. |
| `employers.payers_midsize` | Bound firms that choose to pay and have fewer than 100 uncovered full-timers | Pay $3,000 for each one. |
| `employers.capped` | The 45 large payers above 100 uncovered full-timers | Pay $300,000 whatever the number. |
| `employers.compliant` | Firms of 50+ FTE already offering a K1 plan | Report offer status each quarter (K5); otherwise nothing changes. |
| `employers.small` | Firms under 50 FTE | Exempt; compete with bound firms. |
| `employers.near_50` | Firms with about 40 to 60 FTE | A hire may cross the threshold for the following year. |
| `employers.seasonal` | The 380 firms with 30 to 49 year-round FTE that reach 50 only with seasonal hours | Bound under U1-a only. |
| `employers.tradable` | Bound firms selling against Tarnley producers | Higher labor cost than their rivals. |
| `workers.uncovered` | Full-timers at bound firms (both branches) | Their wages, hours and jobs may adjust; at players they gain cover. Some move to unbound work. |
| `workers.at_players` | Full-timers at players | Gain the option of cover at no more than 30% of the premium. |
| `workers.lean_plans` | The 105,000 offered plans short of K1 | Better plan or larger employer share, where the firm upgrades. |
| `workers.min_wage` | Workers at bound firms at or near $14 | Their money wage cannot fall. |
| `workers.near_30` | Workers scheduled at 30 to 35 hours at bound firms below the cap | Their 30th hour now carries the whole per-head cost. |
| `workers.full_time` | Workers well above 30 hours at bound firms below the cap | An extra hour from them adds no cost; an extra head adds the full cost. |
| `workers.capped_firms` | Full-timers at the 45 capped firms | The charge does not vary with their number. |
| `insurers.group` | Insurers selling group plans (and self-insured employers) | More plans meeting K2; lean plans for bound firms no longer count; plans submitted for K2 certification. |
| `insurers.individual` (`sellers.substitutes`) | Insurers selling individual plans | Some buyers are now offered employer cover. |
| `providers.medical` (`sellers.complements`) | Hospitals and physicians | More patients with insurance. |
| `general_fund` | The state budget | Receives the charges; pays the appropriation; loses income tax on wages turned into premiums; pays less under R3. |
| `taxpayers`, recipients of other general-fund spending | Those whose taxes or spending move with the fund | One or more of them gains or loses as the fund's balance moves. |
| `officials.enforcement` | Departments of Revenue and Insurance | New reporting, assessment and certification work. |
| `buyers.local_services` | Buyers from bound firms in retail, food service, care | Bound sellers' labor costs rise. |
| `neighboring_jurisdictions` | Tarnley employers | Not bound. |
| `workers.unbound` | Workers at firms under 50 FTE, in part-time work under 30 hours, and in Tarnley | More workers seek their jobs; their employers gain customers. |
| `sellers.contract_services` | Staffing agencies and contractors, including capped staffing firms | More demand for contracted and agency labor. |

## 4. Direct effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | `workers.at_players` | `non_wage_compensation` (employer-paid health cover) | increase | short (from 2028) | CR-1, CR-5c, PC-17 | A-1, A-2 |
| C-2 | `employers.players` | `price_paid` (labor cost per full-time head: wage plus contribution) | increase | short | CR-1, CR-5c, CR-8b | A-1, A-2, A-3 |
| C-3 | `employers.payers_midsize` | `price_paid` (labor cost per full-time head: wage plus charge) | increase | short | CR-1, TX-2 | A-1, A-3, A-4 |
| C-4 | `general_fund` | `non_tax_receipts` (K1 charges) | increase | short | CR-8b, TX-1 | A-4 |
| C-5 | `workers.lean_plans` | `non_wage_compensation` (benefits and employer share of their plans) | increase | short | CR-1, CR-5c, PC-17 | A-5 |

C-1 and C-5 are what the Act's supporters point to. C-2 and C-3 are the employer's side of the same change. C-4 is the state's side of every charge paid.

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-7 | `workers.uncovered` (above the minimum wage) | `wage_rate` | decrease | medium | PC-17, TX-2, CR-4, CR-6, CR-7b, CR-12e | A-1, A-6, A-37 |
| C-8 | `workers.uncovered` | `employment`, `hours_worked` (scheduled), `non_wage_compensation` (benefits other than health cover) | at_least_one_decrease | short | PC-17, TX-2, CR-5c, CR-6 | A-1, A-3 |
| C-9 | `workers.uncovered` | `employment`, `hours_worked` (scheduled), `non_wage_compensation` (benefits other than health cover) | at_least_one_decrease | medium | PC-17, TX-2, CR-2, CR-4, CR-12d, CR-12e | Chain P (payers): A-4, A-8. Chain Q (players): A-2, A-7. |
| C-10 | `workers.min_wage` | `employment`, `hours_worked` (scheduled), `non_wage_compensation` (other benefits) | at_least_one_decrease | short to medium | PC-10, CR-6 | A-1, A-9 |
| C-11 | `workers.near_30` | `hours_worked` (jobs scheduled at 30 to 35 hours) | decrease | short to medium | RS-17 (0.9: a line on hours), CR-1, CR-4 | A-1, A-10 |
| C-50 | `workers.near_30` | `employment` (positions under 30 hours) | increase | short to medium | RS-17 (0.9: a line on hours), CR-4 | A-1, A-10 |
| C-12 | `workers.full_time` | `hours_worked` (per full-timer, up to 40 a week) | increase | medium | RS-18 (0.9), CR-4 | A-1, A-11 |
| C-51 | `workers.full_time` | `employment` (full-time heads) | decrease | medium | RS-18 (0.9), CR-4 | A-1, A-11 |
| C-52 | `employers.bound` (below the cap) | `employment` (total heads: full-time and under 30 hours) | ambiguous | short to medium | CR-12b (0.8: two items in one variable) | A-1, A-10, A-11 |
| C-13 | `workers.capped_firms` | `employment`, `hours_worked` (at the 45 capped firms) | at_least_one_increase | medium | RS-18 (0.9: caps per firm), CR-4 (0.8, fixed cost per firm), CR-9, OC-5, CR-12d | Chain S (sales won from mid-size payers): A-8, A-12, A-13, A-22. Chain G (agency business): A-4, A-12, A-34. |
| C-15 | `employers.near_50` | `employment` (hires that would take the 2027 average to 50 FTE or more) | decrease | short (2027) | RS-17, RS-8, CR-4, CR-10a | A-14, A-15 |
| C-16 | `employers.small` | `number_of_sellers` (firms with 40 to 49 FTE) | increase | medium | RS-17, CR-4, CR-7a | A-14 |
| C-17 | `employers.near_50` (owners of firms at 40 to 49 FTE) | `asset_value` | ambiguous | short (from introduction) | RS-17 (0.9: value of firms near the line), CR-7c, CR-10c, CR-12b | A-14, A-16, A-21, A-22 |
| C-18 | `employers.near_50` | `reclassification` (work contracted out to agencies, contractors and franchisees) | increase | medium | RS-17, RS-5 | A-14, A-17 |
| C-19 | `employers.seasonal` | `price_paid` (labor cost per full-time head) | U1-a: increase; U1-b: no_change | short | CR-1 | A-33 |
| C-20 | `employers.seasonal`, `employers.near_50` | `employment` (seasonal engagements of up to 120 days) | U1-a: decrease; U1-b: increase | short to medium | RS-17, RS-5, CR-4 | A-14; under U1-a also A-33 |
| C-21 | `employers.near_50` | `employment` (hires that take firms past 50 FTE in each year from 2028: a flow) | ambiguous | medium | RS-8 (main clause; 0.9: more timing chains), RS-17, CR-10a, CR-12b, CR-12 (0.9) | A-14, A-31 |
| C-53 | `employers.near_50` | `employment` (at firms near 50, at each date from 2028: a stock) | decrease | medium | RS-17, CR-10a, CR-12e, CR-12 (0.9) | A-14 |
| C-22 | `employers.bound` | `legal_breach` (offers reported but not made) | increase | short to medium | RS-3, CR-1, CR-4 | A-18 |
| C-23 | insurers, unions, `employers.payers_midsize`, `employers.capped`, `employers.near_50` | `lobbying_effort` | increase | medium | RS-7 | A-19 |
| C-55 | `workers.uncovered` (at payers, at the margin) | `employment` (at firms under 50 FTE) (+), `employment` (part-time, under 30 hours) (+), `employment` (in Tarnley) (+) | at_least_one_increase | medium to long | CR-4b, CR-7a | A-4, A-6, A-8 |
| C-56 | `employers.payers_midsize` | `reclassification` (direct hires replaced by agency workers from capped staffing firms) | increase | medium | RS-5, RS-18 (0.9: caps per firm), CR-4 | A-4, A-12, A-34 |
| C-57 | `workers.at_players` | `job_changes` (moves to unbound jobs) | decrease | short | CR-4, CR-6 (0.8: at-will stickiness) | A-2, A-3, A-35 |
| C-58 | `workers.at_players` | `job_changes` | ambiguous | medium | CR-4, CR-12b | A-2, A-6, A-35 |

**The choice (CR-4, x: offer, y: pay).** A bound firm compares, per full-timer, the contribution ($5,180 for each one who enrolls, plus administration), less whatever the worker gives up in wages for cover, against the $3,000 charge, which no worker values. For a firm with low-wage staff and high take-up, the charge is cheaper: at take-up above 58%, $3,000 is less than $5,180 times take-up even before any wage offset. For a firm whose staff would buy cover anyway, the tax exclusion (R2) makes a dollar of premium worth more to them than a dollar of wage, so offering can cost less, net of the wage offset, than paying. So some firms play and some pay (A-2, A-4). The class is split by response (CR-1, 0.7); PC-17 is applied to the players only, TX-2 to the payers. PC-17's If clause ("requires every contract of a kind to include a term") is not met by K1 as a whole, because the term can be bought off; it is met for the players, who chose the term over the charge.

**The bargain at players (C-7 to C-9, chain Q).** For the employer, the term costs c per full-timer (the contribution for those who enroll). For the worker, the option of cover at 30% is worth v, not negative, since it only adds an option (CR-3b); with the tax exclusion, v includes the income tax not paid on the part of pay taken as cover. By CR-5c both acceptance ranges fall, so, as wages are reset, the wage falls (C-7). Employment and hours fall after wages adjust only if v is less than c for the marginal pair. These pairs could have agreed on cover, with the same tax exclusion, and did not, which by the 0.7 clarification to CR-2 shows only that no pair found it worth agreeing on in the situation as it was. Whether that reflects their rankings, or an obstacle (adverse selection in small groups, the cost of arranging a plan), is a premise (A-7, p = 0.6).

**The charge at payers (C-7 to C-9, chain P).** The charge is a per-head tax on full-time employment (TX-2 applied to labor). It is worth nothing to the worker, so the worker's acceptance range does not move (CR-5c); only the employer's falls, by $3,000 a year. By CR-4 on the employer, at the old wage the firm wants fewer full-time heads; by CR-6, the wage falls (C-7). Unless workers have no alternatives at all, the wage falls by less than the charge, so employment or hours fall (C-9). That premise is A-8 (p = 0.85): exempt firms, part-time work under 30 hours and Tarnley are open to some. Those at the margin take them (C-55, CR-4b). Their moves are a response to the wage fall and cannot reverse it (CR-12e); since they cannot all move at the old wage (A-37), the response is partial and the wage falls (CR-12, 0.9).

**Recording.** The two chains reach C-9 with the same sign and different premises. By CR-12d the consequence holds if either chain's premises hold; both are listed. In the short run, while wages are fixed (A-3, at-will contracts with pay scales and yearly raises, whose stickiness CR-6's 0.8 clarification makes a premise, p = 0.75), the whole cost falls on employers, who adjust the open margins (C-8). About 6% of private employees are under collective agreements with fixed terms; for them, wages are regulated while the agreement lasts, with no premise needed.

**At the minimum wage (C-10).** The wage cannot fall (R1). PC-10 applies through the floor. The per-head cost is $2.49 an hour at 40 hours and $3.32 at 30 for a player; $1.44 and $1.92 for a payer.

**The 30-hour line (C-11, C-50).** The 30-hour line is a threshold on each worker's hours: below it a job carries no cost, at 130 hours in a month it carries the whole per-head cost. RS-17's 0.9 clause applies it to a line on hours, with "job" for "firm": jobs near the line are kept below it, and work is split across separately counted units (two part-time jobs in place of one full-time job). RS-17's capitalization clause has no counterpart: a job is not an asset. One CR-4 switch (x: schedule the job at 30 or more hours, y: under 30) moves both members: the job loses hours (C-11, decrease) and becomes a position under 30 hours (C-50, increase). Each is signed on its own; CR-6's margins clause, cited in the 0.8 draft for a mixed group, is not the rule that applies. The split does not help with K3, because part-time hours count toward FTE; it helps only with the per-head cost.

**Above the line (C-12, C-51, C-52).** Above 130 hours a month, the per-head cost does not rise with hours. RS-18's derivation applies with the cap reached at the line itself: an extra hour from an existing full-timer adds nothing, while an extra full-timer adds the whole cost (CR-4, x: another full-timer, y: more hours from existing ones). Up to 40 hours (R4), full-timers' hours rise (C-12) and full-time heads fall (C-51). The switch moves both, so each is signed where CR-4 gives it (RS-18, 0.9), not as a group. Full-time heads fall while positions under 30 hours rise (C-50), so total heads at firms below the cap are `ambiguous` (C-52, CR-12's 0.8 clause on two items in one variable).

**The firm-level cap (C-13, C-14).** For the 45 capped firms the charge is $300,000 whatever the number of uncovered full-timers. Above the cap it is operation 4 (CR-1, 0.9) and a fixed cost per firm (CR-4, 0.8): RS-18's 0.9 clause on caps per firm gives no shift of hours toward fewer heads. With the premises that these firms stay above 100 (A-12) and that $300,000 does not decide whether they operate in Quenby (A-13), the charge itself changes neither their hiring nor their hours at the margin. That is not the policy's whole effect on them. The cap gives them a cost advantage over mid-size payers, $200 a head against $3,000, so they win sales from them (C-32, A-22), and capped staffing firms win agency business from them (C-56, A-34). By CR-9 with LW-10 their demand for labor rises with their sales, so employment or hours at the capped firms rise (C-13, `at_least_one_increase`; the group form because the labor goes to an existing activity, OC-5). The two chains have the same sign and separate premises (CR-12d). They pay a sum they cannot avoid except by offering cover, which costs far more (C-14).

**The 50-FTE threshold (C-15 to C-21).** K3 counts the 2027 average for 2028 status. A firm at 49 that adds one FTE takes on the term or the charge for all its full-timers: about 36 times $3,000, about $108,000 a year, for a mid-size payer. By RS-17: hires that would take the 2027 average to 50 fall, from the signing in January 2027 (C-15, A-15); more firms stay at 40 to 49 (C-16); and some work is contracted out (C-18). The value of firms at 40 to 49 falls with their expected growth (A-16) but rises with the burden on their larger rivals (A-22, p = 0.65), so it is `ambiguous` (C-17; RS-17's 0.9 clause on the value of firms near the line; kind 2 at or above 0.5). Firms at 50 to 60 that lack qualifying cover are in C-27. Splitting by ownership is closed by the common-control rule, so RS-17's "separately counted units" is open only through contractors and franchising (A-17). Under U1-a, seasonal hours count: about 380 firms are bound, so far as they lack qualifying cover (C-19, A-33: the survey behind A-1 covers only firms already at 50+ FTE), and firms near 50 cut seasonal hours with the rest (C-20). Under U1-b, seasonal workers are not counted, so the 380 firms are not bound, and firms near 50 replace year-round hires with seasonal engagements of up to 120 days, which do not count (C-20).

**Timing of growth past 50 (C-15, C-21, C-53).** Growth that would have taken a firm past 50 in 2027 is held back in 2027 (C-15). C-15 and C-21 are signed on a flow, hires that take firms past 50 in a window (CR-12, 0.9). In later years two derived chains oppose each other on that flow: some of the growth held back in 2027 crosses later, since a firm that must eventually cross pays the cost one year later by delaying (+, RS-8's main clause: an action moved to a later window rises there; A-31); and the lasting cost of being above 50 deters some growth for good (−, A-14), an opposing chain from a second incentive the policy creates (RS-8, 0.9: more timing chains). Both premises are at or above 0.5, so the flow from 2028 onward is `ambiguous` (CR-12b). The stock is different: employment at these firms at any date from 2028 is below the counterfactual (C-53). Delayed growth only catches up with growth that would already have happened, a response to the hold-back that cannot reverse it (CR-12e), and deterred growth keeps it below (A-14).

**Misreporting (C-22).** Offer status is self-reported on withholding returns. A firm that reports an offer it did not make saves $3,000 a head; the expected penalty is the chance of an audit times twice the charge (CR-1: a risk, CR-4: x: report truly, y: misreport). The trade stays in the legal labor market, so it is `legal_breach`.

**Lobbying (C-23).** Insurers and unions have a stake in a higher charge or a lower cap; mid-size payers in a lower charge or a cap per head; the capped chains in keeping the cap; firms near 50 in a higher threshold or the U1-b reading (RS-7).

**Agency labor under the cap (C-56).** K3 counts agency workers for the agency, and the capped firms include staffing firms. An agency worker placed by a capped staffing firm adds nothing to anyone's charge, while a direct hire costs a mid-size payer $3,000. Where the agency's markup is below that (A-34, p = 0.55), mid-size payers replace direct hires with agency workers (CR-4, x: hire directly, y: hire through a capped agency; RS-5): an arbitrage on K4.

**Job changes (C-57, C-58).** A worker newly offered cover at a player loses it by moving to an unbound job. While wages are fixed (A-3), the bound job is now better than before relative to the unbound one, so those at the margin (A-35) move less (C-57, CR-4). Once wages adjust, the lower wage at players (C-7) pushes the other way, so job changes are `ambiguous` (C-58, CR-12b).

Not reported: employers shortening seasonal and temporary engagements below 60 days so that no offer is ever owed (A-30, p = 0.4: replacing a worker mid-season costs more than one or two months' charge for most such firms).

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-24 | `insurers.group` | `quantity_traded` (group plans meeting K2) | increase | short | CR-9, CR-5 | plans `input_to` the players' compensation | A-2, A-5 |
| C-25 | `insurers.group` | `specification_level` (plans offered by firms that upgrade to K2) | increase | short | CR-1, CR-4, TS-3 (product standards) | as C-24 | A-5 |
| C-26 | `insurers.individual` | `quantity_substitute` (individual plans held by workers newly offered employer cover) | decrease | short | RS-1, CR-9 | group and individual plans: `substitute`, close | A-2, A-20 |
| C-27 | `employers.bound` (owners, below the cap) | `asset_value` | decrease | short (part from introduction, the rest at signing) | CR-7c, CR-10c | — | A-3, A-21 |
| C-47 | `employers.capped` (owners) | `asset_value` | ambiguous | short (from introduction) | CR-7c, CR-10c, CR-9, CR-12b | their output and mid-size bound firms' output: `substitute`, partial | A-12, A-21, A-22 |
| C-28 | `employers.small` (owners of firms under 40 FTE) | `asset_value` | increase | short | CR-7c, CR-10c, CR-9 | their output and bound firms' output: `substitute`, partial | A-21, A-22 |
| C-48 | `employers.compliant` (owners) | `asset_value` | ambiguous | short (from introduction) | CR-7c, CR-10c, CR-9, CR-12b | as C-28 | A-21, A-22 |
| C-29 | `employers.bound` | `return_on_capital` | decrease | short | CR-7b | — | A-3 |
| C-30 | `workers.uncovered` | `tax_share_borne` (gross share of the cost of K1, workers compared with employers) | increase | medium to long | CR-7b, DM-1 | `contract` (employment) | A-6, A-23 |
| C-31 | `employers.payers_midsize`, `employers.players` (local services) | `quantity_supplied` | decrease | medium | RS-14, RS-6, CR-12d | labor `input_to` local services | payers: A-4, A-8, A-22; players: A-2, A-7, A-22 |
| C-32 | `employers.capped`, `employers.small`, `employers.compliant` | `quantity_supplied` (in local markets shared with mid-size bound firms) | increase | medium | CR-9, CR-7a | as C-28 | A-8, A-22 |
| C-33 | `employers.tradable` | `quantity_supplied` (output produced in Quenby) | decrease | long | RS-14, RS-6, RS-4 | Quenby and Tarnley producers: `across_border`, close near Marisport | A-8, A-26 |
| C-34 | `neighboring_jurisdictions` (Tarnley producers) | `quantity_supplied` (sold into Quenby) | increase | medium to long | RS-4 | as C-33 | A-8, A-26 |
| C-35 | `providers.medical` | `quantity_complement` (care billed to insurers) | increase | short to medium | RS-12, CR-9 | insurance and medical care: `complement` | A-2, A-27 |
| C-36 | `general_fund` | `subsidy_outlay` (ICP payments to hospitals) | decrease | short to medium | CR-9, CR-8b | `contract` (insurance replaces the ICP as payer for the newly covered) | A-2, A-28, A-32 |
| C-37 | `general_fund` | `tax_revenue` (income tax) | decrease | medium | TX-10, CR-8b | wages and excluded premiums: `substitute` in compensation | A-2, A-6, A-8 |
| C-59 | `workers.unbound` | `wage_rate` | ambiguous | medium | CR-9, LW-10, CR-7a, CR-12b | bound and unbound jobs: `substitute`, partial | A-6, A-8, A-22 |
| C-60 | `sellers.contract_services` | `quantity_traded` (contracted and agency labor) | increase | medium | CR-9, LW-10, CR-12d | contracted labor `substitute` for direct employment | A-14, A-17; or A-4, A-12, A-34 |
| C-61 | `employers.seasonal` (owners) | `asset_value` | U1-a: decrease; U1-b: no_change | short (from introduction) | CR-7c, CR-10c | — | A-21, A-33 |

**Insurers (C-24 to C-26).** Players buy plans (C-24). Lean plans no longer count for bound firms, so firms that upgrade rather than pay buy plans of a higher specification (C-25; the standard binds on the share of designs that would have been chosen below it, TS-3). A firm that pays keeps no reason to drop its lean plan, since K1 charges it either way; lean plans are still sold to payers, so no fall in `variety` is signed. Insurers and self-insured employers bear the cost of K2 certification (C-54). Workers newly offered employer cover, with its tax exclusion and 70% share, drop individual plans (C-26, RS-1); RS-1's 0.8 wording gives only that buyers turn away, which is what is signed.

**Owners (C-27 to C-29).** Until wages adjust, the cost falls on returns (C-29). Where a firm's value rests on its expected earnings, the fall is capitalized when the Act becomes expected: part of the way from the bill's introduction in November 2026, as passage became likely, and the rest at signing (C-27, CR-7c's probability clause). Small rivals under 40 FTE gain sales, and the gain is capitalized in their value (C-28). For three other classes the gain from rivals' costs (A-22) meets a burden of their own, so their value is `ambiguous` (CR-12b, kind 2): the capped firms pay a fixed $300,000 (C-47); compliant firms bear the quarterly offer reporting (C-48, C-42); firms at 40 to 49 lose the value of growing past 50 (C-17). Seasonal firms' value falls under U1-a, where they are bound, and is unchanged by K1 under U1-b (C-61; those at 40 to 49 year-round FTE are in C-17 under that reading). In the long run returns are equalized (CR-7a), so no lasting change in return is signed.

**Who bears the cost (C-30).** CR-7b with DM-1. Nearly every large employer is bound; a worker who wants to escape the cost must move to a firm under 50, work under 30 hours, or work in Tarnley. Employers can redeploy capital, contract out, or move across the border over time. With the premise that workers' alternatives are clearly worse (A-23), workers bear more of the cost than employers, through the wage (C-7). As CR-7's 0.7 clarification asks, the share is stated as **gross**: at players, the net burden on workers is smaller by whatever cover is worth to them (v), which the method does not compare with the wage given up. At payers the gross and net shares are the same for workers, because the charge buys them nothing; what it buys goes to the general fund (C-39).

**Sales of local services (C-31, C-32).** RS-14 has two branches. Where a seller's competitors face the same cost, the price rises; where they are exempt, the quantity effect dominates. Here the competitors of a mid-size bound firm in retail and food service are mostly small exempt firms or the capped chains, whose charge per head is $200 against $3,000, so the second branch applies: mid-size bound sellers lose sales (C-31) and their rivals gain them (C-32). For players, the loss needs their labor cost per head to rise after wages adjust, which rests on A-7 (C-45). Workers who leave bound work seek jobs at unbound firms, which lowers wages there, while those firms gain customers and hire more, which raises them (C-59, `ambiguous`). A rise in the price of local services would need most rivals to be bound at a material per-head cost (A-24, p = 0.4); it is below the cut-off and not reported.

**Tradable production (C-33, C-34).** Where competitors are in Tarnley, production moves across the border over time (RS-4, RS-6), on the premise that wages do not absorb the whole cost (A-8).

**Medical care and the ICP (C-35, C-36).** Insurance and billed care are complements (RS-12): newly covered workers use more care that is billed to insurers (C-35). Some of them, or their care, were paid for by the ICP; for them the insurer now pays instead, so ICP outlays fall (C-36, CR-9 along the insurance contract). That needs the ICP to pay per claim (A-32): if R3 were a fixed sum, fewer claims could raise the payment per claim instead. The hospitals' receipts for that care come from insurers instead of the state; their price is not signed. The effect of the care on anyone's health is out of scope.

**Income tax (C-37).** At players, part of what would have been taxed wages is paid as an excluded premium (R2), and at all bound firms employment and hours fall (C-9): the income tax base shrinks (TX-10). The other side of this transfer is the smaller tax bill of workers at players, which is part of v (A-7) and so part of why the wage they accept falls; it is not signed separately.

Stopping points: the buyers of local services' other spending (depth 3, diffuse; stopped). Hospitals' prices and capacity (depth 3; the supply of care is not in the record). Payroll and benefits administrators (depth 2, diffuse; stopped).

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `workers.uncovered`, employment and hours (group), medium | — | Chain P (payers: the charge is worth nothing to workers, A-8); chain Q (players: v less than c, A-7). | None needed | **at_least_one_decrease** (C-9). Same sign, independent premises: holds if either chain's premises hold (CR-12d). |
| `workers.at_players`, `non_wage_compensation` (total), short to medium | Health cover (C-1). | Other benefits may be cut, as a member of C-8 and C-9. | CR-12b | **ambiguous** (C-44). Items recorded separately (cover in C-1; other benefits in C-8, C-9), the total here, as CR-12's 0.8 clarification on two items in one variable asks. |
| `workers.full_time`, `hours_worked` (per full-timer), medium | RS-18: an extra hour adds no per-head cost (C-12). | A smaller scale of output at bound firms needs fewer hours in total; whether that falls on hours per head or on heads is not derived, and with a per-head cost CR-4 points to heads. | None | **increase** (C-12), the derived sign. The scale chain is a suspected effect on hours per head that the rules do not derive; Tier C note (CR-12, 0.8 kind 1). Full-time heads fall on both chains (C-51). |
| `employers.bound` (below the cap), `employment` (total heads), short to medium | Positions under 30 hours (C-50). | Full-time heads (C-51). | None | **ambiguous** (C-52). Two items in one variable (CR-12, 0.8). |
| `workers.uncovered`, `wage_rate`, medium | Workers leaving for alternatives (C-55) lower the labor offered to bound firms. | Wage falls with the term or charge (C-7). | CR-12e response argument: the moves are driven by the wage fall and cannot reverse it; partial response (CR-12, 0.9) from A-37. | **decrease** (C-7). |
| `employers.bound`, `price_paid` (labor cost per full-time head), medium | The contribution or charge (C-2, C-3). | Lower wages (C-7). | Players: arithmetic once v is less than c (A-7). Payers: the wage falls by less than the charge (A-8). | **increase** (C-45). Holds if either branch's premise holds (CR-12d, CR-12e). |
| `employers.near_50`, `employment` (hires past 50), 2027 | — | Held back so the 2027 average stays under 50 (C-15). | — | **decrease** (C-15). |
| `employers.near_50`, `employment` (hires past 50, a flow), 2028 onward | Growth held back in 2027 crosses later (RS-8 main clause, A-31). | Lasting cost above 50 deters growth (A-14; RS-8, 0.9: more timing chains). | None | **ambiguous** (C-21). |
| `employers.near_50`, `employment` (a stock), at each date from 2028 | Delayed growth catches up (A-31). | Deterred growth (A-14). | CR-12e: catching up is a response to the hold-back and cannot put employment above the counterfactual. | **decrease** (C-53). |
| `employers.near_50` (40 to 49 FTE), `asset_value`, short | Burden on larger rivals (A-22). | Lower value of growing past 50 (A-16). | None | **ambiguous** (C-17). RS-17, 0.9. |
| `employers.capped`, `asset_value`, short | Sales won from mid-size payers (A-22). | Fixed $300,000 a year capitalized (A-12). | None | **ambiguous** (C-47). |
| `employers.compliant`, `asset_value`, short | Burden on rivals (A-22). | Quarterly offer reporting (C-42). | None | **ambiguous** (C-48). |
| `workers.at_players`, `job_changes`, medium | Lower wage at players (C-7). | Cover lost by moving (A-35). | None | **ambiguous** (C-58). Short run, wages fixed: **decrease** (C-57). |
| `workers.unbound`, `wage_rate`, medium | Their employers gain customers (A-22). | More workers seek their jobs (A-8). | None | **ambiguous** (C-59). |
| `taxpayers`, recipients of other general-fund spending, `resources_available_other_uses`, short | Charges received (C-4, C-39); lower ICP outlays (C-36). | The $4.1 million appropriation (C-38); income tax lost on hours and jobs cut while wages are fixed (C-8). | CR-12e, arithmetic with a premise: the 45 capped firms alone owe at least 45 x $300,000 = $13.5 million (A-4, A-12), $9.4 million more than the appropriation, before mid-size charges and ICP savings; A-36 says collections are not cut below that by misreporting and the short-run income tax lost is smaller. | **at_least_one_increase** (C-40). Items recorded separately (C-38, C-39). |
| `taxpayers`, recipients of other general-fund spending, `resources_available_other_uses`, medium | Charges received (C-4, C-39); lower ICP outlays (C-36). | The $4.1 million appropriation (C-38); income tax lost as wages turn into excluded premiums and wages fall (C-37). | None: the tax lost depends on how many play (A-2) and how far wages fall. | **ambiguous** (C-49). Horizons kept apart (CR-12g). |
| `officials.enforcement`, `enforcement_cost`, short | New reporting, assessment and certification (K5, $4.1 million). | ICP claims administration falls with fewer uninsured patients (C-36). | Arithmetic (CR-12e): the ICP's whole administration is $9 million; even if the newly covered were one ICP case in ten, the saving is under $1 million, less than $4.1 million. | **increase** (C-41), against the right baseline (OC-3, 0.8). |
| `workers.capped_firms`, employment and hours, medium | Sales won from mid-size payers (C-32); agency business (C-56). | None: the charge is fixed above the cap and gives no shift (RS-18, 0.9). | None needed | **at_least_one_increase** (C-13). Holds if either chain's premises hold (CR-12d). |

## 8. Time structure

- **Introduction to signing (November 2026 to January 2027).** Values of bound firms fall part of the way as passage becomes likely; small rivals' rise (C-27, C-28); those of capped, compliant and near-threshold firms move either way (C-47, C-48, C-17); seasonal firms' per reading (C-61). Lobbying starts (C-23).
- **2027: the measurement year.** K3 counts the 2027 average, so firms near 50 hold back hiring through 2027 (C-15, C-20) and contract out work (C-18), a full year before any cover is owed (RS-17, CR-10a). Employers set 2027 and 2028 raises knowing the cost is coming, so wage restraint (C-7) can begin before 2028. Jobs near 30 hours are rescheduled for 2028 (C-11).
- **2028: the duty applies.** Each firm chooses to play or pay for the year (C-1 to C-4). The charge is assessed quarterly, so a firm can change branch at a plan renewal. Insurers' sales of group plans rise (C-24), and individual plans are dropped as workers enroll (C-26). Newly covered workers change jobs less while wages are fixed (C-57). In the first year the charges exceed the appropriation (C-40).
- **Wages adjust over years.** In the short run the cost falls on employers (C-2, C-3, C-29, C-43), who use the open margins (C-8); no ranking of shares is made for this horizon. As raises are set lower (C-7), the burden moves to workers (C-30), and some move to unbound work (C-55). Agency labor from capped staffing firms builds up as contracts are renewed (C-56, C-60). Production moves to Tarnley slowly (C-33, C-34).
- **Growth past 50 after 2028.** The flow of crossings is signed per window: held back in 2027 (C-15), ambiguous after (C-21). The stock of employment at these firms is below the counterfactual at every date (C-53).
- **Erosion (TS-3).** The $3,000 charge and the $300,000 cap are fixed in money; premiums rise with medical costs. Over time, offering becomes dearer relative to paying, so the share of bound firms that pay grows, and the cap is a smaller share of each capped firm's labor cost. The 70% share is a ratio and does not erode. The 50 and the 30 are counts and do not move.

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-14 | `employers.capped` | `resources_available_other_uses` | decrease | What $300,000 a year would otherwise have bought; a sum they cannot avoid except by offering cover, which costs more (CR-3, note). | OC-1, CR-8a, CR-3c |
| C-38 | `taxpayers`, recipients of other general-fund spending | `resources_available_other_uses` (the appropriation) | at_least_one_decrease | What the $4.1 million a year would otherwise have funded. The record names no tax, so the payers are a group (OC-1 and OC-3, 0.8). | OC-3, OC-1, CR-8a |
| C-39 | `taxpayers`, recipients of other general-fund spending | `resources_available_other_uses` (charges received) | at_least_one_increase | Nothing given up by them: the charges paid in are a receipt to the fund, which lowers other taxes or funds other spending (CR-8b, CR-8d). | CR-8b, CR-8d |
| C-40 | `taxpayers`, recipients of other general-fund spending | `resources_available_other_uses` (total, short run) | at_least_one_increase | Nothing given up on net in the first year: the capped firms' charges alone exceed the appropriation and the short-run income tax lost (section 7). | CR-12e, CR-8b |
| C-49 | `taxpayers`, recipients of other general-fund spending | `resources_available_other_uses` (total, medium run) | ambiguous | Section 7. | CR-12b |
| C-41 | `officials.enforcement` | `enforcement_cost` | increase | Staff time on reporting, assessment, audits and plan certification. | OC-3, CR-8c, CR-12e |
| C-42 | `employers.bound`, `employers.compliant` | `compliance_cost` (monthly hours tracking, offer reporting, plan administration) | increase | What that staff time and software would otherwise have done. Every employer of 50+ FTE reports offer status (K5), whether or not it already complied. | OC-2, TX-5, CR-8c |
| C-54 | `insurers.group` | `compliance_cost` (K2 certification of plans) | increase | Staff time spent preparing plans for certification. | OC-2, CR-1, CR-8c |
| C-43 | `employers.players` (those keeping their staff and hours) | `resources_available_other_uses` | decrease | What the contributions would otherwise have bought. While wages are fixed (A-3), the term cannot be avoided for the full-timers kept (CR-3, note). | OC-1, CR-8a, CR-8b, CR-3c |
| C-46 | `employers.payers_midsize` (those keeping their full-timers) | `resources_available_other_uses` | decrease | What the charges would otherwise have bought, for the full-timers they keep while wages are fixed. | OC-1, TX-1, CR-3c |

The jobs and hours not exchanged under C-8 to C-12 are prevented exchanges (OC-4): workers and employers both lose the gain each expected from them. They are recorded in those groups, not again here. The jobs contracted out (C-18, C-56) are sales by contractors and agencies (C-60), and the production moved to Tarnley (C-34) is a gain to the sellers who take it (CR-8b, OC-5); not followed further.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | About 135,000 full-timers at firms of 50+ FTE are offered nothing, and about 105,000 are offered less than K1 requires, so K1 binds for them. | binding | 0.9 | Insurance department survey. | Most consequences shrink to the share that remains. |
| A-2 | Some bound firms that offer nothing now choose to offer (mainly those with higher-paid staff who value cover, given the tax exclusion). | other | 0.75 | Comparison of $5,180 times take-up with $3,000; wage mix by firm. | C-1, C-2, C-24, C-26, C-35 to C-37, C-43, C-57, C-58 and the players' chains of C-9 and C-31 are not reported. |
| A-3 | Money wages are fixed in the short run by pay scales and yearly raises in at-will employment (CR-6, 0.8: stickiness as a premise). | other | 0.75 | Raise cycles; posted pay scales in retail and food service. | C-2, C-3, C-8, C-27, C-29, C-43 and C-46 are smaller; the wage adjusts at once; C-57 is not reported. |
| A-4 | Some bound firms choose to pay the charge for at least some full-timers (all the capped firms, many mid-size low-wage firms). | other | 0.9 | At take-up above 58%, $3,000 is less than $5,180 times take-up before any wage offset. | C-3, C-4, C-31, C-46, C-55, C-56, chain P of C-9 and chain G of C-13 are not reported; C-40 fails. |
| A-5 | Some firms with plans short of K1 upgrade them rather than pay. | other | 0.7 | They already offer a plan; the extra cost of meeting K1 is smaller than for firms starting from nothing. | C-5 and C-25 are not reported; those firms join the payers. |
| A-6 | Wages above the minimum can adjust over the medium horizon, as raises are set. | other | 0.8 | Wage growth in these industries is above zero, so raises can be smaller without cuts. | C-7, C-30, C-55, C-58, C-59 and C-37's wage chain are not reported. |
| A-7 | At players, for the marginal pair, cover at 30% is worth less to the worker than its cost to the employer: they could have agreed on it, with the tax exclusion, and did not. | other | 0.6 | The term was absent for 135,000; against this, adverse selection and the cost of arranging a plan in small groups. | Chain Q of C-9 and the players' chains of C-31 and C-45 fail; C-9 rests on chain P alone. |
| A-8 | Workers at payers have some alternative to bound full-time work (firms under 50, part-time work, Tarnley), so the wage does not fall by the whole charge. | mobility | 0.85 | Employment at firms under 50 (about a third of private jobs); part-time work; cross-border commuting. | Chain P of C-9 fails; C-31 to C-34, C-55 and chain S of C-13 are not reported; C-59 loses its (−) chain. |
| A-9 | The minimum wage binds for some workers at bound firms. | binding | 0.85 | 11% of private employees at or near $14, concentrated in retail and food service. | C-10 is not reported. |
| A-10 | Some employers can reschedule jobs from 30 to 35 hours to under 30 at a cost below the per-head cost. | other | 0.75 | Shift scheduling in retail and food service. | C-11, C-50 and C-52 are not reported. |
| A-11 | Between 30 and 40 hours, extra hours from existing full-timers substitute for extra full-time heads. | substitutability | 0.65 | Scheduling practice; R4 limits it above 40. | C-12, C-51 and C-52 are not reported. |
| A-12 | The 45 capped firms stay above 100 uncovered full-timers. | other | 0.9 | Each has several hundred or more. | C-13, C-14, C-47 and C-56 apply to fewer firms; those that fall below 100 join the mid-size payers; the arithmetic in C-40 fails. |
| A-13 | $300,000 a year does not decide whether a capped firm keeps operating in Quenby. | other | 0.85 | The cap is about $200 a head a year against their Quenby sales. | Chain S of C-13 is not reported; exit by some capped firms would need its own premise. |
| A-14 | Some firms near 50 FTE value staying below the line more than the extra work. | other | 0.7 | For a mid-size payer, crossing costs about $108,000 a year; firm counts at 40 to 60 FTE. | C-15, C-16, C-18, C-20 and C-53, the (−) chain of C-21 and of C-17, and one chain of C-60 are not reported. |
| A-15 | Owners of firms near 50 know from January 2027 that the 2027 average decides 2028 status. | expectations | 0.75 | Signing in January 2027; employer associations' guidance. | C-15 starts later in 2027, or in 2028. |
| A-16 | Values of firms near 50 reflect their expected growth. | expectations | 0.6 | Sale prices of small firms as multiples of earnings. | C-17 loses its (−) chain and becomes an increase with A-22. |
| A-17 | Contracting out and franchising are open to some firms near 50 at a cost below the term or the charge (splitting by ownership is closed by the common-control rule). | other | 0.55 | Use of agencies and contractors in landscaping, cleaning, food service. | C-18 and one chain of C-60 are not reported. |
| A-18 | Revenue cannot cheaply verify reported offers, and some firms report offers not made. | enforcement | 0.55 | Audit rates for withholding returns. | C-22 is not reported. |
| A-19 | Insurers, unions, employer associations and the large chains can organize at a cost below their stakes. | other | 0.85 | Existing associations and their activity on the bill. | C-23 is not reported. |
| A-20 | Some workers newly offered employer cover held individual plans. | other | 0.7 | Individual-market enrollment by income and industry. | C-26 is not reported. |
| A-21 | Business values reflect expected earnings, and buyers expected the Act from its introduction. | expectations | 0.7 | Sale multiples; the governor's support at introduction. | C-17, C-27, C-28, C-47, C-48 and C-61 are not reported. |
| A-22 | Firms not bound (small, compliant, capped) compete with mid-size bound firms in local product markets. | substitutability | 0.65 | Industry overlap in retail and food service. | C-28, C-31, C-32 and chain S of C-13 are not reported; C-17, C-47 and C-48 lose their (+) chain; C-59 loses its (+) chain. |
| A-23 | Over the medium to long run, workers' alternatives to bound employment are clearly worse than employers' alternatives. | mobility | 0.6 | Share of jobs at bound firms; cross-border work is open only near Marisport. | C-30 is not reported; the split is not signed. |
| A-24 | Most competitors of mid-size bound firms in local services are bound at a material per-head cost. | other | 0.4 | Most are small firms or capped chains. | Below the cut-off: a rise in local service prices is not reported (section 6). |
| A-26 | Quenby's tradable producers compete with Tarnley producers. | mobility | 0.65 | Plants on both sides near Marisport; shipping costs. | C-33 and C-34 are not reported. |
| A-27 | Newly covered workers use more care billed to insurers than they used without cover. | other | 0.75 | Use of billed care by insurance status. | C-35 is not reported. |
| A-28 | Some newly covered workers or their care were paid for by the ICP. | other | 0.7 | ICP users by employment status; income limit of 200% of poverty. | C-36 is not reported; one (+) chain of C-40 and C-49 fails. |
| A-29 | The $4.1 million is new general-fund money. | revenue_use | 0.9 | K5. | C-38 is not reported; the time comes from some other use of the two departments, recorded as a group (OC-3, 0.9: fixed budget). |
| A-30 | Employers shorten seasonal and temporary engagements below 60 days so that no offer is owed. | other | 0.4 | Replacement costs mid-season against one or two months' charge. | Below the cut-off; not reported. |
| A-31 | Some firms that would have passed 50 in 2027 still pass it later, so part of the growth held back is delayed rather than lost. | other | 0.6 | Growth plans tied to contracts or sites; one year's cost is smaller than the lasting one. | The (+) chain of C-21 fails; C-21 becomes a decrease. C-53 is unaffected. |
| A-32 | The ICP pays per claim, so fewer claims for newly covered workers lower its outlay rather than raising the payment per remaining claim. | revenue_use | 0.6 | R3 is a payment to hospitals that claim; the $310 million is stated as "about", an outturn rather than a fixed sum. | C-36 is not reported; one (+) chain of C-40 and C-49 fails (C-40 does not rest on it). |
| A-33 | Some of the 380 seasonal firms do not offer qualifying cover to their full-timers. | binding | 0.75 | Farms, food processing, resorts and landscaping pay low wages; 21% of full-timers even at firms of 50+ FTE lack a qualifying offer. The survey behind A-1 does not cover these firms. | C-19, C-61 and the U1-a sign of C-20 are not reported. |
| A-34 | Some mid-size payers can obtain agency workers from capped staffing firms at a markup below the $3,000 charge. | substitutability | 0.55 | Staffing firms are among the 45 capped firms; K3 counts agency workers for the agency; agency use in cleaning, security and food service. | C-56, chain G of C-13 and one chain of C-60 are not reported. |
| A-35 | Some newly covered workers are near the margin between staying and moving to an unbound job. | mobility | 0.6 | Job changes in retail and food service are frequent; a third of private jobs are at firms under 50. | C-57 and C-58 are not reported. |
| A-36 | Charges collected in 2028 are not cut by misreporting below $13.5 million less the short-run income tax lost, and that tax lost is smaller than the $9.4 million by which the capped firms' charges exceed the appropriation. | other | 0.75 | A capped firm would have to misreport hundreds of offers, which payroll counts on the same returns would show; at 4.5%, losing $9.4 million of income tax needs over $200 million of wages lost through hours and jobs cut while wages are fixed. | C-40 is `ambiguous`. |
| A-37 | Workers at bound firms cannot all move to unbound work at the old wage in the medium run (the response is partial). | mobility | 0.9 | Bound firms employ about 1.45 million of 2.2 million private employees; firms under 50, part-time work and cross-border work could not absorb them without lower pay. | C-7 is "decrease or no change" rather than a decrease. |

## 11. Report

**The policy.** From January 2028, every Quenby employer with 50 or more full-time equivalents, counted over the previous year, must either offer each employee who averages 30 or more hours a week a health plan meeting a minimum benefit standard, paying at least 70% of the premium, or pay the state $3,000 a year for each such employee it does not cover, up to $300,000 a firm. Employers report on their withholding returns. The law does not say whether seasonal workers count toward the 50.

**Visible consequences.** Full-timers at firms that choose to offer gain employer-paid cover (C-1); those with lean plans get better ones (C-5); those firms pay more per full-timer (C-2). Firms that choose to pay the charge pay more per full-timer too (C-3), and the state collects the charges (C-4).

**Invisible consequences.**
- *Wages and jobs.* As raises are set, wages at bound firms grow less than they would have (C-7). Before then, bound employers cut at least one of hiring, scheduled hours or other benefits (C-8), and after wages adjust they still do, because the charge buys workers nothing, and, if cover is worth less to workers than it costs, because of the contribution too (C-9). At the minimum wage the wage cannot fall, so those margins carry the whole cost (C-10). Workers bear more of the gross cost than employers over time (C-30); at firms that pay the charge, gross and net are the same for them.
- *The 30-hour line.* Jobs near 30 hours are cut below it (C-11), so there are more positions under 30 hours (C-50); above the line, existing full-timers work more hours (C-12) and fewer full-timers are hired (C-51). Some workers move to small firms, part-time work or Tarnley (C-55).
- *The cap.* For the 45 large chains, the charge does not depend on how many people they employ, so it gives them no reason to change hiring or hours at the margin. They pay it (C-14), at about $200 a head against $3,000 for mid-size firms, win sales from them (C-31, C-32), and, where they are staffing firms, supply agency workers that mid-size firms take in place of direct hires (C-56, C-60). So they employ more people or hours (C-13).
- *The 50 line.* Firms near 50 hold back hiring through 2027 (C-15), more firms stay at 40 to 49 (C-16), employment at these firms stays below what it would have been (C-53), and work is contracted out (C-18). If seasonal hours count, seasonal firms that lack cover are bound (C-19) and lose value (C-61), and seasonal hiring near the line falls; if not, those firms are not bound and seasonal engagements replace year-round hires (C-20).
- *Job changes.* Newly covered workers change jobs less while wages are fixed (C-57).
- *Other markets.* Insurers sell more compliant group plans (C-24), firms that upgrade buy richer plans (C-25), insurers bear the cost of certifying them (C-54), and individual plans are dropped (C-26). More care is billed to insurers (C-35), and, if the indigent care program pays per claim, it pays less (C-36). Production moves partly to Tarnley (C-33, C-34). Bound firms' owners lose value from the bill's introduction (C-27) and their returns fall until wages adjust (C-29); small rivals gain value (C-28).
- *The state in the first year.* The capped chains' charges alone exceed the enforcement appropriation, so the general fund gains on net in 2028 (C-40).
- *Breach and lobbying.* Some firms report offers they did not make (C-22). Insurers, unions, the chains and mid-size firms lobby over the charge, the cap and the threshold (C-23).
- *Costs.* Employers' tracking and reporting, including at firms already compliant (C-42), insurers' certification (C-54), enforcement (C-41) and its appropriation (C-38), the capped chains' charge (C-14), and the outlays of players and payers while wages are fixed (C-43, C-46). The income tax base shrinks as wages are turned into excluded premiums (C-37).

**Ambiguous effects.** Total non-wage compensation at players (C-44); total heads at bound firms below the cap (C-52); the net effect on the general fund and those it serves once wages adjust, where charges and lower indigent care outlays oppose the appropriation and lost income tax (C-49); the flow of firms growing past 50 from 2028 on (C-21); the value of firms at 40 to 49 FTE, of the capped chains and of already compliant firms, each burdened in one way and helped by their rivals' costs in another (C-17, C-47, C-48); job changes by newly covered workers once wages adjust (C-58); wages at unbound firms (C-59). Per reading: whether the 380 seasonal firms are bound (C-19, C-61) and which way seasonal hiring near the line moves (C-20).

**Key conditions.** That the mandate binds for about 240,000 full-timers (A-1, p = 0.9). That some firms play and some pay (A-2, p = 0.75; A-4, p = 0.9). That workers have some alternatives to bound work, so the charge reduces jobs or hours after wages adjust (A-8, p = 0.85). That workers' alternatives are worse than employers', for who bears the cost (A-23, p = 0.6). That wages are sticky in the short run (A-3, p = 0.75). That collections in the first year are not cut by misreporting and exceed the appropriation plus the income tax lost (A-36, p = 0.75).

**What this analysis cannot say.** How large any effect is; how many firms play and how many pay; whether the value of cover to the workers who receive it outweighs the wages and jobs given up for it; any effect on health or the use of care beyond its billing (out of scope for version 1); whether the policy is desirable.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | workers.at_players | non_wage_compensation (health cover) | increase | short | visible | B | CR-1, CR-5c, PC-17 | A-1, A-2 |
| C-2 | employers.players | price_paid (labor cost per full-time head) | increase | short | visible | B | CR-1, CR-5c, CR-8b | A-1, A-2, A-3 |
| C-3 | employers.payers_midsize | price_paid (labor cost per full-time head) | increase | short | visible | B | CR-1, TX-2 | A-1, A-3, A-4 |
| C-4 | general_fund | non_tax_receipts (K1 charges) | increase | short | visible | B | CR-8b, TX-1 | A-4 |
| C-5 | workers.lean_plans | non_wage_compensation (plan benefits, employer share) | increase | short | visible | B | CR-1, CR-5c, PC-17 | A-5 |
| C-7 | workers.uncovered (above minimum wage) | wage_rate | decrease | medium | invisible | B | PC-17, TX-2, CR-4, CR-6, CR-7b, CR-12e | A-1, A-6, A-37 |
| C-8 | workers.uncovered | employment, hours_worked (scheduled), non_wage_compensation (other benefits) | at_least_one_decrease | short | invisible | B | PC-17, TX-2, CR-5c, CR-6 | A-1, A-3 |
| C-9 | workers.uncovered | employment, hours_worked (scheduled), non_wage_compensation (other benefits) | at_least_one_decrease | medium | invisible | B | PC-17, TX-2, CR-2, CR-4, CR-12d, CR-12e | chain P: A-4, A-8; chain Q: A-2, A-7 |
| C-10 | workers.min_wage | employment, hours_worked (scheduled), non_wage_compensation (other benefits) | at_least_one_decrease | short–medium | invisible | B | PC-10, CR-6 | A-1, A-9 |
| C-11 | workers.near_30 | hours_worked (jobs at 30–35 hours) | decrease | short–medium | invisible | B | RS-17, CR-1, CR-4 | A-1, A-10 |
| C-12 | workers.full_time | hours_worked (per full-timer, up to 40) | increase | medium | invisible | B | RS-18, CR-4 | A-1, A-11 |
| C-13 | workers.capped_firms | employment, hours_worked (at the capped firms) | at_least_one_increase | medium | invisible | B | RS-18, CR-4, CR-9, OC-5, CR-12d | chain S: A-8, A-12, A-13, A-22; chain G: A-4, A-12, A-34 |
| C-14 | employers.capped | resources_available_other_uses | decrease | short | invisible | B | OC-1, CR-8a, CR-3c | A-12 |
| C-15 | employers.near_50 | employment (hires taking the 2027 average to 50+) | decrease | short (2027) | invisible | B | RS-17, RS-8, CR-4, CR-10a | A-14, A-15 |
| C-16 | employers.small | number_of_sellers (firms at 40–49 FTE) | increase | medium | invisible | B | RS-17, CR-4, CR-7a | A-14 |
| C-17 | employers.near_50 (owners, 40–49 FTE) | asset_value | ambiguous | short | invisible | B | RS-17, CR-7c, CR-10c, CR-12b | A-14, A-16, A-21, A-22 |
| C-18 | employers.near_50 | reclassification (work contracted out or franchised) | increase | medium | invisible | B | RS-17, RS-5 | A-14, A-17 |
| C-19 | employers.seasonal | price_paid (labor cost per full-time head) | U1-a: increase; U1-b: no_change | short | invisible | B | CR-1 | A-33 |
| C-20 | employers.seasonal, employers.near_50 | employment (seasonal engagements up to 120 days) | U1-a: decrease; U1-b: increase | short–medium | invisible | B | RS-17, RS-5, CR-4 | A-14; U1-a also A-33 |
| C-21 | employers.near_50 | employment (hires past 50 FTE in each year from 2028; flow) | ambiguous | medium | invisible | B | RS-8, RS-17, CR-10a, CR-12b | A-14, A-31 |
| C-22 | employers.bound | legal_breach (offers reported but not made) | increase | short–medium | invisible | B | RS-3, CR-1, CR-4 | A-18 |
| C-23 | insurers, unions, employers.payers_midsize, employers.capped, employers.near_50 | lobbying_effort | increase | medium | invisible | B | RS-7 | A-19 |
| C-24 | insurers.group | quantity_traded (group plans meeting K2) | increase | short | invisible | B | CR-9, CR-5 | A-2, A-5 |
| C-25 | insurers.group | specification_level (plans offered by firms that upgrade) | increase | short | invisible | B | CR-1, CR-4, TS-3 | A-5 |
| C-26 | insurers.individual | quantity_substitute (individual plans) | decrease | short | invisible | B | RS-1, CR-9 | A-2, A-20 |
| C-27 | employers.bound (owners, below the cap) | asset_value | decrease | short | invisible | B | CR-7c, CR-10c | A-3, A-21 |
| C-28 | employers.small (owners, under 40 FTE) | asset_value | increase | short | invisible | B | CR-7c, CR-10c, CR-9 | A-21, A-22 |
| C-29 | employers.bound | return_on_capital | decrease | short | invisible | B | CR-7b | A-3 |
| C-30 | workers.uncovered | tax_share_borne (gross share of the cost of K1) | increase | medium–long | invisible | B | CR-7b, DM-1 | A-6, A-23 |
| C-31 | employers.payers_midsize, employers.players (local services) | quantity_supplied | decrease | medium | invisible | B | RS-14, RS-6, CR-12d | payers: A-4, A-8, A-22; players: A-2, A-7, A-22 |
| C-32 | employers.capped, employers.small, employers.compliant | quantity_supplied (in markets shared with mid-size bound firms) | increase | medium | invisible | B | CR-9, CR-7a | A-8, A-22 |
| C-33 | employers.tradable | quantity_supplied (in Quenby) | decrease | long | invisible | B | RS-14, RS-6, RS-4 | A-8, A-26 |
| C-34 | neighboring_jurisdictions | quantity_supplied (into Quenby) | increase | medium–long | invisible | B | RS-4 | A-8, A-26 |
| C-35 | providers.medical | quantity_complement (care billed to insurers) | increase | short–medium | invisible | B | RS-12, CR-9 | A-2, A-27 |
| C-36 | general_fund | subsidy_outlay (ICP payments) | decrease | short–medium | invisible | B | CR-9, CR-8b | A-2, A-28, A-32 |
| C-37 | general_fund | tax_revenue (income tax) | decrease | medium | invisible | B | TX-10, CR-8b | A-2, A-6, A-8 |
| C-38 | taxpayers, recipients of other general-fund spending | resources_available_other_uses (appropriation) | at_least_one_decrease | short | invisible | B | OC-3, OC-1, CR-8a | A-29 |
| C-39 | taxpayers, recipients of other general-fund spending | resources_available_other_uses (charges received) | at_least_one_increase | short | invisible | B | CR-8b, CR-8d | A-4 |
| C-40 | taxpayers, recipients of other general-fund spending | resources_available_other_uses (total) | at_least_one_increase | short | invisible | B | CR-12e, CR-8b | A-4, A-12, A-29, A-36 |
| C-41 | officials.enforcement | enforcement_cost | increase | short | invisible | B | OC-3, CR-8c, CR-12e | none (arithmetic) |
| C-42 | employers.bound, employers.compliant | compliance_cost (hours tracking, offer reporting) | increase | short | invisible | A | OC-2, TX-5, CR-8c | none |
| C-43 | employers.players (keeping staff and hours) | resources_available_other_uses | decrease | short | invisible | B | OC-1, CR-8a, CR-8b, CR-3c | A-1, A-2, A-3 |
| C-44 | workers.at_players | non_wage_compensation (total, including cover) | ambiguous | short–medium | invisible | B | CR-12b | A-1, A-2, A-3 |
| C-45 | employers.bound | price_paid (labor cost per full-time head) | increase | medium | invisible | B | CR-5c, CR-12d, CR-12e | players: A-2, A-7; payers: A-4, A-8 |
| C-46 | employers.payers_midsize (keeping their full-timers) | resources_available_other_uses | decrease | short | invisible | B | OC-1, TX-1, CR-3c | A-3, A-4 |
| C-47 | employers.capped (owners) | asset_value | ambiguous | short | invisible | B | CR-7c, CR-10c, CR-9, CR-12b | A-12, A-21, A-22 |
| C-48 | employers.compliant (owners) | asset_value | ambiguous | short | invisible | B | CR-7c, CR-10c, CR-9, CR-12b | A-21, A-22 |
| C-49 | taxpayers, recipients of other general-fund spending | resources_available_other_uses (total) | ambiguous | medium | invisible | B | CR-12b, CR-12g | A-2, A-4, A-28, A-29 |
| C-50 | workers.near_30 | employment (positions under 30 hours) | increase | short–medium | invisible | B | RS-17, CR-4 | A-1, A-10 |
| C-51 | workers.full_time | employment (full-time heads) | decrease | medium | invisible | B | RS-18, CR-4 | A-1, A-11 |
| C-52 | employers.bound (below the cap) | employment (total heads) | ambiguous | short–medium | invisible | B | CR-12b | A-1, A-10, A-11 |
| C-53 | employers.near_50 | employment (stock, each date from 2028) | decrease | medium | invisible | B | RS-17, CR-10a, CR-12e | A-14 |
| C-54 | insurers.group | compliance_cost (K2 certification) | increase | short | invisible | A | OC-2, CR-1, CR-8c | none |
| C-55 | workers.uncovered (at payers, at the margin) | employment (firms under 50) (+), employment (part-time) (+), employment (Tarnley) (+) | at_least_one_increase | medium–long | invisible | B | CR-4b, CR-7a | A-4, A-6, A-8 |
| C-56 | employers.payers_midsize | reclassification (direct hires replaced by agency workers from capped staffing firms) | increase | medium | invisible | B | RS-5, RS-18, CR-4 | A-4, A-12, A-34 |
| C-57 | workers.at_players | job_changes (moves to unbound jobs) | decrease | short | invisible | B | CR-4, CR-6 | A-2, A-3, A-35 |
| C-58 | workers.at_players | job_changes | ambiguous | medium | invisible | B | CR-4, CR-12b | A-2, A-6, A-35 |
| C-59 | workers.unbound | wage_rate | ambiguous | medium | invisible | B | CR-9, CR-7a, CR-12b | A-6, A-8, A-22 |
| C-60 | sellers.contract_services | quantity_traded (contracted and agency labor) | increase | medium | invisible | B | CR-9, LW-10, CR-12d | A-14, A-17; or A-4, A-12, A-34 |
| C-61 | employers.seasonal (owners) | asset_value | U1-a: decrease; U1-b: no_change | short | invisible | B | CR-7c, CR-10c | A-21, A-33 |

There is no C-6: the choice between offering and paying is recorded through its two branches, not as a consequence of its own. There is no A-25: a draft premise on the capped chains' local markets was merged into A-22.

## Corrections after the core-only comparison

The core-only re-run and its comparison (`05_examples_core/WE-036_employer_health_cover_mandate_core.md`) were checked row by row against the core rules and catalog 0.9. What changed, by consequence:

- **C-13** (capped firms' employment): `no_change` replaced by `employment`, `hours_worked` `at_least_one_increase`. The 0.8 draft signed one channel; the capped firms also win sales from mid-size payers (C-32) and agency business (C-56), and their demand for labor rises with it (CR-9, LW-10). RS-18's 0.9 clause on caps per firm confirms that the charge itself gives no shift. The comparison's single `employment` increase is recorded as a group, because the added labor goes to an existing activity (OC-5).
- **C-17** (value of firms near 50): narrowed to firms at 40 to 49 FTE and changed from decrease to `ambiguous` (RS-17, 0.9: rivals above the line are burdened too). **C-28** narrowed to firms under 40 FTE so that it no longer overlaps C-17.
- **C-27** narrowed to bound firms below the cap; **C-47** added: capped firms' value `ambiguous` (fixed charge against sales won, CR-12b).
- **C-28** no longer covers compliant firms; **C-48** added: compliant firms' value `ambiguous`, because they bear the quarterly offer reporting. **C-42** now includes compliant firms, which K5 binds to report.
- **C-40** split by horizon (CR-12g): short run `at_least_one_increase` by arithmetic with a premise (the capped firms alone owe $13.5 million against $4.1 million; A-36 covers misreporting and the short-run income tax lost, which the core version had wrongly put at zero); **C-49** added for the medium run, `ambiguous`.
- **C-25**: `variety` decrease replaced by `specification_level` increase for firms that upgrade. A firm that pays keeps its lean plan, since K1 charges it either way.
- **C-11** and **C-12** no longer mixed groups: each member is signed (RS-17 and RS-18, 0.9; one CR-4 switch moves both). **C-50** (positions under 30 hours, increase), **C-51** (full-time heads, decrease) and **C-52** (total heads, `ambiguous`, CR-12's two-items clause, which now reaches them) added.
- **C-21** now states that it is signed on a flow (CR-12, 0.9) and cites RS-8's main clause and its 0.9 clause on more timing chains in place of the 0.8 Unless clause. **C-53** added: employment at firms near 50, as a stock, `decrease` at each date from 2028.
- **C-7**: the response argument against workers' moves to alternatives is recorded in section 7, with the partial-response premise 0.9 requires (A-37).
- Hidden premises made explicit: **C-36** (A-32, the ICP pays per claim); **C-19**, **C-20** under U1-a (A-33, seasonal firms lack cover; A-1's survey does not cover them); **C-31** (A-7 for the players' chain).
- Omissions added: **C-54** (K2 certification cost), **C-55** (workers move to unbound work), **C-56** (agency labor from capped staffing firms, A-34), **C-57** and **C-58** (job changes of newly covered workers, A-35), **C-59** (wages at unbound firms, `ambiguous`), **C-60** (contracted and agency labor sold), **C-61** (seasonal firms' value per reading).
- Classification: PC-17's 0.9 clause on a mandate with a buy-out charge now covers the split by response; K4 is operation 3 below the cap and operation 4 above it (CR-1, 0.9). No promoted pattern (RS-19, RS-20, OC-9, EN-12 to EN-15) applies: there is no payment for crossing a boundary, enforcement is by self-report rather than complaint, there is no borrowing, no right allocated by history or tradable right, no standard on new durable units, and offer-status reporting is not a disclosure to buyers. No chain runs through `proximity` or `shared_facility`, so CR-12's 0.9 rule on Tier C against Tier B does not arise; OC-8's baseline does not arise.

Comparison conclusions rejected or not applied:
- *C-9, chain Q not needed.* Kept: it is an independent chain with the same sign, and CR-12d lets a consequence list every chain that reaches it.
- *C-50 (core), U1-b `no_change` for seasonal firms' value.* Accepted only for the burden of K1 on them; under U1-b any of them at 40 to 49 year-round FTE fall under C-17, as stated in section 6.
- *C-21 and the core's C-22, J.* The pattern version's flow sign is kept; catalog 0.9 asks only that the flow or stock be named, and the stock is now recorded as C-53.
- *C-4 `non_tax_receipts` and other V rows (C-2, C-3, C-5, C-8, C-16, C-26, C-32, C-34, C-35, C-38, C-39).* Not changed: different variable choices for the same claim, with no error found.
- *Core C-18 and C-20 (employers' short-run share; workers at payers' loss of means).* Not added: the comparison itself finds both overclaim.

## Gaps found

Parts (a) to (d) record the 0.8 run. Under 0.9, (c) 1 is adopted as RS-18's clause on caps per firm, (c) 2 as RS-17's clause on lines on hours, and (c) 3 as PC-17's clause on a mandate with a buy-out charge; (b) 1, (c) 4 and (d) remain open.

**(a) Calculus gaps (a step no core rule covers).** None. Every step was derived from CR-1 to CR-12 or from patterns whose preconditions held, or held after the interpretation stated in (c) and (e). The step closest to a gap was the choice between offering and paying, which no pattern covers; CR-4 (x: offer, y: pay) and CR-1's 0.7 clause on splitting a class by response cover it.

**(b) Unclear core rules.**
1. *CR-12d with mixed branches.* C-9 and C-45 are reached by two chains that run through different subclasses (players and payers) of the same class. CR-12d says the consequence holds if any one chain's premises hold. That is right for the class as a group, but the sign then says nothing about which subclass moved. CR-12d could say whether chains through different subclasses count as "independent chains" for (d), or whether the subclasses should be recorded separately.
2. *CR-6, 0.8, at-will stickiness.* Worked as written (A-3). Less clear is what to do with the 6% under fixed-term collective agreements: the clause makes them "regulated while they last" with no premise, so the short-run consequences for them need no A-3. The table carries one premise for the whole class; a per-subclass split would be more exact and add rows for little.
3. *CR-7, 0.7, gross and net, when a policy has a branch the receiver does not value.* The clarification assumes the mandated term "is worth something to the side that receives it". Under play or pay, the same class receives the term at players and nothing at payers. Stating the share as gross, and saying that gross equals net at payers, was a reading of the clause, not something it says.
4. *OC-3, 0.8, right baseline, for administration of another program.* The clause's example is enforcement of an old rule that falls because the activity shrinks. Here what falls is the administration of a spending program (the ICP's claims), because fewer people are uninsured. It was treated as the same case (section 7, arithmetic). The clause could say whether "enforcement without the policy" includes administration of other programs the policy shrinks. Its tier clause also gives Tier B whenever some enforcement is made unnecessary, even where arithmetic on the record settles the sign with no empirical premise, as here (C-41 is recorded at B with no assumption); whether arithmetic restores Tier A is not said.

**(c) Missing or wrong patterns.**
1. *RS-18 with a cap per firm gives the wrong sign.* RS-18's If clause reads "a cost per worker (or per unit) that stops at a cap". K4's cap is per firm. Applied as written, with the firm as the unit, RS-18's Then clause says employers shift hours toward fewer heads. The derivation gives no shift at all for capped firms, since above the cap a head adds nothing (C-13, `no_change`), and CR-4's 0.8 clause on fixed costs per firm is the rule that applies. Proposed: RS-18's If should say "a cap per worker"; add an Unless: "where the cap is per firm, the cost above it is fixed per firm (CR-4, 0.8) and the hours-for-heads shift does not follow". This is a pattern whose preconditions, as worded, were met but whose conclusion was wrong.
2. *RS-17 for a threshold on a worker's hours.* RS-17 is written for a firm's size. The 30-hour line needed it read with "job" for "firm": keep jobs below the line, split them across part-time jobs; its capitalization clause had no counterpart. Proposed: widen RS-17's If to "a threshold on any counted quantity (a firm's staff, a worker's hours, a product's weight)", saying which clauses apply to non-assets.
3. *PC-17 when the term can be bought off.* PC-17's If requires that "every contract of a kind include a term". A play-or-pay mandate lets the bound party pay instead. Splitting by response (CR-1, 0.7) made PC-17 apply to players and TX-2 to payers, which worked; PC-17 could say so in an Unless clause. Candidate pattern: "a mandate with a buy-out charge", derived from CR-4 (x: comply, y: pay), with the charge analyzed as a tax on the option it attaches to and the share of each branch a premise. Seen once.
4. *RS-14's two branches when rivals face the cost at different rates.* Mid-size payers face $3,000 a head; the capped chains $200; small firms nothing. RS-14's branches are "competitors face the same increase" and "competitors are exempt". The case was put in the second branch, with the price rise left as a below-cut-off premise (A-24). RS-14 could say that competitors facing a much smaller cost count as exempt for this purpose.

**(d) Vocabulary.**
1. *A charge per head that buys the payer an exemption.* Neither `mandated_contract_term` nor `per_unit_tax` fits K1 alone; it was recorded as the first with "an alternative charge per head". A combined instrument type (`mandate_with_buyout`) would make the split visible in the policy record.
2. *Hours present and hours scheduled* (raised in WE-029, still open) did not arise here, since cover does not change hours present. *Hours per worker and total hours* did: `hours_worked` is defined as hours per worker, and C-8 to C-10 use it for hours scheduled across the class. Qualifiers keep them apart.
3. *The state budget as an actor class.* `general_fund` is not in the generic list (2.2), though `residual_claimant` is close. Receipts, outlays and lost revenue of one budget, and the group of those it serves, needed both a class for the fund and the group in OC-1's 0.8 wording.

**(e) Test of 0.8.**
- *PC-17 (0.7).* Needed interpretation: its If clause is not met by a play-or-pay mandate as a whole; it applied after splitting the class by response (CR-1, 0.7), and gave the right group sign for players.
- *RS-17 (0.7), the 50-FTE line.* Worked as written: stay below, split (here only by contracting out, since the common-control rule closes splitting), lower value, and the response in the measurement year before the policy takes effect (C-15 to C-18).
- *RS-17 (0.7), the 30-hour line.* Needed interpretation: written for firm size; applied to a worker's hours with "job" for "firm", without the capitalization clause (C-11).
- *RS-18 (0.7).* Worked as written for the per-head cost above the 30-hour line (C-12). Failed for the cap per firm: as worded it gives a shift of hours to fewer heads, where the derivation gives no change (C-13; (c) 1).
- *CR-4 0.8, fixed cost per firm.* Worked as written: it gave the right result for capped firms, which RS-18 did not.
- *CR-7 0.7, gross and net burdens.* Worked, with interpretation: C-30 is stated as a gross share; the clause did not anticipate a branch whose payment the receiving side does not value, where gross and net coincide ((b) 3).
- *CR-6 0.8, existing contracts and at-will stickiness.* Worked as written: wage stickiness in at-will employment is a premise with a probability (A-3); fixed-term collective agreements need none ((b) 2).
- *OC-1 and OC-3 0.8, payers from a general budget as a group.* Worked as written for the appropriation (C-38). Needed interpretation when the same policy pays receipts into the same budget: the group was recorded once as payer (C-38) and once as receiver (C-39), with the total ambiguous (C-40), following CR-12's 0.8 clause on two items in one variable.
- *OC-3 0.8, right baseline.* Needed interpretation: what the policy shrinks here is the administration of a spending program, not enforcement of a rule; arithmetic on the record settled the sign (C-41; (b) 4).
- *CR-12 0.8, two items in one variable.* Worked as written (C-44 for compensation; C-38 to C-40 for the general fund).
- *RS-8 0.8 Unless, opposing timing chains.* Worked as written: growth past 50 after 2028 is `ambiguous` (C-21).
- *CR-12 0.8, three kinds of opposing chain.* Kind 1 used once (a scale effect on hours per full-timer, a Tier C note in section 7); kind 2 used for C-21 and C-40 (premises at or above 0.5, so `ambiguous`). Worked as written.
- *TS-3 0.8, product standards.* Worked as written for C-25; the money parameters erode as in the main clause.
- *Candidate patterns from 06_gaps.md, 6.2e, needed here (second use).* "Selection under a uniform term" (WE-029) was not needed: the charge and contribution are per head, not per use. "Complaint-only enforcement" was not needed: enforcement is by self-report on returns. A near relative of complaint-only enforcement was needed: breach where enforcement rests on self-reporting checked by audit (C-22), derived from CR-1 and CR-4 per firm. The new candidate "a mandate with a buy-out charge" is listed under (c) 3.
- Re-run note: the core-only comparison contradicted four verdicts recorded above as "worked": RS-17 on the 50-FTE line overclaims the value of firms below it (C-17), RS-8's 0.8 Unless was not the clause that applies (C-21), RS-18's failure for the cap per firm was replaced by a `no_change` that left out the capped firms' sales gains (C-13, also qualifying the CR-4 0.8 verdict), and TS-3 with `variety` overclaimed for lean plans (C-25); it also found the general-fund total for the short run signed by arithmetic (C-40, qualifying the OC-1 and OC-3 verdict).
