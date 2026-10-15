# WE-005 Retail gasoline price cap after a refinery outage

Analyst: draft (Handbook 0.2)  |  Rule catalog version: 0.2  |  Status: awaiting expert review

A stylized policy in a fictional state. It resembles emergency fuel-price orders that governments sometimes issue after a supply disruption, but it is not modeled on any particular one. The probabilities are illustrative; the evidence column says what a real analysis would cite.

## 1. Policy record

**Corvane Emergency Fuel Price Order.** Corvane is a state of about six million people. On Day 0 a fire shuts the Port Aldis refinery, which makes about 40% of the gasoline sold in the state. The owner expects repairs to take 8 to 12 weeks. Corvane requires a special clean-burning blend that few refineries outside the state make; replacement cargoes come by tanker and take 2 to 4 weeks to arrive. A products pipeline carries gasoline from Corvane refineries east to the neighboring state of Brennick, which accepts Corvane's blend (it meets a stricter standard than Brennick's own). Its capacity is about a tenth of Corvane's consumption. The eastern Corvane cities are 20 to 45 minutes' drive from the Brennick line.

Before the outage, regular gasoline averaged $3.90 a gallon in Corvane. By Day 3 it was $5.10. In Brennick it was about $4.00. On Day 3 the governor announced that a cap would take effect on Day 5. The order expires on Day 95. Wholesale (rack) prices are not capped.

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Retail price cap | `price_ceiling` | Gasoline sold at retail in Corvane | Retail stations | Regular capped at $4.20 a gallon including taxes; midgrade at $4.50; premium at $4.80 (the pre-outage differentials). Days 5 to 95. | Diesel. Deliveries to commercial fleets under contracts signed before Day 0. |
| K2 No-surcharge rule | Restriction on contract terms (part of K1) | Retail fuel sales | Retail stations | No fees, surcharges or required purchases tied to a fuel sale; the posted price must be the pump price. | None |
| K3 Enforcement | Administration and enforcement | K1, K2 | State Attorney General | Fines up to $5,000 per violation; inspectors check posted prices; a public hotline; funded by an emergency appropriation from the general fund. | None |

Unclear provisions: whether stations may limit the quantity sold per customer, shorten their opening hours or refuse card payments. The order is silent on all three. Assumed allowed (A-4).

## 2. Classification

| Component | Rothbard type | Binding? | Rule families |
|---|---|---|---|
| K1 | Triangular: fixes the terms of exchange between stations and drivers | Yes, while the market price would stay above $4.20 (A-1). As the refinery is repaired and cargoes arrive, the market price would have fallen, so the cap may stop binding before Day 95. | PC, RS, TS |
| K2 | Triangular | Yes, by its text; it closes the most direct ways to charge more than the cap | RS-2, RS-3 |
| K3 | Binary: funded by taxpayers | Yes | OC-3 |

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `drivers` | Everyone who buys gasoline at retail in Corvane | Lower posted price; fuel harder to find. Split into `drivers.served` (those who obtain fuel at the cap) and `drivers.unserved` (those who do not, or not when they want it). |
| `drivers.border` | Drivers in the eastern cities, near Brennick | Can buy in Brennick, where the price is not capped. |
| `stations` | Retail sellers in Corvane | Pump price capped; wholesale cost is not; can change hours, service and payment terms. |
| `suppliers` (`input_suppliers`) | In-state refiners, importers and traders of Corvane-blend gasoline | Corvane stations can no longer pay as much; other outlets (Brennick via the pipeline, other markets for cargoes) are uncapped. |
| `refiner.port_aldis` | Owner of the damaged refinery | The reward for restoring output early is now tied to a capped retail market. |
| `stations.brennick` | Stations just across the line | Some Corvane drivers. |
| `officials.enforcement`, `taxpayers` | Attorney General's office and its funders | New enforcement task. |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | `drivers.served` | `price_paid` | decrease | short | K1, PC-3 | A-1, A-2 |
| C-2 | `stations` | `net_price_received` | decrease | short | K1 | A-1, A-2 |

