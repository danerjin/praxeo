# WE-012 / Analysis: Norvania Social Contribution Amendment (employer payroll contribution from 10% to 14%)

Analyst: core-only re-run (Handbook 0.4)  |  Rules: core rules CR-1 to CR-12 only  |  Status: awaiting comparison

Every derivation below cites only the core rules (CR-1 to CR-12, with clause), the foundations (AX-1, LW-1 to LW-10) and arithmetic. Assumptions A-1 to A-14 are the case assumptions as given; A-N1 is a premise this re-run had to add.

## 1. Policy record

| Field | Value | Source sentence |
|---|---|---|
| Jurisdiction (and what lies just outside) | Norvania, about 10 million people. Abroad (A-13) is the outside option for whole operations; inside the country, the boundaries that matter are the contribution ceiling, self-employment, exempt non-wage benefits and informal work. | Policy record preamble. |
| Announced / enacted / effective / expires | Announced in the budget on 10 January; applies to wages paid from 1 July; no expiry. | "The government announced the increase in the budget on 10 January; it applies to wages paid from 1 July." |
| Enforcement (who, penalties, resources) | Tax Agency and Labor Inspectorate: monthly payroll returns, audits, inspections for undeclared work and false self-employment, fines. Whether the Inspectorate's budget rises is unclear (assumed not). | K2; unclear provisions. |
| Existing rules (in force in the counterfactual too) | Ceiling of 6,000 crowns a month per employee; self-employed contribution 8% of declared income; national minimum wage of 1,500 crowns a month (about 8% of employees at or near it); collective agreements cover about 40% of employees and fix money wages for one or two years; about 15% of employment informal; pension benefits set by a formula based on years worked and past wages, not on the contribution rate. | Policy record preamble. |

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Rate increase | `ad_valorem_tax` on labor (a percentage of the wage) | Gross wages paid to employees, up to the ceiling | Employers | Employer contribution rises from 10% to 14% of the gross wage, up to 6,000 crowns a month per employee. The ceiling is unchanged and not indexed. | Wages above the ceiling. Self-employed income (stays at 8%, paid by the self-employed person). Non-wage benefits: meal vouchers up to 150 crowns a month and employer-paid health insurance premiums. |
| K2 Enforcement | Enforcement | K1, and the line between employees and contractors | Tax Agency and Labor Inspectorate | Monthly payroll returns; audits; complaint-driven and random inspections for undeclared work and false self-employment; fines. | None |

Revenue use: the contribution is paid into the State Pension Fund. The fund has run a deficit covered by an annual transfer from the general budget; the amendment says that transfer "will be reviewed". Pension benefits do not change. Workers therefore receive nothing in exchange for the higher contribution, which matters for incidence (section 7).

Unclear provisions: whether the Labor Inspectorate's budget rises. Assumed not.

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | Core rules applied |
|---|---|---|---|
| K1 | Binary (the state takes a payment on each wage) | Binds on every formal employer, on the part of each wage up to 6,000 crowns | CR-1, CR-3a, CR-4, CR-5c, CR-6 (with the existing minimum wage), CR-7, CR-8, CR-10 |
| K2 | Enforcement | Attaches risk (not removal) to undeclared work and false self-employment, since detection is incomplete (A-3, A-4) | CR-1 (enforcement premise), CR-4 (x: comply, y: violate) |

Arithmetic. Per employee earning W at or below the ceiling, employer cost rises from 1.10 W to 1.14 W, a rise of about 3.6% of total labor cost. For an employee earning above 6,000 crowns, the added contribution is a fixed 240 crowns a month (4% of 6,000), and any further crown of pay above the ceiling bears no contribution. At the minimum wage, employer cost rises from 1,650 to 1,710 crowns a month. The gap between the employer contribution on a wage (14%) and the self-employed contribution (8%, paid by the worker) widens from 2 to 6 points of income.

**CR-1 operations by component and actor class.** Operations: (1) remove an option, (2) add an option, (3) change what an option brings, (4) transfer means.

