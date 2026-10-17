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

The 25 pattern-based worked examples were then corrected against their comparisons and the new final checklist. Each correction was checked against the core rules before it was applied. Most comparison conclusions were accepted. A few were rejected, and the reasons are recorded in the example:
- **WE-006:** a lobbying premise was kept at p 0.6.
- **WE-009:** the core version's "output and consumption fall" was not added, as it would overclaim in the contested case.
- **WE-012:** "employment or hours" was kept for workers below the contribution ceiling, rather than a plain fall in hours.
- **WE-019 and WE-020:** the split of a subsidy was kept as a comparison of shares, with its premise.

The corrections also went beyond the comparison in places, for consistency with the revised patterns. Some premises they added need expert review. For example:
- WE-025's A-29, the dominance premise behind new rental investment;
- WE-006 and WE-009's reading of enforcement budgets as fixed.

The core-only re-runs are kept unchanged, as the record of the test.

---

# Second round: WE-026 to WE-035

The ten gap-probing examples were re-run the same way: blind derivation from the policy record and the case assumptions only, then a comparison by an agent that had written neither version. The derivations used core rules 0.7; the pattern versions were written under catalog 0.6.

**This round is not fully independent.** Many 0.7 clarifications to the core rules, and much of the 0.7 vocabulary, were drawn from these same ten examples' "Gaps found" sections. So agreement on those points is expected, not a test. The comparisons flag where it matters (WE-029, WE-030, WE-033, WE-035 especially). A clean test of 0.7 needs new cases.

## Results

| Case | M | V | S | OP | OC | P | K | A | E | J |
|---|---|---|---|---|---|---|---|---|---|---|
| WE-026 own-production ban | 11 | 12 | 3 | 14 | 0 | 1 | 0 | 2 | 13 | 1 |
| WE-027 deposit-refund | 16 | 9 | 0 | 17 | 6 | 1 | 0 | 3 | 16 | 3 |
| WE-028 fishing quota shares | 19 | 15 | 1 | 19 | 4 | 3 | 0 | 1 | 18 | 2 |
| WE-029 paid sick leave | 18 | 10 | 0 | 19 | 3 | 0 | 0 | 4 | 14 | 4 |
| WE-030 export subsidy | 27 | 7 | 3 | 17 | 2 | 4 | 0 | 2 | 13 | 3 |
| WE-031 energy code | 16 | 13 | 3 | 15 | 2 | 0 | 0 | 1 | 16 | 3 |
| WE-032 fare-free transit | 25 | 15 | 5 | 22 | 5 | 2 | 0 | 1 | 17 | 12 |
| WE-033 debt-funded payment | 9 | 0 | 9 | 15 | 4 | 4 | 0 | 1 | 19 | 4 |
| WE-034 non-compete ban | 13 | 8 | 3 | 16 | 1 | 0 | 0 | 0 | 15 | 6 |
| WE-035 calorie labels | 11 | 10 | 3 | 5 | 1 | 1 | 0 | 0 | 5 | 3 |
| **Total** | **165** | **99** | **30** | **159** | **28** | **16** | **0** | **15** | **146** | **41** |

Of 481 consequences compared, 294 were matched; 264 of these (90%) agree in sign. The comparisons assigned 218 causes to the 217 differences (one difference was given two). **K is again 0**: no valid claim in a pattern version needed anything beyond the core rules.

## What the round shows

**The core rules held on new kinds of policy.** Autistic bans, refundable charges, created tradable rights, mandated and prohibited contract terms, an export subsidy, a scheduled standard, public supply at zero price, a debt-funded transfer and a disclosure mandate were all derivable from CR-1 to CR-12. WE-033 confirms the answer to Q19: for a pure change in means the rules give totals and the rank of the use given up, never a named good, and that is correct rather than a gap.

**Calculus gaps the core versions raised.** Most are wording or premises, not missing rules. Grouped:

