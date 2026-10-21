# WE-032 Fare-free buses and trams funded by an employer payroll tax

Analyst: draft (Handbook 0.6; corrected under 0.8)  |  Rule catalog version: 0.8  |  Status: awaiting expert review

A stylized policy in a fictional city, chosen to probe parts of the method the first 25 examples do not test. Here a public supplier sets its own price at zero, and the quantity it supplies is fixed by its budget. That is not a `price_ceiling` on private sellers, so PC-1 to PC-16 do not fit as written. Catalog 0.7 added the `public_supply` instrument and PC-19 for this case, drawn from this example's gap notes. The case also probes SB-8 for riders who would have paid anyway, effects that pass through a shared unpriced facility (the roads), and a local payroll tax whose revenue buys something the taxed employers themselves partly value. The probabilities are illustrative; the evidence column says what a real analysis would cite.

## 1. Policy record

**Port Hallam Fare-Free Transit Act.** Port Hallam is a city of about 620,000 people in a metropolitan area of 1.3 million. Its western boundary lies 4 to 8 km from downtown; the suburban municipalities of Westmere and Calder Vale begin there, with business parks and two car-oriented shopping malls just across the line. Port Hallam Transit (PHT), a city-owned authority, runs 4 tram lines and 62 bus routes, two of which run 3 km into Westmere. In 2026 PHT carried 92 million boardings. It collected $58 million in fares (single fare $2.00, monthly pass $70) against operating costs of $240 million. Fare collection cost about $13 million a year: $6 million for the fare-card system contract, $3 million for cash handling and ticket offices, and $4 million for fare inspection. Collection employed 140 staff: 85 inspectors and 55 ticket-office and cash staff.

Seniors over 65 and school pupils already ride free; they account for about 22% of boardings. About 5% of boardings were estimated to be fare evasion. 260 employers buy discounted annual passes for about 31,000 staff, at about $9 million a year.

At the morning peak, tram lines 1 and 4 and bus route 12 run at about 95% of planning capacity (four standing passengers per square meter); crush load is about six per square meter. Most other lines run at 60 to 75% of planning capacity at the peak. Off-peak occupancy averages 35%.

Taxi fares are set by a city meter rate. Ride-hail prices are not regulated. A private bike-share scheme charges $1 a ride. Regional commuter rail is run by the province and is not part of PHT.

The mayor campaigned on fare-free transit. The council introduced the bill on 10 February 2027 and enacted it on 28 April 2027. The payroll tax applies to wages paid from 1 July 2027 and is collected quarterly from October. Fares end on 1 September 2027.

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Fare abolition | `public_supply` at a set price of zero, funded from K3 | Rides on all PHT buses and trams, including the two routes into Westmere | PHT | Fare $0 for every rider from 1 September 2027. Fare inspection ends. Unused value on passes bought before then is refunded pro rata on application. | Regional commuter rail is not covered. PHT park-and-ride lots keep their $4 daily fee. |
| K2 Service freeze | Budget rule fixing the quantity supplied (the quantity part of `public_supply`) | PHT service hours | PHT | Service hours are held at the 2026–27 timetable for fiscal years 2027–28 and 2028–29. "After which the council shall review service levels." | None |
| K3 Payroll tax | `ad_valorem_tax` on labor | Gross wages paid to employees at a worksite in the city | Private employers with a worksite in the city and annual payroll above $750,000 | 0.40% of gross city payroll. Once an employer is over the threshold, all its city payroll is taxed (a cliff, not an allowance). Projected revenue $61 million a year. Quarterly returns to the City Revenue Department; penalty of 10% plus interest on late payment. | Public employers, registered charities, employers at or below the threshold. |
| K4 Fare-system wind-down | Administrative provision | PHT's fare-collection operation | PHT | The fare-card contract is terminated, with a termination payment of $5 million. Fare staff are "redeployed to customer-service and safety roles where possible"; the rest receive severance. | None |

Revenue use: K3 revenue goes to PHT, less 1.5% kept by the Revenue Department for administration. Revenue above $58 million is "held in a Transit Reserve for service expansion after the review". Any shortfall below $58 million is covered from the city's general fund.

Unclear provisions:
- **U1.** Whether the $750,000 threshold is measured on the employer's total payroll or only its payroll at worksites in the city. The Act says "an employer with a worksite in the city whose annual payroll exceeds $750,000". Reading U1-a: total payroll, wherever the work is done. Reading U1-b: city payroll only. The tax base is city payroll under both readings. Readings get no probability; where a sign depends on the reading, one sign per reading is given.
- How many fare staff are redeployed. The Act says "where possible". PHT's published plan creates about 60 customer-service and safety posts, and the staff union has agreed the transfer terms. Because the record supplies this evidence, it is treated as an assumption (A-19), not a reading (`02_ontology.md`, 2.5).

Counterfactual: the same city with the same 2026–27 timetable, fares at $2.00 and the $70 pass, and no payroll tax. Out of scope for version 1: environmental effects, health effects of walking and cycling, and safety on crowded vehicles. Congestion's effect on road users is recorded only through `travel_time`.

## 2. Classification

| Component | Rothbard type | Binding? | Rule families |
|---|---|---|---|
| K1 | Binary: the state gives riders a good below its cost, funded by K3. | Yes: the price is zero by law. | PC-19 (CR-6, public supply), SB-8, RS-16 (mirror case), CR-4, CR-9, CR-7c |
| K2 | A fixed quantity, set by the supplier's own budget rule. | Yes, for two years. | PC-19 (the quantity cannot respond), CR-10b |
| K3 | Binary: a forced payment, levied on hiring labor in the city. | Yes, for covered employers. | TX-1, TX-2, TX-3, TX-5, TX-9, RS-4, RS-5, RS-8, DM-1, OC-3 |
| K4 | Binary, inside the state: resources used to collect fares are released. | Yes | CR-8a, CR-8c, CR-9 |

**Is a zero fare a price ceiling?** Not as the instrument is defined. A `price_ceiling` forbids private sellers to charge more than a cap. Here the seller is the city's own authority, its quantity is fixed by K2, and it is made whole from K3. The PC patterns therefore do not fit as written:
- PC-5 (supply shrinks) needs sellers who move resources to uncapped uses. PHT's supply is fixed by K2.
- PC-4 and RS-2 (quality falls) need a seller who gains by cutting quality. PHT gains nothing.
- PC-6 (black markets) needs a seller who can accept a side payment. No one can pay PHT more for a place.
- PC-16 (a ceiling is a transfer from sellers) does not apply: the transfer comes from K3's payers, not from the seller.

What does carry over is CR-6, through its 0.7 clause on public supply, which PC-19 states as a pattern. Where at a zero fare riders wish to take more rides than K2 supplies, the gap is not closed by price, and the pressure goes to the margins open to riders sharing the fixed quantity: crowding on board (a fall in the quality of each ride), waiting when full vehicles pass stops, and allocation by boarding order. These move in opposite directions, so PC-19 records them as one group with sign `at_least_one_as_stated`. Where demand at zero is below capacity (off-peak, most lines at the peak), there is no gap and CR-6 does not apply: more riders simply ride. The space they take from riders already aboard is a `shared_facility` relation (CR-9, 0.7), and chains through it are Tier C pending `06_gaps.md`, Q20. Section 5 therefore splits riders by segment.

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `riders.would_ride_anyway` | Fare-paying riders who would have ridden at $2 (including non-residents from Westmere): single-fare and card riders, and pass holders | Same rides, no fare. At the peak, more crowding. Pass holders apply for refunds. |
| `riders.evading` | The riders behind the 5% of boardings that were fare evasion | Riding without paying is no longer a breach. |
| `riders.new` | People who ride only at a zero fare | A new option at no money price. |
| `riders.concession` | Seniors and pupils who already rode free | No price change; more crowding at the peak. |
| `riders.offpeak`, `riders.peak`, `riders.peak.busiest_lines` | Riders off-peak; at the peak on all lines; and at the peak on tram 1, tram 4 and bus 12 | Lower money price, fuller vehicles; on the busiest lines, pass-ups. |
| `travelers.offpeak`, `travelers.peak` | Everyone choosing a mode for a trip | Transit's money price falls; at the peak its quality falls too. |
| `sellers.substitutes` | Taxi drivers (meter rate fixed), ride-hail drivers (price free), bike share | Fewer riders off-peak. |
| `drivers.ride_hail`, `drivers.taxi` | Ride-hail and taxi drivers | Fewer fares; ride-hail fares fall, taxi fares are fixed by the meter. |
| `riders.taxi` | People who keep using taxis | Taxi drivers compete for fewer riders at a fixed meter rate. |
| `road_users.peak` | Drivers and passengers on congested peak roads | Traffic changes with mode choice (C-13). |
| `park_and_ride_users` | Suburban drivers who park at PHT lots ($4 fee kept) | The rides they connect to are free; the lots are fixed in size. |
| `employers.covered` | Private employers over the threshold | Pay 0.40% of city payroll; file returns. |
| `employers.covered.not_transit_linked`, `employers.covered.transit_linked` | Covered employers whose staff and customers do not, in practice, reach them by PHT (warehouses, plants and back offices away from the lines); and those whose staff or customers do (downtown offices and retail) | Tax only; or tax plus better access for staff and customers. |
| `employers.near_threshold` | Employers with payroll just above or below $750,000 | The cliff rewards staying below it. |
| `employers.outside_branch` | Large firms based outside the city with small city offices | Taxed under U1-a; exempt under U1-b if city payroll is below the threshold. |
| `employers.pass_buyers.exempt`, `employers.pass_buyers.covered` | Employers that bought staff passes | No longer need to buy them; the covered ones also pay the tax. |
| `workers.covered`, `workers.city` | Employees of covered employers; all employees working in the city | Their employers' labor cost rises. Commuting to city jobs by transit becomes free. |
| `neighboring_jurisdictions` | Westmere and Calder Vale, their business parks and malls | Untaxed sites just across the line. |
| `owners.business_parks` | Owners of business-park sites in Westmere and Calder Vale | Their sites are the alternative to taxed city sites. |
| `sellers.downtown.exempt`, `sellers.downtown.covered` | Downtown shops and restaurants below and above the threshold | Transit trips downtown are free. The covered ones also pay the tax. |
| `sellers.car_oriented_retail` | The two suburban malls | Compete with downtown for shopping trips. |
| `garage_operators.downtown` | Private parking garages downtown | Car trips downtown are complements to their service. |
| `owners.residential_near_lines`, `tenants.near_lines` | Owners and renters of housing near PHT lines, including on the Westmere routes | Housing near free transit is worth more to occupiers. |
| `owners.industrial_sites_city`, `owners.downtown_commercial` | Owners of city business sites | The tax lowers what covered users will pay; transit access raises what some will pay. |
| `PHT`, `PHT.fare_staff` | The authority (the residual claimant on K3 revenue above $58 million, through the Transit Reserve) and its 140 fare staff | Fare revenue replaced by tax revenue; collection work ends. |
| `general_fund_payers` | Taxpayers, recipients of other city spending and future taxpayers through borrowing | Make up any K3 shortfall below $58 million. |
| `input_suppliers.fare_system` | The fare-card contractor | Contract terminated. |
| `officials.revenue` | City Revenue Department | New tax to administer. |
| `tax_bearers` | Whoever ends up bearing K3: covered employers at first; later also city workers, owners of city sites and buyers from covered employers | Means taken. |
| `sellers.forgone` | Sellers (and borrowers, where the bearers would have saved) on the other side of the uses the tax bearers give up | Lose that spending or lending. |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | `riders.would_ride_anyway`, `riders.new` | `price_paid` (fare per ride) | decrease | short to medium | CR-1 (op 3: the payment attached to riding is removed) | none |
| C-49 | `PHT` | `net_price_received` (fare per ride) | decrease | short to medium | CR-8b (what riders no longer pay, PHT no longer receives) | none |
| C-2 | `officials.revenue` | `tax_revenue` (payroll tax) | increase | short | TX-1 | none |
| C-3 | `employers.covered` | `price_paid` (labor cost per hour: wage plus tax) | increase | short | TX-2, DM-1 (money wages fixed in the short run) | A-12 |
| C-50 | `riders.evading` | `legal_breach` (fare evasion) | decrease | short to medium | CR-1 (op 2: riding without paying becomes lawful) | none |
| C-51 | `employers.pass_buyers.exempt`, `employers.pass_buyers.covered` | `quantity_traded` (employer annual passes) | decrease | short | CR-1 (op 1: with no fare there is no pass to buy), CR-5a | none |

