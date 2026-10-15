# WE-006 Anti-price-gouging law during a declared hurricane emergency

Analyst: draft (Handbook 0.3)  |  Rule catalog version: 0.3  |  Status: awaiting expert review

A stylized policy in a fictional state. Many places have laws of this kind; this one is not modeled on any of them. The probabilities are illustrative; the evidence column says what a real analysis would cite. The analysis gives particular attention to supplies brought in from outside the affected area and to the timing of decisions before, during and after the emergency.

## 1. Policy record

**Coralia Emergency Pricing Act.** Coralia is a coastal state. The Act was passed two years ago and is a standing law: it applies automatically whenever the governor declares a state of emergency for named counties. This season a hurricane is forecast to strike the six coastal counties (about 1.8 million people). The governor declares an emergency for those counties two days before landfall. A declaration lasts 30 days and may be renewed in 30-day steps; the governor has said it will be renewed "as long as needed". The inland counties of Coralia, 60 to 150 miles from the coast, are not declared. The neighboring state of Hallorn, about three hours north, has no such law. For the first two or three days after landfall, roads into the coast are partly blocked.

The counterfactual is the same hurricane and the same declaration (with its other emergency powers, such as public water distribution and curfews), without the Act's pricing rules.

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Price cap | `price_ceiling` | Generators and fuel cans; bottled water; plywood, tarps and other building materials; hotel, motel and short-term rental rooms; sold or rented in the declared counties | Every seller of these goods in the declared counties, including sellers from outside the area selling there and online sellers delivering there | Price may not exceed 110% of the seller's own average price in the 30 days before the declaration. A seller who did not sell the item then may not charge more than 110% of the average price of the item in that county before the declaration. Applies for the whole declared emergency. | None |
| K2 Cost defense | Exception to K1 | Same | Same | A seller may add any documented increase in its own costs (purchase price, freight) since the base period, but may not raise its markup. | None |
| K3 Enforcement | Administration and enforcement | K1, K2 | State Attorney General | Civil penalty up to $10,000 per violation; repeat violations are a misdemeanor; a public hotline; staff deployed to the declared area; cases are publicized. Funded from the Attorney General's budget. | None |

Unclear provisions: whether repair and tree-removal services count as covered "necessities". The list names goods and lodging only, so assumed not covered; if they were covered, outside repair crews would face the same incentives as outside sellers of goods (C-6). Also unclear: whether minimum-stay rules and deposits count as part of a room's price. Assumed not (fees are counted; conditions are not).

## 2. Classification

| Component | Rothbard type | Binding? | Rule families |
|---|---|---|---|
| K1 | Triangular: fixes the terms of exchange between sellers and buyers in the declared area | Yes for generators, plywood, water and rooms in the first two to three weeks, for independent sellers, sellers from outside the area and hotels (A-1). Large chain stores often hold prices below the cap for reasons of reputation in any case (A-2), so for them it may not bind. | PC, RS, TS |
| K2 | Triangular (softens K1) | Allows increases in documented cost, not in scarcity value | RS-5, OC-2 |
| K3 | Binary: funded by taxpayers | Yes | OC-3 |

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `residents.declared` | Households and businesses in the six counties, including evacuees seeking rooms | Lower money prices where goods can be found; more goods sold out. Split into `buyers.served` (who obtain goods at the capped price) and `buyers.unserved`. |
| `sellers.local` | Hardware stores, groceries and other sellers in the declared counties | Prices capped; can hold stock, change terms, document costs. |
| `sellers.outside` | Firms and individuals in inland counties and in Hallorn who could bring goods into the area (trucks of generators, water, plywood) | Their price in the area is capped at the pre-emergency level plus documented costs; elsewhere it is not. |
| `hotels.declared` | Hotels, motels and short-term rentals in the declared counties | Room rates capped; rooms are fixed in number. |
| `evacuees.in_rooms` | Guests who hold a room at the capped rate | Lose the room if they leave. |
| `repair_contractors.outside` | Roofers, tree crews and insurance adjusters from outside the area | Need somewhere to stay while they work. |
| `sellers.inland` | Stores in undeclared inland counties | Some coastal buyers. |
| `households.coastal` | Coastal households before any storm | Choose how much to buy and store ahead of the season. |
| `officials.enforcement`, `taxpayers` | Attorney General's office and its funders | Enforcement during each emergency. |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | `buyers.served` | `price_paid` (covered goods and rooms) | decrease | short | K1, PC-3 | A-1, A-3 |

