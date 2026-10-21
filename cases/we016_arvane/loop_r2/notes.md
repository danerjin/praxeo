# WE-016 Arvane Interior Design Practice Act: blind expand-as-you-go run (loop_r2)

Read: section 1 of WE-016 (saved as `policy.txt`) and, in its assumption table, only ID, Statement, Type, p. Nothing else of the
example, nothing under handbook/05_examples_core/, nothing in the existing cases/we016_arvane/ files or tests. Files here:
`policy.txt`, `seed.json`, `proposals.json`, `answers.json`, `situation.json` (final).
Final run: DONE in 3 rounds, 11 nodes (8 + 3; round 3 only revisited nodes already answered), 13 questions, 18 proposed facts.

## Seed (the policy's own facts, CR-1)

- Two exchanges of design services, both with seller `designers.arvane` and unsatisfied seller `designers.unlicensed` (practitioners who
  do not qualify, and would-be entrants): `e_home` (buyer `clients.residential`) and `e_comm` (buyer `clients.commercial`). Section 1
  splits the trade half and half between homes and businesses and K3 touches only commercial work, so I used two exchanges.
- K1 licence requirement as `capped` (a rule fixing who may sell, price left free): on `e_home` holders `designers.grandfathered`; on
  `e_comm` holders `designers.grandfathered` and `architects.arvane` (architects are exempt from K1). Premises a1 (A-1, binding) and a2
  (A-2, enforcement). K2 is what makes the grandfathered class the holder at creation.
- K3 stamped plans as a second `capped` on `e_comm`, same holders, premise a5 (A-5, building departments reject unstamped plans).
- K1 licence fee ($250 a year) as `charge` `k1_fee`, `basis: operating` (a sum fixed per seller), payer seller side, receiver
  `board.interior_design`, receipt `non_tax_receipts`. Attached to `e_home` only (see "format" below).
- `compliance`: K1 for `designers.grandfathered` (12 hours of continuing education a year, the fee); K3 for `clients.commercial`
  (permit applicants must have plans stamped).