C-1 is the visible effect: rides cost nothing. `riders.concession` already paid nothing, and their money price does not change. C-49 is the other side of C-1 (CR-8b). The 5% of boardings that were evasion stop being breaches (C-50); the inspection fines evaders paid were a transfer to PHT (CR-8b), which ends with them. Employers stop buying staff passes (C-51); the means this frees are C-38 and C-39. K3 replaces the lost fare revenue with tax revenue, and section 9 records who bears it. In the short run, money wages are fixed by contracts and custom (A-12), so covered employers bear K3 at first (C-3). Section 7 says why that changes.

## 5. Responses

**Riders and travelers (K1, K2)**

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-4 | `riders.offpeak` | `quantity_traded` (off-peak rides) | increase | short to medium | CR-4 (mirror case: transit made cheaper relative to other modes), TS-8 | A-1, A-2 |
| C-5 | `riders.peak` | `quantity_traded` (peak rides) | increase | short | CR-4, CR-6 | A-1, A-3 |
| C-6 | `riders.offpeak`, `riders.peak` (lines below crush load; paying, concession and former evaders alike) | `quality_per_unit` (space per rider: crowding) | decrease | short to medium | CR-9 (relation `shared_facility`: the vehicle; added riders take seats and standing room others used); Tier C pending Q20 | A-1, A-2, A-3 |
| C-7 | `riders.peak.busiest_lines` | `excess_demand` | increase | short to medium | PC-19 (CR-6, public supply) | A-4 |
| C-8 | `riders.peak.busiest_lines` | `wait_time` (+: vehicles passing full), `quality_per_unit` (−: crowding up to crush load), `allocation_by_non_price_criteria` (+: places go by boarding order) | at_least_one_as_stated | short to medium | PC-19 (CR-6, public supply), LW-6 | A-4 |
| C-10 | `riders.would_ride_anyway` | `resources_available_other_uses` | increase | short to medium | SB-8; CR-4 "A change in means alone" (no named use) | A-5 |
| C-11 | `riders.would_ride_anyway` (single-fare and card riders; pass holders once refunds are settled) | `compliance_cost` (buying tickets, topping up cards, buying passes) | decrease | short to medium | CR-1 (op 3), CR-8c | none |
| C-52 | `riders.would_ride_anyway` (pass holders) | `compliance_cost` | ambiguous | short (autumn 2027) | CR-1 (op 3: a refund conditional on applying) and CR-8c (+) vs CR-1 (op 3) and CR-8c (no passes to buy) (−); CR-12b | none |
| C-12 | `travelers.offpeak` | `quantity_substitute` (off-peak trips by car, taxi, ride-hail, bike share, bicycle and on foot, taken together) | decrease | short to medium | CR-4, RS-16 (mirror case); CR-12e against the Tier C crowding chain | A-1, A-28 |
| C-13 | `travelers.peak` | `quantity_substitute` (peak trips by other modes, taken together) | ambiguous | short to medium | CR-4 for the fare (−) vs CR-4 for crowding and waits (C-6, C-8) (+); CR-12b | A-1, A-3, A-4 |

Off-peak (C-4), vehicles have room (A-2), so a zero fare simply adds riders: people at the margin between PHT and walking, cycling, driving or a taxi (A-1), and trips not made at all at $2. The rise builds over weeks as routines change (TS-8). CR-4c says the rides added are the ones valued least: short hops of a stop or two, and uses other than travel. Some of these new rides replace trips by other modes, so trips by other modes taken together fall (C-12). Which mode loses most is not signed. Riders already aboard off-peak do lose some space to the new riders (C-6, Tier C), and CR-12e (0.8) does not bind them: the new riders as a whole cannot reverse the fare cut that drew them, but a rider who did not respond can be crowded off. C-12 keeps its sign on an empirical dominance premise (A-28): with average occupancy at 35%, the space lost is small next to a $2 fare.

At the peak, the fare falls but capacity does not (K2). On most lines vehicles are below crush load (A-3), so more riders board standing: peak rides rise (C-5). Every rider on those lines, including seniors and pupils who gained nothing on price, has less space (C-6). That is not CR-6: there is no excess demand on those lines. It is one rider's use of a shared vehicle, which 0.7 records as a `shared_facility` chain at Tier C. On the busiest lines, demand at zero exceeds even crush load (A-4). That is excess demand (C-7), and PC-19 says the pressure goes to the margins open to riders: vehicles fill at the outer stops and pass riders waiting at inner stops, the remaining space is used up to crush load, and places go by where and when a rider boards. CR-6 establishes that at least one of these is used, not which; they move in opposite directions, so they are one group with sign `at_least_one_as_stated` (C-8). A-4 makes pass-ups likely once crush load is reached, but riders could also move to the shoulders of the peak, so no member is signed alone.

For a peak rider who would have paid anyway, the money price falls and the non-money cost rises. CR-6 says the full price tends back toward the level that rations the fixed capacity, so whether such riders are better off is not signed. `full_cost_per_unit` would be the natural variable, but its definition covers waiting, search and side payments, not crowding (Gaps (d)). The same two chains reach mode choice at the peak (C-13). Some peak riders leave for cars, taxis or bicycles because of crowding, while others arrive because of the fare. The combined sign is ambiguous (CR-12b).

C-10 is SB-8. For riders who would have ridden at $2, free rides work like a cash grant of the fares they no longer pay. Which uses rise with that money is not signed: it is a change in means alone (CR-4), saving is one of the uses (CR-4, 0.7), and no premise in this case names one. SB-8's 0.7 clause on fixed capacity applies at the peak: riders who would have paid anyway share the vehicles with new riders (C-6, C-8). C-11 is the time and effort no longer spent buying tickets, topping up cards and buying passes. Pass holders must apply for the pro rata refund on passes bought before 1 September, which takes time in the autumn of 2027, while they also stop buying passes; that short-run key is ambiguous (C-52). Inspection fines are not a compliance cost but a transfer (CR-8b), and belong to evaders (C-50).