The visible effect: households who find a generator, water, plywood or a room pay close to the pre-storm price, not the much higher price the storm would otherwise bring.

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-2 | `residents.declared` | `quantity_demanded` (more water and generators per household; evacuee families take more rooms, or larger ones) | increase | short | PC-1, LW-3 | A-1 |
| C-3 | `residents.declared` | `excess_demand` | increase | short | PC-1 | A-1, A-3 |
| C-4 | `residents.declared` | `wait_time` (lines outside stores before and after landfall) | increase | short | PC-2, OC-2 | A-1, A-3 |
| C-5 | `residents.declared` | `allocation_by_non_price_criteria` (first come, per-customer limits, regular customers, those who could shop before the storm) | increase | short | PC-2 | A-1, A-3 |
| C-6 | `sellers.outside` | `quantity_supplied` (goods brought into the declared counties) | decrease | short | PC-5, LW-4, RS-4 | A-1, A-3, A-4, A-5 |
| C-7 | `sellers.outside` | `number_of_sellers` (individuals and small firms trucking goods in, relative to established chains) | decrease | short | PC-13 | A-1, A-3, A-5 |
| C-8 | `sellers.local` | `quantity_supplied` (stored goods such as plywood and generators, during the emergency) | decrease | short | RS-8 | A-1, A-6 |
| C-9 | `sellers.local` | `quantity_supplied` (the same goods, in the first weeks after the emergency ends) | increase | short | RS-8 | A-1, A-6 |
| C-10 | `hotels.declared` | `quality_per_unit` (housekeeping and services cut; minimum stays and deposits added) | decrease | short | PC-4, RS-2 | A-1, A-7 |
| C-11 | `evacuees.in_rooms` | `turnover` | decrease | short | PC-7 | A-1, A-8 |
| C-12 | `sellers.local`, `sellers.outside` | `reclassification` (generators sold bundled with delivery or installation; models not sold before the declaration; fees relabeled as costs) | increase | short | RS-5 | A-1, A-9 |
| C-13 | `sellers.local`, `sellers.outside` | `compliance_cost` (records to document costs under K2) | increase | short | PC-13, OC-2 | A-1, A-3 |
| C-14 | `residents.declared` | `informal_activity` (cash sales from trucks and through online listings above the cap) | increase | short | PC-6, RS-3 | A-1, A-10 |
| C-15 | `sellers.local`, `hotels.declared` | `lobbying_effort` (for a wider cost defense or exemptions; consumer groups for coverage of repair services) | increase | medium | RS-7 | A-1 |

C-6 is the central supply effect. In the counterfactual, the price spike in the declared area is what pays a hardware dealer three hours away to load a truck with generators, drive it through damaged roads and sell the load, or pays a chain to divert stock from inland stores. The cap does not stop this, but it lowers the reward. K2 lets a seller pass on documented freight. It does not cover what is hardest to document and what matters most in an emergency: the owner's own time, the risk of damage or of being stuck with unsold stock, and the value the goods would have had in the market they were taken from (A-5). PC-5 is applied here at a short horizon, as in WE-005: the resources that move are truckloads, not durable capital.

C-7 adds a composition effect (PC-13). A cap that allows documented costs falls hardest on sellers who have no invoices for their main costs (an individual with a pickup truck) and least on established firms with freight accounts. It therefore changes not just how much is brought in but who brings it. PC-13 also gives the documentation burden on sellers who use the defense (C-13). Both rest on the Attorney General's definition of a documentable cost (A-5).

