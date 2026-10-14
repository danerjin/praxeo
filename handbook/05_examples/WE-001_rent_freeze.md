# WE-001 Rent freeze with a new-construction exemption

Analyst: draft (Handbook 0.1)  |  Rule catalog version: 0.1  |  Status: awaiting expert review

A stylized policy in a fictional city. It is close to real rent-control ordinances but deliberately differs from the historical cases reserved for evaluation. The probabilities are illustrative; the evidence column says what a real analysis would cite.

## 1. Policy record

**Riverton Rent Stabilization Ordinance.** Riverton is a mid-sized city. Its neighbors, Eastfield and Northgate, are 15 to 25 minutes away by car or train and have no rent regulation. Market rents in Riverton have risen about 5% a year for several years.

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Rent freeze and cap | `price_ceiling` | Rent on residential rental units existing on the effective date | Landlords of those units | Rent frozen at its level on the effective date for 3 years; increases capped at 2% a year after that. The cap applies to the unit, including when a new tenant moves in. | Units first occupied after the effective date. |
| K2 Tenancy rules | Restriction on contract terms (part of K1) | Leases of covered units | Landlords and tenants | Eviction only for cause. Tenancies cannot be assigned or sold. | None |
| K3 Withdrawal route | Permit regime | Conversion of covered buildings to owner-occupied condominiums | Landlords | Permitted after a 12-month permit process; sitting tenants must be given notice and relocation payments. | None |
| K4 Rent board | Administration and enforcement | All of the above | City | Complaint-driven enforcement; fines for overcharging; funded from the city's general budget. | None |

Unclear provisions: whether major renovations allow a rent increase. Assumed not.

## 2. Classification

| Component | Rothbard type | Binding? | Rule families |
|---|---|---|---|
| K1 | Triangular: fixes the terms of exchange between landlords and tenants | Not at the moment of enactment (the cap equals the current rent), but becomes binding as market rents rise (TS-3). A-1. | PC, RS, TS |
| K2 | Triangular | Yes, by its text | PC-7 |
| K3 | Triangular: limits the exit route | Partly; it delays rather than prevents exit | RS-5, PC-5 |
| K4 | Binary: funded by taxpayers | Yes | OC-3 |

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `tenants.controlled` | Sitting tenants of covered units | Rent held below the market level; cannot assign the tenancy; lose the benefit if they move. |
| `tenants.prospective` | People looking for a rental in Riverton, including newcomers and young residents leaving home | Fewer covered units come up for rent; uncontrolled units cost more. |
| `landlords.controlled` | Owners of covered units | Rental return capped; can cut maintenance, convert, or evade. |
| `developers` (`sellers.prospective`) | Builders of new rental housing | New units exempt; but must judge whether the exemption will last. |
| `landlords.uncontrolled` | Owners of new, exempt units | Face more demand. |
| `homebuyers` | Buyers of owner-occupied housing | More condos come on the market through conversion. |
| `renters.neighbors` | Renters in Eastfield and Northgate | Some Riverton seekers move to their market. |
| `officials.enforcement`, `taxpayers` | Rent board and its funders | New administrative task. |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | `tenants.controlled` | `price_paid` | decrease | short to long, growing over time | PC-3, TS-3 | A-1, A-2 |

The visible effect: sitting tenants pay less than they would have, and the gap widens each year that market rents rise faster than 2%.

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-2 | `tenants.prospective` (covered units) | `excess_demand` | increase | short | PC-1 | A-1, A-2 |
| C-3 | `tenants.prospective` | `wait_time`, `search_cost` | increase | short | PC-2 | A-1, A-2 |
| C-4 | `tenants.prospective` | `allocation_by_non_price_criteria` (landlords choose by income, credit, connections, perceived reliability) | increase | short | PC-2 | A-1, A-2 |
| C-5 | `tenants.controlled` | `turnover` | decrease | medium | PC-7 | A-1, A-6 |
| C-6 | `landlords.controlled` | `maintenance_spending`, `quality_per_unit` | decrease | short to medium | PC-4, RS-2 | A-1, A-4 |
| C-7 | `landlords.controlled` / `tenants.prospective` | `side_payments`, `informal_activity` (key money, sublets at market rent) | increase | short | PC-6, RS-3 | A-1, A-3 |
| C-8 | `landlords.controlled` | `reclassification` (conversion to condominiums) | increase | medium (after the 12-month permit process) | RS-5, PC-5 | A-1, A-5 |
| C-9 | `landlords.controlled` | `quantity_supplied` of covered rental units | decrease | medium to long | PC-5, RS-6, TS-1 | A-1, A-5, A-10 |
| C-10 | `tenants.controlled` (in converted buildings) | lose their controlled tenancy: `price_paid` increase for this subgroup after relocation | increase | medium | PC-5, RS-5 | A-5 |
| C-11 | `tenants.controlled`, `landlords.controlled`, `developers` | `lobbying_effort` | increase | medium | RS-7 | A-1 |

