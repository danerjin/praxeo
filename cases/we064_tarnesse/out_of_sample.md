# Out-of-sample run of the quota rules (EN-6, EN-12, EN-13) on WE-064 (Tarnesse 2.9 GHz Award Regulations)

Rules as they stood at commit a0b2aea (handbook catalog 1.4 in the rule files). Nothing under `praxeo/` was changed. EN-6 was written from the catalog text, EN-12 and EN-13 from WE-028 only. WE-064 is a different kind of policy: a right the state creates and sells at auction, with a build-out term, a cap on holdings per bidder, and receipts into the budget that also pays the administration.

Record (`record.json`): K1 `rights_allocation` (the auction), K2 `mandated_contract_term` (build-out to 90% by 2032), K3 `quota` (at most two blocks per bidder and affiliates, with the K5 funding as `general_budget`). K4 (receipts into the Consolidated Fund) has no instrument in the ontology (section 2.3), so it is a source sentence of K1 only. The unclear provision U1 (resale before the deadline) is a `reading_fields` pair on `transferable` of K1 and K3. Answers: 8 questions, all on K3 (K1 and K2 have no instrument rules, so `record_questions` asks nothing of them); 4 probabilities from the assumption table (A-17, A-5, A-13, A-10), 4 judged from the text.

Summary: the table has 44 rows (C-1 to C-44). The engine reports 12 consequences (14 keys: the budget-payer group gives 3). Rows produced: 1 of 44 (C-37, the TCA's enforcement cost). Rows not produced: 43. Engine rows classified WRONG: 5 consequences (7 keys). `verifier_problems` and `citation_problems` are empty.

Two things went right. EN-12 (allocation by history) did not fire: the record has `allocation_by_history` false, no windfall or race rows appear, and the auction was not forced into the history pattern. EN-13 (consolidation) is not reported, because `trade_cheap` (consent of the Authority needed, barred before 2032 under U1-b) is judged at 0.4, below the cut-off. Had it been reported, it would have added wrong rows (see gap 5).

## Engine rows (reported)

| Engine row | Class | Why |
|---|---|---|
| officials.enforcement enforcement_cost increase | in table | C-37 (the table has Tier A; the engine, B, gated on binding and enforced) |
| bidders price_paid increase | **WRONG** | EN-6 raises the price buyers pay under a cap. The cap here is per holder and the six blocks are sold either way; A-17 has the cap holding the clearing price down at the third-highest bidder's value |
| bidders quantity_traded decrease | **WRONG** | EN-6 cuts the quantity traded. All six blocks sell (A-1); only the split among bidders changes (C-8, C-9) |
| bidders resources_available_other_uses decrease | **WRONG** | CR-8b on the higher price above; the example's payment loss is the licensees' (C-36), and no higher price arises |
| licensees asset_value U1-a: increase; U1-b: no_change | **WRONG** (the U1-b cell) | The sign under U1-a is C-2's, but it comes from the cap (SB-4 on a capped right), not from the sale of a created right (CR-7c). Under U1-b the engine derives nothing (SB-4 needs `transferable`); C-2 has an increase under both readings (CR-7, assets without a market price). The row does not match C-2 by key, so C-2 counts as not produced |
| taxpayers, recipients.other_spending, taxpayers.future resources_available_other_uses at_least_one_decrease | **WRONG** | OC-3 with OC-1 puts the TCA's added costs on the payers (true, and C-37 follows), but the auction payments into the Consolidated Fund (K4) are not modeled, and C-35 and C-38 sign the group and the net receipts an increase |
| licensees net_price_received increase | defensible (sign), wrong variable | EN-6's holders' gain. The winners do gain (C-2, A-17), through a lower price paid, not a higher price received. Not in the table |
| licensees lobbying_effort increase | defensible | RS-7 for the rights' holders; C-15 has the wider role "lobbying groups" (operators, entrants, town councils) |
| bidders informal_activity increase | defensible | RS-3 with A-5 (stakes below the affiliate line); C-8 records the same behavior as `reclassification` |
| bidders search_cost increase; quality_information decrease; disputes_settled_outside_courts increase | defensible but off-pattern | RS-10 chains for the buyers of unrecorded trade. The evasion here is control through stakes, not unrecorded trade, so these three do not fit; not in the table |

## Table rows

| Row | Produced | Reason category |
|---|---|---|
| C-1 treasury non_tax_receipts | no | missing rule and instrument: nothing for `rights_allocation` (CR-5c, CR-8b); K4 has no instrument |
| C-2 licensees asset_value | no | sign cell differs (per reading; see above) |
| C-3 licensees investment_target | no | missing rule: PC-17 (`mandated_contract_term`), CR-1/CR-4 |
| C-4 mobile_customers.urban (group) | no | missing rule and role (CR-9, LW-10) |
| C-5 customers.towns quality_per_unit | no | missing rule: PC-17 |
| C-6 bidders applications | no | missing rule: CR-4 for a created right |
| C-7 bidders compliance_cost | no | missing rule: OC-2/CR-8c (EN-1 only for a licensing_requirement) |
| C-8 bidders, licensees reclassification | no | missing rule: RS-17 1.1 |
| C-9 licensees term_prevalence | no | missing rule: RS-17, CR-5 (pooling); no question for A-6 |
| C-10 licensees investment_target decrease | no | missing rule and question (A-7) |
| C-11 licensees legal_breach | no | missing rule: RS-3/RS-5 on a mandated term; no A-9 question |
| C-12 licensees quantity_traded (transfers) | no | EN-13 not reported and has no transfer-volume effect |
| C-13 licensees reclassification (U1) | no | missing rule: RS-5; no A-11 question |
| C-14 bidders.financial applications | no | missing rule and role (A-12) |
| C-15 lobbying groups lobbying_effort | no | role: the engine signs the holders |
| C-16 entrants number_of_sellers | no | missing rule: entry by the winner of a created right |
| C-17 licensees number_of_sellers increase | no | missing rule: EN-13 1.1 clause (no users without the policy) not encoded |
| C-18 entrants quantity_supplied | no | missing rule (A-14, A-18) |
| C-19 mobile_customers.urban quality_adjusted_price | no | missing rule: RS-13/CR-12 |
| C-20, C-21 owners.incumbents asset_value | no | missing rule and role: RS-13, CR-7c |
| C-22, C-23, C-24 Pellow, copper owners | no | missing rule and role: RS-16 (substitute sellers) |
| C-25, C-26, C-27 tower_owners | no | missing rule: CR-9/CR-7c for inputs to the build-out; EN-13's supplier effect has the opposite sign and is not reported |
| C-28, C-29 riggers | no | missing rule and role: CR-9, LW-10 |
| C-30, C-31, C-43 other_projects | no | missing rule and role: CR-8a, RS-13 |
| C-32, C-33, C-44 equipment, foreign buyers | no | missing rule and role: CR-9, CR-6 (small effects signed) |
| C-34 other_borrowers interest_rate | no | missing rule: OC-8, CR-8a |
| C-35 taxpayers group at_least_one_increase | no | sign differs (the engine's group is a decrease; see above) |
| C-36 licensees resources_available_other_uses | no | role: CR-8b is on the bidders |
| C-37 officials.enforcement enforcement_cost | **yes** | OC-3 |
| C-38 treasury net receipts | no | missing rule and instrument |
| C-39 licensees compliance_cost | no | missing rule: OC-2/CR-8c on a mandated term |
| C-40 bidders investment_target (window) | no | missing rule: CR-10a before an auction (EN-12's race is for history) |
| C-41 licensees resources_available_other_uses (mandated sites) | no | missing rule: PC-17 with OC-1 |
| C-42 riggers wage_rate (2033 on) | no | missing rule and role: CR-10b |

Reason categories, by rows: missing rule for a created right sold at auction or a mandated term (C-1 to C-3, C-5, C-6, C-11, C-38, C-39, C-41: 10); missing rule for responses of input suppliers and other markets (C-4, C-19, C-25 to C-34, C-42 to C-44: 17); missing role (C-14, C-15, C-20 to C-24, C-36: 9 rows partly or wholly); sign or cell mismatch (C-2, C-35); EN-13 not applicable or unreported (C-12, C-17); RS-17 (C-8, C-9).

## General gaps

Ranked by the rows each would add or fix. These are patterns, not WE-064 rules.

1. **A right created by the policy and sold (`rights_allocation` by auction): CR-5c, CR-7 (1.1, a right sold at creation), CR-8b, SB-4 (1.1), CR-10c.** The instrument has no rules or questions at all, so the whole of K1 is silent. A rule that fires on the allocation by auction (not by history) would sign the receipts (C-1), the winners' value above the price (C-2, under both readings of U1, since CR-7 0.9 covers assets without a market price), the winners' loss of money (C-36) and the bidders' and entrants' applications (C-6). Adds up to 4 rows (C-1, C-2, C-6, C-36) and fixes the wrong licensees `asset_value` U1-b cell.
2. **Receipts into the budget that also pays the administration: OC-1, CR-8, CR-8b/CR-8d.** There is no instrument for receipts (`revenue_use` is not in section 2.3), so OC-3's group "the payers lose" is signed alone, and is **WRONG** against C-35 and C-38. A general pattern: where the same budget receives a payment and funds the administration, sign the net receipts (C-38) and the payers' group by the larger of the two chains, or do not sign the group from the cost alone (OC-3 with OC-1 in the handbook say the cost falls on the payers only where nothing is paid in). Fixes the 3-key WRONG group and adds C-35, C-38 (2 rows).
3. **A cap per holder (a ceiling on holdings per bidder): RS-17 1.1 and CR-1.** EN-6 treats every `quota` as a cap on the total traded. A per-holder cap with a fixed supply (six blocks sold anyway) cuts nobody's market quantity, does not raise the price (A-17), and works by splitting and by stakes below the line (C-8) and by pooling (C-9). A `holder_cap` flag on the quota (or a new instrument) would stop the three WRONG bidders rows (`price_paid`, `quantity_traded`, `resources_available_other_uses`) and sign `reclassification` (C-8) and `term_prevalence` (C-9) with questions for A-5 and A-6. Fixes 3 wrong rows, adds 2.
4. **A mandated term attached to a right the state creates: PC-17 1.1 with CR-3 1.1 and CR-12 (baseline of patterns).** `mandated_contract_term` has no rules. The example's chain is: the build-out is a burden on an option that exists only under the policy (no loss against the counterfactual), licensees build (C-3), service reaches towns (C-5), money is used (C-41), breach (C-11), proof costs (C-39). Adds up to 5 rows (C-3, C-5, C-11, C-39, C-41).
5. **EN-13's 1.1 clause for a resource with no users without the policy.** If `trade_cheap` were reported, EN-13 would sign the bidders `number_of_sellers` and `capital_stock_target` as `decrease` (it already appears as the U1-a cell of an unreported ambiguous row) and the tower owners `quantity_traded` as `decrease`, against C-17 (users rise from none) and C-25 to C-29 (the build-out raises the demand for sites and riggers). The clause (compare with the users the resource has without the policy; with none, consolidation cannot reduce them) must be encoded before EN-13 is used on a created resource; it would also add C-17 (1 row) and prevent 2 or more wrong rows.
6. **Induced demand for inputs of the new activity: CR-9, CR-6, CR-12b/CR-12e.** The build-out raises the demand for sites, riggers and equipment, and takes them from other projects (C-25 to C-34, C-42 to C-44, 15 rows by far the largest block). The record can name `input_supplier_actor` but only EN-13 reads it, with the opposite effect. A rule "a policy that creates a new use of a scarce input raises its price and quantity (CR-9), with the short-run limit when supply is slow (A-20, A-22), and lowers the use by others (CR-8a)" with a `related` input list for rights and mandated terms would add up to about 12 rows, each needing a question for the slow-supply premises.
7. **Substitute sellers and owners of existing assets: RS-13, RS-16, CR-7c.** The entry of a new network lowers the price, and the value of the incumbent licenses and of the copper network (C-19 to C-24, 6 rows). The quota record has no substitute-seller role; the subsidy rules have one (`substitute_seller_actor`).
8. **Readings with sign cells (U1).** The per-reading sign works (`asset_value`), but a `reading_fields` pair on `transferable` leaves most U1 rows (C-12 to C-14) out of reach: they concern transfer volume, reclassification by company sales and resale-only bidders. A pattern RS-5 (reclassification when a transfer is barred) would add C-13 and C-14.

Smaller: a question for the cap's own enforcement (the record's `enforced` is the engine's gate on every K3 row, so the answer to it, 0.85, decides the whole run); and an instrument or flag for "receipts" so that K4 can be recorded as a component.
