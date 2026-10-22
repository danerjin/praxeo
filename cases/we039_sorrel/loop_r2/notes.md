# WE-039 Sorrel Basin: expand loop, blind run (loop_r2)

Files: `seed.json`, `proposals.json`, `answers.json`, `situation.json` (the `--out` of the last run), `policy.md` (section 1 as given). Final output: DONE in 3 rounds, 20 questions, no `off-list:` lines. Every answer comes from the assumption table (18 questions) or was judged (2).

## Seed (the policy's own facts)
- Exchange `e_water`: buyer growers.lessees (pumpers who must lease in), seller licensees.history (K2 holders), unsatisfied seller owners.no_history; price variable right_lease_price on both sides. Exchange `e_xsub`: buyer growers.south, seller licensees.north_central (the cross-sub-basin lease, which only U1-b opens).
- `capped` k1 on e_water (holders licensees.history, licensees.lottery; a1, a2). K1 fixes the quantity, the lease price rations it; no `wider_price` because the lease price of the permission is set in the basin, not in the national crop market.
- `penalties` k1 ($600 per af; a10, a2). `charges` k5: the $10 per af fee, paid by holders (seller side) to SBWA, `basis: operating` (a sum fixed per holder, independent of leasing), premise a2. `enforcers`, `funded` (holders pay), `compliance` (meters at the owner's cost, on growers.lessees).
- `means` in: k2 (licensees.history), k3 (licensees.lottery). `announced` k1 (a12). `qualifies` k2 on pumping (a17, p 0.2, so unreported).
- `unclear` U1: U1-a lists no component (shares stay in their sub-basin: the cap alone); U1-b lists k4b = `terms` better for growers.south on e_xsub (a4). Signs for e_xsub parties therefore appear as `none` under U1-a and `increase` under U1-b.

## Round 1 (8 nodes)
- growers.lessees: alternatives surface water (a8, "surface water also trades ... $250 per af"), fallow the last af (a25, inverse on quantity_supplied), Lowther (a9), retire backup wells instead of metering (a26, inverse on capital_stock_target); outside margin over-pumping as legal_breach (a10); part growers.overpumping; link cost: lease price to quantity_supplied (judged premise PT, national price taker, from "5% ... under 1%"); same_act: lease price to full_cost_per_unit; crowding: fewer af pumped, lower lift cost (a14, "$0.20 per af" per foot), and fewer domestic dry wells (a14); dominance full_cost_per_unit increase (a23); labour and input-supplier links (a6, a7); tree-nut price link (a19); asset for owners.no_history on the buyer side (a12); yield (PT).
- growers.south: stake in k1 (a11); under U1-b a crowding link from its higher pumping (a22).
- licensees.history: alternatives field crops farmed less (a5, actor licensees.field_crops), idle land (a24); land asset for owners.history (a12); dominance on resources_available_other_uses (judged DOMH, "$800 million" against "$2.1 million a year").
- licensees.north_central: asset under U1-b (a3).
- owners.no_history: alternatives lottery applications (a21), parcel splitting as reclassification (a13, a21); stake in k2 (a11); timing carry_over of investment_target (a20, "draft plan ... 15 March 2022").
- Empty: growers.overpumping, licensees.lottery, officials.enforcement.

## Round 2 (11 nodes)
- growers.lessees#2: surface-water price links to buyers.substitutes and sellers.substitutes (a8, short horizon, supply fixed by allotments); Lowther entry (a9, same_act); crowding to well maintenance and to the county's emergency program (a14).
- growers.south#2: U1-b crowding link to households.south (a22). licensees.field_crops: labour, input suppliers (a6, a7), field-crop price (a18, unreported). owners.history: dominance asset_value increase (DOMH): the fee wedge (side_dir of the charge) would otherwise make it ambiguous. owners.no_history#2: entry fees as SBWA receipts (a21, same_act).
- Empty: growers.overpumping#2, households.domestic, input_suppliers, licensees.history#2, licensees.north_central#2, workers.farm.

## Round 3 (8 nodes)
- growers.lowther: crowding link on its cost (a9). All others empty (buyers.substitutes, growers.lessees#3, households.south, municipalities, owners.history#2, sellers.substitutes).

## Answers
- From the table (18): A-3, A-5, A-6, A-7, A-8, A-9, A-11, A-13, A-14, A-18, A-19, A-20, A-21, A-22, A-23, A-24, A-25, A-26. A-1, A-2, A-4, A-10, A-12, A-17 are the seed's own.
- Judged (2): "Basin growers take national crop prices as given." 0.85 (section 1: the basin grows about 5% of tree nuts and under 1% of each field crop); "The value of the free shares to history holders exceeds the fees they pay on them." 0.95 (about $800 million against about $2.1 million a year).
- Unreported by the cut-off: a17 (qualifies), a18 and a19 (national prices).

## What the format could not hold
- Own use of an allocation is not an exchange: holders who farm their own 63% appear only as holders; the pumping cap falls on `growers.lessees` quantity_traded, so total basin pumping is approximated by lessees' trades.
- The water table. No relation takes less extraction to a higher stock: `crowding` was used (lower lift cost, fewer dry wells), with `resource_stock` unused; Tier C.
- U1: only a better-for-buyers `terms` could be hung on U1-b. The shift of pumping from North and Central to South, and North communities' gain, has no chain (quantity traded out is not quantity pumped out).
- K4 "no carry-over between years" (use it or lose it): `terms` is not proposable at a node, and is not in the seed because no exchange side it makes worse is named in the text.
- The $10 per af fee falls on holding, not on trading; `operating` makes sellers fewer (number_of_sellers decrease) and, through the wedge, makes owners.history asset_value ambiguous until dominance is added.
- K3 lottery (random allocation, entry fee, one entry per parcel): no part holds a lottery; applications and parcel splitting are alternatives of owners.no_history only.
- A-15 (without the cap, decline would cut pumping anyway in the long run): no fact holds a counterfactual trend, so horizons of the cap's effect on pumping are not separated.
- Subclasses growers.nuts / growers.field_crops: the exchange takes one buyer class; the split appears only for licensees.field_crops.
- Fund balance of SBWA (fee receipts against enforcement cost): not stated in the text, left unlinked.
