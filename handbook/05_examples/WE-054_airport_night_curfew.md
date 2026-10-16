# WE-054 Airport night curfew with a daytime slot cap and slots allocated by history

Analyst: draft (Handbook 0.9, held-out test)  |  Rule catalog version: 0.9  |  Status: awaiting expert review

A stylized policy at a fictional airport. It resembles real night curfews and slot regimes at congested airports but is not modeled on any one of them. It was written as a held-out test of catalog 0.9, whose changes were drawn from WE-036 to WE-045. It probes: CR-12's 0.9 rule for a Tier C chain against a Tier B chain, where night noise reaches neighbors through a `proximity` relation while travelers' outcomes run through exchange (Tier B); EN-12 (allocation of a right by history) in its branch where the base seasons run after the announcement, so that airlines race to build history; EN-13 (consolidation of tradable slots); EN-6 with its 0.9 Inputs clause (movements are an input to passenger trips sold locally and to parcel delivery sold nationally); CR-7c for home values near two airports and for the new slots; RS-8 for flights moved from the night into the shoulder hours, per window and per reading; RS-16 for the other airport; and CR-12's 0.9 clause on what the response argument gives. Noise, sleep and health are outside the scope of version 1 and have no variable; they enter only where buyers of homes capitalize them. The probabilities are illustrative; the evidence column says what a real analysis would cite.

## 1. Policy record

**Wexcombe Airport Night Curfew and Slot Order.** Wexcombe International Airport (WXI) is run by the Wexcombe Airport Authority (WAA), a public authority owned by the City of Wexcombe and two counties, which sets the airport's operating rules and charges. In the summer 2025 season WXI handled about 420 movements (a takeoff or a landing) a day: about 380 between 06:00 and 23:00, and about 40 between 23:00 and 06:00. Of the night movements, about 22 are an express parcel carrier's night sort (the "integrator"), about 6 are two other cargo carriers, and about 12 are passenger flights (8 late arrivals scheduled 23:00 to 00:30 and 4 early departures scheduled 05:15 to 05:55). On top of these, about 6 movements a night are daytime flights scheduled before 23:00 that run late and operate between 23:00 and 00:00; about 1 a night operates after midnight. The runway's declared capacity is 34 movements an hour (an existing rule, set by the WAA from air traffic control's assessment); the peaks 07:00 to 09:00 and 17:00 to 20:00 run at 30 to 34, the hour 06:00 to 07:00 at about 10 and the hour 22:00 to 23:00 at about 12. Daytime movements have grown about 3% a year and night cargo about 5%. Fourteen airlines operate in the daytime; the three largest operate about 60% of daytime movements. Aircraft average about 150 seats; airlines can move to larger aircraft only as fleets turn over (two to four years), and three of WXI's gates take wide-bodied aircraft.

