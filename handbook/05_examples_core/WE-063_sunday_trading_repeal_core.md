# WE-063 / Analysis: Repeal of a ban on Sunday opening for large shops, with a right to refuse Sunday work

Analyst: core-only re-run (Handbook 1.0)  |  Rules: core rules CR-1 to CR-12 only  |  Status: compared

## 1. Policy record

**Hastrow Shop Opening (Sunday Trading) Act 2027.** Hastrow is a state of about 4.3 million people. Since the Shop Hours Act 1961, section 9 has barred shops with more than 280 m² of sales area from opening to customers on Sunday; smaller shops may open at any hours. Of about 24,000 shops, about 1,600 are over 280 m² (640 supermarkets, 190 DIY and garden, 260 furniture and electrical, 510 others; about 112,000 employees). About 10,500 of the 22,400 small shops open on Sunday, which brings about 16% of their weekly sales (20% for convenience stores). The three supermarket chains run about 1,250 convenience formats fitted at 250 to 280 m²; about 1,050 shops are between 250 and 280 m² against 260 between 280 and 310 m². About 58,000 of 205,000 shop workers are in small shops, about 31,000 of whom work some Sundays, mostly under "as rostered" clauses. The retail pay agreement pays Sunday hours at time-and-a-half in shops that open, on both paths. Small town-centre units rent for about 12% more per m² than 300 to 400 m² units. Neighboring Corsland allows Sunday opening; about 700,000 Hastrow residents live within 30 minutes of it and spend about 380 million a year in its shops on Sundays. Online is about 11% of retail; about 18% of residents' online orders are placed on Sundays. Sales tax is 6%. The ban is enforced by municipal trading standards officers (about 30 prosecutions a year, about 1.2 million a year of officer time; fines up to 50,000 per Sunday go to municipal budgets).

| Field | Value | Source sentence |
| --- | --- | --- |
| Jurisdiction (and what lies just outside) | Hastrow; Corsland, which allows Sunday opening, lies within 30 minutes of about 700,000 residents; online sellers | Policy record |
| Announced / enacted / effective / expires | Bill introduced 11 January 2027; passed House 9 April, Senate 22 April; signed 3 May 2027; effective 3 November 2027; no expiry | K3 |
| Enforcement (who, penalties, resources) | Of the ban (counterfactual): municipal officers, fines up to 50,000 per Sunday, about 1.2 million a year. Of K2: complaint to the Employment Tribunal, compensation up to 26 weeks' pay | Policy record; s. 6(4) |
| Counterfactual | Section 9 stays in force and is enforced at about its present level (A-24), contested by both sides (A-15) | Workflow, analyzing a repeal |

| Component | Instrument | Target | Bound | Parameters | Exemptions |
| --- | --- | --- | --- | --- | --- |
| K1 Repeal of the ban | Removal of a `prohibition` | Sunday opening of shops over 280 m² | - | Section 9 repealed from 3 November 2027; no other limit on Sunday hours | - |
| K2 Right to refuse Sunday work | `mandated_contract_term` | Employment contracts of shop workers in shops of any size | Employers of shop workers | s. 6(1): written notice; from one month later the employer may not require Sunday work nor disadvantage the worker; s. 6(4): tribunal, up to 26 weeks' pay; s. 6(5): applies to "every contract of employment of a shop worker in force when this Act comes into force" | - |
| K3 Commencement | - | - | - | 3 November 2027 | - |

Existing rules, unchanged on both paths: the retail pay agreement and its Sunday rate; working-time rules; zoning; the sales tax; Corsland's rules. Counterfactual law for K2: employers may require Sunday work where the contract says "as rostered".

Unclear provisions:
- **U1, who has the right to refuse.** U1-a: s. 6(5) fixes when the section starts; it applies to every shop worker's contract in force at any time from 3 November 2027, including later contracts. U1-b: it applies only to contracts in force on 3 November 2027; later hires, including workers who change employer, have no statutory right. No probability is given to either reading.

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | CR-1 operations | Core rules applied |
| --- | --- | --- | --- | --- |
| K1 Repeal | triangular (removes a prohibited exchange) | Yes: some large shops expect Sunday opening to pay (A-1), and the ban is enforced on the counterfactual path (A-24) | 2 (adds the option 'open on Sunday' for shops over 280 m², dated 3 November 2027); removes the risk of fines attached to it (3); for buyers, adds the option of a Sunday trip to a large shop | CR-3b, CR-4, CR-5, CR-7c, CR-9, CR-10 |
| K2 Right to refuse | triangular (mandated term) | Yes where workers object (A-8) | For employers: 1 (removes the option of requiring Sunday work from an objecting worker) and 3 (tribunal risk attached to disadvantaging them). For workers: 2 (adds the option of refusing). U1-a: for all shop workers' contracts at any time; U1-b: only for contracts in force on 3 November 2027, a dated operation that lapses as those contracts end | CR-1 (per reading), CR-4, CR-5c, CR-6, CR-8 (0.7, voiding a contract right), CR-10a |
| K3 Commencement | - | - | Dates the operations of K1 and K2: before 3 November 2027 they act only through expectations (CR-1, 0.7 note) | CR-10a |

K1 and K2 interact: K1 adds the Sunday work that K2 lets workers refuse; K2 applies to small shops, which already opened on Sunday under the ban.

## 3. Actor classes

| Actor class | Role | How its options change (CR-1) |
| --- | --- | --- |
| large_shops | The 1,600 shops over 280 m² and their owners (chains, retailers) | Op 2: may open on Sunday; op 1 under K2 for objecting staff |
| large_retailers (class) | The retailers' association members as a group | Through CR-9: rivals' opening changes each one's best choice (A-13) |
| small_shops | The 22,400 shops of 280 m² or less, about 10,500 open on Sunday | Through CR-9 (substitute): large shops now compete on Sunday; op 1 under K2 for objecting staff |
| buyers (Sunday shoppers) | Hastrow residents who shop on Sunday or would | Op 2: a Sunday trip to a large shop (CR-3b) |
| buyers.border | Residents within 30 minutes of Corsland | As above; Corsland trips can be replaced |
| buyers.small_shop_dependent | Buyers who rely on a nearby small shop | Through CR-9: small shops may close (A-7) |
| shop_workers.small_shops | 58,000 workers, 31,000 work some Sundays under "as rostered" | Op 2 under K2: may refuse Sunday work; through CR-9: large shops hire some (A-19) |
| shop_workers.large_shops | 112,000 workers in large shops | Through CR-9 (input_to): Sunday hours at the Sunday rate; op 2 under K2 |
| shop_workers.new_hires | Workers hired after 3 November 2027 | U1-a: hold the right; U1-b: do not |
| owners_small_units | Owners of units of 280 m² or less | Through CR-9 and CR-7c: the Sunday advantage of their units ends |
| owners_large_units | Owners of large-format premises and retail parks | Through CR-7c: higher expected yields |
| sellers.complements | Cafés, restaurants, fuel stations near large shops; neighboring small sellers near standalone small shops | Through CR-9 (complement, trip) |
| neighboring_jurisdictions | Corsland shops near the line | Through CR-9 (across_border) |
| sellers.substitutes (online) | Online sellers | Through CR-9 (substitute) |
| municipalities | Enforce the ban on the counterfactual path; receive its fines | Op 4 and op 3 removed: no enforcement task, no fines |
| officials.employment_tribunal | Hears K2 complaints | Op 3: new complaints |
| taxpayers (state budget) | Receives sales tax | Through CR-9 and CR-8b |
| lobbying groups | Retailers' association; small shops' federation, union, church groups | CR-4 (x: accept, y: lobby), against the contested counterfactual |

## 4. Direct effect

CR-1 and CR-2: the immediate change for those whose options K1 and K2 alter, against the path on which section 9 stays in force.

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-1 | large_shops | quantity_supplied (Sunday opening and Sunday sales) | increase | short; medium; long | CR-1 op 2, CR-4 (x: stay closed, y: open) | A-1, A-24 |
| C-2 | buyers (Sunday shoppers) | quantity_traded (purchases at large shops on Sunday) | increase | short; medium; long | CR-3b, CR-4, CR-5 | A-1, A-2 |
| C-3 | municipalities | enforcement_cost (Sunday trading enforcement) | decrease | short; medium; long | CR-1, CR-8c | A-24 |
| C-4 | municipalities | non_tax_receipts (fines for Sunday opening) | decrease | short; medium; long | CR-8b | A-24 |
| C-5 | municipalities | resources_available_other_uses (municipal budgets, net of fines and officer time) | ambiguous | short; medium; long | CR-8 (1.0: receipts into the same budget), CR-12b | A-24 |
| C-6 | shop_workers.small_shops (who object) | term_prevalence (enforceable Sunday-work requirement in contracts) | decrease | short; medium; long | CR-1 per reading, CR-8 (0.7, voiding a contract right) | A-8 |
| C-7 | small_shops (employers) and objecting workers | non_wage_compensation (freedom to refuse Sunday work) | increase | short; medium | CR-8 (0.7, voiding a contract right), CR-8b | A-8 |

