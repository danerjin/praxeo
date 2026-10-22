# WE-015 Port Halden taxi license cap: expand-loop blind run (notes)

Branch `loop-we015_porthalden` from 57f997f. Read only `WE-015_section1.md`, `WE-015_assumptions.txt` and the permitted code and
worked situations (we001, we009, we013, and for `capped`/`unclear` style also we016 and we028 loop folders). I did not open
`handbook/05_examples*` or `tests/`. One slip: my first `ls` of `cases/we015_porthalden/` listed that folder, so I saw the file
names there (answers.json, out_of_sample.md, policy.txt, record.json, sample_run); I opened none of them.

Result: DONE in 3 rounds, 14 questions, 16 node visits (7 + 7 + 2). No `off-list:` lines. `engine_output.txt` has the final output.

## Seed (policy's own facts, CR-1)

- Exchanges: `e_taxi` (street hail and ranks: customers.taxi buy from drivers.licensed; unsatisfied: customers.taxi and
  drivers.prospective, the would-be drivers the cap shuts out; criteria group wait_time, side_payments,
  allocation_by_non_price_criteria), `e_medallion` (drivers.prospective buy medallions from licensees), `e_private`
  (customers.booked, drivers.private_hire), `e_app` (short-notice app rides: customers.taxi, drivers.private_hire).
- `held` r1 on `e_taxi` (meter rate, direction below), premises a1 (binding) and a2 (enforcement). The meter is a rule in force that
  the cap makes bind, so it is `held` rather than `fixed`: `fixed` only acts when a charge falls on the same exchange. I left both
  price variables of `e_taxi` empty so the engine does not sign a fare change (the fare is unchanged); see "format" below.
- `capped` k1 on `e_taxi`: holders `licensees`, `wider_price: true` (the council sets the fare, so the medallion's lease price rations,
  CR-6 0.7). Premises a1 and j1.
- `charges`: k1_fee (2% transfer fee on `e_medallion`, ad valorem so `unit`), k2 ($300 private-hire permit on `e_private`, `operating`),
  k2_a (the same permit on `e_app`, only under U1-a).
- `qualifies` k1 (drivers.prospective, applications; a4): applicants rush to hold a license on the effective date. `announced` k1
  (no premise: the text says passage was widely expected). `means` k1 licensees in: medallions are given to existing holders (CR-7c).
- `enforcers` k3 officials.enforcement; `funded` k3 taxpayers (a16, budget rises); `fixed_budget` k3 (j2, the complement of a16).
- `unclear` U1 with components: U1-a has k2_a (the permit applies to app short-notice service), U1-b has k1_b (a `capped` fact on `e_app`
  carrying `reading: "U1-b"`, holders licensees, `wider_price: false` because app fares are agreed at booking).

Seed premises from the table: a1 = A-1, a2 = A-2, a4 = A-4, a16 = A-16 (text and p as in the table). Judged:
j1 "The cap on licenses is enforced against unlicensed street-hail and rank service." p 0.8 (K3 gives 12 inspectors, a $1,000 fine and
impounding; A-7 says some goes undetected). j2 "The 12 inspectors are moved from other duties rather than the Office's budget rising." p 0.45,
the complement of A-16 (1 - 0.55).

## Round 1 (depth 1): 7 nodes

- `customers.taxi` (excess_demand up, quantity_traded down, criteria group up). Proposed: alternative quantity_substitute and a
  substitute link to customers.booked quantity_demanded (A-10); criterion margins wait_time (A-18), allocation_by_non_price_criteria
  (A-5), side_payments (A-7); an `adjust` margin on seller-controlled quality_per_unit (A-6). Sources: the meter rate sentence (R1), K2,
  "Driver and vehicle standards unchanged".
- `drivers.licensed` (quantity_traded down): nothing in section 1 or the table bears on it directly; empty list.
- `drivers.private_hire` (number_of_sellers down from the permit, resources down): outside margins informal_activity on `e_private` (A-7)
  and reclassification on `e_taxi` (street hails passed off as bookings, A-8).
- `drivers.prospective` (applications up in the window, quantity_traded down): alternative entry_rate of private hire (A-15, K2);
  the same alternative under U1-a only, as the exempt form for app short-notice work (A-15, `reading` U1-a); outside margin
  informal_activity on `e_taxi` (A-7, the $1,000 fine); outside margin informal_activity on `e_app` under U1-b only (A-8); a `yield`
  link from their lost trades to their earnings (A-17).
- `licensees` (asset_value up, right_lease_price up, quantity_traded down, resources up): a stake in k1 (A-9); a `cost` link from the lease
  price to drivers.licensed net_price_received (lessee drivers, judged premise); a `yield` link from the lease price to asset_value (A-3,
  CR-7c: value reflects the expected yield).
