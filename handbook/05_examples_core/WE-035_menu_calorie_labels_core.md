# WE-035 / Analysis: Calorie counts on chain restaurant menus (Sallow Menu Calorie Disclosure Act)

Analyst: core-only re-run (Handbook 0.7)  |  Rules: core rules CR-1 to CR-12 only  |  Status: awaiting comparison

## 1. Policy record

**Sallow Menu Calorie Disclosure Act.** The State of Sallow has about 14,000 restaurants. 160 chains have 20 or more outlets in the state (about 5,200 outlets, about 45% of restaurant meals). 38 chains have 10 to 19 outlets, 9 of them 17 to 19. About 25% of covered chains already post calories on menu boards and about 70% on a website. Packaged foods in shops already carry national nutrition labels, in both worlds.

| Field | Value | Source sentence |
|---|---|---|
| Jurisdiction (and what lies just outside) | State of Sallow; the neighboring State of Ambrine has no such rule. Grocery prepared-food counters inside Sallow are not "restaurants" and are not covered. | "The neighboring State of Ambrine has no such rule." L3. |
| Announced / enacted / effective / expires | Introduced 10 March 2025; passed 28 August 2025; Department of Health rules 1 December 2025; effective 1 July 2026; no expiry. | Policy record, dates paragraph. |
| Enforcement (who, penalties, resources) | County health departments, during routine inspections (about two per outlet per year): presence, format, and records. Items may be sent for laboratory testing; $400,000 of state money for tests in year one, nothing stated after. Fines: $250 per item with no count; $1,000 per item more than 20% off, per outlet; at most $10,000 per inspection. Fines go to county general funds. No added county funding. | L4. |

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| L1 Disclosure | `disclosure_mandate` | Calorie content of each "standard menu item" | Chains with 20 or more outlets in Sallow under the same name with substantially the same menu, counting franchised outlets | Count next to each item on every menu and menu board, including drive-through boards, in type no smaller than the price, with the 2,000-calorie statement; combination meals as a range | L3 |
| L2 Accuracy | Condition of L1 (and of voluntary posting under L3) | Declared counts | Covered chains; exempt restaurants that post voluntarily | "Reasonable basis" (laboratory, nutrient database or recipes) kept on file; actual content within 20% of the declared count | — |
| L3 Exemptions | Exemption | — | — | Fewer than 20 outlets (voluntary posting then brings L2); condiments for general use; daily specials; "items appearing on the menu for a limited time" (U1); grocery prepared-food counters | — |
| L4 Enforcement | Enforcement | L1, L2 | County health departments | As above | — |

Compliance costs in the record: nutrient database about $60 per item, laboratory about $600 per item; 80 to 150 standard items per typical chain; boards $1,500 to $4,000 per outlet, normally replaced every three to five years and on major menu changes. One-time cost about $5,500 per outlet for a 20-outlet chain with 100 lab-analyzed items, about $2,600 per outlet for a 500-outlet chain (almost all boards). Each new item adds analysis and a board change at every outlet.

Counterfactual law (CR-1, Recording): no state calorie rule; chains and independents may post counts or not, with no state accuracy tolerance or record requirement; national packaged-food labels in force.