## 5. Responses

CR-4 applied to every pair of options each actor class has; CR-5 for exchanges now permitted; CR-10a for timing, including timing under U1-b.

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-8 | shop_workers.small_shops (who object) | hours_worked (Sunday) | decrease | short; medium | CR-4 (x: work Sunday, y: refuse) | A-8 |
| C-9 | small_shops | compliance_cost (re-rostering Sunday cover around objectors) | increase | short; medium | CR-1 op 1, CR-3a, CR-8c | A-8 |
| C-10 | small_shops | quantity_supplied (Sunday sales) | decrease | short; medium; long | CR-9 (substitute), CR-4, CR-12d | A-3, A-8 |
| C-11 | small_shops | number_of_sellers | decrease | medium; long | CR-4 (x: stay open, y: close), CR-10b | A-7, A-3 |
| C-12 | large_shops | quantity_supplied (sales Monday to Saturday) | decrease | short; medium; long | CR-4 (x: shop Saturday, y: shop Sunday), CR-12h | A-5, A-1 |
| C-13 | buyers.border | cross_border_purchases (Sunday purchases in Corsland) | decrease | short; medium; long | CR-4 (x: there, y: here) | A-6 |
| C-14 | buyers.border | travel_time | decrease | short; medium; long | CR-4, CR-3b | A-6 |
| C-15 | large_shops | investment_target (new large stores and shops enlarged past 280 m²) | increase | medium; long | CR-4, CR-10a, CR-10c | A-4, A-11, A-1 |
| C-16 | large_shops and chain formats near the line | unit_size (sales area of shops near 280 m²) | increase | medium; long | CR-4, CR-10b | A-11, A-4 |
| C-17 | large_shops | employment (replacement hires dated before 3 November 2027) | U1-a: no_change; U1-b: decrease | short (May to 2 November 2027) | CR-1 per reading, CR-10a, CR-4 | A-16 |
| C-18 | large_shops | employment (replacement hires from 3 November 2027) | U1-a: no_change; U1-b: increase | short (from 3 November 2027) | CR-1 per reading, CR-10a | A-16 |
| C-19 | shop_workers (planning to change employer) | job_changes (before 3 November 2027) | U1-a: no_change; U1-b: increase | short (May to 2 November 2027) | CR-1 per reading, CR-10a, CR-4 | A-17 |
| C-20 | shop_workers (planning to change employer) | job_changes (after 3 November 2027, among those who moved early) | U1-a: no_change; U1-b: decrease | short (late 2027 and 2028) | CR-1 per reading, CR-10a | A-17 |
| C-21 | shop_workers.small_shops | job_changes (medium run) | U1-a: increase; U1-b: ambiguous | medium | CR-9, CR-4, CR-12b | A-19, A-18, A-1 |
| C-22 | shop_workers.new_hires | allocation_by_non_price_criteria (screening for willingness to work Sundays) | U1-a: increase; U1-b: no_change | medium; long | CR-5c, CR-6 | A-N1, A-8 |
| C-23 | small_shops and large_shops (employers) | legal_breach (objecting workers pressed to work Sundays) | increase | short; medium | CR-4 (x: comply, y: violate), CR-12 (0.9) | A-20, A-8 |
| C-24 | officials.employment_tribunal | enforcement_cost (Sunday-work complaints) | increase | short; medium | CR-1 op 3, CR-8c | A-8 |
| C-25 | retailers' association; small shops' federation, union, church groups | lobbying_effort (over Sunday opening) | ambiguous | medium; long | CR-4 (0.9 and 1.0 lobbying notes), CR-12b | A-14, A-15 |

## 6. Second-order effects

