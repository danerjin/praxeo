# WE-019 Vestria fleet renewal rebate: expand loop, blind run

Read: section 1 and the assumption table only. `policy.md` is a copy of section 1. Result: DONE in 3 rounds, 23 node visits, 14 proposer questions (plus 8 premises used by the seed).

## Seed (CR-1, the policy's own facts)
- Exchanges: e1 new eligible cars (buyers.rebate / retailers.dealers); e_used used old cars (buyers.used / owners.eligible_cars); e_scrap old car to the dismantler (buyers.dismantlers / buyers.rebate); e_parts parts from scrapped cars (buyers.parts / sellers.dismantlers). Dismantlers are split by activity: buyers.dismantlers (take the car, get the V$150 fee) and sellers.dismantlers (barred from reselling parts), because quantity_traded is not kept per market.
- grants: k1 (V$4,000 to the buyer side of e1, payer treasury); k2_fee (V$150 to the buyer side of e_scrap).
- moves: e1 buyer side (a1, text of the table), e1 seller side (a7: supply of eligible models cannot grow in six months). incidence: sellers (a16).
- banned: k2 on e_used (a4 and j3) and on e_parts (j3): K2's crushing and no-parts-resale remove the legal trade in the scrapped cars and their parts.
- announced k1 (a5); expires k1 (j2); funded k3 by taxpayers.future (j1); compliance k1 buyers.rebate, k2 sellers.dismantlers; enforcer k4 officials.enforcement.
- From the table: a1, a4, a5, a7, a16. Judged: j1 "The additional government bonds are serviced and repaid from general revenue" 0.95 (section 1, K3: "serviced and repaid from general revenue over 10 years"); j2 "Buyers expect the rebate to end on 31 December" 0.9 (section 1: "then expires", ministers have no plan to repeat; not a contradiction of A-15 at 0.35); j3 "Dismantlers do not fake scrapping on a meaningful scale" 0.75 (complement of A-11 at 0.25).

## Round 1 (depth 1; 9 nodes)
- buyers.rebate: alt maintenance_spending (keep and repair the old car, less; A-2); timing bring_forward on quantity_traded (A-3, A-6, A-20; with announced and expires gives the three windows); links: substitute to sellers.substitutes (A-12), substitute to its own fuel bought (A-18) and on to sellers.complements (A-17), maintenance_spending to factor_owners.specific asset_value by yield (A-17), maintenance to sellers.repairs same_act (no premise), new-car purchases to sellers.repairs as input (A-8, repairs to pass the roadworthiness test), to households stock_age by substitute (A-4).
- buyers.parts: complement link to sellers.repairs (A-17). buyers.used: alt maintenance_spending (A-14). owners.eligible_cars: supply link to buyers.used price_paid (A-13) and the same price as the sellers' net_price_received (A-13). retailers.dealers: stake (A-9), asset (inventory of eligible models, A-7), input link to importers (no premise), supply_price link to importers net_price_received (A-7). sellers.dismantlers: outside margins on e_parts and e_used (A-11).
- Empty: buyers.dismantlers, officials.enforcement, taxpayers.future, treasury (nothing in section 1 or the table reaches anyone further; I chose not to add a crowding-out or interest-rate link for the bonds because no premise in the table supports it).
- Answers all from the table (A-2, A-3, A-6, A-8, A-9, A-11, A-12, A-13, A-14, A-17, A-18, A-20).

## Round 2 (depth 2; 10 nodes)
- buyers.rebate#2: dominance, resources_available_other_uses increase (A-2: the rebate is valued above the old car and the cost of buying sooner), to settle the rebate against the paperwork.
- buyers.used#2: substitute link from price_paid to sellers.foreign quantity_traded (used imports), with a judged premise (0.8) "Some used-car buyers can buy imported used cars despite the duty and the registration inspection" (section 1: "Used cars can be imported"; A-13 says only that imports cannot replace quickly).
- importers: stake (A-9); input link to sellers.foreign. sellers.substitutes: stake (A-9); alt specification_level (recertifying variants, A-10, 0.3, so unreported).
- Empty: factor_owners.specific, households, owners.eligible_cars#2, retailers.dealers#2, sellers.complements, sellers.repairs.

## Round 3 (depth 3; 4 nodes): buyers.rebate#3, importers#2, sellers.foreign, sellers.substitutes#2, all empty.

## Answers
From the table: A-2, A-3, A-6, A-8, A-9, A-10, A-11, A-12, A-13, A-14, A-17, A-18, A-20 (and in the seed a1, a4, a5, a7, a16). Judged: j1, j2, j3 (seed) and the used-import statement (round 2). A-1 and A-5 enter the seed; A-15 and A-19 were not used.

## What the format could not hold
- The budget cap (120,000 rebates, first come first served, early closure; A-6, A-15). `capped` fixes the quantity traded with price rationing, so on e1 it made price_paid and quantity_traded of rebate buyers ambiguous against the grant (tested, dropped). A-6 entered only as a premise of the timing rush. Reopening if the budget runs out (A-15, 0.35) has no slot except as a premise.
- Rationing of rebates by queue is a margin only under `held`, so first-come-first-served waiting is not derived.
- A-8 (repair a failing car to qualify) is an entry induced by the improved option, not an alternative used less; I had to write it as an input link, and it opposes the maintenance chain on sellers.repairs, which left that class ambiguous and stopped the chain from it.
- A-17 factor owners were reached by a yield link from buyers.rebate maintenance_spending, around the ambiguous sellers.repairs.
- A-18 (fuel per km) is an efficiency effect: written as a substitute link from new-car purchases to the fuel bought. A-19 (additional purchases) and a total over the three years have no slot: windows are not combined, and the dominance fact is per window.
- Variables are not kept per market, so the dismantlers had to be split by activity; used-car and new-car exchanges for one class would net.
- `qualifies` not used: the "registered since before 15 March" rule fixes the history before the scheme was announced, so no race to qualify.
- The V$150 fee and rebate are paid by the Transport Ministry; I used `treasury` as payer (K3 funds all by bonds).
- Not derived: the fleet benefit (A-18's emissions), cash-for-clunkers price effect on scrap metal, the lender side of the bonds.
