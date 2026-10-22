# WE-012 Norvania employer social contribution, expand loop, blind run (loop)

Branch `loop-we012_payroll` (from 86c9546). Files: `seed.json`, `proposals.json`, `answers.json`, `policy.txt` (section 1 as given), `situation.json` (grown situation), `final_output.txt` (engine output of the last run).
Read only: section 1 and the assumption table's ID, Statement, Type, p. Nothing under handbook/05_examples*, cases/we012_payroll (other than my folder) or tests/ was opened. `vocabulary.py` was read to see how names are checked (it counts examples other than WE-012 when listing names).

Result: `DONE in 3 rounds, 11 questions`; 19 node visits (8 + 10 + 1); no `off-list:` lines. The situation holds 15 assumptions (4 in the seed, 11 asked). 26 proposed facts.

## Seed (CR-1: the policy's own facts)

- Exchanges. `e_cov`: employers.covered buy labour from workers.covered (employees paid above the minimum, wage up to the ceiling; buyer price `price_paid`, seller `wage_rate`). `e_mw`: employers.low_wage buy from workers.min_wage ("about 8% of employees earn at or near" the minimum). The split follows the text: the minimum wage is a rule in force that the contribution cannot move, the rest of the wage bill is set by agreements or custom. No held price, no unsatisfied side.
- `charges` K1 on both exchanges (payer buyer, receiver officials.revenue, `tax_revenue`, projection `tax_revenue_vs_static_projection`). `capped_payers` on the e_cov charge: employers.high_wage, because wages above 6,000 bear no contribution, so those employers pay a fixed 240 crowns per such worker (CR-1 0.9: operation 3 below the ceiling, operation 4 above). Receiver is the Tax Agency class because "State Pension Fund" has no class in the list; the Fund is reached by a link in round 1.
- `fixed`: e_cov seller, short horizon, premise A-1 ("money wages fixed for the first year"); e_mw seller, long horizon, premise A-9 (minimum wage plus contribution exceeds what employers will pay for some workers).
- `moves`: e_cov buyer (short, A-1: employers' labour cost takes the rise while wages are fixed); e_cov seller (medium, A-8 and A-12: employers have better alternatives, and workers do not see the contribution as pay for a benefit, so the wage takes it later); e_mw buyer (long, A-9: the wage cannot give, so the employers' cost takes it).
- `incidence`: k1 on e_cov, workers (seller) side, premise A-8. Section 1 says the absence of a pension benefit "matters for incidence"; A-8 is the statement comparing alternatives.
- `unclear` U1 (Labor Inspectorate budget): U1-a rises (`funded` k2_funded by taxpayers), U1-b does not (`fixed_budget` k2_flat, the text's "assumed not"). No premises on either, the reading is the premise.
- `announced` k1 (budget announcement on 10 January, effective 1 July; premises empty, as in WE-013); `compliance` k2 on both employer classes (payroll returns, audits); `enforcers` k2 officials.enforcement (Tax Agency and Labor Inspectorate).
- Not seeded, with reason: held, banned, capped, grants, backstops, discretion, means (the 240 sum is already `capped_payers`), thresholds (the ceiling is a cap on the base, not a line the measure binds above), qualifies (pensions do not depend on the rate), expires (no end), early_price, transfers.
- Seed premises, all from the table with p: A-1 0.85, A-8 0.75, A-9 0.75, A-12 0.9.

## Round 1 (8 nodes at depth 1)

- employers.covered: adjust margin on e_cov over workers.covered `employment, hours_worked` (A-2; the wage is fixed so hiring and hours are what is left); alternatives under k1: `reclassification` (A-3; source: self-employed stay at 8%), `quantity_substitute` (A-5), `non_wage_compensation` for workers.covered (A-15; the exempt vouchers and premiums), `relocation_out_of_area` (A-13); outside margin `informal_activity` on e_cov (A-4); links: informal_activity same_act to workers.informal employment (A-4), reclassification same_act to workers.self_employed employment (A-3), reclassification and informal_activity as substitutes of `tax_revenue_vs_static_projection` at officials.revenue (A-3, A-4: a wage reshaped or hidden is not taxed at 14%), informal_activity same_act to `non_tax_receipts` at officials.enforcement (A-4's second half: penalties enforced at least sometimes; K2 lists fines), quantity_substitute input to input_suppliers quantity_traded (A-5); stake in k1 (A-7).
- employers.low_wage: adjust margin on e_mw over workers.min_wage (A-2); alternatives reclassification (A-3) and quantity_substitute (A-5); outside margin informal_activity (A-4); link output of price_paid to consumers price_paid (A-10, A-14: the labour-intensive service firms, whose rivals bear the same rise and cannot replace labour at the old cost); links to workers.informal and workers.self_employed (A-4, A-3); stake (A-7).
- officials.revenue: link tax_revenue same_act to officials.pension fund_balance, no premise ("the contribution is paid into the State Pension Fund").
- workers.covered: stake (A-7, unions: collective agreements cover 40%); timing bring_forward of `earnings` in the announcement window (A-6, bonuses moved into June; announced k1 is in the seed).
- Empty lists: employers.high_wage (only a fixed sum, nothing to rest a response on), officials.enforcement, taxpayers, workers.min_wage.
- Not proposed for employers.low_wage: the A-15 shift into vouchers (150 crowns against a 1,500 minimum, and the text does not say vouchers count toward the minimum).

## Round 2 (10 nodes at depth 2)

Only one real proposal: officials.pension, link fund_balance same_act to general_fund fund_balance (A-11, the transfer from the general budget is cut by part of the new revenue; source: "that transfer will be reviewed"). Empty lists for consumers, employers.covered#2, employers.low_wage#2, input_suppliers, officials.enforcement#2, workers.covered#2, workers.informal, workers.min_wage#2, workers.self_employed: terminal effects with nothing in section 1 or the statements to carry them on.

## Round 3 (1 node at depth 3)

general_fund: link fund_balance same_act to taxpayers resources_available_other_uses, no premise (CR-8: a smaller call on the general budget leaves more with those who pay into it; the A-11 premise is already on the chain). Taxpayers then sit at depth 4 and are not visited; they show `ambiguous` (U1-a: the extra enforcement cost, if the Inspectorate's budget rises, against the lower transfer) and increase under U1-b.

## Answers

Every question's statement matches an assumption, so all 11 asked answers come from the table (p copied): A-2 0.85, A-3 0.7, A-5 0.75, A-15 0.7, A-13 0.35, A-4 0.7, A-7 0.8, A-10 0.75, A-14 0.85, A-6 0.7, A-11 0.75. Judged: none. (The four seed premises A-1, A-8, A-9, A-12 are in the seed with table p and were not asked again.) I wrote the answers for round 1 together with the proposals, since the statements are the table's own wording; the file runs the same either way.

Not in the table and left out: A-13 (0.35) is below the 0.5 cut-off, so the relocation alternative is derived but not reported (the `-` line in the output). Unused statement: none of A-1 to A-15 is left unused.

## What the format could not hold

- The pension fund has no actor class in the controlled list, so the receiver of K1 is the collecting agency (officials.revenue) and the Fund (`officials.pension`) is reached by a link; `tax_revenue` for the receiver and `fund_balance` for the Fund are two variables for one flow.
- The ceiling: `capped_payers` gives employers.high_wage a loss of means only; the engine still signs `quantity_traded` down for the parties of the exchange the charge sits on and cannot say that the cap's firms have a zero marginal rate. The ceiling not being indexed (more workers cross it over time) has no slot.
- Employers and workers appear as one class on both sides of two exchanges only by my split (covered / low-wage, covered / min-wage); the same firm pays on both and on the part above the ceiling, but a firm cannot be in three classes at once.
- Bonus timing: the timing actor is the chooser, and the chooser of a payment shift is the employer, while the variable (`earnings`) is a receipt. I put the fact on workers.covered, which the engine makes a chooser only through the medium-run wage fall (price_chooser), so the June rush rests on a wage fall rather than on the employers' own choice.
- `relocation_out_of_area` is defined for members' homes, not for operations moved abroad; it is the closest variable, and the fact is unreported at p 0.35.
- Horizon: the wage effect of A-1/A-8 splits into short (employers' cost, fixed wage) and medium (wage falls), but the adjust margin (`employment`, `hours_worked`) on e_cov is signed in the short window only; the medium-run employment fall comes from the charge's `quantity_traded`, not from a group. The long-run (A-8) incidence is a share rank (`tax_share_borne`), with no level.
- Informal and self-employed work have no exchange of their own (no price, no charge), so only quantities (`employment`) are signed for them, and their lower contribution (8%, none) enters only through the revenue-shortfall variable.
- U1 (budget): the reading-split signs for officials.enforcement and taxpayers are in `situation.json` through the engine, but the CLI prints one line per sign, so `enforcement_cost` shows twice.
- Section 1 states the pension formula, 15% informality and 40% coverage as sizes; none of them can be used as arithmetic (no dominance of `arithmetic` kind is available), so no dominance facts were proposed.
