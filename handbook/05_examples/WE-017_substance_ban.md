# WE-017 Ban on a recreational plant product, with penalties scaled to weight

Analyst: draft (Handbook 0.5)  |  Rule catalog version: 0.5  |  Status: awaiting expert review

A stylized policy in a fictional state, about a fictional substance. It resembles real bans on mildly psychoactive plant products that had been sold legally, but is not modeled on any one of them, and it is kept apart from the historical cases reserved for evaluation. The probabilities are illustrative; the evidence column says what a real analysis would cite.

## 1. Policy record

**Corrin Lirva Control Act.** Lirva is the dried leaf of the lirva shrub, brewed as tea or chewed for a mild stimulant and relaxing effect. It has been sold legally in the State of Corrin (about 6 million people) for fifteen years, in about 400 specialist tea shops, in convenience stores and online, and has been subject to the general sales tax. About 180,000 adults use it regularly. A typical dose is about 5 g of leaf. A concentrated extract, made by soaking the leaf in alcohol and drying the result, gives the same effect at about 0.25 g; it is about 5% of current sales. The neighboring state of Halvet keeps lirva legal; its border is 40 to 90 minutes' drive from Corrin's two largest cities. The Act was passed six months before it took effect.

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Prohibition | `prohibition` | Making, selling, possessing for sale, importing and growing lirva, its active compound lirvine, and any product containing either | Everyone | From the effective date. | Licensed research |
| K2 Penalties | Part of K1 | Possession and sale | Everyone | Graded by the total weight of material, including any carrier or mixture. Possession under 50 g: civil fine of $250. 50 g to 1 kg: misdemeanor, up to 1 year. Over 1 kg: felony, 2 to 10 years. Sale is punished one grade higher than possession of the same weight. | None |
| K3 Transition | Part of K1 | Existing stocks | Licensed sellers | Stocks must be destroyed or exported by the effective date. No compensation. | None |
| K4 Enforcement | Enforcement | K1 to K3 | State police drug unit, local police, state laboratory | Added budget for investigators and lab testing, from the general budget. | None |

Unclear provisions: whether related plants with similar compounds are covered. The Act names only lirva and lirvine, so they are assumed not covered.

Note on K2: 50 g of leaf is about 10 doses; 50 g of extract is about 200. Penalties graded by weight treat the two very differently per dose.

## 2. Classification

| Component | Rothbard type | Binding? | Rule families |
|---|---|---|---|
| K1, K2 | Triangular: prohibits exchanges between users and sellers; for growing for one's own use, autistic | Yes: demand is established (A-1) | EN-7, EN-8, EN-10, RS, RS-10, TX-10 |
| K3 | Triangular: forbids sale of existing stocks in Corrin | Yes | OC-1, RS-8, SB-4 |
| K4 | Binary: funded by taxpayers | Yes | OC-3 |

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `users.current` (`buyers.current`) | Regular users | Can stockpile before the date, buy in Halvet, buy informally, switch, or stop. |
| `users.mobile` | Users within reach of the Halvet border | Can buy legally in Halvet and carry home small amounts. |
| `users.informal` | Users who buy from informal sellers | Buy without brands, reviews or recourse. |
| `users.prospective` (`buyers.prospective`) | People who would have started using lirva | No legal shops; higher price and risk. |
| `shops.lirva` (`sellers.current`) | Specialist shops and their staff | Must stop selling lirva; destroy or export stock. |
| `importers.lirva` (`input_suppliers`) | Importers and wholesalers supplying the shops | May no longer import or sell lirva in Corrin. |
| `sellers.informal` | Former sellers and new entrants who sell illegally | Can earn a risk premium, at the risk of penalties. |
| `sellers.substitutes` | Sellers of legal substitutes (alcohol, other herbal products, unlisted related plants) | More demand. |
| `halvet.sellers` (`neighboring_jurisdictions`) | Lirva sellers in Halvet near the border | More Corrin customers. |
| `users.convicted` | Users and sellers convicted under K2 | Carry a record. |
| `officials.enforcement`, `taxpayers` | Police, laboratory, courts and prisons, and their funders | New enforcement work; lost sales-tax base. |

## 4. Direct effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | `shops.lirva`, `users.current` | `quantity_traded` (legal lirva) | decrease (to near zero) | short | EN-7 | A-2 |
| C-2 | `shops.lirva` | `number_of_sellers` (legal) | decrease (to near zero) | short | EN-7 | A-2 |

