# WE-012 Increase in the employer payroll contribution

Analyst: draft (Handbook 0.2)  |  Rule catalog version: 0.2  |  Status: awaiting expert review

A stylized policy in a fictional country. Its main lesson is the difference between who must pay a tax by law (statutory incidence, here employers) and who ends up bearing it (economic incidence), and how that changes with time. It applies DM-1 to a labor market, where workers are the sellers and employers the buyers, and shows where the rule's wording needs care. The probabilities are illustrative; the evidence column says what a real analysis would cite.

## 1. Policy record

**Norvania Social Contribution Amendment.** Norvania is a country of about 10 million people. Employers pay a social contribution on each employee's gross wage, up to a ceiling of 6,000 crowns a month; wages above the ceiling bear no contribution. Self-employed people pay a separate contribution of 8% of declared income. A national minimum wage of 1,500 crowns a month applies; about 8% of employees earn at or near it. Collective agreements cover about 40% of employees and fix money wages for one or two years at a time. About 15% of employment is informal (undeclared). Pension benefits are set by a formula based on years worked and past wages, not on the contribution rate. The government announced the increase in the budget on 10 January; it applies to wages paid from 1 July.

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Rate increase | `per_unit_tax` on labor (ad valorem on the wage) | Gross wages paid to employees, up to the ceiling | Employers | Employer contribution rises from 10% to 14% of the gross wage, up to 6,000 crowns a month per employee. The ceiling is unchanged and not indexed. | Wages above the ceiling. Self-employed income (stays at 8%, paid by the self-employed person). Non-wage benefits: meal vouchers up to 150 crowns a month and employer-paid health insurance premiums. |
| K2 Enforcement | Enforcement | K1, and the line between employees and contractors | Tax Agency and Labor Inspectorate | Monthly payroll returns; audits; complaint-driven and random inspections for undeclared work and false self-employment; fines. | None |

Revenue use: the contribution is paid into the State Pension Fund. The fund has run a deficit covered by an annual transfer from the general budget; the amendment says that transfer "will be reviewed". Pension benefits do not change. Workers therefore receive nothing in exchange for the higher contribution, which matters for incidence (section 7).

Unclear provisions: whether the Labor Inspectorate's budget rises. Assumed not.

## 2. Classification

| Component | Rothbard type | Binding? | Rule families |
|---|---|---|---|
| K1 | Binary: a forced payment to the state, levied on the hiring of labor | Yes, from 1 July, for all formal employees below the ceiling | TX, DM-1, RS, PC-10 (via the minimum wage) |
| K2 | Binary: funded by taxpayers | Yes | OC-3 |

The existing minimum wage is not part of the policy, but it is part of the situation: it stops money wages at the bottom from falling, so it changes where the tax can land.

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `employers.formal` | Firms and households employing declared workers (buyers of labor) | Each hour of labor below the ceiling costs 4% of the wage more. |
| `employers.labor_intensive` | Restaurants, retail, care, cleaning, construction | Labor is a large share of their costs. |
| `workers.formal` (`sellers.current`) | Declared employees | Their employers' cost of hiring them rises; money wages may adjust later. |
| `workers.min_wage` | Employees at or near the minimum wage | Their money wage cannot fall; their cost to employers rises. |
| `workers.below_ceiling` / `workers.above_ceiling` | Employees earning less / more than 6,000 crowns a month | The contribution is 4% of the whole wage for the first, a smaller share for the second. |
| `workers.prospective` (`sellers.prospective`) | Job seekers, young people, people returning to work | Fewer openings. |
| `workers.informal` | Undeclared workers | Wider gap between declared and undeclared labor costs. |
| `contractors` | People working as self-employed, including former employees | Lower contribution rate (8%) than employers' new 14%. |
| `input_suppliers` | Sellers of labor-saving equipment and software | More demand. |
| `buyers.labor_intensive` | Buyers of labor-intensive services | Sellers' costs rise. |
| `officials.enforcement`, `taxpayers` | Tax Agency, Labor Inspectorate, general-budget funders | More avoidance to police. |

