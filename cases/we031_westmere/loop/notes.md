# WE-031 expand loop, blind run: notes

Read: section 1 of the example and, in the assumption table, only ID, Statement, Type, p (cut with `cut -f2-5`). Two slips to
disclose: (1) one `awk` over the headings printed the section titles of the whole file (titles only, no content); (2) the text
that follows the table ("Final check before the report", which mentions C-numbers) was displayed when I printed the table's
line range. I did not use either.

Branch: loop-we031_westmere (from a522291). 3 rounds, 18 node visits, 15 premise questions beyond the seed's 6 assumptions.

## Seed (policy's own facts, CR-1)
- Exchanges: e_newhomes (builders.homes sell, buyers.new_homes buy), e_large_homes (same builders, buyers.large_homes; exists only to
  carry U1-b).
- `banned` k1 on e_newhomes ("new homes whose DEI exceeds a maximum may not be built"), premises A-1 (binding), A-2 (enforcement).
  `banned` k1_u1b on e_large_homes, premises A-1, A-2, A-28.
- `unclear` U1: U1-a lists no component, U1-b lists k1_u1b ("for homes above 2,500 sq ft the maximum applies to total modeled energy").
- `charges` k3: the DEI report / rater's certificate each home needs, paid by builders to raters (non_tax_receipts), no quantity premise.
- `announced` k1 (A-20): enacted 15 June Y0, effective 1 Jan Y1, schedule published.
- `compliance` builders.homes (k1, k3); `enforcers` building departments and Energy Office (k3); `fixed_budget` building departments
  (A-10: fees fixed by ordinance); `funded` taxpayers (A-25: new general-fund appropriation for the audit unit).
- Seed assumptions all taken from the table: A-1 .8, A-2 .9, A-10 .6, A-20 .7, A-25 .6, A-28 .65.

## Round 1 (depth 1): builders.homes, buyers.new_homes, buyers.large_homes, officials.building_departments, officials.energy_office, raters, taxpayers
builders.homes (11 proposals):
- alternatives k1: reclassification into renovation/small additions (A-11, "Renovations ... Additions ... 50% or less" exempt); building
  across the state line, actor builders.across_state_line (A-13, Halden/Brennick); four-storey projects, actor builders.four_story (A-26,
  "four or more stories ... commercial code"); other construction work, actor sellers.other_construction (A-7); larger homes, unit_size
  (A-28, per-square-foot index).
- timing k1 applications bring_forward (A-9, K2 vesting at filing date).
- margin outside e_newhomes legal_breach (A-16, raters hired and paid by builders, 2% audited).
- stake k1 (A-17).
- asset on the seller side of e_newhomes for landowners.buildable_lots (A-21, A-20).
- links: compliance_cost -> input -> makers.efficiency_products quantity_demanded (A-22); quantity_traded -> input -> workers.construction
  employment,hours_worked and input_suppliers quantity_demanded (no premise; generic CR-9).
buyers.new_homes: alternatives to owners.existing_homes (A-7), sellers.manufactured_homes (A-12), cross_border_purchases (A-13).
buyers.large_homes: alternative k1_u1b to owners.existing_homes (A-7).
raters: non_tax_receipts -yield-> raters.prospective entry_rate (A-15); non_tax_receipts -supply_price-> raters net_price_received (A-14).
officials.building_departments, officials.energy_office, taxpayers: empty lists (see "could not hold").

## Round 2 (depth 2): builders.across_state_line, input_suppliers, landowners.buildable_lots, makers.efficiency_products, owners.existing_homes, raters.prospective, sellers.manufactured_homes, sellers.other_construction, workers.construction
- makers.efficiency_products: yield link to asset_value (A-30), stake k1 (A-18).
- owners.existing_homes: yield link to own asset_value and supply_price link to buyers.existing_homes price_paid, both on one new
  premise (stock of existing homes fixed in the period).
- sellers.other_construction: supply link to buyers.other_construction price_paid (no premise).
- the other five nodes: empty (no further market the text supports).

## Round 3 (depth 3): buyers.existing_homes, buyers.other_construction
- buyers.existing_homes: alternative to manufactured homes (A-12). buyers.other_construction: empty.
The run stops at depth 3 with every node covered.

## Answers
From the table: A-11 .7, A-13 .6, A-26 .35, A-7 .8, A-9 .85, A-16 .55, A-17 .9, A-21 .75, A-22 .6, A-12 .6, A-15 .8, A-14 .7,
A-30 .7, A-18 .7 (A-20, A-28 etc. came with the seed). Judged by me (1): "The stock of existing homes cannot expand in the period, so
more demand for existing homes raises their prices and value." .9 (the text gives 2.4 million homes and a few tens of thousands built
a year; no table row). I reused table statements verbatim even where they hold two concepts (A-7, A-30), so their p carries over.
A-26 (.35) fails the cut, so the four-storey alternative is not reported (shown "-" in the output).

## What the format could not hold
- The existing rebate: the Act re-points the rebate's threshold at the code (looser than the counterfactual in Years 1-3, tighter
  after Year 4; U2 gives two readings). `grants` pays out a fixed subsidy and has no window or comparison with a counterfactual
  threshold, and proposals cannot add a grant, so the rebate (and A-19, A-29, A-31) is absent. Nothing signs rebate qualification or
  outlay.
- A standard that tightens each year (TS-3): no way to say a ban binds more homes in later windows; the ban is on/off. A-1 and
  A-4 (binds a few percent in Year 1) cannot both be expressed.
- A ban defined on a performance index, not a size: `thresholds` is for a measure of size and did not fit the DEI line. Likewise
  the 50%-addition exemption and small-builder fixed cost (A-8, builders of fewer than 20 homes) have no size variable in the list.
- Alternatives are not per reading: the unit_size alternative (A-28) is a U1-a mechanism but sits on k1, which applies under both
  readings; under U1-b the opposite holds for large homes. An alternative always signs the use of the alternative as an increase, so
  "build smaller homes" (unit_size down) under U1-b cannot be stated.
- The exempt existing stock and the large-home segment overlap with e_newhomes: e_large_homes is a segment of the same market, not
  a separate market, so builders.homes is hit twice under U1-b.
- Review capacity: building departments have an increase (enforcer) and a decrease (fixed budget, other work gives way) on
  enforcement_cost, which stays two lines; no variable for review capacity or permit wait, and a link from either line would carry
  both signs, so I proposed nothing (the waiting-time margin on permits is missing).
- Rater capacity: supply_price raises the rating price (short), entry raises capacity (later); links have no window, so I left the
  entry-side price link out to avoid a false ambiguity. A-27 (only part of homes rated without the Act) is not used.
- Lobbying by landowners and existing-home owners (A-29) not proposed: no table premise says they can organize.
- Energy bills, emissions: out of scope per the example (A-24 not used).
- Dominance (CR-12e): no proposal; no premise in section 1 or the table states that one direction outweighs another except via the
  rebate (A-29, A-31), which could not be expressed.
- The seed's `charges` receipt variable for a rater's fee (non_tax_receipts) is a state-receipts variable; raters are private.
