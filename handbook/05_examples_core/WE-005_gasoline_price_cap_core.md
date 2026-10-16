# WE-005 / Analysis: Retail gasoline price cap after a refinery outage (core-only re-run)

Analyst: core-only re-run (Handbook 0.4)  |  Rules: core rules CR-1 to CR-12 only  |  Status: awaiting comparison

Rule set: the core rules CR-1 to CR-12 (`../04a_core_rules.md`), AX-1 and LW-1 to LW-10 (`../01_foundations.md`), and arithmetic. No pattern is cited. New premises that the derivations needed are numbered A-N1, A-N2, ... and are listed in section 10 and under "Gaps found".

## 1. Policy record

**Corvane Emergency Fuel Price Order.** Corvane is a state of about six million people. On Day 0 a fire shuts the Port Aldis refinery, which makes about 40% of the gasoline sold in the state. The owner expects repairs to take 8 to 12 weeks. Corvane requires a special clean-burning blend that few refineries outside the state make; replacement cargoes come by tanker and take 2 to 4 weeks to arrive. A products pipeline carries gasoline from Corvane refineries east to the neighboring state of Brennick, which accepts Corvane's blend (it meets a stricter standard than Brennick's own). Its capacity is about a tenth of Corvane's consumption. The eastern Corvane cities are 20 to 45 minutes' drive from the Brennick line.

Before the outage, regular gasoline averaged $3.90 a gallon in Corvane. By Day 3 it was $5.10. In Brennick it was about $4.00. On Day 3 the governor announced that a cap would take effect on Day 5. The order expires on Day 95. Wholesale (rack) prices are not capped.

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Retail price cap | `price_ceiling` | Gasoline sold at retail in Corvane | Retail stations | Regular capped at $4.20 a gallon including taxes; midgrade at $4.50; premium at $4.80 (the pre-outage differentials). Days 5 to 95. | Diesel. Deliveries to commercial fleets under contracts signed before Day 0. |
| K2 No-surcharge rule | Restriction on contract terms (part of K1) | Retail fuel sales | Retail stations | No fees, surcharges or required purchases tied to a fuel sale; the posted price must be the pump price. | None |
| K3 Enforcement | Administration and enforcement | K1, K2 | State Attorney General | Fines up to $5,000 per violation; inspectors check posted prices; a public hotline; funded by an emergency appropriation from the general fund. | None |

Unclear provisions: whether stations may limit the quantity sold per customer, shorten their opening hours or refuse card payments. The order is silent on all three, and is read here as allowing them. No reported sign depends on this reading: under the other reading [a consequence of the original analysis] and [a consequence of the original analysis] would be smaller, not reversed, because queues still ration fuel and other unregulated terms remain. Whether the Attorney General in practice treats these practices as violations is an enforcement question, A-4.

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | Core rules applied |
| --- | --- | --- | --- |
| K1 Retail price cap | triangular (fixes the terms between stations and drivers) | Yes for most of the 90 days (A-1); enforced at the pump (A-2) | CR-1, CR-2, CR-4, CR-5, CR-6, CR-7, CR-9, CR-10, CR-11 |
| K2 No-surcharge rule | triangular (removes fees, surcharges and tie-ins) | Yes; closes the money-term margins of CR-6 (A-2) | CR-1, CR-6 |
| K3 Enforcement | binary (emergency appropriation) | Yes | CR-1, CR-8 |

**CR-1 operations, by component and actor class.** Operation 1: removes an option; 2: adds an option; 3: changes what an option brings; 4: transfers means.

| Component | Actor class | CR-1 operations |
| --- | --- | --- |
| K1 | stations | 1 (selling above $4.20 / $4.50 / $4.80 removed, Days 5 to 95); 3 (fines for those who would violate) |
| K1 | drivers.corvane | 1 (paying more than the cap to obtain fuel removed at stations) |
| K1 | input_suppliers (in-state refiners, cargo sellers) | none directly (rack prices are not capped); stations' terms change (CR-9, input_to) |
| K1 | commercial fleets (pre-Day-0 contracts); diesel buyers | none (exempt) |
| K2 | stations | 1 (fees, surcharges and required purchases removed) |
| K2 | drivers.corvane | 1 (offering a surcharge or tie-in purchase to obtain fuel removed) |
| K3 | taxpayers | 4 (emergency appropriation from the general fund) |
| K3 | officials.enforcement (Attorney General) | 2 (inspection, fines, hotline) |
| K1 (announcement, Day 3) | drivers.corvane, stations, input_suppliers | 3 (what buying, selling or holding fuel before Day 5 and before Day 95 brings changes; CR-10a) |

## 3. Actor classes