## 4. Direct effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | `employers.formal` | `price_paid` (labor cost per hour: wage plus contribution) | increase | short to long, shrinking over time | TX-2, DM-1 | A-1 |
| C-2 | `officials.enforcement` | `tax_revenue` (social contributions) | increase | short | TX-1 | none |

C-1 is the visible effect, and the one the policy's text describes: employers pay more for each hour of labor. At first, with money wages fixed by contracts and custom, they bear the whole increase. Section 7 explains why this changes.

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-3 | `workers.prospective` | `employment` (hiring into formal jobs) | decrease | short | TX-2, TX-3 | A-1, A-2 |
| C-4 | `workers.formal` | `hours_worked` (overtime and extra shifts cut) | decrease | short | TX-2 | A-1, A-2 |
| C-5 | `employers.formal`, `contractors` | `reclassification` (employees converted to self-employed contracts) | increase | medium | RS-5 | A-3 |
| C-6 | `employers.formal` | `reclassification` (bonuses paid in June instead of later) | increase | short | RS-8 | A-6 |
| C-7 | `employers.formal`, `workers.informal` | `informal_activity` (undeclared work) | increase | medium | RS-3, TX-4 | A-4 |
| C-8 | `employers.labor_intensive` | `quantity_substitute` (labor-saving equipment, outsourcing abroad) | increase | medium to long | RS-1, TX-3 | A-5 |
| C-9 | `employers.formal` | `compliance_cost` (payroll system changes) | increase | short | TX-5 | none |
| C-10 | Employer associations, unions | `lobbying_effort` (sector or small-firm relief, higher ceiling, benefits linked to contributions) | increase | medium | RS-7 | A-7 |

C-5 is the line between employee and contractor: an employer paying 14% on an employee pays nothing on a contractor, who pays 8% herself. Where the work can be reshaped as a contract, both sides can share the difference. Not reported: employers moving whole operations abroad within five years (RS-4); A-13 is below the cut-off (p = 0.35).

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-11 | `workers.formal` | `wage_rate` (money wage, compared with the counterfactual path) | decrease | medium to long | DM-1, TX-2 | | A-8 |
| C-12 | `employers.formal` | `tax_share_borne` (relative to workers) | increase | short | DM-1 | | A-1 |
| C-13 | `workers.formal` | `tax_share_borne` (relative to employers) | increase | long | DM-1 | | A-8 |
| C-14 | `workers.below_ceiling` | `tax_share_borne` (relative to `workers.above_ceiling`) | increase | medium to long | DM-1 | | A-8 |
| C-15 | `workers.min_wage` | `employment`, `hours_worked` | decrease | short to long | PC-10, TX-2 | | A-9 |
| C-16 | `workers.prospective` | `allocation_by_non_price_criteria` (employers choose by experience and credentials) | increase | short to medium | PC-11 | | A-9 |
| C-17 | `workers.formal` | `earnings` | decrease | medium to long | DM-1, TX-3 | | A-2, A-8 |
| C-18 | `workers.informal`, `contractors` (former employees) | `search_cost` (undeclared jobs cannot be advertised); disputes outside the courts | increase | medium | RS-10 | | A-4 |
| C-19 | `input_suppliers` | `quantity_demanded` (labor-saving equipment) | increase | medium | RS-1 | labor and equipment: `substitute`, partial | A-5 |
| C-20 | `buyers.labor_intensive` | `price_paid` (labor-intensive services) | increase | short to medium | GAP-012-1 | labor: `input_to` these services | A-10 |
| C-21 | `officials.enforcement` | `tax_revenue` (personal income tax on wages) | decrease | medium to long | GAP-012-2 | | A-2, A-8 |
| C-22 | `officials.enforcement` | `tax_revenue_vs_static_projection` (social contributions) | decrease | short to medium | TX-9 | | A-2, A-3, A-4 |
| C-26 | `workers.formal` | `employment` | decrease | medium to long | TX-3, RS-1 | labor and equipment: `substitute`, partial | A-2, A-5 |

