# Out-of-sample run of the existing rules on WE-006 (Coralia Emergency Pricing Act)

Rules as they were before any change (rule base `rb-thin-0.7`, handbook catalog 1.4). Record: `record.json`, one `price_ceiling` component for goods and rooms together (bound `sellers.local`, protected `buyers.served`, excluded `buyers.unserved`, neighbour `buyers.inland`, no announcement window, fixed enforcement budget). The engine allows one bound role per component, so `sellers.outside` and `hotels.declared` (named in the table) have no role in this record. Answers: `answers.json`. Run: `python3 -m praxeo cases/we006_coralia --out cases/we006_coralia/sample_run`. Key: (actor class, variable, sign, window).

Summary: the table has 26 rows (C-1 to C-26). The engine reports 26 consequences (the 3 resources entries are a total and its two items). Rows produced by key: 7 (C-1, C-8, C-12, C-15, C-22, C-24, C-26), of which C-12, C-15, C-22 and C-24 only for some of the listed classes and C-8 and C-12 by a different route than the handbook's. Four more rows (C-3, C-5, C-16, and the side-payments member of C-4) are produced under the record's name for the excluded role (`buyers.unserved`; the table says `residents.declared`). Rows not produced: 19. Engine rows classified WRONG: 2.

## Engine rows (reported)

