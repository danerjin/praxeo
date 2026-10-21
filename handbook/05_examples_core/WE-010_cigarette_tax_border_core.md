# WE-010 / Analysis: Cigarette tax increase in a state with low-tax neighbors (core-only re-run)

Analyst: core-only re-run (Handbook 0.4)  |  Rules: core rules CR-1 to CR-12 only  |  Status: awaiting comparison

## 1. Policy record

**Marren Tobacco Tax Act of the current session.** Marren is a state of about 6 million people. Its capital, Port Alder, lies on the river that forms the border with Dunmarch; three bridges cross it. About 45% of Marren's population lives within a 20-minute drive of Dunmarch or of Kessick, its southern neighbor. Per-pack cigarette taxes are $1.50 in Marren, $0.40 in Dunmarch and $0.80 in Kessick; Dunmarch has not changed its rate in 15 years. Before the act, a typical pack cost about $7.50 in Marren and $5.80 in Dunmarch. The bill was introduced in June, passage was expected from early August, it was signed on 1 October, and it took effect on 1 January.

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Tax increase | `per_unit_tax` | Cigarettes sold in Marren | Licensed stamping agents (wholesalers), who buy tax stamps and affix them before sale to retailers | From $1.50 to $3.50 per pack of 20, fixed in money terms (not indexed). | Other tobacco products (roll-your-own tobacco, cigars, "little cigars") stay at 25% of the wholesale price. E-cigarettes are untaxed. |
| K2 Floor-stock tax | `per_unit_tax` | Stamped packs held by wholesalers and retailers at 00:01 on 1 January | Wholesalers and retailers | $2.00 per stamped pack in inventory, reported and paid within 30 days. | Packs held by consumers. |
| K3 Personal allowance and possession rules | Enforcement | Cigarettes brought in from other states | Residents | One carton (10 packs) per person every 30 days may be brought in without Marren tax; anything more owes Marren use tax, self-reported. Possession of more than 5 cartons of unstamped cigarettes is a misdemeanor; more than 50 cartons is a felony with seizure of the vehicle. | None |
| K4 Enforcement | Enforcement | K1 to K3 | Revenue Department Tobacco Unit | Unit grows from 12 to 20 agents; road checks near bridges; retailer audits; counterfeit-stamp detection. | None |
| K5 Revenue use | Earmark | Revenue from the $2.00 increase | State | $0.30 per pack to the Tobacco Unit and to the existing quit-smoking program (already funded from general revenue); the rest to the general fund. | None |

Unclear provisions: whether the use tax on cartons above the allowance will be collected at all in practice. Assumed it will rarely be (A-4).


Horizons used below: short = from expected passage (August) to the first year of the new rate; medium = one to three years; long = beyond.

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | Core rules applied |
|---|---|---|---|
| K1 Tax increase | binary (the state takes $2.00 more per pack from stamping agents) | A per-unit tax binds on every taxed pack; mostly passed on (A-1, p 0.85) | CR-1 (op 3, op 4), CR-4, CR-5c, CR-7b, CR-8, CR-9, CR-10 |
| K2 Floor-stock tax | binary, one time | Binds on all stamped stock held at 00:01 on 1 January | CR-1 (op 4), CR-4, CR-10a |
| K3 Personal allowance and possession rules | triangular in effect (limits private carrying and resale of untaxed packs) | Weakly enforced; use tax rarely collected (A-4, p 0.8) | CR-1 (op 2, op 3), CR-4 |
| K4 Enforcement | binary on the budget side | Unit grows from 12 to 20 agents | CR-1 (op 3), CR-8c |
| K5 Revenue use | binary (earmark of $0.30 per pack) | Program already funded from general revenue (A-15, p 0.6) | CR-8b, CR-8d |

**CR-1: what each component does to each actor class.** Operations: 1 remove an option, 2 add an option, 3 change what an option brings, 4 transfer means. A dash means no direct effect; indirect effects are traced with CR-9.

