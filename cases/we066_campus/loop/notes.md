# WE-066 St Aldric's College e-bike rule: blind expand-loop run

Inputs read: section 1 of WE-066 and the assumption table only (statements, type, p). Nothing under handbook/05_examples*, tests/ or any earlier cases/we066_campus file was opened. Files: `seed.json`, `proposals.json`, `answers.json`, `situation.json` (final), `engine_output.txt` (final consequence list), `policy.txt` (section 1, the text passed to `--policy`).

Result: DONE in 3 rounds, 39 node visits (5 + 13 + 21), 68 proposed facts (21 of the 39 visits got an empty list), 44 questions answered by the decider (plus 7 seed premises). No `off-list:` lines in the final run.

## Seed (the policy's own facts)

The rule is a private rule-maker changing the bundle it sells its members, so it is `terms` (CR-1 op 3 without a payment, CR-5 1.2), not `banned` (nothing is traded that the rule stops) and not `held`/`charges` (no price or payment).

- Exchanges: `e_bundle_th` (students bound under both readings: `members.current.throttle` buys the schooling bundle from `rule_maker.private`), `e_bundle_pa` (`members.current.pedal_assist`, bound only under U1-a) and `e_bundle_oth` (`members.current.non_riders`, the other families). Price variables price_paid / net_price_received (the fee), no `moves` (the fee is $18,600 for the year; I did not assert that it moves).
- `terms`: `k1_throttle` (worse, a1 enforcement), `k1_pedal_assist` (worse, a1; U1-a only), `k1_campus_a` / `k1_campus_b` (better for the families who prefer a campus without e-bikes: a21 under U1-a, a41 under U1-b; each with a1). This is CR-1 for every actor class the rule reaches; I recorded it in the seed because A-21 and A-41 are about the rule's effect on choice of school, not about a response.
- `unclear` U1 (section 2 definition): U1-a lists `k1_pedal_assist` and `k1_campus_a`; U1-b lists `k1_campus_b`. `k1_throttle` is listed under neither, so it applies under both (80 riders).
- `margins` (exchange's own outside trade): `outside` legal_breach for each rider class (A-10, p 0.65); the pedal-assist one carries `reading: U1-a`.
- `compliance` (k1 for each rider class), `enforcers` (k2: `workers.school_staff`, gate duty, section 5), `fixed_budget` (k2: A-20, gate duty is drawn from other duties), `funded` (k2 paid by `members.current` through fees: A-31, p 0.25, so it is not reported).
- `announced` for both k1 components (letter of 21 January 2027, effective 19 April 2027), premise a_ann "Families expect the rule to take effect on 19 April 2027." (judged, 0.95).
- Not in the seed, on purpose: no `fixed` (the fee and the coach pass price are fixed, but `fixed` only acts together with a charge on that exchange, and there is none), no `thresholds`, `qualifies`, `expires` (no expiry; June 2028 is a review), `incidence` (no charge or grant), `dominance`.
- Seed premises, all from the table: A-1 (0.8), A-10 (0.65), A-20 (0.85), A-31 (0.25), A-21 (0.55), A-41 (0.5). Judged: a_ann (0.95).

## Round 1 (5 nodes)

Nodes: members.current.throttle, members.current.pedal_assist, members.current.non_riders, rule_maker.private, workers.school_staff.

- throttle and pedal_assist (the latter with `reading: U1-a` on every fact), each:
  - alternatives (CR-4) to riding on grounds, one fact per mode of the February poll, each on a table premise: pedal bicycle (A-2), coach (A-3, measured as `quantity_demanded` of `customers.coach`), route 14 (A-4, `customers.route14`), driven (A-5, `drivers.school_run` trips), e-scooter (A-6), keep riding and park off school land (A-7, `riders.off_site` trips), walking (poll, 5%; judged 0.6, not in the table), sell the bike (A-12, `sellers.students` quantity_supplied), change school (A-22, `rival_providers` membership). Throttle only, `reading: U1-b`: remove the throttle or swap (A-11, `reclassification`, from "the throttle unplugs; Spokewright removes one for $40").
  - stakes (lobbying) with A-18 and A-19 (the contest would have continued without the rule, CR-4 1.0), `timing` bring_forward on quantity_supplied (A-12, sells before 19 April, with the seed `announced`), `assets` on the e-bike (A-27, expected to last to the June 2028 review), and a `complement` link from the bundle's quantity_traded to `buyers.prospective` quantity_demanded (A-14).
- non_riders: lobbying stakes (A-18, A-19) per reading (Safe Lanes petition).
- rule_maker.private, workers.school_staff: empty. The private rule-maker's gain is safety, out of scope (CR-2 1.2; "In scope: no"), and its ambiguous quantity_traded (fewer riders against more satisfied families) is left as the engine derives it.
- Answers: all table (A-2 0.8, A-3 0.8, A-4 0.6, A-5 0.8, A-6 0.6, A-7 0.85, A-12 0.7, A-22 0.55, A-11 0.7, A-18 0.85, A-19 0.75, A-27 0.7, A-14 0.8) except walking (judged 0.6: 5% in the poll, about 13 riders, but 6 km). I reworded A-3, A-4, A-6 to stand alone ("Some e-bike riders switch to ...") and took the same p.

## Round 2 (13 nodes)

Nodes: buyers.prospective, customers.coach, customers.route14, drivers.school_run, members.current.non_riders#2, pedal_assist#2, throttle#2, riders.e_scooter, riders.off_site, riders.pedal_bicycle, riders.walking, rival_providers, sellers.students.

- buyers.prospective: `same_act` to `retailers.ebikes` quantity_traded (the shops lose the sales), premise "Some of the e-bikes students would have bought are bought from the two local shops." (judged 0.9: 40 of 60 from the shops).
- customers.coach: sales to `contractors.coach` within the free seats (judged "find a free seat", 0.85, 143 free seats); `supply_price` to a group wait_time / allocation_by_non_price_criteria on A-8 (0.6) and A-9 (0.7) (the fixed pass price rations by the published priority and the waiting list); `input` to the contractor's quantity_supplied on A-34 (0.6); `supply_price` to price_paid on A-34 and A-32 (0.45, so not reported); `substitute` to resources_available_other_uses on A-28 (0.85).
- customers.route14: sales to `sellers.route14` (judged "seats free", 0.85: route 14 runs at about 60% of peak); sales through Dunnock News (A-42, `retailers.news_agent`); outlay (A-28).
- drivers.school_run: `supply_price` to its own wait_time on A-23 (0.85) and A-24 (0.65); the same pressure on `contractors.coach` wait_time on A-23 and A-36 (0.75); outlay (A-28).
- throttle#2: `same_act` from reclassification to `repair_shops` quantity_traded (A-11, U1-b). pedal_assist#2, non_riders#2: empty.
- riders.pedal_bicycle, e_scooter: complement to the shops' sales (A-29 0.7; e-scooter version judged 0.6), `supply_price` to price_paid on A-37 (0.6), travel_time up on A-25 (0.8) for pedal bicycle and walking.
- riders.off_site: excess_demand for the free stands (A-15 0.8), legal_breach by locking to street furniture (A-17 0.7), council enforcement_cost (A-43 0.55), rentals of driveway space (A-16 0.55) and of Spokewright's yard (A-45 0.6), purchases at the parade (A-26 0.6), canteen sales down (A-30 0.4, not reported), footway crowding for `neighbors` (A-35 0.6), longer trip (A-25).
- sellers.students: `supply` to its own net_price_received and to `buyers.used_ebikes` price_paid (A-13 0.65). rival_providers: empty.
- Answers: table except S_SHOP_BUY, S_SEAT, S_R14SEAT and the e-scooter shop premise (judged from section 1's figures, 0.9, 0.85, 0.85, 0.6).

## Round 3 (21 nodes; the depth limit)

- buyers.used_ebikes (price down): alternatives that fall as buyers move to used e-bikes: new pedal bicycles and new e-scooters (A-44, 0.5), new e-bikes and throttle-removal work (A-40, 0.6, `reading: U1-b`); `own_price` to staff e-bike trips (A-38, 0.35, not reported).
- contractors.coach: delay passes to the riders' travel_time (A-36). drivers.school_run#2: longer queue and fewer staff car trips (A-33, 0.5). sellers.driveway_space: `yield` to asset_value (A-27). sellers.students#2: `timing` bring_forward of leavers' and upgraders' sales (A-39, 0.6).
- All other round-3 nodes: empty (the chain stops there at depth 3, or nothing in section 1 or the table continues it).
- Answers: all table (A-44, A-38, A-40, A-33, A-39).

## Decider summary

44 questions in `answers.json`: 39 from the table (the A-numbers named in the rounds above; A-3, A-4, A-6 and a few others reworded to stand alone, same p), 5 judged (walking, shops buying e-bikes, free coach seat, route 14 seats, e-scooter shop purchases). Seed: A-1, A-10, A-20, A-21, A-31, A-41 from the table; a_ann judged.

## What the format could not hold

1. A price fixed by a contract already in force (the $420 coach pass) with excess demand from a policy elsewhere: `fixed` acts only with a charge on that exchange, and margins/criteria only fire under a `held` price. I used a `supply_price` link to a group of wait_time and allocation_by_non_price_criteria instead; the sign is right but the held price, the waiting list and the published priority rule are not represented as such.
2. Shared facilities (the drop-off loop and Quarry Lane queue, the coaches delayed on the same road, the footway): the link relations have no `shared_facility`; I used `supply_price` (capacity that does not respond in the period) and `same_act`, which makes these chains Tier B instead of Tier C. A-35 (footways) is the clearest case.
3. A mode switch caused by a cost that is a quantity (a longer queue making staff drive less and ride more, A-33): no relation turns wait_time into a shift to a substitute mode. I recorded `drivers.staff` trips down (`substitute`) and could not reach staff e-bike trips up.
4. Extra outlay of families who switch (A-28) fits no relation; I used `substitute` from the quantity demanded to resources_available_other_uses, which gives the right sign only by the opposite-direction rule.
5. Penalties that take time (detentions, a confiscated bike held until a parent collects) are time costs (CR-8 1.2) with no fact type; `compliance` gives compliance_cost and the fall in resources only for the bound students.
6. A rule that changes where an activity may take place while leaving the trade itself legal: there is no exchange being banned, so the exchange is the membership bundle and "quantity_traded" means membership of the school, not rides.
7. A premise that selects among competing readings by who is bound (U1) is carried by splitting classes (`members.current.throttle` / `pedal_assist`) and component lists; the sign of a class under only one reading prints as `ambiguous` in the plain output, with the sign per reading inside the engine result.
8. Opposing chains (retailers.pedal_bicycles and retailers.escooters up through switching, down through A-44; rule_maker.private down through riders leaving, up through A-21) stay `ambiguous` because the table gives no dominance premise and section 1's figures do not settle it by arithmetic.
9. The aim (safety) is out of scope, so nothing records why the board adopted the rule; the stake of the board itself is not proposed.
10. Stocks and one-off seasonal flows (40 used e-bikes sold each July to September) can be put only as bring_forward timing, not as a change in the size of the used market.
11. The `members.current` funding of gate duty (A-31) is in the seed but falls below the cut-off, so its fee effect is not reported; the alternative sources (other budget uses, owners' return) have no fact type.