WXI employs about 11,000 people on site, including about 900 (mostly part-time night shifts) in the integrator's sort; about 30% of airport workers live within 8 km. About 9,000 homes lie inside the WAA's night-noise contour (the area where night noise exceeds the WAA's threshold), with a median value of about $310,000. The WAA's charges (about $2,000 per movement on average, about $13 per seat) are set each year to recover its costs, which are mostly fixed. Its noise office, which handles residents' complaints, costs about $0.5 million a year; about 60% of its cases concern night movements. The WAA estimates the slot coordination unit and curfew monitoring at about $2.8 million a year.

Pellham Regional Airport, 70 km away by motorway (about 55 minutes), is run by a separate authority, has no curfew, and uses about 45% of its runway capacity. About 1,200 homes lie in the area that would be inside a night-noise contour at Pellham if night cargo moved there; Pellham's commuting area holds about 40,000 homes. Overnight parcel delivery is sold in a national market; Wexcombe's region is about 4% of it.

The WAA board published the draft order, including the base seasons, on 2 March 2026, after a residents' campaign for a curfew that had run since 2023. It adopted the order on 15 September 2026. Slots are issued on 1 September 2027; the curfew and the cap take effect with the winter season on 31 October 2027. No expiry; the WAA will review the cap in 2032.

| Field | Value | Source sentence |
|---|---|---|
| Jurisdiction (and what lies just outside) | WXI only. Pellham Regional (70 km) has no curfew and spare capacity. | "This Order applies to aircraft movements at Wexcombe International Airport." |
| Announced / enacted / effective / expires | Draft with base seasons 2 March 2026; adopted 15 September 2026; slots issued 1 September 2027; curfew and cap from 31 October 2027; review 2032; no expiry. | Order, art. 1 and 12. |
| Enforcement (who, penalties, resources) | WAA, from air traffic control's movement log. $50,000 per movement in the curfew without a dispensation; $10,000 per daytime movement without a slot; slots of a holder fined three times in a season may be withdrawn. Funded from airport charges. | Order, art. 9 to 11. |

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Curfew | `prohibition` | Takeoffs and landings 23:00 to 06:00 | All operators at WXI | None permitted, subject to U1. | Emergencies, medical and state flights. |
| K2 Daytime cap | `quota` | Movements 06:00 to 23:00 | All operators at WXI | 380 a day (the summer 2025 scheduled number); the existing hourly limit of 34 stays. | As K1. |
| K3 Allocation by history | `rights_allocation` | The 380 daily slots | WAA | Issued free to airlines in proportion to the daytime movements each operated in the summer 2026 and winter 2026/27 seasons, each slot in the hour of the movement that earned it. | — |
| K4 Trading | Rule on transfers | Slots | Slot holders | Slots may be sold or leased, and retimed to another daytime hour where the hourly limit leaves room. | — |
| K5 Freed slots | `rights_allocation` | Slots returned to the WAA | WAA | Slots of a holder that ceases to operate at WXI, or that uses a slot on fewer than 80% of a season's days, return to the WAA and are reissued free, first to night operators (those with night movements in winter 2026/27) in proportion to their night movements, then to new entrants. | — |
| K6 Enforcement and funding | Enforcement | K1 to K5 | WAA | Penalties as above; costs recovered through the annual charges. | — |

Existing rules: the hourly limit of 34 movements; the WAA's cost-recovery charge method. Both stay in the counterfactual.

Unclear provision:
- U1, late-running flights. K1 says: "No aircraft shall take off or land between 23:00 and 06:00, save that a flight scheduled to operate before 23:00 and delayed by circumstances beyond the operator's control may be permitted to operate by the duty manager." The WAA's explanatory note says late-running flights "may operate until midnight"; the order itself names no time and no criteria. Reading U1-a: a flight scheduled before 23:00 and delayed may land or take off until 00:00, as of right. Reading U1-b: there is no dispensation for ordinary delays; after 23:00 only emergencies operate, and a late flight diverts (in practice to Pellham) or is cancelled.

Readings get no probability; where a sign depends on one, each reading's sign is reported.

**Figures.** Without the order, daytime movements would be about 409 a day by winter 2027/28 and about 440 by 2030 (3% a year; A-1); the cap holds them at 380. The curfew removes about 40 scheduled night movements a night and, under U1-b, about 6 late-running ones as well. At an illustrative price of $2 million for a slot (one daily movement for every day of the year), the 380 slots are worth about $760 million. A charge of $2,000 per movement spread over about 13% fewer movements than the counterfactual by 2030 rises by about $300 per movement, about $2 per seat. The WAA's slot unit and monitoring ($2.8 million a year) are more than five times its whole noise office ($0.5 million).

The counterfactual is WXI without the order: no curfew, no cap, no slots, daytime and night movements growing as before, and the residents' campaign continuing.

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | Rule families |
|---|---|---|---|
| K1 | Triangular: prohibits exchanges between night operators and their passengers and shippers at WXI at those hours (CR-1, operation 1 where enforced, operation 3, a penalty risk, where not). | Yes: about 40 night movements a night (A-2). | CR-1, RS-4, RS-8 (0.9: more timing chains), RS-3, RS-5, RS-16, EN-6 (0.9 Inputs, for parcel delivery), CR-9 (`proximity`, Tier C), CR-12 (0.9: Tier C against Tier B) |
| K2 | Triangular: fixes the number of daytime movements; the slot price rations them (CR-6, a fixed quantity with a free price). | Yes, from the first season and more each year (A-1; TS-3). | EN-6 (main clause, for passenger trips), CR-6, CR-4c, TS-3, CR-12e and CR-12 (0.9: what the response argument gives), PC-15 |
| K3 | Binary: the WAA creates an asset and gives it to airlines with base-season history (CR-1, operation 4 by way of a new tradable option). | Yes | EN-12 (base seasons after the announcement: a race), SB-4, CR-7c (0.7: claims before creation; competing to qualify), CR-8c, CR-10a |
| K4 | Rule on the market for the created right | Yes | EN-13, CR-5, CR-7a, CR-12 (0.9: activities that exist only under the policy) |
| K5 | Binary: a free claim on a residual flow of slots | Weakly: the flow is small (section 5). | CR-3b, CR-4 |
| K6 | Funded from the policy's own revenue (airport charges) | Yes | OC-3 (own revenue; right baseline), OC-2, CR-8b, CR-8c |

The curfew's purpose, quieter nights near the airport, reaches neighbors through no exchange: a movement changes the situation of those who live under it. That is a `proximity` relation (02_ontology.md, 2.8), so every chain through it is Tier C pending Q20 (CR-9, 0.7). Travelers, shippers, airlines, workers and the airports deal with each other by exchange, so their chains are Tier B.

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `airlines.history` | Airlines with daytime movements in the base seasons | Receive slots in proportion to history; may not add daytime movements without buying or leasing slots; may sell, lease and retime. |
| `operators.night` | The integrator, two other cargo carriers, two passenger airlines with night flights | Lose the night (K1); may buy or lease daytime slots, move to Pellham, or stop; have a priority claim on freed slots (K5). |
| `integrator` | The express parcel carrier with its night sort at WXI | As `operators.night`; owns a sort facility specific to WXI. |
| `airlines.prospective` (`sellers.prospective`) | Airlines that would start or expand at WXI | Must buy or lease slots; rank behind night operators for freed slots. |
| `travelers.wxi` (`buyers.current`) | Passengers using WXI | Face the cap through fares and the routes airlines keep. |
| `travelers.night` | Passengers on late and early flights, and on late-running flights | Flights move to the shoulders, to Pellham, or divert under U1-b. |
| `travelers.pellham` (`buyers.substitutes`) | Passengers using Pellham | More flights and passengers at Pellham. |
| `shippers.wexcombe` | Buyers of overnight parcel service in Wexcombe's region | The sort moves 70 km away. |
| `buyers.parcels.national` | Buyers of overnight parcel service nationally | Wexcombe is 4% of the market. |
| `sellers.substitutes` | Pellham Regional's authority | More movements, including at night. |
| `workers.wxi`, `workers.pellham` | Workers at each airport | Night sort and growth move or stop at WXI; the sort arrives at Pellham. |
| `neighbors.wxi` | Owners of the 9,000 homes in WXI's night-noise contour | Quieter nights, busier shoulders (Tier C); fewer airport workers seeking homes (Tier B). |
| `neighbors.pellham` | Owners of the 1,200 homes in Pellham's prospective night contour | Night cargo arrives (Tier C); hub workers seek homes (Tier B). |
| `concessions.wxi` (`sellers.complements`) | Parking, shops, car hire at WXI | Fewer passengers than without the cap. |
| `officials.enforcement` | WAA | Slot coordination, movement monitoring, penalties; its noise office. |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | `operators.night` | `quantity_supplied` (movements at WXI 23:00 to 06:00) | decrease | short to long (from 31 October 2027) | CR-1 (operation 1), RS-8 | A-2 |
| C-2 | `airlines.history` | `quantity_supplied` (daytime movements at WXI) | decrease | short to long (from 31 October 2027, growing) | CR-1, EN-6, TS-3 | A-1, A-2 |
| C-3 | `airlines.history` | `asset_value` (claim to slots from the draft; the slots from September 2027) | increase | short (part from March 2026, the rest at adoption) | EN-12, CR-7c (0.7: claims before creation), CR-10c, SB-4 | A-1, A-2, A-3 |

C-1 is the curfew's purpose; C-2 is the cap's. The cap is fixed at the summer 2025 number while demand grows, so it binds from the first season and more each year (TS-3, a parameter fixed in physical units). C-1 holds under both readings of U1: under U1-a, late-running flights scheduled before 23:00 still operate until midnight, but the 40 scheduled night movements stop; under U1-b, the late-running ones stop too. The difference is one of size.

C-3 is the created asset. A slot is a claim on part of a capped quantity that airlines would pay to use (A-1), so it has a price (CR-6), and its value goes to whoever receives it at creation (CR-7c). Because the claim is earned by operating in the base seasons, it was valued from the draft of March 2026, rising toward adoption (CR-7c, probability clause). Unlike a history fixed before the announcement, this history could still be built: section 5 (C-5, C-6) records the race, and by CR-7c's 0.7 clarification part of the slots' value is used up in it. C-3 is the value of the slots, not airlines' net position (C-36).

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-4 | `airlines.history`, `operators.night`, `airlines.prospective` | `right_lease_price` (daytime slots) | increase | short to long | EN-6, CR-6 (0.7; 0.8: a free price's rise), CR-12 (0.9: a price that exists only under the policy) | A-1, A-2, A-4 |
| C-5 | `airlines.history` | `quantity_supplied` (daytime movements in the base seasons, March 2026 to March 2027; a flow in the window) | increase | short | EN-12, RS-8, CR-10a, CR-7c (0.7: competing to qualify) | A-5 |
| C-6 | `airlines.history` | `compliance_cost` (crew, fuel and aircraft time on flights added to build history) | increase | short (base seasons) | EN-12, CR-8c | A-5 |
| C-7 | `integrator`, other cargo carriers | `quantity_substitute` (night movements at Pellham) | increase | short to medium | RS-4, RS-1, RS-16 | A-2, A-6 |
| C-8 | `operators.night` | `quantity_supplied` (movements at WXI 06:00 to 07:00) | increase | short to medium | RS-8, CR-4, EN-13 | A-4, A-7 |
| C-9 | `operators.night`, `airlines.history` | `quantity_supplied` (movements at WXI 22:00 to 23:00) | U1-a: increase; U1-b: ambiguous | short to medium | RS-8 (0.9: more timing chains), CR-4, CR-12b | A-4, A-7, A-23, A-24 |
| C-10 | `operators.night` | `quantity_traded` (daytime slots bought or leased by night operators) | increase | short to medium | CR-4, CR-5, EN-13, CR-12 (0.9) | A-4, A-7 |
| C-11 | `airlines.history` | `unit_size` (seats per movement at WXI) | increase | medium | CR-4c (the unit of the constraint is the movement), CR-6, CR-7a | A-1, A-8 |
| C-12 | `airlines.history` | `number_of_sellers` (airlines operating at WXI) | decrease | medium | EN-13, CR-5, CR-7a | A-4, A-10 |
| C-13 | `airlines.prospective` | `entry_rate` (airlines starting at WXI) | decrease | medium | CR-1, CR-4, EN-6 | A-1, A-2 |
| C-14 | `operators.night` | `legal_breach` (movements after the permitted time, penalty paid) | increase | short to medium | RS-3, CR-4 (x: comply, y: violate), CR-12 (0.9: an activity that exists only under the policy) | A-14 |
| C-15 | `airlines.history` | `reclassification` (flights scheduled just before 23:00 that are expected to operate after it) | U1-a: increase; U1-b: no_change | short to medium | RS-5, CR-4 | A-24 |
| C-16 | `operators.night`, `airlines.history`, `airlines.prospective` | `lobbying_effort` (night operators for exemptions and for reading U1-a; slot holders against raising the cap; would-be entrants for a larger new-entrant share) | increase | short to medium | RS-7, EN-5 | A-15 |
| C-17 | `neighbors.wxi` (residents' associations) | `lobbying_effort` | ambiguous | short to medium | RS-7 (Unless), CR-4 | A-15 |
| C-18 | `integrator` | `asset_value` (WXI sort facility and its lease) | decrease | short (from March 2026) | CR-7c, CR-10c, SB-4 | A-6, A-16 |

**What rations the slots (C-4).** The cap fixes the quantity of daytime movements and leaves the price of a slot free (CR-6, a fixed quantity with a free price). Those who value a movement more than the lease price buy or lease; those who value it less lease theirs out. Against the counterfactual, where a daytime movement needed no right at all, the lease price is an `increase` (CR-12, 0.9). By CR-6's 0.8 clarification, the slot price satisfies the "at least one margin" conclusion on its own; no queue or non-price margin is signed.

**The race to build history (C-5, C-6).** The draft of March 2026 named the base seasons, summer 2026 and winter 2026/27, both after the announcement. Each airline's share of 380 slots is its share of base-season movements, so an airline that adds movements in those seasons gains slots at its rivals' expense, and one that does not loses share (EN-12, second branch; CR-10a). With runway room off-peak (about 10 movements an hour at the shoulders and spare midday capacity), airlines add movements, some of them thinly loaded, in the base seasons (C-5; A-5). The cap is fixed at the summer 2025 number, so the race raises no one's total: it changes shares, and the crew, fuel and aircraft time spent on it are used up (C-6; CR-8c; CR-7c, 0.7: part of the value is used up in competing to qualify). C-5 is signed on a flow, movements in the window, against a counterfactual of the same seasons without the order (CR-12, 0.9). In the gap between the base seasons and the cap (summer 2027) nothing is earned, and movements return toward their counterfactual path; no sign is derived for that window. That night operators moved night flights into the daytime during the base seasons, to earn daytime history, would need A-28 (p = 0.35); not reported.

**Night flights move in time and place (C-7 to C-10, RS-8).** A night operator has three options against the curfew: buy or lease a daytime slot and fly in the nearest daytime hour (the shoulders, 06:00 to 07:00 and 22:00 to 23:00), move the flight to Pellham, or stop. The integrator's night sort needs the night: a sort that ends at 05:00 cannot be done in daytime slots. So most of its operation goes to Pellham (C-7; RS-4; A-6). Passenger night flights and some cargo flights move into the shoulders, using slots bought or leased (C-10) and retimed under K4 (C-8, C-9; A-7). The same flights happen without the order, at night, so by 02_ontology.md, 2.5 the shift is signed per window against the counterfactual: night movements at WXI decrease (C-1) and shoulder movements increase.

The 22:00 to 23:00 window has a second timing chain under one reading (RS-8, 0.9: an opposing chain from a second incentive). Under U1-b, a flight scheduled to arrive at 22:40 that runs 25 minutes late cannot land at WXI; airlines move some late-evening flights earlier to keep a buffer (A-23), which lowers movements in that hour against the counterfactual. Under U1-a, a late flight may still operate until midnight, so no buffer is needed, and the hour is if anything more attractive (C-15). So the sign in the hour is `increase` under U1-a and `ambiguous` under U1-b (CR-12b; no premise ranks the night flights moving in against the late flights moving out). The 06:00 to 07:00 hour has no such chain: early arrivals before 06:00 already hold or slow down en route.

**Larger aircraft (C-11).** The constraint is counted in movements, not seats. By CR-4c with the unit of the constraint, an airline that values a slot at the margin gets more from it with more seats on it: where fleets allow (A-8), routes move to larger aircraft.

**Consolidation (C-12, EN-13).** Slots are tradable and airlines value them differently (A-10): network carriers with connecting traffic and large aircraft value a WXI slot more than a small airline flying a thin route. Slots move toward the first (CR-5, CR-7a), and some small airlines sell or lease out their slots and leave WXI, some for Pellham. Night operators who buy slots were already operating at WXI, so they add no operator against the counterfactual. Lessors receive the lease price (C-34).

**The priority for freed slots (K5).** Night operators rank first for slots returned to the WAA. But with slots tradable, a holder that no longer wants a slot sells or leases it rather than let it return free (CR-4: x: let it lapse, y: sell it); a holder below 80% use leases out the unused days. So slots return mainly when a carrier fails. The priority is a free claim on a small and uncertain flow. By CR-3b it cannot make night operators worse off; the case gives no premise that the flow is material, so no consequence is recorded. EN-12's clause on a share reserved for newcomers does not fit a priority on a residual flow (Gaps found, c).

**Entry, breach, scheduling (C-13 to C-15).** Would-be entrants must buy slots, where before they needed only gates and staff (C-13). The curfew penalty is $50,000; an operator whose aircraft would otherwise be stranded at the wrong airport, or whose cargo cannot wait, sometimes pays it (C-14; A-14). Both readings give C-14: under U1-a breach is a movement after midnight or an unscheduled one after 23:00, under U1-b any movement after 23:00 without an emergency. Under U1-a, a flight scheduled at 22:55 that usually operates at 23:20 is protected while a flight scheduled at 23:20 is banned: airlines reshape late flights into the protected form (C-15; RS-5; A-24). Under U1-b the nominal schedule protects nothing, so CR-4 gives no reason for it: `no_change`.

**Lobbying (C-16, C-17).** Night operators have a concentrated stake in exemptions and in reading U1-a; slot holders now gain from scarcity and have a stake in keeping the cap at 380 (EN-5's move, applied to holders of a tradable right); would-be entrants press for a larger new-entrant share (A-15). None of these lobbied on the question without the order. The residents' associations did: their campaign for a curfew had run since 2023 and, on the counterfactual path, would have continued. By RS-7's Unless clause their lobbying is compared with that campaign: under the order they defend it and press for U1-b; without it they would press for a curfew. No premise says which is more, so C-17 is `ambiguous`.

**The integrator's facility (C-18).** The sort facility at WXI has little use other than a night sort (A-16); from the draft its expected yield falls, and the loss falls on the integrator as holder when the change became expected (CR-7c, CR-10c).

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-19 | `travelers.wxi` | `price_paid` (fares on WXI flights) | increase | medium | EN-6, CR-6, CR-12e (response argument), CR-12 (0.9: what the response argument gives) | movements `input_to` passenger trips | A-1, A-2, A-9 |
| C-20 | `travelers.wxi` | `quantity_traded` (passenger trips through WXI) | decrease | medium | EN-6, OC-4, CR-12e, CR-12 (0.9) | as C-19 | A-1, A-2, A-9 |
| C-21 | `airlines.history` | `net_price_received` (per seat on WXI flights, after WAA charges) | increase | medium | EN-2, CR-6, CR-7b, CR-12e (dominance, A-26) | as C-19 | A-1, A-2, A-9, A-13, A-26 |
| C-22 | `travelers.night` | `travel_time` (to Pellham, at shoulder times, or on diverted flights) | increase | short to medium | RS-4, CR-9, CR-3a | night flights and Pellham flights: `substitute`; trip to the airport: `complement` | A-6, A-7, A-11 |
| C-23 | `travelers.wxi` (some) | `quantity_substitute` (trips through Pellham) | increase | medium | RS-1, RS-16 | WXI and Pellham flights: `substitute`, partial | A-1, A-11 |
| C-24 | `sellers.substitutes` (Pellham authority) | `quantity_traded` (movements handled at Pellham) | increase | short to medium | CR-9, RS-16 | as C-23; night cargo `across_border` to Pellham | A-6, A-11 |
| C-25 | `workers.wxi` | `employment`, `hours_worked` (at WXI) | at_least_one_decrease | short to medium | RS-6, CR-9, OC-5 | labor `input_to` movements and the sort | A-6, A-25 |
| C-26 | `workers.pellham` | `employment` (cargo sort and handling at Pellham) | increase | short to medium | OC-5 (0.9: new to the place), CR-9 | labor `input_to` the sort | A-6 |
| C-27 | `neighbors.wxi` | `asset_value` (homes in WXI's night-noise contour; not counting effects through proximity) | decrease | short (from March 2026) to medium | CR-9, CR-7c, CR-10c, CR-12 (0.9) | airport jobs and nearby homes: `complement`, note `location` | A-6, A-12, A-25 |
| C-28 | `neighbors.wxi` | `asset_value` (homes in WXI's night-noise contour) | ambiguous | short to medium | CR-9 (`proximity`; Tier C), CR-7c, CR-12b, CR-12 (0.9: Tier C against Tier B; kind 3) | movements and homes under them: `proximity` | A-6, A-7, A-12, A-22, A-25 |
| C-29 | `neighbors.pellham` | `asset_value` (homes in Pellham's prospective night contour; not counting effects through proximity) | increase | short to medium | CR-9, CR-7c, CR-10c, CR-12 (0.9) | airport jobs and nearby homes: `complement`, note `location` | A-6, A-12 |
| C-30 | `neighbors.pellham` | `asset_value` (homes in Pellham's prospective night contour) | decrease | short to medium | CR-9 (`proximity`; Tier C), CR-7c, CR-12 (0.9), CR-12e (dominance, A-20) | movements and homes under them: `proximity` | A-6, A-12, A-20, A-22 |
| C-31 | `shippers.wexcombe` | `quality_per_unit` (latest collection time for overnight parcels) | decrease | short to medium | CR-9, CR-4 | the sort `input_to` overnight delivery | A-6, A-17 |
| C-32 | `airlines.history`, `operators.night` | `price_paid` (WAA charges per movement) | increase | medium (at the annual reviews) | PC-15, CR-1, CR-2 | WAA services `input_to` movements | A-1, A-13 |
| C-33 | `concessions.wxi` | `quantity_traded` (parking, retail, car hire at WXI) | decrease | medium | RS-12, CR-9 | `complement` in use with trips through WXI | A-9, A-21 |
| C-34 | `airlines.history` (lessors and sellers of slots) | `resources_available_other_uses` (lease and sale receipts) | increase | medium | CR-8b, CR-5, EN-13 | slot lease or sale: `contract` | A-4, A-10 |
| C-35 | `operators.night`, `airlines.prospective` (lessees and buyers of slots) | `resources_available_other_uses` | decrease | medium | CR-8b, CR-3 (note) | as C-34 | A-4, A-7 |
| C-36 | `airlines.history` | `asset_value` (WXI operations as a whole: slots, the forgone option to grow, the race, charges) | ambiguous | medium | CR-7c, CR-12b, CR-12 (0.8: two items in one variable) | — | A-1, A-3, A-5 |

**Fares and trips: what the response argument gives (C-19, C-20).** WXI's passenger trips are sold locally; Pellham is a partial substitute 70 km away. So EN-6's main clause applies to them: with fewer movements than demand would call for, fares rise (CR-6). Two responses push back: larger aircraft (C-11) and travelers moving to Pellham (C-23). Both are responses to the scarcity the cap creates; by CR-12e's response argument they cannot take fares back below their counterfactual level, since they stop once the scarcity premium they respond to is gone. That gives "increase or no change". CR-12's 0.9 clause asks for more to report `increase`: the response must be partial. A-9 supplies it: fleets change over two to four years, WXI has three wide-body gates, and Pellham is 55 minutes away, so the responses cannot carry all of the counterfactual growth at the old cost. With A-9, C-19 is `increase`; the same argument makes passenger trips through WXI a `decrease` (C-20): larger aircraft add seats per movement but cannot take trips past their counterfactual number.

**Parcel delivery and EN-6's Inputs clause.** Movements are also an input to overnight parcel delivery, which is sold nationally. EN-6's 0.9 Inputs clause fits this output: the right's price rations the input (here the curfew prohibits the night input outright, and the day input is rationed by C-4), and the output's price moves in the wider market only by as much as Wexcombe matters there. Wexcombe is 4% of the national market and the integrator keeps serving it from Pellham, so the national price effect is noted as negligible (A-18, p = 0.15, below the cut-off). The local effect is a change in service, not price: with the sort 70 km away, collection cut-offs in Wexcombe move earlier (C-31; A-17).

**Airlines' net price per seat (C-21).** EN-2 gives holders of the scarce permission a higher net price. Against it, the WAA's charges per movement rise (C-32): its costs are mostly fixed and are spread over fewer movements than without the cap (PC-15; A-13). The two chains reach the same key with opposite signs. The figures give a dominance premise (CR-12e, arithmetic with an empirical comparison): the rise in charges is about $2 per seat by 2030, against a scarcity premium per seat that at capped airports is a multiple of that (A-26, p = 0.75). So C-21 is `increase`. Without A-26 it would be `ambiguous`.

**Travelers' outcomes are Tier B.** Fares, trips, travel time and the move to Pellham (C-19 to C-23) run through exchange: airlines sell seats, travelers buy them. No `proximity` chain reaches these keys. A traveler who also lives under the flight path is a `neighbors.wxi` member for C-27 and C-28, a different key. So CR-12's 0.9 rule for a Tier C chain against a Tier B chain is not engaged for travelers, and their consequences carry no "not counting" qualifier.

**Home values near WXI (C-27, C-28): Tier C against Tier B.** Two kinds of chain reach the value of homes in WXI's night contour.
- *Tier B, through exchange.* Fewer jobs at WXI than without the order (C-25: the night sort leaves, growth is capped) means fewer airport workers seeking homes nearby, linked by a `complement` relation noted `location` (02_ontology.md, 2.8; A-12). A home's price falls with the demand for it (CR-6), and the change is capitalized when it becomes expected, from March 2026 (CR-7c, CR-10c). Sign: decrease.
- *Tier C, through proximity.* Buyers of homes under the flight path value quieter nights (A-22), so the end of about 40 night movements raises what they will pay (+). But the same order moves flights into the shoulder hours over the same homes (C-8, C-9), which buyers value negatively (−). The proximity chain is therefore itself a chain whose parts push in opposite directions: by CR-12's 0.9 clause on kind 3, it can push either way.

Under CR-12's 0.9 rule, two consequences are recorded: the Tier B sign, `decrease`, qualified "not counting effects through proximity" (C-27), and the combined sign at Tier C (C-28). The combined sign is `ambiguous` twice over: the proximity chain is kind 3, and even if it were a plain increase no premise in the case says it outweighs the job chain. The Tier C chain does not lower C-27's tier, and C-28 stays at Tier C.

**Home values near Pellham (C-29, C-30).** The mirror case. The sort and its 900 jobs arrive at Pellham (C-26), raising demand for homes in its commuting area (Tier B, increase, C-29; A-12). Night cargo begins over 1,200 homes that had none (Tier C, decrease; A-22); here the proximity chain has one direction only, since nothing leaves Pellham's nights. The record supplies a dominance premise for the homes in the contour: hub workers spread their housing demand over about 40,000 homes in a 30 km commuting area, while the night-noise discount falls on the 1,200 under the new path (A-20, p = 0.6). So the combined sign at Tier C is `decrease` (C-30), and the Tier B sign, `increase`, is recorded beside it, qualified (C-29).

**Workers (C-25, C-26).** At WXI the night sort's part-time night shifts go and growth is capped, so employment or hours fall (RS-6, as a group). At Pellham the sort is an activity new to the place, so OC-5's 0.9 clause gives `employment` increase alone there.

**Pellham (C-23, C-24; RS-16).** Travelers and cargo move to Pellham, so its movements and trips rise. RS-16 asks whether Pellham's fares rise: only where flights there cannot be added at unchanged cost. Airlines can move aircraft to Pellham, whose runway is 45% used; A-19 (p = 0.35) is below the cut-off, so Pellham's fares are not reported. Pellham's own charges are set by its authority; more movements spread its fixed costs further (PC-15's mirror), but night operations need night staff and air traffic control, which raise its costs. No sign is recorded.

**Money between airlines (C-34, C-35).** Slot leases and sales are receipts to their sellers and outlays to their buyers (CR-8b). Night operators and entrants who buy or lease slots keep paying for something that cost them nothing before, so their means for other uses fall (CR-3 note).

**Airlines' WXI operations as a whole (C-36).** Against an airport without the order, a holder has free slots of value (C-3) and a scarcity premium (C-21), and against these the loss of the option to grow at WXI, the race costs (C-6) and higher charges (C-32). No premise ranks them: `ambiguous`. C-3 is recorded as its own item (CR-12, 0.8).

**Concessions (C-33).** Parking, shops and car hire are complements in use of trips through WXI; with fewer trips (C-20), they sell less (RS-12; A-21).

Stopping points: Pellham-area shops and services, hub workers' other spending, aircraft lessors and manufacturers (larger aircraft): depth 3 or 4, diffuse; stopped. Noise, sleep and health: out of scope.

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `travelers.wxi`, `price_paid` (fares), medium | Fewer movements than demand calls for (EN-6, CR-6). | Larger aircraft (C-11); travelers moving to Pellham (C-23). | CR-12e response argument: the responses cannot reverse the scarcity they respond to; A-9 makes them partial (CR-12, 0.9). | **increase** (C-19). Trips: **decrease** (C-20). No proximity chain reaches travelers' keys. |
| `airlines.history`, `net_price_received` (per seat), medium | Scarcity premium (EN-2). | WAA charges spread over fewer movements (C-32, PC-15). | A-26 (arithmetic on the figures, with an empirical comparison) | **increase** (C-21). |
| `operators.night`, `airlines.history`, `quantity_supplied` (22:00 to 23:00), short to medium | Night flights moved into the hour (A-7); under U1-a, flights reshaped to just before 23:00 (C-15). | Under U1-b only: late flights moved earlier to keep a buffer (A-23). | None | **U1-a: increase; U1-b: ambiguous** (C-9). |
| `neighbors.wxi`, `asset_value` (homes in the contour), short to medium | Quieter nights (Tier C, A-22). | Fewer airport workers seeking homes (Tier B, A-12); busier shoulders (Tier C). | None | Tier B: **decrease** (C-27). Tier C: **ambiguous** (C-28; the proximity chain is itself kind 3). |
| `neighbors.pellham`, `asset_value` (homes in the prospective contour), short to medium | Hub workers seeking homes (Tier B, A-12). | Night cargo over the homes (Tier C, A-22). | A-20 (empirical: the jobs' demand is spread over 40,000 homes, the noise falls on 1,200) | Tier B: **increase** (C-29). Tier C: **decrease** (C-30). |
| `neighbors.wxi` associations, `lobbying_effort`, short to medium | Defending the order, pressing for U1-b. | The counterfactual campaign for a curfew. | None (RS-7 Unless) | **ambiguous** (C-17). |
| `airlines.history`, `asset_value` (WXI operations as a whole), medium | Slots (C-3); scarcity premium (C-21). | No growth at WXI; race costs (C-6); charges (C-32). | None | **ambiguous** (C-36). The slots alone: **increase** (C-3). |
| `airlines.history`, `quantity_supplied` (daytime movements), per window | Base seasons: the race (C-5). | From October 2027: the cap (C-2). | Different windows, not combined (CR-12g) | Base seasons: **increase** (C-5). From October 2027: **decrease** (C-2). Summer 2027: not signed. |
| `officials.enforcement`, `enforcement_cost` (total), short to long | Slot unit and curfew monitoring (C-37); shoulder-noise complaints (Tier C). | Fewer night-noise complaints (Tier C, C-38). | CR-12e, arithmetic: the slot unit ($2.8 million) exceeds the whole noise office ($0.5 million) | Not counting proximity: **increase** (C-37). Tier C: **increase** (C-39). |

## 8. Time structure

- **March 2026: the draft.** Expected changes are capitalized from the draft, rising toward adoption in September 2026 (CR-7c, probability clause): the claim to slots (C-3), the integrator's facility (C-18), and homes near both airports (C-27 to C-30), at Tier B through jobs and Tier C through noise.
- **Summer 2026 and winter 2026/27: the race.** Base-season history sets each airline's share, so daytime movements rise in these seasons against the counterfactual (C-5), and the resources spent on thin flights are used up (C-6). No matching dip follows within the policy's own windows: after March 2027 the incentive ends, and from October 2027 the cap governs (C-2). This is a rise in the window and a separate fall under the cap, each signed against the counterfactual (CR-12g), not a shift of the same movements from one window to another.
- **From 31 October 2027: curfew and cap.** Night movements stop (C-1); night flights move to the shoulders (C-8, C-9) and the sort to Pellham (C-7), whose new contour begins to hear it. Slot leasing and trading begin (C-4, C-10). The cap binds by about 7% in the first season against the counterfactual and more each year (TS-3, C-2), so fares, trips and the slot price move further apart from their counterfactual paths over time (C-19, C-20, C-4).
- **Two to four years: fleets.** Larger aircraft arrive as fleets turn over (C-11); A-9 says this is too slow and too limited to carry the counterfactual growth. Small airlines sell or lease out and leave (C-12).
- **The 2032 review.** Holders expect slots to last (A-3); as a change in the cap becomes more or less likely, slot values move on whoever holds them then (CR-7c).
- **Per reading of U1.** Under U1-a, late-running flights keep using 23:00 to 24:00, airlines schedule into the protected hour (C-15), and the shoulder 22:00 to 23:00 rises (C-9). Under U1-b, late flights divert to Pellham, and the hour before 23:00 has two opposing timing chains (C-9).

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-37 | `officials.enforcement` (WAA) | `enforcement_cost` (slot coordination and curfew monitoring; total not counting effects through proximity) | increase | About $2.8 million a year of staff and systems. | OC-3, CR-8c |
| C-38 | `officials.enforcement` (WAA) | `enforcement_cost` (handling night-noise complaints) | decrease | Staff time no longer spent on complaints about night movements. | OC-3 (right baseline), CR-9 (`proximity`; Tier C) |
| C-39 | `officials.enforcement` (WAA) | `enforcement_cost` (total) | increase | As C-37, net of C-38 and of any rise in shoulder complaints. | OC-3, CR-12 (0.9), CR-12e (arithmetic) |
| C-40 | `airlines.history`, `operators.night` | `compliance_cost` (slot applications, movement records, trade and retiming registrations) | increase | Staff time in airlines' scheduling departments. | OC-2, CR-8c |
| C-41 | `operators.night`, `travelers.night`, `shippers.wexcombe` | `quantity_traded` (night air services neither moved to the shoulders nor to Pellham) | decrease | The flights and shipments that stop. Both sides lose the gain each expected. | OC-4, CR-5a |
| C-42 | `officials.enforcement` (WAA) | `non_tax_receipts` (penalties) | increase | Paid by operators who breach (C-14). | CR-8b |
| C-6 | `airlines.history` | `compliance_cost` (flights added to build history) | increase | Crew, fuel and aircraft time used up in the race. | EN-12, CR-8c |

**Who pays the WAA's costs (OC-3).** K6 funds the WAA from its charges, which recover its costs: the policy's own revenue in OC-3's sense. The cost reaches airlines as a higher charge per movement (C-32), and through them travelers. The right baseline is the WAA's work without the order, not zero: its noise office handles fewer night complaints (C-38). That link runs through proximity (a complaint follows from noise, not from an exchange), so C-38 is Tier C and is not netted against C-37. By CR-12's 0.9 rule the total is recorded twice: not counting proximity, `increase` (C-37); at Tier C, `increase` too (C-39), since the slot unit costs more than five times the whole noise office, so no change in complaints can reverse it (arithmetic).

**Both sides of each transfer.** Slot leases and sales: C-34 and C-35. Penalties: C-14 and C-42. Charges: C-32 (airlines pay) and the WAA's receipts, which by its cost-recovery method equal its costs (C-37). The slots themselves are created, not taken from a payer; the value they carry is partly a transfer from would-be entrants and from travelers (C-13, C-19), and partly used up in the race (C-6).

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | Without the order, daytime movements would grow above 380 a day (about 3% a year), and off-peak runway capacity allows it. | counterfactual_trend | 0.85 | Growth 2015 to 2025; airlines' published plans; hourly use. | The cap does not bind; C-2, C-4, C-11, C-13 and C-19 to C-21 fail. |
| A-2 | The WAA detects every movement from air traffic control's log and imposes penalties. | enforcement | 0.9 | Movement logs are complete; penalties are administrative. | C-1 and C-2 shrink; C-14 grows. |
| A-3 | Holders expect slots to last past the 2032 review without reallocation. | expectations | 0.7 | Order art. 12; practice at other slot-controlled airports. | C-3 and C-36 are smaller. |
| A-4 | A slot market forms: slots are sold, leased and retimed at low transaction cost. | other | 0.75 | K4; slot markets at other capped airports. | C-4, C-8 to C-10, C-12, C-34 and C-35 are smaller. |
| A-5 | Airlines expected base-season history to set their share, and some could add off-peak daytime movements at a cost below the expected value of the extra slots. | expectations | 0.8 | The draft named the base seasons; off-peak capacity; expected slot values. | C-5 and C-6 are not reported. |
| A-6 | The integrator moves most of its night sort to Pellham, and other night cargo follows. | mobility | 0.7 | Pellham's spare capacity, no curfew; the sort needs night hours. | C-7, C-18, C-22, C-24 to C-26 and C-29 to C-31 are not reported. |
| A-7 | Some night operators buy or lease daytime slots and fly in the shoulder hours. | substitutability | 0.7 | Passenger night flights' timing needs; shoulder capacity. | C-8, C-10 and C-35 are not reported; C-9 under U1-b loses its (+) chain. |
| A-8 | Airlines can move to larger aircraft on some WXI routes within the medium horizon. | other | 0.7 | Fleet plans; three wide-body gates. | C-11 is not reported. |
| A-9 | Larger aircraft and Pellham together cannot carry all of the counterfactual growth at the old cost (the responses are partial). | other | 0.8 | Fleet lead times of two to four years; gate limits; 55 minutes to Pellham. | C-19 and C-20 are "increase or no change" and "decrease or no change", not reported as signed; C-21 and C-33 fail. |
| A-10 | Airlines differ in the value they get from a WXI slot. | other | 0.8 | Network and point-to-point carriers; aircraft sizes. | C-12 and C-34 are not reported. |
| A-11 | Some travelers find Pellham a substitute. | substitutability | 0.7 | Motorway access; catchment surveys. | C-22 (in part), C-23 and C-24 (in part) are not reported. |
| A-12 | Airport workers' housing demand is a material part of demand for homes near each airport, including the contours. | other | 0.6 | 30% of WXI workers live within 8 km; commuting patterns at Pellham. | C-27 and C-29 are not reported; C-28 loses its Tier B chain (still ambiguous); C-30 rests on the proximity chain alone. |
| A-13 | The WAA sets charges to recover costs that are largely fixed. | other | 0.75 | The WAA's charging policy and accounts. | C-32 is not reported; C-21 needs no dominance premise. |
| A-14 | Some operators sometimes operate after the permitted time and pay the penalty. | enforcement | 0.55 | Penalty against the cost of a stranded aircraft or a missed sort; experience at other curfews. | C-14 and C-42 are not reported. |
| A-15 | Night operators, slot holders, would-be entrants and residents' associations can organize at a cost below their stake. | other | 0.85 | Hearing records 2026; the residents' campaign since 2023. | C-16 and C-17 are not reported. |
| A-16 | The integrator's WXI sort facility has no equally valuable other use. | alternative_uses | 0.7 | Purpose-built hall airside. | C-18 is not reported. |
| A-17 | With the sort 70 km away, collection cut-offs in Wexcombe move earlier. | other | 0.65 | Trucking time to Pellham; the integrator's network times. | C-31 is not reported. |
| A-18 | The move of Wexcombe's sort raises the national price of overnight parcel delivery by more than a negligible amount. | other | 0.15 | Wexcombe is 4% of the market and is still served. | Below the cut-off: noted as negligible, not reported. |
| A-19 | Airlines cannot add flights at Pellham at unchanged cost, so Pellham fares rise. | other | 0.35 | Pellham's runway is 45% used; aircraft are mobile. | Below the cut-off: Pellham fares not reported (RS-16). |
| A-20 | In Pellham's prospective night contour, the discount buyers place on night noise exceeds the added demand from hub workers. | other | 0.6 | 900 hub jobs spread over 40,000 homes; 1,200 homes under the new night path; hedonic studies of night noise. | C-30 is `ambiguous` at Tier C. |
| A-21 | Concession sales follow passenger numbers. | other | 0.8 | Concession accounts. | C-33 is not reported. |
| A-22 | Buyers of homes in a night-noise contour value quieter nights, so night movements are capitalized in home prices. | other | 0.85 | Hedonic studies near airports; the residents' campaign. | The Tier C chains of C-28 and C-30 fail; C-28 would rest on its Tier B chain; C-30 on C-29. |
| A-23 | Under U1-b, airlines move some flights scheduled 22:00 to 23:00 earlier to keep a buffer against delays. | expectations | 0.65 | Delay distributions for late-evening flights; diversion costs. | C-9 under U1-b becomes `increase`. |
| A-24 | Under U1-a, airlines schedule some flights just before 23:00 knowing they will often operate after it. | other | 0.6 | Scheduling practice at curfewed airports with a delay allowance. | C-15 under U1-a is not reported; C-9 under U1-a still increases (A-7). |
| A-25 | Employment and hours at WXI follow movements and the night sort. | alternative_uses | 0.8 | Staffing per movement; the sort's shifts. | C-25 is not reported; C-27 loses its chain. |
| A-26 | The scarcity premium per seat exceeds the rise in WAA charges per seat (about $2 by 2030). | other | 0.75 | Fare premiums at capped airports against the charge arithmetic in the record. | C-21 is `ambiguous`. |
| A-27 | Some night services are neither moved to the shoulders nor to Pellham. | other | 0.7 | Late passenger flights on thin routes; ad hoc cargo charters. | C-41 is not reported. |
| A-28 | Night operators moved night flights into the daytime during the base seasons to earn daytime history. | expectations | 0.35 | A night sort cannot run in the day; passenger night flights have their own timing needs. | Below the cut-off: not reported. If true, night movements fall in the base seasons and night operators hold more slots. |

**Final check before the report.**
1. *Uncombined chains.* Fares (C-19), net price per seat (C-21), the 22:00 hour (C-9), home values at both airports (C-27 to C-30), residents' lobbying (C-17), airlines' operations as a whole (C-36) and the WAA's total cost (C-37 to C-39) are each combined in section 7. The race (C-5) and the cap (C-2) reach daytime movements in different windows and are not combined (CR-12g).
2. *Groups.* Workers at WXI are a group (C-25); at Pellham, `employment` alone (OC-5, new to the place).
3. *Baseline.* Every sign is against WXI without the order. C-9 and C-15 compare readings with the counterfactual, not with each other. The lease price, legal breach and slot trades exist only under the order and are increases against none (CR-12, 0.9).
4. *Worse off is not poorer.* `resources_available_other_uses` is signed only for buyers and lessees of slots, who keep paying (C-35), and lessors, who receive (C-34). Night travelers and the integrator are worse off by their own ranking (CR-3a) but no money sign is given for them.
5. *Timing shifts.* Night to shoulders: per window (C-1, C-8, C-9). The race: a flow in its window (C-5).
6. *Both sides.* Section 9.
7. *Every class, every core rule.* CR-7c checked for slots, the sort facility, homes at both airports, airlines' operations; CR-6 for slots and fares; CR-9 for Pellham, workers, concessions, shippers, homes; enforcement costs and their payers (OC-3).
8. *Unstated premises.* Lobbying (A-15), margins (A-5, A-7, A-8, A-27), the proximity link (A-22) and the dominance premises (A-20, A-26) are in the table.

## 11. Report

**The policy.** From 31 October 2027 no aircraft may take off or land at Wexcombe International between 23:00 and 06:00, and daytime movements are capped at 380 a day, the 2025 number. The 380 daytime slots are given free to airlines in proportion to the flights they operated in summer 2026 and winter 2026/27, seasons that began after the plan was published; slots can be sold, leased and moved to other daytime hours; slots returned to the authority go first to night operators. Whether a late-running flight scheduled before 23:00 may still operate until midnight is unclear.

**Visible consequences.** No more scheduled night flights at WXI (C-1); fewer daytime flights than the airport would otherwise have had (C-2); slots of substantial value for incumbent airlines (C-3).

**Invisible consequences.**
- *Airlines and slots.* A price for slots appears (C-4). Because the base seasons came after the announcement, airlines raced to build history, flying extra, thinly loaded flights in 2026 and 2027 (C-5) and using up crew, fuel and aircraft time (C-6). Slots then consolidate in the airlines that value them most; some small airlines leave (C-12), lessors receive lease income (C-34), and new airlines start less often (C-13). Airlines move to larger aircraft (C-11). The slots' value is not airlines' net gain: counting lost growth, race costs and higher charges, their position may be better or worse (C-36). The priority for night operators is a claim on a small residual flow of slots and has no signed effect.
- *Night operations.* The integrator moves its night sort to Pellham (C-7), its WXI facility loses value (C-18), and collection times in Wexcombe move earlier (C-31). Other night flights buy or lease daytime slots (C-10, C-35) and fly in the shoulder hours: more flights 06:00 to 07:00 (C-8), and 22:00 to 23:00 under the "until midnight" reading (C-9). Some services stop (C-41). Some operators break the curfew and pay penalties (C-14, C-42).
- *Travelers.* Fares at WXI are higher (C-19) and trips fewer (C-20) than without the order; airlines' net price per seat rises (C-21). Night travelers travel longer (C-22); more travelers use Pellham (C-23, C-24). Airport concessions sell less (C-33), and the authority's charge per movement rises (C-32).
- *Workers and homes.* Fewer jobs or hours at WXI (C-25), more at Pellham (C-26). Not counting noise, homes near WXI lose value with the jobs (C-27), and homes near Pellham gain (C-29). Counting noise (Tier C), home values near WXI may rise or fall (C-28); near Pellham's new night path they fall (C-30).
- *Costs.* The authority's slot unit and monitoring (C-37, C-39), net of fewer night complaints (C-38, Tier C); airlines' paperwork (C-40).

**Per reading of U1.** If late flights may operate until midnight (U1-a), airlines schedule into the protected hour (C-15) and the hour before 23:00 gets busier (C-9). If not (U1-b), late flights divert to Pellham, airlines move some late flights earlier, and the hour before 23:00 may get busier or quieter (C-9).

**Ambiguous effects.** Home values near WXI counting noise (C-28): quieter nights against busier shoulders and fewer airport workers. Residents' lobbying (C-17), against a counterfactual campaign. Airlines' overall position (C-36). The 22:00 to 23:00 hour under U1-b (C-9).

**Key conditions.** That demand would have grown (A-1, p = 0.85); that the responses to the cap are partial (A-9, p = 0.8), which turns "fares do not fall" into "fares rise"; that the integrator moves to Pellham (A-6, p = 0.7); that the slot market works (A-4, p = 0.75); that airport jobs matter for nearby housing (A-12, p = 0.6); and, for every claim through noise, that home buyers price quiet nights (A-22, p = 0.85).

**What this analysis cannot say.** How large any effect is; whether the curfew's gain to sleepers exceeds its cost to travelers and shippers; noise, sleep and health as such (out of scope for version 1); how much of the slots' value was used up in the race; whether the policy is desirable.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | operators.night | quantity_supplied (movements 23:00 to 06:00) | decrease | short–long | visible | B | CR-1, RS-8 | A-2 |
| C-2 | airlines.history | quantity_supplied (daytime movements) | decrease | short–long | visible | B | CR-1, EN-6, TS-3 | A-1, A-2 |
| C-3 | airlines.history | asset_value (slots) | increase | short | visible | B | EN-12, CR-7c, CR-10c, SB-4 | A-1, A-2, A-3 |
| C-4 | airlines.history, operators.night, airlines.prospective | right_lease_price (slots) | increase | short–long | invisible | B | EN-6, CR-6, CR-12 | A-1, A-2, A-4 |
| C-5 | airlines.history | quantity_supplied (daytime movements in the base seasons) | increase | short | invisible | B | EN-12, RS-8, CR-10a, CR-7c | A-5 |
| C-6 | airlines.history | compliance_cost (flights added to build history) | increase | short | invisible | B | EN-12, CR-8c | A-5 |
| C-7 | integrator, cargo carriers | quantity_substitute (night movements at Pellham) | increase | short–medium | invisible | B | RS-4, RS-1, RS-16 | A-2, A-6 |
| C-8 | operators.night | quantity_supplied (movements 06:00 to 07:00) | increase | short–medium | invisible | B | RS-8, CR-4, EN-13 | A-4, A-7 |
| C-9 | operators.night, airlines.history | quantity_supplied (movements 22:00 to 23:00) | U1-a: increase; U1-b: ambiguous | short–medium | invisible | B | RS-8, CR-4, CR-12b | A-4, A-7, A-23, A-24 |
| C-10 | operators.night | quantity_traded (slots bought or leased) | increase | short–medium | invisible | B | CR-4, CR-5, EN-13, CR-12 | A-4, A-7 |
| C-11 | airlines.history | unit_size (seats per movement) | increase | medium | invisible | B | CR-4c, CR-6, CR-7a | A-1, A-8 |
| C-12 | airlines.history | number_of_sellers (airlines at WXI) | decrease | medium | invisible | B | EN-13, CR-5, CR-7a | A-4, A-10 |
| C-13 | airlines.prospective | entry_rate (airlines starting at WXI) | decrease | medium | invisible | B | CR-1, CR-4, EN-6 | A-1, A-2 |
| C-14 | operators.night | legal_breach (movements after the permitted time) | increase | short–medium | invisible | B | RS-3, CR-4, CR-12 | A-14 |
| C-15 | airlines.history | reclassification (flights scheduled just before 23:00) | U1-a: increase; U1-b: no_change | short–medium | invisible | B | RS-5, CR-4 | A-24 |
| C-16 | operators.night, airlines.history, airlines.prospective | lobbying_effort | increase | short–medium | invisible | B | RS-7, EN-5 | A-15 |
| C-17 | neighbors.wxi (associations) | lobbying_effort | ambiguous | short–medium | invisible | B | RS-7, CR-4 | A-15 |
| C-18 | integrator | asset_value (WXI sort facility) | decrease | short | invisible | B | CR-7c, CR-10c, SB-4 | A-6, A-16 |
| C-19 | travelers.wxi | price_paid (fares) | increase | medium | invisible | B | EN-6, CR-6, CR-12e, CR-12 | A-1, A-2, A-9 |
| C-20 | travelers.wxi | quantity_traded (trips through WXI) | decrease | medium | invisible | B | EN-6, OC-4, CR-12e, CR-12 | A-1, A-2, A-9 |
| C-21 | airlines.history | net_price_received (per seat, after charges) | increase | medium | invisible | B | EN-2, CR-6, CR-7b, CR-12e | A-1, A-2, A-9, A-13, A-26 |
| C-22 | travelers.night | travel_time | increase | short–medium | invisible | B | RS-4, CR-9, CR-3a | A-6, A-7, A-11 |
| C-23 | travelers.wxi | quantity_substitute (trips through Pellham) | increase | medium | invisible | B | RS-1, RS-16 | A-1, A-11 |
| C-24 | sellers.substitutes (Pellham) | quantity_traded (movements at Pellham) | increase | short–medium | invisible | B | CR-9, RS-16 | A-6, A-11 |
| C-25 | workers.wxi | employment, hours_worked | at_least_one_decrease | short–medium | invisible | B | RS-6, CR-9, OC-5 | A-6, A-25 |
| C-26 | workers.pellham | employment (sort and handling) | increase | short–medium | invisible | B | OC-5, CR-9 | A-6 |
| C-27 | neighbors.wxi | asset_value (homes in the night contour; not counting effects through proximity) | decrease | short–medium | invisible | B | CR-9, CR-7c, CR-10c, CR-12 | A-6, A-12, A-25 |
| C-28 | neighbors.wxi | asset_value (homes in the night contour) | ambiguous | short–medium | invisible | C | CR-9 (proximity), CR-7c, CR-12b, CR-12 | A-6, A-7, A-12, A-22, A-25 |
| C-29 | neighbors.pellham | asset_value (homes in the prospective contour; not counting effects through proximity) | increase | short–medium | invisible | B | CR-9, CR-7c, CR-10c, CR-12 | A-6, A-12 |
| C-30 | neighbors.pellham | asset_value (homes in the prospective contour) | decrease | short–medium | invisible | C | CR-9 (proximity), CR-7c, CR-12, CR-12e | A-6, A-12, A-20, A-22 |
| C-31 | shippers.wexcombe | quality_per_unit (latest collection time) | decrease | short–medium | invisible | B | CR-9, CR-4 | A-6, A-17 |
| C-32 | airlines.history, operators.night | price_paid (WAA charges per movement) | increase | medium | invisible | B | PC-15, CR-1, CR-2 | A-1, A-13 |
| C-33 | concessions.wxi | quantity_traded (parking, retail, car hire) | decrease | medium | invisible | B | RS-12, CR-9 | A-9, A-21 |
| C-34 | airlines.history (lessors, sellers) | resources_available_other_uses (lease and sale receipts) | increase | medium | invisible | B | CR-8b, CR-5, EN-13 | A-4, A-10 |
| C-35 | operators.night, airlines.prospective (lessees, buyers) | resources_available_other_uses | decrease | medium | invisible | B | CR-8b, CR-3 | A-4, A-7 |
| C-36 | airlines.history | asset_value (WXI operations as a whole) | ambiguous | medium | invisible | B | CR-7c, CR-12b, CR-12 | A-1, A-3, A-5 |
| C-37 | officials.enforcement (WAA) | enforcement_cost (slot unit and monitoring; not counting effects through proximity) | increase | short–long | invisible | A | OC-3, CR-8c | none |
| C-38 | officials.enforcement (WAA) | enforcement_cost (night-noise complaints) | decrease | short–long | invisible | C | OC-3, CR-9 (proximity) | A-22 |
| C-39 | officials.enforcement (WAA) | enforcement_cost (total) | increase | short–long | invisible | C | OC-3, CR-12, CR-12e | A-22 |
| C-40 | airlines.history, operators.night | compliance_cost (slot paperwork) | increase | short | invisible | A | OC-2, CR-8c | none |
| C-41 | operators.night, travelers.night, shippers.wexcombe | quantity_traded (night services that stop) | decrease | short–medium | invisible | B | OC-4, CR-5a | A-2, A-27 |
| C-42 | officials.enforcement (WAA) | non_tax_receipts (penalties) | increase | short–medium | invisible | B | CR-8b | A-14 |

## Gaps found

**(a) Calculus gaps (a step no core rule covers).** None new. Every chain through night noise rests on the `proximity` relation, which is GAP-026-1 (closed into CR-9 0.7 as a Tier C relation; Q20 open). Every other step was derived from CR-1 to CR-12.

**(b) Unclear core rules.**
1. *CR-12 0.9, Tier C against Tier B, when the Tier C chain is itself kind 3.* At WXI the proximity chain has two parts (quieter nights, busier shoulders). The 0.9 rule says "the combined sign at Tier C (`ambiguous` unless a dominance premise covers the Tier C chain)". It does not say what a dominance premise would have to cover when the Tier C chain is itself mixed; read with CR-12's 0.9 kind 3 clause, it would have to cover the Tier B chain against both directions of the Tier C chain. Applied that way (C-28); the rule could say so.
2. *CR-12 0.9, the response argument with two responses.* Fares face two responses (larger aircraft, Pellham). The 0.9 clause asks that "the response" be partial; read as the responses together, since either alone might be partial while both together are not. A-9 is stated for both together.
3. *CR-7c and the race.* CR-7c 0.7 says part of a right's value is used up where actors compete to qualify. Here the cap was fixed before the race, so the race raised no one's total and was pure competition for shares. The clause does not say that the whole of what is spent is then used up (CR-8c) with nothing created; read so (C-6).
4. *CR-9 with a location complement for homes.* The Tier B chain on home values runs from jobs to housing demand through a `complement` relation noted `location`. 02_ontology.md, 2.8 defines that note for "holding a good tied to a place (a controlled tenancy)" linking housing to labor markets; used here in the other direction (jobs at a place link to housing near it). It seemed to fit, but the note's definition is narrower.

**(c) Missing or wrong patterns.**
1. *EN-12, a priority on a residual flow.* EN-12's last sentence covers "a share reserved for newcomers by lottery or open eligibility". K5 reserves not a share but a priority on slots that are returned. With tradable slots, holders sell rather than return (CR-4), so the flow is small. No pattern prompts this; derived from CR-3b and CR-4. Not a sign the pattern gave wrongly, but a case it does not reach.
2. *EN-2 under a cap with a cost-recovery charge.* EN-2 gives incumbents `net_price_received` increase. Here an existing rule (cost-recovery charges, PC-15) pushes the other way. EN-2 applied as written would have given `increase` without the opposing chain; the sign held only with a dominance premise (A-26). EN-2 could note that a charge spread over the capped quantity is an opposing chain.
3. *RS-8 and the race.* RS-8 says every timing move "has two sides: the action rises in the favored window and falls in the window it was taken from". The base-season race has no window it was taken from: the extra movements are added, not moved. EN-12 covers the race; RS-8 cited alongside it suggests a matching dip that does not exist. Signed as a rise in the window only (C-5).
4. *PC-15's mirror.* PC-15 covers a shrinking base. Pellham's base grows, but night operation also adds costs; the mirror case needs a premise on costs, which PC-15 does not mention. Not signed.
5. *Candidate "high-grading under a physical-unit cap"* (6.2e, from WE-028). The move to larger aircraft (C-11) is the same derivation: CR-4c with the unit of the constraint (movements, not seats). Valid against the counterfactual (seats per movement are higher than without the cap). If accepted, this is the candidate's second use, though in a wider form than "high-grading" (choosing a larger unit, not discarding low-value catch).

**(d) Vocabulary.**
1. No variable for noise or any amenity, so the curfew's purpose has no consequence of its own; it appears only through home values (C-28, C-30) and complaint handling (C-38). This repeats the "amenity" request in 6.2f.
2. No variable for diversions (a flight landing at another airport than scheduled); recorded through `travel_time` (C-22).
3. No variable for resources used up in competing to qualify for a right (race flights); used `compliance_cost` (C-6), as WE-039 did for lottery entries.
4. The `location` note under `complement` is defined for tenancies; used here for jobs and nearby housing (b4).

**(e) Test of 0.9.**
- *CR-12 0.9, Tier C against Tier B.* Worked as written for Pellham's homes (C-29 Tier B increase qualified; C-30 Tier C decrease with dominance premise A-20) and for the WAA's costs (C-37, C-39). Needed interpretation at WXI, where the Tier C chain is itself kind 3 (b1); the rule gave two consequences (C-27, C-28) as intended. For travelers it was correctly not engaged: no proximity chain reaches their keys.
- *CR-12 0.9, what the response argument gives.* Worked, with interpretation: without A-9 the fares sign would have been "increase or no change"; the clause forced the partial-response premise, which is stated for two responses together (b2). Also used for trips (C-20).
- *CR-12 0.9, kind 3.* Worked as written for the WXI proximity chain (C-28).
- *CR-12 0.9, activities that exist only under the policy.* Worked as written for the lease price (C-4), slot trades (C-10) and breach (C-14).
- *EN-12 (0.9, promoted).* Worked as written for the race branch (C-5, C-6). The newcomer clause does not reach a priority on a residual flow (c1).
- *EN-13 (0.9, promoted).* Worked as written (C-12, C-34): slots move to airlines that value them most; small airlines sell and leave.
- *EN-6 0.9 (Inputs clause).* Worked, with a choice: movements are an input to two outputs. The Inputs clause fitted parcel delivery (sold nationally; negligible, A-18 below the cut-off); the main clause fitted passenger trips (sold locally). The clause does not say that one capped input can feed outputs in both kinds of market, but applying it per output was straightforward.
- *CR-7c (and 0.7 claims before creation, competing to qualify).* Worked as written for slots (C-3), the sort facility (C-18) and homes (C-27 to C-30, from the draft). The used-up part needed reading (b3).
- *RS-8 (0.9, more timing chains).* Worked as written for the 22:00 hour under U1-b (C-9): the buffer chain is an opposing chain from a second incentive (the risk of diversion). Its "two sides" sentence misfits the race (c3).
- *RS-16 (0.9 widened).* Worked as written: quantity at Pellham (C-23, C-24) signed; Pellham's fares need a supply premise, below the cut-off (A-19). Its 0.9 "costs on the substitute" clause was not engaged.
- *RS-7 Unless (and CR-4 0.9 on lobbying).* Worked, by analogy: CR-4 0.9 is written for repeals, but the residents' counterfactual campaign is the same situation in an imposition, and gives `ambiguous` (C-17).
- *OC-3 (0.9 fixed budget; right baseline).* Right baseline worked; the fixed-budget clause was not engaged (own revenue).
- *OC-5 0.9 (new to the place).* Worked as written (C-26).
- *Candidates from 6.2e.* "High-grading under a physical-unit cap": arguably needed in a wider form (c5); the use is valid against the counterfactual. None other needed.
