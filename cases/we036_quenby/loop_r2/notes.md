# WE-036 Quenby, expand loop blind run (loop_r2)

Inputs read: section 1 of the example (saved as `policy.txt`) and the ID, Statement, Type and p columns of its assumption table. Nothing else of the example, nothing under `05_examples_core/`, nothing in the older `cases/we036_quenby/` files or `tests/`. Premise atoms in the seed are `a1`..`a37` (the table's A-n); the loop's own atoms are `q<n>_...`. Final: 3 rounds, 15 nodes proposed for, 15 questions put to the decider (25 premises in all with the 10 in the seed).

## Seed (CR-1: the Act's own facts)

- Exchange e1: employers.bound (50+ FTE, "Employers with 50 or more FTE") buy, workers.full_time (30+ hours) sell; price variables price_paid / wage_rate.
- k1_offer: charge paid in kind to the workers (`non_wage_compensation`), `quantity_premises` a7 (cover at 30% is worth less to the worker than it costs), branch premises a1 (K1 binds for the unoffered and under-offered), a2 (some offer). It is the "play" branch.
- k1_pay: charge of $3,000 per uncovered head to Revenue (`non_tax_receipts`), branch premises a1, a4 (some pay), `capped_payers` employers.capped (K4, the 45 large firms).
- moves: seller (a6, wages above the minimum adjust in the medium run) and buyer (a37, the wage response is partial, so the employer's cost rises).
- thresholds: k3 (50 FTE, employers.near_threshold, employment, a14) and the 30-hour line (workers.near_hours_line, hours_worked, a10).
- announced: k3 (a15, owners know from January 2027 that 2027 decides 2028), k1_offer and k1_pay (a21).
- compliance (employers.bound), enforcer k5 (officials.enforcement), funded k5 by taxpayers (a29, the $4.1 million is new general-fund money).
- Left empty: held (the Act holds no price; the existing minimum wage and overtime rules are not the Act's), capped/banned/grants/expires/backstops/discretion/means/transfers/qualifies/early_price/fixed_budget, and everything the loop supplies.

Seed revision. The first seed had no `buyer_price_var` and no buyer `moves`. Round 2 of that run showed that the employers' side of the wedge had no price variable at all (their cost per head never appeared, so no cost link could leave the employer class). I restarted from a corrected seed with `buyer_price_var: price_paid` and `moves(e1, buyer, a37)`; round-1 proposals and answers were kept and extended with the cost links. The counts above are for the final run only.

## Round 1 (7 nodes)

Nodes and the proposals made (each rests on the sentence or assumption named):

- employers.bound (compliance cost up, price_paid up, quantity_traded down, resources down):
  - alt k1_offer to workers.part_time employment (a10; "Employees averaging under 30 hours" are exempt);
  - alt k1_offer to workers.full_time hours_worked (a11, extra hours from existing full-timers substitute for heads);
  - alt k1_pay to employers.capped quantity_supplied (a34, agency workers from capped staffing firms; "Agency workers count for the agency");
  - margin outside, legal_breach (K5: "Misreporting: twice the unpaid charge"; premises a18 split in two: Revenue cannot cheaply verify reported offers / some firms report offers not made);
  - stake k1_offer (a19);
  - asset factor_owners.specific on the buyer side (a21) and yield employers.bound (a22, unbound rivals in local product markets limit pass-through);
  - links from price_paid: cost to own quantity_supplied (a22), output to consumers price_paid (a24), cost to producers.tradable quantity_supplied (a26, Tarnley has no such law).
- employers.capped: stake k1_pay (a19, "45 large firms").
- employers.near_threshold: alt reclassification (a17, contracting out and franchising; the common-control rule closes splitting); timing carry_over of employment (new premise: firms near 50 can hold their 2027 average FTE below 50; "Status for 2028 is decided by the firm's average FTE over 2027"); stake k3 (a19).
- workers.full_time (non_wage_compensation up, wage down, trades down): alt to workers.part_time, to employers.unbound and to neighboring_jurisdictions (a8 first clause; new premise for Tarnley from "35,000 people commute across the border"); link non_wage_compensation same_act insurers.health quantity_traded (the plan is bought from an insurer, no premise); link non_wage_compensation substitute patients.icp quantity_demanded (a28, ICP care); stake (a19).
- officials.enforcement, taxpayers, workers.near_hours_line: empty (nothing in section 1 or the statements reaches anyone else from them; A-36 is arithmetic on receipts against the appropriation and has no variable to sit on).

## Round 2 (7 nodes)

employers.unbound, factor_owners.specific, neighboring_jurisdictions, workers.part_time: empty (their only effect is an ambiguous or one-way change with nothing further in the text). insurers.health: stake (a19); link complement to providers.health quantity_demanded (a27, newly covered use more care billed to insurers). patients.icp: link same_act to taxpayers subsidy_outlay (a32, the ICP pays per claim). producers.tradable: link substitute to neighboring_jurisdictions quantity_supplied (a26).

## Round 3 (1 node)

providers.health: empty (the ICP side is already carried by a28 / a32).

## Answers

From the table (p taken as is): a11 0.65, a34 0.55, a19 0.85, a22 0.65, a17 0.55, a24 0.40, a26 0.65, a28 0.70, a27 0.75, a32 0.60; seed premises a1 0.9, a2 0.75, a4 0.9, a6 0.8, a7 0.6, a10 0.75, a14 0.7, a15 0.75, a21 0.7, a29 0.9, a37 0.9.
Table, but only part of a statement (p of the whole used for the part): A-8's first clause "Workers at payers have some alternative to bound full-time work (firms under 50, part-time work, Tarnley)" 0.85; A-18 split into "Revenue cannot cheaply verify reported offers" and "Some firms report offers not made" 0.55 each.
Judged (no matching assumption): "Firms near 50 FTE can hold their 2027 average FTE below 50" 0.85 (section 1: status is the 2027 average, and the firms are named); "Workers at payers can take jobs in Tarnley" 0.70 (35,000 commute daily, but only from Marisport).

## Final engine output

36 consequence lines, 35 reported (the one unreported, consumers price_paid up, rests on a24 at 0.4). Ambiguous: employers.unbound employment, neighboring_jurisdictions employment, workers.part_time employment. They come from the workers' class being both on the paying side of the wage change (worse) and the receiving side of the in-kind term (better, as receiver of k1_offer). See `situation.json` for the final record.

## What the format could not hold

- Held prices that exist in the counterfactual: the minimum wage (A-9) cannot be a `held` fact of the loop (PARTS excludes held), so the floor under the wage fall, and the rule that makes the pressure go to hours and employment instead, is not there. `adjust` margins need a `held` to be burdened, so the wage-stickiness and hours/benefit margins (A-3, A-6, A-9) were only carried through `moves`.
- Two readings (U1-a / U1-b, seasonal workers counted or not) and the seasonal firms (A-30, A-33): no field for a reading or for a class defined by an unclear provision.
- Status set by the average over the year before (A-15, A-31, delay not loss): `announced` + `timing` give only an announcement-window decrease; delayed growth is not expressible (`qualifies` is for a right that is created, not one avoided).
- The cap (K4, A-12, A-13): `capped_payers` has no premise, so "stay above 100 uncovered" cannot be tied to the cap; a capped firm's fixed marginal cost is stated but A-12 sits nowhere.
- The two-sided choice (play or pay): the payer has two charges as separate components with separate branch premises; there is no way to say that one replaces the other (their effects add).
- A threshold's actor is both "those near the line" and the chooser; for the 30-hour line the chooser is the employer but the variable is the worker's hours, so the actor had to be workers.near_hours_line.
- A receiver who is also a party (workers) is `better` and `worse` at once, so the engine gives the workers' alternatives ambiguous signs unless a dominance premise is stated; none of the table's premises says which outweighs (A-35 and A-37 come close), so none was proposed.
- Product standard K2, gross versus net burden, general-fund budget identity (A-29 with A-36): no fact type; A-36 is a figure comparison and could be a `dominance` of kind arithmetic only if both sides were variables of one class.
- Wage and benefit stickiness as a premise (A-3) works against `moves` seller (a6) in the same short window; the engine has no horizon on `moves`.
