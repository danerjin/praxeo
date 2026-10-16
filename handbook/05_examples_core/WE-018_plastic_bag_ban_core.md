# WE-018 / Core-only re-run: Ban on single-use plastic shopping bags, with a fee for paper bags

Analyst: core-only re-run (Handbook 0.4)  |  Rules: core rules CR-1 to CR-12 only  |  Status: awaiting comparison

## 1. Policy record

**Brennick Carryout Bag Ordinance.** Brennick is a city of about 400,000 people. Retailers there have given away thin plastic carryout bags at the checkout, at a cost to them of about 2 cents a bag, built into their prices. About 120 million such bags are handed out a year. Surveys suggest that about 60% of households reuse some of them as bin liners or for pet waste. The neighboring town of Fallow Creek has no bag rules; two large supermarkets there are within 1 km of the city line on Route 9, close to several Brennick neighborhoods. Brennick's other edges are mostly residential or rural. The ordinance was passed nine months before it took effect.

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Bag ban | `prohibition` | Single-use plastic carryout bags (plastic bags with handles, thinner than 4 mil (0.1 mm)) provided at the point of sale | All retailers in Brennick | From the effective date. | Bags without handles for produce, meat and bulk goods inside the store; pharmacy prescription bags; restaurant takeout bags |
| K2 Paper bag charge | `price_floor` | Recycled-paper carryout bags | All retailers | May be provided only for a charge of at least 10 cents a bag, kept by the retailer and shown on the receipt. Reusable bags (designed for at least 125 uses; at least 4 mil if plastic) may be sold at any price. | Customers paying with food-assistance benefits receive paper bags free |
| K3 Enforcement | Enforcement | K1, K2 | City Office of Sustainability | Complaint-driven. Written warning, then fines of $100, $250 and $500 per day of violation. Funded from the general budget. | None |

Unclear provisions: how a bag's design for 125 uses is verified. The ordinance sets no test, so a maker's claim is assumed to be accepted. Where a sign depends on it: **U1-a** a maker's claim is accepted; **U1-b** a test is applied.

## 2. Classification

CR-1 operations: 1 remove an option, 2 add an option, 3 change what an option brings, 4 transfer means.

| Component | Rothbard type | Binding? (assumption ID) | Core rules | CR-1 operations, by actor class |
|---|---|---|---|---|
| K1 | triangular (prohibits a term of exchange between retailers and shoppers) | Yes: retailers gave thin bags away and most comply (A-1) | CR-1, CR-3a, CR-4, CR-9, CR-10a | Retailers: 1 (handing out thin bags). Shoppers: 1 (receiving them). Thin bag makers: none directly; their buyers stop (CR-9). Exempt bags (produce, pharmacy, takeout): none. |
| K2 | triangular (a minimum price on a term of exchange) | Yes where retailers would otherwise give paper bags free or charge less (A-N2) | CR-1, CR-4, CR-6, CR-8b | Retailers: 1 (giving paper bags below 10 cents). Shoppers: 3 (a charge attached to the paper bag). Food-assistance shoppers: none (free paper). Reusable bags: none (any price). |
| K3 | binary (budget) plus enforcement | Complaint-driven; small stores may evade (A-5) | CR-1, CR-8 | Retailers: 3 (warnings, then fines). Taxpayers: 4. |

## 3. Actor classes

