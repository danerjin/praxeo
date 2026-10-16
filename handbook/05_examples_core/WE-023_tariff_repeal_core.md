# WE-023 / Analysis: Repeal of a lumber tariff

Analyst: core-only re-run (Handbook 0.4)  |  Rules: core rules CR-1 to CR-12 only  |  Status: awaiting comparison

## 1. Policy record

**Velmora Lumber Duty Repeal Act.** Velmora is a mid-sized country. For twenty years it has charged a 25% ad valorem duty on imported sawn softwood lumber, most of which comes from its larger neighbor, Dravenland. Domestic lumber comes from about forty sawmills in Velmora's northern forest region, which buy logs from private timberland owners. The main domestic users of lumber are home builders and furniture makers. Imported furniture has never been subject to the duty. Velmora's main export industries (machinery and processed foods) sell largely to Dravenland. Duty revenue has gone to the general budget. The Act passed nine months before its effective date; it had been expected for some weeks before that.

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| R1 Repeal | Removal of a `tariff` | Imported sawn softwood lumber | Importers | The duty falls from 25% to zero on the effective date, in one step. | None |
| R2 Customs procedure | End of administration | Classification and valuation of lumber imports for the duty | Customs service | Duty-specific checks end; ordinary customs procedures continue. | None |

Unclear provisions: how the lost duty revenue is to be replaced (higher other taxes, more borrowing, or lower spending). The Act does not say. Treated as unknown and traced with a pattern (A-14).

(The input's reference table of the original tariff's expected consequences, supplied for the metamorphic check, is not copied here; that check is done in the comparison phase.)

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | CR-1 operations | Core rules applied |
| --- | --- | --- | --- | --- |
| R1 Repeal of the duty | removal of a binary intervention (tax on importers) and of a triangular one (privilege to domestic mills) | Yes: imports are a substantial share and the duty raised domestic prices (A-1) | 3 for importers and foreign sellers (the 25% payment attached to importing is removed); 4 in reverse (means no longer transferred from importers and buyers to the treasury); for domestic mills, no operation directly: their situation changes through their competitors (CR-9) | CR-4, CR-5c, CR-6, CR-7a, CR-7b, CR-7c, CR-8b, CR-9, CR-10a, CR-10b, CR-10c |
| R2 End of duty-specific customs checks | end of administration | Yes | 3 for importers (classification and valuation paperwork for the duty removed); 4 for the customs service (tasks and their cost removed) | CR-8c |

The counterfactual is that the 25% duty stays. Every sign below is relative to that path; persistence is relative to the path on which the duty was never imposed.

## 3. Actor classes

| Actor class | Role | How its options change (CR-1) |
| --- | --- | --- |
| buyers.lumber | Builders, furniture makers and households who buy sawn softwood | Op 3 through price: imported lumber no longer carries the duty. |
| importers | Firms that bring lumber in from Dravenland | Op 3: duty and duty paperwork removed. |
| sellers.foreign | Dravenland sawmills selling to Velmora | Op 3: selling to Velmora no longer carries the duty. |
| sawmills.domestic | About forty mills in the northern forest | No direct operation; competitors' option improves (CR-9, substitute). |
| workers.sawmill | Mill employees | Through CR-9 (input_to). |
| timberland_owners | Private owners who sell sawlogs to domestic mills | Through CR-9 (input_to). |
| builders | Home builders | Through CR-9: a main input is cheaper. |
| homebuyers | Buyers of new houses | Through CR-9. |
| furniture_makers.domestic | Domestic furniture firms | Through CR-9: their main input now costs what foreign competitors pay. |
| buyers.furniture | Buyers of furniture | Through CR-9 (substitute: imported furniture). |
| exporters | Machinery and processed-food firms selling to Dravenland | Through CR-9 (across_border trade). |
| workers.export_industries | Employees of exporters | Through CR-9 (input_to). |
| officials.treasury | General budget | Op 4: duty revenue ends. |
| officials.customs | Customs service | Op 3 and op 4: duty-specific tasks end. |
| taxpayers | Those who bear the replacement of the lost revenue | Op 4 (indirect): other taxes, borrowing or cuts (A-14). |

## 4. Direct effect

