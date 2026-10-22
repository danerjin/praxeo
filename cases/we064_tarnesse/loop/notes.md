# WE-064 Tarnesse 2.9 GHz Award: expand-loop notes (blind run, single stand-in for proposer and decider)

Inputs read: section 1 (copied to policy.md) and the assumption table (ID, statement, type, p) only. Final engine output: `final_output.txt`; situation: `situation.json`. Result: DONE in 3 rounds, 30 node visits (9 + 13 + 8), 23 loop questions (20 from the table, 3 judged), plus 11 seed premises (7 from the table, 4 judged). No `off-list:` lines.

## Seed (policy's own facts)

- Exchanges: `e_lic` (licensees buy the right from the state, `treasury`), `e_cap` (large bidders, `licensees.large`, buying beyond two blocks from `treasury.over_cap`), `e_resale` (`licensees.prospective` buy from `licensees.current`).
- K1: charge `k1` on `e_lic`, basis operating (a licence fee fixed per licensee, not per unit), receiver `treasury`, non_tax_receipts (K4's "paid into the Consolidated Fund"); premise A-1. Option added by K1 (the Radio Act ban is lifted for the winner): `terms` `k1_right`, better for the buyer side, no premise (CR-1 op 2). `announced` for k1, k1_right, k2, k3 (A-28). `expires` k1 (judged j4: licences end 31 Dec 2042, "no right of renewal").
- K2: charge `k2` on `e_lic`, operating, paid in kind, receiver `customers.outside_cities` (the subclass that receives coverage), receipt variable quality_per_unit; charge premises A-8 (binding) and A-3 (enforced); quantity premise j1 (judged: they value coverage). `outside` margin on `e_lic`, legal_breach, A-9. Compliance by licensees, enforcement by `officials.enforcement`.
- K3: `banned` `k3` on `e_cap` (premise j2, judged: some bidders would take more than two); `outside` margin reclassification (A-5, stakes below the affiliate line).
- U1: `unclear` with U1-a: `discretion` `k14_u1a` (consent of the Authority, reg. 14) and U1-b: `banned` `k14_u1b` on `e_resale` (premise j3, judged: the bar is enforced), with the `outside` margin A-11 tagged `reading: U1-b`.
- K5: `enforcers` k1, k2, k3 = `officials.enforcement`; `funded` k5 by `taxpayers` (stated in the text, no premise).
- Judged seed premises: j1 0.8, j2 0.9, j3 0.8, j4 0.85. From the table: A-1, A-3, A-5, A-8, A-9, A-11, A-28.

## Round 1 (9 nodes)

- customers.outside_cities: link to DSL supply (substitute), A-18 (Pellow's 1.6m lines, 700k outside fibre).
- licensees: alternative to the new option (densify less, A-7, A-4; measured by investment_target of licensees.operators); alternative to the build-out burden (resale, A-10; reading U1-a, the reading that opens it); links from licences held to tower tenancies, riggers, imported equipment (input, A-31) and to operators' supply (A-4); borrowing (A-27); fewer sellers to consumer price (A-16); stake in k2 (A-13).
- licensees.current: stake in k14_u1b (A-13; reg. 14 reading is a new-clause lobbying), link to bids by investors (A-12), yield and asset on the resale side (A-10).
- licensees.large: alternative to the cap (pool by sharing, A-6), link to entrants' holdings (A-14) and to the licence price (supply_price, A-17), stake (A-13).
- licensees.prospective: yield on the buyer side of resale (A-10).
- officials.enforcement: cost paid from the general fund (text: appropriation); treasury: receipts paid into the fund (reg. text), borrows less (A-26); taxpayers, treasury.over_cap: empty.
- Answers: all 13 from the table (A-18 .7, A-7 .75, A-4 .85, A-10 .6, A-31 .65, A-27 .7, A-16 .3, A-13 .85, A-12 .55, A-6 .6, A-14 .6, A-17 .6, A-26 .6).

## Round 2 (13 nodes)

- borrowers: loan demand raises other borrowers' rate (supply_price); treasury#2: Treasury's lower demand lowers it. Opposite chains (CR-8 0.9), left ambiguous. Premise judged (.6): credit supply cannot expand at an unchanged rate.
- general_fund: receipts and TCA cost are two items of one budget (CR-8 1.0); dominance of the receipts, kind arithmetic. Premise judged (.97) from the case's figures.
- input_suppliers.towers: dominance of band build-out over densification not done (A-31); price rises (supply_price, A-20); asset value rises (A-28).
- licensees.operators: densification not done lowers demand for sites, riggers, equipment, and operators' capacity (the opposing chains); dominance of the band's capacity (judged .85); riggers' wage (A-22); consumer price (A-15).
- licensees.entrants: DSL (A-18), consumer price (A-14, A-15), stake in k3 (A-13).
- sellers.dsl: price falls (A-19), asset falls (A-19, A-28). sellers.foreign: dominance (A-31), price (A-25).
- licensees#2, licensees.current#2, licensees.large#2, licensees.prospective#2, workers.riggers: one link (riggers' wage, A-22) or empty.
- Answers: 5 from the table (A-20 .8, A-22 .75, A-15 .7, A-19 .8, A-25 .6); 3 judged (above).

## Round 3 (8 nodes)

- consumers: own-price response; towers#2: permits (municipalities, applications), tower price to operators (same_act); sellers.dsl#2: DSL price to households; sellers.foreign#2: equipment price to operators; workers.riggers#2: dominance of wage (A-31), training (A-23), other building projects delayed (A-24). borrowers.other, general_fund#2, licensees.entrants#2: empty.
- Answers: A-23 .8, A-24 .6 (table).

## What the format could not hold

1. A right that the policy creates. K1 adds an option (CR-1 op 2) and charges for it. The nearest fact (`terms` better plus an operating charge) gives artefacts against the no-policy baseline: `licensees number_of_sellers decrease` (the fee as deterrent, for a market that did not exist), and a licence fee that reads as a loss before the surplus above the price (CR-3 1.1, CR-7 1.1) is counted. No fact says "the winner keeps value above price".
2. K3 restricts an option that exists only under K1. Signed against the uncapped auction, not against no award: `licensees price_paid decrease`, `licensees.large quantity_traded decrease` and `treasury.over_cap quantity_traded decrease` (the six blocks are sold either way; the seller subclass was split only to keep this off `treasury`). A-17's surplus to operators cannot be stated at all.
3. Dominance cannot settle a group: `workers.riggers employment,hours_worked` stays ambiguous (band build-out against densification not done) although the wage (single variable) is settled by A-31. A group variable also cannot be a link source, so the wage chain had to be run from other variables.
4. Dominance premises with an estimated p stand in for comparisons the text gives only by figures (A-31, the band against densification).
5. Not expressible: the build-out as one branch of "build or lose the licence without refund" (A-30, re-auction, p .3); timing of densification held back until the band arrives (the CR-10a rule exists for the announced "better" option, but the premise needed is not in the table and the text is silent, so not proposed); A-24's delay "after 2032" (a link with a short horizon carries only the delay); A-21 absent from the table.
6. U1 gives a sign per reading, but `licensees.current quantity_traded` under U1-a comes out ambiguous (resale alternative against the discretion's effects) and the engine does not say which chain opposes which.
7. `consumers quantity_demanded` ambiguous follows from the price-fall chain meeting CR-4's means exception (the engine's reading); `borrowers.other interest_rate` ambiguous is intended.
8. Depth 3 left reached but unvisited: municipalities (applications), builders, workers.prospective (enrollment), households (price_paid), `licensees.operators price_paid`; so lobbying by town councils (A-13) and the investment of tower companies could not be proposed.
9. Not covered: the Treasury's receipts in the whole period against borrowing (A-26) beyond `treasury quantity_demanded decrease`; A-5 and A-6 only as reclassification (no variable for sharing a network); A-16 enters with p .3 (below the cut-off, so the exit chain is not reported).
