# WE-025 Housing bill with a rent cap, a vacancy tax and a construction subsidy

Analyst: draft (Handbook 0.3)  |  Rule catalog version: 0.3  |  Status: awaiting expert review

A stylized policy in a fictional city, chosen as the "messy" case: three instruments from three rule families in one bill, each of which changes the options that the others create. The analysis takes each component in turn and then traces the interactions explicitly, labeled I-1 to I-6. It is not modeled on any particular city's legislation. The probabilities are illustrative; the evidence column says what a real analysis would cite.

## 1. Policy record

**Wexmoor Housing Stability and Supply Act.** Wexmoor is a city of about 700,000 people with about 300,000 homes, 55% of them rented. Market rents have risen about 5% a year for several years. The suburbs of Alden County, 20 to 30 minutes away, have no comparable rules. About 12,000 homes (4% of the stock) are not anyone's principal residence for more than six months a year: roughly 5,000 second homes and city apartments of people who live elsewhere, 3,000 short-term rentals, 2,500 units held empty by landlords, and 1,500 estates and renovations. Converting a rental building to separately owned condominiums requires a subdivision permit that takes about nine months.

The bill was introduced on 1 February of Year 1 with a council majority behind it. It passed on 1 May and takes effect on 1 September of Year 1. The vacancy tax is first assessed on occupancy during calendar Year 2. The subsidy applies to units completed from 1 September of Year 1 to 31 August of Year 6. The rent cap has no end date.

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Rent cap | `price_ceiling` | Rent on residential units in buildings of two or more units that were first occupied before 1 September of Year 1 | Landlords of those units | Rent increases for a sitting tenant capped at 3% a year from the rent in force on 1 September. Between tenancies the rent may be reset to any level. Eviction only for cause, including owner move-in, demolition, or withdrawal for conversion with six months' notice and a relocation payment of three months' rent. | Single-family homes; condominium units owned separately; units first occupied on or after 1 September of Year 1, for 15 years from first occupancy. |
| K2 Vacancy tax | `capital_tax` (annual tax on holding an unused unit) | Residential units not occupied as anyone's principal residence for more than six months in a calendar year | Owners | 2% of assessed value a year (about $10,000 for a typical unit). Annual self-declaration; audits using water and electricity records; unpaid tax plus 50% penalty. | Units under an active building permit (up to 24 months); owners in hospital or care; estates, for 12 months after death. Units listed for sale or rent are **not** exempt. |
| K3 Construction subsidy | `per_unit_subsidy` | New rental units completed from 1 September of Year 1 to 31 August of Year 6 that add to the city's housing stock | Developers who claim | $30,000 per unit, paid on completion. The developer records a covenant keeping the unit as a long-term rental (12-month leases to principal residents) for 15 years. No cap on the number of units. | — |
| K4 Funding of K3 | Funding | — | City | K3 is paid first from K2 revenue, held in a Housing Fund; any shortfall comes from the general budget. Unspent K2 revenue stays in the fund for future K3 payments. | — |
| K5 Administration | Enforcement | K1 to K3 | City Housing Department | Rent registry; complaint-driven enforcement of K1 with fines; K2 declarations and audits; K3 claims. Funded from the general budget. | — |

Unclear provisions:
- **U1.** Whether a newly completed unit that is still being leased up counts as vacant under K2. Reading U1-a: not counted (or always leased within six months). Reading U1-b: counted like any other unit. Both readings are analyzed (section 7).
- **U2.** Whether a later council will remove the exemption of new units from K1 before 15 years. The exemption is in the same ordinance and can be amended by a simple majority. Treated as an expectation (A-17).
- **U3.** Whether a unit rented as a short-term rental is "occupied as a principal residence". By the text, no: short-term rentals count as vacant.

## 2. Classification

| Component | Rothbard type | Binding? | Rule families |
|---|---|---|---|
| K1 | Triangular: fixes a term of the exchange between landlords and sitting tenants | Within tenancies, as soon as market rents rise more than 3% a year (A-1). Not at the start of a tenancy, because the rent can be reset. | PC, RS, TS |
| K2 | Binary: a forced payment for holding a unit empty, avoidable by changing its use | Yes for owners who keep units empty or rent them short-term (A-10) | TX, RS |
| K3 | Binary: a transfer from the city to developers, conditional on a 15-year rental covenant | Yes for projects at the margin of being built (A-13) | SB, TS |
| K4 | Binary: links K2 revenue to K3 spending | Yes | SB-1, SB-7 |
| K5 | Binary: funded by taxpayers | Yes | OC-3 |

