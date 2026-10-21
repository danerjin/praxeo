# WE-006 expand loop, blind run: notes

Read only section 1 of the example and the ID / Statement / Type / p columns of its assumption table. Sections 2 to 9, the "If false" and "Evidence" columns, the report, the consequence list, corrections, gaps, `handbook/05_examples_core/` and the existing files under `cases/we006_coralia/` and `tests/` were not opened. `policy.txt` is section 1 verbatim.

Result: DONE in 3 rounds, 12 nodes, 24 proposed facts, 16 questions (all 16 answered from the table, none judged).

## Seed (`seed.json`)

Only the policy's own facts (CR-1):
- Three exchanges, all with the cap held below (K1, "may not exceed 110%"): `e_local` (buyers.local from sellers.local), `e_outside` (buyers.local from sellers.outside; the text binds "sellers from outside the area selling there and online sellers delivering there"), `e_rooms` (guests.local from sellers.lodging; "hotel, motel and short-term rental rooms"). Unsatisfied side: buyers.unserved / guests.unserved. Criteria of the scarce side: wait_time, search_cost, allocation_by_non_price_criteria (the generic CR-6 group; no premise).
- `held` premises: A-1 (binding) and A-3 (enforcement). `transfers` (CR-8b) rest on A-1. `compliance` for the three bound seller classes. `enforcers`: officials.enforcement (K3). `fixed_budget`: A-21 ("Funded from the Attorney General's budget", fixed within the year); no `funded` fact because the text names no new payers. `announced` k1 with A-14 (standing law, applies on every declaration).
- Not in the seed, because section 1 has none: `charges` (the K3 penalty is a sanction for violating the line, not a payment attached to trading), `moves`, `backstops`, `discretion`, `means`, `early_price`.
- Seed assumptions: a1, a3, a14, a21 (same numbering as the table).

## Round 1 (depth 1), 8 nodes, 16 questions

Pending nodes: buyers.local, buyers.unserved, guests.local, guests.unserved, officials.enforcement, sellers.local, sellers.lodging, sellers.outside.

