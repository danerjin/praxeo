# WE-046 Calderford central zone charge: expand loop, blind run

Inputs read: section 1 of the policy record and the assumption table (ID | Statement | Type | p), nothing else about the example. Names come from `--vocab --exclude WE-046`; the runs print no `off-list:` lines.

Result: DONE in 3 rounds (the depth limit), 41 node visits (14 + 18 + 9), 25 premise questions beyond the 5 premises used by the seed. Every answer comes from the assumption table (no judged answers). Table ids are in brackets below.

## Seed (the policy's own facts, CR-1)

The charge falls on a vehicle-day, not on a trade, so I made one exchange per kind of trip it taxes, with the party that gets the trip's other side.
- e_shop: customers.drivers buy from retailers.zone (K1, payer buyer). e_res: drivers.resident buy from retailers.zone (K2, the $1.50 rate, payer buyer). e_commute: employers.zone buy labour from workers.car_commuters (K1, payer seller, seller price wage_rate). e_delivery: retailers.zone buy from distributors.longer_visits (K1, payer seller). e_short: retailers.zone buy from distributors.short_visits (component k1_short, payer seller). e_ride: customers.ride_hail buy from drivers.taxi (K1, payer seller). e_bus: riders buy from sellers.transit.
- Charges: receiver officials.revenue, `tax_revenue`, projection variable set (the policy gives a static revenue and a lower projected one). Basis unit (per vehicle-day). No `quantity_premises` (the receiver is the city, outside the exchange).
- U1 (short visits): `unclear` with U1-a: k1_short applies, U1-b: nothing extra. The short-visit exchange has its own component so only reading U1-a charges it. Exempt buses and emergency vehicles: not modelled (no exchange).
- K3 earmark: a grant `k3` to the seller side of e_bus, payer officials.revenue ("applied to bus services"). Existing fares stay: no `moves` on e_bus (a `fixed` fact would do nothing, the engine only reads it on a charged exchange).
- K4: enforcers k1/k2 -> officials.enforcement (CCO); officials.adjudication (PAO) as enforcer of k1 with `fixed_budget` [A-24 "PAO's budget is not raised..."]. Not funded by taxpayers: the CCO is paid from gross revenue and the $70m set-up is repaid from the first year, so no outside payer.
- `announced` k1 with no premise (enacted 4 Jan 2027, effective 1 Nov 2027). No timing fact was proposed, so it changes nothing.
- `moves`: e_shop buyer [A-1 binding, A-2 enforced] (price paid rises); e_commute seller [A-19] (net wage falls: workers who cannot switch cheaply); e_delivery and e_short buyer [A-14] (zone businesses have worse alternatives than carriers); e_ride buyer with no premise (the text: fares are set by platforms, no regulation).
- Nothing for held, capped, banned, thresholds, qualifies, expires (no expiry; the three-year review is not an expiry), fixed, terms, backstops, discretion, means, transfers.

## Round 1 (14 nodes)

