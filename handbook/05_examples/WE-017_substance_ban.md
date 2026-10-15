# WE-017 Ban on a recreational plant product, with penalties scaled to weight

Analyst: draft (Handbook 0.2)  |  Rule catalog version: 0.2  |  Status: awaiting expert review

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
| K1, K2 | Triangular: prohibits exchanges between users and sellers; for growing for one's own use, autistic | Yes: demand is established (A-1) | EN-7, EN-8, RS, RS-10 |
| K3 | Triangular: forbids sale of existing stocks in Corrin | Yes | OC-1, RS-8 |
| K4 | Binary: funded by taxpayers | Yes | OC-3 |

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `users.current` (`buyers.current`) | Regular users | Can stockpile before the date, buy in Halvet, buy informally, switch, or stop. |
| `users.mobile` | Users within reach of the Halvet border | Can buy legally in Halvet and carry home small amounts. |
| `users.informal` | Users who buy from informal sellers | Buy without brands, reviews or recourse. |
| `users.prospective` (`buyers.prospective`) | People who would have started using lirva | No legal shops; higher price and risk. |
| `shops.lirva` (`sellers.current`) | Specialist shops and their staff | Must stop selling lirva; destroy or export stock. |
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
| C-9 | `sellers.informal` | `variety` (composition shifts toward extract and away from leaf) | increase in the share of concentrated forms | medium | EN-8 | A-1, A-9, A-10 |
| C-10 | `shops.lirva` | `employment` (lirva retail) | decrease | short | EN-7, RS-6 | A-2, A-11 |
| C-11 | `users.current`, `shops.lirva` | `lobbying_effort` (for repeal or for a personal-use exemption) | increase | medium | RS-7 | A-12 |

C-4: the price rises because informal sellers must be paid for the risk of punishment and for operating without shops, advertising or scale (EN-7). This holds only if the risk is real (A-4).

C-9: under K2 the penalty depends on weight, and a dose of extract weighs about a twentieth of a dose of leaf. A seller carrying the same number of doses faces a much lower penalty grade with extract, and extract is easier to hide. Sellers shift toward extract (EN-8). The sign is written as a shift in composition because `variety` counts versions rather than measuring their mix (see GAP-017-5).

Not reported:
- Bundled shopping in Halvet (RS-9). Trips to buy lirva are short, special-purpose trips; that users also do other shopping on them rests on A-13 (p = 0.4), below the cut-off.
- Violence in settling disputes. RS-10 says that disputes in informal trade cannot go to court and are settled privately or not at all (C-15). Whether they are settled by force on a meaningful scale is a separate empirical claim. It needs informal supply to be organized by groups with high-value territories or stocks to defend, which for a bulky, mild, low-margin plant sold mostly by small sellers and cross-border carriers is put at A-14, p = 0.3, below the cut-off. Even if it were reported, violence is a safety outcome, which version 1 does not measure. It would become more likely if the shift to extract (C-9) concentrated value in fewer, larger stocks; that is a question for a later version, not a conclusion here.

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-12 | `users.informal` | `search_cost` | increase | short | RS-10 | | A-3 |
| C-13 | `users.informal` | `quality_variability` (proposed: spread of potency and purity between units) | increase | short to medium | RS-10, GAP-017-1 | | A-3 |
| C-14 | `halvet.sellers` | `quantity_traded` (lirva) | increase | short | RS-4 | Corrin and Halvet lirva markets: `across_border`, partial (40 to 90 minutes) | A-6 |
| C-15 | `users.informal`, `sellers.informal` | `disputes_settled_outside_courts` (proposed) | increase | short | RS-10, GAP-017-2 | | A-3 |
| C-16 | `officials.enforcement` | `enforcement_cost` (investigation, lab testing, courts, prisons) | increase | short to long | OC-3 | | none |
| C-17 | `officials.enforcement`, `taxpayers` | `tax_revenue` (state sales tax, all goods) | ambiguous | short | GAP-017-3 | | A-7, A-15 |
| C-18 | `users.convicted` | `employment` | decrease | long | GAP-017-4 | | A-3, A-16 |
| C-19 | `users.prospective` | `quantity_demanded` (lirva) | decrease | long | EN-7, LW-3 | | A-1, A-4 |

C-12, C-13, C-15 are RS-10 applied to the informal trade in C-3. Informal sellers cannot advertise, so users spend more time finding them (C-12). With no brands, labels or reviews, and with extract (C-9) easy to dose wrongly, the strength of what users buy varies more from unit to unit (C-13). The catalog has no variable for that spread, so C-13 is Tier C. Disputes over short weight or bad product cannot go to court (C-15); the catalog has no variable for this either, so C-15 is Tier C. Whether such disputes involve violence is discussed in section 5 and not reported.

C-18 is at depth 4 (ban, informal trade, conviction, later job search) and is Tier C: no rule links a criminal record to later employment (GAP-017-4).