| Actor class | Role | How its options change (CR-1) |
|---|---|---|
| shoppers (buyers.current) | Brennick households | Free thin bag removed (1); paper bag carries a charge (3). |
| shoppers.food_assistance | Shoppers paying with food-assistance benefits | Thin bag removed (1); paper bag stays free. |
| shoppers.near_route_9 | Households close to the Fallow Creek supermarkets | As shoppers; free bags remain just across the line. |
| retailers, retailers.small | All Brennick retailers; small stores | Thin bags removed (1); paper only for 10 cents or more (1); fines (3). |
| retailers.near_route_9 (Brennick) | Stores competing with Fallow Creek | As retailers; customers can leave (CR-9). |
| neighboring_jurisdictions (Fallow Creek supermarkets) | Two supermarkets within 1 km of the line | No direct change; gain customers (CR-9). |
| staff at stores near the line, on both sides | Store labor | No direct change; hours follow sales (CR-9). |
| input_suppliers (thin bag makers, paper bag makers) | Sell bags to retailers | No direct change; their buyers change (CR-9). |
| sellers.substitutes (reusable bags, liners) | Sell substitutes | No direct change; demand rises (CR-9). |
| officials.enforcement, taxpayers | Office of Sustainability; general budget | New duties; transfer (4). |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | shoppers (buyers.current) | quantity_traded (thin plastic carryout bags, Brennick) | decrease | short | CR-1 op. 1 (retailers may no longer provide them; shoppers can no longer receive them) | A-1 |
| C-2 | shoppers (buyers.current) | price_paid (paper carryout bags) | increase | short | CR-1 op. 3 (a charge of at least 10 cents attached to each paper bag, K2); arithmetic against the free bag of the counterfactual | A-1, A-N2 |
| C-3 | retailers | net_price_received (paper carryout bags) | increase | short | CR-8b (the fee is kept by the retailer: the shoppers' outlay in C-2 is the retailers' receipt) | A-1, A-N2 |
| C-4 | retailers | compliance_cost | increase | short | CR-1 op. 3; CR-8c (new bag stock, receipt changes, signage, staff instruction, fee handling) | A-1 |
| C-5 | input_suppliers (thin bag makers) | quantity_traded (thin carryout bags sold to Brennick retailers, after the effective date) | decrease | short | CR-1 op. 1 for their buyers; CR-9 (input_to: their buyers stop buying) | A-1 |

## 5. Responses

CR-4 for each pair of options:

- **Shoppers.** (x: paper bag at 10 cents, y: reusable or own bag) (C-6, growing with habit, C-7); paper bags gain former plastic users and lose former free-paper users, so paper bag quantity is ambiguous (C-8); food-assistance shoppers move to free paper (C-9). (x: shop here, y: shop across the line) near Route 9 (C-12). (x: later, y: now) under CR-10a: extra free bags taken in the nine-month window (C-13).
- **Retailers.** K2 fixes a minimum price for paper bags. Under CR-6, the pressure from retailers who would charge less moves to open margins: cheap thick plastic bags sold as reusable, which may be sold at any price (C-10, by reading), and waiving the fee or handing out thin bags where enforcement is weak (C-11). Non-price competition for customers near the line is the third margin (see section 6).
- **Bag makers.** Thin bag sales rise in the window as retailers restock (C-14) and fall after (C-5).
- **Organized interests.** (x: accept, y: lobby) (C-15).

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-6 | shoppers (buyers.current) | quantity_substitute (reusable bags) | increase | short | CR-4b (x: paper bag at 10 cents or more, y: reusable or own bag); CR-4 (x: thin bag, now removed) | A-2 |
| C-7 | shoppers (buyers.current) | quantity_substitute (reusable bags) | increase | long | CR-10b (carrying bags is a habit built by repeated trips, so the shift grows); CR-4b | A-2, A-14 |
| C-8 | shoppers (buyers.current) | quantity_traded (paper carryout bags) | ambiguous | short | (+) CR-4b (x: thin plastic bag, removed; y: paper bag) for shoppers who rank paper above reusable even at the fee; (-) CR-4c (shoppers who would have taken free paper bags now pay 10 cents and take fewer); CR-12b | A-1, A-2, A-N2 |
| C-9 | shoppers.food_assistance | quantity_traded (paper carryout bags, free) | increase | short | CR-4b (x: thin plastic bag, removed; y: free paper bag, exempt from the fee) | A-1, A-N1 |
| C-10 | retailers | reclassification (thick plastic bags sold as reusable at the till) | U1-a: increase; U1-b: ambiguous | short | CR-6 (pressure from the fixed minimum on paper bags moves to the unregulated form, reusable bags at any price); CR-4b (x: the covered form, y: the uncovered form). U1-a: maker's claim accepted, so cheap thick bags qualify. U1-b: a test applied; which bags qualify is unknown | A-4, A-N2 |
| C-11 | retailers.small | informal_activity (thin bags handed out or paper fee waived) | increase | short | CR-4b (x: comply, y: violate), where waiving the fee or handing out thin bags keeps customers; CR-6 third margin | A-5, A-N2 |
| C-12 | shoppers.near_route_9 | cross_border_purchases | increase | short | CR-4b (x: shop in Brennick, y: shop at Fallow Creek supermarkets, where bags stay free) | A-6, A-9 |
| C-13 | shoppers (buyers.current) | inventory_held (thin plastic bags, at the effective date) | increase | short | CR-10a; CR-4c (x: take bags later, when they cannot be had; y: take extra bags now) | A-7 |
| C-14 | input_suppliers (thin bag makers) | quantity_traded (thin carryout bags sold to Brennick retailers, nine-month window) | increase | short | CR-10a; CR-9 (input_to: retailers restock as shoppers take extra bags) | A-7 |
| C-15 | bag makers and retailers | lobbying_effort | increase | medium | CR-4b (x: accept, y: lobby to amend, delay or widen exemptions); concentrated stakes | A-8 |

