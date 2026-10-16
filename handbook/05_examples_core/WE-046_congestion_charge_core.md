# WE-046 / Analysis: Congestion charge for a central zone, with a residents' discount and a bus earmark

Analyst: core-only re-run (Handbook 0.9)  |  Rules: core rules CR-1 to CR-12 only  |  Status: awaiting comparison

## 1. Policy record

**Calderford Central Zone Charging Ordinance.** Calderford (about 900,000 people) charges $15 for each weekday on which a vehicle is driven or parked between 7:00 and 19:00 in its central zone, the 7 km² inside (not including) the Inner Ring Road. The zone has about 58,000 residents, 14,500 cars registered to zone addresses, 260,000 jobs and about 4,200 shops, cafés and restaurants. Just outside lies Ringside (about 1,100 shops and offices, three garages with about 7,500 spaces at $9 a day, about 88% full), then the outer districts and, beyond the city line, Merrowdale with a regional shopping centre. On an average weekday about 118,000 vehicles are in the zone in charging hours (92,000 cars, 9,500 of them residents'; 19,000 goods vehicles, 7,000 of them single visits under 30 minutes; 4,000 taxis and ride-hail cars; 3,000 buses and coaches); average speed is about 12 km/h. Commuters to zone jobs: 62% bus or tram, 22% car, 16% on foot or bicycle. Zone off-street parking: about 31,000 spaces at about $21 a day, about 90% full. Calderford Transit: about 850 buses and two tram lines, fares about $180 million a year, general-fund support about $140 million; peak load into the zone about 85%; new buses take 14 to 18 months. Ride-hail fares are set by the platforms, unregulated. The city's model projects about 88,000 vehicles and about 15 km/h with the charge.

| Field | Value | Source sentence |
|---|---|---|
| Jurisdiction (and what lies just outside) | The zone inside the Inner Ring Road. Just outside: Ringside (shops, offices, garages), the Inner Ring Road itself, the outer districts and Merrowdale. | §2: "The zone is the area bounded by, but not including, the Inner Ring Road." |
| Announced / enacted / effective / expires | Announced and enacted 4 January 2027; charging from 1 November 2027; no expiry; the level is reviewed every three years. | §1, §14. |
| Enforcement (who, penalties, resources) | City Charging Office (CCO): plate-reading cameras at 74 entry points and 40 internal points. Penalty notice $130 ($65 within 14 days). Appeals to the existing Parking Adjudication Office (PAO), whose budget is unchanged. | §9 to §11. |

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Daily charge | `per_unit_tax` | A vehicle-day in the zone, weekdays 7:00 to 19:00 | Registered keeper of each vehicle driven or parked in the zone | $15 a day, payable by midnight next day; one charge covers any number of entries that day | Scheduled buses; emergency vehicles |
| K2 Residents' discount | `per_unit_tax` (reduced rate) | Same | Keepers whose registered address is in the zone | 90% discount: $1.50 a day; residence taken from the vehicle register, updated by the keeper's declaration | - |
| K3 Earmark | `revenue_use` | Net revenue of K1 and K2 | The city | Net revenue after the CCO's costs "shall be applied to bus services"; nothing on the level of general-fund support for buses | - |
| K4 Enforcement and administration | Enforcement | K1, K2 | CCO (funded from gross revenue); PAO (budget unchanged) | About $45 million a year to run; about $70 million to set up, advanced from city reserves and repaid from the first year's revenue | - |

Existing rules that stay in the counterfactual: Transit fares and general-fund support (set each year); on-street parking rules and their enforcement in the zone (about $11 million a year); the PAO (about 44,000 parking appeals a year, about 14,000 on zone tickets).

Counterfactual law: no charge on any vehicle-day in the zone; Transit funded from fares and whatever support the council votes; the same parking rules.

Unclear provisions:
- **U1, short delivery visits.** §3(1) charges "each day on which a vehicle is driven or parked in the zone"; §7 says a goods vehicle that enters and leaves within thirty minutes in the course of a delivery "shall be recorded as a short visit"; the schedule sets one daily rate and never mentions short visits. U1-a: a short visit is recorded and pays $15 like any other day. U1-b: a short visit is not a chargeable day and pays nothing. The CCO has issued no guidance. Readings get no probability.

**Figures used.** Static revenue about $414 million; projected revenue about $303 million (about $26 million less under U1-b). Net of the CCO's $45 million, about $230 to $260 million a year for buses, against $140 million of general-fund support. A typical car commuter saves about 8 minutes a day; a multi-drop van covering about 40 km in the zone saves about 40 minutes a day. PAO: about 9,000 new appeals a year against about 2,800 fewer zone parking appeals (net about +6,200, about 14%), same budget.

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | CR-1 operations | Core rules applied |
| --- | --- | --- | --- | --- |
| K1 Daily charge | binary (state takes) | Yes: some drivers value a zone day by less than $15 more than its other costs (A-1); enforced (A-2) | 3 (a payment attached to the option "be in the zone on a weekday in charging hours", per vehicle-day, not per entry); 1 where enforced only in the sense that "enter without paying" carries a penalty risk (op 3 on evasion, A-16) | CR-3a, CR-4 (every pair of options), CR-5a, CR-5c, CR-6 (public-supply clause for road space), CR-7, CR-8, CR-9, CR-10 |
| K2 Residents' discount | binary (state takes, at a lower rate) | Yes for resident keepers: $1.50 against $0 in the counterfactual | 3 (a smaller payment attached to the same option for keepers registered in the zone); it also makes "register at a zone address" and "live in the zone" better relative to living outside, for those who drive into the zone | CR-4 (x: live outside, y: live in the zone; x: register truthfully, y: register at a zone address), CR-7c, CR-10a |
| K3 Earmark | binary (state gives, to bus services) | Yes, on the money earmarked; whether bus service rises depends on general-fund support (A-8, A-9) | 4 (means transferred to bus services); through CR-8d, possibly to other general-fund uses | CR-8b, CR-8d, CR-6 (public supply of bus seats) |
| K4 Enforcement and administration | binary (means used up) | Yes | 4 (about $45 million a year and $70 million advanced from reserves); 3 (penalty risk on non-payment; appeals add to the PAO's fixed capacity) | CR-8a, CR-8c, CR-6 (public-supply clause for the PAO) |

## 3. Actor classes

| Actor class | Role | How its options change (CR-1) |
| --- | --- | --- |
| drivers.non_resident.continuing | Non-resident keepers who keep entering on weekdays | Op 3: $15 per zone day; faster roads (A-3). |
| drivers.non_resident.switching | Non-resident keepers who stop entering in charging hours | Op 3 on "drive in"; they move to bus or tram, Ringside parking, ride-hail, other hours or other shops (CR-4). |
| drivers.through | Through trips across the zone | Op 3 on "cross the zone"; they can use the Inner Ring Road (A-18). |
| residents.zone_keepers | Keepers registered at zone addresses | Op 3: $1.50 per weekday their car is driven or parked in the zone; faster roads. |
| residents.zone_prospective | Zone workers who drive and might move in (A-27) | Living in the zone now saves $13.50 a day against living outside. |
| carriers.short_visit | Goods vehicles making single visits under 30 minutes | U1-a: op 3 ($15 per day); U1-b: no charge. Faster roads. |
| carriers.long_visit | Goods vehicles staying longer (installations, multi-drop rounds) | Op 3: $15 per vehicle-day; faster roads (about 40 minutes a day on a 40 km round). |
| zone_businesses | Shops, cafés, restaurants and firms in the zone | Through CR-9: fewer car shoppers, more bus visitors, deliveries charged, car-commuting staff charged. |
| zone_employers | Employers of zone jobs | Through CR-9 (contract, employment): staff who drive face $15 a day (A-19). |
| workers.zone_car_commuters | Zone workers who drive and cannot switch cheaply | Op 3: $15 a day. |
| bus_riders | Existing and new bus and tram riders | Through CR-9 (shared seats, public supply): more riders; later more service (A-8); faster buses (A-3). |
| calderford_transit | The bus and tram operator | Op 4: receives the earmark (K3); more fares. |
| transit_workers, bus_makers | Drivers and suppliers of buses | Through CR-9 (input_to bus service). |
| taxpayers / recipients of other general-fund spending | General fund | Through CR-8d if general-fund support for buses is cut (A-9). |
| city_reserves | The fund that advances $70 million | Op 4 in 2027, repaid from first-year revenue. |
| zone_garages | Owners of off-street parking in the zone | Through CR-9 (complement: parking with zone vehicle-days): fewer cars. |
| ringside_garages | Owners of the three Ringside garages | Through CR-9 (substitute): more drivers park there; capacity fixed (A-6). |
| ringside_parkers.existing | Current users of Ringside garages | Through CR-9: compete with switchers for the same spaces. |
| ringside_merrowdale_shops | Shops in Ringside and Merrowdale | Through CR-9 (substitute, across_border): some car shoppers come instead (A-7). |
| property_owners.zone_homes, property_owners.zone_commercial, property_owners.ringside_merrowdale_retail | Owners of durable assets tied to place | CR-7c: yields change as above. |
| ride_hail_and_taxi | Platforms, drivers and their riders | Op 3: $15 per vehicle-day; more riders (A-25); faster roads. |
| inner_ring_users | Drivers on the Inner Ring Road | Through CR-6 (public supply of road space at zero price): more through traffic (A-18). |
| evaders | Keepers who evade (A-16) and those who falsely register at zone addresses (A-11) | CR-4 (x: comply, y: violate). |
| keepers.cloned_plates | Keepers whose plates are cloned | Receive notices for others' trips (A-16). |
| appellants.pao | Everyone who appeals a parking or charge notice | Through CR-6 (public supply of hearings at a fixed budget). |
| officials.cco | The charging office | Op 4: runs cameras, collects charges. |
| organized_groups | Zone retailers, delivery firms, Ringside residents, the transit union | CR-4 (x: accept, y: lobby). |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-1 | drivers.non_resident (all who enter) | price_paid (zone vehicle-day, charging hours) | increase | short; medium; long | CR-1 op 3, CR-5c | A-2 |
| C-2 | residents.zone_keepers | price_paid (zone vehicle-day, charging hours) | increase | short; medium; long | CR-1 op 3, CR-5c | A-2 |
| C-3 | officials.cco (city) | tax_revenue | increase | short; medium; long | CR-1 op 3, CR-8b | A-2 |
| C-4 | calderford_transit | subsidy_outlay (total funding of bus services) | increase | medium; long | CR-1 op 4, CR-8b, CR-8d | A-2, A-8 |
| C-5 | bus_riders | wait_time (time between buses at stops on routes into the zone) | decrease | medium; long | CR-1 op 4, CR-9, LW-10 | A-8, A-28 |
| C-6 | vehicles remaining in the zone (continuing drivers, residents, carriers, ride-hail) | travel_time (in the zone, charging hours) | decrease | short; medium; long | CR-4b, CR-6 (public-supply clause), CR-9 (shared_facility) | A-1, A-3 |

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-7 | drivers.non_resident.switching | quantity_demanded (zone vehicle-days, weekday charging hours) | decrease | short; medium; long | CR-4b, CR-4c, CR-5a | A-1, A-2 |
| C-8 | drivers.non_resident.switching | quantity_substitute (bus and tram trips) | increase | short; medium; long | CR-4 (x: drive in, y: bus or tram) | A-5 |
| C-9 | drivers.non_resident.switching | quantity_substitute (Ringside garage parking) | increase | short; medium; long | CR-4 (x: park in the zone, y: park in Ringside and walk) | A-5, A-6 |
| C-10 | drivers.non_resident.switching | quantity_substitute (ride-hail and taxi trips into the zone) | increase | short; medium; long | CR-4 (x: drive own car in, y: ride-hail) | A-25 |
| C-11 | drivers.non_resident (trips movable in time) | quantity_demanded (trips before 7:00, after 19:00 and at weekends) | increase | short; medium; long | CR-4 (x: weekday charging hours, y: other hours), CR-10a; timing signed per window with C-7 | A-17 |
| C-12 | drivers.through | quantity_substitute (Inner Ring Road trips) | increase | short; medium; long | CR-4 (x: cross the zone, y: go round) | A-18 |
| C-13 | drivers.non_resident.switching | travel_time (door to door) | increase | short; medium; long | CR-3a, CR-4b, CR-12e | A-5, A-23, A-29 |
| C-14 | drivers.non_resident.continuing | full_cost_per_unit (zone vehicle-day) | increase | short; medium; long | CR-12b, CR-12e (dominance: A-4; response argument) | A-1, A-2, A-3, A-4 |
| C-15 | residents.zone_keepers | full_cost_per_unit (zone vehicle-day) | ambiguous | short; medium; long | CR-12b | A-2, A-3 |
| C-16 | carriers.short_visit | price_paid (zone access per short visit) | U1-a: increase; U1-b: no_change | short; medium; long | CR-1 op 3 per reading, CR-5c | A-2 |
| C-17 | carriers.short_visit | full_cost_per_unit (short delivery visit) | U1-a: increase; U1-b: decrease | short; medium; long | CR-12b, CR-12e (U1-a: A-N1); CR-6 (U1-b) | A-3, A-N1 |
| C-18 | carriers.long_visit | reclassification (rounds reshaped into visits under 30 minutes) | U1-a: no_change; U1-b: increase | short; medium | CR-4 (x: long visit, y: short visits) | A-12, A-13 |
| C-19 | carriers.long_visit | transaction_size (drops per vehicle-day in the zone) | increase | short; medium | CR-4c (one charge covers the day), CR-1 0.9 (per range) | A-12, A-N2 |
| C-20 | carriers.long_visit | full_cost_per_unit (vehicle-day of a multi-drop round) | ambiguous | short; medium; long | CR-12b | A-2, A-3, A-12 |
| C-21 | zone_businesses | tax_share_borne (charge on deliveries, against carriers) | increase | medium; long | CR-7b | A-2, A-12, A-14 |
| C-22 | evaders | legal_breach (unpaid charges: foreign, cloned, obscured plates) | increase | short; medium; long | CR-4 (x: comply, y: violate) | A-16 |
| C-23 | keepers.cloned_plates | compliance_cost (contesting notices for others' trips) | increase | short; medium; long | CR-9 (contract: the plate register), CR-8c | A-16 |
| C-24 | evaders (non-residents) | reclassification (vehicles registered to zone addresses) | increase | short; medium; long | CR-4 (x: register truthfully, y: register at a zone address) | A-11 |
| C-25 | officials.cco (city) | tax_revenue_vs_static_projection | decrease | short; medium; long | CR-4b (A-1); also CR-4 evasion (A-16), registration (A-11), U1-b | A-1 |
| C-26 | residents.zone_keepers | quantity_demanded (cars kept at zone addresses) | decrease | medium; long | CR-4b, CR-4c | A-N3 |
| C-27 | residents.zone_keepers (who would have moved) | turnover (moves out of the zone) | decrease | medium; long | CR-4 (x: move out, y: stay), CR-3a | A-22 |
| C-28 | residents.zone_prospective | quantity_demanded (zone housing) | increase | short (from announcement); medium; long | CR-4 (x: live outside, y: move in), CR-10a | A-27 |
| C-29 | organized_groups | lobbying_effort | increase | short (from announcement); medium; long | CR-4 (x: accept, y: lobby), CR-8c | A-15 |
| C-30 | officials.cco | enforcement_cost | increase | short; medium; long | CR-1 op 4, CR-8c | - |
| C-31 | city_reserves | resources_available_other_uses | decrease | short (2027 to first-year repayment) | CR-1 op 4, CR-8a, CR-10 | - |
| C-32 | all paying keepers | compliance_cost (paying by midnight next day, keeping registration current) | increase | short; medium; long | CR-1 op 3, CR-8c | - |
| C-33 | drivers.non_resident.continuing, carriers.long_visit | resources_available_other_uses | decrease | short; medium; long | CR-3 (note: they keep paying), CR-8a, CR-8b | A-2 |

## 6. Second-order effects

Depth limit 4; diffuse effects on customers of zone shops (relation: deliveries input_to retail) are pruned at depth 3.

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C-34 | bus_riders (existing) | quality_per_unit (crowding on routes into the zone) | decrease | short | CR-9, CR-6 (public-supply clause) | car trips substitute for bus trips; riders share fixed capacity (shared_facility) | A-5, A-28 |
| C-35 | bus_riders | quality_per_unit (crowding on routes into the zone) | ambiguous | medium; long | CR-12b | as above; earmark funds service (K3) | A-5, A-8 |
| C-36 | bus_riders | travel_time (bus running time in the zone) | decrease | short; medium; long | CR-9, CR-6 (public-supply clause) | buses share road space with cars (shared_facility) | A-1, A-3 |
| C-37 | calderford_transit | quantity_traded (bus and tram trips) | increase | short; medium; long | CR-9, CR-5 | car trips substitute for bus trips (close) | A-5 |
| C-38 | bus_makers | quantity_traded (new buses ordered) | increase | short; medium | CR-9, LW-10 | buses input_to bus service | A-8 |
| C-39 | transit_workers | employment (bus operation) | increase | medium; long | CR-9, LW-10 | labor input_to bus service | A-8, A-28 |
| C-40 | taxpayers / recipients of other general-fund spending | resources_available_other_uses | at_least_one_increase | medium; long | CR-8d, CR-8b | general fund (currency of the budget) | A-9 |
| C-41 | ringside_garages | net_price_received (Ringside garage parking) | increase | short; medium | CR-9, CR-6 (0.8: a free price's rise is enough) | Ringside parking substitute for zone parking (close) | A-5, A-6 |
| C-42 | ringside_parkers.existing | price_paid (Ringside garage parking) | increase | short; medium | CR-9, CR-6 | same market | A-5, A-6 |
| C-43 | ringside_garages | asset_value (garages) | increase | short (from announcement) | CR-7c, CR-10c | as above | A-5, A-6, A-20 |
| C-44 | zone_garages | net_price_received, quantity_traded (zone off-street parking) | at_least_one_decrease | short; medium; long | CR-9, CR-6 (0.9: splitting a shift) | zone parking complement of zone vehicle-days (close) | A-1 |
| C-45 | zone_garages | asset_value (garages) | decrease | short (from announcement) | CR-7c, CR-10c, CR-10b | as above | A-1, A-20, A-21 |
| C-46 | ringside_merrowdale_shops | quantity_traded (retail sales) | increase | short; medium; long | CR-9, CR-4 | Ringside and Merrowdale shops substitute (across_border) for zone shops; trip complements | A-7 |
| C-47 | property_owners.ringside_merrowdale_retail | asset_value (retail property) | increase | short (from announcement) | CR-7c, CR-10c | as above | A-7, A-20 |
| C-48 | zone_businesses (retail) | quantity_traded (retail sales in the zone) | ambiguous | short; medium; long | CR-12b | substitute (A-7); bus service complement of visits (A-10) | A-7, A-8, A-10 |
| C-49 | property_owners.zone_commercial | asset_value (shop and office property) | ambiguous | short (from announcement); medium | CR-12b, CR-7c | as above | A-7, A-8, A-10, A-14, A-20 |
| C-50 | property_owners.zone_homes | asset_value (homes in the zone) | ambiguous | short (from announcement); medium | CR-12b, CR-7c | location complement of zone jobs | A-20, A-27, A-N3 |
| C-51 | workers.zone_car_commuters | wage_rate (zone jobs) | increase | medium; long | CR-9, CR-7b | contract (employment); zone jobs compete with jobs elsewhere | A-19 |
| C-52 | ride_hail_and_taxi (riders) | price_paid (ride-hail trips into the zone) | ambiguous | short; medium | CR-12b | ride-hail substitute for own car (partial) | A-3, A-25, A-26 |
| C-53 | inner_ring_users | travel_time (Inner Ring Road, peak) | increase | short; medium; long | CR-9, CR-6 (public-supply clause) | through trips move to the Inner Ring (substitute; shared_facility) | A-18 |
| C-54 | appellants.pao | wait_time (parking and charge appeals) | increase | short; medium; long | CR-9, CR-6 (public-supply clause), CR-12e (arithmetic) | charge notices and parking tickets share the PAO (shared_facility) | A-2, A-24 |
| C-55 | city (parking enforcement) | non_tax_receipts (zone parking fines) | decrease | short; medium; long | CR-9, CR-4 | parking tickets complement of cars in the zone | A-1 |

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (-) | Dominance premise | Combined sign |
| --- | --- | --- | --- | --- |
| drivers.non_resident.continuing, full_cost_per_unit, all | $15 charge (CR-1 op 3) | faster roads (CR-6, A-3); lower zone parking price if the garage price falls (C-44) | A-4 (empirical: 8 minutes worth much less than $15) against the time chain; CR-12e response argument against the parking chain (the parking price falls because fewer drive and cannot fall so far that the reason to drive less disappears) | increase (C-14) |
| residents.zone_keepers, full_cost_per_unit, all | $1.50 charge | faster roads (A-3) | None: A-4 compares the time saved with $15, not $1.50 | ambiguous (C-15) |
| carriers.short_visit, full_cost_per_unit | U1-a: $15 charge | faster roads (A-3), at most a few minutes in a visit under 30 minutes | U1-a: A-N1 (empirical); U1-b: no (+) chain | U1-a: increase; U1-b: decrease (C-17) |
| carriers.long_visit, full_cost_per_unit, all | $15 charge | about 40 minutes a day saved on a multi-drop round (A-3) | None: A-4 is about car trips | ambiguous (C-20) |
| zone_businesses, quantity_traded (retail sales) | more frequent buses bring new visitors (A-8, A-10, p 0.55) | car shoppers move to Ringside and Merrowdale with their trip complements (A-7) | A-30 would give dominance to the (-) chain but has p 0.4, below the cut-off; both chains are kind (2) with p at least 0.5 | ambiguous (C-48) |
| property_owners.zone_commercial, asset_value | as above (+) | as above (-); deliveries charged and borne more by zone businesses (C-21) | None | ambiguous (C-49) |
| property_owners.zone_homes, asset_value | zone workers who drive move in to pay $1.50 rather than $15 (A-27) | residents who value a car in the zone by less than $1.50 a day more than the alternatives give it up or move out (A-N3) | None | ambiguous (C-50) |
| bus_riders, quality_per_unit, short | more riders on a fixed fleet (A-5, A-28) | faster zone running lets the same fleet run more trips (A-N4, p 0.35) | Kind (2) chain below the cut-off: derived sign reported, chain recorded in section 10 | decrease (C-34) |
| bus_riders, quality_per_unit, medium; long | more riders (A-5) | more service funded by the earmark (A-8) | None | ambiguous (C-35) |
| ride_hail_and_taxi, price_paid, short; medium | $15 per vehicle-day attached to each car (CR-1 op 3, CR-7b); more riders with supply not expandable at once (A-25, A-26) | faster roads mean more trips per hour per car (A-3) | None | ambiguous (C-52) |
| appellants.pao, wait_time | about 9,000 new charge appeals (A-2) | about 2,800 fewer zone parking appeals (A-1) | Arithmetic on the case's figures (CR-12e), stated in A-24 | increase (C-54) |
| officials.cco, tax_revenue, all | collections on about 88,000 vehicle-days | none (the counterfactual collects nothing) | - | increase (C-3) |
| calderford_transit, subsidy_outlay | earmark of about $230 to $260 million | cut in general-fund support (A-9) | A-8 (empirical: the cut is smaller than the earmark) | increase (C-4) |

**Final check before the report** (`03_workflow.md`).
1. Uncombined chains: every key reached by chains from other sections (announcement, earmark, parking, U1) is in the table above; the opposing chains on residents', carriers' and ride-hail full costs, zone sales, property values and bus crowding are combined.
2. Group signs: zone garages (price or quantity, C-44) and the general-fund beneficiaries (taxpayers or other spending, C-40) are groups.
3. Baseline: every sign is against no charge with the same parking and budget rules; residents' $1.50 is an increase against $0, not a decrease against $15.
4. Worse off is not poorer: `resources_available_other_uses` is signed only for those who keep paying (C-33) and for the reserves (C-31); switchers are not signed.
5. Timing shifts: trips in and outside charging hours are signed per window (C-7, C-11).
6. Both sides of every transfer: charge paid (C-33, C-2) and received (C-3); earmark (C-4) and freed general-fund money (C-40); reserves advanced and repaid (C-31); asset-value gains and losses are both recorded (C-43 and C-45, C-47 and C-49).
7. Every actor class, every core rule: CR-7c was applied to garages, homes and shop property; CR-6 to road space, buses, garages, ride-hail and the PAO; enforcement costs and the payer's side are recorded.
8. Unstated premises: four added (A-N1 to A-N4), all flagged.

CR-12f does not apply: no provision undoes another. Different variables (travel_time and price_paid for continuing drivers; quality_per_unit and travel_time for bus riders) are not netted (CR-12c).

## 8. Time structure

- **Announcement window (4 January to 31 October 2027).** The charge was certain ten months before it started (CR-10a). Asset values move when the charge becomes expected, not when it starts (CR-7c, CR-10c): zone garages fall (C-45), Ringside garages and Ringside and Merrowdale retail property rise (C-43, C-47), and zone homes and commercial property move in an ambiguous direction (C-49, C-50). Zone workers who plan to move in can do so before November (C-28). Organized groups lobby from January (C-29), including over the reading of §7 (U1). Transit can order buses on announcement, but they arrive 14 to 18 months later (A-28), so the first year of charging has more riders and no more buses (C-34).
- **Timing of trips.** Vehicle-days in weekday charging hours decrease (C-7); trips before 7:00, after 19:00 and at weekends increase (C-11). Each window is signed against the counterfactual (`02_ontology.md`, 2.5). Because one charge covers the whole day, those who still enter bundle errands into fewer days (C-19 for carriers; for car drivers the same CR-4c argument applies, with no separate variable recorded).
- **First-year repayment.** The $70 million set-up cost is advanced from reserves in 2027 and repaid from the first year's revenue (C-31), so less of the first year's revenue reaches buses than of later years' revenue.
- **Durability.** Garages (A-21), homes and shop premises are durable, so their owners bear or capture the change in expected yields (CR-7b, CR-7c); Ringside's garage capacity cannot grow within a year (A-6), so the Ringside price rise (C-41) is short and medium run, and may fade as capacity is added. The bus fleet grows only after 14 to 18 months (A-28), which is why crowding is signed only in the short run (C-34) and is ambiguous after (C-35).
- **Three-yearly review.** The level may change at each review; buyers of property expect the charge to last (A-20), so the capitalized changes are close to full.
- Persistence: not a repeal; not recorded.

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
| --- | --- | --- | --- | --- | --- |
| C-7 | drivers.non_resident.switching | quantity_demanded (zone vehicle-days, weekday charging hours) | decrease | Trips into the zone that both the driver and the zone's sellers (parking, shops) expected to gain from | CR-5a |
| C-13 | drivers.non_resident.switching | travel_time (door to door) | increase | Time by bus or by walking from Ringside, given up from other ends | CR-3a, CR-8c |
| C-23 | keepers.cloned_plates | compliance_cost | increase | Time spent contesting notices for trips they did not make | CR-8c |
| C-29 | organized_groups | lobbying_effort | increase | Staff time and money spent lobbying | CR-8c |
| C-30 | officials.cco | enforcement_cost | increase | About $45 million a year that would otherwise have gone to buses or stayed with drivers | CR-8c |
| C-31 | city_reserves | resources_available_other_uses | decrease | $70 million held for one year | CR-8a |
| C-32 | all paying keepers | compliance_cost | increase | Time spent paying and keeping registration current | CR-8c |
| C-33 | drivers.non_resident.continuing, carriers.long_visit | resources_available_other_uses | decrease | About $300 million a year of purchases or saving | CR-8a, CR-8b |
| C-54 | appellants.pao | wait_time | increase | Time waiting for hearings at a fixed budget | CR-6, CR-8c |

CR-8b is applied to every transfer: the charge paid (C-33, and by residents C-2) is received by the city (C-3), which pays the CCO (C-30), repays reserves (C-31) and passes the rest to bus services (C-4), freeing general-fund support for other uses (C-40). The switchers do not pay the charge; they are worse off by their own ranking (CR-3a, through C-13) but are not signed on `resources_available_other_uses` (CR-3, note).

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
| --- | --- | --- | --- | --- | --- |
| A-1 | Some drivers who now enter the zone on weekdays value the day there by less than $15 more than its other costs, at today's speeds (the charge binds, and the response is partial). | binding | 0.95 | Trip surveys; the city model (88,000 against 118,000). | C-6, C-7, C-14, C-25, C-36, C-44, C-45, C-55 fail. |
| A-2 | The charge is enforced: cameras read most plates and penalties are collected. | enforcement | 0.85 | 74 entry and 40 internal camera points; $130 penalty. | C-1 to C-4, C-7, C-14 to C-16, C-20, C-21, C-33, C-54 fail. |
| A-3 | Fewer vehicles in the zone raise speeds for those that remain. | other | 0.85 | City traffic model; road closures and holidays. | C-6, C-36 fail; C-14 to C-17, C-20, C-52 lose a chain. |
| A-4 | For most car trips into the zone, the time saved by faster roads is worth much less than $15. | other | 0.8 | About 8 minutes a day; wage levels. | C-14 becomes ambiguous. |
| A-5 | Some drivers switch to bus, tram or Ringside parking. | substitutability | 0.9 | 62% already use transit; Ringside 5 to 10 minutes' walk. | C-8, C-9, C-13, C-34, C-35, C-37, C-41 to C-43 fail. |
| A-6 | Ringside's garages, about 88% full, cannot add spaces within a year. | durability | 0.75 | About 900 spare spaces; planning times. | C-9, C-41 to C-43 fail or become a quantity change only. |
| A-7 | Some shoppers who drove into the zone buy instead in Ringside or Merrowdale, where they can park. | other | 0.7 | Shopper surveys. | C-46, C-47 fail; C-48, C-49 lose the (-) chain. |
| A-8 | General-fund support for buses is cut by less than the earmark, so bus service rises. | revenue_use | 0.7 | Earmark about $230 to $260 million against $140 million. | C-4, C-5, C-38, C-39 fail; C-35, C-48, C-49 lose a chain. |
| A-9 | The council reduces general-fund support for buses below what it would otherwise have been. | revenue_use | 0.7 | No maintenance-of-effort clause; budget pressures. | C-40 fails. |
| A-10 | More frequent buses bring to zone shops some visitors who would not otherwise have come. | other | 0.55 | Earlier service changes. | C-48, C-49 lose the (+) chain. |
| A-11 | Some non-residents can register a vehicle to a zone address without detection. | enforcement | 0.6 | Registration by declaration; rare audits. | C-24 fails. |
| A-12 | Some deliveries cannot be completed within 30 minutes. | other | 0.85 | 12,000 of 19,000 goods vehicles stay longer. | C-18 to C-21 fail. |
| A-13 | Under U1-b some rounds can be reshaped into visits under 30 minutes. | other | 0.7 | Many drops near the edge; Ringside depots. | C-18 (U1-b) fails. |
| A-14 | Carriers have better alternatives (customers elsewhere) than zone businesses have (premises elsewhere). | substitutability | 0.65 | Carriers serve the region; leases. | C-21 fails. |
| A-15 | Zone retailers, delivery firms, Ringside residents and the transit union can organize at a cost below their stakes. | other | 0.85 | Existing associations; 2026 hearings. | C-29 fails. |
| A-16 | Some drivers evade (foreign, cloned or obscured plates). | enforcement | 0.6 | Camera enforcement elsewhere. | C-22, C-23 fail. |
| A-17 | Some weekday trips can move to before 7:00, after 19:00 or to weekends. | other | 0.7 | Shopping hours; shift work. | C-11 fails. |
| A-18 | Some through traffic diverts to the Inner Ring Road. | mobility | 0.85 | About a tenth of vehicle-days are through trips. | C-12, C-53 fail. |
| A-19 | Some zone workers commute by car and cannot switch cheaply, and zone employers compete with employers elsewhere for them. | other | 0.55 | 22% drive; shift workers. | C-51 fails. |
| A-20 | Buyers of property expect the charge to last. | expectations | 0.75 | No expiry; review of the level only. | C-43, C-45, C-47 shrink to the yields of the expected duration (CR-7c); signs unchanged. |
| A-21 | Zone garages cannot be converted to other uses within a year. | durability | 0.8 | Structure and planning rules. | C-45 smaller; sign unchanged in the short run. |
| A-22 | Some residents who drive in the zone would have moved out of it within a few years. | mobility | 0.6 | Household turnover. | C-27 fails. |
| A-23 | For most who switch, the trip by bus or by Ringside parking and walking takes longer than by car. | other | 0.8 | Bus commute about 15 minutes longer. | C-13 fails. |
| A-24 | The PAO's budget is not raised for the new appeals, and its net caseload rises (about 9,000 new appeals against about 2,800 fewer). | revenue_use | 0.8 | No funds in the ordinance; projected rates. | C-54 fails. |
| A-25 | Some drivers switch to ride-hail or taxis. | substitutability | 0.6 | Current use; parking costs. | C-10 fails; C-52 loses a chain. |
| A-26 | Ride-hail supply into the zone at peak cannot expand at an unchanged cost at once. | durability | 0.6 | Surge pricing now. | C-52 loses a chain. |
| A-27 | Some people who work in the zone and drive would move into it to pay $1.50 rather than $15. | mobility | 0.55 | Car commuters' household moves. | C-28 fails; C-50 loses its (+) chain. |
| A-28 | Calderford Transit cannot add buses for at least a year. | durability | 0.8 | Order books; 14 to 18 months. | C-34 fails; C-5 and C-39 come earlier. |
| A-29 | The gap in door-to-door time between car and bus far exceeds what faster roads save the bus. | other | 0.75 | Timetables; city model. | C-13 relies on A-23 alone for bus switchers. |
| A-30 | The loss of car shoppers dominates the gain from new visitors in zone sales. | other | 0.4 | No direct evidence. | Below cut-off: not used. |
| A-N1 | For a delivery visit under 30 minutes, the time saved by faster roads (a few minutes) is worth much less than $15. | other | 0.85 | NEW. At most 30 minutes in the zone, 12 to 15 km/h, so a few minutes saved; same wage evidence as A-4. Flagged: added by this analysis. | C-17 (U1-a) becomes ambiguous. |
| A-N2 | Some carriers can consolidate zone deliveries into fewer vehicle-days (more drops per charged day). | other | 0.7 | NEW. One charge covers any number of entries in a day; carriers already plan rounds; Ringside depots. Flagged. | C-19 fails. |
| A-N3 | Some zone residents value keeping a car at a zone address by less than $1.50 a day more than their next-best (giving it up, keeping it outside the zone, or moving out). | substitutability | 0.6 | NEW. 14,500 cars at zone addresses but only about 9,500 resident cars in the zone on a weekday, so many are little used; car-sharing and transit in the zone. Flagged. | C-26 fails; C-50 loses its (-) chain. |
| A-N4 | Within the first year, Calderford Transit uses faster running in the zone to run more trips with the same fleet, enough to offset the added riders. | other | 0.35 | NEW. Only the zone part of each route is faster; timetables are set in advance; peak load already 85%. Flagged. Below cut-off. | If true, C-34 becomes ambiguous. |

**Not reported** (an assumption below 0.5):
- Zone retail sales decrease (C-48 signed by dominance): needs A-30 (p 0.4).
- Bus crowding in the first year ambiguous rather than worse: needs A-N4 (p 0.35); the derived sign (C-34) is reported and this chain is recorded here (CR-12, 0.8 note, kind 2).

## 11. Report

**The policy:** From 1 November 2027, the keeper of any vehicle driven or parked in Calderford's central zone on a weekday between 7:00 and 19:00 pays $15 for that day ($1.50 for keepers registered at a zone address); scheduled buses and emergency vehicles are exempt. Cameras enforce it, with a $130 penalty. The revenue, after the charging office's costs, goes to bus services. Whether a delivery visit under 30 minutes pays is unclear (U1).

**Visible consequences:** Drivers and residents pay to enter or park (C-1, C-2); the city collects revenue (C-3) and bus services receive more money in total (C-4) and, once new buses arrive, buses run more often (C-5); fewer vehicles enter in charging hours (C-7) and those that remain move faster (C-6), as do buses (C-36). More people ride buses and trams (C-8, C-37).

**Invisible consequences:**
- *Drivers who stop driving in:* take longer door to door (C-13), use Ringside garages, ride-hail or other hours (C-9, C-10, C-11). Through traffic moves to the Inner Ring Road (C-12), which becomes slower (C-53).
- *Drivers who keep driving in:* pay more in full, even counting faster roads (C-14), and have less to spend on other things (C-33).
- *Carriers and zone businesses:* carriers put more drops into each charged day (C-19); zone businesses bear more of the charge on deliveries than carriers do (C-21). U1 decides short visits: under U1-a they pay $15 and their full cost rises; under U1-b they pay nothing, gain speed, and long rounds are reshaped into short visits (C-16 to C-18).
- *Parking:* Ringside garage prices and values rise, and existing Ringside parkers pay more (C-41 to C-43); zone garages earn less and lose value from the announcement (C-44, C-45). City parking fines fall (C-55).
- *Shops outside:* Ringside and Merrowdale sell more and their property gains value (C-46, C-47).
- *Residents:* fewer cars kept at zone addresses (C-26); residents who would have moved out stay (C-27); zone workers who drive move in (C-28).
- *Workers and employers:* zone employers pay more to car-commuting staff who cannot switch (C-51).
- *Buses:* existing riders face more crowding in the first year (C-34); new buses are ordered and more bus staff hired later (C-38, C-39); general-fund money freed by the earmark goes to taxpayers or other spending (C-40).
- *Administration and evasion:* the charging office uses about $45 million a year (C-30); reserves are tied up for a year (C-31); keepers spend time paying (C-32); some evade with foreign, cloned or obscured plates (C-22), and keepers whose plates are cloned contest notices (C-23); some register falsely at zone addresses (C-24); revenue falls short of a static projection (C-25); appeals wait longer at the PAO (C-54). Organized groups lobby (C-29).

**Ambiguous effects:** Zone retail sales (C-48) and zone commercial property values (C-49): car shoppers lost against bus visitors gained, decided by how much bus service is actually added. Zone home values (C-50): car-commuting workers moving in against residents giving up cars or leaving. Residents' and multi-drop carriers' full cost per day (C-15, C-20): the charge against the time saved. Bus crowding after the first year (C-35): more riders against more service. Ride-hail prices (C-52): the charge and added demand against faster trips.

**Key conditions:** The charge binds (A-1, 0.95) and is enforced (A-2, 0.85); roads speed up (A-3, 0.85) but by much less than $15 is worth to a typical driver (A-4, 0.8); general-fund support is cut by less than the earmark (A-8, 0.7). Four premises were added: short visits gain little time (A-N1, 0.85), carriers can consolidate (A-N2, 0.7), some residents give up cars at $1.50 a day (A-N3, 0.6), and the first-year capacity offset from faster buses (A-N4, 0.35, below the cut-off).

**What this analysis cannot say:** The size of any effect; whether zone shops gain or lose on balance; how the charge on deliveries reaches shop prices; whether the gains to those who keep driving and to bus riders outweigh the losses to those priced off the roads; whether the policy is good. Environmental, health and safety effects (air quality, accidents, noise in the zone and on the Inner Ring Road) are out of scope.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C-1 | drivers.non_resident | price_paid (zone vehicle-day, charging hours) | increase | short; medium; long | visible | B | CR-1 (op 3: K1 attaches $15 to each weekday in the zone); CR-5c (the charge moves the terms of entering against the counterfactual of no charge); enforcement makes it paid (A-2) | A-2 |
| C-2 | residents.zone_keepers | price_paid (zone vehicle-day, charging hours) | increase | short; medium; long | visible | B | CR-1 (op 3: K2 attaches $1.50, against $0 in the counterfactual) | A-2 |
| C-3 | officials.cco (city) | tax_revenue | increase | short; medium; long | visible | B | CR-1 (op 3); CR-8b (every payment is a receipt: the city receives what keepers pay) | A-2 |
| C-4 | calderford_transit | subsidy_outlay (total funding of bus services) | increase | medium; long | visible | B | CR-1 (op 4: K3 transfers net revenue to buses); CR-8d (earmarked money frees general-fund money, so the total rises only if support is cut by less than the earmark: A-8); CR-12e (A-8 as dominance premise) | A-2, A-8 |
| C-5 | bus_riders | wait_time (time between buses at stops on routes into the zone) | decrease | medium; long | visible | B | CR-1 (op 4: K3 transfers net revenue to bus services); CR-8d with A-8 (total bus funding rises); CR-9 and LW-10 (more funding buys more buses and drivers, which run more often once the buses arrive, A-28); CR-6 public-supply clause (the operator supplies a fixed quantity at a set fare; added frequency lowers the wait between buses) | A-8, A-28 |
| C-6 | vehicles remaining in the zone | travel_time (in the zone, charging hours) | decrease | short; medium; long | visible | B | CR-4b (marginal drivers stop entering, A-1); CR-6 public-supply clause (road space is supplied by the city at a zero money price; the charge raises the price, so the pressure on the crowding margin, time of travel, falls); CR-9 (shared_facility: remaining users share the road; A-3) | A-1, A-3 |
| C-7 | drivers.non_resident.switching | quantity_demanded (zone vehicle-days, weekday charging hours) | decrease | short; medium; long | visible | B | CR-4b (drivers for whom a zone day was ranked narrowly above the alternatives switch away, A-1); CR-4c (fewer days per driver); CR-5a (trips that would have been made are not) | A-1, A-2 |
| C-8 | drivers.non_resident.switching | quantity_substitute (bus and tram trips) | increase | short; medium; long | visible | B | CR-4 (x: drive in, y: bus or tram; x made worse; CR-4a: none switch the other way) | A-5 |
| C-9 | drivers.non_resident.switching | quantity_substitute (Ringside garage parking) | increase | short; medium; long | invisible | B | CR-4 (x: park in the zone, y: park in Ringside and walk); quantity limited by about 900 spare spaces (A-6), so part of the shift goes to price (C-41) | A-5, A-6 |
| C-10 | drivers.non_resident.switching | quantity_substitute (ride-hail and taxi trips into the zone) | increase | short; medium; long | invisible | B | CR-4 (x: own car, y: ride-hail; the ride-hail car's charge is spread over its trips that day) | A-25 |
| C-11 | drivers.non_resident (trips movable in time) | quantity_demanded (trips before 7:00, after 19:00 and at weekends) | increase | short; medium; long | invisible | B | CR-4 (x: weekday charging hours, y: other hours; y made relatively better); timing signed per window with C-7 (02_ontology.md, 2.5) | A-17 |
| C-12 | drivers.through | quantity_substitute (Inner Ring Road trips) | increase | short; medium; long | invisible | B | CR-4 (x: cross the zone and pay, y: go round on the Inner Ring Road) | A-18 |
| C-13 | drivers.non_resident.switching | travel_time (door to door) | increase | short; medium; long | invisible | B | CR-3a (switchers fall back to an option ranked lower); CR-4b; the bus or Ringside trip takes longer (A-23), and faster roads do not close the gap for bus riders (A-29; CR-12e: the time saved by the bus is a response that cannot reverse the switch) | A-5, A-23, A-29 |
| C-14 | drivers.non_resident.continuing | full_cost_per_unit (zone vehicle-day) | increase | short; medium; long | invisible | B | CR-12b: (+) $15 (CR-1 op 3); (-) time saved (C-6) and any fall in zone parking prices (C-44). Dominance (CR-12e): empirical premise A-4 against the time chain; response argument against the parking chain (the parking price falls because fewer drive and cannot fall so far as to reverse the fall in driving) | A-1, A-2, A-3, A-4 |
| C-15 | residents.zone_keepers | full_cost_per_unit (zone vehicle-day) | ambiguous | short; medium; long | invisible | B | CR-12b: (+) $1.50 (CR-1 op 3); (-) time saved (C-6, A-3); no premise compares the two | A-2, A-3 |
| C-16 | carriers.short_visit | price_paid (zone access per short visit) | U1-a: increase; U1-b: no_change | short; medium; long | visible | B | CR-1 per reading (U1-a: op 3, $15 per day; U1-b: no operation on the charge); CR-5c | A-2 |
| C-17 | carriers.short_visit | full_cost_per_unit (short delivery visit) | U1-a: increase; U1-b: decrease | short; medium; long | invisible | B | U1-a: CR-12b, (+) $15 against (-) a few minutes saved; dominance by A-N1 (CR-12e, empirical). U1-b: only the (-) chain, CR-6 public-supply clause and C-6 (A-3) | A-3, A-N1 |
| C-18 | carriers.long_visit | reclassification (rounds reshaped into visits under 30 minutes) | U1-a: no_change; U1-b: increase | short; medium | invisible | B | CR-4 per reading (U1-b: x: long visit at $15, y: several short visits at $0; carriers for whom they were close switch, A-13; U1-a: both pay $15, no change in ranking) | A-12, A-13 |
| C-19 | carriers.long_visit | transaction_size (drops per vehicle-day in the zone) | increase | short; medium | invisible | B | CR-4c (the charge is per day, not per entry or drop: the first drop of a day bears $15, later drops nothing, so carriers move drops onto days already charged); CR-1 0.9 (operation per range) | A-12, A-N2 |
| C-20 | carriers.long_visit | full_cost_per_unit (vehicle-day of a multi-drop round) | ambiguous | short; medium; long | invisible | B | CR-12b: (+) $15 (CR-1 op 3); (-) about 40 minutes a day saved (C-6, A-3); A-4 covers car trips only | A-2, A-3, A-12 |
| C-21 | zone_businesses | tax_share_borne (charge on deliveries, against carriers) | increase | medium; long | invisible | B | CR-7b (the burden settles more on the side with worse alternatives: carriers serve other customers, zone businesses are tied to premises, A-14); CR-5c | A-2, A-12, A-14 |
| C-22 | evaders | legal_breach (unpaid charges: foreign, cloned, obscured plates) | increase | short; medium; long | invisible | B | CR-4 (x: pay, y: evade; y made relatively better by a charge where evasion costs less than $15 in expected penalty; CR-4a: none become more compliant); CR-12 0.9 (an activity existing only under the policy) | A-16 |
| C-23 | keepers.cloned_plates | compliance_cost (contesting notices for others' trips) | increase | short; medium; long | invisible | B | CR-9 (contract: the vehicle register links a plate to its keeper, so an evader's trip lands on the keeper); CR-1 op 3; CR-8c | A-16 |
| C-24 | evaders (non-residents) | reclassification (vehicles registered to zone addresses) | increase | short; medium; long | invisible | B | CR-4 (x: register truthfully and pay $15, y: declare a zone address and pay $1.50; residence is by declaration) | A-11 |
| C-25 | officials.cco (city) | tax_revenue_vs_static_projection | decrease | short; medium; long | invisible | B | CR-4b (vehicle-days fall, A-1); further independent chains: evasion (A-16), false registration (A-11), and under U1-b the unpaid short visits; CR-12d (holds if any chain holds) | A-1 |
| C-26 | residents.zone_keepers | quantity_demanded (cars kept at zone addresses) | decrease | medium; long | invisible | B | CR-4b (x: keep a car at a zone address, y: give it up or keep it outside; x costs $1.50 a weekday more); CR-4c | A-N3 |
| C-27 | residents.zone_keepers (who would have moved) | turnover (moves out of the zone) | decrease | medium; long | invisible | B | CR-4 (x: move out and pay $15 to drive in, y: stay and pay $1.50; y made relatively better); CR-3a for those who stay against their earlier plan | A-22 |
| C-28 | residents.zone_prospective | quantity_demanded (zone housing) | increase | short (from announcement); medium; long | invisible | B | CR-4 (x: live outside and pay $15, y: move in and pay $1.50); CR-10a (moves can be made before charging starts) | A-27 |
| C-29 | organized_groups | lobbying_effort | increase | short (from announcement); medium; long | invisible | B | CR-4 (x: accept, y: lobby; retailers and carriers against the charge or for the U1-b reading, Ringside residents for parking controls, the union to keep the earmark); CR-8c | A-15 |
| C-30 | officials.cco | enforcement_cost | increase | short; medium; long | invisible | A | CR-1 (op 4: about $45 million a year); CR-8c (resources spent on administering and enforcing are used up) | none |
| C-31 | city_reserves | resources_available_other_uses | decrease | short (2027 to first-year repayment) | invisible | A | CR-1 (op 4: $70 million advanced); CR-8a; repaid from the first year's revenue, so the effect is one-year only (CR-12g) | none |
| C-32 | all paying keepers | compliance_cost (paying by midnight next day, keeping registration current) | increase | short; medium; long | invisible | A | CR-1 (op 3: the duty to pay is attached to every charged day); CR-8c | none |
| C-33 | drivers.non_resident.continuing, carriers.long_visit | resources_available_other_uses | decrease | short; medium; long | invisible | B | CR-3 (note: they keep choosing the burdened option and pay); CR-8a and CR-8b (what they pay to the city is not available for their other uses) | A-2 |
| C-34 | bus_riders (existing) | quality_per_unit (crowding on routes into the zone) | decrease | short | invisible | B | CR-9 (car trips substitute for bus trips; riders share fixed capacity); CR-6 public-supply clause (the fare is fixed by an existing rule and the fleet cannot grow, A-28, so added riders go to crowding); CR-12e 0.8 (riders already aboard can be worse off though new riders cannot reverse the switch); opposing chain A-N4 below cut-off | A-5, A-28 |
| C-35 | bus_riders | quality_per_unit (crowding on routes into the zone) | ambiguous | medium; long | invisible | B | CR-12b: (-) more riders (A-5); (+) more service funded by K3 (A-8); no dominance premise | A-5, A-8 |
| C-36 | bus_riders | travel_time (bus running time in the zone) | decrease | short; medium; long | visible | B | CR-9 (shared_facility: buses share road space); CR-6 public-supply clause as in C-6 | A-1, A-3 |
| C-37 | calderford_transit | quantity_traded (bus and tram trips) | increase | short; medium; long | visible | B | CR-9 (relation: substitute, close); CR-5 (trips sold that would not have been) | A-5 |
| C-38 | bus_makers | quantity_traded (new buses ordered) | increase | short; medium | invisible | B | CR-9 and LW-10 (relation: buses input_to bus service; more funding raises demand for buses) | A-8 |
| C-39 | transit_workers | employment (bus operation) | increase | medium; long | invisible | B | CR-9 and LW-10 (relation: labor input_to bus service); after new buses arrive (A-28) | A-8, A-28 |
| C-40 | taxpayers / recipients of other general-fund spending | resources_available_other_uses | at_least_one_increase | medium; long | invisible | B | CR-8d (money earmarked for buses frees general-fund support; A-9); CR-8b (the freed money goes to some other use, as lower taxes or other spending, not said which: group sign) | A-9 |
| C-41 | ringside_garages | net_price_received (Ringside garage parking) | increase | short; medium | invisible | B | CR-9 (relation: substitute); CR-6 (fixed capacity, A-6: the free price rises to ration it; 0.8 note: a free price's rise is enough) | A-5, A-6 |
| C-42 | ringside_parkers.existing | price_paid (Ringside garage parking) | increase | short; medium | invisible | B | CR-9 (they compete with switchers for the same spaces); CR-6 | A-5, A-6 |
| C-43 | ringside_garages | asset_value (garages) | increase | short (from announcement) | invisible | B | CR-10c and CR-7c (the expected rise in yield, C-41, is captured by whoever owns the garages when the charge becomes expected, 4 January 2027) | A-5, A-6, A-20 |
| C-44 | zone_garages | net_price_received, quantity_traded (zone off-street parking) | at_least_one_decrease | short; medium; long | invisible | B | CR-9 (relation: parking complement of zone vehicle-days); LW-10; CR-6 0.9 (a fall in demand gives the direction; how it splits between price and quantity needs a premise, so a group) | A-1 |
| C-45 | zone_garages | asset_value (garages) | decrease | short (from announcement) | invisible | B | CR-10c and CR-7c (the expected fall in yield, C-44, is borne by the owners when the charge becomes expected); CR-7b and CR-10b (garages cannot move to other uses, A-21) | A-1, A-20, A-21 |
| C-46 | ringside_merrowdale_shops | quantity_traded (retail sales) | increase | short; medium; long | invisible | B | CR-9 (relation: across_border substitute, with trip complements: shoppers who move buy their other goods there too); CR-4 | A-7 |
| C-47 | property_owners.ringside_merrowdale_retail | asset_value (retail property) | increase | short (from announcement) | invisible | B | CR-10c and CR-7c (expected rise in shop yields, C-46, captured at announcement) | A-7, A-20 |
| C-48 | zone_businesses (retail) | quantity_traded (retail sales in the zone) | ambiguous | short; medium; long | invisible | B | CR-12b: (-) CR-9, car shoppers and their trip complements move to Ringside and Merrowdale (A-7); (+) CR-9, more frequent buses bring new visitors (A-8, A-10). A-30 (p 0.4) cannot serve as dominance premise | A-7, A-8, A-10 |
| C-49 | property_owners.zone_commercial | asset_value (shop and office property) | ambiguous | short (from announcement); medium | invisible | B | CR-7c and CR-10c applied to C-48 (ambiguous) and to C-21 (delivery charge borne by zone businesses); CR-12 0.8 kind (3): an ambiguous chain makes the total ambiguous | A-7, A-8, A-10, A-14, A-20 |
| C-50 | property_owners.zone_homes | asset_value (homes in the zone) | ambiguous | short (from announcement); medium | invisible | B | CR-12b: (+) CR-7c on C-28 (car-commuting workers move in, A-27); (-) CR-7c on C-26 (residents for whom a zone car is not worth $1.50 a day give it up or leave, A-N3); no dominance premise | A-20, A-27, A-N3 |
| C-51 | workers.zone_car_commuters | wage_rate (zone jobs) | increase | medium; long | invisible | B | CR-9 (contract: employment); CR-7b (workers who cannot switch and are sought by employers elsewhere shift part of the charge to zone employers, A-19); CR-5c | A-19 |
| C-52 | ride_hail_and_taxi (riders) | price_paid (ride-hail trips into the zone) | ambiguous | short; medium | invisible | B | CR-12b: (+) $15 per vehicle-day attached to each car (CR-1 op 3, CR-7b); (+) more riders with supply fixed at once (CR-6, A-25, A-26); (-) faster roads, more trips per car-hour (C-6, A-3) | A-3, A-25, A-26 |
| C-53 | inner_ring_users | travel_time (Inner Ring Road, peak) | increase | short; medium; long | invisible | B | CR-9 (relation: substitute route, shared_facility); CR-6 public-supply clause (road space at zero price: more users, more crowding) | A-18 |
| C-54 | appellants.pao | wait_time (parking and charge appeals) | increase | short; medium; long | invisible | B | CR-6 public-supply clause (the PAO supplies hearings at a fixed budget; more appeals go to waiting); CR-12b with CR-12e arithmetic (about 9,000 more against about 2,800 fewer, A-24) | A-2, A-24 |
| C-55 | city (parking enforcement) | non_tax_receipts (zone parking fines) | decrease | short; medium; long | invisible | B | CR-9 (relation: parking tickets follow cars parked in the zone); CR-4b (fewer cars, A-1) | A-1 |

## Gaps found

**(a) Steps no core rule covers.**
- GAP-046-C1: How a charge on deliveries reaches the prices zone shops charge their own customers. CR-7b ranks carriers against zone businesses (C-21) and CR-9 names the relation (deliveries input_to retail), but signing shop prices needs a premise on shops' alternatives against their customers', which the case lacks; the chain was stopped at depth 3.
- GAP-046-C2: Trip bundling by car drivers under a per-day charge. CR-4c gives the direction (more errands per charged day), but no variable in 2.4 records "trips per day for households", so it is a note in section 8 only; for carriers `transaction_size` was used.

**(b) Core-rule wording that was hard to apply.**
- CR-9 (0.7) puts chains through a `shared_facility` such as a road at Tier C, but CR-6's public-supply clause names "crowding, time of travel" as the margin to which pressure on a fixed public supply goes, at Tier B. The road speed effects (C-6, C-36, C-53), bus crowding (C-34) and the PAO queue (C-54) were derived through CR-6 at Tier B; under CR-9 alone they would be Tier C. The rules should say which governs where the shared facility is itself a public supply at a set price.
- CR-12e's response argument for C-14: the fall in zone parking prices is a response to the charge, but it runs through a different market (parking) from the one charged (vehicle-days). It was read as covered (the parking price falls only because fewer drive), but the clause speaks of a response "in" the market of the change.
- CR-1 operation 3 on a per-day charge with free re-entry: the 0.9 note on thresholds (a charge per worker capped per firm) was used by analogy for "first drop of the day bears the charge, later drops none" (C-19). An explicit note on charges per period rather than per unit would help.
- CR-8d with a maintenance-of-effort question (A-8, A-9): CR-8d says earmarked money frees other money "unless the other spending is also fixed", but gives no guidance for the total when the earmark exceeds the existing spending. Signed with A-8 as a dominance premise.

**(c) Vocabulary missing from the ontology.**
- No variable for trips or errands per day (trip bundling).
- No variable for the crowding of a public service other than `quality_per_unit` and `wait_time`; `quality_per_unit` (crowding) was used for buses.
- No actor class for keepers whose identity is used by evaders (cloned plates); `keepers.cloned_plates` was coined.