Unclear provisions:
- **U1: "items appearing on the menu for a limited time".** U1-a (department's draft guidance): only items offered two weeks or less are exempt; seasonal items of six to twelve weeks must be analyzed and posted. U1-b (industry comments): any item offered under 90 days a year is exempt. The final rule gives no number and there is no inspection practice, so this is a reading, not an assumption.

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | CR-1 operations | Core rules applied |
| --- | --- | --- | --- | --- |
| L1 Disclosure | triangular (prescribes a term of the sale between chain and buyer) | Yes for the 75% of covered chains that do not post on boards (A-1); format-only for the 25% that do | 1 (offering a standard item without a posted count is removed where enforced); 3 (analysis, board, format and record costs attached to the option 'offer a standard item at a covered outlet', and a fine risk where enforcement is incomplete). For buyers: no operation; the counts work through CR-11c (CR-1 clarification) | CR-1, CR-3a, CR-4 (incl. fixed costs per item), CR-8c, CR-9, CR-10a, CR-11c |
| L2 Accuracy | triangular (condition of L1) | Binds where counts are off by more than 20% (A-2: most are not) and through the risk of a check (A-8) | 3 (fine risk and record-keeping attached to declaring a count) | CR-4 (x: comply, y: violate; x: present portion control, y: tighter), CR-8b, CR-8c |
| L3 Exemptions | defines the boundary of L1; attaches L2 to voluntary posting | Yes: the 20-outlet line binds for chains near it (A-9, A-10); U1 binds per reading | 3 (the compliance cost is attached to the option 'operate a 20th outlet under the same name and menu'); 3 (L2 liability attached to the option 'post voluntarily' for exempt restaurants, against a counterfactual with no state tolerance) | CR-4 (x: covered form, y: exempt form; x: post voluntarily, y: do not), CR-7c, CR-10c |
| L4 Enforcement | binary (state budget and county inspection time used; fines collected) | Yes for inspection time; lab budget year one only | 4 ($400,000 from the state budget to testing); 3 (fines attached to violation); for counties, a task attached with no funding (A-15) | CR-8a, CR-8b, CR-8c, CR-3c |

The instrument `disclosure_mandate` is in `02_ontology.md` 2.3; the input's note that it is missing is out of date (Gaps found, c).

## 3. Actor classes

| Actor class | Role | How its options change (CR-1) |
| --- | --- | --- |
| chains.covered.not_posting | Covered chains (franchisors and franchisees) not now posting on boards (about 75%, A-1) | Op 1 and op 3: must analyze every standard item and change boards at every outlet by 1 July 2026; ongoing per-item cost. |
| chains.covered.posting | Covered chains already posting on boards (about 25%) | Op 3: format, range for combinations, records, L2 liability. |
| chains.covered.small | Covered chains with roughly 20 to 50 outlets | As above, with higher cost per outlet (record arithmetic). |
| chains.near_threshold | The 38 chains with 10 to 19 outlets, especially the 9 with 17 to 19 | Op 3 on the option 'open the 20th outlet under the same name and menu' (A-9); a second brand becomes relatively better (A-10). |
| restaurants.exempt | Independents and chains under 20 outlets | No direct operation on what they do now; op 3 on voluntary posting (L2 attached). Through CR-9 (substitute): compete with covered chains. |
| buyers.current | Buyers at covered chains | No operation; counts at the point of order (CR-11c). Through CR-9: menus with fewer or reformulated items. |
| buyers.exempt_restaurants | Buyers at exempt restaurants | Through CR-9 (substitute): situation changes only through restaurants' responses. |
| input_suppliers.nutrient_analysis | Laboratories, nutrient-database consultants (A-13) | Through CR-9 (input_to): more orders. |
| input_suppliers.menu_boards | Sign and menu-board makers | Through CR-9 (input_to) and CR-10a: orders bunched before 1 July 2026. |
| officials.county_health | County health departments | Op 3: a new inspection task with no added funding (A-15). |
| counties.general_funds | County budgets | Op 4: receive fine revenue (CR-8b). |
| taxpayers.state, recipients_of_other_state_spending | Fund the $400,000 lab budget | Op 4 (CR-8 clarification: payers from the general budget). |
| chains_associations | State restaurant association representing chains (A-11) | CR-4 (x: accept, y: lobby) on U1, the threshold, enforcement. |
| independents_associations | Associations of independent restaurants (A-11) | CR-4 (x: accept, y: lobby); stake only through the boundary (see section 6 notes). |
| sellers.substitutes (grocery prepared-food counters) | Exempt substitute outside "restaurant" | Through CR-9 (substitute) only under A-18 (p 0.35, not reported). |
| neighboring_jurisdictions (Ambrine chains and buyers) | Across the border | Through CR-9 (across_border); no signed chain (section 6 notes). |

## 4. Direct effect

CR-1 and CR-2: the immediate change for those whose situation L1, L2 and L4 alter.

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-1 | chains.covered.not_posting | compliance_cost (item analysis and board changes before 1 July 2026) | increase | short | CR-1 op 1 and op 3, CR-2, CR-8c | A-1 |
| C-2 | chains.covered | compliance_cost (format, records, analysis of each new item) | increase | short; medium; long | CR-1 op 3, CR-4 (x: database, y: laboratory), CR-8c | none |
| C-3 | buyers.current | quality_information (calorie counts at the point of order) | increase | short; medium; long | CR-11c, CR-1 | A-1 |
| C-4 | officials.county_health | enforcement_cost | increase | short; medium; long | CR-1 op 3, CR-8c | none |
| C-5 | taxpayers.state, recipients_of_other_state_spending | resources_available_other_uses | at_least_one_decrease | short (year one) | CR-8b, CR-8a | none |

## 5. Responses

CR-4 applied to every pair of options each actor class has; CR-11c for the information; CR-10a for timing.

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-6 | buyers.current | quantity_demanded (higher-calorie items at covered chains) | decrease | short; medium; long | CR-11c, CR-4, CR-12e | A-1, A-3, A-4 |
| C-7 | buyers.current | product_attribute (calories per item bought at covered chains, sales-weighted) | decrease | short; medium; long | CR-11c, CR-4, CR-12a | A-1, A-3, A-4 |
| C-8 | buyers.current | search_cost (finding counts before ordering) | decrease | short; medium; long | CR-11c, CR-8a | A-1 |
| C-9 | chains.covered | product_attribute (calories of items offered: lighter versions) | decrease | medium; long | CR-9, CR-4 (x: keep recipe, y: lighter version) | A-1, A-3, A-4, A-5 |
| C-10 | chains.covered | variety (standard menu items) | decrease | short; medium; long | CR-4 (fixed cost per item; x: offer, y: drop), CR-4b, CR-10a | A-6 |
| C-11 | chains.covered | variety (seasonal items offered two weeks to 90 days) | U1-a: decrease; U1-b: no_change | short; medium; long | CR-1 op 3 per reading, CR-4 (fixed cost per item) | A-6 |
| C-12 | chains.covered | reclassification (new items launched as limited-time offers) | U1-a: no_change; U1-b: increase | medium; long | CR-4 (x: covered form, y: exempt form) | A-7 |
| C-13 | chains.covered | quality_variability (calorie content between servings of an item) | decrease | medium; long | CR-1 op 3 (L2), CR-4 (x: present portion control, y: tighter) | A-8, A-N3 |
| C-14 | chains.covered | legal_breach (counts more than 20% off, detected) | increase | medium | CR-4 (x: comply, y: violate), CR-1 op 3 | A-17 |
| C-15 | chains.near_threshold | entry_rate (20th and later outlets under the same name and menu) | decrease | medium; long | CR-4 (lumpy cost; x: stay at 19, y: open 20th), CR-10a | A-9 |
| C-16 | chains.near_threshold | reclassification (second brand or distinct menu for new outlets) | increase | medium; long | CR-4 (x: covered form, y: exempt form) | A-10 |
| C-17 | chains.near_threshold | asset_value (chain businesses) | decrease | short (from passage) | CR-7c, CR-10c | A-9 |
| C-18 | chains_associations | lobbying_effort (U1-b reading, threshold, enforcement) | increase | short; medium | CR-4 (x: accept, y: lobby), CR-8c | A-11 |
| C-19 | restaurants.exempt | quality_information (counts posted voluntarily) | ambiguous | medium; long | CR-12b | A-N2, A-12 |
| C-20 | chains.covered | asset_value (chain businesses) | ambiguous | short (from introduction and passage) | CR-12b, CR-7c, CR-10c | A-12 |

## 6. Second-order effects

CR-9 along named relations, then CR-5 to CR-7 in each market reached. Depth limit 4.

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C-21 | input_suppliers.nutrient_analysis | quantity_traded (nutrient analyses and laboratory tests) | increase | short; medium | CR-9, LW-10 | analysis input_to compliance with L1 and L2 (close) | A-13 |
| C-22 | input_suppliers.menu_boards | quantity_traded (menu boards, 28 Aug 2025 to 30 Jun 2026) | increase | short | CR-10a, CR-9, LW-10 | boards input_to compliance with L1 (close) | A-1, A-14 |
| C-23 | input_suppliers.menu_boards | quantity_traded (menu boards, years after 1 Jul 2026) | ambiguous | medium; long | CR-12b, CR-10a, CR-9 | boards input_to compliance with L1 (close) | A-14, A-6 |
| C-24 | chains.covered | quantity_traded (meals at covered chains) | ambiguous | medium; long | CR-12b | covered chain meals substitute for exempt restaurant meals (close) | A-12, A-N1 |
| C-25 | restaurants.exempt | quantity_demanded (meals at exempt restaurants) | ambiguous | medium; long | CR-12b, CR-9 | exempt restaurant meals substitute for covered chain meals (close) | A-12, A-N1 |
| C-26 | chains.covered.small | tax_share_borne (compliance cost per outlet, relative to large covered chains) | increase | short; medium; long | CR-7b, CR-12e (arithmetic) | same_market_other_segment (small and large covered chains) | none |
| C-27 | counties.general_funds | non_tax_receipts (fines) | increase | medium | CR-8b | — | A-17 |
| C-28 | chains.covered | resources_available_other_uses | decrease | short; medium; long | CR-3c, CR-8a, CR-8b | — | none |
| C-29 | officials.county_health | enforcement_cost (other inspection tasks) | decrease | short; medium; long | CR-8a, CR-3c | — | A-15 |

**Relations checked (CR-9).** Exchange: buyers (CR-11c chains), input suppliers (C-21 to C-23), exempt restaurants as substitutes (C-24, C-25), grocery counters as substitutes (A-18, p 0.35, not reported). Contract: franchise agreements between franchisors and franchisees decide who pays for boards and analysis; CR-5c and CR-7b say the split moves within the contract range but no premise ranks the sides, so no share is signed (existing contracts count as fixed terms while they last, CR-6 clarification). Currency: none of note (a state measure on domestic meals). Shared facility, proximity, gift: no relation found. Across border: chains with outlets in Ambrine may use one board design in both states, and Sallow buyers near the border could eat in Ambrine; no premise gives a direction for either, so no consequence (Tier C note).

**Depth.** Buyers' response (C-6) to reformulation (C-9) to input suppliers (not followed: recipe development is internal, A-5) stops at depth 3. Lab budget: state taxpayers (C-5) to laboratories (C-21) is depth 2.

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance premise | Combined sign |
|---|---|---|---|---|
| restaurants.exempt, quality_information (voluntary counts), medium; long | Buyers prefer restaurants with counts (A-12), so posting wins some back (CR-4, y: post, made better) | L3 attaches L2's tolerance, records and fines to voluntary posting, so some who would have posted do not (CR-1 op 3, CR-4b; A-N2) | None stated | ambiguous (C-19) |
| chains.covered, asset_value, short | Buyers prefer covered chains for the counts (A-12; CR-7c) | Compliance costs lower expected yields (C-1, C-2; CR-7c, CR-10c) | None stated | ambiguous (C-20) |
| input_suppliers.menu_boards, quantity_traded, after 1 Jul 2026 | A board change at every outlet for each new item (record) | Replacements pulled into 2025-26 are not repeated in the normal cycle (A-14); fewer new items (C-10, A-6) | None stated | ambiguous (C-23) |
| chains.covered, quantity_traded (meals), medium; long | Buyers who value counts move from exempt restaurants (A-12) | Buyers of dropped items, or who learn a count and rank a meal elsewhere next, leave (A-N1) | None stated | ambiguous (C-24) |
| restaurants.exempt, quantity_demanded, medium; long | Buyers leaving covered chains (A-N1) | Buyers moving to covered chains for counts (A-12) | None stated | ambiguous (C-25) |
| buyers.current, product_attribute (calories per item bought) | — | Buyers' mix shifts (C-7, A-4); items reformulated lighter (C-9, A-5) | Same direction (CR-12a) | decrease (C-7) |
| chains.covered, resources_available_other_uses | — | Compliance costs paid (C-1, C-2; no premise); fines paid (C-14, A-17) | Same direction; independent chains (CR-12d): holds without A-17 | decrease (C-28) |
| chains.covered, variety | — | Low-volume items dropped (C-10); under U1-a seasonal items dropped too (C-11) | Same direction | decrease (C-10); C-11 per reading |

No chains cancel by construction (CR-12f).

## 8. Time structure

- **Announcement (10 March 2025) and passage (28 August 2025).** Expected compliance costs lower the value of covered chains and of near-threshold chains' growth from when the Act became expected, partly at introduction and more at passage (CR-7c, CR-10c; C-17, C-20). Near-threshold chains hold back a 20th outlet from passage (CR-10a; C-15).
- **Window to 1 July 2026.** Chains not posting must analyze items and change boards before the effective date (C-1). Board purchases are brought forward from the normal three-to-five-year cycle (A-14). Signed per window against the counterfactual: boards bought in 28 Aug 2025 to 30 Jun 2026, increase (C-22); after 1 July 2026, ambiguous (C-23). Items a chain expects to drop are dropped before analysis is bought (CR-10a; C-10 short). The pulled-forward replacement is a transition effect; `persistence` n/a (not a repeal).
- **Rule-making (to 1 December 2025) and after.** The final rule leaves U1 open; inspection practice will settle it. Lobbying for U1-b (C-18) continues until it does. Chains' launch practice (C-12) and seasonal menus (C-11) follow the reading inspectors adopt.
- **Lab budget.** $400,000 in year one, nothing stated after. If counties stop sending items for testing after year one, the risk attached to inaccurate counts falls (CR-4), and C-13 and C-14 weaken in the long run; no sign is claimed for after year one beyond what A-8 states.
- **Durability.** Analysis of existing items is a one-time stock; the lasting cost is per new item (C-2 long), which bears on which items are offered (C-10), not on the unit price (CR-4 clarification, fixed costs per item). No unit-price consequence is signed.
- **Learning.** Buyers who see counts once retain them (CR-10b: knowledge is a stock), so the shift in C-6 and C-7 does not need repeated exposure; no sign change over time is claimed.

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
| --- | --- | --- | --- | --- | --- |
| C-1 | chains.covered.not_posting | compliance_cost (item analysis and board changes before 1 July 2026) | increase | About $2,600 to $5,500 per outlet of analysis and boards that would have served other ends | CR-1 op 3, CR-8c |
| C-2 | chains.covered | compliance_cost (format, records, analysis of each new item) | increase | Staff time, records and analysis for every new item | CR-1 op 3, CR-8c |
| C-4 | officials.county_health | enforcement_cost | increase | Inspection time spent checking counts | CR-1 op 3, CR-8c |
| C-29 | officials.county_health | enforcement_cost (other inspection tasks) | decrease | Other inspection work not done with unchanged budgets | CR-8a, CR-3c |
| C-5 | taxpayers.state, recipients_of_other_state_spending | resources_available_other_uses | at_least_one_decrease | $400,000 of other state spending or taxpayers' purchases | CR-8b, CR-8a |
| C-10 | chains.covered | variety (standard menu items) | decrease | Low-volume items buyers would have bought | CR-4, CR-3a |
| C-18 | chains_associations | lobbying_effort (U1-b reading, threshold, enforcement) | increase | Staff time and money spent lobbying | CR-4, CR-8c |
| C-28 | chains.covered | resources_available_other_uses | decrease | Compliance costs and fines paid | CR-3c, CR-8a, CR-8b |

CR-8b both sides: fines paid (C-28) are county receipts (C-27); the state lab budget (C-5) is laboratory receipts (C-21); payments for analysis and boards (C-1, C-2) are receipts of input suppliers (C-21, C-22).

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
| --- | --- | --- | --- | --- | --- |
| A-1 | Most covered chains do not now post counts on boards, and most of their buyers do not look counts up before ordering. | binding | 0.8 | 25% post on boards; website traffic to nutrition pages against meals sold. | C-1, C-3, C-6, C-7, C-8, C-9, C-22 fail or lose this chain. |
| A-2 | Posted counts are within the tolerance for most items. | enforcement | 0.7 | Database methods; error rates in audits of voluntarily posted counts. | Used only as context for C-13 and C-14 (some items are outside tolerance); no consequence rests on it alone. |
| A-3 | Some buyers' beliefs about calorie content differ from the posted counts. | other | 0.75 | Surveys of estimated against actual calories. | C-6, C-7, C-9 fail. |
| A-4 | Among buyers whose choices change, more move away from higher-calorie items than toward them (dominance premise). | other | 0.6 | Direction of estimation errors; stated preferences; sales mix at chains that posted voluntarily. | C-6, C-7, C-9 become ambiguous. |
| A-5 | For some items, a lighter version costs less than the sales it would keep. | other | 0.6 | Recipe-development costs; reformulation at chains that posted voluntarily. | C-9 fails. |
| A-6 | The per-item fixed cost is material relative to the contribution of a chain's lowest-volume items. | other | 0.65 | Record's costs against sales of the bottom tenth of items. | C-10, C-11 fail; C-23 loses a chain. |
| A-7 | Under U1-b, chains can present new items as limited-time offers at low cost. | other | 0.6 | Share of limited-time items in launches. | C-12 (U1-b) fails. |
| A-8 | Chains expect some accuracy checks, or a cost to reputation from wrong counts. | enforcement | 0.6 | Lab budget; press coverage of audits elsewhere. | C-13 fails. |
| A-9 | For some near-threshold chains, the compliance cost reverses the ranking of opening a 20th outlet. | other | 0.65 | About $110,000 against typical outlet profit; growth plans of the 9 chains. | C-15, C-17 fail. |
| A-10 | For some small chains, a second brand costs less than compliance. | other | 0.55 | Branding and menu-development costs; "substantially the same menu" test. | C-16 fails. |
| A-11 | Chains' and independents' associations can organize at a cost below their stake. | other | 0.75 | Existing state restaurant association; hearing testimony. | C-18 fails. |
| A-12 | Some buyers value the counts enough to prefer a covered chain over an exempt restaurant. | other | 0.6 | Surveys of buyers' use of counts; chains' reasons for posting voluntarily. | C-19, C-20, C-24, C-25 lose their (+)/(−) chain and take the other chain's sign. |
| A-13 | Many chains buy analysis from outside laboratories or consultants. | other | 0.8 | Industry practice; hearing testimony. | C-21 fails. |
| A-14 | Boards are replaced every few years without the Act. | durability | 0.8 | Industry replacement cycles. | C-22 holds (no pull-forward, just extra purchases); C-23 loses its pull-forward chain. |
| A-15 | County inspection budgets are not raised for the new task. | revenue_use | 0.65 | No appropriation; county budget calendars. | C-29 fails (the cost falls on county taxpayers instead). |
| A-16 | Exempt restaurants post counts voluntarily because buyers read silence as a bad sign. | other | 0.4 | Voluntary posting by independents where chains post. | Not reported (below 0.5). |
| A-17 | Some inaccurate counts are detected and fined. | enforcement | 0.55 | Lab budget; inspection frequency. | C-14, C-27 fail; C-28 keeps its compliance chain. |
| A-18 | Buyers who dislike seeing counts shift to grocery prepared-food counters. | substitutability | 0.35 | No evidence beyond anecdote. | Not reported (below 0.5). |
| A-N1 | Some buyers of items a covered chain drops, or who after seeing a count rank a meal elsewhere next, go to another restaurant (including exempt ones) rather than another item at the same chain. | substitutability | 0.6 | NEW. Restaurant density (14,000 restaurants, 55% of meals exempt); C-10 removes items; A-3 implies some buyers learn their usual order is heavier than they thought. | C-24, C-25 lose their opposing chain and take A-12's sign. |
| A-N2 | Some exempt restaurants are near the margin of posting counts voluntarily: some would post without the Act, and some would post to win back buyers. | other | 0.6 | NEW. 25% of covered chains post voluntarily today; small chains with websites; A-12. | C-19 is not reported. |
| A-N3 | For some items, actual calorie content varies between servings by enough that portion control matters for staying within 20%. | other | 0.6 | NEW. A-2 says most items, not all, are within tolerance; variation in hand-portioned items. | C-13 fails. |

**Not reported** (an assumption below 0.5, or no premise):
- Exempt restaurants post counts because buyers read silence as a bad sign (CR-11c silence clarification): needs A-16 (p 0.4). Would add a (+) chain to C-19, which is already ambiguous.
- Buyers who dislike counts move to grocery prepared-food counters (CR-4, CR-9 substitute): needs A-18 (p 0.35).
- Chains with just over 20 outlets close or rebrand outlets to fall below the line before 1 July 2026 (CR-4, symmetric to C-15): no case premise; not estimated.
- Items presented as daily specials to use that exemption (CR-4, both readings): no case premise; not estimated.
- Price of laboratory analysis rises in the 2025-26 window (CR-6, demand bunched against fixed lab capacity): no premise on lab capacity.
- Unit menu prices at covered chains: per-item and per-outlet fixed costs bear on which items and outlets are offered, not on the unit price (CR-4 clarification); no sign.

## 11. Report

**The policy:** From 1 July 2026, restaurant chains with 20 or more outlets in Sallow must show the calorie count of every standard item next to the item on every menu and board, in type as large as the price, with a 2,000-calorie statement. Counts must have a documented basis and be within 20% of actual content. Smaller restaurants, daily specials, condiments and "limited-time" items are exempt; what "limited time" means is unsettled (two weeks, or under 90 days). County inspectors check during routine inspections, with $400,000 of state money for lab tests in year one and fines of $250 to $1,000 per item, up to $10,000 per inspection, paid to counties.

**Visible consequences:** Buyers at covered chains see counts when they order (C-3), and fewer higher-calorie items are bought (C-6), so the calories per item bought fall (C-7). Covered chains pay for analysis, new boards and records (C-1, C-2). Counties spend inspection time on the task (C-4).

**Invisible consequences:**
- *Covered chains:* drop low-volume items (C-10), and under the narrow reading of "limited time" also seasonal items (C-11); under the broad reading they launch more items as limited-time offers instead (C-12). They reformulate some items lighter (C-9) and tighten portion control (C-13). Some counts are found wrong and fined (C-14, C-27). Small covered chains bear more cost per outlet than large ones (C-26). They have less for other uses (C-28) and lobby over the reading and the threshold (C-18).
- *Chains near the threshold:* open fewer 20th outlets (C-15), set up second brands instead (C-16), and their businesses lose value from passage (C-17).
- *Buyers:* those who looked counts up spend less effort doing so (C-8).
- *Suppliers:* laboratories and consultants sell more analysis (C-21); board makers sell more boards before July 2026 (C-22).
- *Public budgets:* the lab budget comes out of other state spending or taxpayers' purchases (C-5); with unchanged budgets, other inspection work falls (C-29).

**Ambiguous effects:** Meals sold at covered chains and at exempt restaurants (C-24, C-25): buyers who value counts move toward covered chains, while buyers of dropped items, and some who see their usual order's count, move away. Voluntary posting by exempt restaurants (C-19): the accuracy liability deters it, competition for count-seeking buyers encourages it. Covered chains' business values (C-20): compliance costs against buyers' preference for counts. Board purchases after July 2026 (C-23): pulled-forward replacements and fewer new items against a board change for every new item. What would decide each: the size of the competing flows of buyers, the cost of voluntary compliance against the buyers it wins, and the rate of new items against the replacement cycle.

**Key conditions:** Most chains do not now post and most buyers do not look counts up (A-1, 0.8); some buyers' beliefs are wrong (A-3, 0.75) and more move away from heavier items than toward them (A-4, 0.6); per-item costs matter for the lowest-volume items (A-6, 0.65); the compliance cost reverses the 20th-outlet decision for some (A-9, 0.65); some wrong counts are caught (A-17, 0.55). Three premises were added: buyers who leave a covered chain's item can go elsewhere (A-N1, 0.6), some exempt restaurants are near the margin of posting (A-N2, 0.6), and serving-to-serving variation matters for the tolerance (A-N3, 0.6).

**What this analysis cannot say:** How large any effect is; whether buyers end up eating fewer calories in total (meals elsewhere are not counted); and whether buyers are better off (the counts change beliefs, not options, and the method has no rule for valuing that). Health effects, including weight and nutrient intake, are out of scope. Effects in Ambrine and on unit prices are not signed. It does not weigh compliance costs against buyers' information or say whether the policy is good.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C-1 | chains.covered.not_posting | compliance_cost (item analysis and board changes before 1 July 2026) | increase | short | visible | A | CR-1 (op 1: offering a standard item without a count is removed; op 3: analysis and boards attached to offering it); CR-2 (they keep offering their items, since dropping most of a menu ranks lower); CR-8c (resources spent on complying are used up). A-1 states the class is most covered chains | A-1 |
| C-2 | chains.covered | compliance_cost (format, records, analysis of each new item) | increase | short; medium; long | visible | A | CR-1 (op 3: format, records and L2 basis attached to every standard item; each new item adds analysis and a board change at every outlet); CR-4 (x: database at $60, y: laboratory at $600; L2's fine risk makes y better for some items); CR-8c | none |
| C-3 | buyers.current | quality_information (calorie counts at the point of order) | increase | short; medium; long | visible | B | CR-1 (L1 makes chains show counts); CR-11c (a policy can change actions by conveying information): buyers who did not look counts up (A-1) now see them | A-1 |
| C-4 | officials.county_health | enforcement_cost | increase | short; medium; long | visible | A | CR-1 (op 3: checks of presence, format and records added to routine inspections; lab referrals); CR-8c (resources spent enforcing are used up) | none |
| C-5 | taxpayers.state, recipients_of_other_state_spending | resources_available_other_uses | at_least_one_decrease | short (year one) | invisible | A | CR-8b (the $400,000 lab budget is paid by someone; CR-8 clarification: payers from the general budget recorded as a group); CR-8a | none |
| C-6 | buyers.current | quantity_demanded (higher-calorie items at covered chains) | decrease | short; medium; long | visible | B | CR-11c (counts change beliefs of buyers whose beliefs differed, A-3, among those who did not look them up, A-1); CR-4 (for buyers who learn an item is heavier than thought, x: that item is worse by their own ranking; for those who learn it is lighter, better); CR-12e (A-4: more move away from heavier items than toward them) | A-1, A-3, A-4 |
| C-7 | buyers.current | product_attribute (calories per item bought at covered chains, sales-weighted) | decrease | short; medium; long | visible | B | As C-6 (CR-11c, CR-4, CR-12e with A-4); CR-12a: reformulation (C-9) pushes the same way | A-1, A-3, A-4 |
| C-8 | buyers.current | search_cost (finding counts before ordering) | decrease | short; medium; long | invisible | B | CR-11c (counts shown at the point of order); CR-8a (time those buyers spent looking counts up on websites, A-1: a minority did, is freed) | A-1 |
| C-9 | chains.covered | product_attribute (calories of items offered: lighter versions) | decrease | medium; long | invisible | B | CR-9 (buyers' shift away from heavier items, C-6, changes sellers' situation); CR-4 (x: keep the recipe, y: a lighter version; y made relatively better where it keeps sales at less than its cost, A-5) | A-1, A-3, A-4, A-5 |
| C-10 | chains.covered | variety (standard menu items) | decrease | short; medium; long | invisible | B | CR-4 clarification (a fixed cost per item offered bears on which items are offered: x: offer it, y: drop it); CR-4b (items whose contribution is below the per-item cost, A-6, are dropped); CR-4a (none is added because of the cost); CR-10a (drops before analysis is bought); fewer new items for the same reason | A-6 |
| C-11 | chains.covered | variety (seasonal items offered two weeks to 90 days) | U1-a: decrease; U1-b: no_change | short; medium; long | invisible | B | U1-a: CR-1 (op 3: seasonal items need analysis and a board change at every outlet) and CR-4 clarification (fixed cost per item; A-6 applies with more force to items sold for weeks); U1-b: items under 90 days are exempt, so no operation on them | A-6 |
| C-12 | chains.covered | reclassification (new items launched as limited-time offers) | U1-a: no_change; U1-b: increase | medium; long | invisible | B | U1-b: CR-4 (x: launch as a standard item, covered; y: launch as an offer under 90 days, exempt; y made relatively better, and A-7 says it is cheap to do); U1-a: the 90-day route is not exempt, so the operation does not exist | A-7 |
| C-13 | chains.covered | quality_variability (calorie content between servings of an item) | decrease | medium; long | invisible | B | CR-1 (op 3: L2 attaches fines to counts more than 20% off); CR-4 (x: present portion control, y: tighter; y made better where checks are expected, A-8, and serving variation matters, A-N3) | A-8, A-N3 |
| C-14 | chains.covered | legal_breach (counts more than 20% off, detected) | increase | medium | invisible | B | CR-1 (L2 creates the rule; without it there is no breach); CR-4 (x: comply, y: violate, where accuracy costs more than the expected fine); A-17: some are caught | A-17 |
| C-15 | chains.near_threshold | entry_rate (20th and later outlets under the same name and menu) | decrease | medium; long | invisible | B | CR-1 (op 3: the whole compliance cost attaches to the 20th outlet); CR-4 (lumpy cost: every chain whose ranking of 'open' over 'stay at 19' is reversed, A-9, stays at 19); CR-4a (none opens because of the cost); CR-10a (from passage) | A-9 |
| C-16 | chains.near_threshold | reclassification (second brand or distinct menu for new outlets) | increase | medium; long | invisible | B | CR-4 (x: grow under one name and menu, covered; y: a second brand or distinct menu, not "substantially the same", exempt; y cheaper than compliance for some, A-10) | A-10 |
| C-17 | chains.near_threshold | asset_value (chain businesses) | decrease | short (from passage) | invisible | B | CR-10c (value reflects expected yields); CR-7c (the lower expected yield of growth, whether by bearing the cost, staying small or rebranding, A-9, is borne by owners when the Act becomes expected, partly at introduction and more at passage) | A-9 |
| C-18 | chains_associations | lobbying_effort (U1-b reading, threshold, enforcement) | increase | short; medium | invisible | B | CR-4 (x: accept the narrow reading and the costs, y: lobby; U1 leaves the reading open, so y gains); CR-8c (resources spent lobbying are used up); A-11 | A-11 |
| C-19 | restaurants.exempt | quality_information (counts posted voluntarily) | ambiguous | medium; long | invisible | B | CR-12b: (−) CR-1 (op 3: L3 attaches L2 to voluntary posting, against a counterfactual with no state tolerance) and CR-4b (those who would have posted and were near the margin do not, A-N2); (+) CR-9 and CR-4 (x: stay silent, y: post; y made better because some buyers prefer restaurants with counts, A-12). No premise says which dominates | A-N2, A-12 |
| C-20 | chains.covered | asset_value (chain businesses) | ambiguous | short (from introduction and passage) | invisible | B | CR-12b: (−) CR-7c and CR-10c (compliance costs, C-1, C-2, lower expected yields); (+) CR-7c with CR-9 (buyers who value counts move from exempt restaurants, A-12). No premise says which dominates | A-12 |
| C-21 | input_suppliers.nutrient_analysis | quantity_traded (nutrient analyses and laboratory tests) | increase | short; medium | invisible | B | CR-9 and LW-10 (demand for an input follows demand for what it serves; relation: analysis input_to compliance); chains buy it outside (A-13); second chain: the state lab budget (CR-8b, C-5) | A-13 |
| C-22 | input_suppliers.menu_boards | quantity_traded (menu boards, 28 Aug 2025 to 30 Jun 2026) | increase | short | invisible | B | CR-9 and LW-10 (relation: boards input_to compliance); CR-10a (the deadline brings replacements forward, A-14, and adds them where the cycle would not have reached, A-1) | A-1, A-14 |
| C-23 | input_suppliers.menu_boards | quantity_traded (menu boards, years after 1 Jul 2026) | ambiguous | medium; long | invisible | B | CR-12b: (−) CR-10a (replacements pulled into 2025-26 are not repeated in the normal cycle, A-14); (−) CR-9 (fewer new items, C-10, A-6); (+) CR-1 (each new item needs a board change at every outlet). No premise says which dominates | A-14, A-6 |
| C-24 | chains.covered | quantity_traded (meals at covered chains) | ambiguous | medium; long | invisible | B | CR-12b: (+) CR-9 and CR-4 (relation: substitute; buyers who value counts move from exempt restaurants, A-12); (−) CR-3a and CR-4 (buyers of dropped items, C-10, and some who see a count, C-6, rank a meal elsewhere next, A-N1). No premise says which dominates | A-12, A-N1 |
| C-25 | restaurants.exempt | quantity_demanded (meals at exempt restaurants) | ambiguous | medium; long | invisible | B | CR-12b: mirror of C-24 along the substitute relation: (−) A-12; (+) A-N1. No premise says which dominates | A-12, A-N1 |
| C-26 | chains.covered.small | tax_share_borne (compliance cost per outlet, relative to large covered chains) | increase | short; medium; long | invisible | A | CR-12e (arithmetic on the record: about $5,500 per outlet at 20 outlets against about $2,600 at 500; per-item analysis is spread over fewer outlets); CR-7b (gross burden per outlet; net burden not signed) | none |
| C-27 | counties.general_funds | non_tax_receipts (fines) | increase | medium | invisible | B | CR-8b (fines paid by chains are receipts of county general funds); A-17: some fines are imposed | A-17 |
| C-28 | chains.covered | resources_available_other_uses | decrease | short; medium; long | invisible | A | CR-3c and CR-8a (chains keep offering their menus and pay the compliance costs, C-1, C-2, so these sums are withdrawn from other uses); CR-8b (fines paid, A-17, a second independent chain); CR-12d: the first chain holds alone | none |
| C-29 | officials.county_health | enforcement_cost (other inspection tasks) | decrease | short; medium; long | invisible | B | CR-8a and CR-3c (inspection time spent on counts, C-4, is withdrawn from other tasks when budgets are not raised, A-15) | A-15 |

## Gaps found

**(a) Steps no core rule covers.**
- GAP-035-C1: Whether buyers who change their order after seeing a count are better or worse off. CR-3 is stated over options; a disclosure adds no option and removes none (CR-1 clarification), so CR-3a and CR-3b are silent. The analysis signs only behavior (C-6, C-7) and information (C-3), not the buyers' position.
- GAP-035-C2: Whether total meals bought fall, or only their mix changes. C-6 and C-7 follow from A-4; whether buyers who move away from heavier items stay at the chain, go elsewhere or eat less needs premises the rules cannot supply, and the method has no variable for total meals across restaurants. Recorded as the ambiguity in C-24 and C-25.

**(b) Core-rule wording that was hard to apply.**
- CR-4 clarification on fixed costs per item says such costs bear on which items are offered, "not on the price of each unit sold". Board costs are per outlet, not per item, and a cost per outlet is a cost of operating the outlet; it is unclear whether the same clarification covers it, or whether a long-run unit-price effect through fewer outlets should be derived. Left unsigned.
- CR-1 Recording asks for the counterfactual law. Whether L3's attaching L2 to voluntary posting is an operation depends on whether general false-advertising law already exposed voluntary counts to liability; the record is silent. Treated as op 3 against a counterfactual with no state tolerance (C-19).
- CR-12 clarification on opposing chains "that cannot be derived from the rules": the movement of buyers from covered chains to other restaurants is derivable from CR-4 but needs a premise not in the case (A-N1). The clarification does not say whether such a chain, once its premise is added, should make the consequence ambiguous (done here) or stay a Tier C note.
- CR-7b with a mandate rather than a tax: the per-outlet comparison between small and large chains (C-26) uses `tax_share_borne` as gross cost per outlet; the rule's incidence wording concerns buyers and sellers, not two segments of sellers.
- CR-11c clarification "what a sign needs": applied with A-3 (beliefs before) and A-4 (direction). A-4 is a dominance premise over two groups moving in opposite directions; CR-12e covers it, but CR-11c does not say so.

**(c) Vocabulary missing from the ontology.**
- No variable for the share of sellers who disclose voluntarily; `quality_information` was used (C-19).
- No variable for new product introductions or the rate of menu change; `variety` was used (C-10, C-11).
- No variable for the number of outlets per chain or for growth across a size threshold; `entry_rate` was used (C-15).
- No actor class for franchisees as distinct from franchisors, nor a relation type for franchise agreements beyond `contract`; the split of compliance cost was left unsigned.
- `tax_share_borne` is defined for "a tax's (or a mandate's) burden"; a per-outlet comparison between seller segments fits loosely.
- The input record notes that `disclosure_mandate` is missing from 2.3; it is now listed there (with CR-11c as its rule family), so that note is out of date.
- Nutrient intake and health remain out of scope, so the policy's stated purpose cannot be scored.
