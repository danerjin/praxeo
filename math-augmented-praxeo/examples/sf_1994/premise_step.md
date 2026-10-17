# Premise step: San Francisco Proposition I (1994)

Annex evidence for dominance premises, put to a decider. The decider's answer is the premise's new probability; a proposal is never applied on its own. The frozen original prediction is unchanged.

| Premise | Current p | Annex rung | Proposed p | Decider | Decider's p | Changed |
|---|---|---|---|---|---|---|
| `keepers_dominate(c1)` | 0.60 | M1 | 0.90 | fixture:premise_answers.json | 0.80 | yes |
| `lockin_dominates(c1)` | 0.65 | M1 | 0.65 | (not asked: no change proposed) | 0.65 | no |

Evidence:

- `keepers_dominate(c1)`: annex M1: favoured size [150, 720] exceeds opposed size [18, 144] everywhere
- `lockin_dominates(c1)`: annex M1: ranges overlap ([150, 720] against [32, 180]); no change proposed

Consequences that differ in the annex-informed variant:

- none
