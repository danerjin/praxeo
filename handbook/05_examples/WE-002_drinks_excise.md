# WE-002 Local excise tax on sweetened drinks, earmarked for pre-school

Analyst: draft (Handbook 0.3)  |  Rule catalog version: 0.3  |  Status: awaiting expert review

A stylized policy in a fictional town. It resembles real city drink taxes but is not one of them. The probabilities are illustrative.

## 1. Policy record

**Lakeport Beverage Tax.** Lakeport is a town of about 150,000 people. Three neighboring towns, each 10 to 15 minutes' drive from most Lakeport homes, have no such tax. Many Lakeport households already do part of their grocery shopping in large stores just outside the town line.

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Excise tax | `per_unit_tax` | Drinks with added sugar, distributed to retailers in Lakeport | Distributors | 1.5 cents per fluid ounce, collected from distributors on deliveries into the town | Drinks sweetened only with non-caloric sweeteners; milk-based drinks; 100% juice |
| K2 Earmark | `lump_sum_subsidy` | Pre-school places | Town | Revenue funds free pre-school places for 3- and 4-year-olds, run by the town and by approved providers | None |
| K3 Administration | Enforcement | K1 | Town revenue department | Distributor registration, monthly returns, audits | None |

Unclear provisions: whether approved providers may include existing private pre-schools on equal terms. Assumed yes, with limits on places.

## 2. Classification

| Component | Rothbard type | Binding? | Rule families |
|---|---|---|---|
| K1 | Binary: a forced payment to the town | Yes, from the effective date | TX, RS |
| K2 | Binary: a transfer from the town to families and providers | Yes | SB |
| K3 | Binary: funded from tax revenue | Yes | OC |

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
| C-9 | `retailers.lakeport`, `distributors`, `families.preschool`, `providers.private_preschool` | `lobbying_effort` | increase | medium | RS-7, SB-5 | none |

Not reported: evasion through untaxed deliveries (RS-3). The tax is collected from a small number of registered distributors, which makes it easy to audit; A-5 is below the cut-off (p = 0.3).

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-10 | `retailers.neighbors` | `quantity_traded` (all goods) | increase | short | RS-4 | Lakeport and neighbor stores: `across_border`, close for mobile buyers | A-3 |
| C-11 | `retailers.lakeport` | `quantity_traded` of untaxed goods (bought on the same trip as drinks) | decrease | short | RS-4, RS-9 | taxed drinks and other groceries: `complement`, note `trip` | A-3, A-7 |
| C-12 | `retailers.lakeport`, especially near the town line | `employment` | decrease | medium | TX-3, RS-9 | | A-3, A-7 |
| C-13 | `buyers.lakeport.immobile` | `tax_share_borne` (relative to mobile buyers) | increase | short | DM-1 | | A-3 |
| C-14 | `providers.private_preschool` | `number_of_sellers` (independent private providers) | decrease | medium | SB-3, RS-6 | free and paid places: `substitute`, close | A-6 |
| C-20 | `families.preschool` | pre-school places funded (`quantity_traded`, public places), compared with the earmarked amount | decrease | medium | SB-7 | | A-8 |
| C-21 | `officials.enforcement`, `taxpayers` | `tax_revenue_vs_static_projection` | decrease | short | TX-9 | | A-1, A-2, A-3 |
| C-22 | `families.preschool` who would have paid for a private place anyway | `resources_available_other_uses` | increase | short to medium | SB-8 | | A-6 |
| C-23 | `sellers` of the goods drink buyers would have bought with the tax money | `employment` | decrease | short to medium | OC-5, OC-1 | | A-9 |
| C-24 | pre-school providers and staff paid from the revenue | `employment` | increase | short to medium | OC-5 | | A-9 |

C-11 and C-12 are not obvious. If some buyers drive across the line for drinks, many will buy the rest of their groceries there too (RS-9). Lakeport stores lose those sales as well, not just the drinks.

C-22: for families who would have paid for a private place anyway, a free place works like a cash transfer; they spend the money they save on other things (SB-8). C-23 and C-24 are Bastiat's tailor (OC-5): the jobs funded by the revenue are visible; the jobs that would have been supported by what the taxpayers would otherwise have bought are not.