| Actor class | K1 Tax increase | K2 Floor stock | K3 Allowance and possession | K4 Enforcement | K5 Revenue use |
|---|---|---|---|---|---|
| sellers.current (stamping agents, wholesalers) | 3 and 4: $2.00 more attached to each pack sold in Marren | 4: $2.00 on stamped stock held at the date | — | 3: audits, counterfeit-stamp checks | — |
| sellers.current (Marren retailers) | — (indirectly 3 through wholesale price) | 4: $2.00 on stamped stock held at the date | — | 3: audits | — |
| buyers.current (Marren smokers) | — (indirectly 3 through shelf price) | — | 2: one untaxed carton per 30 days from out of state; 3: use tax, misdemeanor and felony risk above the limits | 3: road checks | — |
| intermediaries (smuggling networks, casual resellers) | — (indirectly: a wider price gap) | — | 3: penalties attached to possession above 5 and 50 cartons | 3: more agents, road checks | — |
| sellers.substitutes (producers and sellers of other tobacco and e-cigarettes) | — (their products are not taxed more) | — | — | — | — |
| neighboring_jurisdictions (Dunmarch and Kessick retailers and governments) | — | — | — | — | — |
| officials.enforcement (Tobacco Unit) | — | 2: collection | 2: duties | 2 and 4: eight more agents | 4: part of the earmark |
| officials.revenue (state general fund) and recipients of its spending | 4: revenue received | 4 | — | — | 4: $0.30 per pack earmarked; the rest to the general fund |

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| buyers.current (Marren smokers) | About 45% live within 20 minutes of a lower-tax state | Shelf price rises (A-1); buying across the line, substitutes, cutting back and buying before 1 January become relatively better |
| buyers.current (smokers far from the border) | The rest | Same, but the cross-border option is costlier for them |
| sellers.current (wholesalers and retailers in Marren) | Stamp, stock and sell cigarettes | Pay the tax and the floor-stock tax; sell fewer packs |
| sellers.current (Marren border retailers) | Retailers near the crossings | Lose cigarette and trip sales to stores across the line (A-10) |
| sellers.substitutes | Producers and sellers of roll-your-own, cigars, little cigars, e-cigarettes | More demand; can design products to fit the "other tobacco" definition (A-7) |
| intermediaries | Smuggling networks and casual resellers | A $3.70 per pack gap expected to last (A-5) |
| neighboring_jurisdictions | Dunmarch and Kessick retailers, governments and owners of sites near crossings | More sales to Marren residents; more tax revenue |
| factor_owners.specific | Owners of Marren border retail businesses and sites | Lasting fall in their expected yield |
| officials.enforcement | Tobacco Unit | Eight more agents, road checks |
| officials.revenue | State general fund | Higher revenue, below the static projection |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | buyers.current (Marren smokers) | price_paid (cigarettes sold in Marren) | increase | short | CR-1 (K1 op 3 on stamping agents) → CR-5c → CR-7b | A-1 |
| C-2 | officials.revenue (state general fund) | tax_revenue (Marren cigarette tax) | increase | short | CR-1 (K1 op 4) → arithmetic ($3.50 on the new base against $1.50 on the old) | A-1, A-N1 |

The visible effect is a higher shelf price and more revenue. Revenue rises only if taxed sales fall by less than 57% (the rate rises from $1.50 to $3.50, and 1.50/3.50 is about 0.43); this is a new premise (A-N1).

## 5. Responses

**CR-2 to CR-5 by actor class.**

| Actor class | CR-2/CR-3: which chosen option is removed or burdened | CR-4 pairs (x made worse relative to y) | CR-5 |
|---|---|---|---|
| buyers.current (smokers) | Buying in Marren at the old price removed (CR-3a) | x: Marren cigarettes, y: fewer cigarettes (CR-4c); x: cigarettes, y: other tobacco or e-cigarettes; x: buy in Marren, y: buy across the line; x: buy a pack per trip, y: a carton per trip; x: buy after 1 January, y: buy and store before; x: report use tax, y: not | 5c: the range of terms is moved by the tax |
| sellers.current (wholesalers, retailers) | Selling at prior net prices (CR-3a, for the part not passed on) | x: hold stamped stock at the date (taxed by K2), y: run it down — cancelled against x: stamp after, y: stamp before (K1); see section 8 | — |
| sellers.substitutes (producers) | — | Mirror: x: make cigarette-like products under the "other tobacco" definition (made better) | — |
| intermediaries | — | x: comply, y: smuggle (gap widened); CR-10a: networks invest when the gap is expected to last | — |
| border retailers in Marren | Customers lost (CR-9) | x: accept, y: lobby; x: stay, y: move across the line (A-14, not reported) | — |
| neighboring retailers | — | Mirror: x: open or expand near the crossings | — |

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-3 | officials.revenue (state general fund) | tax_revenue_vs_static_projection | decrease | short | C-5, C-6, C-8 (taxed base shrinks) → arithmetic | A-2, A-3 |
| C-4 | buyers.current (Marren smokers) | tax_share_borne (relative to sellers) | increase | short | CR-7b (burden settles on the side with fewer alternatives: cigarettes can be sold in other states; smokers have few accepted substitutes) | A-1 |
| C-5 | buyers.current (Marren smokers) | quantity_demanded (cigarettes from all sources, from 1 January) | decrease | short | C-1 → CR-4c; CR-4b (x: smoke, y: substitute) | A-1, A-2 |
| C-6 | buyers.current (Marren smokers) | quantity_substitute (roll-your-own, cigars, little cigars, e-cigarettes) | increase | short | C-1 → CR-4b (x: cigarettes, y: untaxed or lower-taxed products) | A-1, A-6 |
| C-7 | sellers.substitutes (producers) | reclassification (cigarette-like products under the "other tobacco" definition) | increase | medium | CR-4b (x: covered form, y: uncovered form) | A-1, A-7 |
| C-8 | buyers.current (smokers near the border) | cross_border_purchases (cigarettes in Dunmarch and Kessick) | increase | short | C-1 → CR-4b (x: buy in Marren, y: buy across the line) | A-1, A-3 |
| C-9 | buyers.current (cross-border buyers) | transaction_size (cartons rather than packs) | increase | short | C-8 → CR-4c (fixed trip cost against a per-pack saving: the saving per trip grows with packs bought) | A-1, A-3, A-11 |
| C-10 | buyers.current (cross-border buyers) | informal_activity (carrying above the allowance without paying use tax; casual resale) | increase | short | CR-1 (K3 op 3) → CR-4b (x: comply, y: violate) | A-1, A-3, A-4 |
| C-11 | intermediaries (smuggling networks) | informal_activity (organized bootlegging into Marren) | increase | medium | CR-4b (x: comply, y: smuggle; gap widened) → CR-10a (gap expected to last) | A-1, A-4, A-5 |
| C-13 | buyers.current (Marren smokers) | quantity_demanded (window: October to December, stamped at the old rate) | increase | short | CR-10a (date known) → CR-4 (x: buy after 1 January, y: buy and store before) | A-9 |
| C-14 | sellers.current (wholesalers and retailers) | compliance_cost (floor-stock count and report) | increase | short | CR-1 (K2 op 4 with paperwork) → CR-8c | none |
| C-15 | sellers.current (wholesalers and retailers in Marren) | quantity_traded (Marren-stamped cigarettes) | decrease | short | C-5, C-6, C-8 → CR-12a | A-1, A-3 |
| C-27 | sellers.current (Marren border retailers and producers) | lobbying_effort | increase | medium | CR-4 (x: accept, y: lobby) | A-8 |

