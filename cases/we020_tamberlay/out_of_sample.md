# Out-of-sample run of the subsidy rules on WE-020 (Tamberlay Home Start Grant)

Rules as they were after the subsidy commit (`praxeo/rules/subsidies.lp`, developed on WE-019 only); nothing under `praxeo/` was changed. Record: `record.json`, one `purchase_rebate` component for the grant (K1) with eligibility criteria (K2, a condition of K1), temporary, renewable, announcement window and repay-on-move (the 24-month residence rule); bound `buyers.first_time`, seller and asset owner `owners.entry_level`, other buyers `buyers.other`, general-revenue funding (K3, so no debt or own-revenue flag), enforcer `officials.enforcement` (K4). No component has an instrument of its own for K2, K3 or K4. The price cap, the rental market, builders, landowners, intermediaries, renters and Lowen have no role field for a subsidy (the text names builders and Lowen only as context). The text does not say the budget is capped (it says the law is silent on over-subscription), so `budget_capped` is false. Answers: `answers.json`, 12 questions, from WE-020's assumption table (A-1, A-2, A-3, A-4, A-5, A-7, A-9, A-17, A-20) wherever a row matches; `takeup` and `pulled_forward` have no matching assumption and are judged from the text. Run: `python3 -m praxeo cases/we020_tamberlay --out cases/we020_tamberlay/sample_run`; verifier and citation problems are empty. Key: (actor class, variable, sign, window). Test: `tests/test_oos_we020.py`.

Summary: the table has 33 rows (C-1 to C-33). The engine reports 18 consequences. Rows produced by key: 14 of 33 (C-9 for the owners only, not builders or intermediaries). Rows not produced: 19. Engine rows classified WRONG: 2 (one cause).

## Engine rows (reported)

| Engine row | Class | Why |
|---|---|---|
| buyers.first_time price_paid decrease | in table | C-1 |
| buyers.first_time quantity_traded increase | in table | C-2 |
| buyers.first_time quantity_traded decrease, window announcement | in table | C-3 |
| buyers.first_time reclassification increase | in table | C-5 |
| buyers.first_time job_changes decrease | in table | C-7 |
| buyers.first_time turnover decrease | in table | C-8 |
| owners.entry_level lobbying_effort increase | in table (part) | C-9 (owners only) |
| owners.entry_level asset_value increase | in table | C-11 |
| buyers.other price_paid increase | in table | C-12 |
| buyers.other quantity_traded decrease | in table | C-13 |
| officials.enforcement enforcement_cost increase | in table | C-23 |
| taxpayers resources_available_other_uses decrease | in table | C-24 |
| owners.entry_level subsidy_share_received increase | in table | C-28 |
| buyers.first_time compliance_cost increase | in table | C-33 |
| owners.entry_level net_price_received increase | defensible | SB-2 with DM-1: the sellers' side of the capitalization, which the table records as the asset value (C-11) and the share (C-28) |
| owners.entry_level quantity_traded increase | defensible | the sellers' side of C-2; the table signs the buyers' side only (same exception as in WE-019) |
| **owners.entry_level net_price_received decrease, window after_expiry** | **WRONG** | SB-6 fires on `temporary` alone. WE-020 lists the dip after Year 4 and the fall in values under "Not reported": they rest on non-renewal (A-15, p = 0.4, below the cut-off). The record has `renewable` true and the answers carry no premise for non-renewal |
| **owners.entry_level quantity_traded decrease, window after_expiry** | **WRONG** | same (the dip in purchases after 30 June of Year 4 is not reported) |

## Table rows

| Row | Produced? | Reason |
|---|---|---|
| C-1 first-time buyers price_paid decrease | yes | |
| C-2 first-time buyers quantity_traded increase | yes | |
| C-3 first-time buyers quantity_traded decrease (March to June) | yes | |
| C-4 owners quantity_supplied decrease (listings, March to June) | no | missing rule: RS-8 and TS-2 are encoded for the recipients' delay only; no question for sellers holding back |
| C-5 first-time buyers reclassification increase | yes | |
| C-6 owners, first-time buyers side_payments increase | no | missing rule and missing record fact: SB-5 with RS-5 signs the recipients' reclassification only; no field for a price threshold in the criteria (sellers just above the cap) |
| C-7 recipients job_changes decrease | yes | |
| C-8 recipients turnover decrease | yes | |
| C-9 owners, builders, intermediaries lobbying_effort increase | yes (part) | owners only; no builders or intermediaries role |
| C-10 first-time buyers quantity_traded increase (before end of Year 4) | no | missing rule: RS-8's deadline form (renewal uncertain, A-16); no question |
| C-11 owners asset_value increase | yes | |
| C-12 other buyers price_paid increase | yes | |
| C-13 other buyers quantity_traded decrease | yes | |
| C-14 builders investment_target increase | no | missing record fact (no builders role: one seller role per component) and missing rule (LW-4, TS-1 for new supply) |
| C-15 builders reclassification increase | no | same, and a price threshold (see C-6) |
| C-16 other buyers (above cap) quantity_substitute decrease | no | missing record fact: the market relation (entry-level and other building draw on the same builders) has no field; SB-3 needs `substitute_seller_actor`, which the text does not name |
| C-17 landowners asset_value increase | no | missing record fact: land as an input to new homes (`input_to`) has no field; one asset-owner role; `landowners.developable` is not in the text |
| C-18 renters price_substitute ambiguous | no | missing record fact (no renters role, no substitute relation) and combiner (no declared comparison) |
| C-19 intermediaries earnings increase | no | missing record fact (no role) and missing rule (commission premise A-21) |
| C-20 first-time buyers (Kessford) cross_border_purchases decrease | no | missing record fact: `neighbor_actor` exists for price ceilings only; RS-4 is not encoded for subsidies |
| C-21 neighboring_jurisdictions quantity_traded ambiguous | no | combiner (CR-12b over C-20 and C-29 not declared) and no neighbour role |
| C-22 owners (trading up) price_paid increase | no | missing rule: OC-7 not encoded |
| C-23 enforcement_cost increase | yes | |
| C-24 taxpayers resources_available_other_uses decrease | yes | |
| C-25 other buyers resources_available_other_uses decrease | no | missing rule: CR-8b mirror of C-12 for subsidies |
| C-26 builders quantity_traded ambiguous | no | combiner (C-14 against C-16 not declared), neither chain produced |
| C-27 owners resources_available_other_uses increase | no | missing rule: OC-7 |
| C-28 owners subsidy_share_received increase | yes | |
| C-29 other buyers (Kessford) cross_border_purchases increase | no | missing rule and record fact: RS-4 for subsidies, neighbour |
| C-30 landlords quantity_supplied decrease | no | missing record fact (no landlords role) and rule (SB-3, CR-4, CR-7a through the rental market) |
| C-31 renters quantity_substitute decrease | no | missing record fact (no renters role); RS-1 and CR-12a for rental units let |
| C-32 construction_labor wage_rate increase | no | missing record fact (no role) and rule (CR-9, CR-7a for the price of a drawn-in resource under subsidies) |
| C-33 applicants compliance_cost increase | yes | |