## 6. Second-order effects

Depth limit 4; prune diffuse bystander effects after depth 3. Relations used: thin carryout bags and bin liners or pet-waste bags: substitute, secondary_use (A-3); bags and groceries: complement, trip (A-9); Brennick and Fallow Creek grocery stores near Route 9: across_border, close for nearby households (A-6); bags to retailers and store labor to sales: input_to.

Chains:
1. K1 (1) shoppers lose bags they reused (2) buy liners instead (3) (C-16). The price of liners is not reported (A-10).
2. K1 and K2 (1) shoppers near Route 9 move to Fallow Creek (2) the whole basket moves (3): Brennick stores sell less, Fallow Creek stores more (C-17, C-18) (4) staff hours or hiring follow (C-19, C-20). Stopped at depth 4.
3. K1 and K2 (1) paper bag use changes (2) paper bag makers' sales (C-21).
4. K1 and K2 (1) stores' bag spending per transaction and compliance costs change (2) shelf prices over time (C-22).

Component interactions: K2 closes the obvious exit from K1 (free paper bags), which pushes the response toward reusable bags and toward the unregulated form K2 leaves open (reusable bags at any price); the food-assistance exemption in K2 reopens that exit for one group; K3's warning-first, complaint-driven design sets how much evasion pays.

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-16 | shoppers (buyers.current) | quantity_substitute (bin liners and pet-waste bags) | increase | medium | CR-9 (the thin bag was also used as a liner, so its removal raises demand for goods serving that end); CR-4b (x: reuse a carryout bag, removed; y: buy liners) | substitute, secondary_use (carryout bags reused as liners) | A-3 |
| C-17 | retailers.near_route_9 (Brennick) | quantity_traded (groceries) | decrease | short | CR-9 (the whole basket moves with the shopper, C-12) | complement, trip (bags and groceries bought on the same trip); across_border | A-6, A-9 |
| C-18 | neighboring_jurisdictions (Fallow Creek supermarkets) | quantity_traded (groceries) | increase | short | CR-9 (they gain the baskets that move, C-12) | complement, trip; across_border | A-6, A-9 |
| C-19 | staff at Brennick stores near Route 9 | employment, hours_worked | at_least_one_decrease | medium | CR-9, LW-10 (demand for store labor follows store sales, C-17); CR-4 for the stores (x: keep staffing, y: cut hours or hiring) | input_to (store labor to grocery sales) | A-6, A-9, A-15 |
| C-20 | staff at Fallow Creek stores near the line | employment, hours_worked | at_least_one_increase | medium | CR-9, LW-10 (mirror of C-19) | input_to (store labor to grocery sales) | A-6, A-9, A-15 |
| C-21 | input_suppliers (paper bag makers) | quantity_traded (paper bags sold to Brennick retailers) | ambiguous | short | CR-9, LW-10 (follows C-8, which is ambiguous); CR-12b | input_to | A-1, A-2, A-N2 |
| C-22 | shoppers (buyers.current) | price_paid (groceries, Brennick) | ambiguous | long | (-) CR-9 and CR-7a: stores' spending on bags per transaction falls and competition carries cost changes to shelf prices; (+) the same for compliance costs (C-4) and for fixed costs spread over fewer sales near the line; CR-12b | input_to (bags to retail service) | A-12, A-13 |

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance premise | Combined sign |
|---|---|---|---|---|
| shoppers, quantity_traded (paper bags), short | Former thin-bag users who take paper (CR-4b) | Former free-paper users who now pay and take fewer (CR-4c) | None | ambiguous (CR-12b) |
| input_suppliers (paper bag makers), quantity_traded, short | As above (CR-9) | As above (CR-9) | None | ambiguous (CR-12b) |
| shoppers, price_paid (groceries), long | Compliance and fixed costs passed on (CR-9, CR-7a) | Lower bag spending per transaction passed on (CR-9, CR-7a) | None; a one-time cost against a lasting saving cannot be netted | ambiguous (CR-12b) |
| shoppers, resources_available_other_uses, short | None | Fees, reusable bags, liners, time | Not needed | decrease (CR-12a) |