The visible effect: drivers who fill up pay at most $4.20 for regular instead of about $5.10. Stations receive less per gallon by the same amount.

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-3 | `drivers` | `quantity_demanded` (driving not cut back, tanks kept fuller, cans filled) | increase | short | PC-1, LW-3 | A-1 |
| C-4 | `drivers` | `excess_demand` | increase | short | PC-1 | A-1, A-2 |
| C-5 | `drivers` | `wait_time` (queues at stations) | increase | short | PC-2, OC-2 | A-1, A-2, A-3 |
| C-6 | `drivers` | `search_cost` (driving between stations to find one with fuel; finding informal sellers) | increase | short | PC-2, RS-10 | A-1, A-2, A-3 |
| C-7 | `drivers` | `allocation_by_non_price_criteria` (fuel goes to those with time to queue, regular customers, those who arrive just after a delivery; per-car limits) | increase | short | PC-2 | A-1, A-2, A-4 |
| C-8 | `stations` | `quality_per_unit` (shorter hours, fewer attendants, cash only, closed restrooms and air pumps) | decrease | short | PC-4, RS-2 | A-1, A-4 |
| C-9 | `drivers` | `informal_activity` (resale of fuel in cans above the cap, through online listings) | increase | short | PC-6, RS-3 | A-1, A-5 |
| C-10 | `suppliers` | `quantity_supplied` (gasoline delivered into Corvane) | decrease | short | PC-5, LW-4, RS-4 | A-1, A-6 |
| C-11 | `suppliers` | `net_price_received` (wholesale gasoline sold to Corvane stations) | decrease | short | GAP-005-1 | A-1, A-7 |
| C-12 | `drivers` | `quantity_demanded` (Days 3 to 5, between announcement and effective date) | decrease | short | RS-8 | A-8 |
| C-13 | `stations` | `quantity_demanded` (wholesale purchases, Days 3 to 5) | decrease | short | RS-8 | A-8 |
| C-14 | `refiner.port_aldis` | `maintenance_spending` (overtime and expedited parts to finish the repair sooner) | decrease | short | GAP-005-1, LW-4 | A-7, A-9 |
| C-15 | `stations` | `lobbying_effort` (for a wholesale cap or an early end to the order) | increase | short | RS-7 | A-1 |

C-10 applies PC-5 at a short horizon. PC-5's default horizon (medium to long) reflects durable capital that wears out slowly (TS-1). Here the resource that moves is not a building but a tanker cargo or a day's pipeline shipment, which can be sent elsewhere within days. A trader deciding where to send a cargo of Corvane-blend gasoline compares the price it can fetch in Corvane with the price elsewhere (LW-4). The cap lowers the first, so fewer cargoes are ordered for Corvane and more of the in-state refiners' output goes through the pipeline to Brennick.

C-11 and C-14 rest on a move the catalog does not cover. Stations are the only large buyers of wholesale gasoline in Corvane. If they cannot charge more than $4.20, they cannot pay more than $4.20 less taxes and costs. Either the wholesale price for Corvane sales falls, or stations lose money on each gallon and buy less. No rule describes how a ceiling on a final good passes up the chain to its main input (GAP-005-1), so C-11 is Tier C, and so is C-14, which depends on it: the owner of the damaged refinery earns less from output sold before Day 95, so it has less reason to pay for overtime and air-freighted parts to finish sooner.

C-12 and C-13: between the announcement on Day 3 and the cap on Day 5, drivers who can wait for the lower price do, and stations avoid buying wholesale stock at Day 3 prices that they would have to sell at the cap. Both shift purchases to Day 5, so the cap starts with low station stocks and a burst of demand.

Not reported: reclassification (RS-5). The exemptions are closed: fleet contracts must predate the outage, and diesel does not run gasoline engines. A-15 is below the cut-off (p = 0.15). Also not reported: suppliers keeping cargoes away beyond Day 95 because they expect the order to be extended (TS-2); A-14 is below the cut-off (p = 0.35).

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-16 | `drivers.unserved` | `quantity_substitute` (transit, car-sharing, trips not made) | increase | short | PC-3, RS-1 | gasoline and transit: `substitute`, partial | A-1, A-10 |
| C-17 | `drivers.border` | `cross_border_purchases` | ambiguous (section 7) | short | RS-4, PC-2, PC-3 | Corvane and Brennick stations: `across_border`, close for eastern cities | A-11 |
| C-18 | `stations` that run out of fuel | `quantity_traded` (in-store goods: snacks, coffee, lottery) | decrease | short | RS-9 | fuel and in-store goods: `complement`, note `trip` | A-1, A-6, A-12 |
| C-19 | `stations` that have fuel | `quantity_traded` (in-store goods) | increase | short | RS-9 | same | A-1, A-6, A-12 |

C-18 and C-19: when a station runs dry, its customers buy fuel wherever there is some, and they buy their coffee and snacks there too (RS-9). This is a shift between stations, not a change in the total. The chain is at depth 4 (cap, fewer deliveries, dry stations, in-store sales) and stops here.

