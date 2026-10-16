# WE-039 / Analysis: Groundwater pumping cap with tradable shares allocated by history

Analyst: core-only re-run (Handbook 0.8)  |  Rules: core rules CR-1 to CR-12 only  |  Status: awaiting comparison

## 1. Policy record

**Sorrel Basin Groundwater Allocation Plan.** The Sorrel Basin (State of Castellan) is an alluvial aquifer under about 110,000 irrigated acres in three sub-basins. Average pumping in water years 2017 to 2021 was about 300,000 acre-feet (af) a year: North 110,000 (mostly field crops), Central 70,000 (mixed), South 120,000 (mostly tree nuts). Tree nuts use about 160,000 af on 40,000 acres, field crops about 140,000 af on 70,000 acres. Sustainable yield is about 200,000 af. The water table fell about 2.5 feet a year (4 in South); each foot of lift costs about $0.20 per af. About 2,400 agricultural and 4,000 domestic wells draw on the aquifer; about 60 agricultural wells a year were deepened or replaced (about $80,000 each) and about 150 domestic wells went dry in 2017 to 2021; the county runs an emergency water program. Crops are sold nationally (about 5% of the nation's tree nuts, under 1% of each field crop). Irrigated land sells for about $12,000 an acre (nuts) and $6,000 (field crops); dry grazing land about $1,500. About 6,000 people work on basin farms. The Sorrel Irrigation District delivers canal water to about 30,000 acres in North; regional surface water trades at about $250 per af. The Lowther Basin to the east has no cap; its plan is due in 2030.

No allocation method had been proposed before the draft plan, with its 2017 to 2021 base period, was published on 15 March 2022. Adopted 18 November 2026; shares issued 1 July 2027; cap from the water year beginning 1 October 2027. No expiry; reviewed in 2032.

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Cap | `quota` | Groundwater pumped from the basin | Holders of non-domestic wells | 210,000 af a year (70% of the base average). | Domestic wells pumping under 2 af a year. |
| K2 Allocation by history | `rights_allocation` | 90% of the cap (189,000 af) | SBWA | Permanent shares issued to whoever holds a parcel on 1 July 2027, in proportion to its 2017 to 2021 pumping; about 63% of history. | — |
| K3 Reserve for new users | `rights_allocation` (lottery) | 10% of the cap (21,000 af) | SBWA | Permanent shares in 100 af blocks, drawn September 2027. Eligible: each parcel of at least 20 acres, held on 1 July 2027, with no K2 allocation; one entry per parcel; fee $500. | — |
| K4 Trading | Rule on transfers | Shares and annual allocations | Share holders | Shares may be sold and a year's allocation leased separately from land; transfers "between wells in the Basin, subject to the Authority's rules on local impacts". No carry-over. | — |
| K5 Enforcement and funding | Enforcement | K1 to K4 | SBWA | Telemetry meters on every non-domestic well by 1 October 2027 at the owner's cost (about $3,000); monthly readings; satellite checks. Penalty $600 per af over allocation; loss of shares for repeated violation. Fee $10 per af of shares held (about $2.1 million a year). | — |

Unclear provision:
- U1, trading across sub-basins. U1-a: a share may be pumped only in the sub-basin where the parcel that earned it lies. U1-b: a share may be pumped anywhere in the basin, subject only to well-level conditions.

Figures: the cap removes about 90,000 af a year (30%). A holder keeps 63% of its history. At an illustrative lease price of $300 per af and 7%, a 1 af share is worth about $4,300 and the K2 shares about $800 million. Each foot of water table not lost saves about $0.20 per af pumped thereafter.

Counterfactual law: no plan; pumping as landholders choose (near 300,000 af and rising, A-1); the water table keeps falling as in 2017 to 2021.

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | CR-1 operations | Core rules applied |
| --- | --- | --- | --- | --- |
| K1 Cap | triangular and autistic (restricts pumping for own use and its sale through crops) | Yes: counterfactual pumping is far above 210,000 (A-1), and enforced against most pumpers (A-2) | 1 (pumping beyond one's allocation removed, where enforced); 3 (a $600 per af penalty risk attached to over-pumping where detection is weak, A-10) | CR-3a, CR-4, CR-6 (fixed quantity), CR-7, CR-9, CR-10 |
| K2 Allocation by history | binary (the state gives a created right) | Yes | 4 (a valuable tradable right transferred to parcel holders); 2 (option to lease or sell water) | CR-7c (0.7 claims before creation; 0.8 windfall), CR-8b, CR-8 (0.8 value created by ending a race), CR-10c |
| K3 Lottery reserve | binary (the state gives by lot) | Yes | 2 (option to enter, at $500, for parcels of 20 acres or more without history); 4 (rights to winners) | CR-4, CR-7c, CR-7 (0.7 race to qualify), CR-8b, CR-8c |
| K4 Trading | removes a restraint on moving a means | Yes, given a lease market (A-4); across sub-basins depends on U1 | 2 (lease or sell allocations apart from land) | CR-5, CR-7a, CR-7 (0.7 a policy that makes a means mobile) |
| K5 Enforcement and funding | binary | Yes | 3 (meter, readings attached to operating a well); 4 (fee per af of shares held, not avoidable while holding shares); 3 (penalty on over-pumping) | CR-4 (0.7/0.8 fixed cost per outlet), CR-8b, CR-8c |

## 3. Actor classes

| Actor class | Role | How its options change (CR-1) |
| --- | --- | --- |
| pumpers.non_domestic | All holders of non-domestic wells | Op 1/3 (cap), op 3 (meters, penalties). |
| holders.history.tree_nuts | Parcel holders with history, mostly South nut growers; lessees of allocations | Op 4 (shares worth 63% of history); op 1 on the other 37%; option to lease in. |
| holders.history.field_crops | Parcel holders with history, mostly North field-crop growers; lessors | As above; option to lease out (A-5). |
| landholders.no_history.small | Parcels under 20 acres without history that would have irrigated (A-N5) | Op 1: no allocation; may only lease. |
| landholders.no_history.eligible | Parcels of 20 acres or more without history | Op 1 as above; op 2: a lottery entry. |
| lottery_winners | Winners of K3 blocks | Op 4: a created right. |
| planters.prospective | Landholders planning new orchards | Op 3: water for new planting now costs the lease price (from expectation, A-20). |
| owners.domestic_wells | About 4,000 households | Exempt; affected only through the shared aquifer (Tier C). |
| workers.farm | About 6,000 farm workers | Through CR-9 (input_to): demand for their work follows acres farmed (A-6). |
| input_suppliers | Seed, chemical, equipment dealers; well drillers | Through CR-9 (input_to) (A-7). |
| sellers.meters | Suppliers of telemetry meters | Through CR-9 (input_to): required purchases. |
| sellers.surface_water; buyers.surface_water.other_districts | Regional surface-water market | Through CR-9 (substitute) (A-8). |
| neighboring_jurisdictions (Lowther) | Landholders and pumpers in the uncapped basin | Through CR-9 (across_border) (A-9). |
| sbwa | Administers K2 to K5 | Op 4: fees; enforcement duties. |
| county.emergency_water | Supplies households with dry wells | Through the shared aquifer (Tier C). |
| buyers.crops (national) | Buyers of nuts and field crops | Through CR-9; price effects need A-18 or A-19, both below 0.5. |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-1 | pumpers.non_domestic | quantity_supplied (groundwater pumped in the basin) | decrease | medium | CR-1 op 1 and op 3, CR-4 (x: comply, y: violate) | A-1, A-2 |
| C-2 | holders.history | asset_value (K2 shares) | increase | short (from 15 March 2022) | CR-7c, CR-10c, CR-8b | A-1, A-2, A-3, A-12 |
| C-3 | sbwa | non_tax_receipts (share fees, lottery entry fees) | increase | short; medium; long | CR-1 op 4, CR-8b | - |
| C-4 | pumpers.non_domestic | compliance_cost (meters, telemetry, readings) | increase | short; medium | CR-1 op 3, CR-8c | - |
| C-5 | sbwa | enforcement_cost | increase | medium; long | CR-1 op 4, CR-8c | - |

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-6 | holders.history | right_lease_price (annual allocations) | increase | medium; long | CR-6 (fixed quantity; 0.7 wider-market clause), CR-7a | A-1, A-2, A-4 |
| C-7 | holders.history.field_crops | quantity_traded (allocations leased out) | increase | medium | CR-4 (x: farm the allocation, y: lease it), CR-7a, CR-5 | A-4, A-5, A-16 |
| C-8 | holders.history.field_crops | quantity_supplied (basin field crops) | decrease | medium | CR-1 op 1, CR-4c, CR-3, CR-7a | A-1, A-2, A-16 |
| C-9 | holders.history.tree_nuts | quantity_supplied (basin tree nuts) | decrease | medium | CR-1 op 1, CR-4c, CR-3, CR-12e | A-1, A-2 |
| C-10 | pumpers.non_domestic | quantity_supplied (groundwater pumped in the basin) | ambiguous | long | CR-12b, CR-12 (0.8 kind 2) | A-1, A-2, A-14, A-15 |
| C-11 | holders.history.tree_nuts | quantity_supplied (basin tree nuts) | ambiguous | long | CR-12b | A-1, A-2, A-14, A-15 |
| C-12 | holders.history.field_crops | quantity_supplied (basin field crops) | ambiguous | long | CR-12b | A-1, A-2, A-14, A-15 |
| C-13 | holders.history | quantity_traded (allocations leased from North and Central to South) | U1-a: no_change; U1-b: increase | medium; long | CR-7a, CR-4, CR-1 op 1 (U1-a) | A-4, A-16 |
| C-14 | planters.prospective | investment_target (new orchards) | decrease | short (from 2022); medium; long | CR-10a, CR-4 (x: plant, y: not), CR-3 | A-20, A-1, A-2 |
| C-15 | landholders.no_history.small | asset_value (land) | decrease | short (from 15 March 2022) | CR-7c, CR-10c, CR-12e | A-N5, A-1, A-2, A-3, A-12, A-N3 |
| C-16 | landholders.no_history.eligible | asset_value (land) | ambiguous | short | CR-12b | A-N5, A-1, A-2, A-12, A-21 |
| C-17 | holders.history | asset_value (parcels with history, with their claim to shares) | ambiguous | short (from 15 March 2022) | CR-12b | A-1, A-2, A-3, A-12 |
| C-18 | landholders.no_history.eligible | reclassification (parcels split to gain lottery entries) | increase | short (to 1 July 2027) | CR-4 (x: one parcel, y: several of 20 acres or more), CR-7 (0.7 race to qualify) | A-13, A-21 |
| C-19 | landholders.no_history.eligible | compliance_cost (entry fees, lot-line adjustments) | increase | short | CR-8b, CR-8c | A-21, A-13 |
| C-20 | lottery_winners | asset_value (K3 shares) | increase | short (September 2027) | CR-7c, CR-8b | A-1, A-2, A-3 |
| C-21 | pumpers.non_domestic | legal_breach (pumping over allocation) | increase | medium; long | CR-4 (x: comply, y: violate) | A-10 |
| C-22 | sbwa | non_tax_receipts (penalties) | increase | medium; long | CR-8b | A-10, A-2 |
| C-23 | holders.history; landholders.no_history | lobbying_effort | increase | short; medium | CR-4 (x: accept, y: lobby), CR-10a, CR-8c | A-11 |
| C-24 | pumpers.non_domestic | capital_stock_target (active non-domestic wells) | decrease | short; medium | CR-4 (0.7/0.8 fixed cost per outlet), CR-1 op 1 | A-N4 |
| C-25 | sellers.meters | quantity_traded (telemetry meters) | increase | short | CR-9, LW-10 | A-2 |

## 6. Second-order effects

Depth limit 4. Chains through the shared aquifer (relation `shared_facility`) are Tier C (CR-9, 0.7). Chains to national crop prices stop at depth 2: their premises (A-18 p 0.15, A-19 p 0.3) are below the cut-off.

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C-26 | workers.farm | employment (−), hours_worked (−) | at_least_one_decrease | medium | CR-9, LW-10, CR-7a | farm labor input_to basin crops (close) | A-6, A-1, A-2 |
| C-27 | workers.farm | employment (farm work in the basin) | ambiguous | long | CR-12b | as above | A-6, A-14, A-15 |
| C-28 | input_suppliers | quantity_traded (sales to basin farms) | decrease | medium | CR-9, LW-10 | inputs input_to basin crops (close) | A-1, A-2 |
| C-29 | input_suppliers | return_on_capital (local dealers) | decrease | medium | CR-7b | as above | A-7, A-1, A-2 |
| C-30 | sellers.surface_water | price_substitute (regional surface water) | increase | medium; long | CR-9, CR-6 | surface water substitute for groundwater (partial) | A-8, A-1, A-2 |
| C-31 | buyers.surface_water.other_districts | quantity_substitute (surface water bought) | decrease | medium; long | CR-9, CR-4c, CR-8a | same fixed supply bought by both (close) | A-8, A-1, A-2 |
| C-32 | neighboring_jurisdictions (Lowther landholders) | asset_value (Lowther irrigated land) | increase | short; medium | CR-9, CR-7a, CR-7c | across_border (partial) | A-9 |
| C-33 | neighboring_jurisdictions (Lowther pumpers) | quantity_supplied (groundwater pumped in Lowther) | increase | medium | CR-4 (x: farm here, y: there), CR-7a | across_border (partial) | A-9 |
| C-34 | pumpers.non_domestic | full_cost_per_unit (energy to lift an af) | decrease | medium; long | CR-9, CR-10b | shared_facility (the aquifer) | A-14, A-2 |
| C-35 | pumpers.non_domestic | maintenance_spending (deepening and replacing wells) | decrease | long | CR-9, CR-10b, CR-4 | shared_facility | A-14 |
| C-36 | owners.domestic_wells | maintenance_spending (deepening and replacing dry wells) | decrease | long | CR-9, CR-4 | shared_facility | A-14 |
| C-37 | county.emergency_water | subsidy_outlay (water for households with dry wells) | decrease | long | CR-9, CR-8b | shared_facility | A-14 |
| C-38 | input_suppliers (well drillers) | quantity_traded (well deepening and drilling) | decrease | medium; long | CR-9, LW-10 | input_to well maintenance; shared_facility | A-14 |
| C-39 | holders.history.tree_nuts | resources_available_other_uses | decrease | medium | CR-3 (note), CR-8b, CR-12e | lease contract | A-4, A-16, A-N3 |
| C-40 | holders.history.field_crops | resources_available_other_uses (lease receipts) | increase | medium | CR-8b, CR-2 | lease contract | A-4, A-5 |
| C-41 | holders.history | resources_available_other_uses (share fees) | decrease | medium; long | CR-1 op 4, CR-8b, CR-3 | - | - |
| C-42 | holders.history.field_crops | resources_available_other_uses (total) | ambiguous | medium | CR-12b, CR-12 (0.8 two items) | - | A-4, A-5, A-1, A-2 |

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance premise | Combined sign |
| --- | --- | --- | --- | --- |
| pumpers.non_domestic, groundwater pumped, medium | none | cap (C-1); leasing cannot raise total pumping above the cap | Not needed | decrease (C-1) |
| pumpers.non_domestic, groundwater pumped, long | without the cap, falling levels make wells fail and cut pumping (A-15), while under the cap the aquifer falls more slowly (A-14); this narrows or reverses the gap (Tier C: through the shared aquifer) | the cap holds pumping at 210,000 (A-1, A-2) | None: whether counterfactual pumping falls below 210,000 is not in the case | ambiguous (C-10) |
| holders.history.tree_nuts, nut output, medium | lower lift costs (C-34, Tier C) | every af now costs at least the lease price, by purchase or by forgone lease (CR-3, CR-4c) | Response argument (CR-12e): leasing in is a response to the cap and cannot raise nut water above its counterfactual level, where the marginal af cost only energy; A-N3 bounds the lift saving | decrease (C-9) under both readings; smaller under U1-b (A-22) |
| tree nuts, field crops, farm employment, long | as for pumping (A-15) | as for pumping | None | ambiguous (C-11, C-12, C-27) |
| holders.history, parcel asset_value, short | share value (C-2); capitalized lift savings and avoided well failures (Tier C, A-14, A-15) | loss of free pumping above 63% of history; fees (C-41) and meters (C-4) | None: the value of the lost 37% against the shares depends on each holder's use value per af | ambiguous (C-17) |
| landholders.no_history.small, asset_value, short | capitalized lift savings on water they would lease (Tier C) | loss of free pumping they would have used (A-N5) | A-N3: lift savings per af are a small fraction of the lease price | decrease (C-15) |
| landholders.no_history.eligible, asset_value, short | expected value of a lottery entry (A-21) | loss of free pumping (A-N5) | None | ambiguous (C-16) |
| holders.history.field_crops, resources (total), medium | lease receipts (C-40) | fees (C-41); lost farm receipts on the 37% cut (CR-3a, CR-5a) | None | ambiguous (C-42) |
| holders.history.tree_nuts, resources, medium | lower lift costs (Tier C) | lease payments for water they keep buying (CR-3 note) | A-N3 | decrease (C-39) |

The avoided failure of wells (A-15) is not an opposing chain for landholders without history: under the plan they get no free water, so the aquifer's longer life raises the value of the shares, not of their land.

## 8. Time structure

- **Expectation (from 15 March 2022).** The draft plan with its base period made the claim to shares expected. By CR-7c (0.7 claims before creation) the claim travels with parcels with history, and its value was captured by those who held them in March 2022, partly then and more as adoption became likely (A-12). Because the base period (2017 to 2021) was fixed before the plan was expected, no one could compete to build history (A-17, p 0.2): the value is a windfall (CR-7, 0.8). Buyers of parcels after March 2022 paid for the claim. Parcels without history lost value at the same time (C-15). Orchard planting fell from 2022 (C-14, A-20).
- **Adoption to issue (18 November 2026 to 1 July 2027).** The lottery's eligibility rules (parcels held on 1 July 2027, one entry each) reward splitting parcels in this window (C-18), a transition effect with no lasting stock beyond the extra parcels.
- **Cap (from 1 October 2027).** Meters are bought before it (C-25, C-4); low-use wells are retired rather than metered (C-24). No carry-over means each year's allocation must be used or leased within the year.
- **Gradual adjustment.** Orchards are durable stocks (CR-10b): nut acreage adjusts as orchards age out and are not replanted, so the fall in nut output (C-9) grows through the medium horizon while field crops, which are annual, adjust at once (C-8).
- **Water table.** The table falls more slowly than it would have (A-14), so lift costs, well deepening and dry domestic wells fall relative to the counterfactual increasingly over time (C-34 to C-38, Tier C). In the long run, counterfactual well failures (A-15) make the comparison of pumping, output and employment ambiguous (C-10, C-11, C-12, C-27).
- **2032 review.** Holders expect shares to last (A-3); a review that might scale shares down is priced into share values as its likelihood changes (CR-7c), and stakes in the review drive lobbying (C-23).

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
| --- | --- | --- | --- | --- | --- |
| C-4 | pumpers.non_domestic | compliance_cost | increase | About $7 million of meters plus readings, which would have served other ends | CR-8c |
| C-5 | sbwa | enforcement_cost | increase | Staff, satellite checks and audits, paid from about $2.1 million of fees | CR-8c |
| C-8 | holders.history.field_crops | quantity_supplied (basin field crops) | decrease | Field crops not grown on fallowed land | CR-8a, CR-5a |
| C-14 | planters.prospective | investment_target (new orchards) | decrease | Orchards not planted | CR-3a |
| C-19 | landholders.no_history.eligible | compliance_cost (entry fees, lot-line adjustments) | increase | Survey, legal and county work on splits is used up; entry fees are a transfer to SBWA | CR-8b, CR-8c |
| C-23 | holders.history; landholders.no_history | lobbying_effort | increase | Time and money spent at hearings and on the review | CR-8c |
| C-26 | workers.farm | employment (−), hours_worked (−) | at_least_one_decrease | Farm work no longer offered in the basin | CR-9 |
| C-31 | buyers.surface_water.other_districts | quantity_substitute | decrease | Surface water other districts no longer get | CR-8a |
| C-41 | holders.history | resources_available_other_uses (share fees) | decrease | About $2.1 million a year paid to SBWA | CR-8b |

Both sides (CR-8b): fees (C-41, C-19) are SBWA receipts (C-3); lease payments (C-39) are lessors' receipts (C-40); penalties (C-22) are paid by over-pumpers (C-21). The value of the shares (C-2, C-20) has two sources (CR-8, 0.8): rents that the race to pump used up before (falling tables, deeper wells), which no one pays; and free pumping taken from those who would have pumped more than their allocation, chiefly landholders without history (C-15) and holders on the cut 37% (C-17).

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
| --- | --- | --- | --- | --- | --- |
| A-1 | Without the cap, pumping would stay near 300,000 af and above 210,000. | binding | 0.95 | Base average; plantings since. | C-1, C-2, C-6, C-8 to C-12, C-14 to C-17, C-20, C-26 to C-31, C-42 fail. |
| A-2 | The cap is enforced against most pumpers. | enforcement | 0.75 | K5; telemetry; penalty above likely lease prices. | As for A-1, and C-22, C-25, C-34. |
| A-3 | Holders expect shares to last, without early reallocation. | expectations | 0.75 | Shares permanent; review may scale but not reassign. | C-2, C-15, C-17, C-20 lose this chain. |
| A-4 | A lease market forms within a season. | other | 0.8 | SBWA registry; nearby surface-water leasing. | C-6, C-7, C-13, C-39, C-40, C-42 fail. |
| A-5 | Some field-crop growers value lease income above farming their allocation. | alternative_uses | 0.75 | Net returns per af against lease prices. | C-7, C-40, C-42 fail. |
| A-6 | Farm employment and hours adjust to acres farmed. | alternative_uses | 0.75 | Labor per acre by crop. | C-26, C-27 fail. |
| A-7 | Input suppliers sell mainly to basin farms. | other | 0.6 | Dealer locations. | C-29 fails. |
| A-8 | Some basin farms can buy regional surface water, whose supply is fixed in a year. | substitutability | 0.65 | Canal reach; transfer market. | C-30, C-31 fail. |
| A-9 | Some basin growers can farm in the Lowther Basin. | mobility | 0.55 | Distance; listings; growers in both. | C-32, C-33 fail. |
| A-10 | Detection is weak for some wells, so some pumpers over-pump. | enforcement | 0.55 | Telemetry failure rates. | C-21, C-22 fail. |
| A-11 | South growers, North communities and landholders without history can organize at a cost below their stake. | other | 0.85 | Associations; hearing records. | C-23 fails. |
| A-12 | Land buyers priced the expected claim to shares from the draft plan. | expectations | 0.75 | Land prices with and without history after March 2022. | C-2, C-15, C-16, C-17: the timing (from March 2022) fails; the signs hold from 1 July 2027. |
| A-13 | Parcels can be split before 1 July 2027. | other | 0.6 | County processing times. | C-18 fails; C-19 loses this item. |
| A-14 | Under the cap, the water table falls more slowly than it would have. | other | 0.85 | Survey model. | C-34 to C-38 fail; C-10, C-11, C-12, C-27 lose a chain. |
| A-15 | Without the cap, continued decline would make enough wells fail or become uneconomic to cut pumping in the long run. | counterfactual_trend | 0.6 | Saturated thickness in South. | C-10, C-11, C-12, C-27 become decrease. |
| A-16 | Tree nuts earn more per af than field crops for most growers. | other | 0.85 | Crop budgets. | C-7, C-8 (larger cut on field crops), C-13, C-39 lose this chain. |
| A-17 | Some pumpers inflated 2017 to 2021 pumping in anticipation of allocation by history. | expectations | 0.2 | No method proposed before March 2022. | Not reported (below 0.5). |
| A-18 | The fall in basin field-crop output moves national field-crop prices more than negligibly. | other | 0.15 | Under 1% share. | Not reported (below 0.5). |
| A-19 | The fall in basin tree-nut output moves national tree-nut prices more than negligibly. | other | 0.3 | About 5% share. | Not reported (below 0.5). |
| A-20 | Landholders planning new orchards gave weight to the draft plan from 2022. | expectations | 0.7 | Permits and nursery orders. | C-14 loses its short-horizon part. |
| A-21 | The lottery's expected value per entry exceeds the cost of entering for many eligible parcels. | other | 0.85 | Reserve worth about $90 million; $500 fee. | C-16 becomes decrease; C-18, C-19 fail. |
| A-22 | Under U1-b, South growers could lease in enough allocations to approach or pass South's counterfactual pumping. | other | 0.5 | South cut about 44,000 af; about 60,000 af of field-crop shares elsewhere. | Bears only on size: by CR-12e South's pumping cannot pass its counterfactual level, so no sign depends on it. |
| A-N1 | Lowther landholders expect their 2030 plan to allocate by history, and pump or plant more before it to build history. | expectations | 0.45 | NEW. Sorrel's choice is a precedent (CR-11c), but the act allows three methods. | Not reported (below 0.5). |
| A-N2 | Some landholders irrigate small plots from domestic-exempt wells in place of covered wells. | substitutability | 0.4 | NEW. The exemption is by volume (under 2 af), enough for only about an acre. | Not reported (below 0.5). |
| A-N3 | The lease price of an af far exceeds the energy it saves through a slower-falling table over the coming decades. | other | 0.9 | NEW. $0.20 per foot per af and 2.5 feet a year give a few dollars per af after a decade, against surface water at $250 and an illustrative lease price of $300. | C-15 becomes ambiguous; C-39 and C-9's dominance lose this premise. |
| A-N4 | Some non-domestic wells are backups or low-use wells that owners retire rather than meter. | other | 0.6 | NEW. About 125 af per well on average; the $3,000 meter is a fixed cost per well; less water to pump under the cap. | C-24 fails. |
| A-N5 | Some landholders without history would have started or expanded irrigation without the plan. | counterfactual_trend | 0.7 | NEW. A-1 (pumping would rise with new plantings); planting permits after 2021. | C-15, C-16 fail (no loss of free pumping to value). |

**Not reported** (an assumption below 0.5):
- National field-crop and tree-nut prices rise (CR-6 0.7 wider market; CR-9): A-18 (0.15), A-19 (0.3).
- Some pumpers inflated base-period pumping (A-17, 0.2): CR-7 0.7 (race to qualify) would apply only if the method had been expected.
- A race to build history in Lowther before its 2030 plan (A-N1, 0.45).
- Irrigation shifts to exempt domestic wells (CR-4, x: covered well, y: exempt well) (A-N2, 0.4).

## 11. Report

**The policy:** From October 2027, pumping from the Sorrel Basin by non-domestic wells is capped at 210,000 af a year, 70% of the 2017 to 2021 average. Nine tenths of the cap is issued as permanent, tradable shares to whoever holds a parcel on 1 July 2027, in proportion to its 2017 to 2021 pumping; one tenth is drawn by lottery among parcels of 20 acres or more without history. Allocations can be leased or sold apart from land. Every non-domestic well must carry a telemetry meter; over-pumping costs $600 per af; holders pay $10 per af of shares a year.

**Visible consequences:** Pumping falls (C-1). Holders of parcels with history receive shares worth hundreds of millions of dollars at illustrative prices (C-2), and lottery winners receive shares (C-20). Well owners pay for meters (C-4); the authority collects fees and runs enforcement (C-3, C-5).

**Invisible consequences:**
- *Water market:* a lease price for water appears (C-6); field-crop growers lease allocations to nut growers (C-7); under U1-b water moves from North and Central to South, under U1-a it does not (C-13).
- *Output:* field crops fall most (C-8); nut output falls too, more under U1-a (C-9); new orchards are not planted, from the draft plan on (C-14); low-use wells are retired (C-24).
- *Land and rights:* parcels without history lose value from March 2022 (C-15); eligible parcels are split to gain lottery entries (C-18, C-19). The share value was a windfall to those holding parcels with history in March 2022.
- *Others in the basin:* farm work falls (C-26); input dealers sell less and earn less (C-28, C-29); some pumpers over-pump (C-21) and pay penalties (C-22); interested groups lobby (C-23); meter sellers gain (C-25).
- *Neighbors:* surface water costs more and other districts get less of it (C-30, C-31); Lowther land gains value and Lowther pumping rises (C-32, C-33).
- *Through the aquifer (Tier C):* lift costs, well deepening, dry domestic wells, the county's emergency program and drilling work all fall relative to the counterfactual (C-34 to C-38).
- *Money:* nut growers pay for leased water (C-39); lessors receive lease income (C-40); holders pay fees (C-41).

**Ambiguous effects:** Long-run pumping, nut and field-crop output and farm employment (C-10, C-11, C-12, C-27): the cap holds them down, but without it falling levels would have cut them too. The value of parcels with history (C-17): shares on one side, the lost 37% of free pumping on the other. The value of eligible parcels without history (C-16): a lottery entry against the lost option to pump. Field-crop lessors' total means (C-42).

**Key conditions:** The cap binds (A-1, 0.95) and is enforced (A-2, 0.75); a lease market forms (A-4, 0.8); nuts earn more per af (A-16, 0.85); counterfactual well failures (A-15, 0.6) make the long run ambiguous. Five premises were added (A-N1 to A-N5); two are below 0.5 and are not used for reported consequences.

**What this analysis cannot say:** How large any effect is; whether the long-run comparison of pumping and output turns positive; how the water table, land subsidence or water quality change in physical terms (environmental effects are out of scope; the economic effects through the aquifer are Tier C). Which reading of the trading rule applies. Whether the allocation is fair or the policy good.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C-1 | pumpers.non_domestic | quantity_supplied (groundwater pumped in the basin) | decrease | medium | visible | B | CR-1 (op 1: pumping beyond allocations removed where enforced, A-2; op 3: penalty risk where not); CR-4 (x: comply, y: violate; most comply, A-2); the cap binds (A-1) | A-1, A-2 |
| C-2 | holders.history | asset_value (K2 shares) | increase | short (from 15 March 2022) | visible | B | CR-7c (an asset the policy creates is captured by whoever receives it; 0.7: the claim travels with the parcel and is capitalized when the allocation rule becomes expected, A-12; 0.8: base period fixed before then, so a windfall); CR-10c (value reflects expected lease yields, C-6, A-3); CR-8b | A-1, A-2, A-3, A-12 |
| C-3 | sbwa | non_tax_receipts (share fees, lottery entry fees) | increase | short; medium; long | invisible | A | CR-1 (op 4: $10 per af of shares; $500 per lottery entry); CR-8b (receipts equal holders' and entrants' payments, C-41, C-19) | none |
| C-4 | pumpers.non_domestic | compliance_cost (meters, telemetry, readings) | increase | short; medium | visible | A | CR-1 (op 3: a $3,000 meter and monthly readings attached to operating a non-domestic well); CR-8c (used up) | none |
| C-5 | sbwa | enforcement_cost | increase | medium; long | invisible | A | CR-1 (op 4); CR-8c (resources spent enforcing are used up) | none |
| C-6 | holders.history | right_lease_price (annual allocations) | increase | medium; long | invisible | B | CR-6 (a rule fixes the quantity, so a price rises to ration it; 0.7: the crops are priced nationally, so the lease price of the right, not the crop price, rations the capped water); CR-7a. Against a counterfactual in which no right exists and water costs only energy | A-1, A-2, A-4 |
| C-7 | holders.history.field_crops | quantity_traded (allocations leased out) | increase | medium | invisible | B | CR-4 (x: farm the allocation, y: lease it out at C-6; y chosen by those whose return per af is lower, A-5, A-16); CR-7a (water moves to its higher-yield use); CR-5 (both parties expect to gain) | A-4, A-5, A-16 |
| C-8 | holders.history.field_crops | quantity_supplied (basin field crops) | decrease | medium | visible | B | CR-1 (op 1: 37% of history removed); CR-3 (using an af of one's own allocation costs the forgone lease); CR-4c (the lowest-valued af, in field crops, A-16, is given up first); CR-7a | A-1, A-2, A-16 |
| C-9 | holders.history.tree_nuts | quantity_supplied (basin tree nuts) | decrease | medium | invisible | B | CR-1 (op 1); CR-3 and CR-4c (each af now costs at least the lease price, whether bought or own, against energy only without the cap, so the last af is given up); CR-12e (leasing in is a response to the cap and cannot raise nut water above its counterfactual level; lower lift costs, Tier C, are small by A-N3). Under both readings; smaller under U1-b (A-22) | A-1, A-2 |
| C-10 | pumpers.non_domestic | quantity_supplied (groundwater pumped in the basin) | ambiguous | long | invisible | C | CR-12b: (−) the cap (CR-1 op 1, A-1, A-2); (+) CR-9 (shared_facility) and CR-10b: without the cap, falling levels make wells fail and cut pumping (A-15), while under the cap the table falls more slowly (A-14). CR-12 0.8 kind 2 with p at least 0.5: ambiguous. Tier C through the shared aquifer | A-1, A-2, A-14, A-15 |
| C-11 | holders.history.tree_nuts | quantity_supplied (basin tree nuts) | ambiguous | long | invisible | C | As C-10 (CR-12b; CR-9 shared_facility; CR-10b), with South's faster decline in the counterfactual | A-1, A-2, A-14, A-15 |
| C-12 | holders.history.field_crops | quantity_supplied (basin field crops) | ambiguous | long | invisible | C | As C-10 | A-1, A-2, A-14, A-15 |
| C-13 | holders.history | quantity_traded (allocations leased from North and Central to South) | U1-a: no_change; U1-b: increase | medium; long | invisible | B | U1-a: CR-1 (op 1: cross-sub-basin transfers removed). U1-b: CR-4 (x: lease within the sub-basin, y: lease to South at a higher price) and CR-7a (water moves to the higher-yield nuts, A-16, until lease prices are equal net of transfer costs) | A-4, A-16 |
| C-14 | planters.prospective | investment_target (new orchards) | decrease | short (from 2022); medium; long | invisible | B | CR-10a (the expected cap alters planting before it starts, A-20); CR-4 (x: plant, y: not; x made worse because water for new trees must be leased or forgone, CR-3); the cap binds (A-1, A-2) | A-20, A-1, A-2 |
| C-15 | landholders.no_history.small | asset_value (land) | decrease | short (from 15 March 2022) | invisible | B | CR-1 (op 1: pumping without allocation removed); CR-10c and CR-7c (the lost yield of free water these parcels would have used, A-N5, is borne by their holders when the plan became expected, A-12; permanent, A-3); CR-12e: the opposing lift-saving chain (Tier C) is dominated by A-N3 | A-N5, A-1, A-2, A-3, A-12, A-N3 |
| C-16 | landholders.no_history.eligible | asset_value (land) | ambiguous | short | invisible | B | CR-12b: (−) as C-15 (A-N5); (+) CR-7c and CR-10c (the expected value of a lottery entry attaches to the parcel, A-21). No premise says which dominates | A-N5, A-1, A-2, A-12, A-21 |
| C-17 | holders.history | asset_value (parcels with history, with their claim to shares) | ambiguous | short (from 15 March 2022) | invisible | B | CR-12b: (+) the claim to shares (C-2) and, Tier C, capitalized lift savings and avoided well failures (A-14, A-15); (−) CR-1 op 1 and CR-7c (free pumping above 63% removed), fees (C-41) and meters (C-4). No premise compares the lost 37% with the shares | A-1, A-2, A-3, A-12 |
| C-18 | landholders.no_history.eligible | reclassification (parcels split to gain lottery entries) | increase | short (to 1 July 2027) | invisible | B | CR-4 (x: one parcel and one entry, y: several parcels of 20 acres or more and several entries; y made better by the lottery's expected value, A-21, where splits are possible, A-13); CR-7 0.7 (where actors compete to qualify, part of the value is used up) | A-13, A-21 |
| C-19 | landholders.no_history.eligible | compliance_cost (entry fees, lot-line adjustments) | increase | short | invisible | B | CR-1 (op 3: $500 per entry); CR-4 (entrants enter, A-21); CR-8b (fees are SBWA receipts) and CR-8c (splitting costs are used up, A-13) | A-21, A-13 |
| C-20 | lottery_winners | asset_value (K3 shares) | increase | short (September 2027) | visible | B | CR-7c (a created right is captured by whoever receives it); CR-8b; value from the binding, enforced cap (A-1, A-2) and permanence (A-3) | A-1, A-2, A-3 |
| C-21 | pumpers.non_domestic | legal_breach (pumping over allocation) | increase | medium; long | invisible | B | CR-4 (x: comply, y: violate; where detection is weak, A-10, the expected penalty is below the lease price, so some at the margin violate; the option did not exist without the cap) | A-10 |
| C-22 | sbwa | non_tax_receipts (penalties) | increase | medium; long | invisible | B | CR-8b (penalties paid by detected over-pumpers are SBWA receipts; most violations are detected under A-2, some occur under A-10) | A-10, A-2 |
| C-23 | holders.history; landholders.no_history | lobbying_effort | increase | short; medium | invisible | B | CR-4 (x: accept, y: lobby on the formula, the reading of U1, the reserve and the 2032 review; concentrated stakes, A-11); CR-10a (the 2032 review alters choices before it); CR-8c | A-11 |
| C-24 | pumpers.non_domestic | capital_stock_target (active non-domestic wells) | decrease | short; medium | invisible | B | CR-4 0.7/0.8 (a cost fixed per well, the meter, bears on whether the well operates: x: meter and keep, y: retire); CR-1 op 1 (less water to pump); some wells are low-use (A-N4) | A-N4 |
| C-25 | sellers.meters | quantity_traded (telemetry meters) | increase | short | invisible | B | CR-9 and LW-10 (relation: meters input_to operating a well under K5; required purchases, A-2) | A-2 |
| C-26 | workers.farm | employment (−), hours_worked (−) | at_least_one_decrease | medium | invisible | B | CR-9 and LW-10 (relation: farm labor input_to basin crops; fewer acres farmed, C-8, C-9, lower demand for it, A-6); which of employment or hours falls is not licensed, so a group | A-6, A-1, A-2 |
| C-27 | workers.farm | employment (farm work in the basin) | ambiguous | long | invisible | C | CR-12b: as C-10 through CR-9 (input_to), with A-6 | A-6, A-14, A-15 |
| C-28 | input_suppliers | quantity_traded (sales to basin farms) | decrease | medium | invisible | B | CR-9 and LW-10 (relation: inputs input_to basin crops; fewer acres farmed) | A-1, A-2 |
| C-29 | input_suppliers | return_on_capital (local dealers) | decrease | medium | invisible | B | CR-7b (the loss settles on means that cannot move: dealers whose sales are mainly to basin farms, A-7) | A-7, A-1, A-2 |
| C-30 | sellers.surface_water | price_substitute (regional surface water) | increase | medium; long | invisible | B | CR-9 (relation: surface water substitute for groundwater); CR-6 (more bids for a supply fixed in a year, A-8, raise its price) | A-8, A-1, A-2 |
| C-31 | buyers.surface_water.other_districts | quantity_substitute (surface water bought) | decrease | medium; long | invisible | B | CR-9 (competing for the same fixed supply); CR-4c (at a higher price, the last af is given up); CR-8a (water moved into the basin is withdrawn from other users) | A-8, A-1, A-2 |
| C-32 | neighboring_jurisdictions (Lowther landholders) | asset_value (Lowther irrigated land) | increase | short; medium | invisible | B | CR-9 (relation: across_border); CR-7a (growers who can move, A-9, bid for uncapped land); CR-7c (the gain settles on Lowther land, fixed in supply, until its own plan) | A-9 |
| C-33 | neighboring_jurisdictions (Lowther pumpers) | quantity_supplied (groundwater pumped in Lowther) | increase | medium | invisible | B | CR-4 (x: farm in Sorrel, y: farm in Lowther; x made worse by the cap, A-9); CR-7a | A-9 |
| C-34 | pumpers.non_domestic | full_cost_per_unit (energy to lift an af) | decrease | medium; long | invisible | C | CR-9 (relation: shared_facility; each pumper's pumping lowers the table for all; less pumping, C-1, lowers it more slowly, A-14); CR-10b (the saving accumulates, about $0.20 per af per foot); Tier C under CR-9 0.7 | A-14, A-2 |
| C-35 | pumpers.non_domestic | maintenance_spending (deepening and replacing wells) | decrease | long | invisible | C | CR-9 (shared_facility, A-14); CR-4 (x: deepen, y: keep the well as it is; fewer wells reach the point where deepening pays) | A-14 |
| C-36 | owners.domestic_wells | maintenance_spending (deepening and replacing dry wells) | decrease | long | invisible | C | CR-9 (shared_facility, A-14); CR-4 (fewer wells go dry) | A-14 |
| C-37 | county.emergency_water | subsidy_outlay (water for households with dry wells) | decrease | long | invisible | C | CR-9 (shared_facility, A-14); CR-8b (fewer households draw on the program) | A-14 |
| C-38 | input_suppliers (well drillers) | quantity_traded (well deepening and drilling) | decrease | medium; long | invisible | C | CR-9 and LW-10 (relation: drilling input_to well maintenance, which falls, C-35, C-36) | A-14 |
| C-39 | holders.history.tree_nuts | resources_available_other_uses | decrease | medium | invisible | B | CR-3 note (they keep buying water by leasing at C-6, where before it cost only energy); CR-8b (lease payments are lessors' receipts, C-40); CR-12e (lift savings are dominated, A-N3) | A-4, A-16, A-N3 |
| C-40 | holders.history.field_crops | resources_available_other_uses (lease receipts) | increase | medium | invisible | B | CR-8b (lease payments, C-39, are their receipts); CR-2 (they lease because they rank the receipts above farming the water, A-5). Item only (CR-12 0.8 two items) | A-4, A-5 |
| C-41 | holders.history | resources_available_other_uses (share fees) | decrease | medium; long | invisible | A | CR-1 (op 4: $10 per af of shares, not avoidable while holding shares); CR-3 note (a sum they cannot avoid); CR-8b (SBWA receipts, C-3). Item only | none |
| C-42 | holders.history.field_crops | resources_available_other_uses (total) | ambiguous | medium | invisible | B | CR-12b and CR-12 0.8 (two items in one variable): (+) lease receipts (C-40); (−) fees (C-41) and receipts lost on crops no longer grown on the cut 37% (CR-3a, CR-5a). No premise says which dominates | A-4, A-5, A-1, A-2 |

## Gaps found

**(a) Steps no core rule covers.**
- GAP-039-C1: The counterfactual "race" to pump a shared aquifer. CR-8 (0.8) says that ending a race frees means, and CR-9 (0.7) lets chains run through a shared facility at Tier C, but no core rule derives when unowned extraction from a common stock exceeds what owners of the stock would choose, or how the stock's decline feeds back on extraction (A-15). The policy's central intended effect and every long-run sign (C-10, C-11, C-12, C-27) rest on the premises A-14 and A-15 and on the Tier C relation.
- GAP-039-C2: Valuing a lottery entry. CR-7c and CR-10c value an asset by expected yields, and A-21 supplies the comparison; no rule says how an asset whose yield depends on a draw is valued (expected value or less), which matters for C-16 and C-18.

**(b) Core-rule wording that was hard to apply.**
- CR-9 0.7 (Tier C for shared facilities): applying it literally puts the main purpose of a groundwater cap (a slower-falling table and its savings) at Tier C, while the cap's effect on pumping itself is Tier B. The rule does not distinguish a physical common stock whose use the policy directly governs from incidental spillovers between neighbors.
- CR-12g and capitalization: horizons are not to be combined, but asset values (C-15, C-17) capitalize long-run effects, including Tier C ones, at the moment of expectation. It was unclear whether a long-run Tier C chain counts as an opposing chain for a short-run asset value; it was treated as one, and dominated where A-N3 applies.
- CR-12 0.7 and 0.8 on a Tier C opposing chain: the rules say a chain no rule derives is a Tier C note, but say nothing about a chain that is derived but Tier C because of its relation. Treated as a chain (ambiguous), with the consequence at Tier C.
- CR-6 0.7 (fixed quantity priced in a wider market) fitted well: the lease price rations the capped water. But the counterfactual price of the right is undefined (the right does not exist), so "increase" in C-6 is against the cost of water without a right (energy only).
- CR-7c 0.7 (claims before creation): the claim is captured "when the allocation rule becomes expected", but the qualifying date (1 July 2027) is later; parcels sold between March 2022 and July 2027 carried the claim, and the rule had to be read as giving the gain to the March 2022 holders, not to the holders on the issue date.

**(c) Vocabulary missing from the ontology.**
- No variable for the state of a shared resource stock (water table, depletion) or for extraction cost per unit; C-34 uses `full_cost_per_unit`, which is defined for buyers' money and non-money costs.
- No variable for pumping or own-use extraction; `quantity_supplied (groundwater pumped)` is used though most pumping is used by the pumper, not offered for sale.
- No variable for acreage farmed or land use (irrigated, fallowed, dry grazing).
- No variable for lottery entries; C-18 uses `reclassification` and C-19 `compliance_cost`.
- No generic actor class for holders of a created right as distinct from the land that earned it; `holders.history` and `lottery_winners` were added by role.
