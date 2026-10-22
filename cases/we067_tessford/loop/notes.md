# WE-067 Tessford: expand-loop notes (blind run)

Inputs read: section 1 and the assumption table only. Files: `seed.json`, `proposals.json`, `answers.json` (statement to p),
`answers_src.json` (statement to `table` or `judged`), `situation.json` (final), `final_output.txt`, `policy.md` (section 1).
Result: DONE in 3 rounds, 34 node visits (13, 14, 7), 31 loop questions (26 from the table, 5 judged), plus 14 seed
assumptions (11 table: A-1, 2, 3, 4, 5, 7, 9, 12, 16, 17, 36; 3 judged: j1, j2, j3). All 37 table assumptions ended up used.
No `off-list:` lines in the final run.

Two seed corrections were made after trial runs of round 1 (before the final recorded rounds, so the counts above are for
the corrected files): (1) the seller of the sublet exchange was first `tenants.controlled`, which made sitting tenants both
favoured (rent cap) and burdened (sublet cap) and every alternative of theirs ambiguous; the sublessors became their own
class `tenants.sublessors`. (2) The county-line and tenure-line thresholds shared component `k4` with the grant, which made
senior credit holders "worse" and "better" under the same component; they now have their own components (`k4_county`,
`k4_tenure`, `k4w_county`).

## Seed (the policy's own facts, CR-1)
- `e_cov` (covered sitting tenancies): held below by k1 (A-1 binding, A-2 enforcement); `transfers` (A-5, the counterfactual
  where rents follow the market); `announced` k1 and `early_price` (A-4, leases renewed in the window, §3 base date);
  `compliance`/`enforcers` (rent board). No unsatisfied side or criteria: §3 lets the landlord set the initial rent on a
  new tenancy, so the text names no one left unsatisfied.
- k2 (tenancy rules) as `terms` worse: for-cause eviction for sellers (j2, judged 0.85), no assignment for buyers (A-3);
  sublet cap as `held` on `e_sublet` (A-3).
- k3 withdrawal: relocation payments as two `charges` on `e_cov` (to `tenants.displaced`, to `tenants.senior_displaced`),
  `branch_premises` A-12; the five-year bar on re-letting as `banned` on `e_relet` (j1 judged 0.8).
- k5 fee: `charge` with `basis: operating`, receiver `officials.enforcement`, premise A-2 (a fixed $90 per covered unit).
- k4 credit: `grant` to the county landlord side of `e_cred` (A-16), `moves` buyer (A-17) and seller (A-36, long horizon),
  `incidence` buyer (A-17); `thresholds` for the county line (A-7), the three-year tenure line (A-9); `funded` by
  `general_fund` (j3, the section says general fund). k6 (4% county fee): `enforcers` and `funded` only.
- U1 as `unclear`: k4w (credit to displaced seniors, `e_cred_w`) and its threshold apply under U1-a only.

## Round 1 (13 nodes)
- general_fund: paid_from link to `fund_balance`; link to `recipients.other_spending` (judged 0.65: "no tax is named").
- landlords.controlled: alternatives reclassification (A-12), units held vacant (A-34), buyouts as turnover and side payments of
  tenants (A-29); adjust margins maintenance (A-10) and quantity supplied (A-12, A-13); timing bring_forward of vacancy and
  turnover (A-8; the ordinance was expected from Nov 2026); stake (A-18, A-19); asset (A-23); yield; supply link to
  prospective tenants' price (A-30); same_act links from withdrawal to condominium buyers (judged 0.85), displaced turnover,
  displaced relocation (A-14).
- landlords.county: supply_price links to county renters and senior holders (A-20).
- officials.enforcement: paid_from / paid_into `fund_balance` (CR-8 1.0: fee and cost as two items).
- owners.withdrawn: alternative of selling as condominiums.
- tenants.controlled: alternatives turnover, relocation (A-6), job changes (A-25); quality adjust (A-10); stake; vacancy link
  (judged identity 0.95).
- tenants.prospective: substitute links to county and Durnside rents (A-15, A-20, A-21), to exempt rents (A-22) then
  developers (A-24); two links from Tessford's free rent (A-30): movers' relocation and landlords' return.
- tenants.senior: alternatives staying (inverse of turnover, A-16) and buying a home (A-35); stake; vacancy link.
- tenants.sublessors: outside margin (A-11). tenants.displaced, tenants.senior_displaced: payment-to-resources same_act link.
  tenants.senior_near: vacancy link. tenants.subtenants: nothing.

## Round 2 (14 nodes)
- developers: supply link, long horizon (A-24). homebuyers: substitute link to demand for rentals (A-33).
- landlords.controlled#2: dominance on quantity_supplied (A-32) and return_on_capital (A-37), both ambiguous in round 1.
- tenants.controlled#2: the resources-to-moves link for the CR-4 exception (judged 0.75), dominance on turnover (A-27, A-28) and
  relocation (A-27, A-31); part of `tenants.nonsenior`.
- tenants.displaced#2: part of `tenants.nonsenior`; supply_price links to county and Durnside rents (A-20, A-21); link to
  prospective tenants' demand (judged 0.9, 42% left so 58% stayed).
- tenants.prospective#2: demand to price link (A-13). tenants.senior#2: dominance price_paid decrease (A-17).
- renters.neighbors, renters.durnside: yield links to their landlords. Empty: recipients.other_spending, general_fund#2,
  officials.enforcement#2 (fund balance stays ambiguous: no cost figure), tenants.senior_displaced#2, tenants.sublessors#2.

## Round 3 (7 nodes)
- tenants.nonsenior: dominance relocation decrease (A-26). tenants.prospective#3: dominance quantity_demanded increase (A-33).
- Empty: landlords.controlled#3, landlords.county#2, landlords.durnside, tenants.controlled#3, tenants.senior#3.

## Answers
Table: whenever the statement was an assumption (26 in the loop). Judged: the five above, each with its reason in the proposal
text or here (general-fund payers, condominium sales, vacancy identity, savings fund moves, displaced who stay).

## Left unsigned or unresolved
`homebuyers quantity_traded` (condominium buyers against seniors who rent instead of buying), `tenants.nonsenior turnover`,
`tenants.controlled resources_available_other_uses`, `officials.enforcement fund_balance`: opposing chains with no dominance premise.
Per reading: `tenants.senior_displaced` price paid, quantity traded and subsidy share (U1-a changes, U1-b none) and relocation
(U1-a ambiguous, U1-b increase).

## What the format could not hold
- A payment from a payer to the counterparty on the same exchange (relocation payment): the vocabulary has no receipt
  variable for it (`side_payments` used), and the engine treats a charge as a wedge on both sides, so tenants' resources
  show ambiguous.
- Vacancy decontrol: a cap on increases for sitting tenancies with a free initial rent has no exchange of its own; the
  free-rent market is reached only through links.
- The credit's amount (gap recomputed yearly, capped at the new rent), the growth of the gap by year, the registered market rent,
  the 4% fee between public bodies, fines with refunds, 120-day against one-year notice.
- Counts: A-26, A-31, A-33 compare flows (170 against 145 a year, 58%); the format takes them as dominance premises, not arithmetic.
- A class that is both keeper and senior (tenants.controlled includes seniors who stay); `tenants.nonsenior` approximates A-26.
- The reading-specific alternative (a senior vacating before a withdrawal notice under U1-b) was not proposed: no node needed it.
