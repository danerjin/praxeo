# WE-002 Local excise tax on sweetened drinks, earmarked for pre-school

Analyst: draft (Handbook 0.5)  |  Rule catalog version: 0.5  |  Status: awaiting expert review

A stylized policy in a fictional town. It resembles real city drink taxes but is not one of them. The probabilities are illustrative.

## 1. Policy record

**Lakeport Beverage Tax.** Lakeport is a town of about 150,000 people. Three neighboring towns, each 10 to 15 minutes' drive from most Lakeport homes, have no such tax. Many Lakeport households already do part of their grocery shopping in large stores just outside the town line.

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Excise tax | `per_unit_tax` | Drinks with added sugar, distributed to retailers in Lakeport | Distributors | 1.5 cents per fluid ounce, collected from distributors on deliveries into the town | Drinks sweetened only with non-caloric sweeteners; milk-based drinks; 100% juice |
| K2 Earmark | `lump_sum_subsidy` | Pre-school places | Town | Revenue funds free pre-school places for 3- and 4-year-olds, run by the town and by approved providers | None |
| K3 Administration | Enforcement | K1 | Town revenue department | Distributor registration, monthly returns, audits | None |

Unclear provisions: U1, whether approved providers may include existing private pre-schools on equal terms. U1-a: yes, with limits on places (the reading assumed in the text); U1-b: no. Where a sign depends on the reading, one sign per reading is given.

## 2. Classification

| Component | Rothbard type | Binding? | Rule families |
|---|---|---|---|
| K1 | Binary: a forced payment to the town | Yes, from the effective date | TX, RS |
| K2 | Binary: a transfer from the town to families and providers, funded by the tax (payers: C-15; recipients: C-3, C-22) | Yes | SB |
| K3 | Binary: funded from the tax's own revenue (OC-3, third funding case) | Yes | OC |

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `distributors` | Deliver drinks to Lakeport retailers | Must pay the tax and file returns. |
| `retailers.lakeport` | Shops, restaurants and vending operators in Lakeport | Higher wholesale cost on taxed drinks; customers can shop elsewhere. |
| `buyers.lakeport.mobile` | Residents who shop outside the town anyway, or easily could | Can buy taxed drinks across the line. |
| `buyers.lakeport.immobile` | Residents without a car, or with little time to travel | Can switch to untaxed drinks or pay the tax. |
| `retailers.neighbors` | Shops just outside Lakeport | More Lakeport customers. |
| `producers.untaxed` | Makers and sellers of exempt drinks (water, diet drinks, juice) | More demand. |
| `families.preschool` | Families with 3- and 4-year-olds | Free places offered. |
| `providers.private_preschool` | Existing private pre-schools | Compete with free places, or join as approved providers. |
| `officials.enforcement`, `taxpayers` | Revenue department and its funders | New administrative task. |

## 4. Direct effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | `buyers.lakeport` | `price_paid` for taxed drinks in Lakeport | increase | short | TX-2 | A-1 |
| C-2 | `buyers.lakeport` | `quantity_traded` of taxed drinks in Lakeport | decrease | short | TX-2 | A-1, A-2 |
| C-3 | `families.preschool` | `price_paid` for pre-school (free places) | decrease | short to medium | SB-2 | A-6 |

C-2 is the intended effect: less sugar-sweetened drink bought in Lakeport. C-3 is how the revenue is spent.

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-4 | `buyers.lakeport.mobile` | `cross_border_purchases` of taxed drinks | increase | short | TX-4, RS-4 | A-3 |
| C-5 | `buyers.lakeport` | `quantity_substitute` (exempt drinks) | increase | short | RS-1, TX-3 | A-2 |
| C-6 | `producers` | `reclassification` (reformulation with non-caloric sweeteners, larger sizes of exempt types) | increase | medium | RS-5, TX-4 | A-4 |
| C-7 | `distributors` | `compliance_cost` | increase | short | TX-5 | none |
| C-8 | `providers.private_preschool` | `quantity_demanded` for paid places | decrease | short to medium | SB-3, RS-1 | A-6 |
| C-9 | `retailers.lakeport`, `distributors`, approved `providers.private_preschool` | `lobbying_effort` (retailers and distributors for repeal or wider exemptions; approved providers to keep the program) | increase | medium | RS-7, SB-5 | A-12 |

