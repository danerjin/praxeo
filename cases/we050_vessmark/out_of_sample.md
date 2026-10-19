# Out-of-sample run of the prohibition rules on WE-050 (Vessmark Clean Cars Act)

Rules as at commit 9c6d2e9 (`praxeo/rules/prohibition.lp`, written from WE-017 only). Record: `record.json`, three components. K1 (end of sale of new combustion cars) and K2 (PHEVs from 2038) are `prohibition`; K5 (the $250 road charge) is `lump_sum_tax`. K3 (the saving clause) and K4 (enforcement, a fixed budget with no new funds) are not components: K3 is a source sentence of K1, K4 is K1's and K2's `enforcer_actor` with `general_budget` false. U1 is recorded with `reading_fields`: under U1-a K1 also bans used imports (`importer_actor` = `importers.used`, no definition line); under U1-b it does not. Answers: `answers.json`, 17 questions (K1 9, K2 8), from WE-050's assumption table where a row matches (A-2, A-4, A-7, A-14, A-15, A-21, A-25) and judged from the text otherwise. Run: `python3 -m praxeo cases/we050_vessmark --out cases/we050_vessmark/sample_run`; no verifier or citation problems. Test: `tests/test_oos_we050.py`.

Instrument choice. The handbook classes K1 as `product_standard` (EN-14: the good stays legal, the stock is exempt, new units below a specification are forbidden). `product_standard` has no rules, so the run would have been empty. The record uses `prohibition` for K1 and K2, as a parser reading "the Registry shall not register ... a new passenger car fitted with an internal combustion engine" could; this puts the prohibition rules to a test they were not written for. K5 uses `lump_sum_tax` (ontology 2.3), which has no rules either. Both choices are findings, not fixes.

Summary: the table has 47 rows (C-1 to C-48 without the removed C-6). The engine produces 28 consequences, 18 of them reported. Table rows produced by key: 6 (C-1, C-2, C-5, C-14, C-18, C-35), of which C-18 for only some of its classes. Rows not produced: 41. Engine rows classified WRONG: 4.

## Engine rows (reported)

| Engine row | Class | Why |
|---|---|---|
| buyers.new_combustion quantity_traded decrease | in table | C-1 |
| importers quantity_traded decrease | in table | C-1 and C-2 (the bound role stands for importers and dealers) |
| buyers.new_phev quantity_traded decrease | in table | C-2 |
| buyers.new_combustion quantity_substitute increase | in table | C-5 (new BEVs); the substitute is not named, RS-1 only signs the quantity of the substitute |
| importers.used reclassification (U1-a: no_change; U1-b: increase) | in table | C-14, both readings |
| officials.enforcement enforcement_cost increase | in table | C-35 (OC-3, no general budget) |
| importers lobbying_effort increase | in table (part) | C-18, through "dealers" matched to the bound role; fuel retailers, motoring clubs, BEV importers and charging firms have no role |
| buyers.new_combustion, buyers.new_phev lobbying_effort increase | defensible | RS-7 for the buyers; the table names the motoring clubs, the organized part of them (A-15) |
| buyers.new_combustion, buyers.new_phev quantity_demanded decrease | defensible | same direction as C-1 and C-2, but derived through the risk price below |
| buyers.new_phev quantity_substitute increase | defensible | RS-1 for K2's buyers; C-5 has it for K1's |
| buyers.new_phev quantity_demanded increase, window announcement | defensible | RS-8 for the 2038 date; the handbook keeps bunching inside the PHEV window as a path note (section 8, item 5) |
| importers.used quantity_traded (U1-a: decrease; U1-b: no_change) | defensible, half | U1-a is C-13. Under U1-b the engine derives nothing where the table says increase: an omission |
| **buyers.new_combustion price_paid increase** | **WRONG** | EN-7 with CR-7: the risk price of an informal trade. A new combustion car cannot be registered, so there is no informal trade at a risk price (A-2 at 0.95; the evasion row A-14 is below the cut-off). The question `enforcement_risk` was answered yes for a different reason (registration is refused), which the rule reads as informal sellers facing punishment. The table has no price for the banned cars and signs C-38 `no_change` for new BEVs |
| **buyers.new_phev price_paid increase** | **WRONG** | the same, for K2 |
| **buyers.new_combustion quantity_demanded increase, window announcement** | **WRONG** | RS-8's rush alone. C-9 is `ambiguous`: sellers withdraw models from 2031 (A-8, CR-10a) and some buyers wait for pre-registered stock (A-29). The 0.9 clause of RS-8 on opposing timing chains is the point of the example; the engine has the buyers' chain only |
| **importers number_of_sellers decrease** | **WRONG** | EN-7 with CR-1 removes sellers because legal trade stops. The 12 importers and 600 dealers keep selling BEVs, PHEVs and used cars, and the example lists no exit. The rule is gated on `enforced` only; the rules for employment and asset value of the same sellers are correctly gated on `no_other_use` (answered 0.1) and are not reported |

