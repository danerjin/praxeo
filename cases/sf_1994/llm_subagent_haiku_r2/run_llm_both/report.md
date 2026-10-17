# Thin-slice run: San Francisco Proposition I (November 1994)

Rule base: rb-thin-0.5 (handbook catalog 1.4: PC-1, PC-3, PC-5, PC-7, PC-21, RS-4, RS-5, TX-1, TX-2, TX-7, TX-8, RS-14; CR-12 totals)  |  Decider: fixture:answers_remapped.json  |  Run: 2026-10-17T20:22:43+00:00
Prediction log sha256 (frozen before the outcome card was opened): `c6e57b13dff945c4…`

## Policy record

- Rule-maker: San Francisco voters (ballot measure); enacted 1994-11-08, effective Date of certification, for covered units (the certification date is not stated in the text).
- Stated aim: none stated
- C1: price_ceiling on rental_housing in san_francisco; binds landlords.covered, protects tenants.controlled. Source: "Rental units in owner-occupied buildings of two to four units built before June 1979 become subject to the Rent Ordinance."
- C2: prohibition on rental_housing in san_francisco; binds landlords.covered, protects tenants.controlled. Source: "Rental units in owner-occupied buildings of two to four units built before June 1979 become subject to the Rent Ordinance."
- Unclear U1: The Rent Board hears tenant petitions and landlord applications and may order rent reductions and refunds. Readings: U1-a: The Rent Board's power to order reductions and refunds enforces the rent limit in C1 and adds no separate restriction. / U1-b: The Rent Board's power is a separate operative provision on rent adjudication, which no listed instrument covers.
- Citation check: every quoted source sentence was found in the text.
- Verifier: no problems.

## Assumptions (estimated before scoring)

| Atom | Class | p | Text |
|---|---|---|---|
| `binding(c1)` | binding | 0.70 | The ceiling binds: it is below the price the market would otherwise reach. |
| `enforced(c1)` | enforcement | 0.60 | The ceiling is enforced against most bound sellers. |
| `alternative_uses(c1)` | alternative_uses | 0.65 | Owners can move covered units to uses the ceiling does not reach. |
| `nontransferable(c1)` | other | 0.85 | The protected buyers' right is tied to holding the tenancy and cannot be sold. |
| `buyouts_limited(c1)` | other | 0.70 | Buyouts move fewer tenants than the cap keeps in place. |
| `would_leave(c1)` | mobility | 0.85 | Without the rule some protected buyers would have left the area. |
| `lockin_dominates(c1)` | other | 0.62 | The lock-in outweighs moves diverted out of the area by higher free rents. |
| `keepers_dominate(c1)` | other | 0.63 | Among all protected tenants, the fall in moves out of the area among keepers outweighs the rise among the displaced. |
| `substitutes(c1)` | substitutability | 0.70 | Uncovered units in the same market are close substitutes for covered ones. |

## Consequences

| ID | Actor class | Variable | Sign | Horizon | Tier | Rules | Minimal assumption sets | Reported |
|---|---|---|---|---|---|---|---|---|
| C-1 | landlords.covered | quantity_supplied | decrease | long+ | B | PC-1, PC-5 | {alternative_uses(c1), binding(c1), enforced(c1)} | yes |
| C-2 | landlords.covered | reclassification | increase | long+ | B | PC-1, RS-5 | {alternative_uses(c1), binding(c1), enforced(c1)} | yes |
| C-3 | tenants.controlled | price_paid | decrease | medium+ | B | PC-1, PC-3 | {binding(c1), enforced(c1)} | yes |
| C-4 | tenants.controlled | turnover | decrease | medium+ | B | PC-1, PC-7 | {binding(c1), buyouts_limited(c1), enforced(c1), nontransferable(c1)} | yes |
| C-5 | tenants.controlled.displaced | relocation_out_of_area | increase | long+ | B | PC-1, RS-5, PC-21 | {alternative_uses(c1), binding(c1), enforced(c1), would_leave(c1)} | yes |
| C-6 | tenants.controlled.keepers | relocation_out_of_area | decrease | medium+ | B | PC-1, PC-7, PC-21 | {binding(c1), buyouts_limited(c1), enforced(c1), lockin_dominates(c1), nontransferable(c1), would_leave(c1)} | yes |
| C-7 | tenants.prospective | price_paid | increase | medium+ | B | PC-1, PC-7 | {binding(c1), buyouts_limited(c1), enforced(c1), nontransferable(c1)} | yes |
| C-8 | tenants.prospective | price_substitute | increase | long+ | B | PC-1, PC-3, RS-4 | {binding(c1), enforced(c1), substitutes(c1)} | yes |
| C-9 | tenants.controlled | relocation_out_of_area | decrease | medium+ | B | PC-1, PC-7, PC-21, RS-5; CR-12 total of C-6, C-5 | {alternative_uses(c1), binding(c1), buyouts_limited(c1), enforced(c1), keepers_dominate(c1), lockin_dominates(c1), nontransferable(c1), would_leave(c1)} | yes |

