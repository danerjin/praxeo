# Out-of-sample run of the mandate rules on WE-059 (Kestrava Fair Repair Act)

Rules as they were at commit 96d60b0 (`praxeo/rules/mandates.lp`: PC-17 developed on WE-029; PC-18 and EN-14 written from the catalog alone). Nothing under `praxeo/` was changed. Example: `handbook/05_examples/WE-059_right_to_repair.md`.

Record: `record.json`, seven components, the Act's K1 to K3 split by product line because a component has one bound class and the table keeps `makers.ag` and `makers.phone` apart.

- `k1a`, `k1p`: `mandated_contract_term` (K1). Bound `makers.ag` / `makers.phone`; recipients `owners.ag` / `owners.phone`; output buyers `buyers.prospective`; `complaint_only`; `field_contested` (bills failed in 2023 and 2025); `announcement_window`. `k1a` also has `definition_line` (farm equipment "designed primarily for agricultural use"). `k1p` has `already_provider_actor` and `rival_actors` = `makers.phone.matching` (the one maker whose national program already matches K1).
- `k2a`, `k2p`, `k2d`: `term_prohibition` (K2). Bound `makers.ag`, `makers.phone`, `dealers.ag`; freed party the owners; `voids_existing`.
- `k3a`, `k3p`: `product_standard` (K3). Bound the makers; buyers `buyers.prospective`; `stock_exempt` with stock owners `owners.ag.exempt` and `owners.phone.exempt` (equipment sold before 2023).
- K4 (enforcement) is folded into `enforcer_actor` (`officials.enforcement`). `general_budget` is false: the Division's budget is unchanged, so no OC-1 payers.
- Not recorded because no role in the rules fits: independents (the third-party recipients of K1), authorized providers, technicians, used-phone buyers, third-party parts sellers. `tradable_actor` is left empty: it means providers selling against unbound rivals across a line, and the makers do not compete with the six Darnholt dealers.
- U1 (pairing) is recorded as an unclear provision with both readings but no `reading_fields`: neither reading changes a Component field.