C-8 and C-9: plywood and generators keep. Demand for plywood stays high for months during rebuilding. A local seller who expects the emergency to end within weeks (A-6) gains by holding part of its stock until the cap lapses. The Act does not require sellers to sell.

C-11 applies PC-7: an evacuee who checks out gives up a capped room and may not find another, so guests stay longer than they otherwise would, even after their home is habitable or when a relative's home becomes available.

Not reported: outside sellers staying away for the whole season because they expect repeated renewals (TS-2); A-16 is below the cut-off (p = 0.4).

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-16 | `residents.declared` | `search_cost` (driving between stores, finding informal sellers) | increase | short | PC-2, RS-10 | | A-1, A-3 |
| C-17 | `buyers.unserved` | `quantity_substitute` (ice and coolers, candles, staying with relatives, going without) | increase | short | PC-3, RS-1 | generators and ice: `substitute`, partial; rooms and relatives' homes: `substitute`, partial | A-1, A-13 |
| C-18 | `residents.declared` | `cross_border_purchases` (in inland counties and Hallorn) | ambiguous (section 7) | short | RS-4, PC-2, PC-3 | coastal and inland stores: `across_border`, partial | A-12 |
| C-19 | `repair_contractors.outside` | `quantity_supplied` (repair work done in the declared counties) | decrease | short | PC-1, PC-7, LW-4 | rooms in the declared counties and outside repair labor: `complement`, note `location` | A-1, A-8, A-11 |
| C-20 | `sellers.local` | `inventory_held` (generators, plywood and water stocked before each season) | decrease | medium | TS-7 | | A-14, A-17 |
| C-21 | `households.coastal` | `quantity_demanded` (generators and supplies bought before the season) | ambiguous (section 7) | medium | RS-8 | | A-15 |

C-19 is at depth 4: the cap (1) produces excess demand for rooms (2), which are held by the first arrivals and turn over slowly (3, C-11), so contractors from outside who rely on local rooms find none, or stay far inland and work fewer hours on site (4). In the counterfactual, contractors and insurers would outbid many evacuees for rooms, and evacuees would double up or stay further inland. The chain stops here; the effect on how fast homes are repaired has no variable in version 1.

C-20 and C-21 are the time-structure effects of a standing law. Because the Act is permanent, everyone knows before each season that emergency prices will be capped. In the counterfactual, a seller who stocks extra generators before the season is paid for the cost of storing them, and for the risk that no storm comes, by the high price it can charge if one does. The Act caps that payoff, so sellers stock less (C-20, TS-7). It rests on sellers expecting the cap to bind in future storms (A-14) and on storage being costly (A-17). Its consequence matters: fewer goods are already in the area when the storm hits, which is exactly when goods from outside cannot yet get in (roads blocked for two to three days).

RS-9 was checked: if coastal buyers drive inland for generators, they buy fuel and food there too. But the sign of C-18 is ambiguous, so the trip effect inherits that ambiguity and is not listed separately. RS-10 is recorded in C-16. RS-11 was checked: evacuees hold a room tied to a place, but the linked choice the rule is about (taking jobs elsewhere) is not at stake during a 30-day emergency; the effect is recorded as C-11.

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `residents.declared`, `cross_border_purchases`, short | Goods sold out at home (C-3, C-6, C-8) push buyers who must have a generator to drive inland. | Capped prices at home reduce the money gained by buying inland, where prices are uncapped (C-1). | None | **ambiguous**. In the counterfactual, high coastal prices also send buyers inland. |
| `households.coastal`, `quantity_demanded` (before the season), medium | Households expect goods to be sold out after a storm, so buying early is more favorable (RS-8). | Households expect post-storm prices to be capped, so waiting costs less in money (RS-8). | None | **ambiguous**. It depends on which expectation households hold more strongly. |
| `buyers.unserved`, `sellers.outside`, `quantity_traded` (covered goods during the emergency), short (C-22) | None during the emergency. Stock held back is released after it (C-9), which is a different period. | Fewer goods brought in from outside (C-6); stored stock held back (C-8); smaller pre-season stocks (C-20). | None needed | **decrease**. All three chains agree. |

