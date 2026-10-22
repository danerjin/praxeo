# WE-014 Calvar Sugar Market Act: blind expand-as-you-go run

Inputs read: handbook/04a_core_rules.md, praxeo/core/{core.lp,situation.py,expand.py}, cases we001/we009/we013 situation.json (style only), the policy record (policy.md = section 1) and the assumption table. Nothing under handbook/05_examples*, cases/we014_calvar (other than this folder) or tests/ was opened. Vocabulary run with `--exclude WE-014`. No `off-list:` line was printed in any round.

Command: `python -m praxeo.core.expand cases/we014_calvar/loop/seed.json .../proposals.json .../answers.json --policy cases/we014_calvar/loop/policy.md` (final output in engine_output.txt). Result: DONE in 3 rounds, 19 questions (plus 6 premises in the seed), 15 nodes proposed for (32 node visits), 41 facts added. 47 reported consequences, 21 of them `ambiguous`.

## Seed (the policy's own facts, CR-1)
- Exchange `e_sugar`: buyers (price_paid) buy from importers.quota_holders (net_price_received); the shut-out seller is sellers.foreign. I put the quota on the domestic sugar exchange, not on the import leg (importers buying from foreign sellers), because `capped` raises the *buyer's* price and the *holder's* price, and the holders sell the permitted tonnage on the domestic market.
- `capped` k1, holders importers.quota_holders, premises A-1 (binds), A-2 (enforced at the ports). Not `wider_price`: the quota binds, so the domestic price is not the world price.
- `outside` margin on e_sugar: importers.without_rights informal_activity, premise A-12 (land crossing "checked by sample"; p 0.3, so it stays unreported).
- `thresholds` k1: importers.near_threshold, product_attribute (the 65% sugar line is a line on a ratio), premise A-8.
- `qualifies` k2: importers.quota_holders, quantity_traded (shares by imports in the 36 months before the effective date, 9 months of which fall after the bill was introduced), premise A-6.
- `means` k2 in for importers.quota_holders (free, permanent, tradable shares: op 4). `announced` k1 (bill introduced 9 months before).
- k3: `enforcers` officials.enforcement, `funded` taxpayers (A-22, "funded from the general budget"), `compliance` importers.quota_holders (register of transfers, bulk cargo through two ports).
- `unclear` U1 (65% line counted on dry or total weight), components empty for both readings (k1 applies under both); the readings differ in the exempt-form alternatives only.
- Not in the seed: no price line, no charge, no grant (the free shares are `means`), no `expires` (no expiry; the five-year review is expectations, premise A-5 on the assets), no `ban` (seizure and the triple fine only enforce k1).

## Round 1 (depth 1)
Nodes: buyers, importers.near_threshold, importers.quota_holders, officials.enforcement, sellers.foreign, taxpayers.
- buyers: alternatives corn syrup/other sweeteners (quantity_substitute, A-7, "Corn syrup and other sweeteners are not covered") and purchases in Ostria (buyers.border cross_border_purchases, A-11, personal allowance and Varnholt). Links: substitute to producers.beet_factories net_price_received (A-3) and quantity_supplied (A-3, A-4); substitute to sellers.substitutes (corn syrup) net_price_received (A-7, A-13); output to consumers price_paid and cost to producers.sweetened_goods quantity_supplied (both A-14, sugar in finished foods is exempt but locally made goods use dutiable sugar); cost to buyers' own resources_available_other_uses (A-19; see gaps); same_act to importers.quota_holders quantity_traded (a trade seen from the seller). Stake k1 (A-21, five-year review).
- importers.near_threshold: alternative reclassification, reading U1-a (A-8, exempt mixtures, "assumed total weight"); link substitute from reclassification to buyers price_paid (A-8): more exempt blends, a lower sugar price than under the bare quota.
- importers.quota_holders: asset (A-5 survive the review, A-18 no exporter administers a share, so the rent stays in Calvar); yield (A-18); timing carry_over of inventory_held (A-6, "finance and store extra imports"); stake k1 (A-21).
- sellers.foreign: currency link to export_industries quantity_supplied (A-17).
- officials.enforcement, taxpayers: empty lists (nothing the core rules need beyond the seed).

