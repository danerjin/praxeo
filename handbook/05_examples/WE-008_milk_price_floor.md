# WE-008 Price floor for raw milk, with state purchase of the surplus

Analyst: draft (Handbook 0.3)  |  Rule catalog version: 0.3  |  Status: awaiting expert review

A stylized policy in a fictional state. It combines two instruments found in many farm-support schemes, a minimum price and a state agency that buys what the market will not take at that price, but it is not modeled on any particular scheme. The probabilities are illustrative; the evidence column says what a real analysis would cite.

## 1. Policy record

**Velmora Dairy Stabilization Act.** Velmora is a dairy state with about 3,000 dairy farms. It produces about 15% of the milk in a regional market within which raw milk moves freely by tanker and cheese, butter and powder are traded freely. The neighboring states of Ostrand and Quillon, whose dairy areas lie 30 to 90 miles from Velmora's, have no floor. Raw milk prices in the region have averaged $18 per hundredweight (cwt) over five years, varying between $15 and $22; forward prices for the next three years are $17 to $19.

The governor proposed the program in February of Year 0. It was enacted in June and takes effect on January 1 of Year 1. It has no expiry date; the legislature reviews it every four years. It is funded by an open-ended ("sum sufficient") appropriation from the general fund.

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Minimum milk price | `price_floor` | Raw milk produced on farms registered in Velmora | Any plant located in Velmora that buys it | At least $21.00 per cwt (standard components). Not indexed. | Milk produced outside Velmora, even when processed in Velmora. |
| K2 State purchase | State purchase at a support price (treated as a `per_unit_subsidy` to K1; SB family) | Block cheddar and nonfat dry milk | Velmora Dairy Board | The Board buys any quantity offered by licensed Velmora plants, at $2.05 a pound for cheddar and $1.40 for powder (prices set so that a plant paying $21 for milk breaks even), provided the product is certified as made from Velmora milk paid at least the floor. Stocks are held in leased warehouses. | None |
| K3 Disposal of stocks | Part of K2 | Board stocks | Velmora Dairy Board | The Board may sell stocks back into the market when market prices exceed 110% of its purchase price, donate them to school meals and food banks in Velmora, or sell them for export. | None |
| K4 Certification and enforcement | Administration and enforcement | K1, K2 | Velmora Dairy Board | Plants must keep Velmora milk separate and document its origin; audits; penalties are fines and loss of eligibility for Board sales. | None |

Unclear provisions: whether a farm that moves into Velmora after enactment qualifies at once. Assumed yes, after a three-month registration.

## 2. Classification

| Component | Rothbard type | Binding? | Rule families |
|---|---|---|---|
| K1 | Triangular: fixes the terms of exchange between Velmora farmers and Velmora plants | Yes, when the regional price is below $21, which forward prices suggest for most of the next three years (A-1) | PC, RS |
| K2, K3 | Binary: the state buys from plants with taxpayers' money | Yes, whenever K1 binds: the Board is the buyer that makes the floor hold | SB, OC |
| K4 | Binary: funded by taxpayers | Yes | OC-3 |

Because the Board buys everything offered at the support prices, PC-9's "unless" clause applies: there is no lasting unsold surplus in private hands, so PC-11 (non-price selection among excess sellers) does not apply. The surplus becomes the Board's stock instead.

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `farmers.velmora` | Dairy farmers in Velmora | Guaranteed $21 for all the milk they can sell to a Velmora plant. |
| `farmers.prospective` | Would-be dairy farmers, including farmers across the border who could move | Dairy in Velmora pays better. |
| `plants.commodity` | Velmora plants making cheddar and powder | Can buy Velmora milk at $21 and sell to the Board at break-even. |
| `plants.specialty` | Velmora makers of cheese sold under a "Velmora" origin label | Must pay $21 for Velmora milk but sell at market prices. |
| `plants.market` | Velmora plants making fluid milk and other products for the market | Can use out-of-state milk at market prices. |
| `consumers` | Buyers of dairy products in the region | Less product on the market. |
| `farmers.neighbors` | Farmers in Ostrand and Quillon | Velmora plants buy more of their milk. |
| `input_suppliers` | Sellers of feed, heifers, equipment | More demand from Velmora dairy. |
| `factor_owners.specific` | Owners of Velmora dairy land, barns and herds | Returns rise. |
| `farmers.other_uses` | Users of Velmora farmland for crops or beef | Land stays in dairy. |
| `sellers.to_food_programs` (`sellers.substitutes`) | Firms that sell dairy products to school meals and food banks | Compete with donated Board stocks. |
| `officials.enforcement` (Dairy Board), `taxpayers` | Program administrator and its funders | Purchase, storage and audit costs. |

