# LLM stages against fixtures: sf_1994

LLM outputs from `/tmp/claude-0/-home-user-praxeo/6d563eb7-45da-5432-b932-3230b691929b/scratchpad/llmsub/sf_1994`. The fixtures are hand-written; the LLM worked only from the policy text and the stage instructions.

## Parser

- Valid record: yes. Components: 2 (fixture 1). Unclear provisions: 3 (fixture 1).
- Citation check: every quoted sentence found in the text.
- Component 1 `instrument`: fixture `price_ceiling`, LLM `price_ceiling` (same)
- Component 1 `bound_actor`: fixture `landlords.controlled`, LLM `landlords.controlled` (same)
- Component 1 `protected_actor`: fixture `tenants.controlled`, LLM `tenants.controlled` (same)
- Component 1 `excluded_actor`: fixture `tenants.prospective`, LLM `tenants.prospective` (same)
- Component 1 `vacancy_decontrol`: fixture `True`, LLM `True` (same)

## Decider

| Question | Fixture p | LLM p | Difference | Same side of 0.5 |
|---|---|---|---|---|
| c1.binding | 0.75 | 0.85 | +0.10 | yes |
| c1.enforced | 0.85 | 0.40 | -0.45 | NO |
| c1.alternative_uses | 0.70 | 0.60 | -0.10 | yes |
| c1.nontransferable | 0.95 | 0.70 | -0.25 | yes |
| c1.buyouts_limited | 0.70 | 0.45 | -0.25 | NO |
| c1.would_leave | 0.85 | 0.55 | -0.30 | yes |
| c1.lockin_dominates | 0.65 | 0.55 | -0.10 | yes |
| c1.keepers_dominate | 0.60 | 0.40 | -0.20 | NO |
| c1.substitutes | 0.80 | 0.70 | -0.10 | yes |

Mean absolute difference 0.21; answers on the other side of the cut-off: 3.

## Pipeline runs

| Run | Reported | Only in this run | Missing vs baseline | F1 | Brier |
|---|---|---|---|---|---|
| fixtures (baseline) | 9 | - | - | 1.00 | 0.06 |
| fixture record + LLM answers | 0 | - | [('landlords.controlled', 'quantity_supplied', 'decrease'), ('landlords.controlled', 'reclassification', 'increase'), ('tenants.controlled', 'price_paid', 'decrease'), ('tenants.controlled', 'relocation_out_of_area', 'decrease'), ('tenants.controlled', 'turnover', 'decrease'), ('tenants.controlled.displaced', 'relocation_out_of_area', 'increase'), ('tenants.controlled.keepers', 'relocation_out_of_area', 'decrease'), ('tenants.prospective', 'price_paid', 'increase'), ('tenants.prospective', 'price_substitute', 'increase')] | n/a | 0.20 |
| LLM record + LLM answers | 0 | - | [('landlords.controlled', 'quantity_supplied', 'decrease'), ('landlords.controlled', 'reclassification', 'increase'), ('tenants.controlled', 'price_paid', 'decrease'), ('tenants.controlled', 'relocation_out_of_area', 'decrease'), ('tenants.controlled', 'turnover', 'decrease'), ('tenants.controlled.displaced', 'relocation_out_of_area', 'increase'), ('tenants.controlled.keepers', 'relocation_out_of_area', 'decrease'), ('tenants.prospective', 'price_paid', 'increase'), ('tenants.prospective', 'price_substitute', 'increase')] | n/a | 0.20 |
