# WE-017 / Core-only re-run: Ban on a recreational plant product, with penalties scaled to weight

Analyst: core-only re-run (Handbook 0.4)  |  Rules: core rules CR-1 to CR-12 only  |  Status: awaiting comparison

## 1. Policy record

**Corrin Lirva Control Act.** Lirva is the dried leaf of the lirva shrub, brewed as tea or chewed for a mild stimulant and relaxing effect. It has been sold legally in the State of Corrin (about 6 million people) for fifteen years, in about 400 specialist tea shops, in convenience stores and online, and has been subject to the general sales tax. About 180,000 adults use it regularly. A typical dose is about 5 g of leaf. A concentrated extract, made by soaking the leaf in alcohol and drying the result, gives the same effect at about 0.25 g; it is about 5% of current sales. The neighboring state of Halvet keeps lirva legal; its border is 40 to 90 minutes' drive from Corrin's two largest cities. The Act was passed six months before it took effect.

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Prohibition | `prohibition` | Making, selling, possessing for sale, importing and growing lirva, its active compound lirvine, and any product containing either | Everyone | From the effective date. | Licensed research |
| K2 Penalties | Part of K1 | Possession and sale | Everyone | Graded by the total weight of material, including any carrier or mixture. Possession under 50 g: civil fine of $250. 50 g to 1 kg: misdemeanor, up to 1 year. Over 1 kg: felony, 2 to 10 years. Sale is punished one grade higher than possession of the same weight. | None |
| K3 Transition | Part of K1 | Existing stocks | Licensed sellers | Stocks must be destroyed or exported by the effective date. No compensation. | None |
| K4 Enforcement | Enforcement | K1 to K3 | State police drug unit, local police, state laboratory | Added budget for investigators and lab testing, from the general budget. | None |

Unclear provisions: whether related plants with similar compounds are covered. The Act names only lirva and lirvine, so they are assumed not covered. Where a sign depends on it, both readings are reported: **U1-a** related plants are not covered; **U1-b** they are covered.

Note on K2: 50 g of leaf is about 10 doses; 50 g of extract is about 200. Penalties graded by weight treat the two very differently per dose.

## 2. Classification

CR-1 operations: 1 remove an option, 2 add an option, 3 change what an option brings, 4 transfer means.

| Component | Rothbard type | Binding? (assumption ID) | Core rules | CR-1 operations, by actor class |
|---|---|---|---|---|
| K1 | triangular (prohibits exchanges between private parties) | Yes: users continue to want lirva (A-1); licensed shops comply (A-2) | CR-1, CR-4, CR-5a, CR-6, CR-7, CR-9, CR-11 | Licensed sellers and importers: 1 (legal sale and import removed). Users: 1 (legal purchase removed); buying informally or in Halvet remains, with risk (3). Would-be informal sellers: 3 (a risk attached to selling). Researchers: none (exempt). |
| K2 | part of K1 (penalty schedule) | Applied as written (A-9) | CR-1, CR-4c, CR-5c | Users and sellers: 3, graded by weight; per dose the penalty is far lower for extract than for leaf, and lower for loads under 50 g. |
| K3 | part of K1 (transition) | Yes for licensed sellers (A-2) | CR-1, CR-7c, CR-8, CR-10a | Licensed sellers: 1 (sale of stock after the date) and 4 (stock destroyed or exported, no compensation). |
| K4 | binary (budget) plus enforcement | Imperfect (A-3) but real (A-4) | CR-1, CR-8 | Users and sellers: 3 (risk of detection). Taxpayers: 4 (added budget). |

## 3. Actor classes

| Actor class | Role | How its options change (CR-1) |
|---|---|---|
| users.regular (buyers.current) | About 180,000 regular adult users | Legal purchase removed (1); informal, Halvet and substitute options remain with new risk or cost (3). |
| users.informal, users.convicted | Users who buy informally; users convicted under K2 | As above; conviction attaches a record (3). |
| shops.specialist (sellers.current) | About 400 specialist tea shops | Sale removed (1); stock destroyed or exported without compensation (4). |
| convenience stores and online sellers (sellers.current) | Other legal sellers | Sale removed (1); lirva is a small line for them, and their shelf space moves to other goods (CR-7a). No separate consequence. |
| input_suppliers (importers and wholesalers) | Bring lirva into Corrin | Import removed (1). |
| sellers.informal | Would-be illegal sellers | Selling carries penalties graded by weight (3). |
| neighboring_jurisdictions (Halvet sellers) | Legal sellers 40 to 90 minutes away | No direct change; Corrin users come to them (CR-9). |
| sellers.substitutes | Sellers of legal substitutes, including related plants and blends | No direct change under U1-a; covered under U1-b (1). |
| sellers.complements | Sellers of accessories used with lirva | No direct change; demand follows lirva use (CR-9). |
| factor_owners.specific (landlords of shop premises) | Own premises let to specialist shops | No direct change; tenants close (CR-9). |
| employers | Hire users | No direct change; conviction records inform them (CR-11c). |
| officials.enforcement, officials.state (revenue) | Police, laboratory; tax collection | New duties and budget (4); sales tax base changes. |
| taxpayers | Fund K4 | Transfer (4). |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | users.regular (buyers.current) | quantity_traded (lirva, legal market) | decrease | short | CR-1 op. 1 (legal purchase removed); CR-5a (exchanges between shops and users prevented) | A-2 |
| C-2 | shops.specialist (sellers.current) | number_of_sellers | decrease | short | CR-1 op. 1 (legal sale removed); CR-4b (x: stay open with other products, y: close), with lirva the main line | A-2, A-11 |
| C-3 | shops.specialist (sellers.current) | asset_value (shop businesses: stock, fittings, leases, goodwill) | decrease | short | CR-7c (a lasting fall in expected yield is borne by whoever owns the asset when it becomes expected, at passage); CR-1 op. 4 (K3: stocks destroyed or exported without compensation) | A-2, A-11 |
| C-4 | input_suppliers (importers and wholesalers of lirva) | quantity_traded (lirva imports into Corrin, legal) | decrease | short | CR-1 op. 1 (importing prohibited); CR-9 (their buyers, the shops, stop buying) | A-2 |

