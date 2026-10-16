# 8. Core-only re-run: report

All 25 worked examples were re-derived using only the core rules (`04a_core_rules.md`), with no patterns, and each re-run was compared with the pattern-based version. The re-runs are in `05_examples_core/`. Each ends with a section comparing it with the pattern-based version, and the repeals also have a metamorphic check against the core-only version of the original.

## Method

1. **Inputs.** For each case, only the policy record and the case assumptions (with probabilities) were given. The intro paragraph, the "If false" column and every reference to a consequence or a pattern were removed.
2. **Blind derivation.** Five agents each re-derived five cases. They could read only the core rules, the foundations, the ontology, the workflow and the template, not the existing analyses or the pattern catalog. Where a derivation needed a premise that was not among the case assumptions, they added it (marked A-N) and flagged it. `tools/check_handbook.py --core-only` failed any re-run that cited a pattern.
3. **Comparison.** Five further agents, which had not done the re-runs, matched every consequence of each pair. They classified each one:
   - **M:** same claim, same sign.
   - **V:** same claim, recorded differently.
   - **S:** the signs differ.
   - **OP:** only in the core-only version.
   - **OC:** only in the pattern version.

   Every difference (S, OP and OC) was then given a cause:
   - **P:** the pattern version is wrong.
   - **K:** the core rules cannot derive a valid claim.
   - **A:** a difference of premises.
   - **E:** an analyst error or omission in one version.
   - **J:** a judgment call.

## Results

| | Count |
|---|---|
| Consequences compared | 786 |
| Same claim, same sign (M + V) | 499 |
| Matched, signs differ (S) | 42 |
| Only in the core-only version (OP) | 162 |
| Only in the pattern version (OC) | 83 |

Of the 541 matched pairs, 499 (92%) agree in sign. The 287 differences break down by cause:

| Cause | Count |
|---|---|
| **K: the core rules cannot derive a valid claim** | **0** |
| P: the pattern version is wrong | 16 |
| A: a difference of premises | 27 |
| E: an analyst error or omission, in either version | 178 |
| J: a judgment call, both defensible | 66 |

Per-case counts are in each core file's comparison section.

## What the test shows

**The core rules are sufficient for these 25 cases.** No valid claim in any pattern-based analysis needed anything beyond CR-1 to CR-12, the foundations and arithmetic. The hardest steps all came out of the core rules:
- incidence of taxes and subsidies (CR-7b);
- capitalization (CR-7c);
- quota rents;
- the currency channel from import restrictions to exporters (CR-8b, CR-9);
- the time path of repeals (CR-10b);
- the weak, "at least one of" form of the minimum-wage conclusion (CR-6, CR-4).

The one pattern claim the core rules cannot derive is TS-4 (the intervention spiral), which the catalog already marks as not derivable. It had nonetheless been reported as a consequence in WE-010.

**The core rules have one limit by design.** When an actor's means fall, CR-3 and CR-8 say that some other use is given up. They do not say which. "The levy reduces sales at local shops" (WE-004) therefore needs a stated premise. This is the method working as intended: which purchases fall is an empirical question.

**No pattern is wrong in its sign, but five overclaim and several were misapplied.**

| Pattern | Problem | Found in |
|---|---|---|
| EN-3 | Says excluded sellers' money `earnings` fall. CR-3a gives only a loss by their own ranking; their next job may pay more. | WE-003 |
| EN-4, DM-2 | The "down" chain for quality assumes, without saying so, that home and informal provision is lower in quality than the paid provision it replaces. | WE-003 |
| DM-1 | Says the side with fewer alternatives bears or receives "the larger part". CR-7b gives a direction, not a comparison of shares. | WE-019, WE-020 |
| RS-6, TX-3 | Conclude `employment` decrease. The core rules license only a group: employment or hours. | several |
| RS-10 (reverse) | Asserts that quality variability falls after a repeal, ignoring that a repeal also admits untrained entrants. | WE-024 |

| Pattern | Missing clause, which led to misapplication | Found in |
|---|---|---|
| PC-8 | The opposing supply chain (sellers shut out of the controlled segment move into the uncontrolled one) was in a note, so it was missed. | WE-015 |
| OC-3 | No case for a fixed enforcement budget, or for enforcement funded from the policy's own revenue. | WE-010, WE-012 |
| PC-2 | No group form, inviting separate signs for waiting, search and non-price allocation. | WE-006, WE-009 |
| SB-4 | Limited to "lasting" policies, so a five-year subsidy's capitalization was missed. | WE-021 |
| SB-1 | Records the payers of a subsidy but not its recipients, against CR-8's symmetry. | WE-021 |
| SB-3 | Applied to a delay, when the policy only shifted timing. | WE-004 |
| RS-7 | Applied without estimating its own premise (that the group can organize). In repeals, it ignores that the other side lobbies in the counterfactual. | all; WE-022 to WE-024 |

**Both versions make the same kinds of analyst errors.** Most differences (178 of 287) are omissions or slips that the rules would have caught.
- **Failing to combine opposing chains** (CR-12b) that the analysis had itself derived. This was the most common sign error in both versions. Examples: WE-001 short-run rent, WE-002 private pre-schools, WE-007 under reading U1-b, WE-011 capital stock, WE-025 starting rents.
- **Signing one member of a group** (`employment` alone) where only "employment or hours" is licensed.
- **Recording a timing shift as a note** when the action also takes place in the counterfactual, so it should be signed per window.
- **Inferring `resources_available_other_uses` decrease from "worse off"** (CR-3a). The inference fails when some members of the class respond by buying less.
- **Measuring against the wrong baseline:** against the controlled rent, or against a different policy, rather than against no policy (WE-001 C-10, WE-025 C-19, WE-018).
- **Omissions specific to the pattern versions.** These repeat across cases, because no pattern prompts for them:
  - capitalization (SB-4), and the creation of an asset by the policy;
  - the enforcement-cost half of OC-3;
  - effects on the payer of a transfer as well as the recipient.
- **Omissions specific to the core-only versions:** many effects that were easy to derive but were not followed. Without a pattern to prompt them, the analyst must remember to apply every core rule to every actor class.

**Premises that the patterns had left implicit.** The blind re-runs added about 40 premises. Some recur:
- that an interest group can organize (behind every use of RS-7);
- that a new license is actually used;
- that sellers sell at world prices (behind the tariff pass-through);
- that an earmark exceeds what would have been spent anyway;
- that an asset's expected life covers the policy's duration.

## Changes made in response

The following changes are made in catalog 0.5 and the accompanying files.
- **Patterns:** EN-3, EN-4, DM-1, DM-2, RS-6, TX-3, RS-10, PC-8, OC-3, PC-2, SB-4, SB-1, SB-3 and RS-7 are revised as listed above.
- **Core rules:** wording is clarified where the re-runs found it unclear:
  - CR-1: provisions that fit two operations;
  - CR-3: a loss by the actor's own ranking is not a fall in their other spending;
  - CR-6: fixed quantities, existing rules and buyers of last resort;
  - CR-7b: no comparison of shares, and three or more parties;
  - CR-7c: assets created by the policy, and changes of limited duration;
  - CR-12: what counts as a dominance premise, chains that exactly cancel, and consequences reached by independent chains.
- **Workflow:** a final check, before the report, for each of the recurring errors above.
- **Checker:** warns when TS-4 appears in a consequence's derivation.

The pattern-based worked examples are then corrected for the errors the comparison attributed to them (P and E items). The core-only re-runs are kept unchanged, as the record of the test.