The shoppers' paper-bag fees and the retailers' receipts are kept as separate consequences (C-25, C-3), as CR-8's symmetry requires; they are not netted (CR-12c).

## 8. Time structure

- **Announcement window (CR-10a).** Nine months between passage and effect: shoppers take extra free bags (A-7), retailers restock, and thin bag makers sell more in the window and less after. Hoarded bags are used as liners for a time, so the rise in liner purchases is delayed; since the size of this delay against the counterfactual cannot be signed per window, it is a note here, not a consequence.
- **Habit (CR-10b).** Carrying bags is a habit built through frequent trips (A-14), so the shift to reusable bags grows over time (C-7), and paper bag use, if it rises at first, may fall later.
- **Cross-border shopping.** Store choice is also habitual; shoppers who move to Fallow Creek may stay there (CR-10b), so the loss of sales near the line persists into the medium run, as reflected in the staffing consequences.
- **Prices.** Any pass-through of bag and compliance costs to shelf prices runs through competition over time (A-13), hence a long horizon for C-22.

## 9. Opportunity costs

CR-3 and CR-8. Symmetry: the fees shoppers pay for paper bags are retailers' receipts (C-3); the liners and reusable bags shoppers buy are receipts of their sellers; the city's enforcement cost is a taxpayers' outlay.

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-23 | officials.enforcement (Office of Sustainability) | enforcement_cost | increase | Staff time and funds for other city uses | CR-8c; K3 |
| C-24 | taxpayers | resources_available_other_uses | decrease | Other city spending or lower taxes | CR-8a, CR-8b (K3 funded from the general budget) |
| C-25 | shoppers (buyers.current) | resources_available_other_uses | decrease | Money and time shoppers would have spent on other ends | CR-3a (chosen option, the free thin bag, removed); CR-8b (paper-bag fees, reusable bags and liners bought); CR-8c (time spent carrying, remembering and travelling to stores across the line) |

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | Most retailers comply, chains in particular. | enforcement | 0.85 | Store audits in the first months; complaint volumes; size of fines. | Direct effects shrink. |
| A-2 | Shoppers accept reusable and paper bags as substitutes. | substitutability | 0.95 | Experience of comparable towns; availability of bags. | Substitution shrinks; more cross-border shopping. |
| A-3 | Many households reused carryout bags as liners and will buy liners instead. | substitutability | 0.8 | Household surveys (about 60% reuse); liner sales in comparable towns after similar rules. | No liner chain. |
| A-4 | Thick plastic "reusable" bags can be sold cheaply at the till, and shoppers buy them. | other | 0.6 | Price of 4 mil bags; the 125-use claim is not tested. | No reclassification. |
| A-5 | Some small stores keep handing out thin bags, or waive the fee, without being caught. | enforcement | 0.6 | Complaint-driven enforcement; warnings before fines. | No evasion. |
| A-6 | Some shoppers near Route 9 are close to indifferent between stores on either side of the line. | mobility | 0.55 | Store locations; loyalty-card data; surveys of shopping trips. | No cross-border chain. |
| A-7 | Shoppers take extra free bags in the announcement window. | expectations | 0.7 | Bag orders by stores in the window in comparable towns. | No window effects. |
| A-8 | Bag makers and retailers can organize at a cost below their stake. | other | 0.7 | Existing industry and retail associations. | No lobbying. |
| A-9 | A shopper who changes store moves the whole basket, since the fee applies per trip. | other | 0.9 | Basket data; the fee's structure. | Only bag-related spending moves. |
| A-10 | Brennick's demand is large enough to move the price of liners or reusable bags. | other | 0.1 | City population against the regional market. | Below cut-off; not used. |
| A-11 | Checkout times rise meaningfully. | other | 0.45 | Till timing studies in comparable towns. | Below cut-off; not used. |
| A-12 | Stores' spending on bags per transaction falls, because many shoppers bring bags and the fee covers paper. | other | 0.7 | Store bag purchasing records; paper-bag cost against the 10-cent fee. | Grocery price chain is one-sided (+). |
| A-13 | Retail competition is strong enough that cost changes reach shelf prices over time. | other | 0.7 | Number of grocery chains; margins. | No grocery price consequence. |
| A-14 | Shopping trips are frequent and routine, so carrying bags can become a habit. | other | 0.9 | Trip frequency from household surveys (most households shop at least weekly). | No long-run growth in reuse. |
| A-15 | Stores near the line adjust staff hours and hiring to their sales. | alternative_uses | 0.8 | Share of part-time and hourly staff in grocery retail; scheduling practice. | No staffing chain. |
| A-N1 | Shoppers paying with food-assistance benefits take free paper bags where they formerly took thin plastic bags. | substitutability | 0.8 | The exemption's terms; experience of comparable towns with the same exemption. | C-9 vanishes. |
| A-N2 | Without K2, retailers that offer paper bags would give them free or charge less than 10 cents, so the floor binds. | binding | 0.8 | Pre-ordinance practice of free bags at the checkout; paper-bag cost to stores (A-12 evidence). | K2 changes nothing; C-2, C-3, C-10 and C-11 lose their K2 chain. |

