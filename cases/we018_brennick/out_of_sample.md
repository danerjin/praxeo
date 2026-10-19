# Out-of-sample run of the prohibition rules on WE-018 (Brennick Carryout Bag Ordinance)

Rules as they were at commit 9c6d2e9 (prohibition rules written from WE-017 only). Nothing under `praxeo/` was changed. Record: `record.json`, one `prohibition` component (K1: bound `retailers.brennick`, buyers `shoppers`, informal seller `retailers.small`, mobile buyers `shoppers.edge`, neighbour sellers `retailers.fallow_creek`, substitute sellers `sellers.substitutes`, `definition_line`, `announcement_window`, `general_budget`) and one `price_floor` component (K2, the paper-bag charge) that no rule reads. K3 (enforcement) is folded into K1's `enforcer_actor` and `general_budget`. U1 (verification of the 125-use design) changes no component, so it has one reading and no `reading_fields`. Answers: `answers.json`, from WE-018's assumption table where a row exists (A-1, A-2, A-4, A-5, A-6, A-7, A-8); three questions (`demand_persists`, `enforcement_risk`, `no_other_use`) have no matching assumption and were judged from the text. Run: `python3 -m praxeo cases/we018_brennick --out cases/we018_brennick/sample_run` (verifier and citation problems empty). Key: (actor class, variable, sign, window); the table's "retailers" in C-11 is matched to `retailers.brennick`.

Summary: the table has 22 rows (C-1 to C-22). The engine reports 14 consequences (of 24 derived; the rest are below the cut-off), which give 16 keys (the OC-1 entry is a group of three actor classes). Table rows produced by key: 7 (C-1, C-3, C-9, C-10, C-11, C-12, C-22); C-11 for the retailers only. Rows not produced: 15. Engine rows classified WRONG: 3.

## Engine rows (reported)