Notes on the responses.
- C-4: CR-7b is the dominance premise for who bears the tax. Cigarettes are made for many states and can be sold where the tax did not rise, so the side that can move is the sellers'; smokers who stay in Marren have few accepted substitutes. A-1 (most of the increase passed on) is the empirical form of this premise.
- C-5: the CR-4 exception applies to heavy smokers, for whom cigarettes are a large share of spending: the loss of means can change their other choices in either direction. It does not reverse the direction for cigarettes from all sources, which A-2 also supports.
- C-9: the cost of a trip is roughly fixed, the saving is $3.70 a pack (before the K3 allowance), so the trip pays only above some number of packs (A-11); buyers who cross buy by the carton.
- C-10: one carton per 30 days is legal; above that, use tax is owed but rarely collected (A-4).

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-12 | buyers.current (buying from informal sellers) | quality_information | decrease | medium | C-11 → CR-11b | legal and smuggled cigarettes, `same_market_other_segment` | A-1, A-4, A-5 |
| C-16 | sellers.current (Marren border retailers) | quantity_complement (fuel, snacks and other goods bought on the same trip) | decrease | short | C-8 → CR-9 | cigarettes and trip goods, `complement` (trip) | A-1, A-3, A-10 |
| C-17 | neighboring_jurisdictions (Dunmarch and Kessick retailers) | quantity_substitute (cigarette sales to Marren residents) | increase | short | C-8 → CR-9 | Marren and neighbors' cigarettes, `across_border`, close | A-1, A-3 |
| C-18 | neighboring_jurisdictions (Dunmarch and Kessick retailers) | quantity_complement (fuel, snacks sold to Marren cigarette buyers) | increase | short | C-8 → CR-9 | `complement` (trip) | A-1, A-3, A-10 |
| C-19 | neighboring_jurisdictions (Dunmarch and Kessick governments) | tax_revenue | increase | short | C-17 → CR-8b (tax paid there instead) | `across_border` | A-1, A-3 |
| C-20 | neighboring_jurisdictions (retailers near the crossings) | number_of_sellers | increase | medium | C-17 → CR-10a → CR-7a (entry until returns are back in line) | `across_border` | A-1, A-3, A-N2 |
| C-21 | factor_owners.specific (owners of Marren border retail businesses and sites) | asset_value | decrease | medium | C-15, C-16 → CR-7b (lasting loss on means that cannot move) → CR-7c | `across_border` | A-1, A-3, A-N2 |
| C-22 | neighboring_jurisdictions (owners of retail sites near the crossings) | asset_value | increase | medium | C-17 → CR-7b (lasting gain on sites in fixed supply) → CR-7c | `across_border` | A-1, A-3, A-N2 |
| C-23 | buyers.current (smokers far from the border) | tax_share_borne (relative to smokers near the border) | increase | short | CR-7b (burden settles on those without alternatives: crossing is cheap only near the line) | `across_border` | A-1, A-3 |
| C-24 | officials.enforcement (Tobacco Unit) | enforcement_cost | increase | short | CR-1 (K4) → CR-8c | — | none |
| C-25 | buyers.current (Marren smokers) | resources_available_other_uses | decrease | short | C-1 → CR-8b (tax paid is taken from smokers) → CR-3a | — | A-1 |
| C-26 | recipients of general-fund spending | resources_available_other_uses | increase | short | C-2 → CR-8b; K5 → CR-8d (earmark frees general revenue already spent on the quit program) → CR-12a | — | A-1, A-N1 |