## 4. Direct effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | `farmers.velmora` | `net_price_received` | increase | short | K1, PC-9, SB-2 | A-1 |
| C-2 | `officials.enforcement` (Dairy Board) | `quantity_demanded` (purchases of cheddar and powder) | increase | short | K2, SB-2 | A-1 |

The visible effects: Velmora dairy farmers receive at least $21 per cwt instead of about $18, and the Board buys cheese and powder.

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-3 | `farmers.velmora` | `quantity_supplied` (more feed per cow, fewer cows culled) | increase | short | SB-2, LW-4 | A-1 |
| C-4 | `farmers.velmora` | `investment_target` (herd expansion, barns, milking equipment) | increase | medium | SB-2, LW-4, TS-1 | A-1, A-2 |
| C-5 | `farmers.velmora` | `number_of_sellers` (farms that would have closed stay open) | increase | medium to long | SB-2, LW-4 | A-1, A-2 |
| C-6 | `plants.specialty` | `price_paid` (raw Velmora milk) | increase | short | K1 | A-1 |
| C-7 | `plants.specialty` | `quantity_supplied` (Velmora-labeled cheese) | decrease | medium | RS-6, LW-4 | A-1, A-4 |
| C-8 | `plants.market` | `quantity_substitute` (out-of-state raw milk in place of Velmora milk) | increase | short | RS-1 | A-1, A-5 |
| C-9 | `plants.commodity` | `investment_target` (cheddar and powder capacity) | increase | medium | SB-2, LW-4 | A-1, A-2 |
| C-10 | `plants.commodity` | `compliance_cost` (keeping Velmora milk separate; origin records) | increase | short | OC-2 | none |
| C-11 | `plants.commodity`, `farmers.neighbors` | `reclassification` (out-of-state milk passed off as Velmora milk for Board sales) | increase | short | RS-3, RS-5 | A-1, A-6 |
| C-12 | `farmers.prospective` (across the border) | `entry_rate` (farms moved or registered into Velmora) | increase | long | GAP-008-1, SB-5 | A-1, A-2, A-7 |
| C-13 | `farmers.velmora`, `plants.commodity` | `lobbying_effort` (to keep and raise the floor) | increase | medium | RS-7, SB-5 | A-2 |

C-3 to C-5: in the short run, farmers can add milk only by feeding cows more and keeping older cows longer. Herds grow more slowly, because a heifer takes about two years to come into milk, and barns take a season or two to build (TS-1). So the supply response is small at first and grows over the medium run, as long as farmers expect the program to last (A-2).

C-6 to C-8 show how the floor splits Velmora's processors. Commodity plants are protected: they pay $21 and sell to the Board at prices set to cover it. Specialty plants, whose label requires Velmora milk, pay $21 but sell at market prices, so their margins shrink and some cut output (C-7). Plants making fluid milk and other market products are free to buy out-of-state milk and do (C-8). The result is that Velmora milk flows into Board products and out-of-state milk flows into Velmora's market products.

C-11: since out-of-state milk costs about $18 and Velmora milk $21, a plant gains by certifying out-of-state milk as Velmora milk for Board sales (RS-3), and a farm near the border gains by routing milk through a registered Velmora address (RS-5).