| Engine row | Class | Why |
|---|---|---|
| retailers.brennick quantity_traded decrease; shoppers quantity_traded decrease | in table | C-1 (EN-7). The bag makers have no role |
| shoppers quantity_substitute increase | in table | C-3 (RS-1) |
| shoppers quantity_demanded increase, window announcement | in table | C-10 (RS-8) |
| shoppers.edge cross_border_purchases increase | in table | C-9 (RS-4) |
| retailers.fallow_creek quantity_traded increase | in table | C-12 |
| retailers.brennick lobbying_effort increase | in table | C-11 (retailers' side) |
| officials.enforcement enforcement_cost increase | in table | C-22 (OC-3) |
| retailers.small reclassification increase | defensible | RS-5 puts it on the informal-seller role; the table puts it on `retailers.brennick` (C-7) |
| sellers.substitutes reclassification increase | defensible | section 8: bag makers design cheap bags that just meet the 4 mil and 125-use line; the table lists only the retailers (C-7) |
| taxpayers, taxpayers.future, recipients.other_spending resources_available_other_uses at_least_one_decrease | defensible | OC-1 as a group; the table assumes a budget that rises with the task and gives taxpayers a plain decrease (C-19) |
| **retailers.brennick number_of_sellers decrease** | **WRONG** | EN-7's legal sellers leave the trade. Here the ban is on a free giveaway; no store stops selling because of it |
| **shoppers lobbying_effort increase** | **WRONG** | RS-7 gives the buyers of the banned good lobbying. The table has makers, substitute makers and retailers only (C-11); shoppers have no concentrated stake in a 2-cent bag |
| **shoppers.edge search_cost increase** | **WRONG** | RS-4's crossing cost. Section 9 says no separate travel cost is recorded: edge shoppers find the other store about as convenient |

## Table rows

| Row | Produced? | Reason |
|---|---|---|
| C-1 thin bags quantity_traded decrease | yes (part) | shoppers and retailers; no bag-makers role |
| C-2 shoppers price_paid increase | no | unsupported form: K2 is a `price_floor`, which has no rule. The engine's own price_paid (the risk price of EN-7) is unreported, since it needs `demand_persists` (0.2) |
| C-3 shoppers quantity_substitute increase | yes | |
| C-4 households.bag_reusers quantity_substitute increase | no | missing record fact: no household role and no `secondary_use` relation |
| C-5 retailers compliance_cost increase | no | missing rule: compliance cost of the bound sellers under a prohibition (CR-8c, Tier A, no assumption) |
| C-6 retailers net_price_received increase | no | unsupported form (K2) |
| C-7 retailers.brennick reclassification increase | no | role: the rule signs the informal-seller and substitute-seller roles, not the bound sellers who sell the thick bags |
| C-8 retailers.small informal_activity increase | no | missing rule: RS-3 is a hidden market gated on `demand_persists`; open non-compliance by small stores (A-5) does not need persisting demand |
| C-9 shoppers.edge cross_border_purchases increase | yes | |
| C-10 shoppers quantity_demanded increase (announcement) | yes | |
| C-11 bag makers, substitute makers, retailers lobbying_effort increase | yes (part) | retailers only; no bag-makers role, and `sellers.substitutes` lobbying is not derived |
| C-12 retailers.fallow_creek quantity_traded increase | yes | |
| C-13 retailers.edge quantity_traded decrease | no | missing record fact and rule: no edge-store role; the mirror of the neighbours' gain is not encoded |
| C-14 retailers.edge employment, hours_worked at_least_one_decrease | no | missing rule: OC-5 |
| C-15 retailers.brennick resources_available_other_uses ambiguous | no | combiner: no declared comparison |
| C-16 shoppers price_paid (groceries) ambiguous | no | combiner and missing rule: RS-14 pass-through |
| C-17 shoppers resources_available_other_uses decrease | no | missing rule: OC-1 for the buyers' spending (K2 and RS-1) |
| C-18 households.bag_reusers resources_available_other_uses decrease | no | missing record fact (household role) and rule |
| C-19 taxpayers resources_available_other_uses decrease | no (sign form) | the engine's group sign is `at_least_one_decrease` |
| C-20 retailers.fallow_creek employment, hours_worked at_least_one_increase | no | missing rule: OC-5 |
| C-21 sellers.substitutes quantity_traded increase | no | missing rule: CR-9 (`input_to`) for paper-bag makers |
| C-22 officials.enforcement enforcement_cost increase | yes | |

## General gaps

Ranked by table rows added or fixed.

1. **Price floor as a companion instrument (C-2, C-6, C-17; also C-21 and the paper side of C-3).** The handbook treats a minimum charge on a good retailers would otherwise give away (K2, RS-1, RS-5, TS-3) as a price rule. `price_floor` is a legal instrument name with no rules. A general price-floor pattern (buyers' price rises to the floor, sellers' net price received rises, buyers' spending falls on OC-1) would add 3 to 4 rows. At present K2's roles are not read by any rule.
2. **Compliance cost of bound sellers and fee handling (C-5), Tier A.** A prohibition, like a tax or licence, imposes compliance cost (CR-8c) on the bound sellers whenever the rule is enforced; no assumption is needed. 1 row, plus the input to C-15 and C-16.
3. **OC-5 staffing and the whole-basket mirror (C-13, C-14, C-20).** RS-4 with RS-9 gives the neighbours' gain; the mirror on the bound sellers near the line (`retailers.edge` subclass, or the bound role itself at the margin) and OC-5's group `at_least_one_*` on employment and hours for both sides are not derived. 3 rows (2 with a new edge role).
4. **Open non-compliance by the bound sellers (C-8) versus a hidden market.** RS-3 informal activity requires `demand_persists`; WE-018 A-5 (small stores keep giving bags, unchecked) is independent of buyers' willingness to seek the good out. A second route, gated on `enforced` failing and `evasion` alone, would give C-8 and also the missing `informal_activity` row without demand. 1 row.
5. **RS-5 reclassification on the sellers of the near-definition goods (C-7).** The rule signs the informal-seller and substitute-seller roles; the handbook signs the bound sellers when they sell goods just outside the line. Either allow the bound role or let a parser set `substitute_seller_actor` to the retailers. 1 row. A parser choice (retailers as the substitute sellers) would produce it, at the cost of the paper-bag makers' role.
6. **Households and secondary use (C-4, C-18).** A `secondary_use` substitute relation (RS-1) with a household role. 2 rows.
7. **OC-1 group sign (C-19).** Under a budget "taken here as rising with the new task" the handbook gives taxpayers a plain decrease; the engine gives the three-class group `at_least_one_decrease`. The plain decrease follows when the text says the budget rises; the record has no field for that. 1 row.
8. **WRONG rows to gate.** EN-7's `number_of_sellers` should need that the banned good is the sellers' trade, not an incidental giveaway (a record fact, as `protected_concentrated` is for ceilings). RS-7's buyers' lobbying should need a concentrated stake (the same flag). RS-4's crossing search cost should not apply when the shift is a change of store with the same convenience (WE-018 section 9). Removing these removes 3 WRONG rows and no table rows.
9. **Combiners (C-15, C-16).** RS-14 and CR-12b comparisons across compliance cost and bag savings. 2 rows; these depend on gaps 1 and 2.
10. **Bag-makers role (C-1, C-11).** A prohibition has no input-supplier role (EN-7 loses the makers' quantity decrease, RS-7 their lobbying). Parts of two rows.