Chains stopped: buyers of fuel and snacks in Dunmarch are diffuse bystanders past depth 3. Corruption of officers (A-12), limits on sales to Marren residents by the neighbors (A-13) and relocation of Marren border retailers (A-14) are below the cut-off.

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| officials.revenue, tax_revenue, short | higher rate per pack | smaller taxed base (C-5, C-6, C-8, C-10) | Arithmetic with A-N1: revenue rises if taxed sales fall by less than 57% | increase (C-2) |
| buyers.current vs sellers, tax_share_borne, short | smokers have few accepted substitutes | sellers' alternatives are other states | CR-7b: the burden settles on the side with fewer alternatives (smokers) | increase for smokers (C-4) |
| sellers.current, quantity_traded (Marren-stamped), short | none | cutting back (C-5), substitutes (C-6), cross-border (C-8) | none needed (CR-12a) | decrease (C-15) |
| buyers.current, quantity_demanded, window vs after | window (C-13) | after 1 January (C-5) | different windows, not netted | increase in window; decrease after |
| recipients of general-fund spending, resources_available_other_uses, short | new revenue (C-2); earmark freeing general revenue (CR-8d, A-15) | none | none needed (CR-12a) | increase (C-26) |

## 8. Time structure

- June to 1 October: the bill becomes expected from early August. Owners of Marren border retail businesses and Dunmarch sites near crossings see their expected yields change when the gap becomes expected (C-21, C-22, CR-7c), though these are reported in the medium run because the sales pattern takes time to show.
- October to December: smokers who know the date and can store cartons buy ahead at the old rate (C-13, A-9), followed by lower purchases in the first months of the year (part of C-5).
- 1 January: K2 taxes stamped stock held at 00:01 at $2.00. Without K2, the rate increase would have made stamping before the date profitable (CR-4, x: stamp after, y: stamp before); K2 cancels that gain, so no stamping rush is predicted from wholesalers (a note, not a consequence: relative to the no-policy counterfactual there is no change to record).
- Medium run: smuggling networks invest in routes because the gap is expected to last (C-11, A-5); retailers near the crossings in Dunmarch and Kessick expand (C-20); producers bring out products that fit the "other tobacco" definition (C-7). The rate is fixed in money terms, so the real gap shrinks slowly with inflation; Dunmarch's rate has not changed in 15 years.

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-25 | buyers.current (Marren smokers) | resources_available_other_uses | decrease | Other purchases forgone because of the tax and higher price | CR-8b, CR-3a |
| C-14 | sellers.current | compliance_cost | increase | Staff time counting and reporting floor stock | CR-8c |
| C-24 | officials.enforcement | enforcement_cost | increase | Eight more agents, road checks, audits | CR-8c |
| C-9 | buyers.current (cross-border buyers) | transaction_size | increase | Travel time and fuel used for trips; money tied up in cartons | CR-8c |
| C-5 | buyers.current | quantity_demanded | decrease | Cigarettes smokers would have bought at the old price | CR-3a, CR-4c |

K5's earmark: under CR-8d, money earmarked for the quit program frees general revenue that was already funding it (A-15), so the program's budget rises by less than the earmark unless other spending on it is fixed. The controlled list has no variable for a program's budget, so this is recorded only through C-26.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | Most of the increase is passed on in Marren shelf prices. | other | 0.85 | Shelf-price surveys after past increases; stamp tax collected at wholesale; smokers' few accepted substitutes. | Sellers bear more; C-1, C-4 weaken; demand chains shrink. |
| A-2 | Some smokers cut back or switch at the higher price. | substitutability | 0.85 | Range of untaxed products; past sales after increases. | C-3, C-5 rest on cross-border buying alone. |
| A-3 | Many Marren smokers can easily buy in Dunmarch or Kessick. | mobility | 0.85 | 45% of the population within 20 minutes; bridges at Port Alder; existing cross-border shopping for fuel. | C-8 to C-10, C-16 to C-23 fail. |
| A-4 | Enforcement against casual resale and carrying above the allowance is weak, and the use tax is rarely collected. | enforcement | 0.8 | 20 agents for a long border; self-reported use tax; past seizure records. | C-10 to C-12 weaken. |
| A-5 | Smuggling networks expect the price gap to last for years. | expectations | 0.65 | Dunmarch's 15-year-old rate; politics of repealing tax increases in Marren. | C-11, C-12 weaken. |
| A-6 | Untaxed or lower-taxed products are acceptable substitutes for some smokers. | substitutability | 0.75 | Market shares of roll-your-own and e-cigarettes; experience after past increases. | C-6 fails. |
| A-7 | Producers can make cigarette-like products that meet the "other tobacco" definition. | other | 0.7 | Statutory definitions of cigarette and little cigar; products already sold elsewhere. | C-7 fails. |
| A-8 | Border retailers, health groups and producers organize to change the rules. | other | 0.7 | Existing associations; past lobbying on tobacco taxes. | C-27 fails. |
| A-9 | Smokers know the date and can store cartons. | expectations | 0.8 | Publicity of the signing; cartons keep for months. | C-13 fails. |
| A-10 | Cross-border cigarette buyers also buy fuel, snacks and other goods on the same trip. | other | 0.75 | Convenience-store basket data; fuel price differences across the line. | C-16, C-18 fail. |
| A-11 | The cost of a trip is large relative to the saving on one pack but small relative to the saving on a carton. | other | 0.8 | $3.70 a pack against travel time and fuel for a 20-minute drive. | C-9 fails. |
| A-12 | Smuggling networks corrupt enforcement officers on a meaningful scale. | enforcement | 0.25 | Integrity record of the Revenue Department. | (Below cut-off; used by no reported consequence.) |
| A-13 | Dunmarch or Kessick limit sales to Marren residents. | other | 0.2 | Their revenue gain from the trade (C-19). | (Below cut-off; if true, C-17 to C-22 weaken.) |
| A-14 | Marren border retailers move across the line within five years. | mobility | 0.35 | Lease terms; licensing in the neighboring states. | (Below cut-off; used by no reported consequence.) |
| A-15 | The quit program was already funded from general revenue, and the act has no maintenance-of-effort clause. | revenue_use | 0.6 | Budget lines for the program; text of K5. | C-26 rests on new revenue alone. |
| A-N1 | Taxed sales in Marren fall by less than 57% after the increase. | other | 0.85 | Smokers' few accepted substitutes; 55% of the population lives more than 20 minutes from a border; past increases in comparable states raised revenue. | C-2 becomes ambiguous; C-26 rests on the earmark chain. |
| A-N2 | Retailers and owners of sites on both sides of the border expect the price gap to last for years. | expectations | 0.65 | Dunmarch's 15-year-old rate; the same evidence as A-5. | C-20 to C-22 fail. |

