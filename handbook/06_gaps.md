# 6. Gaps and open questions

The to-do list for the catalog and the agenda for the first expert review. Gaps come from the worked examples: each is a move an analysis needed that the catalog does not yet cover. Questions are decisions the Handbook cannot make on its own.

## 6.1 Gaps found in the worked examples

Status as of catalog 0.2. "Closed" means a rule or variable was added and the worked example re-run; it still needs expert review like everything else.

| ID | Found in | Gap | Status |
|---|---|---|---|
| GAP-1 | WE-001 | Announcement effects: the policy record had no announcement date, so RS-8 could not be applied. | Closed: `announced` added to the policy record (2.1); WE-001 C-17. |
| GAP-2 | WE-001 | No rule linked lower housing turnover to the labor market. | Closed: RS-11 lock-in, variable `job_changes`, relation note `location`; WE-001 C-18. Expert check requested (Q12). |
| GAP-3 | all | Opportunity costs were recorded as losses, not signed variables. | Closed: every consequence is now a signed variable (2.5, workflow step 9, OC rules); duplicate OC entries removed from WE-001 to WE-003. |
| GAP-4 | WE-002 | No rule for bundled shopping trips. | Closed: RS-9, relation note `trip`; WE-002 C-11 and C-12 now Tier B. |
| GAP-5 | WE-002 | No variables for health or nutrient intake. | Out of scope for version 1; stated in 2.4 and in every report's "cannot say" section. |
| GAP-6 | WE-002 | No rule for fungibility of earmarked revenue. | Closed: SB-7; WE-002 C-20. |
| GAP-7 | WE-002 | No variable for revenue against a static projection. | Closed: TX-9, variable `tax_revenue_vs_static_projection`; WE-002 C-21. |
| GAP-8 | WE-003 | Informal-market effects were written only into EN-7. | Closed: generic RS-10, now used by PC-6, EN-3 and EN-7; WE-003 C-12 now Tier B. |
| GAP-9 | WE-003 | The direct effect of licensing had no variable. | Closed: `share_of_sellers_licensed`; WE-003 C-1. |
| GAP-10 | WE-003 | No way to compare a one-time cost with later gains. | Resolved as ambiguous by design: DM-3. Expert confirmation requested (Q13). |
| GAP-11 | WE-002 | Tax incidence by subgroup had no variable. | Closed: `tax_share_borne`; WE-002 C-13. |

Gaps found in WE-004 to WE-025 are listed in 6.2.

## 6.2 Gaps found in WE-004 to WE-025, resolved in catalog 0.3

The 22 later examples raised 60 gaps. Many were the same gap found independently in different examples. They are resolved below in catalog 0.3 and ontology 0.3. "Closed" means a rule, variable or format was added and the example updated; expert review is still needed for all of it.