C-15 and C-16 come from the minimum wage. An employer will hire a worker only if the worker's labor is worth to the employer at least what it costs. At the minimum wage, the cost was 1.10 times the minimum; now it is 1.14 times. Workers whose labor is worth between the two to employers are now priced out, because their money wage cannot fall to absorb the tax. The minimum wage plus the higher contribution is a binding floor on labor cost for a wider group, so PC-10 and PC-11 apply to that group, and keep applying in the long run, when other workers' wages have adjusted (C-11).

C-14: above the ceiling, an extra crown of wage bears no contribution, so the tax is a smaller share of high earners' pay. As the tax passes to workers (C-13), it is a larger share of the pay of those below the ceiling.

C-18 (RS-10): undeclared workers and false contractors lose access to labor courts, inspectors and benefits that depend on declared employment; their disputes with employers are settled privately or not at all. C-19 and C-20 are at depth 3; C-20 and C-21 are Tier C because no rule carries a rise in an input's cost into the price of the output (GAP-012-1) or a fall in wages into the revenue of other taxes (GAP-012-2). Chains stop there.

Checks. RS-9: no shopping trips are involved. RS-10 applies (C-18). RS-11: the policy creates no benefit tied to a place, so it does not apply.

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| Split of the tax between employers and workers, short | — | — | DM-1, with fixed contracts | **Employers bear most** (C-12). Money wages are fixed by agreements and custom for one or two years (A-1), so workers cannot have it passed to them yet; this is the "Unless: fixed contract" exception in RS-1, applied to wages. |
| Split of the tax between employers and workers, long | — | — | DM-1 | **Workers bear most** (C-11, C-13). Over time employers' alternatives grow (capital can move into labor-saving equipment, other lines of business, other countries), while most workers' alternatives to formal employment (informal work, self-employment, not working) remain worse (A-8). Note on the side mapping: DM-1's horizon note says incidence shifts "toward buyers" as sellers' capital is redeployed. In a labor market the capital is on the buyers' side (employers), so the same reasoning shifts incidence toward the sellers (workers). See GAP-012-3. Also: this tax falls on nearly all wages, so it is close to a general tax on one factor; Rothbard's view (DM-1 note, Q3) would put it on the factor owners, workers, from the start, without the short-run phase. Not resolved. |
| `employers.formal`, `price_paid` (labor cost), medium to long | The contribution (C-1). | Money wages grow more slowly than they would have (C-11). | DM-1 | **increase**, but by less than the full contribution as wages adjust. At the minimum wage there is no wage adjustment, so the full increase remains, and is met by fewer jobs and hours (C-15). |
| `workers.formal`, `employment`, medium to long | — | Higher labor cost before wages adjust (C-3); substitution of equipment (C-8); exit of labor-intensive firms (TX-3). | None needed | **decrease** (C-26). The effect on workers above the minimum fades as their wages absorb the tax; for minimum-wage workers it persists (C-15). |
| `employers.formal`, `non_wage_compensation`, medium | Pay is reshaped into exempt benefits: meal vouchers and health premiums (RS-5). | Total compensation falls as workers come to bear the tax (DM-1, C-11), and employers cut untaxed terms such as training and flexibility along with wages. | None | **ambiguous**. What would decide it: how much room the exempt categories leave, against how far total compensation falls. |
| `contractors` (former employees), `earnings`, medium | They keep part of the contribution saved (14% against 8%), and some earn more per hour. | One-time cost of setting up as self-employed; loss of paid leave and benefits that came with employment. | DM-3 | **ambiguous** by design. Those who switched expected it to pay (LW-5); some were given no choice by their employer. |

## 8. Time structure