CR-1 and CR-2: the immediate change.

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-1 | buyers.lumber | price_paid (lumber, imported and domestic) | decrease | short; medium; long | CR-1 op 3, CR-5c, CR-6, CR-7a | A-1, A-2 |
| C-2 | officials.treasury | tax_revenue (lumber duty) | decrease | short | CR-1 op 4, CR-8b | - |
| C-3 | importers | quantity_traded (imported lumber) | increase | short; medium | CR-4 (x: domestic lumber, y: imported lumber), CR-5 | A-1 |
| C-4 | officials.customs | enforcement_cost | decrease | short | CR-1 op 4, CR-8c | - |
| C-5 | importers | compliance_cost | decrease | short | CR-1 op 3, CR-8c | - |

## 5. Responses

CR-4 for each pair of options; CR-10a for the announcement window; CR-7c and CR-10c for asset values.

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-6 | buyers.lumber | quantity_traded (lumber bought in the nine months before the effective date) | decrease | short (announcement window) | CR-10a, CR-4 (x: buy now, y: buy after the effective date) | A-6 |
| C-7 | buyers.lumber | inventory_held | decrease | short (announcement window) | CR-10a, CR-4 (x: hold stocks, y: draw them down) | A-6 |
| C-8 | importers | inventory_held (lumber in bonded warehouses awaiting the effective date) | increase | short (announcement window) | CR-10a, CR-4 (x: clear customs now, y: hold in bond) | A-6 |
| C-9 | buyers.lumber | quantity_demanded (lumber) | increase | short; medium; long | CR-4c, LW-3 | A-1, A-2 |
| C-10 | sellers.foreign | net_price_received (lumber sold to Velmora) | increase | short; medium | CR-5c, CR-7b | A-11 |
| C-11 | sawmills.domestic | net_price_received | decrease | short; medium | CR-9, CR-7a, CR-6 | A-1, A-2 |
| C-12 | sawmills.domestic | quantity_supplied | decrease | short; medium | CR-4c (x: produce the marginal unit, y: do not), CR-10b | A-1, A-3 |
| C-13 | sawmills.domestic | investment_target | decrease | medium; long | CR-4 (x: reinvest, y: do not), CR-10c | A-3, A-17 |
| C-14 | sawmills.domestic | capital_stock_target (mill capacity) | decrease | medium; long | CR-10b | A-3, A-17 |
| C-15 | sawmills.domestic | number_of_sellers | decrease | long | CR-10b, CR-7a | A-3, A-17 |
| C-16 | sawmills.domestic | asset_value (mills) | decrease | short (from when the repeal became expected) | CR-7c, CR-10c | A-3, A-17 |
| C-17 | importers | reclassification (lightly processed wood declared outside the lumber heading) | decrease | short | CR-4 (x: reshape to avoid the duty, y: ship as ordinary lumber) | A-5, A-19 |
| C-18 | sawmills.domestic, timberland_owners | lobbying_effort (to restore the duty) | increase | short; medium | CR-4 (x: accept, y: lobby), CR-8c | A-15 |
| C-19 | sawmills.domestic, timberland_owners | lobbying_effort (to restore the duty) | decrease | long | CR-10b, CR-4 | A-3, A-15 |
| C-20 | builders, furniture_makers.domestic, exporters | lobbying_effort | ambiguous | short; medium | CR-12b over two CR-4 chains | A-15 |

## 6. Second-order effects