RS-10 is recorded in C-6 (finding informal sellers) and C-9; buyers of fuel in cans also cannot judge its quality or seek redress, which no variable in version 1 records beyond `search_cost`. RS-11 was checked and does not apply: the right to buy at the cap is not tied to holding anything or living anywhere.

Pruned: the effect on prices in Brennick. It is at depth 3, falls on diffuse bystanders, and combines the pipeline diversion in C-10 (more fuel in Brennick) with the ambiguous C-17 (more or fewer Corvane buyers). Also pruned: state fuel-tax revenue, which falls with the quantity sold (C-20); depth 3, diffuse.

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `drivers.border`, `cross_border_purchases`, short | Queues and dry stations at home raise the cost of buying in Corvane (C-5, C-6), so more drivers cross. | The home price falls from about $5.10 to $4.20, so the money saved by crossing to Brennick (about $4.00) falls from about $1.10 to $0.20 a gallon (C-1). | None | **ambiguous**. It depends on how long the queues are compared with how much drivers value the money saved. Without the cap, many eastern drivers would cross anyway, for the price. |
| `drivers`, cost per gallon including time and searching, short | Wait, search and informal premiums (C-5, C-6, C-9). | Lower money price (C-1). | None | **ambiguous**, Tier C: the version 1 variable list has no variable for the full cost of a unit to the buyer (GAP-005-2). Who gains and who loses is clearer: drivers whose time is cheap to them gain; drivers whose time is dear to them lose (C-7). |
| `suppliers`, `quantity_supplied` (first weeks after Day 95), short | Product held in terminals for sale after the cap ends, and cargoes timed to arrive just after it (RS-8, A-13). | A later repair finish leaves the refinery's output lower in the weeks after Day 95 (C-14, Tier C). | None | **ambiguous**, Tier C (the − chain rests on GAP-005-1). If C-14 were rejected on review, the sign would be **increase**. |

## 8. Time structure

- **Announcement window (Days 3 to 5).** The two-day notice shifts purchases by both drivers and stations to Day 5 (C-12, C-13, RS-8). The cap therefore opens with stations short of stock and a rush of buyers, so queues start at once.
- **Days 5 to about 40.** In the counterfactual, the price spike is what draws cargoes from distant refineries; cargoes ordered in the first week arrive in weeks 3 to 6, and the price falls as they do. Under the cap fewer are ordered (C-10), so the period of shortage lasts longer than the price spike would have. This is when queues, station hopping and informal resale (C-5, C-6, C-9) are greatest.
- **Weeks 8 to 12.** The refinery is due back in this period. The cap lowers the reward for finishing before Day 95, though not after it (C-14, Tier C). If the repair finishes early in any case, the market price would fall toward the cap and the cap stops binding before it expires (A-1).
- **Near Day 95.** Suppliers who expect the order to end on schedule (A-13) gain by holding product in terminals for a few days and by timing cargoes to arrive just after the cap ends (RS-8). This deepens the shortage in the last days of the cap; how supply compares with the counterfactual in the weeks after is ambiguous (section 7). If suppliers instead expected an extension (A-14, below the cut-off), diversion would continue past Day 95 (TS-2).
- **Durability.** No durable capital changes in 90 days; TS-1 and TS-3 play no role. The one long-lived asset involved is the damaged refinery, and the cap changes only how fast it is repaired, not whether.

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-20 | `drivers.unserved`, `suppliers` | `quantity_traded` (retail gasoline in Corvane) | decrease | Gallons that drivers would have bought at the uncapped price, from cargoes that would have come to Corvane and now go elsewhere. Both sides lose the gain each expected. | OC-4 |
| C-21 | `taxpayers` | `resources_available_other_uses` | decrease | What the emergency appropriation for enforcement would otherwise have funded. | OC-3, OC-1 |