**Not reported** (an assumption below 0.5):
- Shoppers' `wait_time` at the checkout increase (A-11, p 0.45).
- Liner and reusable bag sellers: `price_substitute` increase in Brennick (A-10, p 0.1).

## 11. Report

**The policy:** From a date nine months after passage, Brennick retailers may not provide thin plastic carryout bags with handles, and may provide recycled-paper bags only for at least 10 cents each, which they keep. Reusable bags may be sold at any price. Produce, pharmacy and takeout bags are exempt, and shoppers paying with food-assistance benefits get paper bags free. Enforcement is by complaint, with warnings and then daily fines.

**Visible consequences:** Thin bags disappear from Brennick checkouts (C-1, C-5); shoppers pay for paper bags (C-2) and buy reusable bags (C-6); retailers bear one-time compliance costs (C-4); the city spends on enforcement (C-23).

**Invisible consequences:**
- *Shoppers:* buy liners and pet-waste bags to replace reused carryout bags (C-16); took extra bags before the date (C-13); spend money and time on bags, liners and remembering bags (C-25); use of reusable bags grows with habit (C-7); food-assistance shoppers switch to free paper (C-9).
- *Shoppers and stores near Route 9:* some households shop in Fallow Creek, taking their whole basket (C-12); Brennick stores near the line sell less and cut hours or hiring, while Fallow Creek stores sell more and add them (C-17, C-18, C-19, C-20).
- *Retailers:* receive the paper-bag fees (C-3); some sell cheap thick plastic bags as reusable (C-10, by reading); some small stores evade (C-11).
- *Others:* thin bag makers sell more in the window and less after (C-14, C-5); bag makers and retailers lobby (C-15); taxpayers fund enforcement (C-24).

**Ambiguous effects:** How many paper bags are used, and so paper bag makers' sales (former plastic users take some; former free-paper users take fewer) (C-8, C-21); shelf prices over time (lower bag costs per transaction against compliance and fixed costs) (C-22).

**Key conditions:** Retailers comply (A-1, 0.85); shoppers accept substitutes (A-2, 0.95); households reused bags as liners (A-3, 0.8); some shoppers near Route 9 are close to indifferent between stores (A-6, 0.55, the weakest premise behind the cross-border and staffing chains). Two new premises: the 10-cent floor binds (A-N2, 0.8) and food-assistance shoppers take free paper (A-N1, 0.8).