**Employers (K3)**

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-15 | `employers.covered` | `compliance_cost` (registration, quarterly returns) | increase | short | TX-5 | none |
| C-16 | `employers.near_threshold` | `reclassification` (payroll kept at or below $750,000: outsourcing, contractors, splitting firms) | increase | short to medium | RS-5 | A-8 |
| C-62 | `employers.outside_branch` | `resources_available_other_uses` | U1-a: decrease; U1-b: no_change | short | CR-1 (op 4 under U1-a only), CR-8b, CR-3c | A-12 |
| C-17 | `employers.outside_branch` | `entry_rate` (small city offices of large outside firms) | U1-a: ambiguous; U1-b: increase | medium | U1-a: RS-4 (−) vs CR-9, CR-4 (transit access, +); U1-b: CR-9, CR-4 (+ only) | A-10 |
| C-18 | `employers.covered.not_transit_linked` | `entry_rate` (worksites in the city) | decrease | medium to long | RS-4, TX-3 | A-9 |
| C-19 | `neighboring_jurisdictions` | `entry_rate` (worksites just outside the boundary) | increase | medium to long | RS-4 | A-9 |
| C-20 | `employers.covered.transit_linked` | `entry_rate` (worksites in the city) | ambiguous | medium to long | RS-4 (−) vs CR-9, CR-4 (staff and customers reach the city free, +); CR-12b | A-9, A-11, A-16 |
| C-21 | `workers.covered` (at employers not linked to transit) | `employment`, `hours_worked` | at_least_one_decrease | short to medium | TX-3 | A-12, A-13 |
| C-22 | `employers.covered` and business associations; riders' groups | `lobbying_effort` | increase | medium | RS-7 | A-15 |
| C-23 | `workers.covered` | `earnings` (bonuses paid April to June 2027) | increase | short (April to June 2027) | RS-8 | A-23 |
| C-24 | `workers.covered` | `earnings` (bonuses paid July to December 2027) | decrease | short (July to December 2027) | RS-8 | A-23 |

C-16. Because all city payroll is taxed once an employer is over the threshold, an employer just over it saves the whole tax by getting below it (RS-5, A-8). Under U1-b the threshold counts only city payroll, so moving staff to sites outside the city is a further way to stay below it. The sign is the same under both readings, so one sign is given; the forms differ.

C-17 and C-62 are the reading-dependent cases. Under U1-b, a large outside firm whose city office has a payroll below $750,000 pays nothing (C-62: `no_change`), and its staff and customers now reach that office free. Only the + chain applies to its entry (A-10). Under U1-a, the same office is taxed on its city payroll because the firm as a whole is over the threshold, so the firm's means fall while wages are fixed (A-12), and the tax chain opposes the access chain.

C-18 to C-20 are relocation (RS-4, CR-4 with x: a site in the city, y: a site just outside it). For employers whose staff and customers do not reach them by PHT, only the tax applies, and sites are available just across the line (A-9). For downtown employers, the tax pushes out and free access for staff and customers pulls in, so the sign is ambiguous. C-21 is TX-3's group form, limited to employers not linked to transit. The commuting chain of C-36 (free rides make PHT-reachable city jobs better, so workers offer more labor to them, CR-7a, A-11) does not lower what these employers pay: their staff do not commute by PHT, and workers drawn to PHT-reachable jobs leave them, which pushes their labor cost up, not down. Both chains therefore push employment and hours the same way, in the short and the medium run (section 7).

C-23 and C-24 are a timing shift. Bonuses are paid with and without the tax, but the tax applies to wages paid from 1 July, so some employers bring forward bonuses due in the summer (A-23). The shift is signed per window (`02_ontology.md`, 2.5).

