# WE-039 Groundwater pumping cap with tradable shares allocated by history

Analyst: draft (Handbook 0.8, held-out test)  |  Rule catalog version: 0.8  |  Status: awaiting expert review

A stylized policy in a fictional basin. It resembles real groundwater sustainability plans but is not modeled on any one of them. It was chosen as a held-out test of catalog 0.8: a cap on an input (groundwater) whose output (crops) is priced in national markets (EN-6, 0.8 Unless; CR-6, 0.8), tradable rights allocated by a history that was fixed before the plan was proposed (CR-7c, 0.8: windfall rather than a race to qualify), a reserve allocated by lottery, where eligibility can still be earned, a pumping race that the cap ends (CR-8, 0.8: value created by ending a race), and an aquifer that every pumper shares, so that every chain through the water table runs over a `shared_facility` relation and is Tier C (CR-9, 0.7; Q20). It also tests the candidate patterns "consolidation under tradable rights" and "allocation of a right by history" from `06_gaps.md`, 6.2e. Effects on the environment (land subsidence, streams, habitat) are outside the scope of version 1. The probabilities are illustrative; the evidence column says what a real analysis would cite.

## 1. Policy record

**Sorrel Basin Groundwater Allocation Plan.** The Sorrel Basin, in the State of Castellan, is an alluvial aquifer under about 110,000 irrigated acres, divided by the state's hydrologic survey into three sub-basins: North, Central and South. Average pumping in water years 2017 to 2021 was about 300,000 acre-feet (af) a year: North 110,000 (mostly field crops: cotton, alfalfa, grain), Central 70,000 (mixed), South 120,000 (mostly tree nuts). Tree nuts use about 160,000 af on 40,000 acres; field crops about 140,000 af on 70,000 acres. The survey estimates the basin's long-run sustainable yield at about 200,000 af a year. Over 2017 to 2021 the water table fell about 2.5 feet a year on average and about 4 feet a year in South. Pumping lift averages about 300 feet; each foot of lift costs about $0.20 per af in energy. About 2,400 agricultural wells and about 4,000 domestic wells draw on the aquifer; about 60 agricultural wells a year were deepened or replaced (about $80,000 each), and about 150 domestic wells went dry in 2017 to 2021. The county runs an emergency water program for households with dry wells.

Crops are sold in national markets: the basin grows about 5% of the nation's tree nuts and under 1% of each field crop. Irrigated land sells for about $12,000 an acre (nuts) and $6,000 (field crops); dry grazing land for about $1,500. About 6,000 people work on farms in the basin. The Sorrel Irrigation District delivers canal water to about 30,000 acres in North; surface water also trades between districts in the region, at about $250 per af in normal years. To the east, the Lowther Basin has no cap; its plan is due in 2030.

Before March 2022 no allocation method had been proposed in the basin; the state's groundwater act allows allocation by history, by area or by auction. The Sorrel Basin Water Authority (SBWA) published its draft plan, including the 2017 to 2021 base period, on 15 March 2022. After hearings it adopted the plan on 18 November 2026. Shares are issued on 1 July 2027; the cap takes effect with the water year beginning 1 October 2027. No expiry; the cap is reviewed in 2032.

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Cap | `quota` | Groundwater pumped from the basin | Holders of non-domestic wells | 210,000 af a year (70% of the 2017 to 2021 average). | Domestic wells pumping under 2 af a year. |
| K2 Allocation by history | `rights_allocation` | 90% of the cap (189,000 af) | SBWA | Permanent shares of the annual cap, issued to whoever holds a parcel on 1 July 2027, in proportion to the parcel's average metered or estimated pumping in water years 2017 to 2021. A holder receives about 63% of its history. | — |
| K3 Reserve for new users | `rights_allocation` (lottery) | 10% of the cap (21,000 af) | SBWA | Permanent shares in blocks of 100 af, drawn by lottery in September 2027. Eligible: each parcel of at least 20 acres in the basin, held on 1 July 2027, with no K2 allocation; one entry per parcel; entry fee $500. | — |
| K4 Trading | Rule on transfers | K2 and K3 shares and annual allocations | Share holders | Shares may be sold, and a year's allocation leased, separately from land. "Allocations may be transferred between wells in the Basin, subject to the Authority's rules on local impacts." No carry-over between years. | — |
| K5 Enforcement and funding | Enforcement | K1 to K4 | SBWA | Meters with telemetry on every non-domestic well by 1 October 2027, at the owner's cost (about $3,000 a well); monthly readings; satellite checks of crop water use. Penalty $600 per af pumped over allocation; loss of shares for repeated violation. Funded by an annual fee of $10 per af of shares held (about $2.1 million a year). | — |

Unclear provision:
- U1, trading across sub-basins. K4 allows transfers "between wells in the Basin, subject to the Authority's rules on local impacts", and the plan's hydrology chapter says impacts are to be "managed by sub-basin". Reading U1-a: a share may be pumped only from a well in the sub-basin where the parcel that earned it lies. Reading U1-b: a share may be pumped anywhere in the basin; the impact rules only set conditions on individual wells (spacing, monitoring).

Readings get no probability; where a sign depends on one, each reading's sign is reported.

**Figures.** Without the cap, pumping would stay near 300,000 af and rise with new plantings (A-1). The cap removes about 90,000 af a year, 30% of base pumping. A history holder keeps 63% of its history; to keep pumping as before it must lease about 37% from others. A share's annual allocation, leased at a price p per af, is worth roughly p divided by the rate at which land is capitalized; at an illustrative $300 per af and 7%, a share for 1 af is worth about $4,300, and the K2 shares together about $800 million. Each foot of water table not lost saves about $0.20 per af on every af pumped from then on.

The counterfactual is the basin without the plan: pumping as landholders choose, the water table falling as it did in 2017 to 2021.

## 2. Classification