**What this analysis cannot say:** how large any change is; whether the cost to shoppers and stores is worth any other result; whether the policy is good. Environmental effects (litter, plastic in waterways, the footprint of paper and thick plastic bags) are out of scope for version 1 and are not analyzed here.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | shoppers (buyers.current) | quantity_traded (thin plastic carryout bags, Brennick) | decrease | short | visible | B | CR-1 op. 1 (retailers may no longer provide them; shoppers can no longer receive them) | A-1 |
| C-2 | shoppers (buyers.current) | price_paid (paper carryout bags) | increase | short | visible | B | CR-1 op. 3 (a charge of at least 10 cents attached to each paper bag, K2); arithmetic against the free bag of the counterfactual | A-1, A-N2 |
| C-3 | retailers | net_price_received (paper carryout bags) | increase | short | invisible | B | CR-8b (the fee is kept by the retailer: the shoppers' outlay in C-2 is the retailers' receipt) | A-1, A-N2 |
| C-4 | retailers | compliance_cost | increase | short | visible | B | CR-1 op. 3; CR-8c (new bag stock, receipt changes, signage, staff instruction, fee handling) | A-1 |
| C-5 | input_suppliers (thin bag makers) | quantity_traded (thin carryout bags sold to Brennick retailers, after the effective date) | decrease | short | visible | B | CR-1 op. 1 for their buyers; CR-9 (input_to: their buyers stop buying) | A-1 |
| C-6 | shoppers (buyers.current) | quantity_substitute (reusable bags) | increase | short | visible | B | CR-4b (x: paper bag at 10 cents or more, y: reusable or own bag); CR-4 (x: thin bag, now removed) | A-2 |
| C-7 | shoppers (buyers.current) | quantity_substitute (reusable bags) | increase | long | invisible | B | CR-10b (carrying bags is a habit built by repeated trips, so the shift grows); CR-4b | A-2, A-14 |
| C-8 | shoppers (buyers.current) | quantity_traded (paper carryout bags) | ambiguous | short | invisible | B | (+) CR-4b (x: thin plastic bag, removed; y: paper bag) for shoppers who rank paper above reusable even at the fee; (-) CR-4c (shoppers who would have taken free paper bags now pay 10 cents and take fewer); CR-12b | A-1, A-2, A-N2 |
| C-9 | shoppers.food_assistance | quantity_traded (paper carryout bags, free) | increase | short | invisible | B | CR-4b (x: thin plastic bag, removed; y: free paper bag, exempt from the fee) | A-1, A-N1 |
| C-10 | retailers | reclassification (thick plastic bags sold as reusable at the till) | U1-a: increase; U1-b: ambiguous | short | invisible | B | CR-6 (pressure from the fixed minimum on paper bags moves to the unregulated form, reusable bags at any price); CR-4b (x: the covered form, y: the uncovered form). U1-a: maker's claim accepted, so cheap thick bags qualify. U1-b: a test applied; which bags qualify is unknown | A-4, A-N2 |
| C-11 | retailers.small | informal_activity (thin bags handed out or paper fee waived) | increase | short | invisible | B | CR-4b (x: comply, y: violate), where waiving the fee or handing out thin bags keeps customers; CR-6 third margin | A-5, A-N2 |
| C-12 | shoppers.near_route_9 | cross_border_purchases | increase | short | invisible | B | CR-4b (x: shop in Brennick, y: shop at Fallow Creek supermarkets, where bags stay free) | A-6, A-9 |
| C-13 | shoppers (buyers.current) | inventory_held (thin plastic bags, at the effective date) | increase | short | invisible | B | CR-10a; CR-4c (x: take bags later, when they cannot be had; y: take extra bags now) | A-7 |
| C-14 | input_suppliers (thin bag makers) | quantity_traded (thin carryout bags sold to Brennick retailers, nine-month window) | increase | short | invisible | B | CR-10a; CR-9 (input_to: retailers restock as shoppers take extra bags) | A-7 |
| C-15 | bag makers and retailers | lobbying_effort | increase | medium | invisible | B | CR-4b (x: accept, y: lobby to amend, delay or widen exemptions); concentrated stakes | A-8 |
| C-16 | shoppers (buyers.current) | quantity_substitute (bin liners and pet-waste bags) | increase | medium | invisible | B | CR-9 (the thin bag was also used as a liner, so its removal raises demand for goods serving that end); CR-4b (x: reuse a carryout bag, removed; y: buy liners) | A-3 |
| C-17 | retailers.near_route_9 (Brennick) | quantity_traded (groceries) | decrease | short | invisible | B | CR-9 (the whole basket moves with the shopper, C-12) | A-6, A-9 |
| C-18 | neighboring_jurisdictions (Fallow Creek supermarkets) | quantity_traded (groceries) | increase | short | invisible | B | CR-9 (they gain the baskets that move, C-12) | A-6, A-9 |
| C-19 | staff at Brennick stores near Route 9 | employment, hours_worked | at_least_one_decrease | medium | invisible | B | CR-9, LW-10 (demand for store labor follows store sales, C-17); CR-4 for the stores (x: keep staffing, y: cut hours or hiring) | A-6, A-9, A-15 |
| C-20 | staff at Fallow Creek stores near the line | employment, hours_worked | at_least_one_increase | medium | invisible | B | CR-9, LW-10 (mirror of C-19) | A-6, A-9, A-15 |
| C-21 | input_suppliers (paper bag makers) | quantity_traded (paper bags sold to Brennick retailers) | ambiguous | short | invisible | B | CR-9, LW-10 (follows C-8, which is ambiguous); CR-12b | A-1, A-2, A-N2 |
| C-22 | shoppers (buyers.current) | price_paid (groceries, Brennick) | ambiguous | long | invisible | B | (-) CR-9 and CR-7a: stores' spending on bags per transaction falls and competition carries cost changes to shelf prices; (+) the same for compliance costs (C-4) and for fixed costs spread over fewer sales near the line; CR-12b | A-12, A-13 |
| C-23 | officials.enforcement (Office of Sustainability) | enforcement_cost | increase | short | visible | A | CR-8c; K3 |  |
| C-24 | taxpayers | resources_available_other_uses | decrease | short | invisible | A | CR-8a, CR-8b (K3 funded from the general budget) |  |
| C-25 | shoppers (buyers.current) | resources_available_other_uses | decrease | short | invisible | B | CR-3a (chosen option, the free thin bag, removed); CR-8b (paper-bag fees, reusable bags and liners bought); CR-8c (time spent carrying, remembering and travelling to stores across the line) | A-2, A-3 |