## 5. Responses

CR-4 for every pair of options each class has:

- **Users.** (x: comply, y: violate) informal purchases (C-10); (x: here, y: Halvet) carry-home purchases under 50 g (C-11); (x: lirva, y: substitute) (C-12); (x: covered form, y: uncovered form) related plants, by reading (C-13); (x: later, y: now) stockpiling in the six-month window under CR-10a (C-5, C-6), followed by a dip (C-7). The price of lirva from all remaining sources rises, because sellers and carriers must be paid for the risk (CR-5c) (C-15); users then give up their least valued doses (CR-4c) (C-16).
- **Sellers.** Specialist shops close (CR-4b, x: stay open, y: close) (C-2) and run their stocks down before the date, since stock left over is lost (CR-10a) (C-8); in the final weeks, shops clearing stock meet users stockpiling, so the legal price then is ambiguous (C-9). New informal sellers enter where the gain exceeds the expected penalty (CR-4, x: stay out, y: enter; CR-6 third margin) (C-14). Because penalties are graded by total weight, the penalty per dose is much lower for extract, so informal supply shifts toward extract (CR-4c applied per dose) (C-17).
- **Shop staff.** Lose their jobs where shops close (CR-4b, CR-7b) (C-18).
- **Organized interests.** (x: accept, y: lobby) (C-19).

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-5 | users.regular (buyers.current) | quantity_traded (lirva, legal, six-month window before the effective date) | increase | short | CR-10a; CR-4c (x: buy after the effective date, now illegal; y: buy now and store) | A-5 |
| C-6 | users.regular (buyers.current) | inventory_held (lirva, at the effective date) | increase | short | CR-10a (stockpiling ahead of the deadline) | A-5 |
| C-7 | users.regular (buyers.current) | quantity_demanded (lirva, all sources, first months after the effective date) | decrease | short | CR-10a (stored leaf replaces purchases); CR-1 op. 1 and 3 (legal sources removed, others risky) | A-5, A-1 |
| C-8 | shops.specialist (sellers.current) | inventory_held (lirva, at the effective date) | decrease | short | CR-10a; CR-4c (x: reorder, y: run stock down), since stock left at the date must be destroyed or exported (K3) | A-2 |
| C-9 | users.regular (buyers.current) | price_paid (lirva, legal, final weeks before the effective date) | ambiguous | short | (+) CR-6 first paragraph (stockpiling raises planned purchases); (-) CR-4 and CR-10a (shops clear stock they must otherwise destroy or export); CR-12b | A-5, A-2 |
| C-10 | users.regular (buyers.current) | informal_activity | increase | short | CR-4b (x: comply, y: violate) for users who rank lirva above the fine risk; CR-1 op. 3 (imperfect enforcement attaches a risk rather than removing the option) | A-1, A-3 |
| C-11 | users.regular (buyers.current) | cross_border_purchases | increase | short | CR-4b (x: buy in Corrin, y: buy in Halvet and carry home under 50 g, a civil fine at most) | A-1, A-6 |
| C-12 | users.regular (buyers.current) | quantity_substitute (legal substitutes) | increase | short | CR-4b (x: lirva, now illegal or risky; y: a legal substitute) | A-7 |
| C-13 | users.regular (buyers.current) | quantity_substitute (related plants and blends) | U1-a: increase; U1-b: decrease | short | U1-a (related plants not covered): CR-4b (x: the covered form, y: the uncovered form). U1-b (covered): CR-1 op. 1 removes them too | A-8 |
| C-14 | sellers.informal | entry_rate | increase | short | CR-4b (x: stay out, y: enter), where the gain from serving remaining users exceeds the expected penalty; CR-6 third margin (exchanges outside the rule) | A-1, A-3 |
| C-15 | users.regular (buyers.current) | price_paid (lirva, informal and cross-border) | increase | medium | CR-5c (sellers and carriers must now be paid for the risk of penalties, so the range of accepted terms moves up); CR-6 first paragraph | A-1, A-4 |
| C-16 | users.regular (buyers.current) | quantity_demanded (lirva, all sources) | decrease | medium | CR-4c (the least valued doses are the first given up after the price and risk rise); CR-3a | A-4 |
| C-17 | sellers.informal | share_concentrated_forms | increase | medium | CR-4c applied per dose (x: leaf, y: extract): penalties graded by weight make the expected penalty per dose about 20 times lower for extract (arithmetic: 50 g is 10 doses of leaf, 200 of extract) | A-4, A-9, A-10 |
| C-18 | shops.specialist (sellers.current) | employment (shop staff) | decrease | short | CR-4b (exit, after C-2); CR-7b (the loss settles on means that cannot move: staff skills and shop assets specific to lirva) | A-2, A-11 |
| C-19 | users and former shop owners | lobbying_effort | increase | medium | CR-4b (x: accept the ban, y: lobby to repeal or soften it); each has a concentrated stake | A-12 |