C-20: Lakeport already funds some pre-school places from its general budget. Unless the law fixes that funding, the town can reduce it as the earmarked money arrives, so the number of places rises by less than the earmark alone would pay for (SB-7). C-21: the tax base shrinks through C-2 and C-4, so revenue falls short of a projection made at pre-tax sales (TX-9).

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| Lakeport residents' total consumption of taxed drinks (from all sources), short | — | Higher price (C-1) at the Lakeport shelf; switching to exempt drinks (C-5). | — | **decrease**, but by less than C-2 suggests, because part of the fall in Lakeport sales is moved across the line (C-4), not given up. |
| Split of the tax between buyers and sellers, short | — | — | DM-1 | **Not determined overall.** By DM-1: immobile buyers have the fewest alternatives and bear more of it (C-13). Lakeport retailers near the town line face close competition and absorb more of it in their margins. |
| Pre-school places, all providers, medium | Free places (C-3). | Private paid places decline as families switch (C-8, C-14). | None needed | **increase**, but by less than the number of free places, because some free places replace places families were already paying for. |

## 8. Time structure

- Cross-border buying (C-4) and switching to exempt drinks (C-5) start at once.
- Reformulation (C-6) takes months, as producers develop and launch new products.
- Store employment (C-12) and private pre-school closures (C-14) take a year or more.
- Expectations: if other towns are expected to adopt the same tax, cross-border buying will be expected to be temporary, and retailers outside the line will not expand for it (TS-2).

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-15 | `buyers.lakeport` who keep buying taxed drinks in town | `resources_available_other_uses` | decrease | The goods they would have bought with the money paid in tax. | TX-1, OC-1 |
| C-16 | `buyers.lakeport.mobile` | `search_cost` (travel time and cost) | increase | Time and travel cost of shopping across the line. | OC-2 |
| C-18 | `taxpayers` | `resources_available_other_uses` | decrease | What the revenue department's budget for this task would otherwise have funded. | OC-3 |

Two entries from draft 0.1 are dropped as duplicates: compliance resources (already C-7) and purchases priced out by the tax (already C-2).

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | Lakeport retailers pass at least part of the tax on in shelf prices. | other | 0.9 | Distributor-level per-unit taxes; competitive retail; shelf-price surveys from comparable towns. | C-1 fails; C-2 shrinks; the burden falls on sellers. |
| A-2 | Buyers have untaxed substitutes they consider acceptable (water, diet drinks, juice). | substitutability | 0.9 | Exemption list; shelf range. | C-5 fails; C-2 shrinks. |
| A-3 | Enough Lakeport residents can easily shop in the neighboring towns. | mobility | 0.8 | Drive times of 10 to 15 minutes; existing cross-border shopping habits; car ownership. | C-4, C-10 to C-13 fail. |
| A-4 | Reformulation or relabeling to an exempt category is feasible for some products. | other | 0.7 | Existing diet versions; exemption definitions. | C-6 fails. |
| A-5 | Distributors evade the tax on a meaningful scale. | enforcement | 0.3 | Small number of registered distributors; audit powers. | Below cut-off; not reported. |
| A-6 | Free places draw some families who would otherwise have paid for private places. | substitutability | 0.85 | Current private enrollment among 3- and 4-year-olds. | C-8, C-14 fail. |
| A-7 | Shoppers bundle drink purchases with other groceries on the same trip. | other | 0.7 | Shopping surveys; store layout and basket composition. | C-11, C-12 weaken. |
| A-8 | Lakeport would otherwise have funded some pre-school places from general revenue, and the law does not fix that funding level. | revenue_use | 0.65 | Current budget lines for early education; whether the ordinance has a maintenance-of-effort clause. | C-20 not reported. |
| A-9 | Sellers adjust their staffing to their sales. | alternative_uses | 0.75 | Share of part-time and flexible staff in local retail and services. | C-23, C-24 weaken. |

## 11. Report

**The policy.** Lakeport taxes drinks with added sugar at 1.5 cents per ounce, collected from distributors, and spends the revenue on free pre-school places. Diet drinks, milk drinks and pure juice are exempt. Neighboring towns are untaxed and 10 to 15 minutes away.

