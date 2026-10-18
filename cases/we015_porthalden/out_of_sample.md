# Out-of-sample run of the quota rules on WE-015 (Port Halden Taxi Fleet Stabilization Ordinance)

Rules as they stood at commit a0e7be0 (EN-6 written from the catalog text alone, no example used). Record: `record.json`, one `quota` component K1 (bound `drivers.taxi`, buyer `riders`, right holder `medallion_owners.initial`, `transferable`, `seller_cap`, `general_budget`, `announcement_window`, `definition_line`). The meter rate (R1) is in `context` only, as the task says. K2 (private-hire exemption) is an exemption, with no instrument of its own: it is a source sentence of K1 and the `definition_line` flag. K3 (enforcement) is K1's `enforcer_actor` and `general_budget`. U1 is recorded with its two readings and no `reading_fields` (neither reading changes a component's fields; it matters only in the later stage). Answers: `answers.json`, six questions, five from the assumption table (A-1, A-7, A-9, A-3, A-16) and `enforced` judged from the text. Run: `python3 -m praxeo cases/we015_porthalden --out cases/we015_porthalden/sample_run`; verifier and citation problems empty. Key: (actor class, variable, sign, window). Test: `tests/test_oos_we015.py`.

Summary: the table has 34 rows (C-1 to C-34). The engine reports 15 consequences (17 keys once the payer group is split into its three members). Rows produced by key: 5 (C-1, C-2, C-12, C-23 for riders only, C-34). Rows not produced: 29. Engine keys not in the table: 12, of which defensible 9 and **WRONG 3**.

## Engine rows (reported)

