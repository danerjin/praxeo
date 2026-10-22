# WE-020 Tamberlay Home Start Grant: expand loop, blind run (loop_r2)

Inputs read: section 1 of the policy record and the assumption table (ID | Statement | Type | p) only. Names were chosen from `python -m praxeo.core.expand --vocab --exclude WE-020`; the final run prints no `off-list:` lines. Output: `final_output.txt`, `situation.json`. DONE in 3 rounds, 20 questions asked in the loop (plus 5 premises used by the seed), 28 node keys listed (14 with proposals, 14 with an empty list), 34 proposed facts.

## Seed (policy's own facts only)

- Exchange `e_home`: buyer `homebuyers.first_time`, seller `sellers.entry_level` (sellers of homes at or under the cap, existing or new); price variables `price_paid` / `net_price_received`. No unsatisfied side or criteria: nothing holds a price.
- `grants`: k1, paid to the buyer side by `general_fund` (K1; K3 "annual appropriation from general revenue"), outlay `subsidy_outlay`.
- `moves`: buyer side on a1 (prices under the cap rise by less than the grant, so the price net of the grant falls), seller side on a2 (supply slow, so the sellers' price rises).
- `thresholds`: the $450,000 cap, as a line in `price_paid` for `homebuyers.near_cap`, with `sellers.near_cap` as the chooser (a8).
- `expires`: k1 ends 30 June of Year 4, premise a16 (renewal uncertain at the deadline). `announced`: k1, premise a5 (known from March).
- `compliance` k1 `homebuyers.first_time` (applying, sworn declarations); `enforcers` k4 `officials.revenue` (K4); `funded` k4 `taxpayers.current` (K3, general revenue, no premise).
- Assumptions used by the seed: a1, a2, a5, a8, a16.

Choices worth recording:
- `expires` takes a16 ("Renewal is uncertain at the deadline...") and not a15 ("The grant is not renewed after Year 4", p 0.4). The section says renewal is "possible but not promised"; a16 is the table's statement of that. With a15 (below the cut-off) the deadline rush and the fall after expiry would not be reported at all. A15 was not used anywhere.
- The two provisions section 1 calls unclear (indexing of the cap, renewal) are treated by the record itself as expectations (A-3, A-15), so no `unclear` readings were written. K3's "the law does not say what happens if applications exceed the appropriation" is also an unclear provision (rationing by queue against a top-up from the general budget), but the table has no assumption on it and section 1 does not list it among the unclear provisions, so I left it out (see "could not hold").

## Round 1 (depth 1)

Nodes listed: general_fund (subsidy_outlay up), taxpayers.current (resources down), officials.revenue (enforcement_cost up), homebuyers.first_time (compliance_cost up, price_paid down, quantity_traded up, resources ambiguous), sellers.entry_level (net_price_received up, quantity_traded up), homebuyers.near_cap (price_paid down).

Proposed:
- general_fund, taxpayers.current, officials.revenue: empty (the seed already funds and enforces; nothing in section 1 to add).
- homebuyers.first_time:
  - alternatives: `renters` quantity_demanded (keep renting; a4), `buyers.border` cross_border_purchases (buy in Lowen; a12, "Kessford sits on the border with the state of Lowen"), `buyers.substitutes` quantity_substitute (buy above the cap; new statement N1), `homebuyers.first_time` job_changes (taking a job that requires moving forfeits the grant; a9, "principal residence for 24 months; otherwise the full grant is repaid").
  - timing: bring_forward on quantity_traded with a5 and a16 (delay after the March announcement; sign earlier before the deadline).
  - links: quantity_traded -> `intermediaries` earnings (input; a21).
  - dominance: resources_available_other_uses increase, kind empirical, premise N3 (the cost of applying is far smaller than the grant). Needed because grant ("increase") and compliance cost ("decrease") otherwise leave it ambiguous.
- homebuyers.near_cap: alternatives chosen by `sellers.near_cap`: reclassification by `sellers.near_cap` and side_payments by `homebuyers.near_cap` (a8, "value outside the contract price").
- sellers.entry_level:
  - assets: `owners.under_cap` (a3, expected to last to Year 4, CR-7c); yields: `builders` (a2).
  - links: net_price_received -> `builders` investment_target (yield; a10); -> `homebuyers.repeat` price_paid (same_act; N2, many buyers in the segment get no grant); -> `landlords.entry_level` net_price_received (same_act; a13); -> `intermediaries` earnings (yield; a21).
  - timing: bring_forward on quantity_supplied (a6, owners delay listing until after July).

Answers: from the table: a4 0.85, a12 0.7, a9 0.7, a21 0.85, a3 0.75, a10 0.65, a13 0.7, a6 0.55. Judged (not in the table): N1 "Some first-time buyers could buy a home above the cap instead of one under it." 0.85 (section 1: about two thirds of sales are above $450,000 and A-20 names buying above the cap as an option); N2 "Many buyers in the segment get no grant." 0.9 (18,000 first-time purchases out of 60,000, and only those who apply get it); N3 "The cost of applying for the grant and proving eligibility is far smaller than the grant." 0.9 (a $15,000 grant against paperwork and declarations).

## Round 2 (depth 2)

Nodes: builders, buyers.border, buyers.substitutes, homebuyers.first_time#2, homebuyers.near_cap#2, homebuyers.repeat, intermediaries, landlords.entry_level, owners.under_cap, renters, sellers.entry_level#2, sellers.near_cap.

Proposed:
- builders: links investment_target -> `construction_workers` wage_rate (input) and -> `sellers.substitutes` quantity_substitute (substitute), both on a11 (builders and construction labor scarce and used elsewhere); stake (a17).
- buyers.border: link cross_border_purchases -> `sellers.foreign` quantity_traded (same_act; a12).
- buyers.substitutes: link quantity_substitute -> `sellers.substitutes` quantity_traded (same_act; N1).
- homebuyers.repeat (reached through the price rise for buyers with no grant): alternatives legal_breach (a7, partner declarations), reclassification (a14, nominee buyers, p 0.3 so not reported), cross_border_purchases (a12).
- intermediaries: stake (a17). owners.under_cap: stake (a17), and link asset_value -> `buyers.substitutes` quantity_demanded (yield; a18 and a19, owners bid for larger homes with part of the gain).
- landlords.entry_level: alternative quantity_supplied (rentals offered; a13) and link quantity_supplied -> `renters` price_paid (supply; a13).
- renters: link quantity_demanded -> `renters` price_paid (supply_price; N4 "The supply of rental homes responds slowly." judged 0.8 from "the stock of homes responds slowly to prices").
- sellers.entry_level#2: link net_price_received -> `owners.under_cap` subsidy_share_received (same_act; a20, who keeps a subsidy when one side has fewer alternatives, CR-7b).
- homebuyers.first_time#2, homebuyers.near_cap#2, sellers.near_cap: empty.

Answers from the table: a11 0.8, a17 0.85, a7 0.6, a14 0.3, a18 0.6, a19 0.75, a20 0.7. Judged: N4 0.8.

## Round 3 (depth 3, the last)

Nodes: builders#2, buyers.substitutes#2, construction_workers, homebuyers.repeat#2, intermediaries#2, landlords.entry_level#2, owners.under_cap#2, renters#2, sellers.foreign, sellers.substitutes.

Proposed:
- buyers.substitutes#2: two links to `sellers.substitutes` price_substitute (supply_price), one from quantity_demanded (owners bidding for larger homes) and one from quantity_substitute (first-time buyers buying fewer above the cap), premise N5 "The supply of homes above the cap also responds slowly." Judged 0.8 (same section 1 sentence as the supply of homes under the cap). The two chains oppose, so the engine reports the price of homes above the cap as ambiguous, which is what section 1 supports.
- homebuyers.repeat#2: link cross_border_purchases -> `sellers.foreign` quantity_traded (same_act; a12). Opposes the link from first-time buyers' fall in Lowen purchases, so Lowen sellers' quantity_traded is ambiguous.
- all others: empty.

## Final engine output

See `final_output.txt` (DONE in 3 rounds, 20 questions). Ambiguous: renters price_paid (rents: fewer renters against fewer rental homes), sellers.foreign quantity_traded, sellers.substitutes price_substitute. Not reported: homebuyers.repeat reclassification (a14, p 0.3).

## Answers: table against judged

Table: a1, a2, a5, a8, a16 (seed); a3, a4, a6, a7, a9, a10, a11, a12, a13, a14, a17, a18, a19, a20, a21. Judged by me from section 1 (no matching row): N1 0.85, N2 0.9, N3 0.9, N4 0.8, N5 0.8. Unused table rows: a15 (see seed note).

## What the format could not hold

- The clawback (the full grant repaid if the home is not the principal residence for 24 months): it is a payment on a later act, not on trade in an exchange, so `charges` cannot take it. I recorded only its effect on moving (alternative on job_changes, a9).
- Evasion of an eligibility condition for a benefit (a7 declarations, a14 nominees): `alt` runs the wrong way for the recipients of a benefit (a better option makes alternatives used less), and `outside` fires only under a held price, cap, ban or charge. I routed it through those made worse (`homebuyers.repeat`, whose price rose), which is correct for CR-4 but depends on the link from the price to them.
- K3's silence on what happens when applications exceed the 20,000-grant appropriation (rationing against a top-up): needs `unclear` readings with their own components (a queue/discretion component, a funded top-up); no assumption in the table or sentence in the list of unclear provisions covers it, so not written.
- The cap indexed or not: the policy and A-3/A-15 treat it as expectations; there is no fact to say a fixed nominal line erodes as prices rise (4% a year), nor a time-varying threshold.
- The supply response of builders that limits the price rise (A-1, A-10): the link from price to builders' investment and back to price closes a loop, and the engine treats the step round the loop as a response that does not propagate, so a `supply` link from builders to the price cannot be stated; A-1 carries it in `moves`.
- A homeowner who is also a seller (owners.under_cap hold the asset, sellers.entry_level trade): ownership and trading are two classes joined only by the asset fact; no `parts` was needed.
- Overlapping classes: `landlords.entry_level` net_price_received means a sale price, and rents would need another class name, since the same variable cannot carry both.
- The Lowen market (`sellers.foreign`) and the market for homes above the cap (`sellers.substitutes`) are reached only as quantities and one ambiguous price; the format has no exchange for them, since only one exchange is seeded.
- Window effects (announcement, deadline, after expiry) stay inside their windows and do not propagate, so the fall in first-time buying before July and the rush before June of Year 4 are not linked to the price of homes or to the sellers.
