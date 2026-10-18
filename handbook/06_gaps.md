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

The 22 later examples raised 60 gaps, and updating them to catalog 0.3 raised four more (the last four rows). Many were the same gap found independently in different examples. They are resolved below in catalog 0.3 and ontology 0.3. "Closed" means a rule, variable or format was added and the example updated; expert review is still needed for all of it.

| Gaps | What was missing | Resolution |
|---|---|---|
| 004-1 | State provision of a good recipients would have bought anyway | SB-8 |
| 004-2 | Diverted spending diverts work (Hazlitt's tailor) | OC-5 |
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
| 010-3 | Responses with sunk investment outlast the erosion of an incentive | TS-6 widened to erosion (TS-3) |
| 022-4 | Persistence that changes with the horizon | `persistence` may be given per horizon (2.5) |
| 023-4 | The losing side's response to an expected re-imposition | TS-5 losing-side clause |
| 024-4 | Timing shifts had no signed form | Convention in 2.5: signed per window, or a path note in section 8; WE-003 C-7 moved to section 8 |

## 6.2a Audit of the patterns against the core rules (catalog 0.4)

Catalog 0.4 adds a layer of twelve core rules (`04a_core_rules.md`), each universal: stated over any actor, option and means, derived from the action axiom, symmetric, and explicit about its empirical premises. Every pattern was then given a derivation from them. Results:

- **77 of 81 patterns derive cleanly** from the core rules plus the premises they already named.
- **Four problems were exposed and fixed:**
  - **TX-6** asserted as a priori that saving falls when its return is taxed. CR-4's exception (a change in total means, here savers aiming at a fixed sum) means the direction is ambiguous without a premise. The premise is now stated.
  - **OC-7** counted the gain to an asset's seller without the buyer's matching outlay, breaking CR-8's symmetry. The matching chain is now required. WE-020 already recorded it, as C-25.
  - **RS-13** covered added supply but not withdrawn supply. It now covers both.
  - **TS-4** (the intervention spiral) cannot be derived. It needs a premise about what supporters of a policy believe and how politics responds. It stays Tier C and quarantined.
- **Two foundations were missing** and have been added: the law of returns (LW-9) and imputation (LW-10). Patterns on complements, inputs, pass-through and wages relied on them without saying so.
- **Three laws are results, not premises:** LW-3 (law of demand) follows from CR-4, LW-4 from CR-7, and LW-6 from CR-6. They keep their IDs.
- **The workflow changes.** When no pattern fits, derive from the core rules. Mark a GAP only when no core rule applies.

## 6.2b Source check (catalog 0.4)

Every citation was checked against the texts. The editions, the method and the findings are in `07_sources.md`. The main corrections:
- Cost is defined in HA ch. IV, not ch. VII.
- The mutual benefit of exchange is in P&M ch. 2, not ch. 1.
- The tailor is Hazlitt's; Bastiat's own example is shoes or a book.
- The iron law of prohibition is Richard Cowan's.
- The rent control chapter is only in the 1979 edition of Hazlitt.
- DM-1's incidence rule is the standard treatment, not Rothbard's (Q3).

Most citations could be confirmed only from search extracts of the online texts, not by opening them. Opening them directly is still to be done.

## 6.2c Core-only re-run (catalog 0.5)

All 25 worked examples were re-derived blind from the core rules alone and compared with the pattern-based versions; see `08_core_rerun_report.md`. No valid claim needed anything beyond the core rules (Q16, first half). The test led to:
- revisions of 14 patterns that overclaimed or lacked a clause;
- clearer wording in CR-1, CR-3, CR-6, CR-7 and CR-12;
- a final checklist in the workflow for the errors that recur in both kinds of analysis.

The pattern-based examples are being corrected for the errors the comparison found.

## 6.2d Gaps closed in catalog 0.6

The core-only re-runs flagged points where a core rule was unclear, and catalog 0.5 did not address all of them. Catalog 0.6 closes the rest.

| Raised in | Gap | Resolution |
|---|---|---|
| WE-002 core | CR-1 could not record an operation that holds under one reading only | CR-1 "Recording": record operations per reading |
| WE-004 core | Which named purchases fall when means fall | CR-4 "A change in means alone": a premise is required; Q19 remains open |
| WE-010, WE-012 core | Whether CR-4's exception applies to the burdened good itself, and to what an actor offers | CR-4: it applies to both |
| WE-017, WE-003 core | The unit in CR-4c (a gram or a dose); "narrowly ranked" under a large one-time cost | CR-4 "Units and lumpy costs" |
| WE-016 core | Non-money terms of exchange (hours toward a license) | CR-5c: terms include everything given or received |
| WE-001, WE-013 core | "Becomes expected" for a measure likely but not certain; overlap of CR-7c and CR-10c | CR-7c: value moves with the probability; cite both rules |
| WE-017 core | Confiscation: a capital loss or a transfer? | CR-8e: a transfer, recorded on both sides; destruction uses up means |
| WE-018, WE-013, WE-001, WE-004 core | CR-9 covered only goods used together; leases, insurance and the currency link had no relation type | CR-9 widened; relation types `contract` and `currency` (2.8) |
| WE-022, WE-024 core | Persistence of transition-only effects; sunk costs in repeals | CR-10b: sunk costs are not consequences of a repeal; `persistence: n/a` for transition effects |
| WE-024 core | CR-11b covered only trade moving out of the legal market | CR-11b: symmetric |
| WE-021 core | Bunching before subsidy step-downs | CR-12h |
| WE-004 core | A reading that the record gives a probability | 2.5: that is an assumption, not a reading |
| WE-025 core | No variable for unit size | `unit_size` (2.4) |
| Comparison | Recurring moves with no pattern to prompt them | PC-16 (ceiling as transfer), RS-16 (substitute's price), EN-11 (license as signal); RS-8 and SB-6 now state both sides of a timing shift |

Still open, and for the experts: GAP-011-4 (Q14), GAP-013-4 (Q5), and Q19.

## 6.2e Gap-probing examples and catalog 0.7

Ten new examples (WE-026 to WE-035) were written to probe parts of the method the first 25 had not tested: autistic interventions, refundable charges, tradable rights, mandated and prohibited contract terms, export subsidies, product standards with a schedule, public supply at a zero price, debt-funded transfers, non-competes and disclosure mandates. They found two calculus gaps, both now expert questions, and many unclear wordings and missing words, which catalog 0.7 closes.

**Calculus gaps (for the experts).**

| Gap | Step no core rule covers | Status |
|---|---|---|
| GAP-026-1 (also WE-032, congestion) | Effects through physical proximity or a shared facility, not exchange | CR-9 0.7: recorded as `proximity` or `shared_facility` relations, chains at Tier C; Q20 |
| GAP-034-1 | A non-rival means (know-how used by a rival without loss to the first firm) | CR-8 0.7: no claim on total output; Q21 |

**Closed in 0.7.**

| Raised in | Gap | Resolution |
|---|---|---|
| WE-026 | A derived chain against a suspected opposing chain that cannot be derived | CR-12 0.7: report the derived sign; the suspected effect is a Tier C note |
| WE-026, WE-031 | Phased and scheduled operations | CR-1 0.7: operations carry the date they take effect; expected future operations act now through CR-7c and CR-10c |
| WE-027 | A per-unit charge is attached to an option; refunds with residual claimants | CR-1 and CR-8 0.7; instrument `deposit_refund`; actor class `residual_claimant`; variable `non_tax_receipts` |
| WE-028 | Fixed quantity priced in a wider market; who captures a created asset when receipt depends on later actions; the unit of a constraint | CR-6, CR-7 and CR-4 0.7; EN-6 Unless; instrument `rights_allocation`; variables `discards`, `right_lease_price` |
| WE-029 | Direction of terms under a mandated term; burden of a mandate; change of kind against change of timing | CR-5, CR-7 and CR-12 0.7; PC-17; variable `legal_breach` |
| WE-030, WE-013 | The currency link in one direction only; better offers against prevented exchanges; "a response cannot reverse its cause" | CR-9 0.7 (both directions), OC-4 Unless, CR-12(e); TX-8 widened; SB-10; variable `exchange_rate`; `buyers.foreign`, `sellers.foreign` |
| WE-031 | Product standards; counterfactual trend | Instrument `product_standard`; variable `specification_level`; assumption type `counterfactual_trend`; Q11 updated |
| WE-032 | Price set by a public supplier; fixed capacity | CR-6 0.7; PC-19; SB-8 widened; instrument `public_supply`; variable `travel_time` |
| WE-033 | Debt-funded transfers; which uses fall | OC-8; instrument `government_borrowing`; variables `interest_rate`, `consumption`; Q19 updated |
| WE-034 | Prohibited contract terms | PC-18; instrument `term_prohibition`; variable `term_prevalence` |
| WE-035 | Disclosure mandates | CR-11 0.7; instrument `disclosure_mandate` |
| Several | "No change" and mixed-direction groups had no sign | Signs `no_change` and `at_least_one_as_stated` (2.5), also per reading |
| WE-026 | Own-use bans, gifts, neighbors | Instrument `own_production_ban`; variable `home_production`; relation `gift`; actor class `neighbors` |
| WE-029, WE-012 | Size thresholds; per-head costs with a cap | RS-17, RS-18 |

**Candidate patterns.** These moves were derived from the core rules once each. They become patterns when a second example needs them; until then the derivation in the example stands.

| Candidate | Seen in | Derivation |
|---|---|---|
| Ban on own production | WE-026 | CR-1 (option removed), CR-3a, CR-9 to the sellers of the bought substitute |
| Refundable charge (deposit-refund) (promoted to TX-12 in 1.0) | WE-027 | CR-1 (charge on an option, refund on a later act), CR-4 per unit, CR-8b with a residual claimant |
| A claim payable inside a boundary draws items from outside | WE-027 | CR-4, CR-7a across the boundary |
| Circular trade under a payment for crossing a boundary (promoted to RS-19 in 0.9) | WE-030 | CR-4 (gain per round trip against its cost), CR-8c |
| Allocation of a right by history after announcement (promoted to EN-12 in 0.9) | WE-028 | CR-10a, CR-7a, CR-8c |
| High-grading under a physical-unit cap (promoted to RS-21 in 1.0) | WE-028 | CR-4c with the unit of the constraint |
| Consolidation under tradable rights (promoted to EN-13 in 0.9) | WE-028 | CR-5, CR-7a (rights move to the lowest-cost users) |
| Standard on new units, stock exempt (promoted to EN-14 in 0.9) | WE-031 | CR-1, CR-7c on the exempt stock, CR-10b |
| Scheduled tightening faster than the trend (promoted to TS-10 in 1.0) | WE-031 | CR-10c, CR-7c, CR-12h |
| A standard per unit of a chosen attribute shifts the attribute | WE-031 | CR-4 |
| Certifiers hired by those they certify | WE-031 | CR-2, CR-11 |
| Compensating differential from a non-wage term (promoted to RS-22 in 1.0) | WE-032 | CR-5c, CR-7a |
| Debt-funded transfer in two windows (promoted to OC-9 in 0.9) | WE-033 | CR-8, CR-10, CR-12g |
| Ban on a restraint over carryable training; retroactive voiding | WE-034 | CR-5c, CR-7c, CR-10b |
| Fixed cost per item reduces variety (promoted to RS-24 in 1.1; second use WE-059) | WE-035 (WE-040's use was invalid) | CR-4b with a lumpy cost |
| Restriction on using an owned durable good in one place | WE-066 | CR-1 (one place), CR-4 (park elsewhere, convert, switch mode), CR-7c (resale) |
| Selection under a uniform term (promoted to RS-23 in 1.0) | WE-029 | CR-5c, CR-4 per counterparty |
| Complaint-only enforcement (promoted to RS-20 in 0.9) | WE-029 | CR-4 (expected cost of breach differs by counterparty) |

## 6.2f Held-out test of catalog 0.8 (WE-036 to WE-045)

Catalogs 0.7 and 0.8 were tuned on WE-026 to WE-035. Ten new examples were then written with the catalog frozen at 0.8, to see whether the changes work on cases they were not drawn from. Each example ends with a "Test of 0.8" part in its Gaps found, giving a verdict on each change it used.

**Calculus gaps.** One new one: GAP-041-1, residents who value having a team in their city without buying a ticket. No exchange, shared-facility or proximity relation reaches them. It is referred to Q20. Every other step in the ten examples was derived from CR-1 to CR-12.

**Patterns whose conclusion was wrong although their preconditions held.**

| Pattern | Problem | Found in |
|---|---|---|
| RS-18 | Predicts hours moving to fewer heads under a cap per firm; the derivation (CR-4 0.8, fixed cost per firm) gives `no_change`. | WE-036 |
| RS-17 | Signs the value of firms near a threshold as a decrease; the policy also burdens their rivals above the line, so the sign is `ambiguous`. | WE-040 |
| SB-10 | The domestic price need not rise toward the export price plus the subsidy when imports of the finished good cap it. Its If clause fits a refund for exporters (drawback) only in part. | WE-042 |
| EN-11 | A license that is issued on different requirements (recognized from other states) conveys less information, not more. | WE-045 |
| PC-8 | Its Unless clause misses demand the same policy withdraws from the uncontrolled segment (brokers). | WE-037 |

**Changes that needed interpretation.** Most 0.7 and 0.8 changes worked as written. These did not:
- **Tier C against Tier B.** CR-12 0.8 does not say how a Tier C chain (shared facility, proximity) combines with an opposing Tier B chain. Seen in WE-039, WE-041 and WE-044; each read CR-12d as giving `ambiguous` at Tier C. The groundwater plan's central purpose could be reported only at Tier C.
- **OC-8** (WE-038, WE-041): revenue bonds are repaid from fees, not later taxes; no clause for a borrower too small to move its loan market, or for a legal debt limit; the lenders' side gives no sign against the right baseline.
- **Public supply** (WE-038): a public seller at a set price with no fixed quantity is covered by no clause; PC-19 rightly does not apply.
- **PC-17** (WE-036): does not cover a mandate the employer can buy out with a charge.
- **EN-6 0.8 Unless** (WE-039): written for a capped good, needed here for an input (water) whose output is priced in a wider market.
- **CR-8 0.8, value from ending a race** (WE-039): correct, but the race runs through a shared aquifer, so the split is only Tier C.
- **RS-17** for an hours line rather than firm size; **RS-4** where the law reaches resales wherever made; **RS-8 0.8** where the opposing timing chain comes from a second incentive; **TS-3 0.8** where other rules bind first; **CR-11 0.7** on what exempt sellers do, and on buyers who learn a signal became noisier; **CR-7c** for a license that cannot be sold.
- **Repeals** (WE-043): the workflow assumes an analysis of the original rule exists; here it had to be derived first.

**Candidate patterns needed a second time.** By the rule in 6.2e these are promoted: consolidation under tradable rights (WE-039); allocation of a right by history, in a wider form where history was fixed before announcement (WE-039); fixed cost per item reduces variety (WE-040); debt-funded transfer in two windows (WE-041); circular trade under a payment for crossing a boundary (WE-042); standard on new units with the stock exempt (WE-043); complaint-only enforcement (WE-044); and disclosure mandate (WE-040). New candidates proposed: a mandate with a buy-out charge, public entry at a set price against sunk incumbents, a tariff-like burden without a tax, public enforcement of a private term, a below-market lease of a public asset.

**Vocabulary.** A `not_signed` per-reading sign; a way to record a change in the probability of an action (WE-041); variables for the stock of a shared resource, amenity, complaints, and land per dwelling; the line between `legal_breach` and `informal_activity` where a ban has a permitted sub-class.

**Re-run and catalog 0.9.** The blind core-only re-run of WE-036 to WE-045 found K = 0 again, confirmed the pattern failures above and found more (OC-8's baseline, OC-3's fixed-budget clause, RS-16, RS-7). It also showed that the second use of "fixed cost per item reduces variety" was invalid, so that candidate is not promoted. Catalog 0.9 applies the fixes and promotes the other seven (`08_core_rerun_report.md`, third round). WE-036 to WE-045 are then corrected against their comparisons.

## 6.2g Held-out test of catalog 0.9 (WE-046 to WE-055)

Ten new examples were written with the catalog frozen at 0.9, on kinds of policy the 0.9 changes were not drawn from. Each ends with a "Test of 0.9" part giving a verdict on each change it used. These verdicts are the analysts' own; the last round showed that a blind re-run contradicts some of them.

**Calculus gaps.** None. Every step in the ten examples was derived from CR-1 to CR-12. Chains through roads, noise and proximity stay at Tier C under GAP-026-1 (Q20). GAP-039-C2 (the value of a lottery entry) was derived from CR-10c, CR-7c and CR-7a in WE-051.

**The new Tier C rule (CR-12 0.9) worked as written** on its main test, the congestion charge (WE-046, nine consequences), and in WE-051, WE-052 and WE-054. It needed interpretation where the Tier C chain itself pushes both ways (night noise moved to shoulder hours, WE-054) and on whether to record a Tier C sign identical to the Tier B sign (WE-046: recorded both).

**Failures: a pattern or 0.9 clause whose conclusion was wrong although its conditions held.**

| Item | Problem | Found in |
|---|---|---|
| CR-12e 0.9, response argument | Assumes the response restores the old price; with a fixed cost per firm, yields can be equalized at a higher price. Needs a constant-cost premise, or should speak of yields. In WE-051 a partial response required inputs that *can* expand, the reverse of the clause's wording. | WE-049, WE-051 |
| PC-17 0.9, buy-out | Where the charge is paid first and refunded on training, training is free at the margin and demand for the mandated term rises; the terms that adjust are those of employers who do not recover the charge. | WE-048 |
| RS-16 0.9, costs on the substitute | A cost fixed per facility does not oppose net price (CR-4, 0.8); a cost on owners, not sellers, combines with quantity, not price. Prices should be signed per unit of a given quality or risk, so that a change in mix is not a price change. | WE-053, WE-050, WE-049 |
| TX-7 | Under a tariff-rate quota its conditions are met by the cut in the in-quota rate and give a lower price; the right sign comes from the marginal rate. | WE-047 |
| RS-20 | Its main sign compares with uniform enforcement, another policy, not with no policy. | WE-055 |
| EN-11 0.9 Unless | Its decrease is against a license issued on one requirement, not against no license. | WE-055 |
| EN-6 (in reverse) | A cap on sellers is not a cap on quantity; a price fall needs a premise. | WE-052 |
| EN-14 | Omits the chain by which a shrinking stock loses its complements (fuel stations, repair), so long-run used values are `ambiguous`. | WE-050 |

**Needed interpretation.** The 0.9 rule that an asset's persistence follows its stock (a license's value follows a legal count that ends on one date; new supply can return at once; WE-052, WE-050); TX-8 0.9 for services (WE-053); EN-6 for a tariff-rate quota (WE-047); OC-8 0.9's small-borrower clause where a state exemption creates a segment (WE-051); CR-8's voiding clause for a license rather than a contract (WE-052); CR-3 0.9 for a refund capped at what was paid (WE-048); RS-17 for a notch against a kink and for a line in time (WE-048, WE-055); CR-8d's earmark, which needs a premise that the council does not cut its own funding by the full amount (WE-046); EN-12, which does not say where the value of a lottery right settles (WE-051).

**Worked as written** in most uses: OC-8 0.9 (baseline borrowing, revenue bonds, lenders), CR-8 0.9 (a reading that permits, contingent payers), CR-6 0.9 (splitting a shift; public seller with an open quantity), PC-19 0.9, RS-8 0.9, RS-9 0.9, RS-18 0.9, OC-3 0.9, OC-5 0.9, CR-7 0.9 for assets without a market price, CR-12 0.9 on activities that exist only under the policy, the 0.9 workflow note on repeals, EN-12 and EN-13.

**Candidate patterns used validly a second time** (and so to be promoted, subject to a blind re-run): high-grading under a physical-unit cap (WE-047, WE-054), compensating differential from a non-wage term (WE-046), selection under a uniform term (WE-049), deposit-refund (WE-048), scheduled tightening faster than the trend (WE-050), tariff-like burden without a tax (WE-053). Proposed new clauses: a selection clause for PC-19; a notch/kink distinction for RS-17.

**Re-run and catalog 1.0.** The blind core-only re-run of WE-046 to WE-055 found K = 0 again and confirmed the failures above. It found one more pattern compared with the wrong baseline (EN-13), showed that "record as negligible" (OC-8, EN-6) conflicts with CR-6, and settled that congestion below capacity is a Tier C `shared_facility` chain, not CR-6 rationing. Of the six claimed second uses, five were valid; "tariff-like burden without a tax" was not (WE-053 is a different move), so it stays a candidate. Catalog 1.0 applies the fixes (`08_core_rerun_report.md`, fourth round).

## 6.2h Held-out test of catalog 1.0 (WE-056 to WE-065)

Ten examples were written with the catalog frozen at 1.0 and then re-run blind from the core rules (`08_core_rerun_report.md`, fifth round). No calculus gaps were found: every claimed gap was judged a premise, a vocabulary item, a recording limit, or out of scope. The 1.0 baseline rule caught most pattern problems in use, but the pattern texts still needed re-wording (RS-17, RS-23, PC-17, EN-13). New failures: SB-4 when a tax reaches buyers' alternatives, PC-1 and PC-16 with a third-party payer, TX-7 with a matched domestic tax, TX-9 when revenue returns to the payers, EN-14 for a standard buyers value. "Fixed cost per item reduces variety" had a valid second use and is promoted (RS-24). New candidates (one use each): allocation of a right by sale (WE-064), a mandated add-on to an unregulated price (WE-061), a tax on the value of a fixed factor (WE-058), a payment counted in tonnes shifting output to lower-value tonnes (WE-065). Catalog 1.1 applies the fixes.

## 6.3 Questions for the experts

**Q1. Tier A decisions.** Which foundations and rules may produce Tier A conclusions? The draft proposes A for AX-1, LW-1, LW-2, LW-5, LW-6, LW-7, the OC rules, PC-2, PC-3 and PC-11 (given their preconditions), and A for LW-3 by decision, with the price-as-quality-signal and Giffen exceptions recorded. Is that right?

**Q2. Contested empirical rules.** PC-10 (minimum wage) is a standard praxeological conclusion whose empirical support is disputed. Should it stay as written, with the dispute recorded, or be weakened (for example, to "employment, hours or non-wage compensation decrease, in some combination")? The draft already uses the weaker form.

**Q3. Rothbard on incidence.** DM-1, and the incidence clause of CR-7b, state the standard treatment: the burden of a tax falls on the side with fewer alternatives. Rothbard's "first law of incidence" (P&M ch. 4 §3A) holds that no tax can be shifted forward. On his account a general sales tax is in effect a tax on the incomes of original factors, and any later price rise comes from reduced supply, which he does not call shifting. The two accounts agree on the sequence of events but differ in what they call shifting, and for general taxes. Should the Handbook adopt Rothbard's terms, keep the standard ones with the dispute noted (the current draft), or encode both as selectable options?

**Q4. The intervention spiral.** Should TS-4 (Mises: interventions produce problems that lead to further intervention or repeal) be a rule? If so, which variables does it predict, and how could it be checked?

**Q5. Political responses.** RS-7 (lobbying) is an application of the action axiom to political actors. How far should the method go in predicting political responses, as opposed to market ones? This includes responses by foreign governments, such as retaliation against a tariff (WE-013).

**Q6. Depth limit.** Is a limit of four links, with pruning of diffuse bystander effects after three, close to how experts actually stop? (WE-001 needed depth 3 at most.)

**Q7. Non-classical sources.** EN-8 (prohibition favors concentrated forms) comes from Cowan and Thornton rather than Mises or Rothbard. What is the standard for admitting a rule that is consistent with praxeology but not from its canonical texts?

**Q8. Visibility test.** Is "would this appear in a news story about the policy's passage?" a good enough test for visible versus invisible? WE-002's C-2 (fewer drinks sold) is both intended and visible; C-13 (who bears the tax) is neither.

**Q9. Reporting cut-off.** The plan reports a consequence if each of its assumptions has p of at least 0.5. But a consequence that rests on three independent assumptions at 0.6 each holds with probability of only about 0.2. Should the cut-off apply to the joint probability of a consequence's assumptions instead? This changes the plan (Section 7.3) and needs deciding before Phase 4.

**Q10. Grants of privilege.** Rothbard treats licensing, quotas and tariffs as "grants of monopolistic privilege". Should the Handbook adopt that category explicitly, as a shared parent of EN-1, EN-6 and TX-7?

**Q11. The counterfactual.** Every sign is relative to "the same place and time without the policy". When a market is trending (rents rising 5% a year), is that trend part of the counterfactual by default? The draft assumes yes. WE-031 adds a case: part of the trend is driven by an existing rule (a standard already tightening). The draft keeps existing rules in the counterfactual (`existing_rules`) and records the trend as an assumption of type `counterfactual_trend`.

**Q12. Lock-in and jobs.** RS-11 says that people who lose a benefit by moving turn down jobs that would require a move. Is this a praxeological conclusion (moving now costs more, LW-1) or an empirical claim that belongs in an assumption?

**Q13. One-time costs against later gains.** DM-3 leaves these ambiguous rather than netting them. Do experts reason about them differently, for example by appeal to the actors' own revealed choices?

**Q14. Savers aiming at a fixed sum.** A lower net return makes some savers save more to reach a fixed target. The draft adds this to TX-6 as an exception that makes total saving ambiguous where such savers matter (WE-011). How do Mises's and Rothbard's treatments of time preference bear on this?

**Q15. Violence.** Disputes in informal markets may be settled by force (WE-017). Version 1 treats this as a safety effect, out of scope. Should a later version add a variable for it, and what assumption should govern it?

**Q16. Are the core rules complete and minimal?** Every pattern derives from CR-1 to CR-12, but that shows only that the patterns we have are covered. Is there a kind of praxeological reasoning that experts use and none of the twelve captures? Conversely, can any of them be derived from the others? CR-6 and CR-7 might be two faces of one rule about gains not yet taken.

**Q17. Tendencies and equilibrium.** CR-6 and CR-7 speak of tendencies: prices tend toward clearing, and yields toward equality across uses. Mises grounds these in the imaginary construction of the evenly rotating economy. Is it legitimate to use the direction of a tendency as an a priori conclusion while treating its speed and completeness as empirical, as the core rules do?

**Q18. CR-4's exception.** The direction of response to a change in cost is a priori except where the change also alters the actor's total means. That exception covers the Giffen case under LW-3 and the fixed-target saver under TX-6. Is this the right single statement of the exception, and is it complete?

**Q19. Which purchases fall when means fall?** When an actor's means are reduced, the core rules say that some other use is given up but not which (CR-3, CR-8; WE-004). The method treats this as empirical and requires a premise. Is there a praxeological ground (for example, the marginal use is the one given up, LW-2) for saying more? WE-033 tested this. LW-2 says the use given up is the lowest-ranked one served, but names no good, and saving is one of the uses. A named use was reached only through a market, with premises: public borrowing raises the interest rate and crowds out private borrowing (OC-8).

**Q20. Shared facilities and proximity.** Some effects travel without exchange: a neighbor's hens, a congested road, a shared fishing ground (GAP-026-1, WE-032), a shared aquifer (WE-039), and residents who value a team's presence without buying anything (GAP-041-1). Catalog 0.7 records them as `proximity` and `shared_facility` relations and reports chains through them at Tier C. Do such effects belong to praxeological analysis, given that the affected party does not choose them? If so, under what premises may they be signed at Tier B?

**Q21. Non-rival means.** CR-8 treats every means as rival. Know-how carried to a rival firm is used there without being lost to the first (GAP-034-1). Should a core rule cover non-rival means, and what could it say a priori about total output?

**Q22. Choices made with more knowledge.** A disclosure mandate adds no option and removes none, so CR-3 cannot say whether a buyer who changes an order after seeing a calorie count is better or worse off (GAP-035-C1, from the core-only re-run of WE-035). Is a choice made with more knowledge revealed to be better by the actor's own ranking, or must the method stay silent on it? The same question arises for any policy that works through information (CR-11c).

**Q23. Private rules and consent.** For a rule made by a private body over its own premises or members, members accepted the rule-maker's power to set rules when they joined. Is a later rule change a loss to them in the same sense as a law's (LW-5, CR-3), or part of the bargain they made? Catalog 1.2 signs it against the old rules (CR-3) and records exit and rival providers; experts should confirm the reading (WE-066).

**Q24. Stated aims out of scope.** Where a policy's stated aim is out of scope, catalog 1.2 requires the report to say so first and to record exposure consequences. Is that enough to keep the report from reading as a list of costs, or should version 2 bring safety and health into scope for such cases?

**Q25. TX-8 when the form of imports changes (WE-013 against WE-042).** TX-8's 0.9 clause says that where a policy reduces imports of one good but raises imports of goods made from it, the currency chain is itself `ambiguous` (CR-12, kind 3) unless a premise says which change dominates. WE-042 C-35 applies it. WE-013 C-19 (and the labour group C-32) was written under catalog 0.5, before the clause, and signs the same chain a plain decrease. Yet WE-013 has the same structure: lightly fabricated imports just outside the tariff (C-9) and more imported finished goods made of steel (C-17). The two examples now disagree, and the rule engine cannot follow both. It currently follows WE-013 and so gives WE-042 three WRONG rows (`tests/test_out_of_sample_taxes.py`). The clause looks sound a priori: an imported machine replaces a domestic one whose imported steel was only part of its value, so the rise in finished imports can exceed the fall in steel imports, and no core rule says which is larger. Three ways to settle it:

- (a) **Keep the clause and revise WE-013.** C-19 and C-32 become `ambiguous` unless WE-013 adds a premise that the fall in steel imports dominates. For example, the mills supply most of the substitute (A-2) and finished-goods substitution is limited, with a probability and its evidence. The engine then gets the clause, triggered by a record fact for downstream imports (a substitute import role under RS-1, or reshaping under RS-5) together with a dominance premise. This is the recommended option.
- (b) **Narrow the clause.** It would apply only where the policy itself raises the downstream imports, as WE-042's drawback and exemptions do. WE-013's untaxed finished goods would then not count. The difficulty is that WE-013's K1 exemptions are also part of the policy, so the line is hard to draw.
- (c) **Withdraw the clause.** WE-042 C-35 would become a decrease (TX-8 with A-13), alongside its competition chain. This drops a chain that CR-12 says exists.

Under (a) or (c), the engine agrees with both examples and WE-042's three WRONG rows go away. Under (a), WE-013's C-19 and C-32 stay a decrease only if the new premise is at or above the cut-off.

## 6.4 Next steps for Phase 1

The Handbook now has 25 worked examples, the number the plan set for Phase 1, and catalog 0.3 closes the gaps they found. What remains before the Phase 1 exit test:

1. **Expert review.** Go through Q1 to Q15, then review each rule and worked example step by step. Log findings by severity, as in Phase 3. The rules added in 0.3 need the same scrutiny as the originals, since they came from the examples rather than from the canonical texts.
2. **Finish the source check.** Every citation has been checked once (`07_sources.md`), mostly from search extracts. Open each text directly, confirm the quotations, and add sources for the patterns added in 0.3, most of which cite only the core rules they derive from.
3. **Record expert walkthroughs.** Ask two or three praxeologists to analyze a fresh policy aloud, and compare their moves with the workflow. Every move they make that is not in the workflow or catalog becomes a gap.
4. **Run the Phase 1 exit test.** Give someone new the Handbook and three unseen policies, and have experts judge their analyses.
5. **Start the calibration question bank** from the worked examples: every assumption and every workflow step becomes one or more typed questions with an expert-labelled answer.

The metamorphic checks in the three repeal examples (WE-022 to WE-024) are already a first test of consistency: each records which of the original consequences reverse, partly reverse or persist.

### The worked examples

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
| WE-026 | Ban on keeping chickens on residential lots, with a phase-out (autistic) | EN, RS |
| WE-027 | Bottle deposit-refund scheme | TX, SB, RS |
| WE-028 | Tradable fishing quota shares allocated by history | EN, SB |
| WE-029 | Paid sick leave mandate | PC-17, RS |
| WE-030 | Export subsidy on wheat | SB-10, TX-8 |
| WE-031 | Building energy code with a tightening schedule | TS, EN |
| WE-032 | Fare-free buses and trams funded by a payroll tax | PC-19, SB-8 |
| WE-033 | One-time household cash payment funded by borrowing | OC-8, SB |
| WE-034 | Ban on non-compete clauses | PC-18 |
| WE-035 | Calorie labels on restaurant menus | EN, RS |
| WE-036 | Employer health-insurance mandate with a per-worker charge | PC-17, RS-17, RS-18 |
| WE-037 | Cap on ticket resale prices; ban on bulk-buying software | PC, RS |
| WE-038 | Municipal broadband at a set price, revenue bonds | OC-8, RS-16 |
| WE-039 | Groundwater pumping cap with tradable rights | EN-6, SB |
| WE-040 | Country-of-origin labels on meat | EN, RS-17 |
| WE-041 | Stadium funded by city bonds, leased below market | OC-8, OC-5, SB |
| WE-042 | Aluminum tariff with drawback for exporters | TX-7, TX-8, SB-10 |
| WE-043 | Repeal of a minimum lot size | TS-3, TS |
| WE-044 | Short-term rental ban | EN, RS-16, RS-8 |
| WE-045 | Recognition of other states' occupational licenses | EN, TS |
| WE-046 | Congestion charge on a city center | TX-1, RS-9, RS-16 |
| WE-047 | Sugar tariff-rate quota, licenses by history | EN-6, EN-12, EN-13, TX-7 |
| WE-048 | Payroll training levy refunded as vouchers | PC-17, RS-17, RS-18 |
| WE-049 | Public auto insurer at a set premium | PC-19, RS-16 |
| WE-050 | Ban on new combustion-car sales from 2035 | EN-14, TS-3, RS-8 |
| WE-051 | Tax-exempt revenue bonds for rental housing, by lottery | OC-8, EN-12, SB-4 |
| WE-052 | Repeal of a liquor-license cap | EN-6, EN-13, TS |
| WE-053 | Data-localization requirement | RS-17, TX-8, RS-16 |
| WE-054 | Airport night curfew with tradable slots | EN-12, EN-13, RS-8 |
| WE-055 | Licensing of home inspectors | EN-1 to EN-4, EN-11, RS-20 |
| WE-056 | Insulin out-of-pocket cap with a third-party payer | PC-20, CR-6 |
| WE-057 | Wealth tax above 10 million with an exit charge | RS-17, TX-6, SB-4 |
| WE-058 | Revenue-neutral shift to a land value tax | TX-2, CR-7c, TS-10 |
| WE-059 | Right to repair | PC-17, PC-18, RS-24 |
| WE-060 | Basic income funded by VAT | OC-1, TX-9, CR-4 |
| WE-061 | Gig-worker reclassification with a buy-out | PC-17, PC-10, RS-23 |
| WE-062 | Plastic packaging tax with a recycled-content exemption | TX-2, TX-7, RS-21 |
| WE-063 | Repeal of a Sunday-trading ban | RS-9, RS-8, TS |
| WE-064 | Spectrum auction with a build-out obligation | EN-13, PC-17, CR-7c |
| WE-065 | Crop deficiency payments | SB-2, CR-8, EN-12 |
| WE-066 | Campus e-bike ban by a private school | RS-4, RS-5, RS-16, RS-8 |