## 6. Second-order effects

Depth limit 4; prune diffuse bystander effects after depth 3. Relations used: lirva in Corrin and lirva in Halvet: across_border, close for users within reach of the border (A-6); lirva and legal substitutes (including alcohol): substitute, partial (A-7, A-15); lirva and related plants: substitute, close (A-8); lirva and its accessories: complement in use; shop premises to specialist shops: input_to; legal and informal lirva: same market, other segment.

Chains:
1. K1 (1) users buy informally (2) no brands, reviews or courts (3): quality varies more, information falls, search costs rise, disputes are settled outside courts (C-20, C-21, C-22, C-23). With K2 (2) supply shifts to extract (3), which adds to quality variability.
2. K1 (1) users buy in Halvet (2) Halvet sellers' sales to Corrin residents rise (3) (C-24). Bundled shopping on those trips is not reported (A-13).
3. K1 (1) shops close (2) premises stand vacant for a time (3) (C-26); accessory sales fall (3) (C-27).
4. K1 and K2 (1) users caught with lirva (2) conviction records (3) employers who check them hire others (4) (C-28). Stopped at depth 4.
5. K1 (1) spending moves among legal sales, informal sales, Halvet and taxed substitutes (2) state tax revenue (3): opposing chains (C-25).

Component interactions: K3 closes the option of selling stock after the date, which drives C-8 and C-3; K2's weight grading changes which form of the good survives K1 (C-17) and keeps carry-home loads under 50 g, the civil-fine grade (C-11); K4 sets how much risk K1 attaches (A-3, A-4).

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-20 | users.informal (buyers in the informal market) | quality_variability | increase | medium | CR-11b (no brands, certification or courts in the informal market); C-17 adds extract, whose strength per gram varies more | same market, informal segment | A-1, A-3 |
| C-21 | users.informal (buyers in the informal market) | quality_information | decrease | medium | CR-11b | same market, informal segment | A-1, A-3 |
| C-22 | users.informal (buyers in the informal market) | search_cost | increase | medium | CR-11b (no advertising or shopfronts); CR-6 second margin (connections decide who is served) | same market, informal segment | A-1, A-3 |
| C-23 | users.informal (buyers in the informal market) | disputes_settled_outside_courts | increase | medium | CR-11b (contracts for an illegal good cannot be enforced in court) | same market, informal segment | A-1, A-3 |
| C-24 | neighboring_jurisdictions (Halvet sellers) | quantity_traded (lirva sold to Corrin residents) | increase | short | CR-9 (buyers who move across the border buy from Halvet sellers), after C-11 | across_border (lirva in Halvet, close for users within 40 to 90 minutes) | A-1, A-6 |
| C-25 | officials.state (revenue) | tax_revenue (Corrin sales tax and excise) | ambiguous | medium | (-) CR-8b: sales tax on legal lirva sales is lost, and spending moved to Halvet or the informal market pays no Corrin tax; (+) CR-9: spending moved to substitutes that carry an excise on top of sales tax; CR-12b | substitute (alcohol and herbal products, partial) | A-2, A-15 |
| C-26 | factor_owners.specific (landlords of shop premises) | units_held_vacant (premises of closed lirva shops) | increase | short | CR-9 (premises are an input to the shops that close, C-2); CR-10b (re-letting takes time) | input_to (retail premises to specialist shops) | A-11, A-N1 |
| C-27 | sellers.complements (brewing and chewing accessories) | quantity_complement (lirva accessories) | decrease | medium | CR-9, LW-10 (demand for goods used with lirva follows its use, C-16); their main outlets, the shops, close | complement (in use) | A-4, A-11, A-N2 |
| C-28 | users.convicted | employment | decrease | long | CR-11c (a record of conviction conveys information); CR-4b for employers (x: hire an applicant with a record, y: hire another) | exchange relation: users as job applicants to employers (labor market) | A-4, A-16 |

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance premise | Combined sign |
|---|---|---|---|---|
| users.regular, price_paid (legal, final weeks), short | Stockpiling raises planned purchases (CR-6 first paragraph) | Shops clear stock they would otherwise destroy or export (CR-4, CR-10a) | None | ambiguous (CR-12b) |
| officials.state, tax_revenue, medium | Spending moved to substitutes carrying an excise (CR-9) | Sales tax on legal lirva lost; spending moved to Halvet or the informal market untaxed in Corrin (CR-8b) | None | ambiguous (CR-12b) |
| users.regular, quantity_demanded (all sources), medium | None | Higher price and risk (CR-4c); stocks run down (CR-10a) | Not needed | decrease (CR-12a) |
| users.informal, quality_variability, medium | No brands or courts (CR-11b); shift to extract | None | Not needed | increase (CR-12a) |

