# WE-042 Vessland aluminum safeguard and drawback: expand loop, blind run (loop_r2)

Branch `loop_r2-we042_vessland` from 62199f1 (the worktree started at 548262e, so the branch was cut from 62199f1 as instructed).
Read only: section 1 (copied here as `policy.md`), the assumption table (ID, statement, type, p), the handbook core rules,
`praxeo/core/*`, and the we001, we009, we013 situation records (plus grep hits for `fund_balance` links in cases we012 to we036).
One slip to disclose: a `grep -l '"grants": [' cases/*/...` run for style also printed the *file names* `cases/we042_vessland/loop/seed.json`
and `.../loop/situation.json`; neither was opened, and nothing from them was used.

Result: `DONE in 3 rounds, 21 questions` (engine depth 3; 36 proposal keys; 3 file rounds of PENDING then DONE). No `off-list:` lines.

## Seed (policy's own facts, CR-1)

Components: k1 tariff (charge, importers, to the general fund, tax_revenue and the static-projection variable), k2 drawback
(grant to exporters, paid by the general fund, subsidy_outlay), k2_sub (the same grant on domestic metal, which exists only under U1-b),
k3 re-import repayment (charge on a re-import exchange, with the 20% fine as a `penalty`), k4 administration (enforcers and
`fixed_budget` for officials.enforcement on k2, k2_sub, k3, `compliance`).
Exchanges: `e_imp` (importers / sellers.foreign), `e_exp_i` and `e_exp_d` (foreign buyers / exporters using imported or domestic
metal; split because the policy and U1 treat them differently), `e_reimp` (re-importers / sellers.foreign).
`moves`: buyer price in e_imp (A-1), seller price in e_imp (A-18, p 0.15, does not fire), exporters' price in the export exchanges
(exporters sell at world prices). `incidence` k1 buyer side (A-14). `announced` k1 (3 Feb 2027 against 1 Sept 2027).
`unclear` U1: U1-a lists no component, U1-b lists k2_sub.
Seed premises (9): table A-1, A-2, A-14, A-17, A-18, A-26; judged w1 (importers declare re-imports and repay, 0.8; K3 says they
"must declare it"), w2 (some importers fail to declare and are found on audit, 0.65; K3's 20% addition; A-9 says detection is
weak but not nil), w3 (exporters sell at prices set in world markets, 0.85; floating-rate trading country).
Left out of the seed on purpose: `expires` (the engine's expiry rule is for a measure that makes an option better; the tariff makes
importers' option worse), `held`, `capped`, `banned`, `thresholds`, `qualifies`, `fixed`, `terms`, `issued`.

## Round 1 (depth 1 nodes: importers, sellers.foreign, buyers.foreign, exporters.imported_metal, exporters.domestic_metal, importers.reimporters, general_fund, officials.enforcement)

- importers: alternative reclassification (A-7; K1 exempts finished goods); links to producers.smelters price (A-1) and quantity (A-4),
  to remelters price and quantity (A-5), pass-through "output" links to manufacturers.home_market, exporters.domestic_metal and
  exporters.imported_metal price_paid (A-1, import parity); currency link to export_industries (A-13); timing bring_forward of
  quantity_traded and inventory_held (A-21, announcement); stake (A-11).
- exporters.imported_metal: stake on k2 (A-11); outside margin legal_breach on e_exp_i (A-25, p 0.4 so it does not fire); cost link
  price_paid to quantity_supplied (w3: world-price takers); input link to workers.export_industries; asset of owners.exporters (A-12).
- exporters.domestic_metal: alternative "switch to traced imported metal" with `reading: U1-a` (A-20), measured by quantity_substitute;
  stake on k2_sub; outside margin (A-25); cost link (w3); workers link; asset (A-12).
- importers.reimporters: outside margin legal_breach on e_reimp (A-10 round trip is cheaper than the refund, A-9 audits detect few).
- general_fund: paid_into links for tax_revenue and non_tax_receipts, paid_from link for subsidy_outlay, to fund_balance (K4: receipts
  to the general fund, drawback paid out of them); same_act to taxpayers (A-24); dominance fund_balance increase, kind arithmetic (A-3).
- sellers.foreign, buyers.foreign, officials.enforcement: empty (see "could not hold").

## Round 2 (depth 2: export_industries, owners.exporters, manufacturers.home_market, producers.smelters, producers.remelters, taxpayers, workers.export_industries, and revisits of importers, the exporters, general_fund, importers.reimporters)

- manufacturers.home_market (price_paid up): cost link to its quantity_supplied (A-15); output link to consumers price_paid (A-16, goods
  with no close import substitute); substitute link to consumers quantity_substitute (A-15); output link to buyers.border (A-27);
  alternatives: sell more abroad, onto exporters.imported_metal quantity_supplied (A-8) and, with `reading: U1-b`, onto
  exporters.domestic_metal; relocate to Ostrel (A-23, measured by relocation_out_of_area); stake (A-11); asset of owners.manufacturers (A-12, A-15).
- producers.smelters: workers.smelters and input_suppliers (electricity) links; yield link to investment_target (A-19, p 0.35, does not
  fire); yield link to owners.smelters asset_value (A-12); stake.
- producers.remelters: remelters' scrap demand (input link), supply_price link to sellers.scrap net_price_received (A-6); stake.
- exporters.domestic_metal#2: same_act link from quantity_substitute to importers quantity_traded, `reading: U1-a` (A-20).
- importers#2: currency links to exporters.imported_metal and exporters.domestic_metal quantity_supplied (A-13).
- importers.reimporters#2: paid_from link from legal_breach to the fund balance (refunds paid on round trips).
- export_industries: input link to workers.export_industries. Others empty.

## Round 3 (depth 3: buyers.border, consumers, sellers.scrap, workers and owners nodes, input_suppliers, revisits)

- buyers.border: substitute link price_paid to cross_border_purchases (A-23). consumers: own_price link to quantity_demanded.
- exporters.imported_metal#3, exporters.domestic_metal#3: dominance quantity_supplied increase, kind empirical (A-29: relative yield of
  home and export sales outweighs the exchange rate), because the cost link, the currency link and the shift-to-exports alternative clash.
