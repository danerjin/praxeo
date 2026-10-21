# Out-of-sample run of the licensing rules on WE-055 (Aldenmoor Home Inspector Licensing Act)

Rules as they were (`praxeo/rules/licensing.lp`, developed on WE-003 only); nothing under `praxeo/` was changed. Record: `record.json`, one `licensing_requirement` component (K1) with bound `inspectors`, buyer `buyers.current`, right holder `inspectors.licensed`, trainer `training_schools`, enforcer `officials.enforcement`, `announcement_window` (introduced and enacted before the 2027 effective dates) and `field_contested` (the association's campaign since 2022, stated in section 1). The grandfathering line (K2), enforcement on complaint (K3) and the rule on agents (K4) have no instrument or role field and are in the policy text and unclear provision U1 only; U1 changes no Component field, so `reading_fields` is empty and the engine gives one sign under both readings. Answers: `answers.json`, 8 questions, from WE-055's assumption table (A-1, A-2, A-3, A-4, A-9, A-16, A-17, A-18). Run: `python3 -m praxeo cases/we055_aldenmoor --out cases/we055_aldenmoor/sample_run`; verifier and citation problems are empty. Test: `tests/test_oos_we055.py`. Key: (actor class, variable, sign, window). The table's "unlicensed inspectors" is matched to the bound role `inspectors`.

Summary: the table has 37 rows (C-1 to C-37). The engine reports 19 consequences. Rows produced by key: 7 (C-2, C-5, C-6, C-7, C-17, C-29, C-30). Rows not produced: 30. Engine rows: 7 in table, 9 defensible, 3 WRONG.

## Engine rows (reported)

| Engine row | Class | Why |
|---|---|---|
| inspectors share_of_sellers_licensed increase | in table | C-2 |
| inspectors number_of_sellers decrease | in table | C-5 |
| buyers.current price_paid increase | in table | C-6 |
| buyers.current quantity_traded decrease | in table | C-7 |
| inspectors informal_activity increase | in table | C-17 (the unlicensed inspectors are the bound role who evade) |
| buyers.current resources_available_other_uses decrease | in table | C-29 |
| officials.enforcement enforcement_cost increase | in table | C-30 |
| buyers.current disputes_settled_outside_courts increase | defensible | RS-10 for buyers of unlicensed inspections (A-16); not in the table, applied to all buyers |
| buyers.current quantity_substitute increase | defensible | EN-3 with RS-1; the table signs the engineers' side (C-20) |
| inspectors compliance_cost increase | defensible | C-1 and C-15 sign it for three subclasses the record cannot name |
| inspectors employment decrease | defensible | EN-3 exit of those who do not qualify; not in the table |
| inspectors entry_rate decrease | defensible | C-4 for inspectors.prospective; one sign where C-32 and C-33 give horizons |
| inspectors quantity_traded decrease | defensible | OC-4 sellers' side of C-7 |
| inspectors.licensed lobbying_effort ambiguous (policy_field) | defensible | C-19 (RS-7 Unless, A-18), on the license holders rather than on inspectors.grandfathered |
| inspectors.licensed net_price_received increase | defensible | EN-2; C-8 names the grandfathered and the new_requirement who qualify |
| training_schools quantity_demanded increase | defensible | CR-8c receipts of the schools (A-2); consistent with C-13, and C-14 is ambiguous only from 2028 |
| **buyers.current quality_information ambiguous** | **WRONG** | C-3: `increase` under U1-a. The information loss of RS-3 and RS-10 falls on the buyers of unlicensed inspections (C-34). The record has one buyer role, so EN-11's increase (A-4) and RS-3's decrease (A-16) meet on the same class and combine to ambiguous |
| **buyers.current search_cost increase** | **WRONG** | C-25: referral users' search cost is `no_change` under U1-a. The engine's increase is RS-3's search by buyers of unlicensed inspections, applied to every buyer for want of a role for them |
| **inspectors.licensed lobbying_effort increase** | **WRONG** | C-19 is `ambiguous` (A-18: the association would have campaigned without the Act). The engine reports EN-5/RS-7's unqualified increase next to the contested-field `ambiguous` row, so the table's single sign is contradicted by one of the two |

## Table rows

"Part" means the engine row is on the bound or holder role, not the subclass the table names.

| Row | Produced? | Reason |
|---|---|---|
| C-1 compliance_cost increase (three classes) | no | missing record fact: grandfathered, new_requirement, prospective roles; engine has the bound role (defensible row) |
| C-2 inspectors share_of_sellers_licensed increase | yes | |
| C-3 buyers.current quality_information (U1-a increase; U1-b ambiguous) | no | combiner and missing record fact: engine gives ambiguous (WRONG row); no buyers.unlicensed role; U1 sets no field |
| C-4 prospective entry_rate decrease | no | missing record fact: no would-be entrants role; engine row on `inspectors` |
| C-5 inspectors number_of_sellers decrease | yes | |
| C-6 buyers.current price_paid increase | yes | |
| C-7 buyers.current quantity_traded decrease | yes | |
| C-8 grandfathered, new_requirement net_price_received increase | no | missing record fact: engine row on right holder `inspectors.licensed` |
| C-9 grandfathered earnings increase | no | missing rule: CR-7 money earnings (premise A-10) |
| C-10 near_line quantity_supplied increase | no | case-specific provision and missing rule: RS-8 and RS-17 on the grandfathering line (K2) |
| C-11 near_line net_price_received decrease | no | same |
| C-12 other incumbents quantity_supplied decrease | no | same |
| C-13 new_requirement enrollment increase (2027) | no | missing rule: RS-8 for training before the deadline; `announcement_window` set, nothing fires for licensing |
| C-14 training_schools enrollment ambiguous | no | missing rule: CR-9 / CR-12b horizon rows |
| C-15 grandfather applications compliance_cost | no | unsupported form: exemption with an application cost (OC-2) |
| C-16 grandfathered job_changes decrease | no | unsupported form: RS-11 with the 12-month lapse clause |
| C-17 unlicensed inspectors informal_activity increase | yes | |
| C-18 agents, training_schools lobbying_effort increase | no | missing record fact (no agents role) and missing rule (schools' lobbying) |
| C-19 grandfathered lobbying_effort ambiguous | no | missing record fact: engine row on `inspectors.licensed`; also the unqualified increase beside it (WRONG row) |
| C-20 engineers.exempt quantity_substitute increase | no | missing record fact: exempt substitutes have no role field |
| C-21 buyers.substitutes price_substitute increase | no | missing record fact and rule (RS-16 1.0, CR-6) |
| C-22 engineers.exempt quality_information increase | no | missing record fact and rule (CR-11) |
| C-23 inspectors.linmouth quantity_supplied decrease | no | missing record fact: `neighbor_seller_actor` is a per-unit-tax field |
| C-24 inspection_firms asset_value (U1) | no | unsupported form: CR-7c with readings; no firms role |
| C-25 referral users search_cost (U1) | no | unsupported form: K4 rule on agents; engine's search_cost is a different chain (WRONG row) |
| C-26 buyers.current quality_per_unit ambiguous | no | missing rule: EN-4 not encoded |
| C-27 insurers quantity_traded increase | no | missing record fact and rule: no `input_supplier_actor` for licensing |
| C-28 licensed compliance_cost (complaints) | no | missing rule: RS-20 |
| C-29 buyers.current resources_available_other_uses decrease | yes | |
| C-30 Board enforcement_cost increase | yes | |
| C-31 Board non_tax_receipts increase | no | missing rule: CR-1 / CR-8b receipts from fees and fines |
| C-32 prospective entry_rate ambiguous (medium) | no | missing rule: EN-1 1.0 horizons |
| C-33 prospective entry_rate decrease (long) | no | missing rule: EN-1 1.0 horizons (CR-10b) |
| C-34 buyers.unlicensed quality_information decrease | no | missing record fact: no such role; the engine puts the loss on all buyers (WRONG rows) |
| C-35 engineering_other price_paid increase | no | missing record fact and rule (CR-9, CR-7a) |
| C-36 trainees resources_available_other_uses decrease | no | missing record fact: trainees who stay |
| C-37 Board fund_balance ambiguous | no | missing rule: CR-8b (1.0) with OC-1; no receipts side |

## General gaps

Ranked by table rows added or fixed. Each is a pattern-level change, not a WE-055 provision.

1. **Subclasses made by an exemption or a line (EN-1, EN-2, EN-3 with RS-1, RS-16; CR-9).** A licensing component has no fields for the exempt substitutes (engineers), would-be entrants, those who qualify under a lesser route (grandfathered), or neighbouring-jurisdiction sellers. Adding `exempt_actor`, `prospective_actor`, `qualifies_actor`/`excluded_actor` and reusing `neighbor_seller_actor` would add or re-class C-1, C-4, C-8, C-19, C-20, C-21, C-22, C-23, C-35, C-36: up to 10 rows. The same gap in WE-003 appeared as the businesses that employ braiders (C-18 there).
2. **Information loss lands on the buyers of unlicensed service (EN-3, RS-3, RS-10, CR-11b).** A role `unlicensed_buyer_actor` for the RS-3 rows (quality_information, search_cost, disputes) would fix the 2 WRONG rows (quality_information, search_cost) and add C-3 (U1-a) and C-34: 4 rows touched. EN-11 then keeps its increase for the whole buyer class.
3. **RS-8 and RS-17 for licensing with a deadline or line.** `announcement_window` is read for no licensing rule. A rule for training enrollment bunching before the deadline (RS-8, CR-10a), and a grandfathering-line field with RS-17 and its mirror and rivals forms, would add C-10, C-11, C-12, C-13 (and C-15 as OC-2 for the application): 5 rows.
4. **Receipts side of enforcement (CR-1, CR-8b, OC-1, OC-3).** The Board's fees and fines (`non_tax_receipts`) and the fund balance (CR-8b 1.0, ambiguous when fee-funded) are not derived: C-31, C-37, and part of C-28 (OC-2 complaint answering, RS-20): 3 rows.
5. **EN-1 1.0 horizons.** Entry is signed short only. EN-1's refill chain (CR-4, CR-7a, CR-10b) gives medium ambiguous and long decrease: C-32, C-33 (C-4 by class): 2 to 3 rows. Trainer enrollment by horizon (C-14, CR-12b): 1 row.
6. **RS-7 Unless and EN-5 together.** When `field_contested` is set the holders' unqualified increase and the contested-field ambiguous are both reported. Where the contested answer holds, only the second should stand for the same class (the clause is a re-basing against the counterfactual campaign, handbook 1.0 baseline note 9). This removes 1 WRONG row and lets C-19 match once gap 1 names the class.
7. **Input suppliers for licensing.** `input_supplier_actor` exists for tariffs and price ceilings; a licensing component that requires insurance or a bond should take it (CR-1, CR-9, EN-1): C-27, 1 row.
8. **EN-4 (quality received, ambiguous by default).** Not encoded: C-26, 1 row.
9. **Unclear provisions that change no component field (U1).** K4 is a rule on a third party's conduct; U1's readings change C-3, C-24 and C-25 but nothing a parser can write in `reading_fields`. A general `referral_restricted` flag on licensing (agents recommend inspectors as now, or may not) would let a reading set it and let CR-11c and CR-9 fire per reading: C-3, C-24, C-25 (3 rows, which also need gaps 2 and a firms role).

## After the rule changes (second commit)

General fixes from the five out-of-sample runs on licensing and quotas (`rules/licensing.lp`): buyers of the unlicensed or unrecorded trade have their own role (`informal_buyer_actor`), so RS-3 and RS-10 fall on them, not on every buyer; trainers' demand is ambiguous where the training was already common (`training_common`, CR-4b with CR-12b); a price fixed by a rule in force without the measure (`price_fixed`) withholds the price rows and signs excess demand (PC-1); an import quota takes the tariff chains (EN-6: as under TX-7). The record names the buyers of unlicensed inspections (`informal_buyer_actor`). Rows produced: 8 of 37 (was 7): C-34. WRONG: 0 (was 3). Two were the RS-3 rows on all buyers. The third, the license holders' lobbying increase beside the contested-field row (C-19), is reclassified as defensible: CR-4 1.1 signs lobbying over provisions that exist only under the measure as an increase, and WE-067 and WE-065 list both rows.
