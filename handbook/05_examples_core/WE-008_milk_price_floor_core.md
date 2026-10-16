# WE-008 / Analysis: Price floor for raw milk, with state purchase of the surplus (core-only re-run)

Analyst: core-only re-run (Handbook 0.4)  |  Rules: core rules CR-1 to CR-12 only  |  Status: awaiting comparison

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


Horizons used below: short = Year 1 (herds and plants fixed); medium = Years 2 to 4 (to the first review); long = beyond.

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | Core rules applied |
|---|---|---|---|
| K1 Minimum milk price | triangular (forbids purchases of Velmora milk by Velmora plants below $21) | Yes: regional price expected below $21 (A-1, p 0.8) | CR-1, CR-4, CR-5a, CR-6, CR-7, CR-9, CR-10, CR-11a |
| K2 State purchase | binary (the Board buys with general-fund money); makes K1 hold for Velmora milk that goes into cheddar and powder | Yes while market product prices are below the support prices (A-1) | CR-1 (op 2, op 4), CR-4, CR-8 |
| K3 Disposal of stocks | binary (sales and donations by the Board) | Resale only above 110% of purchase price; donation and export otherwise (A-12) | CR-1, CR-8d, CR-9 |
| K4 Certification and enforcement | attaches paperwork and penalties to the Board route | Some false certification undetected (A-6, p 0.55) | CR-1 (op 3), CR-4, CR-8c |

**CR-1: what each component does to each actor class.** Operations: 1 remove an option, 2 add an option, 3 change what an option brings, 4 transfer means. A dash means no direct effect; indirect effects are traced with CR-9.

| Actor class | K1 Floor | K2 State purchase | K3 Disposal | K4 Certification |
|---|---|---|---|---|
| sellers.current (Velmora dairy farmers) | 1: selling to Velmora plants below $21 removed | — (indirectly 2: a buyer at $21 exists through plants that sell to the Board) | — | — |
| buyers.current (Velmora plants) | 1: buying Velmora milk below $21 removed (out-of-state milk still open) | 2: selling cheddar and powder to the Board at the support price | — | 3: segregation, documents, audits, fines attached to the Board route |
| buyers.current (specialty plants needing Velmora origin) | 1 (as above; they cannot switch origin without losing the label) | 2 only for cheddar and powder, which they do not make | — | 3 |
| sellers.prospective (farmers who move or register in Velmora) | 2 after three months' registration (as the record assumes) | — | — | — |
| neighboring_jurisdictions (Ostrand and Quillon farmers and plants) | — (exempt) | — | — | — |
| buyers.downstream (buyers of dairy products in the region) | — | — | 2: Board resale when prices exceed 110% of purchase price | — |
| food programs (Velmora school meals and food banks) | — | — | 4: donated cheese and powder | — |
| buyers.export | — | — | 2: Board export sales | — |
| officials.enforcement (Velmora Dairy Board) | — | 2 and 4: buying, storing; means from the general fund | 2: disposal routes | 2: audit duties |
| taxpayers | — | 4: open-ended appropriation | — | 4 |

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| sellers.current (Velmora dairy farmers) | About 3,000 farms | Receive $21 where they sell to Velmora plants; can still sell to out-of-state plants at market |
| buyers.current (Velmora plants making products for the market) | Fluid, butter and other plants | Must pay $21 for Velmora milk; can buy out-of-state milk at market plus transport (A-5) |
| buyers.current (Velmora plants on the Board route) | Plants making cheddar and powder for the Board | Break even at $21 milk by selling to the Board |
| buyers.current (specialty plants) | Origin-labeled cheesemakers | Must pay $21 to keep the label (A-4); compete with cheesemakers paying market prices |
| sellers.prospective | Farmers near the border who could move or register (A-7) | A $21 outlet after registration |
| neighboring_jurisdictions | Ostrand and Quillon farmers | The regional market loses product withdrawn into Board stocks (CR-9, same market) |
| factor_owners.specific | Owners of Velmora dairy land and barns | Fixed in the medium run (A-8): the floor raises their expected yield |
| sellers.substitutes (crop and beef farmers) | Compete with dairy for land and labor | Land and labor drawn to dairy (A-10) |
| workers (dairy farm labor) | Employed on Velmora dairy farms | More demand for their work (LW-10) |
| buyers.downstream | Buyers of cheese, butter, powder and fluid milk in the region | Regional supply reduced in the short run |
| food programs and their suppliers | School meals and food banks; those who sold dairy to them | Donated stocks replace purchases (A-9) |
| buyers.export | Buyers outside the region | Board export sales |
| officials.enforcement (Dairy Board) | Buys, stores, disposes, audits | New duties and stocks |
| taxpayers | General fund | Fund purchases, storage and audits |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | sellers.current (Velmora dairy farmers) | net_price_received (raw milk) | increase | short | CR-1 (K1 op 1; K2 op 2) → CR-6 | A-1 |
| C-2 | buyers.current (Velmora plants buying Velmora milk) | price_paid (Velmora raw milk) | increase | short | CR-1 (K1 op 1) | A-1 |

