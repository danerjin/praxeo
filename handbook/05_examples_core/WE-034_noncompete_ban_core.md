# WE-034 / Analysis: Non-compete clauses made unenforceable, for new and existing contracts

Analyst: core-only re-run (Handbook 0.7)  |  Rules: core rules CR-1 to CR-12 only  |  Status: compared

## 1. Policy record

**Teravel Freedom to Work Act.** The State of Teravel has about 3.2 million private-sector workers. A 2024 survey by the state labor department found that about 17% had signed a non-compete clause; the share is higher in software and engineering (45%), sales (35%), physicians and dentists in group practices (40%), finance (30%) and hair and beauty salons (25%). Until now Teravel courts enforced "reasonable" non-competes (up to two years, within the employer's trading area) under common law. Employers filed about 400 enforcement suits a year, and many more disputes were settled by letter. Teravel's largest city, Halbrook, lies on a river whose far bank is in the State of Mossgrave, which enforces non-competes; about 60,000 people commute across the river each way.

| Field | Value | Source sentence |
| --- | --- | --- |
| Jurisdiction (and what lies just outside) | State of Teravel; just outside, the State of Mossgrave across the river from Halbrook, which enforces non-competes. About 60,000 commuters cross each way. | "Halbrook, lies on a river whose far bank is in the State of Mossgrave. Mossgrave enforces non-competes" |
| Announced / enacted / effective / expires | Announced 3 February 2025 (introduced with the governor's public support); enacted 12 June 2025; effective 1 January 2026; no expiry. | "introduced on 3 February 2025 ... passed on 12 June 2025 and takes effect on 1 January 2026, with no expiry" |
| Enforcement (who, penalties, resources) | Private suits by workers (actual damages, $5,000 per worker, attorney fees); Attorney General's Labor Bureau (civil penalties up to $10,000 per violation), from its existing budget. | K5 |
| Counterfactual law | Courts keep enforcing reasonable non-competes. The Trade Secrets Act is in force in both worlds (`existing_rules`). | "Without the Act, courts keep enforcing reasonable non-competes." |

| Component | Instrument | Target | Bound | Parameters | Exemptions |
| --- | --- | --- | --- | --- | --- |
| K1 Void restraint | `term_prohibition` (a contract term made unenforceable) | Any term of an employment or independent-contractor agreement that prohibits or restricts a worker, after the work relationship ends, from working for another person or carrying on a business, or that imposes a penalty for doing so | Employers of workers who primarily work in Teravel, whatever law the contract chooses | Void. Applies to agreements made before, on or after the effective date; pending cases are decided under the Act. Includes forfeiture-for-competition clauses. | K2, K3 |
| K2 Sale of a business | Exemption | Restraints given by a person who sells the goodwill of a business or an ownership interest in one | — | No minimum share stated. | — |
| K3 Preserved terms | Exemption | (a) non-disclosure of trade secrets and confidential information; (b) non-solicitation of customers or staff for up to 12 months, where it does not in effect prevent work in the field; (c) a notice period during which the worker remains employed; (d) forfeiture of unvested pay or benefits under a plan that applies to every departure | — | No maximum length for (c). | — |
| K4 Notice | Mandated action | Employers | Every employer with a non-compete with a current worker, or a former worker who left after 1 January 2024 | Written notice by 1 March 2026 that the term is void. | — |
| K5 Enforcement | Enforcement | K1, K4 | Employers | Private suits: actual damages, $5,000 per worker, attorney fees. Labor Bureau: civil penalties up to $10,000 per violation, no new appropriation. | — |

Unclear provisions:
- **U1 (long paid notice periods, "garden leave").** U1-a: a paid notice period of six to twelve months with no duties, during which the worker may not work for anyone else, is preserved by K3(c). U1-b: it is a restraint "in effect" and void under K1. The Attorney General's draft guidance does not decide it.
- **U2 (training repayment agreements).** U2-a: a term requiring repayment of employer-paid training on leaving within 24 months is a "penalty" under K1 and void. U2-b: it is not, because it applies to every departure and only recovers a cost.
- Whether K2 covers token equity grants is an assumption (A-12), not a reading, because the courts' practice under the 1998 partnership statute is evidence of how K2 will be read.

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | CR-1 operations | Core rules applied |
| --- | --- | --- | --- | --- |
| K1 Void restraint | triangular (prohibits an exchange of a restraint between employer and worker) | Yes where enforced and known (A-2); binding for the 17% now bound, and for new contracts that would have contained the term | Employers: op 1 (the option "hire on terms that include an enforceable restraint" is removed; the option "enforce an existing restraint" is removed). Bound workers: op 2 (the option "work for a rival or found a firm without penalty" is added); op 3 (the litigation risk and forfeiture attached to such a move are removed). Hiring firms: op 3 (litigation risk and buy-out payments removed from hiring a bound worker). Counterfactual law: reasonable restraints enforced. | CR-1, CR-3, CR-4, CR-5a, CR-5c, CR-7b, CR-7c, CR-8b, CR-9, CR-10a, CR-10c |
| K2 Sale exemption | exemption from K1 | Binding as an exit route only where a sale or buy-in is bona fide (A-11; A-12 for token equity) | Employers and owners: op 2 relative to K1 (a restraint remains available when attached to a sale of goodwill or ownership interest) | CR-4 (x: covered form, y: exempt form) |
| K3 Preserved terms | exemption from K1 | Yes (A-4) | Employers: op 2 relative to K1 (the preserved forms remain open). U1: op 2 for long paid notice periods under U1-a; op 1 under U1-b. U2: op 1 for repayment agreements under U2-a; op 2 under U2-b. | CR-4, CR-6 (pressure displaced to unregulated terms), CR-12b |
| K4 Notice | mandated action (triangular: forces a communication from employer to worker) | Yes (A-2) | Employers: op 3 (a duty attached to having held a restraint). Workers: information conveyed (CR-11c). | CR-1, CR-8c, CR-11c |
| K5 Enforcement | binary (penalties) and private right of action | Yes, as a deterrent (A-2); actual penalties need violations (A-20, p 0.35, not reported) | Employers: op 3 (damages, fees and penalties attached to enforcing or inserting a void term). Labor Bureau: a new task with no new means (A-18). | CR-4 (x: comply, y: violate), CR-8a, CR-8c |

K1 removes an option that both parties could previously choose (an enforceable restraint exchanged for pay, training or a job). K3 keeps nearby options open, so much of the pressure moves to them (CR-6: pressure seeks every open margin). The ontology's instrument list has `term_prohibition`; K2 to K5 have no instrument type of their own (see Gaps found, c).

## 3. Actor classes

| Actor class | Role | How its options change (CR-1) |
| --- | --- | --- |
| workers.bound | Workers primarily working in Teravel who hold a non-compete now, or left after 1 January 2024 | Op 2: work for a rival or found a firm without penalty (from 1 January 2026; pending suits decided under the Act). Op 3: forfeiture for competition removed. Informed by K4 (CR-11c). |
| workers.bound.founders | Bound workers with plans to found a firm in their field (A-3) | Op 2: the option "found a firm" is added. |
| workers.bound.waiting | Bound workers who would have moved in the second half of 2025 by buy-out or litigation (A-14) | CR-10a: moving after 1 January 2026 brings the same job without the buy-out or suit. |
| workers.bound.field_switchers | Bound workers who, in the counterfactual, change employer by leaving their field (A-8) | Op 2: a move within the field is now open. |
| workers.new_hires | Workers hired after the Act into jobs that would have carried a restraint | CR-5c: the restraint is no longer among the terms either side can give or receive. |
| workers.trainees | Workers in jobs where the restraint protected employer-funded general training (A-5) | Through CR-9 (contract): employers' option to fund training is worth less. |
| workers.unbound | Workers in the same fields without a non-compete | Through CR-9: compete for the same jobs as newly mobile workers and are sought by new firms. |
| workers.other_fields | Workers in the fields that field-switchers would have entered (A-8) | Through CR-9: fewer entrants competing for their jobs. |
| workers.cross_river_commuters | Teravel residents primarily working in Mossgrave, still bound by Mossgrave restraints | Op 2 indirectly: Teravel jobs now come without a restraint (CR-4, x: Mossgrave job, y: Teravel job). |
| employers.restraining | Teravel employers holding non-competes (net trainers among them) | Op 1: enforcement removed; op 3: K4 notice duty, K5 penalties. Op 2 via K2, K3. |
| employers.trainers | Employers funding general training protected by restraints (A-5) | Op 1: the protected recovery of training cost is removed; K3(d), U2 and repayment capped at cost restore part (A-6). |
| employers.hiring_experienced | Firms that hire more trained staff than they train (A-16) | Op 3: litigation risk and buy-out payments removed from hiring bound workers. Face higher pay for experienced staff (CR-7a). |
| employers.group_practices | Practices that can use partnership buy-ins under K2 (A-11) | Op 2 via K2. |
| sellers.prospective | New firms in the bound fields (spin-offs; firms choosing Teravel, A-24) | Entry is cheaper: founders are free, staff can be hired. |
| buyers.services | Clients of salons, clinics, advisory and other firms in the bound fields | Through CR-9 (exchange): may follow their provider (A-17); more sellers (A-23); higher labor costs passed on. |
| intermediaries.recruiters | Placement firms (A-21) | Through CR-9 (complement to hiring): more movable candidates. |
| intermediaries.lawyers | Employment lawyers | Through CR-9: less non-compete enforcement work; more redrafting, trade-secret and non-solicitation work (A-4, A-19). |
| officials.courts | Teravel courts | Fewer non-compete suits; more trade-secret and non-solicitation suits. |
| officials.labor_bureau | Attorney General's Labor Bureau | New task (K4, K5) with no new means (A-18). |
| other_bureau_beneficiaries | Those served by the Bureau's other enforcement work | Through CR-8a: the Bureau's means are diverted. |
| neighboring_jurisdictions | Mossgrave employers and workers | Training-intensive work may move there (A-22); hiring-intensive firms and founders may move away (A-24); compete for cross-river commuters. |
| organized_interests | Employers' associations, worker groups, start-up associations (A-13) | CR-4 (x: accept, y: lobby) from the bill's introduction. |
| owners.restraining_firms | Shareholders and partners of firms whose yields relied on restraints (A-15) | CR-7c: the expected loss of yield is capitalized when the Act becomes expected. |

## 4. Direct effect

CR-1 and CR-2: the immediate change for those whose options K1, K4 and K5 alter.

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-1 | employers.restraining | term_prevalence (enforceable non-compete and forfeiture-for-competition terms) | decrease | short; medium; long | CR-1 op 1, CR-5a, CR-4 (x: comply, y: violate) | A-2 |
| C-2 | workers.bound | job_changes (to rivals and own start-ups, from 1 January 2026) | increase | short; medium; long | CR-1 op 2, CR-11c, CR-4 (mirror), CR-12b with CR-12e | A-1, A-2, A-9 |
| C-3 | workers.bound | wage_rate | increase | short; medium | CR-7b, CR-5c, CR-6 | A-7, A-2 |
| C-4 | sellers.prospective (bound fields, Teravel) | entry_rate | increase | medium; long | CR-1 op 2, CR-4 (x: stay employed, y: found), CR-7a | chain 1: A-3, A-2; chain 2: A-24 |
| C-5 | employers.restraining | compliance_cost (K4 notices; redrafting into preserved forms) | increase | short | CR-1 op 3, CR-8c | A-2, A-4 |
| C-6 | officials.labor_bureau | enforcement_cost (K4 and K5 tasks: guidance, monitoring, suits) | increase | short; medium | CR-1, CR-8c | - |

## 5. Responses

CR-4 for every pair of options each actor class has; CR-6 for displaced pressure; CR-10a for timing.

**Core-rule sweep by actor class** (final check item 7). CR-4 pairs considered for each class: substitute (preserved forms), evade (keep void terms), relocate (Mossgrave), reclassify (K2), exit (stop training, leave the field), lobby, timing (2025 window), entry (found). CR-6: no price is fixed by the Act; pressure moves to unregulated terms (pay, deferred pay, notice periods, repayment terms). CR-7: wages of mobile workers (CR-7a, b), asset values (CR-7c). CR-9: every relation in section 6. Where a pair yields nothing reportable it is noted in "Not reported" (section 10).

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-7 | employers.restraining | term_prevalence (non-solicitation, confidentiality and unvested-pay terms) | increase | short; medium | CR-4 (x: void form, y: preserved form), CR-6, CR-10a | A-4 |
| C-8 | workers.bound | non_wage_compensation (unvested deferred pay and retention bonuses) | increase | short; medium | CR-4, CR-5c, CR-6 | A-10 |
| C-9 | employers.restraining | term_prevalence (paid notice periods of six months or more) | U1-a: increase; U1-b: decrease | short; medium | CR-1 per reading, CR-4, CR-6 | A-4, A-N1 |
| C-10 | employers.trainers | term_prevalence (training repayment agreements) | U2-a: decrease; U2-b: increase | short; medium | CR-1 per reading, CR-4, CR-6 | A-4, A-5, A-N1 |
| C-11 | workers.trainees | non_wage_compensation (employer-funded general training) | decrease | medium; long | CR-4 (x: fund training, y: do not), CR-5a, CR-12b with CR-12e | A-5, A-6 |
| C-12 | employers.group_practices | reclassification (restraints moved into partnership buy-ins under K2) | increase | medium | CR-4 (x: covered form, y: exempt form) | A-11 |
| C-13 | organized_interests (employers' associations; worker groups and start-up associations) | lobbying_effort | increase | short (from 3 February 2025); medium | CR-4 (x: accept, y: lobby), CR-10a, CR-8c | A-13 |
| C-14 | workers.bound | job_changes (to rivals, 3 February to 31 December 2025) | ambiguous | short (announcement window) | CR-10a, CR-4, CR-12b | A-14, A-N4 |
| C-15 | employers.restraining | side_payments (buy-out receipts for releasing bound workers) | decrease | short (from 2025); medium | CR-10a, CR-1 op 1, CR-8b | A-14 |
| C-16 | employers.hiring_experienced | side_payments (buy-out outlays to hire bound workers) | decrease | short (from 2025); medium | CR-8b, CR-1 op 3 | A-14 |
| C-17 | workers.bound | job_changes (to non-competing employers and out of the field) | decrease | medium; long | CR-4 (two chains), CR-12a, CR-12d | chain 1: A-8; chain 2: A-10 |
| C-18 | employers.training_intensive (Teravel) | employment (training-intensive work located in Teravel) | decrease | medium; long | CR-4 (x: here, y: there), CR-7a | A-22 |
| C-19 | workers.cross_river_commuters | job_changes (from Mossgrave to Teravel employers) | increase | short; medium | CR-4 (x: Mossgrave job, y: Teravel job) | A-N3 |
| C-20 | employers.restraining | quantity_traded (client accounts served) | decrease | short; medium | CR-9 (exchange), CR-4 for clients | A-17, A-1, A-2 |

## 6. Second-order effects

CR-9 along named relations, then CR-5 to CR-7 in each market reached. Depth limit 4. The chain to the suppliers and landlords of relocated training-intensive work (depth 4 from K1 via A-22) and to the customers of the Bureau's other work (depth 4) is pruned as diffuse.

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C-21 | employers.hiring_experienced | search_cost (hiring experienced staff) | decrease | short; medium | CR-1 op 3, CR-9 | bound workers' labor input_to hiring firms' output (close) | A-N2, A-2 |
| C-22 | employers.hiring_experienced | asset_value | ambiguous | short; medium | CR-7c, CR-10c, CR-12b | as above; contract (their own restraints) | A-16, A-N2, A-7 |
| C-23 | owners.restraining_firms | asset_value | decrease | short (from 3 February 2025, mostly by 12 June 2025) | CR-7c, CR-10c, CR-8b | contract (the restraint as a right held under the employment contract) | A-15 |
| C-24 | workers.new_hires | wage_rate | ambiguous | medium; long | CR-7b, CR-5c, CR-12b | contract (employment contract terms) | A-7, A-5, A-15 |
| C-25 | workers.unbound | wage_rate (same fields) | ambiguous | medium; long | CR-6, CR-9, CR-12b | same_market_other_segment (bound and unbound workers in a field, close) | A-8, A-3 |
| C-26 | workers.other_fields | wage_rate | increase | medium | CR-9, CR-6 | substitute (labor from the bound fields entering other fields, partial) | chain 1: A-8; chain 2: A-10 |
| C-27 | buyers.services | price_paid (services in the bound fields) | ambiguous | medium; long | CR-9, CR-6, LW-10, CR-12b | exchange; staff labor input_to services (close) | A-3, A-23, A-7 |
| C-28 | buyers.services | search_cost (finding a provider after one's provider changes employer) | decrease | short; medium | CR-3b, CR-9 | exchange (client and provider) | A-17, A-1, A-2 |
| C-29 | sellers (bound fields, Teravel) | number_of_sellers | increase | medium; long | CR-9, CR-7a | same_market_other_segment (spin-offs and incumbents) | A-3, A-2, A-23 |
| C-30 | workers (bound fields, Teravel) | employment | ambiguous | medium; long | CR-9, CR-7a, CR-12b | input_to (labor to services); across_border (Mossgrave) | A-22, A-24, A-3, A-23 |
| C-31 | intermediaries.recruiters | quantity_traded (placements of experienced staff) | increase | short; medium | CR-9, LW-10 | complement (placement services with hiring of experienced staff) | A-21, A-1, A-2 |
| C-32 | intermediaries.lawyers | quantity_traded (redrafting, trade-secret and non-solicitation work) | increase | short; medium | CR-9, LW-10 | input_to (legal services to employers' contracting and claims) | chain 1: A-4; chain 2: A-19 |
| C-33 | intermediaries.lawyers | quantity_traded (non-compete enforcement work) | decrease | short; medium; long | CR-9, CR-1 op 1 | input_to (as above) | A-2 |
| C-34 | officials.courts | enforcement_cost (non-compete enforcement suits) | decrease | short; medium; long | CR-1 op 1, CR-4a, CR-8c | contract (suits arise from employment contracts) | A-2 |
| C-35 | officials.courts | enforcement_cost (trade-secret and non-solicitation suits) | increase | short; medium | CR-4, CR-8c | contract (as above) | A-19 |
| C-36 | other_bureau_beneficiaries | enforcement_cost (other Labor Bureau tasks) | decrease | short; medium | CR-8a, CR-3c | shared_facility (the Bureau's fixed budget and staff) | A-18 |
| C-37 | neighboring_jurisdictions (Mossgrave employers) | employment (training-intensive work located in Mossgrave) | increase | medium; long | CR-4 (x: here, y: there), CR-7a | across_border (Halbrook and the Mossgrave bank, close) | A-22 |
| C-38 | neighboring_jurisdictions (Mossgrave) | entry_rate (hiring-intensive firms and start-ups) | decrease | medium; long | CR-4 (x: there, y: here), CR-7a | across_border (close) | A-24 |
| C-39 | neighboring_jurisdictions (Mossgrave employers of cross-river commuters) | wage_rate (paid to Teravel-resident staff) | increase | short; medium | CR-9, CR-7a, CR-6 | across_border (labor market of commuters, close) | A-N3 |
| C-40 | employers.restraining | resources_available_other_uses | decrease | short; medium | CR-8b, CR-3 note, CR-3c | contract (wages, retention pay, deferred pay under existing contracts) | chain 1: A-7, A-2; chain 2: A-1, A-2 |
| C-41 | workers.bound | resources_available_other_uses | increase | short; medium | CR-8b | contract (as above) | chain 1: A-7, A-2; chain 2: A-1, A-2 |

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance premise (CR-12e) | Combined sign |
| --- | --- | --- | --- | --- |
| workers.bound, job_changes to rivals and start-ups, from 2026 | K1 removes the restraint and K4 tells workers (CR-1 op 2, CR-11c, A-1, A-2) | substitute devices: non-solicitation, unvested pay, retention bonuses, long notice under U1-a (C-7, C-8, C-9; A-4, A-10) | Empirical: A-9 (p 0.65), substitutes deter fewer moves than non-competes did | increase (C-2) |
| workers.bound, job_changes to rivals, 3 Feb to 31 Dec 2025 | workers who move late in 2025 because any suit would be pending on 1 January 2026 and decided under the Act (A-N4) | workers who would have moved by buy-out or litigation and now wait (A-14) | None | ambiguous (C-14); per-window comparison in section 8 |
| workers.bound, job_changes to non-rivals and out of field, medium; long | - | moves within the field replace moves out of it (A-8); unvested pay attaches a cost to every departure (A-10) | Not needed | decrease (C-17) |
| workers.trainees, non_wage_compensation (training), medium; long | substitutes restore part of the protection: unvested pay; repayment agreements under U2-b (C-7, C-10) | lost protection of training cost (A-5) | Empirical: A-6 (p 0.7), substitutes do not fully restore it. Under U2-a the (+) chain is smaller still | decrease (C-11), under both readings |
| workers.new_hires, wage_rate, medium; long | outside offers from rivals (CR-7b, A-7) | the restraint is no longer a term the employer receives, and its value (A-15) and the training cost it protected (A-5) leave the range of acceptable pay (CR-5c) | None | ambiguous (C-24) |
| workers.bound (current), wage_rate, short; medium | outside offers and retention counteroffers (A-7) | none derived: existing workers already gave the restraint, and their pay is not lowered by its voiding (CR-3b, CR-6 on existing contracts) | Not needed | increase (C-3) |
| workers.unbound, wage_rate, medium; long | new firms' demand for experienced staff (A-3) | bound workers who would have left the field stay in it (A-8) | None | ambiguous (C-25) |
| buyers.services, price_paid, medium; long | higher pay for experienced staff, a material part of cost (A-7, A-23) | entry by spin-offs adds supply not offset elsewhere (A-3, A-23) | None | ambiguous (C-27) |
| workers (bound fields, Teravel), employment, medium; long | spin-off entry (A-3, A-23); hiring-intensive firms and founders locate in Teravel (A-24) | training-intensive work moves to Mossgrave (A-22) | None | ambiguous (C-30) |
| employers.hiring_experienced, asset_value, short; medium | lower search cost and no buy-outs when hiring bound workers (A-16, A-N2) | loss of their own restraints; higher pay for experienced staff (A-7) | None | ambiguous (C-22) |
| employers.restraining, term_prevalence (long notice periods) | U1-a: substitute into a preserved form | U1-b: void, and those in the counterfactual are removed (A-N1) | Per reading, not combined | U1-a: increase; U1-b: decrease (C-9) |
| intermediaries.lawyers, quantity_traded | redrafting, trade-secret and non-solicitation work | non-compete enforcement work | Different segments of legal work; not netted (CR-12c) | C-32 increase; C-33 decrease |
| officials.courts, enforcement_cost | trade-secret and non-solicitation suits (A-19) | non-compete suits (A-2) | Different kinds of suit; not netted (CR-12c) | C-35 increase; C-34 decrease |
| sellers.prospective, entry_rate, medium; long | spin-offs (A-3); location choice (A-24) | - | Independent chains, either suffices (CR-12d) | increase (C-4) |

No chains cancel exactly by construction (CR-12f).

## 8. Time structure

- **Announcement window (3 February to 31 December 2025).** The bill was expected from its introduction with the governor's support, more firmly from enactment on 12 June. Three timing effects follow (CR-10a).
  - *Moves by bound workers.* Workers who would have moved in the window by buy-out or litigation wait until 2026 (A-14); others move late in 2025 because a suit filed then would be pending on 1 January 2026 and decided under the Act (A-N4). The window's sign is ambiguous (C-14). From 2026 the sign is increase (C-2). The moves made in 2026 by those who waited are part of C-2. Per window: 2025 ambiguous; 2026 on, increase.
  - *Buy-outs.* Both chains reduce buy-out payments in the window, and from 2026 there is nothing to buy out (C-15, C-16).
  - *Capitalization.* The expected loss of yield to firms that relied on restraints is capitalized as the Act becomes likely: partly from 3 February, mostly by 12 June 2025 (CR-7c, CR-10c; C-23). It is borne by whoever owned those firms then, not by later buyers.
  - *Lobbying* begins at introduction (C-13).
  - *Redrafting* into preserved forms can start in 2025 (C-7, C-5); both windows have more of it than the counterfactual, so this is a path note, not a timing shift (CR-12h).
- **Retroactivity.** K1 applies to existing contracts and pending suits, so the transfer from employers to bound workers (CR-8b; C-40, C-41) happens at once on 1 January 2026, not as contracts expire. K4's deadline (1 March 2026) dates the information to workers (CR-11c).
- **Stocks (CR-10b).** The stock of trained workers in the bound fields changes only through training flows. Less employer-funded training (C-11) lowers the flow from the medium term on, and the effect on the stock grows over the long run. Firms' client books move gradually as clients follow departing providers (C-20, C-28). Relocation of training-intensive work to Mossgrave (C-18, C-37) and location choices of new firms (C-38) happen as leases and investments come up for renewal: medium to long run.
- **Expectations.** The Act has no expiry. If employers expect amendment through lobbying (C-13), long-payback responses (relocation, partnership restructuring) are held back; this is not signed.
- **Persistence.** The `persistence` field applies to repeals only; the Act is not a repeal and has no expiry. The 2025 window effects (C-14, C-15 in 2025, C-16 in 2025) exist only during the transition and would be `n/a`.

## 9. Opportunity costs

Each is written as a signed change in a variable.

| ID | Actor class | Variable | Sign | What is given up | Rules |
| --- | --- | --- | --- | --- | --- |
| C-5 | employers.restraining | compliance_cost (K4 notices; redrafting into preserved forms) | increase | Staff and legal time that would have served other ends | CR-1 op 3, CR-8c |
| C-6 | officials.labor_bureau | enforcement_cost (K4 and K5 tasks) | increase | Bureau time and money used up | CR-1, CR-8c |
| C-11 | workers.trainees | non_wage_compensation (employer-funded general training) | decrease | Training exchanged for a restraint that no longer happens: a gain both parties expected (CR-5a) | CR-4, CR-5a |
| C-13 | organized_interests | lobbying_effort | increase | Members' time and dues spent seeking to change or keep the Act | CR-4, CR-8c |
| C-32 | intermediaries.lawyers | quantity_traded (redrafting, trade-secret and non-solicitation work) | increase | Employers' spending on redrafting and new claims, used up | CR-8c |
| C-35 | officials.courts | enforcement_cost (trade-secret and non-solicitation suits) | increase | Court time | CR-8c |
| C-36 | other_bureau_beneficiaries | enforcement_cost (other Labor Bureau tasks) | decrease | Other enforcement the Bureau would have done with the same budget | CR-8a, CR-3c |
| C-40 | employers.restraining | resources_available_other_uses | decrease | Higher pay and retention pay to keep staff; deferred pay no longer forfeited | CR-8b, CR-3c |

CR-8b's symmetry is applied to every transfer: the voided restraints (C-40) are matched by the gain to bound workers (C-41); buy-out receipts lost by restraining employers (C-15) are matched by buy-out outlays saved by hiring firms (C-16); the capital loss to owners of restraining firms (C-23) is borne by those who held the firms when the Act became expected, and later buyers pay a lower price. The court-time saved on non-compete suits (C-34) is a release of means, not a gain to a named class: who uses the court time freed is not derived.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
| --- | --- | --- | --- | --- | --- |
| A-1 | Non-competes deter some bound workers from moves to rivals or start-ups they would otherwise make. | binding | 0.8 | 17% bound; about 400 suits a year and many more letters; surveys of workers citing a non-compete as the reason for declining an offer. | These consequences fail or lose this chain: C-2, C-20, C-28, C-31, C-40, C-41. |
| A-2 | Employers stop enforcing, and workers learn that the clause is void (K4 notices, damages and fee-shifting). | enforcement | 0.8 | K4 and K5 text; experience with mandated notices. | These consequences fail or lose this chain: C-1, C-2, C-3, C-4, C-5, C-20, C-21, C-28, C-29, C-31, C-33, C-34, C-40, C-41. |
| A-3 | Some bound workers have plans to start a firm in their field that the non-compete blocks. | binding | 0.7 | Founder surveys; spin-off rates in comparable places with and without enforcement. | These consequences fail or lose this chain: C-4, C-25, C-27, C-29, C-30. |
| A-4 | For many employers, reshaping restraints into the preserved forms costs less than the protection it restores. | other | 0.85 | Current use of non-solicitation and deferred pay; legal fees for redrafting. | These consequences fail or lose this chain: C-5, C-7, C-9, C-10, C-32. |
| A-5 | In a material share of trainee jobs, the non-compete protected the employer's recovery of the cost of general training. | other | 0.7 | Training spending by field; how often non-competes go with funded training; employer surveys. | These consequences fail or lose this chain: C-10, C-11, C-24. |
| A-6 | Substitute restraints (non-solicitation, unvested pay, and under U2-b repayment agreements) do not fully restore that protection. | substitutability | 0.7 | Repayment capped at actual cost and hard to collect; non-solicitation does not stop a worker serving a rival's clients. | These consequences fail or lose this chain: C-11 (becomes ambiguous). |
| A-7 | Some bound workers are paid less than a rival would pay them. | other | 0.75 | Pay of movers before and after moves; pay gaps between bound and unbound workers in the same job. | These consequences fail or lose this chain: C-3, C-22, C-24, C-27, C-40, C-41. |
| A-8 | In the counterfactual, some bound workers change employer by leaving their field. | mobility | 0.6 | Field-switching rates of workers with non-competes against those without. | These consequences fail or lose this chain: C-17, C-25, C-26. |
| A-9 | Substitute retention devices deter fewer moves to rivals than non-competes did (dominance premise). | other | 0.65 | Mobility to competitors after non-competes stopped being enforced in comparable places; cost to employers of retention pay. | These consequences fail or lose this chain: C-2 (becomes ambiguous). |
| A-10 | Employers expand unvested deferred pay and retention bonuses. | other | 0.6 | Current plan design; benefits consultants' advice after the Act. | These consequences fail or lose this chain: C-8, C-17, C-26. |
| A-11 | Courts accept bona fide partnership buy-ins as within K2, and practices use them. | other | 0.6 | Rulings under the 1998 partnership statute; how common partner tracks already are. | These consequences fail or lose this chain: C-12. |
| A-12 | Token equity grants, made only to bring a restraint within K2, qualify. | other | 0.3 | The same rulings required a substantial interest. | No reported consequence rests on it (see Not reported). |
| A-13 | Employers' associations, worker groups and start-up associations can organize at a cost below their stake. | other | 0.8 | Existing chambers of commerce, bar and medical associations, start-up councils; the 2025 hearings. | These consequences fail or lose this chain: C-13. |
| A-14 | Some bound workers would have moved to rivals in the second half of 2025, by buy-out or litigation, and can wait. | expectations | 0.6 | Monthly counts of suits and settlements; how long offers stay open. | These consequences fail or lose this chain: C-14, C-15, C-16. |
| A-15 | Non-competes protected a material part of net trainers' expected yield. | other | 0.7 | Share prices and deal values of firms relying on restraints, around the votes; how central trained staff and client books are to their earnings. | These consequences fail or lose this chain: C-23, C-24. |
| A-16 | Some firms hire more trained staff than they train. | other | 0.8 | Hiring records by experience level. | These consequences fail or lose this chain: C-22. |
| A-17 | Non-solicitation bars only contact the worker initiates; clients may follow a provider on their own. | other | 0.7 | K3(b) says "solicit"; common-law meaning of solicitation. | These consequences fail or lose this chain: C-20, C-28. |
| A-18 | The Labor Bureau's budget is not raised for the new task. | revenue_use | 0.7 | No appropriation in the Act; the next budget cycle. | These consequences fail or lose this chain: C-36 (the payers become taxpayers or recipients of other spending). |
| A-19 | Employers turn to trade-secret and non-solicitation claims against departing staff. | substitutability | 0.7 | Claim filings in places that stopped enforcing non-competes. | These consequences fail or lose this chain: C-32, C-35. |
| A-20 | Employers keep writing void clauses and rely on workers not knowing. | enforcement | 0.35 | K4 notices and K5 damages make it costly. | No reported consequence rests on it (see Not reported). |
| A-21 | Recruiters handle a material share of experienced hires in these fields. | other | 0.7 | Placement data. | These consequences fail or lose this chain: C-31. |
| A-22 | Some employers locate new training-intensive work in Mossgrave because restraints are enforceable there. | mobility | 0.55 | Distance across the river; existing two-state employers. | These consequences fail or lose this chain: C-18, C-30, C-37. |
| A-23 | Spin-off entry adds supply that is not offset elsewhere, and experienced staff pay is a material part of these services' costs. | other | 0.6 | Cost structure of salons, clinics and advisory firms; spin-off counts. | These consequences fail or lose this chain: C-27, C-29, C-30. |
| A-24 | Firms that rely on hiring experienced staff, and founders, prefer to locate where staff are mobile. | mobility | 0.6 | Location choices of start-ups and hiring-intensive firms across enforcement boundaries. | These consequences fail or lose this chain: C-4 (chain 2), C-30, C-38. |
| A-25 | Mossgrave-bound workers escape their restraints by taking Teravel jobs. | other | 0.4 | Mossgrave courts may still enforce against them. | No reported consequence rests on it (see Not reported). |
| A-N1 | In the counterfactual, some Teravel employment contracts contain paid notice periods of six months or more, and some contain training repayment agreements. | other | 0.7 | NEW. U1 and U2 are raised in the record because such terms exist; garden leave is common in finance, repayment agreements in funded training. | These consequences fail or lose this chain: C-9 (U1-b sign), C-10 (U2-a sign). |
| A-N2 | In the counterfactual, firms that hire a bound worker from a rival bear litigation risk, demand letters or buy-out payments. | other | 0.85 | NEW. About 400 suits a year and many more letters; A-14 refers to buy-outs. | These consequences fail or lose this chain: C-21, C-22. |
| A-N3 | Some Teravel residents working in Mossgrave rank a Teravel job close enough to their Mossgrave job that freedom from a restraint changes their choice. | mobility | 0.6 | NEW. 60,000 commuters each way; same fields on both banks; short distance. | These consequences fail or lose this chain: C-19, C-39. |
| A-N4 | Some bound workers who would not have moved in 2025 in the counterfactual move late in 2025, because a suit filed against them would still be pending on 1 January 2026 and be decided under the Act. | expectations | 0.55 | NEW. K1 applies to pending cases; enforcement suits take months; offers stay open (A-14 evidence). Preliminary injunctions before 1 January 2026 limit it. | These consequences fail or lose this chain: C-14 (becomes decrease). |

**Not reported** (an assumption below 0.5):
- Token equity grants used to bring restraints within K2, `reclassification` increase (CR-4, x: covered form, y: exempt form): needs A-12 (p 0.3).
- Employers keep writing void clauses (`legal_breach` increase), worker suits under K5 and Labor Bureau penalties (`non_tax_receipts` increase), CR-4 (x: comply, y: violate): needs A-20 (p 0.35). The direction is a priori (CR-4a: K5 makes no employer more willing to violate), the scale is not.
- Mossgrave-bound workers take Teravel jobs to escape their restraints (`job_changes` increase for Mossgrave workers; Mossgrave employers' restraints lose value): needs A-25 (p 0.4).

### Final check before the report

1. **Uncombined chains.** Every (class, variable, horizon) reached by more than one chain is in section 7. Bound workers' moves to rivals combine the Act and the substitutes (dominance A-9). Training combines the lost protection and the substitutes (dominance A-6). The 2025 window, new hires' pay, unbound workers' pay, service prices, employment in the bound fields and hiring firms' asset values have opposing chains and no dominance premise: ambiguous. Current bound workers' pay has no derived opposing chain (existing workers already gave the restraint), so it stays increase.
2. **Group signs.** No rule here licenses only "at least one of": each consequence names one variable. CR-6's displaced pressure is split into named terms, each with its own premise (C-7, C-8, C-9, C-10).
3. **Baseline.** Every sign is against Teravel in the same period with reasonable non-competes still enforced. C-11 is less training than in that world, not less than before 2025.
4. **Worse off is not poorer.** Restraining employers' `resources_available_other_uses` falls (C-40) because they keep employing the workers at higher pay, and pay deferred pay they cannot avoid once forfeiture is void. Trainees who lose training are worse off (CR-3a), but no `resources_available_other_uses` sign is given for them.
5. **Timing shifts.** Moves by bound workers are signed per window (C-14 for 2025, C-2 from 2026). Buy-outs fall in both windows. Redrafting is higher in both windows: a path note.
6. **Both sides of every transfer.** Voided restraints: C-40 and C-41. Buy-outs: C-15 and C-16. Capital loss: C-23 (sellers at the time; later buyers pay less). Bureau task: C-6 and C-36.
7. **Every actor class, every core rule.** See the sweep at the head of section 5. CR-7c was applied to restraining firms (C-23) and hiring firms (C-22); no capitalization is derived for Mossgrave land or Halbrook offices (a premise on fixed supply would be needed).
8. **Unstated premises.** Four premises were added (A-N1 to A-N4). "Some actors at the margin" is carried by A-1, A-3, A-8, A-22, A-24 and A-N3; "can organize" by A-13.

## 11. Report

**The policy:** From 1 January 2026, any term that stops a worker who primarily works in Teravel from working for another person or starting a business after leaving, or penalizes them for it, is void, including terms in existing contracts and in pending suits. Restraints given on selling a business, confidentiality and non-solicitation terms (up to 12 months), notice periods during which the worker stays employed, and forfeiture of unvested pay under plans that apply to every departure remain allowed. Employers must tell affected workers by 1 March 2026. Workers can sue for damages, $5,000 and fees; the Labor Bureau can seek penalties, from its existing budget.

**Visible consequences:** Enforceable non-competes disappear from contracts (C-1). Bound workers move to rivals and start their own firms more often from 2026 (C-2, C-4), and current bound workers are paid more (C-3). Employers bear the cost of notices and redrafting (C-5); the Labor Bureau takes on a new task (C-6).

**Invisible consequences:**
- *Employers that held restraints:* They switch to non-solicitation, confidentiality and unvested-pay terms (C-7), pay more deferred pay and retention bonuses (C-8), and lose clients who follow departing staff (C-20). Their owners bore a capital loss when the Act became likely in 2025 (C-23). They have less to spend on other things (C-40), and the buy-out payments they used to receive stop (C-15). Some move training-intensive work to Mossgrave (C-18, C-37). Group practices restructure restraints into partnership buy-ins (C-12).
- *Workers:* Bound workers gain what employers lose (C-41). They leave their field, or leave for non-competing employers, less often (C-17), so workers in other fields face fewer newcomers (C-26). Trainees receive less employer-funded general training (C-11). Teravel residents working in Mossgrave move to Teravel jobs (C-19), and Mossgrave employers pay more to keep them (C-39).
- *Hiring firms and intermediaries:* Firms that hire experienced staff search more cheaply and pay no buy-outs (C-21, C-16). Recruiters place more experienced staff (C-31). Lawyers do more redrafting and trade-secret work and less non-compete enforcement (C-32, C-33). Courts hear fewer non-compete suits and more trade-secret and non-solicitation suits (C-34, C-35).
- *Clients and markets:* Clients can keep their provider when the provider moves (C-28); there are more sellers in the bound fields (C-29). Mossgrave sees fewer new hiring-intensive firms (C-38).
- *Labor Bureau:* Other enforcement work is cut to fund the new task (C-36).
- *Organized interests:* Employers' associations, worker groups and start-up associations spend more on lobbying from the bill's introduction (C-13).

**Ambiguous effects:**
- Moves by bound workers during 2025 (C-14): some wait for the Act; others move early because suits would be decided under it.
- Pay of new hires (C-24): better outside offers push it up; the loss of a restraint the employer valued, and of the protection for training, pushes it down.
- Pay of unbound workers in the same fields (C-25): new firms' demand pushes it up; former field-leavers staying in the field push it down.
- Prices of services in the bound fields (C-27): entry pushes them down; higher staff pay pushes them up.
- Employment in the bound fields in Teravel (C-30): spin-offs and firms choosing Teravel push it up; training-intensive work moving to Mossgrave pushes it down.
- Asset values of firms that hire experienced staff (C-22).
In each case what would decide it is the size of the opposing effects, which this method cannot measure.

**Key conditions:** Employers comply and workers learn the clause is void (A-2, 0.8); substitutes deter fewer moves than non-competes did (A-9, 0.65), which decides C-2; substitutes do not fully restore protection of training (A-6, 0.7), which decides C-11; some bound workers are underpaid relative to rivals' offers (A-7, 0.75). The Mossgrave effects rest on A-22 (0.55) and A-24 (0.6). Four premises were added: long notice periods and repayment agreements exist in the counterfactual (A-N1, 0.7), hiring firms bore litigation risk and buy-outs (A-N2, 0.85), some commuters are at the margin between banks (A-N3, 0.6), and some workers move early because of the pending-cases clause (A-N4, 0.55).

**What this analysis cannot say:** How large any effect is; whether bound workers' gains outweigh employers' and trainees' losses; whether total output or innovation rises (knowledge carried by moving workers is non-rival, so CR-8 cannot sign it); and whether the policy is good. Health and safety effects (for example on patients of clinics) are out of scope.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C-1 | employers.restraining | term_prevalence (enforceable non-compete and forfeiture-for-competition terms) | decrease | short; medium; long | visible | B | CR-1 (op 1: K1 removes the option of an enforceable restraint; counterfactual law: reasonable restraints enforced); CR-5a (the exchange of a restraint for pay, training or a job no longer takes place); CR-4 (x: comply, y: insert a void term; K5 makes y worse, A-2) | A-2 |
| C-2 | workers.bound | job_changes (to rivals and own start-ups, from 1 January 2026) | increase | short; medium; long | visible | B | CR-1 (op 2: the move is now open; op 3: litigation risk and forfeiture removed); CR-11c (K4 notices tell workers the clause is void, A-2); CR-4 mirror (x: stay, y: move; y made better, so workers deterred by the restraint, A-1, move); CR-12b and CR-12e (substitutes push the other way; dominance premise A-9) | A-1, A-2, A-9 |
| C-3 | workers.bound | wage_rate | increase | short; medium | visible | B | CR-7b, 0.7 clarification (a policy that makes a means mobile gives the gain to its owner); CR-5c (rivals' offers move the range of acceptable pay, A-7); CR-6 (bidding by rivals and counteroffers move pay toward the clearing level); no opposing chain for current workers, who already gave the restraint | A-7, A-2 |
| C-4 | sellers.prospective (bound fields, Teravel) | entry_rate | increase | medium; long | visible | B | Chain 1: CR-1 (op 2: founding is open to bound workers), CR-4 (x: stay employed, y: found; A-3). Chain 2: CR-4 (x: locate in Mossgrave, y: in Teravel; A-24), CR-7a. CR-12d: either chain suffices | chain 1: A-3, A-2; chain 2: A-24 |
| C-5 | employers.restraining | compliance_cost (K4 notices; redrafting into preserved forms) | increase | short | visible | B | CR-1 (op 3: K4 attaches a notice duty); CR-4 (x: void form, y: preserved form, A-4) requires redrafting; CR-8c (resources spent on complying are used up) | A-2, A-4 |
| C-6 | officials.labor_bureau | enforcement_cost (K4 and K5 tasks: guidance, monitoring, suits) | increase | short; medium | visible | A | CR-1 (K5 assigns the Bureau a task; the Attorney General has already drafted guidance); CR-8c (resources spent on administering and enforcing are used up) | none |
| C-7 | employers.restraining | term_prevalence (non-solicitation, confidentiality and unvested-pay terms) | increase | short; medium | invisible | B | CR-4 (x: the void form, y: a preserved form under K3(a), (b), (d); x removed, so y is chosen where it costs less than the protection it restores, A-4); CR-6 (pressure displaced to terms not regulated); CR-10a (redrafting starts once the Act is expected) | A-4 |
| C-8 | workers.bound | non_wage_compensation (unvested deferred pay and retention bonuses) | increase | short; medium | invisible | B | CR-4 (x: lose the worker to a rival, y: pay to retain); CR-5c (retention pay enters the terms); CR-6 (pressure to keep staff moves to unregulated terms; A-10) | A-10 |
| C-9 | employers.restraining | term_prevalence (paid notice periods of six months or more) | U1-a: increase; U1-b: decrease | short; medium | invisible | B | U1-a: CR-1 (op 2: K3(c) keeps the form open), CR-4 (x: void restraint, y: long paid notice; A-4), CR-6. U1-b: CR-1 (op 1: K1 voids such terms; K5 penalizes inserting them), so those in the counterfactual (A-N1) are removed | A-4, A-N1 |
| C-10 | employers.trainers | term_prevalence (training repayment agreements) | U2-a: decrease; U2-b: increase | short; medium | invisible | B | U2-a: CR-1 (op 1: void as a penalty; K5 penalizes inserting them), so those in the counterfactual (A-N1) are removed. U2-b: CR-4 (x: void restraint, y: repayment agreement), CR-6 (pressure to protect training cost, A-5, moves to this term; A-4) | A-4, A-5, A-N1 |
| C-11 | workers.trainees | non_wage_compensation (employer-funded general training) | decrease | medium; long | invisible | B | CR-9 (contract: the restraint protected the training, A-5); CR-4 (x: fund general training, y: do not; x made worse, so employers for whom it was narrowly worth it stop); CR-5a (the exchange of training for a restraint does not take place); CR-12b and CR-12e (substitutes restore part; dominance premise A-6); under U2-a the substitute is smaller, so the sign holds under both readings | A-5, A-6 |
| C-12 | employers.group_practices | reclassification (restraints moved into partnership buy-ins under K2) | increase | medium | invisible | B | CR-4 (x: covered form, an employee restraint; y: exempt form, a restraint given on buying in as a partner; x removed, so practices for whom the buy-in costs less than the restraint is worth switch; A-11) | A-11 |
| C-13 | organized_interests (employers' associations; worker groups and start-up associations) | lobbying_effort | increase | short (from 3 February 2025); medium | invisible | B | CR-4 (x: accept, y: lobby; the bill creates a concentrated stake on both sides; A-13); CR-10a (lobbying starts at introduction); CR-8c (resources spent lobbying are used up) | A-13 |
| C-14 | workers.bound | job_changes (to rivals, 3 February to 31 December 2025) | ambiguous | short (announcement window) | invisible | B | CR-12b: (−) CR-10a and CR-4 (x: move now by buy-out or suit, y: wait until 2026; y made better, A-14); (+) CR-10a and CR-4 (x: stay, y: move late in 2025; a suit would be pending on 1 January 2026 and decided under the Act, A-N4). No dominance premise. Persistence n/a (transition only) | A-14, A-N4 |
| C-15 | employers.restraining | side_payments (buy-out receipts for releasing bound workers) | decrease | short (from 2025); medium | invisible | B | CR-10a (in 2025 workers wait instead of buying out, A-14); CR-1 (op 1: from 2026 there is no enforceable restraint to buy out of); CR-8b (receipts matched by C-16) | A-14 |
| C-16 | employers.hiring_experienced | side_payments (buy-out outlays to hire bound workers) | decrease | short (from 2025); medium | invisible | B | CR-8b (the other side of C-15); CR-1 (op 3: the payment attached to hiring a bound worker is removed) | A-14 |
| C-17 | workers.bound | job_changes (to non-competing employers and out of the field) | decrease | medium; long | invisible | B | Chain 1: CR-4 (x: leave the field, y: move within it; y now open, so field-switchers, A-8, move within it). Chain 2: CR-4 (unvested pay under K3(d) attaches a cost to every departure, A-10; CR-4b). CR-12a: same sign; CR-12d: either chain suffices | chain 1: A-8; chain 2: A-10 |
| C-18 | employers.training_intensive (Teravel) | employment (training-intensive work located in Teravel) | decrease | medium; long | invisible | B | CR-4 (x: locate new training-intensive work here, y: across the river; x made worse by K1, A-22); CR-7a (means move to the higher yield) | A-22 |
| C-19 | workers.cross_river_commuters | job_changes (from Mossgrave to Teravel employers) | increase | short; medium | invisible | B | CR-4 (x: a Mossgrave job with an enforceable restraint, y: a Teravel job without one; y made better; A-N3) | A-N3 |
| C-20 | employers.restraining | quantity_traded (client accounts served) | decrease | short; medium | invisible | B | CR-9 (exchange: clients and providers); CR-4 applied to clients (x: stay with the firm, y: follow the provider; y now open because the provider may serve them, A-1, A-2, and non-solicitation bars only contact the worker initiates, A-17) | A-17, A-1, A-2 |
| C-21 | employers.hiring_experienced | search_cost (hiring experienced staff) | decrease | short; medium | invisible | B | CR-1 (op 3: litigation risk and letters removed from hiring bound workers, A-N2); CR-9 (relation: bound workers' labor input_to hiring firms) | A-N2, A-2 |
| C-22 | employers.hiring_experienced | asset_value | ambiguous | short; medium | invisible | B | CR-12b: (+) CR-7c and CR-10c (cheaper hiring, C-21, C-16, raises expected yield for net hirers, A-16, A-N2); (−) CR-7b (the gain from mobility goes to workers: pay for experienced staff rises, A-7) and loss of their own restraints. No dominance premise | A-16, A-N2, A-7 |
| C-23 | owners.restraining_firms | asset_value | decrease | short (from 3 February 2025, mostly by 12 June 2025) | invisible | B | CR-8b, 0.7 clarification (voiding a contract right is a transfer from its holder); CR-7c (the expected loss of yield, A-15, is borne by whoever owns the firm when it becomes expected, partly at introduction and mostly at enactment); CR-10c | A-15 |
| C-24 | workers.new_hires | wage_rate | ambiguous | medium; long | invisible | B | CR-12b: (+) CR-7b and CR-5c (rivals' offers raise the range, A-7); (−) CR-5c (the restraint, which the employer valued, A-15, and which protected training cost, A-5, is no longer a term the employer receives, so the range of pay it accepts moves down). No dominance premise | A-7, A-5, A-15 |
| C-25 | workers.unbound | wage_rate (same fields) | ambiguous | medium; long | invisible | B | CR-12b: (−) CR-9 and CR-6 (bound workers who would have left the field stay in it, A-8, adding to supply in the field); (+) CR-9 and LW-10 (new firms, A-3, add demand for experienced staff). No dominance premise | A-8, A-3 |
| C-26 | workers.other_fields | wage_rate | increase | medium | invisible | B | CR-9 (substitute: labor from the bound fields entering other fields); CR-6 (fewer entrants, C-17, at each wage moves the wage up). Chain 1: A-8; chain 2: A-10 (CR-12d). Depth 3 | chain 1: A-8; chain 2: A-10 |
| C-27 | buyers.services | price_paid (services in the bound fields) | ambiguous | medium; long | invisible | B | CR-12b: (−) CR-9 and CR-6 (spin-off entry adds supply not offset elsewhere, A-3, A-23); (+) CR-9 and LW-10 (higher pay for experienced staff, C-3, is a material part of cost, A-7, A-23). No dominance premise | A-3, A-23, A-7 |
| C-28 | buyers.services | search_cost (finding a provider after one's provider changes employer) | decrease | short; medium | invisible | B | CR-3b (an option is added: follow the provider); CR-9 (exchange); A-17 (the client may follow on their own initiative) | A-17, A-1, A-2 |
| C-29 | sellers (bound fields, Teravel) | number_of_sellers | increase | medium; long | invisible | B | CR-9 (same_market_other_segment: spin-offs, C-4, join incumbents); CR-7a; not offset by exit (A-23) | A-3, A-2, A-23 |
| C-30 | workers (bound fields, Teravel) | employment | ambiguous | medium; long | invisible | B | CR-12b: (+) CR-9 and CR-7a (spin-offs, A-3, A-23; firms locating in Teravel, A-24); (−) CR-4 and CR-7a (training-intensive work moves to Mossgrave, A-22). No dominance premise | A-22, A-24, A-3, A-23 |
| C-31 | intermediaries.recruiters | quantity_traded (placements of experienced staff) | increase | short; medium | invisible | B | CR-9 and LW-10 (complement: placement services follow the number of movable experienced workers, C-2; A-21) | A-21, A-1, A-2 |
| C-32 | intermediaries.lawyers | quantity_traded (redrafting, trade-secret and non-solicitation work) | increase | short; medium | invisible | B | CR-9 and LW-10 (input_to: legal services follow employers' redrafting, C-7, A-4, and new claims, A-19); CR-8c. CR-12d: either chain suffices | chain 1: A-4; chain 2: A-19 |
| C-33 | intermediaries.lawyers | quantity_traded (non-compete enforcement work) | decrease | short; medium; long | invisible | B | CR-1 (op 1: enforcement removed); CR-9 (input_to: demand for enforcement work follows enforcement, A-2) | A-2 |
| C-34 | officials.courts | enforcement_cost (non-compete enforcement suits) | decrease | short; medium; long | invisible | B | CR-1 (op 1; pending cases decided under the Act); CR-4a (no employer files a suit it cannot win because of the change, A-2); CR-8c | A-2 |
| C-35 | officials.courts | enforcement_cost (trade-secret and non-solicitation suits) | increase | short; medium | invisible | B | CR-4 (x: a non-compete suit, now void; y: a trade-secret or non-solicitation claim, A-19); CR-8c (court time used up) | A-19 |
| C-36 | other_bureau_beneficiaries | enforcement_cost (other Labor Bureau tasks) | decrease | short; medium | invisible | B | CR-8a (the Bureau's means directed to K4 and K5, C-6, are withdrawn from its other tasks, since the budget is not raised, A-18); CR-3c | A-18 |
| C-37 | neighboring_jurisdictions (Mossgrave employers) | employment (training-intensive work located in Mossgrave) | increase | medium; long | invisible | B | CR-4 (x: Teravel, y: Mossgrave, A-22); CR-7a; relation across_border | A-22 |
| C-38 | neighboring_jurisdictions (Mossgrave) | entry_rate (hiring-intensive firms and start-ups) | decrease | medium; long | invisible | B | CR-4 (x: Mossgrave, y: Teravel; y made better for firms that rely on mobile staff, A-24); CR-7a; relation across_border | A-24 |
| C-39 | neighboring_jurisdictions (Mossgrave employers of cross-river commuters) | wage_rate (paid to Teravel-resident staff) | increase | short; medium | invisible | B | CR-9 (across_border: Mossgrave employers compete with Teravel employers for the same commuters, C-19); CR-7a and CR-6 (to keep them, pay moves up; A-N3) | A-N3 |
| C-40 | employers.restraining | resources_available_other_uses | decrease | short; medium | invisible | B | CR-8b, 0.7 clarification (voiding a contract right is a transfer from its holder); CR-3 note (they keep employing the workers and pay more to keep them, A-7; deferred pay no longer forfeited is a sum they cannot avoid, A-1); CR-3c. CR-12d: either chain suffices | chain 1: A-7, A-2; chain 2: A-1, A-2 |
| C-41 | workers.bound | resources_available_other_uses | increase | short; medium | invisible | B | CR-8b (the other side of C-40: higher pay, A-7, and deferred pay kept on joining a competitor, A-1) | chain 1: A-7, A-2; chain 2: A-1, A-2 |

## Gaps found

**(a) Steps no core rule covers.**
- GAP-034-C1: whether total output or innovation in the bound fields rises when workers carry knowledge to rivals and spin-offs. Knowledge is non-rival, so CR-8 cannot sign it (CR-8, non-rival clarification), and no other core rule does. The analysis records the moves (C-2, C-4) but cannot say whether the knowledge they carry adds to production overall.
- GAP-034-C2: cumulative location effects. A-24 says firms that rely on mobile staff prefer to locate where staff are mobile; once more such firms locate in Teravel, staff have more reason to locate there too, and so on. CR-7a gives the direction of each move, but no core rule covers a self-reinforcing sequence, and the depth limit stops it after one round.

**(b) Core-rule wording that was hard to apply.**
- CR-7, 0.7 clarification on a policy that makes a means mobile: "the gain from its mobility goes to the owner of the means (the worker)". This is clear for workers already bound (C-3), but for new hires CR-5c points the other way: the restraint was a term the employer valued and paid for, so its removal also lowers what the employer will offer (C-24). The clarification does not say whether it covers future contracts or only existing ones.
- CR-6, 0.7 clarification: "terms fixed by existing contracts count as regulated while those contracts last". Most employment is at will and has no fixed term, so it is unclear how long existing pay is "regulated". This mattered for deciding that current bound workers' pay has no opposing chain.
- CR-8, 0.7 clarification on voiding a contract right: the worker's gain is mainly a new option (CR-3b), not means. Mapping it to `resources_available_other_uses` needed the CR-3 note (the employer keeps paying more), and it was unclear whether the voiding itself, before any pay changes, should be signed.
- CR-1 dated operations: the clarification covers operations that start at a future date, not a provision that reaches back to pending suits. The effect of the pending-cases clause on 2025 choices (A-N4) was derived through CR-10a, but CR-1 does not say how to record a retroactive operation.
- CR-12h covers activity raised in every window; here one chain shifts moves later (A-14) and another brings some earlier (A-N4), so the 2025 window has opposing timing chains. The rule does not say whether such a window is a timing shift or an ordinary ambiguity; treated as the latter.

**(c) Vocabulary missing from the ontology.**
- A variable for private litigation and claims (suits filed, demand letters). `enforcement_cost` is defined as the state's spending, so courts' time was used as a proxy (C-34, C-35), and employers' and workers' litigation spending has no variable.
- A variable for where production is located across a boundary (only `cross_border_purchases` exists). C-18 and C-37 use `employment` with the location named.
- A variable for the stock of trained workers (human capital); `non_wage_compensation` covers training received but not the stock it builds.
- Generic actor classes for workers (labor as a factor), courts and private litigants. `factor_owners.specific` was too narrow for workers with general skills.
- Instrument types: `term_prohibition` exists, but there is none for a retroactive voiding of existing contracts, an exemption (K2, K3), a mandated notice (K4) or a private right of action with statutory damages (K5).

## Comparison with the pattern-based analysis

**Summary.** The two versions agree on the main structure of the case. Both find more moves by bound workers to rivals and start-ups, which holds only on the dominance premise A-9. Both find higher pay for workers already bound, more same-field entry, and fewer moves out of the field. Both find employers shifting to the preserved forms and group practices moving restraints into partnership buy-ins. Both record lobbying, cheaper hiring for rivals with an ambiguous effect on their firm values, a capital loss to owners of restraining firms from the announcement, lower search costs for clients, more placements by recruiters, and ambiguous prices to clients. On the Labor Bureau, both record a new enforcement cost and less of its other work on a fixed budget. There are three sign differences.

1. The pattern version signs moves to rivals in late 2025 as a decrease (RS-8). It missed the opposing chain that comes from K1's pending-cases clause, so the core's `ambiguous` is right.
2. The pattern version's location key (C-21) combines a (+) chain that reaches hiring-intensive firms with a (−) chain that reaches training-intensive establishments. The core version correctly splits them.
3. The core version signs one member of the trainee group, employer-funded training, as a decrease. CR-5c and CR-6 give only "at least one margin", and lower trainee pay is an open margin, so this overclaims. The pattern's group sign is the valid form.

The core version records much the pattern version left out:
- buy-outs, on both sides;
- clients lost by restraining employers;
- retention pay;
- the Mossgrave side of relocation;
- lawyers' lost enforcement work;
- the transfer from voiding existing rights, including deferred pay that forfeiture-for-competition clauses would have withheld.

The pattern version was written under catalog 0.6. Several 0.7 additions were drawn largely from this example's own Gaps section, and they explain many of the "V" rows and some of the core-only rows:
- CR-6 on margins that move in opposite directions;
- CR-7 on a policy that makes a means mobile;
- CR-8 on voiding a contract right and on non-rival means;
- the `term_prohibition` instrument and the `term_prevalence` variable;
- the `no_change` and `at_least_one_as_stated` signs;
- PC-18.

On voiding, 0.7 went against the pattern version's proposal. The pattern version proposed a CR-8f saying that voiding a right "does not transfer it". The 0.7 CR-8 clarification says that it does.

The core version made errors of its own:
- C-11 (above).
- C-19 and C-39 (cross-river commuters) rest on a direction that CR-3 does not give, and the class the core defines runs into A-25.
- C-4's second chain widens the entry key into one that A-22 also reaches, and the two are not combined.
- Court disputes over U1, U2 and K2 are omitted.

Counts: M 13, V 8, S 3, OP 16, OC 1.

### Pattern version → core version

| Pattern ID | Matched core ID(s) | Class | Cause | Note |
| --- | --- | --- | --- | --- |
| C-1 | C-2 | M | | Moves to rivals and start-ups from 2026, increase, on A-1, A-2 and A-9. Both combine the substitute devices as the opposing chain and use A-9 as the dominance premise (CR-12b, CR-12e). |
| C-2 | C-5 | M | | Compliance cost (CR-8c). |
| C-3 | C-4 | M | | Same-field entry increase (A-3). The core adds an independent location chain (A-24; CR-12d). That chain widens the key to all new sellers in Teravel, which A-22 reaches in the other direction (see Findings). The spin-off chain alone matches the pattern. |
| C-4 | C-7 | V | | Pattern: `reclassification`. Core: `term_prevalence` of the preserved terms. `term_prevalence` was added in 0.7, partly on this example's Gaps (d). |
| C-5 | C-9 | V | | Both sign U1-a as increase. The pattern gives no U1-b sign because 0.6 had no sign for "no chain under this reading" (its Gaps (d)). The core signs U1-b as a decrease: the long notice periods that exist in the counterfactual (A-N1) are void. That sign is valid under CR-1 operation 1, and the pattern version described the same fall in its Gaps (d) without being able to record it. |
| C-6 | C-10 | V | | Same as C-5 for U2. The pattern gives no U2-a sign. The core's "U2-a: decrease" is valid (CR-1 operation 1, A-N1). |
| C-7 | C-11 (and C-24) | S | E (core) | Pattern: trainees' pay during training, funded training and trainee hires as a group, `at_least_one_decrease`, on A-5 and A-6. Core: funded training alone, `decrease`. CR-5c says the range moves; CR-6 says the pressure reaches at least one open margin, and which margins are used needs a premise per margin. Lower trainee pay is an open margin through which the employer can recover the cost of general training without the restraint, and no premise in the core excludes it. A-5 says the restraint protected recovery; A-6 says substitute restraints do not fully restore it. Neither says pay cannot fall. So training alone is an overclaim (final check 2). The core's own final check item 2 says "no rule here licenses only 'at least one of'". That is wrong: the 0.7 CR-6 clarification on margins in opposite directions uses this very case as its example. **Pattern right.** Under 0.7 the pattern's group could also carry the substitute terms (+) as `at_least_one_as_stated` (PC-18), but with A-6 its three-member `at_least_one_decrease` is valid as it stands. |
| C-8 | C-3 | M | | Bound workers' pay increase (A-7). The pattern measures pay including deferred pay as it vests. The core does not, so its C-3 and its C-8 (more unvested pay) overlap where salary is moved into deferred forms. This affects the definition, not the sign. The core cites the 0.7 CR-7 clarification on mobility, which came from this example's Gaps (b). |
| C-9 | C-17 | V | | Decrease, two chains (A-8, A-10; CR-12d). The core widens the variable to "non-competing employers and out of the field". |
| C-10 | none | OC | J | Total job changes, ambiguous (CR-4b against the deterrent of unvested pay). The core rules give both chains (core C-2, C-17 and C-8), but the core version records no aggregate key. That is defensible under CR-12c, and no scorable claim is lost. |
| C-11 | C-14 | S | E (pattern) | Pattern: moves to rivals, July to December 2025, decrease (RS-8, A-14). Core: 3 February to 31 December 2025, ambiguous. K1 says pending cases are decided under the Act, so a worker who moves late in 2025 and is sued has the suit decided under the new law. That makes the move cheaper than in the counterfactual: CR-10a, and CR-4 with x: stay, y: move now (A-N4, p 0.55, above the cut-off). Both chains are valid and no dominance premise is stated, so the sign is ambiguous (CR-12b). The pattern applied RS-8 one way only and did not read the pending-cases clause. The core's window also starts at introduction (CR-10a), which is right: expectations formed from February. **Core right.** |
| C-12 | C-12 | M | | Partnership buy-ins under K2 (A-11). |
| C-13 | C-13 | M | | Lobbying (A-13). The core dates it from introduction. |
| C-14 | C-35, C-32 | V | | Pattern: employers' `quantity_substitute` (trade-secret and non-solicitation claims), from RS-1. Core: the same claims recorded as court time (C-35) and lawyers' work (C-32), A-19. The core version notes that there is no variable for private litigation (its Gaps (c)). |
| C-15 | C-21 | M | | Rivals' search cost decrease. The core names the premise A-N2: hiring firms bore litigation risk, letters or buy-outs in the counterfactual. The pattern rests this on A-1 alone, but A-1 concerns workers' moves, not what rivals bore. That is a minor hidden premise. |
| C-16 | C-23 | M | | Capital loss to owners of restraining firms, partly from February and mostly by June 2025 (CR-7c, CR-10c, A-15). |
| C-17 | C-22 | M | | Rivals' firm values, ambiguous. |
| C-18 | C-28 | M | | Clients' search cost decrease (A-17). |
| C-19 | C-27 | M | | Prices to clients, ambiguous (entry against labor cost). |
| C-20 | C-31 | M | | Recruiters' placements increase (A-21). |
| C-21 | C-18 (and C-30, C-37, C-38) | S | E (pattern) | Pattern: net trainers' `investment_target` (training-intensive establishments in Teravel), ambiguous, with RS-4 (−, A-22) against CR-7 (+, A-24). Core: training-intensive work in Teravel, decrease (C-18). The pattern's (+) chain does not reach the key. A-24 concerns firms that rely on *hiring* experienced staff, and founders. It does not concern training-intensive establishments of net trainers, which a mobile labor pool makes worse off, not better. The two chains reach different keys, so CR-12b does not apply between them. The core records the (+) chain where it belongs: employment in the bound fields overall (C-30, ambiguous) and Mossgrave entry (C-38). **Core right.** |
| C-22 | C-34, C-35 | V | | Pattern: courts' total `enforcement_cost`, ambiguous. Core: non-compete suits decrease, and trade-secret and non-solicitation suits increase, kept apart under CR-12c. Both forms are defensible. The pattern's (+) chain also includes K5 suits and disputes over U1, U2 and K2. The core omits the reading disputes, though litigation is how U1 and U2 get decided (see Findings). |
| C-23 | C-6 | M | | Labor Bureau's enforcement cost increase. |
| C-24 | C-36 | V | | Other Bureau enforcement decrease (CR-8a, A-18). The core puts it on `other_bureau_beneficiaries`, the pattern on `officials.enforcement`. |
| C-25 | C-1 | V | | Pattern: training-for-restraint exchanges, `quantity_traded` decrease (OC-4, CR-5a). Core: `term_prevalence` of enforceable non-competes decrease, over all restraining employers (CR-1 operation 1, CR-5a). It is the same prevented exchange, recorded over a wider class and with a 0.7 variable. |

### Core-only consequences

| Core ID | Class | Cause | Note |
| --- | --- | --- | --- |
| C-8 | OP | E (pattern) | Bound workers' unvested deferred pay and retention bonuses increase (A-10). The pattern version states A-10 and uses it as the (−) chain in its C-1, C-9 and C-10, but never records the response itself as a consequence. Its C-4 records only the reshaping of terms. |
| C-15 | OP | E (pattern) | Restraining employers' buy-out receipts decrease. The pattern mentions buy-outs (C-11, C-17) but does not record either side (final check 6). |
| C-16 | OP | E (pattern) | Hiring firms' buy-out outlays decrease. This is the other side of C-15 (CR-8b). |
| C-19 | OP | E (core) | Teravel residents working in Mossgrave move to Teravel employers (A-N3). The direction assumes that a Teravel job is now better for them. CR-1 shows that for the worker the Act both adds an option (freedom later) and removes one (selling the restraint for pay or training, CR-5c), and CR-3 then gives no single answer, a point the pattern version made in its section 5. A-N3 assumes the direction rather than establishing it. The class is also defined as "still bound by Mossgrave restraints". For those workers, a competing Teravel job is exactly the escape route that A-25 (p 0.4, not reported) covers. The sign needs a premise that freedom from a future restraint is worth more to them than what the restraint would have bought. |
| C-20 | OP | E (pattern) | Restraining employers lose client accounts to departing staff (CR-9, A-17). The pattern records only the clients' side (C-18). |
| C-24 | OP | J | New hires' pay, ambiguous (CR-5c with both chains). The pattern version handles new trainees in a group (C-7) and does not key all new hires. The key is valid but unsigned. |
| C-25 | OP | J | Unbound workers' pay in the same fields, ambiguous. This is a valid CR-9 key that the pattern version did not examine. Nothing scorable is lost. |
| C-26 | OP | J | Workers in other fields: pay increase, from fewer entrants (A-8, A-10), at depth 3. The derivation is valid (CR-9 and CR-6, CR-12d). It is diffuse, and leaving it out is a choice of depth. |
| C-29 | OP | J | `number_of_sellers` increase. The pattern uses it only as the chain behind RS-13 in its C-19. It restates entry (C-4) as a stock, given A-23. |
| C-30 | OP | J | Employment in the bound fields, ambiguous (spin-offs and A-24 against A-22). This is the key where the pattern's two location chains properly meet (see C-21 above). |
| C-33 | OP | E (pattern) | Lawyers' non-compete enforcement work decreases (CR-9 input_to). The pattern counts the end of these suits only for courts (C-22). |
| C-37 | OP | E (pattern) | Training-intensive work in Mossgrave increases (A-22). This is the other side of relocation. The pattern version lists `neighboring_jurisdictions` as an actor class but records nothing for it. |
| C-38 | OP | E (pattern) | Mossgrave entry of hiring-intensive firms and start-ups decreases (A-24). It is the Mossgrave side of the pattern's (+) location chain. |
| C-39 | OP | E (core) | Mossgrave employers pay more to keep Teravel-resident staff. It rests entirely on C-19, so it falls with it. |
| C-40 | OP | E (pattern) | Restraining employers' `resources_available_other_uses` decrease. Chain 1 is higher pay kept up to hold staff, which is spending they keep making on the burdened option (CR-3 note; A-7). Chain 2 is deferred pay that a forfeiture-for-competition clause would have withheld and that must now be paid, an unavoidable sum. K1 names those clauses expressly. Chain 2 is a payment under CR-8b, and was one under 0.6 as well. So the pattern's final check 4 ("no `resources_available_other_uses` is signed") and its statement that voiding is not a transfer missed a real money transfer. The broader claim that voiding a right is itself a transfer comes from the 0.7 CR-8 clarification. That clarification rejected the pattern version's proposed CR-8f, so on that wider point the pattern was defensible under 0.6. |
| C-41 | OP | E (pattern) | Bound workers' `resources_available_other_uses` increase. This is the other side of C-40 (CR-8b). |

### Findings

- **Pattern overclaims or hides premises.**
  - **RS-8 applied one way (C-11).** RS-8 records moves toward the favorable window. Here, though, the provision on pending cases makes the 2025 window partly favorable too. The pattern version signed only the delay and ignored K1's own text. The cause is the analyst, not RS-8. Even so, RS-8's "Then" would help if it asked for a check of whether the policy also improves the earlier window.
  - **RS-4 location (C-21).** The two chains were combined on a key only one of them reaches. RS-4 itself is sound. The analyst attached a CR-7 chain about hiring-intensive firms to a key about net trainers' establishments.
  - **Rivals' search cost (C-15).** This rests on an unstated premise that rivals bore litigation risk or buy-outs in the counterfactual. The core's A-N2 is that premise.
  - **RS-5 and `reclassification` (C-4 to C-6).** The pattern recorded these as `reclassification`, which cannot express the fall of a term that exists in the counterfactual. The pattern version saw this itself (its Gaps (d)), and 0.7 added `term_prevalence` and `no_change`.
- **Errors in the core version.**
  - (1) C-11 signs one member of a CR-6 group, so its final check 2 is wrong. It should be the pattern's group, or a mixed group under `at_least_one_as_stated` (PC-18 form), unless a premise rules out lower trainee pay.
  - (2) C-19 and C-39 assume a direction that CR-3 does not give, and they conflict with A-25 being below the cut-off.
  - (3) C-4's location chain (A-24) widens the entry key to new sellers in Teravel, which A-22 (training-intensive work locating in Mossgrave) reaches in the other direction. The two are not combined. The spin-off chain alone keeps C-4 an increase if the key is held to same-field spin-offs.
  - (4) Court workload omits litigation over U1, U2 and K2, which is how the readings get decided.
  - (5) C-3 and C-8 overlap because pay is not defined to include vested deferred pay.
  - (6) The aggregate of total job changes is not recorded. That is a judgment call.
- **Errors in the pattern version.**
  - Sign errors: C-11 (missed opposing chain) and C-21 (mis-keyed chain).
  - Omissions: retention pay as a consequence (core C-8); buy-outs on both sides (C-15, C-16); clients lost by employers (C-20); lawyers' enforcement work (C-33); the Mossgrave side of relocation (C-37, C-38); and the deferred-pay transfer under voided forfeiture-for-competition clauses (C-40, C-41).
  - The missing U1-b and U2-a signs on C-5 and C-6 were forced by the 0.6 vocabulary.
- **Limits of the core rules.**
  - No difference here is due to the core rules being unable to derive a valid claim, so there is no K.
  - Both versions meet the same real limit: whether total output or innovation rises when know-how spreads (GAP-034-1, GAP-034-C1). The 0.7 CR-8 clarification on non-rival means now states that this needs a premise; that is a statement of the limit, not a resolution of it.
  - The core version's GAP-034-C2 (self-reinforcing location) is a second, smaller limit.
  - Rules that remain unclear:
    - CR-1's recording note still says a void-contract rule "removes an option for one side and adds one for the other". The pattern version's point that both sides lose the option of agreeing to the term is now built into PC-18 and the CR-6 clarification, but not into CR-1. The core's C-19 error shows the cost.
    - CR-6 on "existing contracts" when employment is at will.
    - Whether the CR-7 mobility clarification covers future contracts.
    - How CR-1 records a retroactive operation on pending cases.
    - Whether CR-12h covers a window with opposing timing chains.
  - This comparison is not a fully independent test of the 0.7 clarifications. CR-6 (opposite margins), CR-7 (mobility), CR-8 (voiding and non-rival means), `term_prohibition`, `term_prevalence`, `no_change`, `at_least_one_as_stated` and PC-18 were all drawn largely from this example's Gaps section, and the core version relies on several of them (C-1, C-3, C-9, C-10, C-23, C-40).
