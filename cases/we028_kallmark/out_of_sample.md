# Out-of-sample run of the quota rules on WE-028 (Kallmark Ridge Cod Fishery Act)

Rules as they were at commit a0e7be0 (`licensing.lp`: EN-6 with its Unless clause, written from the catalog text alone; EN-12 and EN-13 not encoded). Handbook catalog 0.8. Nothing under `praxeo/` was changed. Record: `record.json`, three components: K1 `quota` (bound `vessel_owners.history`, buyer `buyers.regional`, right holder `share_recipients`, `transferable`, `wider_market`, `general_budget`, `announcement_window`, `renewable`; the enforcement provisions K4 are folded into K1 as enforcer, general budget and penalties), K2 `rights_allocation` and K3 `term_prohibition` (the crew settlement rule). K2 and K3 have no rules, so they produce no consequences and no questions. Unclear provision U1 is recorded with its two readings and no `reading_fields`: no Component field expresses "leases are covered too". Answers: `answers.json`, 7 questions, every one with a matching WE-028 assumption (A-1, A-2, A-11, A-15, A-3, A-28, A-22). Run: `python3 -m praxeo cases/we028_kallmark --out cases/we028_kallmark/sample_run`; verifier and citation problems are empty. Key: (actor class, variable, sign, window). The table's "(2026–2027)" cells are the announcement window; the engine signs none. The table's C-3 actor "all vessels fishing ridge cod" is matched to the record's right-holder role `share_recipients`.

Summary: the table has 54 rows (C-1 to C-55 without the removed C-15). The engine reports 13 consequences (14 keys; the OC-1 payer group is one consequence with two actors). Rows produced by key: 8 of 54 (C-1, C-2, C-3, C-14, C-17, C-32, C-33, C-49); of these C-1 and C-17 for only some of the classes the row names. Rows not produced: 46. Engine rows classified WRONG: 0; 4 are not in the table (3 defensible in form but attached to the wrong buyers, 1 a CR-8b mirror).

## Engine rows (reported)

| Engine row | Class | Why |
|---|---|---|
| vessel_owners.history quantity_traded decrease | in table | C-1 |
| buyers.regional quantity_traded decrease | in table | C-1 (`buyers.fresh_domestic` has no role) |
| share_recipients asset_value increase | in table | C-2 (SB-4 with `expected_to_last`, A-3). The table says "from the announcement"; the engine row has no window |
| share_recipients right_lease_price increase | in table | C-3 (EN-6 Unless, CR-6). The table names all vessels fishing; the engine puts it on the right holders |
| vessel_owners.history informal_activity increase | in table | C-14 (RS-3, A-11) |
| share_recipients lobbying_effort increase | in table | C-17 (RS-7, A-15), for the recipients only; processors and crew have no role |
| officials.enforcement enforcement_cost increase | in table | C-32 (OC-3). Tier B here, Tier A in the table (the engine gates it on binding and enforced) |
| taxpayers, recipients.other_spending resources_available_other_uses at_least_one_decrease | in table | C-33 (OC-3 with OC-1, A-22) |
| buyers.regional price_paid increase | in table | C-49 (EN-6 Unless with `price_effect_material`, A-28) |
| buyers.regional resources_available_other_uses decrease | defensible | CR-8b mirror of C-49; the table lists the price only |
| buyers.regional search_cost increase | defensible, misattributed | RS-3 with EN-3 for the unrecorded landings: buyers of off-record fish search more. The unrecorded fish is sold at home; the export buyers are not those buyers. The table records the sellers' side only (C-14) |
| buyers.regional disputes_settled_outside_courts increase | defensible, misattributed | RS-10 for the same trade |
| buyers.regional quality_information decrease | defensible, misattributed | EN-3 for the same trade; not in the table |

No row contradicts the example. The held-back result is as designed: the holders' `net_price_received` is not signed under `wider_market` (EN-6 Unless), the lease price is.

## Table rows

