# WE-042 Vessland aluminum safeguard and drawback: blind expand-loop run

Inputs read: the section 1 policy record and the assumption table (ID | Statement | Type | p) only. Files: `seed.json`,
`proposals.json`, `answers.json`, `situation.json` (final), `policy.md` (copy of section 1). `mkseed.py`, `gen.py`,
`rounds.py`, `rounds2.py`, `rounds3.py` are the scripts that wrote them (rounds.py = round 1). Premise ids are `a1`...
(a hyphen breaks the engine atoms), numbered as the table's A-n.

Result: DONE in 3 rounds, 31 node visits (9 + 12 + 10), 21 premise questions asked in the loop (20 matched the
assumption table, 1 judged), plus 9 seed premises (all table).

## Seed (policy's own facts only)
- Exchanges: e_imp (importers / sellers.foreign, price_paid, net_price_received); e_exp, e_exp_tab, e_exp_dom (foreign
  buyers / three exporter subclasses); e_reimp (re-importers / sellers.reexport).
- K1 charge on e_imp to general_fund (tax_revenue, tax_revenue_vs_static_projection; premises a1, a2, a22: binds, is
  enforced, some home users keep buying). K3 charge on e_reimp (no premise; text is unconditional).
- K2 grant (payer general_fund, premise a26) on e_exp; on e_exp_tab with a28 (claimants who use less metal than the
  yield tables count, so are refunded more than they paid: CR-3 0.9 split by position against the standard). K2b grant on
  e_exp_dom, a component only under U1-b (unclear U1: "U1-a": [], "U1-b": ["k2b"]).
- moves: e_imp buyer (a14, foreign sellers have far better alternatives), e_imp seller (a18, p 0.15 so inert);
  incidence k1 on buyer (a14); announced k1 (a21); compliance on the claimants and the importers; officials.revenue as
  enforcer of all four, with fixed_budget (a17: "within its existing appropriation").

## Round 1 (9 nodes)
- importers: alternative reshape to uncovered fabricated forms (a7, text: finished goods exempt); timing bring_forward
  (a21, announcement 3 Feb, effective 1 Sep); links: price_paid substitute to producers.domestic net price (a1) and
  quantity (a4), to producers.secondary quantity (a5); same_act to sellers.foreign; currency to export_industries (a13).
- exporters.imported_metal, exporters.table_claimants: input links to workers.export_industries and to importers (they buy
  imported metal), stake in k2 (a11), part_of export_industries, dominance resources_available_other_uses increase on a26
  (paperwork costs less than the refund), same_act link to legal_breach on a25 (overstating beyond the yield tables).
- exporters.domestic_metal: input links to labour and to producers.domestic (a4), stake in k2b, part_of export_industries.
- general_fund: paid_into / paid_from links to fund_balance, dominance fund_balance increase on a3 (arithmetic on the case's
  figures: 600,000 t x $500 against at most 250,000 t x $495), same_act link to taxpayers' means (a24).
- importers.reimport: outside margin on e_reimp, informal_activity (a9 and a10: audits detect few, round trip cheaper than
  the refund).
- sellers.foreign, sellers.reexport, buyers.foreign, officials.revenue: empty lists.
- Answers: all from the table (a3, a4, a5, a7, a9, a10, a11, a13, a24, a25, and the seed ids).

## Round 2 (12 nodes)
- importers#2: importers quantity_traded was ambiguous (tariff down, exporters' demand up); dominance decrease on a new
  premise N1 "The metal imported for goods sold in Vessland falls by more than the metal imported for exports rises."
  (JUDGED, p 0.75: section 1 puts 500,000 t of home-use imports under the full 20% against a refund on at most 250,000 t of
  export content, 100,000 t imported; no table row states it). Same dominance on sellers.foreign#2. Link importers
  reclassification substitute to manufacturers.home quantity (a7, a15).
- producers.domestic: input links to workers.smelters and electricity (input_suppliers.electricity); same_act of its net price
  to manufacturers.home and exporters.domestic_metal price_paid (a1); yield links to owners.smelters asset_value (a12) and
  own investment_target (a19, p 0.35, so inert); stake k1 (a11).
- producers.secondary: supply_price link to sellers.scrap net price (a6).
- Empty: export_industries, exporters.* #2, general_fund#2, importers.reimport#2, taxpayers, workers.export_industries.

## Round 3 (10 nodes)
- manufacturers.home: cost links to its own quantity (a15) and owners.manufacturers asset_value (a12, a15); substitute to
  buyers.substitutes (a15); input to workers.manufacturers; output / supply links to buyers' price_paid (a16, a27);
  alternatives: sell more abroad (a8, actor export_industries quantity_supplied) and move fabrication to Ostrel (a23,
  investment_target, inverse); stake (a11).
- export_industries#2: dominance quantity_supplied increase on a29 (relative yield of home and export sales outweighs the
  exchange-rate chain).
- exporters.domestic_metal#3: alternative under reading U1-a only: use traced imported metal (a20), actor importers.
- Empty: importers#3, input_suppliers.electricity, owners.smelters, producers.domestic#2, sellers.foreign#3, sellers.scrap,
  workers.smelters.

## Answers
From the table (exact statement): A-1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
25, 26, 27, 28, 29 as used (all 29 rows were used at least once). Judged: N1 only.
A-6 as restated (0.9, no $19 threshold) is used only as "domestic scrap price rises"; A-18 and A-19 sit below the cut-off
and so are inert as in the table.

## What the format could not hold
- A refund conditional on export of a taxed input (K2) is a `grant` on an export exchange; it cannot be tied to the taxed
  import, so the net-zero effect of tariff plus refund on export metal is only reached through links (exporters' demand for
  imported metal) and a dominance premise.
- Misuse of a grant (A-25 overstating content, A-10 round trips to claim the refund) has no home: `outside` margins require a
  charge, ban, cap or held price on the exchange, and an alternative of a "better" chooser moves the alternative down. I used a
  same_act link to legal_breach (A-25, inert at 0.4) and put the round trip on the K3 exchange (informal re-imports).
- Sunset with a renewal vote (K1 expires 2031 unless extended): `expires` only drives deadline timing for a measure that makes
  an option better; the tariff's expiry and A-12 / A-19 can only be reached as asset and investment yields.
- The domestic market is not an exchange in the seed (the policy touches only imports); the import-parity price, home sales
  and scrap are reached only through substitute / same_act / supply_price links.
- Dominance is not applied to a sign that differs by reading, so N1 (imports fall) also absorbs the U1-a switching chain
  (A-20) instead of showing importers quantity_traded per reading.
- `class totals`: export_industries quantity_supplied needs a dominance (a29) because the currency chain and the shift of
  fabricators' sales to exports meet in one variable; the policy gives no figures for the sizes.
- Per-reading effects on classes with no direct component under a reading (exporters.domestic_metal under U1-a) need a
  price chain to make them choosers; the engine reports "none" for U1-a on them.
- Customs' yield-table over-refund appears only as a split of the exporter class and a grant premise (a28), not as a quantity.
