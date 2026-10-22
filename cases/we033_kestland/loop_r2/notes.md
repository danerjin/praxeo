# WE-033 Kestland, expand loop, blind run (loop_r2)

Files: `seed.json`, `proposals.json`, `answers.json`, `situation.json` (final), `policy.md` (copy of section 1). Final engine output: DONE in 3 rounds, 22 questions (20 node visits: 10 + 8 + 2).

## Seed (the policy's own facts, CR-1)
- K1 payment: `means` in (CR-1 op 4: a lump sum no choice avoids) to `households.deposit` (3.4m with bank details) and `households.applicants` (apply by form: `compliance` on them); `penalties` on `claimants.false` (2,000 crowns fine, collector `officials.revenue`; premise A-18); `announced` (4 March, paid from 1 July) and `expires` (once; claim by 31 Dec 2027).
- U1: unclear provision. Component `k1b` (a second payment to `households.separate_filers`) applies only under U1-b; every proposed fact about that class carries `reading: "U1-b"`.
- K2 borrowing: two exchanges, treasury selling to `buyers.domestic` (banks, pension funds, other private buyers) and `buyers.foreign`; `issued` (premise: sold as enacted, judged 0.9).
- K3: `funded` from `taxpayers.future` (premises A-11 and A-4, 0.45, so not reported) and from `recipients.other_spending` (A-11 and "some of the installments are funded by lower spending", judged 0.8). K4: `enforcers` officials.revenue; `funded` by `taxpayers.future` via the bonds (A-11).
- `lenders` is off the controlled list, so the bond buyers are `buyers.domestic` / `buyers.foreign`.

## Round 1 (depth 1: 10 nodes)
- households.deposit: links resources_available_other_uses to consumption (A-1) and saving (A-2); alternative: less household borrowing (A-6); timing: A-15 (delay, 0.25, not reported) and A-5 (borrow before the payment arrives, 0.55).
- households.applicants: same links and A-6; timing for the claim deadline (judged: some file in the last weeks); dominance that the cost of applying is far smaller than 1,000 crowns (judged 0.85), which settles the compliance-against-grant ambiguity.
- households.separate_filers (U1-b): same links; alternative A-7 (reclassification, inverse: splitting households).
- claimants.false: alternative: breach falls under the fine (A-14, A-18).
- buyers.domestic: alternative: lend less to private borrowers (judged 0.85). buyers.foreign, officials.revenue, recipients.other_spending: empty (nothing in section 1 for them).
- treasury: more quantity traded raises the rate (supply_price) for business and mortgage borrowers (A-3, A-17).
- taxpayers.future: A-12 links to saving (substitute) and consumption (input) of every recipient class (the applicants and separate_filers copies were added in the same round after reading round 2's needs; nothing was re-answered).

## Round 2 (depth 2: 8 nodes)
- borrowers.business: rate to investment_target (cost; A-8); investment to capital_stock_economy, long horizon (A-10); dominance on the rate (arithmetic: money recycled by saving is less than the 4.1 bn borrowed, judged 0.9).
- homebuyers: rate to quantity_demanded (own_price; A-8); demand to owners.homes asset_value (supply_price; "supply of homes slow", judged 0.75); same rate dominance.
- households.deposit#2, applicants#2, separate_filers#2: consumption to retailers' quantity_traded (same_act; A-16); saving to the rates (supply; "saved money is lent on", judged 0.8); consumption to homebuyers' demand (A-19, 0.3, not reported).
- borrowers.households, buyers.domestic#2, claimants.false#2: empty (A-17 says household credit rates move little).

## Round 3 (depth 3: 2 nodes)
- retailers: employment and hours (input; A-9); stake in K1 (A-13, 0.45, not reported). borrowers.business#2: empty.

## Answers
From the table: A-1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19 (all used; A-4 at 0.45, A-13 at 0.45, A-15 at 0.25 and A-19 at 0.3 keep their chains unreported). Judged (not in the table): bond buyers would otherwise have lent privately 0.85; applicants file near the deadline 0.8; application cost far below 1,000 crowns 0.85; saved money smaller than the borrowing 0.9; supply of homes slow 0.75; saved money is lent on 0.8; sold as enacted 0.9 (seed); some installments funded by lower spending 0.8 (seed).

## What the format could not hold
- Borrowing as an exchange: `issued` was the nearest fit; its receipts are labelled `non_tax_receipts` (fines, fees), which misnames bond proceeds, and the repayment (K3) and interest have no fact at all.
- K1 as a lump sum is `means`, so the "spend, save or repay" split (CR-4 change in means alone) needs `links` from resources_available_other_uses with relation `input`; no relation says "a use of means".
- Timing: A-5 (borrow and spend before the payment) runs against the engine's "better option, hold back" rule; I used `carry_over` for it and `bring_forward` for A-15, labels that do not describe the acts.
- U1-b shortfall (4.6m payments against 4.1 bn funded): no fact for a rationed lump sum (budget_premises needs a grant on an exchange); not recorded.
- Fraud and duplicates (A-14): only a penalty and an inverse alternative; the payments diverted from households (`outside` margins need a held, charged or granted exchange) are not recorded, and the fall in breach is only against an unfined payment.
- Foreign buyers (30% abroad): no assumption supports a currency link, so none was proposed.
- Per-class duplication: no way to state a link once for the three recipient subclasses; each fact was repeated.
- Consumption stays `ambiguous` (A-1 up against A-12 down, 0.9 and 0.6), and so retailers' sales and employment; the dominance premise needed (how the payment compares with the expected later burden) is not in the figures.
- Magnitudes (A-17 "move little", 35% with thin savings) can only enter as premises, not as sizes.
