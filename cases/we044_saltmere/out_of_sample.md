# Out-of-sample run of the prohibition rules on WE-044 (Saltmere Housing Preservation Ordinance)

Rules as they stood at commit 9c6d2e9 (`praxeo/rules/prohibition.lp`, written from WE-017 only). Nothing under `praxeo/` was changed. Record: `record.json`, three components: k1 `prohibition` (K1 with K4's enforcement: bound `hosts.non_primary`, buyers `guests.whole_unit`, informal sellers `hosts.in_breach`, informal buyers `guests.off_platform`, mobile buyers `guests.whole_unit`, neighbor sellers `neighboring_jurisdictions`, line-adjacent sellers `hosts.mid_term`, `definition_line`, `taxed_before`, `announcement_window`, `general_budget`), k2 `disclosure_mandate` (K2, the platform duty: no rules), k3 `licensing_requirement` (K3, the registry for the exempt use: the licensing rules fire). U1 is in `unclear` with no `reading_fields`: neither reading changes a Component field. Answers: `answers.json`, 18 questions, from WE-044's assumption table wherever a row matches (A-2, A-3, A-4, A-5 inverted, A-8, A-10, A-14, A-15, A-19, A-20, A-22, A-38) and judged from the text for k3.binding, k3.some_qualify and k3.tests_valued_quality. Run: `python3 -m praxeo cases/we044_saltmere --out cases/we044_saltmere/sample_run`; verifier and citation problems are empty. Test: `tests/test_oos_we044.py`. Key: (actor class, variable, sign, window).

Summary: the table has 64 rows (C-1 to C-64). The engine reports 35 consequences (37 keys; the payer group gives three). Rows produced by key: 13 of 64; of these 3 for only some of the classes or by key rather than mechanism (C-2 without platforms, C-15 without platforms, hotels and associations, C-17 without two-unit hosts, C-30 by the ban itself and not through A-11). Rows not produced: 51. Engine keys: 14 in the table, 19 defensible, **4 WRONG**.

## Engine rows (reported)

| Engine row | Class | Why |
|---|---|---|
| guests.off_platform search_cost increase | in table | C-11 |
| guests.off_platform quality_information decrease | in table | C-12 |
| guests.off_platform disputes_settled_outside_courts increase | in table | C-13 |
| hosts.in_breach informal_activity increase | in table | C-10 |
| guests.whole_unit cross_border_purchases increase | in table | C-26 |
| hosts.mid_term reclassification increase | in table | C-8 |
| hosts.non_primary quantity_traded decrease; guests.whole_unit quantity_traded decrease | in table | C-2 (no platforms), C-20; guests also C-30 by key |
| hosts.non_primary, hosts.primary lobbying_effort increase | in table | C-15 (hosts only) |
| hosts.primary compliance_cost increase | in table | C-17 (by K3's licensing chain EN-1, CR-8; no two-unit hosts) |
| officials.enforcement enforcement_cost increase | in table | C-45 (OC-3 for the Registry Unit; also fires for Code Enforcement, whose C-47 is ambiguous) |
| taxpayers, recipients.other_spending resources_available_other_uses at_least_one_decrease | in table | C-46 |
| taxpayers.future resources_available_other_uses (group member) | defensible | OC-1 default payer group has a third member |
| guests.off_platform quality_variability increase | defensible | RS-10 triple |
| hosts.in_breach disputes_settled_outside_courts increase | defensible | RS-10, sellers' side of C-13 |
| hosts.in_breach reclassification increase | defensible | RS-5 on the informal sellers; C-59 has it on the unsplit class |
| hosts.non_primary number_of_sellers decrease | defensible | the head count behind C-1 |
| guests.whole_unit quantity_substitute increase | defensible | RS-1, the guests' side of C-23 and C-57 |
| guests.whole_unit quantity_demanded decrease | defensible | sign of C-30, through the wrong (risk-price) chain |
| guests.whole_unit lobbying_effort increase | defensible | RS-7; the table does not list the diffuse guests |
| guests.whole_unit search_cost increase | defensible | OC-2 of the crossing (C-62 has travel_time) |
| guests.whole_unit disputes_settled_outside_courts increase; quality_information decrease | defensible | RS-3/RS-10 on K3's unregistered lets (k3 buyers); table puts these on guests.off_platform |
| guests.whole_unit resources_available_other_uses decrease | defensible | EN-1, CR-8b on K3's fee |
| neighboring_jurisdictions quantity_traded increase | defensible | RS-4, the sellers' side of C-26 (C-27 has quantity_supplied) |
| hosts.primary entry_rate decrease; number_of_sellers decrease | defensible | C-17: the fixed fee decides whether some hosts list at all |
| hosts.primary informal_activity increase | defensible | RS-3 on K3; C-9 calls it legal_breach |
| hosts.primary quantity_traded decrease | defensible | OC-4 on K3; C-3 has it as quantity_supplied above 90 nights |
| hosts.primary net_price_received increase | defensible | sign of C-39 (hosts.lawful, no role), reached through EN-2 licence rents, not RS-16 |
| hosts.primary share_of_sellers_licensed increase | defensible | true by definition of the requirement |
| **guests.whole_unit price_paid increase** | **WRONG** | EN-7/CR-7 risk premium on the legal buyers; A-27 and C-14 say hosts do not price the risk guest by guest and the on-platform guests face none |
| **guests.whole_unit quantity_demanded increase (announcement)** | **WRONG** | RS-8 gives the (+) chain alone; C-18 and C-19 are ambiguous (A-16 leasing-season chain) |
| **hosts.primary employment decrease** | **WRONG** | EN-3 reads K3 as a licence that excludes people from an occupation; it is a fee and proof of residence on an exempt use |
| **officials.revenue tax_revenue decrease** | **WRONG** | TX-10 alone; C-49 is ambiguous (hotels regain TOT, A-8, A-9; Elsdon, A-10; against A-11) |

## Table rows

| Row | Produced? | Reason |
|---|---|---|
| C-1 | no | variable: EN-7 signs quantity_traded and number_of_sellers, not quantity_supplied |
| C-2 | yes (part) | no platforms role under a prohibition |
| C-3 | no | missing record fact: the 90-night cap (CR-1 above a threshold) has no field |
| C-4, C-5 | no | missing role (two-unit hosts); U1 does not change a Component field |
| C-6 | no | missing rule: RS-6/CR-4 next-best use (12-month lease) for a prohibition |
| C-7 | no | missing rule and role: own-use (autistic) element |
| C-8 | yes | |
| C-9 | no | missing variable: legal_breach; a cap on a lawful use is not a prohibition form |
| C-10 | yes | |
| C-11 to C-13 | yes | |
| C-14 | no | missing rule: RS-20 (complaint-only enforcement) and A-27 |
| C-15 | yes (part) | hosts only |
| C-16 | no | unsupported form: platform duty (disclosure_mandate has no rules) |
| C-17 | yes (part) | through the licensing rules on K3 |
| C-18, C-19 | no | missing rule: RS-8 (0.9) second timing chain and CR-12b; the engine has the (+) chain alone (WRONG row) |
| C-20 | yes (by key) | the ban itself |
| C-21 | no | missing role and record fact (cancelled bookings) |
| C-22 | no | missing rule, role and question: RS-16/CR-9 on the substitute market, A-9 |
| C-23 | no | missing role: one substitute_seller_actor serves RS-5's line and RS-1's hotels |
| C-24, C-25 | no | missing rule and role: CR-7c, CR-7a for hotels |
| C-26 | yes | |
| C-27 | no | variable (quantity_traded for quantity_supplied) and the durability premise A-39 |
| C-28 | no | missing rule: CR-7c for the neighbor sellers' assets |
| C-29 | no | missing role and rule: RS-13 to the neighbor's long-term market |
| C-30 | yes (by key) | through the ban, not A-11 |
| C-31, C-32 | no | missing rule: CR-9/RS-9 related markets under a prohibition (no target_qty); section 1 names no related group |
| C-33 | no | missing rule and role: OC-5 for hotel staff |
| C-34 to C-37 | no | missing rule and role: RS-13 spillover to the long-term rental market |
| C-38 | no | missing rule and role: RS-16 with Unless, RS-13 (mid-term market) |
| C-39 | no | missing role (hosts.lawful) and RS-16 |
| C-40 | no | missing rule: asset value fall tied to no_other_use (SB-4), not to a fall in yield (CR-3a, A-1) |
| C-41 | no | missing role: two-unit owners |
| C-42, C-43, C-53, C-54, C-61 | no | missing rule and role: CR-7c asset and home-price chains; proximity (Tier C) |
| C-44 | no | missing rule: CR-3a/CR-7b return on capital |
| C-45 | yes | |
| C-46 | yes | |
| C-47, C-48 | no | missing role and rule: second enforcer and complainants; OC-3 for complaint-only work, CR-12b |
| C-49 | no | missing combiner: TX-10 alone (WRONG row) |
| C-50, C-51, C-55, C-56 | no | missing rule: CR-8b fines and fees as receipts and as hosts' cost |
| C-52 | no | missing rule: CR-9/RS-9 with the combiner |
| C-57, C-58 | no | missing role and rule: RS-16 spillover to rooms in occupied homes |
| C-59 | no | role split: engine has it on hosts.mid_term and hosts.in_breach |
| C-60 | no | missing role and rule: sale as next-best use |
| C-62 | no | variable: engine has search_cost, table travel_time |
| C-63, C-64 | no | missing rule and role: RS-16 for the hotel guests and the furnished-let market |

## General gaps

Ranked by table rows added or fixed.

1. **Spillover to related markets from a prohibition (RS-16, RS-13, CR-9, RS-1 for the sellers of the substitute).** Rows C-22 to C-25, C-27 to C-29, C-33 to C-39, C-57, C-58, C-63, C-64 (about 20). RS-1 signs only the buyers' `quantity_substitute`; a prohibition removes supply, so the substitute market's sellers (hotels, rooms, the neighbor's hosts, the long-term and mid-term lets) gain demand, their price rises where supply is slow (durability question, A-9, A-35, A-39), their quantity rises, and their asset values and entry follow (CR-7a, CR-7c). Needs a second seller role, `substitute_market_seller_actor` (distinct from the RS-5 line role `substitute_seller_actor`, which here is the mid-term hosts), and the durability question.
2. **Related markets for a prohibition (CR-9, RS-9, RS-12).** `relations.lp` takes `target_qty` from taxes and subsidies only. A prohibition that stops legal trade (`pr_legal_stops`) is `target_qty(C, decrease)`; complements and inputs (cleaners, shops) then follow. Adds C-31, C-32, C-52 if the record names the groups; section 1 names none, so a parser could not fill them (C-31, C-32 also need the parser prompt to list `related` for prohibitions).
3. **Owners' next-best use after a ban (CR-1 with CR-3a, CR-4, CR-7c, SB-4).** EN-7 ties the fall in asset value and employment to `no_other_use`. The handbook signs the asset value down when the best use is removed even though alternatives exist at lower yield (A-1, A-30). Adds C-40, C-41, C-44, and with a response split (hosts converting, selling, mid-term, second-home) C-6, C-7, C-60, C-42, C-54, C-61. A general rule: a removed best use lowers the owner's return and the asset's value (CR-3a, CR-7c); the alternative uses, if any, get the quantity (RS-6).
4. **Partial prohibitions: a threshold and a registered exception (CR-1 operation 1 above a threshold, operation 3 below).** C-3, C-9, C-17 (fully), C-4, C-5, C-41 with U1. The record has no field for a cap on a lawful use, `legal_breach` has no rule, and a reading of the exception (U1) that changes who is covered cannot be written in `reading_fields` because it names no Component field. A role for the exempt class (`exempt_actor`) with its own cap would carry C-3, C-9 and the two-unit rows by reading.
5. **Complaint-only enforcement (RS-20, promoted in 0.9).** C-14 (A-27), and the expected-penalty premise behind C-9, C-10 (EN-7's evasion and enforcement_risk questions cover part). The EN-7 risk price (WRONG row) assumes the risk is priced into what the legal buyers pay; RS-20's premise (hosts screen, do not price the risk) says otherwise. The risk price should attach to the informal buyers only, and only where the seller can price guest by guest.
6. **Penalty receipts and the penalty payers (CR-8b, CR-3c).** C-50, C-51, C-55, C-56. A fine is revenue to the collecting body and a cost to those fined; no prohibition rule signs either. `convicted_actor` serves EN-10 only.
7. **Opposing timing chains in the announcement window (RS-8 0.9, CR-12b).** C-18, C-19 and the WRONG window row. RS-8 for a prohibition signs buyers stocking up; the handbook also has sellers ending or timing exits before the date (A-16), and then signs the window ambiguous. Add the seller-side chain with its question and let the combiner sign `quantity_traded` ambiguous when both fire.
8. **Combiners for taxes lost under a ban (TX-10, CR-12b).** TX-10 signs the lost tax alone (WRONG row, C-49 lost). It should wait for the substitute market's tax (hotels collect the same TOT) before signing; with spillover (gap 1) it becomes ambiguous by the combiner.
9. **Second enforcer and complainants (OC-3, OC-2).** C-47, C-48. One `enforcer_actor` per component; K1 is enforced by Code Enforcement on a fixed budget and K3 by a new unit. OC-3 should sign the fixed-budget enforcer's cost by the complaint volume, not as a plain increase.
10. **Instruments with no rules in the same ordinance.** K2 (platform duty, CR-1 operation 3, CR-8c: C-16) is a `disclosure_mandate`, and K3 as `licensing_requirement` brings EN-3 (a WRONG employment row) and EN-2 (licence rents, a defensible but mechanism-wrong price row): EN-1 to EN-3 presume a barrier to entry into an occupation, while K3 is a fixed registration cost on an exempt use. A record flag (for example `fixed_fee_only`) or CR-4's fixed-cost-per-outlet pattern should replace EN-1 to EN-3 for a registration that tests nothing.

Smaller: `officials.revenue`, `hosts.primary` and the table's `hosts.primary_over90` are matched by a short-name map in the test; a controlled-vocabulary role for hosts would remove it. The variable `quantity_supplied` for lawful sellers (C-1, C-3) is signed as `quantity_traded` and `number_of_sellers` by EN-7.

## After the rule changes (second commit)

General fixes from the out-of-sample runs on WE-018, WE-037, WE-044, WE-050 and WE-053 (`rules/prohibition.lp`): fewer legal sellers only where they cannot turn to other products (`no_other_use`); the underground trade needs the ban to be enforced; the risk price needs an underground trade; the buyers lobby only with their own premise (`buyers_organize`); buying across the boundary costs time only where it takes an extra trip (`crossing_extra_trip`); a ban on a practice of legal firms (`practice_ban`) makes evasion a legal breach, not an informal market; fees or fines paid into the budget that funds enforcement (`fees_to_budget`) leave the payers' net unsigned. The answers gained the two new questions. Rows produced: 13 of 64 (unchanged). WRONG: 4 (unchanged): the guests' risk price under complaint-only enforcement (RS-20, not encoded), the rush before the ban (C-18, C-19 ambiguous: an opposing timing chain), the registration treated as an occupational license (EN-3), and the lost tax revenue (C-49 ambiguous against the substitute market).
