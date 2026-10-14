# 6. Gaps and open questions

The to-do list for the catalog and the agenda for the first expert review. Gaps come from the worked examples: each is a move an analysis needed that the catalog does not yet cover. Questions are decisions the Handbook cannot make on its own.

## 6.1 Gaps found in the worked examples

| ID | Found in | Gap | Proposed fix |
|---|---|---|---|
| GAP-1 | WE-001 | Announcement effects before a policy takes effect: the policy record has no announcement date, so RS-8 cannot be applied. | Add `announced` to the policy record. |
| GAP-2 | WE-001 | No rule links lower housing turnover to worse job matching. | New rule under RS or a cross-market relation `housing → labor mobility`. Needs expert input on whether this is praxeological or empirical. |
| GAP-3 | WE-001, WE-002, WE-003 | Opportunity-cost entries are losses, not signed variables, so they do not fit the normal form cleanly. | Either express each as a signed variable (for example, `resources_available_other_uses` decrease), or add a `loss` type to the normal form. Proposal: the former, so all consequences can be scored the same way. |
| GAP-4 | WE-002 | No rule for bundled shopping trips: cross-border buying of a taxed good takes untaxed purchases with it. | New rule RS-9, using a `complement` relation between the taxed good and the shopping trip. |
| GAP-5 | WE-002 | No variables for health or nutrient intake. | Out of scope for version 1. Note in reports that health effects are not analyzed. |
| GAP-6 | WE-002 | No rule for fungibility of earmarked revenue: an earmark adds less than it appears if the budget would have funded some of the same spending anyway. | New rule SB-7. |
| GAP-7 | WE-002 | No variable for revenue relative to a projection that ignores behavioral responses. | Add `tax_revenue_vs_static_projection`, or leave to reports. |
| GAP-8 | WE-003 | The informal-market effects (higher search costs, no reputation, no legal recourse) are written only into EN-7 (prohibition). | Move them into a generic rule RS-10, used by PC-6, EN-3 and EN-7. |
| GAP-9 | WE-003 | The direct effect of a licensing rule (who may sell) has no variable. | Add `share_of_sellers_licensed`. |
| GAP-10 | WE-003 | No way to compare a one-time cost with a later stream of gains, so some earnings effects stay ambiguous. | Expert input needed; possibly leave as ambiguous by design. |
| GAP-11 | WE-002 | Tax incidence share by subgroup ("immobile buyers bear more") has no variable. | Add `tax_share_borne`, with signs relative to other subgroups. |

## 6.2 Questions for the experts

**Q1. Tier A decisions.** Which foundations and rules may produce Tier A conclusions? The draft proposes A for AX-1, LW-1, LW-2, LW-5, LW-6, LW-7, the OC rules, PC-2, PC-3 and PC-11 (given their preconditions), and A for LW-3 by decision, with the price-as-quality-signal and Giffen exceptions recorded. Is that right?

**Q2. Contested empirical rules.** PC-10 (minimum wage) is a standard praxeological conclusion whose empirical support is disputed. Should it stay as written, with the dispute recorded, or be weakened (for example, to "employment, hours or non-wage compensation decrease, in some combination")? The draft already uses the weaker form.

**Q3. Rothbard on the general sales tax.** Rothbard argued that a general sales tax is not shifted forward to buyers. Should this be encoded as a selectable option alongside DM-1, as the plan's open decision on disagreements within the tradition suggests?

**Q4. The intervention spiral.** Should TS-4 (Mises: interventions produce problems that lead to further intervention or repeal) be a rule? If so, which variables does it predict, and how could it be checked?

**Q5. Political responses.** RS-7 (lobbying) is an application of the action axiom to political actors. How far should the method go in predicting political responses, as opposed to market ones?

**Q6. Depth limit.** Is a limit of four links, with pruning of diffuse bystander effects after three, close to how experts actually stop? (WE-001 needed depth 3 at most.)