| Actor class | K1 | K2 |
|---|---|---|
| `employers.formal` | 3 (employing a worker below the ceiling now carries a larger payment); 4 (the payment transfers their means to the pension fund) | 3 (risk of fines attached to undeclared work and false self-employment, unchanged in law but more often run) |
| `workers.formal` | none directly; their options change through employers' choices (CR-9) | none |
| `workers.min_wage` | none directly; the existing floor stops their wage from falling, so the change reaches them through CR-6 | none |
| `workers.above_ceiling` | none directly; employers' cost per head rises by a fixed 240 crowns | none |
| `self_employed` | none (rate unchanged); the contract form improves relative to employment (3, relative) | 3 (reclassification risk) |
| `workers.informal` | none directly | 3 (inspection risk) |
| `pension_fund` | 4 (receives the revenue) | none |
| `government.general_budget` | none directly; its transfer to the fund "will be reviewed" (A-11) | none |
| `officials.enforcement` | none | 3 (more cases at an unchanged budget) |
| Buyers of labor-intensive services, sellers of labor-saving equipment | none directly; reached through CR-9 | none |

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `employers.formal` | Firms employing declared workers | Labor below the ceiling costs more; exempt forms (contracts, vouchers, insurance premiums, pay above the ceiling, undeclared work, equipment) improve relatively |
| `employers.labor_intensive_services` | Restaurants, care, cleaning, retail: local, untraded, labor-heavy (A-10, A-14) | Same, with the option to raise prices since rivals face the same cost |
| `workers.formal` | Declared employees earning up to the ceiling | Employers' demand for their labor falls; wages fixed at first (A-1) |
| `workers.min_wage` | Employees at or near the 1,500-crown minimum | Wage cannot fall; other terms and jobs take the pressure |
| `workers.below_ceiling` | Employees earning up to 6,000 crowns (the subset of `workers.formal` compared with high earners in C-17) | The added contribution is 4% of their whole pay |
| `workers.above_ceiling` | Employees earning over 6,000 crowns | Per-head cost up by a fixed amount; added pay untaxed |
| `workers.covered_agreements` | The 40% under collective agreements | Wages fixed until renewal, then bargained in a moved range (CR-5c) |
| `self_employed` | Contractors at 8% | Demand for contracts rises (A-3) |
| `workers.informal` | Undeclared workers | Demand for undeclared work rises (A-4) |
| `buyers.labor_intensive_services` | Households and firms buying local services | Pay more (A-10, A-14) |
| `sellers.substitutes` | Sellers of labor-saving equipment and outsourced services (A-5) | Demand rises |
| `pension_fund` | Receives contributions | More revenue |
| `government.general_budget` | Funds the pension deficit | Transfer may be cut (A-11) |
| `lobby.employers_unions` | Employer associations and unions (A-7) | Stake in exemptions and rate |
| `officials.enforcement` | Tax Agency, Labor Inspectorate | More avoidance to police, same budget |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | employers.formal | price_paid (labor cost per employee at or below the ceiling) | increase | short | CR-1 op 3, op 4; arithmetic (about +3.6% at a fixed wage); CR-7b (wages cannot adjust at first, so the burden settles on employers) | A-1 |
| C-2 | pension_fund | tax_revenue | increase | short | CR-1 op 4; CR-8b | none |
| C-3 | employers.formal | return_on_capital | decrease | short | CR-3a; CR-7b (wages fixed, A-1, so employers bear the change until they adjust) | A-1 |

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-4 | workers.formal | employment | decrease | short | CR-4c (x: employ the marginal worker, y: not; the last worker, valued least, is the first not hired or replaced); CR-10a (hires made after 10 January carry the higher cost from July) | A-1, A-2 |
| C-5 | workers.formal | employment | decrease | long | CR-4b for employers (x: formal labor, y: equipment, contracts, abroad); CR-4b for workers (x: formal job at a lower wage, y: self-employment, informal work, not working); CR-7b | A-2, A-8 |
| C-6 | workers.min_wage | employment, hours_worked, non_wage_compensation | at_least_one_decrease | medium | CR-6 (the existing floor keeps the money wage from falling, so the pressure moves to the open margins: jobs, hours, non-wage terms) | A-9 |
| C-7 | workers.formal | wage_rate | decrease | medium | CR-5c (the employer's limit in each bargain falls by the contribution, moving the range within which wages are agreed at each renewal); CR-7b | A-1, A-8, A-12 |
| C-8 | workers.formal | wage_rate | decrease | long | CR-7b (employers have better alternatives than most workers, so the lasting burden settles on workers); CR-4 (workers do not supply more labor in return, as they receive no benefit) | A-8, A-12 |
| C-9 | workers.above_ceiling | hours_worked | ambiguous | medium | (+) CR-4b (x: an extra worker below the ceiling, y: extra hours from an above-ceiling worker whose added pay bears no contribution; arithmetic: the rise is a fixed 240 crowns per head); (−) CR-4c (higher total labor cost, less output, fewer hours); CR-12b | A-2 |
| C-10 | self_employed | reclassification (employment contracts turned into self-employed contracts) | increase | medium | CR-4b (x: covered form, y: uncovered form; arithmetic: the gap widens from 2 to 6 points); CR-4b (x: comply, y: violate) where the contract is false self-employment | A-3 |
| C-11 | employers.formal | reclassification (wage paid as meal vouchers up to 150 crowns or as health insurance premiums) | increase | short | CR-4b (x: covered form, y: uncovered form) | A-N1 |
| C-12 | workers.informal | informal_activity | increase | medium | CR-4b (x: comply, y: violate); CR-1 (incomplete enforcement attaches a risk, not a removal) | A-4 |
| C-13 | sellers.substitutes | quantity_substitute (labor-saving equipment and outsourced services) | increase | medium | CR-4b (x: labor, y: equipment or outsourcing); CR-9 (substitute) | A-5 |
| C-14 | lobby.employers_unions | lobbying_effort | increase | short | CR-4b (x: accept, y: lobby) | A-7 |
| C-15 | pension_fund | tax_revenue_vs_static_projection | decrease | short | CR-10a, CR-4b (x: pay bonuses from July, y: in June) | A-6 |
| C-16 | pension_fund | tax_revenue_vs_static_projection | decrease | medium | CR-4b, CR-4c (base shrinks through C-4, C-10, C-11, C-12) | A-2 |
| C-17 | workers.below_ceiling | tax_share_borne | increase | long | CR-7b; arithmetic (the added contribution is 4% of pay up to 6,000 crowns and a falling share of pay above it) | A-8 |

## 6. Second-order effects

Market relations: `formal_labor` and `labor_intensive_services`: `input_to`, close (A-14). `formal_labor` and `labor_saving_equipment`: `substitute`, partial (A-5). `formal_labor` and `self_employed_contracts`, `informal_labor`: `same_market_other_segment`, partial (A-3, A-4). `pension_fund_contributions` and `general_budget_transfer`: `substitute` (fungible sources of the fund's money), close (A-11).

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-18 | buyers.labor_intensive_services | price_paid | increase | medium | CR-9 (labor is an input); CR-7a (all sellers face the same rise and are brought back into line by raising prices) | input_to; depth 2 | A-10, A-14 |
| C-19 | buyers.labor_intensive_services | quantity_demanded | decrease | medium | CR-4c (LW-3) | input_to; depth 3 | A-10, A-14 |
| C-20 | employers.labor_intensive_services | employment | decrease | medium | CR-9 (less output, less demand for the labor that produces it; LW-10) | input_to; depth 4 | A-10, A-14 |
| C-21 | workers.informal | disputes_settled_outside_courts | increase | medium | CR-11b (undeclared work cannot use courts or inspectors to enforce its terms) | same_market_other_segment; depth 3 | A-4 |
| C-22 | government.general_budget | resources_available_other_uses | increase | medium | CR-8d (money is fungible: new fund revenue lets the general-budget transfer be cut) | substitute (sources of fund money); depth 2 | A-11 |
| C-23 | workers.formal | earnings | decrease | long | Arithmetic from C-5 (employment) and C-8 (wage rate), both lower; CR-12a for earnings as their product | same market; depth 2 | A-2, A-8, A-12 |

Interaction of components. K2 sets the price of the two exits (false self-employment, undeclared work); with the Inspectorate's budget unchanged while avoidance rises, the chance that any one case is inspected falls (CR-1: the risk attached to the exit shrinks), which strengthens C-10 and C-12. This feedback is noted, not separately signed.

Not followed further: effects on firms that sell inputs to labor-intensive services (diffuse bystanders after depth 3).

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance premise | Combined sign |
|---|---|---|---|---|
| workers.above_ceiling, hours_worked, medium | Hours replace heads, since added pay is untaxed (CR-4b) | Higher labor cost, less output (CR-4c) | None stated. CR-12b | ambiguous (C-9) |
| workers.formal, wage_rate, long | none | CR-7b (A-8): burden shifts to workers | CR-7b premise A-8: employers have better alternatives than workers, so the side without alternatives (workers) bears the lasting burden. Workers receive no benefit for the contribution (A-12), so no chain pushes the other way through labor supply | decrease (C-8) |
| employers.formal, return_on_capital | Short: none | Short: C-3 | Medium and long: CR-7a brings employers' returns back in line with other uses as wages adjust and capital moves; no lasting sign | short decrease only (C-3) |
| workers.formal, employment, wage_rate, earnings | — | — | Different variables, not netted (CR-12c) | separate (C-4, C-5, C-7, C-8, C-23) |
| Incidence note | | | In the short run (wages fixed, A-1) employers bear the tax (C-1, C-3); over the medium and long run it moves to workers through slower wage growth (C-7, C-8); workers at the minimum wage cannot absorb it through the wage, so it reaches them through jobs, hours or other terms (C-6) | |

## 8. Time structure

Horizons: short = 10 January to the end of the first year after 1 July; medium = years 2 to 5; long = beyond 5 years.

- **Announcement (CR-10a).** From 10 January, a hire carries the higher cost from 1 July, so marginal hiring slows before the rate changes (C-4).
- **Timing shift (CR-10a).** Where contracts allow (A-6), bonuses due after 1 July are paid in June at the old rate: bonus payments in June rise; bonus payments in July to December fall. Without the policy there would be no reason to move them, so this is a note on the path; its effect on revenue is C-15.
- **Fixed money wages (CR-10b).** Wages are fixed for most workers in the first year (A-1), so the burden starts on employers (C-3) and moves to workers only as agreements are renewed (C-7) and as the stock of jobs adjusts through hiring rather than layoffs (CR-10b).
- **Shrinking share of the wage bill.** The ceiling is not indexed. As money wages grow, more workers rise above the fixed ceiling, so a smaller share of the wage bill bears the contribution, and the added cost of a high earner shrinks relative to pay. The added cost of a worker below the ceiling stays at 4% of pay, so the gap in C-17 widens over time (arithmetic, CR-10).
- **Reversal costs.** Labor-saving equipment bought and contracts restructured (C-10, C-13) persist if the rate is later cut (CR-10b).
- **Relocation of whole operations** abroad within five years (A-13, p 0.35): not reported.

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-24 | employers.formal | resources_available_other_uses | decrease | The added contribution in the short run, before wages adjust | CR-8a, CR-8b; CR-3a |
| C-25 | workers.formal | resources_available_other_uses | decrease | The contribution's lasting burden, taken through lower wages and fewer jobs, with no benefit in return | CR-8a, CR-8b; CR-3a |
| C-26 | employers.formal | compliance_cost | increase | Resources spent restructuring contracts, pay packages and payroll to avoid the contribution | CR-8c |
| C-4, C-6 | workers.formal, workers.min_wage | employment (in section 5) | decrease | Jobs that would have been filled, and the gain each party expected from them | CR-5a |
| C-14 | lobby.employers_unions | lobbying_effort (in section 5) | increase | Resources used up in lobbying | CR-8c |

Revenue: the contribution goes to the pension fund. Pension benefits do not change (CR-8b: the fund's receipt equals what employers and, over time, workers pay). If the general-budget transfer is cut (A-11), the new revenue frees general-budget money for other uses (C-22, CR-8d); what that money is then spent on is not analyzed.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | Money wages are fixed for most workers for the first year (agreements, custom, reluctance to cut). | other | 0.85 | Coverage and duration of collective agreements; frequency of money-wage cuts. | C-1, C-3, C-24 shift toward workers at once; C-7 starts sooner. |
| A-2 | Employers can adjust hiring and hours at the margin. | alternative_uses | 0.85 | Turnover rates; share of overtime; temporary contracts. | C-4, C-5, C-9, C-16, C-23 fail. |
| A-3 | Some work can be reshaped as self-employed contracts without much risk of reclassification by the Inspectorate. | enforcement | 0.7 | Tests for false self-employment; inspection rates; growth of contracting in earlier rate rises. | C-10 fails. |
| A-4 | Enforcement against undeclared work is weak enough that some firms expand it, and penalties for it are enforced at least sometimes. | enforcement | 0.7 | Inspectorate staffing; current informal share (15%); fines actually imposed. | C-12, C-21 fail. |
| A-5 | Labor-saving equipment and outsourcing are available for some tasks. | substitutability | 0.75 | Automation in retail and back-office work; existing outsourcing. | C-13 fails. |
| A-6 | Employers can move bonus payments into June. | other | 0.7 | Bonus timing rules in contracts. | C-15 fails; timing note in section 8 fails. |
| A-7 | Employer associations and unions organize. | other | 0.8 | Existing associations; past lobbying on contributions. | C-14 fails. |
| A-8 | Over the long run, employers have better alternatives to hiring formal labor than most workers have to formal employment. | mobility | 0.75 | Capital mobility; size of informal sector and self-employment; labor-force participation trends. | C-5, C-7, C-8, C-17, C-23, C-25: burden stays with employers; wage signs fail. |
| A-9 | The minimum wage plus contribution exceeds what employers will pay for some workers' labor. | binding | 0.75 | Wage distribution near the minimum; youth unemployment. | C-6 fails. |
| A-10 | Labor-intensive service firms face competitors with the same cost increase, so they can raise prices. | other | 0.75 | Most such services are local and not traded. | C-18 to C-20 fail. |
| A-11 | The general-budget transfer to the pension fund is cut by part of the new revenue. | revenue_use | 0.75 | Budget practice; "will be reviewed". | C-22 fails. |
| A-12 | Workers do not value the contribution as payment for a benefit. | other | 0.9 | Benefits are set by formula, not linked to the contribution rate. | C-7, C-8: workers might accept lower wages willingly; direction unchanged but the employment chain C-5 weakens. |
| A-13 | Employers move whole operations abroad within five years. | mobility | 0.35 | Size of the increase relative to cost differences abroad. | Below cut-off; not used. |
| A-14 | Labor-intensive service firms cannot replace labor at its old cost within the short to medium run; labor is a material part of their costs. | substitutability | 0.85 | Labor's share of costs in restaurants, care, cleaning and retail; pace of automation in those services. | C-18 to C-20 fail. |
| A-N1 | Some employers and workers can move part of pay into meal vouchers (up to 150 crowns a month) or employer-paid health insurance premiums at little loss in value to the worker. | substitutability | 0.7 | Current use of vouchers and premiums; share of workers below the voucher cap; how workers value premiums. | C-11 fails. |

## 11. Report

**The policy:** From 1 July, Norvanian employers pay a social contribution of 14% instead of 10% on each employee's wage up to 6,000 crowns a month. Pay above the ceiling, self-employed income (8%, paid by the worker), meal vouchers up to 150 crowns a month and employer-paid health premiums are not affected. The money goes to the State Pension Fund; benefits do not change. It was announced on 10 January.

**Visible consequences:** Employers' cost per employee rises by about 3.6% at an unchanged wage (C-1); the pension fund collects more (C-2); in the first year, with wages fixed, employers' returns fall (C-3). Employer associations and unions lobby (C-14).

**Invisible consequences:**
- *Workers.* Marginal hiring slows from the announcement (C-4) and formal employment stays lower in the long run (C-5). Wages grow more slowly than they would have, at renewals (C-7) and in the long run (C-8), so workers' earnings fall (C-23) and workers end up bearing much of the contribution with nothing in return (C-25). Workers below the ceiling bear more of it than high earners (C-17). For workers at the minimum wage, whose wage cannot fall, at least one of jobs, hours or non-wage terms falls (C-6).
- *Avoidance.* More work moves to self-employed contracts (C-10), into exempt vouchers and premiums (C-11) and into undeclared work (C-12), where disputes are settled outside the courts (C-21). Employers buy more labor-saving equipment and outsourcing (C-13). Restructuring uses up resources (C-26). Bonuses are moved into June (section 8). Revenue falls short of the rate times the old base (C-15, C-16).
- *Customers.* Prices of local labor-intensive services rise (C-18), customers buy less (C-19) and those services employ fewer people (C-20).
- *Budget.* If the general-budget transfer to the fund is cut, general-budget money is freed for other uses (C-22).

**Ambiguous effects:** Hours of workers above the ceiling (C-9): the fixed per-head rise and untaxed extra pay favor longer hours over more hires, while the higher total cost of labor favors fewer hours. What would decide it: how far firms can substitute hours of high earners for hires below the ceiling.

**Key conditions:** The shift of the burden to workers rests on A-8 (0.75) and A-12 (0.9). The short-run burden on employers rests on A-1 (0.85). Avoidance chains rest on A-3 (0.7), A-4 (0.7) and the new premise A-N1 (0.7). The customer chain rests on A-10 (0.75) and A-14 (0.85).

**What this analysis cannot say:** How much employment falls, how fast wages adjust, how the burden splits in numbers, or whether the pension fund's finances improve on balance. It does not weigh the gains to the fund against the losses to workers and employers, and does not say whether the policy is good. Health, safety and environmental effects are not analyzed. Not reported (assumption below 0.5): relocation of whole operations abroad (A-13, p 0.35).

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | employers.formal | price_paid (labor cost per employee at or below the ceiling) | increase | short | visible | B | CR-1 op 3, op 4; arithmetic; CR-7b (fixed wages leave the burden on employers) | A-1 |
| C-2 | pension_fund | tax_revenue | increase | short | visible | A | CR-1 op 4; CR-8b | none |
| C-3 | employers.formal | return_on_capital | decrease | short | visible | B | CR-3a; CR-7b | A-1 |
| C-4 | workers.formal | employment | decrease | short | invisible | B | CR-4c (x: employ the marginal worker, y: not); CR-10a | A-1, A-2 |
| C-5 | workers.formal | employment | decrease | long | invisible | B | CR-4b (employers: x: formal labor, y: equipment, contracts; workers: x: formal job at lower wage, y: other options); CR-7b | A-2, A-8 |
| C-6 | workers.min_wage | employment, hours_worked, non_wage_compensation | at_least_one_decrease | medium | invisible | B | CR-6 (floor holds the wage; pressure moves to open margins) | A-9 |
| C-7 | workers.formal | wage_rate | decrease | medium | invisible | B | CR-5c (bargaining range moves at renewal); CR-7b | A-1, A-8, A-12 |
| C-8 | workers.formal | wage_rate | decrease | long | invisible | B | CR-7b (burden settles on the side with fewer alternatives); CR-4 | A-8, A-12 |
| C-9 | workers.above_ceiling | hours_worked | ambiguous | medium | invisible | B | (+) CR-4b (x: extra hire, y: extra hours above the ceiling); (−) CR-4c; arithmetic; CR-12b | A-2 |
| C-10 | self_employed | reclassification (employment to self-employed contracts) | increase | medium | invisible | B | CR-4b (x: covered form, y: uncovered form); CR-4b (x: comply, y: violate); arithmetic | A-3 |
| C-11 | employers.formal | reclassification (pay into meal vouchers and health premiums) | increase | short | invisible | B | CR-4b (x: covered form, y: uncovered form) | A-N1 |
| C-12 | workers.informal | informal_activity | increase | medium | invisible | B | CR-1 (enforcement premise); CR-4b (x: comply, y: violate) | A-4 |
| C-13 | sellers.substitutes | quantity_substitute (labor-saving equipment, outsourcing) | increase | medium | invisible | B | CR-4b (x: labor, y: equipment); CR-9 (substitute) | A-5 |
| C-14 | lobby.employers_unions | lobbying_effort | increase | short | visible | B | CR-4b (x: accept, y: lobby) | A-7 |
| C-15 | pension_fund | tax_revenue_vs_static_projection | decrease | short | invisible | B | CR-10a; CR-4b (x: pay bonus from July, y: in June) | A-6 |
| C-16 | pension_fund | tax_revenue_vs_static_projection | decrease | medium | invisible | B | CR-4b, CR-4c (base shrinks) | A-2 |
| C-17 | workers.below_ceiling | tax_share_borne | increase | long | invisible | B | CR-7b; arithmetic (fixed ceiling) | A-8 |
| C-18 | buyers.labor_intensive_services | price_paid | increase | medium | visible | B | CR-9 (input_to); CR-7a | A-10, A-14 |
| C-19 | buyers.labor_intensive_services | quantity_demanded | decrease | medium | invisible | B | CR-9 (input_to); CR-4c | A-10, A-14 |
| C-20 | employers.labor_intensive_services | employment | decrease | medium | invisible | B | CR-9 (input_to; LW-10) | A-10, A-14 |
| C-21 | workers.informal | disputes_settled_outside_courts | increase | medium | invisible | B | CR-9 (same_market_other_segment); CR-11b | A-4 |
| C-22 | government.general_budget | resources_available_other_uses | increase | medium | invisible | B | CR-8d | A-11 |
| C-23 | workers.formal | earnings | decrease | long | invisible | B | Arithmetic (wage times hours times employment) on C-5 and C-8; CR-12a | A-2, A-8, A-12 |
| C-24 | employers.formal | resources_available_other_uses | decrease | short | invisible | B | CR-8a, CR-8b; CR-3a | A-1 |
| C-25 | workers.formal | resources_available_other_uses | decrease | long | invisible | B | CR-8a, CR-8b; CR-3a; CR-7b | A-8, A-12 |
| C-26 | employers.formal | compliance_cost | increase | medium | invisible | B | CR-8c | A-3 |

## Gaps found

**(a) Calculus gaps.** None. Every step was derived from CR-1 to CR-12, the foundations and arithmetic. The interaction of the tax with the existing minimum wage was handled by CR-6 (a floor keeps the price from moving, so pressure moves to other terms).

**(b) New premises.**
- A-N1 (p 0.7): C-11. CR-4b gives the direction of a move from taxed wages into exempt vouchers and premiums, but whether anyone is at that margin depends on how workers value vouchers and premiums compared with cash and on how much room is left under the 150-crown cap. None of the case assumptions covers this exemption.

**(c) Unclear core rules.**
- CR-5c: it says a change in what one party must give "moves that range" within which terms lie, but not whether the agreed terms must move. A wage previously agreed may still lie inside the new range. C-7 needed CR-7b and A-8 in addition to say the agreed wage falls at renewal.
- CR-7b: as in other cases, "settles on the side without alternatives" does not say whether it licenses "all" or "more". A-8 compares employers' and workers' alternatives, and was read as licensing "workers bear the lasting burden, mostly".
- CR-4 exception: lower wages (C-8) change workers' total means, which could raise or lower the hours they wish to work. The exception would make workers' labor supply ambiguous, but the consequence list does not sign workers' desired hours, so it was not applied; it is unclear whether the exception should also be applied to C-5 (employment), which rests partly on workers' choices.
- CR-6 is stated for "a rule [that] prevents the price from moving". Here the existing minimum wage, not the policy, holds the price; CR-6 was applied on the reading that the rule may be an existing rule that the policy makes bind.
- CR-12b refers to "a dominance pattern" for a dominance claim; in a core-only run the dominance premise for C-8 was stated directly from CR-7b and A-8.

## Comparison with the pattern-based analysis

**Summary.** The two versions agree on incidence, which is the lesson of this case. Employers bear the tax while money wages are fixed (A-1). Over the medium and long run it moves to workers through slower wage growth, because employers have better alternatives (A-8). Workers below the ceiling bear more than high earners. At the minimum wage the tax cannot pass to the wage and lands on jobs, hours or non-wage terms (a group consequence in both). The pattern version reaches this with DM-1 and its time note; the core version reaches it with CR-7b and CR-5c. The two derivations give the same signs, so DM-1's time note is consistent with the core rules here. Both versions also agree on avoidance (contracting out, undeclared work), on equipment substitution, on dearer labor-intensive services and on revenue falling short of a static projection. The one sign difference is hours. The pattern version records `hours_worked` decrease for all formal workers. The core version shows that for workers above the ceiling an extra hour bears no added contribution while each extra head costs more, so their hours are `ambiguous`. The pattern version overgeneralized, and the core version in turn omitted the plain decrease for workers below the ceiling. Most other differences are omissions in the core version: non-price selection under the floor, informal workers' search costs, the income-tax base, the bonus-timing shift (again kept as a path note), and the two ambiguous rows. One pattern was misapplied: the pattern version charges taxpayers for added enforcement (OC-3), although the case assumes the Inspectorate's budget does not rise.

**Counts.** M 13, V 8, S 1, OP 3, OC 7. Causes over S, OP and OC (11 items): P 1, K 0, A 0, E 10, J 0.

**Pattern version → core version**

| Pattern ID | Matched core ID(s) | Class | Cause | Note |
|---|---|---|---|---|
| C-1 | C-1 | V | | The core version signs the labor-cost rise only in the short run. The pattern version carries it to the long run, "shrinking". On A-8 ("mostly" on workers) the long-run labor cost stays above the counterfactual, so the pattern version's horizon is defensible. The core version is silent beyond the short run, not opposed. |
| C-2 | C-2 | V | | Actor class `officials.enforcement` vs `pension_fund`. |
| C-3 | C-4 | M | | |
| C-4 | C-9 | S | E (pattern) | Pattern: `hours_worked` decrease for all `workers.formal`. Core: `workers.above_ceiling` hours ambiguous. **Core right for workers above the ceiling**: the added contribution is a fixed 240 crowns per head, and extra pay above the ceiling bears none, so CR-4b moves work from new heads to longer hours for high earners, against CR-4c's output effect (CR-12b). The pattern version's own note under C-14 states the fact it needed. The core version, however, omits the decrease for workers below the ceiling, which CR-4c derives directly (an E in the core version too). The correct pair is: below the ceiling, decrease; above it, ambiguous. |
| C-5 | C-10 | M | | |
| C-6 | (section 8 note), C-15 | OC | E (core) | Bonuses moved into June. As in WE-011, the core version keeps the shift as a path note on the ground that "without the policy there would be no reason to move them". Bonuses are paid in the counterfactual too, so 2.5 requires per-window signed consequences. |
| C-7 | C-12 | M | | |
| C-8 | C-13 | V | | Recorded on `sellers.substitutes`, not on employers. |
| C-9 | C-26 | V | | Payroll system changes (short, Tier A) vs restructuring costs (medium). |
| C-10 | C-14 | M | | |
| C-11 | C-7, C-8 | M | | |
| C-12 | C-1, C-3 | V | | The core version records the short-run employer burden as `return_on_capital` decrease and in the C-1 derivation, not as `tax_share_borne`. |
| C-13 | C-8, C-25 | V | | Long-run burden on workers, recorded as a wage fall and lost resources. |
| C-14 | C-17 | M | | Horizon medium–long vs long. |
| C-15 | C-6 | M | | Same group consequence, with the floor handled by CR-6 in the core version. |
| C-16 | none | OC | E (core) | More selection by credentials under the floor. CR-6's second margin ("the criteria by which the scarce side chooses") derives it from the same widened floor as C-6. |
| C-17 | C-23 | M | | |
| C-18 | none | OC | E (core) | Informal jobs cannot be advertised. CR-11b derives it; the core version applied CR-11b only to disputes (C-21). |
| C-27 | C-21 | M | | |
| C-19 | C-13 | V | | Merged with C-8. |
| C-20 | C-18 | M | | |
| C-21 | none | OC | E (core) | Income-tax revenue on wages falls. Arithmetic on the core version's own C-7, C-8 and C-5 (the tax is a share of wages) with CR-8b. Note that the pattern version narrows the variable to "income tax on wages", which sidesteps the shift of income to other taxed bases that TX-10 would otherwise make `ambiguous`. |
| C-22 | C-15, C-16 | M | | TX-9's Unless clause does not apply: the tax lowers, not raises, the gross wage. |
| C-23 | C-24, C-25 | M | | |
| C-24 | C-4, C-6 (section 9) | V | | Prevented jobs, recorded as `employment` with CR-5a rather than `quantity_traded`. |
| C-25 | none | OC | P | Taxpayers fund added enforcement (OC-3). The case assumes the Inspectorate's budget does not rise, so no added funding is drawn from taxpayers. The cost of more avoidance shows instead as a lower chance of inspection per case, which the core version notes (section 6, interaction of components). OC-3 is misapplied here. |
| C-26 | C-5, C-20 | M | | |
| — (`workers.formal` non_wage_compensation, ambiguous) | (C-11 is one chain only) | OC | E (core) | The core version derives the + chain (C-11, pay moved into exempt vouchers and premiums) and the wage chain, but does not compose them on this variable. |
| — (contractors earnings, ambiguous) | none | OC | E (core) | A one-time setup cost against a later stream of saved contributions. CR-12b (no magnitudes) gives `ambiguous`; the core version did not record contractors' earnings. A minor omission. |

**Core-only consequences**

| Core ID | Class | Cause | Note |
|---|---|---|---|
| C-11 | OP | E (pattern) | Pay moved into exempt meal vouchers and health premiums (`reclassification` increase). The pattern version uses this only as a chain inside its ambiguous non-wage row and never lists the signed response. The core version needed A-N1 for it. |
| C-19 | OP | E (pattern) | Buyers of labor-intensive services buy less. RS-14 itself names the quantity side; the pattern version records only the price. |
| C-22 | OP | E (pattern) | The general budget's freed money (CR-8d). The pattern version derives it in prose (SB-7, A-11) but lists no consequence. |

**Findings**
- Incidence: DM-1, including its time note for factor markets, and CR-7b with CR-5c give identical signs in the short run (employers), in the long run (workers) and at the minimum wage (jobs, hours, terms). No disagreement.
- Pattern misapplied: OC-3 (C-25) charges taxpayers for added enforcement when the record assumes a fixed enforcement budget. OC-3 as written has no clause for a fixed budget, where the cost falls as less enforcement elsewhere rather than as more spending. This is worth an Unless clause in the catalog.
- Error in the pattern version: C-4 extends an hours cut to workers above the ceiling, for whom the marginal hour bears no added contribution. It also omits the signed shift into exempt benefits, buyers' lower quantity and the freed general-budget money.
- Errors in the core version: it omits the hours decrease below the ceiling, non-price selection under the floor (CR-6), informal workers' search cost (CR-11b), the wage income-tax base, and the two ambiguous rows. It keeps the bonus shift as a path note through a misreading of 2.5 (the same error as in WE-011).
- Limits of the core rules: none that changed a sign. The core version's notes on CR-6 (an existing floor that the policy makes bind) and CR-5c (a moved range does not by itself move the agreed term) are fair requests to clarify the wording.
