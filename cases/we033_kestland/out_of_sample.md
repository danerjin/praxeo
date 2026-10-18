# Out-of-sample run of the subsidy rules on WE-033 (Kestland Household Support Payment Act 2027)

Rules as they were at commit 59d879f (`subsidies.lp`, written from WE-019 only; nothing under `praxeo/` changed). Record: `record.json`, one `lump_sum_subsidy` component for the payment (K1): bound `households.recipients`, claims by `households.no_account`, enforcer `officials.enforcement`, funder `taxpayers.later`, flags `debt_funded`, `eligibility_criteria`, `announcement_window`. No seller (`seller_actor` null: the text names no good). K2 (borrowing), K3 (repayment rule) and K4 (administration, fraud) have no instrument the rules encode; K2 and K3 enter only through `debt_funded` and the funder, K4 through the enforcer. Two unclear provisions (U1 household, U2 funding of the installments) are in the record without engine facts. Answers: `answers.json` is `[]`, because a lump sum has no questions (`questions_for`). Run: `python3 -m praxeo cases/we033_kestland --out cases/we033_kestland/sample_run`; verifier and citation problems empty. Key: (actor class, variable, sign, window).

Summary: the table has 31 rows (C-1 to C-33 without the removed C-20 and C-21; the unnumbered last row, employment across sectors, is not parsed). The engine reports 3 consequences. Rows produced by key: 2 (C-2, C-5). Rows not produced: 29. Engine rows classified WRONG: 1. Because the lump sum has no questions, no assumption of the table (A-1 to A-19) is used, and every row that rests on one is out of reach.

## Engine rows (reported)

| Engine row | Class | Why |
|---|---|---|
| officials.enforcement enforcement_cost increase | in table | C-2 (OC-3; Tier A, no assumption) |
| households.no_account compliance_cost increase | in table | C-5 (CR-8c via the claim handler) |
| **taxpayers.later resources_available_other_uses decrease** (medium, long) | **WRONG** | SB-1 puts a plain `decrease` on the funder named in the record. C-19 signs a group, `at_least_one_decrease`, over the later taxpayers and the later recipients of public spending, because the text names no tax and the Finance Ministry says repayment comes "through spending restraint" (A-4, p 0.45; section 7 refuses a whole-period sign for the same reason). The engine's sign is stronger than the example's. The horizon (from medium on) agrees with C-19 (2028 to 2037) |

## Table rows

| Row | Produced? | Reason |
|---|---|---|
| C-1 recipients resources increase | no | missing rule: SB-1 signs the payers only; the recipients' own gain (CR-8b mirror of the funding) is not derived. The one Tier A row of the payment itself |
| C-2 officials.enforcement enforcement_cost increase | yes | |
| C-3 lenders.new quantity_traded increase | no | unsupported form: the bond sale (K2) has no rule |
| C-4 recipients saving increase | no | missing rule (CR-4 "A change in means alone", "Saving is a use") and no question for a lump sum |
| C-5 households.no_account compliance_cost increase | yes | |
| C-6 households.splittable reclassification increase | no | missing question: SB-5 is gated on takeup, which a lump sum does not ask (A-7) |
| C-7 consumer_lenders quantity_traded increase | no | missing rule: RS-8 is encoded for purchases of the subsidized good, not for credit against an announced payment (A-5) |
| C-8 consumer_lenders quantity_traded decrease | no | missing rule: CR-4 timing shift in credit (A-6) |
| C-9 borrowers.private interest_rate (per reading) | no | unsupported form: OC-8; also the table cell is a per-reading sign and the readings carry no engine facts |
| C-10 borrowers.private quantity_traded | no | same as C-9 |
| C-11 sellers.investment_goods_housing quantity_traded | no | same as C-9 (no role for the crowded-out sellers) |
| C-12 same class, employment, hours_worked | no | same as C-11 (OC-5) |
| C-13 sellers.recipients quantity_traded, net_price_received | no | missing record fact (no seller role for a payment with no named good) and missing rule (CR-4 means alone) |
| C-14 sellers.recipients employment, hours_worked | no | same as C-13 |
| C-15 bondholders.existing asset_value | no | unsupported form: OC-8 with CR-7c |
| C-16 lenders.new return_on_capital | no | unsupported form: OC-8 with CR-7a |
| C-17 economy capital_stock_economy | no | unsupported form: OC-8, CR-7 |
| C-18 sellers.all quantity_traded ambiguous | no | combiner: CR-12b total over C-13 and C-11 not declared |
| C-19 taxpayers.later, public_spending_recipients.later resources at_least_one_decrease | no | missing rule: a group over the payers when the funding source is open (OC-1 "Who pays: a group"); the engine's plain `decrease` for `taxpayers.later` is the WRONG row above. Also no role field for the second class |
| C-22 officials.enforcement subsidy_outlay increase | no | missing rule: CR-1 operation 4 with CR-8b; SB-1 does not sign the paying agency's outlay |
| C-23 shortfall_bearers (per reading) | no | case-specific provision: CR-8 "a law that promises more than its budget can pay" under U1-b; no encoding of the shortfall or its bearers |
| C-24 recipients consumption increase | no | missing rule and question: CR-4 means alone with CR-12e (A-1, A-16, A-17) |
| C-25 households.borrowing_in_advance consumption increase | no | missing rule: RS-8 for borrowers against the announced payment (A-5) |
| C-26 households.would_have_borrowed resources increase | no | missing rule: CR-10b/CR-8b for loans not taken (A-6) |
| C-27 claimants.false legal_breach increase | no | missing rule (CR-1 operation 3, CR-4 comply or violate) and no role for false claimants |
| C-28 claimants.false resources increase | no | same as C-27 (CR-8b) |
| C-29 households.defrauded compliance_cost increase | no | missing record fact (no role for the defrauded) and missing rule (CR-8c, OC-2) |
| C-30 officials.enforcement non_tax_receipts increase | no | missing rule: repayments and fines as receipts (CR-1 operation 3 with CR-8b); the same gap as WE-067 C-47 |
| C-31 officials.prosecution enforcement_cost increase | no | case-specific provision: a second agency, no role field |
| C-32 homeowners asset_value (per reading) | no | unsupported form: OC-8, CR-7c |
| C-33 owners.consumer_businesses asset_value ambiguous | no | combiner: CR-12b between the sales chain and the discount-rate chain not declared; OC-8 unsupported |