C-12 needs a move the catalog does not have. RS-4 describes activity moving out of a jurisdiction to escape a burden. Here the policy favors activity inside the boundary, so farmers near it have reason to move in: lease or buy land in Velmora and register there. SB-5 (seeking to qualify) covers the motive but not the movement of production across a border. C-12 is Tier C (GAP-008-1).

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-14 | `consumers` | `price_paid` (cheese, butter, powder) | increase | short to medium | SB-3, LW-3 | Velmora and out-of-state dairy products: `same_market_other_segment`, close | A-1, A-3 |
| C-15 | `farmers.neighbors` | `net_price_received` | increase | short to medium | RS-1, GAP-008-3 | Velmora and out-of-state raw milk: `across_border`, close | A-1, A-5 |
| C-16 | `farmers.neighbors` | `quantity_supplied` | increase | medium | GAP-008-3, LW-4 | same | A-1, A-5 |
| C-17 | `input_suppliers` | `quantity_traded` (feed, heifers, equipment sold to Velmora dairy) | increase | medium | SB-3 | feed and milk: `input_to` | A-1, A-2 |
| C-18 | `factor_owners.specific` | `asset_value` (Velmora dairy farmland and barns) | increase | short to medium | SB-4 | | A-2, A-8 |
| C-19 | `farmers.other_uses` | `quantity_supplied` (crops and beef in Velmora) | decrease | medium to long | SB-3 | dairy and other farm uses: `substitute` (for land and labor), partial | A-1, A-10 |
| C-20 | `officials.enforcement` (Dairy Board) | `inventory_held` (cheddar and powder in storage) — not in the variable list | increase | short to medium | GAP-008-2 | | A-1 |
| C-21 | `sellers.to_food_programs` | `quantity_traded` (dairy sold to school meals and food banks in Velmora) | decrease | medium | GAP-008-2 | donated and purchased cheese: `substitute`, close | A-1, A-9 |

C-14: the Board takes Velmora's milk off the market in the form of stored cheese and powder. The market is offered less, so buyers pay more than they otherwise would, unless out-of-state supply replaces every pound at the old price. Because Velmora is about 15% of the region and other farms take time to expand, it does not do so at first (A-3).

C-15 and C-16 travel the other way. Velmora plants making market products switch to out-of-state milk (C-8), so demand for neighbors' milk rises and so does the price they receive. PC-8 describes this spillover only for ceilings, where demand spills to the uncontrolled segment from buyers who cannot obtain the controlled good. Here buyers leave the controlled segment because it costs more. The movement is the same in kind, but no rule covers it for floors (GAP-008-3), so C-15 and C-16 are Tier C. C-16 is at depth 4 and the chain stops.

C-18: dairy land and barns in Velmora are in fixed supply, so the expected stream of higher returns is capitalized into their price (SB-4), from the time the program became expected in February. Owners at that time gain. Farmers who buy in later pay the higher price and do not gain from the floor in the same way.

C-20 and C-21 rest on a missing variable and rule. The Board's stock grows whenever the floor binds. Cheddar keeps one to two years and powder two to three, so the Board must dispose of stocks within that time (K3). Donations to school meals and food banks replace dairy products those programs would otherwise have bought, so their usual suppliers sell less (C-21). Neither stocks nor disposal have a rule or variable in version 1 (GAP-008-2), so both are Tier C.

RS-9 and RS-11 were checked and do not apply: no buyer changes where they shop, and no benefit is tied to a buyer's location. RS-10 applies only to the false-origin trade in C-11, which takes place inside legal plants; no informal market for milk is expected. Pruned at depth 3: consumers outside the region, where Board exports are sold (diffuse, and outside the jurisdiction).

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `consumers`, `price_paid`, long | The Board keeps buying as long as the floor binds, removing product from the market (C-14). | Neighbors expand supply in response to higher prices (C-16, Tier C). The Board sells stocks back into the market or donates them before they spoil (C-20, C-21, Tier C). | None | **ambiguous**, Tier C. In the short and medium run the sign is **increase** (C-14). Over the long run, disposal and expansion elsewhere push the other way; the method cannot say which dominates. |
| `farmers.velmora` who own their land, `earnings`, short to medium | Higher price (C-1) on more milk (C-3). | None recorded. The extra feed and labor are used only where the farmer expects the extra milk to pay for them (LW-4). | None needed | **increase**. Their land also gains in value (C-18), which is recorded separately. |
| `farmers.velmora` who rent their land, `earnings`, medium | Higher price (C-1) on more milk (C-3). | Rents rise as the floor is capitalized into the value of dairy land (C-18, SB-4). | None | **ambiguous**. If rents rise by as much as the expected gain, tenant farmers keep little of it; the method cannot say how much of the gain the landowner captures. |
| `taxpayers`, `resources_available_other_uses`, short to long | — | Purchases, storage and audits (C-22, C-23), growing as supply responds (C-3, C-4). | — | **decrease**, growing over time. |

