# Out-of-sample run of the subsidy rules on WE-065 (Brisklund Wheat Price Assurance Act)

Rules as they were after the subsidy commit (`praxeo/rules/subsidies.lp`, written from WE-019 only); nothing under `praxeo/` was changed. Record: `record.json`, one `per_unit_subsidy` component for the deficiency payment (K1): bound `wheat_growers` (the recipients are the sellers, so `seller_actor` is null), `asset_owner_actor` `owners.wheat_land`, taxpayers, `officials.enforcement`, flags `temporary`, `renewable`, `announcement_window`. The funding clause (K2) and the administration (K3) are folded into K1's taxpayer and enforcer fields; they have no instrument of their own in the rules. `debt_funded`, `budget_capped`, `eligibility_criteria`, `scrappage` and `repay_on_move` are false, because the text does not say so. U1 (actual output or a historical base) is in `unclear`; the readings carry no engine facts, so the engine runs once, with the mechanism of actual output (U1-a). Answers: `answers.json`, from WE-065's assumption table where a row matches (A-1, A-8, A-11, A-12, A-18, A-3) and judged from the text for the four questions with no matching row (`seller_supply_slow`, `sellers_fewer_alternatives`, `can_delay`, `pulled_forward`). Run: `python3 -m praxeo cases/we065_brisklund --out cases/we065_brisklund/sample_run`. Key: (actor class, variable, sign, window). The table's reading-dependent signs ("U1-a: increase; U1-b: no_change") are keyed by their U1-a sign; the U1-b halves are not checked.

Summary: the table has 43 rows (C-1 to C-43). The engine reports 6 consequences (a 7th, the announcement-window delay, is below the cut-off at p 0.09). Rows produced by key: 3 (C-16, C-25, C-33); rows not produced: 40. Engine rows classified WRONG: 1.

## Engine rows (reported)

| Engine row | Class | Why |
|---|---|---|
| officials.enforcement enforcement_cost increase | in table | C-33 |
| wheat_growers compliance_cost increase | in table | C-16 |
| owners.wheat_land asset_value increase | in table | C-25 (SB-4 with A-11, A-12) |
| taxpayers resources_available_other_uses decrease | defensible | C-7, C-8, C-32, C-34 sign the group of three classes `at_least_one_decrease`, per state of the world; SB-1 gives the one named class a plain decrease. Same fact, different key |
| wheat_growers quantity_traded increase | defensible | the growers sell more wheat (SB-2, A-3); the table signs it as quantity_supplied (C-9) and as the exporters' quantity_traded (C-21). Holds under U1-a only; the engine does not separate U1-b |
| **wheat_growers price_paid decrease** | **WRONG** | SB-2's "recipients pay less" is the rule for recipients who buy the good. These recipients sell it: the example signs net_price_received increase (C-4, C-6) and has no price_paid row for the growers. The payment raises what they receive, it does not lower what they pay |

Not reported but worth noting: `wheat_growers quantity_traded decrease` in the announcement window (RS-8 delay) was derived and is below the cut-off (can_delay p 0.1, judged from the text). Had it been above, it would be WRONG: growers buy nothing that they can postpone, and the table has no such row.

## Table rows

"Part" does not occur here: every row names classes the record has no role for, or is produced whole.

