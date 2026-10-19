# Out-of-sample run of the quota rules (EN-6, EN-12, EN-13) on WE-054 (Wexcombe Airport Night Curfew and Slot Order)

Rules as they were at commit a0b2aea (`licensing.lp`: EN-6 from the catalog text; EN-12 and EN-13 written from WE-028 only). Handbook catalog 1.1 for the rules, WE-054 as corrected under 1.0. Nothing under `praxeo/` was changed. Record: `record.json`, four components. K2 is the `quota` (the daytime cap; bound `airlines.history`, buyer `travelers.wxi`, right holder `airlines.history`, `transferable`, `allocation_by_history`, `base_period_after_announcement`, entrant `airlines.prospective`, worker `workers.wxi`, `announcement_window`, `renewable`, `field_contested`; trading K4, enforcement K6 and the allocation formula K3 are folded in as flags and source sentences). K1 (the curfew) is a `prohibition` bound on `operators.night`, protected `neighbors.wxi`; K3 and K5 (freed slots) are `rights_allocation` components. No rule reads `prohibition` or `rights_allocation`, so K1, K3 and K5 produce no consequences and no questions. Not set: `wider_market` (airfares are not set in a wider market), `price_fixed`, `general_budget` (costs are recovered from airport charges). U1 is recorded with its two readings and no `reading_fields`: no Component field expresses a dispensation for late-running flights, so the engine runs the same facts under both readings. Answers: `answers.json`, 10 questions; 9 have a matching WE-054 assumption (A-1, A-2, A-15, A-3, A-10, A-4, A-5, and A-32 twice), one (`k2.evasion`) has none and was judged from the text (p = 0.15; A-14 is about operators who are caught and pay in the curfew). Run: `python3 -m praxeo cases/we054_wexcombe --out cases/we054_wexcombe/sample_run`; verifier and citation problems are empty. Key: (actor class, variable, sign, window). The table's "in the base seasons" cells are the announcement window. The test is `tests/test_oos_we054.py`.

Summary: the table has 52 rows (C-1 to C-52). The engine reports 20 consequences (22 keys: the workers entries are two groups of two variables); 4 more are derived but not reported (the informal activity of the airlines and three evasion consequences for travelers, because `evasion` fell below the cut-off). Rows produced by key: 12 of 52 (C-3, C-4, C-12, C-16, C-19, C-20, C-21, C-25, C-37, C-39, C-43, C-49). Of these, C-4, C-12 and C-16 are for only some of the classes the row names. Rows not produced: 40. Three more (C-2, C-5, C-6) are produced in substance under a different variable name and count as not produced by key. Engine rows classified WRONG: 2.

## Engine rows (reported)