| Engine row | Class | Why |
|---|---|---|
| drivers.taxi number_of_sellers decrease | in table | C-1 |
| medallion_owners.initial asset_value increase | in table | C-2 (EN-6 with SB-4 and `expected_to_last`) |
| medallion_owners.initial lobbying_effort increase | in table | C-12 |
| riders quantity_traded decrease | in table | C-23 (the riders' half) |
| officials.enforcement enforcement_cost increase | in table | C-34 |
| drivers.taxi entry_rate decrease | defensible | EN-6 with `seller_cap`; the table has the would-be entrants (C-4), for whom a quota record has no role |
| drivers.taxi quantity_traded decrease | defensible | OC-4 names both sides; C-23 names the would-be drivers |
| drivers.taxi informal_activity increase | defensible, with a role gap | RS-3 attaches it to the bound role; the example has the unlicensed drivers (C-10), a class outside `drivers.taxi` as section 3 defines it |
| riders search_cost increase, quality_information decrease, disputes_settled_outside_courts increase | defensible | RS-10 for the unlicensed trade; the example gives all three to `riders.informal` (C-16, C-26, C-27), a subclass of the buyers |
| taxpayers, recipients.other_spending, taxpayers.future resources_available_other_uses at_least_one_decrease | defensible | OC-3 with OC-1 and A-16; C-25 names taxpayers alone as a decrease |
| **medallion_owners.initial net_price_received increase** | **WRONG** | EN-6 raises the holders' price received; the fare is the meter rate, the same as without the ordinance. The holders gain by more trips and lease income (C-13) |
| **riders price_paid increase** | **WRONG** | EN-6 presupposes a free price. The example is explicit: "the cap does not raise the fare, because the meter rate is fixed" (section 5) and the meter fare is the same as in the counterfactual (C-28) |
| **riders resources_available_other_uses decrease** | **WRONG** | CR-8b on the price rise above; with no higher money price nothing is lost on that account |

All three WRONG rows have one cause: an existing price rule that holds the price at the same level in the counterfactual.

## Table rows

| Row | Produced? | Reason |
|---|---|---|
| C-1 number_of_sellers decrease | yes | |
| C-2 asset_value increase | yes | |
| C-3 entry_rate increase (announcement window) | no | missing rule: RS-8 for a quota or license cap; the record has `announcement_window` and no EN rule reads it |
| C-4 prospective entry_rate decrease | no | missing role (would-be entrants); the engine signs the bound role |
| C-5 excess_demand increase | no | missing record fact: R1 has no field (`existing_rules`, GAP-015-3), so PC-1 does not run |
| C-6 wait_time increase | no | same (PC-1, PC-2; A-18 has no question) |
| C-7 outlying riders allocation_by_non_price_criteria | no | same, and no role for outlying riders |
| C-8 quality_per_unit decrease | no | same (PC-4, RS-2); TS-1 not encoded for a cap |
| C-9 side_payments increase | no | same (PC-6, RS-3) |
| C-10 unlicensed informal_activity increase | no | missing role; engine key is on `drivers.taxi` |
| C-11 private_hire reclassification | no | missing rule and role: RS-5 for the exempt segment; `definition_line` unread by EN rules |
| C-12 lobbying_effort increase | yes | |
| C-13 holders' earnings increase | no | missing rule: EN-2 signs net_price_received only (and wrongly here); the earnings form at a fixed fare is not encoded |
| C-14 quantity_substitute increase | no | missing rule: RS-1 premise exists for licensing, not quota; no substitute-seller role |
| C-15 private-hire price_substitute ambiguous | no | missing rule and role: PC-8 Unless with CR-4b |
| C-16, C-26, C-27 riders.informal search_cost, quality_information, disputes | no | missing role: the engine signs the buyer class (exceptions) |
| C-17 lenders quantity_traded | no | missing role and rule |
| C-18 lessees earnings ambiguous | no | missing role and rule |
| C-19 to C-22 app-service stage | no | later stage; U1's readings carry no engine facts, no app_services role, no later-buyer role; C-21 also lacks a holders role covering later buyers |
| C-23 quantity_traded decrease | yes (part) | riders; no would-be-entrant role |
| C-24 prospective earnings decrease | no | missing role; EN-3 is licensing-only |
| C-25 taxpayers resources decrease | no (by key) | sign form: the OC-1 group is `at_least_one_decrease`, with taxpayers as member; the mechanism is the same |
| C-28 full_cost_per_unit increase | no | missing record fact (R1) |
| C-29 private_hire entry_rate increase | no | missing rule and role (PC-8 Unless, CR-4b) |
| C-30 taxi employment ambiguous | no | missing rule: CR-12b over EN-6 and CR-7a |
| C-31 city tax_revenue increase | no | missing record fact and rule: transfer and permit fees |
| C-32 lobbying resources decrease | no | missing rule: CR-8c for lobbying |
| C-33 wait_time decrease (first year) | no | missing rule: RS-8 with CR-9 |
| C-34 enforcement_cost increase | yes | |

## General gaps

Ranked by table rows added or engine rows fixed.

1. **Existing rules in the record (GAP-015-3, catalog 0.3 `existing_rules`; PC-1 to PC-6 with the section 2 classification of R1).** The schema has no field for a rule that is in force in the counterfactual too. Adding it, with the ceiling rules run on it when a new component makes it bind, would add C-5, C-6, C-7, C-8, C-9 and C-28 (six rows) and remove all three WRONG rows by an EN-6 Unless: where an existing rule fixes the price at its counterfactual level, the quota's price rise, the holders' `net_price_received` rise and CR-8b's loss to other uses are not signed. It would also supply the fixed-fare form of C-13.
2. **Exemption from a cap or license (RS-5, PC-8 and its Unless, CR-4b).** `definition_line` is set but only tax and tariff rules read it. Reading it for quotas and licensing, with a role for the exempt segment, adds C-11, C-15 and C-29, and the substitute-quantity C-14 (RS-1 for a quota): four rows.
3. **Would-be entrants and the unlicensed as roles of a quota or license (EN-3, OC-4, RS-3).** An `excluded_actor` read by the EN rules (entry_rate, earnings, quantity_traded) and an unlicensed-sellers role for RS-3's informal activity would add C-4, C-10, C-16, C-24, C-26, C-27 (six rows, and C-23's second half), and turn three defensible rows into table rows. EN-3's earnings premise (A-17) has no question in quotas.
4. **RS-8 on a cap announced before it takes effect.** The window flag is accepted and ignored for quotas. Signing licenses taken out in the window and the first-year effect (C-3, C-33) adds two rows; C-33 also needs A-14.
5. **Transferable rights: secondary roles (SB-4, CR-7a, EN-2, CR-1/CR-8b).** Later buyers, lessees, lenders and the transfer fee (C-17, C-18, C-21, C-22, C-31, plus the earnings chain in C-30) need role fields for later holders and lessees and a fee flag: up to six rows.
6. **Small encodings.** CR-8c for the resources spent lobbying (C-32), the single-class form of OC-3 when the record names the payer (C-25), and per-reading facts for a later-stage unclear provision (C-19, C-20; parsers cannot write `reading_facts`, and U1 changes no Component field).
