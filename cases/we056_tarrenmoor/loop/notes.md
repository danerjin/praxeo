# WE-056 Tarrenmoor, expand loop (blind run)

Branch `loop-we056_tarrenmoor` from c2e834f. Files: `seed.json`, `proposals.json`, `answers.json`, `situation.json`, `policy.txt` (a copy of section 1). Final run: DONE in 3 rounds, 25 questions (24 from the assumption table, 1 judged). Seed premises (a1 A-1, a2 A-2, a4 A-4, a5 A-5, a23 A-23) are table values and are not counted among the 25. Read: section 1 and the assumption table only; the forbidden folders were not opened.

## Seed (the policy's own facts, CR-1)
- Exchanges: `e_ins` (state-plan members buy insulin from in-state pharmacies), `e_mail` (members who use mail order buy from nonresident-permit pharmacies), `e_unins` (uninsured buy on prescription from in-state pharmacies). Price variables price_paid / net_price_received. The state-plan buyers were split into mail-order users and the rest, and the pharmacies into in-state and mail-order, because U1 treats them differently.
- K2 and K3 as `grants` to the buyer side: K2 paid by `insurers` (e_ins, e_mail), K3 paid by `treasury.insulin_fund` (e_unins). K1 (the $35 cap) as `moves` on the buyer side of each exchange (the buyer's price takes the grant's wedge). Premise A-1 (compliance, payments above cost) on grants and on the buyer `moves`; A-4 (pharmacies price at the Fund's limit) on seller `moves` in e_unins (the Fund pays the seller's own posted price up to a limit, CR-6 1.1).
- `fixed` seller price in e_ins and e_mail, short horizon (contracts set for 2028), A-2.
- `unclear` U1: k2_mail and k1_mail apply under U1-a only; U1-b has none.
- `announced` k2 and k3 on A-23 (introduced January 2027, effective January 2028).
- `means(k2, insurers, out)` (the mandated balance), `compliance`, `enforcers` (Board), `fixed_budget` on the Board with A-5 (existing fee-funded budget), `funded(k3, taxpayers)` (K4, general revenue).

## Round 1 (nine nodes), proposals and why
- buyers.state_plan: alt rationing (A-3, survey sentence), alt pens/analogs (A-7), alt cross-border (A-29), timing bring_forward (A-11), link to mail-order users under U1-b (A-19), links for A-26 (move in), A-28 (deductible), A-7 and A-3 to plans' outlay, stake (A-17).
- buyers.state_plan_mail: link same_act to the mail pharmacies (no premise).
- buyers.uninsured: alt rationing (A-3), timing (A-11), link to OTC buyers (A-8), link to individual-market membership (A-25), outside margin by ineligible attesters (A-15), stake (A-17).
- insurers: alt prior authorization / step therapy (A-6), premium links to insured employers, individual-market buyers and premium tax revenue (A-12), link to pharmacies' net price at 2029 renewals (A-22, A-2, long), steering lowers outlay (A-6), dominance on outlay (A-24), stake (A-17).
- officials.enforcement: fines paid into the Fund (policy sentence).
- retailers.in_state: outside margin (A-16), fines link (A-16), price to uncovered cash buyers (A-4), manufacturers' list price (A-10), yield on e_unins (A-4), stake.
- retailers.mail_order: alt stop shipping (A-18, reading U1-a), alt in-state mail-order entry (A-27, reading U1-b), stake (A-17).
- taxpayers: empty. treasury.insulin_fund: paid_from the general fund (K4), link to manufacturers' assistance (A-9).

## Round 2 (new nodes and revisits)
- buyers.border: links to Lisvane retailers and to in-state quantity (A-29).
- buyers.individual_market: alt dropping coverage (A-14); link to insurers' membership.
- buyers.ineligible: link to Fund outlay (A-15). buyers.otc: link to chains' sales (policy sentence).
- employers.insured_group: alt convert to self-funded (A-13), link to insurers' membership.
- insurers#2: steering lowers analog use (A-6), membership to premium tax.
- producers.assistance: link back to uninsured purchases (A-9). producers.manufacturers: link to Fund outlay (WAC plus 20 percent, policy sentence) and to national buyers' price (A-10).
- Empty: buyers.cash_uncovered, buyers.high_deductible, buyers.state_plan#2, buyers.uninsured#2, officials.enforcement#2, retailers.in_state#2, retailers.mail_order#2, treasury, treasury.insulin_fund#2 (nothing in the text or table to add).

