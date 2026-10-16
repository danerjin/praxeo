# Method Handbook

How to analyze the consequences of a policy praxeologically, written so that a newcomer can follow it and a machine can later encode it. This is the Phase 1 deliverable of the project plan (`../Praxeology_AI_Project_Plan_v3.md`, Section 4).

**Status:** draft 0.9 (12 core rules; catalog 0.9, 98 derived patterns; core rules tested by blind re-runs of WE-001 to WE-045), with 55 worked examples (WE-026 to WE-035 probe parts of the method the first 25 did not test; WE-036 to WE-045 and WE-046 to WE-055 are held-out tests of catalogs 0.8 and 0.9), written before any expert review. Gaps found in the worked examples have been closed or turned into questions for the experts; see `06_gaps.md`. Every rule, tier decision and source pointer is a proposal. Citations have been checked once against the texts; `07_sources.md` records how, and which still need a direct check.

## How to use it

To analyze a policy, work through `03_workflow.md` step by step, using `templates/analysis_template.md` as the form to fill in. Use the patterns in `04_rules.md` where they fit, and cite them by ID. When no pattern fits, derive the step from the core rules in `04a_core_rules.md` and cite those. Mark a step `GAP` only if no core rule applies, and add it to `06_gaps.md`. The worked examples in `05_examples/` show what a finished analysis looks like.

## Contents

| File | What it holds |
|---|---|
| `01_foundations.md` | The action axiom and the axiom-level laws that rules rest on, with a proposed tier for each. |
| `02_ontology.md` | The vocabulary: actor classes, variables, interventions, consequences, assumptions, signs, horizons, visibility. Includes the controlled variable list for version 1. |
| `03_workflow.md` | The eleven-step procedure, with the questions to ask at each step, common moves, pitfalls and the output each step produces. |
| `04a_core_rules.md` | The core rules (CR-1 to CR-12): the universal calculus from which every pattern is derived, the tests a rule must pass to count as universal, and a map from workflow steps to core rules. |
| `04_rules.md` | Rule catalog 0.4, patterns: each with its derivation from the core rules. Patterns cover generic responses, opportunity-cost and time rules, and rules for the three version 1 families (price controls; taxes, tariffs and subsidies; licensing, quotas and prohibition), plus dominance rules. |
| `05_examples/` | 25 fully worked analyses, from the broken window to a multi-part housing bill, including three repeals that check the original analyses in reverse. Listed in `06_gaps.md`, 6.4. |
| `06_gaps.md` | Gaps the examples found and how each was resolved, questions that need an expert decision, and next steps. |
| `05_examples_core/` | The same 25 cases re-derived blind from the core rules alone, each with a comparison against the pattern-based version. |
| `08_core_rerun_report.md` | Report of that test: method, results (the core rules derived every valid claim), the patterns and recurring errors it exposed, and the changes made. |
| `07_sources.md` | Editions, short forms and the verification status of every citation. |
| `templates/analysis_template.md` | Blank analysis form following the workflow. |
| `../tools/check_handbook.py` | Consistency checker for the worked examples (sections, rule IDs, variables, signs, assumptions). |

## Conventions

- **Rule IDs** have a family prefix and a number: `RS` generic responses, `OC` opportunity cost, `TS` time structure, `PC` price controls, `TX` taxes and tariffs, `SB` subsidies, `EN` entry restrictions (licensing, quotas, prohibition), `DM` dominance rules. The IDs used for illustration in the project plan (PR-017 and so on) are superseded by these.
- **Foundations** are cited as `AX-n` (axiom) and `LW-n` (axiom-level law). **Core rules** are cited as `CR-n`, with a letter for a clause (`CR-7b`).
- **Tiers** follow the plan: A (axiom-level only), B (named empirical assumptions, each with an estimate), J (typed-decision trail), C (suggestion, not derived). In this Handbook a rule's tier is the tier of its conclusion when its preconditions are met; a consequence derived through several rules takes the lowest tier in its chain.
- **Signs** are `increase`, `decrease` or `ambiguous`. Always relative to what would have happened without the policy, never relative to the past.
- **Horizons** are `short` (under a year), `medium` (one to five years) and `long` (more than five years).
- **Worked-example probabilities** are illustrative, because the examples are stylized policies in a fictional city. In a real analysis, every estimate must cite its evidence.
- **Historical evaluation cases** (for example the 1994 San Francisco rent control expansion) are reserved for Phase 4 and are deliberately not used as worked examples here.
