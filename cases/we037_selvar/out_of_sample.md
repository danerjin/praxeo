# Out-of-sample run of the prohibition and price-ceiling rules on WE-037 (Selvar Fair Ticket Act)

Rules as they stood at commit 9c6d2e9 (prohibition rules written from WE-017 only; price-ceiling rules from WE-001, WE-005 and others). Record: `record.json`, two components: k1 `price_ceiling` (the resale cap; bound `resellers.brokers`, protected `buyers.insiders`, excluded `buyers.outsiders`, neighbour `neighboring_jurisdictions`, announcement window, no evasion-detectability flag, no general-budget flag because the division absorbs the work in its existing budget) and k2 `prohibition` (the bot ban; bound `bot_vendors`, buyers `resellers.brokers`). The text calls the cap a limit on a resale price, so `price_ceiling` (PC-18, `term_prohibition`, is not used, as the handbook says). Answers: `answers.json`, from the assumption table (A-1 to A-24) where a statement matches, otherwise judged. Key: (actor class, variable, sign, window). Run: `python3 -m praxeo cases/we037_selvar --out cases/we037_selvar/sample_run`. Test: `tests/test_oos_we037.py`.

Summary: the table has 47 rows (C-1 to C-49 without the removed C-20 and C-43). The engine reports 31 consequence keys. Rows produced by key: 12 (C-2 and C-25 for only some of the classes named; C-4 by mapping the table's "resale market" to the excluded buyers; C-47 by key only). Rows not produced: 35. Engine rows classified WRONG: 6.

Answer choices that matter: A-8 (holders and buyers time their sales) was not used for `window_repricing` because that question asks about contracts repriced upward in the window. First run with 0.7 gave an ambiguous price for the insiders (C-1 not produced) and a rise in the window, contradicting C-23; the answer was judged at 0.2 instead. The question's wording does not fit resale of tickets (nothing is repriced under contract), so this is a question-design gap, not a rule one. The K2 questions `enforced` and `enforcement_risk` are at 0.45 from A-13 (below the cut-off).

## Engine rows (reported)

| Engine row | Class | Why |
|---|---|---|
| buyers.insiders price_paid decrease | in table | C-1 |
| buyers.insiders price_paid decrease, window first_months | defensible | same sign as C-1 (combiner) |
| buyers.insiders quality_adjusted_price decrease | defensible | PC-4 with quality unreported; table has price only |
| buyers.insiders resources_available_other_uses increase | defensible | CR-8b mirror of C-1 |
| buyers.outsiders excess_demand increase | in table | C-4 (the table puts it on the resale market) |
| buyers.outsiders quantity_traded decrease | in table | C-6 |
| buyers.outsiders quantity_demanded increase | defensible | PC-3, other side of C-4 and C-6 |
| buyers.outsiders wait_time, search_cost, side_payments, allocation (at_least_one_increase) | in table (wait_time, search_cost, side_payments) | C-5; the allocation member sits in C-5 under a cell the key matching cannot split |
| buyers.outsiders side_payments increase | in table | C-10 (tie-ins) |
| buyers.outsiders allocation_by_non_price_criteria increase, search_cost increase | defensible | members of the PC-2 group, implied by C-5 |
| buyers.outsiders disputes_settled_outside_courts increase | in table | C-33 |
| buyers.outsiders informal_activity increase | defensible | RS-3 (C-9 names the sellers; no informal-seller role for a ceiling) |
| buyers.outsiders price_substitute increase | defensible | RS-4 with PC-3: primary demand-priced seats (C-28) |
| neighboring_jurisdictions price_paid increase | **WRONG** | C-39 is ambiguous: A-20 (brokers move purchases to Brackmere City) is an opposing chain with A-19. The engine has the fans' chain alone |
| officials.enforcement enforcement_cost increase | in table | C-40 |
| resellers.brokers net_price_received decrease | in table | C-2 (brokers; no fans role) |
| resellers.brokers quantity_supplied decrease | in table | C-3 |
| resellers.brokers quantity_traded decrease | in table (by key only) | C-47 is season tickets; the engine's row is OC-4's prevented exchange |
| resellers.brokers reclassification increase | in table | C-11 |
| resellers.brokers lobbying_effort increase | in table (part) | C-25 (no platforms, fans or primary sellers) |
| resellers.brokers resources_available_other_uses decrease; increase | defensible | CR-8b sides of C-1, C-2 and the evaders' premiums |
| **resellers.brokers disputes_settled_outside_courts increase** | **WRONG** | EN-7 and RS-10 for the bot ban: the black-market chain is gated on demand_persists and evasion, not on enforced. The example treats K2 as backing a term already in R1 (A-13 at 0.45, below the cut-off) and records no black market in bot software |
| **resellers.brokers quality_information decrease** | **WRONG** | same |
| **resellers.brokers quality_variability increase** | **WRONG** | same |
| **resellers.brokers search_cost increase** | **WRONG** | same |
| **resellers.brokers quantity_substitute increase** | **WRONG** | RS-1 for the ban without a change in what the bot users can buy (not enforced enough, A-13); no such row in the table |

The legal-seller chains of the ban (`bot_vendors` quantity, employment, assets, number of sellers) are correctly unreported: they rest on `enforced(k2)` at 0.45.

## Table rows

| Row | Produced? | Reason |
|---|---|---|
| C-1 insiders price_paid decrease | yes | |
| C-2 brokers, fans net_price_received decrease | yes (part) | no fans role |
| C-3 brokers, fans quantity_supplied decrease | yes (part) | same |
| C-4 resale market excess_demand increase | yes | by role mapping to the excluded buyers |
| C-5 outsiders PC-2 group | yes | |
| C-6 outsiders quantity_traded decrease | yes | |
| C-7 brokers quantity_demanded decrease | no | missing role: PC-12 input supplier (primary sellers) |
| C-8 brokers number_of_sellers decrease | no | missing rule: RS-6 under a ceiling |
| C-9 informal sellers, brokers informal_activity increase | no | no informal-seller role; the engine puts it on the buyers |
| C-10 outsiders side_payments (tie-ins) increase | yes | |
| C-11 brokers, primary sellers reclassification increase | yes (part) | brokers only |
| C-12 outsiders cross_border_purchases (offshore) increase | no | missing rule: RS-4 reach of enforcement |
| C-13, C-14 platforms (compliant, offshore) quantity_traded | no | no platform role; jurisdiction reach |
| C-15 bot_vendors quantity_traded decrease | no | K2 chain unreported (A-13); K1 chain across components not encoded |
| C-16 brokers legal_breach decrease | no | missing variable and rule (LW-10) |
| C-17, C-18, C-19 platform fees under U1 | no | the unclear provision changes no record field; no platform or fee role |
| C-21, C-22, C-23, C-24 window resales | no | RS-8 encoded for repricing only |
| C-25 lobbying increase | yes (part) | brokers only |
| C-26 to C-29 primary buyers and sellers | no | no roles; the free primary segment next to the capped one (PC-8, CR-9) |
| C-30, C-31 offshore, informal, all-channel price | no | no combiner |
| C-32, C-34 outsiders quality_information, quality_variability | no | RS-10 for ceilings is disputes only |
| C-33 outsiders disputes increase | yes | |
| C-35, C-36, C-48 season holders, waitlist, club | no | no roles (related market) |
| C-37 brokers asset_value decrease | no | CR-7c asks about durable covered assets |
| C-38 neighbours cross_border_purchases increase | no | RS-4 signs the neighbours' price only |
| C-39 neighbours price_paid ambiguous | no (wrong sign) | see WRONG row |
| C-40 enforcement_cost increase | yes | |
| C-41 other cases of the division | no | OC-3 fixed-budget case not encoded |
| C-42 platforms compliance_cost | no | no platform role |
| C-44, C-45 brokers to Brackmere City, fans' travel | no | no rule |
| C-46 charities quantity_traded increase | no | the exemption has no record field or rule |
| C-47 brokers season tickets quantity_traded decrease | yes, by key only | the engine row is OC-4's, not a season-ticket mechanism |
| C-49 platform owners asset_value | no | no platform role |

## General gaps

Ranked by table rows added or wrong rows fixed.

1. **Third parties and unregulated adjacent segments as roles of a ceiling (PC-8, CR-9, RS-4, CR-6 0.8).** A ceiling on a secondary market has intermediaries bound with the sellers (platforms), a free primary market it resells from, and out-of-reach channels (offshore). The component has roles only for sellers, protected, excluded and neighbour. A pattern-level field set (an `intermediary_actor`, an `uncapped_supplier_actor` with its price variable, an `out_of_reach_actor`) would allow C-13, C-14, C-12, C-26 to C-29, C-42, C-49 and, with a fee question, C-17 to C-19 (about 12 rows).
2. **RS-8 for quantity, not only repricing (RS-8, CR-10a, CR-12a).** Sellers pull sales into the window and buyers wait: C-21 to C-24 (4 rows). The window questions should also separate "contracts repriced" from "sales moved", as the wording of `window_repricing` forced a judgement here.
3. **Gate the EN-7 informal chain, RS-10 and RS-1 for a prohibition on `enforced` (EN-7, CR-1).** A ban that is not enforced does not move trade underground or change buyers' purchases. Fixes 5 WRONG rows (all from the bot ban at A-13 = 0.45).
4. **Opposing chains for RS-4 (CR-12, 0.8 clarification, kind 2).** The neighbours' price is signed `increase` from the shut-out fans alone. With a second question on suppliers shifting their buying (A-20; RS-16, RS-13), it becomes `ambiguous` (C-39, fixes the WRONG row) and adds the offshore and all-channel combiners C-30, C-31.
5. **RS-10 for ceilings beyond disputes, and an informal-seller role (RS-10, RS-3).** Quality information and variability on the informal channel (C-32, C-34) and the informal sellers (C-9): 3 rows.
6. **Asset-value and exemption patterns (CR-7c, CR-10c, CR-1 operation 4).** The value of resellers' businesses and season seat rights (C-35, C-37) needs its own question rather than `durable_assets` of the covered units; a record field for an exempt group (the charities) would add C-46; OC-3's fixed-budget case adds C-41 (4 rows).
7. **PC-12 for a ceiling on a resale (input is the primary ticket).** C-7, if brokers are the main buyers of the primary seller's output; a role the text does not support directly (1 row).
8. **Unclear provisions that change no field.** U1 changes who pays a fee, not a component field; `reading_fields` cannot express it. A fee-split record field would let the readings produce signs (C-17 to C-19, C-49 per reading).
