# WE-043 / Analysis: Repeal of a minimum lot size

Analyst: core-only re-run (Handbook 0.8)  |  Rules: core rules CR-1 to CR-12 only  |  Status: awaiting comparison

## 1. Policy record

**Larkfield Lot Size Reform Ordinance.** Larkfield is a city of about 180,000 people in a metropolitan region of 2.4 million where about 15,000 homes are built a year. It has about 41,000 detached homes, most in its single-family zones R-1 and R-2 (68% of residential land). Since 1962 a detached home there has needed a lot of at least 6,000 sq ft and 50 feet wide. Lots: 4,500 under 6,000 sq ft (legal nonconforming); 17,000 of 6,000 to 8,999; 11,000 of 9,000 to 11,999; 8,500 of 12,000 and over, which can be split into two (about 120 splits a year). About 14,500 lots (35%) carry recorded covenants forbidding re-subdivision or requiring at least 7,500 sq ft, enforceable by any owner or the HOA and renewing every 25 years unless a majority votes to end them (renewals 2030 to 2045). Land trades at about $70 a sq ft; the median home sells for about $780,000 (2,100 sq ft on 7,500 sq ft); about 250 new detached homes a year average 2,800 sq ft. Neighboring Brackwell allows 3,000 sq ft lots (about $95 a sq ft; new 1,600 sq ft homes at about $640,000); Tessmoor requires 8,000 sq ft. About 60 variance applications a year concern homes on undersized lots; the department projects 400 to 700 split and subdivision applications a year under the new rules.

| Field | Value | Source sentence |
| --- | --- | --- |
| Jurisdiction (and what lies just outside) | Larkfield's R-1 and R-2 zones; Brackwell (3,000 sq ft lots) and Tessmoor (8,000 sq ft) on either side | Policy record |
| Announced / enacted / effective / expires | Introduced 15 Nov 2026 / passed 10 Mar 2027 (7 to 2) / effective 10 Sep 2027 / no expiry; no referendum petition | Policy record |
| Enforcement (who, penalties, resources) | Planning department; split fee $4,800 set to recover review costs; covenants enforced privately in court | R2; covenant terms |

| Component | Instrument | Target | Bound | Parameters | Exemptions |
| --- | --- | --- | --- | --- | --- |
| R1 Minimum lot | Removal of a `product_standard` (lot area per detached home) | New lots for detached homes in R-1 and R-2 | Owners and builders who subdivide or split | Minimum area 6,000 to 1,500 sq ft; minimum width 50 to 20 feet | None |
| R2 Split procedure | Change to an existing procedure | Splits into up to four lots | Planning department | Administrative approval within 60 days (before: about five months of plat review); fee $4,800; five or more lots still go through plat review | - |
| R3 Pending applications | Transition rule | Applications filed after passage | Planning department | Applications filed after passage and complete on the effective date are reviewed under the new standards, in order received | - |
| R4 Existing homes | Saving clause | Existing lots and structures | - | No change required to any existing lot or structure | - |

Existing rules, in force on both paths: setbacks of 20 ft front, 5 ft side, 15 ft rear; height 35 ft; coverage at most 50%; two off-street parking spaces per dwelling; one dwelling per lot. With them the smallest practical lot is about 2,400 to 2,500 sq ft (25 by 100 feet).

**Counterfactual.** This is a repeal: the counterfactual is that the 6,000 sq ft and 50-foot minimum stays in force, with plat review of about five months for every split and variances for homes on undersized lots. The counterfactual law forbids new detached lots under 6,000 sq ft in R-1 and R-2.

Unclear provisions:
- **U1, covenants.** U1-a: covenants requiring large lots or forbidding re-subdivision remain enforceable. U1-b: the ordinance's stated purpose makes them unenforceable as contrary to public policy. No statute, no ruling. Each reading's sign is reported where it matters.

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | CR-1 operations | Core rules applied |
| --- | --- | --- | --- | --- |
| R1 Minimum lot | triangular (the original rule forbade exchanges of small lots between owners, builders and buyers; the repeal ends the prohibition) | Yes: land is worth more as small lots (A-1); the practical minimum is about 2,500 sq ft, so the binding change is from 6,000 to about 2,500, not to 1,500 (A-4) | 2 (adds the option of creating lots down to the practical minimum; per reading for covenant lots, U1-a: not added; U1-b: added); 3 removed (no variance for homes on lots of 1,500 sq ft or more) | CR-3b, CR-4, CR-5, CR-6, CR-7a, CR-7c, CR-9, CR-10 |
| R2 Split procedure | procedural (changes what an existing option brings) | Yes for every split of up to four lots | 3 (shorter wait, attached fee) | CR-1, CR-6 (0.7, public supply), CR-8b, CR-8c |
| R3 Pending applications | transition rule (dated operation) | Yes from passage | 3 (filing after passage brings review under the new standards, in order of receipt) | CR-10a, CR-4 (x: now, y: later) |
| R4 Existing homes | saving clause | No operation: nothing existing must change | none | - |

R1 is dated: from passage to 10 Sep 2027 it acts only through expectations (CR-1, 0.7 note on dated operations; CR-10a).

## 3. Actor classes

| Actor class | Role | How its options change (CR-1) |
| --- | --- | --- |
| owners.splittable_unbound | Owners of lots of about 5,000 sq ft or more without covenants | Op 2: may split down to about 2,500 sq ft. |
| owners.covenant_bound | Owners of the 14,500 covenant lots | U1-a: no option until renewal; U1-b: op 2 as above. |
| owners.covenant_bound.enforcing | Covenant owners who value large lots | U1-b: lose an enforceable right (CR-8 0.7). |
| owners.non_splittable | Owners of lots too small to split (and covenant lots under U1-a) | No new option; through CR-9 (substitute): more homes nearby. |
| owners.lots_under_6000 | Owners of the 4,500 nonconforming lots | Op 3 removed: conforming; through CR-9 as above. |
| owners.modest_older_homes | Owners of older modest homes on splittable lots | Option to demolish and split. |
| builders, builders.small | Builders who split and build | Op 2 through owners; CR-4 entry. |
| applicants.splits, applicants.old_standard, applicants.new_splits, applicants.undersized_lots | Those who apply to the planning department | Op 3: R2 procedure and fee; R3 timing; variances no longer needed. |
| buyers.prospective, buyers.new_detached_homes, buyers.existing_homes, buyers.modest_homes | Households buying homes in Larkfield | Through CR-9 and CR-5: more, smaller, cheaper homes on offer. |
| renters, landlords.apartments_townhouses | Rental market | Through CR-9 (substitute, A-16). |
| households.commuting_in | Work in Larkfield, would buy outside | CR-4 (location): a Larkfield option at their price. |
| neighboring_jurisdictions | Brackwell builders and landowners; Tessmoor landowners | Through CR-9 (across_border). |
| construction_input_suppliers | Labor and materials for building | Through CR-9 (input_to). |
| planning_department | Reviews splits | Op 3: more work, fee receipts. |
| city (general fund) | Property tax | Through CR-8b (A-21). |
| homeowner groups, HOAs | Organized owners | CR-4: lobby or sue. |
| neighbors, street users | Adjacent owners, users of street parking | Through CR-9 (proximity, shared_facility), Tier C. |

