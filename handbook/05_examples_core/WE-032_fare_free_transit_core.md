# WE-032 / Analysis: Port Hallam Fare-Free Transit Act (fare-free buses and trams funded by an employer payroll tax)

Analyst: core-only re-run (Handbook 0.7)  |  Rules: core rules CR-1 to CR-12 only  |  Status: compared

## 1. Policy record

**Port Hallam Fare-Free Transit Act.** Port Hallam is a city of about 620,000 people in a metropolitan area of 1.3 million. Its western boundary lies 4 to 8 km from downtown; the suburban municipalities of Westmere and Calder Vale begin there, with business parks and two car-oriented shopping malls just across the line. Port Hallam Transit (PHT), a city-owned authority, runs 4 tram lines and 62 bus routes, two of which run 3 km into Westmere. In 2026 PHT carried 92 million boardings. It collected $58 million in fares (single fare $2.00, monthly pass $70) against operating costs of $240 million. Fare collection cost about $13 million a year: $6 million for the fare-card system contract, $3 million for cash handling and ticket offices, and $4 million for fare inspection. Collection employed 140 staff: 85 inspectors and 55 ticket-office and cash staff.

Seniors over 65 and school pupils already ride free; they account for about 22% of boardings. About 5% of boardings were estimated to be fare evasion. 260 employers buy discounted annual passes for about 31,000 staff, at about $9 million a year.

At the morning peak, tram lines 1 and 4 and bus route 12 run at about 95% of planning capacity (four standing passengers per square meter); crush load is about six per square meter. Most other lines run at 60 to 75% of planning capacity at the peak. Off-peak occupancy averages 35%.

Taxi fares are set by a city meter rate. Ride-hail prices are not regulated. A private bike-share scheme charges $1 a ride. Regional commuter rail is run by the province and is not part of PHT.

| Field | Value | Source sentence |
| --- | --- | --- |
| Jurisdiction (and what lies just outside) | City of Port Hallam. Just outside: Westmere and Calder Vale, with business parks and two car-oriented malls just across the western line, 4 to 8 km from downtown; two PHT routes run 3 km into Westmere. Regional commuter rail (province) is outside the Act. | "Its western boundary lies 4 to 8 km from downtown ..." |
| Announced / enacted / effective / expires | Expected from the mayor's campaign; bill introduced 10 Feb 2027; enacted 28 Apr 2027; payroll tax on wages paid from 1 Jul 2027, collected quarterly from Oct 2027; fares end 1 Sep 2027. K2 runs to the end of FY 2028-29, then a council review. No expiry for K1 or K3. | "The council introduced the bill on 10 February 2027 ..." |
| Enforcement (who, penalties, resources) | City Revenue Department collects K3 (quarterly returns; 10% penalty plus interest on late payment), keeping 1.5% of revenue for administration. Fare inspection ends. | "Quarterly returns to the City Revenue Department ..." |
| Revenue use | K3 to PHT less 1.5%. Above $58 million: held in a Transit Reserve for service expansion after the review. Below $58 million: shortfall covered from the city's general fund. | "Revenue use: ..." |
| Existing rules | City taxi meter rate; $4 park-and-ride fee (kept); free travel for seniors and pupils (now subsumed). | Policy record. |

| Component | Instrument | Target | Bound | Parameters | Exemptions |
| --- | --- | --- | --- | --- | --- |
| K1 Fare abolition | `public_supply` at a zero price (2.3 now lists this type), funded from K3 | Rides on all PHT buses and trams, including the two routes into Westmere | PHT | Fare $0 for every rider from 1 Sep 2027. Fare inspection ends. Unused value on passes bought before then refunded pro rata on application. | Regional commuter rail not covered. Park-and-ride lots keep their $4 daily fee. |
| K2 Service freeze | Budget rule fixing the quantity supplied (part of `public_supply`) | PHT service hours | PHT | Held at the 2026-27 timetable for FY 2027-28 and 2028-29; then a council review. | None |
| K3 Payroll tax | `ad_valorem_tax` on labor | Gross wages paid to employees at a worksite in the city | Private employers with a city worksite and annual payroll above $750,000 | 0.40% of gross city payroll; a cliff (once over the threshold, all city payroll is taxed). Projected $61 million a year. | Public employers, registered charities, employers at or below the threshold. |
| K4 Fare-system wind-down | Administrative provision | PHT's fare-collection operation | PHT | Fare-card contract terminated with a $5 million payment. Fare staff redeployed to customer-service and safety roles "where possible"; the rest receive severance. | None |

Unclear provisions:
- **U1.** Whether the $750,000 threshold is measured on total payroll (U1-a) or city payroll only (U1-b). The tax base is city payroll under both. Signs that depend on it are given per reading.
- How many fare staff are redeployed: treated as an assumption (A-19), since the record supplies evidence.

Counterfactual: the same city with the same 2026-27 timetable, fares at $2.00 and the $70 pass, and no payroll tax. Out of scope: environmental effects, health effects of walking and cycling, safety on crowded vehicles. Congestion's effect on road users is recorded only through `wait_time`.

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | CR-1 operations | Core rules applied |
| --- | --- | --- | --- | --- |
| K1 Fare abolition | binary (the state gives a service at no charge) | Yes: removes a $2 charge every fare-paying rider paid; no effect on the money price for exempt riders and evaders | 3 (the $2 charge attached to the option "ride PHT" is removed, for fare payers); 2 (riding legally without paying is added, for evaders); 4 (pre-paid pass value refunded); 1 (the exchange "buy a fare or pass" is removed) | CR-2, CR-3, CR-4, CR-5a, CR-6 (public supply), CR-7, CR-9, CR-10, CR-11a |
| K2 Service freeze | binary (fixes the quantity of the public supply) | Not against the counterfactual (same timetable); it binds by closing the supply response to K1 (A-4) | none for riders against the counterfactual; for PHT it removes the option of adding service hours until the review | CR-1, CR-6 (public supply), CR-10a |
| K3 Payroll tax | binary (the state takes) | Yes, for covered employers (A-12 decides who bears it first) | 4 (means transferred from covered employers); 3 (a charge attached to the options "employ at a city worksite" and "cross the threshold", the latter lumpy) | CR-3, CR-4, CR-5c, CR-6, CR-7a, CR-7b, CR-7c, CR-8, CR-10a |
| K4 Wind-down | binary (state spending; ends a contract) | Yes | 1 (the fare-card contract and fare jobs are ended); 4 (termination payment and severance transferred) | CR-5a, CR-8b, CR-8c |

All components are binary. The policy fixes one price (the fare, at zero) and one quantity (service hours), so CR-6 applies where demand at zero exceeds the frozen supply (A-4). K3 has two operations: a proportional charge on city payroll and a lumpy charge on crossing the threshold.

## 3. Actor classes

| Actor class | Role | How its options change (CR-1) |
| --- | --- | --- |
| riders.fare_paying | Current paying riders (single fares, monthly passes) | Op 3: the $2 charge is removed; op 4: unused pass value refunded on application. |
| riders.exempt | Seniors and pupils (22% of boardings) | No money change; their vehicles are shared with added riders (CR-9, shared_facility). |
| riders.evading | The 5% of boardings that evaded | Op 2: riding without paying is now legal; inspection risk removed. |
| travelers.margin | Travelers at the margin between PHT and other modes (A-1) | Option "ride PHT" made better (CR-4 mirror). |
| riders.peak_crush_lines | Morning-peak riders on tram 1, tram 4, bus 12 | Same op 3 for fare payers; demand at zero exceeds crush capacity (A-4) and K2 fixes supply: CR-6. |
| riders.off_peak, riders.peak_other_lines | Riders on vehicles with room (A-2, A-3) | Op 3; added riders share the vehicle. |
| employers.covered | Private employers with a city worksite and payroll above $750,000 | Op 4 and op 3 (K3); compliance duties. |
| employers.covered.transit_independent | Covered employers whose operations do not depend on transit (A-13, A-9) | K3 raises the cost of city labor with no offsetting gain in access. |
| employers.covered.relocating | Those of the above who move to sites just outside (split by response, CR-1 note) | CR-4 (x: here, y: there). |
| employers.near_threshold | Employers whose payroll is near $750,000 (A-8) | Lumpy op 3 on crossing the threshold. |
| employers.city_offices_of_outside_firms | Firms with large payroll outside the city and small city payroll | U1-a: covered; U1-b: exempt if city payroll is at or below $750,000. |
| employers.prospective.transit_independent | Firms choosing where to open a worksite | City site made worse relative to just-outside sites. |
| employers.pass_buying | 260 employers buying annual staff passes | Op 1 (no pass to buy); op 4 (refund); most are also covered by K3. |
| workers.covered_employers | Employees of covered employers, including bonus recipients | K3 dated from 1 Jul 2027: timing of pay (CR-10a); wage terms (CR-5c, CR-7b). |
| workers.city_jobs, workers.suburban_jobs, workers.pht_commuters | Workers choosing between city and suburban jobs (A-11) | Commuting cost to city jobs by PHT falls (CR-7a). |
| workers.pht_fare_staff | 140 fare-collection staff | Op 1 (jobs ended); op 4 (severance) or redeployment (A-19). |
| workers.pht_customer_service | Holders of about 60 new posts | Op 2 (new posts). |
| officials.pht | Supplier; loses fares, receives K3 | Op 4 (K3 receipts); fares and collection ended; K2 freezes service. |
| officials.revenue_department | Collects K3 | Op 4 (1.5% of revenue); administration and audit tasks. |
| residual_claimant (PHT and Transit Reserve) | Holds what K3 and collection savings leave over | CR-8 note on residual claimants. |
| taxpayers.general_fund | Backstop for any K3 shortfall below $58 million | Contingent payer (CR-8 note on payers from the general budget). |
| fare_card_contractor | Supplier of the fare-card system | Op 1 (contract ended); op 4 ($5 million termination payment). |
| sellers.contract_labor | Contractors and staffing agencies | Through CR-9 (substitute for payroll near the threshold). |
| drivers.ride_hail, riders.ride_hail | Substitute mode, price free | Through CR-9 (substitute). |
| drivers.taxi, riders.taxi | Substitute mode, meter price fixed | Through CR-9 (substitute); CR-6 at a fixed price. |
| riders.regional_rail | Province rail, outside the Act | Through CR-9 (substitute and complement). |
| park_and_ride_users | Drivers who park at PHT lots ($4, near capacity) | Through CR-9 (complement: the PHT leg is now free). |
| owners.housing_near_pht_lines, renters.housing_near_pht_lines | Holders and users of housing near lines (incl. the Westmere routes) | Through CR-9 (complement, location). |
| owners.city_commercial_property | Owners of city worksites and shops | Through CR-7b, CR-7c (K3 and K1 both act on city sites). |
| retailers.downtown, neighboring_jurisdictions.malls | Competing shopping destinations (A-16) | Through CR-9 (substitute; trip complements). |
| neighboring_jurisdictions.business_parks | Westmere and Calder Vale business parks with vacancy (A-9) | Through CR-9 (across_border). |
| business_associations, riders_groups | Organized stakeholders (A-15) | CR-4 (x: accept, y: lobby). |
| road_users | Users of the city's roads | Through CR-9 (shared_facility). |

## 4. Direct effect