**Q7. Non-classical sources.** EN-8 (prohibition favors concentrated forms) comes from Cowen and Thornton rather than Mises or Rothbard. What is the standard for admitting a rule that is consistent with praxeology but not from its canonical texts?

**Q8. Visibility test.** Is "would this appear in a news story about the policy's passage?" a good enough test for visible versus invisible? WE-002's C-2 (fewer drinks sold) is both intended and visible; C-13 (who bears the tax) is neither.

**Q9. Reporting cut-off.** The plan reports a consequence if each of its assumptions has p of at least 0.5. But a consequence that rests on three independent assumptions at 0.6 each holds with probability of only about 0.2. Should the cut-off apply to the joint probability of a consequence's assumptions instead? This changes the plan (Section 7.3) and needs deciding before Phase 4.

**Q10. Grants of privilege.** Rothbard treats licensing, quotas and tariffs as "grants of monopolistic privilege". Should the Handbook adopt that category explicitly, as a shared parent of EN-1, EN-6 and TX-7?

**Q11. The counterfactual.** Every sign is relative to "the same place and time without the policy". When a market is trending (rents rising 5% a year), is that trend part of the counterfactual by default? The draft assumes yes.

## 6.3 Next steps for Phase 1

1. **Expert review of this draft.** Go through Q1 to Q11, then review each rule and each worked example step by step. Log findings by severity, as in Phase 3.
2. **Close the gaps.** Add the proposed rules and variables (GAP-1, 3, 4, 6, 8, 9, 11) and re-run the three worked examples.
3. **Record expert walkthroughs.** Ask two or three praxeologists to analyze a fresh policy aloud, and compare their moves with the workflow. Every move they make that is not in the workflow or catalog becomes a gap.
4. **Write 22 more worked examples**, to reach the plan's 25. Proposed list, from simple to messy, all within the version 1 families:

| # | Policy | Main rule families |
|---|---|---|
| WE-004 | Broken window: town pays to replace windows broken in a storm, funded by a levy | OC, TX |
| WE-005 | Price cap on gasoline after a supply disruption | PC |
| WE-006 | Anti-price-gouging law after a natural disaster | PC, TS |
| WE-007 | Cap on interest rates for small consumer loans | PC, RS |
| WE-008 | Agricultural price floor, with the state buying the surplus | PC, SB |
| WE-009 | Minimum wage increase with a lower youth rate | PC |
| WE-010 | Per-unit tax on cigarettes in one state, neighbors untaxed | TX, RS |
| WE-011 | Tax on interest income from savings accounts | TX, TS |
| WE-012 | Payroll tax increase paid by employers | TX, DM |
| WE-013 | Tariff on imported steel, with domestic users of steel | TX |
| WE-014 | Import quota on sugar | EN |
| WE-015 | Cap on the number of taxi licenses (medallions) | EN, SB-4 |
| WE-016 | License requirement for interior designers | EN |
| WE-017 | Ban on a recreational substance, with volume-based penalties | EN |
| WE-018 | Ban on single-use plastic bags, with paper exempt | EN, RS |
| WE-019 | Temporary car scrappage subsidy | SB |
| WE-020 | First-time homebuyer grant | SB, SB-4 |
| WE-021 | Per-unit subsidy for home solar panels | SB |
| WE-022 | Repeal of a rent control ordinance (reverse of WE-001) | PC, TS |
| WE-023 | Repeal of a tariff | TX |
| WE-024 | Abolition of a licensing requirement (reverse of WE-003) | EN |
| WE-025 | Multi-part bill: a rent cap, a tax on vacant units and a subsidy for new building, together | PC, TX, SB |

The three repeals (WE-022 to WE-024) double as metamorphic checks: the analysis of a repeal should reverse the signs of the original, except where the original caused lasting changes (lost capital, sunk training).

5. **Start the calibration question bank** from the worked examples: every assumption and every step of the workflow becomes one or more typed questions with an expert-labelled answer.