The visible effect is what supporters expect: Velmora farmers are paid $21 per cwt instead of the regional $17 to $19 expected in the forward market. K2 is what makes this hold for the bulk of Velmora milk: without a buyer of last resort, Velmora plants would buy out-of-state milk instead (C-3), and the floor alone would leave Velmora farmers selling out of state at the market price.

## 5. Responses

**CR-2 to CR-5 by actor class.**

| Actor class | CR-2/CR-3: which chosen option is removed or burdened | CR-4 pairs (x made worse relative to y) | CR-5 |
|---|---|---|---|
| Velmora farmers | None removed; selling at $21 is added through the Board route | Mirror: x: produce more milk (made better); x: invest in herds and barns; x: lobby to keep the program | 5a: sales to Velmora plants below $21 prevented |
| Velmora plants (market products) | Buying Velmora milk at the market price removed (CR-3a for those who preferred it) | x: Velmora milk at $21, y: out-of-state milk | 5a |
| Velmora plants (Board route) | — | x: sell cheddar and powder on the market below the support price, y: sell to the Board; x: comply, y: certify out-of-state milk as Velmora milk | 5c: the Board's terms set the range |
| specialty plants | Buying origin milk at market price removed (CR-3a) | x: origin-labeled cheese, y: unlabeled cheese or another use of the plant | — |
| farmers near the border | — | Mirror: x: farm in Velmora (made better), y: farm across the line | — |
| neighboring farmers | — | Mirror: x: produce more (regional price higher) | — |
| crop and beef farmers | Land and labor bid away (CR-9) | x: land in crops or beef, y: land in dairy | — |
| buyers.downstream | Paying a higher regional price (CR-3a) | x: dairy products, y: other foods (CR-4c) | — |

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-3 | buyers.current (Velmora plants making products for the market) | cross_border_purchases (raw milk from Ostrand and Quillon) | increase | short | CR-4b (x: Velmora milk at $21, y: out-of-state milk) | A-1, A-5 |
| C-4 | sellers.current (Velmora dairy farmers) | excess_supply (Velmora raw milk at the floor, private market) | increase | short | CR-6 (price held above clearing) with C-3 | A-1, A-5 |
| C-5 | officials.enforcement (Dairy Board) | inventory_held (cheddar and powder) | increase | short | C-4 → CR-1 (K2 op 2) → CR-4b (x: sell on market below support price, y: sell to the Board) | A-1 |
| C-6 | sellers.current (Velmora dairy farmers) | side_payments, allocation_by_non_price_criteria | at_least_one_increase | short | C-4 → CR-6 (pressure from sellers displaced to unregulated terms and to the criteria plants use to choose suppliers) | A-1, A-N3 |
| C-7 | sellers.current (Velmora dairy farmers) | quantity_supplied (Velmora raw milk) | increase | medium | C-1 → CR-4c (mirror: last units now worth producing) → CR-10b | A-1, A-2 |
| C-8 | sellers.current (Velmora dairy farmers) | investment_target (herds, barns, equipment) | increase | medium | CR-10a (program expected to last) → CR-4b (mirror: x: invest) | A-1, A-2 |
| C-9 | sellers.current (Velmora dairy farmers) | capital_stock_target (Velmora dairy capacity) | increase | long | C-8 → CR-10b | A-1, A-2 |
| C-10 | sellers.prospective (farmers near the border) | entry_rate (farms registering in Velmora) | increase | medium | CR-4b (mirror: x: farm in Velmora) → CR-7a | A-1, A-2, A-7 |
| C-14 | buyers.current (specialty plants) | return_on_capital | decrease | short | CR-1 (K1 op 1) → CR-3a → CR-7b (rivals buy at market; burden settles on means that cannot move: label and plant) | A-1, A-4 |
| C-15 | buyers.current (specialty plants) | quantity_supplied (origin-labeled cheese) | decrease | medium | C-14 → CR-4b (x: origin-labeled cheese, y: unlabeled cheese or other use) | A-1, A-4 |
| C-21 | intermediaries (plants certifying falsely) | informal_activity (out-of-state milk certified as Velmora milk) | increase | short | CR-4b (x: comply, y: certify falsely; gain is $21 minus market milk cost) | A-1, A-6 |
| C-22 | buyers.current (Velmora plants on the Board route) | compliance_cost (segregation and origin documents) | increase | short | CR-1 (K4 op 3) → CR-8c | none |
| C-28 | sellers.current (Velmora dairy farmers) | lobbying_effort (to keep the program at the four-year review) | increase | medium | CR-10a → CR-4 (mirror: x: lobby, made better by the stake) | A-2, A-N4 |

