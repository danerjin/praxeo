# WE-014 / Analysis: Calvar Sugar Market Act (import quota with free tradable quota rights)

Analyst: core-only re-run (Handbook 0.4)  |  Rules: core rules CR-1 to CR-12 only  |  Status: awaiting comparison

Every derivation below cites only the core rules (CR-1 to CR-12, with clause), the foundations (AX-1, LW-1 to LW-10) and arithmetic. Assumptions A-1 to A-19 are the case assumptions as given; A-N1 and A-N2 are premises this re-run had to add.

## 1. Policy record

| Field | Value | Source sentence |
|---|---|---|
| Jurisdiction (and what lies just outside) | The Republic of Calvar, about 20 million people. Its only land neighbor, Ostria, has no sugar quota; the border town of Varnholt (150,000 people) is 20 minutes from Ostrian supermarkets; Calvar's main cities are 200 km or more from the border. | Policy record preamble. |
| Announced / enacted / effective / expires | Bill introduced with government backing nine months before the effective date; passed four months later; no expiry, but parliament must review the quota after five years. | "The bill was introduced with government backing nine months before the effective date and passed four months later." |
| Enforcement (who, penalties, resources) | Customs service: imports without quota rights seized and fined three times their value; bulk cargo only through Quellport and Varo, every shipment inspected; Varnholt land crossing checked by sample; funded from the general budget. | K3. |
| Starting conditions | Use about 1.2 million tonnes a year; four beet factories make about 450,000 tonnes from domestic beet; about 750,000 tonnes imported, mostly raw cane refined by two port refineries at Quellport and Varo. World prices below most Calvarian growers' costs for years. Corn syrup made from domestic corn by two wet mills. | Policy record preamble. |

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Import quota | `quota` | Imports of raw and refined sugar, and of mixtures containing more than 65% sugar by weight | Importers | 350,000 tonnes a year from the effective date. No expiry, but parliament must review the quota after five years. | Sugar contained in finished foods; mixtures with 65% sugar or less; a travelers' personal allowance of 10 kg per crossing. Corn syrup and other sweeteners are not covered. |
| K2 Quota rights | Allocation of K1 (part of K1) | Shares of the annual quota | Importers | Shares allocated free, in proportion to each importer's sugar imports over the 36 months before the effective date. Shares are permanent and may be sold or leased; transfers are registered with customs. | None |
| K3 Enforcement | Enforcement | K1, K2 | Customs service | Imports without quota rights are seized and fined three times their value. Bulk cargo may enter only through Quellport and Varo, where every shipment is inspected; the land crossing at Varnholt is checked by sample. Funded from the general budget. | None |

Existing rules: none recorded in the input.

Unclear provisions: whether the 65% threshold counts sugar against dry weight or total weight. Assumed total weight, the reading more favorable to importers of syrups and blends. Recorded here as U1: U1-a, total weight; U1-b, dry weight.

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | Core rules applied |
|---|---|---|---|
| K1 | Triangular (prohibits exchanges between Calvarian buyers and foreign sellers beyond the quota) | Binds from the first year, more tightly as demand grows (A-1); enforced at the ports (A-2) | CR-1 op 1, CR-4, CR-5a, CR-6 (quantity fixed, price free), CR-7, CR-9 |
| K2 | Transfer of a valuable right to past importers (free allocation) | Valuable as long as K1 binds (A-1) and is expected to last (A-5) | CR-1 op 2 and op 4, CR-5c, CR-7b, CR-7c, CR-10a, CR-10c |
| K3 | Enforcement | Strong at the ports (A-2); weak by sample at Varnholt, but the 10 kg allowance makes small cross-border purchases legal | CR-1, CR-4 (x: comply, y: violate), CR-8c |

**CR-1 operations by component and actor class.** Operations: (1) remove an option, (2) add an option, (3) change what an option brings, (4) transfer means.

