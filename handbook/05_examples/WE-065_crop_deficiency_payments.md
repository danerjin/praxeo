# WE-065 Deficiency payments to wheat growers, with a target price set above a world-market price

Analyst: draft (Handbook 1.0 held-out test, corrected under 1.1)  |  Rule catalog version: 1.1  |  Status: awaiting expert review

A stylized policy in a fictional country. Several countries have paid farmers the gap between a target price and the market price; this one is not modeled on any of them. It is a held-out test of catalog 1.0 on a kind of policy none of the 1.0 changes were drawn from: a subsidy per unit of output that is paid only in years when a price set in a wider market falls below a line. It probes SB-2 and SB-10 for a subsidy on output when the price is set abroad, CR-6's 1.0 note that small effects on a world price are signed, CR-8's clause on contingent payers (payments occur only when prices fall), CR-7c on the capitalization of a contingent payment into land, RS-16's 1.0 note on prices per unit of quality (the payment rate is computed from an average price over grades), EN-12 under the reading that payments are made on a fixed historical base, TX-8's mirror case, and CR-12's 1.0 notes on what the response argument needs and on the baseline of patterns. The unclear provision is whether payments are made on each farm's actual output or on a fixed historical base. The counterfactual throughout is **Brisklund without the Act**: wheat sold at the world-linked market price with no support, and the question of farm support still debated. Effects on soils, water and nutrition are outside the scope of version 1. The probabilities are illustrative; the evidence column says what a real analysis would cite.

## 1. Policy record

**Brisklund Wheat Price Assurance Act.** Brisklund is a country of about 9 million people with its own currency, the thaler (Th). About 18,000 farms grow wheat on about 570,000 hectares; at about 7.0 tonnes a hectare they produce about 4.0 million tonnes a year. About 2.5 million tonnes are used at home (1.4 by millers, 1.1 as animal feed) and about 1.5 million tonnes are exported. World wheat production is about 800 million tonnes and world trade about 200 million; Brisklund's exports are under 1% of world trade. The farm-gate price follows the export price less freight. Over the past ten marketing years the national average farm-gate price ranged from Th 175 to Th 285 a tonne, averaged about Th 232, and was below Th 220 in four of the ten years, by about Th 20 on average in those years. Milling varieties fetch about Th 18 a tonne more than feed varieties and yield about 0.6 tonnes a hectare less. Barley (about 1.2 million tonnes, part exported) competes with wheat for land and with feed wheat in animal feed. About 40% of wheat land is rented, on leases of three to five years; wheat land sells for about Th 12,000 a hectare and rents for about Th 300 a hectare a year. The Farm Register, kept by the Ministry of Agriculture, records for each registered farm its annual harvest declarations and, since 2026, its "established production": the average of its wheat output in the crop years 2022 to 2026, entered for a crop-insurance scheme that has since ended. Registration requires that agricultural activity is carried out on the farm. About 3.8 million tonnes of established production are recorded in all.

The bill was introduced with the government's majority on 10 February 2027 and enacted on 30 June 2027. It covers the crop years 2028 to 2032 (the harvests of those years; winter wheat for 2028 is sown in autumn 2027). Parliament must review the target price before 2032.

**Figures.** Payment rate = Th 220 less the national average farm-gate price for the marketing year, when that price is below Th 220; otherwise zero. On the past ten years' prices, the expected payment is about Th 7 to Th 8 a tonne a year, and in a year at Th 180 the payment is Th 40 a tonne: about Th 160 million on 4.0 million tonnes (U1-a) or Th 152 million on 3.8 million tonnes of established production (U1-b), against a general budget of about Th 40 billion. Futures for the 2028 harvest trade at about Th 228. The Ministry's payments office costs about Th 4 million a year. A grower switching a hectare from a milling to a feed variety gains about 0.6 tonnes and loses Th 18 a tonne on 6.6 tonnes: at a payment of Th 8 a tonne the switch gains about Th 5 a hectare more than without the payment; at Th 40, about Th 24.

| Field | Value | Source sentence |
|---|---|---|
| Jurisdiction (and what lies just outside) | Brisklund. Neighbors grow wheat without such payments; grain crosses the borders by rail and road. | §1. |
| Announced / enacted / effective / expires | Announced 10 February 2027 (bill introduced with a majority); enacted 30 June 2027; crop years 2028 to 2032; review before 2032. | §1, §12. |
| Enforcement (who, penalties, resources) | Ministry of Agriculture payments office: claims on the Farm Register; harvest declarations checked by sampling (about 3% of farms a year); false declarations: repayment and a fine of up to twice the payment. | §8 to §10. |

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Deficiency payment | `per_unit_subsidy` (contingent) under U1-a; `lump_sum_subsidy` (contingent) under U1-b | Wheat | Paid to the holder (the person registered as farming the land) of each registered farm | Rate: Th 220 less the national average farm-gate price for the marketing year, if positive. Paid in December after the marketing year. | — |
| K2 Funding | `revenue_use` (outlay) | K1 | The general budget | "Such sums as are needed for payments under this Act shall be paid out of the Consolidated Fund." | — |
| K3 Administration | Enforcement | K1 | Ministry payments office, from its general appropriation | About Th 4 million a year. | — |

Existing rules that stay in the counterfactual: the Farm Register and its registration rule; no tariff or quota on wheat; leases freely negotiated.

Unclear provision:
- **U1, actual output or a historical base.** §4(1): "A deficiency payment is payable to the holder of each registered farm on the farm's wheat production for the crop year." §2: "'Wheat production', in relation to a farm, means the production of wheat recorded for the farm in the Farm Register." The Register records both annual harvest declarations and established production (the 2022 to 2026 average). Reading U1-a: the payment is on the harvest declared for the crop year (actual output). Reading U1-b: it is on the farm's established production, "for the crop year" fixing only the year whose price sets the rate. The Ministry has issued no guidance.

Readings get no probability; where a sign depends on U1, one sign per reading is given.

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | Rule families |
|---|---|---|---|
| K1 | Binary. Under U1-a it attaches a payment to the option of producing each tonne, in years when the market price is below Th 220 (CR-1, operation 3): growers' net price per tonne becomes the higher of the market price and Th 220. Under U1-b it is a transfer to the holder of each farm with established production, independent of what the farm grows (operation 4), conditional on the year's price; and on the option of keeping the farm registered (operation 3, through the registration rule). | Pays in years when the price is below Th 220 (A-2); affects planting under U1-a wherever the expected payment is positive (A-3). | SB-1, SB-2 (1.1), SB-3, SB-4, DM-1, CR-6 (0.7, 1.0), CR-7c, EN-12 (U1-b), RS-16 (1.0), TX-8 (mirror), RS-11 (U1-b), RS-3 (U1-a) |
| K2 | Binary: funded from the general budget, with payers that depend on the year's price. | Yes | SB-1, OC-1, CR-8 (0.7, 0.8: payers from a general budget; contingent payers; 1.0: receipts into the same budget) |
| K3 | Binary: administration from a general appropriation. | Yes | OC-3 |

**SB-2 and SB-10.** SB-2 (a per-unit subsidy) gives buyers' price down and/or sellers' net price up, and the quantity up. SB-10 (an export subsidy) gives a domestic price rising toward the export price plus the subsidy, because sellers move sales abroad. K1 is paid on every tonne produced, whether sold at home or abroad, so there is no gain from moving sales abroad: SB-10's preconditions are not met and its domestic-price conclusion does not apply. SB-2 applies under U1-a, read with CR-6's 0.7 clause on a good priced in a wider market: Brisklund's growers sell at the world-linked price, so the subsidy goes almost entirely to their net price, and buyers' price falls only by the subsidy's small effect on the world price, which CR-6's 1.0 note says to sign (C-17, C-20). SB-2's 1.1 clause now says this itself: where the good is priced in a wider market, the domestic price is set there, and the small effect on the wider price is signed. Under U1-b, the payment is not tied to output at the margin, and SB-2 does not apply.