| Actor class | Role | How its options change |
| --- | --- | --- |
| drivers.corvane | Buy gasoline at Corvane stations | Lower money price; less fuel available; queues |
| stations | Retail sellers bound by the cap | Cannot charge above the cap or add surcharges; rack cost not capped |
| input_suppliers (in-state refiners) | Sell Corvane blend at the rack | Stations' bids limited by the cap (CR-5c); few outlets (A-7) |
| input_suppliers (cargo sellers) | Bring Corvane-blend cargoes by tanker | Can sell elsewhere (A-6) |
| refinery owner (Port Aldis) | Repairing the damaged refinery | Return to extra repair spending changes (CR-4) |
| intermediaries (can resellers) | Resell fuel above the cap | New gain from violation (CR-6) |
| neighboring_jurisdictions (Brennick drivers and stations) | Buy and sell gasoline across the line | Pipeline supply and Corvane drivers' demand change |
| sellers.complements (station convenience stores) | Sell in-store goods on fuel trips | Trips change (CR-9, complement, trip) |
| buyers.substitutes (transit and car-sharing users) | Use alternatives to driving | Unserved drivers turn to them |
| officials.enforcement | Attorney General | Inspects and fines |
| taxpayers | Fund the emergency appropriation | Means transferred |

## 4. Direct effect

CR-1 with CR-2: from Day 5, drivers who obtain fuel at Corvane stations pay no more than the cap, and stations receive no more.

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-1 | drivers.corvane | price_paid (gasoline at Corvane stations) | decrease | short | CR-1 (op 1, K1: sales above the cap removed) → CR-2 | A-1, A-2 |
| C-2 | stations | net_price_received | decrease | short | CR-1 (op 1, K1) → CR-3a | A-1, A-2 |
| C-26 | officials.enforcement | enforcement_cost | increase | short | CR-1 (op 2, K3) → CR-8c | none |
| C-27 | taxpayers | resources_available_other_uses | decrease | short | CR-1 (op 4, K3: emergency appropriation from the general fund) → CR-8a, CR-8b | none |

## 5. Responses

CR-4 pairs of options examined for each actor class (substitute, adjust terms, evade, relocate, reclassify, exit, lobby, change timing, enter), with CR-6 where a price is fixed and CR-5 where an exchange is prevented or compelled.

