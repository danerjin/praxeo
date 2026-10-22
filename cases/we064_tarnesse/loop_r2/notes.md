# WE-064 Tarnesse 2.9 GHz award: blind expand loop (loop_r2)

Read: section 1 and the assumption table only. Result: DONE in 3 rounds, 21 loop questions (20 from the table, 1 judged), plus 8 premises in the seed (6 from the table, 2 judged). No `off-list:` lines. Files: `seed.json`, `proposals.json`, `answers.json`, `situation.json` (final), `rounds/` (the proposals as added each round), `run.sh`, `fill.py` (fills answers from the table and lists the rest), `add.py`.

## Seed (the policy's own facts, CR-1)
- `e_lic`: licences sold; buyers `licensees`, seller `treasury` (receipts go to the Consolidated Fund, reg. K4; the TCA is the enforcer, `officials.enforcement`). Unsatisfied seller: the treasury (unsold blocks).
- `e_resale`: resale under reg. 14; buyer `licensees.prospective`, seller `licensees.reselling` (a separate class so resale volume does not mix with blocks bought at auction).
- K1 `issued` (premise A-1); reserve price as `held` above (judged premise j1, p 0.15: consultant values M100-200m against M40m reserve, so it does not bind and the engine reports no excess supply).
- K2 build-out as `charge` in kind, `basis: operating` (a cost fixed per licensee), payer buyer, receiver `customers.uncovered`, receipt `quality_per_unit`, premises A-8 (binds) and A-3 (enforced), `quantity_premises` j2 (judged 0.7: households outside the cities value coverage). `moves` on the seller side with A-1 (bids fall by the build-out cost). `penalties` on `licensees.noncompliant` with A-30 (p 0.3, below cut-off, so not reported). `compliance` for licensees.
- K3 cap as `thresholds` (A-17), `licensees.near_threshold`, measure `quantity_traded`.
- K5: `enforcers` (TCA) and `funded` (general_fund).
- `announced` K1-K3 with A-28. U1 as `unclear`: reading U1-b adds component `u1_bar` (`banned` on e_resale); `discretion` for the TCA's consent (reg. 14) applies under both.
- Not used: `capped` (it fixes what sellers may supply; K3 limits buyers' holdings), `terms` (tried first for K3; it made quantity_traded ambiguous for the treasury and licensees although all six blocks are still sold; replaced by `thresholds`), `expires` (licence end 2042 is outside what the premises cover), `qualifies`, `fixed`, `incidence`, `grants`, `means`.

## Round 1 (8 nodes)
- customers.uncovered, general_fund, officials.enforcement: empty (no one else reached).
- licensees: alt K2 `legal_breach` (A-9; drive tests, revocation); alt K1 `investment_target` (A-7, densify less); stake K2 (A-13); links quantity_traded -> capital_stock_target (input, A-4) -> consumers `price_paid` (supply, A-15); compliance_cost and investment_target -> towers `quantity_demanded` (input, no premise, from the site counts); resources -> borrowers.other `interest_rate` (supply, A-27).
- licensees.near_threshold: alts `reclassification` for stakes below the affiliate line (A-5) and for network sharing (A-6); stake (A-13); price links to licensees `price_paid` and treasury `net_price_received` (supply_price, A-17); substitute link to `licensees.entrants` (A-14).
- licensees.prospective: complement link to `licensees.investors` (A-12).
- licensees.reselling: alt with `reading: U1-b` (A-11, company sales or leases outside the ban); asset on the seller side of e_resale (A-10).
- treasury: paid_into general_fund `fund_balance` (A-26).
- Answers: 13 from the table.

## Round 2 (9 nodes)
- consumers: own_price link (a priori). general_fund#2: supply link to interest_rate (A-26). input_suppliers.towers: supply_price to its own `net_price_received` (A-20); input and supply_price to `workers.riggers` (A-22, horizon short); to `sellers.foreign` (input; A-25 price); to `municipalities` `applications`; dominance on `quantity_demanded` increase (A-31, the build-out takes more site capacity than the densification not done). licensees#2: timing K1 `investment_target` bring_forward (A-7 with the announcement, A-28). licensees.entrants: substitute link to `sellers.substitutes` (A-18). licensees.investors: supply_price link to licensees `price_paid` (judged: "The six blocks are all that is offered, whatever the price.", p 0.95, from "Six blocks of 20 MHz"). licensees.reselling#2: stake on u1_bar (A-13). borrowers.other, licensees.near_threshold#2: empty.
- Answers: 5 from the table, 1 judged.
- Revision made within the loop: the riggers `wage_rate` link was first written without a horizon (medium by default), which clashed with the medium-run supply response of round 3; I set it to `short` (A-22 is about the short run) and added the medium link later.

## Round 3 (9 nodes, depth limit)
- municipalities: stake on K2 (A-13). sellers.substitutes: yield link to `return_on_capital` (A-19). workers.riggers: supply link employment -> wage_rate, horizon medium (A-23). input_suppliers.towers#2: a single-variable link to riggers `employment` (the group link from round 2 does not chain, see below). Others empty.
- Answers: 2 from the table.

## Final engine output (reported lines)
Treasury receipts up, net price received down; licensees: compliance cost up, price paid down, lobbying up, fewer sellers; tower sites demand and price up (dominance A-31); riggers employment up, wage ambiguous (short up, medium down); foreign equipment price and quantity up; municipalities applications and lobbying up; Pellow (`sellers.substitutes`) quantity and return down; borrowers.other interest rate ambiguous (A-26 against A-27); per-reading lines for U1: resale quantity, asset value, investors' demand, reclassification (decrease or increase under U1-b, none under U1-a).

## What the format could not hold
- K3 limits what a buyer may hold. `capped` is a supply-side quantity rule; `terms` produced a fall in blocks traded; `thresholds` gives only a fall for those near the line, and the price effect had to be a link (supply_price, A-17).
- Every alternative of `licensees` is ambiguous: CR-4 takes the licence price falling as making buyers better off, while the build-out makes them worse. No premise ranks the two, so `legal_breach`, `investment_target`, `capital_stock_target`, `consumers price_paid` come out ambiguous.
- A group variable cannot be the source of a link (employment,hours_worked), so it needed a single-variable link beside it.
- The build-out is a cost fixed per licensee but also a mandated service to others (coverage), with no receipt variable for it (`quality_per_unit` used); the `supply` relation stands in for "less own funds, more borrowing" (licensees to the loan market).
- A-24 (delayed projects done after 2032) and the A-16 exit were not expressible: `timing` carries only announcement and deadline windows, not a shift past a date.
- A transfer permitted with consent (reg. 14) is not a change from a baseline of no licences; only the U1-b ban shows as a component.
