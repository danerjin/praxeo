# WE-042 Aluminum tariff with export drawback

Analyst: draft (Handbook 0.8, held-out test)  |  Rule catalog version: 0.8  |  Status: awaiting expert review

A stylized policy in a fictional country. It resembles real tariffs with "duty drawback" but is not modeled on any one of them. It is a held-out test of catalog 0.8: a tariff on a material (TX-7, DM-1) combined with a refund of that tariff to anyone who exports goods made with the material, on documentation. The refund is a payment conditioned on goods crossing the border, so it brings in SB-10 (an export subsidy, with round trips and a check on the return crossing), RS-4 (payments that depend on a crossing), RS-5 (the line between covered and uncovered aluminum, and between "imported" and other content), TX-8 in both directions of the currency link, CR-8b (who pays and who receives each transfer) and CR-12's three kinds of opposing chain. The unclear provision is whether domestic metal of the same grade can stand in for imported metal in a claim ("substitution drawback"). Health, safety and environmental effects (smelter emissions) are out of scope for version 1. The probabilities are illustrative; the evidence column says what a real analysis would cite.

## 1. Policy record

**Vessland Aluminum Safeguard and Drawback Act.** Vessland is a trading country of about 9 million people with its own currency, the crown, and a floating exchange rate. It uses about 1.0 million tonnes (t) a year of primary aluminum and semi-finished aluminum products (ingot, billet, slab, plate, sheet, foil, rod, wire and extruded profiles), at a world price of about $2,500 a tonne. Two domestic smelters, with a combined capacity of 470,000 t and about 3,800 employees, produce about 400,000 t (85% of capacity); electricity is about 35% of their cost and is bought from the state grid. The other 600,000 t is imported. Vessland buys about 1.5% of the aluminum traded in the world.

About 1,200 firms use aluminum (rolling and extrusion mills, can makers, cable makers, makers of vehicle parts, window frames, machinery and heat sinks), employing about 60,000 people. The aluminum content of their exports is about 250,000 t a year: about 100,000 t of it imported metal and 150,000 t domestic metal. The remaining 750,000 t is used in goods sold in Vessland (500,000 t imported, 250,000 t domestic). Machined and stamped parts are cut from plate and billet and leave 25% to 40% of the metal as process scrap; cans, foil and cable leave 2% to 5%. Secondary producers (remelters) make about 120,000 t a year from scrap, and Vessland exports about 60,000 t of scrap; the domestic scrap price sits near the export price of scrap less about $40 a tonne of freight.

Vessland's main industrial region lies 30 to 60 km from the border with Ostrel, which has no tariff on aluminum. Goods cross the border with customs declarations; trucking costs about $30 a tonne each way.

The trade minister announced the measure on 3 February 2027. Parliament passed it on 20 May 2027, and it applies to aluminum entered on or after 1 September 2027. The tariff expires on 31 August 2031 unless Parliament extends it after a review in 2030.

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Tariff | `tariff` (ad valorem) | Imports of unwrought aluminum and semi-finished products (ingot, billet, slab, plate, sheet, foil over 0.2 mm, rod, wire, profiles) | Importers of record | 20% of customs value: about $500 a tonne at $2,500. | Aluminum scrap. Finished goods and parts containing aluminum (vehicles and their parts, appliances, windows and doors, fabricated structures, cable assemblies, cans and containers). |
| K2 Drawback | Refund of K1, conditional on export | Goods manufactured in Vessland "using imported aluminum on which the tariff was paid" and exported | Paid to the exporter, on claim | 99% of the tariff paid on the aluminum used in manufacturing the exported goods. Claims within three years of the import, with the import entries, a bill of materials and proof of export; paid within 120 days of an accepted claim. The importer of record may designate its entries to the exporter in writing. "Aluminum used" may be shown from the claimant's production records or, at its option, from Customs' standard yield tables, which count process scrap as used (for machined parts, 1.35 t of metal per tonne of product). | Unaltered re-exports of imported metal (not "manufactured"). |
| K3 Re-import rule | Condition of K2 | Exported goods for which drawback was paid | Importers of such goods | If the goods, or goods made from them, are re-imported within three years, the importer must declare it and repay the drawback; undeclared re-imports found on audit repay it plus 20%. | — |
| K4 Revenue and administration | Enforcement and revenue use | K1 to K3 | Customs Service | Tariff receipts go to the general fund; drawback is paid out of them. Customs administers K2 and K3 "within its existing appropriation". | — |

Customs' static projection of revenue: 600,000 t × $500 = $300 million a year, less drawback of at most about 250,000 t × $495 = $124 million.

Unclear provisions:
- **U1, substitution.** K2 pays on goods made "using imported aluminum on which the tariff was paid". Reading U1-a (direct identification): the claimant must show that the metal on which the tariff was paid, or metal traced to it by lot, went into the exported goods. Reading U1-b (substitution): aluminum of the same grade (alloy and form) used in the exported goods within three years of an import qualifies against that import's entry, whatever the metal's origin, so domestic metal can stand in for imported metal. Customs has not issued guidance and no court has ruled. Readings get no probability; where a sign depends on one, each reading's sign is reported.

The counterfactual is Vessland without the Act: no tariff and no drawback, at the same world price.

## 2. Classification

| Component | Rothbard type | Binding? | Rule families |
|---|---|---|---|
| K1, as a tax | Binary: a forced payment by importers to the state. CR-1: operation 3 on the option of importing covered aluminum. | Yes, from 1 September 2027 | TX-1, TX-2, TX-5, TX-9, DM-1 |
| K1, as a privilege | Triangular: makes buying foreign metal dearer to the benefit of the smelters | Yes, while imports remain a material share of supply (A-1) | TX-7, TX-8, RS-1, RS-4, RS-5, RS-14, RS-16, SB-4 |
| K2 | Binary: a refund from the general fund, attached to the option of exporting goods with qualifying content. CR-1 (0.8 clarification): a refund attached to a thing (the exported good) is operation 3 on the option of exporting it, for anyone who holds such goods. Where the yield tables count process scrap, the refund exceeds the tariff borne on the metal in the product (section 5), so that part is an export subsidy. | Yes, for exporters with qualifying content; which content qualifies depends on U1 | SB-10, RS-4, RS-5, RS-8, TX-5, CR-8b |
| K3 | A check on the return crossing: CR-1 operation 3 (a repayment, and a penalty if found on audit, attached to an undeclared re-import) | Yes, as far as audits detect re-imports (A-9) | SB-10, RS-3, CR-4 |
| K4 | Binary: administration within a fixed appropriation (A-17); revenue to the general fund | Yes | OC-3 (fixed-budget case), CR-8b, CR-8d |