Time spent in queues is recorded as C-5 and is not listed again here.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | Without the cap, the retail price would stay above $4.20 for most of the 90 days. | binding | 0.85 | Wholesale forward prices for Corvane blend; the repair estimate; tanker transit times. | Effects shrink to the weeks in which the cap binds. |
| A-2 | Pump prices are enforced: few stations post or charge more than the cap. | enforcement | 0.9 | Posted prices are public; inspector numbers; fine size against the price gap. | C-1 shrinks; overcharging replaces queues. |
| A-3 | Most drivers have no close substitute for the car for daily trips, so they queue and search rather than give up. | substitutability | 0.8 | Commuting mode shares; transit coverage outside the main cities. | C-5 and C-6 shrink; C-16 grows. |
| A-4 | Stations may change hours, service, payment terms and per-car limits (the order is silent). | other | 0.8 | Order text; Attorney General guidance. | C-7 (limits) and C-8 weaken. |
| A-5 | Some resale of fuel in cans above the cap goes undetected. | enforcement | 0.55 | Online listings in past shortages; enforcement focus on stations rather than individuals. | C-9 not reported. |
| A-6 | Cargoes of Corvane blend have other buyers, and the pipeline to Brennick has spare capacity. | alternative_uses | 0.85 | Cargo trading patterns; pipeline nominations. | C-10 shrinks to what in-state refiners withhold. |
| A-7 | Most in-state output has no outlet other than Corvane stations in the short run, so the retail cap holds down the wholesale price for Corvane sales. | other | 0.7 | Pipeline capacity against in-state output; rack price data after the order. | C-11 and C-14 fail (Tier C chain). |
| A-8 | Drivers and stations know the effective date and can shift purchases by two days. | expectations | 0.75 | Coverage of the announcement; typical fill-up intervals; station tank sizes. | C-12, C-13 not reported. |
| A-9 | The repair can be speeded up by spending more (overtime, expedited parts). | other | 0.6 | The owner's repair plan; availability of contractors and parts. | C-14 fails. |
| A-10 | Transit, car-sharing or dropping trips is feasible for some unserved drivers. | substitutability | 0.65 | Transit coverage in the main cities. | C-16 not reported. |
| A-11 | Drivers in the eastern cities can reach Brennick stations easily. | mobility | 0.7 | Drive times of 20 to 45 minutes. | C-17 not reported. |
| A-12 | Drivers buy in-store goods on fuel trips. | other | 0.75 | Station convenience-store sales data. | C-18, C-19 not reported. |
| A-13 | Suppliers expect the order to end on Day 95 and have terminal space to hold product for a few days. | expectations | 0.6 | The governor's statements; terminal storage capacity. | The + chain in section 7 fails. |
| A-14 | Suppliers expect the order to be extended beyond Day 95. | expectations | 0.35 | Statements by officials; history of emergency orders in the state. | Below cut-off; not reported. |
| A-15 | Stations or buyers can reshape sales to fall under an exemption. | other | 0.15 | Exemption text (pre-outage contracts; diesel only). | Below cut-off; not reported. |

## 11. Report

**The policy.** For 90 days after a refinery fire, Corvane caps the retail price of gasoline at $4.20 for regular, about 90 cents below the market price at the time. Surcharges and tie-ins are banned. Wholesale prices are not capped. Diesel and existing fleet contracts are exempt.

**Visible consequences.** Drivers who fill up pay less than they would have (C-1), and stations receive less per gallon (C-2).

**Invisible consequences.**
- *Drivers* want more fuel at the lower price (C-3) than there is (C-4). They wait in queues (C-5), drive around looking for stations with fuel (C-6), and find that fuel goes to those who can queue, regular customers and those who arrive after a delivery (C-7). Some buy fuel in cans from informal sellers at prices above the cap (C-9). Those who cannot get fuel use transit, share cars or skip trips (C-16). Drivers waited for the cap before buying (C-12), which made the first days of the cap worse.
- *Stations* cut hours and services and may refuse cards (C-8). Stations that run dry lose their in-store sales to stations that have fuel (C-18, C-19). Station owners lobby for a wholesale cap or an early end (C-15).
- *Suppliers* send fewer cargoes and more pipeline gasoline elsewhere (C-10), so less gasoline is sold in Corvane than would have been (C-20). As Tier C suggestions: suppliers selling to Corvane stations receive less (C-11), and the damaged refinery has less reason to pay for a faster repair (C-14).
- *Taxpayers* fund enforcement (C-21).

**Ambiguous effects.** Whether more or fewer eastern drivers buy in Brennick (section 7). Whether drivers as a group pay more or less once time and searching are counted; the method can say only that drivers who value their time less gain relative to those who value it more. Whether more or less fuel is available in the weeks after the cap ends.

**Key conditions.** The cap must bind (A-1, p = 0.85); if the repair is quick and cargoes arrive early, the market price would fall toward $4.20 and the order would change little. The diversion of supply (C-10) depends on cargoes and pipeline gasoline having other buyers (A-6, p = 0.85).

