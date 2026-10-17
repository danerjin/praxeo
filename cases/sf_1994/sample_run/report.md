# Thin-slice run: San Francisco Proposition I (1994)

Rule base: rb-thin-0.3 (handbook catalog 1.4: PC-1, PC-3, PC-5, PC-7, PC-21, RS-5)  |  Decider: fixture:answers.json  |  Run: 2026-10-17T16:36:09+00:00
Prediction log sha256 (frozen before the outcome card was opened): `d026b07b069e92fe…`

## Policy record

- Rule-maker: voters of San Francisco (ballot measure); enacted 1994-11-08, effective 1994-12 (certification of the election).
- Stated aim: protect tenants of small multi-unit buildings from large rent increases and evictions
- c1: price_ceiling on rental_housing_small_multiunit_pre1979 in san_francisco; binds landlords.controlled, protects tenants.controlled. Source: "Rental units in owner-occupied buildings of two to four units built before June 1979 become subject to the Rent Ordinance."
- Unclear U1: The summary does not say whether the rent on the effective date is rolled back to an earlier base date. Readings: U1-a: the base rent is the rent on the effective date / U1-b: the base rent is rolled back to an earlier date, cancelling increases made in the announcement window
- Citation check: every quoted source sentence was found in the text.

## Assumptions (estimated before scoring)

| Atom | Class | p | Text |
|---|---|---|---|
| `binding(c1)` | binding | 0.75 | The ceiling binds: it is below the price the market would otherwise reach. |
| `enforced(c1)` | enforcement | 0.85 | The ceiling is enforced against most bound sellers. |
| `alternative_uses(c1)` | alternative_uses | 0.70 | Owners can move covered units to uses the ceiling does not reach. |
| `nontransferable(c1)` | other | 0.95 | The protected buyers' right is tied to holding the tenancy and cannot be sold. |
| `buyouts_limited(c1)` | other | 0.70 | Buyouts move fewer tenants than the cap keeps in place. |
| `would_leave(c1)` | mobility | 0.85 | Without the rule some protected buyers would have left the area, and the benefit does not follow them. |
| `lockin_dominates(c1)` | other | 0.65 | The lock-in outweighs moves diverted out of the area by higher free rents. |
| `substitutes(c1)` | substitutability | 0.80 | Uncovered units in the same market are close substitutes for covered ones. |

## Consequences

| ID | Actor class | Variable | Sign | Horizon | Tier | Rules | Minimal assumption sets | Reported |
|---|---|---|---|---|---|---|---|---|
| C-1 | tenants.prospective | excess_demand | increase | short+ | B | PC-1 | {binding(c1), enforced(c1)} | yes |
| C-2 | tenants.controlled | price_paid | decrease | medium+ | B | PC-1, PC-3 | {binding(c1), enforced(c1)} | yes |
| C-3 | tenants.prospective | price_paid | increase | long+ | B | PC-1, PC-3, RS-4 | {binding(c1), enforced(c1), substitutes(c1)} | yes |
| C-4 | landlords.controlled | reclassification | increase | long+ | B | PC-1, RS-5 | {alternative_uses(c1), binding(c1), enforced(c1)} | yes |
| C-5 | tenants.controlled | relocation_out_of_area | decrease | medium+ | B | PC-1, PC-7, PC-21 | {binding(c1), buyouts_limited(c1), enforced(c1), lockin_dominates(c1), nontransferable(c1), would_leave(c1)} | yes |
| C-6 | landlords.controlled | quantity_supplied | decrease | long+ | B | PC-1, PC-5 | {alternative_uses(c1), binding(c1), enforced(c1)} | yes |
| C-7 | tenants.controlled | turnover | decrease | medium+ | B | PC-1, PC-7 | {binding(c1), buyouts_limited(c1), enforced(c1), nontransferable(c1)} | yes |

## Explanations

