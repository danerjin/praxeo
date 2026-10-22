# WE-033 Kestland, expand loop, blind run (notes)

Files: `seed.json`, `proposals.json`, `answers.json`, `policy.md` (section 1 only), `situation.json` (final, from `--out`).
Run: `python -m praxeo.core.expand cases/we033_kestland/loop/seed.json cases/we033_kestland/loop/proposals.json cases/we033_kestland/loop/answers.json --policy cases/we033_kestland/loop/policy.md`.
Result: DONE in 3 rounds (the depth limit), 20 nodes (7, 7, 6), 33 proposals, 20 questions (13, 3, 4). No `off-list:` lines.

## Seed (the policy's own facts, CR-1)

- Exchange `e_bonds` (treasury sells, `bondholders` buy, `interest_rate` is the treasury's price). It is the only exchange the policy touches. K1 is a lump sum with no trade, so there is no exchange for it.
- `means`: K1 in for `households` and for `households.applying` (the 0.6 million paid after applying by form, a different path from direct deposit); K1b (the second payment per tax-filing unit, U1-b only) in for `households.separate_filers`; K2 out for `bondholders` (CR-8, borrowing: the lenders' side is recorded).
- `compliance` K1 `households.applying` (form, identity documents). `enforcers` K4 `officials.revenue`.
- `funded`: K4 paid by `taxpayers.future` (premise A-11, repaid not rolled over); K3 paid by `taxpayers.future` (A-11, A-4) or by `recipients.other_spending` (A-11, j1 = the complement of A-4). The record leaves K3's funding open (A-4), so both branches are seed facts and each carries its own premise.
- `announced` K1 (A-5). `unclear` U1 with two readings: U1-a applies K1; U1-b applies K1 and K1b.
- Seed assumptions: A-4 (0.45, table), A-5 (0.55, table), A-11 (0.6, table), j1 (0.55, judged: the complement of A-4, "mainly lower spending rather than higher taxes").

## Round 1 (depth 1), 7 nodes

- `households` (resources up). Links, all from the survey, the 2014 rebate or the assumption statements: to `consumption` (short; A-1, A-16), to `saving` (short; A-2), a `substitute` to `borrowers.households` loan demand (A-6), to `homebuyers` demand (A-19), `same_act` to `claimants.false` (A-14: diversion or double payment). Also a `timing` fact for A-15 (delaying purchases for a further payment) and a `stake` for retailers (A-13).
- `bondholders` (resources down): `supply` links to the interest rate of `borrowers.business` and `borrowers.mortgage` (A-3 and A-17; the second splits the borrowers: card and payday rates barely move, business and mortgage rates carry the rise).
- `households.applying` (compliance up, resources ambiguous): a dominance fact (the payment outweighs the cost of applying, kind `response`; premise "apply only if worth more", judged 0.95: applying is chosen, CR-2).
- `households.separate_filers` (ambiguous per reading): link to `reclassification` under reading U1-b (A-7).
- `taxpayers.future`: link to `households` consumption, long (A-12).
- `officials.revenue`, `recipients.other_spending`: empty (nothing in section 1 to go on).

Answers: from the table: A-1 0.9, A-2 0.9, A-3 0.6, A-6 0.8, A-7 0.7, A-12 0.6, A-13 0.45, A-14 0.7, A-15 0.25, A-16 0.85, A-17 0.6, A-19 0.3. Judged: "apply only if worth more to them than the cost" 0.95 (CR-2; no table entry).

## Round 2 (depth 2), 7 nodes

- `borrowers.business`: `own_price` rate to loan demand (no premise); `yield` loan demand to `investment_target` (A-8).
- `borrowers.mortgage`: `own_price` rate to loan demand; `same_act` to `homebuyers` demand (A-8); `cost` rate to `homeowners` asset value (A-8, CR-7c).
- `claimants.false`: `paid_into` the `general_fund` balance (A-18: some false claims are detected and repaid).
- `households` (revisit): `same_act` consumption to `retailers` sales (no premise, an identity; short); `supply` links from saving to the business and mortgage rates (judged premise j2: money saved or used to repay debt returns to the pool of loanable funds; this is the opposing chain to the crowding out, CR-8 0.9 on the borrowing baseline).
- `households.separate_filers` (revisit): `paid_from` general fund balance under U1-b (A-7; the extra payments draw on a fund K2 does not cover).
- `borrowers.households`, `households.applying` (revisit): empty. A-17 says household credit rates barely move, and nothing in section 1 leads on from applications.

Answers: table: A-8 0.75, A-18 0.75. Judged: j2 0.85 (deposits and repayments are lent on; not in the table).

## Round 3 (depth 3), 6 nodes

- `borrowers.business` (revisit), `borrowers.mortgage` (revisit): the rate came out ambiguous because the saving chain (j2) opposes the auction chain. Dominance facts, kind `arithmetic` on the case's figures (premise A-1: some of the payment is spent, so the saved part, at most 4.0 bn, is less than the 4.1 bn borrowed), for the rate, loan demand and investment. Also `yield` investment to `economy` capital stock, long (A-10), with its own dominance fact.
- `homebuyers`: `supply_price` demand to `homeowners` asset value (judged j3: home supply is slow in 2027 and 2028); dominance fact that the fall in mortgage borrowing outweighs housing spending out of the payment (judged j4).
- `homeowners`: the same dominance fact on asset value.
- `retailers`: `input` sales to `workers.retailers` employment and hours, short (A-9).
- `general_fund`: empty.

Answers: table: A-9 0.8, A-10 0.6. Judged: j3 0.85, j4 0.7 (the A-19 chain is 0.3 in the table; this is the premise that the opposing chain is the smaller).

## Table versus judged

Table: A-1, A-2, A-3, A-4, A-5, A-6, A-7, A-8, A-9, A-10, A-11, A-12, A-13, A-14, A-15, A-16, A-17, A-18, A-19 (all 19 are used). Judged (five): j1 (complement of A-4, 0.55), apply-only-if-worth-more (0.95), j2 saved money returns to loanable funds (0.85), j3 home supply slow (0.85), j4 mortgage fall outweighs housing spending (0.7).

## What the format could not hold

1. Means-only components give no `chooser`, so facts that need one are accepted but never fire: `timing` (A-15; the announcement of K1, A-5), `stake` (A-13, retailers lobbying for a repeat payment), `alternatives`. The effects of the announcement (borrowing against the payment before it arrives, A-5; delaying purchases for a further payment, A-15) and retailers' lobbying therefore do not appear. `timing` also has no sign for "spend earlier because richer later": a `bring_forward` by someone made better gives a decrease.
2. Chains at different horizons merge. The short-run rise in consumption (A-1) and the long-run fall from expected installments (A-12) come out `ambiguous` for `households` consumption, and that ambiguity passes to retailers' sales and workers' employment and hours. CR-12g (horizons not combined) is not implemented in the sign merge; a dominance fact would net across horizons, which the rules do not allow, so none was proposed.
3. Dominance is not applied to a sign per reading, so `general_fund` balance (claim recoveries up, extra U1-b payments down) and `households.separate_filers` stay `ambiguous` with a sign per reading.
4. K2's cap and U1-b: 4.6 million payments exceed what 4.1 bn covers. The record does not say who bears the shortfall (fewer payments, or other funds); `funded` has no way to say "unstated". Only the `paid_from` link under U1-b carries it.
5. The fine and repayment under K4 (2,000 crowns, repayment of false claims) attach to no exchange, so `charges` cannot hold them; only the enforcer and the detection link (A-18) are in.
6. Borrowing itself: `means` has no premise, so `bondholders` resources fall unconditionally (Tier A), although CR-8 0.9 says the lenders' side gives no sign by itself (they would have lent elsewhere). The sign was kept as the engine derives it.
7. Foreign versus domestic buyers (30% of bonds abroad, `currency` link) were not split: nothing in the assumptions bears on it, and `e_bonds` takes one `bondholders` side.
8. A group sign for "who pays the later installments" (CR-8, general budget payers: `at_least_one_decrease`) is not available from `funded`; each payer is a separate signed effect, and K3's two branches rest on A-4 (0.45, unreported) and j1 (0.55, reported).
9. The `applications` variable (an activity that exists only under the policy, CR-12 0.9) has no rule that raises it, so the applying households' form-filling shows only as compliance cost.
