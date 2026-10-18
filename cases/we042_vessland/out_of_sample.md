# Out-of-sample run of the existing rules on WE-042

Handbook example: `handbook/05_examples/WE-042_aluminum_tariff_drawback.md`. Case: `cases/we042_vessland`. Rules as they stood before any change for this step (`praxeo/rules/*.lp`, `praxeo/questions.py`, `praxeo/engine.py` untouched; rule base built from WE-013). Run: `python3 -m praxeo cases/we042_vessland --out cases/we042_vessland/sample_run`; compared on (actor, variable, sign, window) with the example's "Consequence list (normal form)".

## Summary

- Table rows: 57. Produced: 15 in full and 2 in part (a part means some of the row's actor classes or variables are missing). Not produced: 40.
- Engine rows reported (one per actor and variable; a group counts once per member): 29. In the table: 18. Not in the table but defensible: 8. WRONG: 3.

Record notes (what the record could and could not say):

- Only K1 (the tariff) is a component. K2 (the drawback, a refund conditional on export) and K3 (the re-import repayment) have no instrument in 02_ontology.md section 2.3 that the rule base uses, so about a quarter of the table (everything that rests on the drawback) is out of reach before any rule is considered. K4 (revenue and administration) is recorded through revenue_actor and the answer to enforcement_budget_raised.
- Roles filled: bound and importer `importers`, buyer `users.home`, domestic seller and protected `smelters`, worker `smelter_workers`, owner `smelters.owners`, input supplier `input_suppliers`, foreign seller `sellers.foreign`, exporter `export_industries.other`, one downstream group `users.home.finished` (competitors exempt: finished goods are not covered; owner and worker actors named), announcement_window, renewable (expiry and review), definition_line. WE-042's table has several more downstream and substitute-market classes (`fabricators.mixed`, `exporters.*`, `remelters`, `holders.aluminum_stocks`), which have no field.
- U1 (substitution) is recorded with two readings and no reading facts; the readings matter only for drawback rows.
- Answers (15): from rows A-1, A-4, A-13, A-22, A-15, A-17, A-21, A-7, A-11, A-19, A-12, A-23 and A-15; asset_supply_slow (0.8) is my estimate (no row), the rest are marked in their rationale.

## Engine rows

| Actor | Variable | Sign | Window | Class | Where / why |
|---|---|---|---|---|---|
| `export_industries.other` | `quantity_supplied` | decrease |  | **WRONG** | C-35 signs this `ambiguous`, citing TX-8's 0.9 clause: a policy that reduces imports of one good but raises imports of goods made from it (here C-12 reshaped imports and C-25 finished-goods imports) makes the currency chain itself ambiguous unless a premise says which dominates (A-13 only supports the first chain). TX-8 as encoded has no such clause, so the engine states a decrease. |
| `workers.export_industries.other` | `employment` | at_least_one_decrease |  | **WRONG** | The labour group of the same TX-8 chain; ambiguous for the same reason (C-35). Group member row, one consequence. |
| `workers.export_industries.other` | `hours_worked` | at_least_one_decrease |  | **WRONG** | As above (group member). |
| `buyers.aluminum_goods` | `quantity_substitute` | increase |  | not in table, defensible | RS-1 with substitute_supply_expands (A-15): buyers of aluminum goods turn to the tariff-free imported finished goods. The table gives the foreign sellers' side (C-25) and, for goods without a close substitute, the price (C-33). |
| `importers` | `resources_available_other_uses` | decrease |  | not in table, defensible | TX-1 for a tariff, as WE-013 C-26 signs it for importers. WE-042's final check signs this variable only for classes that keep paying (C-41) and does not list importers, who may pass the tariff on. |
| `input_suppliers` | `quantity_demanded` | increase |  | not in table, defensible | CR-9 derived demand of the smelters (state grid). C-30 states the same claim under quantity_traded; variable name only. |
| `owners.users_home_finished` | `asset_value` | decrease |  | not in table, defensible | SB-4 for the owners of the squeezed users. C-32's actor is `users.home.finished (owners)`; the record gives the owners a class name, as WE-013's record does for C-22. |
| `users.home.finished` | `capital_stock_target` | decrease |  | not in table, defensible | RS-4 / TS-1: users that cannot pass the cost on move capital out when they next replace plant (can_relocate_capital = A-23). The table has the Ostrel side of the same shift (C-26). |
| `users.home.finished` | `lobbying_effort` | increase |  | not in table, defensible | RS-7 for the harmed users (A-11); C-24 lists `users.home`, of which this is the squeezed part. |
| `workers.users_home_finished` | `employment` | at_least_one_decrease |  | not in table, defensible | RS-6 labour group of the squeezed users; C-22's actor is `users.home.finished (workers)`, and the record names the class workers.users_home_finished. |
| `workers.users_home_finished` | `hours_worked` | at_least_one_decrease |  | not in table, defensible | As above (group member). |
| `importers` | `quantity_traded` | decrease |  | in table | C-8, C-37 |
| `importers` | `reclassification` | increase |  | in table | C-12 (RS-5, A-7) |
| `officials.enforcement` | `enforcement_cost` | increase |  | in table | C-43 (the tariff part; drawback and K3 audits are not in the record) |
| `officials.enforcement` | `tax_revenue` | increase |  | in table | C-3 (gross tariff revenue; the table's is net of drawback, which the record cannot represent) |
| `officials.enforcement` | `tax_revenue_vs_static_projection` | decrease |  | in table | C-40 |
| `sellers.foreign` | `quantity_traded` | decrease |  | in table | C-54 (OC-4) |
| `smelter_workers` | `employment` | at_least_one_increase |  | in table | C-6 (group) |
| `smelter_workers` | `hours_worked` | at_least_one_increase |  | in table | C-6 (group) |
| `smelters` | `lobbying_effort` | increase |  | in table | C-24 (RS-7, A-11); the users' part is under users.home.finished |
| `smelters` | `net_price_received` | increase |  | in table | C-1 |
| `smelters` | `quantity_supplied` | increase |  | in table | C-5 |
| `smelters.owners` | `asset_value` | increase |  | in table | C-31 (SB-4, A-12) |
| `users.home` | `price_paid` | increase |  | in table | C-2 |
| `users.home` | `quantity_traded` | decrease |  | in table | C-7, C-37 |
| `users.home` | `quantity_traded` | increase | announcement | in table | C-9 (RS-8, A-21); the importers' part of C-9 is not produced |
| `users.home` | `reclassification` | increase |  | in table | C-12 |
| `users.home` | `resources_available_other_uses` | decrease |  | in table | C-41 |
| `users.home.finished` | `quantity_supplied` | decrease |  | in table | C-21 (RS-14, RS-6) |

## Table rows

| ID | Actor class | Variable | Sign | Status | Reason / engine row |
|---|---|---|---|---|---|
| C-1 | smelters | net_price_received | increase | produced | smelters net_price_received increase |
| C-2 | users.home | price_paid (covered aluminum) | increase | produced | users.home price_paid increase |
| C-3 | officials.enforcement (general fund) | tax_revenue (net of drawback) | increase | produced | tax_revenue increase, gross; the table's row is net of drawback |
| C-4 | officials.enforcement (general fund), to exporters | subsidy_outlay (drawback refunds) | increase | not produced | The drawback (K2) and the re-import rule (K3): a refund conditional on export is not an instrument the rule base has (SB-10, CR-1, CR-3, CR-8b/c, RS-19; missing rule and missing record fact). Includes every row on exporters' net cost, claims, the outlay and round trips. |
| C-5 | smelters | quantity_supplied | increase | produced | smelters quantity_supplied increase |
| C-6 | smelter_workers | employment, hours_worked | at_least_one_increase | produced | smelter_workers employment, hours_worked at_least_one_increase |
| C-7 | users.home | quantity_traded (covered aluminum, all sources) | decrease | produced | users.home quantity_traded decrease |
| C-8 | importers | quantity_traded (covered imports, from September 2027) | decrease | produced | importers quantity_traded decrease |
| C-9 | importers, users.home | quantity_traded (covered imports, February–August 2027) | increase | partial | users.home in the announcement window; importers' part not produced (RS-8 signs the buyers only) |
| C-10 | users.home | inventory_held (at 1 September 2027) | increase | not produced | RS-8 / CR-10a: inventory_held. RS-8 signs quantity_traded only (missing rule). |
| C-11 | users.home | quantity_substitute (secondary aluminum) | increase | not produced | RS-1 / RS-16 / CR-6 / CR-9: the market for scrap and secondary aluminum (users turn to it, remelters supply it, its price). No substitute-market rule for a tariff and no remelter or scrap role (missing rules and record facts). |
| C-12 | importers, users.home | reclassification (imports reshaped into uncovered forms) | increase | produced | importers and users.home reclassification increase |
| C-13 | exporters.domestic_metal | reclassification (supply switched, lots designated to exports) | U1-a: increase; U1-b: no_change | not produced | The drawback (K2) and the re-import rule (K3): a refund conditional on export is not an instrument the rule base has (SB-10, CR-1, CR-3, CR-8b/c, RS-19; missing rule and missing record fact). Includes every row on exporters' net cost, claims, the outlay and round trips. |
| C-14 | smelters | quantity_traded (metal sold to exporters) | U1-a: decrease; U1-b: ambiguous | not produced | The drawback (K2) and the re-import rule (K3): a refund conditional on export is not an instrument the rule base has (SB-10, CR-1, CR-3, CR-8b/c, RS-19; missing rule and missing record fact). Includes every row on exporters' net cost, claims, the outlay and round trips. |
| C-15 | exporters.low_scrap, exporters.high_scrap | compliance_cost (drawback claims) | increase | not produced | The drawback (K2) and the re-import rule (K3): a refund conditional on export is not an instrument the rule base has (SB-10, CR-1, CR-3, CR-8b/c, RS-19; missing rule and missing record fact). Includes every row on exporters' net cost, claims, the outlay and round trips. |
| C-16 | exporters.low_scrap, exporters.high_scrap | compliance_cost (lot tracing, segregated stocks) | U1-a: increase; U1-b: no_change | not produced | The drawback (K2) and the re-import rule (K3): a refund conditional on export is not an instrument the rule base has (SB-10, CR-1, CR-3, CR-8b/c, RS-19; missing rule and missing record fact). Includes every row on exporters' net cost, claims, the outlay and round trips. |
| C-17 | exporters.low_scrap (at or above the tables' yield) | price_paid (aluminum, net of drawback) | increase | not produced | The drawback (K2) and the re-import rule (K3): a refund conditional on export is not an instrument the rule base has (SB-10, CR-1, CR-3, CR-8b/c, RS-19; missing rule and missing record fact). Includes every row on exporters' net cost, claims, the outlay and round trips. |
| C-18 | exporters.high_scrap | price_paid (aluminum net of drawback and scrap sales, per tonne of product) | ambiguous | not produced | The drawback (K2) and the re-import rule (K3): a refund conditional on export is not an instrument the rule base has (SB-10, CR-1, CR-3, CR-8b/c, RS-19; missing rule and missing record fact). Includes every row on exporters' net cost, claims, the outlay and round trips. |
| C-19 | fabricators.mixed (including parts makers who also sell at home) | quantity_supplied (exports of uncovered goods and parts) | increase | not produced | fabricators.mixed and total exports: need the drawback's shift from home to export sales (CR-4, CR-7a, CR-12e) and a class the record has no field for (missing record fact and rule). |
| C-20 | fabricators.mixed | quantity_traded (home sales of uncovered goods) | decrease | not produced | fabricators.mixed and total exports: need the drawback's shift from home to export sales (CR-4, CR-7a, CR-12e) and a class the record has no field for (missing record fact and rule). |
| C-21 | users.home.finished | quantity_supplied (uncovered goods for Vessland) | decrease | produced | users.home.finished quantity_supplied decrease |
| C-22 | users.home.finished (workers) | employment, hours_worked | at_least_one_decrease | not produced | Actor name: produced under workers.users_home_finished / owners.users_home_finished (see the engine rows); the table's actor is the prose `users.home.finished (workers)` / `(owners)`. |
| C-23 | exporters.high_scrap, exporters.low_scrap, importers | legal_breach (undeclared round trips) | increase | not produced | The drawback (K2) and the re-import rule (K3): a refund conditional on export is not an instrument the rule base has (SB-10, CR-1, CR-3, CR-8b/c, RS-19; missing rule and missing record fact). Includes every row on exporters' net cost, claims, the outlay and round trips. |
| C-24 | smelters; users.home, exporters | lobbying_effort | increase | partial | smelters lobbying_effort; the users and exporters of the row are not produced (the squeezed users appear under users.home.finished) |
| C-25 | sellers.foreign (finished goods) | quantity_supplied (into Vessland) | increase | not produced | RS-14 / RS-16 / CR-9: the foreign sellers' side of the switch to untaxed finished goods. The rule base signs the buyers' quantity_substitute only (missing rule). |
| C-26 | neighboring_jurisdictions (Ostrel fabricators) | quantity_supplied (for Vessland buyers) | increase | not produced | RS-4 for a tariff: Ostrel's fabricators supply Vessland buyers. No neighbour role and no rule (missing rule and record fact); the capital-move rule signs capital_stock_target instead. |
| C-27 | remelters, users.home | price_substitute (scrap) | increase | not produced | RS-1 / RS-16 / CR-6 / CR-9: the market for scrap and secondary aluminum (users turn to it, remelters supply it, its price). No substitute-market rule for a tariff and no remelter or scrap role (missing rules and record facts). |
| C-28 | remelters | quantity_supplied (secondary aluminum) | increase | not produced | RS-1 / RS-16 / CR-6 / CR-9: the market for scrap and secondary aluminum (users turn to it, remelters supply it, its price). No substitute-market rule for a tariff and no remelter or scrap role (missing rules and record facts). |
| C-29 | scrap_sellers | quantity_traded (scrap exports) | decrease | not produced | RS-1 / RS-16 / CR-6 / CR-9: the market for scrap and secondary aluminum (users turn to it, remelters supply it, its price). No substitute-market rule for a tariff and no remelter or scrap role (missing rules and record facts). |
| C-30 | input_suppliers (state grid) | quantity_traded (electricity to smelters) | increase | not produced | Variable: C-30 states the smelters' electricity as quantity_traded; the engine's CR-9 rule gives quantity_demanded (the same claim; see the engine rows). |
| C-31 | smelters.owners | asset_value (smelters) | increase | produced | smelters.owners asset_value increase |
| C-32 | users.home.finished (owners) | asset_value | decrease | not produced | Actor name: produced under workers.users_home_finished / owners.users_home_finished (see the engine rows); the table's actor is the prose `users.home.finished (workers)` / `(owners)`. |
| C-33 | buyers.aluminum_goods | price_paid (goods with no close imported substitute) | increase | not produced | RS-14 for goods with no close imported substitute: the buyers' price rises only where competitors face the same cost, but the record's one downstream group has competitors exempt; the second group (A-16) needs a second Downstream entry that I did not write because the table's classes `users.home` and `buyers.aluminum_goods` coincide (missing record fact). |
| C-34 | buyers.foreign | price_paid (machined and stamped parts in regional markets) | decrease | not produced | CR-9 / CR-6: foreign buyers and regional parts makers on the other side of the export shift. Not encoded (missing rule). |
| C-35 | export_industries.other | quantity_supplied (exports) | ambiguous | not produced | TX-8 with the 0.9 clause on a change in the form of imports: the engine produces a decrease, the table says ambiguous. Counted as not produced; the engine row is WRONG. |
| C-36 | exporters.low_scrap, exporters.high_scrap, fabricators.mixed | quantity_supplied (exports, total) | ambiguous | not produced | fabricators.mixed and total exports: need the drawback's shift from home to export sales (CR-4, CR-7a, CR-12e) and a class the record has no field for (missing record fact and rule). |
| C-37 | importers, users.home | quantity_traded (covered imports, net of reshuffle) | decrease | produced | importers and users.home quantity_traded decrease |
| C-38 | users.home | tax_share_borne (against foreign smelters) | increase | not produced | DM-1: `tax_share_borne`. Not encoded (missing rule). |
| C-39 | users.home.finished | tax_share_borne (against their buyers) | increase | not produced | DM-1: `tax_share_borne`. Not encoded (missing rule). |
| C-40 | officials.enforcement | tax_revenue_vs_static_projection | decrease | produced | tax_revenue_vs_static_projection decrease |
| C-41 | users.home (those who keep buying) | resources_available_other_uses | decrease | produced | users.home resources_available_other_uses decrease |
| C-42 | taxpayers, recipients of other general-fund spending | resources_available_other_uses | at_least_one_increase | not produced | CR-8b / CR-8d: the general fund's net receipts and their recipients (a group). Not encoded; the encoded OC-3 case names the payers (missing rule). |
| C-43 | officials.enforcement | enforcement_cost (tariff, drawback, K3 audits) | increase | produced | enforcement_cost increase (tariff part only) |
| C-44 | customs_users (importers, claimants, those served by other checks) | wait_time (drawback payment) (+), wait_time (customs clearance) (+), enforcement_cost (other customs checks) (−) | at_least_one_as_stated | not produced | OC-3, fixed-budget case with CR-6/CR-8a: customs users' waiting times as a group. The rule base derives nothing for a fixed budget (missing rule). |
| C-45 | importers | compliance_cost (classification and entries) | increase | not produced | TX-5: compliance cost of classification and entries (Tier A). Not encoded (missing rule). |
| C-46 | exporters.low_scrap (at or above the tables' yield) | resources_available_other_uses | decrease | not produced | The drawback (K2) and the re-import rule (K3): a refund conditional on export is not an instrument the rule base has (SB-10, CR-1, CR-3, CR-8b/c, RS-19; missing rule and missing record fact). Includes every row on exporters' net cost, claims, the outlay and round trips. |
| C-47 | exporters.high_scrap | resources_available_other_uses | ambiguous | not produced | The drawback (K2) and the re-import rule (K3): a refund conditional on export is not an instrument the rule base has (SB-10, CR-1, CR-3, CR-8b/c, RS-19; missing rule and missing record fact). Includes every row on exporters' net cost, claims, the outlay and round trips. |
| C-48 | holders.aluminum_stocks | asset_value (covered aluminum held in Vessland) | increase | not produced | CR-7c / CR-10c: the asset value of holders of stocks at the effective date. No rule and no holder role (missing rule and record fact). |
| C-49 | exporters.domestic_metal | price_paid (aluminum in exported goods, net of any drawback) | U1-a: increase; U1-b: ambiguous | not produced | The drawback (K2) and the re-import rule (K3): a refund conditional on export is not an instrument the rule base has (SB-10, CR-1, CR-3, CR-8b/c, RS-19; missing rule and missing record fact). Includes every row on exporters' net cost, claims, the outlay and round trips. |
| C-50 | exporters.low_scrap (beating the tables) | price_paid (aluminum, net of drawback) | ambiguous | not produced | The drawback (K2) and the re-import rule (K3): a refund conditional on export is not an instrument the rule base has (SB-10, CR-1, CR-3, CR-8b/c, RS-19; missing rule and missing record fact). Includes every row on exporters' net cost, claims, the outlay and round trips. |
| C-51 | exporters.low_scrap (beating the tables) | resources_available_other_uses | ambiguous | not produced | The drawback (K2) and the re-import rule (K3): a refund conditional on export is not an instrument the rule base has (SB-10, CR-1, CR-3, CR-8b/c, RS-19; missing rule and missing record fact). Includes every row on exporters' net cost, claims, the outlay and round trips. |
| C-52 | officials.enforcement (general fund) | subsidy_outlay (drawback against Customs' ceiling) | U1-a: decrease; U1-b: ambiguous | not produced | The drawback (K2) and the re-import rule (K3): a refund conditional on export is not an instrument the rule base has (SB-10, CR-1, CR-3, CR-8b/c, RS-19; missing rule and missing record fact). Includes every row on exporters' net cost, claims, the outlay and round trips. |
| C-53 | remelters | net_price_received (secondary aluminum) | increase | not produced | RS-1 / RS-16 / CR-6 / CR-9: the market for scrap and secondary aluminum (users turn to it, remelters supply it, its price). No substitute-market rule for a tariff and no remelter or scrap role (missing rules and record facts). |
| C-54 | sellers.foreign (smelters and mills) | quantity_traded (covered aluminum sold to Vessland) | decrease | produced | sellers.foreign quantity_traded decrease |
| C-55 | sellers.foreign (regional parts makers) | net_price_received (machined and stamped parts) | decrease | not produced | CR-9 / CR-6: foreign buyers and regional parts makers on the other side of the export shift. Not encoded (missing rule). |
| C-56 | fabricators.mixed (workers in export fabrication) | employment, hours_worked | at_least_one_increase | not produced | fabricators.mixed and total exports: need the drawback's shift from home to export sales (CR-4, CR-7a, CR-12e) and a class the record has no field for (missing record fact and rule). |
| C-57 | exporters.high_scrap, exporters.low_scrap, importers | quantity_traded (round-trip shipments to Ostrel and back) | increase | not produced | The drawback (K2) and the re-import rule (K3): a refund conditional on export is not an instrument the rule base has (SB-10, CR-1, CR-3, CR-8b/c, RS-19; missing rule and missing record fact). Includes every row on exporters' net cost, claims, the outlay and round trips. |

## Reading

Seventeen of 57 rows are produced and three engine rows (two consequences: one a labour group) are WRONG. The tariff rules that WE-013 was built on transfer: C-1 to C-9, C-12, C-21, C-31, C-37, C-40, C-41, C-43 and C-54 come out of the same chains as WE-013's rows, and RS-8, RS-7 and SB-4 carry over.

The WRONG rows come from one gap: TX-8 as encoded has no clause for a policy that raises imports of goods made from the covered good (here the reshaped forms of C-12 and the finished goods of C-25). The handbook's TX-8 (0.9) makes the currency chain ambiguous then. The rule base states a plain decrease for export industries and for their workers.

The largest block of unproduced rows (15 plus 4) rests on the drawback, a refund conditional on export that no rule or instrument in the rule base covers; the record cannot even state it. A second block is the substitute markets (scrap, secondary aluminum, foreign sellers of finished goods) where the rule base stops at the buyers' quantity_substitute.