**Not reported (an assumption below 0.5).**
- Smuggling networks corrupt enforcement officers (CR-4b, x: comply, y: bribe): needs A-12 (p 0.25).
- Neighbors limit sales to Marren residents (CR-4 for their governments): needs A-13 (p 0.2).
- Marren border retailers move across the line (CR-4b, x: stay, y: move; CR-7a): needs A-14 (p 0.35).

## 11. Report

**The policy:** Marren raises its cigarette tax from $1.50 to $3.50 a pack from 1 January, taxes stamped stock on hand at that moment at $2.00 a pack, allows residents one untaxed carton from out of state every 30 days, adds eight agents to the Tobacco Unit, and earmarks $0.30 a pack for the Unit and the existing quit program. Other tobacco products and e-cigarettes are not taxed more. The two neighboring states tax cigarettes at $0.40 and $0.80.

**Visible consequences:** Smokers pay more per pack in Marren (C-1). State cigarette tax revenue rises (C-2), if taxed sales fall by less than 57% (A-N1). The Tobacco Unit spends more (C-24).

**Invisible consequences:**
- Smokers bear most of the tax relative to sellers (C-4), and smokers far from the border bear more of it than those near it (C-23). Smokers buy fewer cigarettes from all sources (C-5), switch to other tobacco and e-cigarettes (C-6), buy across the line (C-8), by the carton (C-9), and carry more than the allowance without paying use tax (C-10). Before 1 January they stock up (C-13). They have less for other purchases (C-25).
- Revenue falls short of a projection that ignores these responses (C-3). Recipients of general-fund spending have more (C-26).
- Producers bring out cigarette-like products that fit the lower-taxed definitions (C-7). Organized smuggling grows (C-11), and buyers of smuggled packs have less to judge them by (C-12).
- Marren wholesalers and retailers sell fewer stamped packs (C-15) and spend more on floor-stock reporting (C-14). Border retailers also lose sales of fuel and snacks bought on the same trip (C-16), and the value of their businesses falls (C-21). They, producers and health groups spend more on seeking changes to the rules (C-27).
- Across the line, Dunmarch and Kessick retailers sell more cigarettes and trip goods to Marren residents (C-17, C-18), more stores open near the crossings (C-20), the value of sites there rises (C-22), and those states collect more tax (C-19).

**Ambiguous effects:** None reported as ambiguous. Two signs rest on stated premises: the increase in Marren's revenue (A-N1, arithmetic) and smokers bearing most of the tax (CR-7b, A-1).

**Key conditions:** That most of the increase is passed on (A-1, p 0.85) and many smokers can reach a lower-tax state (A-3, p 0.85); that enforcement against casual carrying is weak (A-4, p 0.8). Smuggling and border-site chains need expectations that the gap lasts (A-5, p 0.65; A-N2, p 0.65). The earmark chain needs A-15 (p 0.6).

