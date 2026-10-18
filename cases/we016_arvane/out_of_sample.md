# Out-of-sample run of the licensing rules on WE-016 (Arvane Interior Design Practice Act)

Rules as committed in a0e7be0 (`praxeo/rules/licensing.lp`, developed on WE-003 only), nothing under `praxeo/` changed. Record: `record.json`, one `licensing_requirement` component (K1): bound `designers`, buyer `clients`, right holder `designers.grandfathered`, trainer `schools.design`, enforcer `officials.enforcement`, `general_budget`, `announcement_window`. K2 (grandfathering) enters only through the right-holder role (and the source sentence), K3 (stamped plans) and K4 (enforcement) have no component of their own: K3 is "part of K1" in the handbook and a second licensing component would double every row, so it is recorded here as a finding. The unclear provision U1 (styling) is recorded with its two readings and no `reading_fields`: neither reading changes a Component field. Answers: `answers.json`, 8 questions; 6 from the assumption table (A-1, A-2, A-3, A-9, A-10, A-13), 2 judged (`some_qualify`, `enforcement_budget_raised`). Run: `python3 -m praxeo cases/we016_arvane --out cases/we016_arvane/sample_run`; verifier and citation problems empty. Test: `tests/test_oos_we016.py`. Key: (actor class, variable, sign, window). The record has one seller role and one buyer role, so the table's `designers.recent`, `.prospective` and "designers" all match `designers`, and `clients.commercial` and `.residential` match `clients`.