| Actor class | Pair of options (CR-4) or rule | Result |
| --- | --- | --- |
| stations | CR-6 (price held below clearing): which unregulated margins are open | Hours, service, card acceptance, per-car limits (A-4); K2 closes fees and tie-ins |
| stations | CR-4 (x: full hours and service, y: cut them) | Cut (A-4) |
| stations | CR-4 (x: buy at the rack and sell at the cap, y: buy less) | Buy less where the rack exceeds the cap less costs |
| stations | CR-4 (x: comply, y: charge above the cap) | Few do (A-2) |
| stations | CR-4 (x: accept, y: lobby against extension or for relief) | Some lobby (A-N1) |
| drivers.corvane | CR-4 (x: queue, y: give up the trip) | Most queue (A-3) |
| drivers.corvane | CR-4 (x: Corvane station, y: Brennick station) | Ambiguous (section 7) |
| drivers.corvane | CR-4 (x: car trip, y: transit or car-sharing) | Some switch (A-10) |
| drivers.corvane | CR-10a (x: buy Days 3 to 5 at about $5.10, y: wait for the cap) | Wait (A-8) |
| drivers.corvane and stations | CR-4 (x: capped form, y: exempt form: fleet contract, diesel) | A-15, p 0.15: not reported |
| intermediaries | CR-4 (x: comply, y: resell in cans above the cap) | Some (A-5) |
| input_suppliers (cargo sellers) | CR-7a (x: deliver to Corvane, y: deliver elsewhere) | Some cargoes diverted (A-6) |
| input_suppliers (in-state refiners) | CR-7a (x: Corvane rack, y: pipeline to Brennick) | Shipments east up to spare capacity (A-6) |
| input_suppliers (in-state refiners) | CR-7a (x: gasoline, y: uncapped diesel) | Needs A-N2, p 0.45: not reported |
| input_suppliers | CR-10a (x: sell under the cap, y: hold product until Day 95) | Hold (A-13) |
| refinery owner | CR-4 (x: pay to speed the repair, y: normal pace) | Less speeding (A-9) |

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-3 | drivers.corvane | quantity_demanded | increase | short | C-1 → CR-4c mirror (units valued between the cap and the counterfactual price are now wanted) and CR-11a (the capped price no longer signals the outage) | A-1, A-2 |
| C-4 | stations | quantity_supplied (gasoline sold at retail in Corvane) | decrease | short | CR-5c (stations will not pay more at the uncapped rack than the cap less their costs) → CR-9 (input_to) → CR-7a (cargoes and pipeline barrels move to buyers who pay more); with C-20 (later restart) and CR-6 (hours cut, A-4) | A-1, A-2, A-6 |
| C-5 | drivers.corvane | excess_demand | increase | short | C-3 and C-4 → CR-6 → arithmetic | A-1, A-2, A-6 |
| C-6 | drivers.corvane | wait_time | increase | short | C-5 → CR-6 (pressure displaced to queues) → CR-4 (x: queue, y: give up the trip; most have no close substitute) | A-1, A-2, A-3 |
| C-7 | drivers.corvane | search_cost | increase | short | C-5 → CR-6 (stations run dry; drivers search for one with fuel) | A-1, A-2, A-3 |
| C-8 | drivers.corvane | quality_per_unit (service: hours, card acceptance, per-car limits) | decrease | short | CR-6 (pressure displaced to unregulated terms; K2 closes fees and tie-ins) → CR-4 (stations' x: full hours and service, y: cut them) | A-1, A-2, A-4 |
| C-9 | drivers.corvane | allocation_by_non_price_criteria | increase | short | C-5 → CR-6 (the scarce side chooses among buyers: regular customers, accounts, per-car limits) | A-1, A-2, A-4 |
| C-10 | drivers.corvane | full_cost_per_unit | ambiguous | short | (−) C-1; (+) C-6, C-7, C-8; CR-12b | A-1, A-2, A-3 |
| C-11 | intermediaries (can resellers) | informal_activity | increase | short | C-5 → CR-6 (exchanges outside the rule) → CR-4 (x: comply, y: resell above the cap) | A-1, A-5 |
| C-13 | drivers.corvane | cross_border_purchases | ambiguous | short | (+) C-6, C-7: queues and empty pumps → CR-4 (x: Corvane station, y: Brennick station); (−) the money price gap to Brennick narrows from about $1.10 (counterfactual $5.10 against $4.00) to about $0.20 → CR-4 mirror; CR-12b | A-1, A-2, A-11 |
| C-14 | buyers.substitutes (transit and car-sharing) | quantity_substitute (transit and car-sharing trips) | increase | short | C-4 (less gasoline reaches Corvane drivers than in the counterfactual) → CR-4 (unserved drivers' x: car trip, y: transit or car-sharing) → CR-9 (substitute) | A-1, A-2, A-6, A-10 |
| C-15 | drivers.corvane | quantity_traded (Days 3 to 5, before the cap) | decrease | short | CR-10a (cap announced Day 3 for Day 5) → CR-4 (x: buy now at about $5.10, y: wait two days for $4.20) | A-8 |
| C-16 | drivers.corvane | quantity_traded (gasoline at Corvane stations, Days 5 to 95) | decrease | short | CR-5a (exchanges between drivers who would pay above the cap and sellers who would supply only above it are prevented) with C-4 | A-1, A-2, A-6 |
| C-21 | input_suppliers (refiners and terminals) | inventory_held (last days before Day 95) | increase | short | CR-10a (cap expected to end on Day 95) → CR-4 (x: sell under the cap now, y: hold product to sell after Day 95) | A-1, A-13 |
| C-22 | stations | quantity_supplied (first days after Day 95) | increase | medium | C-21 → CR-10a (held product released once the cap ends) | A-1, A-13 |
| C-25 | stations | lobbying_effort | increase | short | CR-1 (op 1) → CR-4 (x: accept, y: lobby against extension or for relief) → CR-8c | A-1, A-N1 |

## 6. Second-order effects

Depth limit 4; diffuse bystander effects pruned after depth 3. Each link names the exchange relation it follows (CR-9).

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C-12 | drivers.corvane (buying resold fuel) | quality_information | decrease | short | C-11 → CR-11b (no brands, reviews or recourse outside the legal market) | same_market_other_segment (station ↔ resold fuel) | A-1, A-5 |
| C-17 | input_suppliers (in-state refiners) | net_price_received (rack price for Corvane blend) | decrease | short | C-2 → CR-9 (input_to) → CR-5c (stations' highest rack bid falls toward the cap less costs) → CR-7b (output with no other outlet bears the burden) | input_to (rack gasoline → retail gasoline) | A-1, A-2, A-7 |
| C-18 | input_suppliers (cargo sellers) | quantity_supplied (cargoes delivered to Corvane) | decrease | short | C-17 → CR-7a (cargoes have other buyers; they go where the net yield is higher) | input_to (imported cargoes → Corvane rack) | A-1, A-2, A-6 |
| C-19 | input_suppliers (in-state refiners) | quantity_supplied (pipeline shipments to Brennick) | increase | short | C-17 → CR-7a (the pipeline has spare capacity; barrels move to the uncapped market) | across_border (Corvane rack ↔ Brennick) | A-1, A-2, A-6 |
| C-20 | refinery owner (Port Aldis) | maintenance_spending (expediting the repair) | decrease | short | C-17 → CR-4 (x: pay overtime and expedited parts, y: repair at the normal pace; the return to output during the outage is capped) → CR-10 | input_to (refinery output → Corvane rack) | A-1, A-2, A-9 |
| C-23 | neighboring_jurisdictions (Brennick drivers) | price_paid (Brennick gasoline) | ambiguous | short | (−) C-19 → CR-6 (more supply at the Brennick rack); (+ or −) C-13 (Corvane drivers' cross-border demand is itself ambiguous); CR-12b | across_border (Corvane ↔ Brennick), partial | A-1, A-6, A-11 |
| C-24 | sellers.complements (station convenience stores) | quantity_complement (in-store goods) | ambiguous | short | (−) C-4 and C-8 (fewer gallons, shorter hours) → CR-9; (+) per-car limits and searching mean more station visits per gallon → CR-9; CR-12b | complement, trip (fuel ↔ in-store goods) | A-4, A-12 |

**Where chains were stopped.**

- C-24: effects on convenience-store staff stopped at depth 3 (ambiguous and diffuse).
- C-18: effects in the markets where diverted cargoes are sold are outside Corvane and diffuse at depth 3; stopped.
- C-14: effects on transit crowding and fares are stopped at depth 3; no recorded relation beyond the substitute link.
- Brennick stations' in-store sales follow the ambiguous C-13; not followed.

## 7. Combined effects

Keys reached by one chain, or by chains with the same sign, take that sign (CR-12a). Keys where chains conflict:

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance premise | Combined sign |
| --- | --- | --- | --- | --- |
| drivers.corvane, full_cost_per_unit, short | Queues, search, worse service | Lower money price | None | ambiguous (C-10) |
| drivers.corvane, cross_border_purchases, short | Queues and empty pumps in Corvane | Money price gap to Brennick narrows from about $1.10 to about $0.20 | None | ambiguous (C-13) |
| neighboring_jurisdictions, price_paid (Brennick), short | Corvane drivers' demand, if it rises | More pipeline supply; Corvane drivers' demand, if it falls | None | ambiguous (C-23) |
| sellers.complements, quantity_complement, short | More visits per gallon (limits, search) | Fewer gallons, shorter hours | None | ambiguous (C-24) |
| stations, quantity_supplied, short | None | Rack bids capped; cargoes and pipeline barrels diverted; slower repair; hours cut | Not needed | decrease (C-4) |

## 8. Time structure

- **Announcement (CR-10a).** The cap was announced on Day 3 for Day 5. Drivers who could wait two days did so, so purchases fell on Days 3 to 5 and surged from Day 5, adding to the early queues (C-15).
- **During the cap.** Replacement cargoes take 2 to 4 weeks; the cap lowers what they can earn in Corvane, so some are not sent (C-18). The repair takes 8 to 12 weeks, and the cap reduces the return to finishing it sooner (C-20). Both make the shortage last longer than the outage alone would.
- **Approaching Day 95.** Suppliers who expect the cap to end on Day 95 and have storage hold product back in the last days (C-21), deepening the shortage then and releasing more after the cap ends (C-22). If suppliers instead expected an extension (A-14, p 0.35), diversion would continue; not reported.
- **After the cap.** No durable stock is built or destroyed by the cap at retail (stations stay open), so most effects end with it (CR-10b). The slower repair is the main effect that outlasts the policy period, if the repair is not finished by Day 95.

## 9. Opportunity costs

Each written as a signed change in a variable (CR-3, CR-8).

| ID | Actor class | Variable | Sign | What is given up | Rules |
| --- | --- | --- | --- | --- | --- |
| C-6 | drivers.corvane | wait_time | increase | Drivers' time in queues, used up (CR-8c) | CR-6 → CR-8c |
| C-7 | drivers.corvane | search_cost | increase | Time and fuel spent searching (CR-8c) | CR-6 → CR-8c |
| C-16 | drivers.corvane | quantity_traded (gasoline at Corvane stations, Days 5 to 95) | decrease | Fuel drivers would have bought above the cap, and the trips it would have served (CR-5a) | CR-5a |
| C-25 | stations | lobbying_effort | increase | Resources spent lobbying (CR-8c) | CR-8c |
| C-26 | officials.enforcement | enforcement_cost | increase | Inspectors' time and the hotline (CR-8c) | CR-8c |
| C-27 | taxpayers | resources_available_other_uses | decrease | Other general-fund spending | CR-8a, CR-8b |

## 10. Assumptions

Case assumptions are used as given. New premises added by this re-run are marked A-N.

| ID | Statement | Type | p | Evidence | If false |
| --- | --- | --- | --- | --- | --- |
| A-1 | Without the cap, the retail price would stay above $4.20 for most of the 90 days. | binding | 0.85 | Wholesale forward prices for Corvane blend; the repair estimate; tanker transit times. | Fail or lose support: C-1, C-2, C-3, C-4, C-5, C-6, C-7, C-8, C-9, C-10, C-11, C-12, C-13, C-14, C-16, C-17, C-18, C-19, C-20, C-21, C-22, C-23, C-25 |
| A-2 | Pump prices are enforced: few stations post or charge more than the cap. | enforcement | 0.9 | Posted prices are public; inspector numbers; fine size against the price gap. | Fail or lose support: C-1, C-2, C-3, C-4, C-5, C-6, C-7, C-8, C-9, C-10, C-13, C-14, C-16, C-17, C-18, C-19, C-20 |
| A-3 | Most drivers have no close substitute for the car for daily trips, so they queue and search rather than give up. | substitutability | 0.8 | Commuting mode shares; transit coverage outside the main cities. | Fail or lose support: C-6, C-7, C-10 |
| A-4 | In practice stations can change hours, service, payment terms and per-car limits without being treated as violating the order. | enforcement | 0.8 | Order text (silent); Attorney General guidance and early enforcement actions. | Fail or lose support: C-8, C-9, C-24 |
| A-5 | Some resale of fuel in cans above the cap goes undetected. | enforcement | 0.55 | Online listings in past shortages; enforcement focus on stations rather than individuals. | Fail or lose support: C-11, C-12 |
| A-6 | Cargoes of Corvane blend have other buyers, and the pipeline to Brennick has spare capacity. | alternative_uses | 0.85 | Cargo trading patterns; pipeline nominations. | Fail or lose support: C-4, C-5, C-14, C-16, C-18, C-19, C-23 |
| A-7 | Most in-state refinery output has no outlet other than Corvane stations in the short run. | alternative_uses | 0.7 | Pipeline capacity (about a tenth of consumption) against in-state output; rack price data after the order. | Fail or lose support: C-17 |
| A-8 | Drivers and stations know the effective date and can shift purchases by two days. | expectations | 0.75 | Coverage of the announcement; typical fill-up intervals; station tank sizes. | Fail or lose support: C-15 |
| A-9 | The repair can be speeded up by spending more (overtime, expedited parts). | other | 0.6 | The owner's repair plan; availability of contractors and parts. | Fail or lose support: C-20 |
| A-10 | Transit, car-sharing or dropping trips is feasible for some unserved drivers. | substitutability | 0.65 | Transit coverage in the main cities. | Fail or lose support: C-14 |
| A-11 | Drivers in the eastern cities can reach Brennick stations easily. | mobility | 0.7 | Drive times of 20 to 45 minutes. | Fail or lose support: C-13, C-23 |
| A-12 | Drivers buy in-store goods on fuel trips. | other | 0.75 | Station convenience-store sales data. | Fail or lose support: C-24 |
| A-13 | Suppliers expect the order to end on Day 95 and have terminal space to hold product for a few days. | expectations | 0.6 | The governor's statements; terminal storage capacity. | Fail or lose support: C-21, C-22 |
| A-14 | Suppliers expect the order to be extended beyond Day 95. | expectations | 0.35 | Statements by officials; history of emergency orders in the state. | Fail or lose support: No reported consequence depends on it alone; see Not reported. |
| A-15 | Stations or buyers can reshape sales to fall under an exemption. | other | 0.15 | Exemption text (pre-outage contracts; diesel only). | Fail or lose support: No reported consequence depends on it alone; see Not reported. |
| A-N1 | Station owners and their associations can organize and spend to oppose an extension or seek relief. (new premise) | other | 0.7 | Existing retail fuel associations; a 90-day order invites lobbying on extension. | Fail or lose support: C-25 |
| A-N2 | In-state refiners can shift their output toward uncapped diesel within weeks. (new premise) | alternative_uses | 0.45 | Refinery yields are only modestly flexible, and the clean-burning blend constrains the slate. | Fail or lose support: No reported consequence depends on it alone; see Not reported. |
| A-N3 | Suppliers take the order as a sign that future emergencies will also bring caps, and hold less contingency stock. (new premise) | expectations | 0.45 | First order of its kind in the record; officials' statements unknown. | Fail or lose support: No reported consequence depends on it alone; see Not reported. |

**Not reported** (a premise has p below 0.5, or the record lacks a needed fact):

- Stations or buyers reshape sales into the fleet-contract or diesel exemptions (reclassification increase; CR-4 x: covered form, y: exempt form): A-15, p 0.15.
- Suppliers keep diverting product after Day 95 because they expect an extension (CR-10a): A-14, p 0.35.
- Refiners shift output to diesel (CR-7a, x: gasoline, y: diesel): A-N2, p 0.45.
- Suppliers hold less contingency stock in future emergencies (CR-11c, CR-10a): A-N3, p 0.45.
- Readings of the unclear provision (per-customer limits, hours, card refusal): under the stricter reading, C-8 and C-9 would be smaller, not reversed; no reported sign depends on the reading, so no per-reading signs are given.

## 11. Report

**The policy:** After a refinery fire cut about 40% of Corvane's gasoline supply, the state capped retail gasoline at $4.20 a gallon for regular (with midgrade and premium at the pre-outage differentials) from Day 5 to Day 95, banned surcharges and tie-in purchases, and had the Attorney General enforce it with fines. Wholesale prices, diesel and pre-outage fleet contracts are not capped.

**Visible consequences:** Drivers who obtain fuel at Corvane stations pay less than they would have (C-1); stations receive less (C-2); drivers wait in queues (C-6).

**Invisible consequences:** Less fuel reaches Corvane stations: cargoes go elsewhere (C-18), more is shipped to Brennick (C-19), the repair is not speeded up as much (C-20), and stations sell less (C-4, C-16), while drivers want more at the lower price (C-3). The gap shows up as shortage (C-5), searching (C-7), worse service and shorter hours (C-8), selection of customers (C-9), resale in cans (C-11) with less information for buyers (C-12), and more transit and car-sharing trips (C-14). Refiners with no other outlet receive less at the rack (C-17). Purchases dip on Days 3 to 5 (C-15); product is held back before Day 95 and released after (C-21, C-22). Stations lobby (C-25); taxpayers fund enforcement (C-27, C-26).

**Ambiguous effects:** Drivers' full cost per gallon (C-10): a lower money price against time in queues and searching. Cross-border buying in Brennick (C-13): queues push drivers east, but the price gap to Brennick shrinks from about $1.10 to $0.20. Brennick prices (C-23) and in-store sales at stations (C-24).

**Key conditions:** The cap binds (A-1, p 0.85) and is enforced (A-2, p 0.9); drivers lack close substitutes (A-3, p 0.8); stations can cut hours and service without penalty (A-4, p 0.8); cargoes and pipeline capacity have other outlets (A-6, p 0.85); in-state output has no other outlet (A-7, p 0.7).

**What this analysis cannot say:** How long queues get, how much fuel is diverted, or how much drivers gain or lose in total; whether the cap is good. Safety effects (fuel stored in cans, queues on roads) are out of scope in version 1. Signs marked ambiguous cannot be resolved without magnitudes.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C-1 | drivers.corvane | price_paid (gasoline at Corvane stations) | decrease | short | visible | B | CR-1 (op 1, K1: sales above the cap removed) → CR-2 | A-1, A-2 |
| C-2 | stations | net_price_received | decrease | short | visible | B | CR-1 (op 1, K1) → CR-3a | A-1, A-2 |
| C-3 | drivers.corvane | quantity_demanded | increase | short | invisible | B | C-1 → CR-4c mirror (units valued between the cap and the counterfactual price are now wanted) and CR-11a (the capped price no longer signals the outage) | A-1, A-2 |
| C-4 | stations | quantity_supplied (gasoline sold at retail in Corvane) | decrease | short | invisible | B | CR-5c (stations will not pay more at the uncapped rack than the cap less their costs) → CR-9 (input_to) → CR-7a (cargoes and pipeline barrels move to buyers who pay more); with C-20 (later restart) and CR-6 (hours cut, A-4) | A-1, A-2, A-6 |
| C-5 | drivers.corvane | excess_demand | increase | short | invisible | B | C-3 and C-4 → CR-6 → arithmetic | A-1, A-2, A-6 |
| C-6 | drivers.corvane | wait_time | increase | short | visible | B | C-5 → CR-6 (pressure displaced to queues) → CR-4 (x: queue, y: give up the trip; most have no close substitute) | A-1, A-2, A-3 |
| C-7 | drivers.corvane | search_cost | increase | short | invisible | B | C-5 → CR-6 (stations run dry; drivers search for one with fuel) | A-1, A-2, A-3 |
| C-8 | drivers.corvane | quality_per_unit (service: hours, card acceptance, per-car limits) | decrease | short | invisible | B | CR-6 (pressure displaced to unregulated terms; K2 closes fees and tie-ins) → CR-4 (stations' x: full hours and service, y: cut them) | A-1, A-2, A-4 |
| C-9 | drivers.corvane | allocation_by_non_price_criteria | increase | short | invisible | B | C-5 → CR-6 (the scarce side chooses among buyers: regular customers, accounts, per-car limits) | A-1, A-2, A-4 |
| C-10 | drivers.corvane | full_cost_per_unit | ambiguous | short | invisible | B | (−) C-1; (+) C-6, C-7, C-8; CR-12b | A-1, A-2, A-3 |
| C-11 | intermediaries (can resellers) | informal_activity | increase | short | invisible | B | C-5 → CR-6 (exchanges outside the rule) → CR-4 (x: comply, y: resell above the cap) | A-1, A-5 |
| C-12 | drivers.corvane (buying resold fuel) | quality_information | decrease | short | invisible | B | C-11 → CR-11b (no brands, reviews or recourse outside the legal market) | A-1, A-5 |
| C-13 | drivers.corvane | cross_border_purchases | ambiguous | short | invisible | B | (+) C-6, C-7: queues and empty pumps → CR-4 (x: Corvane station, y: Brennick station); (−) the money price gap to Brennick narrows from about $1.10 (counterfactual $5.10 against $4.00) to about $0.20 → CR-4 mirror; CR-12b | A-1, A-2, A-11 |
| C-14 | buyers.substitutes (transit and car-sharing) | quantity_substitute (transit and car-sharing trips) | increase | short | invisible | B | C-4 (less gasoline reaches Corvane drivers than in the counterfactual) → CR-4 (unserved drivers' x: car trip, y: transit or car-sharing) → CR-9 (substitute) | A-1, A-2, A-6, A-10 |
| C-15 | drivers.corvane | quantity_traded (Days 3 to 5, before the cap) | decrease | short | invisible | B | CR-10a (cap announced Day 3 for Day 5) → CR-4 (x: buy now at about $5.10, y: wait two days for $4.20) | A-8 |
| C-16 | drivers.corvane | quantity_traded (gasoline at Corvane stations, Days 5 to 95) | decrease | short | invisible | B | CR-5a (exchanges between drivers who would pay above the cap and sellers who would supply only above it are prevented) with C-4 | A-1, A-2, A-6 |
| C-17 | input_suppliers (in-state refiners) | net_price_received (rack price for Corvane blend) | decrease | short | invisible | B | C-2 → CR-9 (input_to) → CR-5c (stations' highest rack bid falls toward the cap less costs) → CR-7b (output with no other outlet bears the burden) | A-1, A-2, A-7 |
| C-18 | input_suppliers (cargo sellers) | quantity_supplied (cargoes delivered to Corvane) | decrease | short | invisible | B | C-17 → CR-7a (cargoes have other buyers; they go where the net yield is higher) | A-1, A-2, A-6 |
| C-19 | input_suppliers (in-state refiners) | quantity_supplied (pipeline shipments to Brennick) | increase | short | invisible | B | C-17 → CR-7a (the pipeline has spare capacity; barrels move to the uncapped market) | A-1, A-2, A-6 |
| C-20 | refinery owner (Port Aldis) | maintenance_spending (expediting the repair) | decrease | short | invisible | B | C-17 → CR-4 (x: pay overtime and expedited parts, y: repair at the normal pace; the return to output during the outage is capped) → CR-10 | A-1, A-2, A-9 |
| C-21 | input_suppliers (refiners and terminals) | inventory_held (last days before Day 95) | increase | short | invisible | B | CR-10a (cap expected to end on Day 95) → CR-4 (x: sell under the cap now, y: hold product to sell after Day 95) | A-1, A-13 |
| C-22 | stations | quantity_supplied (first days after Day 95) | increase | medium | invisible | B | C-21 → CR-10a (held product released once the cap ends) | A-1, A-13 |
| C-23 | neighboring_jurisdictions (Brennick drivers) | price_paid (Brennick gasoline) | ambiguous | short | invisible | B | (−) C-19 → CR-6 (more supply at the Brennick rack); (+ or −) C-13 (Corvane drivers' cross-border demand is itself ambiguous); CR-12b | A-1, A-6, A-11 |
| C-24 | sellers.complements (station convenience stores) | quantity_complement (in-store goods) | ambiguous | short | invisible | B | (−) C-4 and C-8 (fewer gallons, shorter hours) → CR-9; (+) per-car limits and searching mean more station visits per gallon → CR-9; CR-12b | A-4, A-12 |
| C-25 | stations | lobbying_effort | increase | short | invisible | B | CR-1 (op 1) → CR-4 (x: accept, y: lobby against extension or for relief) → CR-8c | A-1, A-N1 |
| C-26 | officials.enforcement | enforcement_cost | increase | short | invisible | A | CR-1 (op 2, K3) → CR-8c | none |
| C-27 | taxpayers | resources_available_other_uses | decrease | short | invisible | A | CR-1 (op 4, K3: emergency appropriation from the general fund) → CR-8a, CR-8b | none |

## Gaps found

**(a) Calculus gaps.** None. Every step was derived from a core rule. The most demanding step was carrying a retail cap back to an uncapped wholesale market: CR-5c (the stations' acceptable range moves) with CR-9 (input_to) and CR-7a/b sufficed.

**(b) New premises.**

- A-N1 (p 0.7): CR-4 (x: accept, y: lobby) needs someone at that margin.
- A-N2 (p 0.45, not reported): CR-7a needs output that can move between gasoline and diesel.
- A-N3 (p 0.45, not reported): CR-11c and CR-10a need an expectation that caps recur.

**(c) Unclear core rules.**

- CR-4 "mirror case" when one change makes an option better on one dimension and worse on another: the cap lowers the money price at Corvane stations but adds queues. Whether to treat this as "x made better" or "x made worse" depends on the full price, which is ambiguous; this is why cross-border buying is ambiguous. CR-4 does not say to use the full price.
- CR-6, "every margin that is still open": unclear whether each open margin (hours, card acceptance, per-car limits, favoritism) is predicted to be used, or at least one. Here each was given its own consequence on the strength of A-4; a group consequence would be the cautious reading.
- CR-12b refers to a dominance pattern (DM); no dominance was claimed here, so every conflict is reported ambiguous.
- CR-10a and timing-shift consequences: the normal form forbids duplicate (actor class, variable, horizon), but windows (Days 3 to 5, the days before and after Day 95) share the short horizon. They were separated by naming the window in the variable.

## Comparison with the pattern-based analysis

**Summary.** This is the case of closest agreement. Both versions derive the same chain from a retail cap with an uncapped rack price: drivers who fill up pay less and stations receive less; quantity demanded rises while supply into Corvane falls (cargoes diverted, pipeline barrels sent to Brennick, the in-state rack price pushed down where output has no other outlet, the repair not expedited); the gap shows up as queues, search, worse service, selection of customers and resale in cans with poor information; purchases dip before Day 5; cross-border buying and drivers' full cost are ambiguous for the same reason in both. The core rules carried the cap upstream (CR-5c, CR-9, CR-7a/b) without a pattern, matching PC-12. There is one sign difference: supply in the period after Day 95. The core version reports an increase from the release of held stock, but its own section 8 names the opposing chain (a repair slowed past Day 95 lowers output then) and it did not combine the two; the pattern version's ambiguous is right. The core version also omitted stations' delayed wholesale purchases before Day 5; the pattern version omitted the holding of stock before Day 95 as a consequence and enforcement cost.

Counts: M 18, V 4, S 1, OP 3, OC 1.

### Pattern version → core version

| Pattern ID | Matched core ID(s) | Class | Cause | Note |
| --- | --- | --- | --- | --- |
| C-1 | C-1 | M | | |
| C-2 | C-2 | M | | |
| C-3 | C-3 | M | | |
| C-4 | C-5 | M | | |
| C-5 | C-6 | M | | |
| C-6 | C-7 | M | | |
| C-7 | C-9 | M | | |
| C-8 | C-8 | M | | Recorded for drivers rather than stations; same claim. |
| C-9 | C-11 | M | | Recorded for intermediaries rather than drivers; same claim. |
| C-10 | C-4, C-18, C-19 | V | | Split into retail supply, cargoes and pipeline shipments to Brennick. |
| C-11 | C-17 | M | | |
| C-12 | C-15 | V | | Recorded as quantity_traded in the window rather than quantity_demanded. |
| C-13 | none | OC | E | Stations delay wholesale purchases from Day 3 to Day 5 (CR-10a with CR-4: rack stock bought at Day 3 prices must be sold at the cap). The core's CR-1 table lists the announcement for stations but derives only the drivers' shift. Core-version omission. |
| C-14 | C-20 | M | | |
| C-15 | C-25 | M | | |
| C-16 | C-14 | M | | |
| C-17 | C-13 | M | | Both ambiguous, same chains. |
| C-18 | C-24 | V | | Pattern splits stations by whether they have fuel (signs by construction; no claim on the total); core records the total, ambiguous. No conflict. |
| C-19 | C-24 | V | | As C-18. |
| C-20 | C-16 | M | | |
| C-21 | C-27 | M | | |
| C-22 | C-12 | M | | |
| C-23 | C-10 | M | | |
| C-24 | C-22 | S | E | Pattern ambiguous (held stock released against a repair slowed past Day 95); core increase. Pattern is right: the repair chain (C-20) reaches the same key whenever the repair would otherwise finish near Day 95, and the core's own section 8 says the slower repair can outlast the cap; CR-12b gives ambiguous. Core C-22's horizon (medium) is also inconsistent with its window (first days after Day 95). Error in the core version. |

### Core-only consequences

| Core ID | Class | Cause | Note |
| --- | --- | --- | --- |
| C-21 | OP | E | inventory_held increase in the last days before Day 95 (CR-10a). The pattern version uses this chain in section 7 and section 8 but did not record it as a consequence. |
| C-23 | OP | J | Brennick price ambiguous. The pattern version pruned it explicitly at depth 3; both defensible. |
| C-26 | OP | E | enforcement_cost increase (CR-8c); the pattern version records only the taxpayers' side (C-21). |

### Findings

- **Error in the core version (composition).** C-22 signs post-Day-95 supply an increase while leaving out the slowed-repair chain that the same version identifies in section 8; the sign should be ambiguous, as in the pattern version.
- **Error in the core version (omission).** Stations' wholesale purchases on Days 3 to 5 (pattern C-13).
- **Errors in the pattern version (omissions).** Holding stock before Day 95 (used as a chain but not recorded) and enforcement cost.
- **No pattern found wrong.** PC-12 (a ceiling passes up to the inputs) and PC-5 applied at a short horizon to movable cargoes were both reproduced from the core rules (CR-5c, CR-9, CR-7a/b), which supports their derivations.
- **Limit of the core rules.** None that produced a difference. The core version's note on CR-4's mirror case stands: when a policy improves an option on one dimension (money price) and worsens it on another (queues), CR-4 does not say to use the full price, which is why both versions leave cross-border buying ambiguous.
