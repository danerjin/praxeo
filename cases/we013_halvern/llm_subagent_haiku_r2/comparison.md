# LLM stages against fixtures: we013_halvern

LLM outputs from `/tmp/claude-0/-home-user-praxeo/6d563eb7-45da-5432-b932-3230b691929b/scratchpad/llmsub2/we013_halvern`. The fixtures are hand-written; the LLM worked only from the policy text and the stage instructions.

## Parser

- Valid record: yes. Components: 1 (fixture 1). Unclear provisions: 3 (fixture 1).
- Citation check: every quoted sentence found in the text.
- Component 1 `instrument`: fixture `tariff`, LLM `tariff` (same)
- Component 1 `bound_actor`: fixture `importers`, LLM `importers` (same)
- Component 1 `protected_actor`: fixture `steelmakers.domestic`, LLM `sellers.domestic_steel` (DIFFERS)
- Component 1 `vacancy_decontrol`: fixture `False`, LLM `False` (same)
- Component 1 `buyer_actor`: fixture `steel_users`, LLM `buyers.current` (DIFFERS)
- Component 1 `seller_actor`: fixture `sellers.current`, LLM `sellers.current` (same)
- Component 1 `domestic_seller_actor`: fixture `steelmakers.domestic`, LLM `sellers.domestic_steel` (DIFFERS)
- Component 1 `importer_actor`: fixture `importers`, LLM `importers` (same)
- Component 1 `revenue_actor`: fixture `officials.enforcement`, LLM `general_fund` (DIFFERS)
- Component 1 `exporter_actor`: fixture `export_industries`, LLM `export_industries` (same)
- Component 1 `exporter_worker_actor`: fixture `workers.export_industries`, LLM `workers.export_industries` (same)

## Decider

| Question | Fixture p | LLM p | Difference | Same side of 0.5 |
|---|---|---|---|---|
| k1.binding | 0.85 | 0.85 | +0.00 | yes |
| k1.domestic_substitutes | 0.75 | 0.90 | +0.15 | yes |
| k1.no_offset | 0.60 | 0.68 | +0.08 | yes |
| k1.input_not_replaceable | 0.80 | 0.65 | -0.15 | yes |
| k1.competitors_exempt | 0.80 | 0.85 | +0.05 | yes |

Mean absolute difference 0.09; answers on the other side of the cut-off: 0.

## Pipeline runs

| Run | Reported | Only in this run | Missing vs baseline | F1 | Brier |
|---|---|---|---|---|---|
| fixtures (baseline) | 11 | - | - | n/a | n/a |
| fixture record + LLM answers | 11 | - | - | n/a | n/a |
| LLM record + LLM answers | 10 | - | [('buyers.construction', 'price_paid', 'increase')] | n/a | n/a |

Actor names in the LLM record, mapped to the fixture's by role before comparing rows: `buyers.current` -> `steel_users`; `general_fund` -> `officials.enforcement`; `manufacturers` -> `steel_users`; `sellers.domestic_steel` -> `steelmakers.domestic`