| Engine row | Class | Why |
|---|---|---|
| buyers.served price_paid decrease | in table | C-1 |
| sellers.local net_price_received decrease | in table | C-24 (for `sellers.local` only) |
| sellers.local lobbying_effort increase | in table | C-15 (`hotels.declared` has no role) |
| officials.enforcement enforcement_cost increase | in table | C-26 |
| buyers.unserved quantity_traded decrease | in table | C-22 (`sellers.outside` has no role) |
| sellers.local quantity_supplied decrease | in table (different route) | C-8 by key. The engine gets it from PC-5 (alternative_uses, answered from A-6); the handbook uses RS-8 with the same A-6. Horizon: engine long, table short |
| sellers.local reclassification increase | in table (different route) | C-12 by key. The engine reads A-6 (stock held off the market) as an alternative use; the handbook's C-12 is bundling and new models (A-9) |
| buyers.unserved excess_demand increase | in table (actor name) | C-3; the table's actor is `residents.declared` |
| buyers.unserved search_cost increase | in table (actor name) | C-16 |
| buyers.unserved allocation_by_non_price_criteria increase | in table (actor name) | C-5 |
| buyers.unserved side_payments increase | defensible | a member of C-4's group, signed on its own premise (A-10 evasion); the table gives the group, not the member |
| buyers.served informal_activity increase | defensible | the sign of C-14, but for the protected buyers and through the sublet form (nontransferable, from A-8); A-8 itself says a guest cannot pass the room on. The table puts it on `residents.declared` |
| buyers.served turnover decrease | defensible, rooms only | C-11 holds for guests in rooms (A-8); for the goods in the same component it is meaningless, and the record has one component for both |
| buyers.served quality_per_unit decrease | defensible | PC-4 puts the cut on the protected buyers; the table has it on `hotels.declared` (C-10) |
| sellers.local maintenance_spending decrease | defensible | PC-4 pairs it with quality_per_unit; the table omits it |
| buyers.served resources_available_other_uses increase | defensible | CR-8b, the buyers keep what the sellers forgo (mirror of C-24) |
| sellers.local resources_available_other_uses decrease (total, item rent_forgone) | defensible | CR-8b, the sellers' side of C-1 and C-24 |
| sellers.local resources_available_other_uses increase (item key_money) | defensible | informal sales above the cap by sellers (cash sales from trucks, online listings, C-14) are receipts of those sellers |
| sellers.local quantity_traded decrease | defensible | OC-4 names both sides of a prevented exchange; the table names the outside sellers (C-22) |
| buyers.unserved price_substitute increase | defensible | PC-8 with A-13 (ice, relatives' homes); the table signs the quantity (C-17), and RS-1 leaves the substitute's price to RS-16 |
| buyers.served quality_adjusted_price ambiguous | defensible | the handbook's price-against-quality comparison (WE-001); not in WE-006's table |
| buyers.unserved disputes_settled_outside_courts increase | defensible | RS-10 for informal trade (C-14, C-25); the variable is not in the table |
| buyers.inland price_paid increase | defensible | RS-4 (inland stores take the extra demand, A-12); the table records the crossing (C-18, ambiguous), not the inland price |
| **buyers.served lobbying_effort increase** | **WRONG** | RS-7 needs a gain concentrated on an identifiable group; the households that find goods are not (the table lists the bound sellers and hotels only, C-15) |
| **buyers.served.displaced turnover increase** | **WRONG** | PC-7 and RS-5: holders "displaced by conversion or withdrawal". Here the "reclassification" is sellers keeping stock off the market; no buyer's holding is ended. The table has turnover falling for guests (C-11) and no displaced class |

## Table rows

| Row | Produced? | Reason |
|---|---|---|
| C-1 buyers.served price_paid decrease | yes | |
| C-2 residents.declared quantity_demanded increase | no | missing rule: PC-1 with LW-3 |
| C-3 residents.declared excess_demand increase | no (actor name) | produced for `buyers.unserved` |
| C-4 residents.declared (wait_time, search_cost, side_payments, allocation) at_least_one_increase | no | missing rule: PC-2 in its group form (the engine signs members only on their own premises, and has no wait_time member); side_payments is produced for `buyers.unserved` |
| C-5 residents.declared allocation_by_non_price_criteria increase | no (actor name) | produced for `buyers.unserved` |
| C-6 sellers.outside quantity_supplied decrease | no | missing record fact: one bound role per component, so `sellers.outside` is not in the record |
| C-7 sellers.outside number_of_sellers decrease | no | missing rule PC-13 (documented costs) and the role |
| C-8 sellers.local quantity_supplied decrease | yes | by key, via PC-5 (the handbook uses RS-8) |
| C-9 sellers.local quantity_supplied increase (after the emergency) | no | missing rule: RS-8 release of stock after the cap lapses; the engine has no such window |
| C-10 hotels.declared quality_per_unit decrease | no | the rules sign quality_per_unit on the protected buyers; `hotels.declared` has no role |
| C-11 evacuees.in_rooms turnover decrease | no | `evacuees.in_rooms` is a subclass of the protected buyers; the engine signs turnover for `buyers.served` (all buyers in the component) |
| C-12 sellers.local, sellers.outside reclassification increase | yes (partly) | `sellers.local` only, and via A-6, not A-9 |
| C-13 sellers.local, sellers.outside compliance_cost increase | no | missing rule PC-13 (the cost of documenting under K2); the engine's compliance_cost comes from an exit process (unreported) |
| C-14 residents.declared informal_activity increase | no (actor) | PC-6 informal_activity is encoded only in the sublet form, for the protected buyers |
| C-15 sellers.local, hotels.declared lobbying_effort increase | yes (partly) | `sellers.local` only |
| C-16 residents.declared search_cost increase | no (actor name) | produced for `buyers.unserved` |
| C-17 buyers.unserved quantity_substitute increase | no | missing rule: RS-1 for a ceiling |
| C-18 residents.declared cross_border_purchases ambiguous | no | RS-4 signs the neighbours' price, not the crossing; no combiner entry |
| C-19 repair_contractors.outside quantity_supplied decrease | no | a depth-4 chain through C-11 to a role the record lacks |
| C-20 sellers.local inventory_held decrease (before each season) | no | missing rule TS-7 (expected caps reduce stocks held); the `expected_to_last` answer is used by SB-4 only, and `durable_assets` is p 0.1 |
| C-21 households.coastal quantity_demanded ambiguous | no | missing rule: standing-law RS-8 before the season; no role |
| C-22 buyers.unserved, sellers.outside quantity_traded decrease | yes (partly) | `buyers.unserved` only |
| C-23 officials.enforcement enforcement_cost decrease (other work) | no | missing rule: OC-3's fixed-budget case (enforcement of other rules falls) |
| C-24 sellers.local, sellers.outside, hotels.declared net_price_received decrease | yes (partly) | `sellers.local` only |
| C-25 residents.declared quality_information decrease | no | RS-10 encoded for disputes_settled_outside_courts only |
| C-26 officials.enforcement enforcement_cost increase | yes | |

The `alternative_uses` answer is a judgement call (p 0.55 from A-6, local sellers storing stock; A-4's 0.9 concerns outside sellers, who have no role). Both the C-8 and C-12 key matches and the WRONG displaced-turnover row depend on it.

## After the rule changes (second commit)

Changes that bear on this example: the single component of the first run is now three, which is the record fact the first run lacked (k1 goods sold by `sellers.local`, k2 goods brought in by `sellers.outside`, k3 rooms of `hotels.declared` with the guests `evacuees.in_rooms` as the protected role), because the engine allows one bound role per component; the excluded role is `residents.declared` (the table's actor for the PC-1 and PC-2 rows); all three say the protected buyers are a diffuse public. Answers for k2 and k3 copy k1's except where the table has a row for that bound class (k2 `alternative_uses` 0.9 from A-4; k3 `nontransferable` 0.85 from A-8, k1's 0.1 for the goods) and are marked in their rationale. New rules (`praxeo/rules/ceiling_extensions.lp`): LW-3 with PC-1, PC-2 in its group form, PC-6's informal activity by the buyers; RS-7 lobbying by the protected needs a concentrated group; the displaced-holders subclass (PC-7, RS-5) needs a right tied to holding (`nontransferable`).

Rows produced: 15 of 26 (C-1 to C-6, C-8, C-11, C-12, C-14 to C-16, C-22, C-24, C-26), up from 7. Engine rows WRONG: 0 (the lobbying row of the buying public and the displaced goods-buyers' turnover are gone). `tests/test_out_of_sample.py::test_consistent_with_worked_example_we006` records each remaining gap.
