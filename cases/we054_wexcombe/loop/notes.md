# WE-054 expand loop, blind run (branch loop-we054_wexcombe, base c2e834f)

Read only the section 1 record and the assumption table. Final engine output: `DONE in 3 rounds, 23 questions`, no `off-list:` lines.
Node visits: 13 (round 1), 21 (round 2), 4 (round 3) = 38. Questions: 23 asked by the loop; 21 answered from the table,
2 judged. The seed carries 9 more premises (a1, a2, a4, a5, a13, a28, a29, a31, a33), all from the table. Proposals and
answers were written in one pass per round, so the CLI never printed questions (the answers were already in answers.json
when each round was run). `answerlog.json` lists every statement with its source (table id or judged).

## Seed (policy's own facts only)
- Exchanges (airline-customer markets, not airline-airport): `e_day` (passengers / airlines, unsatisfied sellers = would-be entrants),
  `e_slot` (slot lessees / slot holders, price in `right_lease_price`), `e_nint`, `e_ncargo` (shippers / integrator, other cargo),
  `e_npax` (night passengers / night airlines), `e_late` (passengers / airlines on late-running flights).
- K1 `banned` on the three night exchanges (premise a2, enforcement); K1 on late flights is its own component `k1_late`, `banned` on `e_late`,
  and the only component listed under reading U1-b (U1-a lists none): the ordinary-delay dispensation is the U1 question.
- K2 `capped` on `e_day`, holders = airlines, premises a1 (cap binds: A-1) and a2. `wider_price` false: fares at WXI rise (A-26 speaks of a
  scarcity premium per seat); the slot lease price comes from a link, not from `wider_price`.
- K3 `qualifies` for airlines (a5, A-5), would-be entrants (a29, A-29) and night operators (a28, A-28, below the cut-off, so unreported).
- K4 `terms` better for both sides of `e_slot` (a4, A-4). K5 `qualifies` for the three night-operator classes (a31, A-31).
- K6: `enforcers` (officials.enforcement), `funded` by airlines (a13, a33). `compliance` for K1, K1-late, K2. `announced` for K1 and K2 (draft 2 March 2026, adopted
  15 September 2026, binding 31 October 2027), no premise.
- Not seeded: `held`, `charges`, `grants`, `fixed`, `moves`, `thresholds`, `expires` (none in the policy).

## Round 1 (13 nodes)
All proposals rest on a sentence of section 1 or an assumption statement, quoted in `source`.
- customers.passengers: alternative Pellham (`cross_border_purchases`, A-11); links to Pellham flights (A-34), Pellham fares (`supply_price`, A-19),
  concessions (A-21) and airport employment (A-25). customers.passengers_night / _late: Pellham alternative (A-11; late one tagged U1-b).
- sellers.airlines: slot value to lease price for holders and lessees (`same_act`, A-4); larger aircraft (`yield` from net price, then `supply` to fares: A-8);
  asset (A-3); stakes (A-15) in K2 and K3.
- sellers.prospective: Pellham flights (A-34), buying or leasing slots (A-4), stake in K5 (A-15), fewer movements to charge per movement (A-13).
- Night operators (integrator, other cargo, night passenger airlines): shoulder-hour flights on leased slots (A-7), stake (A-15, A-32), noise to contour home values
  (`substitute`, A-22), fewer movements to cost per movement (`supply`, A-13). Integrator: Pellham (A-6), sort facility asset (A-16), jobs (A-25),
  cut-offs (A-17), parcel price (`supply`, A-18). Other cargo: Pellham (A-6). Night passengers: Pellham flights (A-34) and, tagged U1-a, flights scheduled
  just before 23:00 (A-24, the exempt alternative that reading opens).
- sellers.airlines_late: diversion (U1-b, A-34), flights moved earlier (U1-b, A-23).
- officials.enforcement: enforcement cost to airlines' cost per movement (A-13, A-33).
- Empty: customers.shippers, sellers.slot_holders; buyers.airlines gave one link (slot buyers fly shoulder hours, A-7).

## Round 2 (21 nodes)
- customers.passengers#2: price_paid and cross_border_purchases were `ambiguous` (the larger-aircraft `supply` chain against the cap); proposed dominance,
  kind `response`, premises A-9 and A-35 (CR-12e 1.0: partial response, constant or rising cost).
- Night operators #2: workers' housing demand as a second chain on contour home values (`complement`, A-25 with A-12), since a group (employment, hours) cannot be a link source.
- Pellham cargo/integrator: noise (A-22) against hub workers' housing demand (A-12 with a judged Pellham employment statement).
- workers.night_sort: part of workers.airport. homeowners.contour_wxi: stake in K1 (A-15). The rest: empty.

## Round 3 (4 nodes)
- homeowners.contour_pellham asset_value `ambiguous`: dominance decrease on A-20 (table).
- homeowners.contour_wxi asset_value `ambiguous`: dominance increase on a judged statement (0.7): the discount from removed night noise exceeds lost demand from fewer
  airport workers (9,000 homes in the contour against 900 night-sort jobs, 30% of airport workers within 8 km; A-22 0.85 against A-12 0.6).
- customers.passengers#3, sellers.airlines_pellham#2: empty.

## Judged answers (2)
1. "Employment and hours at Pellham follow the movements and the night sort that move there." 0.75, A-25 (0.8) applied to Pellham.
2. The WXI contour dominance statement above, 0.7.

## Could the format hold it? Gaps
- Fines ($50,000 per curfew movement, $10,000 per daytime movement without a slot) attach to breaking the rule, not to a legal trade: no `charge` fits,
  so penalty receipts (A-33's comparison) and A-14 (operators sometimes operate and pay) are not recorded. A-14 could be an `outside` margin; I left it out as it
  needs a node to propose it and none reached it.
- The airport appears in no exchange (a seller of movements): its lost charge revenue, its concession income and its charge per movement only exist as the airlines' `full_cost_per_unit`.
  Seat price cannot be derived separately from movement charge (A-26's comparison of the two is not expressible except as a dominance on one variable).
- A group (employment, hours) cannot be the source of a link, so the A-12 chain from jobs to home values was shortened to movements -> home values with two premises.
- Premises cannot be negated: A-30 (entrants keep operating rather than lease out, 0.4) and A-34 vs A-19 as opposite premises could not be written.
- A reading that adds an exempt alternative works only where a component still applies to the chooser (k1 for night operators under U1-a); there is
  no way to record that under U1-a a late-flight exchange is simply untouched.
- No `moves` link between the slot lease price and fares or asset value: both were joined by `same_act`, which carries sign only.
- A-27 (some night services are neither moved nor shifted), A-10 (airlines differ in slot value), A-26 and A-31's size (priority claim has value) have no slot
  in the format; A-28 (night operators earn daytime history) is in the seed but its p (0.35) is below the cut-off. A-19 (Pellham fares rise, 0.35) is likewise unreported.
- Hourly retiming within the 34-an-hour limit and the 380 count versus the 409 counterfactual are figures with nowhere to sit.
- Variable names stretched: `cross_border_purchases` stands for passengers using Pellham, `unit_size` for aircraft size,
  `quantity_traded` on `sellers.slot_holders` for slot sales.