## 8. Time structure

The law affects four periods differently.

- **Before the season (every year).** Because the law is standing, it changes decisions made long before any storm. Sellers stock fewer generators and less plywood in coastal stores (C-20, TS-7). Households may stock more or less (C-21, ambiguous). Neither the cap nor its effects show up in prices in this period; they show up as smaller or larger shelves when the storm comes.
- **Declaration to landfall (two days).** The cap starts before landfall. Prices cannot ration the rush of buying in the last two days, so stocks go to those who shop first and buy most (C-2, C-5). In the counterfactual, rising prices in these two days would lead buyers to take less each and leave more for those who shop later.
- **First two to three weeks.** Roads open over the first days; goods from outside could then arrive. This is when the reduced inflow from outside (C-6) matters most, and when local sellers holding durable goods gain from waiting (C-8). Rooms stay with early arrivals (C-11), which keeps repair crews away or far inland (C-19).
- **After the emergency ends.** Held-back stock is released (C-9). Because the declaration can be renewed in 30-day steps, sellers do not know when this will be. If they came to expect repeated renewals, holding stock would not pay, but neither would bringing goods in from outside for a longer time (A-16, below the cut-off).

Compared with the counterfactual, the law lowers the money price during the emergency and changes the time path of supply: less is stored before the storm, less comes in during the first weeks, and some stock moves from during the emergency to after it. No durable capital is involved apart from the stocks themselves; TS-1 and TS-3 do not apply.

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-22 | `buyers.unserved`, `sellers.outside` | `quantity_traded` (covered goods and rooms during the emergency) | decrease | Generators, water, plywood and rooms that would have been brought in and sold at the uncapped price. Both sides lose the gain each expected. | OC-4 |
| C-23 | `taxpayers` | `resources_available_other_uses` | decrease | What the Attorney General's emergency staff and budget would otherwise have done. | OC-3, OC-1 |