| Actor class | K1 | K2 | K3 |
|---|---|---|---|
| `importers.quota_holders` (importers with imports in the base period) | 1 (importing beyond their share is removed) | 2 (a new option: sell or lease the share); 4 (a valuable right granted free is a transfer of means) | 3 (seizure and triple fine attached to importing without rights) |
| `importers.prospective` (would-be importers with no base-period imports) | 1 (importing without rights is removed) | 3 (entry now requires buying or leasing rights) | 3 |
| `buyers.sugar` (households, food and drink makers) | none directly; the price they face changes (CR-6, CR-9) | none | none |
| `beet_growers`, `beet_factories`, `landowners.farmland` | none directly; the price of their close substitute rises (CR-9) | none | none |
| `refineries.port` | none directly as refiners; their raw-cane input is cut (CR-9) | 2/4 if they are importers of record (unknown) | none |
| `corn_syrup_mills` | none (not covered); demand for their substitute rises (CR-9) | none | none |
| `foreign_sellers.sugar` | 1 (sales to Calvar beyond the quota removed) | none | none |
| `sellers.substitutes` (foreign makers of finished sweetened foods) | none; their exempt products improve relative to Calvarian ones (3, relative) | none | none |
| `shoppers.varnholt` | none for up to 10 kg per crossing; 3 (risk) beyond | none | 3 (sample checks) |
| `officials.enforcement` (customs) | none | 3 (registering transfers) | 3 (inspecting every bulk shipment; means used up, CR-8c) |
| `taxpayers.general` | none | none | 4 (enforcement is funded from the general budget) |

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `buyers.sugar` | Households and food and drink makers buying sugar | Pay more; can switch to corn syrup in some uses, to exempt blends, or (in Varnholt) buy in Ostria |
| `importers.quota_holders` | Importers in the 36-month base period | Receive permanent, tradable rights to the scarce import quantity |
| `importers.prospective` | Would-be importers | Must buy or lease rights |
| `beet_growers` | Farmers growing beet | Higher price for beet sugar |
| `beet_factories` | Four beet factories | Can raise throughput (A-4) |
| `landowners.farmland` | Owners of land suited to beet | Rent and value of land rise (CR-7c) |
| `sellers.other_field_crops` | Growers of crops that lose land to beet | Land moves away (A-4) |
| `refineries.port` | Two port refineries of raw cane | Input cut; cannot use beet (A-15) |
| `workers.refineries` | Refinery workers | Demand for their labor falls |
| `corn_syrup_mills` | Two wet mills | Demand for syrup rises; near capacity (A-13) |
| `input_suppliers.corn` | Corn growers selling to wet mills | Demand for corn rises (CR-9) |
| `buyers.corn_syrup` | Drink makers and others using syrup | Syrup costs more (A-13) |
| `makers.local` | Bakers and makers of fresh sweetened goods, competing mainly with each other (A-14) | Can pass the cost on |
| `buyers.local_sweetened_goods` | Their customers | Pay more |
| `makers.import_competing` | Makers of confectionery, biscuits and soft drinks competing with free imports (A-9) | Cannot pass the cost on fully |
| `workers.import_competing` | Their workers | Demand for their labor falls |
| `sellers.substitutes` | Foreign makers of finished sweetened goods | Sell more into Calvar |
| `importers.blends` | Importers of blends and syrups with 65% sugar or less | Exempt form gains (A-8) |
| `shoppers.varnholt` | Varnholt residents | Can buy up to 10 kg per crossing in Ostria (A-11) |
| `grocers.varnholt` | Varnholt grocery stores | Lose trip-complement sales (A-16) |
| `neighboring_jurisdictions` | Ostrian supermarkets | Gain Calvarian shoppers |
| `foreign_sellers.sugar` | World sugar sellers | Sell less to Calvar; many competitors, no country quota shares (A-18) |
| `exporters.other` | Calvar's other exporters | Reached through the foreign-exchange market (A-17) |
| `lobby.sugar` | Rights holders and growers; food makers on the other side | Stake in the five-year review |
| `officials.enforcement` | Customs | Inspections and registrations |
| `taxpayers.general` | General budget | Funds enforcement |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | importers.quota_holders | quantity_traded (sugar imports) | decrease | short | CR-1 op 1; CR-5a (exchanges beyond 350,000 tonnes are prevented); arithmetic (about 750,000 tonnes before) | A-1, A-2 |
| C-2 | buyers.sugar | price_paid | increase | short | CR-6 (with imports fixed below what buyers wish to buy at the world price, the price rises toward the level at which planned purchases match the restricted supply) | A-1, A-2 |
| C-3 | beet_growers | net_price_received | increase | short | CR-9 (close substitute); CR-7a | A-1, A-2, A-3 |

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-4 | buyers.sugar | quantity_demanded | decrease | short | CR-4c (LW-3) | A-1, A-2 |
| C-5 | beet_growers | quantity_supplied | increase | medium | CR-4b (x: other field crop, y: beet; mirror case); CR-7a | A-1, A-3, A-4 |
| C-6 | importers.quota_holders | quantity_traded (sugar imports in the nine months before the effective date) | increase | short | CR-10a (imports in the base period raise each importer's permanent share); CR-4b (x: import later, y: import now) | A-6 |
| C-7 | importers.quota_holders | inventory_held (sugar stocks on the effective date) | increase | short | CR-10a; CR-4b (x: import later, y: import now and store) | A-6 |
| C-8 | buyers.corn_syrup | quantity_substitute (corn syrup used, above all in soft drinks) | increase | medium | CR-4b (x: sugar, y: corn syrup) | A-1, A-7 |
| C-9 | importers.blends | reclassification (imports of blends and syrups at or below 65% sugar) | U1-a: increase; U1-b: increase | short | CR-4b (x: covered form, y: uncovered form). U1-b (dry weight) leaves fewer products under the threshold, so the response is smaller but has the same direction | A-1, A-8 |
| C-10 | shoppers.varnholt | cross_border_purchases (sugar bought in Ostria within the allowance) | increase | short | CR-4b (x: here, y: there) | A-1, A-11 |
| C-11 | importers.prospective | entry_rate | decrease | medium | CR-1 op 1 (entry only by buying or leasing rights); CR-7c (the right's price absorbs the expected gain, so entrants earn no more than elsewhere) | A-1 |
| C-12 | lobby.sugar | lobbying_effort (on the five-year review) | increase | medium | CR-4b (x: accept, y: lobby), for holders and growers (to keep the quota) and for food makers (to end it) | A-5, A-N1 |
| C-13 | makers.import_competing | quantity_supplied | decrease | medium | CR-9 (input_to; substitute); CR-4b for their buyers (x: Calvarian product, y: imported product with untaxed sugar) | A-1, A-9 |

## 6. Second-order effects

Market relations: `domestic_beet_sugar` and `imported_sugar`: `substitute`, close (A-3). `sugar` and `corn_syrup`: `substitute`, partial (A-7). `corn` and `corn_syrup`: `input_to`. `sugar` and `sweetened_goods`: `input_to`, close. `calvarian_sweetened_goods` and `imported_sweetened_goods`: `substitute`, close (A-9). `raw_cane_sugar` and `refining_services`: `input_to`, close (A-15). `sugar_in_calvar` and `sugar_in_ostria`: `across_border`, close for Varnholt (A-11). `sugar_in_ostria` and `other_groceries_in_ostria`: `complement` (trip) (A-16). `sugar_imports` and `other_exports`: linked through the foreign-exchange market, recorded as `across_border` with the note "currency" (A-17). `beet_land` and `other_field_crops`: `same_market_other_segment` (land in alternative uses), partial (A-4).

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-14 | importers.quota_holders | asset_value (quota rights) | increase | short | CR-5c (holders import at the world price, A-18, and sell at the higher Calvar price); CR-7b (the gain settles on the fixed means, the rights); CR-7c, CR-10c (capitalized when the allocation became expected) | substitute; depth 2 | A-1, A-2, A-5, A-18 |
| C-15 | importers.quota_holders | net_price_received (Calvar price received on quota sugar, net of the world price paid) | increase | short | CR-5c; CR-7b | substitute; depth 2 | A-1, A-2, A-18 |
| C-16 | landowners.farmland | asset_value (land suited to beet) | increase | medium | CR-7a (land moves into beet until yields equalize), CR-7b (the lasting gain settles on the fixed factor), CR-7c | input_to; depth 3 | A-3, A-4, A-5 |
| C-17 | sellers.other_field_crops | quantity_supplied | decrease | medium | CR-7a; CR-8a (land drawn into beet is withdrawn from other crops) | same_market_other_segment; depth 3 | A-3, A-4 |
| C-18 | beet_factories | employment | increase | medium | CR-9 (input_to; LW-10) | input_to; depth 3 | A-3, A-4 |
| C-19 | refineries.port | quantity_supplied (refined cane sugar) | decrease | short | CR-9 (input_to: their raw-cane input is cut and cannot be replaced by beet) | input_to; depth 2 | A-1, A-2, A-15 |
| C-20 | workers.refineries | employment | decrease | medium | CR-9 (input_to; LW-10) | input_to; depth 3 | A-1, A-2, A-15 |
| C-21 | refineries.port | capital_stock_target (refining capacity) | decrease | long | CR-10b (capacity shrinks as it wears out and is not replaced); CR-7b | input_to; depth 3 | A-1, A-5, A-15 |
| C-22 | buyers.corn_syrup | price_substitute (corn syrup) | increase | short | CR-9 (substitute); CR-6 (syrup price moves toward the level at which planned purchases match output from mills near capacity) | substitute; depth 2 | A-1, A-7, A-13 |
| C-23 | corn_syrup_mills | investment_target (wet-milling capacity) | increase | medium | CR-7a (capital moves toward the higher yield); CR-10a, CR-10c (on the expectation the quota lasts) | substitute; depth 3 | A-5, A-7, A-13 |
| C-24 | input_suppliers.corn | quantity_traded (corn sold to wet mills) | increase | medium | CR-9 (input_to; LW-10) | input_to; depth 4 | A-5, A-7, A-13 |
| C-25 | buyers.local_sweetened_goods | price_paid (fresh bakery and other local sweetened goods) | increase | medium | CR-9 (input_to); CR-7a (all local makers face the dearer sugar and are brought back into line by raising prices) | input_to; depth 2 | A-1, A-14 |
| C-26 | sellers.substitutes | quantity_substitute (imported confectionery, biscuits, soft drinks) | increase | medium | CR-4b for Calvarian buyers (x: domestic product, y: imported product); CR-9 | substitute; depth 3 | A-1, A-9 |
| C-27 | workers.import_competing | employment | decrease | medium | CR-9 (input_to; LW-10) from C-13 | input_to; depth 3 | A-1, A-9 |
| C-28 | makers.import_competing | capital_stock_target (food plants in Calvar) | decrease | long | CR-4b (x: build the new plant here, y: abroad), CR-10b (mainly at replacement) | substitute; depth 3 | A-1, A-5, A-9, A-10 |
| C-29 | grocers.varnholt | quantity_complement (other groceries sold to Varnholt shoppers) | decrease | short | CR-9 (complement, trip: shoppers who cross for sugar buy other groceries on the same trip) | complement (trip); depth 3 | A-1, A-11, A-16 |
| C-30 | neighboring_jurisdictions | quantity_traded (sales by Ostrian supermarkets to Calvarians) | increase | short | CR-9 (across_border and complement, trip) | across_border; depth 2 | A-1, A-11, A-16 |
| C-31 | foreign_sellers.sugar | quantity_traded (sales to Calvar) | decrease | short | CR-5a | substitute; depth 1 | A-1, A-2 |
| C-32 | exporters.other | net_price_received (Calvar currency per unit exported) | decrease | medium | CR-9 (fewer crowns offered for foreign money); CR-6 (the currency's price moves toward the level at which amounts offered and sought match, so the crown is dearer) | across_border (currency); depth 3 | A-1, A-2, A-17 |
| C-33 | exporters.other | quantity_supplied (exports) | decrease | medium | CR-4c | across_border (currency); depth 4 | A-1, A-2, A-17 |

Interaction of components. K2 decides who receives the gap between the Calvar price and the world price (C-14, C-15): because foreign sellers compete (A-18) and the rights belong to Calvarian importers, the gap goes to rights holders, not to foreign sellers or the budget. K2's base period (the 36 months before the effective date) rewards imports in the nine months after the bill's introduction (C-6). K1's exemptions open three exits: blends at or below 65% (C-9), finished foods (C-13, C-26) and the travelers' allowance (C-10). K3's port-only rule for bulk cargo closes the bulk smuggling exit (A-12, p 0.3, not reported).

Stopping points. The land chain stops at C-17 (depth 3): buyers of other field crops would be diffuse bystanders. The corn chain stops at C-24 (depth 4). The currency chain stops at C-33 (depth 4).

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance premise | Combined sign |
|---|---|---|---|---|
| buyers.sugar, price_paid, short | Quota (C-2) | Stocks built in the window (C-7) are sold after the effective date | A-1 states that the quota binds from the first year, which means the restricted supply including any carried stock falls short of what buyers wish to buy at the world price. The dominance premise is A-1 itself | increase (C-2) |
| buyers.sugar, price_paid, long | Demand grows against a fixed quota (A-1) | Beet supply expands (C-5); syrup capacity expands (C-23) | Neither expansion can bring the price back to the world price while the quota binds (A-1: binds "more tightly as demand grows"); CR-6 | increase (C-34) |
| importers.quota_holders, quantity_traded | Nine-month window before the effective date (C-6) | From the effective date (C-1) | Different time windows, signed separately (normal form, timing shifts) | C-6 increase; C-1 decrease |
| refineries.port, quantity_supplied vs asset_value | — | — | If refineries are importers of record, they hold rights (C-14) while their throughput falls (C-19). Different variables; not netted (CR-12c) | separate |

## 8. Time structure

Horizons: short = from the bill's introduction (nine months before the effective date) to the end of the first quota year; medium = years 2 to 5 (to the review); long = beyond the five-year review.

- **Allocation window (CR-10a).** The bill was introduced nine months before the effective date, and its formula counts imports over the 36 months before that date. Importers who can finance and store sugar (A-6) import more in those nine months (C-6) and hold larger stocks on the effective date (C-7). The stocks are sold over the first months of the quota, which softens, but on A-1 does not reverse, the first-year price rise.
- **Capitalization (CR-7c, CR-10c).** The rights' value (C-14) is fixed at the expected gap between the Calvar and world prices over the expected life of the quota (A-5). It accrues to the importers who receive the rights. Later buyers of rights pay that value and earn no more than elsewhere (C-11). Beet land gains the same way (C-16).
- **Slow stocks (CR-10b).** Food plants last 15 to 25 years (A-10), so relocation of sweetened-goods production happens mainly through new investment (C-28, long). Refining capacity shrinks as it wears out (C-21). Wet-mill capacity grows only with investment (C-23), so the syrup price rises first (C-22).
- **Growing bite.** The quota is fixed in tonnes while demand grows (A-1), so the gap between the Calvar and world prices, and the rights' value, tend to grow.
- **Review (CR-10a).** Expectations about the five-year review (A-5) drive investment in beet, syrup capacity and the value of rights, and give holders and growers a stake in lobbying (C-12).

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-35 | buyers.sugar | resources_available_other_uses | decrease | With demand inelastic (A-19), buyers spend more on sugar and sweeteners in total, leaving less for other goods | CR-8a; CR-3a |
| C-36 | officials.enforcement | enforcement_cost | increase | Inspecting every bulk shipment, sampling at Varnholt, registering transfers | CR-1 op 3; CR-8c |
| C-37 | taxpayers.general | resources_available_other_uses | decrease | The general-budget money that funds customs enforcement | CR-8a, CR-8b |
| C-38 | importers.blends | compliance_cost | increase | Resources spent importing, handling and separating blends and syrups only to stay under the threshold | CR-8c |
| C-1, C-31 | importers.quota_holders, foreign_sellers.sugar | quantity_traded (in sections 4 and 6) | decrease | Imports that would have taken place, and the gains both parties expected | CR-5a |
| C-12 | lobby.sugar | lobbying_effort (in section 5) | increase | Resources used up lobbying | CR-8c |

The gain to rights holders (C-14, C-15) is a transfer from sugar buyers (C-2, C-35); unlike a tariff, it brings no revenue to the budget (CR-8b: the receipt goes to the rights holders). Resources drawn into beet are withdrawn from other crops (C-17).

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | Without the quota, Calvar would keep importing well over 350,000 tonnes a year, so the quota binds from the first year, and more tightly as demand grows. | binding | 0.95 | Import records (about 750,000 tonnes); consumption trend; domestic cost compared with the world price. | Nearly every consequence fails. |
| A-2 | Customs enforces the quota at the ports. | enforcement | 0.85 | Only two ports admit bulk cargo; every shipment is inspected; seizure plus a triple fine. | C-1 to C-4, C-14, C-15, C-19 to C-21, C-31 to C-33 weaken (imports leak). |
| A-3 | Domestic beet sugar and refined imported sugar are close substitutes for buyers. | substitutability | 0.9 | Both are white sugar of standard grades; buyers' specifications. | C-3, C-5, C-16 to C-18 fail. |
| A-4 | Land and labor can move from other field crops into beet within one or two seasons, and the beet factories have some spare capacity. | alternative_uses | 0.7 | Crop rotation practice; factory utilization rates. | C-5, C-16 to C-18 fail. |
| A-5 | Holders, growers and landowners expect the quota to survive the five-year review. | expectations | 0.65 | Political strength of the grower lobby; how comparable programs fared at review. | C-14, C-16, C-21, C-23, C-24, C-28 weaken; C-12 changes. |
| A-6 | Importers know the allocation formula during the window and can finance and store extra imports. | expectations | 0.8 | Formula published with the bill; storage capacity at Quellport and Varo. | C-6, C-7 fail. |
| A-7 | Corn syrup and other sweeteners are acceptable substitutes for sugar in some uses, above all soft drinks. | substitutability | 0.8 | Current use of corn syrup by Calvarian and foreign drink makers. | C-8, C-22 to C-24 fail. |
| A-8 | Importing blends and syrups with 65% sugar or less is technically and commercially workable for some users. | other | 0.6 | Existing trade in sugar-cocoa blends and syrups; cost of using or separating them. | C-9, C-38 fail. |
| A-9 | Imported confectionery, biscuits and soft drinks are close substitutes for Calvarian ones and enter freely. | substitutability | 0.75 | Import shares in these categories; brand overlap; absence of other barriers. | C-13, C-26 to C-28 fail. |
| A-10 | Food plants last 15 to 25 years, so relocation happens mainly through new investment. | durability | 0.9 | Age of the plant stock; equipment lives. | C-28 moves to medium. |
| A-11 | Enough Varnholt residents shop in Ostria within the personal allowance. | mobility | 0.7 | 20-minute drive; existing cross-border shopping; car ownership. | C-10, C-29, C-30 fail. |
| A-12 | Bulk sugar is smuggled on a meaningful scale. | enforcement | 0.3 | Port-only entry for bulk; inspection rates. | Below cut-off; not used. |
| A-13 | Corn syrup output cannot expand at once because the mills are near capacity. | other | 0.7 | Mill utilization; time to add capacity. | C-22 weakens; C-23, C-24 come sooner. |
| A-14 | Makers of locally made sweetened goods compete mainly with each other, all face the dearer sugar, and cannot fully switch to other sweeteners. | other | 0.85 | Import shares of fresh bakery goods; recipe constraints. | C-25 fails. |
| A-15 | The port refineries cannot replace imported raw cane with domestic beet. | other | 0.9 | Beet is processed in beet factories by a different process. | C-19 to C-21 fail. |
| A-16 | Varnholt shoppers buy other groceries on the same trips as sugar. | other | 0.7 | Shopping surveys; basket composition. | C-29, C-30 weaken to sugar only. |
| A-17 | Lower imports are not offset by capital flows or other adjustments within the medium horizon. | other | 0.6 | Calvar's trade and capital accounts; exchange-rate regime. | C-32, C-33 fail. |
| A-18 | Calvar's sugar imports come from many competing foreign sellers, and no exporting country administers a share of the quota. | other | 0.8 | Calvar's share of world sugar trade; number of origin countries and trading houses; K2 gives the rights to Calvarian importers. | C-14, C-15: part of the gap goes to foreign sellers. |
| A-19 | Buyers' demand for sugar and sweeteners taken together is inelastic enough that their total spending on them rises. | substitutability | 0.75 | Sugar is a small share of household and most manufacturers' budgets; corn syrup substitutes well only in some uses (A-7) and itself costs more (C-22). | C-35 becomes ambiguous. |
| A-N1 | Rights holders and beet growers can organize to defend the quota at the five-year review at a cost below their stake; food makers can also organize against it. | other | 0.8 | Existing grower and importer associations; the concentrated value of rights; food industry associations. | C-12 fails. |
| A-N2 | The 10 kg allowance per crossing is enough, and checks at Varnholt are light enough, that Varnholt shoppers do not need to exceed it to make crossing worthwhile. | enforcement | 0.7 | Household sugar use (well under 10 kg a week for most households); sampling rate at the crossing. | C-10 still holds; whether some shoppers exceed the allowance (informal activity) would need a separate premise. Recorded, not cited. |

## 11. Report

**The policy:** From the effective date, Calvar allows only 350,000 tonnes of sugar imports a year, against about 750,000 tonnes now. The right to import is given free to past importers in proportion to their imports over the previous 36 months, and can be sold or leased. Sugar in finished foods, blends with 65% sugar or less, corn syrup and travelers' purchases up to 10 kg per crossing are not covered. Bulk cargo may enter only at two inspected ports.

**Visible consequences:** Imports fall (C-1) and buyers pay more for sugar (C-2), more so as demand grows (C-34). Beet growers receive more (C-3) and grow more (C-5). Importers who receive rights hold a valuable asset (C-14) and earn the gap between the Calvar and world prices on what they import (C-15).

**Invisible consequences:**
- *Before the quota.* Importers bring in extra sugar in the nine months before the effective date to raise their permanent share (C-6), and hold larger stocks on that date (C-7).
- *Buyers.* Buyers use less sugar (C-4), more corn syrup (C-8) and more exempt blends (C-9); with total demand inelastic they have less left for other goods (C-35). Corn syrup costs more (C-22) until wet mills add capacity (C-23), which raises demand for corn (C-24).
- *Food makers and their workers.* Local bakers pass the cost on (C-25). Makers of confectionery, biscuits and soft drinks lose sales to imports (C-13, C-26), employ fewer people (C-27) and, in the long run, build new plants abroad (C-28).
- *Refineries.* The port refineries refine less cane (C-19), employ fewer people (C-20) and lose capacity over time (C-21).
- *Land.* Land suited to beet gains value (C-16); other field crops lose land (C-17); beet factories employ more (C-18).
- *Entry.* New importers must buy or lease rights, so entry falls (C-11).
- *The border.* Varnholt residents buy sugar in Ostria (C-10), with other groceries on the same trips, so Varnholt grocers sell less (C-29) and Ostrian supermarkets more (C-30).
- *Abroad and the currency.* Foreign sugar sellers sell less to Calvar (C-31). Fewer crowns are offered for foreign money, so other exporters receive fewer crowns (C-32) and export less (C-33).
- *Unseen costs.* Customs spends more on enforcement (C-36), paid by general taxpayers (C-37); blends are handled only to stay under the threshold (C-38); holders, growers and food makers lobby over the review (C-12).

**Ambiguous effects:** None at the level of a single actor class and variable. The method cannot say whether total employment rises or falls: beet factory jobs (C-18) and refinery and food-plant jobs (C-20, C-27) are different classes, and are not netted.

**Key conditions:** The quota binds (A-1, 0.95) and is enforced at the ports (A-2, 0.85). The rights capture the price gap only because foreign sellers compete (A-18, 0.8). Values of rights and land and long-lived investment rest on the expectation that the quota survives review (A-5, 0.65). The blend exit rests on A-8 (0.6) and the currency chain on A-17 (0.6), the weakest premises reported. The lobbying consequence needs a new premise (A-N1, 0.8).

**What this analysis cannot say:** How much the price rises, how many jobs move between beet, refining and food making, whether the transfer to rights holders and growers is worth its cost, or whether the policy is good. Health, nutrition, safety and environmental effects (including any change in sugar intake) are not analyzed. Not reported (assumption below 0.5): bulk sugar smuggling (A-12, p 0.3).

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | importers.quota_holders | quantity_traded (sugar imports, from the effective date) | decrease | short | visible | B | CR-1 op 1; CR-5a; arithmetic | A-1, A-2 |
| C-2 | buyers.sugar | price_paid | increase | short | visible | B | CR-6 (quantity fixed, price moves toward the level at which plans are compatible) | A-1, A-2 |
| C-3 | beet_growers | net_price_received | increase | short | visible | B | CR-9 (substitute); CR-7a | A-1, A-2, A-3 |
| C-4 | buyers.sugar | quantity_demanded | decrease | short | invisible | B | CR-4c (LW-3) | A-1, A-2 |
| C-5 | beet_growers | quantity_supplied | increase | medium | visible | B | CR-4b (x: other crop, y: beet); CR-7a | A-1, A-3, A-4 |
| C-6 | importers.quota_holders | quantity_traded (sugar imports, nine months before the effective date) | increase | short | invisible | B | CR-10a; CR-4b (x: import later, y: import now) | A-6 |
| C-7 | importers.quota_holders | inventory_held (sugar stocks on the effective date) | increase | short | invisible | B | CR-10a; CR-4b (x: import later, y: import now and store) | A-6 |
| C-8 | buyers.corn_syrup | quantity_substitute (corn syrup used) | increase | medium | invisible | B | CR-4b (x: sugar, y: corn syrup) | A-1, A-7 |
| C-9 | importers.blends | reclassification (blends and syrups at or below 65% sugar) | U1-a: increase; U1-b: increase | short | invisible | B | CR-4b (x: covered form, y: uncovered form) | A-1, A-8 |
| C-10 | shoppers.varnholt | cross_border_purchases (sugar in Ostria) | increase | short | invisible | B | CR-4b (x: here, y: there) | A-1, A-11 |
| C-11 | importers.prospective | entry_rate | decrease | medium | invisible | B | CR-1 op 1; CR-7c | A-1 |
| C-12 | lobby.sugar | lobbying_effort | increase | medium | visible | B | CR-4b (x: accept, y: lobby) | A-5, A-N1 |
| C-13 | makers.import_competing | quantity_supplied | decrease | medium | invisible | B | CR-9 (input_to; substitute); CR-4b (buyers: x: Calvarian product, y: imported product) | A-1, A-9 |
| C-14 | importers.quota_holders | asset_value (quota rights) | increase | short | visible | B | CR-5c; CR-7b; CR-7c; CR-10c | A-1, A-2, A-5, A-18 |
| C-15 | importers.quota_holders | net_price_received (Calvar price on quota sugar, net of world price) | increase | short | invisible | B | CR-5c; CR-7b | A-1, A-2, A-18 |
| C-16 | landowners.farmland | asset_value (land suited to beet) | increase | medium | invisible | B | CR-9 (input_to); CR-7a, CR-7b, CR-7c | A-3, A-4, A-5 |
| C-17 | sellers.other_field_crops | quantity_supplied | decrease | medium | invisible | B | CR-7a; CR-8a | A-3, A-4 |
| C-18 | beet_factories | employment | increase | medium | visible | B | CR-9 (input_to; LW-10) | A-3, A-4 |
| C-19 | refineries.port | quantity_supplied (refined cane sugar) | decrease | short | invisible | B | CR-9 (input_to) | A-1, A-2, A-15 |
| C-20 | workers.refineries | employment | decrease | medium | invisible | B | CR-9 (input_to; LW-10) | A-1, A-2, A-15 |
| C-21 | refineries.port | capital_stock_target (refining capacity) | decrease | long | invisible | B | CR-9 (input_to); CR-10b; CR-7b | A-1, A-5, A-15 |
| C-22 | buyers.corn_syrup | price_substitute (corn syrup) | increase | short | invisible | B | CR-9 (substitute); CR-6 | A-1, A-7, A-13 |
| C-23 | corn_syrup_mills | investment_target (wet-milling capacity) | increase | medium | invisible | B | CR-9 (substitute); CR-7a; CR-10a, CR-10c | A-5, A-7, A-13 |
| C-24 | input_suppliers.corn | quantity_traded (corn sold to wet mills) | increase | medium | invisible | B | CR-9 (input_to; LW-10) | A-5, A-7, A-13 |
| C-25 | buyers.local_sweetened_goods | price_paid | increase | medium | invisible | B | CR-9 (input_to); CR-7a | A-1, A-14 |
| C-26 | sellers.substitutes | quantity_substitute (imported confectionery, biscuits, soft drinks) | increase | medium | invisible | B | CR-9 (substitute); CR-4b | A-1, A-9 |
| C-27 | workers.import_competing | employment | decrease | medium | invisible | B | CR-9 (input_to; LW-10) | A-1, A-9 |
| C-28 | makers.import_competing | capital_stock_target (food plants in Calvar) | decrease | long | invisible | B | CR-4b (x: build here, y: abroad); CR-10b | A-1, A-5, A-9, A-10 |
| C-29 | grocers.varnholt | quantity_complement (other groceries) | decrease | short | invisible | B | CR-9 (complement, trip) | A-1, A-11, A-16 |
| C-30 | neighboring_jurisdictions | quantity_traded (Ostrian supermarket sales to Calvarians) | increase | short | invisible | B | CR-9 (across_border; complement, trip) | A-1, A-11, A-16 |
| C-31 | foreign_sellers.sugar | quantity_traded (sales to Calvar) | decrease | short | invisible | B | CR-5a | A-1, A-2 |
| C-32 | exporters.other | net_price_received (Calvar currency per unit exported) | decrease | medium | invisible | B | CR-9 (across_border, currency); CR-6 | A-1, A-2, A-17 |
| C-33 | exporters.other | quantity_supplied (exports) | decrease | medium | invisible | B | CR-9 (across_border, currency); CR-4c | A-1, A-2, A-17 |
| C-34 | buyers.sugar | price_paid | increase | long | visible | B | CR-6; CR-12 (domestic supply responses cannot close the gap while the quota binds) | A-1, A-2 |
| C-35 | buyers.sugar | resources_available_other_uses | decrease | medium | invisible | B | CR-8a; CR-3a | A-1, A-19 |
| C-36 | officials.enforcement | enforcement_cost | increase | short | invisible | A | CR-1 op 3; CR-8c | none |
| C-37 | taxpayers.general | resources_available_other_uses | decrease | short | invisible | A | CR-8a, CR-8b | none |
| C-38 | importers.blends | compliance_cost | increase | short | invisible | B | CR-8c | A-8 |

## Gaps found

**(a) Calculus gaps.** None. Every step was derived from CR-1 to CR-12, the foundations and arithmetic. Who captures the gap between the Calvar and world prices (C-14, C-15) followed from CR-5c and CR-7b with A-18; the allocation-window rush (C-6) from CR-10a.

**(b) New premises.**
- A-N1 (p 0.8): C-12. CR-4b (x: accept, y: lobby) gives the direction, but that holders, growers and food makers can organize at a cost below their stake is empirical. The case assumptions include expectations about the review (A-5) but no premise that anyone organizes.
- A-N2 (p 0.7): recorded, not cited. CR-4b (x: comply, y: violate) at the Varnholt crossing would license informal over-allowance purchases only with a premise that the allowance binds for some shoppers; the case assumptions do not cover it, so no consequence on informal activity is reported.

**(c) Unclear core rules.**
- CR-6 is stated for a rule that "prevents the price from moving". A quota fixes a quantity and leaves the price free. CR-6's first paragraph (prices tend toward the level at which planned purchases and sales are compatible) carries C-2, but its "displaced pressure" part does not obviously apply, because the price is free to move. The rule could say explicitly that a fixed quantity is the mirror case (the price moves; the scarce item is the right to supply).
- CR-1: a free grant of a permanent, tradable right (K2) is both an added option (op 2: sell or lease) and a transfer of means (op 4). The rule does not say which, or whether both should be recorded.
- CR-7c says a change in yield is captured by "whoever owns it when the change becomes expected". The quota rights did not exist before the policy; the rule had to be read as "whoever is granted the asset when it is created".
- CR-12b refers to "a dominance pattern" for a dominance claim. For the first-year price (section 7) the dominance premise was simply A-1 (the quota binds from the first year); the core rules do not say whether a binding premise counts as a dominance premise.
- Per-reading signs: U1 (dry versus total weight) gives the same sign under both readings (C-9); the convention was followed, though it adds nothing here.