## Explanations

- C-1. Compared with no San Francisco Proposition I (November 1994), quantity supplied for landlords.covered falls in the long run (tier B, invisible). Why: PC-1: a ceiling held below the price the market would reach binds sellers; where new contracts are priced freely, fewer vacancies raise their initial price instead of leaving a shortage; PC-5: owners move resources to uses whose yield the ceiling does not cap. This holds if: Owners can move covered units to uses the ceiling does not reach (p = 0.65); The ceiling binds: it is below the price the market would otherwise reach (p = 0.70); The ceiling is enforced against most bound sellers (p = 0.60). Reported.
- C-2. Compared with no San Francisco Proposition I (November 1994), reclassification for landlords.covered rises in the long run (tier B, invisible). Why: PC-1: a ceiling held below the price the market would reach binds sellers; where new contracts are priced freely, fewer vacancies raise their initial price instead of leaving a shortage; RS-5: owners move units out of the rule's reach. This holds if: Owners can move covered units to uses the ceiling does not reach (p = 0.65); The ceiling binds: it is below the price the market would otherwise reach (p = 0.70); The ceiling is enforced against most bound sellers (p = 0.60). Reported.
- C-3. Compared with no San Francisco Proposition I (November 1994), price paid for tenants.controlled falls from the medium run onward (tier B, visible). Why: PC-1: a ceiling held below the price the market would reach binds sellers; where new contracts are priced freely, fewer vacancies raise their initial price instead of leaving a shortage; PC-3: those who hold a covered unit pay the controlled price, while those shut out look elsewhere. This holds if: The ceiling binds: it is below the price the market would otherwise reach (p = 0.70); The ceiling is enforced against most bound sellers (p = 0.60). Reported.
- C-4. Compared with no San Francisco Proposition I (November 1994), turnover for tenants.controlled falls from the medium run onward (tier B, invisible). Why: PC-1: a ceiling held below the price the market would reach binds sellers; where new contracts are priced freely, fewer vacancies raise their initial price instead of leaving a shortage; PC-7: the benefit is tied to staying put and cannot be sold, so holders move less. This holds if: The ceiling binds: it is below the price the market would otherwise reach (p = 0.70); Buyouts move fewer tenants than the cap keeps in place (p = 0.70); The ceiling is enforced against most bound sellers (p = 0.60); The protected buyers' right is tied to holding the tenancy and cannot be sold (p = 0.85). Reported.
- C-5. Compared with no San Francisco Proposition I (November 1994), relocation out of area for tenants.controlled.displaced rises in the long run (tier B, invisible). Why: PC-1: a ceiling held below the price the market would reach binds sellers; where new contracts are priced freely, fewer vacancies raise their initial price instead of leaving a shortage; RS-5: owners move units out of the rule's reach; PC-21: leaving the area forfeits the benefit, and fewer holders are priced out, so they leave the area less. This holds if: Owners can move covered units to uses the ceiling does not reach (p = 0.65); The ceiling binds: it is below the price the market would otherwise reach (p = 0.70); The ceiling is enforced against most bound sellers (p = 0.60); Without the rule some protected buyers would have left the area (p = 0.85). Reported.
- C-6. Compared with no San Francisco Proposition I (November 1994), relocation out of area for tenants.controlled.keepers falls from the medium run onward (tier B, invisible). Why: PC-1: a ceiling held below the price the market would reach binds sellers; where new contracts are priced freely, fewer vacancies raise their initial price instead of leaving a shortage; PC-7: the benefit is tied to staying put and cannot be sold, so holders move less; PC-21: leaving the area forfeits the benefit, and fewer holders are priced out, so they leave the area less. This holds if: The ceiling binds: it is below the price the market would otherwise reach (p = 0.70); Buyouts move fewer tenants than the cap keeps in place (p = 0.70); The ceiling is enforced against most bound sellers (p = 0.60); The lock-in outweighs moves diverted out of the area by higher free rents (p = 0.62); The protected buyers' right is tied to holding the tenancy and cannot be sold (p = 0.85); Without the rule some protected buyers would have left the area (p = 0.85). Reported.
- C-7. Compared with no San Francisco Proposition I (November 1994), price paid for tenants.prospective rises from the medium run onward (tier B, invisible). Why: PC-1: a ceiling held below the price the market would reach binds sellers; where new contracts are priced freely, fewer vacancies raise their initial price instead of leaving a shortage; PC-7: the benefit is tied to staying put and cannot be sold, so holders move less. This holds if: The ceiling binds: it is below the price the market would otherwise reach (p = 0.70); Buyouts move fewer tenants than the cap keeps in place (p = 0.70); The ceiling is enforced against most bound sellers (p = 0.60); The protected buyers' right is tied to holding the tenancy and cannot be sold (p = 0.85). Reported.
- C-8. Compared with no San Francisco Proposition I (November 1994), price substitute for tenants.prospective rises in the long run (tier B, invisible). Why: PC-1: a ceiling held below the price the market would reach binds sellers; where new contracts are priced freely, fewer vacancies raise their initial price instead of leaving a shortage; PC-3: those who hold a covered unit pay the controlled price, while those shut out look elsewhere; RS-4: shut-out buyers turn to uncovered units, which are close substitutes. This holds if: The ceiling binds: it is below the price the market would otherwise reach (p = 0.70); The ceiling is enforced against most bound sellers (p = 0.60); Uncovered units in the same market are close substitutes for covered ones (p = 0.70). Reported.
- C-9. Compared with no San Francisco Proposition I (November 1994), relocation out of area for tenants.controlled falls from the medium run onward (tier B, invisible). Why: CR-12 total of C-6, C-5 (a dominance premise decides the sign). This holds if: Owners can move covered units to uses the ceiling does not reach (p = 0.65); The ceiling binds: it is below the price the market would otherwise reach (p = 0.70); Buyouts move fewer tenants than the cap keeps in place (p = 0.70); The ceiling is enforced against most bound sellers (p = 0.60); Among all protected tenants, the fall in moves out of the area among keepers outweighs the rise among the displaced (p = 0.63); The lock-in outweighs moves diverted out of the area by higher free rents (p = 0.62); The protected buyers' right is tied to holding the tenancy and cannot be sold (p = 0.85); Without the rule some protected buyers would have left the area (p = 0.85). Reported.