Because K1 lets rents reset between tenancies, PC-1 (excess demand) does not apply at the start of a tenancy: anyone willing to pay the reset rent can rent a covered unit. The ceiling binds only on sitting tenants, which shapes every K1 consequence below.

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `tenants.covered` | Sitting tenants of covered units | Rent increases capped at 3%; lose the cap if they move. |
| `tenants.prospective` | People looking for a rental | Higher starting rents in covered units; more units from K2 and K3. |
| `landlords.covered` | Owners of covered buildings | Rent growth capped within tenancies; can reset between tenancies; can convert to condominiums; holding units empty is now taxed. |
| `owners.vacant` | Owners of second homes, units held empty, and short-term rentals | Pay 2% a year, or rent long-term, sell, occupy, or find an exemption. |
| `operators.short_term_rental` | Short-term rental operators (a subgroup of `owners.vacant`) | Their use is taxed as vacancy. |
| `guests.short_term` | Visitors who rent short-term | Fewer short-term rentals. |
| `hotels` (`sellers.substitutes`) | Hotels and serviced apartments | Some short-term guests move to them. |
| `developers` (`sellers.prospective`) | Builders of new rental housing | $30,000 per unit; new units exempt from K1, but locked into rental by the covenant. |
| `developers.other` | Builders of condominiums and non-residential projects | Compete with subsidized rental projects for land and labor. |
| `landowners.developable` (`factor_owners.specific`) | Owners of land zoned for apartments | Subsidized developers bid for their land. |
| `homebuyers` | Buyers of condominiums and other owner-occupied homes | More conversions and sales of formerly empty units; fewer new condominiums. |
| `taxpayers`, `officials.enforcement` | General budget and the Housing Department | Fund K3 shortfalls and K5. |

## 4. Direct effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | `tenants.covered` | `price_paid` | decrease | short to long, growing over time | PC-3, TS-3 | A-1, A-2 |
| C-2 | `owners.vacant` who keep units empty | `resources_available_other_uses` | decrease | short | TX-1 | none |
| C-3 | `owners.vacant` | `units_held_vacant` | decrease | short to medium | TX-3, RS-6 | A-10 |
| C-4 | `developers` | `net_price_received` (new rental units, including subsidy) | increase | medium | SB-2 | A-13 |

These are the three intended effects: sitting tenants pay less than they would have (K1), fewer homes sit empty (K2), and building new rentals pays better (K3). C-3 is the direct aim of K2, recorded with `units_held_vacant`. Units offered on the market (C-12) are a related but different quantity: an owner can also end a vacancy by occupying the unit, or by selling it to someone who occupies it.

## 5. Responses

**K1, rent cap**

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-5 | `tenants.prospective` | `price_paid` (starting rents on new tenancies in covered units) | increase | short to medium | RS-2 | A-1, A-3 |
| C-6 | `tenants.covered` | `turnover` | see section 7 | medium | PC-7 vs RS-2 | A-1, A-4, A-6, A-7 |
| C-7 | `landlords.covered` | `maintenance_spending` | decrease | short to medium | PC-4, RS-2 | A-1, A-6 |
| C-8 | `landlords.covered` | `side_payments` (buyouts paid to sitting tenants to leave) | increase | short to medium | RS-2 | A-1, A-7 |
| C-9 | `landlords.covered` | `reclassification` (conversion to separately owned condominiums) | increase | medium | RS-5, PC-5; RS-1 via I-1 | A-1, A-8, A-10 |
| C-10 | `tenants.covered` renewing between 1 February and 1 September | `price_paid` (at renewal before the base date) | increase | short | RS-8 | A-9 |
| C-11 | `tenants.covered` | `informal_activity` (sublets at market rent) | increase | medium | PC-6, RS-3 | A-1, A-18 |

C-5: the starting rent is the one term K1 leaves free. A landlord who expects market rents to outrun the 3% cap sets a higher starting rent to make up for the capped increases to come (RS-2). C-7 and C-8: because rents reset between tenancies, landlords now gain from turnover, so both less maintenance and buyout offers serve to encourage sitting tenants to leave. This is a chain on turnover opposite to PC-7, so C-6 is combined in section 7.

**K2, vacancy tax**

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-12 | `owners.vacant` | `quantity_supplied` (units offered for long-term rent or for sale) | increase | short to medium | RS-6, TX-3 | A-10 |
| C-13 | `owners.vacant` | `reclassification` (building permits taken out to claim the renovation exemption; occupancy arranged on paper) | increase | short to medium | RS-5, TX-4 | A-12 |
| C-14 | `operators.short_term_rental` | `quantity_supplied` (short-stay nights) | decrease | short to medium | TX-2, TX-3 | A-11 |
| C-15 | `owners.vacant` | `compliance_cost` (declarations, records) | increase | short | TX-5 | none |