## 4. Direct effect

CR-1 and CR-2: the immediate changes in situations. The persistence column says how much of the original rule's effect remains, compared with the path on which the 6,000 rule was never imposed.

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions | Persistence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C-1 | owners.splittable_unbound (lots of about 5,000 sq ft or more not under covenants) | asset_value (land) | increase | short (from 15 Nov 2026, most by passage on 10 Mar 2027) | CR-1 op 2, CR-3b, CR-7c, CR-10c, CR-12e | A-1, A-2, A-3, A-4 | none |
| C-2 | owners.covenant_bound (14,500 lots under recorded covenants) | asset_value (land and homes) | U1-a: ambiguous; U1-b: increase | short (from passage); medium | CR-1, CR-7c, CR-9, CR-12b | A-11, A-13, A-1, A-2 | U1-a: full until renewal, partial after; U1-b: none |
| C-3 | owners.splittable, builders | quantity_supplied (new detached lots created by splits) | increase | medium; long | CR-1 op 2, CR-4 (x: keep one lot, y: split), CR-7a | A-1, A-4, A-5 | partial (lots made under the rule cost a demolition or re-plat to change, A-24) |
| C-4 | applicants.splits (splits of up to four lots) | wait_time (approval) | decrease | medium | CR-1 op 3, CR-6, CR-12e | A-20, A-N1, A-23 | none |
| C-5 | applicants.undersized_lots (owners building on lots under 6,000 sq ft) | compliance_cost (variance applications) | decrease | short (from 10 Sep 2027); medium | CR-1 op 3, CR-8c | - | none |

## 5. Responses