Not reported: evasion through untaxed deliveries (RS-3). The tax is collected from a small number of registered distributors, which makes it easy to audit; A-5 is below the cut-off (p = 0.3).

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-10 | `retailers.neighbors` | `quantity_traded` (all goods) | increase | short | RS-4 | Lakeport and neighbor stores: `across_border`, close for mobile buyers | A-3 |
| C-11 | `retailers.lakeport` | `quantity_traded` of other groceries bought on the same trip as drinks (not exempt drinks, see C-5) | decrease | short | RS-4, RS-9 | taxed drinks and other groceries: `complement`, note `trip` | A-3, A-7 |
| C-12 | `retailers.lakeport`, especially near the town line | `employment`, `hours_worked` | at_least_one_decrease | medium | TX-3, RS-9, OC-5 | | A-3, A-7, A-9 |
| C-13 | `buyers.lakeport.immobile` | `tax_share_borne` (relative to mobile buyers) | increase | short | DM-1 | | A-3 |
| C-14 | `providers.private_preschool` | `number_of_sellers` (independent private providers) | U1-a: ambiguous; U1-b: decrease | medium | SB-3, RS-6 (−); under U1-a, approval adds a funded option (CR-1 op 2, +); CR-12b | free and paid places: `substitute`, close | A-6 |
| C-20 | town budget | `resources_available_other_uses` (general fund) | increase | medium | SB-7 (earmarked revenue for places frees general money the town would otherwise have spent on places) | the town's own budget | A-8 |
| C-26 | `families.preschool` buying paid places | `price_substitute` (fees for paid private places) | decrease | medium | C-8 → CR-9 → CR-6 (with paid demand lower, fees tend to a lower clearing level) | free and paid places: `substitute`, close | A-6 |
| C-27 | `families.preschool` | `quantity_traded` (pre-school places used, all providers) | increase | medium | SB-2, SB-8 (a free place adds to places used only for children who would otherwise have stayed at home or in informal care), SB-7 (bounded by A-10); CR-12 | free places, paid places and home care: `substitute` | A-10, A-11 |
| C-21 | `officials.enforcement`, `taxpayers` | `tax_revenue_vs_static_projection` | decrease | short | TX-9 | | A-1, A-2, A-3 |
| C-22 | `families.preschool` who would have paid for a private place anyway | `resources_available_other_uses` | increase | short to medium | SB-8 | | A-6 |
| C-23 | `sellers` of the goods drink buyers would have bought with the tax money | `employment`, `hours_worked` | at_least_one_decrease | short to medium | OC-5, OC-1 | | A-9 |
| C-24 | pre-school providers and staff paid from the revenue | `employment`, `hours_worked` | at_least_one_increase | short to medium | OC-5 | | A-9 |

C-11 and C-12 are not obvious. If some buyers drive across the line for drinks, many will buy the rest of their groceries there too (RS-9). Lakeport stores lose those sales as well, not just the drinks.

C-22: for families who would have paid for a private place anyway, a free place works like a cash transfer; they spend the money they save on other things (SB-8). C-23 and C-24 are Hazlitt's tailor (OC-5): the jobs funded by the revenue are visible; the jobs that would have been supported by what the taxpayers would otherwise have bought are not.

C-20: Lakeport already funds some pre-school places from its general budget. Unless the law fixes that funding, the town can reduce it as the earmarked money arrives, so the general fund has more for other uses than without the tax (SB-7), and the number of places rises by less than the earmark alone would pay for. (Catalog 0.3 recorded this as "places funded compared with the earmarked amount: decrease", which compares with the earmark rather than with the no-tax world; the counterfactual comparison is the freed general fund.) Whether places used rise at all depends on the earmarked spending exceeding what the town would have spent anyway (A-10), and on some free places going to children who would otherwise have had none (A-11): C-27.

C-14 depends on U1. Under U1-a, private pre-schools can supply funded places, which keeps some open against the loss of paying families; the two chains conflict (CR-12b). Under U1-b only the loss of paying families acts. C-26: with fewer paying families, private fees fall below what they would have been.

