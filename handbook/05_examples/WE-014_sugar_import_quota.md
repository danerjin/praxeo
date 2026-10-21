# WE-014 Import quota on raw sugar, with free tradable quota rights

Analyst: draft (Handbook 0.5)  |  Rule catalog version: 0.5  |  Status: awaiting expert review

A stylized policy in a fictional country. It resembles real sugar import quotas but is not modeled on any one of them, and it is kept apart from the historical cases reserved for evaluation. The probabilities are illustrative; the evidence column says what a real analysis would cite.

## 1. Policy record

**Calvar Sugar Market Act.** The Republic of Calvar (about 20 million people) uses about 1.2 million tonnes of sugar a year. Domestic farmers grow sugar beet, which four beet factories turn into about 450,000 tonnes of white sugar. The rest, about 750,000 tonnes, is imported, mostly as raw cane sugar that two refineries at the ports of Quellport and Varo refine. World sugar prices have been below the cost of most Calvarian beet growers for years. Corn syrup is made from domestic corn by two wet mills. Calvar's only land neighbor, Ostria, has no sugar quota; the border town of Varnholt (150,000 people) is 20 minutes from Ostrian supermarkets, but Calvar's main cities are 200 km or more from the border. The bill was introduced with government backing nine months before the effective date and passed four months later.

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Import quota | `quota` | Imports of raw and refined sugar, and of mixtures containing more than 65% sugar by weight | Importers | 350,000 tonnes a year from the effective date. No expiry, but parliament must review the quota after five years. | Sugar contained in finished foods; mixtures with 65% sugar or less; a travelers' personal allowance of 10 kg per crossing. Corn syrup and other sweeteners are not covered. |
| K2 Quota rights | Allocation of K1 (part of K1) | Shares of the annual quota | Importers | Shares allocated free, in proportion to each importer's sugar imports over the 36 months before the effective date. Shares are permanent and may be sold or leased; transfers are registered with customs. | None |
| K3 Enforcement | Enforcement | K1, K2 | Customs service | Imports without quota rights are seized and fined three times their value. Bulk cargo may enter only through Quellport and Varo, where every shipment is inspected; the land crossing at Varnholt is checked by sample. Funded from the general budget. | None |

Unclear provisions: whether the 65% threshold counts sugar against dry weight or total weight. Assumed total weight, the reading more favorable to importers of syrups and blends.

## 2. Classification

| Component | Rothbard type | Binding? | Rule families |
|---|---|---|---|
| K1 | Triangular: prohibits exchanges between Calvarian buyers and foreign sellers beyond the quota; a grant of privilege to domestic growers and to holders of quota rights | Yes: the quota is less than half of current imports, and demand grows with population, so it binds more tightly each year (A-1) | EN-6, TX-8, TS-3, RS, OC |
| K2 | Triangular (part of K1): decides who captures the gap between the domestic and the world price | Yes | EN-6, SB-4, RS-8, DM-4 |
| K3 | Binary: funded from the general budget, assumed to rise with the new work (A-22) | Yes | OC-3 |