| Gap | Assessment |
|---|---|
| GAP-035-C1: whether a buyer who changes an order after a disclosure is better or worse off. CR-3 is stated over options, and a disclosure changes none. | **A real question** for the experts (new Q22): is a choice made with more knowledge revealed to be better by the actor's own ranking, or does the method stay silent? |
| GAP-028-C1: growth of a shared natural stock (fish) after the cap | Physical relation; belongs with Q20 (shared facilities). Needs an empirical premise, not a rule. |
| GAP-032-C1: bus dwell time | Technical relation; an empirical premise, not a rule. |
| GAP-034-C1: non-rival know-how | Same as GAP-034-1 (Q21). |
| GAP-030-C1: sign of export receipts (price falls, quantity rises) | Correctly ambiguous without a premise; not a gap. |
| GAP-033-C1: spending rounds after the first recipient | Stops at the monetary boundary, out of scope in version 1. |
| GAP-034-C2: cumulative location effects | Depth limit (Q6). |
| GAP-032-C3: the council's choice at review | Political response (Q5). |
| GAP-027-C2, GAP-032-C2, GAP-033-C2, GAP-027-C1: a public buyer at a fixed fee; a contingent payer; an entitlement larger than its budget; local program budgets | Extensions of the 0.7 clarifications to CR-6 and CR-8. Wording. |
| GAP-028-C2: who pays for the value of a right created by ending a race | Derivable: the value comes partly from means no longer used up in the race (CR-8c), which is not a transfer. Wording for CR-7c. |
| GAP-026-C1 (culling), GAP-029-C1, GAP-029-C2, GAP-030-C2, GAP-030-C3, GAP-031-C1, GAP-031-C2, GAP-035-C2 | Vocabulary, premises or wording; the comparisons judged GAP-029-C1 and C-2 not real (CR-1 and CR-12e cover them). |

**Pattern problems.** No pattern is wrong in sign. Problems found:

| Pattern | Problem | Found in |
|---|---|---|
| OC-3 | Signs enforcement cost against zero enforcement. When the policy shrinks an activity that was itself enforced (complaints under a nuisance law), there is an opposing chain. | WE-026 |
| OC-3, TX-1, OC-1 | Name taxpayers alone as payers from the general budget. Already fixed by the 0.7 CR-8 clarification (a group); the pattern texts should say so. | WE-027, WE-028, WE-029, WE-030, WE-031 |
| RS-1 | Signs `quantity_substitute` from CR-4 alone; the split between price and quantity needs a supply premise, as RS-16 asks. | WE-031 |
| OC-5 | Gives a group sign (employment or hours) even where the activity is new and starts from zero, where a plain rise in employment is derivable. | WE-027 |
| TS-3 | Its derivation through a clearing price does not fit a product standard; binding is CR-1 and CR-4 over the spread of designs. | WE-031 |
| EN-6 (0.7 Unless) | Says `price_paid` is not signed when the good is priced in a wider market. The price does not ration the cap, but it still moves in the CR-6 direction. | WE-028 |
| SB-10 (new in 0.7) | Should note that round trips (RS-4) are opposed by any check on the return crossing. | WE-030 |
| RS-8 | Applied one way only where a pending-case clause gives an opposing timing chain. | WE-034 |

**The recurring analyst error is unchanged:** failing to combine opposing chains the analysis itself derived (WE-028 C-29, WE-030 C-19 and C-25, WE-034 C-11, WE-035 C-14 in the pattern versions; WE-032 C-5 and C-32 in the core versions). Both versions also again signed one member of a group (a price alone where CR-6 gives price or waiting).

**Core-rule wording the 0.7 clarifications left unclear.**
- CR-12's 0.7 note ("an opposing chain that cannot be derived is not a chain") was read too widely. It should separate an underivable chain (a Tier C note) from a derivable chain that needs a premise the case lacks (state the premise with p) and from a chain whose own sign is ambiguous (WE-030, WE-031, WE-035).
- CR-1's recording note on a void-contract rule says one side loses an option and the other gains one; both lose the option of agreeing to the term (WE-034).
- CR-6: a private supplier that chooses not to charge (WE-026); a capped good only partly priced in a wider market (WE-028); whether a free price's rise satisfies "at least one margin" by itself (WE-031).
- CR-7c: claims fixed before the announcement (a windfall) against history still to be earned (WE-028).
- CR-12e: whether "a response cannot reverse its cause" binds members of a class who did not respond (WE-032); when counts over a distribution are arithmetic (WE-031).
- CR-4's fixed-cost note: whether it covers costs fixed per outlet as well as per item (WE-035).

## Changes made in response