- **Announcement to effective date (January to June).** Employers pay bonuses in June rather than later in the year (C-6). Some hiring planned for the summer is cancelled or delayed (C-3); since the contribution applies to wages paid after 1 July whatever the hire date, there is no rush to hire before it.
- **First year.** Money wages are fixed by agreements and custom, so employers bear the tax (C-12). They respond where they can without touching wages: fewer hires (C-3), less overtime (C-4), and, at the minimum wage, fewer jobs and hours (C-15).
- **One to five years.** As agreements expire, raises are smaller than they would have been (C-11). Inflation helps this along: money wages need not be cut, only grow more slowly. Undeclared work (C-7) and false self-employment (C-5) grow as firms and workers learn the gaps in enforcement. Labor-intensive services cost more (C-20).
- **Long run.** Employers redeploy capital toward equipment and less labor-intensive activities (C-8, TS-1), which is what moves the tax onto workers (C-13). The ceiling is fixed in money terms (TS-3): as wages rise over the years, more workers cross it, and the contribution on their marginal crown falls to zero. The minimum-wage group remains the exception: their wage cannot fall, so the tax stays on their employment rather than their wage.

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-23 | `employers.formal` (short run), `workers.formal` (long run) | `resources_available_other_uses` | decrease | The investment, consumption or saving that the contribution would otherwise have paid for. Who gives it up shifts over time, as in section 7. | TX-1, OC-1 |
| C-24 | `employers.formal`, `workers.prospective` | `quantity_traded` (hours of formal employment) | decrease | Jobs and hours that both sides would have agreed at the old labor cost and no longer do; both lose the gain they expected. | OC-4, TX-2 |
| C-25 | `taxpayers` | `resources_available_other_uses` | decrease | What the Tax Agency's and Inspectorate's extra work on avoidance would otherwise have funded. | OC-3, OC-1 |

Revenue use. The pension benefits do not change, so the revenue funds no new benefit. By SB-7, the general budget's transfer to the fund is cut by part of the new revenue (A-11), so in effect the revenue joins the general budget; its use there is out of scope.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | Money wages are fixed for most workers for the first year (agreements, custom, reluctance to cut). | other | 0.85 | Coverage and duration of collective agreements; frequency of money-wage cuts. | Incidence shifts to workers sooner; C-12 weakens; C-3, C-4 shrink. |
| A-2 | Employers can adjust hiring and hours at the margin. | alternative_uses | 0.85 | Turnover rates; share of overtime; temporary contracts. | C-3, C-4, C-17 weaken. |
| A-3 | Some work can be reshaped as self-employed contracts without much risk of reclassification by the Inspectorate. | enforcement | 0.7 | Tests for false self-employment; inspection rates; growth of contracting in earlier rate rises. | C-5 not reported. |
| A-4 | Enforcement against undeclared work is weak enough that some firms expand it. | enforcement | 0.7 | Inspectorate staffing; current informal share (15%). | C-7, C-18 not reported. |
| A-5 | Labor-saving equipment and outsourcing are available for some tasks. | substitutability | 0.75 | Automation in retail and back-office work; existing outsourcing. | C-8, C-19 not reported. |
| A-6 | Employers can move bonus payments into June. | other | 0.7 | Bonus timing rules in contracts. | C-6 not reported. |
| A-7 | Employer associations and unions organize. | other | 0.8 | Existing associations; past lobbying on contributions. | C-10 not reported. |
| A-8 | Over the long run, employers have better alternatives to hiring formal labor than most workers have to formal employment. | mobility | 0.75 | Capital mobility; size of informal sector and self-employment; labor-force participation trends. | C-11, C-13, C-14, C-17 weaken; employers keep bearing more of the tax. |
| A-9 | The minimum wage plus contribution exceeds what employers will pay for some workers' labor. | binding | 0.75 | Wage distribution near the minimum; youth unemployment. | C-15, C-16 not reported. |
| A-10 | Labor-intensive service firms face competitors with the same cost increase, so they can raise prices. | other | 0.75 | Most such services are local and not traded. | C-20 not reported. |
| A-11 | The general-budget transfer to the pension fund is cut by part of the new revenue. | revenue_use | 0.75 | Budget practice; "will be reviewed". | The revenue reduces the pension deficit but still funds no new benefit. |
| A-12 | Workers do not value the contribution as payment for a benefit. | other | 0.9 | Benefits are set by formula, not linked to the contribution rate. | If benefits were linked, workers would accept lower wages more readily, and the employment effects would shrink. |
| A-13 | Employers move whole operations abroad within five years. | mobility | 0.35 | Size of the increase relative to cost differences abroad. | Below cut-off; not reported. |