The quota collects no revenue. The gap between the domestic and world price of the quota tonnes goes to whoever holds the rights (K2), not to the state.

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `growers.beet` | Domestic beet farmers and the four beet factories | Sell into a market with less import competition. |
| `landowners.beet` (`factor_owners.specific`) | Owners of land suited to beet within reach of the factories | That land earns more in beet. |
| `quota_holders` | Importers who imported in the base period, including both port refineries if they import their raw cane themselves (A-20) | Receive free rights to buy at the world price and sell at the domestic price. |
| `importers.prospective` (`sellers.prospective`) | Firms that would start importing sugar | Must buy or lease quota shares to import. |
| `refiners.port` | The cane refineries at Quellport and Varo | Hold large shares if they were importers of record (A-20), but have less raw cane to refine. |
| `workers.beet_factories` | Employees of the four beet factories | More beet to process. |
| `buyers.sugar` | All buyers of sugar: the two manufacturer classes below and households | Pay more for sugar. |
| `manufacturers.tradable` | Makers of confectionery, biscuits, soft drinks and other sweetened goods that are also imported | Pay more for sugar while competing with imports made with world-price sugar. |
| `manufacturers.local` | Bakeries and makers of fresh desserts and other sweetened goods that are not easily imported | Pay more for sugar; compete mainly with each other. |
| `households` (`buyers.current`) | Buyers of sugar and sweetened goods | Pay more; can switch to other goods. |
| `households.varnholt` | Residents near the Ostrian border | Can buy up to 10 kg per crossing in Ostria. |
| `retailers.varnholt` | Calvarian grocery stores near the border | Lose some shopping trips to Ostria. |
| `sweetener_makers` (`sellers.substitutes`) | Corn syrup mills and sellers of other sweeteners | More demand. |
| `sweetener_users` (`buyers.substitutes`) | Firms already using corn syrup | Compete with switchers for corn syrup. |
| `exporters.foreign` | Foreign sugar sellers | Sell less to Calvar. |
| `ostria.sellers` (`neighboring_jurisdictions`) | Ostrian shops near Varnholt and Ostrian food manufacturers | More Calvarian customers. |
| `buyers.field_crops` | Buyers of the wheat, barley and other crops grown on land that could switch to beet | Less of those crops grown in Calvar. |
| `exporters.calvar` | Calvarian export industries | See C-23. |
| `officials.enforcement`, `taxpayers` | Customs and its funders | More inspection and rights administration. |

## 4. Direct effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | `quota_holders`, `exporters.foreign` | `quantity_traded` (sugar imports into Calvar) | decrease | short | EN-6 | A-1, A-2 |
| C-2 | `growers.beet` | `net_price_received` (sugar) | increase | short | EN-6 | A-1, A-2, A-3 |
| C-3 | `buyers.sugar` | `price_paid` (sugar in Calvar) | increase | short, growing over time | EN-6, TS-3 | A-1, A-2 |

C-1 and C-2 are what the Act's supporters point to: fewer imports and a better price for Calvarian growers. C-2 and C-4 follow from EN-6, which (as widened in catalog 0.3) names the gain to domestic sellers of a good whose imports are restricted, as TX-7 does for a tariff. They rest on domestic and imported white sugar being one market (A-3). C-3 is the same price rise seen from the buyers' side. It is rarely mentioned when the quota is passed.

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-4 | `growers.beet` | `quantity_supplied` (beet sugar) | increase | medium (from the next sowing) | EN-6, LW-4 | A-1, A-4 |
| C-5 | `quota_holders` | `asset_value` (quota shares) | increase | short (from the announcement and the allocation) | EN-6, SB-4 | A-1, A-2, A-5 |
| C-6 | `quota_holders` (incumbent importers) | `quantity_traded` (sugar imports in the announcement window) | increase | short | RS-8 | A-6 |
| C-7 | `importers.prospective` | `entry_rate` (sugar importing) | decrease | short to medium | EN-6, SB-4 | A-1, A-2 |
| C-8 | `manufacturers.tradable`, `manufacturers.local` | `quantity_substitute` (corn syrup and other sweeteners) | increase | short to medium | RS-1 | A-1, A-7 |
| C-9 | `manufacturers.tradable` | `reclassification` (importing sugar as blends and syrups with 65% sugar or less) | increase | short to medium | RS-5 | A-8 |
| C-10 | `manufacturers.tradable` | `quantity_supplied` (sweetened goods made in Calvar) | decrease | medium to long | RS-14, RS-6, RS-4, TS-1 | A-1, A-9, A-10 |
| C-11 | `households.varnholt` | `cross_border_purchases` (sugar and sweetened goods in Ostria) | increase | short | RS-4 | A-1, A-11 |
| C-12 | `growers.beet`, `quota_holders`, `manufacturers.tradable` | `lobbying_effort` (growers and holders to keep or tighten the quota at the five-year review; manufacturers for a larger quota or an exemption for their inputs) | increase | medium | RS-7 | A-1, A-21 |

C-6: shares are allocated by imports over the 36 months before the effective date, and the Act was expected nine months ahead. Each extra tonne imported in that window earns a larger permanent share and adds to a stock that can be sold after the quota bites. Both reasons pull imports into the window.