C-10 is worth stating separately: the ordinance protects sitting tenants as a group, but it gives landlords a reason to remove buildings from the rental market, and the tenants in those buildings end up worse off than they would have been without it.

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-12 | `tenants.prospective` in uncontrolled units | `price_substitute` (rent of exempt new units) | increase | short to medium | PC-8 | covered and exempt units: `same_market_other_segment`, close | A-1, A-7 |
| C-13 | `developers` | `investment_target` (new rental construction) | see section 7 | medium | LW-4, TS-2 | | A-7, A-9 |
| C-14 | `homebuyers` | `quantity_substitute` (condos for sale) | increase | medium | RS-5 | rental and owner-occupied housing: `substitute`, partial | A-5 |
| C-15 | `renters.neighbors` | `price_paid` in Eastfield and Northgate | increase | medium | RS-4, PC-3 | Riverton and neighbors: `across_border`, partial | A-8 |

C-15 is at depth 3 and reaches a diffuse group of bystanders, so the chain stops there (workflow step 6).

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `developers`, `investment_target` (new rental construction), medium | Exempt units command higher rents (C-12), so building them pays better (LW-4). Rests on A-7 and A-9 (developers expect the exemption to last, p = 0.6). | Developers fear the exemption will be withdrawn once the new units exist, so expected returns fall (TS-2). Rests on the negation of A-9 (p = 0.4). | None | **increase**. The − chain rests on an assumption below the 0.5 cut-off, so it is listed as a conditional possibility, not reported. If evidence moved A-9 below 0.5, the sign would flip. |
| `tenants.controlled`, `quality_adjusted_price`, medium | Quality falls (C-6), so they get less for each unit of rent. | Rent is lower (C-1). | None | **ambiguous**. The method cannot say whether lower rent outweighs lower quality for sitting tenants as a group. |
| `tenants.prospective`, total cost of housing (`price_paid` across all segments), short to medium | Higher rent in the exempt segment (C-12) and in neighboring cities (C-15); more search, waiting and side payments (C-3, C-7). | A few obtain covered units at the controlled rent. | None needed | **increase**. Every chain that applies to the group as a whole pushes costs up; the few who find a covered unit become insiders (`tenants.controlled`). |

## 8. Time structure

- The freeze is not binding at first and tightens every year (TS-3). Most effects therefore start small and grow.
- Buildings last decades (A-10). Less maintenance shows up within a year or two (C-6); reduced supply through conversion follows the 12-month permit process (C-8); reduced investment in the existing stock compounds over the long run (C-9, TS-1).
- Announcement effect: landlords who expected the ordinance may raise rents just before the effective date, to lock in a higher base (RS-8). This is not reported, because the record has no evidence on how long the ordinance was announced in advance (`GAP-1` in `06_gaps.md`).

## 9. Opportunity costs

| ID | Actor class | What is given up | Rules |
|---|---|---|---|
| C-16 | `tenants.prospective`, `landlords.controlled` | Rentals that would have been agreed at market rent and now do not happen, because units are converted or kept off the market. Both sides lose the gain they expected. | OC-4 |
| C-17 | `tenants.prospective` | Time spent searching and waiting (C-3). | OC-2 |
| C-18 | `tenants.controlled` | Moves not made (C-5): a home closer to a new job, a smaller unit after children leave. The forgone better match is a cost to the tenant, invisible in any price. | OC-4, PC-7 |
| C-19 | `taxpayers` | What the rent board's budget would otherwise have funded. | OC-3, OC-1 |

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | Market rents keep rising above 2% a year, so the cap binds within the first year. | binding | 0.9 | Five-year rent trend; vacancy rate; pipeline of new supply. | Almost every consequence weakens or disappears until the cap binds. |
| A-2 | The rent board enforces the cap against most landlords. | enforcement | 0.8 | Board's budget and staffing; complaint-driven model; size of fines relative to the rent gap. | C-1 shrinks; C-7 grows. |
| A-3 | Some landlords and tenants evade (key money, illegal sublets) without being caught. | enforcement | 0.8 | Complaint-driven enforcement; tenancies cannot be assigned, which creates an incentive for illegal sublets. | C-7 not reported. |
| A-4 | Housing codes leave landlords room to reduce maintenance above the legal minimum. | other | 0.85 | Content of the city's habitability code and inspection frequency. | C-6 not reported. |
| A-5 | The conversion route is usable for a meaningful number of buildings. | alternative_uses | 0.7 | Permit approval rates; relocation payment size; demand for condominiums. | C-8, C-9 (via conversion), C-10 and C-14 weaken; supply falls only through wear (TS-1). |
| A-6 | Sitting tenants cannot transfer their tenancy. | other | 0.95 | Ordinance text (K2). | C-5 weakens if tenancies can be passed on informally. |
| A-7 | Covered and exempt units are close substitutes. | substitutability | 0.85 | Similar locations and sizes; same tenant pool. | C-12 weakens. |
| A-8 | Commuting from neighboring cities is practical for many seekers. | mobility | 0.7 | Travel times of 15 to 25 minutes; transit links. | C-15 not reported. |
| A-9 | Developers expect the new-construction exemption to last. | expectations | 0.6 | Political history of exemptions in the region; whether the exemption is in the city charter or an ordinance. | The sign of C-13 flips to decrease. |
| A-10 | Rental buildings last several decades, so supply adjusts slowly. | durability | 0.95 | Age of the housing stock. | Supply responses come sooner. |

