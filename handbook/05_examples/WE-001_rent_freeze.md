# WE-001 Rent freeze with a new-construction exemption

Analyst: draft (Handbook 0.5)  |  Rule catalog version: 0.5  |  Status: awaiting expert review

A stylized policy in a fictional city. It is close to real rent-control ordinances but deliberately differs from the historical cases reserved for evaluation. The probabilities are illustrative; the evidence column says what a real analysis would cite.

## 1. Policy record

**Riverton Rent Stabilization Ordinance.** Riverton is a mid-sized city. Its neighbors, Eastfield and Northgate, are 15 to 25 minutes away by car or train and have no rent regulation. Market rents in Riverton have risen about 5% a year for several years. The ordinance was put on the ballot eight months before it took effect, and polls showed it was likely to pass.

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
| K4 | Binary: funded from the general budget, which rises with the new task (A-19), so taxpayers bear it (OC-3, first funding case) | Yes | OC-3 |

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
| C-1 | `tenants.controlled` | `price_paid` | decrease | medium to long, growing over time | PC-3, TS-3; dominance over C-17 by A-14 (CR-12b, CR-12e) | A-1, A-2, A-14 |
| C-21 | `tenants.controlled` | `price_paid` (covered units, first months after the effective date) | ambiguous | short | PC-3 (−) against RS-8 (+, C-17 lifts the frozen base); CR-12b | A-1, A-2, A-11 |
| C-27 | `landlords.controlled` | `net_price_received` (covered units) | decrease | medium to long | PC-3 (the mirror of C-1: the rent sitting tenants no longer pay is rent landlords no longer receive), CR-3a; dominance over C-17 by A-14 | A-1, A-2, A-14 |