**K3, construction subsidy**

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-16 | `developers` | `reclassification` (smaller units, to collect more per-unit subsidy per building) | increase | medium | SB-5, RS-5 | A-14 |
| C-17 | `developers` | `quantity_supplied` (new units completed between 1 February and 1 September of Year 1) | decrease | short | RS-8 | A-21 |

C-17: a unit first occupied before 1 September would be covered by K1 and receive no subsidy. Developers close to completion delay their certificates of occupancy past the base date.

**All components**

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-18 | `tenants.covered`, `landlords.covered`, `owners.vacant`, `developers` | `lobbying_effort` (tenants to tighten K1 or end vacancy decontrol; landlords and owners for exemptions; developers to extend K3) | increase | medium | RS-7, SB-5 | A-19 |

Not reported:
- False declarations of occupancy under K2 (RS-3). Water and electricity records make empty units easy to detect; A-22 is below the cut-off (p = 0.35).
- Short-term rental operators moving to Alden County (RS-4). Demand for short stays is tied to the city center; A-23 is below the cut-off (p = 0.35).
- Developers cutting new rental building because they fear the K1 exemption will be withdrawn (TS-2). This rests on the negation of A-17 (p = 0.45); see section 7.

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-19 | `tenants.covered` in converted buildings | `price_paid` (after relocation) | increase | medium | PC-5, RS-5 | covered and exempt units: `same_market_other_segment`, close | A-1, A-8 |
| C-20 | `tenants.covered` | `job_changes` | decrease | medium | RS-11 | covered tenancy and jobs: `complement`, note `location` | A-1, A-4, A-5 |
| C-21 | subtenants (`tenants.prospective` in informal sublets) | `search_cost` | increase | medium | RS-10 | — | A-18 |
| C-22 | `guests.short_term` | `price_paid` (short stays) | increase | short to medium | TX-2 | — | A-11 |
| C-23 | `hotels` | `quantity_traded` | increase | short to medium | RS-1 | short-term rentals and hotels: `substitute`, close | A-11 |
| C-24 | `landowners.developable` | `asset_value` (land zoned for apartments) | increase | medium | SB-4 | land: `input_to` new rental units, close | A-13, A-15 |
| C-25 | `developers.other` | `quantity_substitute` (new condominiums and other projects) | decrease | medium | SB-3 | rental and condominium building: compete for land and labor | A-13, A-16 |
| C-26 | `owners.vacant` | `asset_value` (units whose best use was to stay empty or short-term) | decrease | short | SB-4 | — | A-10, A-24, A-25 |
| C-27 | `landlords.covered` | `asset_value` (covered buildings with sitting tenants) | decrease | short to medium | SB-4 | — | A-1, A-24, A-25 |
| C-28 | `officials.enforcement` | `tax_revenue_vs_static_projection` (K2) | decrease | medium | TX-9 | — | A-10 |

C-22 and C-23 are at depth 3 (tax → fewer short-term rentals → guests pay more or switch to hotels), and the chains stop there. Effects on Alden County rents are also at depth 3; their direction would follow the ambiguous city rent effect in section 7 (C-31), and they reach a diffuse group, so they are not traced.

C-26 and C-27: a lasting tax on holding a unit empty, and a lasting cap on the rent from sitting tenants, both lower the expected net return of the asset, and so the price a buyer would pay for it, from the time they are expected (SB-4, which in catalog 0.3 covers losses). Both rest on the policies being expected to last (A-24) and on the housing stock growing slowly (A-25). For C-26 the fall is limited by the unit's value in its next-best use (long-term rental, sale to an occupier); for C-27 it is limited by vacancy decontrol, which lets the rent reset at each turnover.

Second-order checks:
- **RS-9 (bundled trips).** No one changes where they buy housing in a way that carries other purchases along. Not applicable.
- **RS-10 (informal trade).** Applies to illegal sublets by sitting tenants (C-11, C-21). Buyouts (C-8) are legal and are not informal trade.
- **RS-11 (lock-in).** Applies: sitting tenants lose the capped rent if they move (C-20).

### Interactions between components

The components were classified separately (step 2), but each changes the alternatives open under the others. These chains are the reason the bill must be analyzed as a whole.

For each pair of components (workflow step 6): K1 and K2 interact through I-1 and I-2; K1 and K3 through I-3; K2 and K3 through I-4, I-5 and I-6 (K4 is the funding link). The components each chain runs through are recorded in the consequence list.