CR-4 for every pair of options each class has (split or keep, sell or build, enter, wait, re-let or hold, sue, lobby); CR-6 where the department's capacity is fixed; CR-7 and CR-10 for capitalization and timing.

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions | Persistence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C-6 | owners.splittable | quantity_traded (lots and parts of lots sold to builders) | increase | medium | CR-5, CR-4 | A-19, A-5 | none |
| C-7 | builders.small | entry_rate | increase | medium | CR-4 (x: stay out, y: enter), CR-7a | A-7, A-5 | none |
| C-8 | buyers.new_detached_homes | unit_size (floor area per new detached home) | decrease | medium; long | CR-4, arithmetic | A-6, A-5 | partial (homes built under the rule remain, A-24) |
| C-9 | buyers.prospective (households buying a detached home) | price_paid (cheapest new detached homes in Larkfield) | decrease | medium; long | CR-4, CR-6, arithmetic | A-5, A-6 | partial |
| C-10 | buyers.prospective | quantity_traded (detached homes sold in Larkfield) | increase | medium; long | CR-5, CR-9 | A-5, A-1 | partial |
| C-11 | owners.non_splittable (lots too small to split, and covenant lots under U1-a) | asset_value (homes) | decrease | short (from passage); medium | CR-9, CR-6, CR-7c, CR-10c | A-11, A-3 | none |
| C-12 | owners.lots_under_6000 (4,500 legal nonconforming lots) | asset_value (lots and homes) | ambiguous | short; medium | CR-12b | A-11 | none |
| C-13 | buyers.existing_homes | price_paid (existing detached homes that cannot be split) | decrease | medium | CR-9, CR-6 | A-11 | none |
| C-14 | owners.splittable | units_held_vacant (homes on splittable lots awaiting a split) | increase | short (10 Mar 2027 until approval) | CR-10a, CR-4 (x: re-let now, y: hold for the split) | A-10 | n/a |
| C-15 | owners.splittable | investment_target (rebuilds on splittable lots, 15 Nov 2026 to approval) | decrease | short (window) | CR-10a, CR-4 (x: rebuild now, y: wait) | A-10 | n/a |
| C-16 | owners.splittable, builders | investment_target (homes built on split lots, after approval) | increase | medium; long | CR-4, CR-7a | A-5, A-1 | none |
| C-17 | applicants.old_standard | quantity_supplied (two-lot splits approved under the old standard, 10 Mar to 10 Sep 2027) | decrease | short (window) | CR-10a, CR-4 (x: file now, y: redesign and wait) | A-9 | n/a |
| C-18 | applicants.splits | wait_time (approval, first months after 10 Sep 2027) | ambiguous | short | CR-12b, CR-6, CR-10a | A-8, A-23 | n/a |
| C-19 | owners.covenant_bound, HOAs | enforcement_cost (court time and parties' legal costs in covenant suits) | increase | short; medium | CR-4 (x: accept, y: sue or split and defend), CR-8c | A-12 | n/a |
| C-20 | owners.covenant_bound.enforcing (owners who value large lots) | asset_value (right to enforce the covenants) | U1-a: no_change; U1-b: decrease | short | CR-8b, CR-8 (0.7, voiding a contract right) | A-17 | U1-a: n/a; U1-b: none |
| C-21 | owners.covenant_bound | term_prevalence (re-subdivision and large-lot covenants in force) | U1-a: decrease; U1-b: no_change | long (renewals 2030 to 2045) | CR-4 (x: renew, y: vote to end), CR-10a | A-13 | U1-a: partial |
| C-22 | homeowner groups, builders | lobbying_effort (to restore a minimum or limit splits; to keep the repeal) | increase | short; medium | CR-4 (x: accept, y: lobby), CR-8c | A-14, A-17 | n/a |
| C-23 | planning_department | enforcement_cost (review of split and subdivision applications) | increase | medium | CR-1, CR-8c | A-23 | none |
| C-24 | planning_department | non_tax_receipts (application fees) | increase | medium | CR-1 op 3, CR-8b | A-20, A-23 | none |
| C-25 | applicants.new_splits | compliance_cost (fees, surveys, demolition and building permits) | increase | medium | CR-1 op 3, CR-8c | A-5 | none |

## 6. Second-order effects

CR-9 along named relations; depth limit 4. Effects on schools and city services used by new residents are not followed: no recorded relation and no premise on how the city spends (revenue use) were given; they are left as a Tier C note. The chain from cheaper rentals to renters' other spending is pruned at depth 3 as diffuse.

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions | Persistence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C-26 | renters (households in rented apartments and townhouses) | price_substitute (rents of apartments and townhouses in Larkfield) | decrease | medium; long | CR-9, CR-6 | small-lot homes substitute for rented units (partial) | A-16, A-5 | partial |
| C-27 | landlords.apartments_townhouses | net_price_received (rent) | decrease | medium; long | CR-9, CR-6 | substitute (partial) | A-16, A-5 | partial |
| C-28 | households.commuting_in (work in Larkfield, would have bought outside) | travel_time | decrease | medium; long | CR-4 (x: buy outside and commute, y: buy in Larkfield), CR-9 | complement (location) between housing and work | A-15, A-5 | partial (households who moved away under the rule have bought there, A-24) |
| C-29 | neighboring_jurisdictions (Brackwell small-lot builders and landowners) | net_price_received (small lots and new small homes in Brackwell) | decrease | medium | CR-9, CR-6 | across_border (close) | A-15, A-5 | partial |
| C-30 | neighboring_jurisdictions (owners of small lots in Brackwell and land in Tessmoor) | asset_value (land) | decrease | short; medium | CR-7c, CR-10c | across_border (close) | A-15, A-5, A-3 | partial |
| C-31 | owners.modest_older_homes | quantity_supplied (older modest homes standing) | decrease | medium; long | CR-4 (x: keep, y: demolish and split), CR-8a | - | A-5 | n/a |
| C-32 | buyers.modest_homes | price_paid (modest homes, older and new small-lot) | decrease | medium; long | CR-9, CR-6, CR-12e | new small homes substitute for older modest homes (close) | A-22, A-5, A-11 | partial |
| C-33 | construction_input_suppliers | quantity_traded (construction labor and materials for homes in Larkfield) | increase | medium | CR-9, LW-10 | input_to new homes (close) | A-5 | none |
| C-34 | city (general fund) | tax_revenue (property tax) | increase | medium; long | CR-8b, arithmetic | - | A-21 | partial |
| C-35 | owners of new homes and of splittable lots | resources_available_other_uses (property tax paid) | decrease | medium; long | CR-3 note, CR-8b | - | A-21 | none |
| C-36 | owners.non_splittable | resources_available_other_uses (property tax paid) | increase | medium; long | CR-3 note, CR-8b | - | A-11, A-21 | none |
| C-37 | neighbors (owners next to new small-lot homes) | asset_value (adjacent homes) | decrease | medium; long | CR-9 (proximity), CR-7c | proximity | A-17 | none |
| C-38 | street users near small-lot homes | search_cost (on-street parking) | increase | medium; long | CR-9 (shared_facility) | shared_facility | A-18 | none |

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (-) | Dominance premise | Combined sign |
| --- | --- | --- | --- | --- |
| owners.splittable_unbound, asset_value, short | option to split (CR-1 op 2, CR-7c) | added supply lowers home prices (A-11) | A-2 (empirical, p 0.65): option exceeds the fall | increase (C-1) |
| owners.covenant_bound, asset_value, short; medium | U1-a: expected option at renewal (A-13); U1-b: option now | U1-a: added supply (A-11) | U1-a: none; U1-b: A-2 | U1-a: ambiguous; U1-b: increase (C-2) |
| owners.lots_under_6000, asset_value | conforming status, no variance (CR-1 op 3) | added supply (A-11) | None | ambiguous (C-12) |
| applicants.splits, wait_time, short | queue on the effective date (A-8, A-23) | 60-day procedure (R2) | None | ambiguous (C-18) |
| applicants.splits, wait_time, medium | more applications (A-23) | 60-day procedure; fee-funded staff (A-20, A-N1) | A-N1 (empirical, p 0.6) | decrease (C-4) |
| buyers.modest_homes, price_paid, medium; long | fewer older modest homes (C-31) | more close substitutes (A-22) | CR-12e arithmetic: two to four homes replace each one demolished | decrease (C-32) |
| owners.splittable, investment_target, by window | after approval (C-16) | 15 Nov 2026 to approval (C-15) | Different windows (CR-12g, CR-12h) | decrease (window); increase (medium; long) |
| owners.non_splittable vs city, property tax | city revenue (C-34) | their lower tax (C-36) | Different classes; C-34 rests on A-21 | separate consequences |

CR-12c is respected: asset values, prices, quantities, tax and resources are kept apart.

**Final check before the report.**
1. *Uncombined chains.* Every (class, variable, horizon) reached by chains of both signs is in the table above. Splittable owners' asset value (C-1) and their property tax (C-35) are different variables. Non-splittable owners lose asset value (C-11) and pay less tax (C-36): different variables, not netted.
2. *Group signs.* No rule here licenses only "at least one of"; the margins of the department's capacity are signed per window with premises (C-4, C-18).
3. *Baseline.* Every sign is against the rule staying in force, not against the situation before 1962 or before 2026.
4. *Worse off is not poorer.* `resources_available_other_uses` is signed only for property tax, which owners cannot avoid while holding the property (C-35, C-36). Non-splittable owners are worse off by asset value (C-11) but are not signed as having less to spend.
5. *Timing shifts.* Rebuilding, re-letting and old-standard splits are signed per window (C-14, C-15, C-16, C-17). Applications filed early to queue (A-8) would not exist without the repeal, so they are a path note in section 8, entering only through the wait at the effective date (C-18).
6. *Both sides of every transfer.* Fees: applicants pay (C-25), the department receives (C-24) and uses them up in review (C-23). Property tax: owners pay (C-35), the city receives (C-34). Voided covenant right under U1-b: enforcing owners lose (C-20), splitting owners gain (C-2). Revaluations: splittable owners gain at expectation (C-1); non-splittable owners (C-11) and Brackwell landowners (C-30) lose; later buyers pay the new prices and earn the normal return (CR-7c).
7. *Every class, every core rule.* CR-4 pairs, CR-6, CR-7 (with CR-7c) and CR-9 were applied to each class in section 3, including capitalization for every landowner class, the department's enforcement cost, and the payers' side of fees and taxes.
8. *Unstated premises.* One premise was added (A-N1). Lobbying rests on A-14; litigation on A-12; every response on a premise that some are at the margin (A-5, A-7, A-9, A-10, A-15, A-16, A-19).

## 8. Time structure

- **Announcement (15 Nov 2026 to 10 Mar 2027).** Values of splittable land rise, and of non-splittable homes fall, part of the way as passage becomes likely and the rest at passage (CR-7c; C-1, C-11, C-30). Owners who would have rebuilt begin to wait (C-15).
- **Window (10 Mar to 10 Sep 2027).** R3 makes the order of filing matter: applicants file complete new-standard applications early to hold a place (A-8); without the repeal those applications would not exist, so this is a path note, not a consequence. Old-standard two-lot splits are held back to be redesigned (C-17); some homes on splittable lots are left empty (C-14). Whether total filings in the window rise or fall is not signed (early new-standard filings against held-back old-standard ones; no premise on their numbers).
- **Effective date and first year.** The queue meets the department's capacity (C-18); later, fee-funded staff restore the 60-day procedure (C-4). Deferred rebuilds come back as multi-home projects (C-16).
- **Medium and long.** Supply responds through flows: one split at a time, each needing a demolition or an empty lot (CR-10b). Most of the 41,000 homes will not be split for years; the effects on unit size, prices, rents and commuting grow over time. Covenant renewals from 2030 to 2045 open more lots under U1-a (C-21).
- **Is the repeal believed?** Owners and builders expect it to last (A-3, p 0.75), so quick-payback splits go ahead. Developers of five or more lots holding back for fear of a return is not reported (A-25, p 0.4). Those with a stake in restoring the minimum lobby (C-22).
- **Lost revenue.** None to make up: fees recover review costs (A-20) and property tax rises (C-34).

**Metamorphic check against the original rule.** Derived first: what the 6,000 sq ft rule did against a path on which it was never imposed (CR-1 op 1 on small lots; CR-4, CR-6, CR-7, CR-9, CR-10). Then: which of its effects the repeal reverses.

| Effect of the original rule (against never imposed) | Sign under the rule | Repeal consequence | Sign under the repeal | Persistence |
| --- | --- | --- | --- | --- |
| New detached lots in R-1 and R-2 (CR-1 op 1, CR-4) | decrease | C-3 | increase | partial: lots and homes made under the rule cost a demolition to change (A-24, CR-10b) |
| Floor area of new homes (CR-4: one larger home per lot) | increase | C-8 | decrease | partial: the existing stock remains |
| Land value of lots that could be split (CR-7c: option removed) | decrease | C-1, C-2 | increase (U1-a covenant lots: ambiguous) | none for unbound lots; U1-a covenant lots: full until renewal, partial after |
| Value of homes that could not be split (CR-6: supply held down) | increase | C-11, C-13 | decrease | none: asset prices adjust at expectation |
| Price of the cheapest detached home in Larkfield | increase | C-9 | decrease | partial: grows with new building |
| Households commuting in from Brackwell and Tessmoor (CR-4, location) | increase | C-28 | decrease (travel_time) | partial: those who moved and bought stay (A-24) |
| Demand and prices for Brackwell small lots (CR-9, across_border) | increase | C-29, C-30 | decrease | partial |
| Rents of apartments and townhouses (CR-9, substitute) | increase | C-26, C-27 | decrease | partial |
| Variance applications for undersized lots (CR-1 op 3) | increase | C-5 | decrease | none |
| Property tax base (A-21 mirror) | decrease | C-34 | increase | partial: grows with new homes |
| Light and privacy kept for neighbors (proximity, Tier C) | increase | C-37 | decrease (asset_value) | none |
| Recorded covenants that duplicated the rule (1965 to 1995) | the rule made re-subdivision covenants largely redundant while it stood | C-2, C-20, C-21 | U1-a: covenants now bind where the rule no longer does; U1-b: voided | U1-a: the rule's effect persists on 35% of lots until renewal votes; U1-b: none |

The signs reverse in every row where the effect runs through a flow or a price; persistence is partial wherever the effect is embodied in buildings, lots or households' completed moves (CR-10b), and none where it is a price of an asset (CR-7c). Two repeal effects have no counterpart in the original rule: R2's faster procedure (C-4) and the covenant litigation and transfer (C-19, C-20), which arise because the repeal and the covenants now differ.

## 9. Opportunity costs

Each is a signed change in a variable.

| ID | Actor class | Variable | Sign | What is given up | Rules |
| --- | --- | --- | --- | --- | --- |
| C-19 | owners.covenant_bound, HOAs | enforcement_cost (court time and parties' legal costs in covenant suits) | increase | Lawyers' and courts' time, and owners' money, that would have served other ends | CR-4 (x: accept, y: sue or split and defend), CR-8c |
| C-22 | homeowner groups, builders | lobbying_effort (to restore a minimum or limit splits; to keep the repeal) | increase | Time and money spent at hearings and on campaigns | CR-4 (x: accept, y: lobby), CR-8c |
| C-23 | planning_department | enforcement_cost (review of split and subdivision applications) | increase | Planning staff time, paid from fees, that would have served other ends of those who pay them | CR-1, CR-8c |
| C-25 | applicants.new_splits | compliance_cost (fees, surveys, demolition and building permits) | increase | Fees, survey and permit work that would have served other ends | CR-1 op 3, CR-8c |
| C-31 | owners.modest_older_homes | quantity_supplied (older modest homes standing) | decrease | The remaining years of service of homes demolished to split their lots | CR-4 (x: keep, y: demolish and split), CR-8a |
| C-35 | owners of new homes and of splittable lots | resources_available_other_uses (property tax paid) | decrease | Other purchases or saving of owners who pay more property tax | CR-3 note, CR-8b |

CR-8's symmetry: fees paid (C-25) are received (C-24) and used up in review (C-23); property tax paid (C-35) is received (C-34); under U1-b the enforcing owners' loss of the covenant right (C-20) is the splitting owners' gain (C-2). Land and labor drawn into building small-lot homes (C-33) are withdrawn from other uses their owners would otherwise have chosen (CR-8a); which uses is not signed without a premise.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
| --- | --- | --- | --- | --- | --- |
| A-1 | The 6,000 rule binds: for many lots of 6,000 to 12,000 sq ft, land is worth more as small lots than as one lot. | binding | 0.85 | $95 a sq ft for small lots in Brackwell against $70 in Larkfield. | These consequences fail or lose this chain: C-1, C-2, C-3, C-10, C-16. |
| A-2 | For splittable lots as a class, the value of the option to split exceeds the fall in their value from added supply. | other | 0.65 | 400 to 700 extra homes a year against 15,000 in the region; land is more than half the value of these lots. | These consequences fail or lose this chain: C-1, C-2. |
| A-3 | Owners and builders expect the repeal to last at least a few years. | expectations | 0.75 | 7 to 2 vote; no referendum petition. | These consequences fail or lose this chain: C-1, C-11, C-30. |
| A-4 | With the setback and parking rules, the practical minimum lot is about 2,500 sq ft, well below 6,000 and above 1,500. | binding | 0.9 | Setbacks, coverage and parking applied to a 25 by 100 foot lot. | These consequences fail or lose this chain: C-1, C-3. |
| A-5 | At current land and home prices, splitting pays for some owners, after demolition, fees and the 60-day wait. | alternative_uses | 0.8 | Split costs; land and home prices. | These consequences fail or lose this chain: C-3, C-6, C-7, C-8, C-9, C-10, C-16, C-25, C-26, C-27, C-28, C-29, C-30, C-31, C-32, C-33. |
| A-6 | Coverage and height limits keep the floor area of homes on small lots below that of homes on large lots. | other | 0.75 | 50% coverage and 35 feet on 2,500 sq ft; Brackwell's 1,600 sq ft homes. | These consequences fail or lose this chain: C-8, C-9. |
| A-7 | Small builders can carry out two-to-four-lot splits at costs close to those of larger firms. | other | 0.6 | Ministerial approval; small project sizes. | These consequences fail or lose this chain: C-7. |
| A-8 | Applicants know R3 and that review is first-come, so some file early to queue. | expectations | 0.7 | The ordinance's text; builders' practice. | These consequences fail or lose this chain: C-18. |
| A-9 | Some old-standard applications that would have been filed in the window are held back to redesign under the new standards. | expectations | 0.7 | About 120 two-lot splits a year under the old rule; a redesign gains lots. | These consequences fail or lose this chain: C-17. |
| A-10 | Some owners of splittable lots who would have built, rebuilt or re-let in the window wait for the effective date and approval. | expectations | 0.7 | Rebuilds and lettings each year on such lots; a few months' delay against the gain from splitting. | These consequences fail or lose this chain: C-14, C-15. |
| A-11 | Added detached homes lower the prices of existing homes in Larkfield somewhat: buyers do not absorb them at unchanged prices. | substitutability | 0.6 | Larkfield is a submarket with its own commuting and school ties. | These consequences fail or lose this chain: C-2, C-11, C-12, C-13, C-32, C-36. |
| A-12 | Some covenant-bound owners try to split, or HOAs sue, so the question is litigated. | other | 0.8 | 35% of lots under covenants; owners on both sides. | These consequences fail or lose this chain: C-19. |
| A-13 | In some covenant subdivisions, owners who want to split can organize a vote at renewal or a petition. | other | 0.6 | Renewal dates from 2030; majority rule. | These consequences fail or lose this chain: C-2, C-21. |
| A-14 | Homeowner groups and builders can organize at a cost below their stake. | other | 0.85 | Their activity on the ordinance. | These consequences fail or lose this chain: C-22. |
| A-15 | Some households who work in Larkfield bought in Brackwell or Tessmoor because Larkfield had no detached homes at their price, and commuting is practical. | mobility | 0.7 | Commuting data; price gaps. | These consequences fail or lose this chain: C-28, C-29, C-30. |
| A-16 | Small-lot detached homes and rented apartments and townhouses are substitutes for some households. | substitutability | 0.7 | Household sizes and incomes of renters. | These consequences fail or lose this chain: C-26, C-27. |
| A-17 | Owners next to new small-lot homes rank light, privacy and lower density above their absence. | other | 0.6 | Their choice of large-lot zones; comments at the hearings. | These consequences fail or lose this chain: C-20, C-22, C-37. |
| A-18 | Some residents of new small-lot homes park on the street despite two off-street spaces. | other | 0.55 | Car ownership per household; driveway sizes on narrow lots. | These consequences fail or lose this chain: C-38. |
| A-19 | Some owners realize their gain by selling a lot or part of one. | other | 0.8 | Builders buy lots to split. | These consequences fail or lose this chain: C-6. |
| A-20 | Application fees are set to recover review costs. | revenue_use | 0.8 | R2. | These consequences fail or lose this chain: C-4, C-24. |
| A-21 | Property tax is charged at a fixed rate on assessed value, and new homes and higher land values add more to the base than lower values of non-splittable homes remove. | other | 0.6 | State assessment rules; the count of new homes against the size of the fall in non-splittable values. | These consequences fail or lose this chain: C-34, C-35, C-36. |
| A-22 | New small-lot homes are close substitutes for the older modest homes demolished to make room. | substitutability | 0.7 | Prices of Brackwell's new small homes against older Larkfield homes. | These consequences fail or lose this chain: C-32. |
| A-23 | Split and subdivision applications (400 to 700 a year) far exceed the 60 variance applications a year they replace, with similar review work each. | other | 0.75 | Planning department projection and caseload. | These consequences fail or lose this chain: C-4, C-18, C-23, C-24. |
| A-24 | Lots and homes made under the 6,000 rule cost a demolition or a re-plat to change, and households who moved away have bought homes there. | reversal_cost | 0.85 | Ages and values of homes on large lots; ownership of homes in neighboring cities. | No reported consequence rests on it (see Not reported). |
| A-25 | Developers of subdivisions of five or more lots fear the minimum's return within their payback period and hold back. | expectations | 0.4 | Long plat reviews; the two-vote minority on the council. | No reported consequence rests on it (see Not reported). |
| A-N1 | The planning department can use fee receipts to add review staff within months, so review capacity grows with applications. | revenue_use | 0.6 | NEW, flagged. Fees are set to recover review costs (R2, A-20); hiring and contract reviewers take months, not years. | These consequences fail or lose this chain: C-4. |

**Not reported** (an assumption below 0.5):
- Developers of subdivisions of five or more lots hold back, fearing that the minimum returns within their payback period (CR-10a, CR-4 with x: plat now, y: wait): needs A-25 (p 0.4).

## 11. Report

**The policy:** From 10 September 2027, Larkfield lowers the minimum lot for a detached home in its single-family zones from 6,000 to 1,500 sq ft (and the minimum width from 50 to 20 feet), and approves splits of up to four lots administratively within 60 days for a $4,800 fee. Applications filed after passage on 10 March and complete on the effective date are reviewed under the new rules in order received. Setbacks, height, coverage and parking rules stay, so the smallest practical lot is about 2,500 sq ft. Whether private covenants against re-subdivision on 35% of lots remain enforceable (U1-a) or not (U1-b) is undecided.

**Visible consequences:** Owners of lots that can be split gain value as soon as the repeal is expected (C-1). More lots are created (C-3) and more, smaller and cheaper detached homes are built and sold (C-8, C-9, C-10, C-16). Splits are approved faster once the department has staffed up (C-4); variances for undersized lots are no longer needed (C-5).

**Invisible consequences:**
- *Other homeowners:* Owners of homes that cannot be split lose value (C-11), and buyers pay less for such homes (C-13) and for modest homes generally (C-32). Under U1-b, owners who wanted their covenants enforced lose that right (C-20). Owners next to new small-lot homes lose light and privacy (C-37, Tier C).
- *Timing:* Between passage and the effective date, rebuilds and old-standard splits are held back and some homes stand empty (C-14, C-15, C-17).
- *Renters and commuters:* Rents for apartments and townhouses fall (C-26, C-27); some households who would have commuted from Brackwell or Tessmoor live in Larkfield (C-28), and Brackwell's small-lot builders and landowners lose (C-29, C-30).
- *Building:* Small builders enter (C-7), owners sell lots to builders (C-6), older modest homes are demolished (C-31), and more construction labor and materials are used in Larkfield (C-33).
- *City and courts:* The planning department reviews many more applications (C-23), paid for by fees (C-24, C-25). Property tax revenue rises (C-34), paid by owners of new and splittable homes (C-35), while owners of non-splittable homes pay less (C-36). Covenant suits use courts' and owners' resources (C-19). Both homeowner groups and builders lobby (C-22). Street parking gets harder near new homes (C-38, Tier C).

**Ambiguous effects:** Values of covenant lots under U1-a (C-2): more supply nearby pushes them down; the chance of ending the covenant at renewal pushes them up. Values of the 4,500 lots under 6,000 sq ft (C-12): conforming status pushes up, more supply pushes down. The wait for approval in the first months (C-18): a faster procedure against a queue at the effective date.

**Key conditions:** The rule binds (A-1, 0.85) and the practical minimum is about 2,500 sq ft (A-4, 0.9); splitting pays for some (A-5, 0.8). The option is worth more than the supply effect for splittable lots (A-2, 0.65). Existing home prices fall somewhat (A-11, 0.6), which drives most losses to non-splittable owners. Persistence rests on A-24 (0.85). One premise was added: fee receipts can fund review staff within months (A-N1, 0.6).

**What this analysis cannot say:** How many lots will be split, or how far prices and rents fall; whether the gains of splittable owners and new buyers outweigh the losses of other owners and neighbors; which reading of the covenant question courts will adopt; whether the policy is good. Health, safety and environmental effects, including traffic and drainage, are out of scope.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions | Persistence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C-1 | owners.splittable_unbound (lots of about 5,000 sq ft or more not under covenants) | asset_value (land) | increase | short (from 15 Nov 2026, most by passage on 10 Mar 2027) | visible | B | CR-1 (op 2: R1 adds the option of splitting into lots down to the practical minimum of about 2,500 sq ft, A-4); CR-3b (an added option cannot make the owner worse off at the time of choice); CR-10c and CR-7c (the value of the land rises for whoever owns it when the repeal becomes expected, part of the way at introduction and the rest at passage; owners expect it to last, A-3); the rule binds, since land is worth more as small lots, A-1. Opposing chain: added supply lowers home prices (A-11). Dominance (CR-12e, empirical premise): for splittable lots as a class the option is worth more than the fall from added supply, A-2 | A-1, A-2, A-3, A-4 | none |
| C-2 | owners.covenant_bound (14,500 lots under recorded covenants) | asset_value (land and homes) | U1-a: ambiguous; U1-b: increase | short (from passage); medium | invisible | B | U1-a: the covenant still forbids the split, so R1 adds no option now; (-) CR-9 (relation: substitute; new homes nearby lower home prices, A-11); (+) CR-7c and CR-10a (the option may come at renewal from 2030, where owners who want to split can organize a vote, A-13, and its expected value is capitalized now). No premise says which dominates. U1-b: the covenants are unenforceable, so the owners are in the position of C-1 (A-1, A-2) | A-11, A-13, A-1, A-2 | U1-a: full until renewal, partial after; U1-b: none |
| C-3 | owners.splittable, builders | quantity_supplied (new detached lots created by splits) | increase | medium; long | visible | B | CR-1 (op 2: splitting into lots of 2,500 sq ft or more becomes legal, A-4); CR-4 (x: keep one lot, y: split; y is newly open and pays for some owners after demolition, fees and the wait, A-5); CR-7a (land moves to the use that yields more, A-1). Under U1-a covenant lots are excluded until renewal; the sign holds under both readings | A-1, A-4, A-5 | partial (lots made under the rule cost a demolition or re-plat to change, A-24) |
| C-4 | applicants.splits (splits of up to four lots) | wait_time (approval) | decrease | medium | visible | B | CR-1 (op 3: R2 replaces about five months of plat review with administrative approval within 60 days). Opposing chain: CR-6 (0.7, public supply: 400 to 700 applications a year against 60 variances, A-23, put pressure on review capacity). Dominance (empirical premise): fees are set to recover review costs (A-20) and the receipts can be used to add review staff within months (A-N1), so capacity grows with the applications | A-20, A-N1, A-23 | none |
| C-5 | applicants.undersized_lots (owners building on lots under 6,000 sq ft) | compliance_cost (variance applications) | decrease | short (from 10 Sep 2027); medium | invisible | A | CR-1 (op 3 removed: a home on a lot of 1,500 sq ft or more no longer needs a variance; about 60 applications a year); CR-8c (the resources those applications used up are no longer spent) | none | none |
| C-6 | owners.splittable | quantity_traded (lots and parts of lots sold to builders) | increase | medium | invisible | B | CR-5 (exchanges that the rule prevented now take place when both sides gain); CR-4 (x: split and build oneself, y: sell to a builder who splits; some owners realize their gain by selling, A-19, and splitting pays, A-5) | A-19, A-5 | none |
| C-7 | builders.small | entry_rate | increase | medium | invisible | B | CR-4 (x: stay out, y: build two-to-four-lot splits; y newly open, and small builders can do it at costs close to larger firms', A-7); CR-7a (builders' means move toward the new yield, A-5) | A-7, A-5 | none |
| C-8 | buyers.new_detached_homes | unit_size (floor area per new detached home) | decrease | medium; long | visible | B | CR-4 (builders choose more, smaller homes per lot where splitting pays, A-5); arithmetic: coverage of 50% and a 35-foot height on about 2,500 sq ft keep floor area below that of homes on large lots (A-6; Brackwell's new homes are 1,600 sq ft against Larkfield's 2,800) | A-6, A-5 | partial (homes built under the rule remain, A-24) |
| C-9 | buyers.prospective (households buying a detached home) | price_paid (cheapest new detached homes in Larkfield) | decrease | medium; long | visible | B | Arithmetic on the case's figures: a 2,500 sq ft lot even at Brackwell's $95 a sq ft (about $240,000) costs far less than a 6,000 sq ft lot at $70 (about $420,000), and the home on it is smaller (C-8, A-6); CR-4 and CR-6 (builders offer such homes where splitting pays, A-5) | A-5, A-6 | partial |
| C-10 | buyers.prospective | quantity_traded (detached homes sold in Larkfield) | increase | medium; long | visible | B | CR-9 (more lots, C-3, become more homes for sale); CR-5 (exchanges that the rule prevented now take place) | A-5, A-1 | partial |
| C-11 | owners.non_splittable (lots too small to split, and covenant lots under U1-a) | asset_value (homes) | decrease | short (from passage); medium | invisible | B | CR-9 (relation: new small-lot homes substitute for existing homes); CR-6 (more homes at each price move prices down somewhat, A-11); CR-7c and CR-10c (the expected fall is borne by whoever owns the homes when the repeal becomes expected, A-3) | A-11, A-3 | none |
| C-12 | owners.lots_under_6000 (4,500 legal nonconforming lots) | asset_value (lots and homes) | ambiguous | short; medium | invisible | B | CR-12b: (+) CR-1 (op 3 removed: the lots become conforming, so rebuilding or enlarging needs no variance, C-5; CR-3b); (-) CR-9 and CR-6 (added supply lowers home prices, A-11). How many of these lots are large enough to split into two practical lots is not in the case's figures. No premise says which dominates | A-11 | none |
| C-13 | buyers.existing_homes | price_paid (existing detached homes that cannot be split) | decrease | medium | invisible | B | CR-9 (relation: substitute; new small-lot homes compete for the same buyers); CR-6 (A-11: buyers do not absorb them at unchanged prices) | A-11 | none |
| C-14 | owners.splittable | units_held_vacant (homes on splittable lots awaiting a split) | increase | short (10 Mar 2027 until approval) | invisible | B | CR-10a (a change expected in the future alters choices now); CR-4 (x: re-let or occupy the home, y: keep it empty to demolish once the split is approved; some owners wait, A-10) | A-10 | n/a |
| C-15 | owners.splittable | investment_target (rebuilds on splittable lots, 15 Nov 2026 to approval) | decrease | short (window) | invisible | B | CR-10a; CR-4 (x: rebuild one home under the old rule now, y: wait for the effective date and approval and build several; owners who would have rebuilt in the window wait, A-10) | A-10 | n/a |
| C-16 | owners.splittable, builders | investment_target (homes built on split lots, after approval) | increase | medium; long | visible | B | CR-4 (x: one home, y: several homes; y newly open and pays for some, A-5); CR-7a (A-1). Includes the rebuilds deferred from the window (C-15) | A-5, A-1 | none |
| C-17 | applicants.old_standard | quantity_supplied (two-lot splits approved under the old standard, 10 Mar to 10 Sep 2027) | decrease | short (window) | invisible | B | CR-10a and CR-4 (x: file the two-lot split under the old standard now, y: wait and file a redesigned split of three or four lots, reviewed under the new standard by R3; some hold back, A-9; without the repeal about 120 such splits a year go ahead) | A-9 | n/a |
| C-18 | applicants.splits | wait_time (approval, first months after 10 Sep 2027) | ambiguous | short | invisible | B | CR-12b: (-) R2's 60-day procedure replaces five months of plat review (CR-1 op 3); (+) applications filed early to hold a place in the queue (A-8, R3's order of receipt) meet the department's capacity on the effective date before fee-funded staff can be added (CR-6, 0.7 public supply; A-23). No premise says which dominates in the first months | A-8, A-23 | n/a |
| C-19 | owners.covenant_bound, HOAs | enforcement_cost (court time and parties' legal costs in covenant suits) | increase | short; medium | invisible | B | CR-4 (x: leave the question open, y: split and defend it, or sue to enforce; the split's value, C-1, and the value of the restriction to others, A-17, give both sides a stake, and the question is litigated, A-12); CR-8c (resources spent on litigation are used up). Until a court rules, both readings are live, so the sign does not depend on the reading | A-12 | n/a |
| C-20 | owners.covenant_bound.enforcing (owners who value large lots) | asset_value (right to enforce the covenants) | U1-a: no_change; U1-b: decrease | short | invisible | B | U1-b: CR-8 (0.7: a rule that voids a right one party held is a transfer; the holders lose the value of the right and the owners who want to split gain it, C-2); the right is worth something to those who rank light, privacy and lower density above their absence (A-17). U1-a: the right stands | A-17 | U1-a: n/a; U1-b: none |
| C-21 | owners.covenant_bound | term_prevalence (re-subdivision and large-lot covenants in force) | U1-a: decrease; U1-b: no_change | long (renewals 2030 to 2045) | invisible | B | U1-a: CR-4 (x: let the covenant renew, y: organize a majority to end it; the value of splitting, C-1, makes y better for owners who want to split, and in some subdivisions they can organize, A-13). U1-b: the covenants are unenforceable whether renewed or not, so renewal changes nothing | A-13 | U1-a: partial |
| C-22 | homeowner groups, builders | lobbying_effort (to restore a minimum or limit splits; to keep the repeal) | increase | short; medium | invisible | B | CR-4 (x: accept the repeal, y: seek a new minimum, A-17; builders, x: accept a return, y: defend the repeal); CR-8c (resources spent lobbying are used up); both groups can organize at a cost below their stake (A-14) | A-14, A-17 | n/a |
| C-23 | planning_department | enforcement_cost (review of split and subdivision applications) | increase | medium | invisible | B | CR-1 (R2 and R3 give the department 400 to 700 applications a year in place of about 60 variances, with similar review work each, A-23); CR-8c (review resources are used up) | A-23 | none |
| C-24 | planning_department | non_tax_receipts (application fees) | increase | medium | invisible | B | CR-1 (op 3: $4,800 per split); CR-8b (the fees applicants pay are received by the department, set to recover review costs, A-20); more applications, A-23 | A-20, A-23 | none |
| C-25 | applicants.new_splits | compliance_cost (fees, surveys, demolition and building permits) | increase | medium | invisible | B | CR-1 (op 3: fees and procedures attach to the newly open option); CR-8c (resources spent on complying are used up). The applicants chose to split (CR-3b), so this is a cost of their choice, not a loss by their own ranking | A-5 | none |
| C-26 | renters (households in rented apartments and townhouses) | price_substitute (rents of apartments and townhouses in Larkfield) | decrease | medium; long | invisible | B | CR-9 (relation: small-lot detached homes substitute for rented apartments and townhouses for some households, A-16; some renters buy, C-10); CR-6 (fewer renters at each rent move it toward a lower clearing level) | A-16, A-5 | partial |
| C-27 | landlords.apartments_townhouses | net_price_received (rent) | decrease | medium; long | invisible | B | As C-26, from the landlords' side | A-16, A-5 | partial |
| C-28 | households.commuting_in (work in Larkfield, would have bought outside) | travel_time | decrease | medium; long | invisible | B | CR-4 (x: buy in Brackwell or Tessmoor and commute, y: buy a small-lot home in Larkfield; y newly open at their price, A-15, C-9); CR-9 (relation: location complement between home and work) | A-15, A-5 | partial (households who moved away under the rule have bought there, A-24) |
| C-29 | neighboring_jurisdictions (Brackwell small-lot builders and landowners) | net_price_received (small lots and new small homes in Brackwell) | decrease | medium | invisible | B | CR-9 (relation: across_border substitute; some buyers who would have bought in Brackwell buy in Larkfield, C-28); CR-6 (fewer buyers at each price) | A-15, A-5 | partial |
| C-30 | neighboring_jurisdictions (owners of small lots in Brackwell and land in Tessmoor) | asset_value (land) | decrease | short; medium | invisible | B | CR-10c and CR-7c (the expected fall in yields, C-29, is borne by whoever owns the land when the repeal becomes expected, A-3) | A-15, A-5, A-3 | partial |
| C-31 | owners.modest_older_homes | quantity_supplied (older modest homes standing) | decrease | medium; long | invisible | B | CR-4 (x: keep the older home, y: demolish it to split the lot; y pays for some, A-5); CR-8a (the remaining services of the demolished home are given up) | A-5 | n/a |
| C-32 | buyers.modest_homes | price_paid (modest homes, older and new small-lot) | decrease | medium; long | invisible | B | CR-12b: (+) CR-6 (fewer older modest homes, C-31); (-) CR-9 and CR-6 (new small-lot homes are close substitutes, A-22, and more of them are built). Dominance (CR-12e, arithmetic): each demolition yields two to four homes in their place, so the number of close substitutes rises; buyers do not absorb them at unchanged prices (A-11) | A-22, A-5, A-11 | partial |
| C-33 | construction_input_suppliers | quantity_traded (construction labor and materials for homes in Larkfield) | increase | medium | invisible | B | CR-9 and LW-10 (relation: labor and materials input_to new homes; more homes are built, C-16) | A-5 | none |
| C-34 | city (general fund) | tax_revenue (property tax) | increase | medium; long | invisible | B | Arithmetic on a fixed rate: new homes and higher land values add more to the assessed base than the lower values of non-splittable homes remove (A-21); CR-8b (the added tax is paid by owners, C-35) | A-21 | partial |
| C-35 | owners of new homes and of splittable lots | resources_available_other_uses (property tax paid) | decrease | medium; long | invisible | B | CR-3 (note: a tax on assessed value is a sum the owner cannot avoid while holding the property); CR-8b (their added tax is the city's receipt, C-34; A-21) | A-21 | none |
| C-36 | owners.non_splittable | resources_available_other_uses (property tax paid) | increase | medium; long | invisible | B | Arithmetic on a fixed rate: lower assessed values (C-11, A-11) mean less tax (A-21) | A-11, A-21 | none |
| C-37 | neighbors (owners next to new small-lot homes) | asset_value (adjacent homes) | decrease | medium; long | invisible | C | CR-9 (relation: proximity; taller, closer homes next door take light and privacy that these owners rank above their absence, A-17); CR-7c (the expected loss is capitalized). Tier C pending the question whether proximity chains belong to the method | A-17 | none |
| C-38 | street users near small-lot homes | search_cost (on-street parking) | increase | medium; long | invisible | C | CR-9 (relation: shared_facility; some residents of new small-lot homes park on the street despite two off-street spaces, A-18, which leaves fewer spaces for others). Tier C | A-18 | none |

## Gaps found

**(a) Steps no core rule covers.** None. Every step was derived from CR-1 to CR-12, LW-10, and arithmetic on the case's figures. The metamorphic check needed no rule beyond the core rules: the original rule's effects were derived with CR-1 op 1 and the same responses, and persistence with CR-10b and CR-7c.

**(b) Core-rule wording that was hard to apply.**
- CR-10b says changes that cost something to undo persist, and CR-7c says asset prices adjust at once. Persistence for a repeal therefore splits by variable (prices: none; stocks: partial), which the persistence field records per consequence but CR-10b's wording does not state directly.
- CR-6's public-supply clause (0.7) covers a fixed quantity of service at a set price. Here the fee is set to recover costs, so capacity can grow with demand after a lag; whether that makes the department a public supplier with a fixed quantity (short run) or not (medium run) needed the added premise A-N1.
- CR-8 (0.7, voiding a contract right) is written for a right held by one party against another. A covenant is held by every owner against every other owner in a subdivision, so the same owners are both holders and bound parties; the class had to be split by what each would do (enforce or split), as CR-1's recording note allows, before the transfer could be signed.
- CR-10a and the normal form's timing-shift rule do not say how to sign filings made only to hold a place in a first-come queue that exists only because of the policy. Treated as a path note, entering through the wait at the effective date.

**(c) Vocabulary missing from the ontology.**
- No variable for private litigation costs; `enforcement_cost` (resources spent by the state) was stretched to cover the parties' legal costs (C-19).
- No variable for the number of lots or parcels as distinct from goods supplied; `quantity_supplied (new detached lots)` was used.
- No variable for applications filed or the size of an administrative queue; filings were left as a path note.
- No actor class for owners bound by a private covenant who also hold the right to enforce it; `owners.covenant_bound` and `owners.covenant_bound.enforcing` were introduced.
- No variable for loss of light, privacy or density as such; the proximity chain was recorded as `asset_value` of adjacent homes (C-37), Tier C.