Time in lines and searching is recorded as C-4 and C-16; documentation as C-13.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | Without the Act, prices of covered goods and rooms would rise more than 10% above the base plus documented cost increases, for independent sellers, outside sellers and hotels, in the first weeks. | binding | 0.85 | Prices in comparable storms in places without such laws; online listing prices. | Most consequences fail. |
| A-2 | Large chains keep prices below the cap anyway, so the Act binds mainly on others. | other | 0.7 | Chains' pricing in past storms. | The Act binds more widely; C-1 and C-6 grow. |
| A-3 | The Attorney General enforces actively in the declared area, including against outside sellers. | enforcement | 0.75 | Staff deployed; past prosecutions; publicity. | C-1 shrinks; C-6 and C-7 weaken; C-14 grows. |
| A-4 | Goods that could be brought in can be sold elsewhere at normal prices. | alternative_uses | 0.9 | Inland and out-of-state demand for the same goods. | C-6 weakens. |
| A-5 | As the Attorney General applies K2, the extra costs of an emergency trip (own time, risk, unsold stock, value elsewhere) are mostly not accepted as documented costs. | enforcement | 0.75 | Attorney General guidance on what counts as a cost. | C-6 and C-7 weaken. |
| A-6 | Local sellers expect the emergency to end within weeks, can store durable goods, and are not required to sell. | expectations | 0.55 | Renewal history; text of the Act; storage space. | C-8, C-9 not reported. |
| A-7 | Hotels may change services and stay conditions (the Act caps the charge only). | other | 0.75 | Text of the Act; Attorney General guidance. | C-10 not reported. |
| A-8 | A guest who checks out loses the capped room and cannot pass it on. | other | 0.85 | Hotel practice; occupancy during the emergency. | C-11 and C-19 weaken. |
| A-9 | Bundling, new models and relabeled fees are open to some sellers. | other | 0.6 | Definitions in the Act; past enforcement cases. | C-12 not reported. |
| A-10 | Some informal sales above the cap go undetected. | enforcement | 0.6 | Online listings in past emergencies; enforcement focus on stores. | C-14 not reported. |
| A-11 | Some outside repair contractors rely on local rooms, and their other lodging is far away. | mobility | 0.6 | Share of crews with their own staging camps; distance to inland hotels. | C-19 not reported. |
| A-12 | Inland stores can be reached within days of landfall. | mobility | 0.7 | Road damage reports; distance of 60 to 150 miles. | C-18 not reported. |
| A-13 | Some unserved buyers have substitutes (ice, relatives' homes). | substitutability | 0.8 | Ice distribution; household surveys. | C-17 weakens. |
| A-14 | Sellers expect the cap to bind in future storms. | expectations | 0.75 | The law is standing and was enforced in the last declaration. | C-20 fails. |
| A-15 | Households know the Act and expect it to apply in future storms. | expectations | 0.55 | Awareness surveys; publicity of past cases. | C-21 not reported. |
| A-16 | Sellers expect the emergency to be renewed for months. | expectations | 0.4 | Governor's statements; renewal history. | Below cut-off; not reported. |
| A-17 | Holding extra stock before the season is costly to sellers (floor and warehouse space, money tied up, stock left unsold or marked down if no storm comes). | other | 0.9 | Retail space costs; end-of-season markdowns of generators and plywood in years without a storm. | C-20 fails: if storage were free, sellers would hold stocks whatever the expected price. |

## 11. Report

**The policy.** While an emergency is declared, Coralia forbids sellers in the declared counties to charge more than 10% above their pre-emergency price for generators, water, building materials and rooms, plus any documented increase in their own costs. The rule is permanent and applies whenever the governor declares an emergency.

**Visible consequences.** Households who find these goods, or a room, pay about the pre-storm price (C-1).

**Invisible consequences.**
- *Residents of the declared counties* want more of the goods at the capped price (C-2) than are available (C-3). They wait in lines and drive from store to store (C-4, C-16). Goods go to those who shop first, those with connections and regular customers, within per-customer limits (C-5). Some buy from informal sellers above the cap (C-14). Those who find nothing use ice, candles or relatives' homes, or go without (C-17). Fewer goods are sold in the area during the emergency than would have been (C-22).
- *Sellers outside the area* bring fewer goods in, because the cap removes most of the reward for the cost and risk of an emergency trip (C-6). Individuals and small firms without documented costs are deterred more than established chains (C-7). Sellers reshape products and fees to fit the rules (C-12) and spend time documenting costs (C-13).
- *Local sellers* hold some durable stock until the emergency ends (C-8, C-9). Because the law is permanent, they also keep smaller stocks before each season (C-20), so fewer goods are already in the area in the first days after landfall, when roads from outside are blocked.
- *Hotels* cut services and add conditions (C-10). Guests holding rooms stay longer (C-11). Repair contractors from outside find fewer rooms and do less work in the area (C-19).
- *Interested groups* lobby over the rules (C-15). *Taxpayers* fund enforcement (C-23).

**Ambiguous effects.** Whether residents buy more or less inland during the emergency. Whether households stock more or less before the season.

**Key conditions.** The cap must bind (A-1, p = 0.85). The supply effects rest on the costs of emergency trips being hard to document (A-5, p = 0.75) and on active enforcement against outside sellers (A-3, p = 0.75). Smaller pre-season stocks rest on sellers expecting the cap in future storms (A-14, p = 0.75). The holding-back effect (C-8) is the least certain reported result (A-6, p = 0.55).

**What this analysis cannot say.** How much less is brought in, how much longer shortages last, or how much repairs are delayed; whether the lower prices for those served outweigh the effects on those not served; effects on health, safety and property damage (out of scope for version 1); whether the law is fair or desirable.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | buyers.served | price_paid | decrease | short | visible | B | K1, PC-3 | A-1, A-3 |
| C-2 | residents.declared | quantity_demanded | increase | short | invisible | B | PC-1, LW-3 | A-1 |
| C-3 | residents.declared | excess_demand | increase | short | invisible | B | PC-1 | A-1, A-3 |
| C-4 | residents.declared | wait_time | increase | short | invisible | B | PC-1, PC-2, OC-2 | A-1, A-3 |
| C-5 | residents.declared | allocation_by_non_price_criteria | increase | short | invisible | B | PC-1, PC-2 | A-1, A-3 |
| C-6 | sellers.outside | quantity_supplied (into declared counties) | decrease | short | invisible | B | PC-5, LW-4, RS-4 | A-1, A-3, A-4, A-5 |
| C-7 | sellers.outside | number_of_sellers (ad hoc sellers) | decrease | short | invisible | B | PC-1, PC-13 | A-1, A-3, A-5 |
| C-8 | sellers.local | quantity_supplied (stored goods, during emergency) | decrease | short | invisible | B | RS-8 | A-1, A-6 |
| C-9 | sellers.local | quantity_supplied (stored goods, after emergency) | increase | short | invisible | B | RS-8 | A-1, A-6 |
| C-10 | hotels.declared | quality_per_unit | decrease | short | invisible | B | PC-4, RS-2 | A-1, A-7 |
| C-11 | evacuees.in_rooms | turnover | decrease | short | invisible | B | PC-7 | A-1, A-8 |
| C-12 | sellers.local, sellers.outside | reclassification | increase | short | invisible | B | RS-5 | A-1, A-9 |
| C-13 | sellers.local, sellers.outside | compliance_cost | increase | short | invisible | B | PC-13, OC-2 | A-1, A-3 |
| C-14 | residents.declared | informal_activity | increase | short | invisible | B | PC-6, RS-3 | A-1, A-10 |
| C-15 | sellers.local, hotels.declared | lobbying_effort | increase | medium | invisible | B | RS-7 | A-1 |
| C-16 | residents.declared | search_cost | increase | short | invisible | B | PC-2, RS-10 | A-1, A-3 |
| C-17 | buyers.unserved | quantity_substitute | increase | short | invisible | B | PC-3, RS-1 | A-1, A-13 |
| C-18 | residents.declared | cross_border_purchases | ambiguous | short | invisible | B | RS-4 vs PC-3 (C-3, C-6 vs C-1) | A-1, A-12 |
| C-19 | repair_contractors.outside | quantity_supplied (repair work in area) | decrease | short | invisible | B | PC-1, PC-7, LW-4 | A-1, A-8, A-11 |
| C-20 | sellers.local | inventory_held (before each season) | decrease | medium | invisible | B | TS-7 | A-14, A-17 |
| C-21 | households.coastal | quantity_demanded (before the season) | ambiguous | medium | invisible | B | RS-8 vs RS-8 | A-15 |
| C-22 | buyers.unserved, sellers.outside | quantity_traded (during emergency) | decrease | short | invisible | B | PC-5, OC-4 | A-1, A-3, A-4, A-5 |
| C-23 | taxpayers | resources_available_other_uses | decrease | short | invisible | A | OC-3, OC-1 | none |

## Gaps found

- GAP-006-1 (closed in catalog 0.3: TS-7 and `inventory_held`). C-20 is now Tier B, resting on A-14 (sellers expect the cap in future storms) and the new A-17 (storage is costly). The third combined entry in section 7 no longer has a Tier C chain.
- GAP-006-2 (closed in catalog 0.3: PC-13). C-7 is now Tier B; PC-13 also supplies the documentation cost in C-13. A-5 is retyped `enforcement`, as PC-13 requires (the agency's definition of a documentable cost).