C-7: the quota fixes the total, so a new importer can enter only by buying or leasing shares from incumbents. The share price carries the expected rent (SB-4), which removes the extra return that would otherwise attract entry.

C-10: imported finished goods are made with world-price sugar and enter freely (A-9), so domestic makers of tradable goods cannot raise their prices enough to cover the dearer sugar; with exempt competitors, the quantity effect of RS-14 dominates. Their return falls. New lines are built in Ostria or further abroad (RS-4), and existing plants are not replaced as they age (RS-6, TS-1). The same competition holds the price of tradable sweetened goods near the import price, so their price is not signed (section 7).

C-9 has a cost of its own: the resources spent buying, handling and separating blends only to stay under the threshold are used up (C-32; CR-8c).

Not reported: bulk smuggling of raw sugar (RS-3). Bulk cargo may enter only through two inspected ports, and the land crossing suits only small amounts; A-12 is below the cut-off (p = 0.3). Because no meaningful informal market is reported, RS-10 does not apply. Buying in Ostria within the 10 kg allowance is legal and is recorded as C-11.

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-13 | `sweetener_users` | `price_substitute` (corn syrup) | increase | short to medium | RS-1 | sugar and corn syrup: `substitute`, close in soft drinks, partial in baking and confectionery | A-7, A-13 |
| C-14 | `sweetener_makers` | `quantity_supplied` (corn syrup) | increase | medium | RS-1, LW-4 | as C-13 | A-7 |
| C-15 | `landowners.beet` | `asset_value` (farmland suited to beet) | increase | short to medium | SB-4, LW-4 | beet land `input_to` beet sugar, close near the factories | A-4, A-5 |
| C-16 | `households` | `price_paid` (locally made sweetened goods: bread, pastry, desserts) | increase | short to medium | EN-6, RS-14 | sugar `input_to` sweetened goods | A-1, A-14 |
| C-17 | `manufacturers.tradable` (workers in Calvar) | `employment`, `hours_worked` | at_least_one_decrease | medium to long | RS-14, RS-6, RS-4 | | A-1, A-9, A-10 |
| C-18 | `refiners.port` | `quantity_supplied` (refined cane sugar) | decrease | short | EN-6 | raw cane `input_to` refined sugar | A-1, A-2 |
| C-19 | `refiners.port` (workers) | `employment`, `hours_worked` | at_least_one_decrease | medium | RS-6 | | A-1, A-15 |
| C-30 | `workers.beet_factories` | `employment`, `hours_worked` | at_least_one_increase | medium | EN-6, CR-9 | beet `input_to` beet sugar; labor `input_to` beet sugar | A-1, A-4 |
| C-31 | `refiners.port` | `capital_stock_target` (refining capacity) | decrease | long | RS-6, TS-1 | | A-1, A-15 |
| C-20 | `ostria.sellers` (shops near Varnholt) | `quantity_traded` (all goods sold to Calvarians) | increase | short | RS-4, RS-9 | Varnholt and Ostrian shops: `across_border`, close; sugar and other groceries: `complement`, note `trip` | A-11, A-16 |
| C-21 | `retailers.varnholt` | `quantity_traded` (other groceries) | decrease | short | RS-4, RS-9 | as C-20 | A-11, A-16 |
| C-22 | `ostria.sellers` (food manufacturers) | `quantity_supplied` (sweetened goods sold into Calvar) | increase | medium | RS-4 | Calvarian and imported sweetened goods: `substitute`, close | A-9 |
| C-23 | `exporters.calvar` | `quantity_supplied` (export industries) | decrease | medium | EN-6, TX-8 | | A-17 |
| C-33 | `exporters.calvar` (workers) | `employment`, `hours_worked` | at_least_one_decrease | medium | TX-8, OC-5 | | A-17 |

C-16: sugar is a material input to these goods and costs more for every maker (C-3), so their price rises and/or their output falls (RS-14). For locally made goods (bread, pastry, desserts), every competitor faces the same dearer sugar (A-14), so the price rise dominates. For tradable goods, competitors abroad use world-price sugar (A-9), so the quantity effect dominates (C-10) and the price is held near the import price; C-16 is therefore stated for locally made goods only (see section 7).

