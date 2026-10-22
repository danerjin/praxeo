# WE-036 Quenby Fair Share Health Cover Act: blind expand-loop run (loop_r4)

Read: section 1 (policy.txt, copied from the extracted file) and the assumption table only. Handbook examples and any other
file under cases/we036_quenby/ and tests/ were not opened. Vocabulary from `--vocab --exclude WE-036`. No `off-list:` line was
printed in any run. Answers: 20 of the 21 questions are table assumptions (kept with their p); one was judged.

Assumption ids in the files are the table ids in lower case without the hyphen (A-8 is a8); component and exchange ids are
lower case because the ASP facts need it.

## Seed (policy's own facts, CR-1)

- Exchanges: three labour exchanges, buyer employers, seller workers, price var wage_rate on the workers' side.
  `e_off` (employers.offering / workers.at_offering_firms: bound firms that newly offer or upgrade), `e_pay`
  (employers.paying / workers.at_paying_firms: bound mid-size firms that pay), `e_seas` (employers.seasonal /
  workers.at_seasonal_firms: the ~380 firms with 30 to 49 year-round FTE; only live under U1-a).
- Charges (K1 play or pay, one branch per component): `k1_offer_new` (A-2) and `k1_offer_upgrade` (A-5) on e_off, in kind,
  receiver workers.at_offering_firms, non_wage_compensation, quantity_premises A-7 (cover is worth less to the worker than its
  cost), branch premises A-1 plus A-2 or A-5. `k1_pay` on e_pay, receiver officials.revenue, non_tax_receipts, branch A-1 and
  A-4, `capped_payers` employers.capped (K4, 45 firms). `k1_pay_seasonal` on e_seas (A-33, A-4), U1-a only.
- moves (seller wage takes the change): e_off A-6; e_pay A-6, A-8; e_seas A-6, A-8 (reading U1-a).
- fixed (seller wage cannot move in the period): R1 minimum wage (A-9) and pay scales (A-3), as two separate facts so that either
  one suffices; for e_seas under U1-a.
- thresholds (K3, A-14): employers.near_threshold on employment; `k3_seasonal` for employers.seasonal (U1-a only). announced: K3 (A-15)
  and K1 branches (no premise: signed 4 Jan 2027, effective 1 Jan 2028).
- unclear U1: U1-a = seasonal workers count (components k3_seasonal, k1_pay_seasonal, k5_seasonal); U1-b = left out (none).
- compliance K5 (employers.offering, paying, capped; K5_seasonal under U1-a), K2 (insurers); enforcers K5 officials.revenue,
  K2 officials.enforcement (the Department of Insurance); funded K5 by taxpayers (A-29, new appropriation).
- Not used: grants, capped, banned, expires, qualifies, backstops, discretion, means, transfers, fixed_budget (no such provision;
  the $4.1 million is new money, so no fixed budget).

## Round 1 (engine run 1: 12 nodes at depth 1; proposals, then 21 questions)

Nodes: employers.paying, employers.offering, employers.capped, employers.near_threshold, employers.seasonal, insurers,
officials.enforcement, officials.revenue, taxpayers, workers.at_offering_firms, workers.at_paying_firms,
workers.at_seasonal_firms.

- employers.paying (14 proposals). Adjust margins on workers.at_paying_firms: hours_worked (A-10, rescheduling to under 30,
  "Employees averaging under 30 hours" is exempt) and employment (A-11, extra hours substitute for heads). Outside margin
  legal_breach (A-18, misreporting; the Act has twice the unpaid charge). Alternatives: reclassification (A-10; A-30, engagements
  under 60 days), quantity_substitute at employers.capped (A-34, agency workers from capped staffing firms, "Agency workers count for
  the agency"). Stake (A-19). Asset for owners.paying (A-21), yield (A-22). Links: quantity_traded input to own quantity_supplied
  (no premise), then quantity_supplied substitute to employers.small (A-22), supply to customers price_paid (A-24, p 0.4, so
  unreported), substitute to sellers.foreign (A-26, Tarnley); legal_breach substitute to officials.revenue non_tax_receipts (A-18).
- employers.offering (8): same hours and employment margins (A-10, A-11), reclassification alternatives, stake, asset for
  owners.offering (A-21), output links as for payers.
- employers.capped (1): stake (A-19). Nothing on exit or hiring: A-12 and A-13 say the cap leaves no marginal charge and does not
  decide operation, so there is no margin to propose.
- employers.near_threshold (5): alternative reclassification (A-17, contracting out and franchising), timing carry_over (A-31, part of
  the growth held back is delayed), link employment yield to owners.near_threshold asset_value (A-16), same_act to
  workers.at_near_threshold_firms, stake (A-19).
- employers.seasonal (4): reclassification (A-30), adjust margins (A-10, A-11), stake. insurers: stake (A-19).
- officials.revenue (2): receipts yield to treasury fund_balance (policy: "Charges are paid into the general fund"); dominance on
  non_tax_receipts, kind arithmetic, A-36 (misreporting does not outweigh collections). officials.enforcement, taxpayers: none.
- workers.at_offering_firms (8): job_changes alternatives (A-35, near the margin), stake for unions (A-19, under this node because
  unions are reached through the workers), links from non_wage_compensation: substitute to quantity_substitute (A-20, individual
  plans), complement to quantity_complement (A-27, more care), complement to insurers quantity_traded (no premise), substitute to
  treasury subsidy_outlay (A-28 and A-32, ICP pays per claim), substitute to treasury tax_revenue (judged premise: part of the cost of
  new cover comes out of taxed pay, R2 excludes premiums and taxes wages).
- workers.at_paying_firms (4): job_changes alternative (A-8), stake for unions, input link to employers.small employment (A-8),
  supply link to workers.at_small_firms wage_rate (A-37, partial response). workers.at_seasonal_firms (1): job_changes (A-8).

Answers: the first rerun printed 21 questions, all new statements. 20 from the table: A-10, A-11, A-16, A-17, A-18, A-19, A-20,
A-21, A-22, A-24 (0.4), A-26, A-27, A-28, A-30 (0.4), A-31, A-32, A-34, A-35, A-36, A-37. Judged (not in the table, 0.8): "Part of the
employer's cost of newly offered cover comes out of taxed pay." (R2 excludes premiums from income and wages are taxed; with A-6, wages
adjust; the same 0.8 as A-6.) The seed's own statements (A-1 to A-9, A-14, A-15, A-29, A-33) were already in the seed.