**What this analysis cannot say:** How much smoking falls, how much revenue rises, how much of the trade moves across the border or underground, or whether the tax is good policy. Health effects of smoking less, or of switching to other products, are out of scope for version 1 and are not analyzed. The method cannot say whether the quit program's budget actually rises, only that the earmark raises it by less than its face value if other funding can be withdrawn.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | buyers.current (Marren smokers) | price_paid (cigarettes sold in Marren) | increase | short | visible | B | CR-1 (K1 op 3 on stamping agents) → CR-5c (range moved) → CR-7b (burden on side with fewer alternatives) | A-1 |
| C-2 | officials.revenue (state general fund) | tax_revenue (Marren cigarette tax) | increase | short | visible | B | CR-1 (K1 op 4) → arithmetic (rate up 133%; base falls by less than 57%) | A-1, A-N1 |
| C-3 | officials.revenue (state general fund) | tax_revenue_vs_static_projection | decrease | short | invisible | B | C-5, C-6, C-8 (taxed base shrinks) → arithmetic | A-2, A-3 |
| C-4 | buyers.current (Marren smokers) | tax_share_borne (relative to sellers) | increase | short | invisible | B | CR-7b (burden settles on the side with fewer alternatives) | A-1 |
| C-5 | buyers.current (Marren smokers) | quantity_demanded (cigarettes from all sources, from 1 January) | decrease | short | invisible | B | C-1 → CR-4c; CR-4b (x: smoke, y: substitute) | A-1, A-2 |
| C-6 | buyers.current (Marren smokers) | quantity_substitute (roll-your-own, cigars, little cigars, e-cigarettes) | increase | short | invisible | B | C-1 → CR-4b (x: cigarettes, y: lower-taxed products) | A-1, A-6 |
| C-7 | sellers.substitutes (producers) | reclassification (cigarette-like products under the "other tobacco" definition) | increase | medium | invisible | B | CR-4b (x: covered form, y: uncovered form) | A-1, A-7 |
| C-8 | buyers.current (smokers near the border) | cross_border_purchases (cigarettes in Dunmarch and Kessick) | increase | short | invisible | B | C-1 → CR-4b (x: buy in Marren, y: buy across the line) | A-1, A-3 |
| C-9 | buyers.current (cross-border buyers) | transaction_size (cartons rather than packs) | increase | short | invisible | B | C-8 → CR-4c (fixed trip cost against per-pack saving; arithmetic) | A-1, A-3, A-11 |
| C-10 | buyers.current (cross-border buyers) | informal_activity (carrying above the allowance without use tax; casual resale) | increase | short | invisible | B | CR-1 (K3 op 3) → CR-4b (x: comply, y: violate) | A-1, A-3, A-4 |
| C-11 | intermediaries (smuggling networks) | informal_activity (organized bootlegging into Marren) | increase | medium | invisible | B | CR-4b (x: comply, y: smuggle) → CR-10a (gap expected to last) | A-1, A-4, A-5 |
| C-12 | buyers.current (buying from informal sellers) | quality_information | decrease | medium | invisible | B | C-11 → CR-11b | A-1, A-4, A-5 |
| C-13 | buyers.current (Marren smokers) | quantity_demanded (window: October to December, stamped at the old rate) | increase | short | invisible | B | CR-10a (date known) → CR-4 (x: buy after 1 January, y: buy and store before) | A-9 |
| C-14 | sellers.current (wholesalers and retailers) | compliance_cost (floor-stock count and report) | increase | short | invisible | A | CR-1 (K2 op 4 with paperwork) → CR-8c | none |
| C-15 | sellers.current (wholesalers and retailers in Marren) | quantity_traded (Marren-stamped cigarettes) | decrease | short | visible | B | C-5, C-6, C-8 → CR-12a | A-1, A-3 |
| C-16 | sellers.current (Marren border retailers) | quantity_complement (fuel, snacks bought on the same trip) | decrease | short | invisible | B | C-8 → CR-9 (complement, trip) | A-1, A-3, A-10 |
| C-17 | neighboring_jurisdictions (Dunmarch and Kessick retailers) | quantity_substitute (cigarette sales to Marren residents) | increase | short | invisible | B | C-8 → CR-9 (across_border) | A-1, A-3 |
| C-18 | neighboring_jurisdictions (Dunmarch and Kessick retailers) | quantity_complement (fuel, snacks sold to Marren cigarette buyers) | increase | short | invisible | B | C-8 → CR-9 (complement, trip) | A-1, A-3, A-10 |
| C-19 | neighboring_jurisdictions (Dunmarch and Kessick governments) | tax_revenue | increase | short | invisible | B | C-17 → CR-8b | A-1, A-3 |
| C-20 | neighboring_jurisdictions (retailers near the crossings) | number_of_sellers | increase | medium | invisible | B | C-17 → CR-10a → CR-7a | A-1, A-3, A-N2 |
| C-21 | factor_owners.specific (owners of Marren border retail businesses and sites) | asset_value | decrease | medium | invisible | B | C-15, C-16 → CR-7b (loss on immobile means) → CR-7c | A-1, A-3, A-N2 |
| C-22 | neighboring_jurisdictions (owners of retail sites near the crossings) | asset_value | increase | medium | invisible | B | C-17 → CR-7b (gain on sites in fixed supply) → CR-7c | A-1, A-3, A-N2 |
| C-23 | buyers.current (smokers far from the border) | tax_share_borne (relative to smokers near the border) | increase | short | invisible | B | CR-7b (burden settles on those without alternatives) | A-1, A-3 |
| C-24 | officials.enforcement (Tobacco Unit) | enforcement_cost | increase | short | visible | A | CR-1 (K4) → CR-8c | none |
| C-25 | buyers.current (Marren smokers) | resources_available_other_uses | decrease | short | invisible | B | C-1 → CR-8b → CR-3a | A-1 |
| C-26 | recipients of general-fund spending | resources_available_other_uses | increase | short | invisible | B | C-2 → CR-8b; K5 → CR-8d (earmark frees general revenue) → CR-12a | A-1, A-N1 |
| C-27 | sellers.current (Marren border retailers and producers) | lobbying_effort | increase | medium | invisible | B | CR-4 (x: accept, y: lobby) | A-8 |

## Gaps found

**(a) Calculus gaps.** None for the derivations. One recording gap: CR-8d yields "the quit program's budget rises by less than the earmark", but the controlled list has no variable for an agency's or program's budget, so the result is folded into C-26 and noted in section 9.