- C-1. Compared with no San Francisco Proposition I (1994), excess demand for tenants.prospective rises from the short run onward (tier B, invisible). Why: PC-1: a ceiling held below the price the market would reach leaves more buyers wanting units than sellers offer. This holds if: The ceiling binds: it is below the price the market would otherwise reach (p = 0.75); The ceiling is enforced against most bound sellers (p = 0.85). Reported.
- C-2. Compared with no San Francisco Proposition I (1994), price paid for tenants.controlled falls from the medium run onward (tier B, visible). Why: PC-1: a ceiling held below the price the market would reach leaves more buyers wanting units than sellers offer; PC-3: those who hold a covered unit pay the controlled price, while those shut out look elsewhere. This holds if: The ceiling binds: it is below the price the market would otherwise reach (p = 0.75); The ceiling is enforced against most bound sellers (p = 0.85). Reported.
- C-3. Compared with no San Francisco Proposition I (1994), price paid for tenants.prospective rises in the long run (tier B, invisible). Why: PC-1: a ceiling held below the price the market would reach leaves more buyers wanting units than sellers offer; PC-3: those who hold a covered unit pay the controlled price, while those shut out look elsewhere; RS-4: shut-out buyers turn to uncovered units, which are close substitutes. This holds if: The ceiling binds: it is below the price the market would otherwise reach (p = 0.75); The ceiling is enforced against most bound sellers (p = 0.85); Uncovered units in the same market are close substitutes for covered ones (p = 0.80). Reported.
- C-4. Compared with no San Francisco Proposition I (1994), reclassification for landlords.controlled rises in the long run (tier B, invisible). Why: PC-1: a ceiling held below the price the market would reach leaves more buyers wanting units than sellers offer; RS-5: owners move units out of the rule's reach. This holds if: Owners can move covered units to uses the ceiling does not reach (p = 0.70); The ceiling binds: it is below the price the market would otherwise reach (p = 0.75); The ceiling is enforced against most bound sellers (p = 0.85). Reported.
- C-5. Compared with no San Francisco Proposition I (1994), relocation out of area for tenants.controlled falls from the medium run onward (tier B, invisible). Why: PC-1: a ceiling held below the price the market would reach leaves more buyers wanting units than sellers offer; PC-7: the benefit is tied to staying put and cannot be sold, so holders move less; PC-21: leaving the area forfeits the benefit, and fewer holders are priced out, so they leave the area less. This holds if: The ceiling binds: it is below the price the market would otherwise reach (p = 0.75); Buyouts move fewer tenants than the cap keeps in place (p = 0.70); The ceiling is enforced against most bound sellers (p = 0.85); The lock-in outweighs moves diverted out of the area by higher free rents (p = 0.65); The protected buyers' right is tied to holding the tenancy and cannot be sold (p = 0.95); Without the rule some protected buyers would have left the area, and the benefit does not follow them (p = 0.85). Reported.
- C-6. Compared with no San Francisco Proposition I (1994), quantity supplied for landlords.controlled falls in the long run (tier B, invisible). Why: PC-1: a ceiling held below the price the market would reach leaves more buyers wanting units than sellers offer; PC-5: owners move resources to uses whose yield the ceiling does not cap. This holds if: Owners can move covered units to uses the ceiling does not reach (p = 0.70); The ceiling binds: it is below the price the market would otherwise reach (p = 0.75); The ceiling is enforced against most bound sellers (p = 0.85). Reported.
- C-7. Compared with no San Francisco Proposition I (1994), turnover for tenants.controlled falls from the medium run onward (tier B, invisible). Why: PC-1: a ceiling held below the price the market would reach leaves more buyers wanting units than sellers offer; PC-7: the benefit is tied to staying put and cannot be sold, so holders move less. This holds if: The ceiling binds: it is below the price the market would otherwise reach (p = 0.75); Buyouts move fewer tenants than the cap keeps in place (p = 0.70); The ceiling is enforced against most bound sellers (p = 0.85); The protected buyers' right is tied to holding the tenancy and cannot be sold (p = 0.95). Reported.

## Score against the outcome card

Card: San Francisco Proposition I (1994). UNVERIFIED: written from memory of Diamond, McQuade and Qian (2019), AER 109(9); the paper could not be fetched from this environment. Every figure must be checked against the paper, and the card checked by a second person, before this case counts.

- **Headline**: precision 1.00, recall 1.00, F1 1.00 (7 predictions; 5 verifiable, 2 unverifiable, 0 ambiguous; matched ['C-3', 'C-4', 'C-5', 'C-6', 'C-7']; false positives []; missed findings []).
- **Logic**: precision 1.00, recall 0.40, F1 0.57 (4 predictions; 2 verifiable, 2 unverifiable, 0 ambiguous; matched ['C-4', 'C-6']; false positives []; missed findings ['F-1', 'F-2', 'F-5']).
- **Assumption Brier score**: 0.04 over 5 assumption(s) with a recorded status.
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