- **Catalog 0.8.** The pattern fixes above (OC-3, OC-1, TX-1, RS-1, OC-5, TS-3, EN-6, SB-10, RS-8) and the core-rule wording above. In CR-12, three kinds of opposing chain: one no rule derives (a Tier C note), one that needs a premise the case lacks (state it with p), and one whose own sign is ambiguous. Also in CR-12: two items moving in opposite directions within one variable. In CR-8: contingent payers, capped budgets and value created by ending a race. In CR-6: public buyers at a fixed fee, and when a free price's rise is enough.
- **Q22** added to `06_gaps.md`.
- **WE-026 to WE-035 corrected** against their comparisons, now at catalog 0.8. Each correction was checked against the core rules before it was applied. Each example has a section "Corrections after the core-only comparison" listing what changed and which comparison conclusions were rejected and why. Some of the rejections:
  - WE-026: the core version's waiting time alone, where CR-6 gives a group.
  - WE-029: a ranking of short-run shares, which needs a premise.
  - WE-030: home flour sales, which are ambiguous once the opposing flour chain is.
  - WE-032: a medium-run ambiguity for employers whose staff do not use transit.
  - WE-034: the core version's single-member sign for funded training.
  - WE-035: a fall in item variety, since the opposing chain (new lighter items) is derivable.
- In all, the corrections changed about 100 consequences, added about 120 and removed 5 (WE-028 C-15, WE-032 C-9 and C-14, WE-033 C-20 and C-21). The removals are claims that needed a premise the case lacks or that duplicated another row.

The core-only re-runs are kept unchanged, as the record of the test.

---

# Third round: the held-out test, WE-036 to WE-045

WE-036 to WE-045 were written with the catalog frozen at 0.8, on cases the 0.7 and 0.8 changes were not drawn from (`06_gaps.md`, 6.2f). They were then re-run blind from the core rules, as before, and compared by agents that had written neither version. Unlike the second round, this one is independent: no catalog change was made between writing the examples and the re-runs.