Notes on the responses.
- C-3 to C-5: the floor binds only on plants located in Velmora buying Velmora milk. Plants selling on the market switch to out-of-state milk (A-5), so the Velmora milk that goes to Velmora plants is the milk made into cheddar and powder for the Board, and specialty milk. The rest of the floor's "surplus" appears as Board stocks.
- C-6: plants on the Board route only break even at $21 (K2's prices are set for that), so they gain nothing from taking more Velmora milk. If their capacity is short in Year 1 (A-N3), farmers compete for access by accepting hauling charges or quality deductions, or plants favor some suppliers. Which margin is used is empirical, so this is a group.
- C-14: specialty plants cannot switch origin without losing the label, and their rivals buy at market (A-4), so the higher cost of milk cannot be passed on fully; under CR-7b it settles on what cannot move: the label's value and the specialty plant.

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-11 | factor_owners.specific (owners of Velmora dairy land and barns) | asset_value | increase | short | CR-7b (gain settles on fixed means) → CR-7c → CR-10a (value moves when the program becomes expected, Year 0) | land and barns `input_to` Velmora milk | A-1, A-2, A-8 |
| C-12 | sellers.substitutes (Velmora crop and beef farmers) | quantity_supplied (Velmora crops and beef) | decrease | medium | C-7 → CR-9 (compete for the same land and labor) → CR-7a | land `input_to` milk and to crops and beef | A-1, A-2, A-10 |
| C-13 | workers (Velmora dairy farm labor) | employment (Velmora dairy farms) | increase | medium | C-7 → CR-9 → LW-10 | labor `input_to` milk | A-1, A-2, A-10 |
| C-16 | buyers.downstream (buyers of origin-labeled cheese) | price_paid (origin-labeled cheese) | increase | medium | C-15 → CR-9 → CR-5c | Velmora milk `input_to` origin-labeled cheese | A-1, A-4 |
| C-17 | neighboring_jurisdictions (Ostrand and Quillon farmers) | net_price_received (raw milk) | increase | short | C-3, C-5 → CR-9 (product withdrawn from the regional market into stocks) → CR-6 (regional price moves toward the new clearing level) | Velmora milk and neighbors' milk, `same_market_other_segment`, close | A-1, A-3, A-5, A-N1 |
| C-18 | buyers.downstream (regional buyers of dairy products) | price_paid (cheese, butter, powder and fluid milk in the region) | increase | short | C-17's chain → CR-9 (raw milk `input_to` products) | raw milk `input_to` dairy products | A-1, A-3, A-5, A-N1 |
| C-19 | buyers.downstream | quantity_demanded (dairy products in the region) | decrease | short | C-18 → CR-4c | — | A-1, A-3, A-5, A-N1 |
| C-20 | neighboring_jurisdictions (Ostrand and Quillon farmers) | quantity_supplied (raw milk) | increase | medium | C-17 → CR-4c (mirror) → CR-10b | same market | A-1, A-2, A-3, A-5, A-N1 |
| C-23 | officials.enforcement (Dairy Board) | enforcement_cost (purchases handling, warehouse leases, audits) | increase | short | C-5 → CR-1 (K2, K4) → CR-8c | — | A-1 |
| C-24 | taxpayers | resources_available_other_uses | decrease | short | C-5, C-21, C-23 → CR-8a, CR-8b (purchases at support price exceed disposal receipts while A-1 holds) → CR-12a | — | A-1 |
| C-25 | food programs (Velmora school meals and food banks) | resources_available_other_uses | increase | medium | C-5 → K3 donation → CR-8d (donated goods free their dairy budgets) | donated stocks `substitute` for purchased dairy | A-1, A-9, A-12 |
| C-26 | sellers.current (dairy suppliers to Velmora food programs) | quantity_traded (dairy sold to Velmora food programs) | decrease | medium | C-25 → CR-9 (substitute) | donated stocks `substitute` for purchased dairy | A-1, A-9, A-12 |
| C-27 | buyers.export | price_paid (cheese and powder in export markets) | decrease | medium | C-5 → K3 export → CR-9 → CR-6 | Velmora stocks to export markets, `across_border` | A-1, A-12, A-N2 |

Chains stopped: C-26 is at depth 4 (floor, stocks, donation, food programs' suppliers). Competing exporters' sales (after C-27) and the users of the land given up by crop and beef farming (after C-12) are diffuse bystanders past depth 3; pruned. Prices of feed and heifers rise with C-7 by the same imputation (LW-10), but the controlled list has no input-price variable for them, so they are noted, not recorded.

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| buyers.downstream, price_paid (regional dairy products), short | Velmora product withdrawn into Board stocks (C-5) and not fully replaced (A-3) | Donated stocks displace food programs' purchases (C-25) | Dominance premise: in Year 1 herds are fixed (CR-10b), so the Board's stocks come from milk that would otherwise have gone to the market; donations come out of those stocks, so they can return at most what was withdrawn (CR-8b, arithmetic), and A-N1 says they return less | increase (C-18) |
| neighboring farmers, net_price_received, short | same as above | same as above | same premise (A-N1) | increase (C-17) |
| taxpayers, resources_available_other_uses, short | none | purchases (C-5), false certification (C-21), storage and audits (C-23) | none needed (CR-12a) | decrease (C-24) |
| Velmora farmers, net_price_received vs side_payments | — | — | different variables, not netted (CR-12c) | C-1 increase; C-6 group increase |

The one dominance claim (C-17, C-18) rests on CR-10b and CR-8b plus A-N1. In the medium run it weakens: Velmora output grows (C-7) and goes to the Board, but neighbors expand too (C-20), and CR-7a brings their returns back in line, so the regional price effect fades; no sign is reported for the medium run.

## 8. Time structure

- Year 0 (proposal in February, enactment in June): the value of Velmora dairy land and barns rises when the program becomes expected, and is captured by those who own them then (C-11, CR-7c). Later buyers of land pay the higher price and gain nothing lasting.
- Year 1: herds are fixed (CR-10b), so Velmora output changes little; the main effects are the switch of Velmora plants to out-of-state milk (C-3), Board stocks (C-5), a higher regional price (C-17, C-18) and, if plant capacity is short, non-price competition among farmers (C-6).
- Years 2 to 4: Velmora herds grow (C-7 to C-9), farmers near the border register (C-10), and land and labor move from crops and beef (C-12, C-13). Board stocks and spending grow with output. Stocks age: cheddar keeps one to two years and powder two to three (A-12), so disposal by donation and export must keep pace.
- K3 resale: if regional prices ever exceed 110% of the Board's purchase price, the Board sells into the market, which caps price rises (a Tier C note, not a consequence: whether prices reach that level is not established).
- Review every four years: farmers' stake in renewal grows with their investment (C-28). If repealed, herds, barns and registered farms persist for a time (CR-10b); A-11 (repeal within two years) is below the cut-off.

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-24 | taxpayers | resources_available_other_uses | decrease | Whatever the general fund would otherwise have paid for | CR-8a, CR-8b |
| C-22 | buyers.current (Velmora plants on the Board route) | compliance_cost | increase | Plant time and tank space for segregation and documents | CR-8c |
| C-23 | officials.enforcement | enforcement_cost | increase | Warehouses, staff and audits | CR-8c |
| C-12 | sellers.substitutes (crop and beef farmers) | quantity_supplied (crops and beef) | decrease | Crops and beef the land and labor would otherwise have produced | CR-8a, CR-7a |
| C-19 | buyers.downstream | quantity_demanded | decrease | Dairy purchases forgone at the higher regional price | CR-3a, CR-4c |
| C-6 | sellers.current | side_payments, allocation_by_non_price_criteria | at_least_one_increase | Resources spent competing for access to Board-route plants | CR-6, CR-8c |

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | The regional raw milk price stays below $21 for most of the next three years. | binding | 0.8 | Forward prices of $17 to $19; five-year price history. | The floor does not bind; nearly every consequence vanishes. |
| A-2 | Farmers and plants expect the program to last several years. | expectations | 0.65 | Open-ended appropriation; political support in the legislature; the four-year review. | Investment and entry (C-7 to C-11) shrink; C-28 weakens. |
| A-3 | Out-of-state supply does not replace all of the withdrawn product at the old price in the short run. | substitutability | 0.75 | Velmora's 15% share; neighbors' capacity to expand; time to raise heifers. | C-17 to C-20 fail. |
| A-4 | Specialty plants need Velmora-origin milk to keep their label and price premium, and compete with cheesemakers who buy milk at market prices. | other | 0.7 | Label rules; price premium of origin-labeled cheese; market shares in specialty cheese. | C-14 to C-16 fail. |
| A-5 | Out-of-state raw milk reaches Velmora plants at little more than transport cost. | mobility | 0.85 | Tanker routes and costs of 30 to 90 miles. | Velmora plants keep buying Velmora milk at $21; C-3, C-4 fail and the burden falls on Velmora plants and their buyers. |
| A-6 | Some false certification of origin goes undetected. | enforcement | 0.55 | Audit frequency; ease of tracing tanker loads. | C-21 fails. |
| A-7 | Moving a dairy operation, or registering one, into Velmora is feasible for some farmers near the border. | mobility | 0.6 | Land for lease near the border; cost of moving herds. | C-10 fails. |
| A-8 | Dairy land and barns are in fixed supply in the medium run. | durability | 0.85 | Land use rules; time to build barns. | The gain is competed away by new land and barns; C-11 weakens. |
| A-9 | Donated stocks replace dairy that food programs would otherwise have bought. | other | 0.7 | Food program budgets and purchase records. | C-25, C-26 fail; the regional price dominance needs no A-N1. |
| A-10 | Velmora farmland and farm labor have other farm uses (crops, beef). | alternative_uses | 0.8 | Land quality; crop rotations in the state. | C-12, C-13 fail. |
| A-11 | The program is expected to be repealed within two years. | expectations | 0.3 | Budget debates; opposition statements. | (Below cut-off; used by no reported consequence.) |
| A-12 | Cheddar keeps one to two years and powder two to three, and the Board disposes of stocks through K3's routes (donation, export, resale when allowed) rather than destroying them. | durability | 0.8 | Shelf lives; K3 text; disposal practice of comparable agencies. | C-25 to C-27 fail. |
| A-N1 | In the short run, donations displace a smaller quantity of food programs' dairy purchases than the Board withdraws from the market. | other | 0.85 | Velmora food programs' dairy purchases are small next to 15% of a regional market's milk; donations draw on the same stocks. | The regional price chains (C-17 to C-20) become ambiguous. |
| A-N2 | The Board exports part of its stocks. | other | 0.65 | Resale is barred while prices stay low (A-1); Velmora food programs cannot absorb the stocks; comparable agencies export. | C-27 fails. |
| A-N3 | In Year 1, Velmora plants' capacity to make cheddar and powder for the Board is smaller than the Velmora milk offered at $21. | durability | 0.6 | Plants break even only at the support prices, so they gain nothing by expanding; converting plant capacity takes time. | C-6 fails; Board-route plants absorb all Velmora milk. |
| A-N4 | Velmora dairy farmers' organizations act on the four-year review. | other | 0.7 | The program was proposed with political support in the legislature; farm organizations exist in a 3,000-farm dairy state. | C-28 fails. |

**Not reported (an assumption below 0.5).**
- Farmers hold back long-lived investment because they expect repeal within two years (CR-10a): needs A-11 (p 0.3). The reported investment chain (C-8) uses A-2 instead.

## 11. Report

**The policy:** Velmora plants must pay at least $21 per cwt for milk from Velmora farms. A state Board buys any quantity of cheddar and powder made from such milk at prices set so that a plant paying $21 breaks even, stores it, and may donate, export or (when market prices are high) resell it. Out-of-state milk is exempt. The program is paid for from the general fund without limit.

**Visible consequences:** Velmora dairy farmers receive more for their milk (C-1); Velmora plants that buy Velmora milk pay more (C-2). The Board accumulates stocks of cheddar and powder (C-5) and spends more on handling and audits (C-23).

**Invisible consequences:**
- Velmora plants making products for the market switch to out-of-state milk (C-3), so Velmora milk at $21 finds private buyers only on the Board route and among specialty plants (C-4). If Board-route capacity is short in Year 1, farmers compete for access through hauling charges or quality deductions, or plants favor some suppliers (at least one, C-6).
- Over Years 2 to 4, Velmora farmers produce more, invest more and build up dairy capacity (C-7 to C-9); farmers near the border register in Velmora (C-10). Dairy farm employment rises (C-13), and crop and beef output in Velmora falls as land and labor move to dairy (C-12).
- Owners of Velmora dairy land and barns gain in asset value when the program becomes expected (C-11); later buyers do not.
- Specialty cheesemakers who need Velmora-origin milk earn less on their capital (C-14) and make less origin-labeled cheese (C-15); its price rises (C-16).
- Across the region in Year 1, product withdrawn into stocks raises prices: neighboring farmers receive more (C-17), buyers of dairy products pay more (C-18) and buy less (C-19); neighbors then expand (C-20).
- Some plants certify out-of-state milk as Velmora milk (C-21); plants spend more on segregation and records (C-22).
- Taxpayers give up other uses of the money spent on purchases, storage and audits (C-24). Food programs that receive donations have more of their budgets for other uses (C-25), and their usual dairy suppliers sell less to them (C-26). Buyers in export markets pay less (C-27).
- Farmers spend more effort on keeping the program at the four-year review (C-28).

**Ambiguous effects:** None reported as ambiguous. The regional price increase in Year 1 rests on a stated dominance premise (A-N1): donations cannot return more to the market than the Board took out. For later years the regional price effect is not signed: Velmora output grows into stocks while neighbors expand.

**Key conditions:** That the floor binds (A-1, p 0.8) and out-of-state milk is cheap to bring in (A-5, p 0.85). The regional chains need A-3 (p 0.75) and A-N1 (p 0.85). Expansion needs farmers to expect the program to last (A-2, p 0.65). The weakest reported premises are false certification (A-6, p 0.55) and Year-1 capacity (A-N3, p 0.6).

**What this analysis cannot say:** How large the stocks or the budget cost will become, how much regional prices rise, whether farmers' gains outweigh taxpayers' and consumers' losses, or whether the program is good policy. Nutrition effects of donated dairy on school meals and food bank users, and environmental effects of a larger dairy herd, are out of scope for version 1 and are not analyzed. The method cannot say when, if ever, regional prices reach the Board's resale threshold.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | sellers.current (Velmora dairy farmers) | net_price_received (raw milk) | increase | short | visible | B | CR-1 (K1 op 1; K2 op 2: a buyer at $21 through the Board route) → CR-6 (price held above clearing) | A-1 |
| C-2 | buyers.current (Velmora plants buying Velmora milk) | price_paid (Velmora raw milk) | increase | short | visible | B | CR-1 (K1 op 1) | A-1 |
| C-3 | buyers.current (Velmora plants making products for the market) | cross_border_purchases (raw milk from Ostrand and Quillon) | increase | short | invisible | B | CR-4b (x: Velmora milk at $21, y: out-of-state milk) | A-1, A-5 |
| C-4 | sellers.current (Velmora dairy farmers) | excess_supply (Velmora raw milk at the floor, private market) | increase | short | invisible | B | CR-6 (price held above clearing) with C-3 → CR-12a | A-1, A-5 |
| C-5 | officials.enforcement (Dairy Board) | inventory_held (cheddar and powder) | increase | short | visible | B | C-4 → CR-1 (K2 op 2) → CR-4b (x: sell on market below support price, y: sell to the Board) | A-1 |
| C-6 | sellers.current (Velmora dairy farmers) | side_payments, allocation_by_non_price_criteria | at_least_one_increase | short | invisible | B | C-4 → CR-6 (pressure from sellers displaced to unregulated terms and to plants' choice of suppliers) | A-1, A-N3 |
| C-7 | sellers.current (Velmora dairy farmers) | quantity_supplied (Velmora raw milk) | increase | medium | invisible | B | C-1 → CR-4c (mirror) → CR-10b (herds grow through flows) | A-1, A-2 |
| C-8 | sellers.current (Velmora dairy farmers) | investment_target (herds, barns, equipment) | increase | medium | invisible | B | CR-10a (program expected to last) → CR-4b (mirror: x: invest) | A-1, A-2 |
| C-9 | sellers.current (Velmora dairy farmers) | capital_stock_target (Velmora dairy capacity) | increase | long | invisible | B | C-8 → CR-10b | A-1, A-2 |
| C-10 | sellers.prospective (farmers near the border) | entry_rate (farms registering in Velmora) | increase | medium | invisible | B | CR-4b (mirror: x: farm in Velmora, y: across the line) → CR-7a | A-1, A-2, A-7 |
| C-11 | factor_owners.specific (owners of Velmora dairy land and barns) | asset_value | increase | short | invisible | B | CR-7b (gain settles on fixed means) → CR-7c → CR-10a (moves when expected, Year 0) | A-1, A-2, A-8 |
| C-12 | sellers.substitutes (Velmora crop and beef farmers) | quantity_supplied (Velmora crops and beef) | decrease | medium | invisible | B | C-7 → CR-9 (compete for land and labor) → CR-7a | A-1, A-2, A-10 |
| C-13 | workers (Velmora dairy farm labor) | employment (Velmora dairy farms) | increase | medium | invisible | B | C-7 → CR-9 (labor input_to milk) → LW-10 | A-1, A-2, A-10 |
| C-14 | buyers.current (specialty plants) | return_on_capital | decrease | short | invisible | B | CR-1 (K1 op 1) → CR-3a → CR-7b (rivals buy at market; burden on label and plant) | A-1, A-4 |
| C-15 | buyers.current (specialty plants) | quantity_supplied (origin-labeled cheese) | decrease | medium | invisible | B | C-14 → CR-4b (x: origin-labeled cheese, y: unlabeled cheese or other use) | A-1, A-4 |
| C-16 | buyers.downstream (buyers of origin-labeled cheese) | price_paid (origin-labeled cheese) | increase | medium | invisible | B | C-15 → CR-9 (input_to) → CR-5c | A-1, A-4 |
| C-17 | neighboring_jurisdictions (Ostrand and Quillon farmers) | net_price_received (raw milk) | increase | short | invisible | B | C-3, C-5 → CR-9 (same market: product withdrawn into stocks) → CR-6 → CR-12b with dominance (CR-10b, CR-8b, A-N1) | A-1, A-3, A-5, A-N1 |
| C-18 | buyers.downstream (regional buyers of dairy products) | price_paid (cheese, butter, powder and fluid milk in the region) | increase | short | invisible | B | as C-17 → CR-9 (raw milk input_to products) | A-1, A-3, A-5, A-N1 |
| C-19 | buyers.downstream | quantity_demanded (dairy products in the region) | decrease | short | invisible | B | C-18 → CR-4c | A-1, A-3, A-5, A-N1 |
| C-20 | neighboring_jurisdictions (Ostrand and Quillon farmers) | quantity_supplied (raw milk) | increase | medium | invisible | B | C-17 → CR-4c (mirror) → CR-10b | A-1, A-2, A-3, A-5, A-N1 |
| C-21 | intermediaries (plants certifying falsely) | informal_activity (out-of-state milk certified as Velmora milk) | increase | short | invisible | B | CR-4b (x: comply, y: certify falsely) | A-1, A-6 |
| C-22 | buyers.current (Velmora plants on the Board route) | compliance_cost (segregation and origin documents) | increase | short | invisible | A | CR-1 (K4 op 3) → CR-8c | none |
| C-23 | officials.enforcement (Dairy Board) | enforcement_cost (purchase handling, warehouse leases, audits) | increase | short | visible | B | C-5 → CR-1 (K2, K4) → CR-8c | A-1 |
| C-24 | taxpayers | resources_available_other_uses | decrease | short | invisible | B | C-5, C-21, C-23 → CR-8a, CR-8b → CR-12a | A-1 |
| C-25 | food programs (Velmora school meals and food banks) | resources_available_other_uses | increase | medium | invisible | B | C-5 → K3 donation → CR-8d (donated goods free dairy budgets) | A-1, A-9, A-12 |
| C-26 | sellers.current (dairy suppliers to Velmora food programs) | quantity_traded (dairy sold to Velmora food programs) | decrease | medium | invisible | B | C-25 → CR-9 (substitute) | A-1, A-9, A-12 |
| C-27 | buyers.export | price_paid (cheese and powder in export markets) | decrease | medium | invisible | B | C-5 → K3 export → CR-9 (across_border) → CR-6 | A-1, A-12, A-N2 |
| C-28 | sellers.current (Velmora dairy farmers) | lobbying_effort (to keep the program at the four-year review) | increase | medium | invisible | B | CR-10a → CR-4 (mirror: x: lobby) | A-2, A-N4 |

## Gaps found

**(a) Calculus gaps.** None for the derivations. One recording gap: CR-9 with LW-10 licenses "demand for the inputs of Velmora milk (feed, heifers) rises", but no variable in the controlled list records an input's price or quantity for an input that is not itself the target, a complement or a substitute; those links were noted in section 6 and not recorded. This is a vocabulary gap, not a missing rule.

**(b) New premises.**
- A-N1 (p 0.85, other): the Year-1 regional price chain has opposing pulls (withdrawal into stocks against donations that displace purchases). CR-12b makes it ambiguous unless a premise establishes dominance; CR-10b and CR-8b give the arithmetic bound (donations come out of withdrawn stocks), and A-N1 supplies the strict inequality.
- A-N2 (p 0.65, other): A-12 says stocks are disposed of through K3's routes but not which; the export chain needs a premise that some go to export.
- A-N3 (p 0.6, durability): CR-6 non-price competition among farmers needs a premise that Board-route plants cannot absorb all Velmora milk offered; with break-even support prices nothing in the case says they will.
- A-N4 (p 0.7, other): CR-4 (x: lobby) needs some farmers at that margin.

**(c) Unclear core rules.**
- CR-12b dominance: the core rule says a dominance claim needs a premise, and the task guidance points to CR-7b as the usual source. Here the premise came instead from CR-10b (fixed herds in Year 1) and CR-8b (arithmetic of stocks), plus an empirical inequality. CR-12b does not say which core rules may ground a dominance premise.
- CR-6 for a floor supported by a buyer of last resort: CR-6 describes displaced pressure when "a rule prevents the price from moving". K2 does not prevent the price from moving; it adds a buyer. Whether the excess supply (C-4) is CR-6 (the floor) or CR-1 op 2 plus CR-4 (the Board route) depends on which component one starts from; both are cited.
- CR-7b and specialty plants (C-14): CR-7b says the lasting loss settles on means that cannot move. A label tied to origin is a legal attribute rather than a physical means; reading it as an immobile means was needed to apply the rule.
