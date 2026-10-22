# WE-047 Kestrany sugar quota, expand loop (blind run)

Inputs read: section 1 and the assumption table only. Names from `--vocab --exclude WE-047`. Result: DONE in 3 rounds,
32 node visits (8 + 11 + 13), 20 loop questions (all 20 matched table assumptions; none judged in the loop), plus 11 premises
in the seed (8 from the table, 3 judged). No `off-list` lines. Final output is in `final_output.txt`; the situation in `situation.json`.

## Seed (policy's own facts, CR-1)
- Exchanges: `e_imp` (importers buy from sellers.foreign inside the quota; foreign sellers unsatisfied), `e_oq` (the same
  parties outside the quota, where the 60% rate and price variables sit), `e_lic` (licence market: importers buy from
  importers.licence_holders; right_lease_price). I split the two-rate tariff into an in-quota and an out-of-quota exchange
  after the first engine view: with the 60% charge and the cap on one exchange, `side_dir` gave the holders' asset value and
  return both a rise (cap) and a fall (charge), a spurious ambiguity. For the same reason the K4 `terms` sit on `e_lic`
  (terms on `e_imp` also set `side_dir` for both sides) and the registration fee on `e_oq`.
- `capped` k1 on e_imp (holders importers.licence_holders, wider_price: world price, Kestrany is 1.2% of trade); premises A-1, A-2.
- `charges`: k1 (60% out-of-quota rate, receiver general_fund, tax_revenue, with projection variable), premise A-2;
  k3_reg ($500 importer registration, basis operating, non_tax_receipts); k3_fee ($200 transfer fee on e_lic).
- `moves` e_oq buyer (A-4); `incidence` k1 on e_oq: buyer side (judged premise: exporters can sell elsewhere).
- `terms` k4 (surrender, worse for importers on e_lic, premise A-19) and k4a (worse/better only under U1-a);
  `discretion` k4a importers.applicants (A-20); `unclear` U1 with U1-a: [k4a], U1-b: [].
- `means` k2 in for importers.licence_holders (allocation by history is a transfer no choice avoids);
  `announced` k1 (A-10); `compliance` k1 importers; `enforcers` k1 customs, k2 licence office;
  `funded` k2 taxpayers (A-27, A-32).
- Not seeded: `qualifies` (the base period 2023-2025 is fixed and over before the 2 March 2026 publication, so there is
  nothing to compete for), `expires` (no expiry), `fixed`, `grants`, `thresholds`, `banned`, `backstops`.

## Round 1 (depth 1: 8 nodes)
Nodes: general_fund, importers, importers.applicants, importers.licence_holders, officials.enforcement, officials.licensing,
sellers.foreign, taxpayers.
- importers: link imports to tariff revenue (A-25); `supply` links from imports to manufacturers.food and households price_paid
  (A-3); `substitute` links from the import price to producers.sugar price and quantity (A-3, A-30); `currency` link to
  export_industries.other (A-21); alternatives: lease licences (A-6), reclassify into mixtures (A-14); timing bring_forward
  for 2026 imports (A-10); stake (A-17); dominance price_paid up and quantity_traded down, kind arithmetic, premise A-1
  ("domestic price must rise above $550", "250,000 t more than the quota").
- importers.applicants: stake under k4a (section 12; A-17).
- importers.licence_holders: yield (A-22) and asset (A-11) on the seller side of e_imp; cost link from lease price to
  trading houses' imports (A-28); carry_over of 2026 stocks (A-29); stake (A-17).
- officials.licensing: paid_from link to general_fund fund_balance (A-27, A-32).
- sellers.foreign: world price falls with lower demand (A-5, link supply_price); alternative: sell to buyers.foreign (judged
  incidence premise reused); dominance quantity_traded down (A-1).
