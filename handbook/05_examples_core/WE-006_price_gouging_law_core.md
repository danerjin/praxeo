# WE-006 / Analysis: Anti-price-gouging law during a declared hurricane emergency (core-only re-run)

Analyst: core-only re-run (Handbook 0.4)  |  Rules: core rules CR-1 to CR-12 only  |  Status: awaiting comparison

## 1. Policy record

**Coralia Emergency Pricing Act.** Coralia is a coastal state. The Act was passed two years ago and is a standing law: it applies automatically whenever the governor declares a state of emergency for named counties. This season a hurricane is forecast to strike the six coastal counties (about 1.8 million people). The governor declares an emergency for those counties two days before landfall. A declaration lasts 30 days and may be renewed in 30-day steps; the governor has said it will be renewed "as long as needed". The inland counties of Coralia, 60 to 150 miles from the coast, are not declared. The neighboring state of Hallorn, about three hours north, has no such law. For the first two or three days after landfall, roads into the coast are partly blocked.

The counterfactual is the same hurricane and the same declaration (with its other emergency powers, such as public water distribution and curfews), without the Act's pricing rules.

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Price cap | `price_ceiling` | Generators and fuel cans; bottled water; plywood, tarps and other building materials; hotel, motel and short-term rental rooms; sold or rented in the declared counties | Every seller of these goods in the declared counties, including sellers from outside the area selling there and online sellers delivering there | Price may not exceed 110% of the seller's own average price in the 30 days before the declaration. A seller who did not sell the item then may not charge more than 110% of the average price of the item in that county before the declaration. Applies for the whole declared emergency. | None |
| K2 Cost defense | Exception to K1 | Same | Same | A seller may add any documented increase in its own costs (purchase price, freight) since the base period, but may not raise its markup. | None |
| K3 Enforcement | Administration and enforcement | K1, K2 | State Attorney General | Civil penalty up to $10,000 per violation; repeat violations are a misdemeanor; a public hotline; staff deployed to the declared area; cases are publicized. Funded from the Attorney General's budget. | None |

Unclear provisions: whether repair and tree-removal services count as covered "necessities". The list names goods and lodging only, so assumed not covered; if they were covered, outside repair crews would face the same incentives as outside sellers of goods ([a consequence of the original analysis]). Also unclear: whether minimum-stay rules and deposits count as part of a room's price. Assumed not (fees are counted; conditions are not).


Readings used below. U1 (repair and tree-removal services): U1-a, not covered (the reading assumed in the record); U1-b, covered. U2 (minimum-stay rules and deposits): taken as conditions, not price, as the record assumes; this leaves the conditions of a stay open as a margin (C-10).

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | Core rules applied |
|---|---|---|---|
| K1 Price cap | triangular (forbids exchanges between private parties above the cap) | Yes for independent sellers, outside sellers and hotels in the first weeks (A-1, p 0.85); mostly not for large chains (A-2, p 0.7) | CR-1, CR-4, CR-5a, CR-6, CR-7, CR-9, CR-10, CR-11 |
| K2 Cost defense | exception to K1 (narrows the triangular restriction) | Narrows K1 only for documented costs; trip costs mostly not accepted (A-5, p 0.75) | CR-1 (op 2), CR-4 |
| K3 Enforcement | binary on the budget side (Attorney General budget); attaches penalties to violation | Active enforcement (A-3, p 0.75) | CR-1 (op 3), CR-8 |

**CR-1: what each component does to each actor class.** Operations: 1 remove an option, 2 add an option, 3 change what an option brings, 4 transfer means. A dash means the component does not touch the class directly; effects that arrive through others' choices are traced with CR-9.