CR-9 along named relations, then CR-5 to CR-7. Depth limit 4. Effects on local businesses of the forest region that sell to mill workers (a location relation) are diffuse bystander effects pruned at depth 3, as are the effects of whatever tax replaces the revenue (A-14 does not say which).

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C-21 | timberland_owners | net_price_received (sawlogs) | decrease | short; medium | CR-9, LW-10, CR-7b | sawlogs input_to domestic lumber (close) | A-7, A-1 |
| C-22 | timberland_owners | asset_value (timberland) | decrease | short (from when the repeal became expected) | CR-7c, CR-10c | sawlogs input_to domestic lumber (close) | A-7, A-17 |
| C-23 | workers.sawmill | employment | decrease | medium; long | CR-9, LW-10, CR-10b | mill labor input_to domestic lumber (close) | A-3, A-4 |
| C-24 | workers.sawmill | wage_rate | decrease | medium | CR-7b, CR-9 | mill labor input_to domestic lumber (close) | A-4, A-1 |
| C-25 | workers.sawmill | job_changes | increase | medium; long | CR-4 (x: mill job, y: other work or a move), CR-7a | mill labor input_to domestic lumber (close) | A-4 |
| C-26 | builders | quantity_supplied (new houses) | increase | medium | CR-9, CR-4c | lumber input_to new houses (partial: a significant share of cost, A-8) | A-8, A-N1 |
| C-27 | homebuyers | price_paid (new houses) | decrease | medium | CR-9, CR-5c, CR-6 | lumber input_to new houses (partial) | A-8 |
| C-28 | furniture_makers.domestic | quantity_supplied (domestic furniture) | increase | medium; long | CR-9, CR-4, CR-10b | lumber input_to domestic furniture (partial: significant input, A-9) | A-9, A-13 |
| C-29 | furniture_makers.domestic | investment_target | increase | medium | CR-4, CR-10c | lumber input_to domestic furniture (partial) | A-9, A-12 |
| C-30 | buyers.furniture | quantity_substitute (imported furniture) | decrease | medium; long | CR-4 (x: domestic furniture, y: imported furniture), CR-9 | imported furniture substitute for domestic furniture (close) | A-9, A-13 |
| C-31 | exporters | quantity_supplied (machinery and processed foods sold to Dravenland) | increase | medium; long | CR-9, CR-5 | Velmoran lumber imports across_border to Velmoran exports to Dravenland (partial, A-10) | A-10, A-18 |
| C-32 | workers.export_industries | employment | increase | medium; long | CR-9, LW-10 | labor input_to exports (close) | A-10, A-18 |
| C-33 | buyers.lumber | resources_available_other_uses | increase | short; medium | CR-8b, CR-3b | - | A-2 |
| C-34 | taxpayers | resources_available_other_uses | decrease | short; medium | CR-8b, CR-8c, CR-12b with a dominance premise | - | A-14, A-N2 |

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (-) | Dominance premise | Combined sign |
| --- | --- | --- | --- | --- |
| taxpayers, resources_available_other_uses, short; medium | duty-specific administration no longer paid for (CR-8c) | lost revenue made up elsewhere (CR-8b, A-14) | A-N2 (p 0.95): administration saved is much smaller than revenue lost; arithmetic | decrease (C-34) |
| buyers.lumber, price_paid | - | duty removed (CR-1, CR-5c); domestic price follows (CR-7a) | - | decrease (C-1) |
| sawmills.domestic and timberland_owners, lobbying_effort | short; medium (C-18) | long (C-19) | Different horizons | increase (short; medium); decrease (long) |
| builders, furniture_makers.domestic, exporters, lobbying_effort | defending the repeal | no longer campaigning for it | None | ambiguous (C-20) |
| buyers.lumber, quantity_traded / quantity_demanded | after the effective date (C-9) | in the announcement window (C-6) | Different windows | decrease (window); increase (after) |

Metamorphic check: added in the comparison phase.

## 8. Time structure

- **Announcement window.** The repeal was expected some weeks before passage and passed nine months before the effective date. Mill and timberland values fall when it becomes expected (CR-7c, CR-10c; C-16, C-22). Buyers defer purchases and draw down stocks (CR-10a; C-6, C-7), and importers hold lumber in bond (C-8); purchases and clearances jump just after the effective date as stocks are rebuilt.
- **Gradual decline of the mills.** Mill capital is specific and durable (A-3): mills keep running while prices cover operating costs and close as equipment wears out (CR-10b). Output, capacity, employment and the number of mills therefore fall over years, not at once (C-12, C-14, C-23, C-15).
- **Slow rebuilding elsewhere.** Furniture making (A-13) and export markets (A-18) were lost or never built under the duty; rebuilding them has sunk costs and takes years (CR-10b), so their gains arrive in the medium and long run (C-28, C-31).
- **What does not reverse (CR-10b, CR-7c).** Owners who held mills and timberland when the duty was imposed captured its capitalized value; if they sold, current owners bear the loss of the repeal. Furniture and export capacity lost over twenty years returns only partly and slowly. The reshaping of imports reverses at once (A-19). The persistence column records this.
- **Belief in the repeal.** Mill and timberland owners give the repeal a meaningful chance of lasting (A-17, 0.9), so their asset values and reinvestment respond. Lumber users' long-payback investment needs the repeal to last ten years (A-12, 0.6). If the duty were expected back, quick-payback responses (buying imported lumber) would go ahead and long-payback ones (new furniture capacity) would be held back (CR-10a).

## 9. Opportunity costs

Each is written as a signed change in a variable.