- `officials.enforcement`: `paid_into` and `paid_from` links to its own fund_balance (the text says it is funded from the general budget
  and license fees; CR-8 1.0 two items of one budget).
- `taxpayers`: empty list.

## Round 2 (depth 2): 7 nodes, all revisits except customers.booked

- `customers.booked` (quantity_demanded up): `same_act` link to drivers.private_hire quantity_traded (A-15, supply is there to serve it);
  `supply_price` link to its own price_paid, short horizon, premise judged p 0.35 (private-hire supply cannot expand within the first
  months). It stays below the cutoff and is not reported; entry (A-15) is judged fast because the permit is uncapped.
- `customers.taxi#2`: a `dominance` fact on wait_time, kind `response`, premise judged p 0.85 (disguised hails relieve only part of the
  shortage). Needed because the two evasion margins (rounds 2 links below) lower wait_time against the first-come chain (CR-12e).
- `drivers.private_hire#2`: `supply` link entry_rate to customers.booked price_paid (A-15); `supply` link reclassification to
  customers.taxi wait_time (A-8).
- `drivers.prospective#2`: `supply` link informal_activity to customers.taxi wait_time (A-7).
- `drivers.licensed#2`, `licensees#2`, `officials.enforcement#2`: empty.

## Round 3 (depth 3): 2 nodes

- `drivers.private_hire#3` (quantity_traded up): `substitute` link, long horizon, to asset_value of a subclass `licensees.bought_near_peak`
  (A-12). I used a subclass because CR-7c gives the gain to holders at creation and the later fall to those who bought near the peak;
  put on `licensees` itself it made asset_value `ambiguous` (the first run did that), since the engine merges a short effect and a long
  one into one consequence.
- `customers.booked#2` (price_paid down): empty.

## Answers

From the table (p as given): A-10 0.8, A-18 0.9, A-5 0.75, A-7 0.75, A-6 0.8, A-8 0.6, A-15 0.75, A-17 0.6, A-9 0.85, A-3 0.75, A-12 0.6
(wording identical to the table, so no matching problem), plus the seed premises a1, a2, a4, a16.
Judged (3 loop questions and 2 seed premises):
- "Many licensed cabs are driven by lessees who pay the medallion holder, rather than by the holders themselves." 0.7 (section 1: medallions "may be sold or leased").
- "Private-hire supply cannot expand within the first months to meet the added bookings." 0.35 (the permit is uncapped and A-15 says shut-out drivers do enter).
- "Disguised street-hail service by private-hire cars relieves only part of the shortage of cabs." 0.85 (K2 bars street hails, so evasion is risky; the fleet shortage persists).
- j1 0.8 and j2 0.45 in the seed, as above.

## What the format could not hold

- A price that is a rule already in force and starts to bind only because another component fixes the quantity. `held` with price
  variables would sign the fare down (it does not move); `capped` with a free price would sign the fare up. I used `held` with no price
  variables plus `capped` with `wider_price`, which gives the right waiting/side-payment/lease-price margins but means the fare itself is
  not a variable in the record. `held` also marks customers.taxi as "favored", so I proposed no `alternatives` for that class (they would
  have come out as both increase and decrease); the substitution to transit and private hire is a link instead.
- A-13 (the council raises the meter above its index after lobbying): no relation carries a political response from lobbying_effort to a price.
  Lobbying is recorded (stake) and stops there.
- A-14 (licenses obtained in the window are put into service in the first year): effects inside a timing window do not propagate, so the
  rise in applications cannot feed the fleet size or the cap level; the cap is "the number outstanding on the effective date", which the
  `qualifies` fact only partly expresses.
- Holders at creation against buyers later (A-3, A-12): needs a subclass, and the time path (windfall now, fall later) is two horizons of
  one asset; the engine merges horizons into one consequence unless the actor classes differ.
- Medallion price in the street-hail market is the lease price (wider_price is a stretch: the fare is set by the council, not a wider market).
- Opposing chains on number_of_sellers of private hire: the permit lowers it (operating charge), entry raises it, but I linked entry to
  entry_rate and price, not to the stock, so the record reports only the decrease; the permit's decrease is doubtful as a consequence
  against the counterfactual, where private hire was not charged either way.
- The readings: the record sets U1-a/U1-b through the permit (k2_a) and the cap on app service (k1_b); the only reported reading
  difference is drivers.private_hire quantity_supplied (U1-a increase, U1-b none).
- The 2% fee's incidence and the $400 fee are not in the loop (no premise compares alternatives; the $400 fee is unchanged).
- No class split of drivers.licensed into owner-drivers and lessees beyond the lease-cost link.