| Actor class | K1 Price cap | K2 Cost defense | K3 Enforcement |
|---|---|---|---|
| buyers.current (households and firms in declared counties) | 3: covered purchases from legal sellers bring a lower money price; 1: the option of outbidding others with a price above the cap is removed | — (indirectly 3: price may include documented costs) | — |
| buyers.current (guests in rooms) | 3: the room they hold costs less than its clearing price | — | — |
| sellers.current (local independent sellers, hotels) | 1: selling above 110% of base removed | 2: adding documented cost increases is permitted | 3: penalty, publicity and misdemeanor risk attached to violation; record keeping attached to selling |
| sellers.current (large chains) | 1 formally; mostly not binding (A-2) | 2 | 3 |
| sellers.prospective (outside sellers, online sellers delivering in) | 1: selling at an emergency price in the declared counties removed | 2: documented costs only; trip costs mostly excluded (A-5) | 3 |
| intermediaries (informal sellers) | 1: legal resale above the cap removed | — | 3: penalty risk attached |
| buyers.prospective (outside repair crews needing rooms) | 3 as buyers of rooms (lower price where a room is found) | — | — |
| buyers.repair_services | U1-a: —; U1-b: 3 (lower money price) | U1-b: as for goods | U1-b: as for goods |
| neighboring_jurisdictions (inland counties, Hallorn) | — | — | — |
| officials.enforcement (Attorney General) | — | — | 2 and 4: new duties; means directed to them from the existing budget |
| taxpayers | — | — | 4: resources directed to K3 from other Attorney General uses |

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| buyers.current | Households and firms in the six declared counties | Lower money price at legal sellers who still have stock; cannot outbid others by price |
| buyers.current (guests in rooms) | Those already holding a hotel or short-term room | Room costs less than clearing price; leaving forfeits it (A-8) |
| sellers.current (independent sellers, hotels) | Local sellers bound by the cap | Cannot sell above cap plus documented costs; can hold durable stock (A-6); hotels can change service and conditions (A-7) |
| sellers.current (large chains) | Local sellers who would price below the cap anyway (A-2) | Little direct change |
| sellers.prospective (outside sellers) | Sellers who would truck goods in, or sell online into the area | Emergency premium removed; trip costs mostly unrecoverable (A-5); other markets open (A-4) |
| intermediaries | Informal resellers (online listings, roadside) | Sales above the cap are illegal and risky; some go undetected (A-10) |
| buyers.prospective (outside repair crews) | Crews coming in to repair, who need rooms | Rooms are scarcer at the capped price (CR-9 from hotels) |
| buyers.repair_services | Households and firms needing repairs | U1-a: price free, supply depends on crews' lodging; U1-b: price capped |
| neighboring_jurisdictions | Inland Coralia and Hallorn sellers and buyers | Receive diverted goods and traveling coastal buyers (CR-9, across_border) |
| officials.enforcement | State Attorney General | New enforcement duties |
| taxpayers | Those who fund the Attorney General | Resources used for K3 |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | buyers.current | price_paid (covered goods and rooms, legal sales in declared counties) | decrease | short | CR-1 (op 1) → CR-6 | A-1, A-3 |
| C-2 | sellers.current (independent sellers, hotels) | net_price_received | decrease | short | CR-1 (op 1) → CR-3a | A-1, A-3 |

The direct effect is what supporters expect: buyers who obtain goods at legal sellers pay less, and sellers receive less, than they would without the Act. It holds only where the cap binds (A-1) and is enforced (A-3); chains that price below the cap anyway (A-2) are not changed.

## 5. Responses

**CR-2 to CR-5 by actor class.**