## 11. Report

**The policy.** Rents on all existing Riverton rental units are frozen for three years and may then rise by at most 2% a year, whoever the tenant. New buildings are exempt. Owners may convert buildings to condominiums after a year-long permit process.

**Visible consequences.** Sitting tenants pay less rent than they would have, and the gap grows every year that market rents rise faster than the cap (C-1).

**Invisible consequences.**
- *People looking for a home in Riverton* find fewer covered units available, wait and search longer, face landlords who choose tenants by income, credit and connections, and sometimes pay key money or illegal sublet premiums (C-2 to C-4, C-7). Many end up in exempt new buildings, where rents rise because of the extra demand (C-12), or in neighboring cities, where they push rents up (C-15).
- *Sitting tenants* receive less maintenance (C-6) and move less often, even when a different home would suit them better (C-5, C-18). Tenants in buildings that are converted lose their controlled tenancy altogether (C-10).
- *Landlords* earn less on covered units, convert some buildings to condominiums (C-8) and invest less in the rest; over many years the covered rental stock is smaller than it would have been (C-9).
- *Homebuyers* see more condominiums for sale than they otherwise would (C-14).
- *Taxpayers* fund the rent board (C-19).

**Ambiguous effects.** Whether sitting tenants are better off overall, taking lower rent and lower quality together, cannot be determined by this method.

**Key conditions.** The most important assumption is that market rents keep rising above 2% (A-1, p = 0.9); if they do not, the ordinance changes little. The direction of new construction depends on whether developers trust the exemption (A-9, p = 0.6): if they come to expect it to be removed, new construction falls instead of rising.

**What this analysis cannot say.** How large any of these effects will be; whether gains to sitting tenants outweigh losses to others; whether the policy is desirable.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | tenants.controlled | price_paid | decrease | short–long | visible | B | PC-1, PC-3, TS-3 | A-1, A-2 |
| C-2 | tenants.prospective | excess_demand | increase | short | invisible | B | PC-1 | A-1, A-2 |
| C-3 | tenants.prospective | wait_time, search_cost | increase | short | invisible | B | PC-1, PC-2 | A-1, A-2 |
| C-4 | tenants.prospective | allocation_by_non_price_criteria | increase | short | invisible | B | PC-1, PC-2 | A-1, A-2 |
| C-5 | tenants.controlled | turnover | decrease | medium | invisible | B | PC-7 | A-1, A-6 |
| C-6 | tenants.controlled | quality_per_unit | decrease | short–medium | invisible | B | PC-4, RS-2 | A-1, A-4 |
| C-7 | tenants.prospective | side_payments | increase | short | invisible | B | PC-6, RS-3 | A-1, A-3 |
| C-8 | landlords.controlled | reclassification | increase | medium | invisible | B | RS-5, PC-5 | A-1, A-5 |
| C-9 | landlords.controlled | quantity_supplied | decrease | medium–long | invisible | B | PC-5, RS-6, TS-1 | A-1, A-5, A-10 |
| C-10 | tenants.controlled (converted buildings) | price_paid | increase | medium | invisible | B | PC-5, RS-5 | A-1, A-5 |
| C-11 | landlords, tenants, developers | lobbying_effort | increase | medium | invisible | B | RS-7 | A-1 |
| C-12 | tenants.prospective | price_substitute (exempt units) | increase | short–medium | invisible | B | PC-3, PC-8 | A-1, A-7 |
| C-13 | developers | investment_target (new rental) | increase | medium | invisible | B | PC-8, LW-4 | A-7, A-9 |
| C-14 | homebuyers | quantity_substitute (condos) | increase | medium | invisible | B | RS-5 | A-1, A-5 |
| C-15 | renters.neighbors | price_paid | increase | medium | invisible | B | PC-3, RS-4 | A-1, A-8 |
| C-16 | tenants.prospective, landlords | prevented rentals | (loss) | medium | invisible | B | OC-4 | A-1, A-5 |
| C-17 | tenants.prospective | search time | (loss) | short | invisible | B | OC-2 | A-1 |
| C-18 | tenants.controlled | forgone moves | (loss) | medium | invisible | B | OC-4, PC-7 | A-1, A-6 |
| C-19 | taxpayers | resources_available_other_uses | decrease | short | invisible | A | OC-3, OC-1 | none |
| — | tenants.controlled | quality_adjusted_price | ambiguous | medium | invisible | B | C-1 vs C-6 | A-1, A-4 |

## Gaps found

- GAP-1: announcement effects before the effective date (RS-8 applies, but the policy record has no field for the announcement date).
- GAP-2: no rule links reduced housing turnover to job matching in the labor market (C-18 stops at the forgone move).
- GAP-3: OC entries are losses, not variables with a sign; the normal form needs a convention for them (see `06_gaps.md`).