Not reported: households moving into the city to ride free. Non-residents ride free too, so residence gains nothing. Not reported: riders using vehicles as shelter in numbers that add to off-peak crowding (A-7, p = 0.4). Not reported: car ownership. Both chains (free off-peak travel against a less reliable peak) need a premise that some marginal travelers own or would buy a car for these trips, which A-1, a premise about all other modes together, does not give; the record supplies no evidence for one.

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-25 | `sellers.substitutes` (ride-hail) | `price_substitute` (off-peak ride-hail fares) | decrease | short | RS-16 (mirror case): CR-9, CR-6 | PHT rides and ride-hail: `substitute`, partial | A-1, A-6 |
| C-54 | `drivers.ride_hail` | `earnings` | decrease | short to medium | CR-9, LW-10, CR-7a; CR-12e (drivers' exit cannot restore the old earnings) | as C-25 | A-6 |
| C-55 | `drivers.taxi` | `quantity_traded` (taxi trips) | decrease | short to medium | CR-9, CR-4b (the meter rate is fixed, so the fall is not absorbed by price) | PHT rides and taxi trips: `substitute`, partial | A-27 |
| C-56 | `riders.taxi` | `wait_time` (−), `quality_per_unit` (+) | at_least_one_as_stated | short to medium | CR-6 (the meter rate is now above the clearing level; sellers' pressure goes to the open margins: more idle taxis, better service) | as C-55 | A-27 |
| C-26 | `road_users.peak` | `travel_time` (delay in peak traffic) | ambiguous | short to medium | CR-9 (relation `shared_facility`: the roads; Tier C pending Q20); follows C-13; CR-12b | PHT rides and peak road space: `shared_facility` | A-1, A-4, A-24 |
| C-27 | `sellers.downtown.exempt` | `quantity_traded` | increase | short to medium | CR-9, RS-9 | PHT trips and downtown purchases: `complement`, trip | A-1, A-16 |
| C-28 | `sellers.downtown.covered` | `quantity_traded` | ambiguous | short to medium | CR-9, RS-9 (+) vs RS-14 (−); CR-12b | as C-27; labor `input_to` their sales | A-1, A-12, A-16 |
| C-29 | `sellers.car_oriented_retail` | `quantity_traded` | decrease | short to medium | CR-9, RS-9 | downtown and suburban mall trips: `substitute`, partial | A-16 |
| C-30 | `garage_operators.downtown` | `quantity_traded` (off-peak parking) | decrease | short to medium | CR-9, RS-12 | car trips downtown and parking: `complement`, close | A-1, A-24 |
| C-31 | `park_and_ride_users` | `wait_time`, `search_cost` (finding a space) | at_least_one_increase | short to medium | CR-9, CR-6 (fee and capacity fixed) | PHT rides and park-and-ride spaces: `complement`, close | A-1, A-20 |
| C-53 | `PHT` | `non_tax_receipts` (park-and-ride fees) | increase | short to medium | CR-9, CR-4c (more spaces are taken at $4 until the lots fill) | as C-31 | A-1, A-20 |
| C-32 | `owners.residential_near_lines` | `asset_value` | increase | short (from February 2027) to medium | SB-4 (CR-7b, CR-7c, CR-10c) | housing near lines and PHT rides: `complement`, location | A-21, A-25 |
| C-33 | `tenants.near_lines` | `price_paid` (rent) | increase | medium | CR-7a, CR-7b, CR-6 | as C-32 | A-21, A-25 |
| C-34 | `owners.industrial_sites_city` | `asset_value` | decrease | short to medium | CR-7b, CR-7c, RS-4 | city and boundary sites: `across_border`, close | A-9 |
| C-57 | `owners.business_parks` | `asset_value` | increase | short (from February 2027) to medium | SB-4 (CR-7c, CR-10c), CR-9, RS-4 | as C-34 | A-9 |
| C-35 | `owners.downtown_commercial` | `asset_value` | ambiguous | short to medium | CR-7c (access, +) vs CR-7b (tax, −); CR-12b | as C-32 and C-34 | A-9, A-16 |
| C-36 | `workers.city` | `wage_rate` | ambiguous | medium | see section 7 | city and suburban jobs: `same_market_other_segment`, close | A-11, A-12, A-16, A-26 |
| C-58 | `workers.city` (PHT commuters) | `job_changes` (toward city jobs reached by PHT) | increase | medium | CR-4 (x: a suburban job, y: a city job reached by PHT, made better by the free ride), CR-7a | as C-36; PHT rides and city jobs: `complement`, location | A-11 |
| C-37 | `employers.covered` | `price_paid` (labor cost per hour: wage plus tax) | ambiguous | medium | TX-2 (+) vs the wage chains of C-36 (−); CR-12b | | A-11, A-12, A-26 |
| C-38 | `employers.pass_buyers.exempt` | `resources_available_other_uses` | increase | short | SB-8 | | A-22 |
| C-39 | `employers.pass_buyers.covered` | `resources_available_other_uses` | ambiguous | short | SB-8 (+) vs TX-1 (−); CR-12b | | A-22 |

C-25 is RS-16's mirror case (added in 0.7 from this example). Buyers leave the substitute, and ride-hail fares, which are free to move, fall off-peak where drivers do not leave as fast as riders (A-6). Drivers then carry fewer fares at lower prices, so their earnings fall; moving their time to other uses cannot restore the old earnings (C-54; CR-12e). Taxi fares are fixed by the meter rate. Where some taxi riders are at the margin with PHT (A-27, a premise about taxis in particular, which A-1 does not give), taxi drivers carry fewer fares at the same price (C-55). The meter is then above the rate that would clear the smaller demand, so the pressure comes from sellers and goes to the margins open to them: more idle taxis and shorter waits, or better service to win riders (C-56; CR-6, recorded as a group because the members move in opposite directions). C-26 follows C-13 through the roads. One driver's use of a road changes the delay others face; this is a `shared_facility` relation (CR-9, 0.7), not an exchange, and chains through it are Tier C. It also needs a premise that some of the travelers who switch between PHT and other modes at the peak drive (A-24). Because C-13 is ambiguous, so is peak road delay; ride-hail drivers who keep cruising with fewer fares add a further + chain. Off-peak roads are not congested, so no sign is given there.

C-27 to C-31 are trip links. A free transit trip downtown carries the purchases made on it (RS-9): exempt downtown sellers gain, and the car-oriented malls just outside the city lose some of the shoppers who switch destination (A-16). Covered downtown sellers also face the higher labor cost (RS-14), so their sign is ambiguous. Fewer car trips downtown off-peak mean less off-peak garage use (C-30); this needs a premise that some off-peak travelers at the margin with PHT drove downtown and parked (A-24), which A-1 alone does not give. Park-and-ride lots keep their $4 fee and their size while the rides they feed become free, so drivers search longer or arrive earlier to find a space (C-31). Lot occupancy is already about 85% (A-20), so until the lots fill more spaces are taken at $4, and PHT's fee receipts rise (C-53), the receipt side of the same demand.

C-32 and C-33. Free transit raises what occupiers will pay to live near a line, including on the two Westmere routes, for households that choose where to live partly by the cost of their trips (A-25; A-1 is about mode choice, not home choice). The housing stock there cannot expand quickly (A-21), so the gain settles on it (CR-7b) and is capitalized when the policy becomes expected (SB-4; CR-7c with CR-10c). How much is capitalized depends on whether buyers expect the policy to outlast the two-year review (A-14), but a two-year change is capitalized with the same sign, so A-14 bears on size only. Tenants near lines pay more rent over the medium run (C-33), which takes back part of their fare saving. The two are different variables and are not netted (CR-12c).

C-34, C-35 and C-57. Land in the city cannot move across the boundary; the employers on it can (C-18). So for sites whose users gain nothing from transit, part of the tax settles on the land (CR-7b), and its value falls when the tax becomes expected (CR-7c). The business-park sites just across the line are the other side of the same move: demand for them rises with C-18 and C-19, their location is fixed, and the gain is capitalized from the announcement (C-57; SB-4, CR-7c with CR-10c). For downtown sites, transit access pulls the other way.

C-36 to C-37 and C-58. Chain (1) of the wage row in section 7, part of K3 shifted to workers, needs a premise that workers at covered employers cannot all move to uncovered jobs at the same pay and commuting cost (A-26). Chain (2) is the commuting term: workers who choose between city and suburban jobs by net yield (A-11) move toward city jobs reached by PHT, so job changes rise while the adjustment lasts (C-58).

C-38 and C-39. Employers that bought staff passes would have kept buying them (A-22). Their staff now ride free anyway, so the pass budget is freed (SB-8). For pass buyers above the threshold, this is set against the tax, and without firm-level figures the sign is not settled. Whether any of the freed budget is passed to staff as pay is not signed.

Depth. C-27 to C-31 are at depth 3. C-26 (depth 3, through C-13) reaches a diffuse group of bystanders, so the chain stops there. Not followed: bike-share and car-dealer sales (depth 4, diffuse); the city's parking-meter revenue (TX-10), since meters cover only a small share of downtown parking.

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `travelers.peak`, `quantity_substitute`, short to medium | Crowding and pass-ups push some peak riders to other modes (C-6, C-8). | The zero fare pulls others onto PHT (C-5). | None | **ambiguous** (C-13). Decided by how near crush load the peak lines are and how much riders mind crowding. |
| `travelers.offpeak`, `quantity_substitute`, short to medium | Riders already aboard who leave because new riders take their space (C-6, Tier C). | The zero fare pulls travelers from other modes (C-4). | CR-12e with an empirical premise (A-28): off-peak vehicles run at about 35% occupancy, so the space lost is small next to the $2 fare removed. The response argument alone does not bind riders who did not respond (CR-12e, 0.8). | **decrease** (C-12). |
| `road_users.peak`, `travel_time`, short to medium | Peak riders who leave PHT for cars and taxis; ride-hail drivers cruising with fewer fares. | Peak drivers who switch to PHT. | None | **ambiguous** (C-26, Tier C). |
| `employers.covered.transit_linked`, `entry_rate`, medium to long | Free access for staff and customers (CR-9). | The tax (RS-4). | None | **ambiguous** (C-20). |
| `employers.outside_branch`, `entry_rate`, medium | Free access. | Under U1-a only, the tax. | None | **U1-a: ambiguous; U1-b: increase** (C-17). |
| `workers.covered` (not transit linked), `employment`, `hours_worked`, medium | None. The commuting chain lowers wages only for jobs reached by PHT, which these are not. | (1) The tax (TX-3), passed back to wages only in part (CR-7b, A-13); the wage response cannot push labor cost below its old level (CR-12e). (2) Workers drawn to PHT-reachable jobs leave these employers, which raises what they must pay (CR-7a, A-11). | Not needed: both chains push the same way (CR-12a). | **at_least_one_decrease** (C-21). |
| `workers.city`, `wage_rate`, medium | Downtown sellers' higher sales raise their demand for labor (C-27). | (1) As money wages are renegotiated, part of the tax shifts to workers who cannot all take uncovered jobs at the same pay (CR-7b, DM-1 time note, A-26). (2) Commuting to a city job by PHT is now free, so for workers who choose between city and suburban jobs by net yield, city jobs gain a term worth the fare (CR-5c). More of them seek city jobs, and the city wage tends down relative to suburban wages (CR-7a, A-11). (3) Covered employers not linked to transit hire less (C-21). | None | **ambiguous** (C-36). Chains (1) to (3) all push down. The method gives a sign only where no + chain is active, which is not the case for the city as a whole. |
| `employers.covered`, `price_paid` (labor cost), medium | The tax. | The wage chains in the row above. | None | **ambiguous** (C-37). In the short run, with wages fixed (A-12), **increase** (C-3). |
| `sellers.downtown.covered`, `quantity_traded`, short to medium | Shopping trips by free transit (RS-9). | Higher labor cost passed into prices (RS-14). | None | **ambiguous** (C-28). |
| `PHT` (all staff), `employment`, short | About 60 new customer-service and safety posts (C-41, A-19). | 140 fare posts end (C-40). | CR-12e, arithmetic on the case's figures: 60 is less than 140. | **decrease**. |
| `PHT`, `fund_balance` (PHT and Transit Reserve), medium (to the 2029 review) | Collection costs of $13 million a year no longer spent (C-43); K3 net revenue above $58 million (about $2.1 million projected). | The new posts (about $4 million a year); any shortfall of K3 below projection (C-46). | CR-12e, arithmetic and the Act's accounting: the posts cost less than the savings, and a shortfall can only reduce the K3 term to zero, since any shortfall below $58 million is made up by the general fund. | **increase** (C-44). |
| `PHT`, `fund_balance`, short (FY 2027–28, one-time items) | Fares and K3 both accrue for July and August; collection savings from September. | The $5 million termination payment; severance for fare staff not redeployed (no figure). | None: severance has no figure. CR-12g keeps these one-time items out of the medium-run row. | **ambiguous** (C-61). |
| `input_suppliers.fare_system`, `resources_available_other_uses`, short (FY 2027–28) | The $5 million termination payment (CR-8b). | Contract payments after September lost (CR-5a). | None | **ambiguous** (C-60). |

**Who pays and who receives.** K1 moves the cost of rides from riders to K3's bearers, and PHT is made whole. The transfer is recorded on both sides: riders' saved fares (C-10, C-1) and the bearers' lost means (C-47). If K3 falls below $58 million, the general fund pays the difference; its payers are then a group (taxpayers, recipients of other city spending, future taxpayers through borrowing) with `at_least_one_decrease` (CR-8, 0.8, contingent payers; OC-1, Who pays). That contingency (A-17, p = 0.45) is below the cut-off, so the chain is listed in section 10, not reported. It goes partly to people who pay no part of K3, such as non-residents who ride and riders who work for exempt employers. Some of those who pay K3 also receive part of it back: staff who ride, pass-buying employers (C-38, C-39), and employers whose sites gain access (C-20). This partial return of benefit to payers is what makes the wage and land rows ambiguous rather than signed.

## 8. Time structure

- **Announcement (10 February 2027).** Housing near lines is revalued from then, to the extent the policy is expected to pass and to last (C-32; CR-7c, CR-10a). Business sites whose users gain nothing from transit lose value from then (C-34), and business-park sites just across the line gain (C-57). Employers bring bonuses forward into June (C-23, C-24).
- **Fiscal year 2027–28.** PHT pays the $5 million termination payment and severance, while fares and K3 both accrue for July and August and collection savings start in September. The one-time balance is not signed (C-61), and neither is the contractor's (C-60); they are kept apart from the medium-run rows (CR-12g). Pass holders apply for refunds in the autumn (C-52).
- **No rush to use up passes.** Unused pass value is refunded pro rata, so riders had no reason to stop buying passes before 1 September (CR-10a: the refund removes the timing gain). No timing shift is recorded.
- **First months after 1 September.** Off-peak ridership builds as routines change (TS-8). Peak crowding builds with it.
- **Two-year service freeze.** For two years K2 fixes service hours, so the excess demand on the busiest lines (C-7) cannot be met by added service. Even after the review, new trams and buses take two to three years to order and deliver (CR-10b). What the council decides at the review is a political choice the method does not predict (`06_gaps.md`, Q5). Under CR-10a, though, what employers and home buyers expect about it affects C-20 and C-32 now (A-14).
- **Medium to long run.** Relocation of employers not linked to transit (C-18, C-19) happens as leases end and plants are replaced (CR-10b). The wage chains (C-36) act only as contracts are renegotiated (A-12), and PHT commuters change jobs while the adjustment lasts (C-58). The fare-card contractor's loss of the contract it would have kept is lasting (C-59).
- **Information.** At a zero fare, ridership no longer shows how much riders would give up for a ride on each route. PHT's counts still show how many ride, but not how much they value it (CR-11a). No variable records this; see "What this analysis cannot say".

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-47 | `tax_bearers` | `resources_available_other_uses` | decrease | About $61 million a year in K3, from covered employers at first and, as wages and prices adjust, partly from city workers, owners of city sites and buyers from covered employers. How it splits is not signed (DM-1 has no clear difference in alternatives to work with). | TX-1, OC-1, CR-8b |
| C-48 | `sellers.forgone` | `quantity_traded` | decrease | What the bearers would have bought, invested, saved or paid in wages with that money. Saving is a use (OC-1; CR-4, 0.7): where bearers save less, those who would have borrowed it lose. None of these markets is named, which OC-1 would require a premise for. | OC-1, CR-8a, CR-9 |
| C-40 | `PHT.fare_staff` | `employment` (fare inspection, ticket offices) | decrease | 140 posts end. The staff's labor is released to other uses: 60 are expected to move to new PHT posts (C-41) and the rest to other employers. | CR-1, CR-8a |
| C-41 | `PHT` | `employment` (customer-service and safety posts) | increase | | CR-2 applied to PHT's redeployment plan |
| C-42 | `input_suppliers.fare_system` | `quantity_traded` (fare-system services) | decrease | The card-system contract ends. The $5 million termination payment is a transfer from PHT to the contractor (CR-8b), counted on PHT's side in C-61 and on the contractor's in C-60. | CR-9 |
| C-59 | `input_suppliers.fare_system` | `resources_available_other_uses` | decrease | Medium to long run: the gains from a contract that would otherwise have continued. Moving its resources to other clients cannot restore more than their next-best use yields. | CR-5a, CR-12e |
| C-60 | `input_suppliers.fare_system` | `resources_available_other_uses` | ambiguous | FY 2027–28: the termination payment against the contract payments lost after September. | CR-8b vs CR-5a; CR-12b |
| C-43 | `PHT` | `enforcement_cost` (fare inspection, cash handling, card system) | decrease | Resources that were used up collecting fares (CR-8c) are released. | CR-8c |
| C-44 | `PHT` | `fund_balance` (PHT and Transit Reserve) | increase | Medium run, to the 2029 review; see section 7. If the city instead draws the reserve into its general fund, the freed resources go to whatever that fund pays for (CR-8d). PHT is the residual claimant on K3 above $58 million, so its receipt is signed with the case's figures, not by default (CR-8, 0.7). | CR-8b, CR-8d, CR-12e |
| C-61 | `PHT` | `fund_balance` | ambiguous | FY 2027–28: the termination payment and severance against two months of both fares and K3 and ten months of collection savings. | CR-8b; CR-12b, CR-12g |
| C-45 | `officials.revenue` | `enforcement_cost` | increase | Registration, returns, audits. Funded from 1.5% of K3 revenue, so this reduces what reaches PHT rather than adding to general taxes (OC-3, third funding case). | OC-3 |
| C-46 | `officials.revenue` | `tax_revenue_vs_static_projection` | decrease | Payroll kept under the threshold (C-16) and worksites moved outside (C-18) shrink the base below 0.40% of 2026 city payroll. | TX-9 |

The resources K4 releases are real. The work of collecting $58 million in fares used up about $13 million a year (CR-8c). Collecting the same sum through K3 uses up less: the Revenue Department's 1.5% (C-45) and employers' compliance costs (C-15). Whether total collection costs fall is not signed, because employers' compliance costs have no figure.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | Some travelers are at the margin between PHT and other modes at a $2 fare. | substitutability | 0.95 | Mode shares; past ridership responses to fare changes; share of short trips walked. | C-4, C-5, C-6, C-12 and everything downstream are not reported. |
| A-2 | Off-peak vehicles have room for added riders (average occupancy about 35% of planning capacity). | other | 0.85 | Automatic passenger counts. | C-4 would bring rationing off-peak, not only the Tier C crowding of C-6. |
| A-3 | At the old fare, most peak lines run below crush load, so added riders board standing. | other | 0.8 | Peak counts at 60–75% of planning capacity on most lines. | C-5 and the peak part of C-6 shrink to the busiest lines. |
| A-4 | On tram 1, tram 4 and bus 12, peak demand at a zero fare exceeds crush capacity. | binding | 0.7 | Already at 95% of planning capacity at $2; ridership responses in comparable fare-free cities. | C-7 and C-8 are not reported; C-13 and C-26 lose their + chain from pass-ups (crowding remains, at Tier C). |
| A-5 | Most fare-paying riders keep riding at a zero fare. | other | 0.9 | Few would stop riding because a price fell. The exceptions are peak riders displaced by crowding. | C-10 shrinks. |
| A-6 | Some off-peak ride-hail users switch to PHT, and ride-hail drivers do not withdraw as fast as riders do. | substitutability | 0.6 | Ride-hail trip data by hour; driver hours. | C-25 and C-54 not reported. |
| A-7 | People using vehicles as shelter add materially to off-peak crowding. | other | 0.4 | Experience of other fare-free systems is mixed. | Below the cut-off; not reported. |
| A-8 | For some employers near the threshold, reshaping payroll costs less than the tax on their whole city payroll. | other | 0.75 | Number of employers with payroll between $600,000 and $900,000; use of contractors in those sectors. | C-16 not reported. |
| A-9 | Some covered employers' operations do not depend on transit, and sites are available just outside the boundary. | mobility | 0.65 | Warehouses and plants near the western boundary; vacancy in the Westmere and Calder Vale business parks. | C-18, C-19, C-34, C-57 not reported. |
| A-10 | Small city offices of large outside firms value transit access for staff or customers. | other | 0.6 | Location of such offices near tram stops; commuting surveys. | C-17's + chain not reported; under U1-b the sign would not be given. |
| A-11 | Some workers choose between city and suburban jobs by pay net of commuting cost, and commute by PHT. | mobility | 0.8 | Commuting surveys; PHT pass holders working in the city. | Chain (2) in the C-36 row drops; the row stays ambiguous. C-58 not reported. |
| A-12 | Money wages are fixed in the short run by contracts and custom, so covered employers bear K3 at first. | other | 0.85 | Contract lengths; annual pay reviews. | C-3 becomes ambiguous; C-21 weakens. |
| A-13 | Covered employers not linked to transit adjust staff or hours when labor costs rise, and their workers have enough uncovered alternatives that wages do not absorb the whole tax. | alternative_uses | 0.75 | Share of hourly staff; automation options in warehousing; suburban warehouse jobs. | C-21 not reported. |
| A-14 | Home buyers expect fare-free transit to continue beyond the two-year review. | expectations | 0.6 | Campaign commitments; council majority; polling on the policy. | C-32 and C-33 shrink to the two-year value, with the same sign (CR-7c); A-14 bears on size only and no consequence rests on it. |
| A-15 | Business associations and riders' groups can organize at a cost below their stakes. | other | 0.7 | The chamber of commerce opposed the bill in hearings; an existing riders' union. | C-22 not reported. |
| A-16 | Some shoppers choose between downtown and the suburban malls partly by trip cost. | substitutability | 0.7 | Shopper origin surveys; share of downtown shoppers arriving by PHT. | C-27, C-29 not reported; C-28, C-35 lose their + chain. |
| A-17 | K3 net revenue falls below $58 million in some year before the review, so the general fund makes up the difference. (Revised: under 0.6 this premise bounded the shortfall for C-44, which the Act's shortfall clause makes unnecessary.) | other | 0.45 | Net projection about $60.1 million, so a shortfall of more than 3.5% is needed; the size of the threshold band; relocation is slow (C-18 is medium to long). | Below the cut-off. If it holds, the general fund's payers (taxpayers, recipients of other city spending, future taxpayers through borrowing) bear the difference: `resources_available_other_uses` at_least_one_decrease, medium (CR-8, 0.8; OC-1, Who pays). Listed as a conditional possibility. |
| A-18 | PHT holds the surplus in the Transit Reserve, as the Act says. | revenue_use | 0.6 | Act text; the city's record of drawing on authority reserves. | C-44's gain goes to the general fund instead (CR-8d). |
| A-19 | PHT creates about 60 customer-service and safety posts, filled mainly by former fare staff. | other | 0.75 | PHT's published plan; union transfer agreement. | C-41 not reported; PHT total employment still falls; C-44 still increases (the posts only add to the savings). |
| A-20 | Park-and-ride lots are near capacity at the $4 fee (about 85% weekday occupancy). | binding | 0.65 | Lot counts. | C-31 and C-53 not reported. |
| A-21 | Housing near PHT lines cannot expand quickly. | durability | 0.85 | Zoning near lines; construction lead times. | C-32 and C-33 weaken: part of the gain goes to new building rather than to existing holders. |
| A-22 | Pass-buying employers would have kept buying staff passes. | other | 0.85 | Multi-year pass agreements; renewal rates. | C-38, C-39 shrink. |
| A-23 | Some covered employers can move bonuses due in July into June. | other | 0.55 | Bonus calendars; past responses to payroll tax dates. | C-23, C-24 not reported. |
| A-24 | Some of the travelers at the margin between PHT and other modes drive: off-peak, to downtown destinations where they park in garages; at the peak, on the roads PHT runs along. | substitutability | 0.75 | Mode shares by trip purpose; garage occupancy off-peak; car trips along PHT corridors. | C-30 not reported; C-26 loses its chains. |
| A-25 | Some households choose where to live partly by the cost of their commuting and shopping trips, and ride PHT. | substitutability | 0.8 | PHT pass holders' home locations; house-price gradients near tram stops. | C-32, C-33 not reported. |
| A-26 | Workers at covered employers cannot all move to uncovered jobs (public employers, charities, small firms, suburban sites) at the same pay and commuting cost. | mobility | 0.85 | Size of the uncovered sector; commuting distances to the suburbs. | Chain (1) in the C-36 row drops; C-36 and C-37 stay ambiguous through the other chains. |
| A-27 | Some taxi riders are at the margin between taxis and PHT at a $2 fare. | substitutability | 0.6 | Taxi trips along PHT routes, especially off-peak and to and from stations. | C-55, C-56 not reported. |
| A-28 | Off-peak, the space new riders take from riders already aboard is small next to the $2 fare removed, so fewer riders leave PHT for other modes because of it than join PHT because of the fare. | other | 0.8 | Off-peak occupancy about 35% of planning capacity (A-2); riders' complaints in comparable fare-free cities. | C-12 becomes ambiguous (CR-12b). |

**Final check before the report** (workflow).
1. *Uncombined chains.* Peak mode choice, peak road delay, city wages, labor cost, covered downtown sellers, downtown sites, pass holders' short-run compliance cost, PHT's and the contractor's one-time balances, and branch offices under U1-a each have opposing chains. All are `ambiguous` in section 7. Off-peak substitutes (C-12) do have an opposing chain, through the Tier C crowding of riders already aboard (C-6); CR-12e does not bind those riders, so C-12 is signed on a stated dominance premise (A-28). For staff and hours at employers not linked to transit (C-21), the commuting chain pushes the same way, not against.
2. *Group signs.* C-8, C-21, C-31 and C-56 are groups. The busiest lines' margins (C-8) and taxi riders' margins (C-56) move in opposite directions and are recorded with `at_least_one_as_stated`, as PC-19 and CR-6 ask.
3. *Baseline.* Every sign is against the same timetable with $2 fares and no tax. Rents (C-33) are compared with rents without the policy, not with past rents. Service hours are the same with and without K2, so nothing is signed for them.
4. *Worse off is not poorer.* `resources_available_other_uses` is signed only for riders who keep riding (C-10), pass buyers (C-38, C-39), tax bearers (C-47), outside firms under U1-a (C-62) and the fare-card contractor (C-59, C-60), who keep paying, pay a sum they cannot avoid, or lose receipts. Peak riders who switch to cars are worse off by their own ranking (CR-3a), but nothing is signed for their means.
5. *Timing.* Bonuses are signed per window (C-23, C-24). Capitalization at announcement is not a shift. One-time payments in FY 2027–28 are kept out of the medium-run rows (C-60, C-61; CR-12g).
6. *Both sides.* Fares: C-1 and C-49. Tax: C-47 and C-2. Fares replaced: C-10 and C-47. Termination payment: PHT (C-61) and the contractor (C-60). Pass budgets: C-38, C-39, with the pass revenue PHT no longer receives inside C-49. Park-and-ride: users' search (C-31) and PHT's fees (C-53). A contingent general-fund payment is recorded as a conditional possibility (A-17).
7. *Every class, every core rule.* CR-7c was applied to residential, industrial, downtown and business-park sites (C-32, C-34, C-35, C-57). Capitalization of the right to ride is not applicable, since the right is not tied to any asset. CR-6 was applied to the park-and-ride lots and to taxis under the fixed meter. Roads and vehicles below crush load are `shared_facility` relations at Tier C (C-6, C-26).
8. *Premises.* Organizing (A-15), margins (A-1, A-13, A-24, A-25, A-27), workers' alternatives (A-26) and dominance (A-28) are all in the table.

## 11. Report

**The policy.** From 1 September 2027, Port Hallam's buses and trams charge no fares. Service is held at the current timetable for two years. The lost fare revenue is replaced by a 0.40% tax on the city payroll of private employers whose payroll exceeds $750,000.

**Visible consequences.** Rides cost nothing (C-1). PHT receives no fares (C-49) and the tax revenue instead (C-2). Covered employers' labor costs rise at first (C-3). Off-peak ridership grows (C-4). The 140 fare-collection posts end (C-40), and about 60 new posts are created (C-41). Employers stop buying staff passes (C-51).

**Invisible consequences.**
- *Riders who would have paid anyway* keep the fares they no longer pay (C-10) and no longer buy tickets, top up cards or buy passes (C-11). The method does not say what they spend or save the money on. Former evaders no longer break the rules when they ride (C-50).
- *Riders on vehicles with room*, off-peak and on most lines at the peak, including seniors and pupils who gained nothing on price, have less space as new riders board (C-6, Tier C).
- *On the three busiest lines at the peak*, riders wish to take more rides than the vehicles carry (C-7). At least one of the following happens, and the method does not say which: vehicles pass riders at inner stops, crowding rises to crush load, or places go by where and when a rider boards (C-8).
- *Other modes* lose off-peak trips (C-12), and off-peak ride-hail fares and drivers' earnings fall (C-25, C-54). Taxis carry fewer fares (C-55), and taxi riders wait less or get better service (C-56). Downtown garages lose off-peak parkers (C-30). Park-and-ride users search longer or arrive earlier for a space (C-31), and PHT collects more parking fees (C-53).
- *Downtown sellers below the threshold* gain shoppers (C-27); the suburban malls lose some (C-29).
- *Owners of housing near lines* gain from the announcement (C-32). Their tenants pay more rent over time (C-33).
- *Workers* who commute by PHT move toward city jobs (C-58).
- *Employers* file new returns (C-15). Some keep payroll under the threshold (C-16), and some bring bonuses forward (C-23, C-24). Over time, those whose staff and customers do not use transit set up fewer worksites in the city and more just outside it (C-18, C-19). Their staff see fewer hires or fewer hours (C-21). Industrial site values in the city fall (C-34), and business-park values just across the line rise (C-57). Revenue falls short of the static projection (C-46).
- *Those who bear the tax* have about $61 million a year less (C-47), and the sellers they would have bought from lose those sales (C-48). The Revenue Department's cost (C-45) is taken from the tax before it reaches PHT. The fare-card contractor loses its contract (C-42) and, after the first year, the means it would have earned from it (C-59). PHT stops spending on fare collection (C-43) and builds a reserve up to the review (C-44).
- *Pass-buying employers* below the threshold save their pass budgets (C-38). Lobbying increases on both sides (C-22).

**Ambiguous effects.**
- Whether peak travelers, and peak road traffic, shift toward or away from PHT (C-13, C-26). The fare pulls one way; crowding pushes the other. The road result is Tier C.
- City wages, and covered employers' labor cost after the first year (C-36, C-37). The tax and the value of a free commute push wages down, while higher downtown sales push them up.
- Downtown employers' location (C-20), downtown site values (C-35), and covered downtown sellers' sales (C-28).
- Small city offices of outside firms: increase if the threshold counts only city payroll (U1-b); ambiguous if it counts total payroll (U1-a) (C-17).
- Pass-buying employers above the threshold (C-39). Pass holders' time in the autumn of 2027, when they apply for refunds but stop buying passes (C-52).
- PHT's and the fare-card contractor's balances in the first fiscal year, when the termination payment and severance fall due (C-60, C-61).

**Key conditions.** Whether the busiest lines exceed crush load at a zero fare (A-4, p = 0.7) decides whether free transit brings pass-ups and allocation by boarding order, or only crowding. Whether home buyers expect the policy to outlast the review (A-14, p = 0.6) decides how much of the gain is capitalized into homes near lines. Whether employers' operations depend on transit and can move just across the line (A-9, p = 0.65) decides where the tax's burden settles. Whether the tax falls below $58 million (A-17, p = 0.45), so that the city's general fund pays the difference, is below the cut-off and not reported.

**What this analysis cannot say.** It cannot say how many riders are added, or how large any effect is. It cannot say whether peak riders who would have paid are better or worse off on balance, or whether total collection costs fall. It cannot say what the council will do at the two-year review, or whether the transfer from tax bearers to riders is fair or the policy worthwhile. It records the loss of fare-based information about what riders value (section 8) but has no variable to sign it. Environmental and health effects, and safety on crowded vehicles, are out of scope for version 1. Congestion is recorded only as peak `travel_time` (C-26), and its sign is not determined. Crowding on vehicles below crush load (C-6) and road delay (C-26) pass through shared facilities, not exchanges; they are reported at Tier C pending `06_gaps.md`, Q20. Car ownership is not signed, for lack of a premise about drivers' car purchases.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions | Components |
|---|---|---|---|---|---|---|---|---|---|
| C-1 | riders.would_ride_anyway, riders.new | price_paid (fare per ride) | decrease | short–medium | visible | A | CR-1 | none | K1 |
| C-2 | officials.revenue | tax_revenue (payroll tax) | increase | short | visible | A | TX-1 | none | K3 |
| C-3 | employers.covered | price_paid (labor cost) | increase | short | visible | B | TX-2, DM-1 | A-12 | K3 |
| C-4 | riders.offpeak | quantity_traded (off-peak rides) | increase | short–medium | visible | B | CR-4, TS-8 | A-1, A-2 | K1 |
| C-5 | riders.peak | quantity_traded (peak rides) | increase | short | invisible | B | CR-4, CR-6 | A-1, A-3 | K1, K2 |
| C-6 | riders.offpeak, riders.peak (lines below crush) | quality_per_unit (crowding) | decrease | short–medium | invisible | C | CR-9 (shared_facility) | A-1, A-2, A-3 | K1, K2 |
| C-7 | riders.peak.busiest_lines | excess_demand | increase | short–medium | invisible | B | PC-19 (CR-6) | A-4 | K1, K2 |
| C-8 | riders.peak.busiest_lines | wait_time (+), quality_per_unit (−), allocation_by_non_price_criteria (+) | at_least_one_as_stated | short–medium | invisible | B | PC-19 (CR-6), LW-6 | A-4 | K1, K2 |
| C-10 | riders.would_ride_anyway | resources_available_other_uses | increase | short–medium | invisible | B | SB-8; CR-4 (means alone) | A-5 | K1 |
| C-11 | riders.would_ride_anyway (single-fare and card riders; pass holders after refunds) | compliance_cost (tickets, top-ups, passes) | decrease | short–medium | invisible | A | CR-1, CR-8c | none | K1 |
| C-12 | travelers.offpeak | quantity_substitute (other modes, together) | decrease | short–medium | invisible | B | CR-4, RS-16 (mirror); CR-12e | A-1, A-28 | K1 |
| C-13 | travelers.peak | quantity_substitute (other modes, together) | ambiguous | short–medium | invisible | B | CR-4 vs CR-4; CR-12b | A-1, A-3, A-4 | K1, K2 |
| C-15 | employers.covered | compliance_cost | increase | short | invisible | A | TX-5 | none | K3 |
| C-16 | employers.near_threshold | reclassification (payroll kept below threshold) | increase | short–medium | invisible | B | RS-5 | A-8 | K3 |
| C-17 | employers.outside_branch | entry_rate (small city offices) | U1-a: ambiguous; U1-b: increase | medium | invisible | B | U1-a: RS-4 vs CR-9, CR-4; U1-b: CR-9, CR-4 | A-10 | K1, K3 |
| C-18 | employers.covered.not_transit_linked | entry_rate (city worksites) | decrease | medium–long | invisible | B | RS-4, TX-3 | A-9 | K3 |
| C-19 | neighboring_jurisdictions | entry_rate (boundary worksites) | increase | medium–long | invisible | B | RS-4 | A-9 | K3 |
| C-20 | employers.covered.transit_linked | entry_rate (city worksites) | ambiguous | medium–long | invisible | B | RS-4 vs CR-9, CR-4; CR-12b | A-9, A-11, A-16 | K1, K3 |
| C-21 | workers.covered (not transit linked) | employment, hours_worked | at_least_one_decrease | short–medium | invisible | B | TX-3 | A-12, A-13 | K3 |
| C-22 | employers.covered, business associations, riders' groups | lobbying_effort | increase | medium | invisible | B | RS-7 | A-15 | K1, K2, K3 |
| C-23 | workers.covered | earnings (bonuses, April–June 2027) | increase | short | invisible | B | RS-8 | A-23 | K3 |
| C-24 | workers.covered | earnings (bonuses, July–December 2027) | decrease | short | invisible | B | RS-8 | A-23 | K3 |
| C-25 | sellers.substitutes (ride-hail) | price_substitute (off-peak) | decrease | short | invisible | B | RS-16 (mirror): CR-9, CR-6 | A-1, A-6 | K1 |
| C-26 | road_users.peak | travel_time (traffic delay) | ambiguous | short–medium | invisible | C | CR-9 (shared_facility); CR-12b | A-1, A-4, A-24 | K1, K2 |
| C-27 | sellers.downtown.exempt | quantity_traded | increase | short–medium | invisible | B | CR-9, RS-9 | A-1, A-16 | K1 |
| C-28 | sellers.downtown.covered | quantity_traded | ambiguous | short–medium | invisible | B | CR-9, RS-9 vs RS-14; CR-12b | A-1, A-12, A-16 | K1, K3 |
| C-29 | sellers.car_oriented_retail | quantity_traded | decrease | short–medium | invisible | B | CR-9, RS-9 | A-16 | K1 |
| C-30 | garage_operators.downtown | quantity_traded (off-peak parking) | decrease | short–medium | invisible | B | CR-9, RS-12 | A-1, A-24 | K1 |
| C-31 | park_and_ride_users | wait_time, search_cost | at_least_one_increase | short–medium | invisible | B | CR-9, CR-6 | A-1, A-20 | K1 |
| C-32 | owners.residential_near_lines | asset_value | increase | short–medium | invisible | B | SB-4 (CR-7b, CR-7c, CR-10c) | A-21, A-25 | K1 |
| C-33 | tenants.near_lines | price_paid (rent) | increase | medium | invisible | B | CR-7a, CR-7b, CR-6 | A-21, A-25 | K1 |
| C-34 | owners.industrial_sites_city | asset_value | decrease | short–medium | invisible | B | CR-7b, CR-7c, RS-4 | A-9 | K3 |
| C-35 | owners.downtown_commercial | asset_value | ambiguous | short–medium | invisible | B | CR-7c vs CR-7b; CR-12b | A-9, A-16 | K1, K3 |
| C-36 | workers.city | wage_rate | ambiguous | medium | invisible | B | CR-7b, DM-1, CR-5c, CR-7a vs CR-9; CR-12b | A-11, A-12, A-16, A-26 | K1, K3 |
| C-37 | employers.covered | price_paid (labor cost) | ambiguous | medium | invisible | B | TX-2 vs C-36 chains; CR-12b | A-11, A-12, A-26 | K1, K3 |
| C-38 | employers.pass_buyers.exempt | resources_available_other_uses | increase | short | invisible | B | SB-8 | A-22 | K1 |
| C-39 | employers.pass_buyers.covered | resources_available_other_uses | ambiguous | short | invisible | B | SB-8 vs TX-1; CR-12b | A-22 | K1, K3 |
| C-40 | PHT.fare_staff | employment (fare roles) | decrease | short | visible | A | CR-1, CR-8a | none | K4 |
| C-41 | PHT | employment (customer-service posts) | increase | short | visible | B | CR-2 | A-19 | K4 |
| C-42 | input_suppliers.fare_system | quantity_traded (fare-system services) | decrease | short | invisible | A | CR-9, CR-5a | none | K4 |
| C-43 | PHT | enforcement_cost (fare collection) | decrease | short | invisible | A | CR-8c | none | K4 |
| C-44 | PHT (residual claimant, Transit Reserve) | fund_balance | increase | medium | invisible | B | CR-8b, CR-8d; CR-12e (arithmetic) | A-18, A-19 | K1, K3, K4 |
| C-45 | officials.revenue | enforcement_cost | increase | short | invisible | A | OC-3 | none | K3 |
| C-46 | officials.revenue | tax_revenue_vs_static_projection | decrease | short–medium | invisible | B | TX-9 | A-8, A-9 | K3 |
| C-47 | tax_bearers | resources_available_other_uses | decrease | short–medium | invisible | A | TX-1, OC-1, CR-8b | none | K3 |
| C-48 | sellers.forgone | quantity_traded | decrease | short–medium | invisible | A | OC-1, CR-8a, CR-9 | none | K3 |
| C-49 | PHT | net_price_received (fare per ride) | decrease | short–medium | invisible | A | CR-8b | none | K1 |
| C-50 | riders.evading | legal_breach (fare evasion) | decrease | short–medium | invisible | A | CR-1 | none | K1 |
| C-51 | employers.pass_buyers.exempt, employers.pass_buyers.covered | quantity_traded (employer annual passes) | decrease | short | visible | A | CR-1, CR-5a | none | K1 |
| C-52 | riders.would_ride_anyway (pass holders) | compliance_cost (refund applications vs pass purchases) | ambiguous | short | invisible | A | CR-1, CR-8c; CR-12b | none | K1 |
| C-53 | PHT | non_tax_receipts (park-and-ride fees) | increase | short–medium | invisible | B | CR-9, CR-4c | A-1, A-20 | K1 |
| C-54 | drivers.ride_hail | earnings | decrease | short–medium | invisible | B | CR-9, LW-10, CR-7a; CR-12e | A-6 | K1 |
| C-55 | drivers.taxi | quantity_traded (taxi trips) | decrease | short–medium | invisible | B | CR-9, CR-4b | A-27 | K1 |
| C-56 | riders.taxi | wait_time (−), quality_per_unit (+) | at_least_one_as_stated | short–medium | invisible | B | CR-6 | A-27 | K1 |
| C-57 | owners.business_parks | asset_value | increase | short–medium | invisible | B | SB-4 (CR-7c, CR-10c), CR-9, RS-4 | A-9 | K3 |
| C-58 | workers.city (PHT commuters) | job_changes | increase | medium | invisible | B | CR-4, CR-7a | A-11 | K1 |
| C-59 | input_suppliers.fare_system | resources_available_other_uses | decrease | medium–long | invisible | A | CR-5a, CR-12e | none | K4 |
| C-60 | input_suppliers.fare_system | resources_available_other_uses | ambiguous | short | invisible | A | CR-8b vs CR-5a; CR-12b | none | K4 |
| C-61 | PHT | fund_balance | ambiguous | short | invisible | B | CR-8b; CR-12b, CR-12g | A-19 | K1, K3, K4 |
| C-62 | employers.outside_branch | resources_available_other_uses | U1-a: decrease; U1-b: no_change | short | invisible | B | CR-1, CR-8b, CR-3c | A-12 | K3 |
| — | PHT (all staff) | employment | decrease | short | invisible | B | C-40 vs C-41; CR-12e (arithmetic) | A-19 | K4 |

## Corrections after the core-only comparison

Changed (checked against the core rules and catalog 0.8):
- C-6: crowding on vehicles below crush load is no longer CR-6 (no excess demand there) but a `shared_facility` chain (CR-9, 0.7) at Tier C, and now covers off-peak riders too; the 0.6 final check wrongly said off-peak crowding existed only under A-7.
- C-8, C-9: the busiest lines' margins are one group with `at_least_one_as_stated` (PC-19; CR-6 needs a premise per margin, and A-4 alone does not give pass-ups); C-9 is merged into C-8 and removed.
- C-11: limited to single-fare and card riders (and pass holders once refunds are settled); fines removed, since they are a transfer that belongs to evaders. New C-52: pass holders' short-run compliance cost is ambiguous (refund applications against no passes to buy).
- C-12: now combined with the Tier C off-peak crowding chain; CR-12e (0.8) does not bind riders already aboard, so the decrease rests on a new dominance premise A-28.
- C-14 (car ownership) removed: both chains need a premise about car owners that A-1 does not give and the record does not support.
- C-16: one sign, since the readings agree.
- C-26: `travel_time` in place of `wait_time`, `shared_facility` relation, Tier C, and a new premise A-24 that some marginal travelers drive.
- C-30: rests on A-24 as well as A-1 (A-1 covers only the other modes together).
- C-32, C-33: rest on new A-25 (households choose where to live partly by trip cost) and A-21 instead of A-1 and A-14; A-14 bears on size only.
- C-36, C-37: chain (1) now names its premise A-26 (workers cannot all move to uncovered jobs).
- C-44: now `fund_balance` for PHT as residual claimant, medium run only; the one-time termination payment and severance moved to new C-61 (FY 2027–28, ambiguous) under CR-12g. Because the Act makes up any shortfall below $58 million from the general fund, the medium-run sign follows from arithmetic and the Act, and A-17 is no longer needed for it. A-17 is revised to the contingency that the general fund pays (p = 0.45), whose payers are a group under CR-8 (0.8); below the cut-off, listed, not reported.
- C-48: the forgone uses include saving (OC-1; CR-4, 0.7).
- C-21: class definition tightened to employers whose staff and customers do not reach them by PHT (A-13 widened to say wages do not absorb the whole tax), with a section 7 row showing that the commuting chain pushes the same way.
- New consequences for valid claims the pattern version omitted: C-50 (evasion ends, `legal_breach`), C-51 (employer passes no longer bought), C-53 (park-and-ride fee receipts), C-54 (ride-hail drivers' earnings), C-55 and C-56 (taxi trips and taxi riders' margins under the fixed meter, on new premise A-27), C-57 (business-park asset values), C-58 (PHT commuters' job changes), C-59 (the fare-card contractor's lasting loss of means). Two J rows are adopted because 0.7 and 0.8 now settle how to record them: C-60 (the contractor's first-year means, the other side of the termination payment once one-time items are split off under CR-12g) and C-62 (outside firms' means per reading, with the 0.7 sign `no_change` under U1-b).
- Vocabulary and citations: K1 and K2 recorded as `public_supply`; PC-19, RS-16 (mirror case) and SB-8's fixed-capacity clause cited.

Rejected or not applied:
- C-21 (comparison: medium run ambiguous): rejected, because for employers whose staff do not commute by PHT the commuting chain does not lower their wage; it draws workers to PHT-reachable jobs and so raises what these employers pay, pushing employment the same way as the tax.
- J rows not settled by 0.8 left as they were: `full_cost_per_unit` for riders on the busiest lines (its definition still omits crowding), regional rail (A-N4), suburban wages, service hours `no_change`, `quantity_demanded` and owners' `subsidy_share_received`. The core version's C-52 (contract labor) is not adopted: A-8 licenses reshaping payroll only as a group.

## Gaps found

**(a) Calculus gaps.** None. Every step was derived from a pattern or from CR-1 to CR-12. (The core-only re-run's contingent-payer question, its GAP-032-C2, is closed in 0.8 by CR-8's clause on contingent payers, applied here through A-17.) The two steps that came closest to having no core rule were the zero price set by a public supplier and congestion on the roads. Both were derived from CR-6, by treating the zero fare as a price held by a rule and road space as a good used at a zero price. The wording strain this caused is recorded under (b).

**(b) Unclear core rules.**
- **CR-6, when the supplier is the rule-maker.** (closed in 0.7: CR-6's public-supply clause and PC-19.) CR-6's mechanism is that "some party on the other side can gain by accepting [better terms]". Here no one on the other side can accept: PHT may not charge, and K2 fixes its quantity. The statement still applies through its second paragraph (the gap is pursued along open margins), but the listed margins are written from the seller's side: quality, service and conditions that the scarce side adjusts. In this case quality falls because more buyers share a fixed facility (crowding), not because the seller cuts it. The margin "exchanges outside the rule" has no seller to deal with, so its counterpart is buyers leaving for substitutes. Proposed wording: "the margins include terms worsened by buyers' own competition for a fixed quantity (crowding, queuing), and, where no seller can accept better terms, buyers' moves to substitutes".
- **CR-6's group default and opposite polarities.** (closed in 0.7: CR-6's clause on margins in opposite directions and the sign `at_least_one_as_stated`; C-8 now uses it.) CR-6 says that without per-margin premises the margins are recorded as a group with `at_least_one_increase`. The main margin here, crowding, is a fall in `quality_per_unit`, while waiting and allocation by non-price criteria are increases. One group sign cannot hold them, so the group default was unusable. Each margin was signed separately with its own premise (C-6 with A-3, C-8 with A-4).
- **CR-9, "exchange relations only".** (closed in 0.7: CR-9's clause on shared facilities and the relation type `shared_facility`, chains at Tier C pending Q20; C-6 and C-26 now use it.) Riders who switch between car and tram change other drivers' delays through a shared, unpriced road, not through any exchange. C-26 was derived by treating peak road space as a good supplied at a zero price, with transit as its `substitute`. Whether CR-9 permits this, and which relation type in 2.8 a shared facility belongs to, is unclear. The same issue arises within PHT: added riders lower the quality for every other rider (C-6) through shared use, not through a trade with them.
- **CR-7b, for a tax whose revenue buys something its payers value.** (closed in 0.7: CR-7's clause on a tax whose revenue buys something the payers value.) CR-7b assigns the lasting burden to the side with fewer alternatives. It does not say how to treat a tax whose proceeds raise the yield of the taxed activity for some payers (city sites near transit, employers whose staff ride). The analysis handled this as opposing chains under CR-12b (C-20, C-35, C-36), which left the wage and land rows ambiguous. A clause would help: "where the revenue of a tax raises the yield of the taxed use for some payers, the burden on them is the tax less that yield, and is signed only with a premise comparing the two".

**(c) Missing patterns.**
- **Proposed pattern: public supply at a set price with a fixed quantity** (numbered PC-17 under 0.6). (closed in 0.7: PC-19; PC-17 is now the mandated contract term.) *If:* a public supplier sets the price of a good (including zero) and its quantity is fixed by a budget or capacity rule. *Then:* in segments where demand at that price is below capacity, `quantity_traded` increases with no rationing. In segments where it exceeds capacity, `excess_demand` increases, and the gap is pursued through crowding (`quality_per_unit` decrease), waiting and allocation by order of arrival, each signed with its own premise. Buyers who value the good least relative to substitutes leave for them. PC-4, PC-5, PC-6 and PC-16 do not apply, because the seller gains nothing from adjusting and the transfer comes from the funders, not the seller. *Derivation:* CR-6 (price held by a rule, quantity fixed by a rule), CR-2 for the supplier (it follows its budget rule), CR-4 for buyers, CR-8b for the funders.
- **Widen RS-16 to the mirror case.** (closed in 0.7: RS-16's mirror case.) RS-16 covers a policy that pushes buyers to a substitute. A subsidy or zero price on a good pulls buyers away from its substitutes, whose price then falls where their supply cannot contract at once (C-25). The core rules are symmetric (test 3), so the pattern should be too. *Derivation:* CR-9, then CR-6 in the substitute's market with excess supply.
- **Proposed pattern: a better non-wage term lowers the wage required** (numbered RS-17 under 0.6; RS-17 is now size thresholds). Still open: listed as a candidate in `06_gaps.md`, 6.2e (compensating differential from a non-wage term). *If:* a policy improves a term attached to a job or location (a free commute, a local amenity) for workers who can choose between locations. *Then:* labor offered there increases, and `wage_rate` there tends to decrease relative to the counterfactual. *Derivation:* CR-5c (the terms include everything received) with CR-7a (net yields equalized across locations). Used in C-36. It is likely to recur in any policy that changes commuting costs or local amenities.
- **SB-8 clause for fixed capacity.** (closed in 0.7: SB-8's fixed-capacity clause.) SB-8 assumes that recipients who would have bought anyway still get the good. With fixed capacity, some of them are crowded out at the peak and get a worse good (C-6) or none (C-8). Proposed clause: "where the provided quantity is fixed, the cash-equivalent gain holds only for recipients who still obtain the good, and is reduced by any fall in its quality".

**(d) Vocabulary.**
- **Instrument types (2.3).** (closed in 0.7: `public_supply`; K1 and K2 now use it.) There is no type for public supply at a set price (a user fee lowered or abolished) or for a budget rule fixing a quantity. K1 and K2 had to be described in words.
- **Group signs with opposite polarities (2.5).** (closed in 0.7: `at_least_one_as_stated`.) There is no way to record "at least one of: quality falls, waiting rises, allocation by non-price criteria rises". A sign convention such as "at_least_one_worse" for the side that bears the pressure, or a rule that groups take the direction of the full cost, would let CR-6's group default work for quality margins.
- **`full_cost_per_unit`.** Still open: the 0.8 definition still omits loss of quality. Its definition covers money price, waiting, search and side payments, but not a fall in quality such as crowding. So the natural variable for "are peak riders better off on balance?" could not be used. Proposed: include the value buyers place on lower quality.
- **Travel time.** (closed in 0.7: `travel_time`; C-26 now uses it.) There was no variable for travel time (in-vehicle time, road delay). `wait_time` was stretched to cover traffic delay (C-26). Proposed: `travel_time`.
- **Relation type for shared facilities (2.8).** (closed in 0.7: `shared_facility`.) There is none for users of a shared facility who affect each other through crowding (riders on a vehicle, drivers on a road). Proposed: `shared_facility`.