- **I-1 (K1, K2). K2 closes one exit from K1 and widens others.** Without K2, a landlord who found the cap too costly could let a unit stay empty at the next turnover and hold it for sale with vacant possession or for later conversion. K2 taxes that after six months. The landlord's other exits are still open: re-let at a reset rent (possible because K1 has vacancy decontrol), sell within six months, or convert, which the renovation-permit exemption shelters from K2 for up to 24 months. When one means becomes costlier, the alternatives are used more (RS-1). So K2 adds a chain to C-9 (more conversion) and a chain to C-29 (more re-letting), in opposite directions on covered rental supply.
- **I-2 (K1, K2). K1 weakens K2's push into long-term renting.** An owner of an empty or short-term unit in an existing multi-unit building who now rents it long-term brings it under K1. Renting is therefore less attractive than it would be under K2 alone, and selling more attractive. Separately owned condominium units are exempt from K1, so their owners face no such deterrent. This changes the mix within C-12 (more sales, fewer rentals), not its sign.
- **I-3 (K1, K3). K3 offsets K1 for new construction only if the exemption is trusted.** New units are exempt from K1 for 15 years, and K3 requires them to stay rentals for 15 years. If developers expect a later council to bring new units under the cap (U2), the covenant removes their usual exit (conversion or sale), so the subsidy comes with greater exposure to the cap. See section 7.
- **I-4 (K2, K3). K2 may tax K3's own output.** Under reading U1-b, newly completed units that take more than six months to lease up are taxed as vacant, a cost on exactly the construction K3 subsidizes.
- **I-5 (K2, K3, K4). Earmark fungibility.** K3's spending is fixed by the number of units completed, at $30,000 each, whatever K2 raises. K2 revenue only changes how much of K3 the general budget pays. Up to the cost of K3, each dollar of K2 revenue reduces the general budget's share by a dollar: the earmark is fully fungible (SB-7, in its limiting case). K2 revenue above K3's cost stays in the Housing Fund and does not return to the general budget.
- **I-6 (K2, K3, K4). K2's success shrinks the funding of K3.** As empty units are rented, sold or occupied (C-12), K2's base shrinks and revenue falls short of a projection at the current vacancy level (C-28), so the general budget pays a larger share of K3 over time (C-34).

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `tenants.covered`, `turnover`, medium | Landlords, who now gain from each turnover, offer buyouts (C-8) and cut maintenance (C-7) to encourage sitting tenants to leave (RS-2). | Sitting tenants lose the capped rent if they move, so they move less (PC-7). | None | **ambiguous** (C-6). Buyouts let some tenants sell back part of the value of the cap, so the − chain is weaker than under a cap without vacancy decontrol; whether they restore turnover to the level it would have had cannot be decided by the method. |
| `landlords.covered`, `reclassification` (conversion), medium | K1 lowers the return on renting to sitting tenants (RS-5, PC-5). I-1: K2 closes the "hold empty" exit, and the renovation exemption shelters conversion (RS-1). | — | None needed | **increase** (C-9). |
| `landlords.covered`, `quantity_supplied` (covered rental units), medium | I-1: empty covered units are re-let to avoid K2 (RS-6, TX-3). | K1: conversion and withdrawal (PC-5, RS-5); I-1: K2 makes conversion the more attractive exit, speeding it (RS-1). | None | **ambiguous** (C-29). Decided by how many covered units were being held empty (about 2,500) compared with how many convert. In the short run, before conversion permits come through, the + chain acts first. |
| `developers`, `investment_target` (new rental units), medium | K3 subsidy (SB-2, C-4). K1 spillover: covered units converted (C-9) and starting rents in covered units raised (C-5) push tenants toward exempt units (RS-1, PC-5), so new units can earn more; rests on A-17 (p = 0.55). PC-8 in its usual form does not apply, because K1 creates no excess demand at the start of a tenancy (section 2). | Fear that the K1 exemption will be removed, made worse by the covenant (TS-2, I-3): rests on the negation of A-17 (p = 0.45), not reported. Under reading U1-b only: K2 on units in lease-up (I-4, A-20). | None | **Reading U1-a: increase.** **Reading U1-b: ambiguous** (C-30; one sign per reading, with no probability on the readings). The sign also turns on A-17: if developers' trust in the exemption fell below 0.5, the fear chain would be reported and the sign would be ambiguous under both readings. |
| `tenants.prospective`, `price_substitute` (rents in exempt units: new buildings, condominiums, houses), medium | K1 spillover: covered units converted or withdrawn (C-9; PC-5, RS-5), and starting rents in covered units raised (C-5), push tenants toward exempt units (RS-1). | Added supply in the rental market (RS-13): K2's empty and short-term units offered for rent (C-12); K3's new subsidized rental units (C-4). | None | **ambiguous** (C-31). The same chains decide the total cost of renting for newcomers: higher starting rents in covered units (C-5) push it up; more units from K2 and K3 push it down. |
| `homebuyers`, `price_substitute` (condominiums), medium | Builders and land moved from condominium to subsidized rental projects (SB-3, C-25). | Conversions (C-9) and sales of formerly empty units (C-12, I-2) add condominiums for sale (RS-13). | None | **ambiguous** (C-32). |
| `tenants.covered`, `quality_adjusted_price`, medium | Less maintenance, used partly to encourage turnover (C-7). | Lower rent (C-1). | None | **ambiguous** (C-33). |
| `taxpayers`, `resources_available_other_uses`, medium | — | General budget pays K5 (OC-3) and any part of K3 that K2 revenue does not cover (SB-1, OC-1); that part grows as K2 revenue falls (I-6, C-28). | None needed | **decrease** (C-34). Compared with no bill, the general budget never gains: K2 revenue only reduces its share of K3 (I-5), and any K2 surplus stays in the Housing Fund. How large the decrease is depends on K2 revenue against K3 spending, which the method cannot measure. |