Stopping points: landlords of closed shop premises are diffuse at depth 3; stopped. RS-11 was checked: no benefit here is lost by moving; it does not apply.

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| Corrin users' total use of lirva (from all sources), short to medium | Stockpiles bought in the window (C-5) keep use up in the first months. | Higher price per dose (C-4), search (C-12), legal risk, and switching (C-7). | None needed | **decrease**, but by much less than legal sales (C-1), because part of the trade moves to Halvet and to informal sellers (C-3, C-6) rather than stopping. The stockpile only shifts some use in time. |
| `tax_revenue` (state sales tax, all goods), short | Spending that moves to legal substitutes is taxed (C-7). | Sales tax on lirva is lost (C-1); informal and Halvet purchases are untaxed (C-3, C-6). | None | **ambiguous** (C-17, Tier C). Decided by how much of lirva spending moves to taxed substitutes and at what rates. |
| `sellers.informal`, `earnings`, medium | The risk premium in the price (C-4). | Fines, seizures, prison terms, and selling without shops or scale. | None | **ambiguous** (C-20). Those who choose to sell informally expect to do better than their next-best option under the ban (LW-5); that says nothing about how they fare compared with legal selling in the counterfactual. |

## 8. Time structure

- **Announcement window (six months).** Users stockpile (C-5) and shops run clearance sales. Dried leaf keeps for about a year (A-5), so the informal market is thin in the first months and grows as stockpiles run down over the first year.
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
| C-23 | `taxpayers` | `resources_available_other_uses` | decrease | What the enforcement budget (C-16) would otherwise have funded. | OC-3, OC-1 |

Prevented exchanges are recorded as C-1 and are not listed again.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | A meaningful share of regular users keep using lirva after the ban. | other | 0.9 | Fifteen years of legal use; user surveys; experience of comparable bans. | C-3, C-4, C-6, C-9 shrink; the ban mainly ends use. |
| A-2 | Licensed shops comply. | enforcement | 0.95 | Visible, licensed premises; inspection powers. | C-1, C-2 weaker; shops sell under the counter. |
| A-3 | Enforcement is imperfect: many informal sales go undetected. | enforcement | 0.85 | Police budget relative to the number of users; experience of comparable bans. | C-3, C-12, C-13, C-15 weaken; C-18 grows. |
| A-4 | Enforcement is active enough that informal sellers face a real risk. | enforcement | 0.8 | Added budget; arrest targets; sentencing. | C-4 and C-19 weaken. |
| A-5 | Users know the date and can store dried leaf for months. | expectations | 0.75 | Publicity of the Act; shelf life of about a year. | C-5 not reported. |
| A-6 | Enough users live within reach of Halvet and will carry home amounts under 50 g. | mobility | 0.65 | Distance to the border (40 to 90 minutes); car ownership; size of the civil fine. | C-6, C-14, C-22 not reported. |
| A-7 | Legal substitutes are acceptable to some users. | substitutability | 0.8 | Survey data on what users would switch to. | C-7 weakens; C-17 shifts toward a decrease. |
| A-8 | Related plants and blends outside the definitions can be sold. | other | 0.6 | Botanical relatives with similar compounds; the Act's wording. | C-8 not reported. |
| A-9 | Penalties are graded by the total weight of material. | enforcement | 0.95 | Act text (K2). | C-9 not reported. |
| A-10 | Extract can be made with simple equipment. | other | 0.75 | Current extract sales; method (alcohol soaking). | C-9 weakens. |
| A-11 | Specialist shops cannot replace lirva sales with other products for most of their staff. | alternative_uses | 0.85 | Share of shop revenue from lirva. | C-10 weakens. |
| A-12 | Users and former shop owners can organize. | other | 0.6 | Existing trade association of shops; user groups. | C-11 not reported. |
| A-13 | Users bundle other shopping with lirva trips to Halvet. | other | 0.4 | Trip surveys; what is sold near the border. | Below cut-off; not reported. |
| A-14 | Informal supply is organized by groups that settle disputes by force on a meaningful scale. | other | 0.3 | Value per unit; scale of sellers; experience with comparable mild substances. | Below cut-off; not reported, and outside version 1 variables. |
| A-15 | Spending moves to substitutes taxed at rates similar to lirva's. | revenue_use | 0.6 | Sales and excise rates on alcohol and herbal products. | C-17 leans toward a decrease. |
| A-16 | Convictions are recorded and employers check them. | other | 0.6 | Record-keeping rules; background-check practice in Corrin. | C-18 not reported. |

## 11. Report

**The policy.** Corrin bans making, selling and possessing lirva, a mild plant product that has been sold legally for fifteen years. Penalties are graded by the weight of the material, from a civil fine under 50 g to prison over 1 kg. Shops had six months to sell, destroy or export their stock. The neighboring state keeps lirva legal.

**Visible consequences.** Lirva leaves the shelves: legal sales and legal sellers fall to almost nothing (C-1, C-2).

