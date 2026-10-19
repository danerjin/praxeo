# Thin-slice run: Teravel Freedom to Work Act

Rule base: rb-thin-0.7 (handbook catalog 1.4: price ceilings PC-1..PC-7, PC-16, PC-21, RS-2..RS-11, SB-4, OC-2..OC-4; taxes and tariffs TX-1, TX-2, TX-4, TX-7..TX-9, RS-1, RS-5..RS-8, RS-14, RS-15, TS-2, SB-4, OC-2..OC-4; CR-12 totals and the declared comparisons; group signs; announcement windows)  |  Decider: fixture:answers.json  |  Run: 2026-10-19T20:00:28+00:00
Prediction log sha256 (frozen before the outcome card was opened): `00483b5a236ccf9e…`

## Policy record

- Rule-maker: the Teravel legislature; enacted 12 June 2025, effective 1 January 2026.
- Stated aim: none stated
- k1: term_prohibition on non_compete_clauses in teravel_labor; binds employers.restraining, protects None. Source: "Any term of an employment or independent-contractor agreement that prohibits or restricts a worker, after the work relationship ends, from working for another person or carrying on a business, or that imposes a penalty for doing so, is void."
- k2: disclosure_mandate on notice_of_void_term in teravel_labor; binds employers.restraining, protects None. Source: "Every employer that has a non-compete with a current worker, or with a former worker who left after 1 January 2024, must give written notice by 1 March 2026 that the term is void."
- Unclear U1: Does the exemption for "a notice period during which the worker remains employed" cover a notice period of six to twelve months, paid in full, with no duties, during which the worker may not work for anyone else? Readings: U1-a: yes, any paid notice period in which the worker remains employed is preserved / U1-b: no, a notice period long enough to keep the worker out of the field is a restraint "in effect", and is void
- Unclear U2: Is a term that requires a worker who leaves within 24 months to repay employer-paid training a "penalty" for working for another person? Readings: U2-a: yes, it penalizes leaving, and leaving is how one comes to work for another / U2-b: no, it applies to every departure, whatever the worker does next, and only recovers a cost
- Citation check: every quoted source sentence was found in the text.
- Verifier: no problems.

## Assumptions (estimated before scoring)

| Atom | Class | p | Text |
|---|---|---|---|
| `binding(k1)` | binding | 0.80 | The term was in use. |
| `term_valued(k1)` | other | 0.70 | The party that used the term valued its protection. |
| `substitute_terms(k1)` | substitutability | 0.85 | Lawful substitute terms give part of the same protection. |
| `can_organize(k1)` | other | 0.80 | The parties that used the term can organize to lobby. |

## Consequences

| ID | Actor class | Variable | Sign | Horizon | Tier | Rules | Minimal assumption sets | Reported |
|---|---|---|---|---|---|---|---|---|
| C-1 | employers.restraining | asset_value | decrease | short+ | B | CR-8 | {binding(k1)} | yes |
| C-2 | employers.restraining | lobbying_effort | increase | medium+ | B | RS-7 | {binding(k1), can_organize(k1)} | yes |
| C-3 | employers.restraining | term_prevalence | increase | short+ | B | PC-18 | {binding(k1), substitute_terms(k1)} | yes |
| C-4 | officials.enforcement | enforcement_cost | increase | short+ | A | OC-3 | {} | yes |
| C-5 | workers.bound | job_changes | increase | short+ | B | CR-7 | {binding(k1)} | yes |
| C-6 | workers.bound | wage_rate or non_wage_compensation | at_least_one_decrease | medium+ | B | PC-18, CR-6 | {binding(k1), term_valued(k1)} | yes |

## Explanations

- C-1. Compared with no Teravel Freedom to Work Act, asset value for employers.restraining falls from the short run onward (tier B, invisible). Why: CR-8: every payment is a receipt: what one side no longer pays or receives is what the other keeps or loses. This holds if: The term was in use (p = 0.80). Reported.
- C-2. Compared with no Teravel Freedom to Work Act, lobbying effort for employers.restraining rises from the medium run onward (tier B, invisible). Why: RS-7: a gain concentrated on an identifiable group draws its lobbying to keep or extend it. This holds if: The term was in use (p = 0.80); The parties that used the term can organize to lobby (p = 0.80). Reported.
- C-3. Compared with no Teravel Freedom to Work Act, term prevalence for employers.restraining rises from the short run onward (tier B, invisible). Why: PC-18: PC-18. This holds if: The term was in use (p = 0.80); Lawful substitute terms give part of the same protection (p = 0.85). Reported.
- C-4. Compared with no Teravel Freedom to Work Act, enforcement cost for officials.enforcement rises from the short run onward (tier A, invisible). Why: OC-3: the measure must be administered, and a raised budget is paid for by taxpayers. This holds if: no assumption. Reported.
- C-5. Compared with no Teravel Freedom to Work Act, job changes for workers.bound rises from the short run onward (tier B, invisible). Why: CR-7: CR-7. This holds if: The term was in use (p = 0.80). Reported.
- C-6. Compared with no Teravel Freedom to Work Act, wage rate or non wage compensation for workers.bound falls for at least one of them from the medium run onward (tier B, invisible). Why: PC-18: PC-18; CR-6: sellers facing fewer buyers than they planned for cut their price. This holds if: The term was in use (p = 0.80); The party that used the term valued its protection (p = 0.70). Reported.

## Score against the outcome card

No outcome card exists for this case (it is fictional), so the run is not scored.