## 8. Time structure

- **Announcement (February to September of Year 1).** The cap's base is the rent on 1 September, so landlords raise rents at renewals before then (C-10). Developers delay completions until after the base date, to be exempt from K1 and eligible for K3 (C-17).
- **First year.** K2 is assessed on Year 2 occupancy, so owners of empty units must have them occupied, sold or under a building permit by about mid-Year 2 (C-12, C-13). Short-term rental supply falls and short-stay prices rise in Year 2 (C-14, C-22). Starting rents in covered units rise at once (C-5).
- **Medium term.** The cap tightens every year market rents rise faster than 3% (TS-3), so the gap between sitting tenants' rents and starting rents grows, and with it the landlord's gain from turnover (C-7, C-8), tenants' reluctance to move (C-20), set against the landlords' push to end tenancies (C-6) and the pull toward conversion (C-9). Conversions arrive after the nine-month permit, and the 24-month renovation exemption lets landlords hold units empty while converting (I-1). Subsidized units arrive from Year 3 onward, given planning and building times.
- **Subsidy deadline.** Completions are rushed to beat 31 August of Year 6 (RS-8), followed by a dip.
- **Long term.** Covered buildings last for decades; reduced maintenance and conversion compound slowly (TS-1). Subsidized units carry a 15-year covenant and a 15-year exemption that end together; what developers expect to happen then (U2) affects how much they invest now (TS-2).
- **Funding over time.** K3 payments begin as soon as subsidized units complete, but the first K2 revenue arrives only in Year 3, so the general budget pays the early subsidies (C-35). Later, K2 revenue falls as the vacancy base shrinks (I-6).

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-35 | `taxpayers` | `resources_available_other_uses` | decrease | Short horizon: K3 payments made before any K2 revenue arrives, and K5's administration. (Medium horizon: C-34.) | SB-1, OC-1, OC-3 |
| C-36 | `officials.enforcement` | `enforcement_cost` | increase | Rent registry, vacancy audits, subsidy claims. | OC-3 |
| C-37 | `guests.short_term`, `operators.short_term_rental` | `quantity_traded` (short stays) | decrease | Stays that would have been booked and are not; both sides lose the gain each expected. | OC-4 |

