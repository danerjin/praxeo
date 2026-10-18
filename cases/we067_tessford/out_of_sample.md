# Out-of-sample run of the existing rules on WE-067 (Tessford Tenant Stability Ordinance 2027)

Rules as they were before any change (rule base `rb-thin-0.7`, handbook catalog 1.4). Record: `record.json`, one `price_ceiling` component for the cap (K1) with vacancy decontrol and an announcement window (bound `landlords.covered`, protected `tenants.covered.other`, excluded `tenants.prospective`, neighbour `tenants.county`; fee-funded board, so no general-budget flag). The withdrawal route (K3), the Portable Senior Credit (K4), the board's fee (K5) and the credit's administration (K6) have no instrument in the rules and are in the policy text and the unclear provision U1 only. Answers: `answers.json`, from WE-067's assumption table (A-1 to A-37) wherever a row exists. Run: `python3 -m praxeo cases/we067_tessford --out cases/we067_tessford/sample_run`. Key: (actor class, variable, sign, window). The handbook's "sitting tenants" is matched to the record's protected role `tenants.covered.other`; the table's `tenants.covered.senior` has no role in the record.

Summary: the table has 71 rows (C-1 to C-73 without the removed C-6 and C-7). The engine reports 33 consequences (the 3 resources entries are a total and its two items). Rows produced by key: 29; of these 10 for only some of the classes the row names, and C-57 and C-60 by key only (C-57 through PC-7, not its for-cause mechanism; C-60 through a row that does not name the destination). Rows not produced: 42. Engine rows classified WRONG: 1.

## Engine rows (reported)

| Engine row | Class | Why |
|---|---|---|
| tenants.covered.other price_paid decrease | in table | C-1 |
| tenants.covered.other price_paid ambiguous, window first_months | in table | C-2 (comparison of PC-16 with RS-8) |
| tenants.covered.other price_paid increase, window announcement | in table | C-12 |
| landlords.covered net_price_received decrease | in table | C-3 |
| landlords.covered net_price_received increase, window announcement | in table | C-54 |
| tenants.covered.other turnover decrease | in table | C-8 (and C-57 by key) |
| tenants.covered.other.keepers relocation_out_of_area decrease | in table | C-9 (the engine cannot name the destination: C-9 out of Tessford, C-60 out of the county) |
| tenants.covered.other relocation_out_of_area decrease (comparison `pc_21_relocation`) | in table | C-49 (the class total with the displaced; C-60 by key) |
| tenants.covered.other.displaced relocation_out_of_area increase | in table | C-22 |
| tenants.covered.other.displaced turnover increase | in table | C-21 (the non-senior half) |
| tenants.covered.other job_changes decrease | in table | C-38 |
| tenants.covered.other quality_per_unit decrease | in table | C-17 |
| landlords.covered maintenance_spending decrease | in table | C-16 |
| tenants.covered.other informal_activity increase | in table | C-18 (sublet form) |
| landlords.covered reclassification increase | in table | C-19 |
| landlords.covered quantity_supplied decrease | in table | C-20 |
| landlords.covered asset_value decrease | in table | C-34 |
| landlords.covered units_held_vacant increase | in table | C-59 |
| landlords.covered quantity_traded decrease | in table | C-39 |
| tenants.prospective quantity_traded decrease | in table | C-39 |
| tenants.prospective price_paid increase | in table | C-53 (initial rents under vacancy decontrol) |
| tenants.prospective price_substitute increase | in table | C-31 (`tenants.exempt` has no role) |
| tenants.county price_paid increase | in table | C-29 |
| officials.enforcement enforcement_cost increase | in table | C-42 |
| landlords.covered resources_available_other_uses decrease (total, item rent_forgone) | in table | C-44 |
| tenants.covered.other resources_available_other_uses increase | in table | C-45 |
| tenants.covered.other quality_adjusted_price ambiguous | in table | C-48 |
| landlords.covered lobbying_effort increase; tenants.covered.other lobbying_effort increase | in table (C-26), with a gap | C-26 (U1, the schedule, the credit). The engine has no RS-7 Unless clause, so it cannot give C-27 (rent regulation as such, `ambiguous` given A-19) and its single unqualified sign agrees with one of the two rows |
| landlords.covered resources_available_other_uses increase (item key_money) | defensible | C-44 lists "rents above the cap taken by landlords who evade" as a (+) chain (section 7); the item is a part of that comparison |
| tenants.prospective disputes_settled_outside_courts increase | defensible | RS-10 for the sublet trade (A-11): the subtenants are households seeking a home. Not in WE-067's table (WE-001 C-23 has the same row) |
| **tenants.prospective side_payments increase** | **WRONG** | PC-6 and PC-2's side payments by seekers presuppose a capped price for them. Under vacancy decontrol the initial rent is free; the handbook removed the seekers' rationing group (C-6, C-7) for that reason and the table's side_payments row is the landlords' buyouts (C-61) |