| Actor class | CR-2/CR-3: which chosen option is removed or burdened | CR-4 pairs (x made worse relative to y) | CR-5 |
|---|---|---|---|
| buyers.current | Paying a premium to be served is removed: worse off for those who would have paid it (CR-3a); better off for those who obtain a unit at the capped price | x: wait for a local unit, y: substitute (ice, relatives' homes) or travel inland; mirror CR-4c: a unit bought now is cheaper, so units valued least are bought by those served first | 5a: exchanges above the cap that would have taken place are prevented |
| guests in rooms | None removed; staying is made cheaper | x: check out, y: keep the room | — |
| sellers.current (independent, hotels) | Selling at the clearing price removed (CR-3a) | x: sell now, y: hold durable stock until after the emergency; x: full service, y: reduced service; x: covered form, y: bundled, new model or relabeled; x: comply, y: violate; x: undocumented cost, y: documented cost (K2) | 5a; 5c: the range of permitted terms is moved |
| sellers.prospective (outside sellers) | Emergency premium removed | x: bring goods into declared counties, y: sell elsewhere | 5a |
| intermediaries | Legal resale above cap removed | x: comply, y: violate | 5a for legal sales |
| outside repair crews | Rooms harder to obtain (CR-9) | x: work in declared counties, y: work elsewhere | — |
| neighboring sellers | None | Mirror: selling where they are is made better by buyers arriving | — |
| sellers in future seasons | Emergency sales capped in every future declaration (A-14) | x: hold extra stock before the season, y: not | — |
| households in future seasons | Mixed (CR-4 exception does not apply; two option changes) | x: stock before the season, y: buy after landfall; y is cheaper in money but harder to obtain | — |
| sellers (lobbying) | — | x: accept, y: lobby for narrower coverage or a wider cost defense | Not reported (A-N3) |

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-3 | buyers.current | quantity_demanded (covered goods at the capped price) | increase | short | CR-1 → CR-4c (mirror) | A-1, A-3 |
| C-4 | sellers.prospective (outside sellers) | quantity_supplied (covered goods brought into declared counties) | decrease | short | CR-1 → CR-4b (x: bring in, y: sell elsewhere) → CR-7a | A-1, A-3, A-4, A-5 |
| C-5 | sellers.current (local independent sellers) | inventory_held (durable covered goods during the emergency) | increase | short | CR-10a → CR-4b (x: sell now, y: hold) | A-1, A-3, A-6 |
| C-6 | sellers.current (local independent sellers) | quantity_supplied (during the emergency) | decrease | short | CR-10a → CR-4b (x: sell now, y: hold) | A-1, A-3, A-6 |
| C-7 | buyers.current | excess_demand (covered goods and rooms) | increase | short | CR-6 (price held below clearing) | A-1, A-3 |
| C-8 | buyers.current | quantity_traded (legal sales of covered goods in declared counties) | decrease | short | CR-6 → C-4 → CR-5a | A-1, A-3, A-4, A-5 |
| C-9 | buyers.current | wait_time, search_cost, allocation_by_non_price_criteria | at_least_one_increase | short | CR-6 (criteria margin) | A-1, A-3 |
| C-10 | sellers.current (hotels) | quality_per_unit (room services and stay conditions) | decrease | short | CR-6 (unregulated terms) → CR-4b (x: full service, y: reduced service) | A-1, A-3, A-7 |
| C-11 | sellers.current | reclassification (bundles, new models, relabeled fees, costs routed through documented channels) | increase | short | CR-6 → CR-4b (x: covered form, y: uncovered form); K2: CR-1 (op 2) → CR-4b (x: undocumented cost, y: documented cost) | A-1, A-3, A-9 |
| C-12 | intermediaries | informal_activity (sales above the cap) | increase | short | CR-6 (exchanges outside the rule) → CR-4b (x: comply, y: violate) | A-1, A-10 |
| C-14 | buyers.current (guests in rooms) | turnover (room check-outs) | decrease | short | CR-1 → CR-4b (x: check out, y: keep room) → CR-3 | A-1, A-3, A-8 |
| C-21 | buyers.current | quantity_substitute (ice, staying with relatives) | increase | short | CR-6 → CR-4b (x: covered good, y: substitute) | A-1, A-3, A-13 |
| C-26 | sellers.current (retailers, future seasons) | inventory_held (pre-season stocks of covered goods) | decrease | long | CR-10a → CR-4b (x: hold extra stock, y: not) → CR-3 | A-1, A-14, A-17 |
| C-27 | buyers.current (households, future seasons) | inventory_held (household storm supplies before the season) | ambiguous | long | CR-10a → CR-4 (two opposing option changes) → CR-12b | A-1, A-14, A-15 |

Notes on the responses.
- C-3: the capped price makes each unit cheaper to the buyer who reaches it, so buyers who are served early take units they value less (LW-2). This is strongest in the two days between declaration and landfall, when the cap already applies.
- C-5 and C-6 are one act seen from two variables (CR-12c: not netted). They need A-6 (p 0.55): sellers must expect the emergency to end within weeks. If they expected renewal for months (A-16, p 0.4), holding would cost more and the chain would weaken; that variant is not reported.
- C-9: CR-6 licenses only that the pressure moves to the criteria by which sellers choose among buyers; which criterion (queues, search, regular-customer preference) is empirical, so the consequence is a group.
- C-11: K2 adds an option (CR-1 op 2) that rewards costs which can be documented; a seller whose real trip cost cannot be documented (A-5) gains by routing it through billed freight or purchase price. This is the same variable as bundling and relabeling, pushed the same way (CR-12a).

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-13 | buyers.current (in informal sales) | quality_information | decrease | short | C-12 → CR-11b | same market, illegal segment (`same_market_other_segment`) | A-1, A-10 |
| C-15 | buyers.prospective (outside repair crews) | search_cost (lodging) | increase | short | C-7, C-14 → CR-9 → CR-6 (criteria margin) | rooms: same market; crews compete with sitting guests | A-1, A-3, A-8, A-11 |
| C-16 | buyers.repair_services | quantity_traded (repair and tree-removal services) | decrease | short | U1-a: C-15 → CR-9 → CR-4b (x: work in declared counties, y: work elsewhere) → CR-5a; U1-b: CR-1 (op 1) → CR-4b → CR-5a | rooms `input_to` repair work (U1-a) | U1-a: A-1, A-3, A-8, A-11, A-N2; U1-b: A-3, A-N1, A-N2 |
| C-17 | buyers.repair_services | price_paid (repair and tree-removal services) | U1-a: increase; U1-b: decrease | short | U1-a: as C-16 → CR-6 (unregulated price moves toward clearing as fewer crews offer); U1-b: CR-1 (op 1) → CR-6 | rooms `input_to` repair work | U1-a: A-1, A-3, A-8, A-11, A-N2; U1-b: A-3, A-N1 |
| C-18 | buyers.current | cross_border_purchases (covered goods bought in inland counties and Hallorn) | increase | short | C-7 → CR-4b (x: wait for local supply, y: travel) | declared counties to inland counties and Hallorn (`across_border`) | A-1, A-3, A-12 |
| C-19 | neighboring_jurisdictions (inland and Hallorn sellers) | quantity_substitute (covered goods sold outside declared counties) | increase | short | C-4 → CR-7a; C-18 → CR-9 → CR-12a | `across_border` | A-1, A-3, A-4, A-5 |
| C-20 | neighboring_jurisdictions (inland and Hallorn sellers) | price_substitute (covered goods outside declared counties) | ambiguous | short | (+) C-18 → CR-9 → CR-6; (−) C-4 → CR-7a → CR-12b | `across_border` | A-1, A-3, A-4, A-5, A-12 |
| C-22 | buyers.current | full_cost_per_unit | ambiguous | short | (−) C-1; (+) C-9 → CR-6 (full price moves toward clearing as far as open margins allow) → CR-12b | same market | A-1, A-3 |

Chains stopped: C-16 and C-17 are at depth 4 under U1-a (cap on rooms, room shortage, crews' lodging search, crews' choice of where to work). Effects on the customers of repaired businesses, and on inland residents who face diverted coastal demand for rooms, are diffuse bystander effects beyond depth 3 and are pruned. The effect on large chains' sales (A-2) has opposing pulls (some buyers are no longer driven away by independents' higher prices; some unserved buyers come to chains) on a stock that is fixed in the first days, so it is not reported.

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| buyers.current, excess_demand, short | C-3 (more wanted at capped price) and C-4, C-6 (less offered) | none | none needed (CR-12a) | increase (C-7) |
| buyers.current, quantity_traded, short | none | C-4 (outside supply), C-6 (local holding) | none needed (CR-12a) | decrease (C-8) |
| buyers.current, full_cost_per_unit, short | waits, search, favoritism (C-9) | money price (C-1) | none: no premise establishes which dominates | ambiguous (C-22) |
| neighboring sellers, quantity_substitute, short | diverted goods (C-4); traveling buyers (C-18) | none | none needed (CR-12a) | increase (C-19) |
| neighboring sellers, price_substitute, short | traveling buyers bid (C-18) | more goods offered (C-4) | none | ambiguous (C-20) |
| households, inventory_held before season, long | after-landfall goods harder to obtain (C-7, C-26) | after-landfall goods cheaper in money (C-1) | none | ambiguous (C-27) |
| sellers.current, reclassification, short | bundling and relabeling (CR-6); documented-cost routing (K2) | none | none needed | increase (C-11) |
| buyers.repair_services, price_paid, short | U1-a: fewer crews | U1-b: cap | not combined: readings are reported separately | per reading (C-17) |