Answers: 56, one per question. Probabilities taken from the assumption table where a row matches: A-1 (enforced, 0.7), A-2 (binding, 0.9), A-9 (reshaping, 0.55), A-10 (complaints, 0.7), A-12 (valued on earnings, 0.85), A-22 (buyers value the standard, 0.7), A-23 (can organize, 0.85), A-6 (term valued by the party that used it, 0.85). The others are judged from the text and say so: `wages_sticky` 0.8 (units already sold carry the term and their prices cannot be renegotiated), `wages_adjust` 0.1 (read literally for a sale: the owner's price does not fall), `worth_less` 0.6, `alternatives_worse` 0.3, `rivals_bound` 0.9, `complaint_unlikely` 0.6 (farm) and 0.7 (phones), `conditions_differ` 0.2, `compete_with_bound` 0.9, `contested_otherwise` 0.8, `stock_competes` 0.7 (farm) and 0.6 (phones), `binding` and `enforced` for K3 0.8 and 0.7, `substitute_terms` 0.8 (makers) and 0.4 (dealers), `recipients_organize` 0.3 for phone owners. The verifier and citation problems are empty (`sample_run/`).

Summary: the table has 47 rows (C-1 to C-47). The engine derives 54 consequences and reports 46 (8 are below the cut-off), which give 50 keys. Table rows produced by key: 8 (C-19, C-20, C-22, C-23, C-26, C-28, C-40, C-46); C-46 is produced for the farm side only, and C-23 by a different chain than the example's. Rows not produced: 39. Engine rows classified WRONG: 14 of the 46 (15 in the table, 17 defensible).

## Engine rows (reported)

| Engine row | Class | Why |
|---|---|---|
| makers.ag, makers.phone compliance_cost increase | in table | C-40 (OC-2, Tier A) |
| makers.ag, makers.phone legal_breach increase | in table | C-20 (RS-20 from none) |
| makers.ag reclassification increase | in table | C-19 (RS-5, A-9) |
| makers.ag, makers.phone asset_value decrease | in table | C-26 (CR-7c, A-12), also voided terms (CR-8) |
| makers.ag, makers.phone, dealers.ag, owners.ag lobbying_effort increase | in table | C-22 (RS-7); the table's "lobbying groups" are makers, dealers and farm groups |
| owners.ag.exempt asset_value ambiguous | in table | C-28: EN-14's rise in the stock's value against its Unless clause (buyers value the standard, A-22) |
| buyers.prospective price_paid increase | in table (farm) | C-46 (RS-14 with the cost staying with makers). The phone half contradicts C-9, which keeps the phone price in a group: see makers.phone price_paid below |
| makers.ag price_paid increase | in table by name | C-46 lists `makers.ag` beside the buyers; the rule means the makers' cost per unit (CR-1, CR-5c) |
| dealers.ag asset_value decrease | in table by key | C-23. The chain is K2's voided terms (CR-8) in the dealers' agreements; the example's reason is lost service income (C-6, C-7), which has no rule here |
| buyers.prospective specification_level increase | defensible | EN-14: the standard raises what new units must do. The example records the same fact as pairing removed (C-12) and as repairability valued (A-22, C-38) |
| makers.ag, makers.phone return_on_capital decrease; resources_available_other_uses decrease | defensible | CR-7b, CR-8b: the cost stays with makers while prices are fixed (units already sold). The example's measure of the loss is value (C-26) and cost (C-40); it signs means only for owners (C-39, final check 4) |
| makers.phone.matching asset_value increase | defensible | CR-7c, CR-9 for the one maker already offering the term (A-2); the example does not single it out |
| makers.phone.matching quantity_supplied increase | defensible | CR-9. The chain runs through the PC-17 group, which the example's CR-12 (1.1) rule does not allow as a chain; the example does not say the gain does not occur |
| makers.ag, makers.phone, dealers.ag, owners.ag lobbying_effort ambiguous (policy_field) | defensible | RS-7 Unless: lobbying on right to repair as such is against the contest of 2023 and 2025; C-22 leaves it unsigned |
| officials.enforcement enforcement_cost increase | defensible | OC-3, Tier A. With the fixed budget (OC-3 0.9) the example records the same work as other complaints waiting (C-41) |
| owners.ag, owners.phone compliance_cost increase | defensible | RS-20: recipients spend time on complaints; the example records the complaints (C-44) |
| owners.ag, owners.phone non_wage_compensation increase | defensible | the term itself; the example records it as cheaper inputs (C-1) and information (C-37) |
| owners.phone.exempt asset_value ambiguous | defensible | EN-14 with Unless for phones sold before 2023; the example applies it to tractors |
| **buyers.prospective quantity_traded decrease** | **WRONG** | RS-14 pass-through. C-30 gives new sales `ambiguous` (buyers value the term, A-22, against dearer units) |
| **makers.ag, makers.phone quantity_supplied decrease** | **WRONG** | EN-14 "fewer units are built"; same as C-30. Unless gates only the stock's value |
| **makers.ag, makers.phone term_prevalence increase** | **WRONG** | PC-18's shift to substitute terms signed alone; C-10 keeps it in a group with the price, "not netted" (final check 2) |
| **makers.phone price_paid increase** | **WRONG** | the phone price is a member of C-9; A-6 names no member, and only the farm price is signed alone (C-46, A-18) |
| **owners.ag, owners.phone employment, hours_worked, non_wage_compensation at_least_one_decrease** | **WRONG** | PC-17's employment group on buyers. The example's group for a sale is price, warranty, models (C-9) |
| **owners.ag, owners.phone wage_rate, non_wage_compensation at_least_one_decrease** | **WRONG** | PC-18's wage and benefits group on buyers; the example's version is C-10 |
| **owners.ag, owners.phone earnings decrease** | **WRONG** | CR-12 earnings from the PC-17 group; owners have no earnings from this contract and C-39 has them with more to spend |
| **owners.ag.exempt, owners.phone.exempt stock_age increase** | **WRONG** | EN-14's "kept in use longer"; the example applies it to covered units, not exempt ones (C-29) |

## Table rows

| Row | Produced? | Reason |
|---|---|---|
| C-1 price of genuine parts, tools, software decrease | no | missing rule: PC-17 gives the recipients the term, not a fall in the price of the inputs; independents have no role |
| C-2 independents quantity_traded increase | no | role: independents; RS-1 for a mandate is not encoded |
| C-3 owners.ag home_production increase | no | missing rule: RS-1 |
| C-4 owners price_paid (independent repair) decrease | no | role: independents; RS-16 per unit of quality, CR-12e |
| C-5 term_prevalence decrease | no | missing rule: PC-18's direct effect; the engine's term_prevalence is the substitute-term increase |
| C-6 authorized repairs quantity_traded decrease | no | missing rule: RS-16 mirror; role: authorized providers |
| C-7 authorized repairs price or wait | no | missing rule: RS-16 mirror with waiting; role |
| C-8 entry_rate increase | no | role: independents.prospective; RS-6 in reverse |
| C-9 phones price (+), warranty (-), variety (-) | no | missing rule: PC-17's group for a sale; the engine's group is wages, hours, jobs |
| C-10 substitute terms (+), price (+) | no | sign form: the engine signs the substitute-term member alone and has no price member |
| C-11 dealers tax_share_borne increase | no | missing rule: CR-7b across makers, dealers, buyers; the engine's incidence needs `wages_adjust` and falls on the recipients |
| C-12 pairing product_attribute | no | unsupported form: no rule for product_attribute; no per-reading fields |
| C-13 non-genuine parts quantity_traded | no | role: third-party sellers; RS-1, CR-4 |
| C-14 stolen-parts trade | no | unsupported form: RS-3 under a standard; per-reading |
| C-15 authorized repairs, deferred (window) | no | missing rule: RS-8 for mandates |
| C-16 independent repairs, first months | no | missing rule: RS-8 first months |
| C-17 cross-border farm purchases ambiguous | no | missing rule: RS-4 for buyers under a mandate; combiner |
| C-18 Darnholt phone owners price_paid decrease | no | missing rule: CR-9 for makers extending a program |
| C-19 makers.ag reclassification increase | yes | |
| C-20 makers legal_breach increase | yes | |
| C-21 specialty models variety decrease | no | missing rule: RS-24 |
| C-22 lobbying on questions under the Act | yes | |
| C-23 dealers asset_value decrease | yes (by key) | the chain is K2's voided terms, not lost service income |
| C-24 independents return_on_capital increase | no | role: independents; CR-7a |
| C-25 independents return_on_capital no_change (long) | no | role; combiner: CR-12e response argument |
| C-26 makers asset_value decrease | yes | |
| C-27 owners asset_value of covered units increase | no | missing rule: CR-7c, RS-12 for the recipients' asset |
| C-28 exempt tractors asset_value ambiguous | yes | EN-14 with Unless |
| C-29 covered units stock_age ambiguous | no | missing rule: CR-10b; the engine has the exempt stock's stock_age, with the wrong sign |
| C-30 new sales quantity_traded ambiguous | no | combiner: the engine has the decrease chain only |
| C-31 dealers parts price ambiguous | no | missing rule: CR-5c for the maker-dealer exchange |
| C-32 harvest wait decrease | no | missing rule: CR-6 queue margin |
| C-33 technicians at dealers | no | role: technicians; RS-6, CR-9, LW-10 |
| C-34 technicians at independents | no | role; OC-5 |
| C-35 technicians wage_rate ambiguous | no | role; combiner |
| C-36 used-phone buyers information | no | role; CR-11c |
| C-37 diagnostic information increase | no | missing rule: EN-15 |
| C-38 replaceable parts product_attribute | no | unsupported form: product_attribute, TS-3 |
| C-39 owners resources_available_other_uses increase | no | missing rule: CR-8b for owners; depends on C-4 |
| C-40 makers compliance_cost increase | yes | |
| C-41 Division: other complaints wait | no | missing rule: OC-3's fixed-budget case; role: complainants.other |
| C-42 independents investment_target increase | no | role; CR-4, CR-8a |
| C-43 dealers parts counter quantity_traded decrease | no | missing rule: CR-9 |
| C-44 complaints (applications) increase | no | missing rule: RS-20 gives owners a compliance cost and makers a breach, not the complaints |
| C-45 genuine phone parts quantity_traded | no | missing rule: CR-9, LW-10; per-reading |
| C-46 farm prices of new equipment increase | yes (farm) | RS-14 pass-through; the phone half is WRONG (C-9) |
| C-47 independent repair price before entry ambiguous | no | role; CR-6 against CR-5c; combiner |

## Patterns for the rule writer

General, pattern-level problems the run shows, ranked by rows affected.

1. **PC-17 and PC-18 are written for employment and are applied to a sale.** The adjusting terms are wage_rate, employment, hours_worked, non_wage_compensation, earnings. For a mandated term in the sale of goods (K1) or a void term in it (K2) the example's adjusting terms are price, warranty and the models offered (C-9, C-10). Run on a sale, the rules put jobs, hours, wages and earnings on owners who are buyers: 6 of the 14 WRONG rows (owners.ag and owners.phone: the employment group, the wage group, earnings), and the engine's group has no price or warranty member, so C-9 and C-10 are not produced. The questions share the problem: `wages_sticky`, `wages_adjust` ("can the wage (or price) adjust downward") and `worth_less` presume a wage that falls, and the answer had to be read literally for a sale (price does not fall). A kind-of-contract field on the component (employment, sale) that selects the variable set and the question wording would repair this. Rows: C-9, C-10, C-11, and the 6 WRONG owners rows.
2. **A group member is signed alone, and a group conclusion is used as a premise.** The example holds a firm line: a group member is a chain only if its own premise names it (CR-12 1.1). The rules do not: RS-14 signs the buyers' price (and then their quantity) from "cost stays" and "rivals bound" for phones as well as farm equipment (C-9 keeps the phone price in a group; only the farm price is signed alone, on A-18); PC-18 signs the substitute-term shift alone (C-10); the PC-17 group (`mc_others_medium`) is a premise of the unbound rivals' sales and of earnings. The ag and phone components merge in one key (`buyers.prospective price_paid increase`), so the farm result hides the phone half. A rule that signs a member alone needs its own premise, and a group should not feed a further `effect`. Rows: C-9, C-10, C-46; engine rows makers.phone price_paid, term_prevalence (both makers), makers.phone.matching quantity_supplied, owners earnings.
3. **EN-14's Unless clause gates the stock's value only.** When buyers value the standard (A-22, answered yes for K3), the example turns three conclusions from EN-14's plain form into `ambiguous` or removes them: the exempt stock's value (produced, C-28), the age of the stock (the kept-longer conclusion belongs to covered units, C-29) and the number of new units sold (C-30, against the dearer units). The rules apply the clause to `asset_value` alone: `stock_age` stays an increase for the exempt stock, and new units' `quantity_supplied` and (through RS-14) the buyers' `quantity_traded` stay decreases. Both should become an opposing chain against the buyers' valuation, giving `ambiguous`. Rows: C-29, C-30; 5 WRONG engine rows (stock_age twice, quantity_supplied twice, buyers' quantity_traded).
4. **A term owed to third parties has one recipient class.** K1 is invoked mainly by independents, whom the owner hires; the component has `recipient_actor` for the contract's party only. The largest block of unproduced rows needs the independent repairers, the authorized providers and the dealers' parts counter as classes with RS-1 (repairs move outside the makers' network), the RS-16 mirror (the substitute loses demand; price and wait as a group), entry (RS-6 in reverse, CR-7a, CR-12e) and RS-12 (the owners' covered units rise in value). Rows: C-1, C-2, C-3, C-4, C-6, C-7, C-8, C-24, C-25, C-27, C-39, C-42, C-43, C-47. This is a new pattern, not a patch: a mandated term owed to third parties moves the bargaining range of a third exchange (PC-17 1.1).
5. **Direct effects are missing.** PC-18 derives the substitute-term shift but not the fall in enforceable terms (C-5). PC-17 derives the term as `non_wage_compensation` but not the price fall of the mandated inputs (C-1). RS-20 derives breach and the recipients' cost but not the complaints (C-44). EN-15 (a disclosure mandate: C-37) and OC-3's fixed-budget case (C-41) have no rule. Rows: C-1, C-5, C-37, C-41, C-44.
6. **RS-8 is not encoded for mandates.** `announcement_window` is set (18 months between signing and effect) and read by no mandate rule: no deferral of authorized repairs before the date, no rush of independent and self repairs after it. Rows: C-15, C-16.
7. **The boundary rules assume providers facing rivals.** `tradable_actor` and `neighbor_seller_actor` model providers selling against unbound rivals. Here the crossing is by buyers (farm owners buying from Darnholt dealers, RS-4 with two chains) and by makers choosing to extend a program to all states (CR-9). Rows: C-17, C-18. Fixed cost per item offered (RS-24, specialty models) also has no rule: C-21.
8. **A reading that changes a premise, not a field, has no channel.** U1 decides whether K3 binds on the maker whose pairing already complies, whether parts from stolen phones work, and what a used phone's notices tell. None is a Component field, so the record has no `reading_fields` and the run has one reading: the per-reading signs of C-12, C-14, C-36 and C-45 cannot be produced or checked. A reading that sets an assumption (or a fact such as `exception(en_14, C)` for the compliant maker) needs a parser-safe form like `reading_fields`. Rows: C-12, C-13, C-14, C-36, C-45.
9. **`price_paid` on the bound provider means two things.** `mc_cost_stays` puts `price_paid increase` on the bound makers (their cost per unit); the example's `makers.ag` price in C-46 is the price they charge. The row matches by name only, and a reader cannot tell the buyer's price from the provider's cost. Rows: C-46, C-9.
10. **Third-party chains are not carried to the repairers' labour and the dealers.** Technicians (C-33, C-34, C-35), dealers' parts price (C-31) and dealers' tax share (C-11) are separate exchanges that follow from RS-16's mirror; they depend on pattern 4. Rows: C-11, C-31, C-33, C-34, C-35.
