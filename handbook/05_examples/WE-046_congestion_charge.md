# WE-046 Congestion charge for a central zone, with a residents' discount and a bus earmark

Analyst: draft (Handbook 0.9, held-out test)  |  Rule catalog version: 0.9  |  Status: awaiting expert review

A stylized policy in a fictional city. Several real cities charge drivers to enter a central zone; this one is not modeled on any of them. It is a held-out test of catalog 0.9 on a case none of the 0.9 changes were drawn from. It probes CR-12's 0.9 rule for a Tier C chain against a Tier B chain (road congestion is a `shared_facility`, so every chain through travel speeds is Tier C under CR-9 0.7, and it opposes Tier B chains on drivers' costs, shops' sales, property values and wages), CR-12's 0.9 note on what the response argument gives (vehicle numbers, where faster roads draw some drivers back), RS-9's 0.9 clause on location complements (shops inside the zone and just outside it), RS-16 and its 0.9 clause on a cost attached to the substitute itself (ride-hail cars pay the charge too), CR-6's 0.9 clauses on splitting a shift between price and quantity and on a public supplier that adds capacity only after a lag (buses), CR-7c capitalization inside the zone and at its edge, TX-1 and TX-2 incidence where the "seller" of road space is the city, CR-8d and SB-7 on an earmark with no maintenance-of-effort clause, and OC-3's 0.9 clause on a fixed budget together with its right-baseline clause. The unclear provision is whether delivery vans that enter and leave within 30 minutes pay. The counterfactual throughout is **Calderford without the charge**: the same roads, buses and parking, with traffic as it would otherwise have been. Effects on air quality, noise, road safety and health are outside the scope of version 1. The probabilities are illustrative; the evidence column says what a real analysis would cite.

## 1. Policy record

**Calderford Central Zone Charging Ordinance.** Calderford is a city of about 900,000. Its central zone, the area inside the Inner Ring Road, covers about 7 km² and has about 58,000 residents, 14,500 cars registered to zone addresses, 260,000 jobs and about 4,200 shops, cafés and restaurants. Just outside the Inner Ring lies Ringside, a band of about 1,100 shops and offices with three large parking garages, five to ten minutes' walk from the zone's edge. Beyond Ringside are the city's outer districts and, beyond the city line, the suburban town of Merrowdale with a regional shopping centre.