Proposals (each cites the sentence or assumption it rests on in `proposals.json`):
- sellers.local (6): adjust_one quantity_supplied (A-6, "not required to sell"); outside informal_activity (A-10); alt inventory_held (A-6, "can store durable goods"); alt reclassification (A-9); timing carry_over inventory_held (A-17, announced via A-14); stake (A-20).
- sellers.outside (4): adjust_one quantity_supplied (A-4); outside informal_activity (A-10); alt "sell elsewhere", measured as quantity_traded of a new class buyers.unaffected (A-4 and A-5: elsewhere at normal prices, and the emergency-trip costs are not accepted under K2); alt reclassification (A-9, "online sellers").
- sellers.lodging (4): adjust_one quality_per_unit falling on guests.local (A-7); outside informal_activity (A-10); alt reclassification (A-9); stake (A-20).
- buyers.local (1): timing bring_forward quantity_traded (A-15: households expect the standing Act to apply in future storms, so they buy less before the declaration).
- buyers.unserved (6): criterion margins allocation_by_non_price_criteria and wait_time (A-18), search_cost (A-19); alt quantity_substitute (A-13); alt travel_time (A-12); link to new class sellers.inland quantity_traded as a substitute (A-12; "inland counties ... not declared").
- guests.local (1): alt turnover (A-8; the favored guest checks out less).
- guests.unserved (1): link guests.unserved quantity_traded -> input -> new class sellers.repair_outside quantity_supplied (A-11 and A-22; the Act's text assumes repair is not covered but outside crews need rooms).
- officials.enforcement: empty. The engine derives enforcement_cost both up (K3 enforcement) and down (fixed budget, A-21); settling that needs a dominance premise that no assumption statement supplies.

Answers: all from the table. A-15 0.55, A-18 0.8, A-19 0.75, A-13 0.8, A-12 0.7, A-8 0.85, A-11 0.6, A-22 0.75, A-6 0.55, A-10 0.6, A-9 0.6, A-17 0.9, A-20 0.6, A-7 0.75, A-4 0.9, A-5 0.75.

## Round 2 (depth 2), 3 nodes, 0 questions

- buyers.unaffected (quantity_traded up): empty. The text gives nothing further about inland or Hallorn buyers.
- sellers.inland (quantity_traded up): empty. The knock-on I would want (demand from the coast raises inland prices) cannot be written as a link, see below.
- sellers.repair_outside (quantity_supplied down): one same_act link to a new class buyers.repair_local quantity_traded (the service the crews do not supply is the service locals do not receive). No premise.

## Round 3 (depth 3), 1 node, 0 questions

- buyers.repair_local (quantity_traded down): empty. Depth limit reached.

## Final engine output

See `final_output.txt` (and `situation.json`). 48 reported lines. Highlights: price_paid down and resources up for buyers.local and guests.local; excess_demand up and quantity_traded down for the unserved; the criteria group up (plus wait_time, search_cost, allocation each singly); sellers' net_price_received, quantity_traded and resources down, compliance_cost, informal_activity, reclassification up; lobbying up for local and lodging sellers; inventory_held up (emergency window) and down (announcement window) for local sellers; buyers.local purchases down in the announcement window; enforcement_cost reported both up and down (left unresolved).

## What the format could not hold

1. Each actor is visited once. Effects that reach an already-visited actor in a later round (sellers.local inventory_held, buyers.unserved quantity_substitute and travel_time, guests.local turnover) never trigger a new proposal for that actor.
2. Several seller classes under one cap need one exchange each; the unserved buyer class is repeated across exchanges. The rooms exchange's unsatisfied side is generic: section 1 gives no criteria for rooms, so no room-specific criterion margin could be proposed.
3. No link relation says "more demand from the coast raises the price in the unaffected market" (price pressure from a quantity change). The inland and Hallorn side stops at quantity_traded.
4. K2 (cost defense) is an exception that shapes the line, not a component with its own effect; it appears only as a premise (A-5) on the outside sellers' alternative.
5. The base period (average of the 30 days before the declaration) and forecast days: sellers could raise prices before the declaration to lift the base. `early_price` is for renewals under an announced line, so this was not proposed.
6. Renewal in 30-day steps and the expectation of renewal (A-16, p 0.4) have no field; the format has no duration.
7. The assumption table's statements A-6 and A-20 hold several concepts each; they were reused verbatim to get p from the table, which breaks the one-concept-per-premise rule.
8. An `adjust` margin names the party it falls on as `actor`, but the party that controls it is the node that must propose it (hotels propose a margin on guests.local). The `split()` keying by `actor` would put it at the wrong node.
9. Timing-window effects (stockpiling, buyers' earlier purchases) do not propagate through links, by design; no consequence beyond the window is reached.
10. The class repair crews is outside the Act's coverage per the text; the chain through it rests on A-11 and A-22 alone, and the engine reports it as a reached effect with no flag that the market is uncovered.

## Revision r2 (engine at a54331b: revisits, CR-4 for price movers, `supply_price`)

Rerun with the round-1 files unchanged: still DONE in 3 rounds, 16 questions, same 48 consequences (revisits replayed the existing proposals, duplicates dropped; no node was listed as pending).

One revision, from section 1 only ("The inland counties ... are not declared", A-12 inland stores reachable): at sellers.inland, a `supply_price` link from sellers.inland quantity_traded to a new class buyers.inland price_paid. Premise: "Supply of covered goods in the inland counties is slow to respond in the first weeks." This is not in the assumption table; p = 0.6 was JUDGED by me (roads and stock are fixed in the first days; no figure in section 1). It adds 1 question (17 in all) and the consequence buyers.inland price_paid increase (49 consequences in total).

buyers.inland then became a node; I proposed nothing for it (CR-4 now fires for it as a price mover, but no assumption names an alternative of inland buyers; a premise would have been invented). The new rules otherwise changed nothing here: the burdened and favored parties were already choosers through the held exchanges.

Still not holdable: limits 2 (one exchange per seller class), 4 to 10 above; limit 1 and limit 3 are now resolved by the engine.

Final: DONE in 3 rounds, 17 questions (16 from the table, 1 judged), 49 consequences; see `final_output.txt`.
