# WE-055 Aldenmoor home inspector licensing: blind expand-as-you-go run

Read: section 1 of WE-055 and, in its assumption table, the columns ID, Statement, Type, p. `policy.txt` is section 1 verbatim.
Not opened: sections 2 to 9, the "If false" and "Evidence" columns, the Report, the consequence list, Corrections, Gaps,
`handbook/05_examples_core/`, the existing files under `cases/we055_aldenmoor/` and `tests/`.

Disclosure of one slip: my first command to print the assumption table ran to the end of section 10 and also printed the
"Final check before the report" paragraph that follows the table. It names consequence ids (C-n) and some chains in
words (entry has no rush, agents' and schools' lobbying, grandfathered earnings, enrollment by window, and the like). I did not
use it, but I had seen it, so its influence on a few judgment calls cannot be ruled out. I tried to decide each point from section 1
and the table alone and say below what each rests on. A reader scoring this run for blindness should treat it as
"table plus a glimpse of the check list".

Result: DONE in 3 rounds, 12 distinct actor classes (19 node visits: 8 + 9 + 2), 21 proposed facts, 14 questions
(13 answered from the table, 1 judged; the 9 seed premises are separate, see below). Final output is in `final_output.txt`.

## Seed (`seed.json`), the policy's own facts (CR-1)

- Exchanges: `e_unlic` (buyers.homebuyers buy an inspection from inspectors.unlicensed) and `e_lic` (from inspectors.licensed).
  Price variables price_paid / net_price_received. No price is held, so no unsatisfied side and no criteria.
- `banned` K1 on `e_unlic` (license requirement: those without a license may not inspect), premises a1 (A-1, binding) and a3 (A-3,
  enforcement despite complaint-only).
- `charges` on `e_lic`, all `basis: operating` (sums fixed per inspector): k1_fee (license, exam and application fees, to officials.board,
  `non_tax_receipts`); k1_training ($3,200, to schools.training, receipt variable `enrollment`, `branch_premises` A-2: some incumbents who
  cannot be grandfathered train, the policy gives them the choice train / grandfathering / stop); k1_insurance ($1,800 a year to
  insurers.liability, receipt variable `quantity_traded`, branch premise A-27: some carried no insurance before).
- `moves`: the buyers' price takes the change, premises A-8 (replacement is partial) and A-33 (cost per inspection does not fall).
- `qualifies` K2 for inspectors.nearline on `quantity_supplied` (grandfathering by history in a window after enactment), premise A-12.
- `announced` K1, K2, k1_training (enacted 3 June 2026, effective 2027 and 2028), premise s1. `expires` K2 (the application window
  closes 31 December 2027), premise s2. Both s1 and s2 are judged (see answers below).
- `compliance` K1 for inspectors.licensed and K4 for agents.realestate; `enforcers` K3 officials.board; `funded` K3 by inspectors.licensed
  ("funded by license, exam and application fees"; no premise, the text states it).
- Left out because section 1 gives nothing for them: `held`, `capped`, `grants`, `backstops`, `discretion`, `means`, `transfers`,
  `early_price`, `thresholds`, `fixed_budget`.
- Seed assumptions: a1 = A-1, a2 = A-2, a3 = A-3, a8 = A-8, a12 = A-12, a27 = A-27, a33 = A-33 (p from the table); s1, s2 judged.

## Round 1 (depth 1): 8 nodes, 14 questions

Pending nodes: agents.realestate, buyers.homebuyers, inspectors.licensed, inspectors.nearline, inspectors.unlicensed, insurers.liability,
officials.board, schools.training.

Proposals (source sentences are quoted in `proposals.json`):
- buyers.homebuyers (2): alt `informal_activity` (A-9: some go without or use an unlicensed inspector); link price_paid -> substitute
  -> engineers.exempt quantity_traded (A-19, "Licensed professional engineers and architects" are exempt).
- inspectors.licensed (7): alt exit to a new class workers.alternative_work, measured by `employment` (A-7, part-timers whose margin
  is gone); alt staying in practice (A-15, a license not renewed for 12 months must be re-earned); link number_of_sellers -> supply ->
  its own net_price_received (A-8 and A-20: the excluded supply is not replaced); yield on the e_lic seller side (A-1) and a yield link to
  inspectors.entrant entry_rate (A-32); timing k1_training enrollment bring_forward (judged premise from the course and deadline dates);
  stake in K1 (A-17, the association).
- inspectors.nearline (3): outside legal_breach in e_lic (A-29, overstated counts); link quantity_supplied -> supply -> own
  net_price_received (A-13, fees cut to win jobs); link quantity_supplied -> substitute -> inspectors.rivals quantity_supplied (A-14,
  total inspections set by home sales). The two links proved inert (below).
- inspectors.unlicensed (4): outside informal_activity in e_unlic (A-16); alt exit to workers.alternative_work (A-7); alt moving work
  to a new class inspectors.linmouth, measured by quantity_traded (A-28); link quantity_traded -> substitute -> inspectors.licensed
  quantity_traded (A-10).
- agents.realestate (1): stake in K1 (A-17). schools.training (1): stake in K1 (A-17).
- insurers.liability and officials.board: empty (nothing in section 1 or the table for either beyond what the seed gives).

