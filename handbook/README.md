# Method Handbook

How to analyze the consequences of a policy praxeologically, written so that a newcomer can follow it and a machine can later encode it. This is the Phase 1 deliverable of the project plan (`../Praxeology_AI_Project_Plan_v3.md`, Section 4).

**Status:** draft 0.1, written before any expert review. Every rule, tier decision and source pointer is a proposal. Source pointers were written from memory and must be checked against the texts before they are relied on.

## How to use it

To analyze a policy, work through `03_workflow.md` step by step, using `templates/analysis_template.md` as the form to fill in. Look up the rules you apply in `04_rules.md` and cite them by ID. When you need a move that no rule covers, use it anyway, mark it `GAP`, and add it to `06_gaps.md`. The worked examples in `05_examples/` show what a finished analysis looks like.

## Contents

| File | What it holds |
|---|---|
| `01_foundations.md` | The action axiom and the axiom-level laws that rules rest on, with a proposed tier for each. |
| `02_ontology.md` | The vocabulary: actor classes, variables, interventions, consequences, assumptions, signs, horizons, visibility. Includes the controlled variable list for version 1. |
| `03_workflow.md` | The eleven-step procedure, with the questions to ask at each step, common moves, pitfalls and the output each step produces. |
| `04_rules.md` | Rule catalog 0.1: generic response rules, opportunity-cost and time rules, and rules for the three version 1 families (price controls; taxes, tariffs and subsidies; licensing, quotas and prohibition), plus dominance rules. |
| `05_examples/` | Fully worked analyses: WE-001 rent freeze, WE-002 local excise tax on sweetened drinks, WE-003 licensing of hair braiders. |
| `06_gaps.md` | Moves used in the examples that the catalog does not yet cover, and questions that need an expert decision. |
| `templates/analysis_template.md` | Blank analysis form following the workflow. |

## Conventions

- **Rule IDs** have a family prefix and a number: `RS` generic responses, `OC` opportunity cost, `TS` time structure, `PC` price controls, `TX` taxes and tariffs, `SB` subsidies, `EN` entry restrictions (licensing, quotas, prohibition), `DM` dominance rules. The IDs used for illustration in the project plan (PR-017 and so on) are superseded by these.
- **Foundations** are cited as `AX-n` (axiom) and `LW-n` (axiom-level law).
- **Tiers** follow the plan: A (axiom-level only), B (named empirical assumptions, each with an estimate), J (typed-decision trail), C (suggestion, not derived). In this Handbook a rule's tier is the tier of its conclusion when its preconditions are met; a consequence derived through several rules takes the lowest tier in its chain.
- **Signs** are `increase`, `decrease` or `ambiguous`. Always relative to what would have happened without the policy, never relative to the past.
- **Horizons** are `short` (under a year), `medium` (one to five years) and `long` (more than five years).
- **Worked-example probabilities** are illustrative, because the examples are stylized policies in a fictional city. In a real analysis, every estimate must cite its evidence.
- **Historical evaluation cases** (for example the 1994 San Francisco rent control expansion) are reserved for Phase 4 and are deliberately not used as worked examples here.