- Everything else empty (the new effects reach no one the record can name without inventing facts).

## Answers

All 21 questions the loop asked were matched to the table (p taken as given): A-3, A-4, A-5, A-6, A-7, A-8, A-9, A-10, A-11, A-12, A-13,
A-15, A-16, A-19, A-20, A-21, A-23, A-24, A-25, A-27, A-29. Judged: none asked in the loop. The three judged premises (w1, w2, w3) are
in the seed, which carries its own p. Table statements not used in any fact: A-22 (home users keep buying: the default, no fact needed) and
A-28 (see below).

## Engine output (headline)

Fund: tax_revenue, non_tax_receipts, subsidy_outlay and fund_balance up (A-3 dominance), revenue below the static projection; taxpayers'
means up (A-24). Importers: price_paid up, quantity_traded ambiguous (falls under K1, rises under U1-a from switching, A-20), tax_share_borne
up (A-14), reclassification up, bring-forward in the announcement window. Domestic smelters and remelters: price and quantity up; owners.smelters
asset_value up; scrap price up. Home-market fabricators: price_paid up, output down, relocation up, owners' asset_value down; consumers and
border buyers pay more, border buyers buy across. Exporters using imported metal: net_price_received and exports up, quantity_supplied
up through the A-29 dominance. Exporters using domestic metal: signs differ by reading (grant effects only under U1-b). Re-importers:
quantity_traded down, legal_breach up. officials.enforcement: enforcement_cost both up and down.

## What the format could not hold

1. A drawback refunds a charge on an input, so it offsets a cost it does not create. As a grant it is a wedge against the no-tariff
   counterfactual, so exporters show exports up before the cost link is counted; the net (unrefunded 1% and holding cost, A-29) is held only
   by a dominance premise on exporters' quantity_supplied, not by a net-of-refund relation.
2. Claims by Customs' yield tables when actual use is lower (A-28), which pay a refund above the tariff on the metal actually used, and
   overstated content (A-25): no variable for "refund above tariff paid"; only legal_breach, and only A-25 (p 0.4, fails). A-28 has no fact.
3. The importer's written designation of its entries to the exporter: a transfer of the claim, a payment moved between two parties; no
   field for who receives a grant that the payer may reassign.
4. The reading U1 changes who is paid and who must switch: it needed a second component, a second export exchange and per-reading
   alternatives and links; the switching under U1-a makes importers' quantity_traded ambiguous (a fall under K1 against a rise from
   switching) with no table premise that settles it, and that ambiguity feeds the currency link into exporters' quantity_supplied.
5. `expires` handles a measure that makes an option better ending; a tariff expiring (A-12, A-19, renewal uncertainty) went in only through
   asset and yield premises, not as a capitalisation over four years against a renewal probability.
6. Scrap has two outlets (home remelters, export): the engine can say the home scrap price rises (A-6) but not that exports of scrap
   fall; this needs an exchange with a fixed price on one side, which no policy component touches.
7. The exchange rate: no link target for the crown's value; "currency" from imports to exporters' quantity_supplied stands in for it.
8. Overlapping classes: mixed fabricators are at once home-market sellers and exporters; split classes (manufacturers.home_market,
   exporters.imported_metal, exporters.domestic_metal) share firms with no `parts` relation.
9. officials.enforcement: enforcement_cost is reported both up (enforcer) and down (fixed budget, other work gives way) with no way to
   state that the two refer to different work.
10. A-22 and the 1.5% world-share premise (A-18) only gate or default; "seller price falls" has no link to a world price for a large buyer.