## General gaps

Ranked by the rows each would add or fix.

1. **Means-only payments (CR-4 "A change in means alone", "Saving is a use", RS-8 for credit against an announced payment, CR-8b mirror).** A `lump_sum_subsidy` today yields only the funder, the agency and the claimants, and asks no question. The handbook patterns give, from the same premises as A-1, A-2, A-5, A-6, A-16 and A-17: the recipients' resources (C-1), saving (C-4), consumption (C-24), credit and consumption in the announcement window (C-7, C-25), credit avoided later (C-8, C-26), and the unnamed sellers' group (C-13, C-14). General fix: give `lump_sum_subsidy` its own question set (spends some, saves some, borrows against it, would have borrowed) and the CR-4 means rules, with SB-1's mirror for the recipients. About 9 rows (C-1, C-4, C-7, C-8, C-13, C-14, C-24, C-25, C-26), plus the sellers' side if a "sellers of whatever recipients buy" role is added.
2. **Public borrowing (OC-8 with CR-7a, CR-7c, CR-9, CR-10c).** The `debt_funded` flag only moves SB-1 to the medium horizon. A borrowing pattern (the new loans compete with private borrowers, existing bonds lose value, homes lose value, investment falls) would give C-3 and C-9 to C-12, C-15 to C-17, C-32 and part of C-18 and C-33, but needs the per-reading sign (U1) and an accounting identity (CR-12e) that the record format does not carry: `reading_facts` is written by a person. 11 to 12 rows; the largest block, and the one the pattern-level rules do not touch at all. Whether it belongs to subsidies or to a `government_borrowing` instrument (K2, already in the ontology) is a design question.
3. **SB-1 when the revenue source is open (the WRONG row, and C-19).** When the funder is not one named tax (no revenue named, "general revenue"), OC-1 "Who pays: a group" gives `at_least_one_decrease` over the funder and the recipients of other spending, not a plain `decrease` on the funder. General fix: a record flag (or a funder role pair, e.g. `taxpayer_actor` plus `spending_recipient_actor`, the controlled list already has `recipients.other_spending`) and a group effect in SB-1 whenever no revenue is named. Fixes 1 WRONG row and adds C-19. The plain `decrease` stays for cases where the record names the payers (WE-019's C-20 signs the taxpayers), so the group form is the new case, not a replacement.
4. **Subsidy outlay and receipts (CR-1 operation 4, operation 3, CR-8b).** `subsidy_outlay` for the paying agency (C-22), repayments and fines as `non_tax_receipts` for false claims (C-30, also WE-067 C-47), and the fraud rows (C-27 to C-29) for a payment made to details that can be changed. A general "payment has claims, claims can be false" pattern with a claimants role. 4 rows (C-22, C-27, C-28, C-30), 5 with the defrauded (C-29).
5. **Per-reading signs in the row format and the record.** Eight table rows (C-9 to C-12, C-15 to C-17, C-23, C-32) carry one sign per reading of U1 and can never match a single key. The parser cannot attach engine facts to a reading (`reading_facts` is for a person), so the engine never runs under U1-b. General fix: let the test harness compare a per-reading cell to `sign_by_reading`, and give the record a way to say that a reading changes the number of payments against the funds (CR-8, a law that promises more than its budget can pay). Mostly a harness and record-format change; it makes the OC-8 rows scorable once gap 2 exists.
6. **Roles that the record has one field for.** Prosecution (C-31), the defrauded (C-29), the shortfall bearers (C-23): each needs a second agency or class beside `enforcer_actor` and `claim_handler_actor`. Recurs with WE-067's second neighbour and second board; a general list-valued role (`other_agencies`) would carry them. 3 rows.

## After the rule changes (second commit)

The record and answers changed only where a new field or question needs it (temporary payments: `ends_as_scheduled` and `supply_slow_at_expiry`; WE-021: `qualifier_actor`, `tax_named`; WE-033: the payer group's names; WE-056: K1's payer and its two PC-20 questions). Rows produced: 3 of 31 (was 2). Engine rows WRONG: 0 (was 1). SB-1 now follows OC-1's who-pays clause: no tax is named, so the payers are a group over actor classes (`taxpayers.later`, `public_spending_recipients.later`, `at_least_one_decrease`), which is C-19. The engine gained groups over actor classes (`Consequence.actor_group`) for this.

## After the payer's side (fourth commit)

SB-1's receipt side (`rules/subsidies.lp`): the paying body's `subsidy_outlay`; what recipients receive (`resources_available_other_uses`, CR-8b); with penalties for false claims in the text (`claim_penalties`), false claims (RS-3, `false_claims`) and their recovery (`non_tax_receipts`, `claims_recovered`); and the other buyers' loss where sellers capture part of the payment. Rows produced: 6 of 31 (was 3): C-1 (households receive the payment), C-22 (the Tax Agency's outlay) and C-30 (repayments and fines, A-18). The false claims (A-14) are signed on the recipients; the table names the false claimants as their own class (C-27).