| ID | Actor class | Variable | Sign | What is given up | Rules |
| --- | --- | --- | --- | --- | --- |
| C-4 | officials.customs | enforcement_cost | decrease | (released, not used) customs staff and time for duty-specific checks | CR-1 op 4, CR-8c |
| C-5 | importers | compliance_cost | decrease | (released) importers' paperwork and classification disputes | CR-1 op 3, CR-8c |
| C-18 | sawmills.domestic, timberland_owners | lobbying_effort (to restore the duty) | increase | Resources spent seeking to restore the duty | CR-4 (x: accept, y: lobby), CR-8c |
| C-25 | workers.sawmill | job_changes | increase | Earnings in mill work, and the cost of retraining and moving | CR-4 (x: mill job, y: other work or a move), CR-7a |
| C-34 | taxpayers | resources_available_other_uses | decrease | Other purchases, or public spending, given up to replace the duty revenue | CR-8b, CR-8c, CR-12b with a dominance premise |

CR-8's symmetry: what buyers no longer pay (C-33) and what foreign sellers no longer give up (C-10) are matched by the revenue the treasury no longer receives (C-2) and its replacement by taxpayers (C-34). The mills' and timberland owners' losses (C-11, C-21, C-16, C-22) are matched by lower prices to buyers; the resources used in the duty's administration and avoidance (C-4, C-5, C-17) are released.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
| --- | --- | --- | --- | --- | --- |
| A-1 | Imports are a substantial share of lumber used, and the duty raised domestic lumber prices. | binding | 0.9 | Import share; domestic prices against Dravenland prices plus transport. | These consequences fail or lose this chain: C-1, C-3, C-9, C-11, C-12, C-21, C-24. |
| A-2 | Velmoran buyers bore at least part of the duty (foreign sellers did not absorb all of it). | other | 0.85 | Price gap across the border; Dravenland's other markets. | These consequences fail or lose this chain: C-1, C-9, C-11, C-33. |
| A-3 | Mill capital is specific and durable: mills keep operating while prices cover operating costs and close as equipment wears out. | durability | 0.85 | Age and type of mill equipment; resale market for used mill equipment. | These consequences fail or lose this chain: C-12, C-13, C-14, C-15, C-16, C-19, C-23. |
| A-4 | Mill workers' skills are partly specific, and the forest region has few other employers. | alternative_uses | 0.75 | Regional employment structure; wages in other local work. | These consequences fail or lose this chain: C-23, C-24, C-25. |
| A-5 | Some imports had been shaped to fall outside the lumber heading. | other | 0.6 | Customs classification disputes; import volumes of lightly processed wood. | These consequences fail or lose this chain: C-17. |
| A-6 | Lumber buyers can defer purchases or draw down stocks for some months. | expectations | 0.7 | Inventory practices of builders and furniture makers; bonded warehouse capacity. | These consequences fail or lose this chain: C-6, C-7, C-8. |
| A-7 | Timberland is valued mainly for sawlogs sold to domestic mills; exporting logs costs too much to replace that demand. | alternative_uses | 0.7 | Land prices against log prices; transport costs; other uses of forest land. | These consequences fail or lose this chain: C-21, C-22. |
| A-8 | Lumber is a significant share of building costs, and builders compete. | other | 0.8 | Cost breakdowns of new houses; number of builders. | These consequences fail or lose this chain: C-26, C-27. |
| A-9 | Lumber is a significant input for domestic furniture, and imported furniture is a close substitute. | substitutability | 0.8 | Cost breakdowns; import share of furniture sales. | These consequences fail or lose this chain: C-28, C-29, C-30. |
| A-10 | Changes in imports are not fully offset by capital flows: Dravenland sellers spend more of the crowns they earn on Velmoran goods. | other | 0.65 | Composition of the balance of payments; trade patterns with Dravenland. | These consequences fail or lose this chain: C-31, C-32. |
| A-11 | Foreign sellers bore part of the duty. | other | 0.6 | Dravenland export prices to Velmora against prices to other markets. | These consequences fail or lose this chain: C-10. |
| A-12 | Lumber users expect the repeal to last at least ten years, the payback of new capacity. | expectations | 0.6 | Size of the parliamentary majority; organization and history of the mill lobby. | These consequences fail or lose this chain: C-29. |
| A-13 | Furniture-making skills, supplier links and retail placement lost over twenty years take years to rebuild. | reversal_cost | 0.7 | Number of furniture firms and workers now against twenty years ago; training available. | These consequences fail or lose this chain: C-28, C-30. |
| A-14 | The lost revenue is made up by some combination of other taxes, borrowing and spending cuts; the Act does not say which. | revenue_use | 0.95 | Budget documents; fiscal rules. | These consequences fail or lose this chain: C-34. |
| A-15 | Mill owners, timberland owners, builders and exporters can organize at a cost below their stake. | other | 0.85 | Twenty years of organized lobbying over the duty. | These consequences fail or lose this chain: C-18, C-19, C-20. |
| A-16 | Lumber smuggling was significant under the duty. | enforcement | 0.15 | Controlled crossing points; seizure records. | No reported consequence rests on it (see Not reported). |
| A-17 | Owners of timberland and mills give the repeal a meaningful probability of lasting. | expectations | 0.9 | The Act passed by a clear majority; no sunset or review clause; restoring a duty needs new legislation. | These consequences fail or lose this chain: C-13, C-14, C-15, C-16, C-22. |
| A-18 | Entering or re-entering export markets in Dravenland has sunk costs (distribution, buyer relationships, product approvals) that take years to pay. | reversal_cost | 0.75 | Export trade structure; how long comparable firms took to enter new markets. | These consequences fail or lose this chain: C-31, C-32. |
| A-19 | Imports reshaped to fall outside the lumber heading can be returned to ordinary sawn lumber at little cost. | reversal_cost | 0.8 | The reshaping is light processing or description, not separate plant. | These consequences fail or lose this chain: C-17. |
| A-N1 | Some house-building projects are at the margin of profitability, so a fall in lumber costs brings some of them forward. | substitutability | 0.75 | NEW. Builders compete (A-8); land and approvals are not the only constraint on every project; building responds to costs in comparable markets. | These consequences fail or lose this chain: C-26. |
| A-N2 | The cost of duty-specific customs administration is much smaller than the revenue the duty raised. | other | 0.95 | NEW. A 25% duty on a substantial import share (A-1) against the cost of classification and valuation checks; ordinary customs procedures continue in any case. | These consequences fail or lose this chain: C-34. |

