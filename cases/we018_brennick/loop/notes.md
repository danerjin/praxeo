# WE-018 Brennick bag ordinance: blind expand-as-you-go run

Read: section 1 of WE-018 and, in its assumption table, only ID, Statement, Type, p. Nothing else of the example, nothing
under handbook/05_examples_core/, nothing in the existing cases/we018_brennick/ files or tests. Files in this folder:
`policy.txt` (section 1 as given to `--policy`), `seed.json`, `proposals.json`, `answers.json`, `situation.json` (final).
Final run: DONE in 3 rounds, 11 nodes, 11 questions, 20 proposed facts.

## Seed (the policy's own facts, CR-1)

- e_plastic: shoppers.brennick buy, retailers.brennick sell, thin plastic carryout bag (price vars price_paid / net_price_received).
- e_paper: same parties, paper bag; unsatisfied seller is the retailer (K2 is a minimum, so the seller side is long).
- K1 `banned` on e_plastic (prohibition), premise a1 "Most retailers comply, chains in particular." (A-1, enforcement).
- K2 `held` above on e_paper (price floor of 10 cents), same premise a1. The charge is kept by the retailer, so it is a held price
  and not a `charge` (no receipt variable fits a retailer's revenue); `transfers` on e_paper records "kept by the retailer" (s2).
- `compliance` for retailers under K1 and K2; `enforcers` K3 officials.enforcement; `funded` K3 taxpayers (s3, "funded from the
  general budget", sentence of K3); `announced` K1 and K2 (s4, "passed nine months before it took effect").
- Left empty on purpose: alternatives, links, other margins, stakes, assets, yields, timing, parts, dominance.
- Seed premises judged (not in the table): s2 0.97, s3 0.95, s4 0.95, each restating a sentence of section 1.
  a1 is the table's A-1 (0.85).

## Round 1 (depth 1). Engine derived first effects; 4 nodes

- officials.enforcement (enforcement_cost up): proposed nothing. Complaint-driven enforcement and fines reach no one new in the
  vocabulary.
- taxpayers (resources_available_other_uses down): proposed nothing.
- retailers.brennick (compliance_cost up, excess_supply up, net_price_received up, quantity_traded down, resources up):
  - alt K1 reclassification, premise A-4 (thick "reusable" plastic bags sold at the till; "Reusable bags ... may be sold at any price").
  - margin `outside` informal_activity on e_plastic and on e_paper, premise A-5 ("keep handing out thin bags, or waive the fee").
  - stake K1, premise A-8 (organise below their stake).
  - link quantity_traded same_act to sellers.bag_makers quantity_supplied (retailers' bag purchases are the bag makers' sales;
    "about 120 million such bags").
  - (added in the second pass, applied on the revisit) link quantity_supplied input to workers.retailers_brennick
    employment,hours_worked, premise A-15; dominance on reclassification (see below).
- shoppers.brennick (price_paid up, quantity_traded down, resources down):
  - alt K1 to buyers.substitutes quantity_substitute, premise A-3 (liners instead of reused bags; "60% of households reuse").
  - link price_paid substitute to buyers.substitutes quantity_substitute, premise A-2.
  - alt K1 and alt K2 cross_border_purchases (Fallow Creek, "within 1 km of the city line on Route 9"); premises A-6 (both),
    A-9 (K2 only, the fee is per trip).
  - links cross_border_purchases same_act to retailers.fallow_creek quantity_supplied (no premise); substitute to
    retailers.brennick quantity_supplied, premise A-9 (whole basket moves).
  - timing K1 quantity_traded bring_forward, premise A-7 (extra free bags in the announcement window).

Answers: all from the table (A-3 0.8, A-2 0.95, A-6 0.55, A-9 0.9, A-7 0.7, A-4 0.6, A-5 0.6, A-8 0.7).

## Round 2 (depth 2). Nodes reached: buyers.substitutes, retailers.fallow_creek, sellers.bag_makers (+ revisits of retailers, shoppers)

- buyers.substitutes (quantity_substitute up): link quantity_substitute same_act to sellers.substitutes quantity_supplied;
  link quantity_substitute supply_price to buyers.substitutes price_substitute with premise A-10 (Brennick's demand moves the
  price of liners or reusable bags). Table p 0.1, so the second link stays dormant (price_substitute is derived but not reported).
- retailers.fallow_creek (quantity_supplied up): link input to workers.retailers_fallow_creek employment,hours_worked, premise A-15.
- sellers.bag_makers (quantity_supplied down): stake K1 (A-8); link input to workers.bag_makers employment,hours_worked (no
  premise); link substitute to sellers.substitutes quantity_supplied, premise A-4 (thick bags take over).
- Revisit of retailers.brennick: A-15 workers link and a dominance fact. The engine returned reclassification as ambiguous
  (K1 makes retailers worse off, which raises their alternative use; the rise in their net_price_received makes them better
  off, which lowers it). I proposed dominance (increase, kind empirical) with premise "The ban moves retailers to reclassify more
  than the fee moves them to reclassify less." This is not in the table: judged 0.7 (the ban is what makes the thick bag worth
  selling; the fee does not remove that incentive). It is the only invented premise among the proposals.
Answers: A-15 0.8 and A-10 0.1 from the table; the dominance premise judged.

## Round 3 (depth 3). Nodes: sellers.substitutes, workers.bag_makers, workers.retailers_brennick, workers.retailers_fallow_creek

Proposed nothing for any of them (empty lists): the policy and the table say nothing about what workers or substitute sellers
do next, and I would have had to invent it. The loop stops at depth 3.

## Summary of answers

Table: A-1 (in the seed), and A-2 to A-10 and A-15: ten of the 11 loop questions (A-2, A-3, A-4, A-5, A-6, A-7,
A-8, A-9, A-10, A-15). Judged: s2, s3, s4 (seed), and the dominance premise (the eleventh loop question).
Not used: A-11, A-12, A-13, A-14 (see below).

## What the format could not hold

- A-12 (stores save on bags) and A-13 (cost changes reach shelf prices): a `cost` link needs a price as its source, and nothing in
  the derived effects is a fall in retailers' bag cost; there is no variable for spending on bags. No shelf-price chain can start.
- A-11 (checkout times rise, p 0.45): no relation from compliance_cost to wait_time fits without forcing one; not proposed.
- A-14 (habit, TS-8): the format has an announcement window and an expiry only; slow adaptation over later periods is not a fact.
- Exemptions (plastic bags without handles, pharmacy, restaurant takeout bags; food-assistance recipients get free paper
  bags): an exchange has no exempt subclass, so the food-assistance buyers and the exempt bag trades are not recorded.
- Fines (warning, then $100, $250, $500 a day): a `charge` is a payment attached to trading, not to a violation, so non_tax_receipts
  from fines has no place; enforcement and `outside` stand for it.
- The paper-bag fee goes to the retailer: `charge` needs a receipt variable from a short list (tax_revenue, non_tax_receipts,
  non_wage_compensation), none of which is a private seller's revenue; modelled as `held` plus `transfers`.
- Reusable and paper bags, and liners and reusable bags, merge under one class (buyers.substitutes, sellers.substitutes), because
  the variable quantity_substitute carries no name of the substitute.
- quantity_traded on shoppers and retailers merges plastic and paper bag trades across both exchanges; an exchange's quantity is
  not separate.
- The proposals file is keyed by actor class only, so a revisited node replays the same list; a new fact for a node already in the
  file can only be added to that list and then applies at the revisit (retailers.brennick's A-15 link and dominance were added
  this way, so the final replay shows them at depth 1 although they were proposed after seeing the round-2 effects).
- Both chains on retailers.brennick reclassification (worse by the ban, better by the higher net price) can only be resolved by a
  dominance premise; there is no way to say the fee does not bear on this alternative.