**The transfers (CR-8b).** Three payments run through the Act, and each is recorded on both sides. (1) Domestic users pay smelters more for domestic metal: users' side in C-2 and C-41, smelters' side in C-1 and C-31. (2) Users pay the tariff on imported metal to the state, which keeps what it does not refund: users' side in C-2 and C-41, the state's in C-3 and the general fund's recipients in C-42. (3) The fund refunds tariff to exporters: the fund's side in C-4, the exporters' in C-46 and C-47.

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `smelters` (`sellers.substitutes`) | The two domestic smelters | Foreign metal is taxed; they can price up to import parity. |
| `smelters.owners` (`factor_owners.specific`) | Owners of the smelters | Specific, durable capital; expected earnings rise for four years and perhaps longer. |
| `smelter_workers` | Employees of the smelters | More output at the smelters. |
| `users.home` (`buyers.current`) | Firms using covered aluminum for goods sold in Vessland | Pay about 20% more for metal, imported or domestic. |
| `users.home.finished` | Those of them making finished goods and parts not covered by K1 (window frames, parts, appliances) | Input up 20%; their own products compete with tariff-free imports. |
| `fabricators.mixed` | Firms making uncovered goods both for Vessland and for export | Home sales bear the tariff; export sales get it back. |
| `exporters.low_scrap` | Exporters of cans, foil, cable (2% to 5% scrap) | Pay the tariff, claim 99% back months later; under U1-a only on traced imported metal. |
| `exporters.high_scrap` | Exporters of machined and stamped parts (25% to 40% scrap) | As above, but the yield tables count their process scrap, which they sell at the domestic scrap price. |
| `exporters.domestic_metal` | Exporters now buying domestic metal (150,000 t of content) | U1-a: no refund unless they switch to traced imported metal. U1-b: refund against any same-grade import entry. |
| `importers` (`intermediaries`) | Metal traders and service centers | Pay the tariff; lose volume; may designate entries to exporters. |
| `remelters`, `scrap_sellers` | Secondary producers and scrap dealers | Scrap is untaxed and substitutes for primary metal. |
| `buyers.aluminum_goods` | Buyers in Vessland of goods made with aluminum | Domestic makers' costs rise; imported finished goods are untaxed. |
| `sellers.foreign` | Foreign smelters; foreign makers of finished aluminum goods | Sell less metal and more finished goods to Vessland. |
| `buyers.foreign` | Foreign buyers of Vessland's parts | Face Vessland exporters whose costs change. |
| `neighboring_jurisdictions` | Fabricators in Ostrel | Untaxed metal, 30 to 60 km away. |
| `export_industries.other` | Vessland's other exporters (food, timber, tourism) | Linked through the currency relation (TX-8). |
| `input_suppliers` | The state grid, as seller of electricity to the smelters | More power sold to smelters. |
| `officials.enforcement` | Customs | Collects the tariff, verifies claims, audits re-imports, within a fixed appropriation. |
| `taxpayers`, recipients of other general-fund spending | Those who gain from the fund's net receipts | One or more of them gains from lower taxes, less borrowing or more spending. |

## 4. Direct effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | `smelters` | `net_price_received` | increase | short–medium | TX-7, CR-9 | A-1, A-2 |
| C-2 | `users.home` | `price_paid` (covered aluminum, imported and domestic) | increase | short–medium | TX-7, TX-2, DM-1 | A-1, A-2, A-14 |
| C-3 | `officials.enforcement` (general fund) | `tax_revenue` (tariff, net of drawback) | increase | short | TX-1, CR-8b | A-2, A-3 |
| C-4 | `officials.enforcement` (general fund), paid to exporters | `subsidy_outlay` (drawback refunds) | increase | short | CR-8b | A-26 |

The visible effects: smelters get a better price and the state collects revenue (C-1, C-3), which the Act's supporters point to, and exporters get their tariff back (C-4), which is the point of the drawback. Users pay import parity, about $3,000 a tonne, for both foreign and domestic metal (C-2): Vessland's purchases are 1.5% of world trade, so foreign smelters lose little by selling elsewhere and absorb almost none of the tariff (DM-1, A-14; C-38). C-3 is positive under either reading, because covered imports exceed the aluminum content of exports (A-3).

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-5 | `smelters` | `quantity_supplied` | increase | short–medium | TX-7, CR-7a, CR-12e | A-1, A-4 |
| C-6 | `smelter_workers` | `employment`, `hours_worked` | at_least_one_increase | short–medium | TX-7, CR-9 | A-1, A-4 |
| C-7 | `users.home` | `quantity_traded` (covered aluminum, all sources) | decrease | short–medium | TX-2, CR-4c, OC-4 | A-1, A-2 |
| C-8 | `importers` | `quantity_traded` (covered imports, from 1 September 2027) | decrease | short–medium | TX-2, TX-7, CR-12e | A-1, A-2 |
| C-9 | `importers`, `users.home` | `quantity_traded` (covered imports, February to August 2027) | increase | short | RS-8 | A-21 |
| C-10 | `users.home` | `inventory_held` (covered aluminum, at 1 September 2027) | increase | short | RS-8, CR-10a | A-21 |
| C-11 | `users.home` | `quantity_substitute` (secondary aluminum from scrap) | increase | short–medium | RS-1 | A-5 |
| C-12 | `importers`, `users.home` | `reclassification` (imports reshaped into uncovered fabricated forms) | increase | short–medium | RS-5, TX-4 | A-7 |
| C-13 | `exporters.domestic_metal` | `reclassification` (supply switched to imported metal, lots designated to export lines) | U1-a: increase; U1-b: no_change | short | RS-5, CR-4 | A-20 |
| C-14 | `smelters` | `quantity_traded` (metal sold to exporters) | U1-a: decrease; U1-b: ambiguous | short–medium | CR-4, CR-9 | A-20 |
| C-15 | `exporters.low_scrap`, `exporters.high_scrap` | `compliance_cost` (drawback claims: entries, bills of materials, proof of export) | increase | short | TX-5, CR-8c | A-26 |
| C-16 | `exporters.low_scrap`, `exporters.high_scrap` | `compliance_cost` (lot tracing, segregated stocks) | U1-a: increase; U1-b: no_change | short | CR-1, CR-8c | A-20 |
| C-17 | `exporters.low_scrap` | `price_paid` (aluminum, net of drawback) | increase | short–medium | CR-1, CR-8b, CR-10 | A-1, A-26 |
| C-18 | `exporters.high_scrap` | `price_paid` (aluminum net of drawback and scrap sales, per tonne of product) | decrease | short–medium | SB-10, CR-12e | A-6, A-20, A-26 |
| C-19 | `exporters.high_scrap` | `quantity_supplied` (exports of machined and stamped parts) | increase | short–medium | SB-10, RS-4, CR-7a | A-6, A-8 |
| C-20 | `fabricators.mixed` | `quantity_traded` (sales of uncovered goods in Vessland) | decrease | short–medium | RS-14, CR-4, CR-7a | A-1, A-15 |
| C-21 | `users.home.finished` | `quantity_supplied` (uncovered goods for the Vessland market) | decrease | medium | RS-14, RS-6 | A-1, A-15 |
| C-22 | `users.home.finished` (workers) | `employment`, `hours_worked` | at_least_one_decrease | medium | RS-6, RS-14, OC-5 | A-1, A-15 |
| C-23 | `exporters.high_scrap`, `exporters.low_scrap`, `importers` | `legal_breach` (drawback kept on goods re-imported undeclared) | increase | medium | SB-10, RS-4, CR-1, CR-4 | A-9, A-10 |
| C-24 | `smelters`; `users.home`, exporters | `lobbying_effort` (smelters: renewal, U1-a, a tariff on finished goods; users and exporters: U1-b, exclusions, no renewal) | increase | medium | RS-7 | A-11 |