## 8. Time structure

- **Announcement (February to December of Year 0).** Land and barn prices rise as soon as the program is expected (C-18, SB-4). Farmers who were planning to sell their herds delay (C-5). Commodity plants plan capacity for Board products (C-9).
- **Year 1.** Supply rises a little through feeding and culling (C-3). The Board starts buying (C-2) and its stocks grow (C-20). Specialty plants feel the higher milk price at once (C-6).
- **Years 2 to 5.** Heifers raised in Year 1 come into milk; new barns are finished (C-4, TS-1). Supply from Velmora grows, so Board purchases and budget costs grow (C-22). Stocks bought in Year 1 approach the end of their shelf life and must be disposed of (K3), which begins to displace sales (C-21). Neighbors expand in response to higher regional prices (C-16).
- **The floor is fixed in money (TS-3).** Two forces change how much it binds. General inflation raises the market price of milk over time and so makes the floor bind less. Rising output per cow tends to lower the market price and so makes it bind more. The method cannot say which dominates; it can say that the program's cost will not stay at its first-year level.
- **Expectations (TS-2).** The investment responses (C-4, C-9, C-12) depend on farmers and plants expecting the program to last (A-2, p = 0.65). The review every four years matters: as a review approaches, investment that would pay only if the program continues is delayed. If repeal came to be expected (A-11, p = 0.3, not reported), the capital built for the program, including herds, would be specific to it, and its owners would bear the loss when it ended (TS-1).

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-22 | `taxpayers` | `resources_available_other_uses` | decrease | What the money spent on purchases and storage would otherwise have bought, privately or through other public spending. | SB-1, TX-1, OC-1 |
| C-23 | `officials.enforcement` (Dairy Board) | `enforcement_cost` (audits of milk origin, warehouse management) | increase | Staff and money that would otherwise have done other work. | OC-3 |
| C-24 | `consumers`, regional dairy sellers | `quantity_traded` (dairy products sold in the regional market) | decrease | Cheese, butter and powder that buyers would have bought at the lower counterfactual price, and that are instead stored, donated or exported. | PC-9, OC-4 |

The land and labor kept in dairy rather than in other farming are recorded as C-19.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | The regional raw milk price stays below $21 for most of the next three years. | binding | 0.8 | Forward prices of $17 to $19; five-year price history. | The program pays little; most consequences fail. |
| A-2 | Farmers and plants expect the program to last several years. | expectations | 0.65 | Open-ended appropriation; political support in the legislature; the four-year review. | C-4, C-5, C-9, C-12, C-17 and C-18 weaken. |
| A-3 | Out-of-state supply does not replace all of the withdrawn product at the old price in the short run. | substitutability | 0.75 | Velmora's 15% share; neighbors' capacity to expand; time to raise heifers. | C-14 and C-24 shrink to nothing. |
| A-4 | Specialty plants need Velmora-origin milk to keep their label and price premium. | other | 0.7 | Label rules; price premium of origin-labeled cheese. | C-7 weakens; they switch to out-of-state milk instead. |
| A-5 | Out-of-state raw milk reaches Velmora plants at little more than transport cost. | mobility | 0.85 | Tanker routes and costs of 30 to 90 miles. | C-8, C-15 and C-16 weaken. |
| A-6 | Some false certification of origin goes undetected. | enforcement | 0.55 | Audit frequency; ease of tracing tanker loads. | C-11 not reported. |
| A-7 | Moving a dairy operation, or registering one, into Velmora is feasible for some farmers near the border. | mobility | 0.6 | Land for lease near the border; cost of moving herds. | C-12 fails (Tier C). |
| A-8 | Dairy land and barns are in fixed supply in the medium run. | durability | 0.85 | Land use rules; time to build barns. | C-18 weakens; more of the gain goes to farmers' current income. |
| A-9 | Donated stocks replace dairy that food programs would otherwise have bought. | other | 0.7 | Food program budgets and purchase records. | C-21 fails (Tier C). |
| A-10 | Velmora farmland and farm labor have other farm uses (crops, beef). | alternative_uses | 0.8 | Land quality; crop rotations in the state. | C-19 not reported. |
| A-11 | The program is expected to be repealed within two years. | expectations | 0.3 | Budget debates; opposition statements. | Below cut-off; not reported. |