**Not reported** (an assumption below 0.5):
- Smuggling falls, with lower enforcement and seizure costs (CR-4, x: comply, y: smuggle; the gain from smuggling disappears with the duty): needs A-16 (p 0.15).

The unclear provision on how the lost revenue is replaced is not a reading with different signs: every route (other taxes, borrowing, cuts) withdraws means from someone (CR-8b), so the sign of C-34 is the same under each; which actor class bears it is unknown and is not reported.

## 11. Report

**The policy:** Velmora removes its 25% duty on imported sawn softwood lumber in one step, nine months after the Act passed, and ends the customs checks that existed only for the duty. The comparison is with the duty staying in force.

**Visible consequences:** Lumber buyers pay less, for both imported and domestic lumber (C-1), and more lumber is imported (C-3). Duty revenue ends (C-2). Domestic mills receive less for their lumber (C-11), and mill employment falls over time (C-23).

**Invisible consequences:**
- *Before the effective date:* buyers hold off and run down stocks, and importers hold lumber in bond (C-6, C-7, C-8); mill and timberland values fall as soon as the repeal is expected (C-16, C-22).
- *Mills and their region:* output, reinvestment, capacity and the number of mills fall gradually as equipment wears out (C-12, C-13, C-14, C-15); mill wages fall and workers change jobs (C-24, C-25); timberland owners receive less for logs (C-21). Mill and timberland owners lobby to restore the duty while their capital lasts, and less once it has worn out (C-18, C-19).
- *Lumber users:* builders build more and new houses cost less (C-26, C-27); domestic furniture makers produce and invest more, and buyers buy less imported furniture, slowly as lost capacity is rebuilt (C-28, C-29, C-30). Buyers have more to spend on other things (C-33); they buy more lumber (C-9).
- *Exporters:* sell more to Dravenland and employ more, slowly (C-31, C-32).
- *Foreign sellers:* receive more per unit (C-10).
- *Taxpayers:* bear the replacement of the lost revenue through other taxes, borrowing or cuts, partly offset by the end of duty administration (C-34, C-4); importers save paperwork (C-5) and stop reshaping imports (C-17).

**Ambiguous effects:** Lobbying by builders, furniture makers and exporters (C-20): they defend the repeal but no longer need to campaign for it.