Payments of K2 by owners who keep units empty are C-2; their declarations are C-15. Rentals that are not made because covered units are converted are not entered separately here: they are one of the two chains in C-29, whose combined sign is ambiguous.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | Market rents keep rising faster than 3% a year, so the cap binds within tenancies. | binding | 0.85 | Rent trend; vacancy rate; pipeline of new supply. | Most K1 consequences weaken or vanish. |
| A-2 | The rent registry enforces the cap against most landlords. | enforcement | 0.75 | Registry budget; complaint volumes; size of fines. | C-1 shrinks. |
| A-3 | Landlords raise starting rents in anticipation of capped increases. | expectations | 0.75 | Starting rents in covered and exempt units after enactment; landlord surveys. | C-5 not reported. |
| A-4 | Sitting tenants lose the capped rent if they move; tenancies cannot be transferred. | other | 0.95 | Ordinance text. | C-6, C-20 weaken. |
| A-5 | Some job opportunities for sitting tenants require moving or a much longer commute. | mobility | 0.7 | Size of the region; job locations. | C-20 not reported. |
| A-6 | Housing codes leave room to reduce maintenance. | other | 0.8 | Habitability code; inspection frequency. | C-7 not reported. |
| A-7 | Landlords offer buyouts where the rent gap is large. | other | 0.6 | Buyout disclosures where they are required; tenant surveys. | C-8 not reported; the + chain of C-6 weakens. |
| A-8 | The conversion route is usable for many buildings. | alternative_uses | 0.7 | Subdivision permit approvals; relocation costs; condominium demand. | C-9, C-19 weaken; − chain of C-29 weakens. |
| A-9 | Enough leases renew before 1 September, and landlords can raise rents at renewal. | expectations | 0.7 | Share of leases renewing in the window. | C-10 not reported. |
| A-10 | Many owners of empty units prefer to rent, sell or occupy them rather than pay 2% a year. | alternative_uses | 0.75 | Vacancy reasons by type (second homes, short-term, landlord-held); sale and rental demand. | C-3, C-12, C-28 weaken; K2 becomes mainly a revenue tax. |
| A-11 | Short-term rental is less profitable than other uses after the tax, and guests have hotel alternatives. | alternative_uses | 0.7 | Short-term rental revenue per unit against $10,000 tax; hotel occupancy. | C-14, C-22, C-23, C-37 not reported. |
| A-12 | Owners can use building permits or occupancy arrangements to fall into exemptions. | other | 0.65 | Permit requirements; audit design. | C-13 not reported. |
| A-13 | The subsidy is large relative to developers' margins, and land and approvals are available. | alternative_uses | 0.75 | Development cost per unit; approval rates; zoned capacity. | C-4, C-24, C-25 and the K3 chain of C-30 weaken. |
| A-14 | The per-unit subsidy makes smaller units more attractive, and zoning allows them. | other | 0.7 | Minimum unit sizes; unit-mix data. | C-16 not reported. |
| A-15 | Land zoned for apartments is scarce. | other | 0.75 | Zoned capacity; land prices. | C-24 weakens. |
| A-16 | Construction land and labor are scarce and in use elsewhere. | other | 0.8 | Construction employment; project pipeline. | C-25 and the + chain of C-32 fail. |
| A-17 | Developers expect new units to stay exempt from K1 for the full 15 years. | expectations | 0.55 | Whether the exemption is in the charter or an ordinance; council politics; history of extending controls. | The fear chain in C-30 becomes reported; C-30 becomes ambiguous under both readings. |
| A-18 | Some sitting tenants sublet at market rent without being caught. | enforcement | 0.6 | Lease terms; complaint-driven enforcement. | C-11, C-21 not reported. |
| A-19 | Tenants, landlords, owners and developers can organize to lobby. | other | 0.85 | Existing associations. | C-18 weakens. |
| A-20 | Under reading U1-b, some newly completed units stay unleased for more than six months. | other | 0.8 | Lease-up times for new buildings. | The K2 chain of C-30 fails; C-30 is an increase under both readings. |
| A-21 | Developers can time certificates of occupancy around 1 September. | expectations | 0.8 | Completion schedules; inspection process. | C-17 not reported. |
| A-22 | Owners make false occupancy declarations on a meaningful scale. | enforcement | 0.35 | Utility-record audits; penalties. | Below cut-off; not reported. |
| A-23 | Short-term rental operators move to Alden County on a meaningful scale. | mobility | 0.35 | Location of short-stay demand. | Below cut-off; not reported. |
| A-24 | Owners and buyers expect K1 and K2 to stay in force for many years. | expectations | 0.75 | Neither has an end date; council majority; history of rent rules in the region once enacted. | C-26, C-27 shrink. |
| A-25 | The housing stock grows slowly relative to its size, so existing units are in slowly expandable supply. | durability | 0.9 | Completions against the stock of 300,000; permit and building times. | C-26, C-27 weaken. |

## 11. Report

**The policy.** Wexmoor caps rent increases for sitting tenants in existing multi-unit buildings at 3% a year, while letting rents reset between tenancies. It taxes homes that are no one's principal residence for more than six months a year at 2% of their value. It pays developers $30,000 for each new rental unit kept as a long-term rental for 15 years, from the vacancy tax first and the general budget for the rest.

**Visible consequences.** Sitting tenants pay less than they would have, and the gap grows each year (C-1). Owners who keep homes empty pay the tax (C-2), and fewer homes sit empty (C-3). Building new rentals pays better (C-4).

