# Out-of-sample run of the quota rules (EN-6, EN-12, EN-13) on WE-047 (Kestrany Sugar Import Regime Act)

Rules as they were at commit a0b2aea (`licensing.lp`: EN-6 written from the catalog text, an import quota takes the tariff chains; EN-12 and EN-13 written from WE-028 only). Handbook catalog 1.0 (the example is corrected under 1.0). Nothing under `praxeo/` was changed. Record: `record.json`, three components, decided from the text: k1 `tariff` (the 60% out-of-quota rate; `rate_rise`, `definition_line`, `renewable`, `announcement_window`, `downstream` for the food manufacturers with exempt competitors, the domestic sellers' owner, worker and input-supplier roles, and a `related` input market for beet), k2 `quota` (`import_quota`, `transferable`, `allocation_by_history`, `base_period_after_announcement` false because the base period 2023 to 2025 ended before the bill was published on 2 March 2026, `wider_market` false because the domestic price is above the landed price, `entrant_actor`, `announcement_window`, `renewable`; it carries the 2% in-quota rate, which has no field) and k3 `rights_allocation` (no rules). K3 trading and K4 surrender are folded into k2 as `transferable` and a source sentence; K4 has no instrument. Unclear provision U1 is recorded with `reading_fields` on k2: under U1-a the applicants for surrendered tonnes are `relief_applicant_actor` (`importers.new`), under U1-b nothing changes. Answers: `answers.json`, 40 questions, 30 with a matching WE-047 assumption (A-1, A-2, A-3, A-6, A-7, A-8, A-9, A-10, A-11, A-14, A-17, A-20, A-21, A-25, A-27), 10 judged from the text (evasion, domestic substitutes, input not replaceable, relocation, supply of substitutes, value of relief). Run: `python3 -m praxeo cases/we047_kestrany --out cases/we047_kestrany/sample_run`; verifier and citation problems are empty. Test: `tests/test_oos_we047.py`. Key: (actor class, variable, sign, window). The table's "March to December 2026" cells are the announcement window.

Summary: the table has 54 rows. The engine reports 38 consequences (41 keys; the two employment and hours groups are one consequence each). Rows produced by key: 26 of 54 (C-3, C-4, C-5, C-6, C-7, C-8, C-10, C-13, C-14, C-16, C-23, C-26, C-27, C-28, C-29, C-30, C-33, C-34, C-37, C-38, C-39, C-42, C-44, C-45, C-48, C-49); of these C-4, C-5, C-6, C-10, C-26 and C-39 for only some of the classes the row names, and C-16 by key only (see below). Rows not produced: 28. Engine keys: 28 in the table, 13 not (10 defensible or misattributed, 3 **WRONG**, which are two consequences: the exporting industries and their workers).

## Engine rows (reported)

| Engine row | Class | Why |
|---|---|---|
| buyers.household price_paid increase | in table | C-5, C-39 (TX-7 at the 60% rate; EN-6 for the import quota). Households only: the record has one buyer role |
| buyers.household quantity_traded decrease; sellers.foreign quantity_traded decrease | in table | C-45 (OC-4), C-4 (TX-2) |
| buyers.household resources_available_other_uses decrease | in table | C-38 (CR-8b) |
| buyers.industrial quantity_supplied decrease | in table | C-27 (RS-14, with A-8 and `input_not_replaceable`) |
| workers.food employment, hours_worked at_least_one_decrease | in table | C-28 |
| food_manufacturers.exporters quantity_supplied decrease | in table | C-30 (RS-6, A-9) |
| buyers.sugar_goods quantity_substitute increase | in table | C-29 (RS-1) |
| owners.food_manufacturers asset_value decrease | in table | C-34 (SB-4) |
| mills.domestic net_price_received, quantity_supplied, investment_target increase | in table | C-6, C-7, C-48. Growers have no role, so only the mills' side |
| workers.mills employment, hours_worked at_least_one_increase | in table | C-37 |
| owners.mills asset_value increase | in table | C-33 |
| importers.history asset_value increase | in table | C-3 (EN-12 windfall, SB-4) |
| importers.history right_lease_price increase | in table | C-8, but through EN-13 (medium horizon); EN-6 does not give it because `wider_market` is false |
| importers.history number_of_sellers decrease | in table | C-10 (EN-13, A-6, A-7). `importers.new` has no number_of_sellers row |
| importers.history quantity_traded decrease | in table | C-4. Also matches C-16 by key only: the engine's row is the whole year's imports, not October to December (no rule for the surrender date) |
| importers.history reclassification increase | in table | C-23 (RS-5, A-14) |
| importers.history compliance_cost increase | in table | C-44 (TX-5; the quota's OC-2 is not encoded) |
| officials.enforcement enforcement_cost increase | in table | C-42, C-49 (OC-3; Tier B in the engine, Tier A in the table) |
| importers.new allocation_by_non_price_criteria, compliance_cost U1-a increase, U1-b no_change | in table | C-13, C-14 (RS-15 on `relief_applicant_actor`, per reading). The first run of this record with a role not in the ontology (`applicants`) was refused by the verifier; `importers.new` stands for the table's applicants |
| lobbying_effort increase: importers.history, mills.domestic, buyers.industrial | in table | C-26 (RS-7 with A-17), for three of the four groups |
| importers.new lobbying_effort U1-a increase, U1-b no_change | defensible | RS-7 for the applicants; C-26 signs would-be importers without readings |
| buyers.household quantity_traded increase (announcement) | defensible, misattributed | RS-8 on the one buyer role; C-18 and C-19 name importers and food manufacturers |
| buyers.household reclassification increase | defensible, misattributed | RS-5 on the tariff's buyer role; C-23 names importers |
| importers.history capital_stock_target decrease | defensible | EN-13; the table does not sign importers' capital |
| importers.history net_price_received increase | defensible | EN-6 (no wider market): the importers' selling price rises with the domestic price; the table signs the lease price |
| importers.history quantity_supplied increase | defensible | EN-13: more per remaining importer; stands beside C-4's fall for the class |
| importers.history resources_available_other_uses decrease | defensible, questionable | TX-1/CR-8b puts the 60% on the bound importers; under the marginal-rate reading (TX-7 1.0, CR-6 1.0) the buyers bear it, and the holders gain the rent. True only for importers above their licence (C-2) |
| input_suppliers quantity_demanded increase | defensible | CR-9; C-36 has the same content under `quantity_traded` |
| officials.enforcement tax_revenue_vs_static_projection decrease | defensible | TX-9; C-40 signs `tax_revenue`, which needs A-25 |
| taxpayers resources_available_other_uses decrease | defensible | OC-3 with OC-1; the group form of C-41, C-43, C-51 needs `general_budget`, which the text does not state |
| export_industries quantity_supplied decrease | **WRONG** | TX-8 alone. C-31 is `ambiguous`: imports of sugar goods rise, which is a further (+) chain through the currency (CR-9, CR-12; the example's Corrections), and A-8 and A-21 decide the net |
| workers.export_industries employment, hours_worked at_least_one_decrease | **WRONG** | the workers of the same industries, same cause |

The held-back results are as designed: the 2026 race of EN-12 is not signed (the base period ended before the announcement, so EN-12 gives the windfall, C-3), and EN-6's lease price is not signed by EN-6 itself. Both follow from the record's flags, which were set from the text.

## Table rows

| Row | Produced? | Reason |
|---|---|---|
| C-1 in-quota landed cost price_paid decrease | no | missing record fact and rule: the 2% rate has no field; TX-2 and TX-7 are for a rise; no rule for a cut at the inframarginal rate |
| C-2 out-of-quota landed cost price_paid increase | no | missing rule: TX-1 puts the 60% on the bound role as resources_available; no price_paid for importers |
| C-3 importers.history asset_value increase | yes | |
| C-4 imports quantity_traded decrease | yes (part) | importers.history and sellers.foreign; `importers.new` has no row |
| C-5 buyers price_paid increase (short–medium) | yes (part) | households only (one buyer role); `buyers.industrial` has no price row |
| C-6, C-7 domestic sugar net price, quantity | yes (part) | mills only; growers have no role |
| C-8 right_lease_price increase | yes | via EN-13 |
| C-9 small holders quantity_traded (licences leased or sold) | no | missing rule and role: EN-13's lessors |
| C-10 number_of_sellers decrease | yes (part) | importers.history only |
| C-11 importers.new entry_rate | no | missing rule: CR-4 for entry under a quota (EN-6 signs entry for `seller_cap` only); EN-12's newcomers |
| C-12 entry_rate (registrations to apply for surrendered tonnes) | no | missing rule: EN-12 (newcomers, U1-a) |
| C-13, C-14 applicants allocation by non-price criteria, compliance cost | yes | per reading, through `reading_fields` |
| C-15 inventory on 30 September | no | missing record fact and rule: K4 has no instrument; dated removal of an option (CR-1, CR-10a, RS-8 0.9) |
| C-16 imports October–December decrease | yes, by key only | the key is C-4's whole-year fall; the dated reason is not derived |
| C-17 imports January–September ambiguous | no | same as C-15 |
| C-18 imports March–December 2026 increase | no | missing rule: RS-8 for the importers' purchases before the effective date (the engine puts the stocking on `buyers.household`) |
| C-19 stocks on 31 December 2026 | no | missing rule: RS-8 inventory |
| C-20 quantity_demanded decrease | no | variable: the engine signs `quantity_traded` and the purchases not made (C-45) |
| C-21 glucose syrup as substitute | no | missing rule: RS-1 for substitutes of an input (A-12) |
| C-22 glucose syrup price | no | missing rule and role: RS-16 |
| C-23 reclassification | yes | |
| C-24 white share of in-quota imports | no | missing rule: RS-21 (high-grading under a cap in physical units) |
| C-25 refiners' quantity_supplied | no | missing rule and role: CR-9 / RS-21; no refiners role |
| C-26 lobbying | yes (part) | three of the four groups |
| C-27, C-28, C-29, C-30 | yes | downstream chain (RS-14) |
| C-31 export industries ambiguous | no | the engine's row is the decrease, **WRONG** |
| C-32 beet land asset_value | no | missing role: SB-4 `asset_owner_actor` is for subsidies only |
| C-33, C-34 | yes | |
| C-35 trading houses' firm value | no | missing role and rule: owners of the importing firms (CR-7c) |
| C-36 beet inputs | no | variable name: the engine has `quantity_demanded` |
| C-37, C-38 | yes | |
| C-39 long-run price | yes (part) | households only; the long-run row is the same key as C-5 |
| C-40 tariff revenue decrease | no | variable: `tax_revenue_vs_static_projection` is produced; `tax_revenue` needs A-25 |
| C-41, C-43, C-51 payer group | no | missing record fact: no `general_budget` (not stated); the engine has `taxpayers` alone |
| C-42, C-44 | yes | |
| C-45 purchases not made | yes | |
| C-46 refiners' and manufacturers' firm value ambiguous | no | missing role and rule: CR-7c, CR-12b |
| C-47 customs revenue March–December 2026 | no | missing rule: RS-8 |
| C-48, C-49 | yes | |
| C-50 licence fee receipts | no | missing rule: CR-8b for fees under a quota |
| C-52, C-53 world sugar price | no | missing rule: CR-6 / CR-9 for the world price under a tariff or import quota; RS-8 for the window |
| C-54 port warehouses | no | missing record fact and rule: not in section 1; RS-12 |

## General gaps

Ranked by the number of table rows each would add or fix (a row may need two gaps; it is counted under its main one).

1. **The payer group for a tariff or quota office (OC-1, OC-3; A-27).** The group of taxpayers, recipients of other spending and future taxpayers (OC-1) is formed only for `general_budget`, which the text here does not state (it says the office's funding is not stated, and names the general budget as the receiver of the tariff). When the agency's budget rises with its task (`enforcement_budget_raised`) the cost falls on a budget that is not the office's own revenue, so the payer group, not `taxpayers` alone, follows. It would add C-41, C-43 and C-51 (3 rows) and remove the exception row.
2. **RS-8, announcement window of a tariff or quota, beyond the buyers (CR-10a).** Importers buy ahead before the effective date (C-18), stocks build (C-19), customs revenue rises in the window (C-47), the world price rises (C-53, CR-6) and storage gains (C-54, RS-12). The engine signs the stocking only on the record's one buyer role, and misattributes it. It would add C-18, C-19, C-47, C-53 and with RS-12 C-54 (up to 5 rows) and fix the misattributed row.
3. **A dated removal of an option that repeats each period (CR-1, 0.7 and 1.0; RS-8, 0.9; EN-12 newcomers).** K4 (surrender on 30 September) has no instrument, so nothing is derived for the stocks before the date (C-15), the imports either side of it (C-16 properly, C-17), or the entry of newcomers who apply for surrendered tonnes (C-11, C-12). A rule for a `surrender` or `use_it_or_lose_it` term of a quota, with the U1 readings, would add C-15, C-17, C-11, C-12 and make C-16 right for the right reason (4 rows, 1 repaired).
4. **A tariff with two rates (TX-7 1.0, TX-2, CR-6 1.0 "a quota on a rate"; CR-1 0.9 threshold).** The handbook says the marginal rate sets the price and the inframarginal rate only divides the gap. The record has no field for the in-quota rate, so the cut (C-1) and the importers' out-of-quota cost (C-2) are not produced, `tax_revenue` (C-40) is not signed, and TX-1 puts the 60% on the bound importers (the questionable `resources_available_other_uses` row). It would add C-1, C-2, C-40 and repair that row (3 rows, 1 repaired).
5. **TX-8 with a change in the form of imports (TX-8 0.9; CR-9, CR-12).** When imports of the uncovered goods that contain the good rise (`downstream` with `competitors: exempt`), the currency chain has a further (+) link and the sign for the export industries is `ambiguous`, as the Corrections section says for C-31. The engine gives the decrease and the same for their workers. It would fix C-31 and remove the **WRONG** rows (1 row, 3 keys).
6. **Owners of the right holders and of beet land (CR-7c claims before creation; SB-4; DM-4).** The importing firms' value (C-35, C-46) and the value of beet land (C-32: SB-4's `asset_owner_actor` exists for subsidies only, not for tariffs) have no role. It would add C-32, C-35, C-46 (3 rows).
7. **EN-13's lessors, and substitutes and refiners.** EN-13 signs the remaining users' side but not those who lease out (C-9, with an `operators` or `holders.small` role); RS-1 and RS-16 for glucose syrup as a substitute of an input (C-21, C-22, with A-12 and A-13); CR-9 with RS-21 for the refiners and high-grading under a cap in physical units (C-24, C-25) (up to 6 rows).
8. **Second buyer role for a tariff or quota whose buyers are both households and manufacturers.** The record names one `buyer_actor`; the table has price rows for `buyers.industrial` and `buyers.household` (C-5, C-39) and the engine puts the window stocking and the reclassification on the one role. The `downstream` group's actor already is the manufacturers; the price row could follow it (completes C-5, C-39, fixes two misattributed rows).
9. **Normalising variables across rules (3 rows).** `quantity_demanded` against `quantity_traded` for inputs (C-36), the buyers' fall (C-20), `tax_revenue` against its static-projection form (C-40, counted in 4), and the fee receipts of CR-8b under a quota (C-50).

Not a gap: EN-6's lease price is derived only through EN-13 here because the price is not set in a wider market; the table's C-8 is the same sign, so the key matches. EN-12 gives the windfall, not the race, because the base period ended before the announcement: that is the rule working as written on a different case from WE-028.