No other key is reached by opposing chains. Fines collected under K2 are transfers from users to the state (CR-8b); they are not netted against enforcement cost (CR-12c).

## 8. Time structure

- **Announcement window (CR-10a).** Six months between passage and effect: users buy and store leaf (shelf life about a year, A-5), so legal sales rise in the window and purchases from all sources dip in the first months after; shops run stock down because stock left at the date must be destroyed or exported. The fall in the value of shop businesses happens at passage, not at the effective date (CR-7c).
- **Informal supply (CR-10b).** Informal supply is a stock of sellers and contacts built through entry over time; search costs are highest early and fall as it develops, but stay above the legal-market level (CR-11b). No sign is recorded for the change within the medium run.
- **Concentration.** The shift toward extract grows as informal sellers learn the method (A-10) and as enforcement makes the per-dose penalty difference felt.
- **Records.** Conviction effects on employment come long after the first arrests and persist (C-28).
- **Reversal.** Closed shops, lost staff skills and destroyed stock would not return at once if the ban were lifted (CR-10b); this is noted, not scored, since no repeal is analyzed.

## 9. Opportunity costs

CR-3 and CR-8. Symmetry (CR-8): the higher prices received by informal and Halvet sellers are the users' outlay, counted in C-31; fines are a receipt to the state and an outlay of users.

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-29 | officials.enforcement (police drug unit, local police, state laboratory) | enforcement_cost | increase | Police and laboratory time and funds that would have served other public uses | CR-8c; K4 (added budget for investigators and lab testing) |
| C-30 | taxpayers | resources_available_other_uses | decrease | Other public spending or lower taxes | CR-8a, CR-8b (K4's added budget from the general budget is withdrawn from other uses) |
| C-31 | users.regular (buyers.current) | resources_available_other_uses | decrease | Money and time users would have spent on other ends | CR-3a (fallback to lower-ranked options); CR-8c (travel, search, storage and fines spent because of the ban); CR-8b (higher prices paid to informal and Halvet sellers) |
| C-32 | shops.specialist (sellers.current) | resources_available_other_uses | decrease | Stock, fittings and work that served users; the owners' other spending | CR-8a and CR-8c (stock destroyed, or exported at a lower net price; fittings and skills specific to lirva lose their use); CR-3a |

Prevented exchanges (CR-5a) between shops and users are C-1.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | A meaningful share of regular users keep using lirva after the ban. | other | 0.9 | Fifteen years of legal use; user surveys; experience of comparable bans. | Informal and cross-border consequences vanish. |
| A-2 | Licensed shops comply. | enforcement | 0.95 | Visible, licensed premises; inspection powers. | Legal sales continue in part. |
| A-3 | Enforcement is imperfect: many informal sales go undetected. | enforcement | 0.85 | Police budget relative to the number of users; experience of comparable bans. | Informal market small. |
| A-4 | Enforcement is active enough that informal sellers face a real risk. | enforcement | 0.8 | Added budget; arrest targets; sentencing. | No risk premium; no shift to extract. |
| A-5 | Users know the date and can store dried leaf for months. | expectations | 0.75 | Publicity of the Act; shelf life of about a year. | No window rush or dip. |
| A-6 | Enough users live within reach of Halvet and will carry home amounts under 50 g. | mobility | 0.65 | Distance to the border (40 to 90 minutes); car ownership; size of the civil fine. | No cross-border chain. |
| A-7 | Legal substitutes are acceptable to some users. | substitutability | 0.8 | Survey data on what users would switch to. | No substitution. |
| A-8 | Related plants and blends outside the definitions can be sold. | other | 0.6 | Botanical relatives with similar compounds; the Act's wording. | No related-plant chain under U1-a. |
| A-9 | Penalties are graded by the total weight of material. | enforcement | 0.95 | Act text (K2). | No shift to extract. |
| A-10 | Extract can be made with simple equipment. | other | 0.75 | Current extract sales; method (alcohol soaking). | Shift to extract slower. |
| A-11 | Specialist shops cannot replace lirva sales with other products for most of their staff. | alternative_uses | 0.85 | Share of shop revenue from lirva. | Fewer closures and job losses. |
| A-12 | Users and former shop owners can organize. | other | 0.6 | Existing trade association of shops; user groups. | No lobbying consequence. |
| A-13 | Users bundle other shopping with lirva trips to Halvet. | other | 0.4 | Trip surveys; what is sold near the border. | Below cut-off; not used. |
| A-14 | Informal supply is organized by groups that settle disputes by force on a meaningful scale. | other | 0.3 | Value per unit; scale of sellers; experience with comparable mild substances. | Below cut-off; also a safety effect, out of scope. |
| A-15 | Some lirva spending moves to substitutes that carry an excise on top of the general sales tax, such as alcohol. | substitutability | 0.6 | Survey data on what users would switch to (A-7); Corrin's excise rates on alcohol and herbal products. | Tax revenue decreases. |
| A-16 | Convictions are recorded and employers check them. | other | 0.6 | Record-keeping rules; background-check practice in Corrin. | No employment chain. |
| A-N1 | Premises of closed specialist shops are not re-let at once. | mobility | 0.6 | Retail vacancy rates and typical re-letting times in Corrin's shopping streets; fit-out specific to tea shops. | C-26 vanishes. |
| A-N2 | Accessories sold for lirva (infusers, chewing pouches, branded tins) are used mainly with lirva and sold mainly through the specialist shops. | substitutability | 0.6 | Shop sales mix; product use. | C-27 vanishes. |

**Not reported** (an assumption below 0.5):
- Bundled shopping on lirva trips to Halvet: `cross_border_purchases` of other goods increase, and Corrin retailers near users' homes lose those sales (A-13, p 0.4).
- Disputes in the informal market settled by force (A-14, p 0.3); this would also be a safety effect, out of scope for version 1.

## 11. Report

**The policy:** From a date six months after passage, Corrin prohibits making, selling, importing, growing and possessing for sale lirva and lirvine. Possession and sale are penalized by the total weight of material: a civil fine under 50 g, a misdemeanor to 1 kg, a felony above, with sale one grade higher. Licensed sellers must destroy or export their stock by the date, without compensation. Police and the state laboratory get added budget.

**Visible consequences:** Legal sales stop (C-1); specialist shops close (C-2), their staff lose jobs (C-18) and the businesses lose value at passage (C-3); legal imports stop (C-4); users who continue pay more (C-15); enforcement spending rises (C-29).

**Invisible consequences:**
- *Users:* a buying rush and stockpiling in the six months before the date, then a dip (C-5, C-6, C-7); fewer doses consumed overall (C-16); some buy informally (C-10), where quality varies more, information is poorer, search is costlier and disputes cannot go to court (C-20, C-21, C-22, C-23); some drive to Halvet (C-11, C-24); some switch to legal substitutes (C-12) or related plants (C-13, by reading); those convicted face worse job prospects (C-28); money and time spent because of the ban (C-31).
- *Informal sellers:* entry (C-14), and a shift toward extract because penalties are by weight (C-17).
- *Shops and their suppliers:* stock run down before the date (C-8), stock and fittings lost (C-32); premises left empty for a time (C-26); accessory sellers sell less (C-27).
- *Others:* lobbying by users and former shop owners (C-19); taxpayers fund enforcement (C-30).

**Ambiguous effects:** State tax revenue (sales tax lost on legal lirva and on spending moved to Halvet or the informal market, against excise on substitutes) (C-25); the legal price in the final weeks (stockpiling against stock clearance) (C-9).

**Key conditions:** Users keep using lirva (A-1, 0.9); shops comply (A-2, 0.95); enforcement is imperfect (A-3, 0.85) but real (A-4, 0.8); penalties are by total weight (A-9, 0.95); Halvet is within reach (A-6, 0.65). Two new premises: closed premises are not re-let at once (A-N1, 0.6) and accessories are used mainly with lirva (A-N2, 0.6).

**What this analysis cannot say:** how large any of these changes are; whether the reduction in use is worth its costs to users, sellers and taxpayers; whether the policy is good. Health and safety effects of lirva, of extract, of variable potency and of any violence in the informal market are out of scope for version 1 and are not analyzed here.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | users.regular (buyers.current) | quantity_traded (lirva, legal market) | decrease | short | visible | B | CR-1 op. 1 (legal purchase removed); CR-5a (exchanges between shops and users prevented) | A-2 |
| C-2 | shops.specialist (sellers.current) | number_of_sellers | decrease | short | visible | B | CR-1 op. 1 (legal sale removed); CR-4b (x: stay open with other products, y: close), with lirva the main line | A-2, A-11 |
| C-3 | shops.specialist (sellers.current) | asset_value (shop businesses: stock, fittings, leases, goodwill) | decrease | short | visible | B | CR-7c (a lasting fall in expected yield is borne by whoever owns the asset when it becomes expected, at passage); CR-1 op. 4 (K3: stocks destroyed or exported without compensation) | A-2, A-11 |
| C-4 | input_suppliers (importers and wholesalers of lirva) | quantity_traded (lirva imports into Corrin, legal) | decrease | short | visible | B | CR-1 op. 1 (importing prohibited); CR-9 (their buyers, the shops, stop buying) | A-2 |
| C-5 | users.regular (buyers.current) | quantity_traded (lirva, legal, six-month window before the effective date) | increase | short | invisible | B | CR-10a; CR-4c (x: buy after the effective date, now illegal; y: buy now and store) | A-5 |
| C-6 | users.regular (buyers.current) | inventory_held (lirva, at the effective date) | increase | short | invisible | B | CR-10a (stockpiling ahead of the deadline) | A-5 |
| C-7 | users.regular (buyers.current) | quantity_demanded (lirva, all sources, first months after the effective date) | decrease | short | invisible | B | CR-10a (stored leaf replaces purchases); CR-1 op. 1 and 3 (legal sources removed, others risky) | A-5, A-1 |
| C-8 | shops.specialist (sellers.current) | inventory_held (lirva, at the effective date) | decrease | short | invisible | B | CR-10a; CR-4c (x: reorder, y: run stock down), since stock left at the date must be destroyed or exported (K3) | A-2 |
| C-9 | users.regular (buyers.current) | price_paid (lirva, legal, final weeks before the effective date) | ambiguous | short | invisible | B | (+) CR-6 first paragraph (stockpiling raises planned purchases); (-) CR-4 and CR-10a (shops clear stock they must otherwise destroy or export); CR-12b | A-5, A-2 |
| C-10 | users.regular (buyers.current) | informal_activity | increase | short | invisible | B | CR-4b (x: comply, y: violate) for users who rank lirva above the fine risk; CR-1 op. 3 (imperfect enforcement attaches a risk rather than removing the option) | A-1, A-3 |
| C-11 | users.regular (buyers.current) | cross_border_purchases | increase | short | invisible | B | CR-4b (x: buy in Corrin, y: buy in Halvet and carry home under 50 g, a civil fine at most) | A-1, A-6 |
| C-12 | users.regular (buyers.current) | quantity_substitute (legal substitutes) | increase | short | invisible | B | CR-4b (x: lirva, now illegal or risky; y: a legal substitute) | A-7 |
| C-13 | users.regular (buyers.current) | quantity_substitute (related plants and blends) | U1-a: increase; U1-b: decrease | short | invisible | B | U1-a (related plants not covered): CR-4b (x: the covered form, y: the uncovered form). U1-b (covered): CR-1 op. 1 removes them too | A-8 |
| C-14 | sellers.informal | entry_rate | increase | short | invisible | B | CR-4b (x: stay out, y: enter), where the gain from serving remaining users exceeds the expected penalty; CR-6 third margin (exchanges outside the rule) | A-1, A-3 |
| C-15 | users.regular (buyers.current) | price_paid (lirva, informal and cross-border) | increase | medium | visible | B | CR-5c (sellers and carriers must now be paid for the risk of penalties, so the range of accepted terms moves up); CR-6 first paragraph | A-1, A-4 |
| C-16 | users.regular (buyers.current) | quantity_demanded (lirva, all sources) | decrease | medium | invisible | B | CR-4c (the least valued doses are the first given up after the price and risk rise); CR-3a | A-4 |
| C-17 | sellers.informal | share_concentrated_forms | increase | medium | invisible | B | CR-4c applied per dose (x: leaf, y: extract): penalties graded by weight make the expected penalty per dose about 20 times lower for extract (arithmetic: 50 g is 10 doses of leaf, 200 of extract) | A-4, A-9, A-10 |
| C-18 | shops.specialist (sellers.current) | employment (shop staff) | decrease | short | visible | B | CR-4b (exit, after C-2); CR-7b (the loss settles on means that cannot move: staff skills and shop assets specific to lirva) | A-2, A-11 |
| C-19 | users and former shop owners | lobbying_effort | increase | medium | invisible | B | CR-4b (x: accept the ban, y: lobby to repeal or soften it); each has a concentrated stake | A-12 |
| C-20 | users.informal (buyers in the informal market) | quality_variability | increase | medium | invisible | B | CR-11b (no brands, certification or courts in the informal market); C-17 adds extract, whose strength per gram varies more | A-1, A-3 |
| C-21 | users.informal (buyers in the informal market) | quality_information | decrease | medium | invisible | B | CR-11b | A-1, A-3 |
| C-22 | users.informal (buyers in the informal market) | search_cost | increase | medium | invisible | B | CR-11b (no advertising or shopfronts); CR-6 second margin (connections decide who is served) | A-1, A-3 |
| C-23 | users.informal (buyers in the informal market) | disputes_settled_outside_courts | increase | medium | invisible | B | CR-11b (contracts for an illegal good cannot be enforced in court) | A-1, A-3 |
| C-24 | neighboring_jurisdictions (Halvet sellers) | quantity_traded (lirva sold to Corrin residents) | increase | short | invisible | B | CR-9 (buyers who move across the border buy from Halvet sellers), after C-11 | A-1, A-6 |
| C-25 | officials.state (revenue) | tax_revenue (Corrin sales tax and excise) | ambiguous | medium | invisible | B | (-) CR-8b: sales tax on legal lirva sales is lost, and spending moved to Halvet or the informal market pays no Corrin tax; (+) CR-9: spending moved to substitutes that carry an excise on top of sales tax; CR-12b | A-2, A-15 |
| C-26 | factor_owners.specific (landlords of shop premises) | units_held_vacant (premises of closed lirva shops) | increase | short | invisible | B | CR-9 (premises are an input to the shops that close, C-2); CR-10b (re-letting takes time) | A-11, A-N1 |
| C-27 | sellers.complements (brewing and chewing accessories) | quantity_complement (lirva accessories) | decrease | medium | invisible | B | CR-9, LW-10 (demand for goods used with lirva follows its use, C-16); their main outlets, the shops, close | A-4, A-11, A-N2 |
| C-28 | users.convicted | employment | decrease | long | invisible | B | CR-11c (a record of conviction conveys information); CR-4b for employers (x: hire an applicant with a record, y: hire another) | A-4, A-16 |
| C-29 | officials.enforcement (police drug unit, local police, state laboratory) | enforcement_cost | increase | short | visible | A | CR-8c; K4 (added budget for investigators and lab testing) |  |
| C-30 | taxpayers | resources_available_other_uses | decrease | short | invisible | A | CR-8a, CR-8b (K4's added budget from the general budget is withdrawn from other uses) |  |
| C-31 | users.regular (buyers.current) | resources_available_other_uses | decrease | medium | invisible | B | CR-3a (fallback to lower-ranked options); CR-8c (travel, search, storage and fines spent because of the ban); CR-8b (higher prices paid to informal and Halvet sellers) | A-1, A-4, A-6 |
| C-32 | shops.specialist (sellers.current) | resources_available_other_uses | decrease | short | invisible | B | CR-8a and CR-8c (stock destroyed, or exported at a lower net price; fittings and skills specific to lirva lose their use); CR-3a | A-2, A-11 |

## Gaps found

**(a) Calculus gaps.** None. Every step was derived from CR-1 to CR-12, LW-10 and arithmetic.

**(b) New premises.**
- A-N1 (premises of closed shops not re-let at once, p 0.6): CR-9 carries the closures to the landlords, but whether premises stand empty depends on how fast they move to other tenants (CR-7's mobility premise); no case assumption covers it.
- A-N2 (accessories used mainly with lirva, p 0.6): CR-9 and LW-10 need the complement relation to be recorded with evidence before the chain can be followed; the case assumptions do not record it.

**(c) Unclear core rules.**
- CR-4c "for each unit": the rule does not say which unit is the margin when a penalty is set per gram and the good is valued per dose. The shift to extract (C-17) needs the unit to be the dose; the rule could be read either way.
- CR-1 and CR-6 on a partly enforced prohibition: CR-1 says an unenforced prohibition attaches a risk instead of removing the option, and CR-6's third margin covers exchanges outside the rule, but neither says how to treat the price of a prohibited good, which has no legal price to be "held". The rise in the informal price was derived through CR-5c (the seller must now be paid for risk) rather than CR-6.
- CR-7c timing: K3 confiscates stock at the effective date, while the fall in the businesses' value happens at passage. CR-7c covers the second; whether the uncompensated stock loss is a CR-7c capital loss or a CR-8a transfer is not settled by the wording, so it was recorded under both `asset_value` and `resources_available_other_uses`.

## Comparison with the pattern-based analysis

**Summary.** The two versions agree closely, with no sign differences. Prohibition, informal trade and its RS-10 effects, the risk premium, cross-border buying, substitution, the weight-graded shift to extract (EN-8), conviction records (EN-10), the tax-revenue ambiguity and the taxpayer cost all appear in both. The core version derived the EN-8 result directly from CR-4c applied per dose, and the EN-7 price rise through CR-5c. Its gaps section records that both were readings of the rule, but no difference in sign follows. The differences are omissions. The core version adds the fall in the value of shop businesses at passage (CR-7c), which the pattern version could have had from SB-4. It also adds importers' lost trade, shops running stock down before the date, the ambiguous legal price in the final weeks, and, on new premises, vacant premises and accessory sales. The pattern version adds a separate sales-tax line (a decrease, correct) and an ambiguous informal-seller earnings row. Two small errors are worth recording. The pattern version's section 7 lists stockpiles as a (+) chain on purchases after the date; they reduce purchases, though they keep consumption up. The core's C-31 (users' `resources_available_other_uses` decrease) is not signed for the class as a whole, since users who quit or switch to cheaper substitutes spend less.

**Counts.** M 18, V 6, S 0, OP 6, OC 2. Causes over S, OP and OC (8 items): P 0, K 0, A 2, E 4 (pattern version 4, core version 0), J 2.

### Pattern version → core version

| Pattern ID | Matched core ID(s) | Class | Cause | Note |
|---|---|---|---|---|
| C-1 | C-1 | M | | |
| C-2 | C-2 | M | | |
| C-3 | C-14, C-10 | V | | Pattern: `informal_activity` by sellers; core: informal sellers' `entry_rate` and users' `informal_activity`. |
| C-4 | C-15 | V | | Short against medium horizon; same risk-premium claim. |
| C-5 | C-5, C-6 | V | | Pattern: window `quantity_demanded`; core: window `quantity_traded` and users' `inventory_held`. |
| C-6 | C-11 | M | | |
| C-7 | C-12 | M | | |
| C-8 | C-13 | V | | The core reports both readings of the related-plant provision; U1-a (not covered) matches the pattern version's increase. |
| C-9 | C-17 | M | | Same result: EN-8 against CR-4c per dose. |
| C-10 | C-18 | M | | |
| C-11 | C-19 | M | | |
| C-12 | C-22 | M | | |
| C-13 | C-20 | M | | |
| C-24 | C-21 | M | | |
| C-14 | C-24 | M | | |
| C-15 | C-23 | M | | |
| C-16 | C-29 | M | | |
| C-17 | — | OC | J | General sales tax decrease. The pattern version's argument is right: spending moved to legal goods pays the same rate, while spending moved to informal and Halvet sellers is untaxed. The core version kept only the all-taxes row (C-25, ambiguous), which matches pattern C-26. Splitting by tax is a recording choice. |
| C-18 | C-28 | M | | |
| C-19 | C-16 | V | | Pattern: prospective users, long run; core: regular users, medium. Both say fewer doses demanded. The core has no separate row for fewer new users. |
| C-20 | — | OC | J | Informal sellers' `earnings` ambiguous. Defensible, but the counterfactual comparison is weak: many informal sellers would not have sold at all without the ban. |
| C-21 | C-32 | M | | |
| C-22 | C-31 | V | | Travel time to Halvet is part of the core's users' resources row. See the finding on C-31's sign. |
| C-23 | C-30 | M | | |
| C-25 | C-16, C-7 | M | | The core splits the short-run dip (stocks replace purchases, C-7) from the medium-run fall. |
| C-26 | C-25 | M | | |

### Core-only consequences

| Core ID | Class | Cause | Note |
|---|---|---|---|
| C-3 | OP | E (pattern) | Shop businesses lose `asset_value` at passage. SB-4 explicitly covers a lasting fall in returns from a restriction. The pattern version recorded the stock loss (C-21) but not the capitalized fall in the value of the businesses. |
| C-4 | OP | E (pattern) | Importers and wholesalers lose their legal trade (CR-9, `input_to`). Minor. |
| C-8 | OP | E (pattern) | Shops run stock down before the date because stock left over must be destroyed or exported (RS-8 with K3). The pattern version mentions clearance sales only in prose. |
| C-9 | OP | E (pattern) | Legal price in the final weeks is ambiguous: stockpiling demand against shops clearing stock (CR-12b). The pattern version described both forces in section 8 but did not record the consequence. |
| C-26 | OP | A | Vacant shop premises; rests on the new premise A-N1. |
| C-27 | OP | A | Accessory sales decrease; rests on the new premise A-N2. |

### Findings

- **No pattern appears wrong in this case.** EN-7, EN-8, EN-10, RS-10 and TX-10 all gave the same signs as the direct derivations. EN-8's result was reproduced from CR-4c with arithmetic on the per-dose penalty.
- **Pattern-version reasoning slip (no sign effect).** Section 7 lists stockpiles as a (+) chain on users' `quantity_demanded` after the date. Stocks bought in the window replace later purchases (CR-10a), so they push the same way as the other chains. The combined decrease is unchanged.
- **Pattern-version omission.** SB-4 was not applied to the shop businesses, although its "If" clause covers a restriction that lowers expected returns. The capital loss at passage is missing.
- **Core rules.** No difference traces to a limit of the calculus (K = 0). The core version's notes on CR-4c (which unit is the margin) and on pricing a prohibited good (CR-5c rather than CR-6) concern wording; neither changed a sign.
- **Core-version error (matched row).** C-31 (users' `resources_available_other_uses` decrease) is not signed for the whole class. Users who quit or switch to cheaper substitutes have more money for other uses. The decrease holds for those who keep buying at the higher price or travel, and for time spent (CR-8c). CR-3a (worse off by their own ranking) does not imply fewer resources.