| Row | Produced? | Reason |
|---|---|---|
| C-1 quantity_traded decrease (ridge cod) | yes (part) | owners and regional buyers; no `buyers.fresh_domestic` role |
| C-2 share_recipients asset_value increase | yes | |
| C-3 right_lease_price increase | yes | holders for "all vessels" |
| C-4, C-5, C-6 race for history: landings, investment, entry (2026–2027) | no | missing rule: EN-12 / CR-10a; `rights_allocation` has no rules; entrant role absent |
| C-7 entrants entry_rate decrease (2028 on) | no | missing rule and question: EN-6 signs entry only for `seller_cap`; no A-27 question |
| C-8 vessels with history asset_value increase | no | missing rule and role: CR-7c claims before creation |
| C-9, C-10, C-40, C-52 consolidation | no | missing rule: EN-13 (and roles for high-cost and low-cost operators) |
| C-11 holders.non_fishing units_held_vacant | no | missing rule and role: the condition for holding the right (CR-1, CR-4) |
| C-12, C-13 high-grading and discards | no | missing rule: physical-unit quota on heterogeneous output |
| C-14 informal_activity increase | yes | |
| C-16 processors reclassification | no | missing rule and role (RS-5, A-14) |
| C-17 lobbying_effort increase | yes (part) | recipients only |
| C-18, C-19 crew employment, hours | no | missing record fact and rule: CR-9 for labor; `related` is read for taxes and subsidies only; C-19 also EN-12 |
| C-20 other-species fishers quantity_supplied | no | missing rule: RS-6/CR-7a; no substitute-seller role for quotas |
| C-21 fresh buyers price_paid increase | no | missing record fact: one buyer role per quota (the record names the regional buyers); the home part's own price is not a second row |
| C-22 ex-vessel net_price_received increase | no | missing rule: EN-6 Unless suppresses the holders' price and nothing signs the processors' competition for fish |
| C-23, C-24, C-25 processors, plant workers | no | missing record fact and rule: CR-9 for the buyers of the capped good |
| C-26, C-37 ports | no | missing rule and roles (CR-9, CR-7a) |
| C-27, C-28 complements | no | missing record fact (section 1 does not name the suppliers) and rule: RS-12 for quotas; C-27 also EN-12 |
| C-29 vessels without shares ambiguous | no | missing rule: CR-12b over RS-13/CR-7c against CR-1/CR-4 |
| C-30, C-51 crew pay, share terms | no | K3 has no rules (CR-5c); CR-12b |
| C-31 compliance_cost increase | no | missing rule: OC-2/CR-8c for quotas (EN-1's compliance cost needs `some_qualify`) |
| C-32 enforcement_cost increase | yes | |
| C-33 payer group at_least_one_decrease | yes | |
| C-34, C-35 sellers and later buyers of shares | no | missing rule: OC-7/CR-8b for trade in the rights (A-23); no question or buyer role |
| C-36 substitutes' price ambiguous | no | missing rule: RS-16, RS-13 |
| C-38 plants asset_value decrease | no | missing rule and role: CR-7c for the plants |
| C-39 racers' means decrease | no | missing rule: CR-8c / CR-7c Unless for the race (EN-12) |
| C-41 large owners lobbying (8% limit) | no | missing record fact and role: the holding limit |
| C-42 acquisitions as leases, per reading | no | case-specific provision: U1 on K3; no rule, and no Component field for a reading to set |
| C-43 enforcer non_tax_receipts | no | missing rule: OC-3 with CR-8b/CR-8e (fees A-23; fines A-2 with A-10 or A-11) |
| C-44 detected violators resources decrease | no | missing rule: CR-8e; the evasion question is about trade not caught |
| C-45, C-47, C-48 race-window effects on fresh price, saithe/ling supply, plants | no | missing rule: EN-12 with CR-9 |
| C-46 fresh buyers quantity_substitute increase | no | missing rule: RS-1/RS-16 under a quota |
| C-49 buyers.regional price_paid increase | yes | |
| C-50 sellers.foreign quantity_traded increase | no | missing rule: RS-1 with a supply premise (A-29) under a quota; no foreign-seller role |
| C-53, C-54 vessel sales in the window | no | missing rule and role: CR-8b/OC-7 with CR-7c |
| C-55 monitors employment increase | no | missing record fact and rule: monitors have no role; CR-8b/CR-9 |

## General gaps

Ranked by the number of table rows each would add or fix (a row may need two gaps; it is counted under its main one).

1. **EN-12, allocation by history (CR-10a with CR-4, CR-7a, CR-8c, RS-8 for the window).** The handbook states the pattern in "Gaps found" (c)1: a valuable right allocated in proportion to an activity measured over a base period that runs after the announcement raises the activity, the investment in it and entry into it in the window, lowers them afterwards, and uses up part of the right's value. It would add C-4, C-5, C-6, C-39, and with CR-9 C-19, C-45, C-47, C-48 (up to 8 rows), and with CR-7c C-8, C-53, C-54 (3 more). It needs an announcement-window consequence for quotas (the record's `announcement_window` is set but nothing reads it for EN-6), a base-period question (A-4) and a `rights_allocation` rule.
2. **CR-9 for a capped good: the buyers of the capped good, its complements and labor.** A binding cap lowers the derived demand for the suppliers of what the capped sellers use and the processors who buy the good (CR-9, RS-12, RS-6). The record's `related` is read for taxes and subsidies only. Reading it for quotas, plus a `processors`-style input-buyer role, would add C-23, C-24, C-25, C-28, and with a labor entry C-18, C-26, C-37, and C-22 with CR-7b (up to 8 rows).
3. **EN-13, consolidation under tradable rights (CR-4, CR-5, CR-7a, CR-10b).** If rights are tradable and holders' costs differ, rights move to the lowest-cost users: `number_of_sellers` falls, catch per remaining user rises, the capital stock falls over time, equipment is sold elsewhere. Gap (c)4 states it. It would add C-9, C-10, C-40, C-52 and the supply side of C-20 and C-26, with the roles `operators.high_cost` and `operators.low_cost` (4 to 6 rows).
4. **The costs and receipts of a cap: OC-2 and CR-8b, CR-8e for quotas.** EN-6 signs the enforcement cost and the payer group, but not the owners' compliance cost (register, fees, monitor fee: C-31), the enforcer's receipts from fees and fines (C-43), the detected violators' loss (C-44), the monitors' employment (C-55), or the two sides of a sale of rights (C-34, C-35). A detected-evasion question next to `evasion` would serve C-43 and C-44 (up to 6 rows).
5. **RS-1 substitution under a quota.** The substitute question exists for licensing (`buyer_substitutes`) and, as `domestic_substitutes`, for import quotas. A cap on a good with close substitutes sold elsewhere (EN-6 Unless) should let buyers turn to them and foreign sellers sell more, given a supply premise. It would add C-46, C-50, and C-36 with RS-16 (2 to 3 rows).
6. **Two buyer roles under EN-6 Unless.** When a good is priced in a wider market and also sold at home, the record has one `buyer_actor`: the engine put the price rise on the regional buyers (C-49), not the fresh domestic buyers (C-21), and attached the evasion consequences (search cost, disputes, quality information) to buyers who do not buy the unrecorded fish. A second buyer role for the home part would add C-21, fix the three misattributed rows and complete C-1 (1 row plus 4 corrections).
7. **Physical-unit quota on heterogeneous output (high-grading).** Gap (c)3: C-12 and C-13, with `quality_per_unit` of the units counted and `discards` where discarding is banned (2 rows).
8. **Narrower items.** The condition for holding a right (C-11, CR-1/CR-4), the holding limit (C-41), claims before creation (CR-7c: C-8, C-38), and the crew settlement term (K3: C-30, C-42, C-51, which also needs a Component field that `reading_fields` can set for a rule such as "leases are covered too").

Not a gap: C-2's "from the announcement" is the capitalization window of SB-4, which the engine signs without a window (the key matches); C-32's Tier A against the engine's Tier B is a difference in the gate, not in the sign.