| Row | Produced? | Reason |
|---|---|---|
| C-1 treasury subsidy_outlay increase | no | missing rule: no outlay variable and no treasury role; SB-1 signs the funders' resources (CR-8b) |
| C-2 treasury subsidy_outlay no_change (years at or above the line) | no | missing rule: CR-8's contingent payer; the engine derives no `no_change` and has no state-of-the-world qualifier |
| C-3 wheat_growers resources_available_other_uses increase | no | missing rule: CR-8b mirror (recipients' resources); SB-1 signs the funders only |
| C-4 wheat_growers net_price_received increase | no | missing rule: SB-2 for sellers who are the recipients; the engine gives the WRONG price_paid decrease |
| C-5 wheat_growers net_price_received decrease (years at or above, small) | no | missing rule and record fact: CR-6, CR-9 world-price chain |
| C-6 wheat_growers net_price_received increase (expected at sowing) | no | missing rule: as C-4 |
| C-7 taxpayers, recipients of other spending, future taxpayers resources at_least_one_decrease | no | combiner: group sign over three classes; the record has one funder class |
| C-8 same, whole period | no | combiner: as C-7, the CR-12 total across states of the world is not declared |
| C-9 wheat_growers quantity_supplied increase | no | missing rule: SB-2 signs quantity_traded; the producer's variable is quantity_supplied |
| C-10 wheat_growers number_of_sellers increase | no | missing rule: RS-6 entry |
| C-11 wheat_growers quantity_substitute (barley) decrease | no | missing record fact: the growers' other output is no role field (SB-3 is for the recipients' purchases) |
| C-12 wheat_growers product_attribute (high-yield varieties) increase | no | unsupported form: RS-16 |
| C-13 wheat_growers legal_breach increase | no | missing rule: RS-3 and RS-5 for overstated claims; the penalty clause has no field |
| C-14 wheat_growers quantity_substitute (hedges) decrease | no | case-specific provision: price cover (RS-1) |
| C-15 lobbying groups lobbying_effort increase | no | missing rule: SB-5 with RS-7 needs a seller class apart from the recipients; and `lobbying groups` is no role |
| C-16 wheat_growers compliance_cost increase | yes | |
| C-17 buyers.foreign price_paid decrease | no | missing record fact and rule: foreign buyers, world-price chain (CR-6, CR-9) |
| C-18 sellers.foreign net_price_received decrease | no | same |
| C-19 sellers.foreign quantity_supplied decrease | no | same |
| C-20 buyers.current price_paid decrease | no | missing record fact and rule: domestic buyers of a subsidized good (buyer_actor is a tax field), same chain |
| C-21 grain_exporters quantity_traded increase | no | missing record fact: exporters (no role), CR-4, CR-7a |
| C-22 treasury subsidy_outlay (against a static projection) increase | no | missing rule: no outlay variable; RS-16 and CR-6 chain |
| C-23 feed_buyers price_paid (feed barley) ambiguous | no | unsupported form: RS-13, CR-12b; no role |
| C-24 input_suppliers quantity_traded (wheat seed) increase | no | missing record fact: no input-supplier field for subsidies; CR-9, LW-10 |
| C-25 owners.wheat_land asset_value increase | yes | via SB-4 (asset_supply_slow A-12, expected_to_last A-11); the table's other premises (A-2, A-18) are not asked |
| C-26 owners.convertible_land asset_value increase | no | missing record fact: one `asset_owner_actor` per component |
| C-27 owners.wheat_land subsidy_share_received (against tenant growers) increase | no | missing rule and record fact: CR-7b and DM-1 between landowners and tenants; no tenants role |
| C-28 tenants price_paid (farmland rent at renewal) increase | no | same |
| C-29 wheat_growers interest_rate decrease | no | missing record fact: lenders; no rule |
| C-30 import_competing_industries quantity_supplied, employment, hours_worked at_least_one_decrease | no | missing rule: TX-8's mirror through the currency for a subsidy; no roles |
| C-31 export_industries.other (same group) | no | same |
| C-32 taxpayers etc. resources at_least_one_decrease (what the payments would have funded) | no | combiner: as C-7 |
| C-33 officials.enforcement enforcement_cost increase | yes | |
| C-34 taxpayers etc. resources at_least_one_decrease (administration) | no | combiner: as C-7; OC-3's funding is encoded as the agency's cost only |
| C-35 wheat_growers quantity_supplied (other output given up) decrease | no | missing record fact: as C-11 |
| C-36 lobbying groups lobbying_effort ambiguous | no | missing rule: RS-7's Unless clause (support is contested without the Act); no lobbying row at all |
| C-37 input_suppliers quantity_traded (fertilizer, contract harvesting) ambiguous | no | unsupported form: CR-12b over crops; as C-24 |
| C-38 wheat_growers quantity_supplied (milling wheat) ambiguous | no | unsupported form: CR-12b |
| C-39 treasury non_tax_receipts increase | no | missing record fact and rule: repayments and fines (CR-8b); no field for the penalty |
| C-40 treasury subsidy_outlay (net of repayments and fines) increase | no | combiner: CR-12e arithmetic on an outlay variable the rules lack |
| C-41 livestock_farmers price_paid (pasture rent) increase | no | missing record fact: no role |
| C-42 sellers.neighboring quantity_traded increase | no | missing record fact and rule: neighbour sellers for a subsidy (RS-4-style field exists for ceilings and taxes only) |
| C-43 buyers.imports price_paid decrease | no | missing rule and record fact: TX-8 chain through the currency |

## General gaps

Ranked by the rows they would add or fix.

