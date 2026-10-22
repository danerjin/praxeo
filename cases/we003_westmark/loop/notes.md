# WE-003 loop notes (blind run; policy = section 1 and the assumption table only)

## Seed (policy's own facts)
- e1: customers buy braiding for pay from sellers.current (price_paid / net_price_received).
- k1 `banned` on e1 (licence requirement removes the legal trade for those lacking it): premises A-1 (binds), A-2 (enforced).
- k1 `charges`: licence cost as an operating charge (sum fixed per seller: 1,500 hours, $12,000-$18,000, exam), payer sellers, receiver schools (tuition), receipt non_tax_receipts; premises A-1, A-2; `branch_premises` A-10 (licensing is one branch of comply/stop/evade).
- `outside` margin on e1: informal_activity, premise A-3 (complaint-driven inspections; "keep working and not caught").
- `moves` e1 buyer (medium): judged statement a11 "fewer braiders ... customers pay a higher price" (p 0.7, judged; not in table).
- `compliance` k1 sellers.current; `enforcers` k2 officials.enforcement; `funded` k2 taxpayers (A-8, 0.6); `fixed_budget` k2 officials.enforcement with a12 "absorbs within a fixed budget" (p 0.4, judged as the complement of A-8).
- `unclear` U1: unpaid family/friends braiding covered or not (U1-a assumed: not covered; U1-b covered). No component differs between readings; the exempt form is an alternative tagged `reading: U1-a`.

## Round 1 (depth 1): nodes customers, officials.enforcement, schools, sellers.current, taxpayers
- customers: alt home_production (actor households), A-4, reading U1-a; alt quality_per_unit (inverse), A-7 ("curriculum ... braiding is a small part or absent" and the exit to home/unlicensed braiding).
- officials.enforcement, taxpayers: empty (effects reach no one new).
- schools: stake (A-9).
- sellers.current: alt obtain licence measured by schools' enrollment (A-10); alt relocation_out_of_area (A-6, neighbouring states do not license); link quantity_traded -> licensees quantity_supplied, relation substitute (judged); stake (A-9).
## Round 2 (depth 2): households (empty), licensees (stake, A-9), schools#2 (empty), sellers.current#2 (empty)
## Round 3 (depth 3): licensees#2 (empty)

Totals: 3 rounds, 10 nodes, 5 questions (4 from table: A-4 0.75, A-7 0.45, A-9 0.7, A-6 0.3; 1 judged: "Licensed cosmetologists take some of the customers who leave unlicensed braiders", 0.6). Two seed premises judged (a11 0.7, a12 0.4). A-1, A-2, A-3, A-8, A-10 from table (in seed). A-5 unused (see below).

## What the format could not hold
- Fines for unlicensed practice (k2) and on businesses that employ unlicensed braiders: a penalty on the outside option. A charge needs an exchange; adding an informal-braiding exchange would mislabel quantity_traded (legal market). So no non_tax_receipts from fines.
- A-5 (training unrelated to braiding quality): premises only switch facts on, so "no quality gain from licensing" cannot be expressed; a positive statement ("training raises quality") would be rejected at 0.15 but I did not add the fact.
- Partial ban: `banned` stops the legal trade for both parties of e1, though licensed braiders keep trading; the licensed and unlicensed parts are not separate exchanges (kept one exchange to avoid inventing a second).
- Prospective entrants: the operating charge reaches number_of_sellers of sellers.current only; entry_rate of new entrants has no hook.
- The 12-month grace period (dated operation): `announced`/`timing` need a premise and an action to time; none in the table.
- Customers crossing the border (cross_border_purchases): not in the table, borders "a long drive"; not proposed.
- Tuition paid to schools: the receipt variable list has no private-receipts variable; non_tax_receipts used.
- households home_production reported `ambiguous`: sign differs by reading of U1 (the exempt form exists only under U1-a).
