# WE-034 expand loop, blind run (notes)

Branch `loop-we034_teravel` (from 57f997f). Read only section 1 and the assumption table (ID | Statement | Type | p). Ids in the
files are lower-case without the hyphen (A-5 is `a5`) because the engine needs atoms. Rounds: 3 (stopped at depth 3). Node visits:
16 (5 + 7 + 4). Proposals: 38 (16 node keys, 5 of them with an empty list). Premise questions: 24 (21 from the table, 3 judged;
`n1` in the seed is a fifth judged statement). Final engine output: DONE in 3 rounds, 24 questions, no `off-list` lines.

## Seed (policy's own facts, CR-1)

- Exchanges. `e_train`: net-training employers (`employers.trainers`) buy, trainees (`workers.trainees`) sell, wage in `wage_rate`.
  `e_hire`: net-hiring employers (`employers.hiring`, rivals and start-ups) buy, bound workers (`workers.bound`) sell. The split is
  A-15/A-16 ("net trainers", "some firms hire more trained staff than they train"); the policy treats the two roles differently
  (the Act worsens the first, improves the second). I did not model an incumbent-employer-keeps-worker exchange.
- `terms` (voiding a restraint is a change in the bundle with no payment, CR-1/CR-5 1.2):
  k1 on `e_train`, buyer worse [A-2, A-5]; k1 on `e_hire`, buyer better [A-2, A-28] (hirers no longer bear litigation risk);
  k1 on `e_hire`, seller better [A-2, A-1]; k1d (the "forfeiture for competition" clause K1 names) on `e_hire`, seller better
  [A-2, A-29]; k1b (garden leave void) on `e_hire`, seller better [A-2, A-26]; k1c (repayment term void) on `e_train`, buyer
  worse [A-2, A-26]. A-2 is the enforcement premise on all.
- `unclear`: U1 (K3(c), readings U1-a no extra component, U1-b adds k1b) and U2 (readings U2-a adds k1c, U2-b none). Components
  that exist under one reading only are the ones the reading differs in.
- `moves`: `e_hire` seller (wage) [A-7]. Only seedable (not a Proposal part), so it is in the seed.
- `announced` k1 [n1: "Employers and workers expect the Act to take effect on 1 January 2026 once it has passed", p 0.9, judged from
  "introduced 3 February 2025 with the governor's public support. It passed on 12 June 2025 and takes effect on 1 January 2026"].
- K4 `compliance` on both employer classes; K5 `enforcers` officials.enforcement; `fixed_budget` K5 [A-18] ("No new appropriation").
- Left out of the seed on purpose: K2/K3 (no instrument; they enter as alternatives), K5 private remedies (no field fits, see below).

## Round 1 (depth 1): hiring, trainers, officials.enforcement, workers.bound, workers.trainees

- employers.hiring: alternatives `enrollment` (trains less, A-16) and `relocation_out_of_area` (stays or comes to Teravel, A-24);
  link to `intermediaries` (recruiters, A-21); link `same_act` to `workers.mossgrave` job_changes (A-25: K1 applies "whatever law the
  contract chooses"); stake (A-13).
- employers.trainers: alternatives `reclassification` four ways (A-4 preserved forms; A-19 trade-secret/non-solicit claims; A-11
  partnership buy-ins as `employers.trainers.practices`, the part K2 treats differently; A-12 token equity), `relocation_out_of_area`
  (A-22), `earnings` of bound workers (A-10 unvested pay and retention bonuses), `term_prevalence` under reading U1-a (paid notice
  preserved) and under U2-b (repayment preserved), each tied to its reading; yield (A-15) with a link yield -> investment_target
  (judged premise "Net trainers cut employer-funded training when its expected yield falls", p 0.8); margin `outside` legal_breach
  (A-20); stake (A-13).
- workers.bound: alternative to the improved option, leaving the field (A-8, as `workers.bound.out_of_field` job_changes); timing on
  job_changes, `bring_forward` (A-14, those who can wait) and `carry_over` (A-27, those who move late in 2025); link to `entrants`
  (A-3 firm start); stake.
- workers.trainees: alternative `enrollment` (A-5); link to `entrants` entry_rate, long horizon (A-30).
- officials.enforcement: empty. Its effects are enforcement_cost up (enforcer) and down (fixed budget, A-18); nothing in the text
  reaches anyone from them.

## Round 2 (depth 2): hiring#2, trainers#2, trainers.practices, entrants, intermediaries, workers.bound#2, workers.bound.out_of_field

- hiring#2: links enrollment -> trainees' quantity_traded (A-16) and relocation -> `neighboring_jurisdictions` employment (A-24).
- trainers#2: same_act link relocation -> neighboring_jurisdictions employment (A-22); `substitute` links reclassification and (under
  U1-a) term_prevalence -> bound workers' job_changes (judged premises: "Substitute restraints such as non-solicitation, unvested pay
  and retention bonuses deter some moves to rivals", 0.85; "A paid notice period of six to twelve months keeps the worker out of the
  field", 0.9, the latter is U1's own description of the provision); yield link reclassification -> return_on_capital (A-4), with
  dominance (decrease) on return_on_capital and investment_target [A-6] (substitutes do not fully restore the protection).
