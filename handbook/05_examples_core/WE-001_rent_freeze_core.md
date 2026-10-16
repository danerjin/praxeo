# WE-001 / Analysis: Rent freeze with a new-construction exemption (core-only re-run)

Analyst: core-only re-run (Handbook 0.4)  |  Rules: core rules CR-1 to CR-12 only  |  Status: awaiting comparison

Rule set: the core rules CR-1 to CR-12 (`../04a_core_rules.md`), AX-1 and LW-1 to LW-10 (`../01_foundations.md`), and arithmetic. No pattern is cited. New premises that the derivations needed are numbered A-N1, A-N2, ... and are listed in section 10 and under "Gaps found".

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

| Component | Rothbard type | Binding? (assumption ID) | Core rules applied |
| --- | --- | --- | --- |
| K1 Rent freeze and cap | triangular (fixes the terms of exchange between landlord and tenant) | Yes, within the first year (A-1); enforced (A-2) | CR-1, CR-6, CR-4, CR-7, CR-10 |
| K2 Tenancy rules | triangular (removes contract terms: eviction without cause, assignment) | Yes for every covered lease (A-6) | CR-1, CR-4, CR-5a, CR-9 |
| K3 Withdrawal route | triangular (attaches conditions and a compelled payment to conversion) | Yes for any landlord who converts (A-5) | CR-1, CR-5b, CR-7a, CR-10b |
| K4 Rent board | binary (funded from the general budget) | Yes (A-2) | CR-1, CR-8 |

**CR-1 operations, by component and actor class.** Operation 1: removes an option; 2: adds an option; 3: changes what an option brings; 4: transfers means.

| Component | Actor class | CR-1 operations |
| --- | --- | --- |
| K1 | landlords.controlled_units | 1 (charging above the frozen or capped rent removed, for those who comply); 3 (fines attached to overcharging, for those who would violate) |
| K1 | tenants.controlled_units | 3 (the rent increase that would have come with staying is removed) |
| K1 | prospective_tenants | 1 (offering more than the cap for a covered unit removed); 3 (key money attaches a penalty risk) |
| K1 | factor_owners.specific (owners of covered buildings) | 3 (the expected yield of the building is reduced) |
| K1 | sellers.prospective (developers), owners of exempt units | none directly (exempt); affected only through CR-9 |
| K2 | landlords.controlled_units | 1 (eviction without cause and non-renewal removed) |
| K2 | tenants.controlled_units | 1 (assigning or selling the tenancy removed); 2 (secure tenure: the option to stay is guaranteed) |
| K3 | landlords.controlled_units | 2 (a lawful route out of the cap); 3 (12-month permit process and relocation payments attached to conversion); 4 (compelled payment to tenants) |
| K3 | tenants.converting_buildings | 1 (the covered tenancy ends on conversion); 4 (relocation payment received) |
| K4 | taxpayers | 4 (means transferred to fund the board) |
| K4 | officials.enforcement | 2 (power to fine) |

## 3. Actor classes

| Actor class | Role | How its options change |
| --- | --- | --- |
| tenants.controlled_units | Sitting tenants of covered units | Pay the frozen or capped rent; cannot assign; secure tenure (K1, K2) |
| landlords.controlled_units | Owners letting covered units | Cannot charge above the cap; cannot evict without cause; may convert after 12 months and payments (K1 to K3) |
| factor_owners.specific (owners of covered buildings) | Holders of the durable asset | Expected yield of the building cut (K1); conversion route burdened (K3) |
| prospective_tenants | Households seeking a rental in Riverton | Cannot outbid others for covered units; face fewer vacancies (K1, via CR-6) |
| tenants.converting_buildings | Tenants in buildings that are converted | Tenancy ends; receive relocation payment (K3) |
| sellers.prospective (developers) | Would-be builders of new rental units | Not bound (exempt); demand and expectations change (CR-9, CR-11c) |
| buyers.substitutes (condominium buyers) | Buyers of owner-occupied units | More converted units offered (CR-9) |
| neighboring_jurisdictions (Eastfield and Northgate renters) | Renters just outside the city | Affected only through CR-9 (across_border) |
| input_suppliers (maintenance and repair trades) | Sellers of repairs and renovations | Affected through landlords' maintenance and conversion choices (CR-9) |
| taxpayers | Fund the rent board | Means transferred (K4) |
| officials.enforcement | Rent board | Administers and fines (K4) |

## 4. Direct effect