Summary: the table has 36 rows (C-1 to C-36). The engine reports 19 consequences (21 keys; the OC-1 payer group is one consequence with three actor classes). Table rows produced by key: 15 of 36; of these C-10 for one of its four classes (`designers.grandfathered`, not schools, retailers, architects) and C-15 by key only (the engine's `quantity_substitute` is shared with C-14 and does not name architects). Rows not produced: 21. Engine rows classified WRONG: 1.

## Engine rows (reported)

| Engine row | Class | Why |
|---|---|---|
| designers share_of_sellers_licensed increase | in table | C-1 |
| designers number_of_sellers decrease | in table | C-2 (the table has the recent designers; the engine cannot separate them from the grandfathered, see General gaps 2) |
| designers informal_activity increase | in table | C-3 |
| designers entry_rate decrease | in table | C-5 (horizon: engine short and onward, table medium to long) |
| designers compliance_cost increase | in table | C-6 (degree route; the engine's row is for those who qualify, some_qualify) |
| designers.grandfathered net_price_received increase | in table | C-13 |
| designers.grandfathered lobbying_effort increase | in table | C-10 (one of four classes) |
| clients price_paid increase | in table | C-11, C-12 (horizon: engine short and onward, table medium to long) |
| clients quantity_substitute increase | in table | C-14 (C-15 by key only) |
| clients search_cost increase | in table | C-18 |
| clients disputes_settled_outside_courts increase | in table | C-29 |
| clients, designers quantity_traded decrease | in table | C-25 |
| officials.enforcement enforcement_cost increase | in table | C-35 |
| clients quality_information ambiguous | defensible | EN-3/RS-10 give a decrease (C-28, buyers of unlicensed designers) and EN-11 gives an increase for the licensed designers' buyers (A-13, p = 0.75); with one buyer role the combiner reports ambiguous. The table has no increase row for licensed buyers, so this is a role-granularity artefact, not a contradiction |
| clients resources_available_other_uses decrease | defensible | CR-8b, mirror of C-11 and C-12; not listed in the table |
| designers employment decrease | defensible | EN-3 with OC-4; the table has the recent designers' earnings (C-26, needs A-19). With `designers` as the whole bound class it overstates: the grandfathered keep working |
| taxpayers, recipients.other_spending, taxpayers.future resources_available_other_uses at_least_one_decrease | defensible | OC-3 with OC-1, the payer group of the general-budget share. The table signs `taxpayers` alone (C-27, Tier A) |
| **schools.design quantity_demanded increase** | **WRONG** | The table has `ambiguous` (C-7). EN-1 with CR-8c derives the up chain (those who now need the degree buy it); the down chain (degree-takers who now also face 3,500 hours and an exam turn to another career, CR-4b) is not derived. This is the misapplication of EN-1 that catalog 0.5 corrected in the handbook (Gaps found), and the engine repeats it |

A second, unkeyed disagreement: every licensing row carries horizons `short, medium, long`. The handbook's grandfathering changes the time structure (section 8): in the short run the licensed pool is the old pool, so prices (C-11, C-12) are medium to long, entry (C-5) medium to long and supply is nearly unchanged at first. The harness compares no horizons, so this is not a row, but a short-run price increase is wrong for this policy.

## Table rows

| Row | Produced? | Reason |
|---|---|---|
| C-1 designers share_of_sellers_licensed increase | yes | |
| C-2 designers.recent number_of_sellers decrease | yes | |
| C-3 designers.recent informal_activity increase | yes | |
| C-4 grandfathered compliance_cost increase | no | missing record fact / rule: OC-2 for fees and continuing education borne by holders; the engine's compliance cost is on the bound role for those who qualify |
| C-5 prospective entry_rate decrease | yes | |
| C-6 prospective (degree route) compliance_cost increase | yes | |
| C-7 schools.design quantity_demanded ambiguous | no | wrong sign (the WRONG row above): EN-1 gives an increase |
| C-8 retailers.furniture, designers.recent reclassification increase | no | missing rule: RS-5 for the exemption of retail staff (the exemption is in the text but no record field carries it for licensing) |
| C-9 clients.commercial quantity_traded increase (window) | no | missing rule: RS-8 is not encoded for licensing; `announcement_window` is set but no question for A-8 is asked |
| C-10 four classes lobbying_effort increase | yes (part) | grandfathered only; schools, retailers (keep the exemption) and architects have no role |
| C-11 clients.residential price_paid increase | yes | |
| C-12 clients.commercial price_paid increase | yes | |
| C-13 grandfathered net_price_received increase | yes | |
| C-14 clients.residential quantity_substitute increase | yes | |
| C-15 clients.commercial quantity_substitute (architects) increase | yes, by key only | the engine's row is C-14's; architects are not a role |
| C-16 retailers.furniture quantity_traded increase | no | missing rule and role: RS-5, RS-9 (complements bought in the same store) |
| C-17 showrooms.trade quantity_traded decrease | no | same |
| C-18 residential search_cost increase | yes | |
| C-19 commercial quality_per_unit increase | no | missing rule: EN-4 with DM-2 (stamped plans leave no unlicensed alternative); the quality family is not encoded for licensing |
| C-20 residential quality_per_unit ambiguous | no | missing rule: EN-4 (up and down chains, DM-2 not decisive) |
| C-21 apprentices wage_rate decrease | no | missing rule and role: EN-9 (supervised hours, A-15) |
| C-22 grandfathered job_changes decrease | no | missing rule: RS-11 in its status form (A-16) |
| C-23 prospective earnings ambiguous | no | combiner: DM-3 over C-11/C-12 against C-6/C-21 |
| C-24 grandfathered earnings increase | no | missing rule: EN-2 stops at net_price_received; CR-9 and the CR-12c separation of fees from earnings |
| C-25 clients, recent, prospective quantity_traded decrease | yes | |
| C-26 recent earnings decrease | no | missing rule: EN-3's premise A-19 (next-best work pays less), marked not encoded in `licensing.lp` |
| C-27 taxpayers resources_available_other_uses decrease | no | sign form: the engine's OC-1 group is `at_least_one_decrease` over three classes; the text says "general budget" and the handbook signs taxpayers without a premise |
| C-28 residential (unlicensed) quality_information decrease | no | role granularity: one buyer role, so EN-11's increase for the licensed designers' buyers combines it into `ambiguous` |
| C-29 residential disputes_settled_outside_courts increase | yes | |
| C-30 recent number_of_sellers (styling), by reading | no | unsupported form: U1 is about the scope of the good; it changes no Component field and U1-b needs RS-5 |
| C-31 apprentices wait_time increase | no | missing rule and role: EN-9 with CR-1 and CR-6 |
| C-32 grandfathered compliance_cost (inactive) increase | no | missing rule: RS-11 with OC-2 (A-16) |
| C-33 commercial quantity_traded decrease (first months) | no | missing rule: RS-8 with CR-10a (as C-9) |
| C-34 architects price_substitute increase | no | missing rule and role: CR-9, CR-6 for the substitute sellers' fees |
| C-35 officials.enforcement enforcement_cost increase | yes | |
| C-36 building departments enforcement_cost increase | no | missing record fact: K3 has no component, so no second enforcer role |

By primary reason (21 rows not produced): missing rule, with or without a missing role, 14 (C-8, C-9, C-16, C-17, C-19, C-20, C-21, C-22, C-24, C-26, C-31, C-32, C-33, C-34); missing record fact or role 2 (C-4, C-36); unsupported form 1 (C-30); combiner, sign form or role granularity 3 (C-23, C-27, C-28); wrong sign 1 (C-7). No row is a case-specific provision.

## General gaps

Proposals are at the level of a handbook pattern, ranked by rows added or fixed.

1. **RS-8 for licensing (C-9, C-33; two rows).** The handbook applies RS-8 to any measure with an announcement window (`02_ontology.md`, 2.5), and this one has the flag and the text ("passed ten months before it took effect"). The licensing rules should use `announcement_window`: ask A-8 (can buyers bring purchases forward) and sign the buyers' quantity in the window up and in the first months down (CR-10a). Since no question is asked now, the record flag has no effect for this instrument.
2. **Exemption in time, TS-1 with EN-1's Unless clause (fixes the horizon of C-2, C-5, C-11, C-12, C-13; adds C-4 and, with 3, C-22 and C-32).** EN-1 as encoded treats every bound seller as excluded. Where a clause licenses existing practitioners (K2), the effect on supply and price comes with the slow turnover of the grandfathered stock. A record field for the exempt (grandfathered) class, and the sellers' decrease on the non-exempt remainder only, would stop `designers.grandfathered` being counted in `designers number_of_sellers` and `employment`, and would move price and entry to medium and long. Without this, a licensing law with grandfathering gets a short-run price rise that the example says does not happen.
3. **OC-2 and RS-11 for holders (C-4, C-22, C-32; three rows).** The license fee and continuing education are compliance costs of the holders (OC-2, no assumption, Tier A in C-4), and a status that cannot be regained once lapsed locks holders in (RS-11, status form, A-16), who then pay fees while partly inactive. Today `compliance_cost` is signed only for the bound role and only through `some_qualify`.
4. **EN-1 on the qualifying input (C-7; one wrong row).** CR-4b has two opposing chains for the demand for the training: entrants who now need it (up) and those who would have taken it anyway and now face further conditions (down). The rule should sign `quantity_demanded` of the trainer `ambiguous` where the requirement adds conditions beyond the training (hours, exam, fees), `increase` only if the training is the only added condition. This removes the one WRONG row.
5. **EN-4 with DM-2, quality (C-19, C-20; two rows).** Quality received rises where the training bears on what buyers value and no close unlicensed substitute exists for the use the buyers need it for (stamped plans, A-5, A-13); it is ambiguous where there are substitutes (A-10) and the training is partly related. The questions `tests_valued_quality` and `buyer_substitutes` exist; the rule that combines them is missing.
6. **EN-9, supervised hours as an entry condition, with CR-1 and CR-6 (C-21, C-31, and C-5's timing; two rows).** Needs a role for the trainees (`apprentices`) and the scarcity premise (A-15).
7. **RS-5 and RS-9 for exemptions and complements (C-8, C-16, C-17; three rows).** An exemption that lets a close substitute provider reclassify work (retail staff giving design help) and moves purchases of complements (furniture) to the exempt channel. Needs a role for the exempt provider and a related-market field, as the subsidy and tariff rules have; `definition_line` exists but is read by tax rules only.
8. **A second enforcer and a substitute-seller role (C-34, C-36; two rows).** K3 is a requirement on permit applicants that a building department must check (OC-3), and architects, as licensed substitute sellers, are asked for more than they can supply (CR-9, CR-6). Both need record fields (enforcer list, substitute seller) and rules.
9. **EN-3's earnings premise (C-26; one row) and EN-2 with CR-9 (C-24; one row).** Both are marked in the rule file as not encoded; each needs a question (A-19 here) and the CR-12c separation of fees from earnings.
10. **Buyer subclasses (C-28, and the `quality_information` artefact).** A licensing record has one buyer role; the buyers who use unlicensed sellers (RS-3, RS-10) are a subclass of buyers, as the displaced holders are in the price-ceiling rules. Naming that subclass would give C-28 as a decrease and keep EN-11's increase for the licensed sellers' buyers apart from it.
11. **OC-3 payers where the text says only "general budget" (C-27).** The handbook signs `taxpayers` alone with no premise where the funding is the general budget; the engine asks `enforcement_budget_raised` and signs the OC-1 group. Either the group should be accepted as the same row (the table's `taxpayers` is the first member) or `taxpayers` should be signed with the named-tax rule when the text says "general budget".

## After the rule changes (second commit)

General fixes from the five out-of-sample runs on licensing and quotas (`rules/licensing.lp`): buyers of the unlicensed or unrecorded trade have their own role (`informal_buyer_actor`), so RS-3 and RS-10 fall on them, not on every buyer; trainers' demand is ambiguous where the training was already common (`training_common`, CR-4b with CR-12b); a price fixed by a rule in force without the measure (`price_fixed`) withholds the price rows and signs excess demand (PC-1); an import quota takes the tariff chains (EN-6: as under TX-7). Rows produced: 16 of 36 (was 15): C-7 (design schools' demand, ambiguous: about 40% already hold the degree). WRONG: 0 (was 1).