| Engine row | Class | Why |
|---|---|---|
| airlines.history asset_value increase | in table | C-3 (EN-6 with SB-4 and `expected_to_last`, A-3; the table has EN-12's windfall and CR-7c) |
| airlines.history right_lease_price increase | in table | C-4, from EN-13 (the lease price of the right, medium horizon). `operators.night` and `airlines.prospective` have no role |
| airlines.history number_of_sellers decrease | in table | C-12 from EN-13 (`values_differ`, `trade_cheap`: A-10, A-4). `airlines.prospective` has no role. The derivation is the 0.9 one (consolidation from the initial allocation); the 1.0 table rests on blocked entry and whole-holding exits |
| airlines.history lobbying_effort increase | in table | C-16 (EN-5/RS-7, A-15), for the holders; the entrants have no lobbying rule |
| airlines.prospective entry_rate increase, announcement | in table | C-43 (EN-12 race, A-5 as `allocation_known`; the table's own premise is A-29) |
| travelers.wxi price_paid increase | in table | C-19 (EN-6). The table also needs the response argument (A-9, A-35, CR-12); the engine signs the price with no premise on the other responses |
| travelers.wxi quantity_traded decrease | in table | C-20 (same) |
| airlines.history net_price_received increase | in table | C-21 (EN-6 without `wider_market`). The table derives it through EN-2 1.0 (cost-recovery charges, A-13, A-26 `ambiguous` if the scarcity premium is small); the engine has no charge chain and gives no ambiguous branch |
| travelers.wxi resources_available_other_uses decrease | in table | C-49 (CR-8b mirror of the price rise) |
| workers.wxi employment, hours_worked at_least_one_decrease | in table | C-25 by key. The engine's chain is EN-13 (the workers of holders who lease out), the table's is the night sort and RS-6 (A-6, A-25): same class and sign, different mechanism |
| officials.enforcement enforcement_cost increase | in table | C-37 and C-39 by key. Tier B here, Tier A in C-37; the engine has no noise-office offset (C-38), so C-39 is produced without its Tier C chain |
| airlines.history quantity_traded decrease | defensible | EN-6; the same fact as C-2, which the table writes as quantity_supplied |
| airlines.history quantity_traded increase, announcement | defensible | EN-12; the same fact as C-5 (quantity_supplied) |
| airlines.history resources_available_other_uses decrease, announcement | defensible | EN-12 with CR-8c, the means used up in the race; the table has compliance_cost (C-6) |
| airlines.history investment_target increase, announcement | defensible, weak | EN-12 text ("investment in it"); the example speaks only of added flights (A-5) |
| airlines.history asset_value increase, announcement | defensible | EN-12 with CR-7c; the table has the slots' value (C-3) with no window |
| airlines.history capital_stock_target decrease | defensible, weak | EN-13 long run; not in the table. Aircraft move to other airports, so a fall in the WXI fleet is not derived against no order |
| workers.wxi employment, hours_worked at_least_one_increase, announcement | defensible | EN-12 crews; employment follows movements (A-25). Not in the table, and the group's two windows are not combined (CR-12g), as the table does for the race and the cap |
| airlines.history quantity_supplied increase | **WRONG** | EN-13's "quantity per remaining user increases". WE-054's corrections drop this claim: against no order the cap lowers total movements, so per-user quantity has no sign |
| airlines.history lobbying_effort ambiguous | **WRONG** | RS-7 Unless (`field_contested`, `contested_otherwise`) attached to the slot holders. The table keeps the holders' lobbying an `increase` (C-16: slots exist only under the order) and gives the contested question to the residents (C-17) and the night operators (C-46), neither of which the quota rules reach |

## Table rows

| Row | Produced? | Reason |
|---|---|---|
| C-1 night operators quantity_supplied decrease | no | missing rule: K1 is a `prohibition` and no rule reads it |
| C-2 daytime movements decrease | no (in substance) | variable: the engine writes quantity_traded for airlines.history |
| C-3 slots asset_value increase | yes | |
| C-4 right_lease_price increase | yes (part) | holders only |
| C-5 race: daytime movements in the base seasons | no (in substance) | variable: the engine writes quantity_traded |
| C-6 compliance_cost of flights added | no | variable: EN-12 signs the means used up, not compliance_cost |
| C-7 night movements at Pellham | no | missing rule and roles (RS-4, RS-1, RS-16 for a prohibition; integrator, Pellham) |
| C-8, C-9 night operators into the shoulders (06:00 to 07:00, 22:00 to 23:00) | no | missing rule and role: RS-8 per window for the curfew; U1 cannot be set |
| C-10 night operators buy or lease slots | no | missing rule and role: EN-13 signs the sellers' quantity traded, not the buyers' purchases; no lessee role |
| C-11 unit_size increase | no | missing rule and question: RS-21 for larger aircraft under a movements cap (A-8) |
| C-12 number_of_sellers decrease | yes (part) | holders only |
| C-13 entry_rate decrease | no | missing rule: EN-6 signs entry only for `seller_cap`; EN-13 1.0 (blocked entry) |
| C-14 legal_breach increase | no | missing rule: RS-3 for a prohibition |
| C-15 reclassification, per reading | no | case-specific provision: U1 on K1; no rule |
| C-16 lobbying_effort increase | yes (part) | holders only |
| C-17, C-46 residents and night operators lobbying ambiguous | no | missing rule and roles; the contested-field row lands on the holders (WRONG row above) |
| C-18 integrator asset_value | no | missing rule and role: CR-7c; K1 has no rules |
| C-19, C-20, C-21 | yes | without the response argument (CR-12) and the charge chain (EN-2) |
| C-22 travel_time | no | missing rule and role: RS-4, CR-9, CR-3a |
| C-23, C-24 Pellham trips and movements | no | missing rule and role: RS-1, RS-16, CR-9; the substitute question is for licensing and import quotas only |
| C-25 workers.wxi group | yes | by key; different mechanism |
| C-26 workers.pellham | no | missing rule and role: OC-5, CR-9 |
| C-27 to C-30 home values at both airports | no | missing record fact and rule: CR-9 over `proximity` and CR-7c; the record has no proximity relation, no neighbors role for a quota |
| C-31 shippers quality_per_unit | no | missing rule and role: CR-9, CR-4 |
| C-32 WAA charges | no | missing record fact and rule: the cost-recovery charge method is an existing rule without a field; PC-15, CR-9 1.0 |
| C-33 concessions | no | missing record fact (section 1 does not name concessions) and rule: RS-12 for a movements cap |
| C-34, C-35 lessors' and lessees' means | no | missing rule: CR-8b for the two sides of a sale or lease (as in WE-028 C-34, C-35) |
| C-36 airlines' operations as a whole ambiguous | no | missing combiner: CR-12b over slot value and scarcity |
| C-37 enforcement_cost increase | yes | |
| C-38 noise office cost decrease | no | missing rule: CR-9 over proximity |
| C-39 total enforcement cost | yes | by key, without the noise-office offset |
| C-40 compliance_cost (slot paperwork) | no | missing rule: OC-2/CR-8c for quotas |
| C-41 night services that stop | no | missing rule: OC-4/CR-5a |
| C-42 penalty receipts | no | missing rule: OC-3 with CR-8b |
| C-43 entry in the base seasons | yes | |
| C-44 K5 claim asset_value | no | missing rule: `rights_allocation` (freed slots reissued by priority) has none |
| C-45 night businesses as a whole ambiguous | no | missing rule and role: CR-12b |
| C-47 off-peak fares in the base seasons | no | missing rule: RS-13/CR-9; EN-12 signs no price |
| C-48 road haulage | no | missing rule and role: CR-9, LW-10 |
| C-49 travelers' means | yes | |
| C-50 penalty payers' means | no | missing rule: CR-8b |
| C-51 national parcel price | no | missing rule and role: EN-6 1.0 with CR-9 for the curfewed good's national buyers |
| C-52 WAA fund_balance | no | missing rule: OC-1/CR-8b; funding from charges is not `general_budget` |

## General gaps

Ranked by the number of table rows each would add or fix.

1. **Rules for a prohibition (EN-7 with RS-3, RS-8, RS-4, RS-1, RS-16, CR-9) and roles for the displaced.** The curfew is one `prohibition` component and nothing reads that instrument. A ban on a time window cuts the activity in it (CR-1), shifts it to the adjacent windows (RS-8, per window), to a neighbouring jurisdiction without the ban (RS-4, RS-16) and into breach where a penalty is cheaper (RS-3), and loses the work and complements tied to it (CR-9). It would add C-1, C-7, C-8, C-9, C-14, C-18, C-22, C-23, C-24, C-26, C-31, C-41, C-48, C-50 and C-51 (up to 15 rows); the roles are the displaced operators, their neighbour-jurisdiction rivals and the travelers. The record fields `neighbor_actor` and `substitute_seller_actor` exist for ceilings and subsidies only.
2. **CR-9 and CR-7c over a proximity relation (homes, noise office).** C-27 to C-30 and C-38 run through a `proximity` relation between the activity and home values. The record has no way to say that the effect of an activity reaches the value of nearby assets, and `neighbors.wxi` has no rule at all under a quota or prohibition. A related-market kind `proximity` read by CR-9/CR-7c would add up to 5 rows, and with the OC-3 offset on the enforcer fix C-39's chain.
3. **Both sides of a trade in rights, and receipts and costs of a quota (CR-8b, OC-2, OC-3, OC-1 for quotas).** EN-13 signs the lease price and the sellers' quantity traded but not the lessors' receipts, the lessees' outlay, the buyers' purchases, the slot paperwork, the penalty receipts or the WAA's balance: C-10, C-34, C-35, C-40, C-42, C-50, C-52 (7 rows; WE-028 C-34, C-35, C-43 are the same gap). A lessee role next to `right_holder_actor` is also needed (the night operators are lessees, C-8 to C-10).
4. **Variable names for the capped activity under EN-6 and EN-12.** EN-6 and EN-12 write the sellers' output as `quantity_traded`; the table writes `quantity_supplied` for sellers who cut their own movements and `compliance_cost` for the resources used up building history (CR-8c, C-6). WE-028 wrote `quantity_traded` and `resources_available_other_uses`. A convention is needed (the catalog's EN-12 says "activity" and "resources used up"). Aligning the engine to the table would add C-2, C-5 and C-6 (3 rows).
5. **Combiners under CR-12b for a holder's operations as a whole.** C-36 and C-45 (`ambiguous`) are totals over the slot value and the scarcity rent, and over the claim and the lost night business. The engine signs the parts only (2 rows, with the roles of gap 1 for C-45).
6. **Repair the two WRONG rows.** (a) EN-13's "quantity per remaining user increases" is dropped in WE-054's corrections (the 1.0 baseline clause: against no order, only the fall in the number of users is derived). The encoded effect `quantity_supplied increase` (and `capital_stock_target decrease`, which rests on it) should wait for a premise that total activity is not cut by the cap (a cap that does not bind per user), or be dropped as the handbook did (EN-13 "Baseline (1.0)"). (b) RS-7's Unless is applied to every lobbying conclusion of the component, including the holders' lobbying for slots that exist only under the order (CR-4 1.1: lobbying over provisions that exist only under the measure stays an increase). The ambiguous row belongs to the parties of the contest (here the residents and the night operators, C-17 and C-46), which needs the roles of gap 1 and a record field for who is on each side of the contested field. Fixing (b) with those roles would add C-17 and C-46 (2 rows) and remove one WRONG row; fixing (a) removes the other.
7. **Rules that need a premise the record cannot hold.** RS-21 for larger aircraft under a cap in movements (C-11), entry onto a capped market where rights must be bought or leased (C-13; EN-6 signs entry only for `seller_cap`), RS-13 for off-peak fares in the race window (C-47), and the PC-15 charge method (C-32) are each one row; U1 (a dispensation for late flights, C-9, C-15) cannot be written as `reading_fields` because no Component field expresses it. A generic field for an exception window on a prohibition would let U1 set the readings.
