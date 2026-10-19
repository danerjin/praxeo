# Out-of-sample run of the quota rules (EN-6, EN-12, EN-13) on WE-039 (Sorrel Basin Groundwater Allocation Plan)

Rules as they were at commit a0b2aea (`licensing.lp`: EN-6 from the catalog text; EN-12 allocation by history and EN-13 consolidation, both written from WE-028 only). Handbook catalog 0.9. Nothing under `praxeo/` was changed. Record: `record.json`, three components: K1 `quota` (bound `pumpers`, buyer `growers.nuts`, right holder `landholders.history`, `transferable`, `wider_market` (EN-6 Inputs clause: the output is priced nationally), `allocation_by_history` with `base_period_after_announcement` false (the 2017 to 2021 base period ended before the March 2022 draft), `announcement_window`, `renewable` (reviewed in 2032), `own_revenue_funded`, `entrant_actor` `growers.prospective`, `worker_actor` `farm_workers`; trading K4 and enforcement K5 are folded into K1), K2 `rights_allocation` (history) and K3 `rights_allocation` (lottery); K2 and K3 have no rules and no questions. Unclear provision U1 is recorded with its two readings and no `reading_fields`: no Component field expresses the sub-basin limit. Answers: `answers.json`, 8 questions, every one with a matching WE-039 assumption (A-1, A-2, A-10, A-11, A-3, A-16, A-4, A-19). The `allocation_known` question is not asked (the base period is not after the announcement), so the race branch of EN-12 is correctly silent. Run: `python3 -m praxeo cases/we039_sorrel --out cases/we039_sorrel/sample_run`; verifier and citation problems are empty. Key: (actor class, variable, sign, window). No window cell occurs in WE-039's table.