The visible effect: sitting tenants pay less than they would have, and the gap widens each year that market rents rise faster than 2% (C-1). In the first months the sign is not determined: landlords whose leases renewed in the announcement window raised rents to lift the frozen base (C-17), and until the counterfactual market path passes that raised base the two chains conflict (C-21). A pre-emptive raise cannot exceed the market rent on the effective date (CR-5c), and the counterfactual rent passes that level within a lease cycle or two (A-14), so from the medium horizon the cap chain dominates. Landlords receive less by the same amount (C-27).

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-2 | `tenants.prospective` (covered units) | `excess_demand` | increase | short | PC-1 | A-1, A-2 |
| C-3 | `tenants.prospective` | `search_cost` | increase | short | PC-2 (search margin open and used: A-15) | A-1, A-2, A-15 |
| C-4 | `tenants.prospective` | `allocation_by_non_price_criteria` (landlords choose by income, credit, connections, perceived reliability) | increase | short | PC-2 (selection margin open and used: A-16; K2's eviction-for-cause rule makes screening worth more) | A-1, A-2, A-16 |
| C-5 | `tenants.controlled` | `turnover` | decrease | medium | PC-7 | A-1, A-6 |
| C-6 | `landlords.controlled` | `maintenance_spending`, `quality_per_unit` | decrease | short to medium | PC-4, RS-2 | A-1, A-4 |
| C-7 | `tenants.prospective` | `side_payments` (key money) | increase | short | PC-2, PC-6, RS-3 (side-payment margin open and used: A-3) | A-1, A-3 |
| C-22 | `tenants.controlled` | `informal_activity` (illegal sublets at market rent) | increase | medium | PC-6, RS-3 (x: comply with K2's no-assignment rule, y: sublet) | A-1, A-3, A-6 |
| C-24 | `landlords.controlled` | `units_held_vacant` | increase | medium | PC-5, RS-5: a vacated unit re-let to a new tenant would need eviction for cause or a relocation payment before conversion (K2, K3), so CR-4 (x: re-let, y: hold vacant pending conversion or sale) | A-1, A-2, A-5 |
| C-25 | `landlords.controlled` | `compliance_cost` (permit process, board proceedings) | increase | medium | OC-2, CR-8c | A-5 |
| C-8 | `landlords.controlled` | `reclassification` (conversion to condominiums) | increase | medium (after the 12-month permit process) | RS-5, PC-5 | A-1, A-5 |
| C-9 | `landlords.controlled` | `quantity_supplied` of covered rental units | decrease | medium to long | PC-5, RS-6, TS-1 | A-1, A-5, A-10 |
| C-10 | `tenants.controlled` (in converted buildings) | `turnover` (they must leave when the building is converted) | increase | medium | PC-5, RS-5, then CR-9 (the landlord's exit ends the lease) | A-1, A-2, A-5 |
| C-11 | `tenants.controlled`, `landlords.controlled`, `developers` | `lobbying_effort` (tenants to keep the ordinance, landlords to loosen it, developers to keep the exemption) | increase | medium | RS-7 | A-1, A-18 |
| C-17 | `tenants.controlled` whose leases renew before the effective date | `price_paid` (in the announcement window) | increase | short | RS-8 | A-11 |

C-10 is worth stating separately: the ordinance protects sitting tenants as a group, but it gives landlords a reason to remove buildings from the rental market, and the tenants in those buildings must move. (Catalog 0.3 recorded this as "`price_paid` increase after relocation". That compared their new market rent with the controlled rent, not with the counterfactual: without the ordinance they would also pay a market rent. No sign for their rent follows; the move itself, and the relocation payment they receive (C-30), do.)

C-3, C-4 and C-7 sign three members of PC-2's group separately; each has its own premise that the margin is open and used (A-15, A-16, A-3). There is no waiting list or allocation rule in the record, so `wait_time` is not signed.

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-12 | `tenants.prospective` in uncontrolled units | `price_substitute` (rent of exempt new units) | increase | short to medium | PC-8, through units withdrawn from the covered stock (C-9, C-24) and sitting tenants' larger consumption at the lower rent (CR-4c mirror: fewer moves to smaller units, fewer roommates, A-17) | covered and exempt units: `same_market_other_segment`, close | A-1, A-7, A-17 |
| C-13 | `developers` | `investment_target` (new rental construction) | see section 7 | medium | LW-4, TS-2 | | A-7, A-9 |
| C-14 | `homebuyers` | `quantity_substitute` (condos for sale) | increase | medium | RS-5 | rental and owner-occupied housing: `substitute`, partial | A-5 |
| C-15 | `renters.neighbors` | `price_paid` in Eastfield and Northgate | increase | medium | RS-4, PC-3 | Riverton and neighbors: `across_border`, partial | A-8 |
| C-20 | `landlords.controlled` | `asset_value` of covered buildings | decrease | short (from the ballot announcement) | SB-4 | sale of buildings | A-1, A-13 |
| C-23 | `tenants.prospective` (subtenants in illegal sublets) | `disputes_settled_outside_courts` | increase | medium | PC-6 → RS-10 (an illegal sublet has no recourse to the courts) | the sublet (tenant to subtenant) | A-1, A-3, A-6 |

PC-8's Unless clause (0.5) does not apply. It applies when the policy itself pushes sellers into the uncontrolled segment. Here covered units stay covered whoever lets them, and converted units leave rental use altogether (C-8, C-14), so no covered landlord can move a unit into the exempt segment. New exempt building is a response to the higher exempt rent (C-13), not an independent addition: an induced supply response moderates C-12 but cannot reverse its sign. Rationing alone changes who occupies the covered stock, not how many households it houses, so the sign rests on the withdrawn units and the insiders' larger consumption, which push the same way (CR-12a).

C-20: a lasting cap on the income from a building lowers what buyers will pay for it, from the moment the cap is expected. Owners at the time of the ballot bear the loss; anyone who buys a covered building later pays the lower price, so the ordinance does not lower their return further.

C-15 is at depth 3 and reaches a diffuse group of bystanders, so the chain stops there (workflow step 6). The price of condominiums is not signed: converted units add to their supply, while some rationed-out seekers buy instead of renting (CR-12b).

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `developers`, `investment_target` (new rental construction), medium | Exempt units command higher rents (C-12), so building them pays better (LW-4). Rests on A-7 and A-9 (developers expect the exemption to last, p = 0.6). | Developers fear the exemption will be withdrawn once the new units exist, so expected returns fall (TS-2). Rests on the negation of A-9 (p = 0.4). | None | **increase**. The − chain rests on an assumption below the 0.5 cut-off, so it is listed as a conditional possibility, not reported. If evidence moved A-9 below 0.5, the sign would flip. |
| `tenants.controlled`, `quality_adjusted_price`, medium | Quality falls (C-6), so they get less for each unit of rent. | Rent is lower (C-1). | None | **ambiguous**. The method cannot say whether lower rent outweighs lower quality for sitting tenants as a group. |
| `tenants.controlled`, `price_paid`, short | Pre-emptive raises in the announcement window lift the frozen base (C-17, RS-8). | Rent capped below a rising market (PC-3). | None at this horizon: the size of the raises against the counterfactual path is a magnitude. | **ambiguous** (C-21). |
| `tenants.controlled`, `price_paid`, medium to long | As above. | As above. | A-14 with CR-5c: a pre-emptive raise is bounded by the market rent on the effective date, which the counterfactual path passes within a lease cycle or two (CR-12e, empirical premise). | **decrease** (C-1); likewise `landlords.controlled`, `net_price_received` (C-27). |
| `landlords.controlled`, `resources_available_other_uses`, medium | Key money received by landlords who evade (C-7). | Rent forgone on every covered unit (C-27); relocation payments and permit costs (C-25, C-30). | A-2: the cap is enforced against most landlords, so key money is confined to a minority and to new lettings, while the cap lowers the rent on every covered unit each month (CR-12e, empirical premise). | **decrease** (C-28). |

Catalog 0.3 also recorded a combined "total cost of housing" for seekers across segments. That netted different variables (rents in two segments, search cost, side payments) into one, which CR-12c forbids; each is recorded separately (C-3, C-7, C-12, C-15).

## 8. Time structure

- The freeze is not binding at first and tightens every year (TS-3). Most effects therefore start small and grow.
- Buildings last decades (A-10). Less maintenance shows up within a year or two (C-6); reduced supply through conversion follows the 12-month permit process (C-8); reduced investment in the existing stock compounds over the long run (C-9, TS-1).
- Announcement effect: the ordinance was expected eight months before it took effect. Landlords whose leases come up for renewal in that window raise rents to lock in a higher base before the freeze (C-17, RS-8). This is a timing shift, signed per window: rents in the announcement window increase (C-17); in the first months after the effective date the sign is ambiguous (C-21); from the medium horizon, a decrease (C-1). Building values fall from the ballot campaign, not from the effective date (C-20).

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-16 | `tenants.prospective`, `landlords.controlled` | `quantity_traded` (rentals of covered units) | decrease | Rentals that would have been agreed at market rent and now do not happen, because units are converted or kept off the market. Both sides lose the gain they expected. | OC-4 |
| C-18 | `tenants.controlled` | `job_changes` | decrease | Moves not made because moving means losing the controlled rent: a job in another part of the region, a smaller unit after children leave. | RS-11, PC-7 |
| C-19 | `taxpayers` | `resources_available_other_uses` | decrease | What the rent board's budget would otherwise have funded (OC-3, first funding case: the general budget rises with the new task, A-19). | OC-3, OC-1 |
| C-26 | `officials.enforcement` | `enforcement_cost` | increase | Staff time and budget of the rent board, used up (CR-8c). | OC-3 |
| C-28 | `landlords.controlled` | `resources_available_other_uses` | decrease | Rent forgone on covered units (it stays with sitting tenants, C-29), relocation payments and permit costs. See section 7. | CR-8b, CR-8c |
| C-29 | `tenants.controlled` | `resources_available_other_uses` | increase | The matching side of C-28: rent they keep (CR-8b). | CR-8b |
| C-30 | `tenants.controlled` (in converted buildings) | `resources_available_other_uses` | increase | The relocation payment landlords must make under K3 (CR-8b), received when the building is converted. | CR-8b |

Time spent searching and waiting is already recorded as C-3, so it is not listed again here.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | Market rents keep rising above 2% a year, so the cap binds within the first year. | binding | 0.9 | Five-year rent trend; vacancy rate; pipeline of new supply. | Almost every consequence weakens or disappears until the cap binds. |
| A-2 | The rent board enforces the cap against most landlords. | enforcement | 0.8 | Board's budget and staffing; complaint-driven model; size of fines relative to the rent gap. | C-1 shrinks; C-7 grows. |
| A-3 | Some landlords and tenants evade (key money, illegal sublets) without being caught. | enforcement | 0.8 | Complaint-driven enforcement; tenancies cannot be assigned, which creates an incentive for illegal sublets. | C-7, C-22 and C-23 not reported. |
| A-4 | Housing codes leave landlords room to reduce maintenance above the legal minimum. | other | 0.85 | Content of the city's habitability code and inspection frequency. | C-6 not reported. |
| A-5 | The conversion route is usable for a meaningful number of buildings. | alternative_uses | 0.7 | Permit approval rates; relocation payment size; demand for condominiums. | C-8, C-9 (via conversion), C-10, C-14, C-24, C-25 and C-30 weaken; supply falls only through wear (TS-1). |
| A-6 | Sitting tenants cannot transfer their tenancy. | other | 0.95 | Ordinance text (K2). | C-5 weakens if tenancies can be passed on informally. |
| A-7 | Covered and exempt units are close substitutes. | substitutability | 0.85 | Similar locations and sizes; same tenant pool. | C-12 weakens. |
| A-8 | Commuting from neighboring cities is practical for many seekers. | mobility | 0.7 | Travel times of 15 to 25 minutes; transit links. | C-15 not reported. |
| A-9 | Developers expect the new-construction exemption to last. | expectations | 0.6 | Political history of exemptions in the region; whether the exemption is in the city charter or an ordinance. | The sign of C-13 flips to decrease. |
| A-10 | Rental buildings last several decades, so supply adjusts slowly. | durability | 0.95 | Age of the housing stock. | Supply responses come sooner. |
| A-11 | Enough leases renew during the announcement window, and landlords can raise rents at renewal. | expectations | 0.7 | Share of leases renewing in any eight-month period; lease terms; whether the ordinance rolls rents back to an earlier date. | C-17 not reported; C-21 becomes a decrease. |
| A-12 | Some job opportunities for sitting tenants would require moving or a much longer commute. | mobility | 0.75 | Size of the region; where jobs are located relative to covered housing. | C-18 not reported. |
| A-13 | Buyers of buildings expect the ordinance to last for many years. | expectations | 0.75 | Margin by which the ballot measure passed; history of repeal attempts in the region. | C-20 weakens. |
| A-14 | Without the ordinance, sitting tenants' rents would follow the market path within one or two lease cycles, so the counterfactual rent passes any pre-emptive raise made in the announcement window within the medium horizon. | other | 0.7 | Typical lease length of 12 months; share of renewals priced at market; a pre-emptive raise is bounded by the market rent on the effective date (CR-5c). | C-1, C-27, C-28 and C-29 become ambiguous at the medium horizon too. |
| A-15 | There is no public waiting list or allocation rule for covered units, so seekers find vacancies by their own search. | other | 0.9 | Ordinance text (no allocation provision); how vacancies are advertised in Riverton. | C-3 not reported; PC-2's group remains. |
| A-16 | Landlords may choose among applicants (no first-come or lottery rule), and fair-housing law leaves room to screen on income, credit and references. | other | 0.85 | Ordinance text; state and city fair-housing rules. | C-4 not reported; PC-2's group remains. |
| A-17 | Some sitting tenants would, at market rents, have moved to smaller units or taken in roommates. | substitutability | 0.8 | Household size and unit size of sitting tenants; share of empty-nest households. | C-12 rests on withdrawn units alone (C-9, C-24, through A-5). |
| A-18 | Landlords, tenant groups and developers can organize and spend to change or defend the ordinance at a cost below their stakes. | other | 0.8 | The ordinance came by ballot measure, which shows organized interests on both sides; existing landlord and tenant associations. | C-11 not reported. |
| A-19 | The rent board is a new appropriation that raises the general budget, rather than being taken from other enforcement within a fixed budget. | revenue_use | 0.75 | Ordinance text ("funded from the city's general budget"); the city's budget practice for new agencies. | C-19 is replaced by a fall in the other enforcement the fixed budget would have funded (OC-3, second funding case). |

## 11. Report

**The policy.** Rents on all existing Riverton rental units are frozen for three years and may then rise by at most 2% a year, whoever the tenant. New buildings are exempt. Owners may convert buildings to condominiums after a year-long permit process.

**Visible consequences.** Sitting tenants pay less rent than they would have from the medium horizon on, and the gap grows every year that market rents rise faster than the cap (C-1); they keep the difference (C-29), and landlords of covered units receive less (C-27). In the first months after the freeze the sign is not determined, because landlords raised rents at renewals in the announcement window to lift the frozen base (C-17, C-21).

**Invisible consequences.**
- *People looking for a home in Riverton* find fewer covered units available, search longer, face landlords who choose tenants by income, credit and connections, and sometimes pay key money (C-2 to C-4, C-7). Subtenants in illegal sublets have no recourse to the courts (C-23). Many end up in exempt new buildings, where rents rise because units are withdrawn from the covered stock and sitting tenants occupy more space per household (C-12), or in neighboring cities, where they push rents up (C-15).
- *Sitting tenants* receive less maintenance (C-6) and move less often, even when a different home or a job elsewhere would suit them better (C-5, C-18); some sublet illegally (C-22). Those whose leases renewed in the months before the freeze paid higher rents than they otherwise would have, as landlords locked in a higher base (C-17). Tenants in buildings that are converted must move (C-10), with a relocation payment (C-30).
- *Landlords* receive less on covered units and have less to spend elsewhere (C-27, C-28); the buildings lose value as soon as the ordinance is expected, and owners at that time bear the loss (C-20). They convert some buildings to condominiums (C-8), hold some vacated units empty ahead of conversion (C-24), bear permit and board costs (C-25), and invest less in the rest; over many years the covered rental stock is smaller than it would have been (C-9).
- *Homebuyers* see more condominiums for sale than they otherwise would (C-14).
- *Taxpayers* fund the rent board (C-19), whose staff time is used up on administration and enforcement (C-26).

**Ambiguous effects.** Sitting tenants' rent in the first months after the freeze (C-21): the cap pushes it down, the pre-emptive raises in the announcement window push it up. Whether sitting tenants are better off overall, taking lower rent and lower quality together, cannot be determined by this method. Condominium prices are not signed.

**Key conditions.** The most important assumption is that market rents keep rising above 2% (A-1, p = 0.9); if they do not, the ordinance changes little. That sitting tenants pay less from the medium horizon rests on counterfactual rents tracking the market within a lease cycle or two (A-14, p = 0.7). The direction of new construction depends on whether developers trust the exemption (A-9, p = 0.6): if they come to expect it to be removed, new construction falls instead of rising.

**What this analysis cannot say.** How large any of these effects will be; whether gains to sitting tenants outweigh losses to others; whether the policy is desirable. Health, safety and housing-condition effects beyond the listed variables are not analyzed in version 1.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | tenants.controlled | price_paid | decrease | medium–long | visible | B | PC-1, PC-3, TS-3; CR-12b with A-14 against C-17 | A-1, A-2, A-14 |
| C-2 | tenants.prospective | excess_demand | increase | short | invisible | B | PC-1 | A-1, A-2 |
| C-3 | tenants.prospective | search_cost | increase | short | invisible | B | PC-1, PC-2 | A-1, A-2, A-15 |
| C-4 | tenants.prospective | allocation_by_non_price_criteria | increase | short | invisible | B | PC-1, PC-2 | A-1, A-2, A-16 |
| C-5 | tenants.controlled | turnover | decrease | medium | invisible | B | PC-7 | A-1, A-6 |
| C-6 | tenants.controlled | quality_per_unit | decrease | short–medium | invisible | B | PC-4, RS-2 | A-1, A-4 |
| C-7 | tenants.prospective | side_payments | increase | short | invisible | B | PC-2, PC-6, RS-3 | A-1, A-3 |
| C-8 | landlords.controlled | reclassification | increase | medium | invisible | B | RS-5, PC-5 | A-1, A-5 |
| C-9 | landlords.controlled | quantity_supplied | decrease | medium–long | invisible | B | PC-5, RS-6, TS-1 | A-1, A-5, A-10 |
| C-10 | tenants.controlled (converted buildings) | turnover | increase | medium | invisible | B | PC-5, RS-5, CR-9 | A-1, A-2, A-5 |
| C-11 | landlords, tenants, developers | lobbying_effort | increase | medium | invisible | B | RS-7 | A-1, A-18 |
| C-12 | tenants.prospective | price_substitute (exempt units) | increase | short–medium | invisible | B | PC-3, PC-8, CR-4c | A-1, A-7, A-17 |
| C-13 | developers | investment_target (new rental) | increase | medium | invisible | B | PC-8, LW-4 | A-7, A-9 |
| C-14 | homebuyers | quantity_substitute (condos) | increase | medium | invisible | B | RS-5 | A-1, A-5 |
| C-15 | renters.neighbors | price_paid | increase | medium | invisible | B | PC-3, RS-4 | A-1, A-8 |
| C-16 | tenants.prospective, landlords | quantity_traded (covered rentals) | decrease | medium | invisible | B | OC-4 | A-1, A-5 |
| C-17 | tenants.controlled (renewing before effective date) | price_paid | increase | short | invisible | B | RS-8 | A-11 |
| C-18 | tenants.controlled | job_changes | decrease | medium | invisible | B | PC-7, RS-11 | A-1, A-6, A-12 |
| C-19 | taxpayers | resources_available_other_uses | decrease | short | invisible | B | OC-3, OC-1 | A-19 |
| C-20 | landlords.controlled | asset_value | decrease | short | invisible | B | SB-4 | A-1, A-13 |
| C-21 | tenants.controlled | price_paid (first months after the effective date) | ambiguous | short | visible | B | PC-3 vs RS-8 (C-17); CR-12b | A-1, A-2, A-11 |
| C-22 | tenants.controlled | informal_activity (illegal sublets) | increase | medium | invisible | B | PC-6, RS-3 | A-1, A-3, A-6 |
| C-23 | tenants.prospective (subtenants) | disputes_settled_outside_courts | increase | medium | invisible | B | PC-6, RS-10 | A-1, A-3, A-6 |
| C-24 | landlords.controlled | units_held_vacant | increase | medium | invisible | B | PC-5, RS-5, CR-4 | A-1, A-2, A-5 |
| C-25 | landlords.controlled | compliance_cost | increase | medium | invisible | B | OC-2, CR-8c | A-5 |
| C-26 | officials.enforcement | enforcement_cost | increase | short | invisible | A | OC-3 | none |
| C-27 | landlords.controlled | net_price_received (covered units) | decrease | medium–long | visible | B | PC-3, CR-3a; CR-12b with A-14 | A-1, A-2, A-14 |
| C-28 | landlords.controlled | resources_available_other_uses | decrease | medium | invisible | B | CR-8b, CR-8c; CR-12b with A-2 against C-7 | A-1, A-2, A-14 |
| C-29 | tenants.controlled | resources_available_other_uses | increase | medium | visible | B | CR-8b (matching C-28) | A-1, A-2, A-14 |
| C-30 | tenants.controlled (converted buildings) | resources_available_other_uses | increase | medium | invisible | B | CR-8b (relocation payment, K3) | A-1, A-5 |
| — | tenants.controlled | quality_adjusted_price | ambiguous | medium | invisible | B | C-1 vs C-6 | A-1, A-4 |

## Gaps found

- GAP-1 (closed in catalog 0.2): announcement date added to the policy record; C-17 now reported.
- GAP-2 (closed in catalog 0.2): RS-11 and the variable `job_changes`; C-18 now a signed consequence.
- GAP-3 (closed in catalog 0.2): opportunity costs written as signed variables; the duplicate entry for search time removed.
- Catalog 0.3: SB-4 now covers losses as well as gains; C-20 added.
- Catalog 0.5: corrected after the core-only comparison (see ../05_examples_core/WE-001_rent_freeze_core.md): sitting tenants' short-run rent made ambiguous (C-21, CR-12b with C-17) and C-1 limited to medium–long with new premise A-14; C-10 replaced by a turnover increase (the price claim used the controlled rent as baseline); added landlords' net price, both sides of the rent transfer and the relocation payment, enforcement and compliance cost, units held vacant, illegal sublets and subtenants' disputes (C-22 to C-30); PC-2 members given per-margin premises (A-15, A-16; wait_time dropped); RS-7 premise A-18; OC-3 funding stated (A-19); PC-8 mechanism and Unless clause addressed; the cross-variable "total cost of housing" row removed (CR-12c).