C-12 and C-23, C-24 record employment and hours as a group (TX-3, OC-5): sellers may cut or add hours rather than staff. C-12 combines the chains that reach Lakeport retail: trips and purchases moved across the line (C-4, C-11) and the tax paid by continuing buyers, which leaves retail (C-15), push down; buyers who switch to exempt drinks in the same store (C-5) keep its volume, and are not an independent chain pushing up. C-21: the tax base shrinks through C-2 and C-4, so revenue falls short of a projection made at pre-tax sales (TX-9).

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| Lakeport residents' total consumption of taxed drinks (from all sources), short | — | Higher price (C-1) at the Lakeport shelf; switching to exempt drinks (C-5). | — | **decrease** (C-28), but by less than C-2 suggests, because part of the fall in Lakeport sales is moved across the line (C-4), not given up. |
| Split of the tax between buyers and sellers, short | — | — | DM-1 | **Not determined overall.** Each side's price moves as TX-2 says (C-1). Within buyers, DM-1 with A-3: immobile buyers have clearly fewer alternatives than mobile ones and bear more of it (C-13). How the rest splits between retailers and distributors would need a premise comparing their alternatives, and is not signed. |
| Pre-school places used, all providers, medium | Free places taken by children who would otherwise have had none (A-11). | Free places taken from paid places (C-8) or from places the town would have funded anyway (SB-7, C-20) add nothing. | A-10: earmarked spending exceeds the town's counterfactual spending on places, so fungibility cannot reduce places below the no-tax level (CR-12e, empirical premise). | **increase** (C-27), by less than the number of free places. |
| `providers.private_preschool`, `number_of_sellers`, medium | U1-a: approval opens a funded option. | Paying families move to free places (C-8). | None | **U1-a: ambiguous; U1-b: decrease** (C-14). |
| `retailers.lakeport`, `employment` and `hours_worked`, medium | None independent (switching to exempt drinks in the same store is part of the same choices as C-2). | Trips moved across the line (C-4, C-11); tax paid by continuing buyers (C-15). | None needed | **at_least_one_decrease** (C-12). |

## 8. Time structure

- Cross-border buying (C-4) and switching to exempt drinks (C-5) start at once.
- Reformulation (C-6) takes months, as producers develop and launch new products.
- Store employment and hours (C-12) and any private pre-school closures (C-14) take a year or more.
- Expectations: if other towns are expected to adopt the same tax, cross-border buying will be expected to be temporary, and retailers outside the line will not expand for it (TS-2).

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-15 | `buyers.lakeport` who keep buying taxed drinks in town | `resources_available_other_uses` | decrease | The goods they would have bought with the money paid in tax. | TX-1, OC-1 |
| C-16 | `buyers.lakeport.mobile` | `search_cost` (travel time and cost) | increase | Time and travel cost of shopping across the line. | OC-2 |
| C-18 | `officials.enforcement` | `enforcement_cost` | increase | Staff time and budget used on registration, returns and audits. It is paid from the tax's own revenue (OC-3, third funding case), so it reduces what the revenue funds (CR-8d), not general taxpayers' means; it is not recorded again as a separate consequence, because without the tax there would be no revenue to compare with. | OC-3 |
| C-25 | town budget | `tax_revenue` | increase | The receipt side of C-15 (TX-1, CR-8b): what drink buyers pay is received by the town, and spent on K2 and K3. | TX-1 |

Two entries from draft 0.1 are dropped as duplicates: compliance resources (already C-7) and purchases priced out by the tax (already C-2).

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | Lakeport retailers pass at least part of the tax on in shelf prices. | other | 0.9 | Distributor-level per-unit taxes; competitive retail; shelf-price surveys from comparable towns. | C-1 fails; C-2 shrinks; the burden falls on sellers. |
| A-2 | Buyers have untaxed substitutes they consider acceptable (water, diet drinks, juice). | substitutability | 0.9 | Exemption list; shelf range. | C-5 fails; C-2 shrinks. |
| A-3 | Enough Lakeport residents can easily shop in the neighboring towns. | mobility | 0.8 | Drive times of 10 to 15 minutes; existing cross-border shopping habits; car ownership. | C-4, C-10 to C-13 fail. |
| A-4 | Reformulation or relabeling to an exempt category is feasible for some products. | other | 0.7 | Existing diet versions; exemption definitions. | C-6 fails. |
| A-5 | Distributors evade the tax on a meaningful scale. | enforcement | 0.3 | Small number of registered distributors; audit powers. | Below cut-off; not reported. |
| A-6 | Free places draw some families who would otherwise have paid for private places. | substitutability | 0.85 | Current private enrollment among 3- and 4-year-olds. | C-8, C-14, C-22 and C-26 fail. |
| A-7 | Shoppers bundle drink purchases with other groceries on the same trip. | other | 0.7 | Shopping surveys; store layout and basket composition. | C-11, C-12 weaken. |
| A-8 | Lakeport would otherwise have funded some pre-school places from general revenue, and the law does not fix that funding level. | revenue_use | 0.65 | Current budget lines for early education; whether the ordinance has a maintenance-of-effort clause. | C-20 not reported. |
| A-9 | Sellers adjust their staffing or hours to their sales. | alternative_uses | 0.75 | Share of part-time and flexible staff in local retail and services. | C-12, C-23, C-24 weaken. |
| A-10 | Earmarked spending on free places exceeds what the town would otherwise have spent on pre-school places from general revenue. | revenue_use | 0.7 | The program funds free places for all 3- and 4-year-olds from the whole revenue; current early-education budget lines. | C-27 becomes ambiguous. |
| A-11 | Some families who would have kept their 3- and 4-year-olds at home or in informal care take a free place. | substitutability | 0.8 | Share of 3- and 4-year-olds not enrolled in any pre-school before the program. | C-27 fails: free places only replace other places. |
| A-12 | Lakeport retailers, the few registered distributors and approved pre-school providers can organize and spend to change or defend the tax at a cost below their stakes. | other | 0.75 | Small number of distributors; existing retail and provider associations. | C-9 not reported. |