Summary: the table has 60 rows (C-1 to C-60). The engine reports 14 consequences (15 keys; the farm-work group is one consequence with two variables), and 2 more below the cut-off (the buyers' `price_paid` and its CR-8b mirror, behind A-19 at p = 0.3, as the example has it). Rows produced by key: 5 of 60 (C-2, C-19, C-30, C-42, C-52); C-19 and C-52 by a different mechanism than the table's (EN-13, not RS-6 with A-5). Rows not produced: 55. Engine rows classified WRONG: 1 (pumpers `quantity_supplied` increase); 9 other keys are not in the table (6 defensible, 3 misattributed to the buyers); 5 keys are in the table.

## Engine rows (reported)

| Engine row | Class | Why |
|---|---|---|
| landholders.history asset_value increase | in table | C-2 (EN-12 windfall branch, history fixed before the announcement; also SB-4). The table says "from March 2022"; the engine row has no window, as in WE-028 |
| officials.enforcement enforcement_cost increase | in table | C-30 (OC-3). Tier B here, Tier A in the table |
| pumpers capital_stock_target decrease | in table | C-42 (here through EN-13, "capital stock falls" in the long run; the table has a cost fixed per well, CR-4) |
| farm_workers employment, hours_worked at_least_one_decrease | in table | C-19 and C-52 (EN-13: workers of those who leave; the table has RS-6 with A-5, and the long-run Tier B row) |
| pumpers quantity_supplied increase | **WRONG** | EN-13's "more per remaining user" is put on the class `pumpers`, which here is every pumper. C-1 and C-47 have the same key and the opposite sign: total groundwater pumped falls under the cap (A-1, A-2). The engine also reports pumpers `quantity_traded` decrease, so the report contradicts itself |
| pumpers quantity_traded decrease | defensible | EN-6 for the capped quantity; the table has the event as C-1 under `quantity_supplied` |
| growers.nuts quantity_traded decrease | defensible, with a caveat | EN-6 for the record's buyer role. Nut growers' pumped water falls (C-6, C-8), but their leased-in water rises against the counterfactual (C-37 is the lessors' side). The key is in no row |
| pumpers number_of_sellers decrease | defensible | EN-13; C-7 has it on growers.field and growers.nuts, the farms that irrigate |
| landholders.history right_lease_price increase | defensible | EN-6 Unless; C-4 has it on `pumpers`. One right-holder field cannot serve C-2 (landholders) and C-4 (pumpers) |
| landholders.history lobbying_effort increase | defensible | RS-7 (A-11); the table's lobbyists are the harmed and priced-out groups (C-14) |
| pumpers informal_activity increase | defensible | RS-3 (A-10); the table has the same over-pumping as `legal_breach` (C-13) |
| growers.nuts search_cost increase; quality_information decrease; disputes_settled_outside_courts increase | defensible in form, misattributed | RS-3 with EN-3, RS-10 for the buyers of unrecorded trade. Over-pumping is self-supply; nobody buys it. Same fault as WE-028 (found there for `informal_buyer_actor`) |

## Table rows

| Row | Produced? | Reason |
|---|---|---|
| C-1 pumpers quantity_supplied decrease | no | unsupported form: EN-6 signs the capped quantity as `quantity_traded`; C-1 is a cap on the bound pumpers' own pumping |
| C-2 landholders.history asset_value increase | yes | |
| C-3 lottery.winners asset_value | no | missing rule: lottery branch of EN-12 (K3) |
| C-4 right_lease_price | no (by key) | missing role: engine puts it on the right holder, `landholders.history` |
| C-5, C-6, C-48, C-50 field and nut crops grown (Tier B, not counting the aquifer) | no | missing record fact and rule: EN-6 Inputs clause (0.9). The output of the capped input falls; no output relation or growers roles |
| C-7 number_of_sellers (farms irrigating) | no (by key) | missing role: engine signs `pumpers` |
| C-8 South pumping | no | missing record fact (sub-basin role) and the per-reading cell |
| C-9 entrants entry_rate decrease | no | missing rule: entry when rights must be bought or leased; the entrant role is set but only the race branch reads it |
| C-10 investment_target decrease | no | missing rule: CR-10a from the announcement; no question for A-20 |
| C-11, C-12 lottery splitting and entry costs | no | missing rule: lottery branch of EN-12 (RS-5, RS-8, CR-7c, CR-8c); no A-13, A-21 questions |
| C-13 legal_breach | no (by variable) | unsupported form: informal_activity vs legal_breach |
| C-14 lobbying | no (by key) | missing role: harmed groups and landholders.no_history |
| C-15, C-17, C-45 surface water: bought, price, other districts | no | missing rule and record fact: RS-1, RS-16 for a quota; Related has no substitute kind |
| C-16, C-18 relocation to Lowther, Lowther land value | no | missing rule and record fact: RS-4 for a quota (`neighbor_actor` is for ceilings) |
| C-19, C-52 farm work | yes | by EN-13, not RS-6 |
| C-20, C-43, C-44 input suppliers, meter sellers, dealers | no | missing record fact and rule: CR-9; section 1 does not name them; `related` is not read for quotas |
| C-21, C-22, C-23, C-24, C-25, C-26, C-46, C-60 the race the cap ends | no | missing rule and record fact: CR-9 over a `shared_facility` relation, Tier C |
| C-27, C-39 land and shares together; field holders' total | no | combiner and missing rule: CR-12b over two items |
| C-28, C-58, C-59 land without history | no | missing rule and role: CR-1 and CR-7c for the excluded (K2, K3 have no rules); C-28 combiner |
| C-29, C-41, C-49, C-51, C-53, C-54, C-55, C-56 Tier C combined rows | no | missing rule and combiner: Tier C against Tier B (CR-12, CR-12e) and the shared facility |
| C-30 enforcement_cost | yes | |
| C-31, C-35 fee on shares; enforcer's fee receipts | no | missing rule: OC-3 with CR-8b for a fee on rights held; `own_revenue_funded` is set and unread |
| C-32 compliance_cost (meters) | no | missing rule: OC-2 and CR-8c for a quota |
| C-33 U1 cross-sub-basin transfers | no | case-specific provision: no Component field for the reading |
| C-34 prevented exchanges (field growers, workers, crop buyers) | no | missing role: OC-4 is signed for the record's bound and buyer roles only |
| C-36 enforcer's penalty receipts | no | missing rule: CR-8b for fines |
| C-37 allocations leased out; C-38 lease receipts; C-40 lease payments | no | missing rule: lessors' side and the lessees' payment of the lease price (CR-5, CR-8b); no lessor role |
| C-42 capital_stock_target | yes | by EN-13, not the fixed per-well cost |
| C-47 pumpers quantity_supplied (long, Tier B) | no | unsupported form, as C-1 |
| C-57 full_cost_per_unit increase | no | missing rule: CR-6 for the cost per unit of the capped input |

## General gaps

Ranked by the number of table rows each would add or fix.

1. **CR-9 over a `shared_facility` relation, with CR-12's Tier C against Tier B rule.** The handbook states it in CR-9 (0.7) and CR-12 (0.9): a common resource that every user draws on makes every chain through it Tier C, and a Tier B consequence the facility chain opposes is reported at Tier B, qualified, next to its combined Tier C sign. Allocation by history caps a stock that all users share, and the cap ends a race (CR-8, 0.8). It would add C-21 to C-26, C-46, C-60 (8 rows) and the Tier C combined rows C-29, C-41, C-49, C-51, C-53, C-54, C-55, C-56, C-59 (9 more), up to 17. It needs a relation kind in `Related`, roles for the other users of the facility, a stock question (A-14) and a trend question (A-15).
2. **EN-12 beyond the holders: newcomers and the lottery reserve.** EN-12 as written signs only the holders' windfall and the race. The handbook's "first branch" and "a share reserved for newcomers by lottery" also give: entry and new investment fall for those without history from the announcement (CR-1, CR-4, CR-10a: C-9, C-10), land without history loses value (CR-7c, CR-10c: C-58, C-28 with CR-12b, C-59), lottery winners gain (C-3), and entries multiply with a cost (RS-5, RS-8, CR-8c: C-11, C-12). A `rights_allocation` rule with an `allocation_method` (history, lottery) and roles for the excluded would add 7 to 9 rows.
3. **Substitutes and relocation for a quota (RS-1, RS-4, RS-16).** The substitute question exists for licensing and the neighbour role for ceilings. A cap on an input should let its users turn to a substitute (surface water) and move activity to an uncapped neighbour. With a `substitute` kind in `Related` it would add C-15, C-17, C-45, C-16, C-18 (5 rows).
4. **The two sides of the lease price (CR-5, CR-7a, CR-8b, CR-6, EN-13).** EN-6 Unless signs the lease price only on the right holder. The pattern needs lessors and lessees as separate roles: lessors lease more and receive the price (C-37, C-38), lessees pay it and the full cost per unit of the input rises (C-40, C-57), and EN-13's number of sellers belongs to the farms, not the whole bound class (C-7). It would add 5 rows (C-37, C-38, C-40, C-57, C-7) and settle C-4 and C-39 with a combiner.
5. **EN-6's Inputs clause (0.9): the output of a capped input.** The handbook: where the cap is on an input whose output is sold in a wider market, the lease price rations the input and the output falls (CR-9). `wider_market` is read for the lease price only. An `output` relation with the growers' roles would add C-5, C-6, C-48, C-50 (4 rows), with C-8 and the Tier C rows after gap 1.
6. **The costs and receipts of a rights scheme (OC-2, OC-3, CR-8b, CR-8c).** The record has `own_revenue_funded`, and the engine reads only `general_budget`. A fee on the rights held is a cost of the holders and a receipt of the enforcer (C-31, C-35), the meters and reporting are the pumpers' compliance cost (C-32), and fines are receipts (C-36): 4 rows.
7. **CR-9 for suppliers, with `related` read for quotas.** EN-13 has an `en_supplier` role, but no question or text sentence sets it here; meters, farm inputs and dealers (C-20, C-43, C-44) would need `related` entries for inputs, which are read for taxes and subsidies only: 3 rows.
8. **Self-supply under a cap on one's own input (autistic intervention, CR-1).** The bound sellers are also the users, so the capped quantity is `quantity_supplied`, not `quantity_traded`, and EN-13's "more per remaining user" must not be put on a class that is the whole bound group. Fixing this adds C-1 and C-47 (2 rows) and **removes the one WRONG row** (pumpers `quantity_supplied` increase). The same fact removes the three misattributed informal-buyer rows (RS-3 has no buyers of over-pumping) and moves the over-pumping to `legal_breach` (C-13), when the activity stays legal (1 row).
9. **Smaller items.** One `right_holder_actor` cannot serve both the recipients of the free shares (C-2) and the class the handbook puts the lease price on (C-4); a second role (`lessee_actor`) would give C-4. RS-7 for the harmed and priced-out groups (C-14). A reading of U1 that sets a Component field (C-33, C-8) has no field to set: case-specific.