CR-1 and CR-2: the immediate change for those whose options K1 to K4 alter.

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-1 | riders.fare_paying | price_paid (PHT rides) | decrease | short; medium; long | CR-1 op 3, CR-2 | - |
| C-2 | riders.fare_paying | resources_available_other_uses | increase | short; medium; long | CR-3 note, CR-8b | A-5 |
| C-3 | officials.pht | non_tax_receipts (fares and passes) | decrease | short; medium; long | CR-1, CR-8b | - |
| C-4 | officials.revenue_department, officials.pht | tax_revenue | increase | short; medium; long | CR-1 op 4, CR-8b | - |
| C-5 | employers.covered | resources_available_other_uses | decrease | short | CR-1 op 4, CR-3c, CR-8b, CR-6 | A-12 |
| C-6 | riders.evading | legal_breach (fare evasion) | decrease | short; medium; long | CR-1 op 2 | - |
| C-7 | officials.pht | enforcement_cost (fare collection and inspection) | decrease | medium; long | CR-1, CR-8a, CR-8c | - |
| C-8 | workers.pht_fare_staff | employment (fare collection) | decrease | short | CR-1 op 1, CR-5a | - |
| C-9 | workers.pht_fare_staff | employment (PHT, all roles, former fare staff) | decrease | short; medium | CR-1, arithmetic | A-19 |
| C-10 | workers.pht_customer_service | employment (customer-service and safety posts) | increase | short; medium | CR-1 op 2, CR-8a | A-19 |
| C-11 | officials.pht | quantity_supplied (PHT service hours) | no_change | short; medium (to the 2029 review) | CR-1 (K2), CR-6 public supply | - |

## 5. Responses

CR-4 for every pair of options each class has; CR-5 for exchanges ended or added; CR-6 where a price or quantity is fixed; CR-10a for timing.

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-12 | travelers.margin | quantity_demanded (PHT rides) | increase | short; medium; long | CR-4 mirror, CR-4b, CR-4c | A-1 |
| C-13 | riders.off_peak | quantity_traded (PHT boardings, off-peak) | increase | short; medium; long | CR-4, CR-5, CR-6 public supply | A-1, A-2 |
| C-14 | riders.peak_other_lines | quantity_traded (PHT boardings, peak, lines below crush) | increase | short; medium | CR-4, CR-5 | A-1, A-3 |
| C-15 | riders.peak_crush_lines | excess_demand (morning peak, tram 1, tram 4, bus 12) | increase | short; medium | CR-6, CR-6 public supply, CR-1 (K2) | A-4 |
| C-16 | riders.peak_crush_lines | wait_time (+), quality_per_unit (−), allocation_by_non_price_criteria (+) | at_least_one_as_stated | short; medium | CR-6, CR-6 public supply | A-4 |
| C-17 | travelers.margin | quantity_substitute (car, ride-hail, taxi, bike-share and walking trips, off-peak and on lines below crush) | at_least_one_decrease | short; medium; long | CR-4b, CR-9 | A-1 |
| C-18 | riders.peak_crush_lines | quantity_substitute (other-mode trips in the tram 1, tram 4, bus 12 corridors at the morning peak) | ambiguous | short; medium | CR-12b | A-1, A-4, A-5 |
| C-19 | employers.near_threshold | reclassification (+), employment (−) | at_least_one_as_stated | short; medium; long | CR-1 op 3, CR-4 (lumpy cost) | A-8 |
| C-20 | employers.covered.transit_independent | employment (−), hours_worked (−) | at_least_one_decrease | short | CR-4b, CR-4c, CR-6 | A-12, A-13 |
| C-21 | employers.covered.transit_independent | employment | ambiguous | medium; long | CR-12b | A-13, A-11, A-N2 |
| C-22 | employers.covered.relocating | employment (at city worksites) | decrease | medium; long | CR-4 (x: here, y: there), CR-7a, CR-10b | A-9 |
| C-23 | employers.prospective.transit_independent | entry_rate (new worksites in the city) | decrease | medium; long | CR-4, CR-7a, CR-10a | A-9 |
| C-24 | employers.city_offices_of_outside_firms | resources_available_other_uses | U1-a: decrease; U1-b: no_change | short | CR-1 per reading, CR-3c, CR-6 | A-12 |
| C-25 | employers.city_offices_of_outside_firms | employment (city offices) | U1-a: ambiguous; U1-b: increase | medium; long | CR-4, CR-12b | A-10 |
| C-26 | employers.covered | compliance_cost (quarterly returns, threshold records) | increase | short; medium; long | CR-1 op 3, CR-8c | - |
| C-27 | workers.covered_employers | earnings (bonus payments in June 2027) | increase | short (June 2027) | CR-10a, CR-4, CR-5c | A-23 |
| C-28 | workers.covered_employers | earnings (bonus payments in July to September 2027) | decrease | short (Q3 2027) | CR-10a, CR-4, CR-5c | A-23 |
| C-29 | officials.revenue_department | tax_revenue_vs_static_projection | decrease | short; medium; long | CR-4, CR-12d | A-8, A-9, A-13, A-23 |
| C-30 | business_associations, riders_groups | lobbying_effort | increase | short; medium; long | CR-4 (x: accept, y: lobby), CR-10a, CR-8c | A-15 |
| C-31 | employers.pass_buying | quantity_traded (employer annual passes) | decrease | short; medium; long | CR-1 op 1, CR-5a | - |
| C-32 | employers.pass_buying | resources_available_other_uses | increase | short; medium; long | CR-8b, CR-7 note (payers who receive part) | A-22 |
| C-33 | riders.fare_paying (pass holders) | compliance_cost (refund applications) | increase | short | CR-1 op 4, CR-8c | - |
| C-34 | park_and_ride_users | search_cost, wait_time | at_least_one_increase | short; medium; long | CR-9, CR-6 | A-1, A-20 |
| C-35 | officials.pht | non_tax_receipts (park-and-ride fees) | increase | short; medium; long | CR-9, CR-4c | A-1, A-20 |

## 6. Second-order effects

CR-9 along named relations, then CR-5 to CR-7 in each market reached. Depth limit 4. Chains pruned: output prices of covered employers' goods (relation: city labor input_to their output) at depth 3 as diffuse bystander effects; car-trip complements (fuel, downtown parking) because A-1 licenses only the group of substitute modes, not car trips in particular; crowding at stops (proximity), which would be Tier C and is close to the out-of-scope safety heading. No gift relation is touched; no currency relation applies to a city tax of this kind.

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C-36 | riders.ride_hail | price_substitute (ride-hail fares, off-peak) | decrease | short; medium | CR-9, CR-6 | PHT rides substitute for off-peak ride-hail (partial) | A-6 |
| C-37 | drivers.ride_hail | earnings | decrease | short; medium | CR-9, LW-10, CR-7a | as above | A-6 |
| C-38 | drivers.taxi | quantity_traded (taxi trips) | decrease | short; medium; long | CR-9, CR-4b | PHT rides substitute for taxi trips (partial) | A-N3 |
| C-39 | riders.taxi | wait_time (−), quality_per_unit (+) | at_least_one_as_stated | short; medium | CR-6 (meter fixed; pressure from sellers) | as above | A-N3 |
| C-40 | owners.housing_near_pht_lines | asset_value | increase | short (from announcement); medium; long | CR-9, CR-7b, CR-7c, CR-10c | PHT rides complement (location) to housing near lines (close) | A-21, A-N1 |
| C-41 | renters.housing_near_pht_lines | price_paid (rents) | increase | medium; long | CR-9, CR-7b, CR-6 | as above | A-21, A-N1 |
| C-42 | owners.housing_near_pht_lines | subsidy_share_received | increase | medium; long | CR-7b | as above | A-21, A-N1 |
| C-43 | retailers.downtown | quantity_traded | increase | medium; long | CR-9, CR-4 | PHT rides complement (trip) to downtown shopping; downtown substitute for suburban malls | A-16 |
| C-44 | neighboring_jurisdictions.malls | quantity_traded | decrease | medium; long | CR-9, CR-4b | downtown shopping substitute for mall shopping (partial), across_border | A-16 |
| C-45 | neighboring_jurisdictions.business_parks | asset_value | increase | short (from announcement); medium; long | CR-9, CR-7c, CR-10c | city worksites across_border substitute for business-park sites | A-9 |
| C-46 | neighboring_jurisdictions.business_parks | employment | increase | medium; long | CR-9, CR-7a | as above | A-9 |
| C-47 | owners.city_commercial_property | asset_value | ambiguous | short; medium; long | CR-12b | city sites input_to covered employers; complement (location) to transit | A-9, A-10, A-16 |
| C-48 | workers.city_jobs | wage_rate | no_change | short | CR-6 (existing contracts) | employment contract | A-12 |
| C-49 | workers.city_jobs | wage_rate | ambiguous | medium; long | CR-12b | city labor input_to covered and uncovered employers; PHT rides complement (location) to city jobs | A-N2, A-11, A-16 |
| C-50 | workers.pht_commuters | job_changes | increase | medium | CR-7a, CR-4 | PHT rides complement (location) to city jobs | A-11 |
| C-51 | workers.suburban_jobs | wage_rate | ambiguous | medium; long | CR-12b | suburban labor same_market_other_segment of city labor | A-11, A-9, A-N2 |
| C-52 | sellers.contract_labor | quantity_traded (contract labor sold to employers near the threshold) | increase | short; medium; long | CR-9, CR-4 | contract labor substitute for payroll employment (close) | A-8 |
| C-53 | fare_card_contractor | quantity_traded (fare-system services) | decrease | short; medium; long | CR-1 op 1, CR-5a | contract | - |
| C-54 | officials.pht | resources_available_other_uses | decrease | short (FY 2027-28, one-time) | CR-8b, CR-3c | contract (fare-card); employment contract (severance) | - |
| C-55 | fare_card_contractor | resources_available_other_uses | ambiguous | short (FY 2027-28) | CR-12b | contract | - |
| C-56 | fare_card_contractor | resources_available_other_uses | decrease | medium; long | CR-5a, CR-12e | contract | - |
| C-57 | residual_claimant (PHT and Transit Reserve) | fund_balance | increase | medium (to the 2029 review) | CR-8b, CR-8d, CR-12e (arithmetic) | - | A-17, A-18, A-19 |
| C-58 | riders.off_peak, riders.peak_other_lines | quality_per_unit (crowding) | decrease | short; medium | CR-9 | shared_facility (vehicles) | A-1, A-2, A-3 |
| C-59 | riders.exempt (on tram 1, tram 4, bus 12 at the peak) | full_cost_per_unit | increase | short; medium | CR-6, CR-9 | shared_facility (vehicles) | A-4 |
| C-60 | riders.peak_crush_lines (fare payers) | full_cost_per_unit | ambiguous | short; medium | CR-12b | - | A-4 |
| C-61 | riders.off_peak (fare payers) | full_cost_per_unit | decrease | short; medium; long | CR-1, CR-12e | - | A-1, A-2 |
| C-62 | road_users | wait_time (road congestion) | ambiguous | short; medium | CR-12b | shared_facility (roads) | A-1, A-4, A-6 |
| C-63 | riders.regional_rail | quantity_substitute (regional rail trips) | ambiguous | short; medium; long | CR-12b | PHT rides substitute for, and complement (transfer) to, regional rail | A-N4 |
| C-64 | officials.revenue_department | enforcement_cost (administering K3, auditing the threshold) | increase | short; medium; long | CR-1 op 4, CR-8c | - | - |