**Visible consequences.** Sugary drinks cost more in Lakeport (C-1), and fewer are sold there (C-2). Families with young children get free pre-school places (C-3).

**Invisible consequences.**
- *Lakeport buyers* switch to exempt drinks (C-5), and those who can, buy taxed drinks in neighboring towns (C-4), so total consumption falls by less than sales in Lakeport do. Residents who cannot easily travel bear more of the tax (C-13).
- *Lakeport retailers* lose drink sales and also the other groceries their customers now buy on cross-border trips (C-11). Over time, employment in Lakeport stores, especially near the town line, is lower than it would have been (C-12). Retailers just outside the line gain (C-10).
- *Producers* reformulate drinks to fall into exempt categories (C-6).
- *Private pre-schools* lose paying families to the free places (C-8), and some close (C-14), so the total number of pre-school places rises by less than the number of free places created. The free places themselves rise by less than the earmark suggests, if the town trims the general funding it already gave pre-school (C-20).
- *The town* collects less than a projection based on pre-tax sales, because the base shrinks (C-21).
- *Distributors and taxpayers* bear compliance and administration costs (C-7, C-18), and everyone who pays the tax gives up what they would have bought with the money (C-15). The jobs the revenue pays for in pre-school (C-24) are matched by fewer jobs among the sellers of what the taxpayers would otherwise have bought (C-23).
- *Families already paying for private pre-school* who switch to a free place have more to spend on other things (C-22).

**Ambiguous effects.** How the tax splits between buyers and sellers overall cannot be determined; the analysis can only say which subgroups bear more.

**Key conditions.** Cross-border shopping (A-3, p = 0.8) drives most of the less obvious effects; in a town far from untaxed neighbors they would be much weaker.

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
| C-9 | retailers, distributors, families, providers | lobbying_effort | increase | medium | invisible | B | RS-7, SB-5 | none |
| C-10 | retailers.neighbors | quantity_traded (all goods) | increase | short | invisible | B | RS-4 | A-3 |
| C-11 | retailers.lakeport | quantity_traded (untaxed goods) | decrease | short | invisible | B | RS-4, RS-9 | A-3, A-7 |
| C-12 | retailers.lakeport | employment | decrease | medium | invisible | B | TX-3, RS-9 | A-3, A-7 |
| C-13 | buyers.lakeport.immobile | tax_share_borne | increase | short | invisible | B | DM-1 | A-3 |
| C-14 | providers.private_preschool | number_of_sellers | decrease | medium | invisible | B | SB-3, RS-6 | A-6 |
| C-15 | buyers.lakeport | resources_available_other_uses | decrease | short | invisible | A | TX-1, OC-1 | none |
| C-16 | buyers.lakeport.mobile | search_cost | increase | short | invisible | B | OC-2 | A-3 |
| C-18 | taxpayers | resources_available_other_uses | decrease | short | invisible | A | OC-3 | none |
| C-20 | families.preschool | quantity_traded (public places) vs earmark | decrease | medium | invisible | B | SB-7 | A-8 |
| C-21 | officials.enforcement | tax_revenue_vs_static_projection | decrease | short | invisible | B | TX-9 | A-1, A-2, A-3 |
| C-22 | families.preschool (would have paid anyway) | resources_available_other_uses | increase | short–medium | invisible | B | SB-8 | A-6 |
| C-23 | sellers (forgone purchases) | employment | decrease | short–medium | invisible | B | OC-5, OC-1 | A-9 |
| C-24 | pre-school providers | employment | increase | short–medium | visible | B | OC-5 | A-9 |

## Gaps found

- GAP-4 (closed in catalog 0.2): RS-9 bundled trips; C-11 and C-12 now Tier B.
- GAP-5 (out of scope): health and nutrient variables; reports now say so explicitly.
- GAP-6 (closed in catalog 0.2): SB-7 earmark fungibility; C-20 added.
- GAP-7 (closed in catalog 0.2): TX-9 and `tax_revenue_vs_static_projection`; C-21 added.
- GAP-11 (closed in catalog 0.2): `tax_share_borne` used for C-13.
- Catalog 0.3: SB-8 and OC-5 added; C-22 to C-24 added.