CR-9 along named relations, then CR-5 to CR-7 in each market reached. Depth limit 4. Effects on sellers who supply goods to large shops (input_to) are stopped at depth 3 as diffuse.

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C-26 | shop_workers.large_shops | hours_worked (Sunday) | increase | short; medium; long | CR-9, LW-10 | shop labor input_to large-shop Sunday sales (close) | A-1, A-9 |
| C-27 | shop_workers.large_shops | hours_worked (Monday to Saturday) | decrease | short; medium; long | CR-9, LW-10 | shop labor input_to large-shop weekday sales (close) | A-5, A-10 |
| C-28 | shop_workers.large_shops | hours_worked (total per week) | increase | short; medium; long | CR-12e (empirical premise), CR-12 (0.8, two items) | - | A-9, A-10, A-1 |
| C-29 | shop_workers.large_shops | earnings | increase | short; medium; long | CR-9, arithmetic | - | A-9, A-10, A-1, A-N1 |
| C-30 | shop_workers (all) | hours_worked (total retail hours) | ambiguous | medium; long | CR-12b | shop labor input_to retail sales (close) | A-9, A-3, A-7, A-8 |
| C-31 | shop_workers.small_shops | employment | decrease | medium; long | CR-9, LW-10 | shop labor input_to small-shop sales (close) | A-3, A-7 |
| C-32 | owners_small_units | asset_value (units of 280 m² or less) | decrease | short (from 11 January 2027, rising with the bill's passage) | CR-7c, CR-10c | small units same_market_other_segment of large units (close) | A-23, A-4 |
| C-33 | small_shops (tenants) | price_paid (rent of units of 280 m² or less) | decrease | medium; long | CR-6, CR-10b | as above | A-23 |
| C-34 | owners_large_units | asset_value (large-format premises and retail parks) | increase | short (from 11 January 2027, rising with the bill's passage) | CR-7c, CR-10c | - | A-1, A-4 |
| C-35 | large_retailers (class) | return_on_capital | increase | medium | CR-9, CR-12e (empirical premise) | large shops compete for the same buyers (close) | A-13 |
| C-36 | sellers.substitutes (online) | quantity_traded (Sunday online orders by Hastrow residents) | decrease | short; medium; long | CR-9 (substitute), CR-4 | online orders substitute for large-shop Sunday trips (partial) | A-22 |
| C-37 | neighboring_jurisdictions (Corsland shops) | quantity_traded (Sunday sales to Hastrow residents) | decrease | short; medium; long | CR-9 (across_border) | Corsland shops across_border with Hastrow large shops (close near the line) | A-6 |
| C-38 | neighboring_jurisdictions (Corsland shops near the line) | asset_value | decrease | short (from announcement) | CR-7c, CR-10c | as above | A-6, A-4 |
| C-39 | taxpayers (state budget) | tax_revenue (sales tax) | increase | short; medium; long | CR-9, CR-8b | Corsland purchases across_border | A-6 |
| C-40 | sellers.complements (cafés, meals, fuel near large shops) | quantity_traded (Sunday) | increase | short; medium; long | CR-9 (complement, trip) | cafés, meals, fuel complement (trip) of large-shop Sunday trips (partial) | A-12, A-2 |
| C-41 | sellers.complements (small sellers next to standalone small shops) | quantity_traded (Sunday) | decrease | short; medium; long | CR-9 (complement, trip) | neighboring small sellers complement (trip) of small-shop Sunday trips (partial) | A-21, A-3 |
| C-42 | buyers.small_shop_dependent | travel_time | increase | medium; long | CR-9, CR-3a | buyers of closing small shops (exchange) | A-7, A-3 |
| C-43 | large_shops | resources_available_other_uses (fines and compliance with the ban no longer paid) | increase | short; medium; long | CR-8b | - | A-24 |

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (-) | Dominance premise | Combined sign |
| --- | --- | --- | --- | --- |
| shop_workers.large_shops, hours_worked (total), all horizons | Sunday crews (A-9) | Weekday hours follow sales (A-10) | Empirical premise A-9 (p 0.65): minimum crews make Sunday staffing exceed the hours saved | increase (C-28) |
| shop_workers (all), hours_worked (total retail) | Large shops' hours | Small shops' sales and closures; objectors' Sunday hours | None | ambiguous (C-30) |
| large_retailers, return_on_capital, medium | Trade drawn from small shops, Corsland and online | Forced seventh day | A-13 (p 0.7) | increase (C-35) |
| municipalities, budget net of fines and officer time | Officer time freed | Fines lost | None (figures do not decide) | ambiguous (C-5) |
| small_shops, quantity_supplied (Sunday) | - | Buyers move (A-3); objecting staff (A-8) | Same sign, independent chains (CR-12d) | decrease (C-10) |
| shop_workers.small_shops, job_changes, medium | New jobs at large shops (A-19) | U1-b: covered workers keep their contract (A-18) | None | U1-a: increase; U1-b: ambiguous (C-21) |
| lobbying, medium; long | Restoration and defence campaigns | End of the repeal campaign | None (CR-4, 1.0 note: contested counterfactual) | ambiguous (C-25) |
| large_shops, sales Monday to Saturday and Sunday | Sunday (C-2) | Weekdays (C-12) | Different windows (CR-12h); not netted | per window |

No chains cancel by construction (CR-12f).

## 8. Time structure

- **Announcement (11 January to 3 November 2027).** The bill was introduced in January, became more likely with the House vote on 9 April and the Senate vote on 22 April, and was signed on 3 May. Asset values moved part of the way at each step (CR-7c, probability): small units down (C-32), large premises up (C-34), Corsland shops near the line down (C-38). Before 3 November the operations of K1 and K2 act only through expectations.
- **Timing under U1-b.** Because only contracts in force on 3 November 2027 are covered under U1-b, large shops defer replacement hires past the date (C-17, C-18) and workers who plan to move do so before it (C-19, C-20). Under U1-a nothing depends on the date. These are signed per window (CR-12h).
- **First year.** Large shops open on Sunday; buyers move from small shops, Corsland and online (C-10, C-13, C-36). Small shops re-roster around objectors (C-9). Whether shop wages rise in the first year needs A-26 (p 0.45) and is not reported.
- **Medium and long run.** Small shops that relied on Sunday trade close as leases end (CR-10b; C-11); small-unit rents fall at lease renewal (C-33); new large stores are built and shops near the line are enlarged on refit (C-15, C-16). Under U1-b the share of covered contracts falls with turnover (about 2% a month), so C-6 fades toward new hires having no right; under U1-a it does not fade.
- **Belief in the repeal.** Votes of 68 to 57 and 21 to 14 support an expectation that it lasts (A-4, 0.75); expected restoration within the payback period of new stores has p 0.25 (A-25), so long-payback investment is reported.

### Metamorphic check: the original ban and what the repeal does to its effects

The original rule (section 9 of the 1961 Act, against a path with no ban) is derived first from the core rules, then each effect is checked against the repeal.

| Original effect (ban against no ban) | Derivation | Repeal | Persistence |
| --- | --- | --- | --- |
| Large shops' Sunday sales: decrease (to none where enforced) | CR-1 op 1; CR-5a | Reverses (C-1, C-2) | none |
| Small shops' Sunday sales: increase | CR-9 (substitute), CR-4 | Reverses (C-10) | none |
| Number of small shops: increase (some survive only on Sunday trade) | CR-4, CR-10b | Reverses gradually (C-11) | partial (medium); none (long) |
| Sunday purchases in Corsland: increase | CR-4 (x: here, y: there) | Reverses (C-13, C-37) | none |
| Sunday online orders: increase | CR-9 (substitute) | Reverses (C-36) | none |
| Large shops' weekday sales: increase (purchases moved from Sunday) | CR-4 (timing) | Reverses (C-12) | none |
| Small-unit premium (12%): increase in asset value and rent | CR-7c, CR-10c | Reverses (C-32, C-33) | none for the premium; the stock of small units persists |
| Shops fitted under 280 m²: unit_size decrease near the line | CR-1 notch, CR-4 | Partly reverses as shops are refitted (C-16) | partial |
| Large-format premises: asset value decrease | CR-7c | Reverses (C-34) | none |
| Sunday hours in large shops: decrease | CR-9, LW-10 | Reverses (C-26) | none |
| Cafés and fuel near large shops, Sunday: decrease | CR-9 (trip) | Reverses (C-40) | none |
| Municipal enforcement cost and fines: increase | CR-1, CR-8b, CR-8c | Reverses (C-3, C-4) | none |
| Lobbying over the ban: increase | CR-4 | Not reversed: the question stays contested (C-25) | full |
| State sales tax on purchases made in Corsland: decrease | CR-9, CR-8b | Reverses (C-39) | none |
| (no counterpart) Right to refuse Sunday work | - | New effects of K2: C-6, C-7, C-8, C-9, C-23, C-24, C-22, C-21 | n/a |

Effects the repeal does not simply reverse: shops fitted under the line and the stock of small units (durable stocks, CR-10b), and the contest over Sunday trading. Costs already incurred under the ban (fit-outs to 280 m², fines paid) are the same on both paths and are not consequences of the repeal (CR-10b).

## 9. Opportunity costs

Each is written as a signed change in a variable.

| ID | Actor class | Variable | Sign | What is given up | Rules |
| --- | --- | --- | --- | --- | --- |
| C-3 | municipalities | enforcement_cost (Sunday trading enforcement) | decrease | Officer time now available for other municipal work (about 1.2 million a year) | CR-1, CR-8c |
| C-9 | small_shops | compliance_cost (re-rostering Sunday cover around objectors) | increase | Owners' and managers' time and other staff hours spent covering Sundays | CR-1 op 1, CR-3a, CR-8c |
| C-24 | officials.employment_tribunal | enforcement_cost (Sunday-work complaints) | increase | Tribunal time that would have served other cases | CR-1 op 3, CR-8c |

CR-8's symmetry: fines no longer paid are both a lower receipt for municipalities (C-4) and means kept by large shops (C-43); the voided right to roster objectors is a transfer from employers to workers (C-7, C-9); trade drawn by large shops (C-2) is matched by trade lost by small shops, Corsland and online sellers (C-10, C-37, C-36); officer time freed (C-3) is a resource no longer used up.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
| --- | --- | --- | --- | --- | --- |
| A-1 | Some large shops expect Sunday opening to cover its costs, including staff at the Sunday rate and, under U1-a, volunteers only. | alternative_uses | 0.9 | Corsland's large shops open on Sunday; the association's campaign. | These consequences fail or lose this chain: C-1, C-2, C-12, C-15, C-21, C-26, C-28, C-29, C-34. |
| A-2 | Some buyers rank a Sunday trip to a large shop above their counterfactual shopping times. | other | 0.85 | Hastrow residents' Sunday trips to Corsland; surveys. | These consequences fail or lose this chain: C-2, C-40. |
| A-3 | Some buyers who shop at small shops on Sunday move to large shops when they open. | substitutability | 0.85 | Small shops' Sunday share (16% to 20%); Corsland's experience. | These consequences fail or lose this chain: C-10, C-11, C-30, C-31, C-41, C-42. |
| A-4 | Owners and buyers of shops and premises expect the repeal to last. | expectations | 0.75 | Votes of 68 to 57 and 21 to 14; the failed 2024 bill on the other side. | These consequences fail or lose this chain: C-15, C-16, C-32, C-34, C-38. |
| A-5 | Some buyers move purchases from Saturday or weekdays to Sunday. | other | 0.8 | Corsland's sales by day of the week. | These consequences fail or lose this chain: C-12, C-27. |
| A-6 | Some border residents bought in Corsland on Sundays because Hastrow's large shops were shut, and now buy at home. | mobility | 0.8 | The revenue department's 380 million estimate; 700,000 residents within 30 minutes. | These consequences fail or lose this chain: C-13, C-14, C-37, C-38, C-39. |
| A-7 | Some small shops cover their costs only with Sunday trade at its counterfactual level. | alternative_uses | 0.7 | Margins of convenience stores; Corsland's closures after its own change. | These consequences fail or lose this chain: C-11, C-30, C-31, C-42. |
| A-8 | Some small-shop workers object to Sunday work and give notice. | other | 0.7 | Union surveys; 31,000 small-shop workers work Sundays under "as rostered" clauses. | These consequences fail or lose this chain: C-6, C-7, C-8, C-9, C-10, C-22, C-23, C-24, C-30. |
| A-9 | Large shops need a minimum crew for each hour open, so Sunday staffing exceeds the hours saved on other days. | other | 0.65 | Staffing rules; store opening practice in Corsland. | These consequences fail or lose this chain: C-26, C-28, C-29, C-30. |
| A-10 | Large shops' Monday to Saturday staffing follows sales. | other | 0.7 | Rostering systems. | These consequences fail or lose this chain: C-27, C-28, C-29. |
| A-11 | Some shops near the line would have been larger without it. | binding | 0.8 | About 1,050 shops at 250 to 280 m² against 260 at 280 to 310 m²; 1,250 chain formats fitted under the line. | These consequences fail or lose this chain: C-15, C-16. |
| A-12 | Sunday shoppers at large shops combine the trip with cafés, meals, fuel and nearby small shops. | other | 0.75 | Retail park footfall data; Corsland's Sunday trade. | These consequences fail or lose this chain: C-40. |
| A-13 | For large retailers as a class, the trade drawn from small shops, Corsland and online sellers outweighs the cost of opening a seventh day that rivals' opening may force. | other | 0.7 | Fifteen years of campaigning (demonstrated preference); Corsland's large shops' Sunday trade. | These consequences fail or lose this chain: C-35. |
| A-14 | Organized interests on both sides can lobby at a cost below their stake. | other | 0.85 | Existing associations; the 2024 and 2027 campaigns. | These consequences fail or lose this chain: C-25. |
| A-15 | On the counterfactual path the ban would have stayed contested, with both sides lobbying. | other | 0.8 | The 2024 vote (61 to 64); the association's continuing campaign. | These consequences fail or lose this chain: C-25. |
| A-16 | Under U1-b, some large shops defer replacement hires past 3 November 2027 so that the new contracts are not covered. | expectations | 0.6 | Employers' advisers' guidance; turnover of about 2% a month. | These consequences fail or lose this chain: C-17, C-18. |
| A-17 | Under U1-b, some workers who plan to change employer move before 3 November 2027 to hold a covered contract. | expectations | 0.55 | Union advice to members. | These consequences fail or lose this chain: C-19, C-20. |
| A-18 | Under U1-b, some covered workers value the right enough to turn down moves that would end it. | other | 0.6 | Survey of workers who object to Sunday work. | These consequences fail or lose this chain: C-21. |
| A-19 | Large shops hire some Sunday staff from among existing shop workers. | mobility | 0.75 | Hiring patterns in retail. | These consequences fail or lose this chain: C-21. |
| A-20 | The right is enforced only on complaint, and some workers who are pressed do not complain. | enforcement | 0.75 | Tribunal claim rates under other employment rights. | These consequences fail or lose this chain: C-23. |
| A-21 | Some Sunday buyers at standalone small shops combine the trip with purchases at a neighboring small seller. | other | 0.65 | Parades of shops in residential streets. | These consequences fail or lose this chain: C-41. |
| A-22 | Some Sunday online orders by Hastrow residents were placed because large shops were shut. | substitutability | 0.6 | Sunday share of online orders (18%) against Corsland's lower share. | These consequences fail or lose this chain: C-36. |
| A-23 | The 12% rent premium on small units reflects Sunday trading, and the stock of small units cannot shrink at once. | durability | 0.7 | Letting agents' evidence; rents of comparable units in Corsland. | These consequences fail or lose this chain: C-32, C-33. |
| A-24 | On the counterfactual path the ban is enforced at about its present level. | enforcement | 0.85 | About 30 prosecutions a year; municipal budgets. | These consequences fail or lose this chain: C-1, C-3, C-4, C-5, C-43. |
| A-25 | Retailers expect the ban to be restored within the payback period of new large stores. | expectations | 0.25 | The federation's lobbying; against it, the 2027 margins. | No reported consequence rests on it (see Not reported). |
| A-26 | Retail labor cannot expand at the old wage in the first year, so large shops' Sunday hiring raises shop wages. | other | 0.45 | Retail vacancy rates; the pay agreement fixes base rates until April. | No reported consequence rests on it (see Not reported). |
| A-N1 | The retail pay agreement fixes base and Sunday rates between April renegotiations, so changes in what employers must give go to other terms (hiring choices, hours) rather than the wage. | binding | 0.8 | NEW. The record: the agreement is renegotiated each April and applies on both paths; A-26's evidence says it fixes base rates until April. | These consequences fail or lose this chain: C-22, C-29. |

**Not reported** (an assumption below 0.5):
- Shop wage rates rise in the first year because large shops' Sunday hiring meets labor that cannot expand at the old wage (CR-9, CR-6): needs A-26 (p 0.45). The chain is kind 2 (CR-12, 0.8); with p below 0.5 it does not make C-29 ambiguous, and C-29 is signed by arithmetic with wage rates unchanged (A-N1).
- Long-payback investment in large stores held back by expected restoration (CR-10a): needs A-25 (p 0.25). Recorded here; C-15 rests on A-4 instead.

## 11. Report

**The policy:** From 3 November 2027 Hastrow repeals the 1961 ban on Sunday opening by shops with more than 280 m² of sales area, with no other limit on Sunday hours. At the same time every shop worker may give notice objecting to Sunday work; a month later the employer may not require it or penalize the refusal, with complaint to the Employment Tribunal. It is unclear whether the right covers only contracts in force on 3 November 2027 (U1-b) or later contracts too (U1-a). Everything is compared with the ban staying in force.

**Visible consequences:** Large shops open on Sunday and buyers shop there (C-1, C-2); large-shop workers work Sunday hours (C-26); small shops lose Sunday sales (C-10); border residents buy less in Corsland (C-13); objecting small-shop workers can no longer be rostered on Sunday (C-6).

**Invisible consequences:**
- *Large shops and owners of large premises:* sales move from weekdays to Sunday (C-12); large premises gain value from the announcement (C-34); retailers as a class earn more (C-35); they invest in larger stores and enlarge shops near the line (C-15, C-16); they keep the fines they would have paid (C-43); under U1-b they defer hires past 3 November (C-17, C-18).
- *Small shops and owners of small units:* re-rostering costs (C-9); closures (C-11); small units lose value and their rents fall (C-32, C-33).
- *Workers:* large-shop workers work fewer weekday hours but more hours in total and earn more (C-27, C-28, C-29); small-shop employment falls (C-31); objectors work fewer Sundays and gain the freedom to refuse (C-8, C-7); some are pressed in breach of the right (C-23), and complaints use tribunal time (C-24); under U1-a new hires are screened for willingness to work Sundays (C-22); under U1-b workers move before 3 November (C-19, C-20).
- *Others:* online sellers and Corsland shops lose Sunday trade and Corsland shops near the line lose value (C-36, C-37, C-38); cafés and fuel near large shops gain (C-40) while small sellers next to standalone small shops lose (C-41); buyers who relied on closing small shops travel farther (C-42); border residents travel less (C-14); the state collects more sales tax (C-39); municipalities spend less on enforcement and receive no fines (C-3, C-4).

**Ambiguous effects:** Total retail hours (C-30): large shops add hours; small shops and objectors lose them. The municipal budget net of fines and officer time (C-5). Small-shop workers' job changes under U1-b (C-21): new jobs at large shops against holding on to a covered contract. Lobbying (C-25): the restoration campaign against the end of the repeal campaign. What would decide each: the relative sizes, which the method cannot measure.

**Key conditions:** Large shops expect Sunday opening to pay (A-1, 0.9); buyers move from small shops (A-3, 0.85) and Corsland (A-6, 0.8); the ban would be enforced (A-24, 0.85); the repeal is believed (A-4, 0.75); minimum crews (A-9, 0.65); small shops that depend on Sunday trade (A-7, 0.7); workers object (A-8, 0.7); retailers' class gain (A-13, 0.7). One premise was added: the pay agreement fixes rates between Aprils (A-N1, 0.8). U1 decides the signs of C-17, C-18, C-19, C-20, C-21 and C-22.

**What this analysis cannot say:** How large any effect is; whether total retail employment or hours rise or fall; whether municipalities gain or lose. It does not weigh buyers' and large retailers' gains against small shops' and objecting workers' losses, or value the Sunday rest that church groups and the union defend, and does not say whether the repeal is good. Health and safety effects are out of scope.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions | Persistence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C-1 | large_shops | quantity_supplied (Sunday opening and Sunday sales) | increase | short; medium; long | visible | B | CR-1 (op 2: K1 adds the option of opening on Sunday from 3 November 2027; on the counterfactual path it is removed where enforced, A-24); CR-4 (x: closed on Sunday, y: open; y now open and, for some, expected to cover its costs at the Sunday rate and, under U1-a, with volunteers only, A-1) | A-1, A-24 | none |
| C-2 | buyers (Sunday shoppers) | quantity_traded (purchases at large shops on Sunday) | increase | short; medium; long | visible | B | CR-3b (an option added cannot make buyers worse off at the time of choice); CR-4 (x: shop at another time or place, y: a Sunday trip to a large shop, which some buyers rank higher, A-2); CR-5 (exchanges the ban prevented now take place, both parties expecting to gain) | A-1, A-2 | none |
| C-3 | municipalities | enforcement_cost (Sunday trading enforcement) | decrease | short; medium; long | invisible | B | CR-1 (the enforcement task ends with section 9); CR-8c (about 1.2 million a year of officer time that the counterfactual uses up is freed); counterfactual enforcement at its present level (A-24) | A-24 | none |
| C-4 | municipalities | non_tax_receipts (fines for Sunday opening) | decrease | short; medium; long | invisible | B | CR-8b (fines that large shops pay on the counterfactual path are no longer received; the same sum stays with the shops); A-24 | A-24 | none |
| C-5 | municipalities | resources_available_other_uses (municipal budgets, net of fines and officer time) | ambiguous | short; medium; long | invisible | B | CR-8 1.0 (fines and officer time are two items of the municipal budget, C-3 and C-4); (+) officer time freed; (-) fines lost. With about 30 prosecutions a year and fines up to 50,000 per Sunday, the fines can be smaller or larger than 1.2 million; no figure decides it | A-24 | none |
| C-6 | shop_workers.small_shops (who object) | term_prevalence (enforceable Sunday-work requirement in contracts) | decrease | short; medium; long | visible | B | CR-1 (K2 removes, for each objecting worker, the employer's option of requiring Sunday work under an "as rostered" clause; under both readings this covers contracts in force on 3 November 2027; under U1-a also later contracts, under U1-b the covered contracts end with turnover); some workers give notice (A-8) | A-8 | n/a (no counterpart in the original rule) |
| C-7 | small_shops (employers) and objecting workers | non_wage_compensation (freedom to refuse Sunday work) | increase | short; medium | invisible | B | CR-8 0.7 (a rule that voids a right held under an existing contract is a transfer: employers lose the value of requiring Sunday work, objecting workers gain it); CR-8b (both sides recorded: the employers' side is C-9) | A-8 | n/a (no counterpart in the original rule) |
| C-8 | shop_workers.small_shops (who object) | hours_worked (Sunday) | decrease | short; medium | invisible | B | CR-1 (op 2: K2 adds the option of refusing); CR-4 (x: work the rostered Sunday, y: give notice; y now open and chosen by those who object, A-8); not all who object enforce it where pressed (A-20), which limits but does not reverse the sign | A-8 | n/a (no counterpart in the original rule) |
| C-9 | small_shops | compliance_cost (re-rostering Sunday cover around objectors) | increase | short; medium | invisible | B | CR-1 (op 1: the option of rostering an objector on Sunday is removed); CR-3a (the employer falls back to a lower-ranked arrangement: other staff, the owner's own time, shorter hours); CR-8c (the work of re-rostering is used up) | A-8 | n/a (no counterpart in the original rule) |
| C-10 | small_shops | quantity_supplied (Sunday sales) | decrease | short; medium; long | visible | B | Two independent chains with the same sign (CR-12d): CR-9 (relation: a Sunday trip to a large shop is a substitute for one to a small shop; buyers move, A-3); CR-1 op 1 under K2 (objecting staff cannot be rostered, so some shops cut Sunday hours, A-8) | A-3, A-8 | none (the original raised small shops' Sunday sales; this reverses) |
| C-11 | small_shops | number_of_sellers | decrease | medium; long | invisible | B | CR-4 (x: keep trading, y: close; x made worse by the lost Sunday trade, C-10; some shops cover costs only with Sunday trade at its counterfactual level, A-7); CR-10b (closures come as leases end and stock is run down) | A-7, A-3 | none (the original kept these shops trading; closures caused by the repeal persist if the ban were restored) |
| C-12 | large_shops | quantity_supplied (sales Monday to Saturday) | decrease | short; medium; long | invisible | B | CR-4 (x: shop on Saturday or a weekday, y: on Sunday; y now open, and some buyers move purchases, A-5); signed per window against the counterfactual (Monday to Saturday window: decrease; Sunday window: increase, C-2) | A-5, A-1 | none |
| C-13 | buyers.border | cross_border_purchases (Sunday purchases in Corsland) | decrease | short; medium; long | visible | B | CR-4 (x: a Sunday trip to Corsland, y: a Sunday trip to a large shop at home; y now open; some residents bought there only because Hastrow's large shops were shut, A-6) | A-6 | none |
| C-14 | buyers.border | travel_time | decrease | short; medium; long | invisible | B | CR-4 (as C-13: a nearer trip replaces one to Corsland, A-6); CR-3b (the option added) | A-6 | none |
| C-15 | large_shops | investment_target (new large stores and shops enlarged past 280 m²) | increase | medium; long | invisible | B | CR-4 (x: a format at 280 m² or less, y: a larger one; y made better by Sunday trade); CR-10a and CR-10c (pays only if the repeal is expected to last, A-4; that restoration within the payback period is expected has p 0.25, A-25) | A-4, A-11, A-1 | none |
| C-16 | large_shops and chain formats near the line | unit_size (sales area of shops near 280 m²) | increase | medium; long | invisible | B | CR-4 (x: stay at 250 to 280 m², y: enlarge on refit; some shops would have been larger without the line, A-11); CR-10b (the stock changes only through refits and new building, so the response is gradual) | A-11, A-4 | partial (medium); partial (long): shops fitted under the line remain until refitted |
| C-17 | large_shops | employment (replacement hires dated before 3 November 2027) | U1-a: no_change; U1-b: decrease | short (May to 2 November 2027) | invisible | B | CR-1 per reading: under U1-a every contract is covered whenever made, so the date of hiring changes nothing; under U1-b a contract made before 3 November 2027 carries the right and one made after does not; CR-10a and CR-4 (x: hire before, y: defer past the date; A-16). Signed per window (CR-12h) | A-16 | n/a |
| C-18 | large_shops | employment (replacement hires from 3 November 2027) | U1-a: no_change; U1-b: increase | short (from 3 November 2027) | invisible | B | As C-17: the deferred hires are made after the date (A-16) | A-16 | n/a |
| C-19 | shop_workers (planning to change employer) | job_changes (before 3 November 2027) | U1-a: no_change; U1-b: increase | short (May to 2 November 2027) | invisible | B | Under U1-b a move made before the date gives a covered contract; CR-4 (x: move later, y: move before 3 November; y made better, A-17); under U1-a the right travels, so nothing changes | A-17 | n/a |
| C-20 | shop_workers (planning to change employer) | job_changes (after 3 November 2027, among those who moved early) | U1-a: no_change; U1-b: decrease | short (late 2027 and 2028) | invisible | B | As C-19: moves brought forward are not made later (A-17) | A-17 | n/a |
| C-21 | shop_workers.small_shops | job_changes (medium run) | U1-a: increase; U1-b: ambiguous | medium | invisible | B | U1-a: CR-9 (large shops hire some Sunday staff from existing shop workers, A-19) and CR-4 (x: stay, y: move; y made better by the new jobs), with the right kept on moving. U1-b: the same chain against CR-4 for covered workers who value the right (x: stay with a covered contract, y: move and lose it; y made worse, A-18). No premise says which dominates | A-19, A-18, A-1 | n/a (no counterpart in the original rule) |
| C-22 | shop_workers.new_hires | allocation_by_non_price_criteria (screening for willingness to work Sundays) | U1-a: increase; U1-b: no_change | medium; long | invisible | B | U1-a: CR-5c (K2 changes what an employer receives from a new hire who may object); the pay agreement fixes base and Sunday rates (A-N1), so by CR-6 the pressure goes to an unregulated margin, here the choice among applicants. U1-b: new contracts carry no right, so no change | A-N1, A-8 | n/a (no counterpart in the original rule) |
| C-23 | small_shops and large_shops (employers) | legal_breach (objecting workers pressed to work Sundays) | increase | short; medium | invisible | B | CR-4 (x: respect the notice, y: press the worker; enforced only on complaint and some pressed workers do not complain, A-20, so for some employers y pays); the right exists only under the Act, so the counterfactual has no breach (CR-12, 0.9 note) | A-20, A-8 | n/a |
| C-24 | officials.employment_tribunal | enforcement_cost (Sunday-work complaints) | increase | short; medium | invisible | B | CR-1 (op 3: s. 6(4) gives a complaint to the tribunal); some objecting workers who are pressed complain (A-8; A-20 says only that some do not); CR-8c (used up) | A-8 | n/a |
| C-25 | retailers' association; small shops' federation, union, church groups | lobbying_effort (over Sunday opening) | ambiguous | medium; long | invisible | B | CR-4 (x: accept, y: lobby), signed against the counterfactual, on which the ban stays contested and both sides lobby (A-15). (+) the federation and its allies now lobby to restore the ban, and the association to defend the repeal, with the losses and gains now realized; (-) the association no longer campaigns for repeal. Both can organize (A-14). No premise says which dominates | A-14, A-15 | full (the question stays contested on both paths) |
| C-26 | shop_workers.large_shops | hours_worked (Sunday) | increase | short; medium; long | visible | B | CR-9 and LW-10 (relation: labor input_to Sunday sales at large shops; demand for it follows Sunday opening, C-1); a minimum crew is needed for each hour open (A-9) | A-1, A-9 | none |
| C-27 | shop_workers.large_shops | hours_worked (Monday to Saturday) | decrease | short; medium; long | invisible | B | CR-9 and LW-10 (weekday sales fall, C-12, and weekday staffing follows sales, A-10) | A-5, A-10 | none |
| C-28 | shop_workers.large_shops | hours_worked (total per week) | increase | short; medium; long | invisible | B | CR-12 0.8 (two items, C-26 and C-27; the total combined under CR-12b); dominance premise (CR-12e, empirical): Sunday staffing exceeds the hours saved on other days, because of minimum crews per hour open (A-9) | A-9, A-10, A-1 | none |
| C-29 | shop_workers.large_shops | earnings | increase | short; medium; long | invisible | B | Arithmetic on the record: total hours rise (C-28) and the added Sunday hours are paid at time-and-a-half under the pay agreement, which applies on both paths, while the hours lost are paid at the base rate; with wage rates unchanged (A-N1) earnings rise | A-9, A-10, A-1, A-N1 | none |
| C-30 | shop_workers (all) | hours_worked (total retail hours) | ambiguous | medium; long | invisible | B | CR-12b: (+) large shops' total hours (C-28); (-) small shops' Sunday sales and closures (C-10, C-11) and objecting workers' Sunday hours (C-8). No premise says which dominates | A-9, A-3, A-7, A-8 | n/a |
| C-31 | shop_workers.small_shops | employment | decrease | medium; long | invisible | B | CR-9 and LW-10 (relation: labor input_to small-shop sales; sales fall and some shops close, C-10, C-11); moves to large shops (A-19) also reduce it | A-3, A-7 | none |
| C-32 | owners_small_units | asset_value (units of 280 m² or less) | decrease | short (from 11 January 2027, rising with the bill's passage) | invisible | B | CR-10c (a unit's value reflects its expected rents); CR-7c (the 12% premium reflects Sunday trading, A-23; it falls as the repeal becomes expected, part of the way at introduction, more at passage in April and the rest at signing in May, and is borne by those who own the units then; expected to last, A-4) | A-23, A-4 | none (the premium reverses; the stock of small units built under the rule persists and holds their value below the no-ban path for a while, CR-7, 0.9 persistence note) |
| C-33 | small_shops (tenants) | price_paid (rent of units of 280 m² or less) | decrease | medium; long | invisible | B | CR-6 (less demand for small units at each rent, as their Sunday advantage ends, A-23); CR-10b (the stock of small units cannot shrink at once, A-23, so the rent falls as leases are renewed) | A-23 | none |
| C-34 | owners_large_units | asset_value (large-format premises and retail parks) | increase | short (from 11 January 2027, rising with the bill's passage) | invisible | B | CR-10c and CR-7c (Sunday trade raises the expected yields of large premises, C-1, and their owners when the repeal becomes expected capture it, part of the way as its probability rose; A-4) | A-1, A-4 | none |
| C-35 | large_retailers (class) | return_on_capital | increase | medium | invisible | B | CR-12b over two chains: (+) trade drawn from small shops, Corsland and online sellers (C-10, C-13, C-36); (-) the cost of a seventh day that rivals' opening may force on each (CR-9, competitors for the same buyers). Dominance premise (CR-12e, empirical): for the class the first outweighs the second (A-13, from fifteen years of campaigning as demonstrated preference, CR-2) | A-13 | none |
| C-36 | sellers.substitutes (online) | quantity_traded (Sunday online orders by Hastrow residents) | decrease | short; medium; long | invisible | B | CR-9 (relation: online orders substitute for a Sunday trip to a large shop); CR-4 (some orders were placed because large shops were shut, A-22) | A-22 | none |
| C-37 | neighboring_jurisdictions (Corsland shops) | quantity_traded (Sunday sales to Hastrow residents) | decrease | short; medium; long | invisible | B | CR-9 (relation: across_border; residents buy at home, C-13, A-6) | A-6 | none |
| C-38 | neighboring_jurisdictions (Corsland shops near the line) | asset_value | decrease | short (from announcement) | invisible | B | CR-10c and CR-7c (the expected fall in their Sunday trade, C-37, is borne by owners when it becomes expected); A-4 | A-6, A-4 | none |
| C-39 | taxpayers (state budget) | tax_revenue (sales tax) | increase | short; medium; long | invisible | B | CR-9 (relation: across_border; purchases that were made in Corsland, C-13, are made in Hastrow and bear its 6% sales tax); CR-8b (the receipt). Purchases moved between Hastrow shops bear the same tax on both paths; online orders, C-36, are treated as taxed on both paths | A-6 | none |
| C-40 | sellers.complements (cafés, meals, fuel near large shops) | quantity_traded (Sunday) | increase | short; medium; long | invisible | B | CR-9 (relation: complement, trip; Sunday shoppers at large shops combine the trip with them, A-12) | A-12, A-2 | none |
| C-41 | sellers.complements (small sellers next to standalone small shops) | quantity_traded (Sunday) | decrease | short; medium; long | invisible | B | CR-9 (relation: complement, trip; Sunday buyers at standalone small shops combine the trip with a neighboring small seller, A-21, and fewer such trips are made, C-10) | A-21, A-3 | none |
| C-42 | buyers.small_shop_dependent | travel_time | increase | medium; long | invisible | B | CR-9 (relation: these buyers bought from shops that close, C-11); CR-3a (their chosen option is removed, so they fall back to a farther shop) | A-7, A-3 | n/a (no counterpart in the original rule) |
| C-43 | large_shops | resources_available_other_uses (fines and compliance with the ban no longer paid) | increase | short; medium; long | invisible | B | CR-8b (both sides of the fines: what municipalities no longer receive, C-4, the shops keep); A-24 | A-24 | none |

## Gaps found

**(a) Steps no core rule covers.**
- GAP-063-C1: under U1-b, K2 creates a right that attaches to a contract made before a date and is lost when the worker moves. CR-1 (dated operations), CR-10a and CR-4 cover the timing and the lock-in, but no rule says how a right that decays with turnover should be signed over horizons; it was described in section 8 rather than signed as a fading consequence.
- None otherwise: every step was derived from CR-1 to CR-12, LW-10 and arithmetic.

**(b) Core-rule wording that was hard to apply.**
- `persistence` for a repeal is defined against the path on which the original rule was never imposed; for consequences of a new provision bundled with the repeal (K2) there is no original effect, and `n/a` is defined only for transition effects. Used "n/a (no counterpart in the original rule)".
- CR-4 (0.9 and 1.0 lobbying notes): with the counterfactual contested, the case premises (A-14, A-15) establish only that both sides lobby on both paths, not which way the repeal moves either side's effort, so the sign is ambiguous by default.
- CR-12 (0.8, two items): large-shop hours on Sunday and on weekdays are two items of `hours_worked`; the total needed the dominance premise A-9. The note does not say whether the total for all retail workers is a third item or a different actor class; treated as a different class.
- CR-8 (1.0, receipts into the same budget) for municipal budgets: the case gives the range of fines (up to 50,000 per Sunday) but not the sum, so the net is ambiguous; the rule says so, but the arithmetic route was blocked only by missing figures.

**(c) Vocabulary missing from the ontology.**
- No variable for opening hours or days as such; `quantity_supplied (Sunday opening and Sunday sales)` was used.
- No variable for a worker's statutory right as held; `term_prevalence` and `non_wage_compensation` carry it.
- No actor class for workers by contract date (covered against uncovered under U1-b).

## Comparison with the pattern-based analysis

**Summary.** The two versions agree on the main lines of the repeal. Large shops open and sell on Sunday, and sales move from other days. Border residents buy less in Corsland and online Sunday orders fall. Small shops lose Sunday trade and some close. Small units lose their premium and their rents fall, while large premises gain. Large-shop workers work Sunday hours, fewer weekday hours and, by the minimum-crew premise, more hours in total. Cafés and fuel stations near large stores gain, and neighbors of corner shops lose. Unit size near 280 m² rises as shops are refitted. Both have the same U1-dependent job changes in the medium run, breach of the right, tribunal work, the end of ban enforcement and fines, the sales-tax gain, and lobbying over Sunday opening `ambiguous` on both sides. Both have large retailers' gain resting on the same dominance premise (A-13). There are two sign conflicts, and in both the core version is wrong. It signs all small shops' Sunday sales down, though its own A-12 names nearby small shops as complements of large-store trips, so shops in anchored centres are `ambiguous`. It also signs job changes in the window from workers' timing alone, leaving out its own employers' deferral of hires and the preparation hiring. The pattern version records more values, the weekly sales total, the window effects and the Corsland trip goods. The core version records more of K2: the voided rostering right as a transfer, the re-rostering cost, both sides of the U1-b timing moves, and the municipal net. The pattern version signs small-shop owners' means from lost receipts without the saved outlays. CR-3's note requires them to be combined.

Counts: M 17, V 13, S 2, OP 13, OC 9.

### Pattern version → core version

| Pattern ID | Matched core ID(s) | Class | Cause | Note |
| --- | --- | --- | --- | --- |
| C-1 | C-1, C-2 | V | | Split into sellers' supply and buyers' purchases. Persistence differs: see Findings, metamorphic checks. |
| C-2 | C-14 | V | | Pattern: all buyers who prefer large shops on Sunday, `full_cost_per_unit` (time given up) decrease, by CR-3b. Core: border residents' `travel_time` only. The core version keeps the general gain in C-2's derivation (CR-3b) without a key. |
| C-3 | C-10 | V | | Pattern: standalone small shops. Core: all small shops, with K2's objecting staff as a second (−) chain (CR-12d). |
| C-4 | none | OC | E | Standalone small shops' value as going concerns decrease (CR-7c, CR-10c with A-3, A-4). Core recorded small units (C-32) but no shop value. Core omission. |
| C-5 | C-12 | M | | |
| C-6 | none | OC | E | Large shops' weekly sales increase, by an accounting identity (CR-12e): purchases moved between days cancel, and purchases drawn from small shops, Corsland and online add. Core section 7 refuses to net the windows, citing CR-12h. CR-12h is about bunching where a policy raises activity in every window. CR-12's 0.8 note on two items in one variable asks for the total to be recorded separately. Core error (omission from a misreading). |
| C-7 | C-13 | M | | |
| C-8 | C-11 | M | | |
| C-9 | C-31 | V | | Group against `employment` alone. Here the core sign is valid, because closures (A-7) remove jobs. |
| C-10 | C-28 | V | | Group of staff and hours against `hours_worked` total. Same premise A-9. |
| C-11 | C-26 | M | | |
| C-12 | C-27 | M | | |
| C-13 | C-16 | M | | |
| C-14 | C-16 | V | | Chains stop fitting formats to the line, recorded by the core as unit size of chain formats near the line. |
| C-15 | none | OC | E | Near-line shops' value `ambiguous`. CR-7c gives both chains: the freedom to grow (+) and the lost Sunday advantage (−). Core omission. Nothing scorable is lost. |
| C-16 | C-10 | S | E | Small shops in anchored centres, Sunday sales. Pattern: `ambiguous` (the anchor's Sunday footfall, + against the anchor's competition, −). Core: decrease for all small shops. CR-9 along the complement (trip) relation gives the (+) chain. The core version's own A-12 (p 0.75) says Sunday shoppers at large shops combine the trip with "nearby small shops", but it used A-12 only for cafés and fuel (C-40). With p ≥ 0.5 the chain is kind 2 (CR-12, 0.8), so the in-centre sign is `ambiguous`. Core error. |
| C-17 | none | OC | E | In-centre shops' value `ambiguous`, as C-16. Core omission. |
| C-18 | C-35 | V | | `asset_value` of large retailers against `return_on_capital` of the class. Same chains and dominance premise A-13. |
| C-19 | C-25 | V | | Core puts both sides in one key. Both are `ambiguous` against the contested counterfactual (A-15). |
| C-20 | C-25 | V | | As C-19. |
| C-21 | none | OC | E | Lobbying on U1 and the rules for s. 6, increase from none (CR-4 1.0, CR-12 0.9 with A-14). Core omission. |
| C-22 | none | OC | E | Large shops' preparation in the window (rosters, systems, recruitment), an activity from none (CR-10a, CR-12 0.9). The core version's C-15 is long-run investment in larger stores, a different key. Core omission. |
| C-23 | C-17, C-18 | V | | Pattern: all hires in the window, U1-a increase (preparation), U1-b `ambiguous`. Core: replacement hires only, U1-a `no_change`, U1-b decrease before and increase after the date. On the replacement item the two agree. The core version omits preparation hiring, which gives the window an increase under U1-a. |
| C-24 | C-19 | S | E | Job changes in the window. Pattern: U1-a increase, U1-b `ambiguous`. Core: U1-a `no_change`, U1-b increase. Under U1-a, large shops hire some Sunday staff from existing shop workers ahead of opening (A-19, CR-9), which the core version omits. Under U1-b, the employers' deferral of hires past the date is the core version's own C-17 (A-16). It removes job changes from the window and opposes the workers' early moves (A-17). Core error on both readings. |
| C-25 | C-21 | M | | Class differs slightly (contracts in force on 3 November; small-shop workers). |
| C-26 | C-8 | V | | PC-17's group for small-shop workers (wage, other benefits, employment or hours, `at_least_one_as_stated`). Core C-8 signs objectors' Sunday hours down, one member of the group, but as the workers' choice. The core version does not derive where employers' higher cost of cover (its C-9) goes on other terms for existing small-shop workers (CR-5c, CR-6). It does so only for new hires under U1-a (C-22). Partial core omission. |
| C-27 | C-23 | M | | |
| C-28 | C-40 | M | | |
| C-29 | C-41 | M | | |
| C-30 | C-37 | V | | Pattern: group of quantity and price (CR-6, 0.9). Core: quantity sold to Hastrow residents alone. That is defensible, since a price fall caused by the lost demand cannot restore it (CR-12e). |
| C-31 | none | OC | E | Corsland cafés and fuel stations lose trip sales (CR-9 complement, trip, with A-6, A-12). Core omission. |
| C-32 | C-36 | V | | `quantity_substitute` against `quantity_traded`. |
| C-33 | C-33 | M | | Horizons short to medium against medium and long. |
| C-34 | C-32 | M | | |
| C-35 | C-34 | M | | The pattern rests the large units' gain on A-13 as well as A-1 and A-4. The core version omits A-13. If rivals' opening could lower the class's yield, the rent large retailers will pay for units could fall too. Hidden premise in the core version. |
| C-36 | C-3 | M | | |
| C-37 | C-4 | M | | |
| C-38 | C-24 | M | | |
| C-39 | C-39 | M | | Pattern adds an online chain, which needs an unstated premise that online orders by Hastrow residents bear no Hastrow sales tax. The core version treats them as taxed on both paths. The Corsland chain alone gives the sign (CR-12d). |
| C-40 | none | OC | P | Small-shop owners' `resources_available_other_uses` decrease from lost Sunday receipts (cites CR-3, CR-5, OC-4). CR-3's note says to combine lost receipts with saved outlays (stock not bought, staff hours not paid) under CR-12b. OC-4's Unless says who loses by their own ranking, not who has less money. Without a premise that the margins on the lost sales exceed the outlays saved, the sign is `ambiguous`. Analyst's misapplication. The core version recorded nothing. |
| C-41 | none | OC | E | Total retail purchases in Hastrow increase (CR-4, CR-9 with A-6; the online chain needs the same unstated tax premise as C-39). Core omission. |

### Core-only consequences

| Core ID | Class | Cause | Note |
| --- | --- | --- | --- |
| C-5 | OP | E | Municipal budgets net of fines and officer time `ambiguous` (CR-8, 1.0: receipts into the same budget). The pattern version records both items (C-36, C-37) but not the net. Pattern omission. |
| C-6 | OP | E | `term_prevalence` of enforceable Sunday-work requirements decrease, the direct CR-1 effect of K2 on existing small-shop contracts. Pattern omission. |
| C-7 | OP | E | The voided "as rostered" right as a transfer: objecting workers gain `non_wage_compensation` (CR-8, 0.7 voiding note, CR-8b). The pattern text says the right "is worth something to workers who use it" but records only the other terms falling (C-26). The two are items of one variable moving in opposite directions (CR-12, 0.8). Each should be recorded with the total `ambiguous`. Pattern omission. |
| C-9 | OP | E | Small shops' re-rostering cost (CR-1 op 1, CR-3a, CR-8c). The pattern text names it ("rosters, replacement staff") but records no key. Pattern omission. |
| C-15 | OP | E | Long-payback investment in new and enlarged large stores (CR-4, CR-10a with A-4, A-11; A-25 below the cut-off). The pattern discussed it under TS-5 but did not record it. Pattern omission. |
| C-18 | OP | E | Under U1-b, replacement hires rise after 3 November 2027, the other side of the deferral. RS-8 says to record both sides of a timing move. Pattern omission. |
| C-20 | OP | E | Under U1-b, job changes after the date fall among workers who moved early, the other side of C-19. Pattern omission (RS-8, both sides). |
| C-22 | OP | E | New hires screened for willingness to work Sundays, under U1-a. Core error. CR-6 establishes that at least one open margin takes the pressure, and a named margin needs its own premise. A-N1 says only that pressure goes to "other terms (hiring choices, hours)". The key should be a group of the unregulated margins (selection, hours, other terms) with `at_least_one_as_stated`. The pattern version has the small-shop part of that group (C-26) but nothing for large shops' new hires under U1-a. |
| C-29 | OP | E | Large-shop workers' earnings increase. Sunday hours are paid at time-and-a-half and total hours rise (A-9); wage rates are fixed until April (A-N1). Pattern omission for the short run. A-N1 covers rates only until the April renegotiation, so the core version's medium and long signs need a further premise. This is a core error on those horizons. |
| C-30 | OP | J | Total retail hours across all shop workers `ambiguous`. The pattern version declined to combine classes (CR-12c). The core version treated the union as its own class. Both are defensible, and nothing scorable is lost. |
| C-38 | OP | E | Corsland shops near the line lose value (CR-7c, CR-10c with A-6, A-4). Pattern omission. |
| C-42 | OP | E | Buyers who relied on closing small shops travel farther (CR-9, CR-3a with A-7). Pattern omission. |
| C-43 | OP | E | Large shops keep the fines they would have paid (CR-8b), the other side of C-4. The pattern's section 9 names it but records no key. Pattern omission. |

### Findings

- **Pattern overclaims or hidden premises.**
  - No pattern applied as written overclaims. PC-17, RS-4, RS-5, RS-7's repeal clause, RS-8, RS-9, RS-11, RS-16's mirror case, RS-17 in reverse, RS-20's 1.0 baseline, OC-3's baseline clause, TS-6 and TX-10 all agree with what the core rules give. Where the versions differ on those keys, the pattern version is right (C-16, C-24).
  - The analyst's errors are C-40 (lost receipts without saved outlays) and an unstated tax premise on online orders in C-39 and C-41. The sign of C-39 survives on the Corsland chain.
  - The ban table (B-1 to B-19) carries no premises. B-12 needs A-13 mirrored and B-13's weekly decrease needs A-9 mirrored.
- **Errors in the core version.**
  - Signs: C-10 for small shops in anchored centres (should be `ambiguous`, using its own A-12). C-19 on both readings, which ignores its own C-17 and the preparation hiring. C-22 signs one CR-6 margin with no premise for it. C-29 extends A-N1 past the April renegotiation. C-34 omits A-13. The weekly sales total was refused on a misreading of CR-12h.
  - Omissions: shop values (pattern C-4, C-15, C-17), the weekly total (C-6), lobbying on U1 (C-21), window preparation and hiring (C-22, C-23 U1-a), Corsland trip goods (C-31), total purchases in Hastrow (C-41), and the employers' adjustment of other terms for existing small-shop workers (C-26).
- **Errors in the pattern version.**
  - C-40 should be `ambiguous`, or carry a premise that the lost sales' margins exceed the saved outlays.
  - B-4 and B-6 in the ban table sign all small shops' Sunday sales and values up. By the mirror of the pattern version's own C-16 and C-17, shops in anchored centres are `ambiguous` under the ban too. The metamorphic check passed this over ("reverses for standalone shops") instead of flagging it.
  - Omissions: the municipal net (core C-5), K2's direct effects and its transfer (C-6, C-7, C-9), long-payback investment (C-15), the other side of the U1-b timing moves (C-18, C-20), short-run earnings (C-29), Corsland shops' value (C-38), dependent buyers' travel (C-42) and saved fines (C-43).
- **Metamorphic checks compared.** Both versions derive the ban from the core rules first, and neither finds a sign that fails to reverse without a reason. Every row the two share has the same ban sign and the same reversal: Sunday and weekday sales, small shops' Sunday sales and number, Corsland, online, the small-unit premium, unit size, large premises, Sunday hours, complements near large stores, enforcement and fines, sales tax and lobbying. The differences are as follows.
  - *Coverage.* The pattern version has 19 ban rows plus two derived ones. The core version has 14. It lacks the weekly sales total (B-3), Corsland's prices (B-8), bunching below the line and fitted formats (B-9, B-10), near-line values (B-11), large retailers' value (B-12 is only premises in the core), large-shop weekday and weekly hours (B-13), small-shop workers (B-14), complements next to small shops (B-15) and small shops' own values (B-6). Each missing ban row matches a repeal key the core version also omitted or recorded differently, so the check could not catch those omissions.
  - *Habits.* The pattern version gives partial persistence in the short run for sales, Corsland, online and complements (TS-8: habits formed under the ban change over months; CR-3, CR-10b). The core version gives none throughout. The pattern version is right. A routine is a stock that changes only through flows, and the core rules give it through CR-10b.
  - *Unit size in the long run.* Pattern: none. Core: partial. The flow of refits eventually turns the stock over, but how long that takes is a premise neither states. This is a judgment call.
  - *Lobbying.* Pattern: "does not reverse in sign; n/a". Core: "full". On the repeal both signs are `ambiguous`, so there is no signed effect whose persistence could be stated. The pattern's n/a is the consistent entry.
  - *Small units.* Both give none for the premium. The core version adds that the stock of small units built under the ban persists and holds their value below the no-ban path for a while (CR-7, 0.9 persistence). That is a point the pattern version missed. It is an overshoot rather than persistence of the ban's (+) effect, and belongs in section 8.
  - *Ban rows that need care.* Both versions sign small shops' Sunday sales under the ban up for all small shops. That is the mirror of the in-centre error above, so both checks are blind to it. The pattern version's own repeal derivation (C-16) should have made it adjust B-4.
- **Test of 1.0 (the pattern version's verdicts).**
  - *CR-7 1.0, which stock (needed interpretation):* confirmed that the interpretation was needed to apply that clause. But the core version did not need the clause at all. It reached the same answer (the premium falls at once, the stock of units persists) through CR-7c, CR-10c and CR-7's 0.9 persistence clause, and so the clause's wording is the problem, as (b) 1 says.
  - *CR-8 1.0, statutory rights (needed interpretation):* confirmed. The core version did not treat small shops' advantage as a right. It used CR-9 and CR-7c on units. It used CR-8's 0.7 voiding note where it does fit, on employers' "as rostered" right under K2 (C-7), which the pattern version did not record.
  - *PC-17 for large shops (failed):* confirmed in part. Against the ban, the core version derived no wage or benefit cut for large-shop workers, and found their earnings up (C-29). But read precisely, PC-17's If clause ("absent from some contracts that would otherwise be made") already excludes large shops. So the failure lies in how the clause reads, not in its logic. And the core version shows that the right still moves terms of the new Sunday contracts under U1-a against none (C-22, as a group). The pattern version's replacement statement, that in large shops the right only narrows the option and has no consequence, is too strong.
  - *RS-17 in reverse (worked, with a reading):* confirmed for the flow and stock split (core C-16 with CR-10b). The core version, with no 0.9 value clause to prompt it, omitted near-line values (C-15).
- **Candidate patterns (6.2e).** The pattern version claims none ("None needed"). Its two new moves (a status fixed at a date: rush before and lock-in after; an option added to all competitors that can lower their joint yield) are first uses, not second uses of a 6.2e candidate. There is nothing to check against the counterfactual. Both moves are valid against the ban in force: C-24 and C-25 are signed per reading against no right, and C-18 carries A-13.
- **Limits of the core rules.** None produced a difference (K = 0). The core version's GAP-063-C1 (a right that decays with turnover) is covered by CR-1's dated operations and CR-10b with per-horizon signs, so it is not a calculus gap. The following wording caused trouble:
  - CR-12h reads as if windows may never be summed. It should point to CR-12's 0.8 two-items note for a total across windows.
  - CR-6's "a premise per margin" is easy to skip when one regulated term (the pay agreement) diverts pressure (core C-22).
  - CR-7's 1.0 which-stock clause does not cover a protected party's capital where the rivals' capacity already exists. CR-7's 0.9 persistence clause covers it.
  - CR-8's 1.0 statutory-rights note does not cover an advantage held through a restriction on others (pattern (b) 2).
  - CR-3b speaks of one actor, not a class of competitors (pattern (b) 3). Both versions handled this with A-13.
  - CR-3's note on combining lost receipts with saved outlays is phrased for producers who also sold, and was missed for sellers who lose sales to a better offer (pattern C-40).
  - `persistence` has no entry for effects of a component with no counterpart in the original rule (core (b)).