- general_fund, officials.enforcement, taxpayers: empty lists (nothing reaches a new actor, or the policy gives no funding fact for customs).
Answers: A-25 .85, A-3 .8, A-30 .85, A-21 .6, A-6 .8, A-14 .6, A-17 .85, A-22 .85, A-11 .75, A-28 .6, A-29 .7, A-5 .8, all from the table.
A-5 is the one statement I shortened: the table's parenthetical ("Restated under 1.0 ...") is a note on the answer key, so I asked only
"Kestrany's import cut lowers world demand for sugar on net" and took p = 0.8.

## Round 2 (depth 2: 11 nodes)
buyers.foreign [], export_industries.other [] (A-23 does not cover timber or machinery jobs), general_fund#2, households,
importers#2, importers.applicants#2 [], importers.licence_holders#2 [], importers.trading_houses, manufacturers.food,
producers.sugar, sellers.foreign#2 [].
- general_fund#2: dominance tax_revenue down (A-25: revenue below $56m against $62.5m); `paid_into` link from revenue to the balance.
- households: own_price link (no premise: the law of demand). A-24 states the size of the response, not a condition, so I did not use it as a gate.
- importers#2: reclassification reduces tariff revenue (A-14); licences shift to white sugar (A-15), via a new subclass importers.white_sugar.
- trading_houses: lease-out shifts imports to refiners and importing manufacturers (A-28).
- manufacturers.food: cost links to output (A-8), to exporters (A-9), to owners' asset value (A-8, A-11); substitute links to
  glucose syrup quantity (A-12) and price (A-12, A-13); employment link (A-23); stake (A-17).
- producers.sugar: input links to growers (A-16) and mill workers (A-23); yield link to investment (A-31).
Answers, all from the table: A-15 .6, A-8 .8, A-9 .75, A-12 .65, A-13 .6, A-23 .75, A-16 .75, A-31 .6.

## Round 3 (depth 3: 13 nodes)
growers (employment link A-23, stake A-17), importers.white_sugar (substitute for raw: A-15), manufacturers.exporting
(employment A-23), manufacturers.food#2 (imported goods gain: A-8; sugar demand own_price), producers.glucose (input
suppliers, no premise); empty: general_fund#3, households#2, importers.refiners, manufacturers.importing,
owners.manufacturers, producers.sugar#2, workers.food_manufacturing, workers.mills. No new questions.

## Final engine lines
54 reported lines. Ambiguous: importers and importers.licence_holders quantity_traded (U1-a ambiguous, U1-b decrease),
importers.applicants (U1-a increase or ambiguous, U1-b none), licence_holders resources, importers.refiners quantity_traded.
Everything else has a sign (e.g. general_fund tax_revenue decrease, importers price_paid increase, licence value, lease price up).

## What the format could not hold
- Intra-year timing: A-18 (holders use or sell before 30 September, so October to December imports fall) and A-19. Timing
  windows are only announcement, deadline and after-expiry; a surrender date inside the quota year has no window.
- Dominance cannot settle a sign that differs by reading (U1-a quantity_traded), so A-1/A-19 arithmetic does not remove that ambiguity.
- A two-rate tariff (a lower rate in a quota, a higher rate outside it) has no single instrument: I used two exchanges and a
  capped component with a charge. The in-quota 2% (down from 25%) has no fact of its own.
- Quota size by volume (400,000 t) and the old/new rate are not quantities the engine reads; the rent being positive comes from the cap only.
- K3 trading as an enabling right (selling or leasing lowers the cost of shifting licences to higher-value users, A-7, A-28)
  is only expressed through links and the fee; no fact says "trading makes the cap cheaper".
- An operating fee (registration) must sit on one exchange side; it lands on e_oq though it is paid by importers at large.
- A-20 (non-price allocation under U1-a) and A-27/A-32 fit only as premises of existing facts; there is no fact for
  "the licence office's budget is raised with its task" other than `funded`.
- A-24 (households keep buying) and A-26 (ten-year supply) state sizes and horizons the engine does not use.
- Reading-specific questions: reading labels on facts weren't needed beyond the k4a component.
