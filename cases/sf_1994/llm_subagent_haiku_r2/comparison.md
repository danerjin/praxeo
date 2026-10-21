# LLM stages against fixtures: sf_1994

LLM outputs from `/tmp/claude-0/-home-user-praxeo/6d563eb7-45da-5432-b932-3230b691929b/scratchpad/llmsub2/sf_1994`. The fixtures are hand-written; the LLM worked only from the policy text and the stage instructions.

## Parser

- Valid record: yes. Components: 2 (fixture 1). Unclear provisions: 1 (fixture 1).
- Citation check: every quoted sentence found in the text.
- Component 1 `instrument`: fixture `price_ceiling`, LLM `price_ceiling` (same)
- Component 1 `bound_actor`: fixture `landlords.controlled`, LLM `landlords.covered` (DIFFERS)
- Component 1 `protected_actor`: fixture `tenants.controlled`, LLM `tenants.controlled` (same)
- Component 1 `excluded_actor`: fixture `tenants.prospective`, LLM `tenants.prospective` (same)
- Component 1 `vacancy_decontrol`: fixture `True`, LLM `True` (same)
- Component 1 `buyer_actor`: fixture `buyers.current`, LLM `buyers.current` (same)
- Component 1 `seller_actor`: fixture `sellers.current`, LLM `sellers.current` (same)
- Component 1 `domestic_seller_actor`: fixture `sellers.substitutes`, LLM `sellers.substitutes` (same)
- Component 1 `revenue_actor`: fixture `officials.enforcement`, LLM `officials.enforcement` (same)
- Component 1 `exporter_actor`: fixture `export_industries`, LLM `export_industries` (same)

## Decider

| Question | Fixture p | LLM p | Difference | Same side of 0.5 |
|---|---|---|---|---|
| c1.binding | 0.75 | 0.70 | -0.05 | yes |
| c1.enforced | 0.85 | 0.60 | -0.25 | yes |
| c1.alternative_uses | 0.70 | 0.65 | -0.05 | yes |
| c1.nontransferable | 0.95 | 0.85 | -0.10 | yes |
| c1.buyouts_limited | 0.70 | 0.70 | +0.00 | yes |
| c1.would_leave | 0.85 | 0.85 | +0.00 | yes |
| c1.lockin_dominates | 0.65 | 0.62 | -0.03 | yes |
| c1.keepers_dominate | 0.60 | 0.63 | +0.03 | yes |
| c1.substitutes | 0.80 | 0.70 | -0.10 | yes |

Mean absolute difference 0.07; answers on the other side of the cut-off: 0.

## Pipeline runs

| Run | Reported | Only in this run | Missing vs baseline | F1 | Brier |
|---|---|---|---|---|---|
| fixtures (baseline) | 9 | - | - | 1.00 | 0.06 |
| fixture record + LLM answers | 9 | - | - | 1.00 | 0.09 |
| LLM record + LLM answers | 9 | - | - | 1.00 | 0.09 |

Actor names in the LLM record, mapped to the fixture's by role before comparing rows: `landlords.covered` -> `landlords.controlled`