**Smelters (C-1, C-5, C-6).** With imports still supplying most of the market (A-1), the domestic price rises to import parity, and smelters run their idle 70,000 t (A-4). Whether they add capacity beyond that is not reported: restarting or building a potline pays back over more than the tariff's four years, so it rests on owners expecting renewal (A-19, p = 0.35, below the cut-off).

**The drawback, reading by reading.** Under both readings an exporter pays about $3,000 a tonne for metal and receives $495 back after the claim is accepted, so its net cost is about $2,505 plus the claim's cost and the months between paying and being refunded (C-15, C-17; CR-10, LW-7).
- *U1-a.* Only traced imported metal qualifies. An exporter using domestic metal now pays $3,000 with no refund, against $2,505 net for traced imported metal. CR-4 (x: domestic metal, y: traced imported metal): those who can, switch to imported metal and keep it in separate, traced lots (C-13, C-16; A-20). Smelters lose those sales (C-14). They do not lose the tonnage: the freed metal is sold to home users at the same import-parity price, displacing their imports. The home market's imports (500,000 t) are far larger than the 150,000 t that moves, so this is arithmetic on the case's figures (CR-12e), and C-5 holds under U1-a. The two flows cancel one for one in total imports, so C-8 is unchanged in sign; what changes is who buys which metal, at a cost in tracing and transport (C-16). Exporters who cannot switch (long contracts, alloys only the smelters make) bear the whole tariff on their content.
- *U1-b.* Domestic metal of the same grade qualifies against any import entry, the claimant's own or one designated to it. Exporters have no reason to change supplier (C-13 `no_change`), and smelters keep their sales to exporters at the higher price; the tonnage follows export output, which is `ambiguous` (C-14, C-36). Importers can sell designations; there are far more import entries (about 600,000 t a year, less after C-8) than export content (250,000 t), so by CR-6 the price of a designation falls toward the cost of preparing it, and exporters keep almost all of the refund. No sign is given for importers' receipts from designations.

**Where the drawback becomes an export subsidy (C-18, C-19).** The yield tables count process scrap as aluminum used. A maker of machined parts uses 1.35 t of plate per tonne of product and sells 0.35 t as scrap. Per tonne of product, against the counterfactual: it pays 1.35 × $500 = $675 more for metal, gets 1.35 × $495 = $668 back, and sells its scrap for 0.35 × Δs more, where Δs is the rise in the scrap price (C-27). Its net cost changes by 1.35 × $5 − 0.35 × Δs, which is negative once Δs exceeds about $19 a tonne. With Δs = $60 it falls by about $14 a tonne of product. This is arithmetic once Δs is known (CR-12e); the premise is A-6. The refund, a payment per unit exported, then exceeds the tariff borne on the exported metal, and SB-10 applies to that part: export sales of such parts pay more than before (C-19), and the gain is paid partly by the fund (the refund on scrap metal sold at home) and partly by buyers of scrap (C-27). For cans and cable, with 3% scrap, the same arithmetic gives 1.03 × $5 − 0.03 × Δs = $3.35 a tonne more at Δs = $60, so the net cost rises (C-17). SB-10's domestic-price clause does not carry over: these parts are not covered by K1, so domestic buyers can import them untaxed and the domestic price cannot rise above import parity; sales move abroad and imports replace them at home (C-20, C-25), rather than the domestic price rising toward the export price plus the subsidy (Gaps found, e).

**Home and export sales (C-20 to C-22).** A firm making uncovered goods sells at home against tariff-free imported goods and abroad at world prices. Its metal costs about 20% more for both, but only export sales get the tariff back. RS-14: its home competitors (imports) are exempt, so the quantity effect dominates at home (C-21, C-22). CR-7a: the yield of export sales has risen relative to home sales, so mixed firms move sales toward export (C-20). Whether they can sell more abroad at world prices is A-8.