## Table rows

| Row | Produced? | Reason |
|---|---|---|
| C-1 buyers.new_combustion, importers quantity_traded decrease | yes | |
| C-2 buyers.new_phev, importers quantity_traded decrease | yes | |
| C-3 owners.bev resources_available_other_uses decrease | no | unsupported instrument: `lump_sum_tax` has no rules (TX-1, CR-8b) |
| C-4 taxpayers tax_revenue increase | no | same |
| C-5 buyers.new_combustion quantity_substitute increase | yes | |
| C-7 buyers.new_cars quantity_traded (U1) | no | missing rule: CR-12 combination of new cars and imports; no combiner entry, no role |
| C-8 buyers.new_phev quantity_traded increase | no | missing rule: RS-1 signs the bound buyers' quantity_substitute, not the substitute class's quantity in a window |
| C-9 buyers.new_combustion quantity_traded ambiguous | no | missing rule: RS-8's opposing chains (A-8, A-29) and a combiner |
| C-10 importers variety decrease | no | missing rule: CR-4 and CR-10a for model withdrawal |
| C-11 dealers inventory_held increase | no | missing rule and role: pre-registration (RS-8 with RS-5); the engine's run-down is for destroyed stocks |
| C-12 importers.used quantity_traded increase | no | missing rule: RS-4 and CR-7c for the substitute durable good before the date |
| C-13 importers.used quantity_traded (U1-a: decrease; U1-b: increase) | no | the U1-a half is produced; U1-b is silent (RS-4 with A-20) |
| C-14 importers.used reclassification | yes | |
| C-15 owners.combustion maintenance_spending increase | no | unsupported instrument: EN-14 (stock exempt) and CR-10b have no rules; no role |
| C-16 owners.combustion quantity_traded (scrapping) decrease | no | same |
| C-17 same, ambiguous after 2040 | no | same |
| C-18 lobbying_effort increase | yes (part) | dealers (matched to the bound role) only |
| C-19 owners.combustion.2026 asset_value increase | no | EN-14 with CR-7c: revaluation of the stock; no role |
| C-20 buyers.used_combustion price_paid increase | no | EN-14, RS-16, CR-6; no role |
| C-21 owners.combustion net_price_received increase | no | same |
| C-22 buyers.used_combustion price_paid ambiguous | no | same |
| C-23 owners.bev.existing asset_value ambiguous | no | RS-16 with CR-7c; no role |
| C-24 fuel retailers quantity_complement decrease | no | missing rule: a prohibition does not feed `target_qty`, so RS-12 (relations.lp) never fires; no role |
| C-25 number_of_sellers (fuel stations) decrease | no | same |
| C-26 fuel stations asset_value decrease | no | SB-4 with CR-7c not encoded for a ban |
| C-27 fuel_station_workers employment, hours_worked at_least_one_decrease | no | RS-6 with CR-9; no role |
| C-28 charging quantity_complement increase | no | RS-12 for the substitute's complement |
| C-29 repair_shops quantity_traded increase | no | CR-9; no role |
| C-30 same after 2040, ambiguous | no | same |
| C-31 owners.combustion travel_time increase | no | RS-12; no rule |
| C-32 taxpayers tax_revenue (fuel excise) decrease | no | TX-10 is for a tax on the banned good (`taxed_before`); the fuel excise is a tax on a complement |
| C-33 taxpayers tax_revenue ambiguous | no | combiner: fuel excise against the road charge; the charge is not encoded |
| C-34 dealers compliance_cost increase | no | CR-8c and OC-2 for pre-registration: no rule, no role |
| C-35 officials.enforcement enforcement_cost increase | yes | |
| C-36 other Registry users wait_time, other checks | no | OC-3's fixed-budget case is not encoded |
| C-37 importers.used compliance_cost (U1) | no | CR-8c under the readings; no rule |
| C-38 buyers.new_bev price_paid no_change | no | no rule derives no_change (CR-6 with A-5); no role |
| C-39 buyers.new_combustion quantity_traded ambiguous (2026 to 2032) | no | RS-8, TS-10 with CR-7c; no rule |
| C-40 buyers.new_bev quantity_traded ambiguous | no | RS-8 for the substitute; no role |
| C-41 dealers asset_value decrease | no | CR-7c for stock at the date; no role |
| C-42 sellers.foreign price_paid (U1) | no | RS-13 with EN-6 wider market: no clause in the prohibition rules, and no `neighbor_seller_actor` was set (the Drevland sellers are not buyers' alternatives for the banned good) |
| C-43 importers.used wait_time, allocation_by_non_price_criteria (U1) | no | CR-6 for the inspection queue; no rule |
| C-44 repair_shops employment, hours_worked at_least_one_increase | no | CR-9; no role |
| C-45 same after 2040, ambiguous | no | same |
| C-46 repair_shops asset_value ambiguous | no | CR-7c; no role |
| C-47 buyers.used_bev price_paid ambiguous | no | RS-16 with CR-6; no role |
| C-48 owners.combustion stock_age increase | no | EN-14 with CR-10b; no rule, no role |

By reason: the stock, used goods and the substitute (EN-14, TS-3, CR-7c, CR-10b, RS-16) 13 rows; related markets (CR-9, RS-12) 10 rows; the road charge (`lump_sum_tax`) 2 rows plus the part of C-33; timing chains and pre-registration (RS-8) 7 rows; the readings, the wider market and the queue (C-7, C-13, C-37, C-42, C-43) 5 rows; OC-3's fixed budget, C-36, and `no_change`, C-38, one each; C-8, C-10, C-12 and C-34 are single missing encodings.

## General gaps

Ranked by the rows each would add or fix.

1. **Product standards with the stock exempt (EN-14, TS-3, CR-10b, CR-7c).** This is the example's classification, and its largest block: about 11 rows (the kept stock: maintenance, scrapping, fleet age; revaluation of held cars; used prices; used BEVs). Pattern: a rule that forbids new units only does not touch the stock, so the stock becomes scarcer relative to the counterfactual (the used price rises per unit of a given car, holders' assets revalue at once, owners keep cars and repair them longer). A `product_standard` instrument with a flag for "stock exempt", the roles for used-good buyers and owners of the stock, and rules for these chains would add them. It also removes the prohibition rules' misfires (gap 5), because K1 would no longer be read as a ban on a good.
2. **A prohibition or standard must feed `target_qty` (RS-12, CR-9).** `relations.lp` takes the target market's change only from subsidies and taxes. A ban that cuts the quantity of the good cuts its complements (fuel, repairs, station staff) and the derived demand for its inputs, and raises those of the substitute (charging). With `related` entries (the text names stations, repair shops and mechanics) this would add up to 10 rows (C-24 to C-31, C-44, C-45), subject to the premises in the table (A-16, A-17, A-19, A-26). The parser instruction limits `related` to taxes and subsidies; it should include any instrument that moves a quantity.
3. **Opposing timing chains around a date (RS-8, 0.9 clause) with a combiner.** RS-8's rush is encoded alone and signs `quantity_demanded` increase. The handbook's rule is that the rush is one chain among others (sellers withdraw models, buyers wait for the pre-registered stock, the substitute's purchases move too), and the total is `ambiguous` unless one chain is shown to dominate. A declared comparison over the window would fix the WRONG rush row and add C-9, C-39, C-40 and possibly C-10 and C-11 (pre-registration, withdrawal): 4 to 6 rows.
4. **EN-7's chains need an informal trade to exist.** The risk price (`price_paid` increase, `quantity_demanded` decrease) and the search and quality rows presuppose that sellers trade the banned good outside the law. Where the rule works through a registry (a car cannot be registered, hence cannot be driven or resold as new), there is no such trade; A-14 puts the evasion at 0.3. A record flag (a gate: the good cannot be traded or used without registration) or a question that separates "enforcement is a real risk to informal sellers" from "the registry refuses" would remove 2 WRONG rows (the two price rows) and the two `quantity_demanded` decreases that rest on them.
5. **EN-7's `number_of_sellers` should be gated on `no_other_use`.** The legal sellers exit only if the banned good is their business (CR-1 with SB-4); the rules for employment and asset value already follow that gate, the number-of-sellers rule does not. This fixes 1 WRONG row without losing any table row (WE-017 answers `no_other_use` at 0.85, so Corrin keeps the row).
6. **Instrument roles for owners and sellers of the substitute and the stock.** A prohibition has `bound_actor` (one) and `buyer_actor`, so dealers, importers, owners of the stock, buyers of used goods, the substitute's buyers (buyers.new_bev) and the wider-market sellers (Drevland) have no role. One extra bound role (dealers beside importers) would add C-11, C-34, C-41 only if rules existed (gap 3).
7. **`lump_sum_tax` has no rules (TX-1, OC-1, CR-8b).** Ontology 2.3 says TX-1 and OC-1 apply. Rules for a charge paid by the owners of a good would produce C-3, C-4 and part of C-33: 3 rows.
8. **Smaller gaps.** (a) U1-b silence in C-13: imports of used cars rise when the used price rises (RS-4 with A-20) is not a rule for the substitute durable good; 1 row. (b) `no_change` for a price that cannot move (CR-6 with A-5, constant cost): 1 row (C-38). (c) OC-3's fixed-budget case (a mixed group of the agency's other users): 1 row (C-36). (d) The engine's single unqualified RS-7 lobbying sign cannot name which of the table's classes organize.

Whole-run figures: 6 of 47 rows produced (13%), 14 of 18 reported engine rows in the table or defensible, 4 WRONG. For comparison, the development example WE-017 is produced in full by construction; this run shows the prohibition rules transfer only the first-order core (quantity traded, enforcement cost, reclassification, lobbying) to a case whose real content is the stock and the substitute.