## Table rows

Rows are listed in table order. "Part" means the row names classes the record has no role for.

| Row | Produced? | Reason |
|---|---|---|
| C-1 sitting tenants price_paid decrease | yes (part) | `tenants.covered.other`; no `.senior` role |
| C-2 sitting tenants price_paid ambiguous (first months) | yes (part) | same |
| C-3 landlords.covered net_price_received decrease | yes | |
| C-4 seniors.credit price_paid decrease | no | unsupported form: the credit (K4) is a payment attached to renting elsewhere; no rule covers it |
| C-5 City subsidy_outlay increase | no | unsupported form (K4); no subsidy rule |
| C-8 tenants.covered.other turnover decrease | yes | |
| C-9 tenants.covered.other (keep) relocation_out_of_area decrease | yes | destination (out of Tessford) not represented |
| C-10 tenants.covered.senior relocation_out_of_area decrease | no | needs the senior class and the credit's portable range (PC-21 1.4 per destination) |
| C-11 tenants.covered.senior relocation_out_of_area ambiguous | no | same |
| C-12 sitting tenants price_paid increase (announcement) | yes (part) | |
| C-13 tenants.window_terminated turnover increase | no | missing record fact (no-cause terminations under state law, the class) and a question for A-8; RS-8 is encoded for repricing only |
| C-14 tenants.covered.senior turnover ambiguous | no | senior class and credit |
| C-15 tenants.covered.near_qualifying turnover decrease | no | credit; RS-8 delay to qualify |
| C-16 landlords.covered maintenance_spending decrease | yes | |
| C-17 sitting tenants quality_per_unit decrease | yes (part) | |
| C-18 sitting tenants informal_activity increase | yes (part) | |
| C-19 landlords.covered reclassification increase | yes | |
| C-20 landlords.covered quantity_supplied decrease | yes | |
| C-21 tenants.displaced.other, .senior turnover increase | yes (part) | non-senior only |
| C-22 tenants.displaced.other relocation_out_of_area increase | yes | the engine names the class `tenants.covered.other.displaced` |
| C-23 tenants.displaced.senior relocation_out_of_area (Tessford) | no | senior class, credit, reading U1 (the parser's readings carry no engine facts) |
| C-24 tenants.displaced.senior relocation_out_of_area (county) | no | same |
| C-25 tenants.window_terminated relocation_out_of_area increase | no | same as C-13 |
| C-26 landlords, tenant unions, senior advocates lobbying_effort increase | yes (part) | landlords and the protected tenants; no advocates role |
| C-27 same, rent regulation as such, ambiguous | no | missing rule: RS-7's Unless clause (the counterfactual is contested, A-19) |
| C-28 landlords.covered compliance_cost increase | no | missing record fact and rule: OC-2 for registration and the fee; the engine's compliance cost is the exit-process form (unreported, p 0.3) |
| C-29 tenants.county price_paid increase | yes | |
| C-30 renters.durnside price_paid increase | no | missing record fact: one neighbour role per component |
| C-31 tenants.exempt, tenants.prospective price_substitute increase | yes (part) | `tenants.prospective` only |
| C-32 tenants.prospective, tenants.exempt relocation_out_of_area increase | no | missing rule: PC-21's population caveat (shut-out residents leave more) |
| C-33 homebuyers quantity_substitute increase | no | RS-5 signs reclassification only; the rental to owner-occupied relation is a record fact (as in WE-001 C-14) |
| C-34 landlords.covered asset_value decrease | yes | |
| C-35 landlords.exempt asset_value increase | no | no `landlords.exempt` role; SB-4 is applied to the bound sellers only |
| C-36 developers investment_target increase | no | no role or exemption fact (as in WE-001 C-13) |
| C-37 landlords.county asset_value increase | no | no role |
| C-38 tenants.covered.other job_changes decrease | yes | |
| C-39 tenants.prospective, landlords.covered quantity_traded decrease | yes | |
| C-40 general_fund_payers resources_available_other_uses at_least_one_decrease | no | unsupported form: the credit is paid from the general fund (K4); no rule for it |
| C-41 seniors.credit resources_available_other_uses increase | no | unsupported form (K4) |
| C-42 officials.enforcement enforcement_cost increase | yes | |
| C-43 county_housing_office enforcement_cost increase | no | unsupported form (K6) |
| C-44 landlords.covered resources_available_other_uses decrease | yes | |
| C-45 sitting tenants resources_available_other_uses increase | yes (part) | |
| C-46 displaced households resources_available_other_uses increase | no | case-specific provision (relocation payment, K3), as in WE-001 C-30 |
| C-47 officials.enforcement non_tax_receipts increase | no | missing rule: OC-3's own-revenue funding case with CR-8b |
| C-48 sitting tenants quality_adjusted_price ambiguous | yes (part) | |
| C-49 covered.other, displaced.other relocation_out_of_area decrease (total) | yes | |
| C-50 same, long horizon, ambiguous | no | missing: a per-horizon sign (TS-3). The engine's decrease for C-49 holds "from medium onward", so at long it contradicts C-50: a limit of the crude horizons, not a row |
| C-51 all insiders (class total) relocation_out_of_area ambiguous | no | the total across kept, displaced and senior classes; no senior class |
| C-52 tenants.covered.senior turnover ambiguous | no | senior class, credit |
| C-53 tenants.prospective price_paid increase | yes | |
| C-54 landlords.covered net_price_received increase (announcement) | yes | |
| C-55 landlords.covered net_price_received ambiguous (first months) | no | the combiner declares the first-months total for the buyers' price only |
| C-56 sitting tenants resources_available_other_uses decrease (announcement) | no | missing rule: CR-8b mirror of C-12 in the window |
| C-57 sitting tenants turnover decrease (no-cause terminations) | yes, by key only | engine row C-8 (PC-7); the for-cause rule's own mechanism is not modeled |
| C-58 landlords.covered units_held_vacant increase (announcement) | no | missing record fact and rule: RS-8 for landlords' no-cause terminations; the engine's row is C-59 |
| C-59 landlords.covered units_held_vacant increase | yes | |
| C-60 tenants.covered.other (keep) relocation_out_of_area decrease (county) | yes, by key only | destination not represented (same row as C-9 and C-49) |
| C-61 landlords.covered, sitting tenants side_payments increase (buyouts) | no | missing rule: PC-6 buyout form (A-29 has no question) |
| C-62 tenants.covered.senior quantity_demanded increase (rental homes) | no | credit |
| C-63 county_housing_office non_tax_receipts increase | no | unsupported form (K6) |
| C-64 tenants.prospective travel_time increase | no | no rule for commuting by shut-out seekers |
| C-65 landlords.county net_price_received increase | no | no role (CR-8b side of C-29) |
| C-66 landlords.credit subsidy_share_received increase | no | unsupported form (K4) |
| C-67 displaced search_cost increase | no | no rule for moving cost (CR-1 and CR-8c) |
| C-68 displaced resources_available_other_uses ambiguous | no | no rule |
| C-69 officials.enforcement fund_balance ambiguous | no | no variable rule |
| C-70 covered.other, displaced.other turnover ambiguous (total) | no | the combiner forms no turnover total (README); the engine signs the two subclasses |
| C-71 same relocation_out_of_area (county) ambiguous | no | destination not represented |
| C-72 covered.senior, displaced.senior relocation_out_of_area (county) ambiguous | no | senior classes |
| C-73 landlords.covered net_price_received increase (initial rents) | no | missing rule: the landlords' side of C-53 (CR-8b mirror); the only increase the engine reports for this key is the announcement-window one (C-54) |

## After the rule changes (second commit)

The record and answers are unchanged. None of the new patterns adds a row here: PC-2's group, LW-3 and PC-6's buyers rows are not met under vacancy decontrol (PC-1 1.4), PC-12 needs an input supplier, and RS-7 and the displaced subclass keep their results (the tenants are a concentrated group; `nontransferable` is 0.9). The rows produced stay at 29 of 71 and the engine rows are the same 33.

Engine rows WRONG: 1, unchanged (`tenants.prospective` side payments). The fix (PC-6's side payments by the excluded buyers presuppose a capped price for them, so not under vacancy decontrol) would also remove the same row from `sf_1994`, whose agreement list in `tests/test_config_b.py` contains it; it was not made. The gaps that need new encodings are listed with reasons in `tests/test_out_of_sample.py::test_consistent_with_worked_example_we067`: the credit and its administration (K4, K6), RS-7's Unless clause (C-27), the buyout form of PC-6 (C-61), the senior classes, the mirrors of the window rows (C-55, C-56, C-73), and the second neighbour (Durnside).