**Invisible consequences.**
- *People looking for a rental* face higher starting rents in covered buildings, as landlords make up in advance for capped increases (C-5). Those who sublet from sitting tenants search harder and have no recourse (C-21).
- *Sitting tenants* turn down jobs that would require a move (C-20), receive less maintenance and buyout offers to leave (C-7, C-8), and some sublet illegally (C-11). Those who renewed just before the base date paid more (C-10). Those in buildings that are converted lose their tenancy and pay more afterwards (C-19).
- *Landlords* convert more buildings to condominiums (C-9), more so because the vacancy tax closes the alternative of holding units empty while the renovation exemption shelters conversion (I-1). Covered buildings lose value from the time the bill is expected (C-27).
- *Owners of empty homes and short-term rentals* offer them for rent or sale (C-12), more often for sale because renting long-term would bring them under the cap (I-2); some take out permits or arrange occupancy to qualify for exemptions (C-13). Units whose best use was to stay empty or be let short-term lose value (C-26).
- *Visitors* pay more for short stays, and hotels gain business (C-14, C-22, C-23, C-37).
- *Developers* design smaller units (C-16) and delay completions past the base date (C-17). Owners of apartment land gain (C-24); condominium and other projects lose land and labor to subsidized rentals (C-25).
- *The city* collects less vacancy tax than a projection at today's vacancy level, because the tax works (C-28). The earmark does not change how much is spent on the subsidy (I-5). Taxpayers fund the early subsidies and the administration (C-35, C-36), and over the medium term any part of the subsidy that vacancy-tax revenue does not cover (C-34); compared with no bill, the general budget does not come out ahead.
- All affected groups lobby (C-18).

**Ambiguous effects.** Whether sitting tenants move less overall, given that landlords pay and press them to leave (C-6). Whether the stock of covered rental units is larger or smaller (empty units re-let against conversions) (C-29). Whether new rental building rises, which depends on whether units in lease-up are taxed as vacant (C-30). Whether rents in exempt units, and the total cost of renting for newcomers, rise or fall (C-31). Whether condominium prices rise or fall (C-32). Whether sitting tenants get more housing per dollar (C-33).

**Key conditions.** That market rents outrun the cap (A-1, p = 0.85). That empty-unit owners have uses they prefer to paying the tax (A-10, p = 0.75); otherwise K2 mainly raises revenue. That developers trust the exemption of new units (A-17, p = 0.55): this is the closest call in the analysis, and if it fell below 0.5, new rental building would become ambiguous under both readings of the lease-up provision. Clarifying U1 would settle one of the ambiguous signs.

**What this analysis cannot say.** How large any effect is; whether the bill as a whole adds or removes rental housing; whether gains to sitting tenants and developers outweigh costs to newcomers, empty-unit owners, visitors and taxpayers; whether the bill is desirable.

## Consequence list (normal form)