| Component | Rothbard type | Binding? | Rule families |
|---|---|---|---|
| K1 | Triangular toward buyers of water (who now buy it from share holders) and autistic for a pumper using its own well: by CR-1, removes the option of pumping above one's allocation (operation 1, where enforced; operation 3, a risk, where not). | Yes: 210,000 af against about 300,000 (A-1). | EN-6 (main clause for water; Unless for crops), CR-6 (0.7 and 0.8), CR-4, RS-1, RS-3, RS-4, RS-6, RS-16, TS-3 |
| K2 | Binary: the state creates an asset and gives it to holders of qualifying parcels (CR-1, operation 4 by way of a new tradable option, operation 2). | Yes | SB-4, CR-7c (0.7: claims before creation; 0.8: windfall), CR-8 (0.8: value created by ending a race), CR-10c |
| K3 | Binary: the same, by lottery among eligible parcels, with eligibility still open until 1 July 2027 | Yes | CR-7c (0.8: competing to qualify), CR-8c, RS-5, RS-8, CR-6 |
| K4 | Rule on the market for the created right | Yes | CR-5, CR-7a (candidate "consolidation under tradable rights"), CR-6 (0.8: a free price's rise) |
| K5 | Binary: funded from the policy's own revenue (a fee on shares held) | Yes | OC-3 (own revenue; right baseline), OC-2, CR-8c |

The aquifer is a common resource: one pumper's water lowers the table under every other well. That is a `shared_facility` relation (02_ontology.md, 2.8), not an exchange. Under CR-9's 0.7 clarification, every chain that runs through it (lift costs, well deepening, dry domestic wells, the long-run yield of the aquifer) is reported at Tier C pending Q20. This includes the race the cap ends.

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `landholders.history` | Holders, on 1 July 2027, of parcels with 2017 to 2021 pumping | Receive shares worth about 63% of history; may pump only their allocation plus what they lease or buy. |
| `landholders.history.march2022` | Those who held such parcels when the plan was proposed | The claim's value is capitalized into their land from then (CR-7c). |
| `landholders.no_history` | Holders of parcels without 2017 to 2021 pumping, including those who started pumping in 2022 to 2027 | Lose the option of pumping without a share; may enter the K3 lottery with each eligible parcel. |
| `lottery.entrants`, `lottery.winners` | Eligible parcel holders who enter, and those who win | Pay $500 an entry; winners get 100 af shares. |
| `growers.nuts` (`buyers.current` of water) | Tree-nut growers, mostly in South | Water's marginal value to them is high; they lease or buy shares. |
| `growers.field` | Field-crop growers, mostly in North | May fallow and lease out their allocation. |
| `growers.prospective` (`sellers.prospective`) | Would-be new irrigated farms | Must buy shares or win the lottery. |
| `farm_workers` | About 6,000 workers | Fewer acres farmed. |
| `input_suppliers` | Seed, fertilizer, chemicals, custom harvesting | Fewer acres farmed. |
| `buyers.substitutes` | Buyers of surface water transfers in the region | More bidders. |
| `neighboring_jurisdictions` | Landholders and farmers in the Lowther Basin | Some basin farmers rent or buy land there. |
| `neighbors` (domestic well owners) | About 4,000 households on exempt wells | The table falls more slowly (Tier C). |
| `buyers.crops` (national) | Buyers of tree nuts and field crops | Basin output falls; their price may move by a negligible amount. |
| `officials.enforcement` | SBWA | Meters, readings, satellite checks, trading registry, lottery. |
| `officials.county` | County emergency water program | Fewer dry domestic wells (Tier C). |
| `pumpers` | Everyone who pumps under K1 | Bear meters and reporting; face the lease price as the cost of each af. |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | `pumpers` | `quantity_supplied` (groundwater pumped in the basin) | decrease | short to medium (from October 2027) | CR-1, EN-6 | A-1, A-2 |
| C-2 | `landholders.history` | `asset_value` (claim to shares, capitalized into qualifying land from March 2022; the shares themselves from July 2027) | increase | short (part from 15 March 2022, the rest at adoption) | CR-7c (0.7: claims before creation; 0.8: windfall), CR-10c, SB-4 | A-1, A-2, A-3, A-12 |
| C-3 | `lottery.winners` | `asset_value` (K3 shares) | increase | short (September 2027) | CR-7c, SB-4 | A-1, A-2, A-3 |

C-1 is the cap's purpose. C-2 and C-3 are the created assets. A share is a claim on part of a capped quantity that people would pay to use (A-1), so it has a price (CR-6), and its value is captured by whoever receives it at creation (CR-7c). Because the claim travels with the parcel until 1 July 2027 (K2), its value entered land prices as soon as the base period was published and the plan became likely: part of the way from 15 March 2022, rising with each step toward adoption, the rest on 18 November 2026 (CR-7c, probability clause; A-12). Those who held qualifying land then captured it; buyers of such land in 2022 to 2027 paid for it in the price. And because the base period (2017 to 2021) had ended before any allocation method was proposed, no one could add to their history once the rule was expected: under CR-7c's 0.8 clarification the value is a windfall to its holders, with no part used up in competing to qualify. (If some pumpers had anticipated allocation by history before 2022 and pumped more to build history, part would have been used up; A-17, p = 0.2, below the cut-off.)

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-4 | `pumpers` | `right_lease_price` (annual allocations) | increase | short to medium | EN-6 (Unless), CR-6 (0.7: fixed quantity priced in a wider market; 0.8: a free price's rise) | A-1, A-2, A-4 |
| C-5 | `growers.field` | `quantity_supplied` (field crops grown in the basin) | decrease | short to medium | CR-4, CR-5, CR-7a, EN-6 | A-1, A-2, A-5, A-16 |
| C-6 | `growers.nuts` | `quantity_supplied` (tree nuts grown in the basin) | decrease | medium | CR-4, CR-6, EN-6 | A-1, A-2, A-4 |
| C-7 | `growers.field`, `growers.nuts` | `number_of_sellers` (farms irrigating in the basin) | decrease | medium | CR-5, CR-7a (candidate: consolidation under tradable rights) | A-4, A-5, A-16 |
| C-8 | `growers.nuts` (South) | `quantity_supplied` (groundwater pumped in South) | U1-a: decrease; U1-b: ambiguous | medium | CR-1, CR-4, CR-7a, CR-12b | A-1, A-2, A-16, A-22 |
| C-9 | `growers.prospective` | `entry_rate` (new irrigated farms in the basin) | decrease | medium | CR-1, CR-4 | A-1, A-2 |
| C-10 | `landholders.history`, `landholders.no_history` | `investment_target` (new irrigated plantings in the basin) | decrease | short (from March 2022) | CR-10a, CR-4 | A-1, A-20 |
| C-11 | `lottery.entrants` | `reclassification` (parcels split, or parcels without history moved into separate ownership, to create eligible entries before 1 July 2027) | increase | short (November 2026 to July 2027) | RS-5, RS-8, CR-7c (0.8: competing to qualify), CR-6 | A-13, A-21 |
| C-12 | `lottery.entrants` | `compliance_cost` (entry fees, surveys, legal work, subdivision applications) | increase | short | CR-8c, OC-2 | A-21 |
| C-13 | `pumpers` | `legal_breach` (pumping over allocation) | increase | short to medium | RS-3, CR-4 (x: comply, y: violate) | A-10 |
| C-14 | `growers.nuts`, `growers.field`, `landholders.no_history`, local water groups | `lobbying_effort` (South growers for basin-wide trading or a larger cap; North communities for limits on transfers south; non-history landholders for a larger reserve) | increase | short to medium | RS-7 | A-11 |
| C-15 | `growers.field`, `growers.nuts` | `quantity_substitute` (surface water bought through regional transfers) | increase | short to medium | RS-1, RS-16 | A-1, A-8 |
| C-16 | `growers.field`, `growers.nuts` | `cross_border_purchases` (land rented or bought in the Lowther Basin to farm with its groundwater) | increase | medium | RS-4 | A-1, A-9 |

**What rations the capped water (C-4).** The capped good, groundwater, has no price of its own before the plan; the goods it produces are priced nationally. So the price of crops does not ration the cap (EN-6 Unless; CR-6, 0.7). The lease price of an annual allocation does: those who value an af more than its lease price buy or lease; those who value it less lease theirs out (CR-6, CR-5). By CR-6's 0.8 clarification, a free price's rise satisfies the "at least one margin" conclusion on its own; no waiting or other non-price margin is signed. Under both readings of U1 lease prices rise against the counterfactual, where no right exists; the readings differ in their spread (under U1-a South's price is above North's; under U1-b they are brought together, net of transfer costs, CR-7a). That difference is one of size, not of sign against the counterfactual, so it is not recorded as a per-reading consequence (Gaps found, d).

**Who uses the water (C-5 to C-7).** A field-crop grower with an allocation can now pump it or lease it. Where the lease price exceeds what an af earns on field crops, the grower leases it out and fallows (CR-4, CR-5; A-5); the water moves to the uses that value it most, tree nuts (CR-7a; A-16). Field-crop output falls (C-5). Nut growers face a cost per af they did not face before: the lease price, or the lease income they forgo by pumping their own allocation. By CR-4 they pump no more than without the cap, and those at the margin pump less (C-6), even though they are the buyers of the field growers' water. Fewer farms irrigate, as allocations concentrate in the operations that value them most (C-7). This is the candidate pattern "consolidation under tradable rights", second use. Under U1-a, consolidation happens within each sub-basin; under U1-b, across the basin. The sign is the same.

**South under each reading (C-8).** South's growers hold about 75,600 af of shares against 120,000 of history. Under U1-a they may lease only within South, so South's pumping falls against the counterfactual. Under U1-b they may lease North's and Central's field-crop allocations (about 60,000 af), and South's pumping could approach or pass what it would have been without the cap (A-22, p = 0.5). That (+) chain is a chain the rules derive, with a premise at 0.5, so under CR-12's 0.8 clarification (kind 2) the sign under U1-b is `ambiguous`.

**Before the cap (C-9, C-10).** From the draft plan in March 2022, land without history has no claim to a share, and land with history will be cut to 63%. New plantings, which need water for decades, become less attractive from then (CR-10a; A-20), and new irrigated farms after 2027 need to buy shares (C-9). There is no rush to pump before October 2027: pumping in 2022 to 2027 earns no history, and water cannot be stored on the farm in any quantity. So RS-8 has no pumping window to move toward.

**The lottery (C-11, C-12).** The reserve shares are given at a price of $500 an entry, far below their value (21,000 af at the illustrative price is about $90 million, against perhaps 1,500 eligible parcels). The scarce side allocates by chance, and the gap pursues the open margin: the number of entries (CR-6). Eligibility is still open until 1 July 2027, so holders of large parcels without history split them, or move parts into separate ownership, to multiply entries (C-11; RS-5; A-13). By CR-7c's 0.8 clarification, part of the reserve's value is used up in this competition (CR-8c): surveys, legal work, subdivision fees (C-12). The K2 allocation has no such competition: its history was fixed.

**Evasion (C-13).** Over-pumping costs $600 per af if detected; leasing costs the lease price. Where detection is weak (wells without working telemetry, satellite checks that miss deficit irrigation), some pumpers over-pump (CR-4; A-10). The trade stays inside a legal activity, so it is `legal_breach`.

**Substitutes and relocation (C-15, C-16).** Surface water bought in the regional market substitutes for groundwater (RS-1, A-8); some growers farm across the line in Lowther, which has no cap until its plan (RS-4, A-9).

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-17 | `buyers.substitutes` | `price_substitute` (regional surface water transfers) | increase | short to medium | RS-16, CR-6 | surface water and groundwater: `substitute`, close where canals reach | A-1, A-8 |
| C-18 | `neighboring_jurisdictions` | `asset_value` (irrigated land in the Lowther Basin) | increase | medium | RS-4, CR-7c, CR-9 | basin and Lowther farmland: `across_border`, close | A-1, A-9 |
| C-19 | `farm_workers` | `employment`, `hours_worked` (farm work in the basin) | at_least_one_decrease | medium | RS-6, CR-9 | farm labor `input_to` crops | A-5, A-6 |
| C-20 | `input_suppliers` | `quantity_traded` (seed, fertilizer, custom harvesting sold in the basin) | decrease | medium | CR-9 | inputs `input_to` crops | A-5, A-7 |
| C-21 | `pumpers` | `full_cost_per_unit` (pumping energy per af) | decrease | medium to long | CR-9 (relation `shared_facility`: the aquifer; Tier C pending Q20), CR-8 (0.8: ending a race), CR-8a | aquifer: `shared_facility` | A-1, A-2, A-14 |
| C-22 | `pumpers` | `maintenance_spending` (deepening and replacing agricultural wells) | decrease | medium to long | CR-9 (`shared_facility`; Tier C), CR-8 (0.8), CR-8a | as C-21 | A-1, A-2, A-14 |
| C-23 | `neighbors` (domestic wells in North and Central) | `maintenance_spending` (deepening or replacing domestic wells) | decrease | medium to long | CR-9 (`shared_facility`; Tier C) | as C-21 | A-1, A-2, A-14 |
| C-24 | `neighbors` (domestic wells in South) | `maintenance_spending` (deepening or replacing domestic wells) | U1-a: decrease; U1-b: ambiguous | medium to long | CR-9 (`shared_facility`; Tier C), follows C-8 | as C-21 | A-1, A-2, A-14, A-22 |
| C-25 | `officials.county` | `enforcement_cost` (emergency water deliveries to dry domestic wells) | decrease | medium to long | OC-3 (right baseline), CR-9 (`shared_facility`; Tier C) | as C-21 | A-1, A-2, A-14 |
| C-26 | `pumpers` | `quantity_supplied` (groundwater pumped in the basin) | ambiguous | long | CR-9 (`shared_facility`; Tier C), CR-12b | as C-21 | A-1, A-2, A-15 |
| C-27 | `landholders.history` | `asset_value` (land and shares together, against irrigated land with free pumping) | ambiguous | short to medium | CR-7c, CR-12b (0.8: two items in one variable) | — | A-1, A-2, A-3, A-12 |
| C-28 | `landholders.no_history` | `asset_value` (land, with its lottery entries) | ambiguous | short | CR-7c, CR-10c, CR-12b | — | A-1, A-2, A-12, A-21 |

**The race the cap ends (C-21 to C-26).** Without the cap, each pumper's water lowers the table under every other well, and none gains by pumping less alone: water left in the ground is pumped by the neighbors. The resulting fall of 2.5 feet a year raises everyone's lift cost and forces deepening of wells. Under the cap, total pumping is near the sustainable yield, so the table falls much more slowly (A-14). Lift energy per af is lower than it would have been (C-21), fewer wells need deepening (C-22, C-23), and the county trucks water to fewer dry wells (C-25). Every one of these links runs over the aquifer, a `shared_facility`: one pumper's action changes what is available to others without an exchange. Under CR-9's 0.7 clarification they are Tier C.

**CR-8's 0.8 clarification (value created by ending a race).** The value of the shares (C-2, C-3) has two parts. One part is means no longer used up: the energy and well deepening of C-21 and C-22, which no one pays (CR-8a). The rest is a transfer under CR-8b, with payers to name: those whose pumping the cap removes without giving them a matching share, that is, landholders without history who pumped or would have pumped (C-28's (−) chain), would-be new farms (C-9), and the history holders themselves for the 37% of their pumping they give up (C-27's (−) chain). The first part rests on the Tier C link. So the clarification can be applied here only at Tier C: the method cannot say at Tier B how much of the shares' value is created rather than transferred.

**Holders of history: two items (C-2, C-27).** Under CR-12's 0.8 clarification on two items in one variable, the share (C-2, increase) and the land and share together (C-27) are recorded separately. Against the counterfactual, a history holder has a share worth about 63% of its history (+), lower lift and well costs (+, Tier C), and the loss of the option to pump as much as it likes (−). No premise ranks these, so C-27 is `ambiguous`; it is ambiguous on its Tier B chains alone, so it stays Tier B. CR-7c's "windfall" is the value of the created asset; it is not a net gain to its holders.

**Land without history (C-28).** Such land loses the option of pumping without a share (−, from March 2022). An eligible parcel gains a lottery entry (+, from adoption in November 2026). Ambiguous.

**Long-run pumping (C-26).** In the long run the counterfactual race may itself cut pumping: as the table falls, wells fail and pumping becomes too costly, so the aquifer yields less (A-15). Against that, the cap holds pumping at 210,000 af. The (+) chain runs over the shared facility and is Tier C; the (−) chain is Tier B. Under CR-12d a consequence takes the lowest tier in its chains, so the long-run sign is `ambiguous` at Tier C (Gaps found, b). In the short and medium run, before the counterfactual depletion would bind, C-1 stands.

**Crops in national markets (EN-6 Unless; CR-6, 0.8).** The basin's output of field crops falls (C-5), but it is under 1% of national output, so national field-crop prices move in the CR-6 direction by a negligible amount. EN-6's 0.8 Unless allows a choice: record `price_paid` as `increase` with a premise that the effect is not negligible, or note it as negligible. Here the premise is A-18 (p = 0.15) for field crops and A-19 (p = 0.3) for tree nuts (5% of national output, with basin output falling less than for field crops): both below the cut-off, so they are noted, not reported. The same holds for growers elsewhere (`net_price_received`, increase, negligible).

**Surface water (C-17).** Regional surface water is fixed by the year's allotments, so more bidders raise its price (RS-16, A-8).

**Lowther (C-18).** Growers who farm across the line raise the demand for Lowther's irrigated land, whose supply is fixed; its value rises (CR-7c, A-9), and more so if Lowther's own plan is expected to allocate by history from a later base period. The pumping it adds in Lowther lowers Lowther's table (Tier C); not followed (depth 3).

Stopping points. Farm workers' and input suppliers' other spending, and the basin towns' sales: depth 3, diffuse; stopped. Subsidence, streams and habitat: out of scope.

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `landholders.history`, `asset_value` (land and shares together), short to medium | Share worth 63% of history (C-2); lower lift and well costs (C-21, C-22; Tier C). | Loss of the option to pump without limit; 37% of history cut. | None | **ambiguous** (C-27). The share alone is an increase (C-2), recorded as its own item (CR-12, 0.8). |
| `landholders.no_history`, `asset_value`, short | Lottery entry for eligible parcels (K3). | Loss of the option to pump without a share. | None | **ambiguous** (C-28). For parcels too small to enter, a decrease, but those are mostly domestic users, exempt. |
| `pumpers`, `quantity_supplied` (basin), short to medium | None. | The cap (C-1). | None needed | **decrease** (C-1). |
| `pumpers`, `quantity_supplied` (basin), long | The counterfactual race would deplete the aquifer and cut pumping (Tier C, A-15). | The cap (C-1). | None | **ambiguous** at Tier C (C-26). |
| `growers.nuts` (South), `quantity_supplied` (groundwater pumped in South), medium | Under U1-b, allocations leased in from North and Central (A-22). | The cap on South's own shares (C-1). | None | **U1-a: decrease; U1-b: ambiguous** (C-8). |
| `pumpers`, `full_cost_per_unit` (water to the marginal user: lease price plus energy), medium | The lease price, now a cost of each af used (C-4). | Lower lift energy (C-21, Tier C). | None | **ambiguous** at Tier C (C-29). The energy item alone is C-21 (CR-12, 0.8: two items in one variable). |
| `growers.nuts`, `quantity_supplied` (tree nuts), medium | Allocations leased from field growers (C-5's water). | The cap; the lease price as a cost of each af (CR-4). | CR-12e: leasing is a response to the cap and cannot raise nut growers' water above what they would pump with no cap and no lease price. | **decrease** (C-6). |
| `neighbors` (South), `maintenance_spending`, medium to long | Under U1-b, pumping concentrated in South (C-8). | The cap (C-1). | None | **U1-a: decrease; U1-b: ambiguous** (C-24, Tier C). |

## 8. Time structure

- **March 2022 to November 2026: expectation.** As adoption becomes more likely, qualifying land rises in value relative to land without history (C-2, C-28), and new plantings fall (C-10). The base period has ended, so pumping in these years earns no history and no race to qualify arises for K2. The counterfactual race to pump against the falling table continues until the cap takes effect.
- **November 2026 to July 2027: the lottery window.** Eligibility is fixed on 1 July 2027, so parcel splitting and transfers bunch in these months (C-11, C-12). Without the policy, such splitting would happen at its ordinary rate; this is a rise in the window against the counterfactual, with no matching dip after, because the incentive ends rather than moves.
- **From October 2027: the cap.** Lease prices form in the first irrigation season (C-4). Fallowing and leasing out are quick (C-5); the move of nut growers' water purchases and of farms' numbers (C-6, C-7) and the move of some farming to Lowther (C-16) take several seasons. Tree nuts are long-lived: orchards are pulled out only as they age or when the lease price exceeds their return for some years (TS-1).
- **The water table (Tier C).** The table falls more slowly from the first year of the cap, and the savings in lift energy and well work build each year against the counterfactual, where the fall continues (C-21 to C-25).
- **Review in 2032 (TS-3).** The cap is a physical quantity. If the review lowers it toward 200,000 af, share holders bear the cut on their holdings when it becomes expected (CR-7c); the plan says shares are fractions of the cap, so they shrink in af, not in number.
- **Lowther's plan (2030).** If Lowther adopts a cap that allocates by a later history, land farmed there by Sorrel growers from 2027 may earn history; that would be a race to qualify there (CR-7c, 0.8). Not followed.

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-30 | `officials.enforcement` (SBWA) | `enforcement_cost` | increase | Staff, meter reading, satellite checks, registry and lottery. | OC-3, CR-8c |
| C-31 | `landholders.history`, `lottery.winners` (share holders) | `resources_available_other_uses` (the $10 per af fee) | decrease | What the fee would otherwise buy; it is unavoidable while the share is held. | OC-3, CR-8b, CR-3 |
| C-32 | `pumpers` | `compliance_cost` (meters, telemetry, monthly reporting, transfer applications) | increase | About $3,000 a well for meters, and the time spent reporting. | OC-2, CR-8c |
| C-33 | `pumpers` | `compliance_cost` (applications and impact reviews for transfers to wells in another sub-basin) | U1-a: no_change; U1-b: increase | Time and fees spent on cross-sub-basin transfers, which exist only under U1-b. | CR-1, CR-8c |
| C-34 | `growers.field`, `farm_workers`, `buyers.crops` | `quantity_traded` (crops grown and sold from the fallowed water) | decrease | The crops not grown. Growers who lease out their water gain by their own ranking (CR-5); the exchanges prevented are those that water would have supported without the cap. | OC-4, CR-5a |

**OC-3, who pays, and the right baseline.** K5 funds the SBWA from a fee on shares held: "from the policy's own revenue". The fee reduces what holders get from their shares, and is capitalized into their value (CR-7c), so it is borne by those holding shares at issue (C-31). The baseline is enforcement without the plan, not zero: the county's emergency water program for dry domestic wells shrinks (C-25), and well-interference disputes between neighbors may too. Those are different budgets from the SBWA's and run over the aquifer (Tier C), so the SBWA's cost is signed alone at Tier A (C-30) and the county's saving separately at Tier C; they are not netted.

**Prevented exchanges.** The fallowed acres' crops (C-34). Leasing itself is voluntary and gains both sides (CR-5).

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | Without the cap, pumping would stay near 300,000 af and above 210,000. | binding | 0.95 | 2017 to 2021 average; plantings since. | The cap does not bind; nothing follows. |
| A-2 | The cap is enforced against most pumpers: meters, telemetry and satellite checks detect most over-pumping. | enforcement | 0.75 | K5; telemetry reliability; penalty above likely lease prices. | C-1 and every consequence that follows from it shrink; C-13 grows. |
| A-3 | Holders expect shares to last, without early reallocation. | expectations | 0.75 | Shares are permanent; the review in 2032 may scale them but not reassign them. | C-2, C-3, C-27 and C-31 are smaller. |
| A-4 | A lease market forms: transaction costs are low enough for holders to lease to others within a season. | other | 0.8 | SBWA registry; leasing in surface water districts nearby. | C-4, C-6 and C-7 are smaller; water stays with its allocated holders. |
| A-5 | Some field-crop growers value lease income above farming their allocation. | alternative_uses | 0.75 | Net returns per af of field crops against likely lease prices. | C-5, C-7, C-19 and C-20 come from the cap alone, proportionally. |
| A-6 | Farm employment and hours adjust to acres farmed. | alternative_uses | 0.75 | Labor per acre by crop. | C-19 is not reported. |
| A-7 | Input suppliers sell mainly to basin farms. | other | 0.6 | Dealer locations and sales areas. | C-20 is not reported. |
| A-8 | Some basin farms can buy regional surface water, whose supply is fixed by allotments in a given year. | substitutability | 0.65 | Canal reach in North; regional transfer market. | C-15 and C-17 are not reported. |
| A-9 | Some basin growers can farm in the Lowther Basin, which has no cap until its plan. | mobility | 0.55 | Distance; Lowther land listings; growers already farming both. | C-16 and C-18 are not reported. |
| A-10 | Detection is weak for some wells, so some pumpers over-pump. | enforcement | 0.55 | Telemetry failure rates; experience in other basins. | C-13 is not reported. |
| A-11 | South growers, North communities and landholders without history can organize at a cost below their stake. | other | 0.85 | Growers' associations; hearing records 2022 to 2026. | C-14 is not reported. |
| A-12 | Land buyers priced the expected claim to shares from the publication of the draft plan. | expectations | 0.75 | Land sale prices with and without history after March 2022. | C-2's 2022 part, C-27 and C-28 date from adoption instead. |
| A-13 | Parcels can be split or transferred into separate ownership before 1 July 2027 (lot-line adjustments approved within months). | other | 0.6 | County processing times. | C-11 is smaller and limited to transfers. |
| A-14 | Under the cap, the water table falls more slowly than it would have. | other | 0.85 | Survey's model: 210,000 af against a sustainable yield of 200,000 and counterfactual pumping of 300,000. | C-21 to C-25 are not reported. |
| A-15 | Without the cap, continued decline would make enough wells fail or become uneconomic to cut pumping in the long run. | counterfactual_trend | 0.6 | Saturated thickness in South; depth of wells. | The (+) chain of C-26 fails; long-run pumping is a decrease. |
| A-16 | Tree nuts earn more per af than field crops for most growers. | other | 0.85 | Crop budgets. | C-5, C-7 and the direction of transfers under U1-b weaken. |
| A-17 | Some pumpers inflated 2017 to 2021 pumping in anticipation of allocation by history. | expectations | 0.2 | No method proposed before March 2022; the act allowed several. | Below the cut-off: not reported. If true, part of K2's value was used up (CR-7c, 0.8; CR-8c). |
| A-18 | The fall in basin field-crop output moves national field-crop prices by more than a negligible amount. | other | 0.15 | Basin share under 1% of each crop. | Below the cut-off: national `price_paid` for field crops (increase) is noted as negligible, not reported. |
| A-19 | The fall in basin tree-nut output moves national tree-nut prices by more than a negligible amount. | other | 0.3 | Basin share about 5%; nut output falls less than field crops. | Below the cut-off: noted as negligible, not reported. |
| A-20 | Landholders planning new orchards gave weight to the draft plan from 2022. | expectations | 0.7 | Planting permits and nursery orders 2022 to 2026. | C-10 is not reported. |
| A-21 | The lottery's expected value per entry exceeds the cost of entering for many eligible parcels. | other | 0.85 | Reserve worth about $90 million at illustrative prices; $500 fee. | C-11, C-12 and the (+) chain of C-28 are not reported. |
| A-22 | Under U1-b, South growers could lease in enough North and Central allocations to approach or pass South's counterfactual pumping. | other | 0.5 | South's cut about 44,000 af below history, more below its trend; about 60,000 af of field-crop shares elsewhere. | C-8 and C-24 under U1-b become decreases. |

## 11. Report

**The policy.** From October 2027 the Sorrel Basin Water Authority caps groundwater pumping at 210,000 acre-feet a year, 70% of the 2017 to 2021 average. Ninety percent of the cap is issued as permanent, tradable shares to parcels in proportion to their pumping in 2017 to 2021, the five years before the plan was proposed; 10% goes by lottery to parcels with no history. Shares can be sold or leased apart from land. Whether they can be pumped outside the sub-basin where they were earned is unclear.

**Visible consequences.** Less groundwater is pumped (C-1). Holders of qualifying land receive shares of substantial value (C-2), and lottery winners too (C-3).

**Invisible consequences.**
- *Who gets the value.* The value of the history shares went to those who held qualifying land when the plan became expected, from 2022 (C-2); because the history was already fixed, none of it was used up in a race to qualify. That windfall is the share, not a net gain: against free pumping, holders' land and shares together may be worth more or less (C-27). Land without history loses the option to pump freely and gains a lottery ticket (C-28). The lottery draws parcel splitting and paperwork before its eligibility date (C-11, C-12).
- *Who uses the water.* A lease price appears and rations the cap (C-4). Field-crop growers lease to nut growers and fallow (C-5); nut growers still pump less than they would have (C-6); fewer farms irrigate (C-7). Fewer new farms start (C-9), and new plantings fell from 2022 (C-10).
- *Around the basin.* Farm jobs or hours (C-19) and input sales (C-20) fall. Growers buy more surface water, at higher prices (C-15, C-17), and some farm in the Lowther Basin, raising land values there (C-16, C-18). Some over-pump (C-13); groups lobby over the cap, the reserve and transfers (C-14).
- *The water table (Tier C).* Lift energy per acre-foot (C-21), deepening of farm wells (C-22) and of domestic wells (C-23) fall against the counterfactual, and so do the county's emergency water deliveries (C-25). These run through the shared aquifer and are Tier C.
- *Costs.* The authority's enforcement (C-30), paid by share holders through the fee (C-31); meters and reporting for pumpers (C-32); crops not grown on fallowed land (C-34).

**Per reading of U1.** If shares can be pumped only in their own sub-basin (U1-a), South pumps less than it would have, and its domestic wells fare better (C-8, C-24). If they can move anywhere (U1-b), South may pump about as much as it would have, and those signs are ambiguous; cross-sub-basin transfers bring applications and reviews (C-33).

**Ambiguous effects.** Holders' and non-holders' land values (C-27, C-28); the full cost of water to the marginal user (C-29); long-run pumping (C-26, Tier C), since without the cap the aquifer might have yielded less in the end.

**Key conditions.** Enforcement (A-2, p = 0.75); that the lease market works (A-4, p = 0.8); the hydrology (A-14, p = 0.85), on which every Tier C claim rests; for U1-b, how much water would move south (A-22, p = 0.5). National crop prices move in the expected direction but by amounts too small to record (A-18, A-19).

**What this analysis cannot say.** How large any effect is; how much of the shares' value is created by ending the race and how much is taken from those cut without shares (only at Tier C); whether the plan is fair to those who began pumping after 2021; subsidence, streams and habitat (out of scope for version 1); whether the policy is desirable.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | pumpers | quantity_supplied (groundwater pumped) | decrease | short–medium | visible | B | CR-1, EN-6 | A-1, A-2 |
| C-2 | landholders.history | asset_value (claim to shares; the shares) | increase | short | visible | B | CR-7c, CR-10c, SB-4 | A-1, A-2, A-3, A-12 |
| C-3 | lottery.winners | asset_value (K3 shares) | increase | short | visible | B | CR-7c, SB-4 | A-1, A-2, A-3 |
| C-4 | pumpers | right_lease_price | increase | short–medium | invisible | B | EN-6, CR-6 | A-1, A-2, A-4 |
| C-5 | growers.field | quantity_supplied (field crops) | decrease | short–medium | invisible | B | CR-4, CR-5, CR-7a, EN-6 | A-1, A-2, A-5, A-16 |
| C-6 | growers.nuts | quantity_supplied (tree nuts) | decrease | medium | invisible | B | CR-4, CR-6, EN-6, CR-12e | A-1, A-2, A-4 |
| C-7 | growers.field, growers.nuts | number_of_sellers (irrigating farms) | decrease | medium | invisible | B | CR-5, CR-7a | A-4, A-5, A-16 |
| C-8 | growers.nuts (South) | quantity_supplied (groundwater pumped in South) | U1-a: decrease; U1-b: ambiguous | medium | invisible | B | CR-1, CR-4, CR-7a, CR-12b | A-1, A-2, A-16, A-22 |
| C-9 | growers.prospective | entry_rate (new irrigated farms) | decrease | medium | invisible | B | CR-1, CR-4 | A-1, A-2 |
| C-10 | landholders.history, landholders.no_history | investment_target (new plantings) | decrease | short | invisible | B | CR-10a, CR-4 | A-1, A-20 |
| C-11 | lottery.entrants | reclassification (parcel splits and transfers) | increase | short | invisible | B | RS-5, RS-8, CR-7c, CR-6 | A-13, A-21 |
| C-12 | lottery.entrants | compliance_cost (entries, surveys, subdivision) | increase | short | invisible | B | CR-8c, OC-2 | A-21 |
| C-13 | pumpers | legal_breach (over-pumping) | increase | short–medium | invisible | B | RS-3, CR-4 | A-10 |
| C-14 | growers, landholders.no_history, local groups | lobbying_effort | increase | short–medium | invisible | B | RS-7 | A-11 |
| C-15 | growers.field, growers.nuts | quantity_substitute (surface water transfers) | increase | short–medium | invisible | B | RS-1, RS-16 | A-1, A-8 |
| C-16 | growers.field, growers.nuts | cross_border_purchases (land rented or bought in Lowther) | increase | medium | invisible | B | RS-4 | A-1, A-9 |
| C-17 | buyers.substitutes | price_substitute (surface water transfers) | increase | short–medium | invisible | B | RS-16, CR-6 | A-1, A-8 |
| C-18 | neighboring_jurisdictions | asset_value (Lowther irrigated land) | increase | medium | invisible | B | RS-4, CR-7c, CR-9 | A-1, A-9 |
| C-19 | farm_workers | employment, hours_worked | at_least_one_decrease | medium | invisible | B | RS-6, CR-9 | A-5, A-6 |
| C-20 | input_suppliers | quantity_traded (farm inputs in the basin) | decrease | medium | invisible | B | CR-9 | A-5, A-7 |
| C-21 | pumpers | full_cost_per_unit (pumping energy per af) | decrease | medium–long | invisible | C | CR-9 (shared_facility), CR-8, CR-8a | A-1, A-2, A-14 |
| C-22 | pumpers | maintenance_spending (deepening farm wells) | decrease | medium–long | invisible | C | CR-9 (shared_facility), CR-8, CR-8a | A-1, A-2, A-14 |
| C-23 | neighbors (North, Central) | maintenance_spending (domestic wells) | decrease | medium–long | invisible | C | CR-9 (shared_facility) | A-1, A-2, A-14 |
| C-24 | neighbors (South) | maintenance_spending (domestic wells) | U1-a: decrease; U1-b: ambiguous | medium–long | invisible | C | CR-9 (shared_facility), CR-12b | A-1, A-2, A-14, A-22 |
| C-25 | officials.county | enforcement_cost (emergency water deliveries) | decrease | medium–long | invisible | C | OC-3, CR-9 (shared_facility) | A-1, A-2, A-14 |
| C-26 | pumpers | quantity_supplied (groundwater pumped) | ambiguous | long | invisible | C | CR-9 (shared_facility), CR-12b, CR-12d | A-1, A-2, A-15 |
| C-27 | landholders.history | asset_value (land and shares together) | ambiguous | short–medium | invisible | B | CR-7c, CR-12b | A-1, A-2, A-3, A-12 |
| C-28 | landholders.no_history | asset_value (land with lottery entries) | ambiguous | short | invisible | B | CR-7c, CR-10c, CR-12b | A-1, A-2, A-12, A-21 |
| C-29 | pumpers | full_cost_per_unit (lease price plus energy, marginal user) | ambiguous | medium | invisible | C | CR-6, CR-9 (shared_facility), CR-12b | A-1, A-2, A-4, A-14 |
| C-30 | officials.enforcement (SBWA) | enforcement_cost | increase | short–long | invisible | A | OC-3, CR-8c | none |
| C-31 | landholders.history, lottery.winners | resources_available_other_uses (fee) | decrease | short–long | invisible | B | OC-3, CR-8b, CR-3 | A-3 |
| C-32 | pumpers | compliance_cost (meters, reporting) | increase | short | invisible | A | OC-2, CR-8c | none |
| C-33 | pumpers | compliance_cost (cross-sub-basin transfer applications) | U1-a: no_change; U1-b: increase | short–medium | invisible | B | CR-1, CR-8c | A-4 |
| C-34 | growers.field, farm_workers, buyers.crops | quantity_traded (crops from fallowed water) | decrease | medium | invisible | B | OC-4, CR-5a | A-1, A-2 |

## Gaps found

**(a) Calculus gaps (a step no core rule covers).** None new. Every chain through the water table rests on the `shared_facility` relation, which is GAP-026-1 (CR-9, 0.7; Q20, open): it is covered by a core rule, at Tier C. The step closest to a new gap is the long-run counterfactual: that the aquifer, pumped without a cap, would itself yield less in the end (C-26). CR-9 and CR-10b derive it, but only over the shared facility.

**(b) Unclear core rules.**
1. *Combining a Tier B chain with an opposing Tier C chain (CR-12d, CR-9 0.7).* CR-12 0.8 lists three kinds of opposing chain, but not a chain that is derived and well supported (A-15, p = 0.6) yet Tier C because it runs over a shared facility. Read here as CR-12d says: the combined consequence takes the lowest tier, so C-26 and C-29 are `ambiguous` at Tier C. The alternative reading, that a Tier C chain is a "suggestion" and leaves the Tier B sign standing (like CR-12 0.7's underivable chain), would give C-26 a decrease at Tier B. The rules should say which.
2. *CR-8 0.8 (ending a race) depends on Tier C.* Where the race is over a common resource (an aquifer, a fishing ground), the part of the rights' value that is "means no longer used up" exists only through a `shared_facility` link. So the clause can only be applied at Tier C, and the split between created value and transfer cannot be stated at Tier B. This is not in the clause's text.
3. *CR-7c 0.8, windfall versus net gain.* The clause says the value of a right whose history was fixed is "a windfall to its holders". Read literally, that could be recorded as a gain to the holders. Here the same holders lose 37% of their pumping, so the windfall is the value of one item (the share), not their net position (C-2 against C-27). The clause would be clearer if it said "the value of the right is captured without competition", and pointed to CR-12's two-items clarification for the holder's total.
4. *EN-6 Unless, and a cap on an input.* The Unless clause speaks of "the capped good's price set in a wider market". Here the capped good (groundwater) has no wider market; its output does. Read as: the right's lease price rations the input (CR-6 0.7), and the output's national price moves in the CR-6 direction, negligible here. That reading needed CR-9 (`input_to`) as a link the clause does not mention.

**(c) Missing or wrong patterns.**
1. *Candidate "consolidation under tradable rights"* (6.2e, from WE-028). Needed here (C-5, C-7), with one change: rights move to the users who value them most (here, by crop), not only to the lowest-cost producers of one good. Derivation CR-5, CR-7a, as listed. Second use: by the catalog's rule this promotes it.
2. *Candidate "allocation of a right by history after announcement"* (6.2e, from WE-028). Needed in its other branch: history fixed **before** announcement, so no race to qualify (CR-7c 0.8 windfall), while a second allocation channel (the lottery) leaves eligibility open and draws a competition to qualify (C-11, C-12). A pattern "allocation of a created right" should cover history before and after announcement, and lotteries with open eligibility. Second use, in a wider form.
3. *EN-6 applied as written.* EN-6's main clause gives `price_paid` increase for the capped good; here there is no price paid for groundwater, only the new lease price. No sign was overridden, because the Unless clause applies, but only by reading "a good priced in a wider market" as including the output of a capped input (b4).
4. *A per-reading difference in size.* U1 changes the spread of lease prices and share values between sub-basins (section 5) without changing their signs against the counterfactual. No pattern or recording rule captures a reading that matters only for size or for relative prices between segments.

**(d) Vocabulary.**
1. No variable for the stock of a shared resource (the water table, a fish stock). Its effects were recorded through `full_cost_per_unit` (lift energy) and `maintenance_spending` (wells); the stock itself is unrecorded.
2. No way to record a per-reading difference that is not a difference in sign against the counterfactual (relative lease prices between sub-basins under U1-a and U1-b).
3. No actor class for holders of a created right as distinct from `factor_owners.specific`; used `landholders.history` and `lottery.winners`.
4. `rights_allocation` (2.3) lists "history, auction or lottery" but not the date of the qualifying history relative to announcement, which decides between windfall and race (CR-7c 0.8). Proposed field: `qualifying_period_fixed_before_announcement: yes/no`.

**(e) Test of 0.8.**
- *EN-6 0.8 Unless (the wider-market price still moves).* Needed interpretation: the capped good is an input with no wider market; the clause was applied to its output via CR-9 (b4). Once so read, its choice ("record with a premise, or note as negligible") worked well: both crops noted as negligible with premises below the cut-off (A-18, A-19).
- *CR-6 0.8 (wider-market price; a free price's rise is enough).* Worked as written: the lease price alone satisfies the margin conclusion (C-4); no non-price margin signed.
- *CR-7c 0.8 (windfall where history was fixed; competition where it is not).* Worked as written for the two channels: K2 is a windfall with no race (C-2), K3's open eligibility draws a competition to qualify (C-11, C-12). Needed interpretation on "windfall to its holders": the windfall is the right's value, not the holders' net gain (b3).
- *CR-7c 0.7 (claims before creation).* Worked as written: the claim travels with land from March 2022 and is capitalized then (C-2, A-12).
- *CR-8 0.8 (value created by ending a race).* Worked in logic, failed in tier: the "means no longer used up" part runs over the aquifer and so is Tier C; the clause cannot separate created value from transfer at Tier B (b2).
- *CR-9 0.7 (`shared_facility`, Tier C, Q20).* Worked as written, with a large consequence: every effect of ending the race, which is the plan's stated purpose, is Tier C (C-21 to C-26). How a Tier C chain combines with an opposing Tier B chain is unclear (b1).
- *CR-12 0.8 (three kinds of opposing chain).* Worked as written for kind 2 with p ≥ 0.5 (A-22, C-8 under U1-b). Does not cover an opposing chain that is Tier C (b1).
- *CR-12 0.8 (two items in one variable).* Worked as written: shares against land and shares together (C-2, C-27); energy against total cost of water (C-21, C-29).
- *CR-12e 0.8 (response argument binds the response as a whole).* Worked as written for nut growers' output (C-6): leasing as a response cannot raise their water above the no-cap level.
- *OC-3 0.8 (right baseline).* Worked, with care: the enforcement the plan makes less necessary (county emergency water) is on a different budget and runs over the aquifer, so it was signed separately at Tier C rather than netted (C-25, C-30).
- *RS-16.* Worked as written for surface water (C-17).
- *Candidates from 6.2e.* "Consolidation under tradable rights": needed, second use (c1). "Allocation of a right by history": needed, in its fixed-history branch and with a lottery (c2).
