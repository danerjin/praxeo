# WE-039 Sorrel Basin: expand-loop blind run (notes)

Inputs read: handbook/04a_core_rules.md, praxeo/core/{core.lp,situation.py,expand.py}, cases we001/we009/we013-style records (and the seed of we014/we028 for how a cap with holders is recorded), the policy section 1 and the assumption table only. Process slip: while looking for how `resource_stock` is used I ran one recursive grep over the repository root; its output was filtered to non-example paths, but that grep did cover handbook/05_examples and tests/ (one filename under tests/ was printed; nothing from either was opened or read). Final result: DONE in 3 rounds, 23 node visits, 26 questions (20 from the table, 6 judged).

## Seed (policy's own facts, CR-1)
- Exchanges (crops are sold in national markets, so the cap is a quantity rule on a good priced in a wider market, CR-6 0.7): `e_south` (buyers.tree_nuts / growers.south, South being mostly tree nuts), `e_north` (buyers.field_crops / growers.north_central), `e_new` (buyers / growers.no_history, the landholders history-based allocation shuts out). The seller side is also the unsatisfied seller. Sub-basin stands in for crop type because U1 is about sub-basins and the policy gives uses by sub-basin.
- `capped` k1 on e_south and e_north, k2 (allocation by history) on e_new; holders landowners.history; `wider_price` true; premises a1 (A-1), a2 (A-2); e_new also a27 (A-27).
- `means`: k2 in for landowners.history; k3 (lottery reserve) in for landowners.eligible.
- `charges` k5: the $10/af fee as an `operating` charge on sellers of e_south and e_north to officials.enforcement (non_tax_receipts), premise a2. `compliance` (meters at owner's cost) for the two grower classes, `enforcers` officials.enforcement, `funded` by the grower classes (the fee funds SBWA).
- `announced` k1 (a20, A-20). `qualifies` k2 landowners.history (a17, A-17, p 0.2: the base period closed before the March 2022 draft, so a race to qualify is unlikely; kept so the answer is recorded).
- `thresholds` k1, households.domestic, quantity_demanded (domestic wells under 2 af a year are exempt), premise s1 (judged 0.3, a new statement of mine: not in the table).
- `unclear` U1 with `terms` k4b (U1-b only): trading in e_south made better for the seller side, premise a22 (A-22, p 0.5). U1-a has no extra component; U1-b adds the option that South growers lease in North/Central allocations.
- Not in the seed (loop's): alternatives, links, margins, stakes, assets, yields, timing, parts, dominance.

## Round 1 (9 nodes)
- buyers.tree_nuts, buyers.field_crops, buyers: alternative, buy substitutes from outside the basin (quantity_substitute on sellers.substitutes), premise J1 (judged 0.85: basin is 5% of nuts, under 1% of each field crop).
- growers.south: lease in (right_lease_price on landowners.history; A-4, A-16), give up the last af (quantity_supplied, inverse; A-25), regional surface water (price_substitute; A-8), farm in Lowther (relocation_out_of_area; A-9), retire backup wells rather than meter (capital_stock_target, inverse; A-26), over-pump (outside, legal_breach; A-10), stake (lobbying; A-11), timing carry_over of investment_target (new orchards; A-20), links: national tree-nut price (supply; A-19), farm labour (input; A-6), input suppliers (input; A-7), aquifer stock (owners.wells resource_stock; A-14).
- growers.north_central: the same minus A-16 and the stake, with the field-crop price link on A-18.
- growers.no_history: lease in (A-4), Lowther (A-9), over-pump (A-10), stake (A-11).
- landowners.eligible: enter the lottery (applications, inverse; A-21), split or transfer parcels before 1 July 2027 (reclassification, inverse; A-13).
- landowners.history: lease out / stop irrigating (A-5 measured on growers.north_central's quantity_supplied; A-24 on its own), asset tied to e_south seller side (A-3, A-12), lease price as a cost to the two grower classes (cost link; A-4).
- officials.enforcement: empty.

## Round 2 (9 nodes)
- growers.* #2: same_act link from relocation_out_of_area to growers.lowther entry_rate (A-9). input_suppliers, sellers.substitutes, workers.farm: empty.
- landowners.eligible#2: link applications to officials.enforcement non_tax_receipts (the $500 entry fee; no premise, it is in the policy).
- landowners.history#2: dominance asset_value increase, kind arithmetic (fee about $2.1m a year against shares worth about $800m; no premise); labour and input links from its quantity_supplied (A-6, A-7).
- owners.wells: links from the aquifer stock to the grower classes' resources (input; J2), maintenance_spending of growers and of households.domestic (substitute; J3, J4); dominance resource_stock increase (empirical, A-14).

## Round 3 (5 nodes)
- growers.lowther: link entry_rate to owners.lowther resource_stock (supply; J6). households.domestic: link to municipalities.county subsidy_outlay (same_act; J5). growers.north_central#3 and growers.south#3: dominance resources_available_other_uses decrease (A-23: lease price far above the energy saved). landowners.history#3: empty.

## Answers
Table: A-3, A-4, A-5, A-6, A-7, A-8, A-9, A-10, A-11, A-12, A-13, A-14, A-16, A-18, A-19, A-21, A-24, A-25, A-26 (all 19 in answers.json) plus the seed premises A-1, A-2, A-17, A-20, A-22, A-27 (carried in the seed). A-15 and A-23 are in the table; A-23 is used (round 3 dominance, p 0.9); A-15 could not be used (see below).
Judged (my own, from section 1): J1 substitutes outside the basin 0.85; J2 slower-falling table lowers energy cost 0.9 (figure in section 1: $0.20 per af per foot); J3 fewer ag wells deepened 0.8; J4 fewer domestic wells dry 0.85; J5 county program spends less 0.85; J6 Lowther movers pump the Lowther aquifer 0.9. Also seed premise s1 (domestic wells near the 2 af line) 0.3.

## What the format could not hold
- The lottery (K3): entry is a choice with a $500 fee and a chance of shares. `means in` records the transfer; the fee and the entry choice only came through an `applications` alternative (inverse) and a same_act link. A threshold that grants (parcel at least 20 acres) rather than burdens cannot be written; the parcel-splitting response (A-13) needed `inverse`.
- Shut-out landholders (A-27): assets tied to a capped exchange's seller side rise, so the land value loss of parcels without shares has no asset form; the shut-out sellers are recorded only by lost trades.
- Aquifer depletion: no relation says "pumping draws down a stock". `supply` (opposite sign) and `substitute` (a higher table replaces deepening) were used as the nearest signs; chains are Tier C by the ontology but the engine does not mark them.
- A-15 (counterfactual trend: decline would itself cut pumping in the long run) lowers the cap's long-run effect on pumping; there is no fact for a counterfactual trend, so it is unused. Likewise the penalty ($600 per af) and loss-of-shares rule are only a premise (a2) and an `outside` margin, not a charge.
- Sub-basin tracking (U1-a: shares pumped only where earned) is not a ban here; it is carried as "U1-b adds an option" with A-22 as its premise, a baseline of U1-a, not the no-plan counterfactual.
- Landowner versus grower (tenants farm leased parcels, shares go to the parcel holder) is collapsed: landowners.history holds and growers pump.
- Dominance on owners.wells resource_stock was not applied: that consequence carries a sign per reading (U1), and the dominance step skips those.
- Detail of the sub-basin/crop mapping (Central is mixed) is approximated by growers.north_central.