## 11. Report

**The policy.** Lakeport taxes drinks with added sugar at 1.5 cents per ounce, collected from distributors, and spends the revenue on free pre-school places. Diet drinks, milk drinks and pure juice are exempt. Neighboring towns are untaxed and 10 to 15 minutes away.

**Visible consequences.** Sugary drinks cost more in Lakeport (C-1), and fewer are sold there (C-2). The town collects the tax (C-25). Families with young children get free pre-school places (C-3), and more children attend pre-school than would have (C-27).

**Invisible consequences.**
- *Lakeport buyers* switch to exempt drinks (C-5), and those who can, buy taxed drinks in neighboring towns (C-4), so total consumption falls (C-28), but by less than sales in Lakeport do. Residents who cannot easily travel bear more of the tax (C-13).
- *Lakeport retailers* lose drink sales and also the other groceries their customers now buy on cross-border trips (C-11). Over time, employment or hours in Lakeport stores, especially near the town line, are lower than they would have been (C-12). Retailers just outside the line gain (C-10).
- *Producers* reformulate drinks to fall into exempt categories (C-6).
- *Private pre-schools* lose paying families to the free places (C-8) and charge lower fees than they would have (C-26). If they cannot become approved providers (reading U1-b), some close; if they can (U1-a), the number that close is not determined (C-14). Places used rise by less than the number of free places created (C-27), and the town can trim the general funding it already gave pre-school, freeing general money for other uses (C-20).
- *The town* collects less than a projection based on pre-tax sales, because the base shrinks (C-21).
- *Distributors* bear compliance costs (C-7); the revenue department's administration is paid out of the tax revenue (C-18). Everyone who keeps buying taxed drinks in town gives up what they would have bought with the money paid in tax (C-15). The jobs or hours the revenue pays for in pre-school (C-24) are matched by fewer jobs or hours among the sellers of what the taxpayers would otherwise have bought (C-23).
- *Families already paying for private pre-school* who switch to a free place have more to spend on other things (C-22).

**Ambiguous effects.** How the tax splits between buyers and sellers overall cannot be determined; the analysis can only say that immobile buyers bear more than mobile ones (C-13). Whether the number of private pre-schools falls, if they can be approved as providers (C-14, reading U1-a).

**Key conditions.** Cross-border shopping (A-3, p = 0.8) drives most of the less obvious effects; in a town far from untaxed neighbors they would be much weaker. That places used rise rests on the earmark exceeding what the town would have spent anyway (A-10, p = 0.7).

