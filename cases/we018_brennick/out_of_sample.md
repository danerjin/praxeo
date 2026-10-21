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

## After the rule changes (second commit)

General fixes from the out-of-sample runs on WE-018, WE-037, WE-044, WE-050 and WE-053 (`rules/prohibition.lp`): fewer legal sellers only where they cannot turn to other products (`no_other_use`); the underground trade needs the ban to be enforced; the risk price needs an underground trade; the buyers lobby only with their own premise (`buyers_organize`); buying across the boundary costs time only where it takes an extra trip (`crossing_extra_trip`); a ban on a practice of legal firms (`practice_ban`) makes evasion a legal breach, not an informal market; fees or fines paid into the budget that funds enforcement (`fees_to_budget`) leave the payers' net unsigned. The answers gained the two new questions. Rows produced: 7 of 22 (unchanged). WRONG: 0 (was 3).


## Out-of-sample run of the floor rules

Rules as at commit 5944604 (`praxeo/rules/floors.lp`, PC-9 to PC-11 as CR-6, developed on WE-009). Nothing under `praxeo/` was changed. K2 (the paper-bag charge, a `price_floor`) was recorded for the prohibition run and no rule read it; the floor rules now read it, and the fixture had no answers for the new k2 questions.

**What was recorded.** Only K2 changed. `seller_actor` = `retailers.brennick` (the sellers held at the charge; table C-6); `contract_kind` = `sale` (the field defaults to `employment`; the charge is on a good); `mobile_buyer_actor` = `shoppers.edge` (section 5, C-9: the fee is what pushes edge shoppers over the line); `substitute_seller_actor` = `sellers.substitutes` (reusable bags, C-3, C-21, RS-1 in section 2). `bound_actor` was changed from `retailers.brennick` to `shoppers`: floors.lp reads `bound` as the buyers who must pay at least the floor, and the table puts the price rise on the shoppers (C-2). Not set, and why: `excluded_actor` (the table names no one left out), `output_buyer_actor` (C-16 is the shoppers' grocery prices, ambiguous between compliance costs and bag savings; the floor does not raise retailers' cost, so RS-14 from the floor would give an increase alone), `definition_line` (K2's RS-5 row, C-7, is on the retailers, and the rule would sign the bound buyers), `lower_tier_seller_actor`, `asset_owner_actor`, `fixed_budget`. `protected_actor` `shoppers.assistance` (bags free for food-assistance customers) is not read by any floor rule.

**What was answered (8 new answers, `k2.*`).** From the assumption table: `enforced` A-1 (0.85), `evasion` A-5 (0.6), `sellers_organize` A-8 (0.7), `cross_border_feasible` A-6 (0.55), `substitute_exists` A-2 (0.95). Judged from the text, and said so in each rationale: `binding` (0.95; section 2 classifies K2 as binding because stores would otherwise give paper bags free), `cost_not_offset` (0.85, the figure of A-1 on which C-2 rests; shoppers who take paper pay at least 10 cents), `can_organize` (no, 0.1; the bound buyers are shoppers, and A-8 names makers and retailers; same reading as `k1.buyers_organize`). Run: `python3 -m praxeo cases/we018_brennick --out cases/we018_brennick/sample_run` (verifier and citation problems empty).

**Numbers.**

| | Before (K2 unread) | After |
|---|---|---|
| Table rows produced | 7 of 22 | 10 of 22 (adds C-2, C-6, C-21) |
| Engine consequences reported (derived) | 11 (24) | 17 (29) |
| Engine keys (actor, variable, sign, window) | 13 | 19 |
| Engine rows WRONG | 0 | 2 rows, and 1 more masked inside a key of the table (see below) |

### New engine rows

| Engine row | Class | Why |
|---|---|---|
| shoppers price_paid increase | in table | C-2 (PC-9: the buyers pay at least the charge) |
| retailers.brennick net_price_received increase | in table | C-6 (the store keeps the fee) |
| sellers.substitutes quantity_traded increase | in table | C-21; derived by RS-1 from the floor, where the table cites CR-9 |
| retailers.brennick excess_supply increase | defensible | PC-9 on the sellers' side: at 10 cents against a cost of a few cents retailers would sell more bags than shoppers take. The example lists no surplus of bags, and bags are handed out on request, so this is weak |
| **shoppers compliance_cost increase** | **WRONG** | OC-2 signs the floor's compliance cost on `bound`, here the shoppers. The example puts it on the retailers (C-5: stock, tills, signs, training, fee handling); shoppers comply with nothing |
| **shoppers informal_activity increase** | **WRONG** | RS-3 signs the evasion on `bound`. The example puts it on the small stores that waive the fee (C-8, A-5), not on shoppers |
| **shoppers and retailers.brennick quantity_traded decrease (masked)** | **WRONG** | PC-9's "fewer units traded" (`fl_fewer`) for the paper bags is merged into K1's consequence with the same key, which is C-1 for the thin bags, so the row looks like a table row. For paper bags the example says the opposite: they are bought more (C-3, C-21), and use stays above the counterfactual as habits form (section 8). The test checks that `fl_fewer(k2)` is in the derivation |

The floor's RS-4, RS-1 and RS-7 chains give keys K1 already gave (shoppers.edge cross_border_purchases, shoppers quantity_substitute, retailers lobbying_effort), so they add no row.

### Table rows newly produced

| Row | Produced? | Reason |
|---|---|---|
| C-2 shoppers price_paid increase | yes (was: unsupported form, K2 had no rule) | |
| C-6 retailers net_price_received increase | yes (was: unsupported form) | |
| C-21 sellers.substitutes quantity_traded increase | yes (was: missing rule CR-9) | the floor's RS-1 gives it with `substitute_exists` (A-2) |

Rows that K2 touches and the floor rules still miss: C-5 (role: the compliance cost lands on the bound buyers), C-8 (role: the evasion lands on the bound buyers, and the table row is for `retailers.small`), C-7 (the RS-5 reclassification is on the retailers; not recorded for the reason above), C-16 and C-17 (no output-buyer reading, no rule for the buyers' spending), C-19 and C-4 (not floor rows).

### Patterns for the rule writer

1. **`bound` does three jobs in floors.lp, and a floor on a seller's price splits them.** The buyers who pay more, the party the law binds (and who complies, OC-2), and the party who evades (RS-3) are one role, `bound`. A wage floor has them all in the employer. A minimum charge on a good has the law bind the seller while the buyer pays more. With `bound` = shoppers (as the schema comment asks) C-2 is right and the compliance cost and the evasion land on shoppers (two WRONG rows; C-5 and C-8 are missed). Tried the other way, with `bound` = `retailers.brennick` as recorded for the prohibition: C-5 appears, but `price_paid` and `quantity_substitute` land on the retailers and C-2 is lost. A separate role for the party the law binds and who complies (the sellers, for a minimum price) would give both. Rows: C-2, C-5, C-7, C-8, the two WRONG rows.
2. **A floor next to a ban on its substitute.** PC-9's "fewer units traded" assumes the floor lifts the price of a good people would buy anyway, against a counterfactual in which it is bought at a low price. Here the counterfactual price of paper is zero and the ban on thin bags sends buyers to paper, so the quantity rises (C-3, C-21), the opposite of `fl_fewer`. The rule needs a premise that the demand is not being moved by a companion measure in the same Act, or the floor's quantity effect should be left to the combiner against RS-1. Rows: the masked WRONG row, C-3, C-21.
3. **Consequences of different components merge under one key.** K1's thin-bag `quantity_traded` and K2's paper-bag `quantity_traded` have the same (actor, variable, sign, window) and are reported as one row, which hides a WRONG derivation behind a table row. The good, or at least the component, should be part of the key (the report names the variable without the good, as the table does in brackets). Rows: C-1 and the masked row.
4. **PC-9 `excess_supply` on sellers with no excluded role.** The rule signs the sellers when `excluded_actor` is empty, whether or not they want to sell more at the floor. For a good handed out on request that premise is not shown by the record. A question or a role (do sellers press the good?) would gate it. Row: the defensible `excess_supply`.