Answers: all from the table except two. From the table: A-17 .85, A-9 .6, A-19 .6, A-7 .7, A-15 .6, A-20 .65, A-32 .65, A-29 .45,
A-14 .75, A-16 .7, A-28 .65, A-10 .65. A-13 .55 is the table's "They win the extra jobs mainly by cutting fees" with the pronoun
replaced by "Near-line inspectors" so the statement stands alone (same premise). Judged: "Inspectors who must train enroll in the first
approved courses rather than wait for the 2027 deadline" 0.7 (no table row; the dates are in section 1, the behaviour is my reading).

## Round 2 (depth 2): 9 visits, 4 new nodes, 0 new questions

New nodes: engineers.exempt (quantity_traded up), inspectors.entrant (entry_rate down), inspectors.linmouth (quantity_traded up),
workers.alternative_work (employment ambiguous). The five others were revisits (new effects reached them) and returned the same
proposals, which the loop drops as duplicates.
- engineers.exempt: link quantity_traded -> supply_price -> own net_price_received (A-20).
- inspectors.entrant: link entry_rate -> supply -> buyers.homebuyers price_paid (A-33 and A-32: long-run entry below the counterfactual
  flow, cost not falling). Premises already answered.
- inspectors.linmouth: empty.
- workers.alternative_work: dominance, direction increase, kind empirical, on A-7. The ambiguity came from the engine itself: the
  license holders who stay see their net price rise (CR-4 means effect) against the charge, so the exit alternative has a worse chain and a
  better chain. A-7 ("they stop") is the only statement that says exit outweighs; I used it as the dominance premise. This is the one
  place I stretched a table statement beyond what it literally says.

## Round 3 (depth 3): 2 visits (engineers.exempt, workers.alternative_work), both revisits; nothing new proposed.

## Final engine output (30 lines; 29 reported)

Reported: agents compliance_cost up, lobbying up, resources down; buyers informal_activity up, price_paid up, quantity_traded down;
engineers quantity_traded up, net_price_received up; entrants entry_rate down; licensed: compliance_cost up, employment ambiguous,
enrollment (announcement) ambiguous, lobbying up, net_price_received up, number_of_sellers down, quantity_traded up, resources down,
return_on_capital down; Linmouth quantity_traded up; nearline quantity_supplied (announcement) up, resources down; unlicensed
informal_activity up, quantity_traded down; insurers quantity_traded up; Board enforcement_cost up, non_tax_receipts up; schools
enrollment up, lobbying up; workers.alternative_work employment up. Unreported: nearline legal_breach (A-29 at .45).

## What the format could not hold

- Readings of an unclear provision (U1). K4 forbids agents to "direct, steer or require"; under U1-a nothing changes, under U1-b agents lose
  recommendations. The Situation has no per-reading facts and readings get no probability, so only K4 compliance cost is recorded. The
  referral exchange has no price, and `banned` on it would impose the U1-b reading on both parties.
- Information effects (CR-11): that buyers can see the license (A-5), the competence the training conveys (A-4), the national
  certification (A-30), engineers advertising a license (A-21), and quality received by priced-out buyers (A-26). Links only move
  quantities and prices by fixed direction rules, so `quality_information` cannot be derived without writing a sign by hand. Not proposed.
- Exemptions. The engineers' exemption leaves a class untouched by any seed fact, so it is not an exchange the engine acts on; it enters
  only as a link target. Likewise the Linmouth border (the Act applies wherever the inspector lives) enters only through an alt.
- Classes the policy names but nothing reaches: the inspectors' association (A-17, A-18, A-31). A stake can only be proposed at a node
  that was reached, so I put the association's stake on inspectors.licensed as a proxy. Also, `stake` has no counterfactual baseline: it always
  gives lobbying_effort up, while A-18 and A-31 say the licensing campaign would have continued without the Act (lobbying signed against
  that path). Not proposed with A-18 or A-31 because the engine's sign would contradict their meaning.
- The grandfathering rush. `qualifies` marks its result as a timing conclusion, so the quantity_supplied rise in the window does not
  propagate: the near-line links (A-13 fees cut, A-14 rivals lose jobs) are inert, and inspectors.rivals was never reached. The same
  conclusion blocks the extra-jobs chain to fees and to rivals' volume, which the premises were written to carry.
- Grandfathered status and licenses as assets (not sellable, A-11 earnings, A-22 firms' values): `asset` follows the side direction of the
  exchange, which for a charged exchange is down, the wrong way for a status that incumbents gain. Not proposed.
- Training bunching. Timing needs the announced component to be the chooser's; the proposal on k1_training works, but there is no way to
  say the bunch ends at the deadline or that training shifts between windows.
- Complaint-only enforcement and agents' use of complaints (A-24, A-25): no fact kind for who may trigger enforcement; it appears only as
  the binding premise on the ban (A-3) and the outside margins (A-16, A-29).
- A staying option (A-15, grandfathered inspectors who would otherwise leave) is recorded as an alternative whose use is `employment`, which
  the engine reads as "increase"; it then meets the price-rise chain and the class comes out ambiguous. A status quo is not an alternative use.
- Exit appears as `number_of_sellers` decrease for inspectors.licensed (a class that exists only under the Act), through the operating-charge
  rule. Read against the counterfactual, the licensed stock is smaller than the unlicensed stock was, which is the intended meaning, but the
  class name makes it look like a level.
- The ambiguity on workers.alternative_work and inspectors.licensed employment/enrollment comes from the engine's means exception, not an
  error. I settled only the first (A-7); the other two stay ambiguous because no statement says which chain dominates.
