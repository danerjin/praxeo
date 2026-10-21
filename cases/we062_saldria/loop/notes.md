# WE-062 expand loop, blind run: notes

Read: section 1 of the example and, in the assumption table, only the ID, Statement, Type and p columns (cut with `-f2-5`). Nothing else of the example, no `05_examples_core/`, no existing file under `cases/we062_saldria/` other than what I created here. Branch `loop-we062_saldria` from ab5d6eb.

Files: `policy.txt` (section 1), `seed.json`, `proposals.json`, `answers.json`, `situation.json` (final). Output: DONE in 3 rounds, 29 questions (plus 5 seed premises), 25 nodes visited, 13 of them with proposals (54 proposals).

## Seed (CR-1)
Four exchanges: `e_dom` (packaging_users buy from converters.domestic), `e_imp_empty` (importers.packaging buy from converters.foreign), `e_imp_goods` (importers.goods buy from sellers.foreign.packaged_goods, packaging around imported goods), `e_export` (buyers.foreign buy from converters.domestic; "chargeable whether or not the component is later exported ... No export relief"). Price variables price_paid / net_price_received. Charge k1 on each (payer: the manufacturer = seller on e_dom and e_export; the importer of record = buyer on the two import exchanges), receiver officials.enforcement, receipt tax_revenue, projection tax_revenue_vs_static_projection. Compliance for the three liable classes, enforcer k4 (Revenue Service), funded by taxpayers, announced k1. No held line, backstop, discretion, means, transfer or early_price: the Act is a tax with exemptions, none of those operations applies. Exemptions K2 and K3 are not seed facts (the format has no place for an exemption); they appear only as the sentences alternatives rest on.

Seed premises (ids are lowercase because the id becomes a clingo atom; `A-2` failed to ground):
- a2 = A-2 (0.75, table): moves buyer on e_dom and e_imp_empty.
- a12 = A-12 (0.80, table): moves seller on e_export.
- a24 = A-24 (0.90, table): funded.
- s1 (0.70, judged): moves buyer on e_imp_goods. "Foreign sellers of packaged goods, with many other markets, absorb little of the tax on the packaging around their goods." Not in the table; A-2 is about empty packaging only, section 1 says Saldria buys about 0.4% of world resins.
- s2 (0.95, judged): announced k1. "Firms expect the tax to take effect on 1 January 2028 as enacted." Section 1: announced 2 March 2027, enacted 28 June 2027.

## Round 1 (depth 1), derived effects at each node
Nodes: converters.domestic, converters.foreign, buyers.foreign, importers.packaging, importers.goods, officials.enforcement, packaging_users, sellers.foreign.packaged_goods, taxpayers.
Proposed:
- converters.domestic (14): alternatives reclassification (A-32, "plastic is the heaviest material by weight"), product_attribute = recycled content (A-4, s.4(1)), specification_level = lighter (A-5), legal_breach (A-17, mass-balance evidence and penalty), relocation_out_of_area (A-13, no export relief); stake (A-18); links quantity_traded to workers.converters (A-25), to input_suppliers (no premise: resin all imported); net_price_received (yield) to owners.converters asset_value (A-20, A-19) and to own investment_target (A-19); product_attribute to recyclers.domestic quantity_supplied (input, A-27), to input_suppliers quantity_demanded (substitute, judged premise "Recycled resin takes the place of virgin resin in the components that use it."), to recyclers.domestic price_complement (A-10); reclassification to sellers.substitute_packaging quantity_supplied (same_act, A-6).
- importers.packaging (8 after round 2): alternatives transaction_size (A-14, K3), reclassification (A-15, importer of record), legal_breach (A-17), specification_level (A-5); timing bring_forward quantity_demanded and carry_over inventory_held (A-16, with the announced premise s2); link to importers.small_packaging quantity_traded (substitute, A-30).
- importers.goods (7 after round 2): alternatives transaction_size (A-14), reclassification (A-15), legal_breach (A-17); timing bring_forward (A-16); links price_paid to consumers.packaged_goods price_paid (output, A-11), quantity_traded to importers.small_goods quantity_traded (substitute, A-22).
- packaging_users (7): stake (A-18); links price_paid to consumers (output, A-11), own_price to own quantity_demanded (A-3), cost to exporters.packaged_goods quantity_supplied (A-12, A-11), quantity_traded to own quantity_substitute (substitute, A-6), quantity_substitute to sellers.substitute_packaging quantity_supplied (same_act, A-6) and net_price_received (same_act, A-7).
- buyers.foreign (1): quantity_traded substitute to converters.foreign quantity_supplied (A-12).
- converters.foreign, sellers.foreign.packaged_goods, officials.enforcement, taxpayers: empty. Foreign sellers have many other markets (A-2) and Saldria is a tiny buyer; the revenue goes to the general budget and "OC-1 is applied to the payers, and the recipients are not signed".
Answers: 21 questions, all 21 matched the table except "Recycled resin takes the place of virgin resin..." (judged 0.9: section 1 prices recycled and virgin resin side by side). Table answers: A-3, A-4, A-5, A-6, A-7, A-10, A-11, A-13, A-14, A-15 (0.4), A-16, A-17, A-18, A-19, A-20, A-22, A-25, A-27, A-30, A-32, A-12 already in seed.