## 11. Report

**The policy.** Velmora requires plants in the state to pay at least $21 per cwt for milk from Velmora farms, about $3 above the expected market price. A state board buys any cheddar and powder made from that milk, at prices that cover the floor, and stores it until it can sell, donate or export it. The program is open-ended and paid for from the general budget.

**Visible consequences.** Velmora dairy farmers receive more for their milk (C-1). The state buys and stores cheese and powder (C-2).

**Invisible consequences.**
- *Velmora farmers* produce more, at first by feeding and culling, later by expanding herds (C-3, C-4), and fewer farms close (C-5). Farmers who own their land earn more; for those who rent, higher rents may take part or all of the gain, so their earnings are ambiguous (section 7). Owners of dairy land and barns gain as the program is capitalized into prices (C-18); later entrants pay for that gain.
- *Velmora plants* split. Commodity plants expand and sell to the Board (C-9) and bear certification costs (C-10). Specialty plants pay more for milk (C-6) and make less (C-7). Plants making fluid milk and other market products buy out-of-state milk instead (C-8). Some plants pass off out-of-state milk as Velmora milk (C-11).
- *Consumers* in the region pay more for dairy products (C-14) and buy less (C-24), at least in the short and medium run.
- *Neighboring farmers* and *input suppliers* sell more (C-17, and as Tier C suggestions C-15, C-16). Some farmers may move into Velmora (C-12, Tier C).
- *Other farming* in Velmora is smaller than it would be, because land and labor stay in dairy (C-19).
- *Taxpayers* pay for purchases, storage and audits (C-22, C-23), and the cost grows as supply responds. As Tier C suggestions: the Board's stocks grow (C-20), and their donation displaces sales by firms that supply school meals and food banks (C-21).
- *Interested groups* lobby to keep and raise the floor (C-13).

**Ambiguous effects.** The long-run effect on consumer prices, once stocks are released and neighbors expand. The earnings of farmers who rent their land.

**Key conditions.** The floor must bind (A-1, p = 0.8). The investment responses, and so the growth of the program's cost, depend on farmers expecting it to last (A-2, p = 0.65).