C-17, C-19, C-30 and C-33 are group consequences (RS-6, catalog 0.5): firms that produce more or less may change staff or hours, and the method does not say which. C-30: more beet sugar (C-4) needs more processing at the beet factories (CR-9, labor `input_to` beet sugar). C-31: the refineries' lost throughput is lasting, so as their plant wears out it is not fully replaced (RS-6, TS-1).

C-23: by cutting imports, the quota leaves foreigners with less Calvarian currency to spend on Calvarian exports. TX-8, widened in catalog 0.3 to import quotas, applies directly; the consequence rests on A-17 (p = 0.6). TX-8 also names employment; as under RS-6, that is recorded as a group (C-33).

Stopping points: C-14 leads to more demand for corn from corn farmers (depth 4), a diffuse group, so the chain stops there. Port service firms that handled the lost raw cane are diffuse bystanders at depth 4; stopped. RS-11 (lock-in) was checked: no benefit here is lost by moving, so it does not apply.

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `refiners.port`, `return_on_capital` (owners), medium | Rent on their quota shares (C-5), if they were importers of record in the base period (A-20): they buy raw cane at the world price and sell refined sugar at the domestic price. | Less raw cane to refine (C-18), so idle capacity and fixed costs spread over fewer tonnes (C-19). | None | **ambiguous**. Decided by how large their shares are relative to their former throughput, and whether they can lease extra shares from other holders. |
| Division of the gap between the domestic and world price, short to medium | Holders of quota rights capture it if many foreign sellers compete for Calvarian sales (C-5). | Foreign sellers capture part of it if they are few and can raise their price on quota sales. | DM-4 (A-18) | **Holders of quota rights capture most of the gap.** Calvar's imports come from many competing sellers on the world market, and the rights are held and administered in Calvar (K2), not by exporting countries (A-18, p = 0.8). This supports C-5. If A-18 failed, foreign sellers would capture part of the gap and C-5 would be smaller, but still an increase. |
| `households`, `price_paid` (tradable sweetened goods: confectionery, soft drinks), medium | Domestic makers pay more for sugar (C-3), and some lines leave Calvar (C-10). | None. | None needed | **Not signed.** Imports made with world-price sugar are close substitutes (A-9), so the price is held near the import price, and the domestic makers' higher cost is met by lower output (C-10) rather than a higher price. A rise needs a premise that imports are imperfect substitutes, which the analysis does not have. C-16 covers locally made goods only. |
| `growers.beet`, `investment_target` (new beet factory capacity), long | A higher sugar price (C-2) raises the return on new capacity, if growers expect the quota to survive the five-year review (A-5, p = 0.65). | If growers expect the quota to be cut at the review (negation of A-5, p = 0.35), the expected return on capacity that takes decades to pay off is lower (TS-2). | None | **increase** (C-24). The − chain only weakens the + chain; it cannot push investment below the counterfactual, and it rests on an assumption below the cut-off. |

## 8. Time structure