## Round 3
- retailers.chains: one link to producers.human_insulin full cost per unit (A-20 on horizon long, A-21). Empty: buyers.national, buyers.state_plan#3, employers.insured_group#2, retailers.neighbors.
- treasury#2: dominance on tax_revenue, increase (judged premise below), because the premium tax is raised by added premiums (A-12) and lowered by conversions and drops (A-13, A-14, A-25).

## Answers
- From the table (24): A-3, A-7, A-29, A-11, A-19, A-26, A-28, A-17, A-8, A-25, A-15, A-6, A-12, A-22, A-24, A-16, A-10, A-18, A-27, A-9, A-14, A-13, A-20, A-21 (plus the seed's A-1, A-2, A-4, A-5, A-23).
- Judged (1): "Premium tax lost to employers who convert and members who drop coverage is smaller than the premium tax raised by the added premiums." p 0.8. Basis: added premiums are about 0.36 percent of $9.4 billion, and A-13, A-14 and A-25 say only "some".
- No fact uses A-30 (see below).

## Engine output (final)
Reported unambiguous: members' and uninsured price_paid down, quantity up; insurers' subsidy_outlay up; Fund subsidy_outlay up; taxpayers' resources down; pharmacies' quantity_traded, return_on_capital up and compliance cost up; Board's non_tax_receipts up; manufacturers' list price up (national buyers' price up); treasury tax_revenue up (via dominance), general-fund balance down; employers' premium price up and reclassification up; ineligible attesters' legal_breach up; OTC buyers' quantity_substitute down; chains' quantity_traded down; Lisvane retailers' quantity down; human-insulin cost per vial up; manufacturers' assistance supply down. Ambiguous: in-state pharmacies' net_price_received (up from A-4, down from A-22) and the uncovered cash buyers' price that follows it; state-plan product_attribute (A-7 up, A-6 down); enforcement_cost (the Act's work up, other work down). Per reading: mail-order buyers' price_paid (U1-a down, U1-b none) and quantity (U1-a up, U1-b down), mail pharmacies' quantity_traded (up / down) and compliance cost (up / none).
Unreported (below the cut-off): insurers' membership down, individual-market membership down (A-13, A-14, A-25 at 0.55 or 0.4), members' membership up (A-26, 0.2).

## What the format could not hold
1. K1, a cap on the buyer's payment with a third party paying the balance, has no type. I used `moves` on the buyer side plus grants for K2/K3; K1 has no component of its own with an effect, and `held` would have produced a shortage CR-6 1.1 says does not arise.
2. A payer that is not an agency (plans paying the balance) is a chooser only if I add `means` (a transfer no choice avoids), which is a stretch for plans that can steer; without it the A-6 alternative would not fire.
3. An alternative or entry by a seller needs the seller to be a chooser, which needs a moved price. Mail-order pharmacies under U1-a (A-18 stop shipping) and U1-b (A-27 open an in-state mail-order pharmacy) get no chooser, so those two alternatives are in `proposals.json` but derive nothing. A rule that adds paperwork or billing duties for sellers (`terms`) would drag in the moves premise and a spurious price rise; I left it out.
4. Fines on an overcharge (a penalty tied to violation, not to each trade) fit neither `charges` nor `grants`; modeled as an `outside` margin, a link to receipts, and `paid_into` the Fund.
5. Signs that differ by period (A-4 now, A-22 at the 2029 renewals) are one ambiguous sign for net_price_received; link horizons do not become separate windows.
6. Link relations have no "price falls when the buyer's outlay rises" form; I used `supply` (A-22), `input` (premium follows outlay, A-12), `own_price` (A-26, A-28) and `substitute` (A-25, A-9) for direction, not meaning. Variables are borrowed: `membership` for coverage or inflow, `product_attribute` for the analog/pen share (inverse alternative), `reclassification` for converting to self-funded.
7. A chain longer than the depth limit was cut: A-20 and A-21 (human-insulin makers) are one link from retailers.chains with two premises instead of two links through the producers, since a producers node would be depth 4.
8. A-30 (money-term trend after 2028) and the fiscal-note comparison ($19 million against about $39 million, and the 2,000 OTC buyers) have no home: there are no magnitudes, counterfactual baselines or quantities in the format.
9. Self-funded plans and national programs (the exempt groups) have no exchange of their own; they enter only as `buyers.ineligible` (A-15) and `buyers.cash_uncovered`.
10. U1-a for uninsured residents' mail orders (the Fund billed by nonresident pharmacies) is not represented; one nonresident exchange covers state-plan mail order only.

Environment note: the shared scratchpad directory is used by other concurrent runs (a file there was overwritten by another task); scratch files for this run were kept in the untracked `scratch056/` of the worktree.