| Gaps | What was missing | Resolution |
|---|---|---|
| 004-1 | State provision of a good recipients would have bought anyway | SB-8 |
| 004-2 | Diverted spending diverts work (Bastiat's tailor) | OC-5 |
| 004-3 | No lump-sum tax instrument | `lump_sum_tax` in 2.3 |
| 005-1 | A ceiling passes up to inputs | PC-12 |
| 005-2 | Full cost per unit to the buyer | `full_cost_per_unit` |
| 006-1, 008-2 (variable) | Stocks held against future scarcity | `inventory_held`; TS-7 |
| 006-2 | Ceilings that allow documented costs | PC-13 |
| 007-1 | Rate caps and transaction size | PC-14; `transaction_size` |
| 008-1 | Activity moves into the favored jurisdiction | RS-4 widened |
| 008-2 | Public stocks and their disposal | SB-9 |
| 008-3 | Spillover under a floor | PC-8 widened to floors |
| 009-1 | Disjunctive ("at least one") conclusions | Group consequences, sign `at_least_one_decrease` (2.5) |
| 009-2, 012-1, 013-3 | Input cost pass-through to output buyers | RS-14 |
| 010-1, 017-1, 024-3 | Quality uncertainty in informal trade | `quality_variability`, `quality_information`; named in RS-10 |
| 010-2, 012-2, 017-3 | Other taxes' revenue when a base shrinks or shifts | TX-10 |
| 011-1 | Saving, economy-wide capital and wages | `saving`, `capital_stock_economy`; TS-9 |
| 011-2, 013-2, 015-1, 020-1, 025-1 | Capitalization of losses, and decapitalization when a gain erodes | SB-4 generalized |
| 011-3 | Tax on nominal returns under inflation | TX-11 |
| 011-4 | Savers aiming at a fixed sum | TX-6 Unless clause, pending expert decision (Q14) |
| 011-5 | Revenue sign for an ad valorem tax on a price it raises | TX-9 Unless clause |
| 012-3 | DM-1's time note gave the wrong direction in factor markets | DM-1 note restated by who owns the redeployable capital |
| 013-1 | Discretionary relief (exclusions, waivers) | RS-15 |
| 013-4 | Retaliation by foreign governments | Not encoded; added to Q5 |
| 013-5 | Return on capital | `return_on_capital` |
| 014-1 | Export losses under a quota | TX-8 widened to quotas |
| 014-2 | Split of the quota rent | DM-4 |
| 014-3 | Domestic sellers under a quota | EN-6 widened |
| 015-2 | Caps fixed in physical units | TS-3 widened |
| 015-3 | Existing rules the policy makes binding | `existing_rules` in the policy record (2.1) |
| 016-1 | Supervised-practice requirements | EN-9 |
| 016-2 | Lock-in by status, not only location | RS-11 widened |
| 017-2 | Disputes settled outside the courts | `disputes_settled_outside_courts` (violence remains out of scope) |
| 017-4 | Criminal records and later employment | EN-10 |
| 017-5 | Mix of concentrated forms | `share_concentrated_forms`; used in EN-8 |
| 018-1 | Free by-products reused for another end | Relation note `secondary_use` (2.8) |
| 018-2 | Responses that grow as routines change | TS-8 |
| 019-1 | Complements in use | RS-12 |
| 019-2, 021-1 | Subsidy incidence | DM-1 extended to SB-2; `subsidy_share_received` (020-3) |
| 019-3 | Netting a surge against a dip | DM-5 |
| 020-2 | Spending out of asset gains | OC-7 |
| 020-3 | Split of a subsidy | `subsidy_share_received` |
| 021-2 | Regulated cost recovery over a shrinking base | PC-15 |
| 021-3 | Added supply lowers price in a linked market | RS-13 |
| 022-1, 023-2, 024-2 | Whether a repeal is believed | TS-5 |
| 022-2, 023-1, 024-1 | Changes that persist after a repeal | TS-6; assumption type `reversal_cost`; `persistence` field (2.5); "Analyzing a repeal" in the workflow |
| 022-3 | Speed of rebuilding after a repeal | TS-1 extended |
| 023-3 | Lost revenue made up elsewhere | OC-6 |
| 025-2 | Interactions between components | Pairwise check in workflow step 6; `components` field (2.5) |
| 025-3 | Signs that depend on an unclear provision | `reading` field (2.5); readings get no probability (step 10) |
| 025-4 | Units held vacant | `units_held_vacant` |

## 6.3 Questions for the experts

**Q1. Tier A decisions.** Which foundations and rules may produce Tier A conclusions? The draft proposes A for AX-1, LW-1, LW-2, LW-5, LW-6, LW-7, the OC rules, PC-2, PC-3 and PC-11 (given their preconditions), and A for LW-3 by decision, with the price-as-quality-signal and Giffen exceptions recorded. Is that right?

**Q2. Contested empirical rules.** PC-10 (minimum wage) is a standard praxeological conclusion whose empirical support is disputed. Should it stay as written, with the dispute recorded, or be weakened (for example, to "employment, hours or non-wage compensation decrease, in some combination")? The draft already uses the weaker form.

**Q3. Rothbard on the general sales tax.** Rothbard argued that a general sales tax is not shifted forward to buyers. Should this be encoded as a selectable option alongside DM-1, as the plan's open decision on disagreements within the tradition suggests?

**Q4. The intervention spiral.** Should TS-4 (Mises: interventions produce problems that lead to further intervention or repeal) be a rule? If so, which variables does it predict, and how could it be checked?

**Q5. Political responses.** RS-7 (lobbying) is an application of the action axiom to political actors. How far should the method go in predicting political responses, as opposed to market ones? This includes responses by foreign governments, such as retaliation against a tariff (WE-013).

**Q6. Depth limit.** Is a limit of four links, with pruning of diffuse bystander effects after three, close to how experts actually stop? (WE-001 needed depth 3 at most.)

**Q7. Non-classical sources.** EN-8 (prohibition favors concentrated forms) comes from Cowen and Thornton rather than Mises or Rothbard. What is the standard for admitting a rule that is consistent with praxeology but not from its canonical texts?

**Q8. Visibility test.** Is "would this appear in a news story about the policy's passage?" a good enough test for visible versus invisible? WE-002's C-2 (fewer drinks sold) is both intended and visible; C-13 (who bears the tax) is neither.

**Q9. Reporting cut-off.** The plan reports a consequence if each of its assumptions has p of at least 0.5. But a consequence that rests on three independent assumptions at 0.6 each holds with probability of only about 0.2. Should the cut-off apply to the joint probability of a consequence's assumptions instead? This changes the plan (Section 7.3) and needs deciding before Phase 4.

**Q10. Grants of privilege.** Rothbard treats licensing, quotas and tariffs as "grants of monopolistic privilege". Should the Handbook adopt that category explicitly, as a shared parent of EN-1, EN-6 and TX-7?

**Q11. The counterfactual.** Every sign is relative to "the same place and time without the policy". When a market is trending (rents rising 5% a year), is that trend part of the counterfactual by default? The draft assumes yes.

**Q12. Lock-in and jobs.** RS-11 says that people who lose a benefit by moving turn down jobs that would require a move. Is this a praxeological conclusion (moving now costs more, LW-1) or an empirical claim that belongs in an assumption?

**Q13. One-time costs against later gains.** DM-3 leaves these ambiguous rather than netting them. Do experts reason about them differently, for example by appeal to the actors' own revealed choices?

**Q14. Savers aiming at a fixed sum.** A lower net return makes some savers save more to reach a fixed target. The draft adds this to TX-6 as an exception that makes total saving ambiguous where such savers matter (WE-011). How do Mises's and Rothbard's treatments of time preference bear on this?

**Q15. Violence.** Disputes in informal markets may be settled by force (WE-017). Version 1 treats this as a safety effect, out of scope. Should a later version add a variable for it, and what assumption should govern it?

## 6.4 Next steps for Phase 1

The Handbook now has 25 worked examples, the number the plan set for Phase 1, and catalog 0.3 closes the gaps they found. What remains before the Phase 1 exit test:

1. **Expert review.** Go through Q1 to Q15, then review each rule and worked example step by step. Log findings by severity, as in Phase 3. The rules added in 0.3 need the same scrutiny as the originals, since they came from the examples rather than from the canonical texts.
2. **Check the sources.** Every source pointer was written from memory. Check each against the texts, and add sources for the 0.3 rules, most of which have none yet.
3. **Record expert walkthroughs.** Ask two or three praxeologists to analyze a fresh policy aloud, and compare their moves with the workflow. Every move they make that is not in the workflow or catalog becomes a gap.
4. **Run the Phase 1 exit test.** Give someone new the Handbook and three unseen policies, and have experts judge their analyses.
5. **Start the calibration question bank** from the worked examples: every assumption and every workflow step becomes one or more typed questions with an expert-labelled answer.

The metamorphic checks in the three repeal examples (WE-022 to WE-024) are already a first test of consistency: each records which of the original consequences reverse, partly reverse or persist.

### The 25 worked examples

| # | Policy | Main rule families |
|---|---|---|
| WE-001 | Rent freeze with a new-construction exemption | PC, RS, TS |
| WE-002 | Local excise tax on sweetened drinks, earmarked for pre-school | TX, SB, RS |
| WE-003 | Cosmetology license required for hair braiding | EN, RS, OC |
| WE-004 | Broken window: a town pays to replace storm-damaged windows, funded by a levy | OC, TX |
| WE-005 | Price cap on gasoline after a refinery outage | PC |
| WE-006 | Anti-price-gouging law after a hurricane | PC, TS |
| WE-007 | Cap on interest rates for small consumer loans | PC, RS |
| WE-008 | Milk price floor, with the state buying the surplus | PC, SB |
| WE-009 | Minimum wage increase with a lower youth rate (contested case) | PC |
| WE-010 | Cigarette tax increase in one state, neighbors taxed less | TX, RS |
| WE-011 | Tax on interest income | TX, TS |
| WE-012 | Payroll tax increase paid by employers | TX, DM |
| WE-013 | Tariff on imported steel | TX, RS |
| WE-014 | Import quota on sugar | EN, DM |
| WE-015 | Cap on the number of taxi licenses | EN, SB |
| WE-016 | License requirement for interior designers, with grandfathering | EN |
| WE-017 | Ban on a recreational substance, penalties by weight | EN, RS |
| WE-018 | Ban on single-use plastic bags, paper bags for a fee | EN, RS, TS |
| WE-019 | Temporary car scrappage subsidy | SB, RS |
| WE-020 | First-time homebuyer grant | SB |
| WE-021 | Per-watt subsidy for rooftop solar, funded by a surcharge | SB, PC |
| WE-022 | Repeal of the WE-001 rent freeze | PC, TS |
| WE-023 | Repeal of a long-standing lumber tariff | TX, TS |
| WE-024 | Abolition of the WE-003 braiding license | EN, TS |
| WE-025 | Multi-part housing bill: rent cap, vacancy tax, construction subsidy | PC, TX, SB |