## Round 2 (engine run 3: 18 nodes at depth 2, among them revisits)

- employers.small: supply link to customers price_paid (A-22), same_act to workers.at_small_firms employment, stake (A-19).
- employers.capped#2: input link from quantity_substitute (agency work) to workers.at_capped_firms employment.
- employers.near_threshold#2: same_act from reclassification to contractors quantity_supplied (A-17).
- treasury: tax_revenue yield to fund_balance; dominance on fund_balance, arithmetic, A-36 (receipts, misreporting and income tax lost
  are opposite chains on the balance).
- workers.at_offering_firms#2: quantity_substitute input to insurers.individual quantity_traded (a subclass for the individual market);
  quantity_complement input to sellers.complements quantity_traded (care providers).
- workers.at_small_firms: output link from wage_rate to customers price_paid (A-22).
- Empty lists: employers.offering#2, paying#2, seasonal#2, insurers#2, owners.near_threshold, owners.offering, owners.paying,
  sellers.foreign, unions, workers.at_near_threshold_firms, workers.at_paying_firms#2, workers.at_seasonal_firms#2 (effects reach
  no one the policy or the table gives a link to).

No new question in this round (all statements reused).

## Round 3 (engine run 4: 8 nodes at depth 3)

insurers.individual: stake (A-19, reused). contractors, customers, employers.small#2, sellers.complements, treasury#2,
workers.at_capped_firms, workers.at_small_firms#2: empty. Final run: DONE in 3 rounds, 21 questions, 38 nodes (12 + 18 + 8),
59 proposals. Output in engine_output.txt, final record in situation.json.

## What the format could not hold

- A premise on the comparison of alternatives (A-23, workers' alternatives clearly worse than employers' in the medium to long run,
  which decides tax_share_borne) has no fact type: dominance only settles an ambiguous sign, and no sign is ambiguous there.
  A-12 and A-13 (capped firms stay above 100 and do not leave) also only appear as the absence of a margin.
- `charge_capped` takes the payer's total as a fixed sum but `c_qty` still lowers trades for every party of the exchange, so the
  45 capped firms had to be left out of the exchange's parties (e_pay holds the uncapped payers) and appear only as a payer of the
  charge; their 62,000 workers have no exchange of their own. A cap that becomes binding by size (100 uncovered head count) cannot
  be written.
- An in-kind branch needs its receiver to be a party to the same exchange, so play and pay needed three exchanges (offering,
  paying, seasonal) and the two ways of offering (new, upgrade) became two components on the same exchange, each with its own
  branch premise. The choice between branches (each firm picks the cheaper) is only the premise that some firms take each.
- Budget identities: the fund balance cannot take the appropriation outlay (no link relation turns a rise in `enforcement_cost`
  into a fall in `fund_balance`), nor the fall in ICP outlay; the sign of the balance rests on the A-36 dominance premise, and
  `subsidy_outlay` and `tax_revenue` reach the treasury but do not enter the balance except through the tax link.
- A-31 (growth held back is delayed, not lost) can only be written as a carry_over timing in the announcement window; the later
  catch-up has no window.
- Medium-term wage flexibility (A-6) and short-run stickiness (A-3, A-9) sit in the same window: the engine gives wage_rate a
  decrease (moves) and the pressure on other terms (fixed) together, with no horizon split.
- Seasonal U1 readings: the components that differ were duplicated (`k3_seasonal`, `k1_pay_seasonal`, `k5_seasonal`); the consequences
  are reported per reading, with `none` under U1-b.
- No place for the Tarnley border as a market (35,000 commuters): it appears only inside A-8 (job_changes) and A-26 (sellers.foreign).
- Subclass names invented for the actors the policy implies but the list lacks: owners.paying/offering/near_threshold,
  workers.at_*_firms, insurers.individual, contractors (listed), workers.at_capped_firms; `insurers` was used for the group-plan side.
- A-3 was used as a `fixed` premise (stickiness) even though it is an empirical premise rather than a rule in force.