## Gaps found

**(a) Calculus gaps.** None. Every step was derived from CR-1 to CR-12, LW-10 and arithmetic.

**(b) New premises.**
- A-N1 (food-assistance shoppers take free paper bags, p 0.8): CR-4 gives the direction for these shoppers, but the case assumptions do not say that any of them are at the margin between paper and their own bags.
- A-N2 (the 10-cent floor binds, p 0.8): CR-6 applies only where a fixed price differs from what the parties would otherwise set; the case assumptions state that thin bags were free but not what paper bags would cost without K2. Every K2 chain needs it.

**(c) Unclear core rules.**
- CR-9 on trip complements: CR-9 speaks of "goods used together"; groceries and carryout bags are bought together, not used together. The link was made through the trip relation recorded in 02_ontology 2.8, which CR-9 refers to, but the rule's own wording does not cover it.
- CR-9 on secondary use: the thin bag served two ends (carrying and lining bins). CR-9's statement that demand for "goods that compete with it" moves "in the opposite direction" fits only if a bag reused as a liner is read as competing with liners; 2.8's secondary_use note supplies this, not CR-9 itself.
- CR-6 on a minimum price for a good the seller keeps the proceeds of: CR-6 is written for a price prevented from moving between buyers and sellers who both want to trade more or less. Here the retailer may wish to give paper bags away to win customers; that this is "pressure from sellers" displaced to cheap reusable bags and fee waivers is a reading, not a statement of the rule.

## Comparison with the pattern-based analysis

**Summary.** The versions agree on the main chain: thin bags disappear, a paper bag now costs the shopper at least 10 cents and the retailer keeps it, shoppers switch to reusable bags and households to bought liners, edge shoppers move whole baskets across the line (RS-4 with RS-9), small stores evade, shelf prices are ambiguous, and shoppers and taxpayers have less for other uses. There are two sign differences. The pattern version's `employment` decrease at edge stores (C-14) should be the group sign `at_least_one_decrease` over employment and hours. OC-5 itself says "employment or hours_worked", and 2.5 says that writing one member as a plain decrease overclaims, so the core is right. The pattern version counts paper bags with reusable bags as an increase (C-3); the core makes paper-bag use ambiguous (C-8). The core's minus chain, shoppers who "would have taken free paper bags" and now pay, compares with a world with the ban but no fee (A-N2), not with the counterfactual of no policy. The record says stores gave thin plastic bags, so on the case as stated the pattern version's increase is better supported. The pattern version's retailers' `resources_available_other_uses` increase (C-15) avoids CR-12 by treating compliance spending as a separate variable, although compliance spending reduces the same pool of resources. The core omitted the row.

**Counts.** M 12, V 4, S 2, OP 4, OC 1. Causes over S, OP and OC (7 items): P 1, K 0, A 1, E 5 (pattern version 4, core version 1), J 0.

