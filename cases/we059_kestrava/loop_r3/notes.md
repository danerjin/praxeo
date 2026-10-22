# WE-059 Kestrava Fair Repair Act: blind expand-loop run (loop_r3)

Inputs read: section 1 and the assumption table only (copied to policy.md for `--policy`). Nothing under handbook/05_examples*, tests/ or the other cases/we059_kestrava folders was opened. `mkseed.py` and `mkprops.py` build seed.json, proposals.json and answers.json. Table ids map as a1..a25 = A-1..A-25 in the seed; `s1`, `s2` are seed statements with no table row. Result: DONE in 3 rounds, 14 loop questions, no `off-list:` lines (final_output.txt).

## Seed (policy's own facts, CR-1)
- Exchanges: e1/e2 phone repair inputs (independent phone shops / phone owners buy from phone makers), e3/e4 the same for farm equipment (independent farm shops / growers from farm makers), e5 sale of new phones, e6 sale of new farm equipment, e7 salvaged and stolen phone parts. Buyers of new equipment are split from owners (`buyers.new_phones`, `growers.new_buyers` against `owners.phones`, `growers`): the Act treats a sale and a repair purchase differently and the engine merges one actor's `quantity_traded` over all its exchanges.
- K1: `duties` on e1 to e4 (premises a2 "makers did not offer", a1 "most makers comply"). `charges` k1_term on e5/e6, the mandated term paid in kind to the buyer, with `other_receivers` the independent repairers and `quantity_premises` a25. k1_item on e6, `basis: item`, branch premise a11 (specialty models under 20 sales).
- K2: `terms` on e5/e6, better for the buyer (a2, a22), worse for the seller (a2, a6).
- K3 under U1-a only (`unclear` U1, components {U1-a: k3, U1-b: none}): `terms` on e5 (buyer better) and e7 (seller and buyer better, a17). Under U1-b the lock is lawful with a maker tool, which K1 already supplies.
- K4: `enforcers`, `fixed_budget` (s2), `penalties` (a10) collected by `treasury`, `compliance` for makers and dealers, `announced` (a20), `moves` e6 buyer (a18).
- Answers in the seed: from the table a1 a2 a6 a10 a11 a17 a18 a20 a22 a25. Judged: s1 "Most makers comply with K3 in most cases" 0.7 (by analogy with A-1 and A-10); s2 "The Consumer Protection Division's budget is unchanged, so its other complaint work gives way" 0.85 (section 1: no new appropriation).

## Round 1 (depth 1, 12 nodes)
- Independents (`repair_shops.independent_farm`, `_phone`): input link to their repair supply and a yield link to entry (A-5), substitute link to dealers / authorized providers (A-3), phone: substitute link to salvaged parts (A-21), stake in k1 (A-23). Source sentences: independents buy mechanical parts but lack the software; "some 900 independent shops".
- `growers`, `owners.phones` (owners who now get parts): alternative whose use falls is the dealer or authorized repair (A-3); input link from parts bought to self repair, `home_production` (A-3, A-16); timing, carry repairs past the 1 Sep 2028 start (A-7, with a20 announced).
- `growers.new_buyers`: cross-border purchases by `growers.near_border` (judged J1 below); dominance `quantity_traded` decrease (A-25). `buyers.new_phones`: dominance (A-25).
- Makers: alternatives reclassification (A-9, farm), integrate components or pair more parts (A-24), phone makers extend programs nationally (A-8); asset (A-12, A-20) and yield (A-12) of the repair-input margin; stakes in k1, k2 (A-23). Dealers: stakes (A-23).
- Empty: `officials.enforcement`, `sellers.stolen_parts`, `treasury` (nothing the sections give to go on).
- Error caught on the engine output and fixed in the round-1 file before round 2: I first proposed `home_production` as an alternative; for an actor made better the alternative falls, so it printed "home_production decrease". Replaced by the input link above.

## Round 2 (depth 2, 12 nodes, 9 of them revisits)
- Dealers#2: supply_price link to their service price (A-4, short), crowding link to growers' `wait_time` (A-14), yield link to `asset_value` (A-19, A-20). `growers.new_buyers#2`: own_price link to quantity demanded, same_act link to dealers' sales. `manufacturers.phone#2`: supply link to owners in other states' price (A-8), new class `owners.other_states`. Authorized phone providers: supply_price link (A-4). Independents#2: yields (A-20).
- Empty: growers#2, owners.phones#2, buyers.new_phones#2, manufacturers.farm#2 (reclassification and integration reach no one the sections name), growers.near_border (its sign is `ambiguous`, so no link would act), sellers.substitutes.

## Round 3 (depth 3, 7 nodes)
- Independents#3: investment_target follows return_on_capital (A-5, long). `owners.other_states`: own_price link. Others empty.

## Answers
- From the table (13 loop questions): A-3, A-4, A-5, A-7, A-8, A-9, A-12, A-14, A-16, A-19, A-21, A-23, A-24, with the table's p. Seed premises from the table: 10 (above).
- Judged (1 loop question): J1 "Some farms near the state line buy new equipment from Darnholt dealers when Kestrava prices rise." 0.7, from section 1: about 3,000 farms within 30 km of the line, six Darnholt dealers within 30 km. Plus seed s1, s2.

## What the format could not hold
- `quantity_traded` merges all of an actor's exchanges: makers' parts sales (up) and equipment sales (down) stay `ambiguous`, and A-25 (the net loss per maker) could not be placed as a dominance on them. Reported `ambiguous` for both makers.
- A-15 (used-phone buyers discount unpaired parts), A-13 (constant cost, so no long-run repair price change), A-1 to A-10 enforcement weakness as a limit on K1 for individual makers, A-6 recovery through other terms (no `margins` without a held or fixed price), A-17 beyond one `terms` fact (thieves' incentive and theft are not variables), A-18 beyond the `moves` on e6 (Kestrava against Darnholt prices). Not placed: no relation links a repair choice to resale value (A-15).
- A receipt variable for access to inputs: used `quality_per_unit` for owners and independent repairers.
- Where fines go (`treasury`) is not in the sections; chosen to name a collector.
- Dealers' repair and new-equipment sales are one actor class with one `quantity_traded`; the $100 million shift in the Figures could not be used (no quantities in the format).
- Cross-border purchases: the alternative has the buyer both better (term received) and worse (price), so the engine reports `ambiguous`.
