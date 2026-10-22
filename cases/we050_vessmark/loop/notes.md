# WE-050 Vessmark Clean Cars Act: expand-loop blind run (loop)

Branch `loop-we050_vessmark`, from bb7ea4b. Read: section 1 and the assumption table only (extracted files); nothing under `handbook/05_examples*`, no existing `cases/we050_vessmark/` file, no `tests/`. Files: `seed.json`, `proposals.json`, `answers.json`, `situation.json` (the final grown situation), `policy.txt` (section 1, passed as `--policy`). Result: DONE in 3 rounds (depth limit), 33 node visits, 57 proposals, 34 questions asked (26 answered from the assumption table, 8 judged), plus 4 table assumptions already in the seed. No `off-list:` lines.

## Seed (the policy's own facts, CR-1)

Four exchanges, each split into subclasses because the Act treats the parts differently: `e_comb` (buyers.combustion / retailers.dealers), `e_comb_w` (retailers.dealers / importers.combustion: both dealers and importers are bound by K1), `e_phev` (buyers.phev / importers.phev), `e_bev` (buyers.bev / importers.bev), `e_used_imp` (buyers.used / sellers.foreign: used cars imported from Drevland).
- `banned` k1 on e_comb and e_comb_w (s. 3), k2 on e_phev (s. 4, from 2038), each with A-2 (enforcement). `banned` k1_used on e_used_imp holds only under U1-a: `unclear` U1 gives components {U1-a: [k1_used], U1-b: []}.
- `charges` k5 (s. 8): buyer pays the general_fund, tax_revenue, with the projection variable, premise A-2. `moves` e_bev buyer with A-5 (world supply at unchanged cost: importers are price takers, 0.4% of world demand).
- `announced` k1, k2 with A-3 (dates not postponed); k5 announced with no premise (the charge is not postponable under s. 9).
- `enforcers` and `fixed_budget` (A-28) for k1, k2 at officials.enforcement (K4: budget fixed by law); `compliance` k1 for importers.combustion and retailers.dealers.
- Seed assumptions (from the table, not asked): A-2 0.95, A-3 0.7, A-5 0.8, A-28 0.8.
- Not used in the seed: K3 (saving clause: no operation, it only keeps existing cars out of CR-1), K2's exemption as such (the exemption is relative to K1; against the no-Act counterfactual only the 2038 ban is an operation).

## Round 1 (11 nodes: buyers.bev, buyers.combustion, buyers.phev, buyers.used, general_fund, importers.bev, importers.combustion, importers.phev, officials.enforcement, retailers.dealers, sellers.foreign)

38 proposals.
- buyers.combustion (the main node, 14 facts): alternatives to the banned option: keep the present car (maintenance_spending, stock_age on owners.combustion; A-4, A-19), buy used (buyers.used quantity_demanded; A-4), PHEV (A-25), new BEV (judged), used BEV (A-27, class buyers.used_bev), and under U1-b imported used cars (reading U1-b, judged); timing bring_forward (A-7); outside margin cross_border_purchases (A-14, p 0.3); links to fuel sales (A-16), to the asset value of existing cars through expected further restrictions (A-13, p 0.3), to repair demand at the long horizon (A-10); stake of motoring clubs (A-15, A-34).
- buyers.phev: to a new BEV, to used/keep, bring forward into 2036 to 2037 (three judged premises, s. 4).
- buyers.bev: PHEV as the road-charge-free alternative (judged), dominance of the ban chain on quantity_traded (A-22), incidence of k5 on buyers (A-5, the comparison of alternatives), link to charging sales (A-24), to BEV price where supply is slow (A-6, p 0.3), same_act to importers.bev.
- importers.bev: dominance (A-22), stake (A-15, A-34). importers.combustion: stop offering models (A-8, `inverse` on variety), reclassification under U1-b (A-21), shift to BEV supply (A-5). importers.phev: shift to BEV (A-5). retailers.dealers: carry_over of stock (A-9), stake.
- buyers.used: demand to price with slow supply (A-12); price to imports (A-20) and to the owner's receipt and asset value; under U1-a, to a domestic used car (judged) and to a new car (A-30). sellers.foreign: less offered under U1-a raises the used price (A-20); the import response (A-32).
- general_fund and officials.enforcement: empty lists (nothing the policy text supports beyond the seed).
- Revision before the rerun: I first wrote the import-response links (A-20 price to imports, A-32 imports to price) without a reading, and saw in the next listing that the engine showed imports rising under U1-a, where the ban stops them; I then tagged both `reading: "U1-b"` (the exempt route that reading opens). It is the only edit to an earlier round.

## Round 2 (14 nodes: 6 revisits with new effects, plus owners.combustion, buyers.used_bev, drivers.clubs, retailers.fuel, sellers.charging, sellers.repair, and revisits of dealers, importers, sellers.foreign, buyers.*)