- trainers.practices: substitute link to job_changes (judged "deter" premise).
- entrants: supply link entry_rate -> customers price_paid [A-23]; stake (A-13).
- workers.bound#2: same_act link quantity_traded -> job_changes (no premise: a move to a rival is a new trade in `e_hire`); output
  link wage_rate -> customers price_paid [A-23, the staff-pay-is-a-cost half]; dominance job_changes increase [A-9].
- intermediaries, workers.bound.out_of_field: empty (nothing in the text carries the effect further).

## Round 3 (depth 3): customers, entrants#2, neighboring_jurisdictions, workers.bound#3

All empty. customers (price_paid) and neighboring_jurisdictions (employment) are ambiguous, which reaches no one definite; the
others had no new need.

## Answers

- From the table (21): a16, a24, a21, a25, a13, a4, a19, a11, a12, a22, a10, a15, a20, a8, a14, a27, a3, a30, a6, a23, a9 (a6, a23
  and a9 asked in round 2; the rest in round 1). a2, a28, a1, a5, a7, a18, a26, a29 are seed premises.
- Judged (not in the table): n1 (seed), "Net trainers cut employer-funded training when its expected yield falls" 0.8, "Substitute
  restraints such as non-solicitation, unvested pay and retention bonuses deter some moves to rivals" 0.85, "A paid notice period of six
  to twelve months keeps the worker out of the field" 0.9. Each is a plain response or description premise that section 1 or the table
  implies but does not state; n1 comes from the dates in section 1.
- Table statements with two concepts (A-23, A-26, A-30 with its reference to C-3, A-9's "(dominance premise, CR-12e)") were reused
  verbatim so they match the table.

## Final run

Reported (R) and not reported (-, p below cut-off) results are in `situation.json` (run with `--out`). Notable: wage_rate of bound
workers is ambiguous (buyer-better terms raise it, seller-better terms lower it); job_changes increases only because of the A-9
dominance premise, and is ambiguous in the announcement window (A-14 against A-27); term_prevalence is ambiguous by reading
(increase except under U1-b with U2-a, where no preserved alternative exists); employers.trainers return_on_capital and
investment_target decrease only via A-6 dominance; employers.trainers quantity_traded and workers.trainees quantity_traded fall;
bound workers' and hirers' quantity_traded rise; entry_rate rises (A-3), its fall from A-30 is unreported (0.4); customers price_paid
is ambiguous (supply vs staff-pay cost, A-23); Mossgrave link (A-25, 0.4), outside breach (A-20, 0.35) and token equity (A-12, 0.3)
are unreported.

## What the format could not hold

- Terms effects on quantity apply to both parties and a terms fact on the seller side also moves the money price (lower), so one
  void restraint gives wage_rate both a rise (rival bidding, A-7) and a fall (the freer contract is worth something to the worker).
  There is no way to say which one the text means, so it stays ambiguous.
- Timing: the chooser must be a party of the exchange, so A-27's sub-group (those with a suit pending) cannot be its own class;
  I used `carry_over` for them only to take the sign (an increase in late-2025 moves), which is not what carry_over means.
- Dominance (A-9, A-6) settles the sign of the variable it names but does not stop the opposed chain propagating downstream.
- `moves` is seed-only and needs a premise on the other side's response; the fall in trainee pay (A-5) has no premise in the table, so
  no `moves` on `e_train`.
- K5's remedies ($5,000 per worker, damages, fees, civil penalties up to $10,000) are a cost on breach, not a payment attached to a
  trade: no charge fits, and nothing for the employer suits that stop (about 400 a year) or the worker suits that start
  (officials.adjudication); only the Bureau's fixed budget was recorded.
- The retroactive application to existing contracts and pending cases is carried only by the timing facts; K4's 1 March 2026 deadline
  has no place.
- Mossgrave workers (60,000 commute each way): a class outside the exchanges can be reached only through a link, so A-25 is a link
  and falls below the cut-off; the commuter flow itself has no field.
- A-17 (non-solicitation bars only contact the worker initiates) has no fact to hang on: it weakens one substitute inside the
  `reclassification` alternative, which is not separately signed. Not used.
- `reading` on a link/alternative only selects the facts; there is no way to say a reading changes the size of a response.