- **Announcement window (nine months).** Imports rush in (C-6), both to build base-period shares and to stock sugar. The first months after the effective date are supplied partly from these stocks, so the domestic price (C-3) climbs over several months as stocks run down instead of jumping on the effective date.
- **Asset values move first.** Quota shares (C-5) and beet land (C-15) gain value as soon as the quota is expected, before any sugar is held back (SB-4).
- **Growers respond at the next season.** Beet is sown in spring and processed in autumn, so extra beet sugar (C-4) arrives in the second season at the earliest, limited by the four factories' capacity until new capacity is built (C-24, long).
- **Substitution is fast in some uses, slow in others.** Soft-drink makers can switch to corn syrup with a recipe change (C-8, short); confectionery recipes change more slowly. Corn syrup prices rise at first because the mills are near capacity (C-13, A-13) and ease as capacity grows (C-14).
- **Relocation is slow and grows.** Food plants last 15 to 25 years (A-10). New lines go abroad first; existing plants close as they age, so the fall in domestic output and in jobs or hours (C-10, C-17) is small in the first year and grows over the long horizon (TS-1).
- **The quota is fixed in tonnes while demand grows.** The gap between domestic and world prices therefore tends to widen each year (TS-3, which since catalog 0.3 covers parameters fixed in physical units; the expected demand path is part of A-1). C-3 grows over time for this reason.
- **The five-year review.** As it approaches, the value of shares and of beet land depends on what holders expect it to decide (TS-2), and lobbying (C-12) peaks before it.

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-25 | `buyers.sugar`, `exporters.foreign` | `quantity_traded` (sugar sold in Calvar, all sources) | decrease | Sugar that buyers would have bought at the world price and foreign sellers would have sold, and that extra beet sugar does not replace. Both sides lose the gain they expected. | OC-4 |
| C-26 | `buyers.field_crops` | `quantity_traded` (field crops grown in Calvar) | decrease | The wheat, barley and other crops that the land and labor now growing beet would have produced. | OC-1, LW-4 |
| C-27 | `buyers.sugar` | `resources_available_other_uses` | decrease | The other goods buyers would have bought with what they now pay above the world price for sugar. This requires their total spending on sugar and sweeteners to rise, which holds where few uses have a close substitute (A-19). | EN-6, LW-1 |
| C-28 | `quota_holders`, `importers.prospective` | `compliance_cost` | increase | Time and fees spent registering, trading and leasing shares and documenting shipments. | OC-2 |
| C-29 | `taxpayers` | `resources_available_other_uses` | decrease | What the customs budget for inspection and rights administration would otherwise have funded (budget rising with the task, A-22). | OC-3, OC-1 |
| C-32 | `manufacturers.tradable` | `compliance_cost` (buying, handling and separating blends to stay under the threshold) | increase | What those resources would otherwise have produced. | OC-1, CR-8c |
| C-34 | `officials.enforcement` | `enforcement_cost` | increase | Inspection of every bulk shipment, sample checks at Varnholt, and the register of quota transfers. | OC-3 |

OC-3 funding: customs is funded from the general budget (K3); A-22 takes that budget to rise with the new work, so the cost falls on taxpayers (C-29). If it were fixed, other customs checks would fall instead.