No dominance claim is made in this analysis.

## 8. Time structure

- Before landfall (two days after declaration): the cap already applies; C-3 (more bought by early buyers at the capped price) is concentrated here (CR-10a). Stocks in the area are fixed (CR-10b), so the first days' shortage (C-7) is driven by demand.
- Days 1 to 3 after landfall: roads are partly blocked, so outside supply could not arrive in either world. C-4 bites from about day 3 onward, when trucks could come in but the cap removes the premium that would have drawn them.
- Weeks: C-5 and C-6 depend on sellers expecting the emergency to end within weeks (A-6). Renewal in 30-day steps keeps the cap in force; if renewal for months were expected (A-16, not reported), holding back would weaken.
- Future seasons (long): the law is standing (A-14), so sellers carry fewer pre-season stocks (C-26). Households' pre-season stocking is ambiguous (C-27). These effects persist as long as the law stands.

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-8 | buyers.current | quantity_traded | decrease | Exchanges above the cap that both parties would have chosen; each expected a gain | CR-5a, CR-3a |
| C-9 | buyers.current | wait_time, search_cost, allocation_by_non_price_criteria | at_least_one_increase | Time spent queuing and searching, used up and serving no other end | CR-6, CR-8c |
| C-15 | buyers.prospective (outside repair crews) | search_cost | increase | Crews' time spent finding lodging | CR-8c |
| C-23 | sellers.current | compliance_cost (base-period records, cost documentation) | increase | Staff time and records kept to stay within or prove K1 and K2 | CR-1 (op 3) → CR-8c |
| C-24 | officials.enforcement | enforcement_cost | increase | Staff, hotline and prosecutions | CR-8c |
| C-25 | taxpayers | resources_available_other_uses (other Attorney General work) | decrease | Whatever the deployed staff and budget would otherwise have done | CR-8a |

