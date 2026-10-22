# WE-046 Calderford, expand-as-you-go blind run (loop_r2)

Inputs read: section 1 and the assumption table only. Names chosen from `--vocab --exclude WE-046`; no `off-list:` line appeared in any run. `policy.md` is a copy of section 1 for `--policy`.
Result: DONE in 3 rounds (depth limit), 11 + 19 + 5 = 35 node visits (first-visit nodes and revisits), 30 premise questions asked in the loop (29 from the table, 1 judged), plus 7 seed premises (6 table, 1 judged). Final engine output: 83 reported consequences, 1 unreported (`retailers.zone quantity_traded decrease`, whose dominance premise A-30 has p 0.4).

## Seed (policy's own facts only)
- Exchanges: `e_car` (drivers.nonresident buys zone road space from municipalities), `e_res` (drivers.resident), `e_taxi` (drivers.taxi), `e_goods` (retailers.zone buys deliveries from distributors.long_visit), `e_short` (retailers.zone, distributors.short_visit), `e_bus` (riders, sellers.transit). The class split follows the text: K2 residents vs K1 others; goods vehicles by §7 short visits (U1); taxis and ride-hail; buses.
- Charges K1 split by payer class (k1c cars, k1t taxis, k1g long-visit goods, k1s short-visit goods) so each can carry its own binding/enforcement premises; k2 residents. The goods charges are levied on the seller side of the delivery exchange so that incidence between carriers and zone businesses (A-14) has a place. Premises: A-1/A-33/A-12 (binds), A-2 (enforced). `moves` on the buyer side with the premise that carries the response (A-1, A-33, A-2, A-14).
- `grants`: K3 earmark as a payment to the seller side of `e_bus`. `fixed`: bus fares (rule already in force, short). `unclear` U1: k1s applies only under U1-a. `announced`: k1c, k2 (4 Jan 2027 to 1 Nov 2027; judged premise a36, p 0.9). `compliance`, `enforcers` (CCO, plus PAO on k1c), `fixed_budget` (PAO, A-24).

## Round 1 (11 nodes)
- drivers.nonresident (k1c): alternatives bus/tram (riders) and Ringside parking (A-5), switchers' travel time (A-5, A-23, A-29: bus trip takes longer), shopping at Ringside and Merrowdale (A-7), trips off-hours (A-17), through traffic to the Ring Road with longer travel time (A-18, A-31), ride-hail (A-25), moving into the zone for the $1.50 rate (A-27), registering at a zone address (A-11) with a bring-forward timing in the ten months before charging, evasion as an outside margin (A-16). Crowding links from fewer vehicles to travel time of every road class (A-3). Full cost of a day in the zone: charge (same_act) against time saved (input), with dominance for increase on A-4. Complement links to zone retailers (A-7) and zone parking; assets/yields of zone garages (A-21, A-20); part of `drivers`.
- drivers.resident (k2): moving out (A-33, A-22), bus (A-33, A-5), part of `drivers`.
- drivers.taxi: ride-hail demand raises the substitute's price where supply cannot expand at once (A-26, short); demand feeds vehicle-days; part of `drivers`.
- distributors.long_visit: consolidation (A-32), reshaping rounds into short visits only under U1-b (A-13, `reading: U1-b`), stake (A-15), incidence on the buyer side (A-14).
- distributors.short_visit: consolidation (A-32), stake (A-15), incidence (A-14).
- officials.enforcement: earmark substitutes for general-fund support (A-9); charge fund = receipts paid into, enforcement cost paid from, dominance by arithmetic (net $230-260m vs $45m).
- retailers.zone: cost link, yield to premises value (A-20), stake (A-15), dominance of lost shoppers over new visitors (A-30).
- riders: crowding on a bus system at 85% peak load that cannot add buses within a year (A-28, short); same-act link to the operator.
- sellers.transit: complement to zone retailers via new visitors (A-10); extra buses add congestion (A-34, long); dominance for bus service rising (A-8).
- municipalities, officials.adjudication: empty (the format has no variable for caseload or appeal backlog).

## Round 2 (19 nodes, 6 with proposals)
`drivers` (A-35 dominance: switching to ride-hail lowers total vehicle-days), drivers.nonresident#2 (car commuters' cost passes to the commuting wage, A-19), general_fund (support falls, so transit service falls: an input link), homebuyers (zone housing price rises where supply cannot expand; judged premise), sellers.ringside_parking (price rises, garages full: A-6), sellers.zone_parking (price falls, garages cannot be converted: A-21). Empty: both distributor nodes, drivers.offpeak, drivers.resident#2, drivers.ring_road, drivers.switchers, drivers.taxi#2, officials.enforcement#2, both owners nodes, retailers.ringside, retailers.zone#2, riders#2.

## Round 3 (5 nodes)
homebuyers#2 (price to zone homeowners' asset value, A-20), sellers.ringside_parking#2 (to garage owners' asset value, A-20), workers.commuting (wage to zone employers, A-19); empty: drivers#2, sellers.zone_parking#2.

## Answers
From the table (29 loop questions, 6 seed): A-1 to A-35 all used at least once, p as in the table. Judged: a36 (seed) "Drivers, carriers and residents expect the charge to start on 1 November 2027 as enacted." 0.9 (announcement of 4 Jan 2027, effective 1 Nov 2027); "Housing in the zone cannot be expanded within a few years." 0.9 (a built-up zone of 7 km2; no table assumption on housing supply).

## What the format could not hold
- `grants` has no premises: the K3 earmark raises bus trades and the operator's means unconditionally; A-8, A-9 and A-28 (net rise, fungibility, buses cannot be added for 14-18 months) enter only through links and a dominance fact, not as gates, and the short-run effect of A-28 cannot be placed on the grant's own effect.
- Stakes and incidence can be proposed only at the stakeholder's own node: the transit union and Ringside residents (A-15) are never reached, so they have no node.
- No variable for caseload/backlog (PAO), setup cost advanced from reserves and repaid from year-one revenue, or "funded from the gross receipts of the same charge" (only the fund-balance pair of links approximates it).
- A review every three years (no expiry) and the three-year capitalisation of asset values have no field.
- Travel time: the engine merges medium and long chains (speed gain, bus congestion) into one ambiguous consequence with horizons listed, where CR-12g would keep one per horizon.
- A dominance with p below the cut-off (A-30, 0.4) replaces the ambiguous consequence by an unreported signed one, so the ambiguity itself disappears from the reported list.
- Vehicle-days of one class as `quantity_traded` and rides demanded as `quantity_demanded` on the same class (taxis) are different variables, so A-35's substitution (more than one private car-day per ride-hail car-day) is expressible only as dominance on the `drivers` total.
- The exempt scheduled buses and the 30-minute line itself (a size threshold on duration) have no field; U1 was handled by readings, and the reshaping into under-30-minute visits as an alternative open only under U1-b.
