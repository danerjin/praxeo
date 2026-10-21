# Out-of-sample run of the price-floor rules on WE-008 (Velmora Dairy Stabilization Act)

Rules as they were at commit 5944604 (price-floor rules written from WE-009 only). Nothing under `praxeo/` was changed. Record: `record.json`, one `price_floor` component (K1: raw milk, a good, so `contract_kind` is `sale`; bound `plants.commodity`, sellers `farmers.velmora`, output buyers `consumers`, asset owners `factor_owners.specific`, `definition_line`, `announcement_window`, `general_budget`, `state_buys_surplus`). K2 (the Board's purchase) and K3 (disposal) are folded into K1 through `state_buys_surplus` and `outlay_actor`, and K4 (enforcement) through `enforcer_actor`: the handbook treats K2 as a `per_unit_subsidy` to K1, but recording it as a second component would count the Board's stocks and the taxpayers' cost twice. `future_taxpayer_actor` is null, since the example's payer is `taxpayers`. No `excluded_actor`, `mobile_buyer_actor` or `substitute_seller_actor`: no class in the example fits those roles (see pattern 3). U1 (whether a farm that moves in qualifies at once) changes no field the rules read, so `unclear` is empty. Answers: `answers.json`, ten questions. Probabilities from the assumption table of WE-008: `binding` (A-1), `evasion` and `reshaping_pays` (A-6), `can_organize` and `sellers_organize` (A-14), `expected_to_last` (A-2). Judged from the text, with the reason in each rationale: `enforced`, `cost_not_offset`, `rivals_bound` (no, 0.15), `expected_ahead`. Run: `python3 -m praxeo cases/we008_velmora --out cases/we008_velmora/sample_run` (verifier and citation problems empty). Key: (actor class, variable, sign, window); the table's "Dairy Board" is matched to `officials.enforcement`.

Summary: the table has 28 rows (C-1 to C-28; the two unnumbered earnings rows are not compared). The engine reports 13 consequences (of 14 derived; the consumers' price is below the cut-off), which give 14 keys (the OC-1 entry is a group of two actor classes). Table rows produced by key: 6 (C-1, C-10, C-11, C-13, C-20, C-23); C-11 in part (the plants only), C-13 in full (both `farmers.velmora` and `plants.commodity`). Rows not produced: 22. Engine rows classified WRONG: 3.

## Engine rows (reported)

| Engine row | Class | Why |
|---|---|---|
| farmers.velmora net_price_received increase | in table | C-1 (PC-9, the floor binds) |
| plants.commodity compliance_cost increase | in table | C-10 (OC-2) |
| plants.commodity reclassification increase | in table | C-11 (RS-5 from `definition_line` and `reshaping_pays`); `farmers.neighbors` has no role |
| farmers.velmora lobbying_effort increase; plants.commodity lobbying_effort increase | in table | C-13 (RS-7). The engine's rule is about the bound buyers' and the sellers' lobbying over the floor; the key matches, the direction (to keep and raise it) is not in the key |
| officials.enforcement inventory_held increase | in table | C-20 (SB-9) |
| officials.enforcement enforcement_cost increase | in table | C-23 (OC-3) |
| plants.commodity price_paid increase | defensible | the floor raises what every Velmora plant pays; the table gives it to the specialty plants (C-6), and section 5 says commodity plants pay $21 too |
| officials.enforcement subsidy_outlay increase | defensible | SB-9's outlay for the Board's purchases (K2 is treated as a `per_unit_subsidy`); the table gives stocks (C-20), taxpayers' cost (C-22) and audits (C-23) |
| taxpayers, recipients.other_spending resources_available_other_uses at_least_one_decrease | defensible | OC-1 as a group; the table gives taxpayers a plain decrease (C-22) |
| **plants.commodity informal_activity increase** | **WRONG** | RS-3 from the evasion premise. Section 6: RS-10 applies only to the false-origin trade, which takes place inside legal plants; "no informal market for milk is expected". The table records the evasion as reclassification (C-11) |
| **plants.commodity investment_target decrease** | **WRONG** | TS-2: the bound buyers' planned investment falls when the floor is expected. Here the Board buys their product at prices that cover the floor, and C-9 signs commodity plants' investment up |
| **factor_owners.specific asset_value decrease** | **WRONG** | SB-4 as written is for assets of the buyers (employers). The asset owners here own the sellers' land and barns, whose value rises with the floor (C-18) |

## Table rows

| Row | Produced? | Reason |
|---|---|---|
| C-1 farmers.velmora net_price_received increase | yes | |
| C-2 Dairy Board quantity_demanded increase | no | missing rule: the state_buys branch signs stocks and outlay, not the Board's purchases |
| C-3 farmers.velmora quantity_supplied increase | no | missing rule: no sellers' supply response (SB-2, LW-4) |
| C-4 farmers.velmora investment_target increase | no | missing rule: sellers' investment (TS-1); TS-2 is written for the buyers |
| C-5 farmers.velmora number_of_sellers increase | no | missing rule |
| C-6 plants.specialty price_paid increase | no | role: one bound_actor; the record uses commodity plants (the engine signs the same variable on them) |
| C-7 plants.specialty quantity_supplied decrease | no | role, and missing rule: RS-14 for exempt rivals (quantity effect) is not encoded for floors |
| C-8 plants.market quantity_substitute increase | no | role: another class of bound buyers, who can use out-of-state milk |
| C-9 plants.commodity investment_target increase | no | missing rule (SB-2 with CR-9); the engine's TS-2 row says the opposite |
| C-10 plants.commodity compliance_cost increase | yes | |
| C-11 plants.commodity, farmers.neighbors reclassification increase | yes (part) | plants only; `farmers.neighbors` has no role |
| C-12 farmers.prospective entry_rate increase | no | missing rule: RS-4 widened, SB-5, and a prospective-sellers role |
| C-13 farmers.velmora, plants.commodity lobbying_effort increase | yes | |
| C-14 consumers price_paid increase | no | missing rule: SB-9 withdrawal into stocks. The engine derives consumers' price_paid through RS-14, but `rivals_bound` is answered no (0.15), so it is unreported |
| C-15 farmers.neighbors net_price_received increase | no | missing rule (PC-8 for a floor) and role |
| C-16 farmers.neighbors quantity_supplied increase | no | missing rule (PC-8, LW-4) and role |
| C-17 input_suppliers quantity_traded increase | no | missing rule: SB-3; `input_supplier_actor` is not a floor role |
| C-18 factor_owners.specific asset_value increase | no | missing rule (SB-4 for the sellers' assets); the engine's row says the opposite |
| C-19 farmers.other_uses quantity_supplied decrease | no | missing rule: SB-3 |
| C-20 Dairy Board inventory_held increase | yes | |
| C-21 sellers.to_food_programs quantity_traded decrease | no | missing rule: SB-9 disposal by donation |
| C-22 taxpayers resources_available_other_uses decrease | no (sign form) | the engine's group sign is `at_least_one_decrease` |
| C-23 Dairy Board enforcement_cost increase | yes | |
| C-24 consumers, dairy sellers quantity_traded decrease | no | missing rule: OC-4 with a state that buys (`fl_fewer` is switched off under `state_buys`) |
| C-25 farmers.neighbors quantity_supplied ambiguous | no | combiner, and no rules for the two chains |
| C-26 consumers price_paid ambiguous | no | combiner, and no rules for the two chains |
| C-27 workers.dairy employment, hours_worked at_least_one_increase | no | missing rule: SB-3 with CR-9 for the sellers' labour |
| C-28 food_programs resources_available_other_uses increase | no | missing rule: SB-8, SB-9 |

## Patterns for the rule writer

General problems in how floors.lp is written, not patches for this case. Ranked by rows affected.

1. **A floor on a good with the state buying the surplus has only the buyers' and the Board's side (C-2, C-3, C-4, C-5, C-9, C-12, C-17, C-19, C-27; also C-21, C-28).** The `state_buys` branch gives stocks, outlay and the payers. What the sellers do with a guaranteed price (more supply, investment, fewer exits, entrants, input suppliers, labour and land drawn from other uses) is the subsidy chain (SB-2, SB-3, SB-5, LW-4, TS-1, CR-9), and no floor rule reaches it. A floor on a good that the state backs is a subsidy to the sellers, and the floor rules and `subsidies.lp` need a common path from the sellers' higher net price to these responses. Affects 11 rows.
2. **Rules written for a wage floor give the wrong sign when the floor is on a good and the asset or the buyers are protected (WRONG: asset_value, investment_target; C-9, C-18).** SB-4's `fl_capitalized` and TS-2's `fl_invest` take the asset owners and the investors to be on the buyers' side (employers' specific assets, employers' planned investment). For a good, `fl_asset_owner` can sit on the sellers' side (land) and investment can be protected by the state's purchase. The rules need to know which side owns the asset, and TS-2 should not apply to buyers who recover the cost through the state's purchase (`state_buys`). Removes 2 WRONG rows; adds C-18 (with the seller-side rule) and, with pattern 1, C-9.
3. **One `bound_actor`, but the milk case has three classes of bound buyers who respond differently (C-6, C-7, C-8; the price_paid and lobbying rows depend on the choice).** The record picked `plants.commodity`, so the engine's `price_paid` and `compliance_cost` land there and specialty plants (price and output down) and market plants (switch to out-of-state milk) have no role. The substitute and mobile roles are for sellers of a substitute and buyers of the output, not for a second class of bound buyers. A list of bound classes with a flag for each (can substitute the input, protected by a purchase, label-bound) would let the rules sign each separately. Affects 3 rows.
4. **RS-3 informal activity is signed whenever `evasion` holds, but not every evasion is an informal market (WRONG: informal_activity; C-11).** Here the evasion is false certification inside legal plants, which the table records as reclassification and says produces no informal market. The same distinction appears under `practice_ban` for prohibitions. The floor needs a record fact or a question that separates trade outside the law from false labelling of legal trade. Removes 1 WRONG row.
5. **No exempt-rivals branch for RS-14 (C-7, C-14).** `fl_pass` signs a price rise when rivals face the same floor and nothing otherwise. The handbook's other case, rivals not bound, gives a fall in the bound buyers' output (quantity effect dominates) and is encoded for tariffs only. In this run it also meant the consumers' price route (C-14) was gated off by a correct "no". Affects 2 rows.
6. **Neighbors across the boundary have no place in a floor (C-12, C-15, C-16, C-25).** PC-8 widened to floors (buyers switch to unbound sellers, whose price and supply rise) and RS-4's entry across the boundary have no roles (`neighbor_seller_actor`, `prospective seller`) or rules in floors.lp. Affects 4 rows, 3 of which also need a combiner (C-25, C-26).
7. **Fewer units traded is switched off under `state_buys`, but the regional market still shrinks (C-24, C-14, C-26).** `fl_fewer` has `not state_buys` because the surplus does not stay unsold. The example's OC-4 and SB-9 say the quantity traded in the market falls anyway, because product moves into stocks. Affects 3 rows.
8. **SB-9 stops at the Board's stocks (C-21, C-28).** Disposal by donation (substitutes' sales fall, recipients keep money) is not encoded. Affects 2 rows.
9. **The OC-1 group sign again (C-22).** A plain decrease for taxpayers when the budget is open-ended ("sum sufficient") and rises with the task; the engine signs the group. The record has no field for an open-ended appropriation (the same as pattern 7 of the WE-018 run). Affects 1 row.
10. **Lobbying has no direction (C-13).** Two keys match C-13 (lobbying to keep and raise the floor), but the engine's rule is the bound buyers' lobbying over a floor, which for a wage floor is against it. The key does not carry the direction, so a match here does not show the rule right. This concerns the comparison, not the rule.
11. **Combiners (C-25, C-26).** Ambiguous rows that rest on the pairs of chains in patterns 1, 6 and 7; none can be declared until those chains exist.


## After the floor rule changes

General fixes from the floor runs on WE-008, WE-018 and WE-061 (`rules/floors.lp`): a `complier_actor` role for who must comply and can evade when that is not the bound buyers (the retailers who must charge a minimum bag price), with OC-2 and RS-3 on it; `open_breach` for evasion within the legal market (`legal_breach`, not `informal_activity`); under a floor on a good that the state backs by buying the surplus, the long side gains (the sellers supply more, and where the floor is expected to last they invest, more enter and specific assets gain value), and the short side's losses (returns, planned investment, specific assets) are kept to wage floors. The record sets `open_breach` (false certification of origin is a breach by legal plants). Rows produced: 10 of 28 (was 6): C-3, C-4, C-5, C-18. WRONG: 0 (was 3): the informal market, the plants' investment and the assets' fall are gone. One new defensible row: the plants' legal breach (the table records the same act as reclassification, C-11).