## Round 2 (depth 2)
Nodes: consumers.packaged_goods, exporters.packaged_goods, importers.small_goods, importers.small_packaging, input_suppliers, owners.converters, recyclers.domestic, sellers.substitute_packaging, workers.converters.
Before this round I added to the round-1 nodes importers.packaging and importers.goods a currency link (quantity_traded to export_industries quantity_supplied, A-21; section 1: own currency and a floating exchange rate). I had missed it in round 1; it is a round-1 node fact added late, and it was the only edit of an earlier round.
Proposed:
- consumers.packaged_goods: own_price to own quantity_demanded (no premise); quantity_demanded substitute to own quantity_substitute (A-33, loose produce and refill water).
- exporters.packaged_goods: quantity_supplied input to workers.exporters (judged premise "Exporters of packaged goods adjust their labor to their output.", 0.8).
- importers.small_goods: part_of importers.goods. No dominance: no premise says which direction wins for goods.
- importers.small_packaging: part_of importers.packaging; dominance on importers.packaging quantity_traded = decrease, kind empirical, premise A-31 (0.65). This turned the ambiguous total (imports of empty packaging by liable firms fall, small users' direct imports rise) into a reported decrease.
- recyclers.domestic: stake (A-18); quantity_supplied input to workers.recyclers (A-23); price_complement yield to municipalities quantity_supplied (A-26); price_complement cost to converters.recycled_heavy product_attribute (A-8, the new class: components above 30% on the counterfactual path); price_complement yield to own investment_target (A-19).
- sellers.substitute_packaging: quantity_supplied input to workers.substitute_makers (A-23); net_price_received yield to own investment_target (A-19).
- input_suppliers, owners.converters, workers.converters: empty (foreign resin sellers; Saldria buys 0.4% of world resin; nothing further the policy text supports).
Answers: A-33 and A-26 and A-23, A-21, A-8 from the table; one judged (exporters' labor). 7 answered this round.

## Round 3 (depth 3)
Nodes: export_industries, converters.recycled_heavy, municipalities, workers.exporters, workers.recyclers, workers.substitute_makers; the engine then reached workers.export_industries (an extra node after export_industries' proposal), answered empty.
Proposed: export_industries quantity_supplied input to workers.export_industries (judged premise "Export industries adjust their labor to their output.", 0.8); converters.recycled_heavy: part_of converters.domestic, links product_attribute to recyclers.domestic quantity_supplied (A-27) and to input_suppliers quantity_demanded (substitute, the judged resin premise). Others empty. These produce the opposite chains on recyclers.domestic and input_suppliers, left ambiguous (no dominance premise exists).
Answers: 1, judged.

## Final engine output
DONE in 3 rounds, 29 questions; situation in `situation.json`. Reported effects include: packaging_users price_paid up and quantity_traded down; importers.packaging price_paid up, quantity_traded down (via A-31); converters.domestic net_price_received down, quantity_traded down, product_attribute ambiguous; sellers.substitute_packaging net_price_received and quantity_supplied up; officials.enforcement tax_revenue up with the shortfall against the static projection down; ambiguous: importers.goods quantity_traded, recyclers.domestic (quantity_supplied, price_complement, investment_target), input_suppliers quantity_demanded, municipalities quantity_supplied, export_industries quantity_supplied.

## What the format could not hold
1. An exemption is not a fact kind. K2 (30% recycled, measured per component or averaged) and K3 (10 t notch on the previous year) appear only as the source sentences of alternatives. The two readings of U1 get no representation: there is no per-reading sign for a chain, so I could not record that the sign depends on U1-a or U1-b. A-9 (firms with both cheap and expensive components) has no home for the same reason.
2. Alternatives fire only for a chooser who is a charge payer (chooser/3 is derived from the charge). Packaging users, who bear the tax through price, cannot be choosers; their reduction of taxed plastic (A-3) had to be expressed as own_price and substitute links.
3. Assets and yields (CR-7) are tied to a held line; a charge creates none. Plant values and returns had to come as `yield` links from a price effect.
4. A node is proposed once. Effects that reach an already-visited actor in a later round (converters.domestic product_attribute, packaging_users quantity_demanded) get no second node, so a new link that actor needs can only be added by editing its first proposal.
5. Quantity-to-price steps: no relation takes a quantity to a price except same_act/complement/input/yield (all same direction). The dearer recycled resin (A-10) is carried on `price_complement` with the complement relation, and the dearer board (A-7) on a same_act link to net_price_received: both are stretches of the vocabulary.
6. A-29 (foreign suppliers cannot document recycled content, so taxed as 0%) and A-28 (campaign spending unchanged on both paths, p 0.45) found no fact to rest on; A-34 (real rate falls, long run) and A-1 (the tax is collected from most liable firms) have no fact either: the format has no premise-only or time-trend fact.
7. The tax's incidence on exports: converters' exports at prices set abroad needed a fourth exchange (buyers.foreign) in the seed; moves of the seller on that exchange puts the tax on net_price_received.
8. Clingo atoms: assumption ids must be lowercase atoms (`a2`, not `A-2`) in the seed.