**(b) New premises.**
- A-N1 (p 0.85, other): the sign of revenue under a higher per-unit rate and a smaller base is an arithmetic comparison that needs a premise about how far the base falls; none of the case assumptions gives it.
- A-N2 (p 0.65, other): CR-7a and CR-7c (entry and asset values near the crossings) depend on retailers and site owners expecting the gap to last; A-5 states that expectation only for smuggling networks.

**(c) Unclear core rules.**
- CR-7b as a dominance premise (C-4, C-23): CR-7b says the lasting burden settles on means that cannot move and on "actors without alternatives". Applied to buyers versus sellers it decides the split; applied within buyers (near against far from the border) it decides a second split. The rule does not say that both readings are intended, nor whether "lasting" excludes the short-run incidence reported here.
- CR-4 for floor stock (K2): K1 alone would make stamping before the date better; K2 cancels that. CR-4 is stated for one change; with two components acting on the same pair of options in opposite directions and exactly cancelling, the analysis used CR-12 to combine, which gives "no change" rather than "ambiguous". CR-12 does not mention exact cancellation by construction.
- CR-4 exception (C-5): for heavy smokers the price rise takes a large share of means. The exception speaks of shifting "their ranking among other options in the opposite direction"; it is unclear whether it can reverse the direction for the taxed good itself. The analysis assumed it cannot here (supported by A-2).

## Comparison with the pattern-based analysis

**Summary.** Both versions agree on the main chains: a higher shelf price borne mostly by smokers, fewer stamped sales, cross-border buying, casual and then organized smuggling, switching to other tobacco and reclassified products, buying ahead before 1 January, the floor-stock paperwork, trip goods moving across the line, interior smokers bearing more, the neighbors' revenue gain and revenue below the static projection. The largest difference is coverage. The core version omits a run of consequences the pattern version derives and the core rules support: RS-10's search cost and quality variability in the informal trade, the TX-10 base effects (Marren sales tax on trip goods down, other-tobacco tax up), border retailers' lower net price, light smokers bearing more than heavy smokers, border-store employment, and the travel cost of crossing (which the core version misrecords under transaction_size). The pattern version in turn omits capitalization on both sides of the border (SB-4) and the enforcement cost of the eight new agents (OC-3). There are two sign disagreements. On cigarette tax revenue, the core version adds A-N1 (p 0.85: taxed sales fall by less than 57%), which is well supported by experience, and signs it as an increase; the pattern version leaves it ambiguous. This is a difference in premises. On the funding of enforcement, the pattern version applies OC-3 mechanically: "taxpayers' resources decrease". But K4 is funded from K5's earmark of the new tax, so its cost is borne by smokers and by the general fund's forgone share of new revenue, not by other taxpayers. Given its own ambiguous revenue sign, the pattern version cannot sign taxpayers' resources as a decrease. Finally, the pattern version lists a Tier C consequence from TS-4 (further enforcement powers), a pattern the catalog itself marks as not derivable.

**Counts.** M 13, V 5, S 2, OP 5, OC 11. Causes over S/OP/OC: P 2, K 0, A 2, E 11, J 3.

### Pattern version → core version

