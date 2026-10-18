# Out-of-sample run of the quota rules on WE-014 (Calvar Sugar Market Act)

Rules as they were at commit a0e7be0 (`praxeo/rules/licensing.lp`; the quota rules written from EN-6's text alone, licensing developed on WE-003). Nothing under `praxeo/` was changed. Record: `record.json`, one `quota` component for K1 with K2 (the free, transferable shares: `right_holder_actor` `quota_holders`, `transferable`) and K3 (customs: `enforcer_actor` `officials.enforcement`, `general_budget`) folded into it, since neither has an instrument of its own. Flags set because the text says so: `import_quota`, `transferable`, `general_budget`, `renewable` (five-year review), `definition_line` (65% line, finished foods), `announcement_window` (nine months). Not set: `wider_market` (the text does not say the price is set in a wider market), `field_contested`. The 65% threshold is U1; its two readings change no Component field, so `reading_fields` is empty. Answers: `answers.json`, from WE-014's assumption table (A-1, A-2, A-3, A-5, A-12, A-17, A-21, A-22); all eight questions have a matching assumption. Run: `python3 -m praxeo cases/we014_calvar --out cases/we014_calvar/sample_run`; verifier and citation problems are empty. Key: (actor class, variable, sign, window). Test: `tests/test_oos_we014.py`.

Summary: the table has 34 rows (C-1 to C-34). The engine reports 16 keys (13 consequences; the OC-1 payer group and the exporters' RS-6 group give one key per member). Rows produced by key: 10 of 34 (C-2, C-3, C-4, C-5, C-12, C-23, C-25, C-27, C-33, C-34), of which C-12 and C-25 for only some of the classes the row names (no manufacturers; no foreign sellers) and C-23 and C-33 through a naming map (the table's `exporters.calvar` is the engine's default `export_industries` and its workers; section 1 names no exporters). Rows not produced: 24. Engine rows classified WRONG: 0.

## Engine rows (reported)

| Engine row | Class | Why |
|---|---|---|
| buyers.sugar price_paid increase | in table | C-3 |
| buyers.sugar quantity_traded decrease | in table | C-25 (buyers' side only) |
| buyers.sugar resources_available_other_uses decrease | in table | C-27 |
| growers.beet net_price_received increase | in table | C-2 |
| growers.beet quantity_supplied increase | in table | C-4 |
| quota_holders asset_value increase | in table | C-5 (EN-2/EN-6 with SB-4, `expected_to_last` 0.65) |
| quota_holders lobbying_effort increase | in table | C-12 (holders only; growers and manufacturers have no role) |
| export_industries quantity_supplied decrease | in table | C-23 (TX-8 for an import quota) |
| workers.export_industries employment, hours_worked at_least_one_decrease | in table | C-33 |
| officials.enforcement enforcement_cost increase | in table | C-34 |
| importers quantity_traded decrease | defensible | the bound role from the text (all importers); C-1 names the subclass quota_holders, the sound claim for the wider class |
| quota_holders net_price_received increase | defensible | the holders receive the domestic price on the quota tonnes; the table gives the same gain as share value (C-5) and as the division of the gap (section 7, DM-4) |
| taxpayers; recipients.other_spending; taxpayers.future resources_available_other_uses at_least_one_decrease | defensible | OC-3 with OC-1: general budget, no tax named, so the payers are a group. C-29 signs taxpayers alone on A-22 (the budget is raised); a sign-form difference, not a contradiction |

No engine row contradicts the example. No reported row is outside both the table and a defensible reading.

## Table rows

| Row | Produced? | Reason |
|---|---|---|
| C-1 quota_holders, exporters.foreign quantity_traded decrease | no | naming and missing role: bound role `importers`, no base-period subclass; foreign sellers have no quota role (OC-4 is not encoded for quotas) |
| C-2 growers.beet net_price_received increase | yes | |
| C-3 buyers.sugar price_paid increase | yes | |
| C-4 growers.beet quantity_supplied increase | yes | |
| C-5 quota_holders asset_value increase | yes | |
| C-6 quota_holders imports increase (announcement) | no | missing rule: RS-8 is not encoded for quotas |
| C-7 importers.prospective entry_rate decrease | no | missing rule: SB-4 with EN-6 for tradable rights; `entry_rate` only under `seller_cap` |
| C-8 manufacturers quantity_substitute increase | no | missing rule/role: RS-1 for quotas |
| C-9 manufacturers.tradable reclassification increase | no | missing rule: RS-5 for quotas (`definition_line` inert) |
| C-10 manufacturers.tradable quantity_supplied decrease | no | missing rule: RS-14, RS-4 for quotas (`downstream` unread) |
| C-11 households.varnholt cross_border_purchases increase | no | missing role: RS-4 neighbour/mobile buyer for quotas |
| C-12 growers, quota_holders, manufacturers lobbying_effort increase | yes (part) | holders only |
| C-13 sweetener_users price_substitute increase | no | RS-1 for quotas |
| C-14 sweetener_makers quantity_supplied increase | no | RS-1 with LW-4 for quotas |
| C-15 landowners.beet asset_value increase | no | missing record fact (no landowners in section 1) and rule: SB-4 for owners, as TX-7 has |
| C-16 households price_paid (local goods) increase | no | RS-14 for quotas |
| C-17 manufacturers.tradable employment, hours_worked | no | RS-14, RS-6, RS-4 for quotas |
| C-18 refiners.port quantity_supplied decrease | no | CR-9 input chain: `related` not read for quotas |
| C-19 refiners.port employment, hours_worked | no | RS-6 (as C-18) |
| C-20 ostria.sellers quantity_traded increase | no | RS-4, RS-9 for quotas: no neighbour role |
| C-21 retailers.varnholt quantity_traded decrease | no | same |
| C-22 ostria.sellers quantity_supplied increase | no | RS-4 for quotas |
| C-23 exporters.calvar quantity_supplied decrease | yes | name mapped to the default `export_industries` |
| C-24 growers.beet investment_target increase | no | TS-2: `renewable` read only by tariff rules |
| C-25 buyers.sugar, exporters.foreign quantity_traded decrease | yes (part) | buyers only |
| C-26 buyers.field_crops quantity_traded decrease | no | OC-1 with LW-4: no rule or role |
| C-27 buyers.sugar resources_available_other_uses decrease | yes | |
| C-28 quota_holders, importers.prospective compliance_cost increase | no | OC-2 not encoded |
| C-29 taxpayers resources_available_other_uses decrease | no | sign form: engine gives the OC-1 payer group (at_least_one_decrease) |
| C-30 workers.beet_factories employment, hours_worked at_least_one_increase | no | `domestic_seller_worker_actor` unread for quotas |
| C-31 refiners.port capital_stock_target decrease | no | RS-6, TS-1 (as C-18) |
| C-32 manufacturers.tradable compliance_cost increase | no | OC-1, CR-8c for quotas (as C-9) |
| C-33 exporters.calvar employment, hours_worked | yes | name mapped; group of RS-6 form from TX-8 |
| C-34 officials.enforcement enforcement_cost increase | yes | |

By reason: all of C-2 to C-5, C-23, C-27, C-33, C-34 are the core EN-6 chain (quantity, price, domestic sellers, rights value, TX-8, enforcement cost) and match the table in sign. Everything the rules miss is a second-order or side chain that the tariff rules already encode for tariffs but that is not wired to `import_quota`.

## General gaps

Ranked by table rows added or fixed. Each is a pattern-level change, not a WE-014 fact.

1. **An import quota should inherit the tariff rule set, not just TX-7 and TX-8** (EN-6 as widened "names the gain to domestic sellers of a good whose imports are restricted, as TX-7 does for a tariff"). Quota records carry the same role fields (`domestic_seller_owner_actor`, `domestic_seller_worker_actor`, `foreign_seller_actor`, `downstream`, `neighbor_actor`/`mobile_buyer_actor`, `renewable`, `definition_line`, `relief_applicant_actor`) and the tariff questions already exist; `_en_facts` and `_en_specs` ignore them. Wiring them gives, from patterns already encoded: OC-4 on foreign sellers (C-1 part, C-25 part), SB-4 for the factor owners (C-15), TS-2 for review (C-24), CR-9/LW-4 for domestic workers (C-30), RS-14 with RS-6 and RS-4 for downstream users (C-10, C-16, C-17), RS-5 for the definition line (C-9, C-32), RS-4 for border buyers and neighbours (C-11, C-20, C-21, C-22). Up to 13 rows, most of them without a new rule. (Section 1 names no landowners, beet workers or sweetened-goods makers, so some of these also need the parser to find the roles; the neighbours, the definition line, the review and the foreign sellers are in the text.)
2. **RS-1 (substitutes) for any restriction on a good** (C-8, C-13, C-14): buyers turn to unrestricted substitutes, whose price and output rise. It is encoded for tariffs and licensing (`lic_substitute`); a quota is the same pattern with `en_buyer` and a substitute-sellers role (`substitute_seller_actor` exists for subsidies). 3 rows.
3. **CR-9 input chains for the sellers of a restricted good's input** (C-18, C-19, C-31): the refineries lose throughput because raw cane is their input. `related` (kind input) is read for taxes and subsidies only; reading it for quotas, with RS-6 and TS-1, gives 3 rows. The parser would need the refineries from the text, which it has.
4. **RS-8 for rights allocated on past activity** (C-6): an allocation by imports in a base period that ends after the announcement pulls the activity into the window. A quota with `announcement_window` and a `base_period_allocation` fact (or a question) would sign the incumbents' quantity increase in the window. 1 row; the announcement flag is already set and inert.
5. **SB-4/EN-6 for entry under tradable rights** (C-7): where the cap is on quantity and rights are `transferable`, a new seller must buy or lease shares, and the share price carries the expected rent, so entry falls. `entry_rate` is now signed only under `seller_cap`. 1 row.
6. **OC-2 for registering and trading rights** (C-28): a compliance cost for holders and entrants whenever rights are transferable and registered. Absent in WE-067 too (C-28 there), so it is a general OC-2 gap. 1 row.
7. **OC-1 sign form** (C-29): with a general budget that is stated to rise, the table signs `taxpayers`; the engine signs the payer group. This is a convention difference between the handbook (A-22 names taxpayers) and the rule (group unless a tax is named). Either the example's row should be a group or the rule should sign `taxpayers` alone when `enforcement_budget_raised` holds. 1 row, and a point for the catalog rather than the engine.
8. **OC-1 with LW-4 for resources drawn into the protected sector** (C-26): the crops forgone. Needs a role for the buyers of the other goods the land and labor would have produced; the text does not name it. 1 row, low priority.

Not a gap, but a note on roles: the table's `quota_holders` is a subclass (base-period importers) of the bound role `importers`. The engine's `importers quantity_traded decrease` is sound and covers it; matching subclass names to parent roles by prefix in the harness, as for `.served`/`.unserved`, would score C-1 in part.

## After the rule changes (second commit)

General fixes from the five out-of-sample runs on licensing and quotas (`rules/licensing.lp`): buyers of the unlicensed or unrecorded trade have their own role (`informal_buyer_actor`), so RS-3 and RS-10 fall on them, not on every buyer; trainers' demand is ambiguous where the training was already common (`training_common`, CR-4b with CR-12b); a price fixed by a rule in force without the measure (`price_fixed`) withholds the price rows and signs excess demand (PC-1); an import quota takes the tariff chains (EN-6: as under TX-7). Rows produced: 11 of 34 (was 10): C-24 (the growers invest on expected renewal, TS-2, through the tariff chain). The record names no downstream users, owners or workers, so RS-14, SB-4 and the labour groups stay unproduced; the tariff chain also adds reshaping into blends (RS-5) and the growers' lobbying, defensible rows not in the table. WRONG: 0.