CR-1 with CR-2: what changes at once for the bound and the protected. The direct effect on sitting tenants' rent is split by horizon because the announcement (CR-10a) raises the frozen base.

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-1 | tenants.controlled_units | price_paid (covered units, after the effective date) | ambiguous | short | (−) CR-1 (op 1, K1: rent above the frozen level removed) → CR-2; (+) CR-10a (freeze at the effective-date level announced 8 months ahead) → CR-4 mirror (x: raise at renewal before the effective date) → higher frozen base; CR-12b | A-1, A-2, A-11 |
| C-2 | tenants.controlled_units | price_paid (covered units) | decrease | medium | CR-1 (op 1, K1) → CR-2; the opposing announcement chain is bounded by CR-5c (a pre-emptive raise cannot exceed what the tenant accepts, the market rent on the effective date) and is overtaken by the counterfactual path (A-1, A-N1): dominance premise under CR-12b | A-1, A-2, A-N1 |
| C-3 | tenants.controlled_units | price_paid (covered units) | decrease | long | CR-1 (op 1, K1) → CR-2; arithmetic: a 2% cap against a counterfactual rising above 2% a year opens a gap that compounds | A-1, A-2 |
| C-4 | landlords.controlled_units | net_price_received (covered units) | decrease | medium | CR-1 (op 1, K1) → CR-3a; dominance over the announcement chain as for C-2 | A-1, A-2, A-N1 |
| C-30 | taxpayers | resources_available_other_uses | decrease | short | CR-1 (op 4, K4 funded from the general budget) → CR-8a, CR-8b | none |
| C-31 | officials.enforcement | enforcement_cost | increase | short | CR-1 (op 2, K4) → CR-8c | none |

## 5. Responses

CR-4 pairs of options examined for each actor class (substitute, adjust terms, evade, relocate, reclassify, exit, lobby, change timing, enter), with CR-6 where a price is fixed and CR-5 where an exchange is prevented or compelled.