**A contingent payment.** In years when the price is at or above Th 220, K1 pays nothing. So its consequences are signed per state of the world: years below the line, years at or above it, and the whole period with a premise on how many years fall below (CR-8, 0.8; CR-12, 0.7, whole period). Before each sowing, growers act on the expected payment, which is positive whenever a price below Th 220 is possible (CR-10a).

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `wheat_growers` (holders of registered farms) | Owner-occupiers and tenants who grow wheat | U1-a: each tonne grown earns at least Th 220. U1-b: a payment on established production in years below Th 220, whatever they grow. |
| `owners.wheat_land` (`factor_owners.specific`) | Owners of land with wheat history | Expected yield of the land rises. |
| `owners.convertible_land` | Owners of pasture and other land that could grow wheat but has no wheat history | U1-a: wheat becomes a better use of the land. |
| `tenants` | Growers who rent | Receive the payment until their leases are renegotiated. |
| `buyers.current` | Millers and feed users in Brisklund | Buy at the world-linked price. |
| `feed_buyers` | Livestock producers buying feed barley and feed wheat | Feed wheat and barley supplies shift. |
| `grain_exporters` | Traders exporting Brisklund wheat | More to export under U1-a. |
| `buyers.foreign`, `sellers.foreign` | Wheat buyers and growers abroad | The world price moves by Brisklund's added exports. |
| `input_suppliers` | Seed, fertilizer and contract-harvesting firms | More wheat grown under U1-a, partly in place of barley. |
| `livestock_farmers` (renters of pasture) | Livestock producers who rent grazing land | Pasture that can be converted to wheat is worth more in wheat under U1-a. |
| `sellers.neighboring` | Growers and traders in neighboring countries | Grain sold into Brisklund can be declared as Brisklund harvest under U1-a. |
| `buyers.imports` | Buyers of imported goods in Brisklund | Import prices in thaler move with the currency. |
| `lenders.farm` | Banks lending to growers | Growers' income in low-price years is higher. |
| `hedge_sellers` | Sellers of put options and forward contracts on wheat | Growers' price risk is partly covered by the Act. |
| `import_competing_industries`, `export_industries.other` | Other industries linked through the currency | TX-8's mirror case. |
| `treasury`; `taxpayers`, recipients of other spending, future taxpayers | The general budget and those it serves | Pays in years below the line. |
| `officials.enforcement` | The Ministry's payments office | Administers claims and checks declarations. |
| `lobbying groups` | Farm unions, millers, holders of established production, expanding growers | Stakes in the target, the formula, the review and U1. |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | `treasury` | `subsidy_outlay` (crop years with the average price below Th 220) | increase | short (each such year) | SB-1, CR-8b | A-1 |
| C-2 | `treasury` | `subsidy_outlay` (crop years with the average price at or above Th 220) | no_change | short (each such year) | CR-1, CR-8 (0.8: contingent payers) | none |
| C-3 | `wheat_growers` | `resources_available_other_uses` (crop years below Th 220) | increase | short | SB-1, CR-8b, CR-4 (1.1: several changes in means) | A-1, A-18 |
| C-4 | `wheat_growers` | `net_price_received` (per tonne, years below Th 220: market price plus payment) | U1-a: increase; U1-b: no_change | short | SB-2, CR-5c, CR-1 | A-1 |
| C-5 | `wheat_growers` | `net_price_received` (per tonne, years at or above Th 220) | U1-a: decrease; U1-b: no_change | short | CR-6 (0.7; 1.0: small effects are signed), CR-9 | A-3, A-9, A-10 |
| C-6 | `wheat_growers` | `net_price_received` (expected per tonne at sowing, over 2028 to 2032) | U1-a: increase; U1-b: no_change | short to medium | SB-2, CR-10a, CR-12e (arithmetic, A-18) | A-1, A-18 |

The visible effect is the cheque in a bad year: the state pays (C-1) and growers receive (C-3). Growers' means change in two ways under U1-a, the payment and the slightly lower world price (C-5, C-17); by CR-4's 1.1 note (several changes in means) they are netted first: in a year below the line the payment (up to Th 40 a tonne) is far larger than the world-price effect (a fraction of a thaler; A-18), so the net is an increase (C-3). Under U1-a, every tonne sold in such a year earns Th 220 in all (C-4). Under U1-b, the payment does not depend on what is sold, so growers' price per tonne is unchanged (C-4, `no_change`): the payment is a sum per farm.

**The price in good years (C-5).** Under U1-a, Brisklund grows more wheat (C-9) and exports it into a world market, which lowers the world price by a small amount (C-17). In years when the price is below Th 220, growers do not feel that fall: they receive Th 220 whatever the market pays. In years at or above Th 220, they receive the market price, which is now slightly lower than it would have been. CR-6's 1.0 note requires the sign even though the effect is small (C-5; its size, a fraction of a thaler, goes in the evidence). Supporters would not expect the Act to lower growers' price in any year.

