# WE-036 expand loop, blind run: notes

Read: section 1 of the WE-036 record and the ID / Statement / Type / p columns of its assumption table only (copied to `policy.txt`:
section 1 verbatim). Not read: sections 2 to 9, the "If false" and "Evidence" columns, the report, the consequence list, corrections,
gaps, `05_examples_core/`, anything existing under `cases/we036_quenby/` or `tests/`.

Result: DONE in 3 rounds, 25 premise questions asked by the loop, 16 distinct nodes (23 node visits: 6 at depth 1, 15 at depth 2,
2 at depth 3). 36 reported consequence lines plus 1 unreported (`consumers.local_services price_paid`, premise A-24 at p 0.4).

## Seed (CR-1, the Act's own facts)

- Exchange e1: employers.bound (50+ FTE) buy full-time labour (30+ hours a week) from workers.full_time_bound; wage_rate on the seller
  side, full_cost_per_unit on the buyer side (the only buyer-side price variable in the list that is a cost to a buyer of labour).
- Exchange e2: the same employers buy from workers.minimum_wage_bound. Split from e1 because R1 (existing minimum wage, section 1: "about
  11% ... at or near it") makes the operation differ within the class (CR-1 recording: split an actor class where the operation differs):
  the wage cannot take the charge there. This is a judgement; R1 is an existing rule, not part of the Act.
- Charges (K1, "play or pay") as two components, on both exchanges: `k1_cover` (the mandated term, paid in kind to the worker:
  receipt non_wage_compensation, with `quantity_premises` A-1 and A-7 because the term is worth something to its receiver) and
  `k1_charge` ($3,000 a head to the Department of Revenue: receipt non_tax_receipts; `quantity_premises` A-1: K1 binds).
- Moves: e1 buyer (A-3, wages sticky), e1 seller (A-6, wages above the minimum adjust), e2 buyer (A-9, the minimum wage binds).
- Announced (both K1 components): signed 4 January 2027, effective 1 January 2028; premise judged.
- Compliance: employers.bound with k1_cover; insurers.health with k2 (K2 binds "insurers and self-insured employers").
  Enforcer: officials.enforcement (K5). Funded: taxpayers (K5, A-29 "new general-fund money").
- Not in the seed: held (the Act holds no price), grants, capped, banned, expires ("It has no expiry"), backstops, discretion, means,
  transfers, early_price, fixed_budget (A-29 says the appropriation is new money).

Seed premises: a1 = A-1 (0.9), a3 = A-3 (0.75), a6 = A-6 (0.8), a7 = A-7 (0.6), a9 = A-9 (0.85), a29 = A-29 (0.9) from the table;
a_ann "Employers expected the Act to take effect on 1 January 2028." judged 0.85 (signed with the governor's support, a year ahead;
the table's A-21 mixes this with asset values).

## Round 1 (depth 1): six nodes

Engine effects arriving: employers.bound (compliance_cost +, full_cost_per_unit +, quantity_traded -, resources -), workers.full_time_bound
(non_wage_compensation +, quantity_traded -, wage_rate -), workers.minimum_wage_bound (non_wage_compensation +, quantity_traded -),
insurers.health (compliance_cost +), officials.enforcement (enforcement_cost +, non_tax_receipts +), taxpayers (resources -).

employers.bound (14 proposals):
- alternatives to the charge: reschedule 30-35 hour jobs to under 30, so workers.part_time employment (A-10; "employees averaging
  under 30 hours" exempt); more hours from existing full-timers, workers.full_time_bound hours_worked (A-11); offer cover instead
  (non_wage_compensation: A-2 for firms offering nothing, A-5 for firms upgrading short plans); agency labour, workers.agency
  employment (A-34); contracting out / franchising, reclassification (A-17).
- margin: outside the rule, legal_breach, misreported offers (A-18; K5 "Misreporting: twice the unpaid charge").
- stake: lobbying over k1_cover (A-19: the large chains, employer associations).
- yield (return_on_capital falls; A-8: the wage does not fall by the whole charge) and asset (factor_owners.bound_firms asset_value; A-21).
- links from full_cost_per_unit: output to consumers.local_services price_paid (A-24), substitute to employers.unbound quantity_traded
  (A-22, the exemption below 50 FTE) and to sellers.foreign quantity_traded (A-26, Tarnley across the border).
- timing: carry_over of employment into 2027, the year whose FTE average sets 2028 status (A-14, A-15; the announcement is the seed's).
workers.full_time_bound (7): alternative workers.unbound employment (A-8: firms under 50, part-time, Tarnley; the engine's CR-4 chooser
is the wage fall); stake (A-19, unions); links from non_wage_compensation: same_act to insurers.health quantity_traded (A-2), substitute
to insurers.individual_market (A-20), complement to hospitals.providers (A-27), substitute to officials.indigent_care subsidy_outlay
(A-28, A-32); link from wage_rate (same_act) to officials.enforcement tax_revenue, premises "Wages are subject to Quenby's 4.5% income
tax." and "Employer contributions to health premiums are excluded from the employee's income for Quenby's income tax." (R2).
workers.minimum_wage_bound (1): stake (A-19). insurers.health (1): stake (A-19). officials.enforcement, taxpayers: empty list.

## Round 2 (depth 2): nine new nodes and revisits

New nodes: employers.unbound (+quantity_traded): input link to workers.unbound as a group (employment, hours_worked), CR-6 1.1,
no premise. officials.indigent_care (-subsidy_outlay): substitute link to taxpayers (the Program and the appropriation draw on the same
fund), premise "The Indigent Care Program is paid from the general fund." workers.agency (+employment): same_act link to
employers.staffing quantity_traded (A-34). Empty: factor_owners.bound_firms, hospitals.providers, insurers.individual_market,
sellers.foreign, workers.part_time, workers.unbound (the further reach is diffuse, or needs a premise I could not tie to a sentence).
Revisits: employers.bound gets a substitute link legal_breach -> officials.enforcement non_tax_receipts (A-18: a misreported offer is
a charge not paid) and a yield link return_on_capital -> investment_target (A-21). officials.enforcement (tax_revenue falls, receipts
rise) gets two links to taxpayers resources_available_other_uses: substitute from non_tax_receipts, premise "Charges under the Act are
paid into the general fund." (K5); same_act from tax_revenue, premise "Income tax revenue lost to the general fund is made up by
other taxpayers." The effect: non_tax_receipts and taxpayers resources become ambiguous (opposite chains, CR-12b).

## Round 3 (depth 3)

Nodes: employers.staffing (empty), workers.unbound revisited (nothing new). Dominance (CR-12e, kind arithmetic, premise A-36) added
for officials.enforcement non_tax_receipts (increase: charges collected are not cut below the figure A-36 gives by misreporting) and for
taxpayers resources_available_other_uses (increase: A-36 says the income tax lost is smaller than the excess of capped firms' charges
over the appropriation). Direction read off A-36 alone.

## Answers: table or judged

From the table (p copied): A-1, A-3, A-6, A-7, A-9, A-29 (seed); A-2, A-5, A-8, A-10, A-11, A-14, A-15, A-17, A-18, A-19, A-20, A-21,
A-22, A-24, A-26, A-27, A-28, A-32, A-34, A-36 (loop; 20 of the 25 questions).
Judged (5 loop questions + the seed's a_ann): "Wages are subject to Quenby's 4.5% income tax." 0.97 and "Employer contributions to
health premiums are excluded from the employee's income for Quenby's income tax." 0.97 (both R2, section 1); "The Indigent Care
Program is paid from the general fund." 0.97 (R3); "Charges under the Act are paid into the general fund." 0.97 (K5); "Income tax
revenue lost to the general fund is made up by other taxpayers." 0.65 (CR-8 payers from the general budget; the one real judgement);
a_ann 0.85.
Table assumptions never used: A-4, A-12, A-13, A-16, A-23, A-30, A-31, A-33, A-35, A-37 (A-25 is absent from the table).

## What the format could not hold

1. A cap on a charge (K4, $300,000 a firm, A-12, A-13). `capped` is a cap on quantity traded; `means` carries no premises, so "the 45
   capped firms are in operation 4 (a lump sum) above the cap" cannot be stated with A-12. Left out.
2. A threshold in the firm's size (K3, 50 FTE; A-14, A-15, A-16, A-17, A-31). The firms just under the line are not a party to e1, and
   a restraint on growth is a fall in a quantity, while an `alt` chain always signs its variable as an increase. I used a timing
   (carry_over of employment) on employers.bound as the nearest thing, which is a stretch: it puts firms at 40-49 FTE in the class of
   bound firms. A-31 (growth delayed, not lost: a later window) has no fact.
3. The in-kind receiver's response. A worker who receives a mandated term gets a better option, but `chooser(.., better)` is derived only
   from grants, held lines and caps, not from a charge's receiver. So A-35 (newly covered workers near the margin of leaving) has no
   place, and "workers stay" cannot be signed.
4. A response that is a partial reversal (A-37, A-23): unbound hiring pulling the bound wage back up needs a link from the alternative's
   variable back to wage_rate; the loop test (`response_concl`) reads links only, an `alt` is not an edge. Adding the link would create
   an opposing chain that needs its own dominance and spills into the tax chain, so I did not add it; wage_rate stays a plain decrease.
5. Netting inside one budget (A-36). The format has no fund. I got the effect with two links into taxpayers' resources plus a dominance
   fact whose direction I took from A-36; "receipts" and "outlay" are different variables so they are never netted by the engine.
   The relations used (`substitute`: two draws on one fund) are a stretch of the vocabulary's names.
6. A charge that the payer may avoid by taking another option (play or pay) is two charges here; the engine takes both as paid
   (`c_paid` is Tier A for each), so the in-kind receipt and the fee are both signed as increases without a premise that anyone chooses
   that branch. The premises for each branch (A-2, A-4, A-5) could only go on separate `alt` facts, which repeat what `c_paid` already gives.
   A-4 ("some firms choose to pay") is unused for that reason.
7. The 30-hour threshold on workers (A-10, A-11) is held as alternatives of the employer into workers.part_time and hours_worked.
8. Mechanics of the file-driven run: a node's list is returned whole at every visit, so a proposal I appended later for a revisited node
   was also in effect from its first visit; depth numbers in the log are therefore earlier than a real per-round run would give for
   those facts. The results do not change.