## Score against the outcome card

Card: San Francisco Proposition I (1994). UNVERIFIED: written from memory of Diamond, McQuade and Qian (2019), AER 109(9); the paper could not be fetched from this environment. Every figure must be checked against the paper, and the card checked by a second person, before this case counts.

- **Headline**: precision 1.00, recall 0.60, F1 0.75 (9 predictions; 3 verifiable, 6 unverifiable, 0 ambiguous; matched ['C-4', 'C-7', 'C-9']; false positives []; missed findings ['F-3', 'F-4']).
- **Logic**: precision n/a, recall 0.00, F1 n/a (4 predictions; 0 verifiable, 4 unverifiable, 0 ambiguous; matched []; false positives []; missed findings ['F-1', 'F-2', 'F-3', 'F-4', 'F-5']).
- **Assumption Brier score**: 0.09 over 6 assumption(s) with a recorded status.
- Low-confidence findings on the card: ['F-5'].

## Card findings

| ID | Actor class | Variable | Type | Sign | Horizon | Magnitude | Confidence |
|---|---|---|---|---|---|---|---|
| F-1 | tenants.controlled | turnover | effect | decrease | medium, long | treated tenants roughly 10-20% more likely to remain at their 1994 address | high |
| F-2 | tenants.controlled | relocation_out_of_area | effect | decrease | medium, long | lower displacement from San Francisco | high |
| F-3 | landlords.controlled | quantity_supplied | effect | decrease | long | rental housing supply of treated buildings down about 15% | high |
| F-4 | landlords.controlled | reclassification | effect | increase | long | more conversion to condominiums and tenancies-in-common, sale to owner-occupiers, redevelopment | high |
| F-5 | tenants.prospective | price_paid | effect | increase | long | citywide market rents about 5% higher | low |

Confounders: Dot-com boom of the late 1990s and later technology booms raised demand for housing citywide; Costa-Hawkins Rental Housing Act (state law, 1995); Ellis Act withdrawals and changes to condominium conversion rules over the period