The visible aim: lirva disappears from shop shelves. Licensed shops are easy to find and inspect, so legal sales stop almost entirely (A-2). How much less lirva is used is a different question, taken up in section 7.

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-3 | `sellers.informal` | `informal_activity` | increase | short | EN-7, RS-3 | A-1, A-3 |
| C-4 | `users.current` | `price_paid` (per dose, all sources in Corrin) | increase | short | EN-7 | A-1, A-4 |
| C-5 | `users.current` | `quantity_demanded` (legal lirva in the announcement window: stockpiling) | increase | short | RS-8 | A-5 |
| C-6 | `users.mobile` | `cross_border_purchases` (lirva in Halvet, carried home in amounts under 50 g) | increase | short | RS-4 | A-1, A-6 |
| C-7 | `users.current` | `quantity_substitute` (alcohol, other legal herbal products) | increase | short | RS-1 | A-7 |
| C-8 | `sellers.substitutes`, `sellers.informal` | `reclassification` (related plants and blends outside the Act's definitions, sold as lirva alternatives) | increase | short to medium | RS-5 | A-8 |
| C-9 | `sellers.informal` | `share_concentrated_forms` (extract rather than leaf) | increase | medium | EN-7, EN-8 | A-1, A-9, A-10 |
| C-10 | `shops.lirva` | `employment` (lirva retail) | decrease | short | EN-7, RS-6 | A-2, A-11 |
| C-11 | `users.current`, `shops.lirva` | `lobbying_effort` (for repeal or for a personal-use exemption) | increase | medium | RS-7 | A-12 |
| C-29 | `shops.lirva` | `inventory_held` (lirva, at the effective date) | decrease | short | RS-8, K3 | A-2 |
| C-30 | `users.current` | `price_paid` (legal lirva, final weeks before the effective date) | ambiguous | short | RS-8, CR-6, CR-12b (section 7) | A-2, A-5 |

C-10: lirva retail itself is removed (CR-1, operation 1), not merely made less profitable, so the jobs in it go with it; RS-6's group form (employment or hours) is not needed for this activity. Whether the staff find other work is not signed here.

C-29, C-30: stock left at the effective date must be destroyed or exported without compensation (K3), so shops stop reordering and run their stock down before the date (RS-8, CR-4c with x: reorder, y: run stock down). In the final weeks, users' stockpiling (C-5) raises planned purchases while shops clear stock they would otherwise lose; the two push the legal price in opposite directions.

C-4: the price rises because informal sellers must be paid for the risk of punishment and for operating without shops, advertising or scale (EN-7). This holds only if the risk is real (A-4).

C-9: under K2 the penalty depends on weight, and a dose of extract weighs about a twentieth of a dose of leaf. A seller carrying the same number of doses faces a much lower penalty grade with extract, and extract is easier to hide. Sellers shift toward extract (EN-8), recorded with the variable `share_concentrated_forms`.

Not reported:
- Bundled shopping in Halvet (RS-9). Trips to buy lirva are short, special-purpose trips; that users also do other shopping on them rests on A-13 (p = 0.4), below the cut-off.
- Violence in settling disputes. RS-10 says that disputes in informal trade cannot go to court and are settled privately or not at all (C-15). Whether they are settled by force on a meaningful scale is a separate empirical claim. It needs informal supply to be organized by groups with high-value territories or stocks to defend, which for a bulky, mild, low-margin plant sold mostly by small sellers and cross-border carriers is put at A-14, p = 0.3, below the cut-off. Even if it were reported, violence is a safety outcome, which version 1 does not measure. It would become more likely if the shift to extract (C-9) concentrated value in fewer, larger stocks; that is a question for a later version, not a conclusion here.

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-12 | `users.informal` | `search_cost` | increase | short | RS-10 | | A-3 |
| C-13 | `users.informal` | `quality_variability` (spread of potency and purity between units) | increase | short to medium | RS-10 | | A-3 |
| C-24 | `users.informal` | `quality_information` (no brands, labels, reviews or recourse) | decrease | short | RS-10 | | A-3 |
| C-14 | `halvet.sellers` | `quantity_traded` (lirva) | increase | short | RS-4 | Corrin and Halvet lirva markets: `across_border`, partial (40 to 90 minutes) | A-6 |
| C-15 | `users.informal`, `sellers.informal` | `disputes_settled_outside_courts` | increase | short | RS-10 | | A-3 |
| C-16 | `officials.enforcement` | `enforcement_cost` (investigation, lab testing, courts, prisons) | increase | short to long | OC-3 | | none |
| C-17 | `officials.enforcement`, `taxpayers` | `tax_revenue` (general sales tax) | decrease | short | TX-10 | | A-1, A-3, A-6 |
| C-18 | `users.convicted` | `employment` | decrease | long | EN-10 | | A-4, A-16 |
| C-19 | `users.prospective` | `quantity_demanded` (lirva) | decrease | long | EN-7, LW-3 | | A-1, A-4 |
| C-27 | `shops.lirva` | `asset_value` (shop businesses: fittings, leases, goodwill, stock) | decrease | short (at passage) | SB-4 | | A-2, A-11 |
| C-28 | `importers.lirva` | `quantity_traded` (legal lirva imports into Corrin) | decrease | short | EN-7, CR-9 | importers and shops: `input_to`, close | A-2 |

C-12, C-13, C-15, C-24 are RS-10 applied to the informal trade in C-3. Informal sellers cannot advertise, so users spend more time finding them (C-12). With no brands, labels or reviews, users can judge a seller's product less well before buying (C-24), and with extract (C-9) easy to dose wrongly, the strength of what they buy varies more from unit to unit (C-13). Disputes over short weight or bad product cannot go to court (C-15). Whether such disputes involve violence is discussed in section 5 and not reported (`06_gaps.md`, Q15).

C-17: lirva was subject to the general sales tax, and the ban removes that base (TX-10). Spending that moves to other legal goods pays the same general rate, so it only replaces the revenue lost on lirva; spending that moves to informal sellers and to Halvet is untaxed in Corrin (C-3, C-6). For the general sales tax the sign is therefore a decrease. Excise taxes on substitutes such as alcohol are a separate question (section 7).

C-27: the ban is a lasting fall in the expected return of businesses built around lirva, whose fittings, leases and goodwill have few other uses (A-11). By SB-4 their value falls when the ban becomes expected, at passage, six months before the effective date, and the owners at that time bear it. This is the capitalized form of the loss; the stock destroyed or sold abroad at a discount is C-21.

C-18 is at depth 4 (ban, informal trade, conviction, later job search): EN-10 links a recorded conviction to later employment, given that records are kept and checked (A-16) and that enforcement produces convictions (A-4).

Stopping points: landlords of closed shop premises are diffuse at depth 3; stopped. RS-11 was checked: no benefit here is lost by moving; it does not apply.

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `users.current`, `quantity_demanded` (lirva from all sources, after the effective date), short to medium | None. | Higher price per dose (C-4), search (C-12), legal risk, and switching (C-7). Stockpiles bought in the window (C-5) also replace purchases in the first months (CR-10a): they keep consumption up, but push purchases after the date down. | None needed | **decrease** (C-25), but by much less than legal sales (C-1), because part of the trade moves to Halvet and to informal sellers (C-3, C-6) rather than stopping. The stockpile only shifts some purchases in time. |
| `users.current`, `price_paid` (legal lirva, final weeks before the effective date), short | Stockpiling raises planned purchases (C-5; CR-6). | Shops clear stock they must otherwise destroy or export (C-29; CR-4). | None | **ambiguous** (C-30). |
| `officials.enforcement`, `taxpayers`, `tax_revenue` (all state taxes, including excises), short | Spending that moves to legal substitutes carrying an excise on top of the sales tax, such as alcohol, adds excise revenue (C-7, A-15). | Sales tax on spending that moves to informal and Halvet sellers is lost (C-17). | None | **ambiguous** (C-26; TX-10). Decided by how much lirva spending moves to excised substitutes, against how much moves to untaxed informal and cross-border purchases. The general sales tax alone decreases (C-17). |
| `sellers.informal`, `earnings`, medium | The risk premium in the price (C-4). | Fines, seizures, prison terms, and selling without shops or scale. | None | **ambiguous** (C-20). Those who choose to sell informally expect to do better than their next-best option under the ban (LW-5); that says nothing about how they fare compared with legal selling in the counterfactual. |

## 8. Time structure

- **Announcement window (six months).** Users stockpile (C-5), shops stop reordering and run clearance sales (C-29), and the legal price in the final weeks moves either way (C-30). The value of shop businesses falls at passage, not at the effective date (C-27); importers lose their trade (C-28). Dried leaf keeps for about a year (A-5), so the informal market is thin in the first months and grows as stockpiles run down over the first year.
- **Short run: leaf and the border.** Early informal supply is mostly leaf carried from Halvet in amounts under 50 g, where the penalty is a civil fine (C-6). Price rises at once (C-4) but supply chains are still forming.
- **Medium run: concentration.** As enforcement targets larger quantities, and informal sellers learn that weight sets the penalty, supply shifts to extract (C-9). Because extract is easier to dose wrongly and its strength depends on how it was made, quality variability (C-13) grows with the shift, not at once.
- **Enforcement costs lag.** Investigation and lab testing start at once, but prison costs build up over years as felony sentences of 2 to 10 years accumulate (C-16, long). Effects of criminal records on employment (C-18) appear over the long run.
- **Fewer new users.** With no shops, and a higher price and risk, fewer people start using lirva (C-19); this shows over the long run as the user population turns over.
- **Expectations.** If repeal is expected (Halvet keeps lirva legal; lobbying, C-11), informal sellers invest less in supply networks and users hold small stocks rather than switching for good (TS-2). If tightening is expected, the shift to extract comes sooner.

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-21 | `shops.lirva` | `resources_available_other_uses` | decrease | Stock destroyed or sold abroad at a discount without compensation; fixtures and know-how specific to lirva. | OC-1 |
| C-22 | `users.mobile` | `search_cost` (travel to Halvet) | increase | Time and travel cost of buying across the border. | OC-2 |
| C-23 | `taxpayers`, `recipients.other_spending`, `taxpayers.future` | `resources_available_other_uses` | at_least_one_decrease | What the enforcement budget (C-16) would otherwise have funded: higher taxes, other spending its recipients no longer receive, or later taxes. | OC-3, OC-1 (who pays) |

C-23: OC-3's funding case. K4 adds budget for the new task from the general budget, so the cost does not fall on other enforcement. The record names no tax, so by OC-1 (who pays) the payers are a group: taxpayers, recipients of other spending and future taxpayers, at least one of whom loses.

Prevented exchanges are recorded as C-1 and are not listed again.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | A meaningful share of regular users keep using lirva after the ban. | other | 0.9 | Fifteen years of legal use; user surveys; experience of comparable bans. | C-3, C-4, C-6, C-9 shrink; the ban mainly ends use. |
| A-2 | Licensed shops comply. | enforcement | 0.95 | Visible, licensed premises; inspection powers. | C-1, C-2, C-27 to C-30 weaker; shops sell under the counter. |
| A-3 | Enforcement is imperfect: many informal sales go undetected. | enforcement | 0.85 | Police budget relative to the number of users; experience of comparable bans. | C-3, C-12, C-13, C-15, C-24 weaken; C-17 weakens; C-18 grows. |
| A-4 | Enforcement is active enough that informal sellers face a real risk. | enforcement | 0.8 | Added budget; arrest targets; sentencing. | C-4, C-19 and C-25 weaken; C-18 is smaller. |
| A-5 | Users know the date and can store dried leaf for months. | expectations | 0.75 | Publicity of the Act; shelf life of about a year. | C-5 and C-30 not reported. |
| A-6 | Enough users live within reach of Halvet and will carry home amounts under 50 g. | mobility | 0.65 | Distance to the border (40 to 90 minutes); car ownership; size of the civil fine. | C-6, C-14, C-22 not reported; C-17 weakens. |
| A-7 | Legal substitutes are acceptable to some users. | substitutability | 0.8 | Survey data on what users would switch to. | C-7 weakens; C-26 becomes a decrease. |
| A-8 | Related plants and blends outside the definitions can be sold. | other | 0.6 | Botanical relatives with similar compounds; the Act's wording. | C-8 not reported. |
| A-9 | Penalties are graded by the total weight of material. | enforcement | 0.95 | Act text (K2). | C-9 not reported. |
| A-10 | Extract can be made with simple equipment. | other | 0.75 | Current extract sales; method (alcohol soaking). | C-9 weakens. |
| A-11 | Specialist shops cannot replace lirva sales with other products for most of their staff. | alternative_uses | 0.85 | Share of shop revenue from lirva. | C-10 and C-27 weaken. |
| A-12 | Users and former shop owners can organize. | other | 0.6 | Existing trade association of shops; user groups. | C-11 not reported. |
| A-13 | Users bundle other shopping with lirva trips to Halvet. | other | 0.4 | Trip surveys; what is sold near the border. | Below cut-off; not reported. |
| A-14 | Informal supply is organized by groups that settle disputes by force on a meaningful scale. | other | 0.3 | Value per unit; scale of sellers; experience with comparable mild substances. | Below cut-off; not reported, and outside version 1 variables. |
| A-15 | Some lirva spending moves to substitutes that carry an excise on top of the general sales tax, such as alcohol. | substitutability | 0.6 | Survey data on what users would switch to (A-7); Corrin's excise rates on alcohol and herbal products. | C-26 becomes a decrease. |
| A-16 | Convictions are recorded and employers check them. | other | 0.6 | Record-keeping rules; background-check practice in Corrin. | C-18 not reported. |

## 11. Report

**The policy.** Corrin bans making, selling and possessing lirva, a mild plant product that has been sold legally for fifteen years. Penalties are graded by the weight of the material, from a civil fine under 50 g to prison over 1 kg. Shops had six months to sell, destroy or export their stock. The neighboring state keeps lirva legal.

**Visible consequences.** Lirva leaves the shelves: legal sales and legal sellers fall to almost nothing (C-1, C-2).

**Invisible consequences.**
- *Users* stockpiled before the date (C-5), and afterwards pay more per dose (C-4). Some buy in Halvet and carry home small amounts (C-6, C-22); some switch to alcohol or other products (C-7); some buy from informal sellers, who are harder to find (C-12), whose product is harder to judge in advance (C-24) and varies more in strength (C-13). Disputes with sellers cannot go to court (C-15). Total use falls, by less than legal sales do (C-25), and fewer people start using lirva (C-19).
- *Sellers* shift toward extract, because the penalty depends on weight and extract packs about twenty times as many doses into a gram (C-9). Products from related plants are sold as alternatives (C-8).
- *Shops* lose the value of their businesses as soon as the Act passes (C-27), run their stock down before the date (C-29), lose what stock remains, and their staff lose their jobs in lirva retail (C-21, C-10). Importers lose their trade (C-28). Halvet shops gain (C-14).
- *The state* spends more on police, laboratories, courts and, over the years, prisons (C-16), funded from the general budget: by taxpayers, recipients of other spending or future taxpayers (C-23). The general sales tax loses the part of lirva spending that moves to informal and Halvet sellers (C-17). Those convicted find it harder to get jobs later (C-18).
- Users and former shop owners lobby for repeal (C-11).

**Ambiguous effects.** The legal price in the last weeks before the ban (C-30). Total state tax revenue, counting excises on substitutes such as alcohol as well as the sales tax (C-26). Whether informal sellers earn more or less than they would have selling legally (C-20).

**Key conditions.** That demand persists (A-1, p = 0.9) and enforcement is imperfect but real (A-3, p = 0.85; A-4, p = 0.8). The shift to extract rests on the weight-based penalties in the Act itself (A-9). Violence in the informal trade is not reported: it rests on an assumption below the cut-off (A-14, p = 0.3), and it is in any case a safety outcome outside version 1.

**What this analysis cannot say.** How much less lirva is used; health and safety effects, including any violence (out of scope for version 1); whether reduced use is worth the costs to users, sellers and taxpayers; whether the policy is desirable.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | shops.lirva, users.current | quantity_traded (legal) | decrease | short | visible | B | EN-7 | A-2 |
| C-2 | shops.lirva | number_of_sellers (legal) | decrease | short | visible | B | EN-7 | A-2 |
| C-3 | sellers.informal | informal_activity | increase | short | invisible | B | EN-7, RS-3 | A-1, A-3 |
| C-4 | users.current | price_paid (per dose) | increase | short | invisible | B | EN-7 | A-1, A-4 |
| C-5 | users.current | quantity_demanded (announcement window) | increase | short | invisible | B | RS-8 | A-5 |
| C-6 | users.mobile | cross_border_purchases | increase | short | invisible | B | RS-4 | A-1, A-6 |
| C-7 | users.current | quantity_substitute | increase | short | invisible | B | RS-1 | A-7 |
| C-8 | sellers.substitutes, sellers.informal | reclassification | increase | short–medium | invisible | B | RS-5 | A-8 |
| C-9 | sellers.informal | share_concentrated_forms | increase | medium | invisible | B | EN-7, EN-8 | A-1, A-9, A-10 |
| C-10 | shops.lirva | employment (lirva retail) | decrease | short | invisible | B | EN-7, CR-1 (the activity is removed) | A-2, A-11 |
| C-11 | users.current, shops.lirva | lobbying_effort | increase | medium | invisible | B | RS-7 | A-12 |
| C-12 | users.informal | search_cost | increase | short | invisible | B | RS-3, RS-10 | A-3 |
| C-13 | users.informal | quality_variability | increase | short–medium | invisible | B | RS-3, RS-10 | A-3 |
| C-14 | halvet.sellers | quantity_traded | increase | short | invisible | B | RS-4 | A-6 |
| C-15 | users.informal, sellers.informal | disputes_settled_outside_courts | increase | short | invisible | B | RS-3, RS-10 | A-3 |
| C-16 | officials.enforcement | enforcement_cost | increase | short–long | invisible | A | OC-3 | none |
| C-17 | officials.enforcement, taxpayers | tax_revenue (general sales tax) | decrease | short | invisible | B | EN-7, TX-10 | A-1, A-3, A-6 |
| C-18 | users.convicted | employment | decrease | long | invisible | B | EN-7, EN-10 | A-4, A-16 |
| C-19 | users.prospective | quantity_demanded | decrease | long | invisible | B | EN-7, LW-3 | A-1, A-4 |
| C-20 | sellers.informal | earnings | ambiguous | medium | invisible | B | C-4 vs penalties | A-1, A-3, A-4 |
| C-21 | shops.lirva | resources_available_other_uses | decrease | short | invisible | A | OC-1 | none |
| C-22 | users.mobile | search_cost | increase | short | invisible | B | OC-2 | A-6 |
| C-23 | taxpayers, recipients.other_spending, taxpayers.future | resources_available_other_uses | at_least_one_decrease | short | invisible | A | OC-3, OC-1 (who pays) | none |
| C-24 | users.informal | quality_information | decrease | short | invisible | B | RS-3, RS-10 | A-3 |
| C-25 | users.current | quantity_demanded (all sources, after the effective date) | decrease | short–medium | invisible | B | EN-7, RS-1 | A-1, A-4 |
| C-26 | officials.enforcement, taxpayers | tax_revenue (all state taxes, including excises) | ambiguous | short | invisible | B | C-17 vs C-7 (TX-10) | A-6, A-7, A-15 |
| C-27 | shops.lirva | asset_value (shop businesses) | decrease | short | invisible | B | SB-4 | A-2, A-11 |
| C-28 | importers.lirva | quantity_traded (legal imports) | decrease | short | invisible | B | EN-7, CR-9 | A-2 |
| C-29 | shops.lirva | inventory_held (at the effective date) | decrease | short | invisible | B | RS-8, K3 | A-2 |
| C-30 | users.current | price_paid (legal, final weeks) | ambiguous | short | invisible | B | RS-8, CR-6 vs CR-4; CR-12b | A-2, A-5 |

## Gaps found

- GAP-017-1 (closed in catalog 0.3: `quality_variability` and `quality_information`, named in RS-10). C-13 is now Tier B; C-24 added for `quality_information`.
- GAP-017-2 (closed in catalog 0.3: `disputes_settled_outside_courts`). C-15 is now Tier B. Whether violence in settling disputes should get a variable remains open: Q15 (A-14 here).
- GAP-017-3 (closed in catalog 0.3: TX-10). C-17 is now Tier B. On review its sign is corrected from ambiguous to decrease: under a general sales tax, spending that moves to other legal goods pays the same rate and only replaces the lost revenue, while spending that moves to informal and cross-border sellers is untaxed. The ambiguity belongs to total revenue across all taxes, including excises on substitutes, now C-26.
- GAP-017-4 (closed in catalog 0.3: EN-10). C-18 is now Tier B, resting on A-4 (convictions happen) and A-16 (records are checked); it previously cited A-3, which concerns undetected sales.
- GAP-017-5 (closed in catalog 0.3: `share_concentrated_forms`, used in EN-8). C-9 now uses it with a plain increase.

Also on the update: users' total use, previously a prose row in section 7, is now C-25 (`quantity_demanded`, all sources), and A-15's type is corrected from `revenue_use` to `substitutability`.
- Catalog 0.5: corrected after the core-only comparison (see ../05_examples_core/WE-017_substance_ban_core.md): added the fall in shop businesses' value at passage (C-27, SB-4), importers' lost trade (C-28), shops running stock down before the date (C-29) and the ambiguous legal price in the final weeks (C-30); stockpiles moved from a (+) to a (−) chain on purchases after the date in section 7 (sign unchanged); C-10 rederived from the removal of the activity rather than RS-6; OC-3's funding case stated.
- Catalog 1.4: C-23 corrected to follow OC-1's who-pays clause. The record names no tax, so the payers are the group of taxpayers, recipients of other spending and future taxpayers (`at_least_one_decrease`), not taxpayers alone.