Two lapses from the blind protocol were reported by the agents themselves: one read past the cut-off in the format reference (WE-021's comparison section, which cites patterns for another case); another ran one `git log` line after finishing its analyses. Neither re-run cites a pattern, and neither lapse concerned its own case.

## Results

| Case | M | V | S | OP | OC | P | K | A | E | J |
|---|---|---|---|---|---|---|---|---|---|---|
| WE-036 health cover mandate | 20 | 19 | 6 | 11 | 4 | 1 | 0 | 0 | 18 | 2 |
| WE-037 ticket resale cap | 24 | 9 | 3 | 11 | 7 | 0 | 0 | 1 | 16 | 4 |
| WE-038 municipal broadband | 14 | 10 | 4 | 8 | 1 | 0 | 0 | 2 | 7 | 4 |
| WE-039 groundwater allocation | 23 | 5 | 2 | 14 | 4 | 0 | 0 | 0 | 20 | 0 |
| WE-040 origin labeling | 25 | 13 | 0 | 10 | 7 | 1 | 0 | 0 | 10 | 6 |
| WE-041 stadium bond | 15 | 10 | 3 | 12 | 10 | 3 | 0 | 0 | 16 | 6 |
| WE-042 tariff drawback | 25 | 11 | 4 | 12 | 7 | 3 | 0 | 1 | 15 | 4 |
| WE-043 lot size repeal | 11 | 9 | 2 | 13 | 6 | 0 | 0 | 1 | 17 | 3 |
| WE-044 short-term rental ban | 30 | 10 | 6 | 14 | 5 | 4 | 0 | 1 | 14 | 6 |
| WE-045 license recognition | 19 | 6 | 3 | 12 | 7 | 2 | 0 | 2 | 15 | 3 |
| **Total** | **206** | **102** | **33** | **117** | **58** | **14** | **0** | **8** | **148** | **38** |

Of 516 consequences compared, 341 were matched; 308 of these (90%) agree in sign. The 208 differences have 208 causes. **K is 0 for the third time.** Every step in ten cases written against a frozen catalog was derivable from CR-1 to CR-12.

## What the round shows

**The core rules held; several patterns did not.** The comparisons confirmed, from the core rules alone, every pattern failure the pattern versions had reported (RS-18, SB-10, EN-11, PC-8, PC-17 and RS-17's value clause), and found more:
- **OC-8** gives the wrong sign where the counterfactual also borrows (a team that would have renovated with its own loan): other borrowers' rate is `ambiguous`. The CR-8 borrowing note shared the flaw. (WE-041)
- **RS-17's value clause** failed a second time, on the 50-staff line. (WE-036)
- **OC-3's fixed-budget clause** assumes the time comes from enforcing other rules; it can come from any other use of the agency's time. (WE-042)
- **RS-16** misses a cost the policy puts on the substitute itself. (WE-040)
- **RS-7's repeal clause** reads as if the old rule was always contested. (WE-045)

**One promotion was wrong.** "Fixed cost per item reduces variety" was counted as used a second time in WE-040. The comparison showed the use was invalid: in the counterfactual each cut had one version, so a fixed cost per version cannot reduce the count. It stays a candidate.

**Some "worked as written" verdicts were wrong.** The comparisons contradicted the pattern versions' own verdicts on CR-12 0.8 kind 2 (WE-039, misapplied), RS-17 (WE-036), the drawback as an export subsidy (WE-042, once holding costs are counted), and RS-8's Unless (WE-036, WE-044). Self-assessment by the analyst is not enough; the blind re-run is needed.

**The Tier C problem is real.** Both versions, independently, met a Tier C chain opposing a Tier B chain with no rule for combining them (WE-039, WE-041, WE-044).

**New calculus gaps raised by the core versions:** GAP-039-C1 (the counterfactual race to pump a shared stock: a physical relation, under Q20), GAP-039-C2 (the value of a lottery entry; changed no sign), GAP-045-C1 (how beliefs adjust after a policy stops conveying something: empirical). None produced a difference.

**The recurring analyst errors are unchanged:** uncombined opposing chains (in both versions), employment signed alone, signs taken against the other reading or against no lobbying instead of the counterfactual.

## Changes made in response: catalog 0.9

- **Core rules.** CR-12: a rule for Tier C against Tier B (report the Tier B sign, qualified, and the combined sign at Tier C); what the response argument gives (not reversed; `increase` needs a partial response); kind 3; activities that exist only under the policy; flows and stocks. CR-8: the borrowing baseline, revenue bonds, tax-exempt interest, a permissive reading, mutual rights. CR-6: splitting a shift into price and quantity needs a premise; a public seller with an open quantity; a capped price with a free fee. CR-7: assets without a market price, contract terms that remove an option, persistence following the stock. CR-11: sellers' response to silence; beliefs after a signal ends. CR-1, CR-3, CR-4: operations that switch at a cap, refunds on a standard, lobbying in repeals.
- **Patterns.** Corrected: RS-17, RS-18, SB-10, EN-11, OC-8, PC-8. Widened: PC-17, PC-19, RS-4, RS-7, RS-8, RS-9, RS-16, OC-3, OC-5, EN-6, TX-8. Promoted: RS-19, RS-20, OC-9, EN-12, EN-13, EN-14, EN-15. 98 patterns.
- **Ontology and workflow.** Instrument `mandate_with_charge`; variables `resource_stock`, `enrollment`; for a repeal with no earlier analysis, derive the original rule first.
- **WE-036 to WE-045 corrected** against their comparisons under catalog 0.9. Each correction was checked against the core rules before it was applied; each example has a section "Corrections after the core-only comparison", and its part (e) "Test of 0.8" is kept as the record of the test, with a "Re-run note" where the comparison contradicted a verdict. Five consequences were removed: WE-037 C-20 and C-43, WE-038 C-14, WE-040 C-10 and WE-045 C-15. The new Tier C rule is applied throughout, for example in WE-039 (Tier B signs "not counting effects through the aquifer", with combined signs at Tier C).

---

# Fourth round: the held-out test of catalog 0.9, WE-046 to WE-055

WE-046 to WE-055 were written with the catalog frozen at 0.9 (`06_gaps.md`, 6.2g), then re-run blind from the core rules and compared by agents that had written neither version. The blind protocol was tightened after the third round (a line limit on the format reference; no git history); every re-run agent reported keeping to it.

## Results

| Case | M | V | S | OP | OC | P | K | A | E | J |
|---|---|---|---|---|---|---|---|---|---|---|
| WE-046 congestion charge | 27 | 13 | 4 | 9 | 12 | 1 | 0 | 0 | 23 | 1 |
| WE-047 sugar tariff-rate quota | 27 | 8 | 5 | 7 | 5 | 2 | 0 | 0 | 11 | 4 |
| WE-048 training levy | 18 | 13 | 4 | 10 | 6 | 1 | 0 | 2 | 14 | 3 |
| WE-049 public auto insurer | 13 | 14 | 0 | 9 | 3 | 0 | 0 | 2 | 7 | 3 |
| WE-050 combustion-car ban | 24 | 7 | 2 | 17 | 4 | 2 | 0 | 0 | 15 | 6 |
| WE-051 housing revenue bonds | 21 | 9 | 2 | 9 | 4 | 1 | 0 | 1 | 10 | 3 |
| WE-052 liquor license cap repeal | 23 | 8 | 6 | 11 | 3 | 0 | 0 | 2 | 16 | 2 |
| WE-053 data localization | 16 | 10 | 5 | 9 | 4 | 0 | 0 | 3 | 11 | 4 |
| WE-054 airport night curfew | 27 | 10 | 0 | 7 | 5 | 0 | 0 | 1 | 9 | 2 |
| WE-055 home inspector licensing | 19 | 7 | 2 | 7 | 3 | 0 | 0 | 1 | 6 | 5 |
| **Total** | **215** | **99** | **30** | **95** | **49** | **7** | **0** | **12** | **122** | **33** |

Of 488 consequences compared, 344 were matched; 314 of these (91%) agree in sign. The 174 differences have 174 causes. **K is 0 for the fourth time.** "Pattern version wrong" fell from 14 to 7, and most of those were analysts leaving a chain uncombined rather than a pattern giving a wrong sign.

## What the round shows

**Every failure the analysts reported was confirmed by the blind re-runs:** the 0.9 response argument (fixed costs per firm), PC-17's buy-out clause, RS-16's 0.9 clause, TX-7 under a tariff-rate quota, EN-14, RS-20 and EN-11's baselines. Unlike the third round, few "worked" verdicts were contradicted (WE-047's response argument in part, WE-052's CR-7 0.9 "not needed").

**One systemic fault.** Three patterns (RS-20, EN-11's 0.9 clause, EN-13) compared with something other than the no-policy counterfactual. Catalog 1.0 re-bases them and adds a general rule and a final-check item.

**"Record as negligible" is wrong.** OC-8's small-borrower clause and EN-6's wider-market clause let an effect go unsigned; CR-6 asks for a sign. Both versions left prices unsigned because of it.

**Tier C settled.** In WE-046 the core version put road and bus crowding at Tier B through CR-6's public-supply clause. The comparison found CR-9 (Tier C) right: the public-supply clause covers only excess demand over a fixed quantity, and gives a group sign. Catalog 1.0 says so.

**Promotions.** Five candidates had a valid second use and are promoted; "tariff-like burden without a tax" did not (WE-053 is a location requirement with a route around it, a different move).

**No new calculus gaps.** The core versions raised several (GAP-046-C1 to GAP-055-C2); the comparisons judged each to be a premise, a vocabulary item, or out of scope (safety, productivity, security).

## Changes made in response: catalog 1.0

- **Core rules.** CR-12: what the response argument needs (constant cost; which total; a second response is a second chain); dominance does not raise a tier; the baseline of patterns. CR-6: the scope of the public-supply clause; one public price for many costs; a quota on a rate; small effects are signed. CR-8: receipts into the same budget; statutory rights. CR-9: a charge on users is an exchange relation. CR-7: which stock. CR-1, CR-3, CR-4: notches, capped refunds, lobbying generally.
- **Patterns.** Re-based: RS-20, EN-11, EN-13. Corrected: PC-17, RS-16, TX-7, EN-14, EN-6, OC-8. Widened: EN-1, EN-2, PC-19, RS-7, RS-8, RS-13, RS-17, RS-18, TS-5, OC-1. Promoted: RS-21, RS-22, RS-23, TS-10, TX-12. 103 patterns.
- **Workflow and ontology.** Final check item 9 (the baseline of every pattern); variables `stock_age`, `applications`.
- **WE-046 to WE-055 corrected** against their comparisons under catalog 1.0. Each correction was checked against the core rules before it was applied; each example has a section "Corrections after the core-only comparison", and its part (e) "Test of 0.9" is kept as the record of the test, with a "Re-run note" where the comparison contradicted a verdict. One consequence was removed (WE-050 C-6, a change of good recorded as a price change). Examples of the 1.0 rules at work: bus crowding below capacity moved to Tier C (WE-046); the importers' count re-based on no policy under EN-13 (WE-047); small effects now signed (WE-047, WE-051, WE-054); response arguments state their total and their constant-cost premise throughout.


---

# Fifth round: the held-out test of catalog 1.0, WE-056 to WE-065

WE-056 to WE-065 were written with the catalog frozen at 1.0 (`06_gaps.md`, 6.2h), re-run blind from the core rules, and compared by agents that had written neither version. The re-run agents all reported keeping to the blind protocol.

## Results

| Case | M | V | S | OP | OC | P | K | A | E | J |
|---|---|---|---|---|---|---|---|---|---|---|
| WE-056 insulin cap | 24 | 9 | 5 | 13 | 4 | 1 | 0 | 0 | 16 | 5 |
| WE-057 wealth tax | 20 | 8 | 3 | 9 | 5 | 0 | 0 | 0 | 13 | 4 |
| WE-058 land value tax | 32 | 7 | 3 | 8 | 8 | 1 | 0 | 1 | 11 | 6 |
| WE-059 right to repair | 23 | 6 | 6 | 5 | 7 | 1 | 0 | 0 | 13 | 4 |
| WE-060 basic income | 29 | 12 | 7 | 6 | 14 | 0 | 0 | 1 | 23 | 3 |
| WE-061 gig workers | 20 | 12 | 1 | 7 | 6 | 1 | 0 | 0 | 11 | 2 |
| WE-062 packaging tax | 30 | 15 | 2 | 13 | 8 | 2 | 0 | 0 | 21 | 0 |
| WE-063 Sunday trading repeal | 17 | 13 | 2 | 13 | 9 | 1 | 0 | 0 | 23 | 1 |
| WE-064 spectrum auction | 23 | 6 | 5 | 8 | 6 | 0 | 0 | 0 | 14 | 5 |
| WE-065 crop payments | 18 | 11 | 1 | 11 | 6 | 1 | 0 | 0 | 10 | 7 |
| **Total** | **236** | **99** | **35** | **93** | **73** | **8** | **0** | **2** | **155** | **37** |

Of 536 consequences compared, 370 were matched; 335 of these (91%) agree in sign. **K is 0 for the fifth time.** "Pattern version wrong" stayed low (8), and every one of those was an analyst misapplying a pattern, not a pattern giving a wrong sign as written.

## What the round shows

- **The baseline rule (1.0) works in use but the pattern texts lagged.** Analysts re-signed RS-17, RS-23, PC-17 and EN-13 against the counterfactual, as the rule asks; 1.1 rewrites those clauses.
- **Failures confirmed by the core versions:** SB-4 (a tax that reaches buyers' alternatives), PC-1 and PC-16 (a cap on the buyer's share with a third-party payer), TX-7 (a matched domestic tax), TX-9 (revenue returned to the payers), EN-14 (a standard buyers value), PC-17's buy-out clause (a payment to the counterparty).
- **Core-rule wording** that both versions found hard: the response argument for an expansion or a price fall; items that cancel against CR-12f; using a group member as a chain; "the same question" for lobbying; a right sold at creation; a third-party payer.
- **No calculus gaps.** The core versions raised fifteen; the comparisons judged each to be a premise, a recording limit, vocabulary, or out of scope.
- **The analysts' own verdicts were mostly confirmed;** a few "worked" verdicts were contradicted, nearly all for an uncombined opposing chain.

## Changes made in response: catalog 1.1

- **Core rules.** CR-12: the response argument in every direction; items that cancel; group members are not chains; ratios. CR-6: a third-party payer; margins the policy creates; labor demand as a group. CR-7: a right sold at creation; alternatives taxed too. CR-4: several changes in means; the same question. CR-1, CR-3, CR-8: lines on ratios, burdens inside a new option, dedicated funds.
- **Patterns.** Re-based: RS-17, RS-23, PC-17, EN-13. Corrected: SB-4, PC-1, PC-16, TX-7, TX-9, EN-14, SB-8, TX-1. Widened: twelve more. New: PC-20. Promoted: RS-24. 105 patterns.