## 11. Report

**The policy.** Norvania raises the contribution employers pay on wages from 10% to 14%, up to a monthly ceiling. Self-employed contributions, wages above the ceiling and certain non-wage benefits are untouched. Pension benefits do not change.

**Visible consequences.** Employers pay more for each hour of labor (C-1), and the pension fund collects more (C-2).

**Invisible consequences.**
- *Who pays changes over time.* At first, with wages fixed, employers bear the tax (C-12). Over the following years, as agreements are renewed and capital moves to other uses, wages grow more slowly than they would have, and workers come to bear most of it (C-11, C-13), especially those below the ceiling (C-14). Workers' total earnings are lower (C-17).
- *Minimum-wage workers* cannot have the tax passed to them, because their wage cannot fall. Instead fewer of them are hired and they work fewer hours (C-15), and employers choose more strictly among applicants (C-16).
- *Job seekers* find fewer openings at first (C-3), and *employees* work less overtime (C-4). Formal employment stays below the counterfactual over the following years (C-26).
- *Work leaves the formal sector*: some becomes undeclared (C-7), some is reshaped as self-employment (C-5). Those workers lose access to inspectors, courts and employment benefits (C-18).
- *Employers* buy more labor-saving equipment and outsource more (C-8, C-19), shift pay into exempt benefits, and move bonuses before the increase (C-6). Labor-intensive services cost more (C-20).
- *The state* collects less than a static projection (C-22) and less income tax on wages (C-21). Everyone who bears the contribution gives up what it would have bought (C-23); some jobs are never agreed (C-24).

**Ambiguous effects.** Whether non-wage compensation rises or falls. Whether workers who become contractors earn more or less.

**Key conditions.** That wages are fixed in the short run (A-1, p = 0.85) and that employers have better long-run alternatives than workers (A-8, p = 0.75) together decide how the burden moves from employers to workers. That the minimum wage binds for some workers (A-9, p = 0.75) is what makes the job losses at the bottom persist.