17 proposals; most revisits got an empty list.
- buyers.used#2: dominance by the response argument (CR-12e: imports cannot reverse the price rise; A-12 partial response, A-32 cost per car does not fall).
- importers.combustion#2: link from variety to buyers.combustion (the second clause of A-8); under U1-b reclassification adds nearly-new supply to the used price (A-21).
- owners.combustion: stock_age to maintenance_spending (A-26 medium, A-31 long: the same link under `complement` and `input`, to carry two horizons); maintenance to repair demand (no premise: the same money).
- retailers.fuel: stations exit (A-17, long), staff/hours (A-18), fuel excise revenue (judged identity), number_of_sellers to asset value of existing cars and to used demand (A-10, the thinning chain), stake. sellers.charging: stake. sellers.repair: mechanics, exit (A-10), asset value (A-10).

## Round 3 (8 nodes: buyers.used#3, general_fund#2, owners.combustion#2, retailers.fuel#2, sellers.charging#2, sellers.repair#2, workers.fuel, workers.repair)

2 proposals: dominance of the scarcity chain over the thinning chain on used price_paid and on owners.combustion asset_value (A-11). Others empty: general_fund tax_revenue is ambiguous (road charge up, fuel excise down) and nothing in the figures settles it (no BEV fleet number); repair and the workers are ambiguous for the same reason (A-31 against A-10, no dominance premise).

## Answers

From the table (26 asked): A-4, A-6, A-7, A-8, A-9, A-10, A-11, A-12, A-13, A-14, A-15, A-16, A-17, A-18, A-19, A-20, A-21, A-22, A-24, A-25, A-26, A-27, A-30, A-31, A-32, A-34, each at its table p. Reused seed ones (A-2, A-3, A-5, A-28) are not asked.
Judged (8), each from section 1:
- new BEV as the nearest legal new car, 0.90 (BEV is 20% of 2025 sales and 50% on trend by 2035);
- PHEV buyers move to a new BEV after 2038, 0.90; to used/keep, 0.80 (as A-4); bring a PHEV forward into 2036-37, 0.80 (as A-7, 0.85);
- BEV buyers move to PHEV to avoid the road charge, 0.65 ($250 a year against a $6,000 price gap: only those near the margin);
- under U1-a, buy a domestic used car, 0.85; under U1-b, buy an imported used or nearly-new combustion car, 0.85 (the figures paragraph allows about 15,000 more imports a year);
- fuel excise revenue follows the volume of fuel sold, 0.98 (a rate per liter).
Table assumptions not used: A-1 (it is the counterfactual itself, not a fact the engine needs), A-23, A-29, A-33 (see below).

## What the format could not hold

1. Dated windows. A-25 (PHEV substitution in 2035 to 2037) and the 2038 PHEV ban act on the same variables in different years; likewise 2035 to 2040 against after 2040 (A-10, A-11, A-26, A-31). Only the horizons short/medium/long and the announcement windows exist. I carried A-26 and A-31 by writing the same stock_age to maintenance link twice with different relations (`complement` medium, `input` long); the A-25 and 2038 chains share the horizon, so I used different variables (quantity_demanded against quantity_traded).
2. A stock added once before the date (the rush, pre-registered stock A-9, A-29, A-33). Timing effects stay in their window and do not propagate, so the dealers' clearing sale in 2035 that holds the used price down (A-29, A-33) could not be chained; those two are unused.
3. A price gap between two options (A-23: the BEV costs more than the combustion car). An alternative carries no cost, and the displaced buyers' extra outlay has no variable to sit on; A-23 is unused.
4. Two items of one variable. General_fund tax_revenue takes the road charge (up) and the lost fuel excise (down) as opposing chains, so it comes out `ambiguous`; the `item` convention exists only for fixed budgets, not for links. The same for repair demand and workers.repair (maintenance up, fleet thinner down).
5. Dominance does not settle a per-reading sign (`dominate` skips them). The used price under U1-b needed the response-argument dominance to propagate as `increase`; the per-reading sign and the dominance of a chain that exists in only one reading are not expressible together.
6. A response closed by a reading (imports cannot answer the price when U1-a stops them) needs `reading` on each link of the response loop, written by hand.
7. The same actor class in several exchanges (dealers selling combustion, PHEV and BEV cars) had to be split by line or limited to the combustion chain; exchanges cannot be added by proposals, and a chooser must be a party of the exchange, so dealers were made the seller of e_comb and the buyer of e_comb_w in the seed.
8. The motoring clubs are not a party to any exchange, so no node of their own is reached before the stake is proposed; I put their stake at buyers.combustion (the node whose members they represent), and the node drivers.clubs then appeared in round 2.