Proposals, with the sentence or assumption each rests on:
- customers.drivers: alternatives (CR-4) to a car day in the zone, component k1: bus/tram (riders) [A-5, A-4]; Ringside garages [A-5]; shop in Ringside/Merrowdale (retailers.neighbors) [A-7]; ride-hail (customers.ride_hail) [A-25]; move trips outside 7:00-19:00 (customers.off_hours, `trips`) [A-17]; evade (`legal_breach`) [A-16]; register at a zone address (drivers.resident, `reclassification`) [A-11]; divert round the zone (drivers.through, `trips`) [A-18]. Link complement to zone garages' demand (sellers.garages_zone) from the 31,000 spaces.
- customers.ride_hail: link supply_price to drivers.taxi net_price_received [A-26].
- distributors.longer_visits: consolidate into fewer van-days (`transaction_size`) [A-32]; the exempt alternative under U1-b (reshape rounds into short visits, `reclassification`, `reading: U1-b`) [A-13]; incidence on e_delivery, buyer side [A-14]; stake in k1 [A-15].
- distributors.short_visits: consolidate [A-32]; stake [A-15].
- drivers.resident: leave the zone / give up the car (`relocation_out_of_area`), component k2 [A-33].
- employers.zone and retailers.zone: relocate premises out of the zone [A-14, which names "premises elsewhere" as the zone businesses' alternative].
- officials.enforcement: link paid_from the revenue fund (CCO cost comes out of the revenue before the earmark). officials.revenue: link paid_into the fund; link substitute earmark outlay -> general-fund outlay [A-9]; dominance on fund_balance, kind arithmetic ($230-260m net against a $45m cost).
- retailers.zone: asset (zone property owners, tied to e_shop seller) [A-20]; stake [A-15]; dominance for quantity_traded decrease [A-30].
- riders: link complement to zone shop sales [A-10]; link same_act to switchers' travel_time [A-23].
- sellers.transit: link resources -> quantity_supplied at long horizon [A-28]; link quantity_supplied -> workers.transit employment,hours_worked; dominance resources increase [A-8].
- workers.car_commuters: bus/tram [A-5, A-4]; Ringside garages [A-5]; move into the zone (drivers.resident `membership`) [A-27]; evade [A-16].
- Empty: drivers.taxi (nothing the text gives that the seed does not), officials.adjudication.

## Round 2 (18 nodes)

Nodes were new classes (customers.off_hours, drivers.through, general_fund, owners.property_zone, retailers.neighbors, sellers.garages_ringside, sellers.garages_zone, workers.transit) and revisits.
- drivers.through: link same_act to its travel_time [A-31]. general_fund: link paid_into sellers.transit resources (the cut in support; its premise A-9 is already on the upstream link).
- sellers.garages_ringside: supply_price to its own price received [A-6]. sellers.garages_zone: supply_price to its price received [A-21, cannot be converted], then yield to owners.garages_zone asset_value [A-20].
- workers.transit: stake in k3 [A-15, the transit union].
- customers.drivers#2: link same_act from legal_breach to officials.revenue non_tax_receipts [A-2, penalties are collected]. Parts: customers.drivers, drivers.resident, drivers.taxi, distributors (both), workers.car_commuters are parts of the whole `drivers` (vehicle-days in the zone; the text counts 118,000 vehicles).
- customers.ride_hail#2: link same_act to drivers.taxi quantity_traded (the ride bought is the ride sold).
- Empty: customers.off_hours, owners.property_zone, retailers.neighbors, officials.revenue#2, retailers.zone#2, sellers.transit#2.

## Round 3 (9 nodes)

- drivers (the whole): dominance quantity_traded decrease, kind empirical [A-35: a ride-hail car-day carries more than one private car-day]. This settles the total of vehicle-days, which would otherwise be ambiguous (taxis: charge down, switching up).
- sellers.transit#3: dominance quantity_supplied increase [A-8]. sellers.garages_ringside#2: yield to owners.garages_ringside asset_value [A-20].
- Empty: drivers.taxi#3, drivers.through#2, officials.revenue#3, owners.garages_zone, sellers.garages_zone#2, workers.transit#2.

## Answers

All from the table, none judged: A-5 .9, A-4 .8, A-7 .7, A-25 .6, A-17 .7, A-16 .6, A-11 .6, A-18 .85, A-26 .6, A-32 .7, A-13 .7, A-15 .85, A-33 .6, A-9 .7, A-20 .75, A-30 .4, A-10 .55, A-23 .8, A-28 .8, A-8 .7, A-27 .55, A-31 .75, A-6 .75, A-21 .8, A-35 .8. Seed premises: A-1 .95, A-2 .85, A-14 .65, A-19 .55, A-24 .8.
Unused table rows: A-3, A-12, A-22, A-29, A-34 (see below).

## What the format could not hold

1. Road speed (A-3, A-34, the 4 minutes saved, the 40 minutes for a van, bus crowding and bus speed, A-29). The relation list has no shared_facility; the nearest (complement, same_act) would give the wrong meaning. So fewer vehicles raising speed, and the claim that the time saved is worth much less than $15, appear only as premise A-4 on the switching alternatives. A-3 and A-34 are unused, and the 8-minute gain to car commuters is not derived.
2. A charge cannot carry its binding and enforcement premises (A-1, A-2). Only `moves` takes them (the price effect); the fall in trades is unconditional. Same for the grant: bus service rises at once in the engine (quantity_traded of riders and transit, short), while A-28 (no new buses for 14-18 months) can only sit on a separate long-horizon link, which leaves the short-horizon rise standing. No `fixed` or fare effect for the unchanged fares either.
3. The charge is on a vehicle-day, not a trade. I had to make seller classes per kind of trip; the resident exchange (e_res) has an arbitrary seller (retailers.zone), and through traffic and parking customers are in no exchange: the diversion alternative (A-18) has chooser customers.drivers though the actors are through drivers.
4. A dominance premise below the cut-off (A-30, p .4) removes the consequence from the report (the retailers.zone quantity_traded line prints "-") rather than leaving it reported as ambiguous. Without the dominance fact it would be reported ambiguous (A-10 .55 gives the opposing chain).
5. Groups (workers.transit employment, hours) stay ambiguous, as dominance does not apply to groups.
6. Residents' misregistration and evasion reduce the revenue against the static projection, but there is no link from `reclassification` or `legal_breach` to tax_revenue that does not misuse a relation; I linked only to fines (non_tax_receipts). The PAO appears with both signs on enforcement_cost (appeals up, other work down); the net caseload (9,000 more, 2,800 fewer) and the parking-ticket fall cannot be given separately. A-22 (residents who would have moved anyway) needs a counterfactual baseline and was left out; A-12 (deliveries that cannot be done in 30 minutes) has no place except as the reason there is a longer-visits class.
7. The charge hours (7:00-19:00) and the ten months between enactment and start are held only as the off-hours alternative and a bare `announced` fact; no stock is timed.
