# WE-017 loop notes (blind run)

Inputs read: section 1 and the assumption table only. All premise answers came from the table (A-1 to A-16 matched by exact statement); none were judged, because every proposed premise has a table statement. Seed assumptions: A-1, A-2, A-4, A-5, A-6, A-9. The loop asked 10 further questions (A-3, A-7, A-8, A-10, A-11, A-12, A-13, A-14, A-15, A-16), all answered from the table at the table's p. The run took 3 rounds, 20 node visits and no off-list names.

## Seed (policy's own facts, CR-1)
- Exchanges: `e_legal` (buyers.current / sellers.current), `e_informal` (buyers.current / sellers.prospective; penalties act here), `e_related` (buyers.current / sellers.substitutes; reached only under reading U1-b).
- `banned` k1 on e_legal (premise A-2); k1_b on e_related with `reading` U1-b. `unclear` U1: U1-a related plants not covered (assumed by the Act), U1-b covered; only U1-b lists k1_b.
- `charges` k2 (penalties), one per payer side on e_informal, receiver treasury, non_tax_receipts, premise A-4; `moves` e_informal buyer, premise A-1.
- `thresholds` k2 at the 50 g line (buyers.border, transaction_size, A-9 and A-6) and the 1 kg line (sellers.prospective, transaction_size, A-9 and A-4): the grading by weight.
- `discretion` k1 for licensees.research (licensed research exemption, no premise); `compliance` k3 sellers.current; `enforcers` k4 officials.enforcement; `funded` k4 taxpayers (general budget); `announced` k1 (A-5).

## Round 1 (8 nodes)
- buyers.border: alternative of more, smaller trips (A-6); trips to travel_time; cross-border purchases to Halvet sellers (A-6); bundling links to Halvet and Corrin retailers (A-13, p 0.4, so not reported).
- buyers.current: alternatives to the ban: informal activity (A-1, A-3), cross-border purchases (A-6), substitutes (A-7), concentrated form (A-9, A-10), home production of extract (A-10); bring-forward of purchases (A-5); link to informal sellers (A-1); to substitute sellers (A-7); conviction record to employment (A-16); stake (A-12).
- licensees.research, taxpayers, treasury: empty (reach no one else).
- officials.enforcement: spending paid from the general fund (text: "from the general budget").
- sellers.current: reclassification into blends under U1-a (A-8); sell-down timing, carry_over of stock and bring_forward of sales (A-2, the K3 deadline); links to specialist-shop staff (A-11), growers, sales-tax revenue ("subject to the general sales tax"); assets and yields of shops (A-11, no compensation); stake (A-12).
- sellers.prospective: concentrated form (A-9, A-10); reclassification under U1-a (A-8).

## Round 2 (10 nodes)
Empty: buyers.border#2, buyers.current#2, general_fund, growers, sellers.foreign, treasury#2, workers.specialist_shops. Added: sellers.current#2 link of reclassification to substitute sellers (U1-a, A-8); sellers.prospective#2 informal activity to disputes settled outside courts (A-14, p 0.3, so not reported); sellers.substitutes: excise yield to treasury (A-15).

## Round 3 (2 nodes)
sellers.substitutes#2 and treasury#3 (tax_revenue ambiguous: lost sales tax on lirva against excise on substitutes): empty. No dominance premise is stated in the policy or table, so I did not add one.

## What the format could not hold
- The informal market is not an exchange the policy names; I added `e_informal` and `e_related` to the seed to carry the penalties and the reading. Exchanges cannot be proposed in the loop.
- Fines go on "possession" and "sale" at grades of weight: a charge has one rate; the grading is carried only by the two thresholds, and the per-dose difference between leaf and extract (the policy's note on K2) rests on premises A-9 and A-10 in alternatives.
- Growers, importers and makers are banned directly but trade in no exchange, so they appear only through links (growers) or not at all.
- K3 (destroy or export stocks, no compensation) is `compliance` plus timing; "no compensation" and "export" have no field (a loss of means that a choice can avoid).
- Effects tied to the ban in e_legal reach only the quantity; the price of the banned legal good is not defined, so the price rise comes from the informal exchange.
- A-16 (convictions recorded, employers check) has no relation; I used `substitute` from informal_activity to employment, which is a stretch.
- Per-reading effects show as `ambiguous` for reclassification; the signs by reading are in the engine's per-reading output, not the printed line.