**What this analysis cannot say.** How much of the tax each side bears, or how many jobs are lost; whether the pension fund's finances justify the change; whether the policy is desirable.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | employers.formal | price_paid (labor cost) | increase | short–long | visible | B | TX-2, DM-1 | A-1 |
| C-2 | officials.enforcement | tax_revenue (contributions) | increase | short | visible | A | TX-1 | none |
| C-3 | workers.prospective | employment (formal hiring) | decrease | short | invisible | B | TX-2, TX-3 | A-1, A-2 |
| C-4 | workers.formal | hours_worked | decrease | short | invisible | B | TX-2 | A-1, A-2 |
| C-5 | employers.formal, contractors | reclassification (to self-employment) | increase | medium | invisible | B | RS-5 | A-3 |
| C-6 | employers.formal | reclassification (bonus timing) | increase | short | invisible | B | RS-8 | A-6 |
| C-7 | employers.formal, workers.informal | informal_activity | increase | medium | invisible | B | RS-3, TX-4 | A-4 |
| C-8 | employers.labor_intensive | quantity_substitute (equipment, outsourcing) | increase | medium–long | invisible | B | RS-1, TX-3 | A-5 |
| C-9 | employers.formal | compliance_cost | increase | short | invisible | A | TX-5 | none |
| C-10 | employer associations, unions | lobbying_effort | increase | medium | invisible | B | RS-7 | A-7 |
| C-11 | workers.formal | wage_rate | decrease | medium–long | invisible | B | DM-1, TX-2 | A-8 |
| C-12 | employers.formal | tax_share_borne | increase | short | invisible | B | DM-1 | A-1 |
| C-13 | workers.formal | tax_share_borne | increase | long | invisible | B | DM-1 | A-8 |
| C-14 | workers.below_ceiling | tax_share_borne | increase | medium–long | invisible | B | DM-1 | A-8 |
| C-15 | workers.min_wage | employment, hours_worked | decrease | short–long | invisible | B | PC-10, TX-2 | A-9 |
| C-16 | workers.prospective | allocation_by_non_price_criteria | increase | short–medium | invisible | B | PC-11 | A-9 |
| C-17 | workers.formal | earnings | decrease | medium–long | invisible | B | DM-1, TX-3 | A-2, A-8 |
| C-18 | workers.informal, contractors | search_cost | increase | medium | invisible | B | RS-10 | A-4 |
| C-19 | input_suppliers | quantity_demanded (equipment) | increase | medium | invisible | B | RS-1 | A-5 |
| C-20 | buyers.labor_intensive | price_paid | increase | short–medium | invisible | C | GAP-012-1 | A-10 |
| C-21 | officials.enforcement | tax_revenue (income tax on wages) | decrease | medium–long | invisible | C | GAP-012-2 | A-2, A-8 |
| C-22 | officials.enforcement | tax_revenue_vs_static_projection | decrease | short–medium | invisible | B | TX-9 | A-2, A-3, A-4 |
| C-23 | employers.formal, then workers.formal | resources_available_other_uses | decrease | short–long | invisible | A | TX-1, OC-1 | none |
| C-24 | employers.formal, workers.prospective | quantity_traded (formal hours) | decrease | short–medium | invisible | B | OC-4, TX-2 | A-1, A-2 |
| C-25 | taxpayers | resources_available_other_uses | decrease | short | invisible | A | OC-3, OC-1 | none |
| C-26 | workers.formal | employment | decrease | medium–long | invisible | B | TX-3, RS-1 | A-2, A-5 |
| — | employers.formal | non_wage_compensation | ambiguous | medium | invisible | B | RS-5 vs DM-1 | A-8 |
| — | contractors (former employees) | earnings | ambiguous | medium | invisible | B | C-5 vs setup and benefit loss; DM-3 | A-3 |

## Gaps found

- GAP-012-1: No rule carries a rise in the cost of an input (here labor) into the price or quantity of the goods made with it. TX-7 mentions that input users "face higher costs" but stops there. Needed for C-20. Proposed new TX rule "Input cost pass-through": where a policy raises the cost of an input, sellers of goods that use it intensively and whose competitors face the same increase raise `price_paid` for their buyers; where competitors do not face it (imports, untaxed sellers), the sellers' `quantity_supplied` decreases instead (RS-6). Tier B, assuming the share of the input in costs and the competitors' exposure.
- GAP-012-2: No rule carries a shrinking base of one tax to the revenue of other taxes (here, lower wages mean less personal income tax). Needed for C-21. Proposed rule "Base erosion spreads to other taxes": where a policy lowers wages, employment or sales that bear other taxes, `tax_revenue` from those taxes decreases. Tier B, inheriting the assumptions that shrink the base. (WE-010 found the same gap as GAP-010-2.)
- GAP-012-3: DM-1's horizon note ("seller alternatives grow as capital can be redeployed, so incidence shifts toward buyers over time") is written for product markets, where the sellers own the capital. In factor markets such as labor, the capital is on the buyers' side, and the same reasoning moves incidence toward the sellers. Applied literally, the note gives the wrong direction here. The analysis used DM-1's main statement with A-8 instead, so C-11 and C-13 stay Tier B. Proposed fix: restate the note in terms of whichever side owns the redeployable capital, and add a worked line for factor markets.