| Actor class | Pair of options (CR-4) or rule | Result |
| --- | --- | --- |
| landlords.controlled_units | CR-6 (rent held below clearing): which unregulated margins are open | Maintenance and quality (A-4), tenant selection, key money (A-3) |
| landlords.controlled_units | CR-4 (x: maintain above code minimum, y: cut to the minimum) | Maintenance falls (reading U1-a) |
| landlords.controlled_units | CR-4 (x: comply, y: violate by charging key money) | Some violate (A-3) |
| landlords.controlled_units | CR-4 (x: rental use, y: condominium use); CR-7a | Some convert (A-5) |
| landlords.controlled_units | CR-4 (x: re-let a vacated unit, y: hold it vacant pending conversion or sale) | Some hold units vacant |
| landlords.controlled_units | CR-4 (x: accept, y: lobby) | Some lobby (A-N2) |
| landlords.controlled_units | CR-10a (x: raise rent at renewal after the effective date, y: raise it before) | Raises brought forward (A-11) |
| landlords.controlled_units | CR-4 (x: covered form, y: uncovered form) | No route found other than conversion (K3); the unit, not the lease, is covered. Major renovation is reading U1-b |
| tenants.controlled_units | CR-4 (x: move to a market-rent unit, y: stay) | Fewer moves |
| tenants.controlled_units | CR-4 (x: comply with no-assignment, y: sublet illegally) | Some sublet (A-3, A-6) |
| tenants.controlled_units | CR-4 (x: take a job that requires moving, y: keep the tenancy) | Fewer job changes (A-12) |
| tenants.controlled_units | CR-4 mirror (x: accept repeal, y: lobby to keep the ordinance) | Some lobby (A-N2) |
| prospective_tenants | CR-6 (queues, criteria, side payments); CR-4 (x: covered unit, y: exempt unit or neighboring city) | More search, more selection by landlords, some key money; some turn to exempt units (A-7) or neighbors (A-8) |
| sellers.prospective (developers) | CR-4 (x: stay out, y: build exempt units) | Ambiguous (see section 7) |
| prospective_tenants | CR-5a (exchanges above the cap prevented) | New covered leases fall |

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-5 | tenants.controlled_units | price_paid (leases renewed in the 8-month announcement window) | increase | short | CR-10a (rent to be frozen at its level on the effective date) → CR-4 mirror (landlords' x: raise at renewal now, made better) → CR-5c (raise bounded by market rent) | A-11 |
| C-6 | landlords.controlled_units | maintenance_spending | U1-a: decrease; U1-b: ambiguous | medium | CR-6 (rent held below clearing; pressure displaced to unregulated terms: maintenance) → CR-4 (x: maintain above code minimum, y: cut to the minimum); under U1-b, CR-4 mirror (x: major renovation that unlocks a rent rise) pushes the other way, CR-12b | A-1, A-2, A-4 |
| C-8 | tenants.controlled_units | turnover | decrease | medium | CR-1 (op 3, K1; op 2, K2) → CR-4 (x: move to a market-rent unit, y: stay in the covered unit, now better) → CR-4a | A-1, A-2, A-6 |
| C-10 | prospective_tenants | excess_demand (covered units) | increase | short | CR-6 (price held below clearing) → arithmetic: units wanted at the cap exceed units offered | A-1, A-2 |
| C-11 | prospective_tenants | search_cost | increase | short | C-10 and C-8 (fewer covered vacancies) → CR-6 (pressure displaced to search) → CR-8c | A-1, A-2 |
| C-12 | prospective_tenants | allocation_by_non_price_criteria | increase | short | CR-6 (the scarce side chooses among applicants by other criteria) + CR-1 (op 1, K2: a poor tenant cannot be removed without cause) → CR-4 (x: accept the first applicant, y: screen harder) | A-1, A-2 |
| C-13 | prospective_tenants | side_payments | increase | short | CR-6 (exchanges outside the rule) → CR-4 (x: comply, y: charge key money) | A-1, A-3 |
| C-14 | tenants.controlled_units | informal_activity (illegal sublets) | increase | medium | CR-1 (op 1, K2: assignment and sale removed) + CR-6 (gap between capped and clearing rent) → CR-4 (x: comply, y: sublet illegally) | A-1, A-3, A-6 |
| C-16 | landlords.controlled_units | capital_stock_target (covered rental units) | decrease | medium | CR-7a (yield of rental use cut; x: rental use, y: condominium use via K3) → CR-10b (conversion is a flow; 12-month permit) | A-1, A-2, A-5, A-10 |
| C-17 | landlords.controlled_units | units_held_vacant | increase | medium | CR-1 (op 3, K3: relocation payment per sitting tenant; op 1, K2: no eviction without cause) → CR-4 (x: re-let a vacated unit, y: hold it vacant pending conversion or sale) | A-1, A-2, A-5 |
| C-18 | landlords.controlled_units | compliance_cost | increase | medium | CR-1 (op 3, K3: permit process and relocation payments; K4: board proceedings) → CR-8c | A-5 |
| C-20 | landlords.controlled_units | lobbying_effort | increase | medium | CR-1 (op 1, K1) → CR-4 (x: accept the ordinance, y: lobby to change it, e.g. for a renovation allowance) → CR-8c | A-1, A-N2 |
| C-21 | tenants.controlled_units | lobbying_effort | increase | medium | CR-4 mirror (sitting tenants hold a gain that repeal would remove; x: accept repeal, y: lobby to keep the ordinance) → CR-8c | A-1, A-N2 |
| C-28 | prospective_tenants | full_cost_per_unit (covered units) | ambiguous | short | (−) CR-1 (op 1): money rent capped; (+) CR-6: search, side payments and selection (C-11, C-13, C-12); CR-12b | A-1, A-2, A-3 |
| C-29 | prospective_tenants | quantity_traded (new leases on covered units) | decrease | medium | CR-5a (exchanges at rents above the cap prevented) with C-8, C-17 and C-16 (fewer units offered) | A-1, A-2 |

## 6. Second-order effects

Depth limit 4; diffuse bystander effects pruned after depth 3. Each link names the exchange relation it follows (CR-9).

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C-7 | tenants.controlled_units | quality_per_unit | U1-a: decrease; U1-b: ambiguous | long | C-6 → CR-9 (maintenance is part of what the lease delivers) → CR-10b (quality of the stock changes through flows of maintenance and wear) | the lease (same exchange: landlord to tenant) | A-1, A-2, A-4, A-10 |
| C-9 | tenants.controlled_units | job_changes | decrease | medium | C-8 → CR-9 (tenancy tied to a place) → CR-4 (x: take a job that requires moving or a much longer commute, y: keep the tenancy) | complement, location (covered tenancy ↔ regional labor market) | A-1, A-2, A-6, A-12 |
| C-15 | prospective_tenants (subtenants in illegal sublets) | disputes_settled_outside_courts | increase | medium | C-14 → CR-11b (an exchange outside the legal market has no access to courts) | the sublet (tenant to subtenant) | A-1, A-3, A-6 |
| C-19 | tenants.converting_buildings | turnover | increase | medium | C-16 → CR-9 (the landlord's exit ends the lease) → CR-1 (op 1 and op 4, K3) | the lease (landlord to tenant) | A-1, A-2, A-5 |
| C-22 | factor_owners.specific (owners of covered buildings) | asset_value | decrease | short | CR-10a (the cut in expected yield is known from the ballot campaign) → CR-7c and CR-10c (price of the durable asset falls to the new expected yield; borne by owners when the change becomes expected) | sale of buildings (owner to buyer) | A-1, A-2, A-13 |
| C-23 | buyers.substitutes (condominium buyers) | price_substitute (condominiums) | ambiguous | medium | (−) C-16 → CR-9 (converted units added to condominium supply) → CR-6; (+ or −) CR-9 (substitute: some rationed-out seekers buy instead of renting, while sitting tenants who would have bought stay put); CR-12b | same_market_other_segment (rental units ↔ condominiums), close | A-1, A-2, A-5 |
| C-24 | prospective_tenants | price_substitute (rent on exempt new units) | ambiguous | medium | (+) C-17 and C-16: units withdrawn from rental use push households toward exempt units, CR-9 → CR-6; (−) C-25: added exempt supply; arithmetic: lower turnover alone moves no net households between segments (each sitting tenant who stays blocks one seeker who goes elsewhere); CR-12b | same_market_other_segment (covered ↔ exempt units), close | A-1, A-2, A-5, A-7, A-9 |
| C-25 | sellers.prospective (developers) | investment_target (new rental construction) | ambiguous | long | C-24 → CR-7a (investment follows the expected yield on exempt units, whose sign is ambiguous); CR-11c (the ordinance conveys that the city regulates rents; limited by A-9); CR-12b | input_to (construction → exempt rental units) | A-7, A-9, A-10 |
| C-26 | neighboring_jurisdictions (Eastfield and Northgate renters) | price_substitute (rents in neighboring cities) | ambiguous | medium | (+) C-17 and C-16: households pushed out of Riverton rental use, CR-9 → CR-6; (−) C-25: exempt construction in Riverton absorbs households; arithmetic as for C-24; CR-12b | across_border (Riverton ↔ neighboring rentals), partial | A-1, A-5, A-8 |
| C-27 | input_suppliers (maintenance and repair trades) | earnings | ambiguous | medium | (−) C-6 → CR-9 → LW-10; (+) C-16: conversion works → CR-9 → LW-10; CR-12b | input_to (repairs and renovation → housing) | A-1, A-4, A-5 |
| C-32 | landlords.controlled_units | resources_available_other_uses | decrease | medium | C-4 → CR-8b (the rent forgone by landlords is what sitting tenants keep) | the lease | A-1, A-2, A-N1 |
| C-33 | tenants.controlled_units | resources_available_other_uses | increase | medium | C-2 → CR-8b (matching gain to the loss in C-32) | the lease | A-1, A-2, A-N1 |
| C-34 | prospective_tenants | resources_available_other_uses | decrease | short | C-11 and C-13 → CR-8c (search time used up) and CR-8b (key money transferred to landlords) | the lease (seeker to landlord) | A-1, A-2, A-3 |

**Where chains were stopped.**

- C-9: the effect on employers who would have hired covered tenants is a diffuse bystander effect at depth 3; stopped.
- C-27: the effect on the trades' own suppliers and workers is stopped at depth 3 (diffuse).
- C-26 and C-24: effects on landlords and land values in the exempt segment and the neighboring cities follow the ambiguous sign of rents there; not carried further.
- C-22: effects on lenders holding mortgages on covered buildings stopped at depth 3 (no recorded relation beyond the sale of buildings).

## 7. Combined effects

Keys reached by one chain, or by chains with the same sign, take that sign (CR-12a). Keys where chains conflict:

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance premise | Combined sign |
| --- | --- | --- | --- | --- |
| tenants.controlled_units, price_paid, short | CR-10a: frozen base raised by pre-emptive raises (A-11) | CR-1 → CR-2: rent capped below a rising market (A-1) | None at this horizon: the size of pre-emptive raises against the counterfactual path is magnitude | ambiguous (C-1) |
| tenants.controlled_units, price_paid, medium | CR-10a (as above) | CR-1 → CR-2 | CR-5c bounds a pre-emptive raise by the market rent on the effective date; the counterfactual path passes that level within a lease cycle or two (A-N1, A-1) | decrease (C-2) |
| landlords.controlled_units, maintenance_spending, medium (reading U1-b) | CR-4 mirror: renovation unlocks a rent rise | CR-6 → CR-4: cut to code minimum | None | U1-a: decrease; U1-b: ambiguous (C-6) |
| buyers.substitutes, price_substitute (condominiums), medium | Rationed-out seekers buy | Converted units added; sitting tenants who would have bought stay | None | ambiguous (C-23) |
| prospective_tenants, price_substitute (exempt units), medium | Units withdrawn from rental use (vacancy, conversion) | Added exempt construction | None; lower turnover alone moves no net households (arithmetic) | ambiguous (C-24) |
| sellers.prospective, investment_target, long | Exempt rents higher, if they are | CR-11c regulatory signal; exempt rents lower, if they are | None | ambiguous (C-25) |
| neighboring_jurisdictions, price_substitute, medium | Households pushed out of Riverton rental use | Exempt construction in Riverton absorbs households | None | ambiguous (C-26) |
| input_suppliers, earnings, medium | Conversion works | Less maintenance | None | ambiguous (C-27) |
| prospective_tenants, full_cost_per_unit, short | Search, key money, selection | Capped money rent | None | ambiguous (C-28) |

## 8. Time structure

- **Announcement (CR-10a).** The measure was on the ballot eight months before it took effect and was expected to pass. Rents are frozen at their level on the effective date, so landlords whose leases renew in the window raise rents then (C-5). Building values fall when the cut in expected yield becomes expected, which is during the campaign, not at the effective date (C-22; CR-7c, CR-10c).
- **A cap that binds more each year.** Three years of freeze, then 2% a year, against a counterfactual rising about 5% a year (A-1): the gap compounds by arithmetic. This is why the short-run sign for sitting tenants is ambiguous and the medium and long-run signs are decreases (C-1, C-2, C-3).
- **Durable stock (CR-10b).** Buildings last decades (A-10). Quality declines through under-maintenance, gradually (C-6, C-7). Conversions start only after the 12-month permit process (C-16), so stock withdrawal is a medium-horizon effect that accumulates in the long run.
- **Expectations about the exemption.** Developers' response depends on whether the exemption is expected to last (A-9, p 0.6) and on the ambiguous exempt-segment rent (C-25).
- **Persistence.** Converted buildings do not return to rental use if the ordinance ends (CR-10b: reversal is costly). Tenancies held longer because of the cap build lock-in that grows with the gap (C-8, C-9).

## 9. Opportunity costs

Each written as a signed change in a variable (CR-3, CR-8).

| ID | Actor class | Variable | Sign | What is given up | Rules |
| --- | --- | --- | --- | --- | --- |
| C-2 | tenants.controlled_units | price_paid (covered units) | decrease | Rent landlords would have received; retained by sitting tenants (CR-8b) | CR-1 → CR-8b |
| C-9 | tenants.controlled_units | job_changes | decrease | Jobs not taken because they would cost the tenancy | CR-3a, CR-4 |
| C-11 | prospective_tenants | search_cost | increase | Time and money spent searching, used up (CR-8c) | CR-6 → CR-8c |
| C-17 | landlords.controlled_units | units_held_vacant | increase | Housing services the vacant units would have provided | CR-4 → CR-8a |
| C-18 | landlords.controlled_units | compliance_cost | increase | Resources spent on permits and proceedings (CR-8c) | CR-8c |
| C-20 | landlords.controlled_units | lobbying_effort | increase | Resources spent lobbying (CR-8c) | CR-4 → CR-8c |
| C-29 | prospective_tenants | quantity_traded (new leases on covered units) | decrease | Leases seekers and landlords would have agreed at higher rents (CR-5a) | CR-5a |
| C-30 | taxpayers | resources_available_other_uses | decrease | What the general budget would otherwise have funded (CR-8a) | CR-8a, CR-8b |
| C-31 | officials.enforcement | enforcement_cost | increase | Staff time and budget used on administration (CR-8c) | CR-8c |
| C-32 | landlords.controlled_units | resources_available_other_uses | decrease | Rent income forgone | CR-8b |

## 10. Assumptions

Case assumptions are used as given. New premises added by this re-run are marked A-N.

| ID | Statement | Type | p | Evidence | If false |
| --- | --- | --- | --- | --- | --- |
| A-1 | Market rents keep rising above 2% a year, so the cap binds within the first year. | binding | 0.9 | Five-year rent trend; vacancy rate; pipeline of new supply. | Fail or lose support: C-1, C-2, C-3, C-4, C-6, C-7, C-8, C-9, C-10, C-11, C-12, C-13, C-14, C-15, C-16, C-17, C-19, C-20, C-21, C-22, C-23, C-24, C-26, C-27, C-28, C-29, C-32, C-33, C-34 |
| A-2 | The rent board enforces the cap against most landlords. | enforcement | 0.8 | Board's budget and staffing; complaint-driven model; size of fines relative to the rent gap. | Fail or lose support: C-1, C-2, C-3, C-4, C-6, C-7, C-8, C-9, C-10, C-11, C-12, C-16, C-17, C-19, C-22, C-23, C-24, C-28, C-29, C-32, C-33, C-34 |
| A-3 | Some landlords and tenants evade (key money, illegal sublets) without being caught. | enforcement | 0.8 | Complaint-driven enforcement; tenancies cannot be assigned, which creates an incentive for illegal sublets. | Fail or lose support: C-13, C-14, C-15, C-28, C-34 |
| A-4 | Housing codes leave landlords room to reduce maintenance above the legal minimum. | other | 0.85 | Content of the city's habitability code and inspection frequency. | Fail or lose support: C-6, C-7, C-27 |
| A-5 | The conversion route is usable for a meaningful number of buildings. | alternative_uses | 0.7 | Permit approval rates; relocation payment size; demand for condominiums. | Fail or lose support: C-16, C-17, C-18, C-19, C-23, C-24, C-26, C-27 |
| A-6 | Sitting tenants cannot transfer their tenancy. | other | 0.95 | Ordinance text (K2). | Fail or lose support: C-8, C-9, C-14, C-15 |
| A-7 | Covered and exempt units are close substitutes. | substitutability | 0.85 | Similar locations and sizes; same tenant pool. | Fail or lose support: C-24, C-25 |
| A-8 | Commuting from neighboring cities is practical for many seekers. | mobility | 0.7 | Travel times of 15 to 25 minutes; transit links. | Fail or lose support: C-26 |
| A-9 | Developers expect the new-construction exemption to last. | expectations | 0.6 | Political history of exemptions in the region; whether the exemption is in the city charter or an ordinance. | Fail or lose support: C-24, C-25 |
| A-10 | Rental buildings last several decades, so supply adjusts slowly. | durability | 0.95 | Age of the housing stock. | Fail or lose support: C-7, C-16, C-25 |
| A-11 | Enough leases renew during the announcement window, and landlords can raise rents at renewal. | expectations | 0.7 | Share of leases renewing in any eight-month period; lease terms; whether the ordinance rolls rents back to an earlier date. | Fail or lose support: C-1, C-5 |
| A-12 | Some job opportunities for sitting tenants would require moving or a much longer commute. | mobility | 0.75 | Size of the region; where jobs are located relative to covered housing. | Fail or lose support: C-9 |
| A-13 | Buyers of buildings expect the ordinance to last for many years. | expectations | 0.75 | Margin by which the ballot measure passed; history of repeal attempts in the region. | Fail or lose support: C-22 |
| A-N1 | In the counterfactual, rents of sitting tenants in covered units follow the market path within one or two lease cycles, so the counterfactual rent passes any pre-emptive raise made in the announcement window within the medium horizon. (new premise) | other | 0.7 | Typical lease length of 12 months; share of renewals priced at market in Riverton; a pre-emptive raise is bounded by the market rent on the effective date (CR-5c). | Fail or lose support: C-2, C-4, C-32, C-33 |
| A-N2 | Landlords and tenant groups can organize and spend to change or defend the ordinance. (new premise) | other | 0.8 | The ordinance came by ballot measure, which shows organized interests on both sides. | Fail or lose support: C-20, C-21 |

**Not reported** (a premise has p below 0.5, or the record lacks a needed fact):

- Developers read the ordinance as a sign that the exemption will later be removed, and build less (CR-11c → CR-4 (x: build, y: stay out)): this is A-9 failing, p 0.4.
- Effect of the ordinance on the number of households living in Riverton: the counting argument (arithmetic) shows that only units withdrawn from use change it, and their number against new exempt units is magnitude; no sign.
- Earnings of sitting tenants who forgo moves for jobs (C-9): CR-3a says they are worse off by their own ranking than with the cap and free mobility, but no sign for `earnings` follows, because they chose the tenancy over the job.

## 11. Report

**The policy:** Riverton freezes rents on all existing rental units for three years at their level on the effective date, then caps increases at 2% a year, including between tenants. Tenants may be evicted only for cause and cannot assign their tenancy. Landlords may leave the system by converting buildings to condominiums after a 12-month permit process and relocation payments. Units first occupied after the effective date are exempt. A rent board funded from the general budget enforces the rules on complaint.

**Visible consequences:** Sitting tenants pay less rent than they would have in the medium and long run (C-2, C-3) and keep the difference (C-33); landlords of covered units receive less (C-4). In the first months the sign for sitting tenants is not determined, because landlords raised rents at renewals before the effective date to lift the frozen base (C-5, C-1).

**Invisible consequences:** Landlords: maintenance falls toward the code minimum (reading U1-a) and unit quality declines over years (C-6, C-7); some buildings are converted and some units held vacant ahead of conversion (C-16, C-17); compliance and lobbying costs rise (C-18, C-20); building values fall during the campaign (C-22). Sitting tenants: they move less (C-8), take fewer jobs that require moving (C-9), some sublet illegally (C-14), and some lobby to keep the ordinance (C-21). Tenants in converted buildings move (C-19). Seekers: more searching, more selection by landlords, key money and fewer covered leases (C-11, C-12, C-13, C-29), with less legal recourse for subtenants (C-15). Taxpayers fund the board (C-30, C-31).

**Ambiguous effects:** Rents on exempt new units and in the neighboring cities (C-24, C-26): units withdrawn from use push up, new exempt construction pushes down, and lower turnover alone moves no net households. Developers' investment (C-25), condominium prices (C-23), the repair trades' earnings (C-27) and seekers' full cost of a covered unit (C-28) are also ambiguous. What would decide each is stated in section 7.

**Key conditions:** The cap binds (A-1, p 0.9) and is enforced (A-2, p 0.8); housing codes leave room to cut maintenance (A-4, p 0.85); the conversion route is usable (A-5, p 0.7); counterfactual sitting-tenant rents track the market within a lease cycle or two (A-N1, p 0.7, new). If the cap did not bind, almost every consequence above would vanish.

**What this analysis cannot say:** How large any effect is; whether tenants' gains outweigh landlords' and seekers' losses; whether the policy is good. Health, safety and housing-condition effects beyond the listed variables are not analyzed in version 1. Signs marked ambiguous cannot be resolved without magnitudes.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C-1 | tenants.controlled_units | price_paid (covered units, after the effective date) | ambiguous | short | visible | B | (−) CR-1 (op 1, K1: rent above the frozen level removed) → CR-2; (+) CR-10a (freeze at the effective-date level announced 8 months ahead) → CR-4 mirror (x: raise at renewal before the effective date) → higher frozen base; CR-12b | A-1, A-2, A-11 |
| C-2 | tenants.controlled_units | price_paid (covered units) | decrease | medium | visible | B | CR-1 (op 1, K1) → CR-2; the opposing announcement chain is bounded by CR-5c (a pre-emptive raise cannot exceed what the tenant accepts, the market rent on the effective date) and is overtaken by the counterfactual path (A-1, A-N1): dominance premise under CR-12b | A-1, A-2, A-N1 |
| C-3 | tenants.controlled_units | price_paid (covered units) | decrease | long | visible | B | CR-1 (op 1, K1) → CR-2; arithmetic: a 2% cap against a counterfactual rising above 2% a year opens a gap that compounds | A-1, A-2 |
| C-4 | landlords.controlled_units | net_price_received (covered units) | decrease | medium | visible | B | CR-1 (op 1, K1) → CR-3a; dominance over the announcement chain as for C-2 | A-1, A-2, A-N1 |
| C-5 | tenants.controlled_units | price_paid (leases renewed in the 8-month announcement window) | increase | short | invisible | B | CR-10a (rent to be frozen at its level on the effective date) → CR-4 mirror (landlords' x: raise at renewal now, made better) → CR-5c (raise bounded by market rent) | A-11 |
| C-6 | landlords.controlled_units | maintenance_spending | U1-a: decrease; U1-b: ambiguous | medium | invisible | B | CR-6 (rent held below clearing; pressure displaced to unregulated terms: maintenance) → CR-4 (x: maintain above code minimum, y: cut to the minimum); under U1-b, CR-4 mirror (x: major renovation that unlocks a rent rise) pushes the other way, CR-12b | A-1, A-2, A-4 |
| C-7 | tenants.controlled_units | quality_per_unit | U1-a: decrease; U1-b: ambiguous | long | invisible | B | C-6 → CR-9 (maintenance is part of what the lease delivers) → CR-10b (quality of the stock changes through flows of maintenance and wear) | A-1, A-2, A-4, A-10 |
| C-8 | tenants.controlled_units | turnover | decrease | medium | invisible | B | CR-1 (op 3, K1; op 2, K2) → CR-4 (x: move to a market-rent unit, y: stay in the covered unit, now better) → CR-4a | A-1, A-2, A-6 |
| C-9 | tenants.controlled_units | job_changes | decrease | medium | invisible | B | C-8 → CR-9 (tenancy tied to a place) → CR-4 (x: take a job that requires moving or a much longer commute, y: keep the tenancy) | A-1, A-2, A-6, A-12 |
| C-10 | prospective_tenants | excess_demand (covered units) | increase | short | invisible | B | CR-6 (price held below clearing) → arithmetic: units wanted at the cap exceed units offered | A-1, A-2 |
| C-11 | prospective_tenants | search_cost | increase | short | invisible | B | C-10 and C-8 (fewer covered vacancies) → CR-6 (pressure displaced to search) → CR-8c | A-1, A-2 |
| C-12 | prospective_tenants | allocation_by_non_price_criteria | increase | short | invisible | B | CR-6 (the scarce side chooses among applicants by other criteria) + CR-1 (op 1, K2: a poor tenant cannot be removed without cause) → CR-4 (x: accept the first applicant, y: screen harder) | A-1, A-2 |
| C-13 | prospective_tenants | side_payments | increase | short | invisible | B | CR-6 (exchanges outside the rule) → CR-4 (x: comply, y: charge key money) | A-1, A-3 |
| C-14 | tenants.controlled_units | informal_activity (illegal sublets) | increase | medium | invisible | B | CR-1 (op 1, K2: assignment and sale removed) + CR-6 (gap between capped and clearing rent) → CR-4 (x: comply, y: sublet illegally) | A-1, A-3, A-6 |
| C-15 | prospective_tenants (subtenants in illegal sublets) | disputes_settled_outside_courts | increase | medium | invisible | B | C-14 → CR-11b (an exchange outside the legal market has no access to courts) | A-1, A-3, A-6 |
| C-16 | landlords.controlled_units | capital_stock_target (covered rental units) | decrease | medium | invisible | B | CR-7a (yield of rental use cut; x: rental use, y: condominium use via K3) → CR-10b (conversion is a flow; 12-month permit) | A-1, A-2, A-5, A-10 |
| C-17 | landlords.controlled_units | units_held_vacant | increase | medium | invisible | B | CR-1 (op 3, K3: relocation payment per sitting tenant; op 1, K2: no eviction without cause) → CR-4 (x: re-let a vacated unit, y: hold it vacant pending conversion or sale) | A-1, A-2, A-5 |
| C-18 | landlords.controlled_units | compliance_cost | increase | medium | invisible | B | CR-1 (op 3, K3: permit process and relocation payments; K4: board proceedings) → CR-8c | A-5 |
| C-19 | tenants.converting_buildings | turnover | increase | medium | invisible | B | C-16 → CR-9 (the landlord's exit ends the lease) → CR-1 (op 1 and op 4, K3) | A-1, A-2, A-5 |
| C-20 | landlords.controlled_units | lobbying_effort | increase | medium | invisible | B | CR-1 (op 1, K1) → CR-4 (x: accept the ordinance, y: lobby to change it, e.g. for a renovation allowance) → CR-8c | A-1, A-N2 |
| C-21 | tenants.controlled_units | lobbying_effort | increase | medium | invisible | B | CR-4 mirror (sitting tenants hold a gain that repeal would remove; x: accept repeal, y: lobby to keep the ordinance) → CR-8c | A-1, A-N2 |
| C-22 | factor_owners.specific (owners of covered buildings) | asset_value | decrease | short | invisible | B | CR-10a (the cut in expected yield is known from the ballot campaign) → CR-7c and CR-10c (price of the durable asset falls to the new expected yield; borne by owners when the change becomes expected) | A-1, A-2, A-13 |
| C-23 | buyers.substitutes (condominium buyers) | price_substitute (condominiums) | ambiguous | medium | invisible | B | (−) C-16 → CR-9 (converted units added to condominium supply) → CR-6; (+ or −) CR-9 (substitute: some rationed-out seekers buy instead of renting, while sitting tenants who would have bought stay put); CR-12b | A-1, A-2, A-5 |
| C-24 | prospective_tenants | price_substitute (rent on exempt new units) | ambiguous | medium | invisible | B | (+) C-17 and C-16: units withdrawn from rental use push households toward exempt units, CR-9 → CR-6; (−) C-25: added exempt supply; arithmetic: lower turnover alone moves no net households between segments (each sitting tenant who stays blocks one seeker who goes elsewhere); CR-12b | A-1, A-2, A-5, A-7, A-9 |
| C-25 | sellers.prospective (developers) | investment_target (new rental construction) | ambiguous | long | invisible | B | C-24 → CR-7a (investment follows the expected yield on exempt units, whose sign is ambiguous); CR-11c (the ordinance conveys that the city regulates rents; limited by A-9); CR-12b | A-7, A-9, A-10 |
| C-26 | neighboring_jurisdictions (Eastfield and Northgate renters) | price_substitute (rents in neighboring cities) | ambiguous | medium | invisible | B | (+) C-17 and C-16: households pushed out of Riverton rental use, CR-9 → CR-6; (−) C-25: exempt construction in Riverton absorbs households; arithmetic as for C-24; CR-12b | A-1, A-5, A-8 |
| C-27 | input_suppliers (maintenance and repair trades) | earnings | ambiguous | medium | invisible | B | (−) C-6 → CR-9 → LW-10; (+) C-16: conversion works → CR-9 → LW-10; CR-12b | A-1, A-4, A-5 |
| C-28 | prospective_tenants | full_cost_per_unit (covered units) | ambiguous | short | invisible | B | (−) CR-1 (op 1): money rent capped; (+) CR-6: search, side payments and selection (C-11, C-13, C-12); CR-12b | A-1, A-2, A-3 |
| C-29 | prospective_tenants | quantity_traded (new leases on covered units) | decrease | medium | invisible | B | CR-5a (exchanges at rents above the cap prevented) with C-8, C-17 and C-16 (fewer units offered) | A-1, A-2 |
| C-30 | taxpayers | resources_available_other_uses | decrease | short | invisible | A | CR-1 (op 4, K4 funded from the general budget) → CR-8a, CR-8b | none |
| C-31 | officials.enforcement | enforcement_cost | increase | short | invisible | A | CR-1 (op 2, K4) → CR-8c | none |
| C-32 | landlords.controlled_units | resources_available_other_uses | decrease | medium | invisible | B | C-4 → CR-8b (the rent forgone by landlords is what sitting tenants keep) | A-1, A-2, A-N1 |
| C-33 | tenants.controlled_units | resources_available_other_uses | increase | medium | visible | B | C-2 → CR-8b (matching gain to the loss in C-32) | A-1, A-2, A-N1 |
| C-34 | prospective_tenants | resources_available_other_uses | decrease | short | invisible | B | C-11 and C-13 → CR-8c (search time used up) and CR-8b (key money transferred to landlords) | A-1, A-2, A-3 |

## Gaps found

**(a) Calculus gaps.** None. Every step was derived from a core rule. One near-gap: deciding where households displaced or blocked by the cap end up needed arithmetic (counting households and units in use) on top of CR-9, which names the relations but does not say how a reallocation that leaves the number of units in use unchanged nets out across segments.

**(b) New premises.**

- A-N1 (p 0.7): needed to resolve CR-12b for sitting tenants' rent in the medium horizon, because the announcement chain (CR-10a) and the cap chain (CR-1) push in opposite directions and CR-5c bounds the first only by the market rent on the effective date.
- A-N2 (p 0.8): CR-4 (x: accept, y: lobby) gives the direction; that someone is at that margin is empirical, and no case assumption covered it.

**(c) Unclear core rules.**

- CR-12b refers to "a dominance pattern, DM, with its premises stated". In a core-only run there is no pattern; the rule does not say what a dominance premise derived from the core rules must contain. Here it was CR-5c plus arithmetic plus A-N1.
- CR-1 for K3: whether the conversion permit is operation 2 (a route out of the cap) or operation 3 (a burden on conversion) depends on the counterfactual law of conversion, which the record does not state. Both were recorded.
- CR-6, "every margin that is still open": unclear whether each open margin is predicted to be used, or only at least one. Each margin here (search, selection, key money, maintenance) was given its own premise rather than a group consequence.
- CR-7c and CR-10c overlap (both say a durable asset's price reflects expected yields); and "when the change becomes expected" is unclear for a ballot measure that was likely but not certain to pass.
- CR-9 relations: the lease itself (landlord to tenant, maintenance as part of what is bought) is not one of the relation types in 2.8 (substitute, complement, input_to, same_market_other_segment, across_border).