## Round 2 (depth 2; revisits listed as node#2)
Nodes: buyers#2, buyers.border, consumers, export_industries, importers.near_threshold#2, importers.quota_holders#2, producers.beet_factories, producers.sweetened_goods, sellers.substitutes.
- buyers#2: price_paid was `ambiguous` (the cap pushes up, the exempt-blend leak pushes down): proposed a dominance, response argument (CR-12e, 0.9 and 1.0: the response is partial), premise "Blends and syrups at or below the 65% line can serve only some users, so imports in that form cannot replace all the sugar the quota keeps out." (judged).
- buyers.border: complement link to quantity_complement and substitute to retailers.border quantity_traded (A-16, other groceries on the same trips).
- consumers: own_price to quantity_demanded. export_industries: input link to workers.export_industries employment,hours_worked (same shape as WE-013).
- importers.near_threshold#2: the reclassification effect differed by reading (U1-a increase, U1-b none), so I gave the dry-weight reading its own alternative (reading U1-b, premises A-8 and "When sugar is counted against dry weight, a narrower range of blends and syrups still falls at or below the 65% line.", judged). Both readings exempt mixtures at or below the line, only the range differs; without it the reading made price_paid differ by reading and dominance could not be applied (see gaps). Stake k1 (lobbying over the reading, A-21, CR-4 1.1).
- importers.quota_holders#2: input link to importers.refineries quantity_supplied (A-15), `parts` refineries in quota_holders (A-20 is used in round 3), dominance for resources_available_other_uses (free shares vs compliance cost: ambiguous otherwise), premise "The value of the free quota shares to their holders far exceeds their cost of compliance." (judged).
- producers.beet_factories: input links to input_suppliers.beet_growers quantity_traded and workers; yield links to owners.beet_land asset_value and own investment_target (A-5); stake (A-21).
- producers.sweetened_goods: substitute to sellers.imported_goods quantity_traded (A-9); yield to capital_stock_target and owners.sweetened_goods asset_value (A-10, plants last 15 to 25 years); input link to workers; stake (A-21).
- sellers.substitutes: yield to investment_target (A-13).

## Round 3 (depth 3; last round, facts proposed here still enter the final run)
Nodes: buyers#3, buyers.border#2, consumers#2, importers.near_threshold#3, importers.quota_holders#3, importers.refineries, input_suppliers.beet_growers, owners.beet_land, owners.sweetened_goods, producers.beet_factories#2, producers.sweetened_goods#2, retailers.border, sellers.imported_goods, sellers.substitutes#2, workers.beet_factories, workers.export_industries, workers.sweetened_goods. Empty lists for all but two:
- importers.refineries: asset on e_sugar seller side (A-20 large shares, A-5); input link to workers.refineries.
- input_suppliers.beet_growers: substitute link to producers.other_crops quantity_supplied (A-4, land and labour move out of other field crops).
Deliberately not proposed: a currency link from imported finished goods (it would oppose A-17, "not offset"); stocking up by buyers (no sentence or table row says buyers can store sugar); a second market for quota rights (not expressible, see gaps).

## Answers
Table (16 asked here plus the 6 seed premises, so every row A-1 to A-22 is used): A-1, A-2, A-6, A-8, A-12, A-22 (seed); A-3, A-4, A-5, A-7, A-9, A-10, A-11, A-13, A-14, A-15, A-16, A-17, A-18, A-19, A-20, A-21 (loop). Statements taken verbatim, p from the table.
Judged (3), p from section 1:
- "Blends and syrups at or below the 65% line can serve only some users, so imports in that form cannot replace all the sugar the quota keeps out." 0.85 (A-8 says "some users"; A-1: quota binds more tightly as demand grows).
- "When sugar is counted against dry weight, a narrower range of blends and syrups still falls at or below the 65% line." 0.75 (section 1 says total weight is the reading more favorable to blend importers).
- "The value of the free quota shares to their holders far exceeds their cost of compliance." 0.9 (compliance is a register and two ports; shares are permanent and tradable over 350,000 t a year, at a domestic price above a world price that is below beet cost).

## What the format could not hold
1. Dominance is applied after propagation (situation.dominate), so settling buyers' price_paid as `increase` leaves every downstream consequence reached through it `ambiguous` (beet factories, corn syrup, consumers, sweetened-goods makers, border shopping, employment, asset values: 21 of 47 reported). Each would need its own dominance fact with the same premise; I did not hand-sign 20 of them (they would be signs the proposer states, not the engine).
2. Dominance is skipped for a consequence whose sign differs by reading. A reading that only adds an exempt alternative flips a clean `increase` into `ambiguous` under one reading and blocks the dominance; I worked around it by giving both readings the exempt alternative (the readings truly differ in range, not in kind), but a reading whose exempt form exists under only one reading cannot be settled.
3. A quota right's secondary market (sale or lease of shares, the lease price, entrants buying in, the price of the right) has no exchange to sit on: `capped` without `wider_price` gives holders `asset_value` but no `right_lease_price`, and a proposal cannot add an exchange.
4. A capped price has no transfer: `transfer` needs a held line, so buyers' extra spending (A-19: total spending on sugar and sweeteners rises) and the matching rent to holders were encoded as a `cost` link from price_paid to resources_available_other_uses, a stretch of that relation.
5. Seizure and the triple fine (op 3 on evasion, CR-8e confiscation) and the 5-year review (expectations on the quota's life, no expiry) have no fact; only `outside` (A-12) and the asset premise A-5 stand for them.
6. The unsatisfied seller (sellers.foreign) is upstream of the exchange I chose (importers sell on the domestic market): `unsatisfied_seller` accepts it but the exchange then mixes two legs.
7. A window-only effect (holders' extra imports to qualify, stocks held) cannot be followed by its reversal after the allocation date; the engine has no "after allocation" window for `qualifies`.
8. `parts` are proposed at the part's own node, which is reached only by an effect; importers.refineries had to be reached through a link before it could be declared part of importers.quota_holders.