Not applicable here: the case-specific provision category (no row rests on a provision particular to this grant beyond the 24-month residence rule, which RS-11 covers), and unsupported form (K2 to K4 are conditions, funding and enforcement of K1, which the K1 component carries).

## General gaps

Ranked by the rows each would add or fix.

1. **Market-relation facts for subsidies** (handbook section 6 "Market relation" column: `substitute`, `input_to`, `across_border`, `same_market_other_segment`; SB-3, SB-4, RS-1, RS-4, CR-12a/b). The record can hold one seller role, one asset owner and one substitute seller, and no neighbour or input relation. A general change is a list of related markets on the component, each with an actor class and a relation type, and rules that run SB-3/SB-4/RS-1/RS-4 over it. It would add C-14, C-16, C-17, C-18, C-20, C-29, C-30, C-31, C-32 directly (about 9), and with the declared comparisons (CR-12) C-21 and C-26. The ceiling rules already have `neighbor_actor` and `input_supplier_actor`; this generalizes them to the subsidy and tax families.
2. **SB-6 after-expiry rows need a non-renewal premise** (SB-6 in the catalog, WE-020 A-15 and the "Not reported" note). Fixes the 2 WRONG rows. The general fix: the dip and the fall in values apply only when expiry is expected to be final, so a temporary subsidy with `renewable` asks a `lapses` question (the premise A-15 states) and SB-6's after-expiry chains require it to hold; a probability of 0.4 stays below the cut-off and the rows are not reported, as in WE-020. WE-019 has `renewable` true as well, with "no plan to repeat", so its answer would be high there (its table keeps the dip).
3. **RS-8 for the other timing groups** (RS-8, TS-2, A-5, A-6, A-16). Sellers holding back listings in the announcement window (C-4) and the rush before the deadline when renewal is uncertain (C-10) are the same pattern as the buyers' delay: a party who expects the terms to change shifts action across the date. Adds 2 rows; needs a question each (`sellers_can_hold_back`, `renewal_uncertain`) and a deadline window kind.
4. **SB-5 with RS-5 on a numeric line in the criteria** (C-6, C-15, and the bunching in section 8). A record field for "the criterion is a threshold on the price or size of what is bought" lets the rule sign reclassification and side payments on the sellers' side of the line, with the sellers as the role. Adds 2 rows.
5. **OC-7 and the CR-8b mirror under subsidies** (C-22, C-25, C-27). What sellers gain by selling at the capitalized price, other buyers pay (a resources entry for `buyers.other` mirroring C-12), and sellers can spend or borrow against the gain. Adds 3 rows from rules the ceiling and tax families already have in other forms.
6. **Intermediaries and construction labor as role fields with RS-style premises** (C-19, C-32, and the intermediaries and builders part of C-9). These come with item 1 once related actor classes can be named.

Record-level note (not a rule gap): the parser's readings for the two unclear provisions (price-cap indexation, renewal) carry no engine facts, as the schema requires; reading U2 (renewal) is exactly the fact SB-6 needs in item 2, so a person who writes `reading_facts` for it would change the after-expiry rows between readings.

## After the rule changes (second commit)

The record and answers changed only where a new field or question needs it (temporary payments: `ends_as_scheduled` and `supply_slow_at_expiry`; WE-021: `qualifier_actor`, `tax_named`; WE-033: the payer group's names; WE-056: K1's payer and its two PC-20 questions). Rows produced: 14 of 33 (unchanged). Engine rows WRONG: 0 (was 2). The dip and the fall in owners' prices after Year 4 now need the grant to end as scheduled (`ends_as_scheduled`, A-15, p = 0.4), so they are not reported, as in the example. The payers are now the OC-1 group (taxpayers, recipients of other spending, future taxpayers, `at_least_one_decrease`), since the record names no tax; WE-020's C-24, written under catalog 0.5 with taxpayers alone, was corrected in the handbook to the same group, so C-24 is still produced.