**Invisible consequences.**
- *Users* stockpiled before the date (C-5), and afterwards pay more per dose (C-4). Some buy in Halvet and carry home small amounts (C-6, C-22); some switch to alcohol or other products (C-7); some buy from informal sellers, who are harder to find (C-12) and whose product varies more in strength (C-13, Tier C). Disputes with sellers cannot go to court (C-15, Tier C). Fewer people start using lirva (C-19).
- *Sellers* shift toward extract, because the penalty depends on weight and extract packs about twenty times as many doses into a gram (C-9). Products from related plants are sold as alternatives (C-8).
- *Shops* lose their stock and staff lose their jobs (C-21, C-10). Halvet shops gain (C-14).
- *The state* spends more on police, laboratories, courts and, over the years, prisons (C-16), funded by taxpayers (C-23). Those convicted find it harder to get jobs later (C-18, Tier C).
- Users and former shop owners lobby for repeal (C-11).

**Ambiguous effects.** Total sales-tax revenue (C-17, Tier C). Whether informal sellers earn more or less than they would have selling legally (C-20).

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
| C-9 | sellers.informal | variety (share of concentrated forms) | increase | medium | invisible | B | EN-7, EN-8 | A-1, A-9, A-10 |
| C-10 | shops.lirva | employment | decrease | short | invisible | B | EN-7, RS-6 | A-2, A-11 |
| C-11 | users.current, shops.lirva | lobbying_effort | increase | medium | invisible | B | RS-7 | A-12 |
| C-12 | users.informal | search_cost | increase | short | invisible | B | RS-3, RS-10 | A-3 |
| C-13 | users.informal | quality_variability (proposed) | increase | short–medium | invisible | C | RS-10, GAP-017-1 | A-3 |
| C-14 | halvet.sellers | quantity_traded | increase | short | invisible | B | RS-4 | A-6 |
| C-15 | users.informal, sellers.informal | disputes_settled_outside_courts (proposed) | increase | short | invisible | C | RS-10, GAP-017-2 | A-3 |
| C-16 | officials.enforcement | enforcement_cost | increase | short–long | invisible | A | OC-3 | none |
| C-17 | officials.enforcement, taxpayers | tax_revenue | ambiguous | short | invisible | C | GAP-017-3 | A-7, A-15 |
| C-18 | users.convicted | employment | decrease | long | invisible | C | GAP-017-4 | A-3, A-16 |
| C-19 | users.prospective | quantity_demanded | decrease | long | invisible | B | EN-7, LW-3 | A-1, A-4 |
| C-20 | sellers.informal | earnings | ambiguous | medium | invisible | B | C-4 vs penalties | A-1, A-3, A-4 |
| C-21 | shops.lirva | resources_available_other_uses | decrease | short | invisible | A | OC-1 | none |
| C-22 | users.mobile | search_cost | increase | short | invisible | B | OC-2 | A-6 |
| C-23 | taxpayers | resources_available_other_uses | decrease | short | invisible | A | OC-3, OC-1 | none |

## Gaps found

- **GAP-017-1** (Tier C: C-13; variable). RS-10 says quality in informal trade becomes "harder to judge and more variable", but the variable list has only `quality_per_unit`, which measures a level, not a spread. Proposed fix: add a variable `quality_variability` to 2.4: the spread of quality (for a drug, potency and purity) between units bought in a market.
- **GAP-017-2** (Tier C: C-15; variable). RS-10 says disputes in informal trade "are settled privately or not at all", but no variable records this. Proposed fix: add `disputes_settled_outside_courts`, the share of disputes in a market that are settled without legal recourse. Violence used in such settlement remains a safety outcome, out of scope for version 1; whether it should get a variable in a later version, and what assumption should govern it (here A-14), is for the experts.
- **GAP-017-3** (Tier C: C-17). TX-9 covers a tax base that shrinks because of the tax itself (TX-2, TX-4), but not an existing general tax whose base a prohibition removes, with part of the spending moving to other taxed goods and part to untaxed informal or cross-border purchases. Proposed fix: widen TX-9, or add a rule "Base shift": when a policy moves spending from a taxed good to other goods, `tax_revenue` on the target decreases and revenue on substitutes increases; the combined sign is ambiguous unless the substitutes are untaxed.
- **GAP-017-4** (Tier C: C-18). No rule links penalties under a prohibition to the later options of those penalized. Proposed fix: a rule "EN-10 Penalty records": if a prohibition is enforced by criminal convictions that are recorded and checked, then for those convicted `employment` decreases over the long run; assumes record-keeping and checking practice (`other`).
- **GAP-017-5** (no Tier C consequence; variable definition). EN-8 concludes that `variety` "changes toward high-potency products", but `variety` is defined as the number of distinct versions offered, not their mix. C-9 stays Tier B because EN-8 names the variable, but its sign has to be written as a shift in composition. Proposed fix: add a variable `share_concentrated_forms` (the share of sales in high-potency forms), and use it in EN-8.