**Timing (C-9, C-10).** Users can import untaxed until 31 August 2027 and store the metal (RS-8, A-21). Imports rise in the window and fall in the months after, when stocks are drawn down; the later fall has the same sign as C-8 and is part of it. No drawback is paid on pre-tariff metal, since no tariff was paid on it, so the window brings no claim forward (RS-8's Unless clause on claims acquired before a charge does not apply).

**Reclassification (C-12, C-13).** K1 draws two lines. One is between covered metal and uncovered fabricated forms: importers bring in profiles cut to length and drilled as "parts of structures", or sheet formed into containers, where the work costs less than $500 a tonne (RS-5, TX-4; A-7). The other, under U1-a only, is between imported and domestic content: firms reorganize supply and stocks so that imported lots are the ones used for export (C-13). Under U1-b that line does not exist.

**Round trips (C-23).** A firm near the border could import plate (pay $500 a tonne), make window frames or parts, export them to Ostrel, claim $495, and bring the same goods back. Finished goods enter untaxed, so the round trip would deliver the metal to Vessland users without the tariff, for about $60 a tonne of freight (RS-4: items drawn across a boundary by a payment that depends on the crossing, including round trips made only to claim it; SB-10). K3 checks the return crossing: a declared re-import repays the drawback, so declared round trips gain nothing and are not made. Undeclared ones keep the refund unless an audit finds them, which costs the refund plus 20% (CR-1, operation 3). CR-4 (x: no round trip, y: an undeclared round trip): where the gain ($495 less freight) exceeds the probability of detection times the repayment and penalty, some firms make them. Goods without serial identity are hard to trace (A-9), and bulky goods made near the border make the trip cheap (A-10). Every remaining round trip is a breach of K3 within the legal market, so it is recorded as `legal_breach`. Section 7 says how the check combines with the round-trip chain.

**Lobbying (C-24).** The tariff gives smelters a concentrated gain that depends on renewal in 2030 and on Customs' reading of U1; users and exporters bear concentrated costs. Each lobbies (RS-7, A-11). The counterfactual has no tariff to defend or attack after May 2027, so the change is an increase for each.

Not reported: content overstated in claims beyond the yield tables (`legal_breach`). The tables are generous enough that most claimants have no reason to go beyond them (A-25, p = 0.4).

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-25 | `sellers.foreign` (finished goods) | `quantity_supplied` (finished aluminum goods sold into Vessland) | increase | medium | RS-14, RS-16, CR-9 | domestic and imported finished goods: `substitute`, close | A-1, A-15 |
| C-26 | `neighboring_jurisdictions` (Ostrel fabricators) | `quantity_supplied` (finished goods for Vessland buyers) | increase | medium | RS-4 | Vessland and Ostrel fabrication: `across_border`, close near the border | A-15, A-23 |
| C-27 | `remelters`, `users.home` | `price_substitute` (scrap) | increase | short–medium | RS-16, CR-12e | primary and secondary aluminum: `substitute`, partial | A-5, A-6 |
| C-28 | `remelters` | `quantity_supplied` (secondary aluminum) | increase | short–medium | RS-16, CR-9 | as C-27 | A-5 |
| C-29 | `scrap_sellers` | `quantity_traded` (scrap exports) | decrease | short–medium | CR-7a, CR-9 | scrap at home and abroad: `across_border` | A-5 |
| C-30 | `input_suppliers` (state grid) | `quantity_traded` (electricity sold to smelters) | increase | short–medium | CR-9, RS-12 | electricity `input_to` smelting | A-4 |
| C-31 | `smelters.owners` | `asset_value` (smelters) | increase | short (from February 2027) | SB-4, CR-7c, CR-10c | — | A-1, A-12 |
| C-32 | `users.home.finished` (owners) | `asset_value` (firms making uncovered goods for Vessland) | decrease | short (from February 2027) | CR-7c, CR-10c | — | A-12, A-15 |
| C-33 | `buyers.aluminum_goods` | `price_paid` (goods with no close imported substitute: installed windows and facades, cans for local bottlers, custom profiles) | increase | short–medium | RS-14 | aluminum `input_to` these goods | A-1, A-16 |
| C-34 | `buyers.foreign` | `price_paid` (machined and stamped parts from Vessland) | decrease | short–medium | SB-10 | Vessland parts in Ostrel and regional markets | A-6, A-8, A-27 |
| C-35 | `export_industries.other` | `quantity_supplied` (exports) | ambiguous | medium | TX-8, CR-9, CR-12b | `currency`; electricity and labor shared with smelters: `input_to` | A-13 |
| C-36 | `exporters.low_scrap`, `exporters.high_scrap`, `fabricators.mixed` | `quantity_supplied` (exports of aluminum-containing goods, total) | ambiguous | medium | CR-12b | `currency`; foreign buyers | A-6, A-8, A-13, A-20 |
| C-37 | `importers`, `users.home` | `quantity_traded` (covered imports, net of the U1-a reshuffle) | decrease | short–medium | TX-7, CR-12e | — | A-1, A-20 |
| C-38 | `users.home` | `tax_share_borne` (tariff, against foreign smelters) | increase | short–medium | DM-1, CR-7b | — | A-14 |
| C-39 | `users.home.finished` | `tax_share_borne` (metal cost increase, against their buyers) | increase | medium | CR-7b | domestic and imported finished goods: `substitute` | A-15 |
| C-40 | `officials.enforcement` | `tax_revenue_vs_static_projection` | decrease | short | TX-9 | — | A-1, A-7 |

**Scrap (C-27 to C-29).** Users turn from primary metal to scrap (C-11). Scrap was being exported at the export price less freight, so as home demand rises, exports fall first (C-29) and the domestic price rises toward the price of imported scrap, a range of about $80 a tonne; remelters' output rises (C-28; RS-16). One chain pushes the other way: high-scrap exporters who expand (C-19) sell more process scrap at home (RS-13). That expansion pays only while Δs stays above about $19 (section 5), so it cannot bring the scrap price back to its old level. CR-12e's response argument applies here, because the response is driven by the scrap price itself: the tariff and its refund cancel except for the unrefunded 1%, so no second change drives it. The combined sign is an increase.

**Capitalization (C-31, C-32).** The tariff raises the expected earnings of the smelters and lowers those of firms making uncovered goods for the home market, for four years and longer if renewed. Both are capitalized when the change becomes expected: part of the way from the announcement in February 2027, as passage became likely, and the rest at passage in May (CR-7c, a change of limited duration). Exporters' values are not signed: under U1-b their costs barely change, and under U1-a it depends on whether each can switch.

**Buyers (C-33, C-34).** Where domestic buyers can import the finished good untaxed, the domestic maker cannot pass the cost on (C-21, C-39). Where they cannot (goods installed on site, bulky containers for local bottlers), the cost passes through (RS-14, A-16). Foreign buyers of high-scrap parts gain only where Vessland makers are a material share of their supply (A-27).

**Imports in total (C-37).** Chains: (−) home users buy less (C-7) and smelters supply more (C-5); (+) under U1-a, exporters switch 150,000 t to imported metal (C-13). The switch is matched one for one by smelter metal displacing home users' imports (section 5), an accounting identity used as a dominance premise (CR-12e). Decrease under both readings. C-8 records the same fact for importers.

**The currency link, both ways (C-35).** TX-8: fewer imports of metal leave foreigners with fewer crowns to spend on Vessland's exports. But K1 also raises imports of finished goods (C-25, C-26) and, through the drawback, may raise some exports (C-19), which gives Vessland's residents more foreign means and so draws more imports (TX-8, mirror case). Whether Vessland's total imports rise or fall depends on whether the fall in metal imports outweighs the rise in finished goods, which the case's figures do not settle. So the currency chain is itself `ambiguous`. Section 7 combines it with the other chain reaching other exporters.

**Stopping points.** Buyers of power from the state grid (C-30): the grid's tariff is regulated, and whether added smelter load raises it at the next review (PC-15) is depth 3 and not followed. The spending of users who pay more (C-41): a change in means alone, uses not named (CR-4). Workers moving from home fabricators to smelters and exporters (C-6, C-22): depth 3, not followed.

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `smelters`, `quantity_supplied`, short–medium | Home users' imports are displaced at import parity (TX-7, C-5). | U1-a: exporters switch to imported metal (C-14). | CR-12e, arithmetic: the 150,000 t that moves is redirected to home users, whose imports (500,000 t) are far larger. | **increase** (C-5), both readings. |
| `importers`, `quantity_traded` (covered imports), short–medium | U1-a: exporters' switch to imported metal (C-13). | Home users buy less and smelters supply more (C-7, C-5). | CR-12e, accounting identity: the switch is matched one for one by smelter metal displacing imports. | **decrease** (C-8, C-37). In the announcement window, **increase** (C-9), a separate window. |
| `remelters`, `users.home`, `price_substitute` (scrap), short–medium | Users turn to scrap (C-11, RS-16). | High-scrap exporters expand and sell more scrap at home (C-19, RS-13). | CR-12e, response argument: the expansion pays only while the scrap price stays more than about $19 above its old level. | **increase** (C-27). |
| `exporters.low_scrap`, `exporters.high_scrap`, `fabricators.mixed`, `quantity_supplied` (exports, total), medium | High-scrap parts become cheaper to export (C-19, A-6). Mixed firms move sales from home to export (C-20; A-8, p = 0.6, a kind (2) chain whose premise clears the cut-off). | Low-scrap exporters' net cost rises (C-17), by the whole tariff on content for those who cannot switch under U1-a; claim costs and delay (C-15). The currency chain (C-35) is itself `ambiguous` (kind (3)). | None | **ambiguous** (C-36), under both readings. A further (+) chain is not counted: if foreign smelters absorbed part of the tariff, the world price would fall and every claimant would get metal below its counterfactual cost. That chain is derivable (CR-7b) but needs A-18 (p = 0.15), so by CR-12's 0.8 clarification it is a kind (2) chain below the cut-off and is recorded in section 10. |
| `export_industries.other`, `quantity_supplied`, medium | Currency chain, if imports of finished goods rise by more than imports of metal fall (C-25, C-26). | Currency chain, if metal imports fall by more (TX-8). Smelters compete with other industries for electricity and labor (C-6, C-30; CR-9, competition for the same means). | None: the currency chain is `ambiguous` in its own right, and no premise covers the competition chain against both of its directions. | **ambiguous** (C-35). Kind (3) under CR-12's 0.8 clarification. |
| `exporters.high_scrap`, `exporters.low_scrap`, `importers`, `legal_breach` (undeclared round trips), medium | The refund kept on a re-imported good (SB-10, RS-4). | K3: repayment plus 20% if found on audit. | Not CR-12b: the check is a burden attached to the same option (CR-1, operation 3), not a second chain that can push round trips below their counterfactual level of zero. CR-4 decides, with the premise that detection is unlikely for some goods. | **increase** (C-23), given A-9 and A-10. If audits were thorough, `no_change`. |
| `users.home`, `price_paid` (covered aluminum), short–medium | TX-7. | — (terms-of-trade chain needs A-18, p = 0.15) | — | **increase** (C-2). |

**A chain no rule derives (kind (1)).** That Ostrel or other trading partners retaliate with tariffs on Vessland's exports would push C-35 and C-36 down. It rests on what foreign governments decide, which no core rule derives (compare TS-4). Tier C note, not a chain.

**Different variables are not netted (CR-12c).** Exporters' lower or higher net metal cost (C-17, C-18) and their claim costs (C-15, C-16) are kept apart.

## 8. Time structure

- **Announcement to effective date (February to August 2027).** Smelter and fabricator values move from February, part of the way, and the rest at passage in May (C-31, C-32). Users import and store untaxed metal (C-9, C-10). Smelters prepare to restart idle capacity (C-5). Exporters and Customs prepare claims procedures; under U1-a, exporters renegotiate supply contracts with smelters to switch to imported metal from September (C-13).
- **First months.** Imports fall below the counterfactual as stocks are drawn down (C-8). The first refunds arrive only after claims are prepared and accepted, so exporters carry the tariff for several months (C-17, C-46).
- **2027 to 2031.** Home fabrication of uncovered goods shrinks and finished-goods imports and Ostrel fabrication grow (C-21, C-25, C-26) as firms redeploy capital (CR-7b with CR-10b); so the burden on home fabricators is largest at first and shifts toward their buyers only where imports cannot replace them (C-39, C-33). Round trips grow as firms learn which goods audits miss (C-23).
- **Renewal in 2030.** The tariff's expiry limits what is capitalized (C-31) and what smelters invest (A-19 below the cut-off). Lobbying centers on the review and on U1 (C-24).
- **Erosion.** The tariff is ad valorem, so it does not erode with prices; the drawback is 99% of the tariff paid, so it moves with it. The yield tables fix scrap ratios in physical units, so the subsidy element moves with the scrap price (A-6), not with the metal price.

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-41 | `users.home` (those who keep buying covered aluminum) | `resources_available_other_uses` | decrease | What the higher metal price would otherwise have bought. Signed only for users who keep buying (CR-3, note). | OC-1, CR-8b, CR-3c |
| C-42 | `taxpayers`, recipients of other general-fund spending | `resources_available_other_uses` | at_least_one_increase | Nothing given up: the fund's net receipts allow lower taxes, less borrowing or more spending. The record names no use, so the recipients are a group. | CR-8b, CR-8d |
| C-43 | `officials.enforcement` | `enforcement_cost` (tariff collection, drawback verification, K3 audits) | increase | Customs staff time. | OC-3 |
| C-44 | `officials.enforcement` | `enforcement_cost` (other customs work) | decrease | Checks on other goods that the fixed appropriation no longer covers; the cost falls on those whom that work protected. | OC-3, CR-8a |
| C-45 | `importers` | `compliance_cost` (classification and tariff entries) | increase | The other uses of that staff time. | TX-5 |
| C-46 | `exporters.low_scrap` | `resources_available_other_uses` | decrease | The 1% not refunded, and the tariff carried for months before the refund. | CR-8b, CR-3c, CR-10 |
| C-47 | `exporters.high_scrap` | `resources_available_other_uses` | increase | Nothing given up: the refund on scrap metal plus the higher scrap price exceed the tariff borne. Paid by the fund (C-4) and by buyers of scrap (C-27). | CR-8b |

The metal home users no longer buy (C-7) is a prevented exchange: users and their former suppliers both lose the gain each expected from it (OC-4, CR-5a). The jobs home fabricators no longer offer (C-22) are visible only as a decline; those added at the smelters are visible as the policy's success (OC-5). Compliance with K2 is C-15 and C-16.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | Imports remain a material share of supply, so the domestic price is set at import parity. | binding | 0.9 | Smelter capacity 470,000 t against home use of about 750,000 t. | C-1, C-2 and most chains shrink; the domestic price would be set by the smelters' costs. |
| A-2 | Most covered imports pay the tariff; misdeclaration is limited. | enforcement | 0.85 | Customs' classification checks; the headings are well defined. | C-1 to C-3, C-7 and C-8 shrink. |
| A-3 | Covered imports exceed the aluminum content of exports under either reading, so the fund keeps net receipts. | other | 0.95 | 600,000 t imported against 250,000 t of content; imports fall but not by 350,000 t. | C-3 and C-42 fail. |
| A-4 | The smelters can bring their idle 70,000 t into use within months. | durability | 0.75 | Pots idled within existing lines; power contract allows more load. | C-5, C-6 and C-30 come later or shrink. |
| A-5 | Secondary aluminum substitutes for primary metal in some uses. | substitutability | 0.8 | Remelters' alloys used in castings and extrusions. | C-11, C-27, C-28 and C-29 not reported. |
| A-6 | The domestic scrap price rises by more than about $19 a tonne. | substitutability | 0.65 | The domestic price sits $40 below the scrap export price; exports of 60,000 t fall first, so the price can rise by up to about $80 before scrap is imported. | C-18 becomes an increase; C-19, C-34 and C-47 not reported; C-36 loses a (+) chain. |
| A-7 | Some imports can be reshaped into uncovered fabricated forms for less than $500 a tonne. | other | 0.7 | Cutting and drilling costs for profiles; container forming. | C-12 not reported; C-40 rests on C-7 alone. |
| A-8 | Mixed fabricators and makers of parts can sell more abroad at world prices. | alternative_uses | 0.6 | Their export share; size of regional markets. | C-19 and C-34 not reported; C-36 loses its (+) chains and becomes a decrease. |
| A-9 | K3 audits detect few undeclared re-imports of goods without serial identity. | enforcement | 0.65 | Audit rates; no serial marking on frames and parts. | C-23 `no_change`. |
| A-10 | For some bulky, low-value goods made near the Ostrel border, a round trip costs less than the refund. | mobility | 0.6 | Freight about $60 a tonne both ways against $495 of refund per tonne of content. | C-23 not reported. |
| A-11 | Smelters, users and exporters can organize at a cost below their stake. | other | 0.85 | Industry associations active on the bill. | C-24 not reported. |
| A-12 | Firms are valued on expected earnings, and buyers expect the tariff to last at least its four years. | expectations | 0.75 | Sale prices as multiples of earnings; the statutory term. | C-31 and C-32 not reported. |
| A-13 | Trade flows are not offset by capital flows in the period considered. | other | 0.6 | TX-8's premise; Vessland's capital account. | The currency chain in C-35 and C-36 vanishes; C-35 becomes a decrease (competition chain only). |
| A-14 | Foreign smelters have far better alternatives than Vessland's users. | substitutability | 0.9 | Vessland buys 1.5% of world trade. | C-38 not reported; the split is not signed. |
| A-15 | Buyers of uncovered finished goods can buy tariff-free imports, and home fabricators' capital is specific. | substitutability | 0.75 | Import shares of frames, parts and appliances; equipment specific to aluminum work. | C-20, C-21, C-22, C-25, C-26, C-32 and C-39 shrink. |
| A-16 | Some aluminum goods have no close imported substitute. | other | 0.7 | Goods installed on site; bulky containers for local bottlers. | C-33 not reported. |
| A-17 | Customs' appropriation does not rise with the new work. | revenue_use | 0.8 | K4 "within its existing appropriation". | C-44 not reported; the payers are taxpayers (OC-3, first case). |
| A-18 | Vessland's purchases are large enough to lower the world price. | other | 0.15 | 1.5% of world trade. | Below the cut-off: the terms-of-trade chain (section 7) is not reported. |
| A-19 | Smelters build or restart capacity beyond 470,000 t within the tariff's term, expecting renewal. | expectations | 0.35 | Potline payback of ten years or more; four-year term. | Below the cut-off; not reported. |
| A-20 | Under U1-a, most exporters using domestic metal can switch to traced imported metal of the same grade within a year. | substitutability | 0.7 | Standard alloys available abroad; supply contracts renewed yearly. | Under U1-a, C-13, C-14 and C-16 shrink; more exporters bear the whole tariff (C-17 larger). |
| A-21 | Users expect the tariff and can import and store metal ahead of 1 September at a cost below $500 a tonne. | expectations | 0.8 | Six months' notice; storage costs. | C-9 and C-10 not reported. |
| A-22 | Some home users keep buying covered aluminum at the higher price. | other | 0.95 | Few substitutes for many uses. | C-41 not reported. |
| A-23 | Some fabrication for the Vessland market can move to plants in Ostrel within the tariff's term. | mobility | 0.55 | Existing plants near the border; four-year term. | C-26 not reported. |
| A-24 | The fund's net receipts are used for lower taxes, less borrowing or other spending, not held idle. | revenue_use | 0.85 | Budget practice. | C-42 not reported. |
| A-25 | Claimants overstate content beyond the yield tables. | enforcement | 0.4 | The tables already count process scrap. | Below the cut-off; not reported. |
| A-26 | Exporters with qualifying content file claims; for most, the paperwork costs less than the refund. | other | 0.9 | $495 a tonne against claim costs. | C-4, C-15 and C-46 shrink; exporters bear the tariff (C-17 larger). |
| A-27 | Vessland's makers of machined and stamped parts are a material share of supply to some regional buyers. | other | 0.55 | Their share of parts sold in Ostrel. | C-34 not reported. |

## 11. Report

**The policy.** From September 2027 Vessland taxes imported aluminum metal and semi-finished products at 20% for four years. Exporters of goods made with imported aluminum can claim back 99% of the tariff on the metal used, on documentation, and goods re-imported after a refund must repay it. Scrap and finished goods are not taxed. Whether domestic metal of the same grade can stand in for imported metal in a claim is not settled.

**Visible consequences.** Smelters get a better price and run their idle capacity (C-1, C-5); their workers get more work (C-6). The state collects revenue (C-3) and refunds part of it to exporters (C-4). Users pay about 20% more for metal (C-2).

**Invisible consequences.**
- *Users and their buyers.* Users buy less metal (C-7) and more scrap (C-11), and reshape imports into forms the tariff does not cover (C-12). Makers of finished goods for the home market, competing with untaxed imports, cannot pass the cost on: they produce and employ less (C-21, C-22), their firms lose value (C-32), and imports and Ostrel plants take their place (C-25, C-26). Where buyers have no imported alternative, they pay more (C-33). Users who keep buying have less for other things (C-41).
- *Exporters.* For most, the refund leaves their metal cost slightly higher than without the policy, after the unrefunded 1%, the paperwork and the months of waiting (C-15, C-17, C-46). For makers of machined parts, whose process scrap is counted in the claim and sold at a higher scrap price, the refund exceeds the tariff they bear: the drawback works as a small export subsidy (C-18, C-47), so they export more (C-19) and some foreign buyers pay less (C-34). Mixed firms move sales from home to export (C-20).
- *Depending on the reading.* If only traced imported metal qualifies, exporters switch from domestic to imported metal and keep separate stocks (C-13, C-16), and smelters sell less to exporters (C-14) but the same tonnage overall, to home users (C-5). If substitution is allowed, none of this happens.
- *Round trips.* Some goods are exported to claim the refund and brought back undeclared (C-23).
- *Other markets.* Scrap rises in price (C-27); remelters produce more (C-28) and less scrap is exported (C-29); the grid sells more power to smelters (C-30). Smelter owners gain value from the announcement (C-31). Customs' other checks are reduced (C-44). Each side lobbies over renewal and over the reading (C-24).

**Ambiguous effects.** Total exports of aluminum-containing goods (C-36) and the exports of Vessland's other industries (C-35): the policy moves imports both ways (less metal, more finished goods), so the currency link can push either way. Per reading: smelters' sales to exporters (C-14).

**Key conditions.** Imports remain the marginal supply (A-1, p = 0.9). The export-subsidy element rests on the scrap price rising by more than about $19 a tonne (A-6, p = 0.65). Round trips rest on weak audits of goods without serial identity (A-9, p = 0.65). That foreign smelters bear almost none of the tariff rests on Vessland being a small buyer (A-14, p = 0.9); if they bore part, every claimant would gain (A-18, p = 0.15).

**What this analysis cannot say.** How large any effect is; whether smelter jobs gained outweigh jobs lost in fabrication; the size of the subsidy element; whether the tariff or the drawback is desirable; effects of smelting on emissions and health (out of scope for version 1).

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | smelters | net_price_received | increase | short–medium | visible | B | TX-7, CR-9 | A-1, A-2 |
| C-2 | users.home | price_paid (covered aluminum) | increase | short–medium | visible | B | TX-7, TX-2, DM-1 | A-1, A-2, A-14 |
| C-3 | officials.enforcement (general fund) | tax_revenue (net of drawback) | increase | short | visible | B | TX-1, CR-8b | A-2, A-3 |
| C-4 | officials.enforcement (general fund), to exporters | subsidy_outlay (drawback refunds) | increase | short | visible | B | CR-8b | A-26 |
| C-5 | smelters | quantity_supplied | increase | short–medium | visible | B | TX-7, CR-7a, CR-12e | A-1, A-4 |
| C-6 | smelter_workers | employment, hours_worked | at_least_one_increase | short–medium | visible | B | TX-7, CR-9 | A-1, A-4 |
| C-7 | users.home | quantity_traded (covered aluminum, all sources) | decrease | short–medium | invisible | B | TX-2, CR-4c, OC-4 | A-1, A-2 |
| C-8 | importers | quantity_traded (covered imports, from September 2027) | decrease | short–medium | invisible | B | TX-2, TX-7, CR-12e | A-1, A-2 |
| C-9 | importers, users.home | quantity_traded (covered imports, February–August 2027) | increase | short | invisible | B | RS-8 | A-21 |
| C-10 | users.home | inventory_held (at 1 September 2027) | increase | short | invisible | B | RS-8, CR-10a | A-21 |
| C-11 | users.home | quantity_substitute (secondary aluminum) | increase | short–medium | invisible | B | RS-1 | A-5 |
| C-12 | importers, users.home | reclassification (imports reshaped into uncovered forms) | increase | short–medium | invisible | B | RS-5, TX-4 | A-7 |
| C-13 | exporters.domestic_metal | reclassification (supply switched, lots designated to exports) | U1-a: increase; U1-b: no_change | short | invisible | B | RS-5, CR-4 | A-20 |
| C-14 | smelters | quantity_traded (metal sold to exporters) | U1-a: decrease; U1-b: ambiguous | short–medium | invisible | B | CR-4, CR-9 | A-20 |
| C-15 | exporters.low_scrap, exporters.high_scrap | compliance_cost (drawback claims) | increase | short | invisible | B | TX-5, CR-8c | A-26 |
| C-16 | exporters.low_scrap, exporters.high_scrap | compliance_cost (lot tracing, segregated stocks) | U1-a: increase; U1-b: no_change | short | invisible | B | CR-1, CR-8c | A-20 |
| C-17 | exporters.low_scrap | price_paid (aluminum, net of drawback) | increase | short–medium | invisible | B | CR-1, CR-8b, CR-10 | A-1, A-26 |
| C-18 | exporters.high_scrap | price_paid (aluminum net of drawback and scrap sales, per tonne of product) | decrease | short–medium | invisible | B | SB-10, CR-12e | A-6, A-20, A-26 |
| C-19 | exporters.high_scrap | quantity_supplied (exports of machined and stamped parts) | increase | short–medium | invisible | B | SB-10, RS-4, CR-7a | A-6, A-8 |
| C-20 | fabricators.mixed | quantity_traded (home sales of uncovered goods) | decrease | short–medium | invisible | B | RS-14, CR-4, CR-7a | A-1, A-15 |
| C-21 | users.home.finished | quantity_supplied (uncovered goods for Vessland) | decrease | medium | invisible | B | RS-14, RS-6 | A-1, A-15 |
| C-22 | users.home.finished (workers) | employment, hours_worked | at_least_one_decrease | medium | invisible | B | RS-6, RS-14, OC-5 | A-1, A-15 |
| C-23 | exporters.high_scrap, exporters.low_scrap, importers | legal_breach (undeclared round trips) | increase | medium | invisible | B | SB-10, RS-4, CR-1, CR-4 | A-9, A-10 |
| C-24 | smelters; users.home, exporters | lobbying_effort | increase | medium | invisible | B | RS-7 | A-11 |
| C-25 | sellers.foreign (finished goods) | quantity_supplied (into Vessland) | increase | medium | invisible | B | RS-14, RS-16, CR-9 | A-1, A-15 |
| C-26 | neighboring_jurisdictions (Ostrel fabricators) | quantity_supplied (for Vessland buyers) | increase | medium | invisible | B | RS-4 | A-15, A-23 |
| C-27 | remelters, users.home | price_substitute (scrap) | increase | short–medium | invisible | B | RS-16, CR-12e | A-5, A-6 |
| C-28 | remelters | quantity_supplied (secondary aluminum) | increase | short–medium | invisible | B | RS-16, CR-9 | A-5 |
| C-29 | scrap_sellers | quantity_traded (scrap exports) | decrease | short–medium | invisible | B | CR-7a, CR-9 | A-5 |
| C-30 | input_suppliers (state grid) | quantity_traded (electricity to smelters) | increase | short–medium | invisible | B | CR-9, RS-12 | A-4 |
| C-31 | smelters.owners | asset_value (smelters) | increase | short | invisible | B | SB-4, CR-7c, CR-10c | A-1, A-12 |
| C-32 | users.home.finished (owners) | asset_value | decrease | short | invisible | B | CR-7c, CR-10c | A-12, A-15 |
| C-33 | buyers.aluminum_goods | price_paid (goods with no close imported substitute) | increase | short–medium | invisible | B | RS-14 | A-1, A-16 |
| C-34 | buyers.foreign | price_paid (Vessland machined and stamped parts) | decrease | short–medium | invisible | B | SB-10 | A-6, A-8, A-27 |
| C-35 | export_industries.other | quantity_supplied (exports) | ambiguous | medium | invisible | B | TX-8, CR-9, CR-12b | A-13 |
| C-36 | exporters.low_scrap, exporters.high_scrap, fabricators.mixed | quantity_supplied (exports, total) | ambiguous | medium | invisible | B | CR-12b | A-6, A-8, A-13, A-20 |
| C-37 | importers, users.home | quantity_traded (covered imports, net of reshuffle) | decrease | short–medium | invisible | B | TX-7, CR-12e | A-1, A-20 |
| C-38 | users.home | tax_share_borne (against foreign smelters) | increase | short–medium | invisible | B | DM-1, CR-7b | A-14 |
| C-39 | users.home.finished | tax_share_borne (against their buyers) | increase | medium | invisible | B | CR-7b | A-15 |
| C-40 | officials.enforcement | tax_revenue_vs_static_projection | decrease | short | invisible | B | TX-9 | A-1, A-7 |
| C-41 | users.home (those who keep buying) | resources_available_other_uses | decrease | short–medium | invisible | B | OC-1, CR-8b, CR-3c | A-1, A-22 |
| C-42 | taxpayers, recipients of other general-fund spending | resources_available_other_uses | at_least_one_increase | short–medium | invisible | B | CR-8b, CR-8d | A-3, A-24 |
| C-43 | officials.enforcement | enforcement_cost (tariff, drawback, K3 audits) | increase | short | invisible | A | OC-3 | none |
| C-44 | officials.enforcement | enforcement_cost (other customs work) | decrease | short–medium | invisible | B | OC-3, CR-8a | A-17 |
| C-45 | importers | compliance_cost (classification and entries) | increase | short | invisible | A | TX-5 | none |
| C-46 | exporters.low_scrap | resources_available_other_uses | decrease | short | invisible | B | CR-8b, CR-3c, CR-10 | A-26 |
| C-47 | exporters.high_scrap | resources_available_other_uses | increase | short–medium | invisible | B | CR-8b | A-6, A-26 |

Final check (workflow): every (actor class, variable) reached by more than one chain is in section 7 or carries one sign from chains of the same sign (C-2; C-8 with its post-window draw-down). Group signs are used for labor (C-6, C-22) and the general fund's recipients (C-42). Every sign is against Vessland without the Act, not against a tariff without drawback; that is why exporters' net cost (C-17) is a small increase rather than the decrease the refund looks like. Each transfer has both sides (section 2). `resources_available_other_uses` is signed only for classes that keep paying (C-41, C-46) or receive (C-42, C-47). Timing: the import rush is signed per window (C-9 and C-8). Capitalization (C-31, C-32), enforcement and its funding (C-43, C-44) and the payers' side are recorded.

## Gaps found

**(a) Calculus gaps (a step no core rule covers).** None. Every step was derived from patterns or from CR-1 to CR-12. The nearest was foreign retaliation (section 7), which is a chain no rule derives and is recorded as a Tier C note under CR-12's 0.7 clarification, not a gap.

**(b) Unclear core rules.**
1. *CR-12b and a check on the same option.* SB-10 says to combine the round-trip chain with the check under CR-12b. Here the check does not produce a chain with an opposite sign on `legal_breach`: without the policy there are no round trips, so the check can lower the increase but not reverse it. It is a burden on the same option (CR-1, operation 3), and the sign comes from CR-4 with an enforcement premise. CR-12 could say that a provision that only burdens the response is not an opposing chain.
2. *CR-12e, "a second change the policy also causes".* For the scrap price, the expansion of high-scrap exports is driven by the scrap price and by the refund on scrap. The argument holds only because the tariff and the refund cancel except for 1%, so the scrap price is the only thing that changes. Deciding whether the refund counts as a "second change" took arithmetic; the clarification gives no test.
3. *CR-1, 0.8 refund attached to a thing.* It applied cleanly to the drawback (operation 3 on the option of exporting a good with qualifying content), although its example is a container deposit.

**(c) Missing or wrong patterns.**
1. *SB-10's preconditions and domestic-price clause.* SB-10's "If" is a fixed sum per unit exported; a drawback is a refund of a tax that varies with content. The pattern was applied only to the part of the refund that exceeds the tariff borne (the scrap allowance), which had to be found by arithmetic first. Its conclusion that the domestic price rises toward the export price plus the subsidy was wrong for these goods and was overridden: the goods are not taxed at import, so tariff-free imports cap the domestic price, and the result is that sales move abroad while imports replace them at home (C-20, C-25). SB-10 assumes, without saying so, that domestic buyers cannot import the good more cheaply than the domestic price; a clause for an open import side is needed.
2. *Duty drawback* (candidate). If a tax on an input is refunded on the content of exported goods, then: (i) relative to no policy, exporters' net input cost rises by the unrefunded share, the claim cost and the time value of the wait (CR-1, CR-8b, CR-10); (ii) where the refund rule counts more than the content actually exported (scrap allowances, standard yields), the excess is an export subsidy (SB-10); (iii) under direct identification, input flows are reshuffled between exporters and home users with no change in totals (CR-4, CR-12e identity); (iv) round trips arise unless the return crossing is checked (RS-4, SB-10). Derivation: CR-1, CR-4, CR-7a, CR-8b, CR-12e. Seen once.
3. *TX-7's input users.* TX-7 says input users "face higher costs"; whether they can pass them on depends on whether their outputs are covered by the tariff (effective protection). RS-14 decided it here, with the exemption of finished goods as the decisive fact. A cross-reference in TX-7 would help.

**(d) Vocabulary.**
1. *No instrument type for a refund of a tax conditioned on export.* K2 was classified as a binary refund under CR-1's 0.8 clarification; `deposit_refund` and `export_subsidy` each fit only part of it.
2. *No variable for exports as such.* Exports were recorded as `quantity_supplied` with a qualifier (C-19, C-35, C-36). Outcome cards would be easier to score with `quantity_exported`.
3. *Rights to claim a refund.* Designations of import entries under U1-b are tradable rights the policy creates. `right_lease_price` and `asset_value` fit badly, since the rights are used once; no sign was given (section 5).

**(e) Test of 0.8.**
- *TX-8 0.7, both directions of the currency link.* Needed interpretation. TX-8's "If" (a tariff reduces imports) was met for metal, but the same tariff raises imports of finished goods, so the policy moves imports both ways. Applying both directions gave a currency chain whose own sign is `ambiguous` (C-35), which then had to be combined as a kind (3) chain under CR-12. TX-8 could say what to do when one policy moves imports in both directions.
- *SB-10 0.8, round trips and checks on the return crossing.* Needed interpretation. Round trips were derived as written (C-23), but "combine the round-trip chain with the check under CR-12b" did not fit: the check is a burden on the round-trip option, not an opposing chain, so CR-4 with an enforcement premise decided the sign ((b) 1). SB-10's domestic-price clause failed for goods not covered at import ((c) 1).
- *Drawback as close to an export subsidy (SB-10 with CR-12e).* Worked once the subsidy element was isolated by arithmetic; the threshold (a scrap price rise above about $19 a tonne) is a premise, A-6.
- *RS-4 0.7, payments that depend on a crossing.* Worked as written: it covered the round trips and the move of fabrication to Ostrel (C-23, C-26).
- *RS-5.* Worked as written, on two lines: covered against uncovered forms (C-12), and, under U1-a only, imported against domestic content (C-13), which gave a clean per-reading sign with `no_change`.
- *CR-8 payers (0.7 general budget, both sides of every transfer).* Worked as written. The fund's recipients were recorded as a group with `at_least_one_increase` (C-42), the mirror of the 0.7 payers clause, and the three transfers each have both sides (section 2). The 0.8 clause on contingent payers did not arise.
- *OC-3 0.8, the right baseline and funding cases.* Worked as written: no enforcement is made unnecessary (C-43 at Tier A), and the fixed-budget case gave C-44.
- *CR-12 0.8, three kinds of opposing chain.* Worked as written, and all three kinds arose: (1) foreign retaliation, a Tier C note; (2) the terms-of-trade chain, derivable but resting on A-18 (p = 0.15), so the derived sign stands and the chain is recorded in section 10, while the redirection chain (A-8, p = 0.6) clears the cut-off and makes C-36 `ambiguous`; (3) the currency chain, ambiguous in its own right, which makes C-35 `ambiguous` because no premise covers the competition chain against both of its directions.
- *CR-12e 0.8, the response argument and a second change.* Needed interpretation ((b) 2); it worked for the scrap price only after arithmetic showed that the refund does not drive the response.
- *DM-1.* Worked as written between users and foreign smelters (C-38). Downstream, between home fabricators and their buyers, it was applied through CR-7b (C-39), since DM-1's "If" names a tax or a subsidy on the market itself.
- *RS-8 0.7/0.8.* Worked as written for the import rush (C-9, C-10). The Unless clause on claims acquired before a charge starts was checked and does not apply, because pre-tariff metal carries no refund; no provision improves the earlier window, so there are no opposing timing chains.
- *Candidates from 06_gaps.md, 6.2e.* "Circular trade under a payment for crossing a boundary" (WE-030) was needed (C-23); this is its second use. RS-4 0.7 and SB-10 already carry the move, so promotion would mainly add the point in (b) 1 about how a check combines. "A claim payable inside a boundary draws items from outside" (WE-027) was not needed: the drawback pays on goods leaving, not entering.