On an average weekday, about 118,000 vehicles are driven or parked in the zone between 7:00 and 19:00: about 92,000 cars (about 9,500 of them residents'), 19,000 goods vehicles (about 7,000 of which make a single visit lasting under 30 minutes), 4,000 taxis and ride-hail cars, and 3,000 buses and coaches. Average speed in the zone in charging hours is about 12 km/h. Of commuters to zone jobs, about 62% come by bus or tram, 22% by car and 16% on foot or by bicycle. A typical car commute ends with about 4 km inside the zone (about 20 minutes at 12 km/h); the same commute by bus takes about 15 minutes longer door to door. There are about 31,000 off-street parking spaces in the zone, at an average of $21 a day and about 90% weekday occupancy; the three Ringside garages have about 7,500 spaces at $9 a day and about 88% occupancy (about 900 spare). Calderford Transit runs about 850 buses and two tram lines, with fare revenue of about $180 million a year and general-fund support of about $140 million; peak load on routes into the zone is about 85% of capacity, and new buses take 14 to 18 months from order to service. Through traffic can go round the zone on the Inner Ring Road, which is itself busy at peak. Ride-hail fares are set by the platforms; there is no fare regulation.

The city's model projects that with the charge about 88,000 vehicles a day would be in the zone in charging hours, and the average speed would rise to about 15 km/h (saving about 4 minutes on the typical 4 km of a car commute).

The ordinance was adopted and published on 4 January 2027; charging starts on 1 November 2027 (ten months later). No expiry; the council must review the charge level every three years.

| Field | Value | Source sentence |
|---|---|---|
| Jurisdiction (and what lies just outside) | The zone inside the Inner Ring Road. Just outside: Ringside (shops, offices, garages), the Inner Ring Road itself, then the outer districts and Merrowdale. | §2: "The zone is the area bounded by, but not including, the Inner Ring Road." |
| Announced / enacted / effective / expires | Announced and enacted 4 January 2027; effective 1 November 2027; no expiry. | §1, §14. |
| Enforcement (who, penalties, resources) | The City Charging Office (CCO): cameras reading number plates at all 74 entry points and at 40 points inside the zone. Unpaid charge: penalty notice of $130 ($65 if paid within 14 days). Appeals against notices go to the existing Parking Adjudication Office (PAO). | §9 to §11. |

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Daily charge | `per_unit_tax` | A vehicle-day in the zone | Registered keeper of each vehicle driven or parked in the zone on a weekday between 7:00 and 19:00 | $15 per vehicle per day, payable by midnight the next day. One charge covers any number of entries that day. | Scheduled buses; emergency vehicles. |
| K2 Residents' discount | `per_unit_tax` (reduced rate) | Same | Registered keepers whose registered address is in the zone | 90% discount: $1.50 a day. Residence is taken from the vehicle register, which keepers update by declaration. | — |
| K3 Earmark | `revenue_use` | Net revenue of K1 and K2 | The city | "The net revenue of the charge, after the costs of the City Charging Office, shall be applied to bus services." No clause on the level of general-fund support for buses. | — |
| K4 Enforcement and administration | Enforcement | K1, K2 | CCO, funded from gross revenue (K3: "after the costs of the City Charging Office"); PAO, whose budget the ordinance does not change | About $45 million a year to run; about $70 million to set up, advanced from city reserves and repaid from the first year's revenue. | — |

Existing rules that stay in the counterfactual: Calderford Transit's fares and its general-fund support (set each year in the city budget); on-street parking rules and their enforcement in the zone (about $11 million a year); the PAO, which hears about 44,000 parking appeals a year, about 14,000 of them on zone tickets.

Unclear provision:
- **U1, short delivery visits.** §3(1): "The charge is payable for each day on which a vehicle is driven or parked in the zone during charging hours." §7: "A goods vehicle which enters and leaves the zone within thirty minutes in the course of a delivery shall be recorded as a short visit." The schedule of charges sets a single daily rate and nowhere refers to short visits. Reading U1-a: a short visit is recorded (the CCO's freight statistics) and pays the daily charge like any other day in the zone. Reading U1-b: a short visit is not a chargeable day; such vans pay nothing. The CCO has issued no guidance.

Readings get no probability; where a sign depends on U1, one sign per reading is given.

**Figures.** Static revenue (118,000 vehicles, 252 charging days): about $410 million from non-residents and $3.6 million from residents. Projected revenue (88,000 vehicles, of which about 8,000 residents'): about $303 million, less about $26 million under U1-b if the 7,000 short delivery visits do not pay. Net of the CCO's $45 million, about $230 million to $260 million a year is earmarked for buses, against $140 million of general-fund support now. For a typical car commuter, the charge is $15 a day and the time saved by faster roads is about 4 minutes each way inside the zone, about 8 minutes a day. For a multi-drop van covering about 40 km in the zone, the same speed change saves about 40 minutes a day. The PAO's workload: about 180,000 penalty notices a year are projected, about 5% appealed (about 9,000 appeals); fewer cars in the zone are projected to cut zone parking tickets by about a fifth (about 2,800 fewer appeals): a net rise of about 6,200 appeals a year, about 14%, with the same budget.

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | Rule families |
|---|---|---|---|
| K1 | Binary: a payment to the state attached to the option of driving in the zone on a weekday (CR-1, operation 3, charged per day rather than per entry). Road space in the zone is a `public_supply` at a price of zero in the counterfactual, rationed by congestion (CR-6, 0.7, public supply); K1 adds a money price. | Yes (A-1). | TX-1, TX-2, TX-9, RS-1, RS-3, RS-4, RS-5, RS-8, RS-9 (0.9), RS-12, RS-16 (0.9), CR-6 (0.9), CR-7c, CR-12 (0.9) |
| K2 | Binary: the same operation at a tenth of the rate, for a class defined by registered address. Against the counterfactual it is still a burden, not a subsidy; it draws a line at the zone boundary. | Yes, for residents who drive in the zone (A-1). | RS-5, RS-11, CR-7c |
| K3 | Binary: the use of the revenue; funds an existing public supplier whose budget is set each year. | Yes | SB-7, CR-8d, CR-6 (0.9, a public supplier that adds capacity after a lag), RS-13, RS-16 Unless |
| K4 | Binary: administration funded from the policy's own revenue (CCO) and from an unchanged budget (PAO). | Yes | OC-3 (own revenue; 0.9 fixed budget; right baseline) |

The roads of the zone are a facility every driver, van and bus shares: one vehicle fewer speeds every other vehicle. That is a `shared_facility` relation (02_ontology.md, 2.8), not an exchange. Under CR-9's 0.7 clarification every chain through travel speeds is Tier C, pending Q20. Where such a chain opposes a Tier B chain on the same key, CR-12's 0.9 rule applies: the Tier B sign is reported, qualified "not counting effects through the roads", and the combined sign is reported separately at Tier C.

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `drivers.nonresident` (`buyers.current` of road space) | Drivers of cars into the zone who do not live there: commuters, shoppers, visitors | A weekday in the zone costs $15 more. Split by response (CR-1, 0.7): `drivers.keep` (keep driving in), `drivers.switch` (switch to bus, tram, ride-hail or Ringside parking), `drivers.retime` (move trips to evenings or weekends), `drivers.through` (cross the zone without stopping; may go round it) and `drivers.stop` (stop coming). |
| `residents.zone` | Zone residents who drive in the zone on weekdays | Pay $1.50 a day; would pay $15 if they moved out and kept driving in. |
| `goods_vehicle_operators` | Carriers and own-account suppliers delivering into the zone | Pay $15 per van-day; under U1-b, not for visits under 30 minutes. |
| `businesses.zone` | Shops, cafés, restaurants and services in the zone | Customers who drove in face the charge; deliveries cost more; streets are less congested (Tier C). |
| `businesses.edge` | Shops and services in Ringside | Customers who park outside the zone and shoppers who stop short of it pass their doors. |
| `owners.zone_commercial`, `owners.zone_residential`, `owners.edge_commercial` (`factor_owners.specific`) | Owners of property in the zone and in Ringside at the time the charge became expected | Values capitalize the change in expected yields (CR-7c). |
| `owners.parking.zone`, `owners.parking.edge` | Owners of garages in the zone and in Ringside | Demand for parking in the zone falls (complement of driving in); demand in Ringside rises (substitute). |
| `bus_riders` | Existing riders of buses and trams into the zone | New riders join; service may expand from the earmark; buses run faster (Tier C). |
| `transit_operator` | Calderford Transit | Receives the earmark; general-fund support may fall. |
| `ride_hail_drivers` (`sellers.substitutes`) | Ride-hail and taxi drivers | More riders; each car pays $15 a day in the zone. |
| `employers.zone`, `workers.zone` | Employers in the zone and their staff who commute by car | The cost of reaching a zone job by car rises. |
| `ring_road_users` | Drivers on the Inner Ring Road | Through traffic diverted round the zone joins them (Tier C). |
| `shoppers` | Buyers who drove into the zone to shop | May shop in Ringside or at Merrowdale instead. |
| `officials.enforcement` | The City Charging Office | Collects the charge, runs cameras, issues penalty notices. |
| `officials.adjudication`, `parking_appellants` | The Parking Adjudication Office and those who appeal parking tickets | New appeals against penalty notices; fewer zone parking tickets. |
| `taxpayers`, recipients of other city spending | Funders and beneficiaries of the general fund | General-fund support for buses may fall (SB-7). |
| `input_suppliers` | Sellers of cameras, payment systems and buses | New orders. |
| `lobbying groups` | Zone retailers, delivery firms, Ringside residents, the transit union | Concentrated stakes in the charge level, exemptions and U1. |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | `drivers.nonresident` | `price_paid` (money cost of a weekday in the zone by car) | increase | short (from 1 November 2027) | CR-1, TX-2 | A-2 |
| C-2 | `residents.zone` | `price_paid` (money cost of a weekday driving in the zone, at the discount) | increase | short | CR-1, TX-2 | A-2 |
| C-3 | `officials.enforcement` | `tax_revenue` (charge) | increase | short | TX-1 | none |
| C-4 | `drivers.nonresident`, `goods_vehicle_operators` | `quantity_traded` (vehicle-days in the zone, weekdays 7:00 to 19:00; not counting effects through the roads) | decrease | short to medium | CR-4c, TX-2, CR-12 (0.9) | A-1, A-2 |
| C-5 | `drivers.keep`, `goods_vehicle_operators`, `bus_riders` | `travel_time` (per km in the zone in charging hours) | decrease | short to medium | CR-9 (`shared_facility`; Tier C), CR-6 (0.7, public supply) | A-1, A-2, A-3 |
| C-6 | `drivers.nonresident`, `goods_vehicle_operators` | `quantity_traded` (vehicle-days in the zone, weekdays 7:00 to 19:00) | decrease | short to medium | CR-9 (`shared_facility`; Tier C), CR-12e (response argument), CR-12 (0.9: what the response argument gives) | A-1, A-2, A-3 |

C-1 to C-4 are what the ordinance's supporters expect: drivers pay, the city collects, fewer vehicles enter. The residents' discount does not make residents better off against the counterfactual: they pay $1.50 a day where they paid nothing (C-2). K1 is a charge per day, not per entry, so it bears on whether a vehicle is in the zone on a given day; a driver already in the zone pays nothing more for further trips that day (CR-4, units).

**Road space has no seller (TX-2).** TX-2 gives `price_paid` up and/or `net_price_received` down, with the split decided by the two sides' alternatives (DM-1). Here the "seller" of road space is the city, which supplies a fixed quantity whatever the price: there is no seller whose net price can fall. So the charge is borne in the first instance by those who keep driving (C-1, C-2), and its further burden travels along the relations of the trips it prices: to businesses whose customers or deliveries it reaches (C-27, C-46) and, through CR-7b, to the immobile means in the zone (C-33). This is TX-2 read for a public supply at a zero price (Gaps found, c1).

**Fewer vehicles, and faster roads (C-4 to C-6).** Without the charge, road space in the zone is rationed by congestion: the time cost rises until the drivers who still enter value the trip at least at its time cost (CR-6, 0.7, public supply). The charge attaches $15 to the option of a weekday in the zone; those for whom the trip was worth less than $15 more than its other costs switch, retime or stop (CR-4b; A-1). That is C-4 at Tier B. With fewer vehicles, the rest move faster (C-5): one vehicle's use of the road changes the time cost to every other user, which is the `shared_facility` relation, so C-5 is Tier C. Faster roads draw some drivers back (a lower time cost on the option of driving in). That chain opposes C-4, and it runs over the shared facility, so CR-12's 0.9 rule applies: C-4 stands at Tier B, qualified "not counting effects through the roads", and the combined sign is recorded at Tier C (C-6). The combined sign is decided by CR-12e's response argument: the drivers drawn back respond to a speed gain that exists only because drivers left in response to the charge; if the number of vehicle-days returned to its old level, so would the speed, and every driver would face the old time cost plus $15, so the number would fall again. The response cannot reverse its cause. By CR-12's 0.9 note, that alone gives "a decrease or no change"; to report `decrease`, the response must be partial. A-1 supplies that: at the old time cost, some drivers value a weekday in the zone by less than $15 more than its other costs. The Tier C chain does not lower the tier of C-4, and C-6 is Tier C because its chain runs over the roads.

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-7 | `drivers.switch` | `quantity_substitute` (bus and tram trips into the zone) | increase | short to medium | RS-1, CR-6 (0.7, public supply) | A-5 |
| C-8 | `drivers.switch` | `quantity_substitute` (day parking in Ringside garages) | increase | short | RS-1, RS-16, CR-6 (0.9: splitting a shift) | A-5, A-6 |
| C-9 | `owners.parking.edge` (`sellers.substitutes`) | `price_substitute` (Ringside garage day rate) | increase | short to medium | RS-16, CR-6 (0.9: splitting a shift) | A-5, A-6 |
| C-10 | `drivers.switch` | `quantity_substitute` (ride-hail and taxi trips into the zone) | increase | short | RS-1 | A-25 |
| C-11 | `ride_hail_drivers` | `price_substitute` (ride-hail fares for trips into the zone) | increase | short | RS-16 (0.9: costs on the substitute), CR-6, CR-12a | A-25, A-26 |
| C-12 | `ride_hail_drivers` | `net_price_received` (per trip into the zone, after the charge) | ambiguous | short | RS-16 (0.9: costs on the substitute), CR-12b | A-25, A-26 |
| C-13 | `drivers.retime` | `quantity_traded` (car trips into the zone on weekdays before 7:00 and after 19:00) | increase | short to medium | RS-8, CR-10a, CR-4 | A-17 |
| C-14 | `drivers.retime` (shopping and personal trips) | `quantity_traded` (car trips into the zone at weekends) | increase | short to medium | RS-8, CR-4 | A-17 |
| C-15 | `drivers.through` | `travel_time` (through trips diverted round the zone) | increase | short | CR-4 (x: cross the zone and pay, y: go round), CR-3a | A-18 |
| C-16 | `ring_road_users` | `travel_time` (on the Inner Ring Road) | increase | short to medium | CR-9 (`shared_facility`; Tier C) | A-3, A-18 |
| C-17 | `drivers.nonresident` | `reclassification` (vehicles registered to zone addresses to claim the discount) | increase | short to medium | RS-5 | A-11 |
| C-18 | `drivers.nonresident`, `goods_vehicle_operators` | `legal_breach` (unpaid charges; false, cloned or obscured plates) | increase | short | RS-3, CR-4 (x: pay, y: evade) | A-16 |
| C-19 | `lobbying groups` | `lobbying_effort` (retailers for a lower charge or shoppers' exemption; delivery firms on U1; Ringside residents for the discount; the transit union to keep the earmark) | increase | short to medium | RS-7 | A-15 |
| C-20 | `residents.zone` | `turnover` (moves out of the zone by residents who drive in it) | decrease | medium | RS-11, CR-3 | A-22 |
| C-21 | `goods_vehicle_operators` | `reclassification` (routes reshaped into visits of under 30 minutes) | U1-a: no_change; U1-b: increase | short to medium | RS-5, CR-1 | A-13 |
| C-22 | `goods_vehicle_operators` | `quantity_traded` (delivery visits into the zone lasting under 30 minutes) | U1-a: decrease; U1-b: increase | short to medium | CR-4, RS-5 | A-1, A-13 |
| C-23 | `goods_vehicle_operators` | `compliance_cost` (records proving that a visit was a delivery under 30 minutes) | U1-a: no_change; U1-b: increase | short | CR-8c, OC-2 | A-13 |
| C-24 | `goods_vehicle_operators` | `legal_breach` (false short-visit claims by vehicles not delivering) | U1-a: no_change; U1-b: increase | short | RS-3 | A-13, A-16 |
| C-25 | `businesses.zone` (retailers whose customers mostly drive: furniture, hardware, bulky goods) | `number_of_sellers` (in the zone) | decrease | medium | RS-4, RS-6, CR-7a | A-7, A-20 |
| C-26 | `shoppers` | `cross_border_purchases` (purchases made outside the zone, in Ringside or Merrowdale, by former car shoppers) | increase | short to medium | RS-4, RS-9 | A-7 |

**Substitutes (C-7 to C-12).** RS-1 gives the direction of each switch; CR-4 gives only that more buyers turn to the substitute, and a traded quantity or a price needs a premise on the substitute's supply (RS-1; RS-16; CR-6, 0.9). Buses and trams run to a fixed schedule at a set fare: the riders drawn from cars are carried while there is room, and beyond that the pressure goes to crowding (CR-6, 0.7, public supply; C-38). Ringside's garages have about 900 spare spaces against the several thousand drivers the city model expects to park outside the zone: the quantity rises until the garages are full (C-8), and beyond that the shift goes to price (C-9). By CR-6's 0.9 clause, the split between price and quantity is signed only with a premise on supply: A-6 (garages cannot be added within a year). For ride-hail, RS-16's 0.9 clause applies: the policy attaches a cost to the substitute itself, since each ride-hail car pays $15 for a day in the zone. On the fare (C-11) both chains push up: more riders (where supply cannot expand at an unchanged cost at peak, A-26) and a higher cost per car-day. On drivers' net price per trip (C-12) they oppose: more demand (+) against the charge, spread over the day's trips (−); no premise ranks them, so `ambiguous` (CR-12b).

**Timing (C-13, C-14).** A trip into the zone happens with and without the charge, at different times. Trips that can be moved go to the free windows: weekday evenings and early mornings (C-13) and weekends (C-14). Each window is signed against the counterfactual (02_ontology.md, 2.5); the weekday 7:00 to 19:00 window is C-4. These are flows (trips in each window), not stocks (CR-12, 0.9).

**Through traffic and the ring road (C-15, C-16).** A driver who crossed the zone without stopping now pays $15 to do so, or goes round on the Inner Ring Road, which takes longer (C-15; CR-4, CR-3a: the chosen alternative was ranked lower before). Diverted traffic slows the ring road for everyone on it (C-16): `shared_facility`, Tier C. Both push C-15 the same way, so no combination is needed.

**The discount draws registrations (C-17).** The residents' discount depends on the registered address, which keepers update by declaration. Non-residents who can name a zone address (a relative's flat, a business address) save $13.50 a day by doing so (RS-5; A-11). Penalties for false registration exist but checks are by audit.

**Evasion (C-18).** Foreign plates, cloned plates and obscured plates escape the cameras; some drivers risk the penalty (RS-3; A-16). The trade itself stays in a legal activity, so it is `legal_breach`.

**Lock-in (C-20).** A resident who drives in the zone and moves out would pay $15 instead of $1.50 for each weekday in the zone. Moving now costs that difference too (CR-3), so some residents who would have moved stay (RS-11; A-22).

**Deliveries and U1 (C-21 to C-24).** The charge is per day, so a van making twenty drops pays the same as one making one. Under U1-a, a supplier making a single short drop pays $15 for it; some such visits are given up, consolidated onto carriers' multi-drop rounds, or moved to before 7:00 (C-22, U1-a: decrease; A-1). Under U1-b, short visits are free, while a van that stays longer pays for the day; operators reshape long rounds into several in-and-out loops of under 30 minutes where the layout allows (C-21; A-13), so short visits rise against the counterfactual (C-22, U1-b: increase). Proving that a visit was a delivery and lasted under 30 minutes needs records (C-23), and other vehicles may claim the status falsely (C-24). Under U1-a none of this exists.

**Relocation (C-25, C-26).** Shoppers who drove in to buy bulky goods can buy them in Ringside or at Merrowdale, where they can park (RS-4). Retailers that depend on such customers move out of the zone as their leases end (C-25; RS-6, CR-7a; A-7). Where they reopen in Ringside, the activity is new to Ringside and lost to the zone (OC-5, 0.9: new to the place).

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-27 | `businesses.zone` | `quantity_traded` (sales to customers who drove into the zone; not counting effects through the roads) | decrease | short to medium | RS-9 (0.9: location complements), CR-9 | purchases at zone shops: `complement` (note `location`) to being in the zone | A-1, A-7 |
| C-28 | `businesses.zone` | `quantity_traded` (all sales; not counting effects through the roads) | ambiguous | medium | RS-9 (0.9: new occupants), CR-12b | as C-27; buses: `complement` to reaching the zone | A-1, A-7, A-8, A-10 |
| C-29 | `businesses.edge` | `quantity_traded` (sales; not counting effects through the roads) | increase | short to medium | RS-9 (0.9), RS-4, CR-9 | purchases in Ringside: `complement` (note `location`) to parking there | A-7 |
| C-30 | `businesses.edge` | `quantity_traded` (sales) | ambiguous | short to medium | RS-9, CR-9 (`shared_facility`; Tier C), CR-12 (0.9) | as C-29; Inner Ring Road: `shared_facility` | A-3, A-7, A-18 |
| C-31 | `owners.edge_commercial` | `asset_value` (Ringside shops and offices; not counting effects through the roads) | increase | short (from 4 January 2027) | CR-7c, CR-10c, SB-4 | follows C-29 | A-7, A-20 |
| C-32 | `owners.edge_commercial` | `asset_value` (Ringside shops and offices) | ambiguous | short | CR-7c, CR-9 (`shared_facility`; Tier C), CR-12 (0.9) | as C-30 | A-3, A-7, A-18, A-20 |
| C-33 | `owners.zone_commercial` | `asset_value` (zone shops and offices; not counting effects through the roads) | ambiguous | short | CR-7b, CR-7c, CR-10c, CR-12b | follows C-28, C-46 | A-7, A-8, A-10, A-20 |
| C-34 | `owners.zone_residential` | `asset_value` (zone housing; not counting effects through the roads) | ambiguous | short | CR-7c, CR-10c, CR-6 (0.9: splitting a shift), CR-12b | zone housing and outer housing: `substitute` | A-2, A-8, A-20, A-27 |
| C-35 | `owners.parking.zone` | `price_complement` (zone garage day rate) | decrease | short to medium | RS-12, CR-6 (0.9: splitting a shift) | zone parking: `complement` to driving in | A-1, A-21 |
| C-36 | `owners.parking.zone` | `asset_value` (zone garages) | decrease | short | CR-7c, CR-10c, SB-4 | as C-35 | A-1, A-20, A-21 |
| C-37 | `owners.parking.edge` | `asset_value` (Ringside garages) | increase | short | CR-7c, CR-10c, SB-4 | follows C-9 | A-6, A-20 |
| C-38 | `bus_riders` | `quality_per_unit` (crowding on routes into the zone, before new buses arrive) | decrease | short | CR-6 (0.7, public supply; 0.9, capacity after a lag), PC-19 | buses and cars: `substitute` | A-5, A-28 |
| C-39 | `bus_riders` | `quality_per_unit` (crowding, after new buses arrive) | ambiguous | medium | RS-16 (Unless), RS-13, SB-7, CR-12b | as C-38 | A-5, A-8 |
| C-40 | `bus_riders` | `wait_time` (headways) | decrease | medium | SB-7, CR-8d | earmark funds service | A-8 |
| C-41 | `bus_riders` | `travel_time` (bus journeys in the zone) | decrease | short to medium | CR-9 (`shared_facility`; Tier C) | roads: `shared_facility` | A-1, A-3 |
| C-42 | `transit_operator` | `quantity_supplied` (bus service-km) | increase | medium | SB-7, CR-8d | earmark | A-8 |
| C-43 | `taxpayers`, recipients of other city spending | `resources_available_other_uses` | at_least_one_increase | medium | SB-7, CR-8d, CR-8b | general fund | A-9 |
| C-44 | `goods_vehicle_operators` | `full_cost_per_unit` (a van-day in the zone: charge plus time; not counting effects through the roads) | U1-a: increase; U1-b: increase | short to medium | CR-1, CR-3, CR-12 (0.9) | — | A-2, A-12 |
| C-45 | `goods_vehicle_operators` | `full_cost_per_unit` (a van-day in the zone: charge plus time) | U1-a: ambiguous; U1-b: ambiguous | short to medium | CR-9 (`shared_facility`; Tier C), CR-12b, CR-12 (0.9) | roads: `shared_facility` | A-2, A-3, A-12 |
| C-46 | `businesses.zone` | `price_paid` (deliveries; not counting effects through the roads) | U1-a: increase; U1-b: increase | short to medium | RS-14, CR-7b, DM-1 | deliveries `input_to` zone businesses | A-2, A-12, A-14 |
| C-47 | `businesses.zone` | `tax_share_borne` (charge on deliveries, against carriers) | U1-a: increase; U1-b: increase | medium | DM-1, CR-7b | as C-46 | A-12, A-14 |
| C-48 | `drivers.keep` | `full_cost_per_unit` (a weekday in the zone by car: charge plus time; not counting effects through the roads) | increase | short to medium | CR-1, CR-3, CR-12 (0.9) | — | A-2 |
| C-49 | `drivers.keep` | `full_cost_per_unit` (a weekday in the zone by car: charge plus time) | increase | short to medium | CR-9 (`shared_facility`; Tier C), CR-12 (0.9), CR-12e (dominance, A-4) | roads: `shared_facility` | A-2, A-3, A-4 |
| C-50 | `drivers.switch` | `travel_time` (door to door, by bus or by parking in Ringside and walking; not counting effects through the roads) | increase | short to medium | CR-3a, CR-4 | — | A-5, A-23 |
| C-51 | `drivers.switch` | `travel_time` (door to door) | increase | short to medium | CR-9 (`shared_facility`; Tier C), CR-12 (0.9), CR-12e (dominance, A-29) | roads: `shared_facility` | A-3, A-5, A-23, A-29 |
| C-52 | `employers.zone`, `workers.zone` | `wage_rate` (zone jobs reached by car) (+), `employment` (zone) (−); not counting effects through the roads | at_least_one_as_stated | medium | CR-5c, CR-7a, CR-12 (0.9) | labor: workers choose between zone jobs and jobs elsewhere | A-19 |
| C-53 | `employers.zone`, `workers.zone` | `wage_rate` (zone jobs reached by car), `employment` (zone) | ambiguous | medium | CR-9 (`shared_facility`; Tier C), CR-12b, CR-12 (0.9) | as C-52; roads: `shared_facility` | A-3, A-19 |
| C-54 | `input_suppliers` | `quantity_traded` (cameras and payment systems; later, buses) | increase | short to medium | CR-9, SB-7 | `input_to` K4 and to bus service | A-8 |

**Shops inside and outside the zone (RS-9, 0.9; C-25 to C-30).** Purchases made while in the zone are tied to being there: a shopper who no longer drives in buys where she now parks or goes instead (RS-9, location complements). So sales to customers who drove in fall in the zone (C-27) and rise in Ringside (C-29), and some go to Merrowdale (C-26). RS-9's 0.9 clause adds: when a policy changes who occupies the location, record the new occupants' purchases as the opposing chain. Here the charge changes who is in the zone in two ways. Through the earmark, more frequent buses bring people who would not otherwise have come (A-8, A-10): a Tier B chain. Through the roads, quieter and faster streets attract some visitors who avoided the congestion (Tier C). With the bus chain at p ≥ 0.5, the zone's total sales are `ambiguous` at Tier B (C-28; CR-12b; CR-12 0.8, kind 2). A premise that the loss of car shoppers dominates (A-30, p = 0.4) is below the cut-off. Counting the roads, the combined sign is still ambiguous (CR-12, kind 3), so it is not recorded again. For Ringside (C-29), the Tier B chain is a clean increase; the Tier C chain opposes it: traffic diverted round the zone slows the Inner Ring Road on which Ringside's customers arrive (C-16). Under CR-12's 0.9 rule C-29 stands at Tier B, qualified, and the combined sign at Tier C is `ambiguous` (C-30), since no premise compares the two.

**Property values (CR-7c; C-31 to C-37).** Each value moves when the charge becomes expected, on 4 January 2027 (CR-7c, CR-10c; A-20); owners then capture the gain or bear the loss, and later buyers pay the new price.
- *Ringside commercial (C-31, C-32).* Its sales rise at Tier B (C-29), so its value rises at Tier B (C-31). The ring road chain opposes it at Tier C, so the combined Tier C sign is `ambiguous` (C-32).
- *Zone commercial (C-33).* The yield of a zone shop falls with sales to car shoppers (C-27) and rises with new bus-borne visitors (C-28's (+) chain). The share of the charge that shoppers and deliveries pass back to zone businesses settles, as far as businesses can move, on the immobile means: the buildings (CR-7b). No premise ranks the chains: `ambiguous`.
- *Zone housing (C-34).* Three chains. Residents who drive in the zone pay $1.50 a day and their visitors and tradespeople pay $15 (−). Car commuters to zone jobs compare living in the zone ($1.50 a day) with living outside and driving in ($15); against the counterfactual, where both cost nothing, the zone gains relative to outside, and some of them would move in (A-27) (+). More frequent buses (A-8) raise the value of every address near a route, in the zone and outside (+, for the zone). With the housing stock fixed in the short run, the demand shift goes to price (CR-6, 0.9). The chains oppose: `ambiguous`. Quieter streets (Tier C) do not change that (kind 3).
- *Parking (C-35 to C-37).* Parking in the zone is a complement of driving in (RS-12): demand falls, and with the stock fixed (A-21) the day rate falls (C-35, CR-6 0.9) and so does the garages' value (C-36). C-6 shows that the number of vehicle-days falls at Tier C too, so no opposing chain reaches C-35. Ringside garages gain (C-37).

**Buses (C-38 to C-42).** Buses are a public supply at a set fare: riders drawn from cars share a fixed capacity, and the pressure goes to crowding (CR-6, 0.7). The earmark lets Calderford Transit add buses, but only after 14 to 18 months (A-28). CR-6's 0.9 clause on a public seller that adds capacity from its fees after a lag says the public-supply clause applies until the capacity arrives: in the first year crowding worsens for existing riders (C-38). Once new buses arrive, RS-16's Unless clause applies: the policy adds supply to the substitute's market (RS-13), so crowding is `ambiguous` (C-39). Headways shorten as service grows (C-40), on A-8. Faster roads speed the buses (C-41, Tier C); no Tier B chain opposes it. The new riders join existing ones; the riders themselves are better off by their own ranking only as far as the switch was their best remaining option (CR-3a: those who switched were made worse off, C-50).

**The earmark (CR-8d, SB-7; C-42, C-43).** The ordinance applies net revenue "to bus services" and says nothing about general-fund support, which is set each year. Money is fungible (CR-8d): the council can reduce the $140 million of general-fund support as the earmark arrives, so bus spending rises by less than the earmark, and the rest funds other spending or lower taxes (SB-7; A-9, p = 0.7). Service still rises if the reduction is less than the earmark (A-8, p = 0.7). The freed general funds reach a group: taxpayers, or recipients of other city spending (C-43, `at_least_one_increase`; CR-8, 0.7, payers from the general budget, in reverse). The CCO's costs come out of gross revenue first (K3), so they reduce what the earmark does (OC-3, own revenue; C-57).

**Deliveries (C-44 to C-47).** A van-day in the zone costs $15 more (C-44 at Tier B; under U1-b only for vans that stay over 30 minutes, A-12: some deliveries cannot be done in 30 minutes). Through the roads, a van covering 40 km in the zone saves about 40 minutes a day, worth more than $15 at a driver's and van's hourly cost; a van making one short drop saves almost nothing. So the combined sign at Tier C is `ambiguous` under both readings (C-45): there is no dominance premise either way across the class. CR-12e's response argument does not decide C-45: the speed gain comes from cars leaving, which is a response to the charge on cars, not to the charge on vans; for vans it is a second change (CR-12e, 0.8). Zone businesses buy deliveries: carriers can serve customers anywhere in the city, while a zone business cannot move its premises cheaply (A-14), so carriers pass more of the charge on and zone businesses bear more of it than carriers do (C-46, C-47; DM-1, CR-7b). The Tier C chain reaches C-46 through the carriers' costs: the combined sign at Tier C is `ambiguous` (kind 3 through C-45) and is not recorded again.

**Drivers who keep driving (C-48, C-49).** A weekday in the zone costs $15 more in money (C-48, Tier B). Through the roads, the same day takes less time. For a typical car commute the saving is about 8 minutes a day, worth much less than $15 for most drivers (A-4, p = 0.8: arithmetic on the case's figures and a premise on the value drivers place on time). That premise dominates the Tier C chain, so the combined sign at Tier C is also `increase` (C-49; CR-12e, dominance). Some drivers who value their time highly gain on balance; A-4 is about the class. The response argument would not give C-49: it binds the number of vehicles as a whole (C-6), not each driver's cost (CR-12e, 0.8).

**Drivers who switch (C-50, C-51).** A driver who switches to the bus or to Ringside parking took an option ranked below driving before the charge (CR-3a), and for most such trips it takes longer (A-23: the bus commute is about 15 minutes longer). Faster roads shorten the bus trip by a few minutes (Tier C). A-29 (the gap exceeds the saving) dominates that chain, so C-51 at Tier C is `increase` too.

**Zone jobs (C-52, C-53).** A zone job reached by car now costs its holder $15 a day more to reach; workers compare zone jobs with jobs elsewhere (CR-7a), so the terms on which zone employers can hire car commuters move against them (CR-5c): they pay more, or employ fewer, as a mixed group (C-52; A-19). This is the move of the candidate pattern "compensating differential from a non-wage term" (06_gaps.md, 6.2e; Gaps found, e). Through the roads, the remaining commute is faster by car and by bus, which lowers the cost of reaching zone jobs (Tier C). No premise compares the two for the class, so the combined Tier C sign is `ambiguous` (C-53).

Stopping points. The suppliers of zone and Ringside shops, the spending of workers whose hours change, Merrowdale's own traffic and the suppliers of new buses beyond the first order: depth 3 to 4, diffuse; stopped. Air quality, noise and road safety: out of scope.

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `drivers.nonresident`, `goods_vehicle_operators`, `quantity_traded` (vehicle-days in the zone, weekdays 7:00 to 19:00), short to medium | Faster roads draw some drivers back (Tier C). | The charge (CR-4b; A-1). | CR-12e, response argument: the return is a response to a speed gain that the leaving drivers caused and cannot restore the old number; A-1 makes the response partial (CR-12, 0.9). | Tier B: **decrease** (C-4). Tier C: **decrease** (C-6). |
| `drivers.keep`, `full_cost_per_unit`, short to medium | — | The charge (+ to cost); faster roads (− to cost, Tier C). | A-4 (arithmetic on the case's figures, with a premise on drivers' value of time). | Tier B: **increase** (C-48). Tier C: **increase** (C-49). |
| `goods_vehicle_operators`, `full_cost_per_unit`, short to medium | The charge (under U1-b, for vans staying over 30 minutes; A-12). | Faster roads (Tier C), large for multi-drop vans. | None: the saving exceeds $15 for some vans and is near zero for others. Response argument not applicable (the speed gain is a second change for vans). | Tier B: U1-a **increase**, U1-b **increase** (C-44). Tier C: **ambiguous** under both readings (C-45). |
| `drivers.switch`, `travel_time`, short to medium | Bus or walk is slower door to door (A-23). | Faster buses (Tier C). | A-29 (the gap far exceeds the saving). | Tier B: **increase** (C-50). Tier C: **increase** (C-51). |
| `businesses.zone`, `quantity_traded` (all sales), medium | New bus-borne visitors (A-8, A-10); visitors drawn by quieter streets (Tier C). | Car shoppers who buy elsewhere (C-27). | None (A-30, p = 0.4, below the cut-off). | Tier B: **ambiguous** (C-28). Tier C: ambiguous (kind 3), not recorded again. |
| `businesses.edge`, `quantity_traded`, short to medium | Shoppers who park in Ringside (C-29). | Slower Inner Ring Road (Tier C, C-16). | None | Tier B: **increase** (C-29). Tier C: **ambiguous** (C-30). |
| `owners.edge_commercial`, `asset_value`, short | Follows C-29. | Follows C-16 (Tier C). | None | Tier B: **increase** (C-31). Tier C: **ambiguous** (C-32). |
| `owners.zone_commercial`, `asset_value`, short | New bus-borne visitors. | Lost car shoppers; delivery costs borne by businesses (C-46, C-47). | None | **ambiguous** (C-33). |
| `owners.zone_residential`, `asset_value`, short | Car commuters moving in (A-27); more buses (A-8). | Residents' $1.50; visitors' and tradespeople's $15. | None | **ambiguous** (C-34). |
| `bus_riders`, `quality_per_unit` (crowding), short | — | New riders on a fixed fleet (A-28). | None needed | **decrease** (C-38). |
| `bus_riders`, `quality_per_unit` (crowding), medium | New buses from the earmark (A-8). | New riders. | None | **ambiguous** (C-39). |
| `ride_hail_drivers`, `price_substitute`, short | More riders (A-25, A-26); the charge per car-day. | — | None needed | **increase** (C-11). |
| `ride_hail_drivers`, `net_price_received`, short | More riders. | The charge per car-day. | None | **ambiguous** (C-12). |
| `employers.zone`, `workers.zone`, `wage_rate`/`employment`, medium | Faster commutes (Tier C) lower the cost of reaching zone jobs. | The charge raises it. | None | Tier B: **at_least_one_as_stated** (C-52). Tier C: **ambiguous** (C-53). |
| `officials.adjudication`, workload, short to medium | Appeals against penalty notices (about 9,000). | Fewer zone parking tickets (about 2,800 fewer appeals). | Arithmetic on the case's figures (A-24). | Net rise in work on an unchanged budget: **at_least_one_as_stated** (C-58). |

The charge and the earmark are recorded on both sides: drivers pay (C-1, C-2, C-55), the city receives (C-3), the CCO's costs come out of the receipts (C-57), and the net revenue funds buses (C-42) and, through fungibility, other spending or lower taxes (C-43).

## 8. Time structure

- **4 January to 31 October 2027: expectation.** Property and garage values move at once (C-31, C-33, C-34, C-36, C-37). Driver-dependent retailers whose leases end in 2027 begin to move to Ringside or close (C-25); delivery firms reorganize rounds, more so under U1-b (C-21). No rush to drive in the zone before November: a trip cannot be stored, and the charge applies per day from 1 November. Address re-registrations for the discount begin before charging starts (C-17).
- **November 2027 to end 2028: first year.** Vehicle-days fall at once (C-4, C-6) and speeds rise (C-5). Drivers move to buses, Ringside garages, ride-hail and other hours (C-7 to C-14); these responses grow over months as routines change (TS-8). Buses are crowded (C-38) and Ringside garages fill and raise their rates (C-8, C-9). The PAO's queue lengthens (C-58).
- **2029 onward.** New buses arrive from the earmark (C-40, C-42), turning crowding from worse to ambiguous (C-39). General-fund support is set at each budget (A-9). Retail relocation continues as leases turn over (C-25, TS-1). The charge is fixed at $15 in money and reviewed every three years; as prices and incomes rise, it binds less unless raised (TS-3).

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-55 | `drivers.keep`, `residents.zone`, `goods_vehicle_operators` (those who keep paying) | `resources_available_other_uses` (money) | decrease | What the $15 (or $1.50) a day would otherwise have bought or saved. Only those who keep paying are counted (CR-3, note); those who switch are worse off by their own ranking (C-50) but may spend more elsewhere. | TX-1, OC-1, CR-3 |
| C-56 | `drivers.nonresident`, `residents.zone`, `goods_vehicle_operators` | `compliance_cost` (accounts, payments, penalty disputes) | increase | Time spent registering, paying and disputing. | OC-2, TX-5, CR-8c |
| C-57 | `officials.enforcement` (CCO) | `enforcement_cost` | increase | About $45 million a year, and $70 million to set up, paid from gross revenue before the earmark: buses get that much less. | OC-3, CR-8c, CR-8d |
| C-58 | `officials.adjudication`, `parking_appellants` | `wait_time` (decisions on other parking appeals) (+), `enforcement_cost` (time per other appeal) (−) | at_least_one_as_stated | The PAO's other work: its budget is unchanged and its caseload rises about 14% net. | OC-3 (0.9: fixed budget; right baseline), CR-8a |
| C-59 | `officials.enforcement` | `tax_revenue_vs_static_projection` | decrease | Revenue is about $303 million against a static $414 million. | TX-9 |

**OC-3, three ways.** The CCO is funded from the policy's own revenue (K3: net revenue goes to buses after the CCO's costs), so its cost reduces what the earmark buys (C-57; OC-3, own revenue; CR-8d), not general taxpayers' means. The PAO's budget is not changed (A-24), so OC-3's 0.9 fixed-budget clause applies: its added work comes from some other use of its time: slower decisions on other appeals, or less time per case, recorded as a group with `at_least_one_as_stated` (C-58). The right baseline is the PAO's work without the charge, not zero: fewer cars in the zone mean fewer zone parking tickets and appeals. Arithmetic on the case's figures (about 9,000 new appeals against about 2,800 fewer) gives the net direction. Zone parking enforcement ($11 million a year) also has fewer cars to watch; that is a separate budget, and its staff are not cut by the ordinance, so it is not signed.

**Prevented trips.** Road use in the zone is not an exchange with a seller, so OC-4 does not apply to it as such. Those who stop driving in are worse off by their own ranking (CR-3a); where a shopper who stops coming does not buy the same goods elsewhere, the purchases are prevented exchanges (CR-5a), but whether she buys elsewhere is C-26's question and no separate sign is given.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | Some drivers who now enter the zone on weekdays value the day there by less than $15 more than its other costs, at today's speeds (the charge binds, and the response is partial). | binding | 0.95 | Trip surveys: many trips are discretionary or could use other modes; the city model projects about 88,000 vehicles against 118,000. | Nothing in C-4 to C-6 follows; C-6's response argument gives only "decrease or no change". |
| A-2 | The charge is enforced: cameras read most plates and penalties are collected. | enforcement | 0.85 | 74 entry and 40 internal camera points; penalty $130. | C-1, C-2 and the consequences that follow shrink; C-18 grows. |
| A-3 | Fewer vehicles in the zone raise speeds for those that remain. | other | 0.85 | City traffic model (12 to 15 km/h); experience of road closures and holidays. | Every Tier C consequence (C-5, C-6, C-16, C-30, C-32, C-41, C-45, C-49, C-51, C-53) fails. |
| A-4 | For most car trips into the zone, the time saved by faster roads is worth much less than $15. | other | 0.8 | About 8 minutes a day on a typical commute; wage levels in Calderford. | C-49 becomes `ambiguous`. |
| A-5 | Some drivers switch to bus, tram or Ringside parking. | substitutability | 0.9 | 62% of commuters already use transit; routes from most districts; Ringside is 5 to 10 minutes' walk. | C-7, C-8, C-38, C-50, C-51 are not reported. |
| A-6 | Ringside's garages, about 88% full, cannot add spaces within a year. | durability | 0.75 | About 900 spare spaces; planning and construction times. | C-9 and C-37 shrink; the shift goes to quantity. |
| A-7 | Some shoppers who drove into the zone buy instead in Ringside or Merrowdale, where they can park. | other | 0.7 | Shopper surveys; Ringside's and Merrowdale's ranges. | C-25 to C-33 lose their location chains. |
| A-8 | General-fund support for buses is cut by less than the earmark, so bus service rises. | revenue_use | 0.7 | Earmark about $230 to $260 million against $140 million of support; council statements; past budgets. | C-28's (+) chain, C-39, C-40, C-42 and C-54's bus part are not reported. |
| A-9 | The council reduces general-fund support for buses below what it would otherwise have been (no maintenance-of-effort clause). | revenue_use | 0.7 | No clause in K3; budget pressures. | C-43 is not reported; the earmark adds its full amount to buses. |
| A-10 | More frequent buses bring to zone shops some visitors who would not otherwise have come. | other | 0.55 | Effect of earlier service changes on footfall. | C-28 becomes `decrease` at Tier B. |
| A-11 | Some non-residents can register a vehicle to a zone address without detection. | enforcement | 0.6 | Registration by declaration; audits rare. | C-17 is not reported. |
| A-12 | Some deliveries cannot be completed within 30 minutes (installations, large drops, multi-drop rounds). | other | 0.85 | Freight survey: 12,000 of 19,000 goods vehicles stay longer. | C-44, C-46 and C-47 under U1-b are not reported. |
| A-13 | Under U1-b some rounds can be reshaped into visits under 30 minutes. | other | 0.7 | Many zone drops lie near the edge; Ringside depots. | C-21 to C-24 under U1-b are not reported; C-22 under U1-b is `no_change`. |
| A-14 | Carriers have better alternatives (customers elsewhere) than zone businesses have (premises elsewhere). | substitutability | 0.65 | Carriers serve the whole region; zone businesses' leases and locations. | C-47 is not reported; C-46 rests on RS-14 alone. |
| A-15 | Zone retailers, delivery firms, Ringside residents and the transit union can organize at a cost below their stakes. | other | 0.85 | Existing associations; hearings in 2026. | C-19 is not reported. |
| A-16 | Some drivers evade (foreign, cloned or obscured plates). | enforcement | 0.6 | Experience of camera enforcement elsewhere. | C-18 and C-24 are not reported. |
| A-17 | Some weekday trips can move to before 7:00, after 19:00 or to weekends. | other | 0.7 | Shopping hours; shift work. | C-13 and C-14 are not reported. |
| A-18 | Some through traffic diverts to the Inner Ring Road. | mobility | 0.85 | Origin-destination survey: about a tenth of vehicle-days are through trips. | C-15, C-16, C-30 and C-32 are not reported. |
| A-19 | Some zone workers commute by car and cannot switch cheaply, and zone employers compete with employers elsewhere for them. | other | 0.55 | 22% of commuters drive; shift workers and those far from transit. | C-52 and C-53 are not reported. |
| A-20 | Buyers of property expect the charge to last. | expectations | 0.75 | No expiry; three-yearly review of the level only. | C-31, C-33, C-34, C-36, C-37 shrink. |
| A-21 | Zone garages cannot be converted to other uses within a year. | durability | 0.8 | Structure and planning rules. | C-35 and C-36 shrink; the shift goes to quantity. |
| A-22 | Some residents who drive in the zone would have moved out of it within a few years. | mobility | 0.6 | Household turnover in the zone. | C-20 is not reported. |
| A-23 | For most who switch, the trip by bus or by Ringside parking and walking takes longer than by car. | other | 0.8 | Bus commute about 15 minutes longer door to door. | C-50 and C-51 are not reported. |
| A-24 | The PAO's budget is not raised for the new appeals, and its net caseload rises (about 9,000 new appeals against about 2,800 fewer). | revenue_use | 0.8 | The ordinance gives the PAO no funds; projected notice and appeal rates. | C-58 is replaced by OC-3's rising-budget case. |
| A-25 | Some drivers switch to ride-hail or taxis. | substitutability | 0.6 | Current ride-hail use; parking costs in the zone. | C-10 to C-12 are not reported. |
| A-26 | Ride-hail supply into the zone at peak cannot expand at an unchanged cost at once. | durability | 0.6 | Peak surge pricing now. | C-11 rests on the charge alone; C-12 becomes `decrease`. |
| A-27 | Some people who work in the zone and drive would move into it to pay $1.50 rather than $15. | mobility | 0.55 | Car commuters' household moves. | C-34 loses one (+) chain; still ambiguous with A-8. |
| A-28 | Calderford Transit cannot add buses for at least a year (14 to 18 months to order). | durability | 0.8 | Order books; fleet size; peak load 85%. | C-38 becomes ambiguous. |
| A-29 | The gap in door-to-door time between car and bus far exceeds what faster roads save the bus (15 minutes against a few). | other | 0.75 | Timetables; the city model. | C-51 becomes `ambiguous`. |
| A-30 | The loss of car shoppers dominates the gain from new visitors in zone sales. | other | 0.4 | No direct evidence; depends on the bus service actually added. | Below the cut-off: C-28 stays `ambiguous`. |

## 11. Report

**The policy.** From 1 November 2027, every vehicle driven or parked in Calderford's central zone on a weekday between 7:00 and 19:00 pays $15 for the day; vehicles registered to zone addresses pay $1.50. Scheduled buses are exempt. The net revenue, after the charging office's costs, goes to bus services. It is unclear whether delivery vans that enter and leave within 30 minutes pay.

**Visible consequences.** Drivers pay (C-1, C-2) and the city collects (C-3). Fewer vehicles are in the zone in charging hours (C-4, and C-6 counting the roads), and traffic there moves faster (C-5, Tier C).

**Invisible consequences.**
- *Drivers.* Those who keep driving pay more per day even counting the time they save (C-48, C-49), and have less to spend (C-55). Those who switch to buses, Ringside parking or ride-hail take longer door to door (C-50, C-51). Some drive in the evenings and at weekends instead (C-13, C-14); through drivers go round on the ring road, which slows it (C-15, C-16). Some register cars at zone addresses (C-17) or evade (C-18). Zone residents who drive move less (C-20).
- *Substitutes.* Bus and tram trips rise (C-7) and buses are more crowded until new buses arrive (C-38); after that, crowding may go either way (C-39), while headways shorten (C-40) and buses run faster (C-41, Tier C). Ringside's garages fill and charge more (C-8, C-9). Ride-hail fares rise (C-10, C-11); drivers' net earnings per trip may rise or fall (C-12).
- *Shops and property.* Zone shops lose sales to customers who drove in (C-27); whether their total sales fall depends on how many new visitors the added buses bring (C-28). Driver-dependent retailers leave the zone (C-25), and shoppers buy in Ringside or Merrowdale (C-26). Ringside's shops sell more (C-29) and their property rises in value (C-31), unless the busier ring road outweighs it (C-30, C-32, Tier C). Zone commercial and residential values may rise or fall (C-33, C-34). Zone garages lose value and charge less (C-35, C-36); Ringside garages gain (C-37). These values moved in January 2027, when the charge became expected.
- *Deliveries.* Van operators pay more per day (C-44), though counting faster roads, multi-drop rounds may gain (C-45). Zone businesses pay more for deliveries and bear more of the charge on them than carriers do (C-46, C-47).
- *Jobs.* Zone employers pay more or employ fewer car commuters (C-52); counting faster commutes, the sign is open (C-53).
- *The budget.* The earmark raises bus service only as far as the council does not cut its own support (C-42); what it cuts funds other spending or lower taxes (C-43). The charging office's costs come out of the earmark (C-57). The adjudication office's other work slows (C-58). Revenue falls short of a static projection (C-59).

**Per reading of U1.** If short delivery visits pay (U1-a), single short drops are given up or consolidated (C-22). If they do not (U1-b), delivery rounds are reshaped into short loops (C-21, C-22), with records to prove them (C-23) and false claims (C-24). Under both readings, delivery costs and their burden on zone businesses rise (C-44, C-46, C-47).

**Ambiguous effects.** Zone shops' total sales and zone property values (C-28, C-33, C-34); ride-hail drivers' net price (C-12); bus crowding after new buses (C-39); counting the roads, Ringside's sales and values (C-30, C-32), van operators' cost (C-45) and zone employers' wages and jobs (C-53).

**Key conditions.** That the charge binds and is enforced (A-1, A-2); that fewer vehicles mean faster roads (A-3, p = 0.85), on which every Tier C claim rests; that the time saved is small against $15 for car trips (A-4, p = 0.8); that the council does not cut bus support by the full earmark (A-8, p = 0.7).

**What this analysis cannot say.** How large any effect is; whether drivers as a whole gain or lose counting the time saved; whether the city as a whole is better off; air quality, noise, safety and health (out of scope for version 1); whether the policy is desirable.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | drivers.nonresident | price_paid (weekday in the zone by car) | increase | short | visible | B | CR-1, TX-2 | A-2 |
| C-2 | residents.zone | price_paid (weekday in the zone, discounted) | increase | short | visible | B | CR-1, TX-2 | A-2 |
| C-3 | officials.enforcement | tax_revenue (charge) | increase | short | visible | A | TX-1 | none |
| C-4 | drivers.nonresident, goods_vehicle_operators | quantity_traded (vehicle-days in the zone; not counting effects through the roads) | decrease | short–medium | visible | B | CR-4c, TX-2, CR-12 | A-1, A-2 |
| C-5 | drivers.keep, goods_vehicle_operators, bus_riders | travel_time (per km in the zone) | decrease | short–medium | visible | C | CR-9 (shared_facility), CR-6 | A-1, A-2, A-3 |
| C-6 | drivers.nonresident, goods_vehicle_operators | quantity_traded (vehicle-days in the zone) | decrease | short–medium | visible | C | CR-9 (shared_facility), CR-12e, CR-12 | A-1, A-2, A-3 |
| C-7 | drivers.switch | quantity_substitute (bus and tram trips) | increase | short–medium | invisible | B | RS-1, CR-6 | A-5 |
| C-8 | drivers.switch | quantity_substitute (Ringside garage parking) | increase | short | invisible | B | RS-1, RS-16, CR-6 | A-5, A-6 |
| C-9 | owners.parking.edge | price_substitute (Ringside day rate) | increase | short–medium | invisible | B | RS-16, CR-6 | A-5, A-6 |
| C-10 | drivers.switch | quantity_substitute (ride-hail trips) | increase | short | invisible | B | RS-1 | A-25 |
| C-11 | ride_hail_drivers | price_substitute (ride-hail fares into the zone) | increase | short | invisible | B | RS-16, CR-6, CR-12a | A-25, A-26 |
| C-12 | ride_hail_drivers | net_price_received (per trip) | ambiguous | short | invisible | B | RS-16, CR-12b | A-25, A-26 |
| C-13 | drivers.retime | quantity_traded (weekday trips before 7:00 and after 19:00) | increase | short–medium | invisible | B | RS-8, CR-10a, CR-4 | A-17 |
| C-14 | drivers.retime | quantity_traded (weekend trips) | increase | short–medium | invisible | B | RS-8, CR-4 | A-17 |
| C-15 | drivers.through | travel_time (diverted through trips) | increase | short | invisible | B | CR-4, CR-3a | A-18 |
| C-16 | ring_road_users | travel_time (Inner Ring Road) | increase | short–medium | invisible | C | CR-9 (shared_facility) | A-3, A-18 |
| C-17 | drivers.nonresident | reclassification (registrations to zone addresses) | increase | short–medium | invisible | B | RS-5 | A-11 |
| C-18 | drivers.nonresident, goods_vehicle_operators | legal_breach (unpaid charges, false plates) | increase | short | invisible | B | RS-3, CR-4 | A-16 |
| C-19 | lobbying groups | lobbying_effort | increase | short–medium | invisible | B | RS-7 | A-15 |
| C-20 | residents.zone | turnover (moves out of the zone) | decrease | medium | invisible | B | RS-11, CR-3 | A-22 |
| C-21 | goods_vehicle_operators | reclassification (rounds reshaped into short visits) | U1-a: no_change; U1-b: increase | short–medium | invisible | B | RS-5, CR-1 | A-13 |
| C-22 | goods_vehicle_operators | quantity_traded (delivery visits under 30 minutes) | U1-a: decrease; U1-b: increase | short–medium | invisible | B | CR-4, RS-5 | A-1, A-13 |
| C-23 | goods_vehicle_operators | compliance_cost (short-visit records) | U1-a: no_change; U1-b: increase | short | invisible | B | CR-8c, OC-2 | A-13 |
| C-24 | goods_vehicle_operators | legal_breach (false short-visit claims) | U1-a: no_change; U1-b: increase | short | invisible | B | RS-3 | A-13, A-16 |
| C-25 | businesses.zone (driver-dependent retailers) | number_of_sellers (in the zone) | decrease | medium | invisible | B | RS-4, RS-6, CR-7a | A-7, A-20 |
| C-26 | shoppers | cross_border_purchases (outside the zone) | increase | short–medium | invisible | B | RS-4, RS-9 | A-7 |
| C-27 | businesses.zone | quantity_traded (sales to car customers; not counting effects through the roads) | decrease | short–medium | invisible | B | RS-9, CR-9 | A-1, A-7 |
| C-28 | businesses.zone | quantity_traded (all sales; not counting effects through the roads) | ambiguous | medium | invisible | B | RS-9, CR-12b | A-1, A-7, A-8, A-10 |
| C-29 | businesses.edge | quantity_traded (Ringside sales; not counting effects through the roads) | increase | short–medium | invisible | B | RS-9, RS-4, CR-9 | A-7 |
| C-30 | businesses.edge | quantity_traded (Ringside sales) | ambiguous | short–medium | invisible | C | RS-9, CR-9 (shared_facility), CR-12 | A-3, A-7, A-18 |
| C-31 | owners.edge_commercial | asset_value (not counting effects through the roads) | increase | short | invisible | B | CR-7c, CR-10c, SB-4 | A-7, A-20 |
| C-32 | owners.edge_commercial | asset_value | ambiguous | short | invisible | C | CR-7c, CR-9 (shared_facility), CR-12 | A-3, A-7, A-18, A-20 |
| C-33 | owners.zone_commercial | asset_value (not counting effects through the roads) | ambiguous | short | invisible | B | CR-7b, CR-7c, CR-10c, CR-12b | A-7, A-8, A-10, A-20 |
| C-34 | owners.zone_residential | asset_value (not counting effects through the roads) | ambiguous | short | invisible | B | CR-7c, CR-10c, CR-6, CR-12b | A-2, A-8, A-20, A-27 |
| C-35 | owners.parking.zone | price_complement (zone day rate) | decrease | short–medium | invisible | B | RS-12, CR-6 | A-1, A-21 |
| C-36 | owners.parking.zone | asset_value (zone garages) | decrease | short | invisible | B | CR-7c, CR-10c, SB-4 | A-1, A-20, A-21 |
| C-37 | owners.parking.edge | asset_value (Ringside garages) | increase | short | invisible | B | CR-7c, CR-10c, SB-4 | A-6, A-20 |
| C-38 | bus_riders | quality_per_unit (crowding, before new buses) | decrease | short | invisible | B | CR-6, PC-19 | A-5, A-28 |
| C-39 | bus_riders | quality_per_unit (crowding, after new buses) | ambiguous | medium | invisible | B | RS-16, RS-13, SB-7, CR-12b | A-5, A-8 |
| C-40 | bus_riders | wait_time (headways) | decrease | medium | invisible | B | SB-7, CR-8d | A-8 |
| C-41 | bus_riders | travel_time (bus journeys in the zone) | decrease | short–medium | invisible | C | CR-9 (shared_facility) | A-1, A-3 |
| C-42 | transit_operator | quantity_supplied (bus service-km) | increase | medium | visible | B | SB-7, CR-8d | A-8 |
| C-43 | taxpayers, recipients of other city spending | resources_available_other_uses | at_least_one_increase | medium | invisible | B | SB-7, CR-8d, CR-8b | A-9 |
| C-44 | goods_vehicle_operators | full_cost_per_unit (van-day; not counting effects through the roads) | U1-a: increase; U1-b: increase | short–medium | invisible | B | CR-1, CR-3, CR-12 | A-2, A-12 |
| C-45 | goods_vehicle_operators | full_cost_per_unit (van-day) | U1-a: ambiguous; U1-b: ambiguous | short–medium | invisible | C | CR-9 (shared_facility), CR-12b, CR-12 | A-2, A-3, A-12 |
| C-46 | businesses.zone | price_paid (deliveries; not counting effects through the roads) | U1-a: increase; U1-b: increase | short–medium | invisible | B | RS-14, CR-7b, DM-1 | A-2, A-12, A-14 |
| C-47 | businesses.zone | tax_share_borne (charge on deliveries, against carriers) | U1-a: increase; U1-b: increase | medium | invisible | B | DM-1, CR-7b | A-12, A-14 |
| C-48 | drivers.keep | full_cost_per_unit (weekday by car; not counting effects through the roads) | increase | short–medium | invisible | B | CR-1, CR-3, CR-12 | A-2 |
| C-49 | drivers.keep | full_cost_per_unit (weekday by car) | increase | short–medium | invisible | C | CR-9 (shared_facility), CR-12, CR-12e | A-2, A-3, A-4 |
| C-50 | drivers.switch | travel_time (door to door; not counting effects through the roads) | increase | short–medium | invisible | B | CR-3a, CR-4 | A-5, A-23 |
| C-51 | drivers.switch | travel_time (door to door) | increase | short–medium | invisible | C | CR-9 (shared_facility), CR-12, CR-12e | A-3, A-5, A-23, A-29 |
| C-52 | employers.zone, workers.zone | wage_rate (+), employment (−) (not counting effects through the roads) | at_least_one_as_stated | medium | invisible | B | CR-5c, CR-7a, CR-12 | A-19 |
| C-53 | employers.zone, workers.zone | wage_rate, employment | ambiguous | medium | invisible | C | CR-9 (shared_facility), CR-12b, CR-12 | A-3, A-19 |
| C-54 | input_suppliers | quantity_traded (cameras, payment systems, buses) | increase | short–medium | invisible | B | CR-9, SB-7 | A-8 |
| C-55 | drivers.keep, residents.zone, goods_vehicle_operators | resources_available_other_uses (money) | decrease | short–long | invisible | B | TX-1, OC-1, CR-3 | A-2 |
| C-56 | drivers.nonresident, residents.zone, goods_vehicle_operators | compliance_cost (accounts, payments, disputes) | increase | short | invisible | A | OC-2, TX-5, CR-8c | none |
| C-57 | officials.enforcement (CCO) | enforcement_cost | increase | short–long | invisible | A | OC-3, CR-8c, CR-8d | none |
| C-58 | officials.adjudication, parking_appellants | wait_time (other appeals) (+), enforcement_cost (time per other appeal) (−) | at_least_one_as_stated | short–medium | invisible | B | OC-3, CR-8a | A-24 |
| C-59 | officials.enforcement | tax_revenue_vs_static_projection | decrease | short | invisible | B | TX-9 | A-1 |

## Gaps found

**(a) Calculus gaps (a step no core rule covers).** None new. Every chain through travel speeds runs over the `shared_facility` relation (the zone's roads, the Inner Ring Road): that is the open GAP-026-1 (also raised in WE-032 for congestion), covered by CR-9's 0.7 clarification at Tier C pending Q20.

**(b) Unclear core rules.**
1. *CR-12 0.9, Tier C against Tier B, where both give the same sign.* For vehicle-days (C-4, C-6), drivers' cost (C-48, C-49) and switchers' time (C-50, C-51), the Tier C combined sign equals the Tier B sign. The rule says "record two consequences" without saying whether the second is needed when it adds no information. Recorded both here, because the Tier C one rests on extra premises (A-3, A-4, A-29) and a reader needs to see that the Tier B sign survives them.
2. *CR-12e's response argument across a shared facility.* The argument applies to vehicle-days (C-6): the drivers drawn back are responding to a speed gain caused by drivers leaving. It does not apply to vans (C-45): for them the speed gain is caused by cars' response, a second change (CR-12e, 0.8). Nor to each driver's full cost (C-49): it binds the class's number, not each member's cost. The 0.8 and 0.9 notes cover both limits, but only when read together; a sentence saying "the argument signs the quantity of the responding class; costs to members or to other classes need their own premise" would help.
3. *CR-6 0.9, public seller adding capacity after a lag.* Worked, but it needed CR-12g to keep the two horizons apart (C-38 short, C-39 medium). The clause could say so.
4. *CR-1, operation by registered address.* The residents' discount is a reduced rate for a class defined by a declaration the actor controls. CR-1 0.7 says to split a class by response; here the class boundary is itself something actors choose (C-17). RS-5 covers the response, but CR-1 does not say that a class defined by a declared status is open to entry.

**(c) Missing or wrong patterns.**
1. *TX-2 (and DM-1) where the seller of the taxed good is the state.* TX-2 gives `price_paid` up and/or `net_price_received` down. Road space has no seller whose net price can fall: it is a public supply at a zero money price, rationed by time (CR-6, 0.7). Applied as written, TX-2's "and/or" leaves the seller's side empty and says nothing about where the rest of the burden goes. It was read as: buyers bear the charge first, and the burden passes along the trips' other relations (customers' purchases, deliveries) to immobile means in the zone (CR-7b). No sign had to be overridden, but a clause for a charge on the use of a public facility would help.
2. *RS-16 0.9, costs on the substitute.* Worked as written for ride-hail (C-11, C-12): both chains raise the fare, and they oppose on drivers' net price. The clause speaks of "the substitute's net price to its sellers"; the buyers' price is the other half and needed CR-12a.
3. *RS-9 0.9, location complements and new occupants.* Applied as written, but "the new occupants" came through two different relations: buses funded by the earmark (Tier B, a second component) and quieter streets (Tier C, the shared facility). The clause does not say that the new occupants' chain may run through another component or another tier; both were needed here (C-28, C-30).
4. *SB-7 needs two premises, not one.* SB-7 states that spending on the purpose "rises by less than the earmarked amount", with one premise (general funding can be cut). Whether it still rises at all needs a second premise, that the cut is less than the earmark (A-8). Without it, C-42 could not be signed. SB-7 should say so.
5. No pattern gave a sign that had to be overridden.

**(d) Vocabulary.**
1. No variable for vehicle-days in a zone or use of a road; recorded as `quantity_traded` with a qualifier, though no exchange takes place.
2. `full_cost_per_unit` is defined for a buyer's wait, search and side payments; it was used for the money charge plus travel time (C-48, C-49), which fits the definition's spirit but not its examples.
3. `wait_time` serves both for bus headways (C-40) and for adjudication queues (C-58); no variable for an agency's other work slowed by a fixed budget.
4. No actor class for users of a shared facility as such; `ring_road_users` was coined.

**(e) Test of 0.9.**
- *CR-12 0.9, Tier C against Tier B.* Worked as written on nine keys: three where a dominance premise or the response argument made the Tier C sign equal the Tier B sign (C-6, C-49, C-51), four where the Tier C sign is `ambiguous` (C-30, C-32, C-45, C-53), and two where the Tier B sign was already ambiguous and kind 3 made a second record unnecessary (C-28, C-34). The Tier C chain never lowered a Tier B tier. Needed interpretation only on whether to record an identical Tier C sign ((b) 1).
- *CR-12 0.9, what the response argument gives.* Worked as written for vehicle-days (C-6): the argument gave "decrease or no change", and A-1 (some drivers at the margin at the old speed) supplied the partial-response premise. Correctly did not apply to vans or to each driver's cost ((b) 2).
- *RS-9 0.9, location complements.* Worked as written for zone and Ringside shops (C-27, C-29), and its "new occupants" clause turned the zone's total into `ambiguous` (C-28). Needed interpretation on new occupants arriving through another component and another tier ((c) 3).
- *RS-16 (0.8 split premise; 0.9 costs on the substitute; Unless with RS-13).* Worked as written for Ringside garages (C-9, with A-6), for ride-hail (C-11, C-12), and for buses once new buses arrive (C-39, Unless clause).
- *CR-6 0.9, splitting a shift into price and quantity.* Worked as written: Ringside garages (quantity until full, then price, on A-6), zone garages (price, on A-21), zone housing (price, stock fixed). Its public-seller-with-a-lag clause worked for buses, with CR-12g ((b) 3).
- *CR-7c (inside and at the edge).* Worked as written: values move at announcement for Ringside commercial (C-31), zone garages (C-36) and Ringside garages (C-37); zone commercial and residential values are `ambiguous` (C-33, C-34). The Tier C rule carried through to capitalization (C-32).
- *TX-1, TX-2 incidence.* TX-1 worked as written (C-3, C-55). TX-2 needed interpretation: road space has no seller ((c) 1). DM-1 worked for deliveries between carriers and zone businesses (C-47, on A-14).
- *CR-8d, SB-7 (earmark fungibility).* Worked, with a second premise SB-7 does not name ((c) 4): C-42 on A-8, C-43 on A-9, recorded as a group of payers in reverse (CR-8, 0.7).
- *OC-3 0.9, fixed budget, and right baseline.* Worked as written: the PAO's added work is a group with `at_least_one_as_stated` (C-58), and the right baseline (fewer zone parking appeals) was netted by arithmetic on the case's figures (A-24). The CCO's cost fell under the own-revenue case (C-57).
- *RS-8 0.9 (more timing chains).* No opposing timing chain arose; per-window signs for evening and weekend trips (C-13, C-14) followed 02_ontology.md, 2.5, signed on flows (CR-12 0.9).
- *OC-5 0.9 (new to the place).* Worked as written for retailers moving from the zone to Ringside (C-25).
- *Candidates from 06_gaps.md, 6.2e.* "Compensating differential from a non-wage term" (WE-032) was needed for zone jobs reached by car (C-52): CR-5c and CR-7a, with the cost of reaching a job in place of a non-wage term. The use is against the no-charge counterfactual (a cost the charge adds to taking a zone job), so it is valid; this is its second use. Its name should be widened to "a change in the cost of taking a job at a place". "A claim payable inside a boundary draws items from outside" (WE-027) resembles the residents' discount drawing registrations (C-17), but RS-5 covered it; not counted as a use.