C-26 is the classic unseen effect of protection: the beet is visible, the crops that would have grown in its place are not.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | Without the quota, Calvar would keep importing well over 350,000 tonnes a year, so the quota binds from the first year, and more tightly as demand grows. | binding | 0.95 | Import records (about 750,000 tonnes); consumption trend; domestic cost compared with the world price. | Almost every consequence fails. |
| A-2 | Customs enforces the quota at the ports. | enforcement | 0.85 | Only two ports admit bulk cargo; every shipment is inspected; seizure plus a triple fine. | C-1 to C-3 shrink; smuggling grows. |
| A-3 | Domestic beet sugar and refined imported sugar are close substitutes for buyers. | substitutability | 0.9 | Both are white sugar of standard grades; buyers' specifications. | C-2 weakens. |
| A-4 | Land and labor can move from other field crops into beet within one or two seasons, and the beet factories have some spare capacity. | alternative_uses | 0.7 | Crop rotation practice; factory utilization rates. | C-4, C-15, C-26 and C-30 weaken; the price rise (C-3) is larger. |
| A-5 | Holders, growers and landowners expect the quota to survive the five-year review. | expectations | 0.65 | Political strength of the grower lobby; how comparable programs fared at review. | C-5, C-15 and C-24 are smaller. |
| A-6 | Importers know the allocation formula during the window and can finance and store extra imports. | expectations | 0.8 | Formula published with the bill; storage capacity at Quellport and Varo. | C-6 not reported. |
| A-7 | Corn syrup and other sweeteners are acceptable substitutes for sugar in some uses, above all soft drinks. | substitutability | 0.8 | Current use of corn syrup by Calvarian and foreign drink makers. | C-8, C-13, C-14 weaken. |
| A-8 | Importing blends and syrups with 65% sugar or less is technically and commercially workable for some users. | other | 0.6 | Existing trade in sugar-cocoa blends and syrups; cost of using or separating them. | C-9, C-32 not reported. |
| A-9 | Imported confectionery, biscuits and soft drinks are close substitutes for Calvarian ones and enter freely. | substitutability | 0.75 | Import shares in these categories; brand overlap; absence of other barriers. | C-10, C-17 and C-22 weaken; domestic makers pass more of the cost on, and the price of tradable sweetened goods rises. |
| A-10 | Food plants last 15 to 25 years, so relocation happens mainly through new investment. | durability | 0.9 | Age of the plant stock; equipment lives. | Relocation is faster. |
| A-11 | Enough Varnholt residents shop in Ostria within the personal allowance. | mobility | 0.7 | 20-minute drive; existing cross-border shopping; car ownership. | C-11, C-20, C-21 not reported. |
| A-12 | Bulk sugar is smuggled on a meaningful scale. | enforcement | 0.3 | Port-only entry for bulk; inspection rates. | Below cut-off; not reported. |
| A-13 | Corn syrup output cannot expand at once because the mills are near capacity. | other | 0.7 | Mill utilization; time to add capacity. | C-13 is smaller and shorter. |
| A-14 | Makers of locally made sweetened goods compete mainly with each other, all face the dearer sugar, and cannot fully switch to other sweeteners. | other | 0.85 | Import shares of fresh bakery goods; recipe constraints. | C-16 weakens for these goods. |
| A-15 | The port refineries cannot replace imported raw cane with domestic beet. | other | 0.9 | Beet is processed in beet factories by a different process. | C-19, C-31 weaken. |
| A-16 | Varnholt shoppers buy other groceries on the same trips as sugar. | other | 0.7 | Shopping surveys; basket composition. | C-20, C-21 weaken. |
| A-17 | Lower imports are not offset by capital flows or other adjustments within the medium horizon (the assumption of TX-8). | other | 0.6 | Calvar's trade and capital accounts; exchange-rate regime. | C-23, C-33 not reported. |
| A-18 | Calvar's sugar imports come from many competing foreign sellers, and no exporting country administers a share of the quota (the assumption of DM-4). | other | 0.8 | Calvar's share of world sugar trade; number of origin countries and trading houses; K2 gives the rights to Calvarian importers. | Foreign sellers capture part of the gap; C-5 is smaller. |
| A-19 | Buyers' demand for sugar and sweeteners taken together is inelastic enough that their total spending on them rises. | substitutability | 0.75 | Sugar is a small share of household and most manufacturers' budgets; corn syrup substitutes well only in some uses (A-7) and itself costs more (C-13). | C-27 not reported; buyers still lose, but the money they spend elsewhere may not fall. |
| A-20 | The port refineries imported their raw cane as importers of record in the base period, and so receive large quota shares. | other | 0.8 | Customs import records by importer; whether the refineries buy raw cane themselves or through trading houses. | The refineries hold few shares: the + chain of the refinery row in section 7 vanishes and their return is a **decrease**. |
| A-21 | Growers, quota holders and manufacturers can organize at a cost below their stake. | other | 0.85 | Existing grower associations; the few large holders; food manufacturers' trade body. | C-12 not reported. |
| A-22 | The customs budget is raised to cover inspection of bulk shipments and the register of quota rights. | revenue_use | 0.7 | Budget documents; K3 says only that it is funded from the general budget. | C-29 not reported; other customs work falls instead (OC-3, fixed budget). |

## 11. Report

**The policy.** Calvar limits sugar imports to 350,000 tonnes a year, less than half of what it now imports. The rights to import that amount are handed out free to existing importers in proportion to their recent imports, and can be sold or leased. Sugar inside finished foods, blends with 65% sugar or less, corn syrup, and up to 10 kg carried by a traveler are not covered.

**Visible consequences.** Fewer imports (C-1) and a higher price for Calvarian beet growers (C-2).