| Pattern ID | Core ID(s) | Class | Cause | Note |
|---|---|---|---|---|
| C-1 | C-1 (and C-4) | M | | Shelf price increase; the core version also records smokers' tax_share_borne relative to sellers, which DM-1 tells the pattern version to record and which it states only in section 7. |
| C-2 | C-15 | M | | Stamped sales in Marren decrease. |
| C-3 | C-8 | M | | Cross-border purchases increase. |
| C-4 | C-10 | V | | Casual bootlegging: bootleggers vs cross-border buyers carrying above the allowance. |
| C-5 | C-11 | M | | Organized smuggling increase, medium. |
| C-6 | C-6 | M | | Substitutes increase. |
| C-7 | C-7 | M | | Reclassification by producers increase. |
| C-8 | C-13 | V | | Buying ahead: quantity_traded vs quantity_demanded in the window. |
| C-9 | C-14 | M | | Floor-stock compliance_cost increase. |
| C-10 | C-27 | M | | Lobbying increase (both cite A-8). |
| C-11 | C-17, C-18 | V | | Neighbors' retailers: one quantity_traded entry vs separate cigarette and trip-good entries. |
| C-12 | C-16 | V | | Marren border retailers' trip goods decrease: quantity_traded vs quantity_complement. |
| C-13 | — | OC | E (core) | Border-store employment decrease. Derivable (CR-9, LW-10 from C-16). Both TX-3, which the pattern cites, and the core's own practice elsewhere use a plain employment decrease where LW-10 supports only employment or hours (a group). |
| C-14 | — | OC | E (core) | Border retailers' net_price_received decrease. CR-7b: near the line, buyers have an alternative, so more of the tax settles on those sellers. The core version applied CR-7b within buyers (C-23) but not across sellers. |
| C-15 | C-23 | M | | Interior smokers bear more. |
| C-16 | — | OC | E (core) | Light smokers bear more than heavy smokers. The core version has the mechanism (A-11, fixed trip cost) but records it only as transaction_size (C-9). CR-7b within buyers gives the pattern's claim, exactly as for C-23. |
| C-17 | — | OC | E (core) | search_cost increase for buyers of informal cigarettes (CR-11b: no open advertising). |
| C-18 | — | OC | E (core) | quality_variability increase in informal trade (CR-11b with CR-4: sellers outside courts and brands face less penalty for counterfeit or stale product). |
| C-19 | C-19 | M | | Neighbors' tax revenue increase. |
| C-20 | — | OC | E (core) | Marren sales tax on trip goods decrease (CR-8b, CR-9: the base moves with the trip). The core version recorded the trip-goods shift (C-16) but not its tax consequence. |
| C-21 | C-3 | M | | Revenue below the static projection. |
| C-22 | — | OC | J | Earmark fungibility (SB-7, CR-8d). The pattern version records it as quit-program clients' quantity_traded "funded from general revenue" decrease. This is a valid statement about general funding, but misleading as a statement about clients, whose total services probably rise by less than the earmark. The core version folded it into C-26 and called it a vocabulary gap; `quantity_traded` with a named market could have recorded the program's general-revenue funding. |
| C-23 | — | OC | P | Further enforcement powers (TS-4, Tier C). The catalog marks TS-4 as not derivable from the core rules and keeps it out of Tier A and B results. Listing it as a consequence, even at Tier C, reports something the calculus cannot support. The core version is right to omit it. |
| C-24 | C-25 | M | | Smokers' resources decrease. |
| C-25 | C-5 | V | | Purchases forgone: quantity_traded (priced out entirely) vs quantity_demanded from all sources. |
| C-26 | — | OC | E (core) | Border smokers' search_cost (travel) increase (CR-8c). The core version lists travel time and fuel under C-9 transaction_size in its opportunity-cost table; that is a misrecording. |
| C-27 | C-26 | S | P | Pattern: taxpayers' resources decrease (OC-3); core: general-fund recipients' resources increase. The enforcement expansion is funded from K5's earmark of the new tax (the pattern version's own classification says so), so OC-3's "funded by taxpayers" does not apply. The cost is borne by smokers (C-24) and by the general fund's forgone share of new revenue. With revenue ambiguous in the pattern version itself, the general fund's net position, and so other taxpayers', is ambiguous at best. With A-N1 it is an increase, as the core version says. |
| C-28 | C-12 | M | | quality_information decrease in informal trade. |
| C-29 | — | OC | E (core) | Other-tobacco tax revenue increase (base shift, CR-8b with C-6, C-7). The core version recorded the substitution but not its revenue effect. |
| — (cigarette tax_revenue, ambiguous) | C-2 | S | A | The core version adds A-N1 (p 0.85, taxed sales fall by less than 57%) and signs revenue as an increase. Both follow CR-12b correctly given their premises. The core's premise is well evidenced (state cigarette tax increases nearly always raise revenue), so the core sign is the better forecast. The pattern version's caution is defensible only if no such evidence is admitted. |
| — (new stores' earnings at the line, ambiguous) | — | OC | J | DM-3 by design. The core version records entry (C-20) and site values (C-22) instead. |

### Core-only consequences

| Core ID | Class | Cause | Note |
|---|---|---|---|
| C-9 | OP | J | Cross-border buyers buy by the carton (transaction_size increase). Valid (fixed trip cost, A-11). The pattern version used the same mechanism for incidence (C-16) instead. |
| C-20 | OP | A | Retailers near the crossings increase in number, resting on the new premise A-N2 (expectations of retailers and site owners). The pattern version implies it in its DM-3 entry but does not list it. |
| C-21 | OP | E (pattern) | asset_value decrease for Marren border retail businesses and sites. SB-4 covers a lasting change that lowers returns on assets in fixed supply; the pattern version did not apply it. |
| C-22 | OP | E (pattern) | asset_value increase for retail sites near the crossings in Dunmarch and Kessick; SB-4 again. |
| C-24 | OP | E (pattern) | enforcement_cost increase for the eight new agents (K4). OC-3 gives it directly; the pattern version recorded only the TS-4 escalation (C-23) and the funding entry (C-27). |

### Findings

- **Pattern misapplied (pattern version C-27):** OC-3 assumes enforcement is funded by taxpayers; here it is funded from an earmark of the new tax. The consequence should name smokers and the general fund, and its sign depends on the revenue sign. The catalog could add to OC-3: "where the policy funds its own enforcement from its revenue, apply CR-8b to that revenue instead".
- **Pattern not derivable (pattern version C-23):** TS-4 is quarantined in catalog 0.4 as not derivable. A worked example should not list a TS-4 consequence in the normal-form list, even at Tier C; it belongs in a note.
- **Premise difference (revenue):** the core version's A-N1 settles the sign. TX-9 and TX-10 in the pattern version do not prevent adding such a premise; the pattern version chose not to.
- **Core-version errors:** eight omissions that the core rules would have caught (RS-10-type information effects under CR-11b; TX-10-type base effects under CR-8b and CR-9; CR-7b applied to border sellers and to light smokers; border-store employment; travel cost). Travel time is misrecorded as transaction_size. The "no variable for a program's budget" gap is overstated.
- **Pattern-version omissions:** SB-4 on both sides of the border, the OC-3 enforcement_cost.
- **Core rules:** no genuine limit. The one pattern consequence the core cannot derive (C-23, TS-4) is one the catalog already marks as not derivable.
