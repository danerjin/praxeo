# WE-062 Tax on plastic packaging, with a recycled-content exemption and a small-firm threshold

Analyst: draft (Handbook 1.0, held-out test)  |  Rule catalog version: 1.0  |  Status: awaiting expert review

A stylized, fictional policy in a fictional country. Several real countries tax plastic packaging by weight and exempt packaging above a recycled-content line; this one is not modeled on any of them. It is a held-out test of catalog 1.0 on a case none of the 1.0 changes were drawn from (they came from WE-046 to WE-055). It probes TX-2 and TX-7 where a tax is collected both from domestic manufacturers and at the border, on empty packaging and on the packaging of imported goods (a tax on the form of imports, with TX-8's 0.9 clause), RS-5 on redesign around a 30% recycled-content line, RS-21 where the tax counts tonnes but is not a cap, RS-17 and CR-1's 1.0 clauses on a 10-tonne notch measured over the previous year, CR-6's 1.0 clause that small effects in a wider market are signed (recycled and virgin resin, paperboard), RS-16's 1.0 clause on substitute prices per unit of a given quality, and CR-12's 1.0 clauses on the baseline of patterns and on what the response argument needs. The unclear provision is whether the 30% line is measured on each packaging component or averaged over a firm's output. The counterfactual throughout is **Saldria without the tax**: the same firms, rules and markets, with packaging choices as they would otherwise have been. Effects on the environment, litter and health are outside the scope of version 1. The probabilities are illustrative; the evidence column says what a real analysis would cite.

## 1. Policy record

**Saldria Plastic Packaging Tax Act.** Saldria is a country of about 9.4 million people with its own currency, the taler (T), and a floating exchange rate. It produces no virgin plastic resin; all of it is imported, at world prices (about 1,150 T a tonne for the common grades). Saldria buys about 0.4% of the world's packaging resins. The figures:

| Item | Figure |
|---|---|
| Plastic packaging placed on the Saldrian market | about 610,000 tonnes a year |
| Of which made by domestic converters from resin | about 330,000 t (about 210 converters, about 19,000 employees) |
| Of which imported empty | about 120,000 t |
| Of which arriving around imported goods | about 160,000 t |
| Converters' exports of empty packaging | about 70,000 t a year, at prices set abroad |
| Packaging leaving Saldria around exported goods | about 45,000 t a year |
| Average recycled content of packaging placed on the market | about 11% |
| Packaging already at 30% recycled or more | about 85,000 t (14%), mostly PET drink bottles and some non-food rigid containers; a few brand owners use 50% or more for marketing |
| Food-contact flexible films | about 150,000 t, essentially 0% recycled; the Food Safety Authority approves recycled plastic for food contact only from approved PET processes |
| Recycled resin | 7 domestic plants produce about 48,000 t a year from collected plastic; about 12,000 t imported. Food-grade recycled PET about 1,400 T a tonne (virgin PET 1,150); non-food recycled polyolefins about 950 T (virgin 1,100) but usable only in some designs. Saldria buys about 3% of the regional recycled-resin market. |
| Collection | Municipalities collect about 140,000 t of plastic a year and sell it in bales by auction, at about 300 T a tonne; collection is near the capacity of current routes and sorting lines |
| Substitutes | Two domestic paper and board mills (about 92% capacity use); paperboard also traded regionally at regional prices; one glass container plant (88% capacity use; a new furnace takes about two years); one can maker |
| Firms | The Revenue Service estimates about 3,900 firms at or above 10 t a year (converters, importers of packaging, fillers who import, importers of packaged goods). About 21,000 firms import packaged goods; about 17,000 firms of all kinds handle under 10 t, together about 25,000 t (4%). About 520 firms handle between 7 and 10 t; about 380 between 10 and 13 t. |
| Compliance | Revenue Service estimate: 2,500 to 4,000 T a year per registered firm for weighing, records and returns |
| Packaging in the price of goods | 1% to 3% for most packaged goods; 6% to 10% for bottled water and pre-packed fresh produce |
| Static revenue projection | Treasury: 98 million T a year (taxed tonnage at enactment times the rate) |

The tax was announced in the budget statement of 2 March 2027, enacted on 28 June 2027 and takes effect on 1 January 2028. It has no expiry. The rate is fixed in talers and not indexed.

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Tax | `per_unit_tax` | Plastic packaging components (a component in which plastic is the heaviest material by weight) manufactured in or imported into Saldria, empty or around imported goods | The manufacturer (who performs the last substantial modification) or the importer of record | 200 T per tonne; quarterly returns; chargeable on manufacture or import. "The tax is chargeable whether or not the component is later exported, empty or filled." No export relief. | K2, K3 |
| K2 Recycled-content exemption | Exemption | As K1 | — | s. 4(1): "A plastic packaging component containing 30 per cent or more recycled plastic is not chargeable." s. 4(2): "The proportion of recycled plastic is to be determined over the plastic packaging components a person manufactures or imports in the quarter." Recycled content must be shown by supplier declarations or mass-balance records; components without such evidence are treated as containing none. | — |
| K3 Small-firm threshold | Exemption | Persons | — | s. 7: "A person who manufactured or imported less than 10 tonnes of plastic packaging components in the previous calendar year is not liable for the tax in the current year." The count includes exempt components. Companies under common control are counted together. A person over the line pays on all its chargeable tonnage. | — |
| K4 Administration | Enforcement | K1 to K3 | Revenue Service (plastics unit) | Registration, records, audits; penalty of 30% of tax underpaid, more for false declarations of recycled content. The Act appropriates 7 million T a year from the general budget for the plastics unit. | — |

Revenue use: general budget. What it funds is not stated; OC-1 is applied to the payers, and the recipients are not signed.

Existing rules, unchanged on both paths: the Food Safety Authority's rule on recycled plastic in food contact, customs procedures, the general sales tax, and municipal collection contracts.

A campaign by environmental groups for a ban on single-use plastic packaging has run since 2023; a ban bill failed in 2025; the converters' association opposed it.

Unclear provisions:
- **U1, how the 30% is measured.** Section 4(1) speaks of "a component containing 30 per cent or more"; section 4(2) says the proportion is "determined over the components a person manufactures or imports in the quarter". Reading U1-a (per component): 4(2) fixes only the period over which each kind of component's content is measured by mass balance; each kind of component must itself reach 30% to be exempt. Reading U1-b (averaged): the proportion is the average over all the person's components in the quarter; if it is 30% or more, every component the person made or imported that quarter is exempt, and if not, none is. The Revenue Service has consulted and has not decided; no court has ruled. Readings get no probability; where a sign depends on one, each reading's sign is reported.

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | Rule families |
|---|---|---|---|
| K1, on domestic manufacture | Binary: a payment per tonne to the state. CR-1, operation 3 on the option of making a taxed component, dated 1 January 2028; before then it acts through expectations (CR-10a), while asset values move from the announcement (CR-7c; CR-1, 0.7, dated operations). | Yes for components that stay taxed (A-1, A-3) | TX-1, TX-2, TX-3, TX-5, TX-9, DM-1, RS-1, RS-14, RS-16, RS-3, RS-6, RS-8, CR-4, CR-6, CR-7 |
| K1, on imports (empty and around goods) | Binary, at the same rate as on domestic manufacture. Not a tariff in effect: the same tonne pays the same tax whether made at home or abroad, so it grants no privilege to domestic producers (see below). | Yes (A-1) | TX-2; TX-7 considered and not applied; TX-8 (0.9: form of imports) |
| K2 | An exemption with a notch (CR-1, 1.0): below the line the tax falls on the whole weight; at the line it falls to nothing. Under U1-a the notch is per component (a component at 29% pays on all its weight); under U1-b it is per person and quarter (a firm at a 29% average pays on all its tonnage). | Binds on components whose recycled content would be below 30% (A-4) | RS-5, CR-1 (1.0), CR-4, CR-9 |
| K3 | A notch on the size of the firm (CR-1, 1.0; RS-17, 1.0): under 10 t, no operation; at 10 t, operation 3 on all chargeable tonnage, plus registration and records, a cost fixed per firm (CR-4, 0.8). Measured over the previous calendar year, so 2027 tonnage decides 2028 liability, and the response comes from the announcement in March 2027 (RS-17). | Binds for firms near the line (A-14) | RS-17 (0.9, 1.0), CR-1 (1.0), CR-4, RS-5, RS-8 |
| K4 | Binary: funded by a fixed appropriation from the general budget, which also receives the tax (CR-8, 1.0) | Yes | OC-3, TX-5, CR-8 |

**Why TX-7 is not applied to the import leg.** TX-7's If clause is "a tariff on an imported good". Taken alone, the tax collected at the border on imported packaging, and on the packaging of imported goods, meets it, and TX-7 would then conclude that domestic converters and fillers, as sellers of substitutes, gain. That conclusion compares the policy with another policy (imports taxed, domestic output not), not with Saldria without the tax (CR-12, 1.0, the baseline of patterns). Against no tax, domestic output pays the same 200 T a tonne. Collected at home and at the border, K1 is one tax on packaging placed on the Saldrian market and on packaging manufactured there for export. TX-2 is applied to it as a whole. The places where imports and domestic output are treated differently are derived separately: the small-firm threshold, which lets small users import packaging free of tax that they would pay on domestic packaging (C-37, C-55); the evidence rule in K2, which taxes imported packaging whose recycled content its foreign supplier cannot document (C-53); and the absence of export relief (C-38).

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `converters` (`sellers.current`) | About 210 domestic makers of plastic packaging | Pay 200 T a tonne on chargeable output, including exports; may raise recycled content, lighten designs, or lose sales to substitutes |
| `converters.owners` (`factor_owners.specific`) | Owners of converting plants | Plant specific to plastic converting |
| `converter_workers` | About 19,000 employees | Their employers' output may fall |
| `packaging_users` (`buyers.current`) | Fillers, brand owners and retailers who buy plastic packaging to pack goods in Saldria | Pay more for taxed packaging; may switch to recycled content, lighter designs or other materials |
| `importers.packaging`, `importers.packaged_goods` | Importers of record at or above 10 t | Pay the tax at import; must document recycled content of foreign packaging |
| `small_importers` | Firms handling under 10 t a year (about 17,000) | Not liable; their packaging and their imported goods are untaxed |
| `firms.near_threshold` | Firms handling about 7 to 13 t (about 900) | 2027 tonnage decides whether they pay on all their tonnage in 2028 |
| `buyers.packaged_goods` | Households and businesses buying packaged goods | Prices of goods with a high packaging share may rise |
| `exporters` | Converters exporting empty packaging; fillers exporting packaged goods | Taxed with no export relief, against foreign rivals who are not |
| `recyclers`, `recyclers.owners`, `recycler_workers` (`input_suppliers`) | Seven recycling plants and their staff | More demand for recycled resin |
| `municipalities` | Sellers of collected plastic bales | Bales sell for more |
| `sellers.foreign` | Foreign resin makers, foreign converters, foreign sellers of packaged goods, regional recycled-resin sellers | Less virgin resin and empty packaging sold to Saldria; more recycled resin |
| `buyers.foreign` | Regional buyers of recycled resin | Compete with Saldrian demand |
| `sellers.substitutes` (and their owners and workers) | Board mills, the glass plant, the can maker; regional board sellers | More demand |
| `buyers.substitutes` | Existing users of board, glass and cans | Compete with switching plastic users |
| `export_industries` | Other exporters | Linked to imports through the currency (TX-8) |
| `intermediaries` | Certifiers of recycled content, compliance consultants | New work |
| `officials.enforcement`, state budget | Revenue Service plastics unit; the general budget | New work; receipts and an appropriation |
| Lobbies: converters' association, recyclers, environmental groups | Organized interests | New questions to lobby on (U1, implementing rules) |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | state budget | `tax_revenue` (plastic packaging tax) | increase | short | TX-1 | none |
| C-2 | `packaging_users` | `price_paid` (taxed plastic packaging, tax included, per tonne of a given specification) | increase | short | TX-2, DM-1, CR-7b | A-2, A-3 |
| C-3 | `packaging_users`, `converters`, `sellers.foreign` | `quantity_traded` (taxed plastic packaging) | decrease | short–medium | TX-2, OC-4, CR-4c, CR-5a | A-3 |
| C-4 | `packaging_users`, `converters` | `product_attribute` (average recycled content of plastic packaging placed on the market) | increase | short–medium | RS-5, CR-1 (1.0: notch), CR-4, CR-12e | A-4, A-10 |
| C-52 | `packaging_users` | `tax_share_borne` (against domestic and foreign sellers of packaging) | increase | short–medium | DM-1, CR-7b | A-2 |

**C-2, C-52: incidence.** TX-2 gives that buyers' price rises or sellers' net price falls, or both. DM-1 decides the split here (A-2): about a fifth of the packaging Saldria uses is imported empty, foreign converters have many other markets, and Saldria is a small buyer, so the price of each kind of packaging is set near the import price plus the tax, and packaging users bear more of the tax than sellers do. Because buyers bear more, their price rises (C-2). Domestic converters' net price on home sales falls or is unchanged; that is not signed. The price is per tonne of a given specification (RS-16, 1.0): a lighter or recycled design is a different specification, and a shift in the mix is not a price change. DM-1's horizon note points the same way over time: converters' capital is the redeployable side only slowly, so the burden shifts toward buyers as it does.

**C-3.** At the higher price, users buy less taxed packaging: they lighten designs (C-8), raise recycled content to reach the exemption (C-5), or switch to other materials (C-9) (CR-4c, A-3). The exchanges no longer made are a loss to both sides (OC-4, CR-5a), converters and foreign sellers on one side, users on the other.

**C-4.** The visible aim: components whose content can be raised to 30% at a cost below the tax are raised (CR-4, x: below 30% and taxed, y: at 30% and exempt; A-4). Recycled PET for food contact costs about 250 T a tonne more than virgin; at 30% that adds about 75 T to a tonne of bottles, against 200 T of tax. Some components already above 30% may cut their content toward the line when recycled resin becomes dearer (C-6, under U1-a), but that is a response to the price rise which the added demand itself causes, and it cannot reverse the rise in total recycled resin used (CR-12e, response argument; section 7). With total recycled tonnes up (C-26) and total taxed plastic down (C-3), the average rises.

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-5 | `converters`, `packaging_users` | `reclassification` (components redesigned to reach 30% recycled; composites redesigned so that plastic is not the heaviest material) | increase | short–medium | RS-5, CR-4, CR-1 (1.0) | A-4 |
| C-6 | `packaging_users` (components above 30% on the counterfactual path) | `product_attribute` (recycled content of those components) | U1-a: decrease; U1-b: ambiguous | medium | CR-4c, CR-9, CR-12b | A-8, A-9, A-10 |
| C-7 | `converters`, `packaging_users`, `importers.packaging` | `reclassification` (output combined across product lines or affiliates to average recycled content) | U1-a: no_change; U1-b: increase | short–medium | RS-5, CR-1, CR-4 | A-9 |
| C-8 | `converters`, `packaging_users` | `unit_size` (plastic weight per taxed component) | decrease | short–medium | CR-4c, CR-1 | A-5 |
| C-9 | `packaging_users` | `quantity_substitute` (paper and board, glass and metal packaging) | increase | short–medium | RS-1, RS-16 | A-6 |
| C-12 | `firms.near_threshold` | `number_of_sellers` (firms handling just under 10 t a year) | increase | short–medium (from March 2027) | RS-17 (1.0: notch), CR-1 (1.0), CR-4, CR-10a | A-14 |
| C-13 | `firms.near_threshold` | `number_of_sellers` (firms handling 10 t to about 13 t a year) | decrease | short–medium | RS-17, CR-4 | A-14 |
| C-15 | liable firms well above 10 t | `quantity_traded` (taxed packaging manufactured or imported, October to December 2027) | increase | short | RS-8, CR-10a | A-16 |
| C-16 | liable firms well above 10 t | `quantity_traded` (packaging manufactured or imported, January to March 2028) | decrease | short | RS-8, CR-10a | A-16 |
| C-17 | liable firms well above 10 t | `inventory_held` (packaging stocks on 31 December 2027) | increase | short | RS-8, CR-10a, CR-7a | A-16 |
| C-18 | `firms.near_threshold` | `quantity_traded` (packaging manufactured or imported, March to December 2027) | ambiguous | short | RS-8 (0.9), RS-17, CR-12b | A-14, A-16 |
| C-19 | `converters`, `importers.packaging`, `importers.packaged_goods` | `legal_breach` (recycled content or weight misdeclared) | increase | short–medium | RS-3, CR-4 | A-17 |
| C-20 | liable firms | `compliance_cost` (registration, weighing, recycled-content records, returns) | increase | short | TX-5, CR-4 (0.8), CR-8c | none |
| C-21 | converters' association, `packaging_users` with mixed product lines, `recyclers` | `lobbying_effort` (on U1 and the implementing rules) | increase | short–medium | RS-7 (1.0), CR-4 (1.0), CR-12 (0.9) | A-18 |
| C-22 | `converters` | `investment_target` (equipment to process recycled resin) | increase | short–medium | CR-4, CR-10a | A-4, A-27 |
| C-23 | `converters` | `investment_target` (plastic converting capacity) | decrease | medium | TX-3, RS-6 | A-3, A-19 |
| C-24 | `converters` | `investment_target` (total) | ambiguous | medium | CR-12 (0.8: two items), CR-12b | A-3, A-27 |
| C-25 | `recyclers` | `investment_target` (recycling and sorting capacity) | increase | medium | CR-4, CR-7a, CR-10a | A-10, A-19 |
| C-55 | `small_importers` (small packaging users) | `quantity_traded` (empty packaging imported directly by users under 10 t) | increase | medium | RS-5, CR-4 | A-31 |

**Redesign around the 30% line (C-5 to C-7).** RS-5 applies as written: the line divides covered from uncovered components, and components are reshaped to fall on the exempt side where that costs less than the tax (A-4). The material definition is a second line: a component is plastic packaging only if plastic is its heaviest material, so laminates and coated board can be redesigned to keep plastic just under half their weight (C-5). Both are notches (CR-1, 1.0): a component at 29% pays tax on its whole weight, at 30% none, so components bunch just above the line.

The two readings differ on what happens beyond the line and across a firm's products.
- *Above the line (C-6).* On the counterfactual path some components carry more than 30% recycled content, some of them 50% or more for marketing. Under U1-a, content above 30% earns nothing from the tax, while recycled resin becomes dearer (C-27): where that content was chosen at the margin on cost (A-8), it is cut toward 30% (CR-4c), a decrease. Under U1-b, content above 30% on easy components (bottles, non-food tubs) lets a firm's average reach 30% while its films stay virgin, and so exempts its whole output (A-9). That chain raises content on easy components (+) against the dearer resin (−); no premise ranks them: `ambiguous`.
- *Across products (C-7).* Under U1-b the line is drawn over a person's whole quarterly output, so firm boundaries matter: a film converter that merges with, or registers its imports through, a bottle maker can exempt both (CR-4, x: separate, y: combined; RS-5 applied to organizations). Common control is counted together for K3, which helps here. Under U1-a, the exemption is decided component by component, and combining output changes nothing: `no_change` on this chain.
- *Components that cannot reach 30%.* Food-contact films cannot use recycled plastic (Food Safety Authority, on both paths). Under U1-a they pay tax on every tonne, so their users lighten them (C-8) or move to other materials (C-9). Under U1-b they escape the tax inside firms whose average reaches 30%, and pay it elsewhere. Under either reading, single-product film converters lose value (C-41).

**RS-21 and the per-tonne count (C-8).** RS-21's If clause is a cap, quota or right counted in physical units. K1 is a tax counted in tonnes, not a cap, so RS-21's preconditions are not met as written, and C-8 is derived from CR-4c with the unit of the charge: the tax per component rises with its weight, so where a design can be lightened at a cost below the tax saved (A-5), it is. The move is RS-21's (the value carried per counted unit rises), but its direction for `unit_size` is the reverse of RS-21's examples: with a count in tonnes and a free choice of items per tonne, items get lighter, where under a slot cap aircraft get larger. Gaps found (c) 2 records this. For exempt components the weight is untaxed and this chain does not run.

**Substitutes (C-9).** Paper and board, glass and metal serve some of the same ends (A-6); users move to them where the tax exceeds the cost of switching (RS-1, CR-4). Their prices are section 6's question (RS-16).

**The 10-tonne notch (C-12, C-13, C-18).** A firm with 9.9 t in 2027 pays nothing in 2028; one with 10.1 t pays 200 T on every chargeable tonne, at least 2,000 T, plus registration and records (2,500 to 4,000 T a year). Crossing costs about 5,000 T a year or more (CR-1, 1.0: the jump is a cost of crossing). RS-17 says that firms near the line stay below it. Its main clause is phrased "just below the threshold increases relative to just above", a comparison between two bands. Against the counterfactual (CR-12, 1.0), each band is signed separately: firms that would have handled 10 to 13 t keep their tonnage under 10 t (A-14), so the count just below rises (C-12) and the count just above falls (C-13). Because the line is measured over the previous year, the response begins in 2027, from the announcement in March (RS-17; CR-10a). RS-17's other move, splitting activity across separately counted units, is limited by the common-control rule: only moving the importer of record to unrelated parties (customers, foreign sellers) remains, and A-15 (p = 0.4) is below the cut-off, so it is not reported. RS-17's 1.0 clause on eligibility does not apply: no program is lost at the line.

For firms near the line, two timing chains meet in 2027 (C-18). Bringing purchases forward before the tax starts (RS-8, A-16) raises 2027 tonnage (+), but that would push some of them over the line for 2028; those staying under cut 2027 tonnage instead (−). The class contains both, so the sign is `ambiguous` (RS-8, 0.9: more timing chains; CR-12b).

**Small users importing directly (C-55).** K3 exempts a small firm on what it imports, but a small firm that buys from a domestic converter pays the tax in the price (C-2), since the converter is liable. Small users who can import their own packaging at a cost below the tax (A-31: 5 t a year saves 1,000 T, against minimum order sizes and freight) do so (RS-5: the actor reshapes who imports; CR-4). This is a burden on domestic converters' sales to small users that their foreign rivals selling directly to those users do not bear: the reverse of a tariff, for one class of buyers.

**Timing for liable firms (C-15 to C-17).** Firms well above the line, which will pay in 2028 whatever they do, bring purchases and production forward into late 2027 and carry larger stocks into January (RS-8, CR-7a across time; A-16). Each window is signed against the counterfactual (02_ontology, 2.5).

**Evasion (C-19).** Recycled content is hard to verify chemically and rests on declarations and mass-balance records. Where misdeclaring costs less than the tax, given the audit rate and penalties, some firms misdeclare (RS-3, A-17). This is breach within the legal market, `legal_breach`, not `informal_activity`; it rises from none, since there is no tax to evade on the counterfactual path.

**Compliance (C-20).** TX-5. Registration and records are a cost fixed per firm (CR-4, 0.8): they bear on whether, and at what size, a firm handles packaging itself, which is why they add to the notch, not on the price per tonne.

**Lobbying (C-21).** CR-4's 1.0 clause and RS-7's 1.0 clause apply: lobbying is signed against the counterfactual contest. U1 and the implementing rules (evidence of recycled content, definitions of "substantial modification") are questions that exist only under the Act, so lobbying on them rises from none (CR-12, 0.9; A-18). Multi-product firms press for U1-b, recyclers for the reading they expect to raise demand for their resin. Lobbying over a ban on single-use plastic, which was contested on the counterfactual path, is not signed: whether the tax makes the ban campaign and its opponents spend more or less needs a premise the case lacks (A-29, p = 0.45, below the cut-off).

**Investment (C-22 to C-25).** Two items of one variable move in opposite directions (CR-12, 0.8): converters invest in drying, decontamination and blending lines to use recycled resin (C-22; A-27), and invest less in converting capacity as taxed output falls (C-23; TX-3, RS-6). The total is `ambiguous` (C-24). Recyclers expand (C-25), if they expect the tax and its exemption to last (A-19).

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-26 | `recyclers`, `packaging_users` | `quantity_traded` (recycled resin delivered in Saldria, from all sources) | increase | short–medium | CR-9, LW-10, CR-6 | recycled resin `input_to` packaging | A-4, A-10 |
| C-27 | `recyclers` | `net_price_received` (recycled resin sold in Saldria) | increase | short | CR-9, CR-6 | as C-26 | A-4, A-10 |
| C-28 | `recyclers` | `net_price_received` (recycled resin sold in Saldria) | increase | medium | CR-6, CR-12e (response argument; 0.9, 1.0) | as C-26 | A-4, A-10 |
| C-29 | `packaging_users` already at or above 30% on the counterfactual path | `price_paid` (recycled resin) | increase | short–medium | CR-9, CR-6 | as C-26 | A-4, A-10 |
| C-30 | `buyers.foreign` (regional) | `price_paid` (recycled resin, regional market) | increase | short–medium | CR-6 (1.0: small effects), CR-9 | Saldria and the region: `across_border` | A-4 |
| C-31 | `sellers.foreign` (virgin resin) | `net_price_received` (virgin resin, world market) | decrease | short–medium | CR-6 (1.0: small effects), CR-9, LW-10 | resin `input_to` packaging | A-3 |
| C-32 | `converters`, `sellers.foreign` | `quantity_traded` (virgin resin imported into Saldria) | decrease | short–medium | CR-9, LW-10 | resin `input_to` packaging | A-3 |
| C-33 | `municipalities` | `net_price_received` (collected plastic bales) | increase | short–medium | CR-9, LW-10, CR-6 | bales `input_to` recycled resin | A-4, A-26 |
| C-34 | `municipalities` | `quantity_supplied` (plastic collected and sold) | increase | medium | CR-4, CR-9 | as C-33 | A-26 |
| C-10 | `packaging_users`, `buyers.substitutes` | `price_substitute` (paperboard, per tonne of a given grade; regional market) | increase | short | RS-16 (1.0), CR-6 (1.0: small effects) | plastic and board packaging: `substitute`, partial | A-6, A-7 |
| C-11 | `packaging_users`, `buyers.substitutes` | `price_substitute` (glass containers, per unit of a given size and type) | increase | short | RS-16 (1.0), CR-6 | plastic and glass containers: `substitute`, partial | A-6, A-7 |
| C-35 | `buyers.packaged_goods` | `price_paid` (goods with a high packaging share: bottled water, pre-packed produce) | increase | short–medium | RS-14, CR-9 | packaging `input_to` packaged goods | A-2, A-11 |
| C-36 | `buyers.packaged_goods` | `quantity_demanded` (those goods) | decrease | short–medium | RS-14, CR-4c | as C-35 | A-2, A-11 |
| C-37 | `small_importers` | `quantity_traded` (packaged goods imported by firms under 10 t) | increase | medium | CR-9, CR-4 | small importers' goods and liable firms' goods: `substitute`, partial | A-22 |
| C-53 | `importers.packaged_goods`, `sellers.foreign` | `quantity_traded` (packaged goods imported into Saldria) | ambiguous | medium | TX-2, CR-4, CR-9, CR-12b | imported and domestic packaged goods: `substitute`, close | A-11, A-22, A-30 |
| C-54 | `importers.packaging`, `sellers.foreign` | `quantity_traded` (empty plastic packaging imported) | decrease | short–medium | TX-2, CR-4c, CR-12e | imported and domestic packaging: `substitute`, close | A-3, A-30, A-32 |
| C-38 | `exporters` | `quantity_supplied` (exports of empty packaging and of packaged goods) | decrease | medium | RS-14, RS-6, CR-7b | — | A-12 |
| C-39 | `exporters` | `capital_stock_target` (domestic filling and converting lines serving export markets) | decrease | long | RS-4, RS-6, TS-1 | — | A-12, A-13 |
| C-40 | `export_industries` | `quantity_supplied` (other exports) | ambiguous | medium | TX-8 (0.9: form of imports), CR-9 (currency), CR-12 (0.8: kind 3) | imports and exports: `currency` | A-21 |
| C-41 | `converters.owners` | `asset_value` (converting plants and firms) | decrease | short (from March 2027) | CR-7c, CR-10c, SB-4 | — | A-3, A-19, A-20 |
| C-42 | `recyclers.owners` | `asset_value` (recycling plants) | increase | short (from March 2027) | CR-7c, CR-10c, SB-4 | — | A-10, A-19 |
| C-43 | owners of `sellers.substitutes` (board mills, glass plant, can maker) | `asset_value` | increase | short (from March 2027) | CR-7c, SB-4 | — | A-6, A-7, A-19 |
| C-44 | `converter_workers` | `employment`, `hours_worked` | at_least_one_decrease | medium | TX-3, RS-6, OC-5 | — | A-3, A-25 |
| C-45 | `recycler_workers`, workers of `sellers.substitutes` | `employment`, `hours_worked` | at_least_one_increase | medium | OC-5, CR-9, LW-10 | — | A-6, A-23 |
| C-46 | `intermediaries` | `quantity_traded` (recycled-content certification and compliance services) | increase | short | CR-9, CR-8c | certification `input_to` the K2 exemption | A-4 |

**Recycled resin (C-26 to C-30).** More components need recycled resin (C-5), so at the old price users wish to buy more than recyclers and importers wish to sell (CR-9 with LW-10; CR-6). Domestic supply is limited by collection, which is near the capacity of current routes and sorting lines; more resin comes from added collection and from the region only at a higher cost (A-10). So in the short run the quantity delivered rises and the price rises (C-26, C-27; CR-6, 0.9: the split between price and quantity rests on A-10). In the medium run recyclers expand (C-25) and imports grow. CR-12e's response argument says these responses cannot push the price back below its old level, since expansion stops once yields are equal. Under CR-12's 1.0 clause it gives `increase` only with three things stated. *The total it bounds:* recycled resin delivered in Saldria from all sources, domestic and imported. *A premise that cost per unit does not fall as the activity expands:* collecting more means reaching more dispersed sources and accepting dirtier bales, and the regional price itself rises (C-30); A-10 states this rising-cost premise. *A partial response:* supply cannot fully expand at the old cost within the medium run, also A-10. Imports are a second response to the same price rise; once the total is named over both sources they are inside the argument, not a separate chain (Gaps found, (b) 1). No stock built in advance holds the price down: recycled resin is not stockpiled for the tax. So C-28 is an increase. The long run is not signed: plants have fixed costs, and with enough expansion the cost per tonne could fall.

Users who used recycled resin anyway (C-29) pay more for it and gain nothing from the exemption, which they would have met without the tax. They are worse off by their own ranking (CR-3a), and, since they keep buying, have less to spend on other things (CR-3, note). Municipalities sell their bales for more (C-33) and in time collect more (C-34; A-26).

**Small effects in wider markets (C-30, C-31, C-10).** CR-6's 1.0 clause: a chain that moves a price in a wider market is signed, with its size in the evidence column. Saldria buys about 3% of the regional recycled-resin market: the added demand raises the regional price (C-30), small. It buys about 0.4% of the world's packaging resins: the fall in its virgin resin purchases (C-32) lowers the world price (C-31), very small. Paperboard is traded regionally: the move to board raises its regional price (C-10), small, and more than that at the domestic mills while they run near capacity (A-7).

**Substitute prices per unit of quality (C-10, C-11).** RS-16 as written, with its 1.0 clause. The price is per tonne of a given grade of board and per container of a given size and type. Users moving from plastic tend to buy coated, barrier-grade board, which costs more per tonne than plain grades. The average price of board bought in Saldria would rise from that change in mix alone, and the mix change is not counted. The policy attaches no cost to the substitutes, so RS-16's clause on costs on the substitute does not apply; and it adds no supply to their markets, so the Unless clause (RS-13) does not either. Glass containers are costly to transport, so the domestic plant's price rises while it runs at 88% capacity and a new furnace is two years away (C-11, short run only). Existing users of board and glass (`buyers.substitutes`) pay the higher prices too.

**Packaged goods (C-35, C-36).** For goods in which packaging is 6% to 10% of the price, RS-14 applies: the input's cost rises, and the sellers' competitors face the same increase, because imported goods pay the tax on their packaging too, apart from the small importers' 4% share. So the price rise dominates (C-35; A-11), and at the higher price buyers buy less (C-36; CR-4c). For goods in which packaging is 1% to 3% of the price, the sign is the same but its premise (that packaging is a "material part" of cost, A-11) is weaker. Those goods are not reported separately.

**Imports by form (C-37, C-53, C-54) and the currency (C-40).** The tax changes the form of Saldria's imports as well as their quantity:
- virgin resin imports fall (C-32);
- recycled resin, board and glass imports rise (C-26, C-9);
- empty packaging imports fall. They are taxed like domestic output, and imports whose recycled content the foreign supplier cannot document are taxed as 0% (A-30). Small users who import directly push the other way (C-55); they handle at most 25,000 t in all, and A-32 states that their shift is smaller than the fall in liable firms' imports (CR-12e, an empirical premise). So C-54 is a decrease;
- imported packaged goods: three chains with opposite signs. The tax on all packaged goods lowers purchases (C-36, −). The evidence rule falls on foreign suppliers who cannot document their content (A-30, −). Goods brought in by small importers are untaxed and gain against taxed rivals (C-37, +; A-22). No premise ranks them: `ambiguous` (C-53).

So imports of some goods fall and of others rise. TX-8's 0.9 clause applies: where a policy reduces imports of one good and raises imports of others made from it or used in its place, the currency chain is itself `ambiguous` (kind 3) unless a premise says which dominates. Exports of packaging and packaged goods also fall (C-38). By the mirror case, that gives residents fewer foreign means for imports, and, by CR-9's 0.7 clause, leaves foreign buyers' means to other exporters, a (+) chain for them. The effect on other export industries is `ambiguous` (C-40; A-21 is the premise that trade is not offset by capital flows within the medium run). TX-8 has no 1.0 clause; the 0.9 one worked as written.

**Exporters (C-38, C-39).** The Act taxes packaging that is exported, empty or filled. Exporters sell at prices set abroad (A-12), against foreign rivals who pay no Saldrian tax, so they cannot pass it on. RS-14's "competitors exempt" case applies: the quantity effect dominates (C-38; RS-6, CR-7b). Over the long run, some export filling lines are replaced abroad rather than at home (C-39; RS-4, TS-1; A-13). That is a move across the boundary which the tax favors. TS-6 says it is hard to reverse.

**Asset values (C-41 to C-43).** Expected from the March 2027 announcement (CR-7c, CR-10c). Converting plants are specific (A-20), and their expected yield falls with taxed output: decrease (C-41). Single-product film converters lose most, under either reading: under U1-a they pay on every tonne, and under U1-b they compete with multi-product rivals whose films are exempt. Recycling plants (C-42) and board, glass and can makers (C-43) gain. Each assumes investors expect the tax to last (A-19). For firms near the 10-tonne line, see section 7 (C-14).

**Labor (C-44, C-45).** Converters that make less use less labor, in staff or hours (C-44; TX-3, RS-6, OC-5). Recyclers and substitute makers expand existing activities, so the group form applies to them too, as at_least_one_increase (C-45; OC-5).

**Certification (C-46).** K2's evidence rule creates demand for certificates and mass-balance audits (CR-9). Some certification exists on the counterfactual path for marketing claims, so this is an increase on an existing activity, not one from none.

**Stopping points.** Suppliers of converters' equipment, the workers of export industries (depth 4 through the currency), and municipal taxpayers who gain from bale receipts are not followed further.

**Checks.** RS-9: no shopping trips are moved. RS-10: no trade goes underground; misdeclaration (C-19) stays in the legal market. RS-11: no benefit is tied to a place. RS-12: no complement in use is identified. RS-13: the policy adds no supply to a linked market.

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `packaging_users`, `converters`, `product_attribute` (average recycled content), short–medium | Components raised to 30% (A-4). | Under U1-a, content above 30% cut back as recycled resin gets dearer (C-6). | CR-12e response argument: the cut-back responds to the price rise the added demand causes, and cannot reverse the rise in total recycled resin used (C-26), while total taxed plastic falls (C-3). Arithmetic on the ratio. | **increase** (C-4), under both readings. |
| Components above 30% on the counterfactual path, recycled content, medium | U1-b: surplus content averages a firm's films into the exemption (A-9). | Dearer recycled resin (A-8, A-10). | U1-a: only the (−) chain. U1-b: none. | **U1-a: decrease; U1-b: ambiguous** (C-6). |
| `recyclers`, `net_price_received`, medium | Added demand (C-26). | Recyclers' expansion (C-25) and imports. | CR-12e response argument, on recycled resin delivered in Saldria from all sources, with the rising-cost and partial-response premise (A-10). | **increase** (C-28). |
| `converters`, `investment_target`, medium | Recycled-resin processing equipment (C-22). | Converting capacity (C-23). | None (two items, CR-12 0.8). | **ambiguous** (C-24). |
| `firms.near_threshold`, `quantity_traded`, March to December 2027 | Purchases brought forward before the tax (A-16). | Tonnage held under 10 t to avoid 2028 liability (A-14). | None (RS-8, 0.9). | **ambiguous** (C-18). |
| `firms.near_threshold`, `asset_value`, short | Rivals above the line bear the tax and compliance (RS-17, 0.9). | Growing past the line costs more (the notch). | None. | **ambiguous** (C-14). |
| `importers.packaging`, `quantity_traded` (empty packaging), short–medium | Small users import directly (C-55). | General fall in taxed packaging (A-3); undocumented content taxed in full (A-30). | A-32, an empirical premise (CR-12e). | **decrease** (C-54). |
| Imported packaged goods, `quantity_traded`, medium | Small importers' untaxed goods (A-22). | Tax on packaging lowers purchases (C-36); undocumented content (A-30). | None. | **ambiguous** (C-53). |
| `export_industries`, `quantity_supplied`, medium | Fewer Saldrian exports leave foreign means to other exporters; imports of board, recycled resin and some packaged goods rise. | Imports of resin and empty packaging fall. | None (TX-8, 0.9; kind 3). | **ambiguous** (C-40). |
| `packaging_users`, `price_paid` (taxed packaging), short | The tax (TX-2). | None derived. Converters' net price may absorb part of it. | DM-1 (A-2): buyers bear more, so their price rises. | **increase** (C-2). |
| State budget, `tax_revenue` net of the plastics unit's appropriation, short | Tax receipts (C-1). | The 7 million T appropriation (C-48). | Arithmetic on the case's figures (CR-8, 1.0; CR-12e): even if the base fell by half, receipts of about 45 million T exceed 7 million T. | **increase** (C-49). |

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-14 | `firms.near_threshold` | `asset_value` | ambiguous | short (from March 2027) | RS-17 (0.9), CR-7c, CR-12b | A-14, A-19, A-22 |

**Different variables and classes are not netted (CR-12c).** Converters' workers (C-44) and recyclers' and substitute makers' workers (C-45) are separate classes; the method does not say whether employment across packaging as a whole rises or falls. The price of taxed packaging per tonne (C-2) and the weight per component (C-8) are separate variables: the cost per item of a lightened component can fall even though the price per tonne rises.

**Packaging users as a whole.** Those who keep using taxed plastic pay more (C-2, C-47). Those who switch bear the cost of switching instead (C-51) and are worse off by their own ranking (CR-3a), but no money flows from them to the state. No sign is given for users' total outlay on packaging.

**The tax on imported packaging (TX-7 re-signed).** As section 2 says, no chain gives domestic converters or fillers a gain from the import leg against the no-tax path. The one place where domestic sellers gain against foreign ones is the evidence rule, which taxes undocumented foreign content (A-30); the one place where they lose is the small-firm threshold (C-55, C-37). Both are recorded where they act (C-53, C-54).

## 8. Time structure

- **Announcement to enactment (March to June 2027).** Values move: converters down, recyclers and substitute makers up (C-41 to C-43). Firms near the 10-tonne line start managing their 2027 tonnage, since it decides 2028 liability (C-12, C-13, C-18). Lobbying on U1 begins (C-21).
- **Second half of 2027.** Converters order recycled-resin equipment (C-22) and redesign components (C-5); recycled resin contracts for 2028 are written at higher prices (C-27). In the last quarter, liable firms bring purchases forward and build stocks (C-15, C-17).
- **2028.** Liable firms draw down stocks in the first quarter (C-16). Recycled resin, board and glass prices are highest while capacity is fixed (C-10, C-11, C-27). Exporters lose sales (C-38).
- **Medium run.** Recyclers expand and collection grows (C-25, C-34), and the recycled resin price stays above its counterfactual level by A-10 (C-28). Converters' capacity shrinks (C-23). Under U1-b, firms reorganize to average (C-7). The 30% line and the definitions settle into product design; habits of buying change gradually (TS-8).
- **Long run.** Export lines are replaced abroad (C-39), which is hard to reverse (TS-6). The rate is fixed in talers and not indexed (TS-3): as prices rise, the real tax per tonne falls, the gain from meeting the 30% line shrinks, and the notch at 10 t matters less. Whether the recycled resin price stays above its counterfactual level in the long run is not signed (section 6).

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-47 | `packaging_users` and importers who keep using taxed plastic | `resources_available_other_uses` | decrease | The tax they pay in the price or directly, which they would have spent, invested or saved (they keep paying: CR-3, note). | TX-1, OC-1, CR-3 |
| C-48 | `officials.enforcement` | `enforcement_cost` | increase | Staff time on registrations, returns and audits of recycled content, funded by a 7 million T appropriation from the general budget (A-24). | OC-3, CR-8c |
| C-49 | state budget | `tax_revenue` (net of the plastics unit's appropriation) | increase | Nothing given up by the state: the tax is payers' outlay (C-47). | CR-8 (1.0), CR-12e |
| C-50 | state budget | `tax_revenue_vs_static_projection` | decrease | — | TX-9 |
| C-51 | `packaging_users`, `converters` (who redesign, switch or lighten) | `compliance_cost` (redesign, testing and qualification of new materials and designs) | increase | Engineering and testing time used up to avoid the tax (CR-8c). | CR-8c, CR-3a, OC-2 |

The tax and the appropriation pass through one budget (CR-8, 1.0): the receipts (C-1) and the outlay (C-48) are two items, and the net (C-49) is signed by arithmetic. Who gains from the net, through more spending or lower taxes or borrowing, the record does not say, so no class of taxpayers or recipients is signed. Prevented exchanges of packaging (OC-4) are C-3, with both sides named there. Resources used in lobbying (C-21), misdeclaration and audits (C-19), and certification (C-46) are used up (CR-8c). Converters' plant and labor withdrawn from converting (C-23, C-44) go to other uses (CR-7), which are not named without a premise.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | The tax is collected from most liable firms. | enforcement | 0.85 | Registration via customs and the converter register; audit powers. | Every consequence weakens; C-19 grows. |
| A-2 | Imported empty packaging is at the margin of supply for most kinds of packaging, and foreign converters, with many other markets, absorb little of the tax, so packaging users bear more of it than sellers do. | substitutability | 0.75 | About 120,000 t of 610,000 t imported empty; Saldria's small share of regional demand. | C-2 is not signed by DM-1 (TX-2's group only); C-52 not reported; C-35 weakens. |
| A-3 | Some packaging users can reduce their use of taxed plastic (lighter designs, recycled content, other materials) at a cost below 200 T a tonne. | substitutability | 0.85 | Design studies; the share of packaging already at 30%; board and glass alternatives. | C-3, C-9, C-23, C-32, C-44 and C-50 not reported. |
| A-4 | For some components, raising recycled content to 30% costs less than the tax. | alternative_uses | 0.85 | About 75 T a tonne extra for food-grade PET at 30%, against 200 T; non-food recycled polyolefins cheaper than virgin. | C-4, C-5, C-22, C-26 to C-29, C-33 and C-46 not reported. |
| A-5 | Some components can be made lighter at a cost below the tax saved. | alternative_uses | 0.75 | Lightweighting already under way for cost reasons. | C-8 not reported. |
| A-6 | Paper and board, glass and metal packaging serve some of the same ends as plastic for some users. | substitutability | 0.8 | Board trays, glass jars and cans already compete with plastic in many uses. | C-9 to C-11, C-43, C-45 not reported. |
| A-7 | Board and glass container supply cannot expand at an unchanged cost within the first year. | durability | 0.7 | Board mills at 92% and the glass plant at 88% of capacity; a new furnace takes two years. Board's regional market makes its price effect small. | C-10, C-11 become quantity effects only. |
| A-8 | Some components above 30% recycled on the counterfactual path carry that content at a margin chosen on cost, so that a dearer recycled resin leads their makers to cut it toward 30%. | other | 0.6 | Brand owners' published content targets; contracts priced on resin cost. | C-6 under U1-a not reported; under U1-b it becomes an increase. |
| A-9 | Some firms make or import both components that reach 30% cheaply and components that cannot (food-contact films). | other | 0.85 | Converters' product ranges; importers of mixed goods. | C-7 under U1-b and C-6's (+) chain not reported. |
| A-10 | Recycled resin delivered in Saldria can expand only at a higher cost: collection and sorting are near capacity, added collection reaches more dispersed sources and dirtier bales, and regional resin costs more (C-30); the cost per tonne does not fall as supply expands within the medium run. | durability | 0.7 | Collection near route and sorting capacity; regional prices; bale quality data. | C-27, C-28 and C-29 not signed (C-28 not by the response argument); C-26 still increases if supply is perfectly elastic at the old price. |
| A-11 | Packaging is a material part of the cost of some packaged goods (6% to 10% for bottled water and pre-packed produce), and their sellers cannot switch fully at the old cost. | substitutability | 0.75 | Cost shares from industry surveys. | C-35, C-36 not reported. |
| A-12 | Exporters of empty packaging and packaged goods sell at prices set abroad. | substitutability | 0.8 | Saldria's small share of its export markets; contracts in foreign currency. | C-38 weakens to the TX-8 chain; C-39 not reported. |
| A-13 | Some exporters can replace export filling or converting lines abroad when they come up for replacement. | mobility | 0.55 | Firms with plants in the region; replacement cycles. | C-39 not reported. |
| A-14 | Some firms that would handle 10 to 13 t can keep under 10 t at a cost below the notch (2,000 T of tax and 2,500 to 4,000 T of compliance a year). | binding | 0.7 | About 380 firms at 10 to 13 t; ordering patterns; some packaging can be bought from suppliers who are already liable instead of imported. | C-12, C-13 not reported; C-14 and C-18 lose a chain. |
| A-15 | Moving the importer of record to unrelated parties (customers, foreign sellers who register) is cheap enough for some near-line firms. | other | 0.4 | The common-control rule blocks splitting among affiliates. | Below the cut-off; not reported. |
| A-16 | Liable firms can store packaging and bring orders forward into late 2027. | expectations | 0.75 | Warehouse capacity; packaging keeps. | C-15 to C-17 not reported; C-18 becomes a decrease. |
| A-17 | Misdeclaring recycled content or weight costs some firms less than the tax, given audits and penalties. | enforcement | 0.6 | Recycled content is hard to verify chemically; mass-balance records; audit rates in comparable taxes. | C-19 not reported. |
| A-18 | Converters, multi-product users and recyclers can organize to lobby on U1 and the rules at a cost below their stake. | other | 0.8 | Existing associations; responses to the Revenue Service's consultation. | C-21 not reported. |
| A-19 | Investors expect the tax, and its exemption, to last at least several years. | expectations | 0.8 | No expiry; cross-party support in the vote. | C-23, C-25 and C-41 to C-43 shrink. |
| A-20 | Converting plants are specific to plastic converting and cannot move to other uses without large losses. | durability | 0.8 | Extrusion and moulding lines. | C-41 smaller. |
| A-21 | Changes in imports and exports are not offset by capital flows within the medium run. | other | 0.6 | Floating rate; capital account. | C-40 not reported (it is `ambiguous` either way). |
| A-22 | Goods imported by small importers compete with goods packaged or imported by liable firms. | substitutability | 0.65 | Specialty food and household goods sold through the same retailers. | C-37 not reported; C-53 loses its (+) chain and becomes a decrease. |
| A-23 | Recyclers and substitute makers adjust their labor to their sales. | alternative_uses | 0.75 | Staffing practice. | C-45 not reported. |
| A-24 | The plastics unit is funded by the 7 million T appropriation in the Act, from the general budget that receives the tax. | revenue_use | 0.9 | The Act's text. | C-49's arithmetic changes. |
| A-25 | Converters adjust labor to output. | alternative_uses | 0.8 | Shift patterns; overtime. | C-44 not reported. |
| A-26 | Municipalities can extend collection and sell more bales at the higher price. | alternative_uses | 0.7 | Collection contracts; sorting capacity plans. | C-33 smaller; C-34 not reported. |
| A-27 | Converters can buy equipment that lets them process recycled resin, and expect the exemption to last long enough to pay for it. | expectations | 0.7 | Equipment suppliers' lead times; A-19. | C-22 not reported; C-24 becomes a decrease. |
| A-29 | With the tax in place, the ban campaign and its opponents spend as much as on the counterfactual path. | other | 0.45 | The campaign's statements after the tax was announced. | Below the cut-off; lobbying over a ban is not signed. |
| A-30 | Some foreign suppliers cannot document recycled content that meets K2's evidence rule, so their packaging is taxed as 0% recycled. | other | 0.65 | Supplier surveys; the Revenue Service's draft guidance on evidence. | C-53 loses a (−) chain (still `ambiguous`); C-54 rests on A-3 and A-32. |
| A-31 | Some users under 10 t can import their own packaging at a cost below the tax they would pay on domestic packaging. | other | 0.55 | Minimum order sizes; freight costs for small lots; 1,000 T saved on 5 t a year. | C-55 not reported; C-54 becomes a decrease without A-32. |
| A-32 | The shift of small users to direct imports is smaller than the fall in liable firms' imports of empty packaging. | other | 0.65 | All firms under 10 t together handle about 25,000 t; liable firms import about 120,000 t. | C-54 becomes `ambiguous`. |

A-28 is not used: the Food Safety Authority's rule is a fact of the record on both paths, not an assumption.

## 11. Report

**The policy.** From 1 January 2028, Saldria taxes plastic packaging at 200 talers a tonne, collected from domestic makers and from importers of empty packaging and of packaged goods, with no relief for exports. Packaging with at least 30% recycled plastic is exempt; whether that is judged component by component or averaged over a firm's quarterly output is unclear (U1). Firms that handled under 10 tonnes in the previous year pay nothing; above that, they pay on everything.

**Visible consequences.** The state collects the tax (C-1). Taxed packaging costs its users more (C-2), and users bear more of the tax than sellers (C-52). Less taxed plastic is used (C-3), and the average recycled content of packaging rises (C-4).

**Invisible consequences.**
- *Design.* Components are redesigned to reach 30% and composites to keep plastic under half their weight (C-5); taxed components get lighter (C-8); users move to board, glass and metal (C-9). Under U1-a, components that carried more than 30% recycled content cut it toward the line; under U1-b the sign is open (C-6). Under U1-b only, firms combine product lines to average (C-7).
- *Recycled resin.* More is used, and it costs more in Saldria, in the short and medium run (C-26 to C-28). Users who already met 30% pay more for it and gain nothing (C-29). The regional price rises slightly (C-30); the world price of virgin resin falls very slightly (C-31), and Saldria imports less of it (C-32). Municipalities sell bales for more and collect more (C-33, C-34). Recyclers invest (C-25) and gain value (C-42).
- *Substitutes.* Board and glass cost more per unit of a given grade (C-10, C-11), also for those who used them anyway. Their makers gain value and hire (C-43, C-45).
- *Converters.* Lose value (C-41), use less labor (C-44), invest in recycled-resin equipment but less in capacity (C-22, C-23; the total is open, C-24).
- *Small firms.* Firms near 10 t keep under the line, starting in 2027 (C-12, C-13). Small users import packaging directly rather than buy taxed domestic packaging (C-55), and small importers' goods gain sales (C-37).
- *Timing.* Liable firms stock up in late 2027 and buy less in early 2028 (C-15 to C-17).
- *Trade.* Exporters, taxed with no relief, sell less abroad (C-38) and in time replace export lines abroad (C-39). Imports of empty packaging fall (C-54).
- *Buyers.* Goods with a high packaging share cost more and sell less (C-35, C-36).
- *Compliance and enforcement.* Registration and records (C-20), redesign and testing (C-51), certification (C-46), the Revenue Service's work (C-48), misdeclaration (C-19), and lobbying on U1 (C-21). Revenue falls short of the static projection (C-50); net of the appropriation, the budget gains (C-49). Those who keep using taxed plastic have less to spend elsewhere (C-47).

**Ambiguous effects.** Converters' total investment (C-24); the value of firms near the 10-tonne line (C-14) and their 2027 purchases (C-18); imports of packaged goods (C-53); other export industries, through the currency (C-40); under U1-b, recycled content of components already above 30% (C-6).

**Key conditions.** That users can cut taxed plastic at a cost below the tax (A-3, p = 0.85) and that some components can reach 30% cheaply (A-4, p = 0.85) drive most results. The rise in the recycled resin price into the medium run rests on rising collection costs (A-10, p = 0.7). Incidence on users rests on imports at the margin (A-2, p = 0.75).

**What this analysis cannot say.** How much plastic or revenue changes; whether the tax reduces litter or emissions, which is outside the scope of version 1; whether users or converters bear the larger loss in money; whether the policy is desirable.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | state budget | tax_revenue (plastic packaging tax) | increase | short | visible | A | TX-1 | none |
| C-2 | packaging_users | price_paid (taxed plastic packaging, per tonne of a given specification) | increase | short | visible | B | TX-2, DM-1, CR-7b | A-2, A-3 |
| C-3 | packaging_users, converters, sellers.foreign | quantity_traded (taxed plastic packaging) | decrease | short–medium | visible | B | TX-2, OC-4, CR-4c, CR-5a | A-3 |
| C-4 | packaging_users, converters | product_attribute (average recycled content) | increase | short–medium | visible | B | RS-5, CR-1, CR-4, CR-12e | A-4, A-10 |
| C-5 | converters, packaging_users | reclassification (redesign to reach 30%; composites under half plastic) | increase | short–medium | invisible | B | RS-5, CR-4, CR-1 | A-4 |
| C-6 | packaging_users (components above 30% on the counterfactual path) | product_attribute (their recycled content) | U1-a: decrease; U1-b: ambiguous | medium | invisible | B | CR-4c, CR-9, CR-12b | A-8, A-9, A-10 |
| C-7 | converters, packaging_users, importers.packaging | reclassification (output combined to average recycled content) | U1-a: no_change; U1-b: increase | short–medium | invisible | B | RS-5, CR-1, CR-4 | A-9 |
| C-8 | converters, packaging_users | unit_size (plastic weight per taxed component) | decrease | short–medium | invisible | B | CR-4c, CR-1 | A-5 |
| C-9 | packaging_users | quantity_substitute (board, glass, metal packaging) | increase | short–medium | invisible | B | RS-1, RS-16 | A-6 |
| C-10 | packaging_users, buyers.substitutes | price_substitute (paperboard, per tonne of a given grade) | increase | short | invisible | B | RS-16, CR-6 | A-6, A-7 |
| C-11 | packaging_users, buyers.substitutes | price_substitute (glass containers, per unit of a given type) | increase | short | invisible | B | RS-16, CR-6 | A-6, A-7 |
| C-12 | firms.near_threshold | number_of_sellers (just under 10 t) | increase | short–medium | invisible | B | RS-17, CR-1, CR-4, CR-10a | A-14 |
| C-13 | firms.near_threshold | number_of_sellers (10 t to about 13 t) | decrease | short–medium | invisible | B | RS-17, CR-4 | A-14 |
| C-14 | firms.near_threshold | asset_value | ambiguous | short | invisible | B | RS-17, CR-7c, CR-12b | A-14, A-19, A-22 |
| C-15 | liable firms well above 10 t | quantity_traded (October to December 2027) | increase | short | invisible | B | RS-8, CR-10a | A-16 |
| C-16 | liable firms well above 10 t | quantity_traded (January to March 2028) | decrease | short | invisible | B | RS-8, CR-10a | A-16 |
| C-17 | liable firms well above 10 t | inventory_held (31 December 2027) | increase | short | invisible | B | RS-8, CR-10a, CR-7a | A-16 |
| C-18 | firms.near_threshold | quantity_traded (March to December 2027) | ambiguous | short | invisible | B | RS-8, RS-17, CR-12b | A-14, A-16 |
| C-19 | converters, importers | legal_breach (misdeclared content or weight) | increase | short–medium | invisible | B | RS-3, CR-4 | A-17 |
| C-20 | liable firms | compliance_cost (registration, records, returns) | increase | short | invisible | A | TX-5, CR-4, CR-8c | none |
| C-21 | converters' association, multi-product users, recyclers | lobbying_effort (U1 and implementing rules) | increase | short–medium | invisible | B | RS-7, CR-4, CR-12 | A-18 |
| C-22 | converters | investment_target (recycled-resin processing equipment) | increase | short–medium | invisible | B | CR-4, CR-10a | A-4, A-27 |
| C-23 | converters | investment_target (converting capacity) | decrease | medium | invisible | B | TX-3, RS-6 | A-3, A-19 |
| C-24 | converters | investment_target (total) | ambiguous | medium | invisible | B | CR-12, CR-12b | A-3, A-27 |
| C-25 | recyclers | investment_target (recycling and sorting capacity) | increase | medium | invisible | B | CR-4, CR-7a, CR-10a | A-10, A-19 |
| C-26 | recyclers, packaging_users | quantity_traded (recycled resin delivered in Saldria) | increase | short–medium | invisible | B | CR-9, LW-10, CR-6 | A-4, A-10 |
| C-27 | recyclers | net_price_received (recycled resin) | increase | short | invisible | B | CR-9, CR-6 | A-4, A-10 |
| C-28 | recyclers | net_price_received (recycled resin) | increase | medium | invisible | B | CR-6, CR-12e | A-4, A-10 |
| C-29 | packaging_users already at 30% or more | price_paid (recycled resin) | increase | short–medium | invisible | B | CR-9, CR-6 | A-4, A-10 |
| C-30 | buyers.foreign (regional) | price_paid (recycled resin, regional market) | increase | short–medium | invisible | B | CR-6, CR-9 | A-4 |
| C-31 | sellers.foreign (virgin resin) | net_price_received (virgin resin, world market) | decrease | short–medium | invisible | B | CR-6, CR-9, LW-10 | A-3 |
| C-32 | converters, sellers.foreign | quantity_traded (virgin resin imported) | decrease | short–medium | invisible | B | CR-9, LW-10 | A-3 |
| C-33 | municipalities | net_price_received (plastic bales) | increase | short–medium | invisible | B | CR-9, LW-10, CR-6 | A-4, A-26 |
| C-34 | municipalities | quantity_supplied (plastic collected and sold) | increase | medium | invisible | B | CR-4, CR-9 | A-26 |
| C-35 | buyers.packaged_goods | price_paid (goods with a high packaging share) | increase | short–medium | invisible | B | RS-14, CR-9 | A-2, A-11 |
| C-36 | buyers.packaged_goods | quantity_demanded (those goods) | decrease | short–medium | invisible | B | RS-14, CR-4c | A-2, A-11 |
| C-37 | small_importers | quantity_traded (packaged goods imported by firms under 10 t) | increase | medium | invisible | B | CR-9, CR-4 | A-22 |
| C-38 | exporters | quantity_supplied (exports of packaging and packaged goods) | decrease | medium | invisible | B | RS-14, RS-6, CR-7b | A-12 |
| C-39 | exporters | capital_stock_target (export lines in Saldria) | decrease | long | invisible | B | RS-4, RS-6, TS-1 | A-12, A-13 |
| C-40 | export_industries | quantity_supplied (other exports) | ambiguous | medium | invisible | B | TX-8, CR-9, CR-12 | A-21 |
| C-41 | converters.owners | asset_value | decrease | short | invisible | B | CR-7c, CR-10c, SB-4 | A-3, A-19, A-20 |
| C-42 | recyclers.owners | asset_value | increase | short | invisible | B | CR-7c, CR-10c, SB-4 | A-10, A-19 |
| C-43 | owners of sellers.substitutes | asset_value | increase | short | invisible | B | CR-7c, SB-4 | A-6, A-7, A-19 |
| C-44 | converter_workers | employment, hours_worked | at_least_one_decrease | medium | invisible | B | TX-3, RS-6, OC-5 | A-3, A-25 |
| C-45 | recycler_workers, workers of sellers.substitutes | employment, hours_worked | at_least_one_increase | medium | invisible | B | OC-5, CR-9, LW-10 | A-6, A-23 |
| C-46 | intermediaries | quantity_traded (certification and compliance services) | increase | short | invisible | B | CR-9, CR-8c | A-4 |
| C-47 | packaging_users and importers who keep using taxed plastic | resources_available_other_uses | decrease | short | invisible | B | TX-1, OC-1, CR-3 | A-2 |
| C-48 | officials.enforcement | enforcement_cost | increase | short | invisible | A | OC-3, CR-8c | none |
| C-49 | state budget | tax_revenue (net of the plastics unit's appropriation) | increase | short | invisible | B | CR-8, CR-12e | A-24 |
| C-50 | state budget | tax_revenue_vs_static_projection | decrease | short | invisible | B | TX-9 | A-3 |
| C-51 | packaging_users, converters (who redesign, switch or lighten) | compliance_cost (redesign, testing, qualification) | increase | short | invisible | B | CR-8c, CR-3a, OC-2 | A-4, A-5 |
| C-52 | packaging_users | tax_share_borne | increase | short–medium | invisible | B | DM-1, CR-7b | A-2 |
| C-53 | importers.packaged_goods, sellers.foreign | quantity_traded (imported packaged goods) | ambiguous | medium | invisible | B | TX-2, CR-4, CR-9, CR-12b | A-11, A-22, A-30 |
| C-54 | importers.packaging, sellers.foreign | quantity_traded (empty plastic packaging imported) | decrease | short–medium | invisible | B | TX-2, CR-4c, CR-12e | A-3, A-30, A-32 |
| C-55 | small_importers (small packaging users) | quantity_traded (empty packaging imported directly by users under 10 t) | increase | medium | invisible | B | RS-5, CR-4 | A-31 |

Final check (workflow). (1) Uncombined chains: every key reached by opposing chains is in section 7: average recycled content against the cut-back above 30% (C-4, C-6), the recycled resin price against recyclers' expansion and imports (C-28), converters' two investment items (C-24), near-line firms' 2027 tonnage and value (C-18, C-14), empty-packaging and packaged-goods imports (C-54, C-53), and the currency (C-40). The price per tonne and the weight per component are different variables (C-2, C-8). (2) Groups: converters' and recyclers' labor (C-44, C-45); no single member is signed alone. (3) Baseline: every sign is against Saldria without the tax, not against a tax without the exemption or the threshold; U1 readings are each signed against no tax, never against each other (C-6, C-7). (4) Worse off is not poorer: `resources_available_other_uses` is signed only for those who keep paying the tax (C-47); switchers bear a cost of switching (C-51) and users already at 30% pay more for recycled resin (C-29), but neither is signed as having less to spend. (5) Timing: the last quarter of 2027 and the first of 2028 are signed per window (C-15, C-16) for firms that pay on both sides of the date; near-line firms' 2027 is a separate key (C-18). (6) Transfers: the tax paid (C-47) and received (C-1); the budget's two items and the net (C-1, C-48, C-49); the higher recycled resin price paid (C-29) and received (C-27, C-33); prevented packaging sales on both sides (C-3). (7) Every class against CR-4, CR-6, CR-7 and CR-9: capitalization for converters, recyclers, substitute makers and near-line firms (C-41 to C-43, C-14); enforcement and compliance (C-20, C-48); CR-9 to inputs (resin, bales), substitutes, buyers of packaged goods, certifiers and, through the currency, other exporters. (8) Premises: every derivation's premises are in section 10, including those below the cut-off (A-15, A-29); the response argument for C-28 names its total and its rising-cost and partial premises (A-10). (9) Baseline of every pattern cited: TX-7 compares the import leg with a policy that taxes imports only; it is re-signed against no tax (section 2) and not used. RS-17's main clause compares the band below the line with the band above; each band is signed against no tax (C-12, C-13). DM-1 compares two sides' shares, as `tax_share_borne` is defined (C-52). TX-1, TX-2, TX-3, TX-5, TX-8, TX-9, RS-1, RS-3, RS-4, RS-5, RS-6, RS-7, RS-8, RS-14, RS-16, OC-1 to OC-5, SB-4 and TS-1 compare with the path without the tax. RS-21 is not cited: its preconditions are not met. Small effects in wider markets are signed (C-10, C-30, C-31).

## Gaps found

**(a) Calculus gaps (a step no core rule covers).** None. Every step was derived from CR-1 to CR-12, with patterns where their preconditions held.

**(b) Unclear core rules.**
1. *CR-12 1.0, what the response argument needs: "a second response to the same change".* The clause says a second response to the same change is a second chain to combine. For the recycled resin price (C-28), recyclers' expansion and imports from the region both respond to the same price rise. Read literally, imports would be a second chain with no dominance premise, and the medium-run price would be `ambiguous`. But neither response, nor both together, can push the price below its old level once the total is named over both sources and each has rising cost. The clause's examples (a new competitor attracted by the policy, a stock built in advance) are changes that are not responses to the price itself. I read "second response" as a response to a different change the policy causes, or one outside the named total. The clause should say that responses to the same price movement are covered together once the total includes them all.
2. *CR-1 1.0, notches on a ratio.* Under U1-b the notch is on a firm's average recycled content, not on a size. It can be crossed by raising the numerator (more recycled resin) or by changing the denominator (adding high-content output, dropping virgin lines). CR-1's notch note ("record the operation on each side, and the jump as a cost of crossing") covers it, but RS-17 and CR-1 are written for a line on a quantity. A sentence that a line on a ratio is crossed by moving either term would help.
3. *CR-6 1.0, small effects are signed.* Worked as written, but in a chain with several links the "small" effect can sit at different depths (Saldria's tonnage, then virgin resin demand, then the world price). The clause does not say whether the depth limit of workflow step 6 still applies to such chains. C-31 is at depth 3.

**(c) Missing or wrong patterns.**
1. *TX-7 on a border tax matched by an equal domestic tax.* TX-7's preconditions are met by the import leg taken alone (a tax collected on imported goods). Its conclusion, that domestic sellers of substitutes gain, is wrong against the no-tax counterfactual when domestic output pays the same rate. Applied as written it gives a sign I had to override (section 2; CR-12, 1.0, the baseline of patterns). TX-7 needs an Unless clause: where domestic output of the same good pays the same tax, apply TX-2 to the whole tax, and derive gains or losses to domestic sellers only from the points where imports and domestic output are treated differently. Here those points ran the other way: the small-firm threshold favors imports by small users (C-55, C-37), the evidence rule disfavors undocumented imports (C-53), and the lack of export relief burdens exporters (C-38).
2. *RS-21 and a tax counted in physical units.* RS-21 is written for a cap, quota or right. A per-tonne tax prices the counted unit as a cap's lease price does, and CR-4c gives the same move: the value carried per counted unit rises. But RS-21's examples sign `unit_size` as an increase (larger aircraft per slot). With a count by weight and a free choice of items per tonne, the item gets lighter (C-8). RS-21 could be widened to "a charge or cap counted in physical units", and say that the item moves so as to raise value per counted unit, which under a weight count means less weight per item.
3. *RS-17's main clause is phrased against the other band.* "Just below the threshold increases relative to just above" is a comparison between two bands, not with the counterfactual. Signed against no tax, the band below rises and the band above falls (C-12, C-13). The 1.0 preamble says to re-sign such phrasing; RS-17 could be reworded.
4. *A threshold that exempts small importers but not domestic sellers.* K3 exempts a small firm on what it imports, while its domestic supplier is liable. This works as a negative tariff on domestic sales to small buyers (C-55). No pattern prompts it; it was derived from CR-1 (the operation depends on who is the importer) and CR-4. Candidate pattern: "a size exemption for the person liable moves liability toward the exempt party's own imports".
5. No other pattern gave a sign I had to override.

**(d) Vocabulary.**
1. No variable for the distribution of a product attribute around a line (bunching of recycled content at 30%); recorded through `reclassification` (C-5) and `product_attribute` with a qualifier (C-6).
2. No actor class for a firm defined by its size against a threshold; `firms.near_threshold` was coined, as in WE-048.
3. `tax_share_borne` is defined between subgroups "in the same market"; here buyers are compared with domestic and foreign sellers together (C-52).

**(e) Test of 1.0.**
- *TX-2 and TX-7 on imports of packaged goods (tax on the form of imports).* TX-2 worked as written for the tax as a whole, with DM-1 for the split (C-2, C-52). TX-7 failed: its preconditions are met by the border leg, but its conclusion (protected sellers gain) is against another policy. Re-signed under CR-12 1.0 and not used ((c) 1).
- *TX-8, form of imports.* TX-8 has no 1.0 clause; the 0.9 clause worked as written. Imports of resin and empty packaging fall, imports of recycled resin, board and some packaged goods rise, and exports fall, so the currency chain is kind 3 and `ambiguous` (C-40).
- *RS-5, redesign around the 30% line.* Worked as written (C-5), and also covered the material-weight line for composites. It does not by itself give the per-reading signs; those came from CR-4 applied under each reading (C-6, C-7).
- *RS-21, counted in tonnes.* Failed on preconditions: a tax is not a cap. The same move was derived from CR-4c, with the direction of `unit_size` the reverse of RS-21's examples ((c) 2). Not cited.
- *RS-17 1.0, notch or kink, and CR-1 1.0, notches.* Worked: the 10-tonne line is a notch (tax on all tonnage, plus a fixed compliance cost), and the past-period clause put the response in 2027 (C-12, C-13). RS-17 0.9's value clause gave `ambiguous` (C-14). Needed interpretation on the main clause's phrasing "relative to just above" ((c) 3). The 1.0 eligibility clause did not apply. CR-1's notch note also covered the 30% line, under both readings ((b) 2).
- *CR-6 1.0, small effects are signed.* Worked as written for the regional recycled resin price (C-30), the world virgin resin price (C-31) and the regional board price (C-10), each with its size in the evidence. Depth question in (b) 3.
- *RS-16 1.0, substitute prices per unit of quality.* Worked as written: board and glass prices are signed per grade and type (C-10, C-11), and the shift toward barrier board is excluded as a change in mix. The clauses on costs on the substitute and on fixed costs per facility did not apply.
- *CR-12 1.0, the baseline of patterns.* Worked as written, and it mattered: it caught TX-7 ((c) 1) and RS-17's phrasing ((c) 3). DM-1's comparison of shares is its own definition and was kept.
- *CR-12 1.0, what the response argument needs.* Worked with interpretation. For the recycled resin price (C-28) the total, the rising-cost premise and the partial response were stated (A-10); whether imports are a "second response" needed reading ((b) 1). The argument also signed the average recycled content (C-4) against the cut-back above 30%.
- *CR-12 1.0, tiers and dominance.* Not exercised: no Tier C chain.
- *CR-8 1.0, receipts into the same budget.* Worked as written: receipts, appropriation and net, signed by arithmetic (C-1, C-48, C-49).
- *CR-4 1.0 and RS-7 1.0, lobbying generally.* Worked as written: lobbying on U1 exists only under the Act (C-21). Lobbying over a ban, contested on the counterfactual path, was left unsigned for want of a premise (A-29).
- *RS-8 0.9 and 1.0.* The 0.9 clause on more timing chains worked for near-line firms (C-18). The 1.0 clause on races and rivals did not apply.
- *Candidate patterns from 06_gaps.md, 6.2e.* None needed. "A standard per unit of a chosen attribute shifts the attribute" (WE-031) was considered for the per-tonne tax and lightweighting (C-8), but K1 is a charge per unit of the attribute itself, not a standard normalized by an attribute the seller chooses, so it is a different move. "Tariff-like burden without a tax" does not apply: here there is a tax, and it is not a burden on imports alone. One new candidate is proposed in (c) 4.