- `enforcers` K4 `board.interior_design`; `funded` K4 by `taxpayers` (s2, "general budget") and `designers.grandfathered` (s3, "license
  fees"), both from the K4 sentence.
- `announced` K1 and K3 (s1: "passed ten months before it took effect").
- Not used: held, moves, grants, banned, expires, thresholds, qualifies, backstops, discretion, means, early_price, transfers,
  fixed_budget, capped_payers, branch_premises (no sentence of section 1 supports them; reasons for qualifies below).
- Left empty on purpose: alternatives, links, margins, stakes, assets, yields, timing, parts, dominance.
- Seed premises: a1, a2, a5 are the table's A-1, A-2, A-5 (p 0.9, 0.7, 0.85). s1 (0.95), s2 (0.97), s3 (0.97) restate sentences of section
  1 and were judged.

## Round 1 (depth 1). Eight nodes

Effects the engine gave: architects (asset_value up, net_price_received up); board (enforcement_cost up, non_tax_receipts up);
clients.commercial (compliance_cost up, price_paid up, quantity_traded down, resources down); clients.residential (price_paid up,
quantity_traded down); designers.arvane (number_of_sellers down, resources down); designers.grandfathered (asset_value up,
compliance_cost up, net_price_received up, resources down); designers.unlicensed (quantity_traded down); taxpayers (resources down).

- architects.arvane: stake K1 (A-9); link quantity_supplied -> net_price_received, `supply_price` (A-18: capacity cannot expand at
  unchanged fees; the stamp and the exemption send work their way).
- board.interior_design, taxpayers, designers.arvane: nothing. The Board's cost and receipts reach no one new; the fee and the
  fall in sellers have no further link in section 1.
- designers.grandfathered: stake K1 (A-9); alternative `turnover` (A-16: some would otherwise leave for a time and return; the licence
  lapses if not renewed and cannot be regained, so the holder leaves less). Chooser is "better" (holder), so the engine gives a decrease.
- designers.unlicensed:
  - margin `outside` informal_activity on `e_home` (A-3, "undetected, mainly in homes"; K4 is complaint-driven, so the penalty is
    weak). Not on `e_comm`: A-3 says homes.
  - alternative `reclassification` (A-7, the retail exemption used for full-room design with furniture sales).
  - alternative `wait_time` (A-15: supervised hours are scarce; K1 needs 3,500 supervised hours).
  - alternative `enrollment` on `schools.design` (judged premise: some would-be entrants earn the degree; K1 lists the degree, and
    section 1 gives the two programs and 300 graduates a year).
  - link quantity_traded `same_act` earnings, A-19 (next-best work pays less in money). A stretch, see "format".
- clients.commercial: timing `bring_forward` quantity_traded (A-8, ten-month window; announced is in the seed); link price_paid
  `substitute` -> architects quantity_supplied (A-11).
- clients.residential: alternative home_production (A-10); alternative cross_border_purchases (A-17, Corvan 20 km from Velmark; p 0.4,
  so below the cut-off and not reported); links price_paid `substitute` -> `retailers.furnishings` quantity_supplied (A-10 and A-7)
  and -> `sellers.online_design` quantity_supplied (A-10).

Answers, round 1. From the table: A-9 0.8; A-18 0.7; A-8 0.6; A-11 0.7; A-10 0.85; A-17 0.4; A-7 0.75; A-16 0.65; A-3 0.8; A-15 0.6; A-19 0.65.
Judged: "Some would-be entrants earn the accredited degree in order to qualify." 0.7 (the degree route is the only one open to
new entrants and the programs exist; not in the table).

## Round 2 (depth 2). Three nodes

- retailers.furnishings (quantity_supplied up): stake K1 (A-9); link quantity_supplied `complement` -> own quantity_traded (A-12:
  households that use a store's design help buy most furnishings there).
- schools.design (enrollment up): stake K1 (A-9).
- sellers.online_design: nothing (no sentence ties them to anyone further).
Answers: A-12 0.75 from the table. A-9 reused by wording.

## Round 3 (depth 3)

Only nodes already answered were revisited (e.g. retailers.furnishings got a new effect, quantity_traded up); no new
proposals, nothing pending. Final output: 35 consequence lines, of which 34 reported; the one not reported is
clients.residential cross_border_purchases up (A-17 at 0.4).

## Answers from the table vs judged

Table (A-id): A-1, A-2, A-3, A-5, A-7, A-8, A-9, A-10, A-11, A-12, A-15, A-16, A-17, A-18, A-19.
Judged: s1, s2, s3 (seed, restating sentences of K4 and the enactment date) and the "would-be entrants earn the degree" premise.

## What the format could not hold

- Quality. A-6, A-13, A-14, A-20 (training useful to commercial clients, largely unrelated for homes; substitutes give lower quality
  than the designer replaced) are not used: a licence conveying quality or standing (CR-11c) has no fact in the situation
  vocabulary, and a link would need a made-up relation (a rise in a substitute's use lowering `quality_per_unit`). No proposal
  could carry them, so the commercial gain and the residential loss in quality are missing.
- Persistence and attrition. A-4 (3 to 5% of grandfathered designers leave a year; a licence is not regained) is a stock running
  down over time, a CR-10b matter; the run signs only the first effect, and only `turnover` for the holders.
- Grandfathering as a claim. K2 gives a licence by three years of practice before the effective date, a period that overlaps the
  ten months of announcement only for those with 2 years 2 months or more; `qualifies` needs a premise I would have had to
  invent, so I left it out. A race to qualify would show as quantity_supplied up in the announcement window.
- A fee on a seller that sells in several exchanges. `charge` is tied to one exchange, so `k1_fee` is on `e_home` only; attaching it to
  both would double the receipts and the resource effects (same sign). The exam fee ($1,200) is a one-off cost of the entry option and
  has no fact: it stays in the alternatives (`wait_time`, `enrollment`), not as a charge.
- The exempt retail sellers. They are sellers of a bundle (design help with furniture), not holders of a capped permission in these
  exchanges, so they entered only as the substitute side of a link (and as a reclassification), not as `holders`.
- Overlap of K1 and K3 on `e_comm`. K3 adds who may stamp (the same holders), so the two `capped` facts duplicate each other's effects
  with the same sign; the format has no "narrower route for permits".
- The market for supervised positions. Scarce supervision (A-15) is an excess-demand condition between graduates and supervisors,
  and `held` is the only fact that raises one; I put it as an alternative `wait_time` on the unlicensed class. A class for graduates
  would need a node that the engine reaches, and none is reached.
- `designers.unlicensed` mixes practitioners who leave and entrants who never start. The `same_act` link to earnings (A-19) is the nearest
  fact to "next-best work pays less" and says only that fewer sales are fewer earnings.