1. **The world-price and currency chain for a subsidy on a traded good** (about 10 rows: C-5, C-17 to C-21, C-30, C-31, C-43, and the first link of C-22). The example turns on SB-2 and CR-6 for a good priced abroad (SB-2's clause on a good priced in a wider market; SB-10 for export subsidies, not encoded) and on TX-8's mirror through the currency. General fix: add to the subsidy rules the pattern that already exists for tariffs and taxes: record fields for the foreign sellers and buyers, the exporters and the export industries (the tariff fields `foreign_seller_actor` and `exporter_actor` have the same roles), and a rule that, where the subsidized output is tradable (a flag or a context fact such as "price follows the export price"), signs the world price, the foreign sellers and the exporters (CR-6, CR-9, SB-2 1.1 clause, TX-8), with the small-effect note of CR-6 as a premise (A-18/A-9 type question).
2. **The payer's side of a subsidy: outlay, mirror, contingency and group** (about 9 rows: C-1, C-2, C-3, C-7, C-8, C-32, C-34, C-39, C-40). General fix, three small pattern changes: (a) SB-1/OC-1 should sign the funders as the group "taxpayers, recipients of other spending, future taxpayers" with `at_least_one_decrease` (the handbook's normal form in WE-019 as well), instead of a plain decrease on one class; (b) CR-8b: add the recipients' resources increase and an outlay variable for the paying budget (`subsidy_outlay`, role `treasury`); (c) CR-8's contingent payer: a flag `contingent` (payment only in states of the world, such as years below a line) that adds the per-state `no_change`, and a declared CR-12 total across states; plus penalties and repayments (non_tax_receipts, OC-3) as a `penalty` flag with its question.
3. **SB-2 when the recipients are the sellers (a payment to producers)** (about 5 rows added: C-4, C-6, C-9, C-10, C-15 in part; and the WRONG row removed). The rule written from WE-019 treats `bound_actor` as a buyer. General fix, from SB-2 and the WE-065 and WE-019 pairing: where `seller_actor` is null (recipients are the sellers), SB-2 signs the recipients' `net_price_received` increase (and the expected price at sowing as RS-8-type timing for a crop), `quantity_supplied` rather than `quantity_traded` for producers (with RS-6's entry as `number_of_sellers`), and does not sign `price_paid`. SB-5 with RS-7 should then name the recipients as the lobbying seller class (the `sb_seller` fact falls back to the recipients), and RS-7's Unless clause gives the `ambiguous` row (C-36). RS-8's delay and SB-6's dip should not fire for a producer payment: guard them on the recipients buying.
4. **Second asset-owner, input-supplier and tenant roles** (about 8 rows: C-24, C-26, C-27, C-28, C-37, C-41; C-29 lenders). General fix: allow more than one `asset_owner_actor` (owners of land with and without the benefit; SB-4, CR-7a) and add the roles already used for tariffs and ceilings to subsidies: `input_supplier_actor` (CR-9, LW-10), and a tenants role for CR-7b/DM-1, which would also give WE-001 and WE-067 rows.
5. **Quality, substitute output and declarations** (about 6 rows: C-11, C-35, C-12, C-38, C-13, C-23). RS-16 (payment per unit of one grade), SB-3 for the producers' own alternative output (a role field for "the output given up"), and RS-3/RS-5 for overstated claims need new rules and fields; each adds one or two rows, and CR-12b ambiguous rows need declared combiners.
6. **Readings of an unclear provision** (affects the reading-dependent halves of about 25 rows). The parser's `reading_facts` is empty by design, so the engine cannot run U1-b (`no_change` for supply responses). General fix: a record flag or reading-level instrument change (the subsidy is on a fixed base, so `quantity_expands` and the SB-2 quantity chain are blocked), set by a person for each reading, as the schema already allows for exceptions.

## After the rule changes (second commit)

The record and answers changed only where a new field or question needs it (temporary payments: `ends_as_scheduled` and `supply_slow_at_expiry`; WE-021: `qualifier_actor`, `tax_named`; WE-033: the payer group's names; WE-056: K1's payer and its two PC-20 questions). Rows produced: 10 of 43 (was 3). Engine rows WRONG: 1 (was 1, a different row). SB-2 now signs a payment to producers on the sellers' side: `net_price_received` and `quantity_supplied` increase (C-4, C-6, C-9), not the buyers' `price_paid`; no delay before the start and no dip after expiry. The payers are the OC-1 group (C-7, C-8, C-32, C-34). New WRONG row: the growers' lobbying for renewal (RS-7, now that the recipients count as the gaining sellers), which C-36 signs ambiguous by RS-7's Unless clause; that clause is not encoded (as WE-067 C-27).