**What this analysis cannot say.** How large any effect is; health effects (out of scope for version 1); whether the trade-off is worthwhile.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | buyers.lakeport | price_paid (taxed drinks, in town) | increase | short | visible | B | TX-2 | A-1 |
| C-2 | buyers.lakeport | quantity_traded (taxed drinks, in town) | decrease | short | visible | B | TX-2 | A-1, A-2 |
| C-3 | families.preschool | price_paid (pre-school) | decrease | short–medium | visible | B | SB-2 | A-6 |
| C-4 | buyers.lakeport.mobile | cross_border_purchases | increase | short | invisible | B | TX-4, RS-4 | A-3 |
| C-5 | buyers.lakeport | quantity_substitute (exempt drinks) | increase | short | invisible | B | RS-1, TX-3 | A-2 |
| C-6 | producers | reclassification | increase | medium | invisible | B | RS-5, TX-4 | A-4 |
| C-7 | distributors | compliance_cost | increase | short | invisible | A | TX-5 | none |
| C-8 | providers.private_preschool | quantity_demanded (paid places) | decrease | short–medium | invisible | B | SB-3, RS-1 | A-6 |
| C-9 | retailers, distributors, approved providers | lobbying_effort | increase | medium | invisible | B | RS-7, SB-5 | A-12 |
| C-10 | retailers.neighbors | quantity_traded (all goods) | increase | short | invisible | B | RS-4 | A-3 |
| C-11 | retailers.lakeport | quantity_traded (other groceries on drink trips) | decrease | short | invisible | B | RS-4, RS-9 | A-3, A-7 |
| C-12 | retailers.lakeport | employment, hours_worked | at_least_one_decrease | medium | invisible | B | TX-3, RS-9, OC-5 | A-3, A-7, A-9 |
| C-13 | buyers.lakeport.immobile | tax_share_borne | increase | short | invisible | B | DM-1 | A-3 |
| C-14 | providers.private_preschool | number_of_sellers | U1-a: ambiguous; U1-b: decrease | medium | invisible | B | SB-3, RS-6; CR-1 (op 2 under U1-a); CR-12b | A-6 |
| C-15 | buyers.lakeport | resources_available_other_uses | decrease | short | invisible | A | TX-1, OC-1 | none |
| C-16 | buyers.lakeport.mobile | search_cost | increase | short | invisible | B | OC-2 | A-3 |
| C-18 | officials.enforcement | enforcement_cost | increase | short | invisible | A | OC-3 | none |
| C-20 | town budget | resources_available_other_uses (general fund) | increase | medium | invisible | B | SB-7 | A-8 |
| C-21 | officials.enforcement | tax_revenue_vs_static_projection | decrease | short | invisible | B | TX-9 | A-1, A-2, A-3 |
| C-22 | families.preschool (would have paid anyway) | resources_available_other_uses | increase | short–medium | invisible | B | SB-8 | A-6 |
| C-23 | sellers (forgone purchases) | employment, hours_worked | at_least_one_decrease | short–medium | invisible | B | OC-5, OC-1 | A-9 |
| C-24 | pre-school providers | employment, hours_worked | at_least_one_increase | short–medium | visible | B | OC-5 | A-9 |
| C-25 | town budget | tax_revenue | increase | short | visible | A | TX-1 | none |
| C-26 | families.preschool (paid places) | price_substitute (private fees) | decrease | medium | invisible | B | SB-3, CR-9, CR-6 | A-6 |
| C-27 | families.preschool | quantity_traded (places used, all providers) | increase | medium | visible | B | SB-2, SB-8, SB-7; CR-12 | A-10, A-11 |
| C-28 | buyers.lakeport | quantity_demanded (taxed drinks, from all sources) | decrease | short | invisible | B | TX-2, RS-1 (in town the tax, across the line the trip, raise what a unit costs them) | A-1, A-2 |

## Gaps found

- GAP-4 (closed in catalog 0.2): RS-9 bundled trips; C-11 and C-12 now Tier B.
- GAP-5 (out of scope): health and nutrient variables; reports now say so explicitly.
- GAP-6 (closed in catalog 0.2): SB-7 earmark fungibility; C-20 added.
- GAP-7 (closed in catalog 0.2): TX-9 and `tax_revenue_vs_static_projection`; C-21 added.
- GAP-11 (closed in catalog 0.2): `tax_share_borne` used for C-13.
- Catalog 0.3: SB-8 and OC-5 added; C-22 to C-24 added.
- Catalog 0.5: corrected after the core-only comparison (see ../05_examples_core/WE-002_drinks_excise_core.md): C-14 given per-reading signs (U1-a ambiguous, U1-b decrease); added tax revenue (C-25), lower private fees (C-26) and places used (C-27, new premises A-10, A-11); C-20 re-recorded against the no-tax baseline as freed general fund; employment recorded as employment-or-hours groups (C-12, C-23, C-24); RS-7 premise A-12 and lobbying classes narrowed; OC-3 third funding case (C-18 now enforcement_cost, paid from the revenue); DM-1 split claim limited to what A-3 supports; section 7's total-consumption claim listed as C-28.