**Expected price at sowing (C-6).** Under U1-a, a grower deciding what to sow expects the higher of the market price and Th 220. On the past ten years, that adds about Th 7 to Th 8 a tonne to the expected price; the opposing chain (C-5) is far smaller (A-18: Brisklund's added output is a few percent of its own crop against 800 million tonnes of world output). Arithmetic on the case's figures dominates (CR-12e): `increase`.

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-7 | `taxpayers`, recipients of other spending, future taxpayers | `resources_available_other_uses` (crop years below Th 220) | at_least_one_decrease | short | SB-1, OC-1, CR-8 (0.7: payers from a general budget; 0.8: contingent payers) | A-1 |
| C-8 | `taxpayers`, recipients of other spending, future taxpayers | `resources_available_other_uses` (whole period 2028 to 2032) | at_least_one_decrease | whole period | CR-8 (0.8), CR-12 (0.7: whole period) | A-1, A-2 |
| C-9 | `wheat_growers` | `quantity_supplied` (wheat grown in Brisklund) | U1-a: increase; U1-b: no_change | short to medium | SB-2, CR-4 | A-3 |
| C-10 | `wheat_growers` | `number_of_sellers` (farms growing wheat) | U1-a: increase; U1-b: no_change | medium | RS-6 (1.1: mirror), CR-4 | A-3 |
| C-11 | `wheat_growers` | `quantity_substitute` (barley and oilseed rape grown) | U1-a: decrease; U1-b: no_change | short to medium | SB-3, CR-4 | A-3, A-4 |
| C-12 | `wheat_growers` | `product_attribute` (share of high-yield feed varieties in wheat grown) | U1-a: increase; U1-b: no_change | short to medium | CR-4 (the unit of the payment), RS-16 (1.0: per unit of quality) | A-5 |
| C-13 | `wheat_growers` | `legal_breach` (overstated harvest declarations; bought grain declared as own) | U1-a: increase; U1-b: no_change | short | RS-3, RS-5, CR-4 | A-6 |
| C-14 | `wheat_growers` | `quantity_substitute` (put options and forward sales bought for price protection) | decrease | short | RS-1 | A-7 |
| C-15 | `lobbying groups` | `lobbying_effort` (provisions that exist only under the Act: which average price sets the rate, U1) | increase | medium | RS-7 (1.1), CR-4 (1.1: the same question), CR-12 (0.9: activities only under the policy) | A-8 |
| C-36 | `lobbying groups` | `lobbying_effort` (the level and continuation of wheat support: the target at the 2032 review, extension beyond 2032) | ambiguous | medium | RS-7 (1.0: Unless; 1.1), CR-4 (1.0, 1.1: the same question), CR-12b | A-8 |
| C-38 | `wheat_growers` | `quantity_supplied` (milling wheat) | U1-a: ambiguous; U1-b: no_change | short to medium | CR-4, CR-12b | A-3, A-5 |
| C-39 | `treasury` | `non_tax_receipts` (repayments and fines for false declarations) | U1-a: increase; U1-b: no_change | short to medium | CR-8b, CR-1 (operation 3) | A-6, A-21 |

**Contingent payers (C-7, C-8).** The money comes from the general budget, and the record names no tax. By CR-8's 0.7 note and OC-1, the payers are a group: taxpayers, recipients of other spending, or future taxpayers through borrowing, signed `at_least_one_decrease`. By CR-8's 0.8 note, a budget that pays only if something happens is recorded with the contingency: in years below Th 220 the group pays (C-7); in other years nothing is paid out (C-2). Over the whole term, the group pays if at least one year falls below the line (C-8; A-2, p = 0.85: four of the past ten years did). The administration costs fall on the same group every year (C-34).

**Output (C-9 to C-11).** Under U1-a, the expected price at sowing rises (C-6), so growers at the margin sow wheat on land that would have grown barley or rapeseed, or grow it more intensively (C-9; CR-4; A-3), fewer leave wheat (C-10), and other crops fall (C-11; SB-3; A-4: land moves between crops from year to year). Under U1-b, the payment on a farm is the same whatever it grows: the return to the last tonne, and to sowing wheat rather than barley, is unchanged, so CR-4 gives no switch (`no_change`). A change in growers' means alone could change what they do, but CR-4 says nothing about which uses (CR-4, a change in means alone): no chain. One margin does change under U1-b: a holder who takes a farm out of agriculture loses its registration and the payments (RS-11, a registration that lapses). Whether that keeps any wheat land in farming within five years is a premise below the cut-off (A-19, p = 0.35: land leaving farming goes mostly to building, worth far more than the payments), so by CR-12's 0.8 note the derived sign `no_change` is reported, and the chain is recorded in section 10.

**Varieties (C-12).** Under U1-a, the payment is the same on every tonne, of any grade. That makes the higher-yielding feed varieties gain more from it than milling varieties do: about Th 5 a hectare at an expected payment of Th 8, about Th 24 in a year at Th 40 (CR-4 with the payment's unit; A-5). Growers at the margin switch, and the share of feed varieties rises. This is the reverse of RS-21's high-grading: a payment counted in tonnes lowers value per tonne, as a cap counted in tonnes raises it ((c) 3). Under U1-b, the payment does not depend on what the farm grows: `no_change`.

**Declarations (C-13).** Under U1-a, each tonne declared earns the payment in a low-price year, and declarations are checked on about 3% of farms. Some growers overstate their harvest or declare grain bought from neighbors or across the border as their own (RS-3, RS-5; A-6). Under U1-b, the base is fixed: nothing is gained by declaring more.

**Hedging (C-14).** Under both readings the Act pays more when the price falls: under U1-a per tonne grown, under U1-b on the base. That is the cover a put option or a forward sale provides. Growers who bought such cover buy less (RS-1, x: buy cover, y: rely on the Act; A-7).

**Lobbying (C-15, C-36).** Farm support was debated in 2025 and 2026, and would have stayed contested without the Act. By CR-4's 1.0 note and RS-7 (1.0), lobbying on that question is signed against that contest. CR-4's 1.1 note says what "the same question" is: the question of the policy field contested on the counterfactual path (support for farmers), not the exact provision. The target at the 2032 review and the Act's extension beyond 2032 are that question: whether, and how generously, wheat growers are supported. Farm unions and taxpayers' groups lobbied on it in both worlds, so by RS-7's Unless clause the sign for each is `ambiguous` without a premise, and the case has none (C-36). The provisions that exist only under the Act are another matter: which average price sets the rate, and U1, on which holders of established production who now grow less wheat (U1-b better) and growers who have expanded (U1-a better) are on opposite sides. Lobbying on them is an increase against none (C-15; CR-4, 1.1; A-8).

**Milling wheat (C-38).** Under U1-a, more wheat is grown (C-9), which raises milling wheat with the rest; and growers at the margin switch from milling to feed varieties (C-12), which lowers it. The two chains oppose, and no figure ranks them: `ambiguous` (CR-12b). Under U1-b, neither happens.

**Repayments and fines (C-39).** Under U1-a, false declarations rise (C-13), and those found by the 3% sampling are repaid with a fine of up to twice the payment (§10). Detection of some of them is a premise (A-21). Repayments and fines are receipts of the general budget that also pays the outlay, so by CR-8's 1.0 note they and the outlay are two items, and the net is a separate consequence (C-40, section 6).

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-16 | `wheat_growers` | `compliance_cost` (claims and declarations) | increase | short | OC-2, CR-8c | — | none |
| C-17 | `buyers.foreign` | `price_paid` (world wheat price) | U1-a: decrease; U1-b: no_change | short to medium | CR-6 (0.7; 1.0: small effects are signed), SB-2 (1.1), CR-9, CR-12e (1.0, 1.1) | Brisklund and world wheat: `across_border` (export) | A-3, A-9 |
| C-18 | `sellers.foreign` | `net_price_received` (wheat) | U1-a: decrease; U1-b: no_change | short to medium | CR-6, CR-9 | as C-17 | A-3, A-9 |
| C-19 | `sellers.foreign` | `quantity_supplied` (wheat) | U1-a: decrease; U1-b: no_change | medium | CR-4, CR-7a | as C-17 | A-3, A-9 |
| C-20 | `buyers.current` | `price_paid` (wheat of a given grade, in Brisklund) | U1-a: decrease; U1-b: no_change | short to medium | CR-6 (0.7, 1.0), RS-16 (1.0: per unit of quality) | domestic price follows export parity | A-3, A-9, A-10 |
| C-21 | `grain_exporters` | `quantity_traded` (wheat exports) | U1-a: increase; U1-b: no_change | short to medium | CR-4, CR-7a | as C-17 | A-3, A-10 |
| C-22 | `treasury` | `subsidy_outlay` (rate per tonne in years below Th 220, against a static projection: the rate on counterfactual prices per grade and the counterfactual mix of grades) | U1-a: increase; U1-b: no_change | short | RS-16 (1.0: per unit of quality), CR-6 (1.0), CR-9, CR-4 | the rate is computed from the national average over grades | A-3, A-5, A-9 |
| C-23 | `feed_buyers` | `price_paid` (feed barley, per tonne of a given grade) | U1-a: ambiguous; U1-b: no_change | short to medium | RS-16 (1.0: Unless; per unit of quality), RS-13, CR-6 (1.0), CR-12b | barley and feed wheat: `substitute` in feed and in land | A-4, A-5, A-20 |
| C-24 | `input_suppliers` | `quantity_traded` (wheat seed) | U1-a: increase; U1-b: no_change | short to medium | CR-9, LW-10 | seed `input_to` wheat | A-3, A-4 |
| C-25 | `owners.wheat_land` | `asset_value` (land with wheat history) | increase | short (from February 2027) | CR-7c, CR-10c, SB-4, EN-12 (U1-b), CR-12e (A-12, A-18; 1.1: every direction) | — | A-1, A-2, A-11, A-12, A-18 |
| C-26 | `owners.convertible_land` | `asset_value` (land that could grow wheat, without wheat history) | U1-a: increase; U1-b: no_change | short (from February 2027) | CR-7c, CR-7a, CR-10c | land: `substitute` between crops | A-11, A-13 |
| C-27 | `owners.wheat_land` | `subsidy_share_received` (against tenant growers) | increase | medium | CR-7b, DM-1 | lease: `contract` | A-14, A-15 |
| C-28 | `tenants` | `price_paid` (farmland rent, at lease renewal) | increase | medium | CR-6 (0.7: existing contracts), CR-7b | lease: `contract` | A-14, A-15 |
| C-29 | `wheat_growers` | `interest_rate` (farm borrowing) | decrease | medium | CR-7a, CR-7c | loans secured on income and land | A-16 |
| C-30 | `import_competing_industries` | `quantity_supplied` (−), `employment` (−), `hours_worked` (−) | U1-a: at_least_one_decrease; U1-b: no_change | medium | TX-8 (mirror), CR-9 (currency) | `currency` | A-3, A-17 |
| C-31 | `export_industries.other` | `quantity_supplied` (−), `employment` (−), `hours_worked` (−) | U1-a: at_least_one_decrease; U1-b: no_change | medium | TX-8 (mirror), CR-9 (currency) | `currency` | A-3, A-17 |
| C-37 | `input_suppliers` | `quantity_traded` (fertilizer and contract harvesting, all crops) | U1-a: ambiguous; U1-b: no_change | short to medium | CR-9, LW-10, CR-12b | inputs `input_to` wheat and barley | A-3, A-4, A-13 |
| C-40 | `treasury` | `subsidy_outlay` (net of repayments and fines, years below Th 220) | increase | short | CR-8 (1.0: receipts into the same budget), CR-12e (arithmetic) | — | A-1 |
| C-41 | `livestock_farmers` | `price_paid` (pasture rent) | U1-a: increase; U1-b: no_change | medium | CR-9, CR-7a, CR-6 (0.7: existing contracts) | land: `substitute` between wheat and grazing | A-13, A-15 |
| C-42 | `sellers.neighboring` | `quantity_traded` (grain sold into Brisklund to be declared as Brisklund harvest) | U1-a: increase; U1-b: no_change | short | CR-9, CR-5, CR-4 | grain `across_border` | A-6 |
| C-43 | `buyers.imports` | `price_paid` (imported goods, in thaler) | U1-a: decrease; U1-b: no_change | medium | CR-9 (0.7: the currency link), CR-6 | `currency` | A-3, A-17 |

**The world price and the response argument (C-17 to C-21).** Under U1-a, Brisklund's extra wheat, beyond a small rise in use at home, is exported (C-21; A-10: Brisklund exports in every year). By CR-6's 0.7 clause, the world price is not set by Brisklund, but it moves in the CR-6 direction by as much as Brisklund's extra exports matter, and by the 1.0 note it is signed even if small (C-17). Foreign growers receive less (C-18) and grow less (C-19). Their contraction is a response to the fall, and opposes it; CR-12e's response argument says it cannot reverse it. CR-12's 1.0 note says what the argument needs. (1) The total it bounds: world wheat output, Brisklund's and foreign together. (2) The cost premise: here the response is a contraction after a price fall, so the premise is the mirror of the 1.0 note's wording, which CR-12's 1.1 note (the response argument in every direction) now states: foreign growers' cost per tonne does not rise as they contract (the land they give up is their least productive, and their costs are not mainly fixed per farm; A-9). (3) Partial response: they cannot contract at once, since land and machinery are committed for the season. (4) A second response, stockholders buying while the price is lower, opposes the fall too. It is not within the total bounded (world output), so by CR-12's 1.1 note it is a second chain to combine; by the same argument it cannot reverse the fall (if the price were back at its old level, there would be no gain from storing). With A-9 the world price is `decrease`. Millers and feed users in Brisklund buy at the world-linked price, so theirs falls by the same small amount (C-20). Per RS-16's 1.0 note, it is signed per tonne of a given grade.

**The rate per tonne (C-22).** The rate is Th 220 less the national average farm-gate price, an average over all grades. Under U1-a two things lower that average. The world price falls a little (C-17), a price change. And the share of feed varieties rises (C-12), which lowers the average without any price per grade changing: by RS-16's 1.0 note, a change in mix is not a price change, but the formula counts it as one. Both raise the rate in years below the line, and the mix can carry a year whose prices per grade would put the average just above Th 220 below it, so that a payment is made where none would have been. This comparison is not with the counterfactual: without the Act there is no rate and no outlay, and against that the outlay rises from zero under both readings (C-1). It is with a static projection, the rate computed on the prices per grade and the mix of grades that would hold without the Act, as `tax_revenue_vs_static_projection` is for a tax (TX-9). C-22 is recorded with that qualifier: against the projection, the rate per tonne is higher under U1-a, and under U1-b neither the mix nor the world price moves, so the rate equals the projection (`no_change` against the projection, not against no Act). The size is unknown; the sign is derived (CR-4 on varieties, arithmetic on the formula).

**Barley (C-23).** Under U1-a, land moves from barley to wheat (C-11), which withdraws barley supply (RS-13, withdrawn: price up). More feed wheat is grown (C-12) and offered to the same feed buyers, which adds supply of a substitute (RS-13, added: price down). RS-16's Unless clause covers this case: the policy adds supply to the substitute's market, so the price is `ambiguous` without a premise. Barley is partly exported, so each effect may be small; each is signed (CR-6, 1.0). Signed per tonne of a given grade (RS-16, 1.0).

**Inputs (C-24, C-37).** Under U1-a, wheat area rises, on land taken from barley and rapeseed (C-11) and from pasture (C-26), so more wheat seed is sold (C-24; CR-9, LW-10). For fertilizer and contract harvesting across all crops the chains oppose: conversion of pasture and more intensive growing (A-3, A-13) raise them; the inputs no longer bought for the barley and rapeseed that wheat replaces lower them, and whether wheat takes more of them per hectare than barley needs a premise the case lacks. So the total is `ambiguous` (C-37; CR-12b). Under U1-b, nothing changes.

**Land (C-25 to C-28).** The payment's expected value attaches to land, the means that cannot move (CR-7b). Under U1-a, it raises the expected yield of any land that grows wheat: wheat land (C-25) and land that could be converted (C-26; A-13). Under U1-b, the right to payments attaches to each farm's established production, fixed for 2022 to 2026, before the Act became expected: EN-12's windfall case. Land with that history gains (C-25); land without it gains nothing (C-26, `no_change`), and there is no race to build history (EN-12; TS-5, 1.0: a line fixed before announcement). Values move from February 2027, when the bill was introduced with a majority (CR-10c; A-11). CR-7c's clause on a change of limited duration applies: the Act covers five crop years, plus the chance of renewal, so the value capitalizes only those years. The opposing chain, the slightly lower price in good years (C-5), is far smaller than the expected payment (A-18; CR-12e, arithmetic). Under U1-a, conversion of other land to wheat (C-26) is a response that cannot push the value of wheat land below its old level (CR-12e), with the premise that converting land does not get cheaper per hectare as more is converted (A-12).

**Capitalizing a contingent payment.** The yield capitalized is an expected payment: zero in most years, Th 40 a tonne in a year like the worst of the past decade. CR-7c and CR-10c say a durable asset's price reflects expected yields; here the expected yield depends on beliefs about the level and spread of future world prices. Land values therefore rise at announcement even if no payment is ever made, and while the Act runs they move with the expected world price: when futures rise above Th 220 the expected payment shrinks and land values fall back on whoever holds the land then (SB-4). An owner who bought at the capitalized price in 2027 and saw five good years paid for payments that never came: a loss by outcome, not by the policy as it stood when bought ((b) 2).

**Tenants (C-27, C-28).** Under both readings the payment goes to the holder, who on rented land is the tenant. Lease terms fixed before the Act count as regulated while they last (CR-6, 0.7: existing contracts), so tenants keep the payments until renewal. At renewal, landowners can ask for more, since the land now yields more and the tenants' labor and machinery could farm elsewhere (A-14); rents rise (C-28), and landowners receive more of the subsidy than its nominal recipients, the growers (C-27; DM-1, CR-7b). Under U1-b the established production belongs to the farm, not to the person whose output built it: a tenant who farmed the land in 2022 to 2026 and leaves it gets nothing.

**Pasture (C-41).** Under U1-a, convertible pasture is worth more growing wheat (C-26), so its owners ask livestock farmers who rent it for more, or convert it (CR-7a; A-13). Grazing leases fixed before the Act count as regulated while they last (CR-6, 0.7), so the rise comes at renewal (A-15).

**Neighboring sellers (C-42).** Under U1-a, a tonne declared as Brisklund harvest earns the payment in a low-price year. Some growers buy grain from neighbors across the border to declare as their own (C-13; A-6), so neighboring growers and traders sell more grain into Brisklund (CR-9, CR-5, CR-4). Under U1-b the base is fixed, and nothing is gained.

**Repayments, fines and the net outlay (C-39, C-40).** Repayments and fines go into the general budget that pays the outlay (CR-8, 1.0). The net is an increase by arithmetic (CR-12e): sampling covers about 3% of farms, so even if every sampled farm's whole payment were false, repayments and fines of up to three times the payment recovered would come to under a tenth of the outlay. The Act has no dedicated fund (CR-8, 1.1): both items are in the Consolidated Fund.

**Lenders (C-29).** Growers' income in low-price years is higher than it would have been (C-3, and under U1-a C-4), so the chance that they cannot repay is lower, and their land, the usual security, is worth more (C-25). Lenders compete for borrowers by rate (CR-7a): growers' rates fall (A-16).

**Currency (C-30, C-31).** Under U1-a, more wheat exports (C-21) give Brisklund's residents more foreign means; imports rise, and the exporters of other goods face the competition of wheat for foreign buyers' means (TX-8's mirror case; CR-9, currency; A-17). TX-8's mirror names an export subsidy; here the subsidy is on output and raises exports only through output, which the mirror case covers. Industries competing with imports and other exporters sell less, or employ fewer people or hours, as a group. Buyers of imports pay less in thaler (C-43; CR-9, 0.7: the currency link runs both ways). The transfer from taxpayers to growers moves spending between groups but does not by itself change spending on imports in a known direction (CR-4, a change in means alone): no chain.

Stopping points. The spending of growers' added income and of the group that pays (C-3, C-7): diffuse, depth 3, not followed to named uses. Livestock producers' output through feed prices: depth 3, and the feed price chain is ambiguous; stopped. Foreign governments' responses (Q5): no rule. Soil and water effects of more intensive wheat growing: out of scope.

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `wheat_growers`, `net_price_received` (expected at sowing), short to medium | Expected payment (about Th 7 to Th 8 a tonne). | Slightly lower world price in good years (C-5). | CR-12e, arithmetic on the case's figures (A-18). | U1-a **increase**; U1-b **no_change** (C-6). |
| `buyers.foreign`, `price_paid` (world), short to medium | Foreign growers contract; stockholders buy. | Brisklund's added exports. | CR-12e response argument with its 1.0 premises: world output as the total; foreign cost per tonne not rising as they contract (A-9); partial response. | U1-a **decrease**; U1-b **no_change** (C-17). |
| `feed_buyers`, `price_paid` (barley, per grade), short to medium | Land moved from barley. | More feed wheat offered. | None (RS-16 Unless). | U1-a **ambiguous**; U1-b **no_change** (C-23). |
| `owners.wheat_land`, `asset_value`, short | Expected payments (A-2). | Slightly lower price in good years; conversion of other land (U1-a). | CR-12e: arithmetic (A-18); response argument for conversion (A-12). | **increase** (C-25). |
| `wheat_growers`, `quantity_substitute` (hedges), short | — | The Act covers part of the price risk (A-7). | None needed. | **decrease** (C-14). |
| `wheat_growers`, `quantity_supplied` (milling wheat), short to medium | More wheat grown (C-9). | Switch to feed varieties (C-12; A-5). | None | U1-a **ambiguous**; U1-b **no_change** (C-38). |
| `input_suppliers`, `quantity_traded` (fertilizer, harvesting, all crops), short to medium | Conversion of pasture; more intensive growing (A-3, A-13). | Inputs no longer bought for barley and rapeseed (C-11). | None: inputs per hectare of wheat against barley are not in the case. | U1-a **ambiguous**; U1-b **no_change** (C-37). |
| `lobbying groups`, `lobbying_effort` (level and continuation of support), medium | Under the Act: lobbying to renew and raise the target. | On the counterfactual path: the farm-support campaign the Act settles for five years. | None (RS-7 Unless; CR-4 1.0, 1.1). | **ambiguous** (C-36). |
| Budget: outlay and repayments and fines, years below Th 220 | Outlay (C-1). | Repayments and fines (C-39). | Arithmetic (CR-12e): receipts under a tenth of the outlay. | Net outlay **increase** (C-40). |
| Split of the subsidy between growers and buyers | — | — | DM-1 with A-10: buyers' price is set in the world market and they have the world as an alternative; growers receive nearly all of it (C-4 against C-20). Within growers, land receives more than tenants (C-27). | Not a separate consequence; see C-4, C-20, C-27. |

**Final check** (`03_workflow.md`).
1. Uncombined chains: growers' expected price (C-6) combines the payment with the world-price chain; land (C-25) combines the payment with the world-price chain and conversion; the world price (C-17) combines Brisklund's exports with foreign contraction and stockholding; barley (C-23) combines withdrawn and added supply; milling wheat (C-38) combines more wheat with the switch to feed varieties; inputs across crops (C-37) combine conversion and intensity with the barley inputs given up; lobbying on support (C-36) is signed against the counterfactual campaign; the outlay is netted against repayments and fines (C-40). Per-year signs (C-1, C-2; C-4, C-5) are states of the world, not chains to combine.
2. Group signs: payers (C-7, C-8, C-34) and the currency chains (C-30, C-31) are groups. No member of a group is used as a chain elsewhere (CR-12, 1.1). No labor consequence is signed for a single member (CR-6, 1.1: labor demand as a group).
3. Baseline: every sign is against no Act, except C-22, which is recorded against a static projection and says so in its qualifier (as TX-9's variable does for a tax); against no Act the outlay is C-1. SB-10's domestic-price conclusion is not used (its conditions are not met). U1-b's `no_change` signs are against the counterfactual, not against U1-a. Lobbying on the target and extension is signed against the counterfactual campaign (C-36), not as a new question.
4. Worse off is not poorer: the payers (C-7, C-8) pay sums they cannot avoid; growers' means rise in low-price years (C-3), netted against the world-price effect first (CR-4, 1.1). Buyers abroad are not signed on their means.
5. Timing: no action is moved in time by the Act (the rate depends on the year's national average, not on when a grower sells). The contingency is per year, recorded per state of the world.
6. Both sides of every transfer: the state pays (C-1) and growers receive (C-3); the payers (C-7, C-8); landowners take part through rents (C-27, C-28) and pasture rents (C-41); repayments and fines (C-39) and the net (C-40); administration (C-33, C-34).
7. Every actor class, every core rule: CR-7c for wheat land, convertible land and tenancies; CR-7a for pasture; CR-6 for world, domestic and barley prices; CR-9 along the currency link to both sides (C-30, C-31, C-43) and across the border for declared grain (C-42); enforcement and compliance costs recorded (C-16, C-33).
8. Unstated premises: the response argument's premises (A-9), the registration chain under U1-b (A-19, below the cut-off), lenders (A-16), organizing (A-8), detection (A-21).
9. Baseline of every pattern (1.0): SB-2 (1.1) is against no subsidy, with its wider-market clause; SB-3, RS-6 (mirror, 1.1), RS-16, RS-13, TX-8 (mirror), EN-12 (U1-b) and SB-4 are against no Act. RS-7 (1.1) signs only provisions that exist only under the Act as new; the target and extension are the contested question. DM-1 compares shares by definition. RS-11 gives only a chain below the cut-off. RS-16 exposed the mix effect in C-22, whose comparison is a projection, recorded as such. Of the other 1.1 changes, PC-20, PC-1 and PC-16 do not apply (no price is capped); SB-4's clause on alternatives does not apply (the Act changes no other asset's return); SB-8, TX-1, TX-7, TX-9's Unless, EN-14, RS-23, RS-17, EN-13, PC-17 and RS-24 do not arise.

## 8. Time structure

- **10 February 2027: announcement.** Land values move (C-25, C-26), partly then and the rest at enactment in June. Under U1-b, established production was fixed in 2026, so nothing can be done to qualify (EN-12; TS-5, 1.0): no race.
- **Autumn 2027: first sowing under the Act.** Under U1-a, sowing decisions for the 2028 crop respond (C-9, C-11, C-12). Growers buy less price cover for 2028 (C-14).
- **2028 to 2032: each crop year.** Whether anything is paid depends on the year's world price (C-1, C-2). In each low-price year, the payment is computed after the marketing year and paid in December, so growers receive it up to 16 months after sowing. Under U1-a, overstated declarations appear in low-price years (C-13). Leases signed before February 2027 are renewed at higher rents as they end (C-28), most within the term (A-15).
- **2032: review.** Lobbying peaks (C-15, C-36). If renewal looks unlikely, land values fall back toward their old level on whoever holds the land (SB-4). Under U1-a, wheat area moves back toward other crops in the first sowing after the Act ends; capacity added for wheat (drying, storage) stays (TS-6, if repealed).

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-32 | `taxpayers`, recipients of other spending, future taxpayers | `resources_available_other_uses` (what the payments would otherwise have funded) | at_least_one_decrease | Other spending, lower taxes or less borrowing, in years below Th 220; recorded as C-7 and C-8 and not counted again. | OC-1, CR-8a |
| C-33 | `officials.enforcement` (payments office) | `enforcement_cost` | increase | About Th 4 million a year of staff and checks. | OC-3, CR-8c |
| C-34 | `taxpayers`, recipients of other spending, future taxpayers | `resources_available_other_uses` (administration, every year) | at_least_one_decrease | What the Th 4 million a year would otherwise have funded. | OC-3, OC-1, CR-8 (0.7) |
| C-35 | `wheat_growers` | `quantity_supplied` (other uses of the land and inputs drawn into wheat) | U1-a: decrease; U1-b: no_change | Barley, rapeseed and pasture output given up for wheat (as C-11 and C-26); not counted again. | SB-3, CR-8a |

Growers' time on claims is C-16. Prevented exchanges: none; the Act prevents no exchange. Under U1-a, the resources drawn into wheat (C-11, C-24, C-35) produce wheat that is exported at a world price slightly lower than it would have been, while what they would otherwise have produced is not produced: the seen harvest against the unseen barley and pasture (SB-3).

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | The Act is in force for 2028 to 2032 and payments are made as it provides. | enforcement | 0.9 | Enacted; open-ended appropriation; payments office set up. | C-1, C-3 to C-8 and everything downstream fail. |
| A-2 | The national average price falls below Th 220 in at least one of the five crop years. | other | 0.85 | Four of the past ten years; 2028 futures at Th 228 with wide spread. | C-8 is not reported; C-25 shrinks (the expected payment remains positive). |
| A-3 | Some growers at the margin sow more wheat, or grow it more intensively, when the expected price including the payment rises. | substitutability | 0.85 | Crop rotations; past responses of wheat area to price. | Under U1-a, C-5, C-9 to C-11, C-17 to C-24, C-30, C-31, C-37, C-38, C-43 are not reported. |
| A-4 | Land can be moved between wheat and other crops from year to year. | alternative_uses | 0.9 | Rotations; soil suitability. | C-11 and C-23 are not reported. |
| A-5 | Some growers switch to high-yield feed varieties when every tonne is paid alike. | other | 0.6 | Yield gap 0.6 t/ha against a premium of Th 18; seed sales by variety. | C-12 is not reported; C-22 rests on the world-price chain alone; C-23 loses its (−) chain and becomes `increase` under U1-a; C-38 becomes `increase` under U1-a. |
| A-6 | Declarations are checked only by sampling, so some growers overstate or declare bought grain as their own. | enforcement | 0.55 | 3% sampled; grain moves freely across borders. | C-13, C-39, C-42 are not reported. |
| A-7 | Some growers who now buy put options or forward sales for price cover buy less. | substitutability | 0.7 | Hedging use by larger growers. | C-14 is not reported. |
| A-8 | Farm unions, millers and holders of established production can organize at a cost below their stakes. | other | 0.9 | Existing unions; the 2025 to 2026 campaign. | C-15 is not reported; C-36 loses its (+) chain. |
| A-9 | Foreign growers' cost per tonne does not rise as their output contracts (the land given up is the least productive; costs are not mainly fixed per farm), and they cannot contract at once. | other | 0.85 | Structure of world wheat costs; seasonal commitment of land. | C-17's response argument gives only "not above the old level"; C-17 to C-20 and C-22's world-price part become `decrease or no change`. |
| A-10 | The domestic farm-gate price follows export parity in every year (Brisklund exports in every year). | other | 0.9 | Exports of 1.5 Mt in each of the past ten years. | C-20 and C-21 change: with no exports in a year, the domestic price would be set at home and fall more. |
| A-11 | Land buyers expected the Act from February 2027 and expect it to run its term, with some chance of renewal. | expectations | 0.8 | Government majority; land market reports. | C-25 and C-26 move later or less. |
| A-12 | Wheat land with history is in fixed supply in the short run, and converting other land to wheat does not get cheaper per hectare as more is converted. | durability | 0.8 | Soil limits; the cost of draining and liming pasture. | C-25's response argument gives only "not below the old level". |
| A-13 | Some pasture or other land can be converted to wheat. | alternative_uses | 0.7 | Land-use surveys. | C-26 and C-41 under U1-a are not reported; C-37 loses part of its (+) chain. |
| A-14 | Land has fewer alternatives than tenants' labor and machinery, and leases are let competitively. | substitutability | 0.7 | Tenancy market; contractors farm across districts. | C-27 is not reported; C-28 rests on CR-6 alone. |
| A-15 | Most leases come up for renewal within the five-year term. | durability | 0.85 | Three- to five-year leases. | C-27, C-28 and C-41 shrink and come later. |
| A-16 | Lenders lower rates to wheat growers whose income in low-price years is now higher. | other | 0.6 | Banks' farm-risk models; land as security. | C-29 is not reported. |
| A-17 | The rise in wheat exports is not offset by capital flows in the medium run. | other | 0.55 | Floating exchange rate; capital account. | C-30, C-31 and C-43 are not reported. |
| A-18 | The effect of Brisklund's added output on the world price is far smaller than the expected payment per tonne. | other | 0.9 | Added output of a few percent of 4 Mt against world output of 800 Mt; expected payment Th 7 to Th 8. | C-6 and C-25 become `ambiguous` under U1-a; C-3's netting needs another premise. |
| A-19 | Under U1-b, some land that would have left farming is kept registered, and some of it grows wheat. | other | 0.35 | Land leaving farming goes mostly to building, worth far more than five years of payments. | Below the cut-off: C-9 to C-11 stay `no_change` under U1-b; if true, they would be small increases (RS-11). |
| A-20 | Feed buyers substitute between feed wheat and feed barley of a given quality. | substitutability | 0.7 | Feed rations; compounders' practice. | C-23 loses its (−) chain and becomes `increase` under U1-a. |
| A-21 | The payments office's sampling finds some false declarations, and repayments and fines are collected. | enforcement | 0.7 | 3% of farms sampled each year; harvest declarations can be checked against deliveries. | C-39 is not reported; C-40 equals C-1. |

## 11. Report

**The policy.** For the wheat harvests of 2028 to 2032, Brisklund pays growers the gap between Th 220 a tonne and the national average market price, whenever that price is lower. The money comes from the general budget. The world market sets Brisklund's wheat price. It is unclear whether the payment is on each farm's actual harvest or on a fixed base of its output in 2022 to 2026.

**Visible consequences.** In years when the price is below Th 220, the state pays (C-1) and growers receive (C-3), and those who pay are taxpayers, recipients of other spending or future taxpayers (C-7; over the term, C-8). In other years, nothing is paid (C-2).

**Invisible consequences.**
- *Land.* The value of wheat land rises from the announcement (C-25), even if no payment is ever made, because the payment is expected; it moves with expected world prices. Rents rise as leases are renewed (C-28), so landowners receive more of the subsidy than the growers it names (C-27). Lenders charge growers less (C-29).
- *Hedging and administration.* Growers buy less price cover (C-14), spend time on claims (C-16), and the payments office costs money every year (C-33, C-34).
- *Lobbying.* On the formula and U1, which exist only under the Act, lobbying rises (C-15). On the target at review and extension, which is the farm-support question that would have been contested anyway, the method cannot say whether lobbying is more or less than without the Act (C-36).

**Per reading of U1.**
- *If payments are on actual output (U1-a):* each tonne earns at least Th 220 in a bad year (C-4), and growers' expected price at sowing rises (C-6). More wheat is grown (C-9) by more farms (C-10), less barley and rapeseed (C-11), with more high-yield feed varieties (C-12); some declarations are overstated (C-13), partly with grain bought from neighbors (C-42), and some are caught and repaid with fines (C-39; net outlay, C-40). Milling wheat may rise or fall (C-38). The extra wheat is exported (C-21) and lowers the world price by a small amount (C-17): buyers abroad and at home pay a little less (C-17, C-20), foreign growers receive and grow less (C-18, C-19), and Brisklund's growers receive a little less in good years (C-5). The national average price falls through the mix of grades as well as the world price, which raises the rate paid above what a static projection on the counterfactual prices per grade would give (C-22). More wheat seed is sold (C-24); fertilizer and harvesting across all crops may rise or fall (C-37). Land that could be converted to wheat gains value (C-26), and livestock farmers pay more for pasture (C-41). Through the currency, other industries sell less (C-30, C-31), and imports cost less in thaler (C-43). The price of feed barley may rise or fall (C-23).
- *If payments are on a fixed base (U1-b):* the payment is a sum per farm that does not change what anyone grows: output, varieties, prices, trade and declarations are unchanged (`no_change` throughout). Its value is a windfall to land with a 2022 to 2026 history (C-25), not to land without one (C-26), and there is no race to build history.

**Ambiguous effects.** Under U1-a: the price of feed barley (C-23), milling wheat (C-38), fertilizer and harvesting across crops (C-37). Under both readings: lobbying on the target and extension (C-36).

**Key conditions.** That payments are made (A-1) and at least one year falls below the line (A-2, p = 0.85); under U1-a, that growers respond at the margin (A-3, p = 0.85) and that foreign growers' costs do not rise as they contract (A-9); that the world-price effect is small against the payment (A-18).

**What this analysis cannot say.** How much is paid in any year or in total; how much land values rise; how large the world-price effect is; whether the policy is desirable; soil, water and nutrition (out of scope).

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | treasury | subsidy_outlay (years below Th 220) | increase | short | visible | B | SB-1, CR-8b | A-1 |
| C-2 | treasury | subsidy_outlay (years at or above Th 220) | no_change | short | visible | A | CR-1, CR-8 | none |
| C-3 | wheat_growers | resources_available_other_uses (years below Th 220) | increase | short | visible | B | SB-1, CR-8b, CR-4 | A-1, A-18 |
| C-4 | wheat_growers | net_price_received (per tonne, years below Th 220) | U1-a: increase; U1-b: no_change | short | visible | B | SB-2, CR-5c, CR-1 | A-1 |
| C-5 | wheat_growers | net_price_received (per tonne, years at or above Th 220; small) | U1-a: decrease; U1-b: no_change | short | invisible | B | CR-6, CR-9 | A-3, A-9, A-10 |
| C-6 | wheat_growers | net_price_received (expected at sowing) | U1-a: increase; U1-b: no_change | short–medium | invisible | B | SB-2, CR-10a, CR-12e | A-1, A-18 |
| C-7 | taxpayers, recipients of other spending, future taxpayers | resources_available_other_uses (years below Th 220) | at_least_one_decrease | short | invisible | B | SB-1, OC-1, CR-8 | A-1 |
| C-8 | taxpayers, recipients of other spending, future taxpayers | resources_available_other_uses (whole period) | at_least_one_decrease | whole period | invisible | B | CR-8, CR-12 | A-1, A-2 |
| C-9 | wheat_growers | quantity_supplied (wheat) | U1-a: increase; U1-b: no_change | short–medium | invisible | B | SB-2, CR-4 | A-3 |
| C-10 | wheat_growers | number_of_sellers (farms growing wheat) | U1-a: increase; U1-b: no_change | medium | invisible | B | RS-6, CR-4 | A-3 |
| C-11 | wheat_growers | quantity_substitute (barley, rapeseed grown) | U1-a: decrease; U1-b: no_change | short–medium | invisible | B | SB-3, CR-4 | A-3, A-4 |
| C-12 | wheat_growers | product_attribute (share of high-yield feed varieties) | U1-a: increase; U1-b: no_change | short–medium | invisible | B | CR-4, RS-16 | A-5 |
| C-13 | wheat_growers | legal_breach (overstated declarations) | U1-a: increase; U1-b: no_change | short | invisible | B | RS-3, RS-5, CR-4 | A-6 |
| C-14 | wheat_growers | quantity_substitute (price hedges bought) | decrease | short | invisible | B | RS-1 | A-7 |
| C-15 | lobbying groups | lobbying_effort (provisions that exist only under the Act: the rate's average, U1) | increase | medium | invisible | B | RS-7, CR-4, CR-12 | A-8 |
| C-16 | wheat_growers | compliance_cost (claims, declarations) | increase | short | invisible | A | OC-2, CR-8c | none |
| C-17 | buyers.foreign | price_paid (world wheat; small) | U1-a: decrease; U1-b: no_change | short–medium | invisible | B | CR-6, CR-9, CR-12e | A-3, A-9 |
| C-18 | sellers.foreign | net_price_received (wheat; small) | U1-a: decrease; U1-b: no_change | short–medium | invisible | B | CR-6, CR-9 | A-3, A-9 |
| C-19 | sellers.foreign | quantity_supplied (wheat; small) | U1-a: decrease; U1-b: no_change | medium | invisible | B | CR-4, CR-7a | A-3, A-9 |
| C-20 | buyers.current | price_paid (wheat of a given grade, Brisklund; small) | U1-a: decrease; U1-b: no_change | short–medium | invisible | B | CR-6, RS-16 | A-3, A-9, A-10 |
| C-21 | grain_exporters | quantity_traded (wheat exports) | U1-a: increase; U1-b: no_change | short–medium | invisible | B | CR-4, CR-7a | A-3, A-10 |
| C-22 | treasury | subsidy_outlay (rate per tonne in years below Th 220, against a static projection) | U1-a: increase; U1-b: no_change | short | invisible | B | RS-16, CR-6, CR-9, CR-4 | A-3, A-5, A-9 |
| C-23 | feed_buyers | price_paid (feed barley, per grade) | U1-a: ambiguous; U1-b: no_change | short–medium | invisible | B | RS-16, RS-13, CR-6, CR-12b | A-4, A-5, A-20 |
| C-24 | input_suppliers | quantity_traded (wheat seed) | U1-a: increase; U1-b: no_change | short–medium | invisible | B | CR-9, LW-10 | A-3, A-4 |
| C-25 | owners.wheat_land | asset_value (land with wheat history) | increase | short | invisible | B | CR-7c, CR-10c, SB-4, EN-12, CR-12e | A-1, A-2, A-11, A-12, A-18 |
| C-26 | owners.convertible_land | asset_value (land without wheat history) | U1-a: increase; U1-b: no_change | short | invisible | B | CR-7c, CR-7a, CR-10c | A-11, A-13 |
| C-27 | owners.wheat_land | subsidy_share_received (against tenant growers) | increase | medium | invisible | B | CR-7b, DM-1 | A-14, A-15 |
| C-28 | tenants | price_paid (farmland rent at renewal) | increase | medium | invisible | B | CR-6, CR-7b | A-14, A-15 |
| C-29 | wheat_growers | interest_rate (farm borrowing) | decrease | medium | invisible | B | CR-7a, CR-7c | A-16 |
| C-30 | import_competing_industries | quantity_supplied (−), employment (−), hours_worked (−) | U1-a: at_least_one_decrease; U1-b: no_change | medium | invisible | B | TX-8, CR-9 | A-3, A-17 |
| C-31 | export_industries.other | quantity_supplied (−), employment (−), hours_worked (−) | U1-a: at_least_one_decrease; U1-b: no_change | medium | invisible | B | TX-8, CR-9 | A-3, A-17 |
| C-32 | taxpayers, recipients of other spending, future taxpayers | resources_available_other_uses (what the payments would have funded; as C-7, C-8) | at_least_one_decrease | short | invisible | B | OC-1, CR-8a | A-1 |
| C-33 | officials.enforcement (payments office) | enforcement_cost | increase | short–medium | invisible | A | OC-3, CR-8c | none |
| C-34 | taxpayers, recipients of other spending, future taxpayers | resources_available_other_uses (administration) | at_least_one_decrease | short–medium | invisible | A | OC-3, OC-1, CR-8 | none |
| C-35 | wheat_growers | quantity_supplied (other output given up for wheat; as C-11) | U1-a: decrease; U1-b: no_change | short–medium | invisible | B | SB-3, CR-8a | A-3, A-4 |
| C-36 | lobbying groups | lobbying_effort (level and continuation of support: target at review, extension) | ambiguous | medium | invisible | B | RS-7, CR-4, CR-12b | A-8 |
| C-37 | input_suppliers | quantity_traded (fertilizer and contract harvesting, all crops) | U1-a: ambiguous; U1-b: no_change | short–medium | invisible | B | CR-9, LW-10, CR-12b | A-3, A-4, A-13 |
| C-38 | wheat_growers | quantity_supplied (milling wheat) | U1-a: ambiguous; U1-b: no_change | short–medium | invisible | B | CR-4, CR-12b | A-3, A-5 |
| C-39 | treasury | non_tax_receipts (repayments and fines) | U1-a: increase; U1-b: no_change | short–medium | invisible | B | CR-8b, CR-1 | A-6, A-21 |
| C-40 | treasury | subsidy_outlay (net of repayments and fines, years below Th 220) | increase | short | invisible | B | CR-8, CR-12e | A-1 |
| C-41 | livestock_farmers | price_paid (pasture rent) | U1-a: increase; U1-b: no_change | medium | invisible | B | CR-9, CR-7a, CR-6 | A-13, A-15 |
| C-42 | sellers.neighboring | quantity_traded (grain sold into Brisklund to be declared) | U1-a: increase; U1-b: no_change | short | invisible | B | CR-9, CR-5, CR-4 | A-6 |
| C-43 | buyers.imports | price_paid (imported goods, in thaler) | U1-a: decrease; U1-b: no_change | medium | invisible | B | CR-9, CR-6 | A-3, A-17 |

## Corrections after the core-only comparison

The core-only re-run (`05_examples_core/WE-065_crop_deficiency_payments_core.md`) was compared with this analysis. Each correction below was checked against the core rules before it was applied; the catalog is now 1.1.

**Changed.**
- C-15: narrowed to the provisions that exist only under the Act (which average sets the rate; U1), still `increase`. The target at review and extension beyond 2032 are the farm-support question that was contested on the counterfactual path, so by RS-7's Unless clause and CR-4's 1.0 and 1.1 notes (the same question is the policy field, not the provision) they are signed against that contest: new C-36, `ambiguous` (comparison, cause P).
- C-22: re-qualified as against a static projection (the rate on counterfactual prices per grade and mix), as TX-9's variable is for a tax. Against no Act the outlay rises from zero under both readings (C-1); the U1-b `no_change` holds only against the projection, and now says so (comparison, cause E against this version).
- C-24: narrowed from all inputs to wheat seed, which rises with wheat area; the aggregate needed a premise on inputs per hectare of wheat against barley that the case lacks. The aggregate is new C-37, `ambiguous` under U1-a. The comparison's narrower key (feed-variety seed only) was widened to all wheat seed, which the rise in area (C-10, C-11, C-26) gives directly.
- C-3: netted against the world-price effect before signing (CR-4, 1.1: several changes in means); sign unchanged.
- C-17, C-25: cite CR-12's 1.1 note (the response argument in every direction), which now states the mirror cost premise used here; stockholding in C-17 is a second chain outside the total bounded (CR-12, 1.1).
- C-10 cites RS-6 (1.1: mirror). Section 2 cites SB-2's 1.1 clause (a good priced in a wider market), which now states what (c) 1 asked for.
- Sections 3 to 11, the final check (with item 9 and the 1.1 changes), assumption "if false" entries (A-3, A-5, A-6, A-8, A-13, A-15, A-17) and the report updated to match.

**Added.** C-36 (lobbying on the level and continuation of support, `ambiguous`), C-37 (fertilizer and contract harvesting across crops, U1-a `ambiguous`), C-38 (milling wheat, U1-a `ambiguous`; core C-9), C-39 (repayments and fines, U1-a increase; core C-12, with the detection premise A-21), C-40 (outlay net of repayments and fines, increase by arithmetic; CR-8 1.0), C-41 (pasture rents, U1-a increase; core C-21), C-42 (neighboring sellers' grain sold into Brisklund to be declared, U1-a increase; core C-30), C-43 (import prices in thaler, U1-a decrease; core C-34). New actor classes `livestock_farmers`, `sellers.neighboring`, `buyers.imports`; new assumption A-21.

**Removed.** None.

**Comparison conclusions rejected or not applied.**
- Core C-8 (feed wheat increases, cause J): not added; it is implied by C-9 and C-12 and adds no sign.
- Core C-11 (grain bought abroad as its own key, cause J): not added as a growers' key; 1.1 does not settle it, and the purchase stays inside C-13, while the sellers' side is now C-42.
- Core C-17 (conversion investment, cause J): not added; its effects are C-26, C-35 and C-41, and 1.1 does not settle it.
- Core C-29 (sellers of price cover sell less, cause J): not added; 1.1 does not settle it.
- Core C-32 (exchange rate, cause J): not added; it stays a link in C-30, C-31 and C-43.
- Core C-35 (growers without established production, cause J): not added; 1.1 does not settle the split, and C-3 is per state of the world for all growers.
- Pattern C-2 (per-state `no_change`, cause J): kept; the comparison found it true by the formula.

## Gaps found

**(a) Calculus gaps (a step no core rule covers).** None. Every step was derived from CR-1 to CR-12.

**(b) Unclear core rules.**
1. *CR-8 0.8, contingent payers, when the contingency is a state of the world each year.* The clause says to record payers "per reading or with a premise on the contingency". Here the contingency is not a reading and not a single premise: it recurs each year with a price no one controls. It was recorded as signs per state of the world (years below and at or above the line: C-1, C-2, C-7) plus a whole-period sign with a premise (C-8; CR-12 0.7). That worked, but neither CR-8 nor the ontology names per-state signs; the analogy with per-window timing signs had to be drawn by hand ((d) 1).
2. *CR-7c and CR-10c, capitalizing a contingent payment.* CR-7c is written for a change in expected yield, and "becomes expected" is about the measure. Here the yield itself is a probability-weighted payment: the land's value moves at announcement, then keeps moving with expected world prices and their spread while the Act runs, and an owner can lose by outcome on a payment that never came. Derivable, but CR-7c does not say that the expected yield of a contingent payment depends on beliefs about the contingency, so that the asset's value moves with them.
3. *CR-12 1.0, what the response argument needs, after a price fall.* The 1.0 note is worded for a price rise ("cost per unit does not fall as the activity contracts"). For the world price, which falls, the needed premise is the mirror: foreign growers' cost per tonne does not rise as they contract (A-9). With fixed costs per farm, contraction could raise cost per tonne and push the price back. Worked with that reading; the note should state both directions.
4. *CR-4, a change in means alone, for a transfer that is also conditional on a status.* Under U1-b, the payment is a lump sum (no marginal effect on output) and a reward for keeping the farm registered (operation 3 on leaving farming). CR-1's 0.9 note on operations per range covers a provision that does different things on either side of a threshold; here one provision is operation 4 for growing and operation 3 for registration. Recorded both (section 2), but CR-1 could say so.

**(c) Missing or wrong patterns.**
1. *SB-2 has no clause for a good priced in a wider market.* Applied as written, its "price paid by buyers decreases and/or net price received increases" is right but uninformative, and its "quantity traded increases" does not say which market (domestic use barely changes; output and exports rise). CR-6's 0.7 and 1.0 clauses had to be imported to say that growers receive nearly all of it and that buyers' price falls only by the small world-price effect. EN-6 has a wider-market Unless clause; SB-2 should have the mirror.
2. *SB-10 does not apply, and nothing says so.* SB-10's domestic-price conclusion (rising toward the export price plus the subsidy) would be wrong here: a subsidy on all output gives no reason to move sales abroad. Its If clause ("a fixed sum per unit of a good exported") excludes the case, so no sign had to be overridden; but a reader looking for "subsidy on a traded good" finds SB-10 first. A sentence in SB-2 or SB-10 would help: "a subsidy paid on all output of a good priced in a wider market raises output and exports and lowers the world price; it does not raise the domestic price."
3. *A payment counted in physical units lowers value per unit (the mirror of RS-21).* RS-21 says a cap counted in tonnes raises the value per tonne. A payment counted in tonnes does the reverse: growers choose higher-yield, lower-value varieties (C-12). RS-21's derivation (CR-4 with the unit of the constraint) covers both, but its If clause names only caps and rights. Proposed as a candidate pattern: "a payment or charge counted in physical units shifts the mix toward more units of lower value per unit (or the reverse for a charge)", derivation CR-4 with the unit of the payment.
4. *A formula that reads a mix change as a price change.* The rate is computed from an average over grades, so a shift in mix raises the outlay with no change in any price per grade (C-22). RS-16's 1.0 note ("a change in the mix is not a price change") is what exposed it, but no pattern covers payments indexed to an average price. Seen once.
5. *DM-1 for a subsidy where one side is a world market.* DM-1 worked: buyers' alternative is the world market, so growers receive nearly all. It needed no premise beyond A-10, because CR-6 0.7 gives the comparison of alternatives directly. No sign overridden.
6. No other pattern gave a sign I had to override.

**(d) Vocabulary.**
1. *Signs per state of the world.* The ontology has per-reading signs and per-window timing signs, but no per-state sign for a consequence that holds only in years when a market price is below a line. Recorded as separate consequences with the state in the variable's qualifier (C-1, C-2, C-4, C-5). A field like `state: price below 220 | price at or above 220` would make these comparable with outcome cards.
2. *Subsidy outlay against a projection.* `tax_revenue_vs_static_projection` has no counterpart for outlays; the feedback through the mix and the world price (C-22) would be cleanly recorded as `subsidy_outlay_vs_static_projection` increase.
3. *Price cover.* No variable for insurance or hedging bought; `quantity_substitute` with a qualifier was used (C-14).

**(e) Test of 1.0.**
- *SB-2 and SB-10 (a subsidy on output when the price is set in a wider market).* SB-2 needed interpretation: it had to be read with CR-6's wider-market clause ((c) 1). SB-10 correctly did not apply; its conditions exclude the case, but its conclusion would have given a wrong domestic price if applied by resemblance ((c) 2).
- *CR-6 1.0, small effects are signed.* Worked as written, and mattered: signing the small world-price fall (C-17) gave three consequences a supporter would not expect, a lower price to growers in good years (C-5), a slightly lower price to domestic buyers (C-20) and a higher rate per tonne through the formula (C-22).
- *CR-8 0.8, contingent payers (payments occur only when prices fall).* Worked, with interpretation: per-state signs and a whole-period sign with a premise ((b) 1). CR-8's 1.0 clauses (receipts into the same budget; statutory rights) did not arise: the Act has no receipts.
- *CR-7c (land values; capitalization of a contingent payment).* Worked as written for the timing of capitalization (from announcement), the limited duration (five years plus renewal) and who captures it (owners at announcement; landowners at lease renewal against tenants, with CR-6 0.7 on existing contracts). Needed interpretation on the expected yield of a contingent payment ((b) 2).
- *RS-16 1.0 (prices per unit of quality; Unless clause).* Worked as written: prices signed per grade (C-20, C-23), the barley price `ambiguous` under the Unless clause (C-23), and the per-quality note exposed that the payment formula counts a mix change as a price change (C-22; (c) 4).
- *EN-12 (if paid on a historical base).* Worked as written under U1-b: base fixed before the announcement, so a windfall to land with history and no race (C-25, C-26; TS-5 1.0 agrees). It needed one addition: the history belongs to the farm, not to the person whose output built it, so a former tenant gets nothing and the landowner captures it at renewal (section 6).
- *CR-12 1.0, what the response argument needs.* Worked, with the mirror reading of the cost premise for a price fall ((b) 3); the total bounded (world output) and the second response (stockholding) were stated as the note asks (C-17). Also used for land against conversion (C-25, A-12).
- *CR-12 1.0, the baseline of patterns.* Worked: every pattern cited was checked against no Act; none compared with another policy except DM-1, which compares shares by definition.
- *CR-12 0.8, kind 2 below the cut-off.* Worked as written for the registration chain under U1-b (A-19): the derived `no_change` stands.
- *CR-12 1.0, tiers and dominance.* Arithmetic dominance (A-18) settled C-6 and C-25 without changing their tier. Worked as written.
- *TX-8 1.0 (mirror case).* Worked with interpretation: the mirror names an export subsidy; here exports rise through output, which the same derivation (CR-9, currency) covers (C-30, C-31). Under U1-b there are no added exports, so `no_change`.
- *RS-7 1.0 and CR-4 1.0, lobbying against a contested counterfactual.* Worked as written: lobbying for support as such is not signed; questions that exist only under the Act are (C-15).
- *Readings against the counterfactual (02_ontology.md, 2.5).* Under U1-b, most consequences are `no_change`, which the derivation establishes (the marginal return is unchanged, CR-4), not merely fails to sign. Worked as written.
- *Candidates from 06_gaps.md, 6.2e.* None of the listed candidates was needed. A new candidate is proposed ((c) 3: a payment counted in physical units lowers value per unit).
- Re-run note: the core-only comparison contradicted two verdicts recorded above as "worked as written": RS-7 1.0 and CR-4 1.0 on lobbying (the target at review and extension are the contested farm-support question, not new ones; C-36 is now `ambiguous`), and RS-16 1.0 as used for C-22 (the mix effect was compared with a static projection, not with no Act; C-22 is now qualified as a projection claim). It also found the aggregate input claim (C-24) resting on an unstated premise.