## 7. Combined effects

Every (actor class, variable, horizon) key reached by more than one chain, including chains from section 8 and from other components.

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance premise | Combined sign |
| --- | --- | --- | --- | --- |
| riders.peak_crush_lines (fare payers), full_cost_per_unit, short; medium | waiting, crowding and being passed up (CR-6, A-4) | $2 fare removed (CR-1) | None | ambiguous (C-60) |
| riders.off_peak (fare payers), full_cost_per_unit | slightly fuller vehicles (CR-9 shared_facility, Tier C) | $2 fare removed (CR-1) | CR-12e (response cannot reverse its cause): with room on vehicles (A-2) no one is left behind, and added riders board only while their own full cost is below the old one; the crowding chain is Tier C | decrease (C-61) |
| riders.exempt (crush lines), full_cost_per_unit | waiting and crowding (CR-6, A-4) | none (no fare change) | - | increase (C-59) |
| riders.peak_crush_lines, quantity_substitute | displaced peak riders turn to other modes (A-4, A-5 exceptions) | new riders drawn from other modes up to crush load (A-1) | None | ambiguous (C-18) |
| employers.covered.transit_independent, employment, short | - | K3 raises labor cost with money wages fixed (A-12, A-13) | - | at_least_one_decrease with hours (C-20) |
| employers.covered.transit_independent, employment, medium; long | lower city wages as more PHT commuters seek city jobs (A-11, CR-7a) | K3 raises labor cost (A-13); wages fall only partly (CR-7b, A-N2) | None (the commuting chain is a separate cause, so CR-12e does not apply to it) | ambiguous (C-21) |
| workers.city_jobs, wage_rate, medium; long | more downtown trade raises demand for retail labor (A-16, CR-9, LW-10) | K3 incidence shared by workers (CR-7b, A-N2); more PHT commuters supply city labor (A-11, CR-7a) | None | ambiguous (C-49) |
| workers.suburban_jobs, wage_rate, medium; long | relocating employers add suburban jobs (A-9); PHT commuters move to city jobs (A-11) | workers leaving covered city employers seek suburban jobs (CR-7a, A-N2) | None | ambiguous (C-51) |
| owners.city_commercial_property, asset_value | transit-linked uses (downtown retail, A-16; outside firms' offices, A-10) gain | K3 lowers yields on city sites for transit-independent covered employers who can move (A-9; CR-7b: the immobile site bears) | None | ambiguous (C-47) |
| employers.city_offices_of_outside_firms, employment, U1-a | cheaper commuting and customer access (A-10) | tax on city payroll (K3 under U1-a) | None | U1-a: ambiguous; U1-b: increase (C-25) |
| road_users, wait_time | displaced crush-line riders who drive (A-4); ride-hail drivers who keep cruising (A-6) | travelers who leave cars off-peak (A-1, group only) | None | ambiguous, Tier C (C-62) |
| riders.regional_rail, quantity_substitute | rail-plus-PHT trips cheaper (complement, A-N4) | city trips switch from rail to free PHT (substitute, A-N4) | None | ambiguous (C-63) |
| fare_card_contractor, resources_available_other_uses, short | $5 million termination payment (CR-8b) | contract payments from Sept 2027 lost (CR-5a) | None | ambiguous (C-55); decrease in the medium and long run (C-56) |
| residual_claimant, fund_balance, medium | K3 receipts (about $60.1 million projected net of 1.5%); collection savings ($13 million a year) | fares lost ($58 million); new posts; K3 shortfall below projection | Arithmetic (CR-12e): change = 2.1 − shortfall + (13 − cost of posts); A-17 says the shortfall is below 13 − cost of posts, so the change exceeds $2.1 million | increase (C-57) |
| officials.revenue_department, tax_revenue_vs_static_projection | - | four independent chains: threshold reshaping (A-8), relocation (A-9), staff cuts (A-13), bonus timing (A-23, first quarter) | CR-12d: reported if any chain's premises hold | decrease (C-29) |
| employers.covered vs employers.pass_buying, resources_available_other_uses | passes no longer bought (C-32) | K3 paid (C-5) | Not combined: different classes overlap only partly; CR-7 note says sign each side separately | separate (C-5, C-32) |

No chains cancel exactly by construction (CR-12f). K2 and the counterfactual hold the same timetable, so K2 enters only by closing the supply response (C-11).

## 8. Time structure

- **Announcement (campaign, then 10 Feb 2027).** From the bill's introduction, and partly from the campaign, the fare-free service and the tax became expected (CR-10a). Housing near lines (C-40) and business-park sites (C-45) change value as the probability of passage rises, so the gain is captured by holders at that time and spread across holders as the bill advanced (CR-7c, CR-10c). Relocation planning and lobbying (C-22, C-30) start before the effective dates.
- **Tax before benefit (1 Jul to 31 Aug 2027).** K3 applies to wages paid from 1 July while fares are still charged until 1 September. Employers and riders both pay in that window; this is part of C-4 and C-5. It also shifts bonuses (C-27, C-28): a timing shift signed per window, since the bonuses are paid with or without the policy. Receipts begin in October (quarterly), so PHT's cash flow in July to September rests on fares.
- **One-time costs (FY 2027-28).** The $5 million termination payment and severance fall in the first year (C-54). No sign is given for PHT's first-year balance: the July-August tax receipts (about $10 million on the projection) and seven months of collection savings stand against these costs, and the severance sum is not in the record.
- **Shoulder of the peak.** On tram 1, tram 4 and bus 12, some riders shift to the shoulders of the peak (CR-6: time of travel is an open margin). Boardings in both windows are higher than in the counterfactual, so this is a path note (CR-12h), recorded as a consequence only through C-16.
- **Service freeze and review (to mid-2029).** K2 holds service hours for two fiscal years (C-11), so the excess demand and crowding (C-15, C-16, C-59) last at least until the review. Whether service is then expanded with the Transit Reserve depends on the council and on A-18; riders' groups have a stake in expansion and business associations in reducing the tax (C-30).
- **Wages.** Money wages are fixed by contracts in the short run (A-12; C-48), so covered employers bear K3 first (C-5). In the medium run wages adjust and the incidence is shared (CR-7b), but the commuting and retail chains make the city wage ambiguous (C-49).
- **Durable responses and persistence.** Relocated worksites (C-22, C-46), forgone entry (C-23) and reshaped payroll (C-19, C-52) are stocks that change through flows (CR-10b). If the tax were later cut or repealed, they would persist in part: relocated firms carry moving costs (`reversal_cost`) and would not return just because the tax ended. The capitalized gain on housing (C-40) would be reversed on repeal, with the loss borne by holders when repeal becomes expected (CR-7c). These are notes; the persistence field is formally defined only for repeals.
- **Expectations about continuation (A-14).** If buyers expect fare-free transit to continue past the review, the capitalized gain in C-40 is larger; if they expect only two years, it is capitalized for those yields only (CR-7c). The sign is the same either way.

## 9. Opportunity costs

Each is written as a signed change in a variable.

| ID | Actor class | Variable | Sign | What is given up | Rules |
| --- | --- | --- | --- | --- | --- |
| C-5 | employers.covered | resources_available_other_uses | decrease | About $61 million a year of purchases, investment or pay the employers would have made | CR-8a, CR-8b, CR-3c |
| C-24 | employers.city_offices_of_outside_firms | resources_available_other_uses | U1-a: decrease; U1-b: no_change | The tax on small city payrolls under U1-a | CR-3c, CR-8b |
| C-26 | employers.covered | compliance_cost | increase | Staff time and records for quarterly returns and threshold tests | CR-8c |
| C-33 | riders.fare_paying (pass holders) | compliance_cost | increase | Time spent applying for pro rata refunds | CR-8c |
| C-64 | officials.revenue_department | enforcement_cost | increase | 1.5% of K3 (about $0.9 million a year) used up in collection and audit | CR-8c |
| C-30 | business_associations, riders_groups | lobbying_effort | increase | Time and money spent on lobbying | CR-8c |
| C-16 | riders.peak_crush_lines | wait_time (+), quality_per_unit (−), allocation_by_non_price_criteria (+) | at_least_one_as_stated | Time spent waiting for a vehicle with room; comfort | CR-6, CR-8c |
| C-34 | park_and_ride_users | search_cost, wait_time | at_least_one_increase | Time spent finding a space or arriving earlier | CR-6, CR-8c |
| C-20 | employers.covered.transit_independent | employment (−), hours_worked (−) | at_least_one_decrease | Work not done because city labor costs more | CR-4c, CR-8a |
| C-54 | officials.pht | resources_available_other_uses | decrease | $5 million termination payment and severance | CR-8b |
| C-56 | fare_card_contractor | resources_available_other_uses | decrease | Gains from a contract that would otherwise have continued | CR-5a |

CR-8b symmetry is checked for every transfer: fares no longer paid (C-1, C-2) against fares lost by PHT (C-3); the tax paid (C-5, C-24) against tax revenue (C-4); employer pass spending saved (C-32) against PHT's lost pass receipts (in C-3); the termination payment (C-54) against the contractor's receipt (C-55); collection costs released (C-7) against the new posts (C-10) and PHT's balance (C-57). The general fund's side is not signed: it pays only if K3 receipts net of 1.5% fall below $58 million, and no premise says whether they will (see Not reported). Means released by the end of fare collection (C-7) are the reverse of CR-8c: they become available for other uses.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
| --- | --- | --- | --- | --- | --- |
| A-1 | Some travelers are at the margin between PHT and other modes at a $2 fare. | substitutability | 0.95 | Mode shares; past ridership responses to fare changes; share of short trips walked. | These consequences fail or lose this chain: C-12, C-13, C-14, C-17, C-18, C-34, C-35, C-58, C-61, C-62. |
| A-2 | Off-peak vehicles have room for added riders (average occupancy about 35% of planning capacity). | other | 0.85 | Automatic passenger counts. | These consequences fail or lose this chain: C-13, C-58, C-61. |
| A-3 | At the old fare, most peak lines run below crush load, so added riders board standing. | other | 0.8 | Peak counts at 60–75% of planning capacity on most lines. | These consequences fail or lose this chain: C-14, C-58. |
| A-4 | On tram 1, tram 4 and bus 12, peak demand at a zero fare exceeds crush capacity. | binding | 0.7 | Already at 95% of planning capacity at $2; ridership responses in comparable fare-free cities. | These consequences fail or lose this chain: C-15, C-16, C-18, C-59, C-60, C-62. |
| A-5 | Most fare-paying riders keep riding at a zero fare. | other | 0.9 | Few would stop riding because a price fell; exceptions are peak riders displaced by crowding. | These consequences fail or lose this chain: C-2, C-18. |
| A-6 | Some off-peak ride-hail users switch to PHT, and ride-hail drivers do not withdraw as fast as riders do. | substitutability | 0.6 | Ride-hail trip data by hour; driver hours. | These consequences fail or lose this chain: C-36, C-37, C-62. |
| A-7 | People using vehicles as shelter add materially to off-peak crowding. | other | 0.4 | Experience of other fare-free systems is mixed. | No reported consequence rests on it (see Not reported). |
| A-8 | For some employers near the threshold, reshaping payroll costs less than the tax on their whole city payroll. | other | 0.75 | Employers with payroll between $600,000 and $900,000; use of contractors in those sectors. | These consequences fail or lose this chain: C-19, C-29, C-52. |
| A-9 | Some covered employers' operations do not depend on transit, and sites are available just outside the boundary. | mobility | 0.65 | Warehouses and plants near the western boundary; vacancy in the Westmere and Calder Vale business parks. | These consequences fail or lose this chain: C-22, C-23, C-29, C-45, C-46, C-47, C-51. |
| A-10 | Small city offices of large outside firms value transit access for staff or customers. | other | 0.6 | Location of such offices near tram stops; commuting surveys. | These consequences fail or lose this chain: C-25, C-47. |
| A-11 | Some workers choose between city and suburban jobs by pay net of commuting cost, and commute by PHT. | mobility | 0.8 | Commuting surveys; PHT pass holders working in the city. | These consequences fail or lose this chain: C-21, C-49, C-50, C-51. |
| A-12 | Money wages are fixed in the short run by contracts and custom, so covered employers bear K3 at first. | other | 0.85 | Contract lengths; annual pay reviews. | These consequences fail or lose this chain: C-5, C-20, C-24, C-48. |
| A-13 | Covered employers not linked to transit adjust staff or hours when labor costs rise. | alternative_uses | 0.75 | Share of hourly staff; automation options in warehousing. | These consequences fail or lose this chain: C-20, C-21, C-29. |
| A-14 | Home buyers expect fare-free transit to continue beyond the two-year review. | expectations | 0.6 | Campaign commitments; council majority; polling on the policy. | No reported sign rests on it; it bears on the size of C-40 and C-42 (section 8). |
| A-15 | Business associations and riders' groups can organize at a cost below their stakes. | other | 0.7 | The chamber of commerce opposed the bill; an existing riders' union. | These consequences fail or lose this chain: C-30. |
| A-16 | Some shoppers choose between downtown and the suburban malls partly by trip cost. | substitutability | 0.7 | Shopper origin surveys; share of downtown shoppers arriving by PHT. | These consequences fail or lose this chain: C-43, C-44, C-47, C-49. |
| A-17 | K3's revenue shortfall below projection stays smaller than the collection costs saved, net of the new posts. | other | 0.75 | Projection margin; size of the threshold band; relocation is slow. | These consequences fail or lose this chain: C-57. |
| A-18 | PHT holds the surplus in the Transit Reserve, as the Act says. | revenue_use | 0.6 | Act text; the city's record of drawing on authority reserves. | These consequences fail or lose this chain: C-57. |
| A-19 | PHT creates about 60 customer-service and safety posts, filled mainly by former fare staff. | other | 0.75 | PHT's published plan; union transfer agreement. | These consequences fail or lose this chain: C-9, C-10, C-57. |
| A-20 | Park-and-ride lots are near capacity at the $4 fee (about 85% weekday occupancy). | binding | 0.65 | Lot counts. | These consequences fail or lose this chain: C-34, C-35. |
| A-21 | Housing near PHT lines cannot expand quickly. | durability | 0.85 | Zoning near lines; construction lead times. | These consequences fail or lose this chain: C-40, C-41, C-42. |
| A-22 | Pass-buying employers would have kept buying staff passes. | other | 0.85 | Multi-year pass agreements; renewal rates. | These consequences fail or lose this chain: C-32. |
| A-23 | Some covered employers can move bonuses due in July into June. | other | 0.55 | Bonus calendars; past responses to payroll tax dates. | These consequences fail or lose this chain: C-27, C-28, C-29 (first-quarter chain only). |
| A-N1 | Some households choose where to live partly by the cost of commuting and shopping trips, and ride PHT. | substitutability | 0.8 | NEW (flagged). Needed for the location-complement chain to housing; A-11 covers job choice, not home choice. Evidence: PHT pass holders' home locations; house-price gradients near tram stops. | These consequences fail or lose this chain: C-40, C-41, C-42. |
| A-N2 | Workers at covered employers cannot all move to uncovered jobs (public employers, charities, small firms, suburban sites) at the same pay and commuting cost. | mobility | 0.85 | NEW (flagged). Needed for CR-7b to place part of K3 on workers; the record gives no premise on worker mobility between covered and uncovered jobs. Evidence: size of the uncovered sector; commuting distances to the suburbs. | These consequences fail or lose this chain: C-21, C-49, C-51. |
| A-N3 | Some taxi riders are at the margin between taxis and PHT at a $2 fare. | substitutability | 0.6 | NEW (flagged). A-1 licenses only the group of other modes; a claim about taxis in particular needs its own premise. Evidence: taxi trips along PHT routes, especially off-peak and to and from stations. | These consequences fail or lose this chain: C-38, C-39. |
| A-N4 | Some regional rail riders make part of their trip on PHT, and some trips within the city can be made by either. | substitutability | 0.7 | NEW (flagged). Needed to follow the relation to province rail, which the Act does not cover. Evidence: transfer counts at rail stations; rail stops inside the city. | These consequences fail or lose this chain: C-63. |

**Not reported** (an assumption below 0.5, or no premise to sign):
- Off-peak crowding raised materially by people using vehicles as shelter (CR-4 mirror: shelter on a vehicle becomes free; CR-9 shared_facility): needs A-7 (p 0.4).
- The general fund's payments (taxpayers.general_fund, resources_available_other_uses): the general fund pays only if K3 receipts net of 1.5% fall below $58 million (a shortfall of more than about $2.1 million against the projection). A-17 bounds the shortfall only by the collection savings, so no sign is given. If A-18 fails (p 0.4) the city may instead draw on the reserve, which would raise the general fund's means.
- Bus dwell times (travel_time for bus riders): more boardings lengthen stops while the end of fare payment shortens them. This is a physical relation, not a choice, and is not derived (GAP-032-C1).

**Final check before the report** (workflow):
1. Uncombined chains: every key in section 7 was checked against sections 4 to 6 and 8, including the K3 chains that reach city wages and the commuting chain that reaches transit-independent employers (C-21 made ambiguous for the medium and long run; C-20 kept for the short run only, where A-12 holds wages fixed).
2. Single signs for a group: CR-6 margins on crush lines (C-16), park-and-ride (C-34) and taxis (C-39), staff or hours (C-20), reshaping or staff (C-19) and the substitute modes (C-17) are group signs.
3. Baseline: every sign is against the same city with $2 fares, the same timetable and no tax. K2's own sign is therefore no_change (C-11), and exempt riders' money price is unchanged.
4. Worse off is not poorer: riders displaced on crush lines are worse off by their own ranking (CR-3a) but no resources_available_other_uses sign is given for them; resources signs are given only where a class keeps paying or pays a sum it cannot avoid (C-5, C-24, C-54) or keeps buying and stops paying (C-2, C-32).
5. Timing shifts: bonuses are signed per window (C-27, C-28); shoulder-of-peak shifts are a path note because both windows rise (CR-12h).
6. Both sides of every transfer: see the end of section 9.
7. Every actor class, every core rule: CR-7c was applied to housing, business parks and city commercial sites; CR-6 to the crush lines, park-and-ride and taxis (the two fixed prices that remain); enforcement costs to PHT (C-7) and the Revenue Department (C-64); the payer's side to employers (C-5) and the general fund (not signed).
8. Unstated premises: the four new premises are A-N1 to A-N4; lobbying rests on A-15.

## 11. Report

**The policy:** From 1 September 2027 every ride on Port Hallam's buses and trams is free, including the two routes into Westmere; fare inspection ends and the fare-card contract is terminated, with about 60 of the 140 fare staff moved to customer-service and safety posts. Service hours are frozen at the 2026-27 timetable until a council review in 2029. The money comes from a 0.40% tax on the city payroll of private employers whose payroll exceeds $750,000, charged on all their city payroll once they are over the line, on wages paid from 1 July 2027. Revenue above $58 million goes into a Transit Reserve; any shortfall below it is covered by the general fund.

**Visible consequences:** Fare-paying riders pay nothing and have more to spend on other things (C-1, C-2); travelers at the margin ride PHT more, off-peak and on most peak lines (C-12, C-13, C-14). PHT loses $58 million of fares (C-3) and receives the tax (C-4); covered employers pay it, at first out of their own means because wages are fixed (C-5). Fare-collection jobs end (C-8, C-9) and new service posts are created (C-10). Service hours are unchanged (C-11). On tram 1, tram 4 and bus 12 at the morning peak, more people want to ride than the frozen service can carry (C-15), and the shortfall shows up as waiting, crowding or riders at later stops being passed up (C-16). Employers stop buying staff passes (C-31).

**Invisible consequences:**
- *Riders:* off-peak fare payers are better off on the full cost of a ride (C-61); seniors and pupils on the crowded peak lines gain nothing on price and lose on waiting and crowding (C-59); vehicles elsewhere are fuller (C-58, Tier C). Fare evasion disappears as a breach (C-6). Pass holders spend time claiming refunds (C-33). Park-and-ride lots fill, so drivers search or arrive earlier (C-34), while PHT collects more parking fees (C-35).
- *Other modes:* fewer trips by at least one of car, ride-hail, taxi, bike-share or walking off-peak (C-17); off-peak ride-hail fares and drivers' earnings fall (C-36, C-37); taxis carry fewer trips and, with the meter fixed, taxi riders wait less or get better service (C-38, C-39).
- *Employers and workers:* employers near the $750,000 line reshape payroll (contractors, smaller staff) to stay under it (C-19), which raises the use of contract labor (C-52). Covered employers that do not depend on transit cut staff or hours in the short run (C-20); some move to the Westmere and Calder Vale business parks (C-22), fewer new worksites open in the city (C-23), and the business parks gain value and jobs (C-45, C-46). Bonuses due in July are paid in June (C-27, C-28). Employers file returns (C-26) and the Revenue Department spends 1.5% of the tax on collection and audit (C-64); revenue falls short of the static projection (C-29). Pass-buying employers save what they spent on passes (C-32). PHT commuters change jobs toward the city (C-50).
- *Property and shopping:* housing near PHT lines gains value from the announcement (C-40), rents there rise (C-41), and landowners keep part of the riders' gain (C-42). Downtown shops gain trade from the suburban malls (C-43, C-44).
- *PHT and its counterparties:* collection costs fall (C-7); the termination payment and severance are a one-time cost (C-54); the fare-card contractor loses the contract (C-53, C-56). Over the freeze, PHT and its reserve end up with more money than without the policy (C-57). Business associations and riders' groups lobby, the first against the tax and the second for service expansion at the review (C-30).

**Ambiguous effects:**
- Full cost of a peak ride on tram 1, tram 4 and bus 12 for fare payers (C-60): the fare falls to zero, but waiting and crowding rise. Decided by how much riders value the $2 against the time and comfort lost.
- City wages in the medium and long run (C-49): the tax and the cheaper commute push them down; more downtown trade pushes them up. Suburban wages (C-51) and employment at transit-independent covered employers (C-21) are ambiguous for the same reasons.
- Value of city commercial property (C-47): the tax lowers it for sites used by employers who could move; free transit raises it for transit-linked uses.
- Small city offices of outside firms (C-25): under U1-a they pay the tax but gain transit access (ambiguous); under U1-b they gain access without the tax (employment rises).
- Other-mode trips in the crowded peak corridors (C-18), road congestion (C-62, Tier C), regional rail ridership (C-63), and the fare-card contractor's first-year means (C-55).

**Key conditions:** Peak demand at a zero fare exceeds crush load on the three busiest lines (A-4, 0.7), which drives the crowding results; wages are fixed at first (A-12, 0.85), which puts the first-year burden on employers; transit-independent employers can move just outside (A-9, 0.65); employers near the threshold can reshape payroll (A-8, 0.75); the revenue shortfall stays below the collection savings (A-17, 0.75) and PHT keeps the surplus (A-18, 0.6), which decide PHT's balance. Four premises were added: households choose location partly by trip cost (A-N1, 0.8), workers are not perfectly mobile out of covered jobs (A-N2, 0.85), some taxi riders are at the margin with PHT (A-N3, 0.6), and rail and PHT are linked by transfers and overlapping trips (A-N4, 0.7).

**What this analysis cannot say:** how large any effect is; whether the tax will raise more or less than $58 million, and so whether the general fund pays anything; how the burden of the tax is split between employers, workers and landowners after the first year; and whether the gains to riders outweigh the losses to employers, displaced peak riders, exempt riders and other modes. It does not say whether the policy is good. Environmental effects, the health effects of walking and cycling, and safety on crowded vehicles are out of scope; congestion is recorded only as road users' waiting time.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C-1 | riders.fare_paying | price_paid (PHT rides) | decrease | short; medium; long | visible | A | CR-1 (op 3: K1 removes the $2 charge attached to riding); CR-2 (riders who rode before still choose to ride; the price they pay is what the rule sets) | none |
| C-2 | riders.fare_paying | resources_available_other_uses | increase | short; medium; long | visible | B | CR-3 note (resources rise for a class that keeps taking the option and no longer pays for it: A-5); CR-8b (the fare no longer paid stays with the rider; pre-paid value is refunded) | A-5 |
| C-3 | officials.pht | non_tax_receipts (fares and passes) | decrease | short; medium; long | visible | A | CR-1 (op 1: the exchange of a fare for a ride is ended); CR-8b (the receipt side of C-2: what riders keep, PHT does not receive) | none |
| C-4 | officials.revenue_department, officials.pht | tax_revenue | increase | short; medium; long | visible | A | CR-1 (op 4: K3 transfers about $61 million a year projected); CR-8b (every payment is a receipt: the Revenue Department keeps 1.5% and passes the rest to PHT) | none |
| C-5 | employers.covered | resources_available_other_uses | decrease | short | visible | B | CR-1 (op 4 and op 3: 0.40% of city payroll); CR-6 (existing contracts fix money wages, so the tax cannot be passed back at once: A-12); CR-3c and CR-8b (what is paid is not available for other uses) | A-12 |
| C-6 | riders.evading | legal_breach (fare evasion) | decrease | short; medium; long | invisible | A | CR-1 (op 2: riding without paying is now lawful, so the 5% of boardings that were breaches cease to be breaches) | none |
| C-7 | officials.pht | enforcement_cost (fare collection and inspection) | decrease | medium; long | invisible | A | CR-1 (K4 ends the fare-card contract, cash handling and inspection, about $13 million a year); CR-8c in reverse and CR-8a (means no longer used up in collection become available for other uses) | none |
| C-8 | workers.pht_fare_staff | employment (fare collection) | decrease | short | visible | A | CR-1 (op 1: K4 ends the 140 fare-collection jobs); CR-5a (employment exchanges that would have continued are ended) | none |
| C-9 | workers.pht_fare_staff | employment (PHT, all roles, former fare staff) | decrease | short; medium | visible | B | CR-1 (K4: redeployment "where possible", severance for the rest); arithmetic (about 60 posts, A-19, against 140 jobs ended) | A-19 |
| C-10 | workers.pht_customer_service | employment (customer-service and safety posts) | increase | short; medium | visible | B | CR-1 (op 2: about 60 new posts, A-19); CR-8a (part of the collection budget is redirected to them) | A-19 |
| C-11 | officials.pht | quantity_supplied (PHT service hours) | no_change | short; medium (to the 2029 review) | visible | A | CR-1 (K2 fixes service hours at the 2026-27 timetable, which is also the counterfactual timetable); CR-6 public supply clarification (the supplier does not respond as a seller would while the budget rule holds) | none |
| C-12 | travelers.margin | quantity_demanded (PHT rides) | increase | short; medium; long | visible | B | CR-4 mirror (x: ride PHT is made better relative to other modes; those who ranked it narrowly below switch to it, A-1); CR-4c (each traveler takes more trips, the extra trips being those valued less than $2) | A-1 |
| C-13 | riders.off_peak | quantity_traded (PHT boardings, off-peak) | increase | short; medium; long | visible | B | CR-4 (C-12); CR-5 (rides now take place that would not have); CR-6 public supply (with room on vehicles, A-2, the added demand is carried rather than rationed) | A-1, A-2 |
| C-14 | riders.peak_other_lines | quantity_traded (PHT boardings, peak, lines below crush) | increase | short; medium | visible | B | CR-4 and CR-5 as in C-13; added riders board standing because these lines run below crush load (A-3) | A-1, A-3 |
| C-15 | riders.peak_crush_lines | excess_demand (morning peak, tram 1, tram 4, bus 12) | increase | short; medium | visible | B | CR-6 (at a price held at zero, quantity demanded exceeds the quantity supplied: A-4); CR-6 public supply clarification and CR-1 (K2 fixes the quantity, so the supplier does not close the gap before the review) | A-4 |
| C-16 | riders.peak_crush_lines | wait_time (+), quality_per_unit (−), allocation_by_non_price_criteria (+) | at_least_one_as_stated | short; medium | visible | B | CR-6 (the pressure from unsatisfied buyers goes to the open margins: waiting for a vehicle with room, crowding up to crush load, and allocation by stop position, riders at earlier stops boarding first); CR-6 establishes that at least one is used; the margins move in opposite directions on the welfare scale, so the group is recorded as stated | A-4 |
| C-17 | travelers.margin | quantity_substitute (car, ride-hail, taxi, bike-share and walking trips, off-peak and on lines below crush) | at_least_one_decrease | short; medium; long | invisible | B | CR-4b (those who switch to PHT leave some other mode, A-1); CR-9 (relation: PHT rides substitute for each other mode); A-1 does not say which mode, so the modes are a group | A-1 |
| C-18 | riders.peak_crush_lines | quantity_substitute (other-mode trips in the tram 1, tram 4, bus 12 corridors at the morning peak) | ambiguous | short; medium | invisible | B | CR-12b: (−) new riders drawn from other modes up to crush load (CR-4, A-1); (+) earlier riders crowded off take other modes (CR-6, CR-4b; A-4 and the exception in A-5). No premise says which dominates | A-1, A-4, A-5 |
| C-19 | employers.near_threshold | reclassification (+), employment (−) | at_least_one_as_stated | short; medium; long | invisible | B | CR-1 (op 3: crossing $750,000 attaches a tax on all city payroll, a lumpy cost); CR-4 (x: payroll just above the threshold, y: payroll below it, by using contractors, splitting entities or employing fewer; the lumpy cost reverses the ranking for many, CR-4 note on lumpy costs, A-8). Under U1-b, firms with sites outside the city can also move city payroll to them; under U1-a they cannot. The sign is the same under both readings | A-8 |
| C-20 | employers.covered.transit_independent | employment (−), hours_worked (−) | at_least_one_decrease | short | invisible | B | CR-1 (K3 raises the cost of each hour of city labor by 0.40%); CR-6 (existing contracts fix money wages, A-12, so the cost is not passed back at once); CR-4b and CR-4c (the last hours or jobs, valued least, are given up: A-13); which of the two is cut is not licensed | A-12, A-13 |
| C-21 | employers.covered.transit_independent | employment | ambiguous | medium; long | invisible | B | CR-12b: (−) K3 raises labor cost, only partly passed back to workers (CR-7b, A-N2; CR-4c, A-13); (+) cheaper commuting by PHT draws workers to city jobs and lowers city wages (CR-7a, A-11), which raises hiring at any employer that pays them. The commuting chain has a different cause, so CR-12e does not apply | A-13, A-11, A-N2 |
| C-22 | employers.covered.relocating | employment (at city worksites) | decrease | medium; long | invisible | B | CR-4 (x: a city worksite, made worse by K3 with no gain in access for operations not tied to transit; y: a site just outside, A-9); CR-7a (the means that can move do so until yields are equal net of moving cost); CR-10b (the move happens as leases end and plant is replaced, so it is gradual) | A-9 |
| C-23 | employers.prospective.transit_independent | entry_rate (new worksites in the city) | decrease | medium; long | invisible | B | CR-4 (x: open in the city, y: open just outside, A-9; CR-4a: none switch toward the city because of K3); CR-7a; CR-10a (from the announcement, location choices take the expected tax into account) | A-9 |
| C-24 | employers.city_offices_of_outside_firms | resources_available_other_uses | U1-a: decrease; U1-b: no_change | short | invisible | B | CR-1 per reading: under U1-a total payroll above $750,000 makes the small city payroll taxable (op 4); under U1-b a city payroll at or below $750,000 is exempt. CR-6 (wages fixed at first, A-12); CR-3c, CR-8b | A-12 |
| C-25 | employers.city_offices_of_outside_firms | employment (city offices) | U1-a: ambiguous; U1-b: increase | medium; long | invisible | B | CR-4 mirror (a city office is made better by free travel for staff and customers, A-10); under U1-a CR-12b against K3 on its payroll (CR-4b), no dominance premise; under U1-b only the first chain applies | A-10 |
| C-26 | employers.covered | compliance_cost (quarterly returns, threshold records) | increase | short; medium; long | invisible | A | CR-1 (op 3: K3 attaches quarterly returns and payroll tests); CR-8c (resources spent on complying are used up) | none |
| C-27 | workers.covered_employers | earnings (bonus payments in June 2027) | increase | short (June 2027) | invisible | B | CR-10a (a charge expected from 1 July alters choices before it); CR-4 (x: pay a bonus due in July in July, taxed; y: pay it in June, untaxed; A-23); CR-5c (the timing is a term both parties can move). Signed per window: the bonuses are paid with or without the policy | A-23 |
| C-28 | workers.covered_employers | earnings (bonus payments in July to September 2027) | decrease | short (Q3 2027) | invisible | B | As C-27: the window from which the bonuses were moved | A-23 |
| C-29 | officials.revenue_department | tax_revenue_vs_static_projection | decrease | short; medium; long | invisible | B | CR-12d (independent chains with the same sign; reported if any one holds): payroll reshaped below the threshold (C-19, A-8); payroll moved out of the city (C-22, A-9); staff and hours cut (C-20, A-13); bonuses moved before 1 July (C-27, A-23, first quarter only) | A-8, A-9, A-13, A-23 |
| C-30 | business_associations, riders_groups | lobbying_effort | increase | short; medium; long | invisible | B | CR-4 (x: accept, y: lobby; K3 makes accepting worse for covered employers, and the review in 2029 and the Transit Reserve give riders a stake in expansion; A-15); CR-10a (the dated review alters choices before it); CR-8c (resources spent lobbying are used up) | A-15 |
| C-31 | employers.pass_buying | quantity_traded (employer annual passes) | decrease | short; medium; long | visible | A | CR-1 (op 1: with no fare, there is no pass to buy; existing passes are refunded pro rata); CR-5a (the exchange ends) | none |
| C-32 | employers.pass_buying | resources_available_other_uses | increase | short; medium; long | invisible | B | CR-8b (the $9 million a year the employers would have paid, A-22, stays with them); CR-7 note on a tax whose revenue buys something the payers value: their K3 payments (C-5) are signed separately and not netted | A-22 |
| C-33 | riders.fare_paying (pass holders) | compliance_cost (refund applications) | increase | short | invisible | A | CR-1 (op 4 conditional on applying); CR-8c (time spent applying is used up) | none |
| C-34 | park_and_ride_users | search_cost, wait_time | at_least_one_increase | short; medium; long | invisible | B | CR-9 (relation: a park-and-ride space is a complement to a PHT ride; the ride is now free, so demand for spaces rises, A-1); CR-6 (the $4 fee is fixed and lots are near capacity, A-20, so the gap is closed on at least one non-price margin: searching, arriving earlier) | A-1, A-20 |
| C-35 | officials.pht | non_tax_receipts (park-and-ride fees) | increase | short; medium; long | invisible | B | CR-9 (complement, as C-34); CR-4c (more spaces are taken at $4 until the lots fill; 15% are free on a weekday, A-20) | A-1, A-20 |
| C-36 | riders.ride_hail | price_substitute (ride-hail fares, off-peak) | decrease | short; medium | invisible | B | CR-9 (relation: PHT substitute for off-peak ride-hail; riders leave, A-6); CR-6 (the price is free and drivers do not withdraw as fast as riders, A-6, so the price moves toward a lower clearing level); in the medium run drivers' exit cannot push it back above the old level (CR-12e) | A-6 |
| C-37 | drivers.ride_hail | earnings | decrease | short; medium | invisible | B | CR-9 and LW-10 (demand for drivers' time follows demand for rides, C-36); CR-7a (drivers move to other uses until yields are equal net of moving cost, but the move cannot restore the old earnings, CR-12e) | A-6 |
| C-38 | drivers.taxi | quantity_traded (taxi trips) | decrease | short; medium; long | invisible | B | CR-9 (relation: PHT substitute for taxis); CR-4b (taxi riders at the margin switch, A-N3); the meter rate is fixed, so the fall is not absorbed by price | A-N3 |
| C-39 | riders.taxi | wait_time (−), quality_per_unit (+) | at_least_one_as_stated | short; medium | invisible | B | CR-6 (with the meter rate fixed above the new clearing level, the pressure from sellers goes to open margins: more idle taxis and shorter waits, or better service to win riders); CR-6 establishes at least one | A-N3 |
| C-40 | owners.housing_near_pht_lines | asset_value | increase | short (from announcement); medium; long | invisible | B | CR-9 (relation: PHT rides complement, location, to housing near lines, A-N1); CR-7b (the gain settles on the means that cannot move: housing near lines cannot expand quickly, A-21); CR-7c and CR-10c (the expected rise in yields is capitalized when it becomes expected, from the campaign and the bill's introduction, and captured by holders then; larger if continuation past the review is expected, A-14) | A-21, A-N1 |
| C-41 | renters.housing_near_pht_lines | price_paid (rents) | increase | medium; long | invisible | B | CR-9 and CR-7b as in C-40; CR-6 (existing leases fix rents while they last, so the rise comes as leases renew) | A-21, A-N1 |
| C-42 | owners.housing_near_pht_lines | subsidy_share_received | increase | medium; long | invisible | B | CR-7b (part of riders' gain from K1 settles on the immobile complement, housing near lines, A-21, through C-41) | A-21, A-N1 |
| C-43 | retailers.downtown | quantity_traded | increase | medium; long | invisible | B | CR-9 (relation: a PHT ride is a trip complement to downtown shopping; downtown is a substitute for the malls); CR-4 mirror (shoppers who choose partly by trip cost switch to downtown, A-16) | A-16 |
| C-44 | neighboring_jurisdictions.malls | quantity_traded | decrease | medium; long | invisible | B | CR-9 (relation: across_border substitute); CR-4b (shoppers at the margin leave the malls, A-16; CR-5 note: the mall loses the sale, the shopper does not) | A-16 |
| C-45 | neighboring_jurisdictions.business_parks | asset_value | increase | short (from announcement); medium; long | invisible | B | CR-9 (relation: across_border substitute for city worksites; demand rises with C-22 and C-23, A-9); CR-7c and CR-10c (the rise in expected yield is captured by holders when the tax becomes expected) | A-9 |
| C-46 | neighboring_jurisdictions.business_parks | employment | increase | medium; long | invisible | B | CR-9 (relocated worksites bring their jobs, C-22); CR-7a | A-9 |
| C-47 | owners.city_commercial_property | asset_value | ambiguous | short; medium; long | invisible | B | CR-12b: (−) K3 lowers the yield of city sites to transit-independent employers who can move (A-9), and CR-7b places the lasting loss on the immobile site, CR-7c; (+) free travel raises the yield of sites used by transit-linked activities: downtown shops (A-16), offices of outside firms (A-10). No premise says which dominates | A-9, A-10, A-16 |
| C-48 | workers.city_jobs | wage_rate | no_change | short | invisible | B | CR-6 (terms fixed by existing contracts count as regulated while those contracts last: A-12) | A-12 |
| C-49 | workers.city_jobs | wage_rate | ambiguous | medium; long | invisible | B | CR-12b: (−) CR-7b (K3's incidence is shared and workers who cannot all move to uncovered jobs bear part, A-N2); (−) CR-7a (cheaper commuting by PHT makes city jobs better net of commuting cost, so more workers offer labor to them, A-11); (+) CR-9 and LW-10 (more downtown trade raises demand for retail labor, A-16). No dominance premise | A-N2, A-11, A-16 |
| C-50 | workers.pht_commuters | job_changes | increase | medium | invisible | B | CR-7a and CR-4 (x: a suburban job, y: a city job reached by PHT, made better by the free ride; workers who chose by net pay switch, A-11). The rate rises during the adjustment | A-11 |
| C-51 | workers.suburban_jobs | wage_rate | ambiguous | medium; long | invisible | B | CR-12b: (+) relocating employers add demand for suburban labor (C-22, A-9); (+) PHT commuters move to city jobs (A-11); (−) workers leaving covered city employers offer labor in the suburbs (CR-7a, A-N2). No dominance premise | A-11, A-9, A-N2 |
| C-52 | sellers.contract_labor | quantity_traded (contract labor sold to employers near the threshold) | increase | short; medium; long | invisible | B | CR-9 (relation: contract labor substitute for payroll employment); CR-4 (employers near the threshold replace payroll with contracts, C-19, A-8) | A-8 |
| C-53 | fare_card_contractor | quantity_traded (fare-system services) | decrease | short; medium; long | invisible | A | CR-1 (op 1: K4 terminates the contract); CR-5a (the exchange would have continued under the counterfactual) | none |
| C-54 | officials.pht | resources_available_other_uses | decrease | short (FY 2027-28, one-time) | invisible | A | CR-8b (the $5 million termination payment and severance are paid by PHT); CR-3c (what is paid is not available for other uses) | none |
| C-55 | fare_card_contractor | resources_available_other_uses | ambiguous | short (FY 2027-28) | invisible | A | CR-12b: (+) CR-8b (the $5 million termination payment); (−) CR-5a (the gains from contract payments after September are lost). The record does not say which is larger in the first year | none |
| C-56 | fare_card_contractor | resources_available_other_uses | decrease | medium; long | invisible | A | CR-5a (the contractor loses the gain it expected from a contract that would have continued); CR-12e (redeploying its resources to other clients cannot restore more than the next-best use yields) | none |
| C-57 | residual_claimant (PHT and Transit Reserve) | fund_balance | increase | medium (to the 2029 review) | invisible | B | CR-8b and CR-8d (K3 receipts about $60.1 million projected net of 1.5%, fares lost $58 million, collection savings $13 million less the new posts, A-19); CR-12e (arithmetic: the change equals 2.1 − shortfall + (13 − cost of posts), positive when the shortfall is below the net savings, A-17); held by PHT rather than drawn by the city (A-18) | A-17, A-18, A-19 |
| C-58 | riders.off_peak, riders.peak_other_lines | quality_per_unit (crowding) | decrease | short; medium | invisible | C | CR-9 (relation: shared_facility, the vehicle; added riders, C-13 and C-14, fill seats and standing room that others used, A-2 and A-3); Tier C pending the question on shared-facility chains | A-1, A-2, A-3 |
| C-59 | riders.exempt (on tram 1, tram 4, bus 12 at the peak) | full_cost_per_unit | increase | short; medium | invisible | B | CR-6 (the rationing margins in C-16 fall on every peak rider of these lines, A-4); CR-1 (no money price change for exempt riders, who already rode free) | A-4 |
| C-60 | riders.peak_crush_lines (fare payers) | full_cost_per_unit | ambiguous | short; medium | invisible | B | CR-12b: (−) CR-1 (the $2 fare is removed); (+) CR-6 (waiting, crowding, being passed up, A-4). No premise says which dominates | A-4 |
| C-61 | riders.off_peak (fare payers) | full_cost_per_unit | decrease | short; medium; long | invisible | B | CR-1 (the $2 fare is removed); CR-12e (the added riders come only while their full cost is below the old one, and with room on vehicles, A-2, no rider is left behind; the remaining crowding chain, C-58, is Tier C and cannot reverse the change that causes it) | A-1, A-2 |
| C-62 | road_users | wait_time (road congestion) | ambiguous | short; medium | invisible | C | CR-9 (relation: shared_facility, roads); CR-12b: (−) some travelers leave cars off-peak (A-1, group only); (+) riders crowded off peak lines drive (A-4); (+) ride-hail drivers keep cruising with fewer fares (A-6) | A-1, A-4, A-6 |
| C-63 | riders.regional_rail | quantity_substitute (regional rail trips) | ambiguous | short; medium; long | invisible | B | CR-12b: (+) CR-9 (relation: complement; the PHT leg of a rail trip is free); (−) CR-9 and CR-4b (relation: substitute; trips within the city switch from rail to free PHT). Both relations rest on A-N4; no dominance premise | A-N4 |
| C-64 | officials.revenue_department | enforcement_cost (administering K3, auditing the threshold) | increase | short; medium; long | invisible | A | CR-1 (op 4: 1.5% of K3 retained for administration); CR-8c (resources spent on administering and enforcing are used up) | none |

## Gaps found

**(a) Steps no core rule covers.**
- GAP-032-C1: Physical relations in production. Whether more boardings lengthen bus stops (dwell time) and whether ending fare payment shortens them is a technical relation, not a choice, so no core rule derives it and no sign is given for bus riders' travel_time. CR-9's shared_facility clause covers the effect of one rider's use on another's, but not the supplier's production function.
- GAP-032-C2: Contingent payers. The general fund pays only if K3 receipts fall below $58 million. CR-8's note on payers from the general budget gives `at_least_one_decrease` for a cost that is funded from the budget, but no rule says how to record a payer whose payment depends on an outcome the analysis cannot sign. It is left unsigned under Not reported.
- GAP-032-C3: The motives of the supplier and the council. CR-6's public-supply clarification says the supplier does not respond as a seller would "unless the budget rule changes", but no core rule, and no premise in the case, says what the council will do at the 2029 review or with the Transit Reserve. CR-4 applies to political actors symmetrically, but only given their ranking, which the rules never assume. Consequences after the review are not signed.

**(b) Core-rule wording that was hard to apply.**
- CR-6 public supply and CR-9 shared_facility overlap. Crowding on a vehicle is both a rationing margin of a fixed public supply (CR-6, Tier B) and an effect of one rider's use on others sharing a facility (CR-9, Tier C pending the open question). The crush lines were treated under CR-6 (C-16, C-59) and the lines with room under CR-9 (C-58), but the rules do not say which governs when the same physical crowding is both.
- CR-4's note on lumpy costs speaks of "a large one-time cost" on an option. The K3 threshold is a cliff: a cost that recurs every year and depends on a quantity choice (payroll), so it is a notch in CR-4c rather than a one-time cost. The direction follows, but the wording fits only by analogy (C-19).
- CR-7b with three or more parties and a benefit chain. K3's burden is shared by employers, workers and site owners, while K1 raises some of the same parties' yields (commuting workers, transit-linked sites). CR-7b says to rank each pair, but with a benefit chain running through the same price every pair becomes ambiguous; the rule does not say how to state incidence when the tax and the spending act on the same market.
- CR-12e "a response cannot reverse the change that causes it": applying it to off-peak riders (C-61) needed the argument that the crowding comes from riders who join only while their own full cost has fallen; for riders who value comfort more than the marginal rider, crowding could in principle outweigh $2. The rule does not say whether the argument holds for inframarginal members of the class.
- CR-1 for a zero price: removing a charge is op 3 for fare payers, but for evaders it adds an option (op 2) and for exempt riders it does nothing. The rule handles this by splitting classes, which worked, but the classification table needs one row per class rather than per component.
- Persistence is defined only for repeals (2.5), but this policy creates durable stocks (relocated worksites, capitalized housing values) whose persistence after a later reversal matters. Recorded as notes in section 8.

**(c) Vocabulary missing from the ontology.**
- Instrument types: the input record says no type in 2.3 fits fare abolition or the service freeze, but 2.3 now lists `public_supply` (a good supplied by the state at a set price, quantity set by a budget), which covers both. The budget rule fixing quantity is a parameter of that type rather than a separate instrument; 2.3 could say so.
- Variables: no variable for vehicle occupancy or crowding (recorded as `quality_per_unit`); no variable for the location of worksites or relocation (recorded as `employment (at city worksites)` and `entry_rate`); no variable for service hours of a public supplier (recorded as `quantity_supplied`); no variable for the timing of pay (recorded as `earnings` per window). No variable records the information loss CR-11a describes when a price is held at zero (PHT loses the fare signal of where demand is highest), so CR-11a was applied without a consequence.
- Actor classes: 2.2 has no generic class for a contingent payer (a general fund that backs a dedicated tax), or for the supplier itself when the supplier is the rule-maker (here `officials.pht` was used).
- Relations: 2.8 has no relation type for a transfer between modes on one trip (rail to PHT); it was recorded as `complement`, like the trip-complement note for shopping.

## Comparison with the pattern-based analysis

**Summary.** The two versions agree on the main structure of the fare-free case. Both find that rides cost nothing, PHT loses fares and receives the tax, and covered employers bear it at first while wages are fixed. Off-peak ridership and peak boardings on lines with room rise. On tram 1, tram 4 and bus 12 there is excess demand, rationed by waiting, crowding and boarding order. Fare-paying riders keep the fares they no longer pay, and off-peak trips by other modes fall. Ride-hail fares fall off-peak, and park-and-ride users search longer. Housing near lines is capitalized at announcement and rents there rise. Employers near the threshold reshape payroll, transit-independent employers relocate and open fewer city sites, and bonuses move into June. Lobbying rises on both sides, revenue falls short of the static projection, the fare-card contract and the fare posts end, new posts are created, collection costs fall and PHT's reserve grows. Both versions leave road delay, peak mode choice, city wages, downtown sites and outside firms' offices under U1-a ambiguous. The differences are of four kinds. (1) **Five keys with different signs, all from omitted chains.** In the medium run, the pattern version keeps a decrease in staff or hours at transit-independent employers, but the commuting-wage chain it derived itself (C-36) runs against it. The core version signs all downtown retailers up, missing the labor-cost chain on covered retailers. It merges industrial and downtown sites into one ambiguous class, which loses the decrease for industrial sites. It gives covered pass buyers an increase in C-32 and a decrease in C-5 on the same key without combining them. On compliance cost, each version misses the chain the other found. (2) **Premises.** Two pattern claims (off-peak garage use and car ownership) need a premise about car drivers in particular, which A-1, a premise about all other modes together, does not give. The core version avoided this for cars and taxis (A-N3) but made the same move itself for contract labor (C-52). (3) **Core-version errors of its own.** Its CR-12e argument for off-peak fare payers (C-61) does not hold for riders who were already riding, as its own gap note concedes. Its one-time PHT decrease (C-54) contradicts its own section 8. (4) **Breadth.** The core version followed more relations and both sides of more transfers: evasion, ride-hail drivers, taxis, business-park values, park-and-ride receipts, the contractor's means and regional rail. The pattern version alone recorded the taxed bearers' forgone purchases. The two versions are not fully independent. The pattern version was written under catalog 0.6, and several 0.7 clarifications the core version relied on were drawn from this very example's gap notes: CR-6's public-supply clause and `at_least_one_as_stated` (its gaps b1, b2, d2), CR-9's `shared_facility` (its gap b3), CR-7's clause on a tax whose revenue buys something the payers value (its gap b4), SB-8's fixed-capacity clause (its gap c4) and the `public_supply` instrument type (its gap d1). Where a pattern-version record has since been superseded by one of these, it is counted as V, not as an error.

Counts: M 25, V 15, S 5, OP 22, OC 5.

### Pattern version → core version

| Pattern ID | Matched core ID(s) | Class | Cause | Note |
| --- | --- | --- | --- | --- |
| C-1 | C-1 | M | | Pattern class includes new riders; core has fare payers only. |
| C-2 | C-4 | M | | |
| C-3 | C-5 | V | | Pattern: labor cost per hour (`price_paid`) increase. Core: covered employers' `resources_available_other_uses` decrease; the per-hour cost rise appears in C-20's derivation. Both short and both on A-12. |
| C-4 | C-13 | M | | |
| C-5 | C-14 | V | | Pattern: all peak lines. Core: lines below crush only; the crush lines are covered by C-15 and C-16. |
| C-6 | C-58, C-16 | V | | Same direction, different derivation and tier. On lines below crush there is no excess demand, so CR-6 does not apply there; the pattern version's own section 2 says so. Crowding is one rider's use of a shared vehicle, which 0.7 records as `shared_facility` at Tier C (CR-9), drawn from this example's gap b3. On crush lines the core puts it in the C-16 group. The core's C-58 also covers off-peak riders, where the pattern version's final check said there was no crowding chain except under A-7. That is a pattern-version slip, but only at Tier C. |
| C-7 | C-15 | M | | |
| C-8 | C-16 | V | | Pattern: `wait_time` increase on its own, on A-4. Core: one group, `at_least_one_as_stated`, the record that 0.7 added from this example's gaps b2 and d2. CR-6 wants a premise for each margin. A-4 nearly gives pass-ups, because at crush load the crowding margin is used up, but riders could also shift to the shoulders of the peak. Not counted as an error. |
| C-9 | C-16 | V | | As C-8, for allocation by boarding order. |
| C-10 | C-2 | M | | Both A-5. |
| C-11 | C-33 | S | E | The two versions reach opposite signs for overlapping classes on the same key (fare payers, `compliance_cost`, short). Pattern: decrease (no ticket buying, top-ups or fines). Core: increase for pass holders (refund applications). Each version omits the other's chain. The pattern misses the refunds "on application" in the record; the core misses the end of ticket buying (CR-1 op 3 removes paperwork; CR-8c). The pattern also puts fines in `compliance_cost`, but fines are a transfer (CR-8b) and belong to evaders, whom the core records as C-6. Correct record: single-fare riders decrease; pass holders ambiguous in the short run. |
| C-12 | C-17 | V | | Pattern: other modes "taken together" decrease. Core: group `at_least_one_decrease`. Both follow from CR-4b with A-1. |
| C-13 | C-18, C-17 | V | | Pattern: all peak travelers, ambiguous. Core: ambiguous in the crush corridors (C-18), but lines below crush are folded into C-17's decrease. That drops the crowding chain there, though it is only Tier C under 0.7. Not a sign conflict at the pattern version's level of aggregation. |
| C-14 | none | OC | P | Car ownership, ambiguous. Both chains need a premise that some marginal travelers own or would buy cars. A-1 covers only the other modes together, and the pattern version's own C-12 says no single mode is signed. The core version pruned car-specific chains for this reason (section 6), and that is the better answer. Low stakes, since the key is ambiguous. |
| C-15 | C-26 | M | | |
| C-16 | C-19 | V | | Pattern: `reclassification` alone. Core: group of reclassification (+) or employment (−). A-8 ("reshaping payroll") fits the pattern's single sign, so neither is wrong. |
| C-17 | C-25 | V | | `entry_rate` against `employment` (city offices). Same signs per reading. Core adds C-24 (means, per reading). |
| C-18 | C-23, C-22 | M | | Both versions leave out the commuting-wage chain (CR-7a with A-11), which lowers city wages for any employer competing for PHT commuters. The pattern dodges it by defining the class as employers whose staff rarely use PHT. The core does not: its class is "operations do not depend on transit", and it uses the chain for employment (C-21) but not for location (C-22, C-23). See Findings. |
| C-19 | C-46 | V | | `entry_rate` at boundary sites against business-park `employment`. Core adds C-45 (asset value). |
| C-20 | none | OC | J | Transit-linked employers' city entry, ambiguous (CR-4 x: city site, y: outside, with K3 (−) against access (+)). The core rules give both chains, and the core has C-47 for their sites, but it did not record the key. Nothing signed is lost. |
| C-21 | C-20, C-21 | S | E | Short run: M (core C-20). Medium run: pattern `at_least_one_decrease`, core ambiguous. The core is right. The commuting-wage chain (CR-7a, A-11) is an independent cause, so CR-12e does not rule it out. The pattern version derived this chain itself in C-36, chain (2), but did not carry it into C-21, and A-12 (wages fixed) holds only in the short run. Pattern-version error. |
| C-22 | C-30 | M | | |
| C-23 | C-27 | M | | Window April–June against June. |
| C-24 | C-28 | M | | Window July–December against July–September. |
| C-25 | C-36 | M | | |
| C-26 | C-62 | V | | Pattern: peak road delay, Tier B, derived as CR-6 on road space. Core: all road users, Tier C (`shared_facility`, 0.7, drawn from this example's gap b3). Both ambiguous. |
| C-27 | C-43 | M | | Downtown sellers below the threshold. Horizon short–medium against medium–long. |
| C-28 | C-43 | S | E | Pattern: covered downtown sellers, ambiguous (more trips (+) against the higher labor cost (−)). Core: all downtown retailers increase. The (−) chain is derivable at depth 1. K3 raises the covered seller's own cost (CR-1 op 3), and buyers move to exempt competitors (CR-4b). The core's pruning of covered employers' output prices as "diffuse bystander effects" does not cover the seller itself. Core-version omission. |
| C-29 | C-44 | M | | |
| C-30 | none | OC | P | Off-peak downtown garage use decrease rests on A-1, which licenses only the other modes together. It needs a premise that some marginal off-peak travelers drove downtown, a hidden premise. The core version declined it for this reason. With such a premise (and RS-12's own) the decrease is valid. |
| C-31 | C-34 | M | | |
| C-32 | C-40 | M | | Premises differ. The pattern rests on A-1 and A-14. The core rests on A-21 and a new A-N1 (households choose where to live partly by trip cost), and keeps A-14 for size only. The core is right on both counts. A-1 does not cover residential choice. CR-7c gives the same sign for a two-year change, as the pattern version's own "If false" for A-14 concedes, so A-14 is not needed for the sign. |
| C-33 | C-41 | M | | |
| C-34 | C-47 | S | E | Pattern: industrial sites decrease. Core: one class, `owners.city_commercial_property`, ambiguous. The core merged two classes with opposed chains. CR-1's recording note asks for a split where the operation differs. That merge lost the signed decrease for sites whose users gain nothing from transit. Core-version error. Both versions omit the commuting-wage chain here (see C-18). |
| C-35 | C-47 | M | | Downtown sites ambiguous in both. |
| C-36 | C-49 | M | | The pattern's chain (1), part of K3 shifted to workers, needs a premise that workers cannot all move to uncovered jobs. The core states it as A-N2; the pattern leaves it unstated. The sign is ambiguous either way. |
| C-37 | none | OC | J | Covered employers' labor cost in the medium run, ambiguous (tax (+) against the commuting-wage chain (−)). Derivable; the core recorded only the wage (C-49). Nothing signed is lost. |
| C-38 | C-32 | M | | Exempt pass buyers. Both on A-22. |
| C-39 | C-32, C-5 | S | E | Pattern: covered pass buyers ambiguous (saved passes (+) against tax (−), CR-12b). Core: C-32 increase for all pass buyers, of whom "most are also covered", plus C-5 decrease for covered employers, left uncombined. That leaves two opposite signs on one key, which CR-12b does not allow. The 0.7 CR-7 clause ("sign each side separately and combine only with a premise") was drawn from this example. It means a combined sign needs a premise, not that overlapping keys stay uncombined. Core-version error, though the clause's wording invites it. |
| C-40 | C-8 | M | | |
| C-41 | C-10 | M | | |
| C-42 | C-53 | M | | |
| C-43 | C-7 | M | | Core horizon starts at medium, though collection ends in September 2027; short applies too. |
| C-44 | C-57 | V | | `resources_available_other_uses` (Transit Reserve) against `fund_balance` (residual claimant). Same premises: A-17, A-18, A-19. The pattern's medium-run combination includes the year-one $5 million payment, which mixes horizons (CR-12g). The core separates it. |
| C-45 | C-64 | M | | |
| C-46 | C-29 | M | | The core lists four independent chains under CR-12d; the pattern cites TX-9 on A-8 and A-9. |
| C-47 | C-5 | V | | Pattern: `tax_bearers`, short–medium. Core: covered employers, short only. The core does not record the bearers' side after wages adjust. CR-8b gives a group decrease for employers, workers or site owners in the medium run, and the core leaves it to "cannot say". Minor core omission. |
| C-48 | none | OC | E | Forgone sales where the bearers would have spent (CR-8a, CR-9). A use is given up even if it is saving (0.7, CR-4), and someone on the other side of it loses. Core-version omission. |
| C-49 | C-3 | V | | `net_price_received` against `non_tax_receipts`. |
| — (PHT all staff, employment, decrease) | C-9 | V | | Pattern class: all PHT staff. Core class: former fare staff, all roles. Same arithmetic (60 < 140, A-19). |

### Core-only consequences

| Core ID | Class | Cause | Note |
| --- | --- | --- | --- |
| C-6 | OP | E | Fare evasion stops being a breach (CR-1 op 2). The pattern version noted fines only inside C-11. 0.6 had `informal_activity` for it. Pattern-version omission. |
| C-11 | OP | J | Service hours `no_change`. The counterfactual has the same timetable; a recording choice. |
| C-12 | OP | J | `quantity_demanded` of PHT rides. A demand-side record of the response the pattern version records as `quantity_traded` per segment plus `excess_demand`. Nothing new. |
| C-24 | OP | J | Outside firms' means, per reading. Implied by the pattern's C-17 text and C-47. |
| C-31 | OP | E | Employer passes no longer bought (CR-1 op 1). Trivially derivable; pattern-version omission. |
| C-35 | OP | E | PHT's park-and-ride fee receipts rise (CR-9, A-20). The receipt side of C-34's demand; pattern-version omission. |
| C-37 | OP | E | Ride-hail drivers' earnings fall (CR-9, LW-10, A-6). Pattern-version omission. |
| C-38 | OP | A | Fewer taxi trips. The pattern version says this is "inside C-12" with no taxi-specific premise. The core adds A-N3, which is the right standard. |
| C-39 | OP | E | Taxi riders wait less or get better service (CR-6 with the meter above the new clearing level; A-N3). The pattern version noted the fixed meter but did not apply CR-6 to it. |
| C-42 | OP | J | Owners' `subsidy_share_received`. Implied by C-40 and C-41; a recording choice. |
| C-45 | OP | E | Business-park asset value rises from announcement (CR-7c, CR-10c, A-9). Pattern-version omission of capitalization (workflow final check 7). |
| C-48 | OP | J | City wages `no_change` in the short run. This records A-12 as a consequence. |
| C-50 | OP | E | PHT commuters change jobs toward the city (CR-4, CR-7a, A-11). In the pattern version's C-36 text but not recorded. |
| C-51 | OP | J | Suburban wages ambiguous. Derivable; not recorded by the pattern version. |
| C-52 | OP | E | More contract labor sold to employers near the threshold. A-8 licenses only "reshaping payroll" as a group (contractors, splitting firms, fewer staff, as C-19 itself records). Contract labor in particular needs its own premise, the standard the core version applied to taxis (A-N3) and cars. Core-version hidden premise. |
| C-54 | OP | E | PHT's means decrease in FY 2027-28 from the termination payment and severance. Its own section 8 sets these against July–August tax receipts and collection savings and says the first-year balance cannot be signed. By CR-12b, the key (`officials.pht`, `resources_available_other_uses`, short) is ambiguous. Core-version error (one chain signed alone). |
| C-55 | OP | J | Contractor's first-year means, ambiguous (termination payment against lost contract gains). |
| C-56 | OP | E | Contractor's means decrease in the medium and long run (CR-5a). The pattern version's final check 6 claims both sides of the termination payment but records only `quantity_traded` for the contractor. Pattern-version omission. |
| C-59 | OP | J | Exempt riders on the crush lines: `full_cost_per_unit` increase. The pattern version made the same point in words (C-6, C-8: "including seniors and pupils") but declined the variable because its definition omits crowding (its gap d3). That definition is unchanged in 0.7 (2.4), so the core version stretches it. With waiting alone, C-16's group would not give the sign. |
| C-60 | OP | J | Fare payers on the crush lines: `full_cost_per_unit` ambiguous. The pattern version says the same in words; vocabulary as C-59. |
| C-61 | OP | E | Off-peak fare payers: `full_cost_per_unit` decrease, combined by CR-12e. Riders already on board did not choose the crowding that others' boarding creates, so "a response cannot reverse its cause" does not bound their cost. The core version's own gap note (b4) concedes this. The (+) chain is Tier C. The sign needs an empirical dominance premise (for example, off-peak crowding small next to $2, building on A-2) or `ambiguous`. Core-version error. |
| C-63 | OP | J | Regional rail trips ambiguous (A-N4). Scope: the pattern version did not follow the province's rail. |

### Findings

- **Pattern overclaims and hidden premises.** C-30 (garages) and C-14 (car ownership) use A-1, which covers only the other modes together, for claims about cars in particular. C-32 uses A-1 for where households live; the core's A-N1 is the missing premise. C-36's chain (1) needs a premise on workers' alternatives to covered jobs, which the core states as A-N2. C-6 cites CR-6 for crowding on lines below crush, where by the pattern version's own section 2 there is no excess demand. Under 0.7 that crowding is a `shared_facility` chain at Tier C. C-8 and C-9 sign two CR-6 margins separately on A-4 alone. That is defensible for pass-ups once crush load is reached, but 0.7 now records them as one `at_least_one_as_stated` group.
- **Errors in the pattern version.** C-21 keeps a medium-run decrease against the commuting-wage chain the analysis itself derived (C-36). C-11 omits refund applications and counts fines, a transfer, as `compliance_cost`. C-44 folds year-one payments into a medium-run sign (CR-12g). The final check wrongly states that off-peak crowding exists only under A-7. Omissions: evasion (C-6), passes no longer bought (C-31), park-and-ride receipts (C-35), ride-hail drivers' earnings (C-37), taxis under the fixed meter (C-39), business-park capitalization (C-45), job changes (C-50), and the contractor's means (C-56).
- **Errors in the core version.** Downtown retailers are signed up without the covered sellers' labor-cost chain (C-43). Industrial and downtown sites are merged into one ambiguous class (C-47), losing the industrial decrease. Covered pass buyers carry two uncombined opposite signs (C-32 with C-5). Off-peak fare payers' full cost is signed with a CR-12e argument that does not bind riders already on board (C-61). PHT's one-time decrease (C-54) contradicts its own section 8. Contract labor (C-52) rests on a premise that licenses only a group. Location results (C-22, C-23, C-45, C-46) ignore the commuting-wage chain that C-21 uses. Under the core's class definition the chain applies, so either the class must be narrowed to employers whose staff do not commute by PHT, as the pattern version does, or these keys become ambiguous. Omissions: ticket-buying effort ended (part of the pattern's C-11), forgone sales (C-48), labor cost in the medium run (C-37), and transit-linked employers' entry (C-20).
- **Limits of the core rules.** None produced a difference here. Every pattern-version claim that the core version lacks is derivable from CR-1 to CR-12, so no K is assigned. The core version's own gaps stand. Physical relations such as bus dwell time cannot be derived (GAP-032-C1). There is no rule for a contingent payer such as the general fund (GAP-032-C2), and none for what the council will do at the review (GAP-032-C3). Two wording problems contributed to core-version errors. CR-7's 0.7 clause on a tax whose revenue buys something the payers value says "sign each side separately" but does not say that overlapping keys must still be combined under CR-12b (C-32). CR-12e does not say whether "a response cannot reverse its cause" covers members of a class who did not make the response (C-61). `full_cost_per_unit` still omits loss of quality, which both versions ran into (pattern gap d3; core C-59, C-60).