**What this analysis cannot say.** How large the surplus or the budget cost will be; whether farmers' gains outweigh the costs to consumers, taxpayers and other farmers; effects on nutrition in school meals or on the environment (out of scope for version 1); whether the program is desirable.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | farmers.velmora | net_price_received | increase | short | visible | B | K1, PC-9, SB-2 | A-1 |
| C-2 | Dairy Board | quantity_demanded (cheddar, powder) | increase | short | visible | B | K2, SB-2 | A-1 |
| C-3 | farmers.velmora | quantity_supplied | increase | short | invisible | B | SB-2, LW-4 | A-1 |
| C-4 | farmers.velmora | investment_target | increase | medium | invisible | B | SB-2, LW-4, TS-1 | A-1, A-2 |
| C-5 | farmers.velmora | number_of_sellers | increase | medium–long | invisible | B | SB-2, LW-4 | A-1, A-2 |
| C-6 | plants.specialty | price_paid (raw milk) | increase | short | invisible | B | K1 | A-1 |
| C-7 | plants.specialty | quantity_supplied (labeled cheese) | decrease | medium | invisible | B | RS-6, LW-4 | A-1, A-4 |
| C-8 | plants.market | quantity_substitute (out-of-state milk) | increase | short | invisible | B | RS-1 | A-1, A-5 |
| C-9 | plants.commodity | investment_target | increase | medium | invisible | B | SB-2, LW-4 | A-1, A-2 |
| C-10 | plants.commodity | compliance_cost | increase | short | invisible | A | OC-2 | none |
| C-11 | plants.commodity, farmers.neighbors | reclassification (false origin) | increase | short | invisible | B | RS-3, RS-5 | A-1, A-6 |
| C-12 | farmers.prospective | entry_rate (moves into Velmora) | increase | long | invisible | C | GAP-008-1, SB-5 | A-1, A-2, A-7 |
| C-13 | farmers.velmora, plants.commodity | lobbying_effort | increase | medium | invisible | B | RS-7, SB-5 | A-2 |
| C-14 | consumers | price_paid (dairy products) | increase | short–medium | invisible | B | SB-3, LW-3 | A-1, A-3 |
| C-15 | farmers.neighbors | net_price_received | increase | short–medium | invisible | C | RS-1, GAP-008-3 | A-1, A-5 |
| C-16 | farmers.neighbors | quantity_supplied | increase | medium | invisible | C | GAP-008-3, LW-4 | A-1, A-5 |
| C-17 | input_suppliers | quantity_traded | increase | medium | invisible | B | SB-3 | A-1, A-2 |
| C-18 | factor_owners.specific | asset_value | increase | short–medium | invisible | B | SB-4 | A-2, A-8 |
| C-19 | farmers.other_uses | quantity_supplied (crops, beef) | decrease | medium–long | invisible | B | SB-3 | A-1, A-10 |
| C-20 | Dairy Board | inventory_held (proposed variable) | increase | short–medium | invisible | C | GAP-008-2 | A-1 |
| C-21 | sellers.to_food_programs | quantity_traded | decrease | medium | invisible | C | GAP-008-2 | A-1, A-9 |
| C-22 | taxpayers | resources_available_other_uses | decrease | short–long | invisible | A | SB-1, TX-1, OC-1 | none |
| C-23 | Dairy Board | enforcement_cost | increase | short | invisible | A | OC-3 | none |
| C-24 | consumers, dairy sellers | quantity_traded (regional market) | decrease | short–medium | invisible | B | PC-9, OC-4 | A-1, A-3 |
| — | farmers.velmora (owners) | earnings | increase | short–medium | invisible | B | C-1, C-3 | A-1 |
| — | farmers.velmora (tenants) | earnings | ambiguous | medium | invisible | B | C-1, C-3 vs C-18 | A-1, A-2, A-8 |
| — | consumers | price_paid (dairy products) | ambiguous | long | invisible | C | C-14 vs C-16, C-20, C-21 | A-1, A-3, A-5, A-9 |

## Gaps found

- **GAP-008-1. Activity moving into a jurisdiction that a policy favors.** Needed for C-12 (Tier C). RS-4 covers only movement out of a boundary to escape a burden. A floor, subsidy or exemption that applies inside a boundary gives activity near it a reason to move in. Proposed fix: generalize RS-4 to "activity and purchases move to whichever side of a boundary the policy favors", with `entry_rate` increase on the favored side and `quantity_supplied` decrease on the other, under the same `mobility` assumption.
- **GAP-008-2. Public stocks and their disposal.** Needed for C-20 and C-21 (Tier C) and for the long-run entry in section 7. When the state buys a surplus, it holds a stock that grows while the floor binds and must later be sold, given away or destroyed; disposal displaces private sales. Proposed fix: the variable `inventory_held` (as proposed in GAP-006-1), and a new SB rule. *If* the state buys a surplus at a support price, *then* `inventory_held` by the agency increases while the floor binds; when the stock is released, `quantity_traded` decreases for the private sellers it displaces (donation) or `price_paid` decreases in the market it is sold into (resale). *Assumes* the product's shelf life and the disposal routes allowed (`durability`, `other`). Tier B.
- **GAP-008-3. Spillover to the uncontrolled segment under a floor.** Needed for C-15 and C-16 (Tier C). PC-8 covers buyers moving from a capped segment to an uncontrolled one. Under a floor that covers only part of a market, buyers move from the controlled segment to the uncontrolled one because it is cheaper, raising its price. Proposed fix: extend PC-8 to any binding control on part of a market: *if* a binding `price_ceiling` or `price_floor` covers one segment and an uncontrolled segment exists, *then* demand moves to the uncontrolled segment (ceiling: from outsiders; floor: from buyers avoiding the higher price), and `price_substitute` increases there. *Assumes* `substitutability`. Tier B.