**Invisible consequences.**
- *Buyers of sugar* pay more (C-3), and households pay more for locally made sweetened goods such as bread and pastry (C-16); for confectionery and soft drinks, imports hold the price near the import price. They give up the other goods that money would have bought (C-27), and buy less sugar in total (C-25).
- *Importers who held the base-period trade* receive a valuable asset for free (C-5); because foreign supply is competitive, they rather than foreign sellers keep most of the gap between the domestic and world price (section 7, DM-4). They rushed imports into the announcement window to enlarge their shares (C-6). New importers must buy their way in (C-7).
- *Food manufacturers* switch to corn syrup where they can (C-8), import sugar as blends just under the threshold (C-9), at a cost (C-32), and, for goods that compete with imports, move production abroad over the years (C-10, C-22), with fewer jobs or hours in Calvar (C-17). Firms already using corn syrup pay more for it (C-13).
- *Landowners* near the beet factories see their land gain value (C-15); land that switches to beet stops growing other crops (C-26).
- *The port refineries* refine less, use less labor in jobs or hours (C-18, C-19), and over the long run keep less refining capacity (C-31). *Beet factories* use more labor (C-30).
- *Near the border*, Varnholt residents buy sugar in Ostria and take other shopping with them, to the benefit of Ostrian shops and the cost of Varnholt's (C-11, C-20, C-21).
- *Taxpayers* fund customs work (C-29, C-34); importers bear paperwork (C-28).
- *Calvarian export industries* sell less abroad over time, because foreigners who sell less sugar to Calvar have less Calvarian money to spend on its exports (C-23), and those industries use less labor, in jobs or hours (C-33).

**Ambiguous effects.** Whether the port refineries gain or lose overall: their quota rents push one way (if they hold rights, A-20), their lost throughput the other. Not signed: the price of tradable sweetened goods, which imports hold near the import price.

**Key conditions.** The quota binds (A-1, p = 0.95). How far manufacturers relocate depends on how freely finished goods are imported (A-9, p = 0.75). Asset values and new beet capacity depend on expectations about the five-year review (A-5, p = 0.65).

**What this analysis cannot say.** How large any effect is; whether growers' and quota holders' gains outweigh buyers', manufacturers' and their workers' losses; exactly how much of the gap foreign sellers capture; health effects of lower sugar use (out of scope for version 1); whether the policy is desirable.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | quota_holders, exporters.foreign | quantity_traded (imports) | decrease | short | visible | B | EN-6 | A-1, A-2 |
| C-2 | growers.beet | net_price_received | increase | short | visible | B | EN-6 | A-1, A-2, A-3 |
| C-3 | buyers.sugar | price_paid (sugar) | increase | short (growing) | invisible | B | EN-6, TS-3 | A-1, A-2 |
| C-4 | growers.beet | quantity_supplied | increase | medium | invisible | B | EN-6, LW-4 | A-1, A-4 |
| C-5 | quota_holders | asset_value (quota shares) | increase | short | invisible | B | EN-6, SB-4 | A-1, A-2, A-5 |
| C-6 | quota_holders | quantity_traded (imports, announcement window) | increase | short | invisible | B | RS-8 | A-6 |
| C-7 | importers.prospective | entry_rate | decrease | short–medium | invisible | B | EN-6, SB-4 | A-1, A-2 |
| C-8 | manufacturers.tradable, manufacturers.local | quantity_substitute (corn syrup) | increase | short–medium | invisible | B | RS-1 | A-1, A-7 |
| C-9 | manufacturers.tradable | reclassification | increase | short–medium | invisible | B | RS-5 | A-8 |
| C-10 | manufacturers.tradable | quantity_supplied (domestic) | decrease | medium–long | invisible | B | RS-14, RS-6, RS-4, TS-1 | A-1, A-9, A-10 |
| C-11 | households.varnholt | cross_border_purchases | increase | short | invisible | B | RS-4 | A-1, A-11 |
| C-12 | growers, quota_holders, manufacturers | lobbying_effort | increase | medium | invisible | B | RS-7 | A-1, A-21 |
| C-13 | sweetener_users | price_substitute (corn syrup) | increase | short–medium | invisible | B | RS-1 | A-7, A-13 |
| C-14 | sweetener_makers | quantity_supplied (corn syrup) | increase | medium | invisible | B | RS-1, LW-4 | A-7 |
| C-15 | landowners.beet | asset_value (beet land) | increase | short–medium | invisible | B | SB-4, LW-4 | A-4, A-5 |
| C-16 | households | price_paid (locally made sweetened goods) | increase | short–medium | invisible | B | EN-6, RS-14 | A-1, A-14 |
| C-17 | manufacturers.tradable (workers) | employment, hours_worked | at_least_one_decrease | medium–long | invisible | B | RS-14, RS-6, RS-4 | A-1, A-9, A-10 |
| C-18 | refiners.port | quantity_supplied | decrease | short | invisible | B | EN-6 | A-1, A-2 |
| C-19 | refiners.port (workers) | employment, hours_worked | at_least_one_decrease | medium | invisible | B | RS-6 | A-1, A-15 |
| C-20 | ostria.sellers (shops) | quantity_traded (all goods) | increase | short | invisible | B | RS-4, RS-9 | A-11, A-16 |
| C-21 | retailers.varnholt | quantity_traded (other groceries) | decrease | short | invisible | B | RS-4, RS-9 | A-11, A-16 |
| C-22 | ostria.sellers (manufacturers) | quantity_supplied (into Calvar) | increase | medium | invisible | B | RS-4 | A-9 |
| C-23 | exporters.calvar | quantity_supplied | decrease | medium | invisible | B | EN-6, TX-8 | A-17 |
| C-24 | growers.beet | investment_target (factory capacity) | increase | long | invisible | B | EN-6, LW-4, TS-2 | A-4, A-5 |
| C-25 | buyers.sugar, exporters.foreign | quantity_traded (all sugar in Calvar) | decrease | short | invisible | B | OC-4 | A-1, A-2 |
| C-26 | buyers.field_crops | quantity_traded (field crops) | decrease | medium | invisible | B | OC-1, LW-4 | A-4 |
| C-27 | buyers.sugar | resources_available_other_uses | decrease | short | invisible | B | EN-6, LW-1 | A-1, A-2, A-19 |
| C-28 | quota_holders, importers.prospective | compliance_cost | increase | short | invisible | A | OC-2 | none |
| C-29 | taxpayers | resources_available_other_uses | decrease | short | invisible | B | OC-3, OC-1 | A-22 |
| C-30 | workers.beet_factories | employment, hours_worked | at_least_one_increase | medium | invisible | B | EN-6, CR-9 | A-1, A-4 |
| C-31 | refiners.port | capital_stock_target (refining capacity) | decrease | long | invisible | B | RS-6, TS-1 | A-1, A-15 |
| C-32 | manufacturers.tradable | compliance_cost (blends) | increase | short–medium | invisible | B | OC-1, CR-8c | A-8 |
| C-33 | exporters.calvar (workers) | employment, hours_worked | at_least_one_decrease | medium | invisible | B | TX-8, OC-5 | A-17 |
| C-34 | officials.enforcement | enforcement_cost | increase | short | invisible | A | OC-3 | none |
| — | refiners.port | return_on_capital | ambiguous | medium | invisible | B | C-5 vs C-18, C-19 | A-1, A-2, A-15, A-20 |