### Pattern version → core version

| Pattern ID | Matched core ID(s) | Class | Cause | Note |
|---|---|---|---|---|
| C-1 | C-1, C-5 | M | | Core splits off the thin-bag makers (C-5). |
| C-2 | C-2 | M | | The core adds A-N2 (the floor binds). |
| C-3 | C-6, C-7, C-8 | S | E (core) | Reusable bags: both increase (C-6, C-7). Paper bags: pattern increase (inside C-3), core ambiguous (C-8). **Pattern better supported.** The sign is against the counterfactual without the policy (2.5), in which stores hand out thin plastic bags. The core's minus chain (free paper bags now charged) needs paper bags to have been given away before the ordinance, and the record does not say so. A-N2 asks what stores would do under K1 without K2, a counterfactual that mixes components. If free paper bags were common before the ordinance, the core's ambiguity would be right. |
| C-4 | C-16 | M | | |
| C-5 | C-4 | M | | The pattern version cites OC-1; the derivation is CR-8c (OC-2 or TX-5 in form). Citation only. |
| C-6 | C-3 | M | | |
| C-7 | C-10 | V | | The core reports both readings of the 125-use provision (U1-a increase; U1-b ambiguous). The pattern version assumed U1-a. |
| C-8 | C-11 | M | | |
| C-9 | C-12 | M | | |
| C-10 | C-13, C-14 | V | | Window bag-taking is recorded as shoppers' `inventory_held` and makers' window sales. |
| C-11 | C-15 | M | | |
| C-12 | C-18 | M | | |
| C-13 | C-17 | M | | |
| C-14 | C-19 | S | P | Pattern: `employment` decrease; core: employment or hours, `at_least_one_decrease`. **Core right.** OC-5's conclusion is "employment or hours_worked", and 2.5 (group consequences) says that writing one variable as a plain decrease overclaims. CR-4 gives stores several margins (hiring, hours). |
| C-15 | — | OC | E (pattern) | Retailers' `resources_available_other_uses` increase from lower bag spending. The pattern version avoids netting by calling compliance a different variable (`compliance_cost`). But compliance spending is drawn from the same resources (CR-8c), so on this variable the chains oppose: bag savings and fee receipts (+) against compliance spending and lost edge sales (−). CR-12b gives ambiguous unless a premise says which dominates. The core omitted the row; the correct entry is ambiguous. |
| C-16 | C-22 | V | | Both ambiguous; medium against long horizon. |
| C-17 | C-25 | M | | |
| C-18 | C-25 | V | | Liners are inside the core's shoppers' row. |
| C-19 | C-24 | M | | |

### Core-only consequences

| Core ID | Class | Cause | Note |
|---|---|---|---|
| C-9 | OP | A | Food-assistance shoppers take more free paper bags; rests on the new premise A-N1. |
| C-20 | OP | E (pattern) | Fallow Creek staff, `at_least_one_increase`. The pattern version noted the mirror of C-14 but chose not to record it; OC-5 calls for both sides. |
| C-21 | OP | E (pattern) | Paper-bag makers' sales. The pattern version did not follow the `input_to` link. The core's ambiguous sign inherits the counterfactual problem in C-8; against the counterfactual without the policy, the sign is an increase. |
| C-23 | OP | E (pattern) | Office of Sustainability `enforcement_cost`. OC-3 gives it; the pattern version recorded only the taxpayer side (C-19). |

### Findings

- **Pattern overclaimed (P).** Pattern-version C-14 writes OC-5's "employment or hours_worked" as a plain `employment` decrease. The pattern is right; its application overclaims, contrary to 2.5.
- **Composition error in the pattern version.** C-15 (retailers' resources increase) avoids CR-12b by treating compliance spending as a separate variable, though that spending comes from the same resources. The sign should be ambiguous.
- **Core-version error.** Paper-bag use (C-8) and paper-bag makers' sales (C-21) are made ambiguous through a chain that compares with a ban-without-fee world, not with the counterfactual without the policy (2.5). The same framing appears in A-N2's wording: the floor's bindingness is posed against K1 alone.
- **Core rules.** No difference traces to a limit of the calculus (K = 0). The core version's notes (CR-9 wording for trip complements and secondary uses; CR-6 for a floor on a good sellers would give away) are wording issues that 2.8's relation notes already cover.
