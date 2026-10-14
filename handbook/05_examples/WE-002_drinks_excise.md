# WE-002 Local excise tax on sweetened drinks, earmarked for pre-school

Analyst: draft (Handbook 0.1)  |  Rule catalog version: 0.1  |  Status: awaiting expert review

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
| C-11 | `retailers.lakeport` | `quantity_traded` of untaxed goods (bought on the same trip as drinks) | decrease | short | RS-4, `GAP-4` | taxed drinks and other groceries: `complement` (bundled shopping trips) | A-3, A-7 |
| C-12 | `retailers.lakeport`, especially near the town line | `employment` | decrease | medium | TX-3 | | A-3, A-7 |
| C-13 | `buyers.lakeport.immobile` | share of tax borne | larger than for mobile buyers | short | DM-1 | | A-3 |
| C-14 | `providers.private_preschool` | `number_of_sellers` (independent private providers) | decrease | medium | SB-3, RS-6 | free and paid places: `substitute`, close | A-6 |

C-11 and C-12 are not obvious. If some buyers drive across the line for drinks, many will buy the rest of their groceries there too. Lakeport stores lose those sales as well, not just the drinks.

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

| ID | Actor class | What is given up | Rules |
|---|---|---|---|
| C-15 | `buyers.lakeport` who keep buying taxed drinks in town | The goods they would have bought with the money paid in tax. | TX-1, OC-1 |
| C-16 | `buyers.lakeport.mobile` | Time and travel cost of shopping across the line. | OC-2 |
| C-17 | `distributors` | Resources spent on compliance (C-7). | OC-1 |
| C-18 | `taxpayers` | What the revenue department's budget for this task would otherwise have funded. | OC-3 |
| C-19 | `buyers.lakeport`, `retailers.lakeport` | Purchases priced out by the tax: both sides lose the gain they expected. | OC-4 |

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

## 11. Report

**The policy.** Lakeport taxes drinks with added sugar at 1.5 cents per ounce, collected from distributors, and spends the revenue on free pre-school places. Diet drinks, milk drinks and pure juice are exempt. Neighboring towns are untaxed and 10 to 15 minutes away.

**Visible consequences.** Sugary drinks cost more in Lakeport (C-1), and fewer are sold there (C-2). Families with young children get free pre-school places (C-3).

**Invisible consequences.**
- *Lakeport buyers* switch to exempt drinks (C-5), and those who can, buy taxed drinks in neighboring towns (C-4), so total consumption falls by less than sales in Lakeport do. Residents who cannot easily travel bear more of the tax (C-13).
- *Lakeport retailers* lose drink sales and also the other groceries their customers now buy on cross-border trips (C-11). Over time, employment in Lakeport stores, especially near the town line, is lower than it would have been (C-12). Retailers just outside the line gain (C-10).
- *Producers* reformulate drinks to fall into exempt categories (C-6).
- *Private pre-schools* lose paying families to the free places (C-8), and some close (C-14), so the total number of pre-school places rises by less than the number of free places created.
- *Distributors and taxpayers* bear compliance and administration costs (C-7, C-18), and everyone who pays the tax gives up what they would have bought with the money (C-15).

**Ambiguous effects.** How the tax splits between buyers and sellers overall cannot be determined; the analysis can only say which subgroups bear more.

**Key conditions.** Cross-border shopping (A-3, p = 0.8) drives most of the less obvious effects; in a town far from untaxed neighbors they would be much weaker.

**What this analysis cannot say.** How large any effect is; health effects (outside the method's vocabulary; see `GAP-5`); whether the trade-off is worthwhile.

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
| C-11 | retailers.lakeport | quantity_traded (untaxed goods) | decrease | short | invisible | C | RS-4, GAP-4 | A-3, A-7 |
| C-12 | retailers.lakeport | employment | decrease | medium | invisible | C | TX-3, GAP-4 | A-3, A-7 |
| C-13 | buyers.lakeport.immobile | tax share borne | increase | short | invisible | B | DM-1 | A-3 |
| C-14 | providers.private_preschool | number_of_sellers | decrease | medium | invisible | B | SB-3, RS-6 | A-6 |
| C-15 | buyers.lakeport | resources_available_other_uses | decrease | short | invisible | A | TX-1, OC-1 | none |
| C-16 | buyers.lakeport.mobile | travel time | (loss) | short | invisible | B | OC-2 | A-3 |
| C-17 | distributors | compliance resources | (loss) | short | invisible | A | OC-1 | none |
| C-18 | taxpayers | resources_available_other_uses | decrease | short | invisible | A | OC-3 | none |
| C-19 | buyers.lakeport, retailers.lakeport | prevented purchases | (loss) | short | invisible | B | OC-4 | A-1 |

C-11 and C-12 are Tier C because they rely on a move that is not yet a rule (`GAP-4`). Once a rule for bundled shopping trips is reviewed and added, they become Tier B.

## Gaps found

- GAP-4: no rule for complementarity through bundled shopping trips (cross-border buying of a taxed good pulls untaxed purchases with it).
- GAP-5: no variables for health or consumption of a nutrient; out of scope for version 1, but readers will ask.
- GAP-6: no rule for fungibility of earmarked revenue. If the town would have funded some pre-school places from the general budget anyway, the earmark adds fewer places than it appears to.
- GAP-7: no variable for revenue relative to a static projection (projections that ignore the responses overstate revenue).