**What does not reverse:** Owners who held mills and timberland when the duty was imposed kept its capitalized gain if they sold; current owners bear the loss (CR-7c). Furniture-making and export capacity lost over twenty years comes back only partly and slowly (A-13, A-18).

**Key conditions:** The duty bound (A-1, 0.9) and buyers bore part of it (A-2, 0.85); mill capital is specific and durable (A-3, 0.85); timberland depends on domestic mills (A-7, 0.7); lumber matters for builders and furniture makers (A-8, A-9); trade is not fully offset by capital flows (A-10, 0.65). Two premises were added: marginal house-building projects exist (A-N1, 0.75), and duty administration costs much less than the duty raised (A-N2, 0.95).

**What this analysis cannot say:** How large any effect is, how many mills close or how fast, how many jobs move between regions and industries, or which taxpayers bear the lost revenue. It does not weigh gains to lumber users, furniture makers and exporters against losses to mill owners, mill workers and timberland owners, or say whether the repeal is good. Health, safety and environmental effects, including effects on forests, are out of scope.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions | Persistence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C-1 | buyers.lumber | price_paid (lumber, imported and domestic) | decrease | short; medium; long | visible | B | CR-1 (op 3: the 25% payment attached to importing is removed); CR-5c (the range of terms moves down for buyers; A-2: buyers bore at least part of the duty); CR-7a (domestic and imported lumber serve the same end, so buyers move between them until prices are back in line; the domestic price falls with the import price, A-1); CR-6 | A-1, A-2 | none |
| C-2 | officials.treasury | tax_revenue (lumber duty) | decrease | short | visible | A | CR-1 (op 4: the duty, a transfer to the treasury, ends); CR-8b (every payment is a receipt to someone: the receipt ends with the payment) | none | none |
| C-3 | importers | quantity_traded (imported lumber) | increase | short; medium | visible | B | CR-4 (x: buy domestic lumber, y: buy imported; y made better, so buyers for whom the two were close switch); CR-4c (more lumber is bought at the lower price); CR-5 (exchanges the duty prevented now take place) | A-1 | none |
| C-4 | officials.customs | enforcement_cost | decrease | short | invisible | A | CR-1 (R2: duty-specific classification and valuation end); CR-8c (resources no longer used up in administering the duty) | none | none |
| C-5 | importers | compliance_cost | decrease | short | invisible | A | CR-1 (op 3: duty paperwork removed); CR-8c (resources spent complying are no longer used up) | none | none |
| C-6 | buyers.lumber | quantity_traded (lumber bought in the nine months before the effective date) | decrease | short (announcement window) | invisible | B | CR-10a (an expected change alters choices now); CR-4 (x: buy in the window with the duty, y: defer purchases or draw down stocks until it ends; y made better by the expected repeal) | A-6 | n/a (transition effect) |
| C-7 | buyers.lumber | inventory_held | decrease | short (announcement window) | invisible | B | CR-10a; CR-4 (x: keep normal stocks bought with the duty, y: draw them down and restock after the effective date); restocking after the effective date adds to purchases then | A-6 | n/a (transition effect) |
| C-8 | importers | inventory_held (lumber in bonded warehouses awaiting the effective date) | increase | short (announcement window) | invisible | B | CR-10a; CR-4 (x: clear lumber through customs and pay the duty now, y: hold it in bond until the duty is zero) | A-6 | n/a (transition effect) |
| C-9 | buyers.lumber | quantity_demanded (lumber) | increase | short; medium; long | invisible | B | CR-4c (at a lower price, units previously not worth buying are bought; LW-3) | A-1, A-2 | none |
| C-10 | sellers.foreign | net_price_received (lumber sold to Velmora) | increase | short; medium | invisible | B | CR-5c (removing what one party must give moves the range of terms); CR-7b (the part of the duty that settled on foreign sellers, A-11, is lifted from them) | A-11 | none |
| C-11 | sawmills.domestic | net_price_received | decrease | short; medium | visible | B | CR-9 (relation: imported lumber substitute for domestic lumber, close); CR-7a (buyers move between the two until prices are in line, so the domestic price falls with the import price, A-1, A-2); CR-6 | A-1, A-2 | none |
| C-12 | sawmills.domestic | quantity_supplied | decrease | short; medium | invisible | B | CR-4c (at a lower price, the units that cost most to produce are the first given up); CR-10b (mills keep operating while prices cover operating costs, so the fall is gradual, A-3) | A-1, A-3 | partial (short; medium: mills built under the duty keep operating, A-3); none (long) |
| C-13 | sawmills.domestic | investment_target | decrease | medium; long | invisible | B | CR-4 (x: replace worn equipment, y: let it wear out; x made worse by the lower price); CR-10c (investment follows expected yields; A-17: owners believe the repeal may last) | A-3, A-17 | none |
| C-14 | sawmills.domestic | capital_stock_target (mill capacity) | decrease | medium; long | invisible | B | CR-10b (a stock changes only through flows: capacity falls as equipment wears out and is not replaced, C-13; specific capital has no other use to move to, A-3) | A-3, A-17 | partial (medium); none (long) |
| C-15 | sawmills.domestic | number_of_sellers | decrease | long | invisible | B | CR-10b (mills close as equipment wears out, A-3); CR-7a (the owners' movable means go to uses that now yield more) | A-3, A-17 | partial (mills close only as equipment wears out) |
| C-16 | sawmills.domestic | asset_value (mills) | decrease | short (from when the repeal became expected) | invisible | B | CR-10c (the value of a durable means reflects expected yields); CR-7c (the lasting fall in expected yield is borne by whoever owns the mill when the repeal becomes expected, some weeks before passage; A-17) | A-3, A-17 | partial: owners when the duty was imposed kept its capitalized gain if they sold (CR-7c); current owners bear the loss |
| C-17 | importers | reclassification (lightly processed wood declared outside the lumber heading) | decrease | short | invisible | B | CR-4 (the reshaping cost something and now saves nothing, so x is worse than y); the reshaping is light processing or description, so it is undone at little cost (A-19, CR-10b) | A-5, A-19 | none (A-19: reversal is cheap) |
| C-18 | sawmills.domestic, timberland_owners | lobbying_effort (to restore the duty) | increase | short; medium | invisible | B | CR-4 (x: accept the repeal, y: lobby to restore the duty; the repeal makes x worse for them while their specific capital is intact, A-3); CR-8c (resources spent lobbying are used up) | A-15 | n/a |
| C-19 | sawmills.domestic, timberland_owners | lobbying_effort (to restore the duty) | decrease | long | invisible | B | CR-10b (as mill capital wears out, fewer owners have a stake in the duty; in the counterfactual the mills remain and keep defending it); CR-4 (the gain from lobbying shrinks with the stake) | A-3, A-15 | n/a |
| C-20 | builders, furniture_makers.domestic, exporters | lobbying_effort | ambiguous | short; medium | invisible | B | CR-12b: (+) CR-4 (x: accept a possible restoration, y: lobby to keep the repeal; their gains are at stake); (-) in the counterfactual they would keep spending to obtain the repeal, which they no longer need. No premise says which dominates | A-15 | n/a |
| C-21 | timberland_owners | net_price_received (sawlogs) | decrease | short; medium | invisible | B | CR-9 and LW-10 (relation: sawlogs input_to domestic lumber; demand for logs follows domestic mill output, C-12); CR-7b (the loss settles on the means that cannot move: land whose logs cannot be sold elsewhere at a comparable price, A-7) | A-7, A-1 | none |
| C-22 | timberland_owners | asset_value (timberland) | decrease | short (from when the repeal became expected) | invisible | B | CR-10c and CR-7c (the expected fall in log prices, C-21, is borne by whoever owns the land when the repeal becomes expected, A-17) | A-7, A-17 | partial: owners when the duty was imposed kept its capitalized gain if they sold (CR-7c) |
| C-23 | workers.sawmill | employment | decrease | medium; long | visible | B | CR-9 and LW-10 (relation: mill labor input_to domestic lumber; demand for it follows mill output and capacity, C-12, C-14); CR-10b (gradual, as mills wind down) | A-3, A-4 | partial (medium); none (long) |
| C-24 | workers.sawmill | wage_rate | decrease | medium | invisible | B | CR-9 (relation: input_to); CR-7b (the loss settles on means that cannot move: partly specific skills in a region with few other employers, A-4) | A-4, A-1 | none |
| C-25 | workers.sawmill | job_changes | increase | medium; long | invisible | B | CR-4 (x: stay in mill work at a lower wage or none, y: other local work or moving; x made worse); CR-7a (labor moves toward uses that now yield more, net of the cost of moving, A-4) | A-4 | none |
| C-26 | builders | quantity_supplied (new houses) | increase | medium | invisible | B | CR-9 (relation: lumber input_to new houses; a cheaper input lowers the cost of each house); CR-4c (projects that were narrowly not worth building now are, A-N1) | A-8, A-N1 | partial (the houses not built over twenty years are made up only through new building, CR-10b) |
| C-27 | homebuyers | price_paid (new houses) | decrease | medium | invisible | B | CR-9 (relation: input_to); CR-5c and CR-6 (with competing builders, A-8, a lower cost per house moves the price toward a lower clearing level) | A-8 | none |
| C-28 | furniture_makers.domestic | quantity_supplied (domestic furniture) | increase | medium; long | invisible | B | CR-9 (relation: lumber input_to furniture); CR-4 (domestic makers' main input now costs what foreign competitors pay, while imported furniture was never taxed, so domestic furniture becomes a better option for buyers relative to imported, A-9); CR-10b (skills, supplier links and retail placement lost over twenty years are rebuilt only through flows, A-13) | A-9, A-13 | partial (A-13: lost capacity takes years to rebuild) |
| C-29 | furniture_makers.domestic | investment_target | increase | medium | invisible | B | CR-4 (x: no new capacity, y: invest); CR-10c (investment follows expected yields; A-12: users expect the repeal to last long enough to pay back new capacity) | A-9, A-12 | none |
| C-30 | buyers.furniture | quantity_substitute (imported furniture) | decrease | medium; long | invisible | B | CR-9 (relation: imported furniture substitute for domestic furniture, close, A-9); CR-4 (domestic furniture made relatively better, C-28, so buyers for whom the two were close switch to it) | A-9, A-13 | partial (A-13) |
| C-31 | exporters | quantity_supplied (machinery and processed foods sold to Dravenland) | increase | medium; long | invisible | B | CR-9 (relation: across_border trade; Dravenland sellers earn more crowns from lumber and spend more of them on Velmoran goods, A-10); CR-5 (more exchanges take place); CR-10b (entering markets has sunk costs that take years to pay, A-18) | A-10, A-18 | partial (A-18: markets lost or never entered are re-entered slowly) |
| C-32 | workers.export_industries | employment | increase | medium; long | invisible | B | CR-9 and LW-10 (relation: labor input_to exports; demand for it follows export sales, C-31) | A-10, A-18 | partial (A-18) |
| C-33 | buyers.lumber | resources_available_other_uses | increase | short; medium | invisible | B | CR-8b (the duty borne by buyers, A-2, is no longer transferred away from them); CR-3b (removing a burden cannot make them worse off by their own ranking) | A-2 | none |
| C-34 | taxpayers | resources_available_other_uses | decrease | short; medium | invisible | B | CR-8b (the duty revenue, C-2, must be made up by other taxes, borrowing or spending cuts, A-14: CR-8's symmetry requires counting this against C-33); against it, CR-8c (the duty-specific administration, C-4, is no longer paid for). CR-12b: dominance premise A-N2 (by arithmetic, the administration saved is much smaller than the revenue lost), so the combined sign is decrease | A-14, A-N2 | none |

## Gaps found

**(a) Calculus gaps.** None. Every step used CR-1 to CR-12, LW-3, LW-10 or arithmetic.

**(b) New premises.**
- A-N1 (p 0.75): needed for C-26. CR-4c gives the direction a priori, but that some building projects are actually at the margin is empirical; A-8 states cost share and competition, which carry the price chain (C-27) but not the quantity chain.
- A-N2 (p 0.95): needed to combine C-34. Two chains reach taxpayers' resources with opposite signs (revenue replaced, administration saved); CR-12b requires a premise to sign the combination, and none of the case assumptions compares the two.

**(c) Unclear core rules.**
- CR-12b: whether an arithmetic comparison of two sums of money on the same actor class counts as "a premise that establishes that one chain dominates". It was treated as one, with its empirical part stated as A-N2.
- CR-4 for lobbying on a repeal (C-20, C-18): the counterfactual also has lobbying, by the other side. CR-4 compares accepting and lobbying for one change; it does not say how to sign the change in effort when both paths have a stake. For mills and timberland the stake moves from defending to restoring and was signed increase; for users it was left ambiguous.
- CR-7c on a repeal: the rule says the gain or loss goes to the owner when the change becomes expected. For persistence this means a capitalized gain under the original policy stays with whoever sold, while the repeal's loss falls on the current owner. The persistence field has no place to say that the asset value reverses but its incidence does not; this was written out in words.
