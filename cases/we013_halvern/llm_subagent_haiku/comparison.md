# LLM stages against fixtures: we013_halvern

LLM outputs from `/tmp/claude-0/-home-user-praxeo/6d563eb7-45da-5432-b932-3230b691929b/scratchpad/llmsub/we013_halvern`. The fixtures are hand-written; the LLM worked only from the policy text and the stage instructions.

## Parser

- Valid record: yes. Components: 2 (fixture 1). Unclear provisions: 2 (fixture 1).
- Citation check: every quoted sentence found in the text.
- Component 1 `instrument`: fixture `tariff`, LLM `tariff` (same)
- Component 1 `bound_actor`: fixture `importers`, LLM `importers.current` (DIFFERS)
- Component 1 `protected_actor`: fixture `steelmakers.domestic`, LLM `None` (DIFFERS)
- Component 1 `excluded_actor`: fixture `None`, LLM `None` (same)
- Component 1 `vacancy_decontrol`: fixture `False`, LLM `False` (same)

## Decider

| Question | Fixture p | LLM p | Difference | Same side of 0.5 |
|---|---|---|---|---|
| k1.binding | 0.85 | 0.72 | -0.13 | yes |
| k1.domestic_substitutes | 0.75 | 0.30 | -0.45 | NO |
| k1.no_offset | 0.60 | 0.35 | -0.25 | NO |
| k1.input_not_replaceable | 0.80 | 0.65 | -0.15 | yes |
| k1.competitors_exempt | 0.80 | 0.80 | +0.00 | yes |

Mean absolute difference 0.20; answers on the other side of the cut-off: 2.

## Pipeline runs

| Run | Reported | Only in this run | Missing vs baseline | F1 | Brier |
|---|---|---|---|---|---|
| fixtures (baseline) | 11 | - | - | n/a | n/a |
| fixture record + LLM answers | 7 | - | [('export_industries', 'quantity_supplied', 'decrease'), ('steelmakers.domestic', 'net_price_received', 'increase'), ('steelmakers.domestic', 'quantity_supplied', 'increase'), ('workers.export_industries', 'employment', 'decrease')] | n/a | n/a |
| LLM record + LLM answers | 5 | [('buyers.current', 'price_paid', 'increase'), ('buyers.current', 'resources_available_other_uses', 'decrease'), ('importers.current', 'quantity_traded', 'decrease'), ('importers.current', 'resources_available_other_uses', 'decrease')] | [('buyers.construction', 'price_paid', 'increase'), ('export_industries', 'quantity_supplied', 'decrease'), ('importers', 'quantity_traded', 'decrease'), ('importers', 'resources_available_other_uses', 'decrease'), ('steel_users', 'price_paid', 'increase'), ('steel_users', 'quantity_supplied', 'decrease'), ('steel_users', 'resources_available_other_uses', 'decrease'), ('steelmakers.domestic', 'net_price_received', 'increase'), ('steelmakers.domestic', 'quantity_supplied', 'increase'), ('workers.export_industries', 'employment', 'decrease')] | n/a | n/a |