## Gaps found

- GAP-014-1 (closed in catalog 0.3: TX-8 widened to import quotas). C-23 is now Tier B, derived from EN-6 and TX-8, resting on A-17.
- GAP-014-2 (closed in catalog 0.3: DM-4). Section 7 now reports that holders of quota rights capture most of the gap between the domestic and world price, resting on A-18.
- GAP-014-3 (closed in catalog 0.3: EN-6 widened to domestic sellers of the restricted good). C-2 and C-4 now follow from EN-6 directly.

Also applied on the update to catalog 0.3: TS-3 (widened to parameters fixed in physical units) for the tonnage quota (C-3, section 8); RS-14 for the pass-through of dearer sugar to sweetened goods (C-10, C-16, C-17). Review corrections: C-27 now carries the assumption it needed about buyers' total spending (A-19); the refiners' combined effect uses `return_on_capital` rather than `earnings`, which measures labor income; two real place names were replaced with fictional ones.

- Catalog 0.5: corrected after the core-only comparison (see ../05_examples_core/WE-014_sugar_import_quota_core.md): the refinery row now states its premise that the refineries hold rights (A-20); RS-7's organization premise estimated (A-21); C-16 limited to locally made goods and the tradable-goods price no longer signed; labor effects recorded as RS-6 groups (C-17, C-19, new C-33 split from C-23); added beet-factory labor (C-30), refining capacity (C-31), the cost of reshaping into blends (C-32) and enforcement cost (C-34); OC-3 funding stated (A-22).