Resources used for evasion and disguise (C-11, C-12) are also used up under CR-8c; they are recorded under their own variables, not netted.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | Without the Act, prices of covered goods and rooms would rise more than 10% above the base plus documented cost increases, for independent sellers, outside sellers and hotels, in the first weeks. | binding | 0.85 | Prices in comparable storms in places without such laws; online listing prices. | The cap does not bind; nearly every consequence vanishes. |
| A-2 | Large chains keep prices below the cap anyway, so the Act binds mainly on others. | other | 0.7 | Chains' pricing in past storms. | Chains are also bound; C-2 and C-5 widen to chains. |
| A-3 | The Attorney General enforces actively in the declared area, including against outside sellers. | enforcement | 0.75 | Staff deployed; past prosecutions; publicity. | The cap becomes a risk rather than a removed option; C-1 weakens and C-12 grows. |
| A-4 | Goods that could be brought in can be sold elsewhere at normal prices. | alternative_uses | 0.9 | Inland and out-of-state demand for the same goods. | C-4, C-8, C-19 fail. |
| A-5 | As the Attorney General applies K2, the extra costs of an emergency trip (own time, risk, unsold stock, value elsewhere) are mostly not accepted as documented costs. | enforcement | 0.75 | Attorney General guidance on what counts as a cost. | K2 restores the trip premium; C-4 and C-8 weaken. |
| A-6 | Local sellers expect the emergency to end within weeks, can store durable goods, and are not required to sell. | expectations | 0.55 | Renewal history; text of the Act; storage space. | C-5, C-6 fail. |
| A-7 | Hotels may change services and stay conditions (the Act caps the charge only). | other | 0.75 | Text of the Act; Attorney General guidance. | C-10 fails. |
| A-8 | A guest who checks out loses the capped room and cannot pass it on. | other | 0.85 | Hotel practice; occupancy during the emergency. | C-14 weakens; C-15 to C-17 (U1-a) weaken. |
| A-9 | Bundling, new models and relabeled fees are open to some sellers. | other | 0.6 | Definitions in the Act; past enforcement cases. | C-11 rests on the K2 route alone. |
| A-10 | Some informal sales above the cap go undetected. | enforcement | 0.6 | Online listings in past emergencies; enforcement focus on stores. | C-12, C-13 fail. |
| A-11 | Some outside repair contractors rely on local rooms, and their other lodging is far away. | mobility | 0.6 | Share of crews with their own staging camps; distance to inland hotels. | C-15 and the U1-a chains of C-16, C-17 fail. |
| A-12 | Inland stores can be reached within days of landfall. | mobility | 0.7 | Road damage reports; distance of 60 to 150 miles. | C-18 fails; C-20 loses its (+) chain. |
| A-13 | Some unserved buyers have substitutes (ice, relatives' homes). | substitutability | 0.8 | Ice distribution; household surveys. | C-21 fails. |
| A-14 | Sellers expect the cap to bind in future storms. | expectations | 0.75 | The law is standing and was enforced in the last declaration. | C-26 fails. |
| A-15 | Households know the Act and expect it to apply in future storms. | expectations | 0.55 | Awareness surveys; publicity of past cases. | C-27 vanishes. |
| A-16 | Sellers expect the emergency to be renewed for months. | expectations | 0.4 | Governor's statements; renewal history. | (Below cut-off; used by no reported consequence.) |
| A-17 | Holding extra stock before the season is costly to sellers (floor and warehouse space, money tied up, stock left unsold or marked down if no storm comes). | other | 0.9 | Retail space costs; end-of-season markdowns of generators and plywood in years without a storm. | C-26 fails. |
| A-N1 | Under reading U1-b, prices of repair and tree-removal services would, without the Act, rise more than 10% above base after landfall. | binding | 0.8 | The same demand surge as for covered goods; crews travel from far away. | The U1-b chains of C-16, C-17 fail. |
| A-N2 | Outside repair crews have other work they can do (other storm areas, normal jobs elsewhere), so some are at the margin of coming. | alternative_uses | 0.75 | Crews work across states; other demand for repair work continues. | C-16 fails under both readings; C-17 (U1-a) fails. |
| A-N3 | Bound sellers (hotel and retail associations) spend resources to narrow the Act or widen the cost defense. | other | 0.45 | Standing law passed two years ago; bound sellers are many small independents; no record of a campaign in the case. | Lobbying chain stays unreported. |

**Not reported (an assumption below 0.5).**
- Sellers' lobbying effort increase (CR-4, x: accept, y: lobby): needs A-N3 (p 0.45).
- Local sellers ship held stock out of the declared counties instead of holding it (CR-4, x: hold, y: sell elsewhere), if they expect renewal for months: needs A-16 (p 0.4).

## 11. Report

**The policy:** During a declared emergency, sellers of generators, fuel cans, bottled water, building materials and rooms in the six declared counties may not charge more than 110% of their own pre-emergency average price, plus documented increases in their own costs. The Attorney General enforces it with fines, publicity and staff in the area. Inland counties and the neighboring state are not covered.

**Visible consequences:** Buyers who obtain covered goods and rooms from legal sellers pay less than they would have without the Act (C-1), and sellers bound by the cap receive less (C-2). Shelves and rooms run out sooner: more is wanted at the capped price than is offered (C-7). The Attorney General spends more on enforcement (C-24).

**Invisible consequences:**
- Buyers in the declared counties: early buyers take more units at the capped price (C-3); fewer exchanges take place in the legal market (C-8); buyers spend more time queuing or searching, or sellers favor some buyers (at least one of these, C-9); more people turn to ice and relatives' homes (C-21) and drive inland or to Hallorn to buy (C-18). Buyers in informal sales have less to go on in judging sellers (C-13). All short run, and all need the cap to bind and be enforced (A-1, A-3).
- Outside sellers bring fewer goods into the declared counties and sell them elsewhere (C-4), because the cap removes the premium and the cost defense mostly does not cover trip costs (A-5).
- Local independent sellers hold more durable stock back during the emergency and offer less (C-5, C-6), if they expect the emergency to end within weeks (A-6, p 0.55).
- Hotels cut services and change stay conditions (C-10). Sellers bundle, relabel, introduce new models or route costs through documented channels (C-11). Some informal sales above the cap take place (C-12).
- Guests holding capped rooms check out less (C-14), so outside repair crews spend more effort finding lodging (C-15). Fewer repair jobs get done in the declared counties under either reading of the coverage of repair services (C-16); their price rises if repair is not covered and falls if it is (C-17).
- Inland and Hallorn sellers sell more covered goods (C-19).
- Sellers spend more on records and cost documentation (C-23); other Attorney General work is forgone (C-25).
- Future seasons: sellers carry less pre-season stock of covered goods (C-26), because the standing law caps the return to holding stock for a storm while the cost of holding is unchanged.

**Ambiguous effects:**
- Buyers' full cost per unit (C-22): the money price is lower, but waits, searches and favoritism are higher. No premise says which dominates.
- Prices of covered goods inland and in Hallorn (C-20): traveling coastal buyers push them up; goods diverted from the coast push them down.
- Households' pre-season stocking (C-27): buying after landfall is cheaper in money but harder.

**Key conditions:** That the cap binds for independents, outside sellers and hotels (A-1, p 0.85) and is enforced (A-3, p 0.75). That the cost defense excludes trip costs (A-5, p 0.75). The holding-back chain rests on the weakest reported premise (A-6, p 0.55), as does household awareness (A-15, p 0.55). The repair-service chains need A-N2 (p 0.75) and, under reading U1-a, A-11 (p 0.6).

**What this analysis cannot say:** How large any effect is; whether the gain to buyers who obtain capped goods outweighs the loss to those who do not; whether the Act is good policy. Health and safety effects of shortages, of delayed repairs and of informal sales (for example, unsafe generators or fuel) are out of scope for version 1 and are not analyzed. The method cannot say which non-price criterion sellers use (C-9 is a group), nor how many outside sellers or crews are at the margin.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | buyers.current | price_paid (covered goods and rooms, legal sales in declared counties) | decrease | short | visible | B | CR-1 (op 1: sales above cap removed; op 2: K2 documented costs) → CR-6 (price held below clearing) | A-1, A-3 |
| C-2 | sellers.current (independent sellers, hotels) | net_price_received | decrease | short | visible | B | CR-1 (op 1) → CR-3a (chosen option removed) | A-1, A-3 |
| C-3 | buyers.current | quantity_demanded (covered goods at the capped price) | increase | short | invisible | B | CR-1 (op 3: lower price) → CR-4c (mirror: unit made cheaper; least-valued units now bought, LW-2) | A-1, A-3 |
| C-4 | sellers.prospective (outside sellers) | quantity_supplied (covered goods brought into declared counties) | decrease | short | invisible | B | CR-1 (op 1; K2 op 2 excludes trip costs) → CR-4b (x: bring goods in, y: sell elsewhere) → CR-7a (goods move to higher-yield use) | A-1, A-3, A-4, A-5 |
| C-5 | sellers.current (local independent sellers) | inventory_held (durable covered goods during the emergency) | increase | short | invisible | B | CR-1 (op 1) → CR-10a (emergency expected to end) → CR-4b (x: sell now, y: hold and sell later) | A-1, A-3, A-6 |
| C-6 | sellers.current (local independent sellers) | quantity_supplied (during the emergency) | decrease | short | invisible | B | CR-1 (op 1) → CR-10a → CR-4b (x: sell now, y: hold) | A-1, A-3, A-6 |
| C-7 | buyers.current | excess_demand (covered goods and rooms) | increase | short | visible | B | CR-6 (price held below clearing) with C-3, C-4, C-6 → CR-12a | A-1, A-3 |
| C-8 | buyers.current | quantity_traded (legal sales of covered goods in declared counties) | decrease | short | invisible | B | CR-6 (trade limited by sellers' offers) → C-4 → CR-5a (prevented exchanges) | A-1, A-3, A-4, A-5 |
| C-9 | buyers.current | wait_time, search_cost, allocation_by_non_price_criteria | at_least_one_increase | short | invisible | B | CR-6 (pressure displaced to criteria by which sellers choose among buyers) → CR-8c | A-1, A-3 |
| C-10 | sellers.current (hotels) | quality_per_unit (room services and stay conditions) | decrease | short | invisible | B | CR-6 (pressure displaced to unregulated terms) → CR-4b (x: full service, y: reduced service) | A-1, A-3, A-7 |
| C-11 | sellers.current | reclassification (bundles, new models, relabeled fees, costs routed through documented channels) | increase | short | invisible | B | CR-6 → CR-4b (x: covered form, y: uncovered form); CR-1 (K2 op 2) → CR-4b (x: undocumented cost, y: documented cost) → CR-12a | A-1, A-3, A-9 |
| C-12 | intermediaries | informal_activity (sales above the cap) | increase | short | invisible | B | CR-6 (exchanges outside the rule) → CR-4b (x: comply, y: violate) | A-1, A-10 |
| C-13 | buyers.current (in informal sales) | quality_information | decrease | short | invisible | B | C-12 → CR-11b (reputation and recourse unavailable outside the legal market) | A-1, A-10 |
| C-14 | buyers.current (guests in rooms) | turnover (room check-outs) | decrease | short | invisible | B | CR-1 (op 3) → CR-4b (x: check out, y: keep the room) → CR-3 (leaving gives up a below-clearing room) | A-1, A-3, A-8 |
| C-15 | buyers.prospective (outside repair crews) | search_cost (lodging) | increase | short | invisible | B | C-7, C-14 → CR-9 (same market: crews compete with sitting guests) → CR-6 (criteria margin) | A-1, A-3, A-8, A-11 |
| C-16 | buyers.repair_services | quantity_traded (repair and tree-removal services) | decrease | short | invisible | B | U1-a: C-15 → CR-9 (rooms input_to repair) → CR-4b (x: work in declared counties, y: elsewhere) → CR-5a; U1-b: CR-1 (op 1) → CR-4b → CR-5a | U1-a: A-1, A-3, A-8, A-11, A-N2; U1-b: A-3, A-N1, A-N2 |
| C-17 | buyers.repair_services | price_paid (repair and tree-removal services) | U1-a: increase; U1-b: decrease | short | invisible | B | U1-a: as C-16 → CR-6 (unregulated price moves toward clearing); U1-b: CR-1 (op 1) → CR-6 | U1-a: A-1, A-3, A-8, A-11, A-N2; U1-b: A-3, A-N1 |
| C-18 | buyers.current | cross_border_purchases (covered goods bought inland and in Hallorn) | increase | short | invisible | B | C-7 → CR-4b (x: wait for local supply, y: travel) | A-1, A-3, A-12 |
| C-19 | neighboring_jurisdictions (inland and Hallorn sellers) | quantity_substitute (covered goods sold outside declared counties) | increase | short | invisible | B | C-4 → CR-7a; C-18 → CR-9 (across_border) → CR-12a | A-1, A-3, A-4, A-5 |
| C-20 | neighboring_jurisdictions (inland and Hallorn sellers) | price_substitute (covered goods outside declared counties) | ambiguous | short | invisible | B | (+) C-18 → CR-9 (across_border) → CR-6; (−) C-4 → CR-7a → CR-12b | A-1, A-3, A-4, A-5, A-12 |
| C-21 | buyers.current | quantity_substitute (ice, staying with relatives) | increase | short | invisible | B | CR-6 → CR-4b (x: covered good, y: substitute) | A-1, A-3, A-13 |
| C-22 | buyers.current | full_cost_per_unit | ambiguous | short | invisible | B | (−) C-1; (+) C-9 → CR-6 (full price moves toward clearing) → CR-12b | A-1, A-3 |
| C-23 | sellers.current | compliance_cost (base-period records, cost documentation) | increase | short | invisible | B | CR-1 (op 3: records attached to selling) → CR-8c | A-3 |
| C-24 | officials.enforcement | enforcement_cost | increase | short | visible | A | CR-1 (K3) → CR-8c | none |
| C-25 | taxpayers | resources_available_other_uses (other Attorney General work) | decrease | short | invisible | A | C-24 → CR-8a | none |
| C-26 | sellers.current (retailers, future seasons) | inventory_held (pre-season stocks of covered goods) | decrease | long | invisible | B | CR-10a (cap expected in future storms) → CR-4b (x: hold extra stock, y: not) → CR-3 (holding cost unchanged) | A-1, A-14, A-17 |
| C-27 | buyers.current (households, future seasons) | inventory_held (household storm supplies before the season) | ambiguous | long | invisible | B | CR-10a → CR-4 (y: buy after landfall made cheaper by C-1 and harder by C-7, C-26) → CR-12b | A-1, A-14, A-15 |

## Gaps found

**(a) Calculus gaps.** None. Every step was derived from CR-1 to CR-12 and the foundations.

**(b) New premises.**
- A-N1 (p 0.8, binding): needed only under reading U1-b, to say that a cap on repair services would bind; the case assumptions state bindingness only for goods and rooms.
- A-N2 (p 0.75, alternative_uses): CR-4b needs some crews to be at the margin between working in the declared counties and working elsewhere; A-11 says crews depend on local rooms but not that they have other work to go to.
- A-N3 (p 0.45, other): CR-4 (x: accept, y: lobby) gives a direction but needs a premise that some bound sellers are at that margin; with no evidence in the case it is set below the cut-off and the lobbying chain is not reported.

**(c) Unclear core rules.**
- CR-4 with two option changes at once (C-27): the cap makes buying after landfall cheaper in money and harder to obtain. CR-4 is stated for a change that makes x worse relative to y; it does not say how to treat a change that moves y both ways. The analysis treated it as two CR-4 applications combined under CR-12b; a sentence in CR-4 saying so would help.
- CR-6 versus CR-10a on held stock (C-5): CR-6 lists the open margins as terms, criteria and exchanges outside the rule; timing appears only in "terms (…timing)". Holding goods for sale after the price rule lapses is a timing margin, but it is not clear whether CR-6 or CR-10a is the governing clause; the analysis cites both.
- CR-12d with alternative chains (C-8, C-19): CR-12d says a consequence holds only if all its premises hold, which reads naturally for one chain. When two independent chains each establish the same sign, it is unclear whether the consequence's assumptions are the union or either set. The analysis lists the minimal set of one sufficient chain.