**What this analysis cannot say.** How long the queues will be, how much less gasoline arrives, or how much later the shortage ends than the price spike would have; whether gains to drivers who fill up at the cap outweigh losses to those who wait or go without; safety effects of fuel stored in cans (out of scope for version 1); whether the order is desirable.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | drivers.served | price_paid | decrease | short | visible | B | K1, PC-3 | A-1, A-2 |
| C-2 | stations | net_price_received | decrease | short | visible | B | K1 | A-1, A-2 |
| C-3 | drivers | quantity_demanded | increase | short | invisible | B | PC-1, LW-3 | A-1 |
| C-4 | drivers | excess_demand | increase | short | invisible | B | PC-1 | A-1, A-2 |
| C-5 | drivers | wait_time | increase | short | invisible | B | PC-1, PC-2, OC-2 | A-1, A-2, A-3 |
| C-6 | drivers | search_cost | increase | short | invisible | B | PC-1, PC-2, RS-10 | A-1, A-2, A-3 |
| C-7 | drivers | allocation_by_non_price_criteria | increase | short | invisible | B | PC-1, PC-2 | A-1, A-2, A-4 |
| C-8 | stations | quality_per_unit | decrease | short | invisible | B | PC-4, RS-2 | A-1, A-4 |
| C-9 | drivers | informal_activity | increase | short | invisible | B | PC-6, RS-3 | A-1, A-5 |
| C-10 | suppliers | quantity_supplied (into Corvane) | decrease | short | invisible | B | PC-5, LW-4, RS-4 | A-1, A-6 |
| C-11 | suppliers | net_price_received (wholesale, Corvane sales) | decrease | short | invisible | C | GAP-005-1 | A-1, A-7 |
| C-12 | drivers | quantity_demanded (Days 3–5) | decrease | short | invisible | B | RS-8 | A-8 |
| C-13 | stations | quantity_demanded (wholesale, Days 3–5) | decrease | short | invisible | B | RS-8 | A-8 |
| C-14 | refiner.port_aldis | maintenance_spending (speed of repair) | decrease | short | invisible | C | GAP-005-1, LW-4 | A-7, A-9 |
| C-15 | stations | lobbying_effort | increase | short | invisible | B | RS-7 | A-1 |
| C-16 | drivers.unserved | quantity_substitute (transit, fewer trips) | increase | short | invisible | B | PC-3, RS-1 | A-1, A-10 |
| C-17 | drivers.border | cross_border_purchases | ambiguous | short | invisible | B | RS-4 vs PC-3 (C-5, C-6 vs C-1) | A-1, A-11 |
| C-18 | stations (out of fuel) | quantity_traded (in-store goods) | decrease | short | invisible | B | PC-5, RS-9 | A-1, A-6, A-12 |
| C-19 | stations (with fuel) | quantity_traded (in-store goods) | increase | short | invisible | B | PC-5, RS-9 | A-1, A-6, A-12 |
| C-20 | drivers.unserved, suppliers | quantity_traded (retail gasoline) | decrease | short | invisible | B | PC-5, OC-4 | A-1, A-6 |
| C-21 | taxpayers | resources_available_other_uses | decrease | short | invisible | A | OC-3, OC-1 | none |
| — | drivers | full cost per gallon (no variable; GAP-005-2) | ambiguous | short | invisible | C | C-1 vs C-5, C-6, C-9 | A-1, A-2, A-3 |
| — | suppliers | quantity_supplied (first weeks after Day 95) | ambiguous | short | invisible | C | RS-8 vs C-14 | A-7, A-9, A-13 |

## Gaps found

- **GAP-005-1. A ceiling on a final good passes up the supply chain.** Needed for C-11 and C-14 (Tier C). No rule says what happens to the price of an input when the good it is used to make is capped and capped sellers are the input's main buyers. Proposed fix: a new PC rule. *If* a binding `price_ceiling` on a good, and the sellers of that good buy most of a named input (relation `input_to`), *then* either `net_price_received` by input suppliers for sales into the capped market decreases, or the capped sellers' margins fall and they buy less of the input (`quantity_demanded` for the input decreases), or both. *Assumes* few uncapped outlets for the input in the period considered (`alternative_uses`). Tier B. Builds on LW-4 and the logic of PC-5.
- **GAP-005-2. No variable for the full cost of a unit to the buyer.** Needed for the second combined entry in section 7. WE-001 met the same problem informally ("total cost of housing"). Under a ceiling the money price falls while time, search and side payments rise; the method needs a single place to record how these combine, even if the sign is usually ambiguous. Proposed fix: add `full_cost_per_unit` to 2.4 (money price plus the money value the buyer places on wait time, search and side payments per unit obtained), with a note that it is ambiguous under PC-1 unless a dominance rule is added.