The last column is the `components` field (2.5): the components each chain runs through, with the interaction (I-n) where there is one.

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions | Components |
|---|---|---|---|---|---|---|---|---|---|
| C-1 | tenants.covered | price_paid | decrease | short–long | visible | B | PC-3, TS-3 | A-1, A-2 | K1 |
| C-2 | owners.vacant (keeping units empty) | resources_available_other_uses | decrease | short | visible | A | TX-1 | none | K2 |
| C-3 | owners.vacant | units_held_vacant | decrease | short–medium | visible | B | TX-3, RS-6 | A-10 | K2 |
| C-4 | developers | net_price_received (new rental) | increase | medium | visible | B | SB-2 | A-13 | K3 |
| C-5 | tenants.prospective | price_paid (starting rents, covered units) | increase | short–medium | invisible | B | RS-2 | A-1, A-3 | K1 |
| C-6 | tenants.covered | turnover | ambiguous | medium | invisible | B | PC-7 vs RS-2 (C-7, C-8) | A-1, A-4, A-6, A-7 | K1 |
| C-7 | landlords.covered | maintenance_spending | decrease | short–medium | invisible | B | PC-4, RS-2 | A-1, A-6 | K1 |
| C-8 | landlords.covered | side_payments (buyouts) | increase | short–medium | invisible | B | RS-2 | A-1, A-7 | K1 |
| C-9 | landlords.covered | reclassification (conversion) | increase | medium | invisible | B | RS-5, PC-5, RS-1 (I-1) | A-1, A-8, A-10 | K1, K2 (I-1) |
| C-10 | tenants.covered (renewing before base date) | price_paid | increase | short | invisible | B | RS-8 | A-9 | K1 |
| C-11 | tenants.covered | informal_activity (sublets) | increase | medium | invisible | B | PC-6, RS-3 | A-1, A-18 | K1 |
| C-12 | owners.vacant | quantity_supplied (offered for rent or sale) | increase | short–medium | invisible | B | RS-6, TX-3 | A-10 | K2; mix shaped by K1 (I-2) |
| C-13 | owners.vacant | reclassification (exemption claims) | increase | short–medium | invisible | B | RS-5, TX-4 | A-12 | K2 |
| C-14 | operators.short_term_rental | quantity_supplied (short-stay nights) | decrease | short–medium | invisible | B | TX-2, TX-3 | A-11 | K2 |
| C-15 | owners.vacant | compliance_cost | increase | short | invisible | A | TX-5 | none | K2 |
| C-16 | developers | reclassification (smaller units) | increase | medium | invisible | B | SB-5, RS-5 | A-14 | K3 |
| C-17 | developers | quantity_supplied (completions, February to August of Year 1) | decrease | short | invisible | B | RS-8 | A-21 | K1, K3 |
| C-18 | tenants, landlords, owners, developers | lobbying_effort | increase | medium | invisible | B | RS-7, SB-5 | A-19 | K1, K2, K3 |
| C-19 | tenants.covered (converted buildings) | price_paid (after relocation) | increase | medium | invisible | B | PC-5, RS-5 | A-1, A-8 | K1 |
| C-20 | tenants.covered | job_changes | decrease | medium | invisible | B | PC-7, RS-11 | A-1, A-4, A-5 | K1 |
| C-21 | subtenants | search_cost | increase | medium | invisible | B | RS-3, RS-10 | A-18 | K1 |
| C-22 | guests.short_term | price_paid (short stays) | increase | short–medium | invisible | B | TX-2 | A-11 | K2 |
| C-23 | hotels | quantity_traded | increase | short–medium | invisible | B | RS-1 | A-11 | K2 |
| C-24 | landowners.developable | asset_value | increase | medium | invisible | B | SB-4 | A-13, A-15 | K3 |
| C-25 | developers.other | quantity_substitute (condominium and other projects) | decrease | medium | invisible | B | SB-3 | A-13, A-16 | K3 |
| C-26 | owners.vacant | asset_value | decrease | short | invisible | B | SB-4 | A-10, A-24, A-25 | K2 |
| C-27 | landlords.covered | asset_value | decrease | short–medium | invisible | B | SB-4 | A-1, A-24, A-25 | K1; K2 (I-1) |
| C-28 | officials.enforcement | tax_revenue_vs_static_projection (K2) | decrease | medium | invisible | B | TX-9 | A-10 | K2 |
| C-29 | landlords.covered | quantity_supplied (covered rental units) | ambiguous | medium | invisible | B | RS-6, TX-3 (I-1) vs PC-5, RS-5, RS-1 | A-1, A-8, A-10 | K1, K2 (I-1) |
| C-30 | developers | investment_target (new rental) | U1-a: increase; U1-b: ambiguous | medium | invisible | B | SB-2, RS-1, PC-5 vs TX-2 (I-4) | A-13, A-17, A-20 | K1, K2, K3 (I-3, I-4) |
| C-31 | tenants.prospective | price_substitute (rents in exempt units) | ambiguous | medium | invisible | B | RS-1, PC-5 vs RS-13 | A-1, A-3, A-8, A-10, A-13 | K1, K2, K3 |
| C-32 | homebuyers | price_substitute (condominiums) | ambiguous | medium | invisible | B | SB-3 vs RS-5, RS-6, RS-13 | A-8, A-10, A-16 | K1, K2, K3 (I-2) |
| C-33 | tenants.covered | quality_adjusted_price | ambiguous | medium | invisible | B | C-1 vs C-7 | A-1, A-6 | K1 |
| C-34 | taxpayers | resources_available_other_uses | decrease | medium | invisible | A | SB-1, OC-1, OC-3; SB-7 (size only) | none | K2, K3, K4, K5 (I-5, I-6) |
| C-35 | taxpayers | resources_available_other_uses | decrease | short | invisible | A | SB-1, OC-1, OC-3 | none | K3, K4, K5 |
| C-36 | officials.enforcement | enforcement_cost | increase | short | invisible | A | OC-3 | none | K5 |
| C-37 | guests.short_term, operators.short_term_rental | quantity_traded (short stays) | decrease | short–medium | invisible | B | OC-4 | A-11 | K2 |

## Gaps found

- GAP-025-1 (closed in catalog 0.3: SB-4 generalized to lasting changes that lower returns). C-26 and C-27 now Tier B, with A-24 and A-25.
- GAP-025-2 (closed in catalog 0.3: pairwise check in workflow step 6; `components` field in 2.5). The interactions are labeled with their components (I-1 to I-6), and the consequence list carries a components column.
- GAP-025-3 (closed in catalog 0.3: `reading` field in 2.5; readings get no probability, step 10). C-30 now records one sign per reading ("U1-a: increase; U1-b: ambiguous") and is Tier B.
- GAP-025-4 (closed in catalog 0.3: `units_held_vacant`). C-3 now Tier B.
