# WE-043 Repeal of a minimum lot size

Analyst: draft (Handbook 0.8 held-out test, corrected under 0.9)  |  Rule catalog version: 0.9  |  Status: awaiting expert review

A stylized repeal in a fictional city. Many cities have minimum lot sizes, and some have cut them; this one is not modeled on any of them. It is a held-out test of catalog 0.8 on a repeal for which no prior worked example of the original rule exists, so the metamorphic check (end of section 7) compares the repeal with what the original rule did, derived here from the core rules rather than taken from another example. The case probes TS-3's clause on product standards (a minimum lot size is a specification of new detached homes, with the existing stock exempt), CR-7c capitalization (land values of lots that become splittable against lots that do not), CR-10b's transition-only effects with `persistence` `n/a`, CR-9's proximity effects on neighbors at Tier C (Q20), RS-8's opposing timing chains in the announcement window, and `unit_size`. The unclear provision is whether private deed restrictions (covenants) that require large lots remain enforceable; the ordinance is silent. The counterfactual throughout is **the 6,000 square foot minimum stays in force**; every sign is relative to that path. `persistence` compares each consequence with the path on which the minimum was never imposed (TS-6). Effects on health, safety and the environment (impervious surface, tree cover) are out of scope for version 1. The probabilities are illustrative; the evidence column says what a real analysis would cite. Written under catalog 0.8 and corrected under 0.9 after its core-only re-run: what changed is listed in "Corrections after the core-only comparison"; the test of 0.8 (Gaps found, e) is kept as written.

## 1. Policy record

**Larkfield Lot Size Reform Ordinance.** Larkfield is a city of about 180,000 people in a metropolitan region of 2.4 million, where about 15,000 homes are built a year. It has about 41,000 detached homes, most in its two single-family zones, R-1 and R-2, which cover 68% of its residential land. Since its 1962 zoning code, a detached home in R-1 or R-2 has needed a lot of at least 6,000 square feet (sq ft) and 50 feet wide. The city assessor's lot count:

| Lot size | Lots | Can be split under the 6,000 rule? |
|---|---|---|
| Under 6,000 sq ft (platted before 1962; legal nonconforming) | 4,500 | No |
| 6,000 to 8,999 | 17,000 | No |
| 9,000 to 11,999 | 11,000 | No |
| 12,000 and over | 8,500 | Into two lots; about 120 such splits a year |

About 14,500 detached lots (35%), in subdivisions recorded between 1965 and 1995, carry recorded covenants that forbid re-subdividing a lot or require lots of at least 7,500 sq ft. Any owner in the subdivision, or its homeowners' association (HOA), can sue to enforce them. Each set renews every 25 years unless a majority of the owners vote to end it; the next renewals fall between 2030 and 2045.

Land on a typical R-1 lot trades at about $70 a sq ft. The median detached home sells for about $780,000 (about 2,100 sq ft of floor area on 7,500 sq ft of land); new detached homes average about 2,800 sq ft, about 250 a year, mostly rebuilds after demolition and two-lot splits of large lots. Neighboring Brackwell allows detached homes on 3,000 sq ft lots; builders there pay about $95 a sq ft for such lots, and new 1,600 sq ft homes on them sell for about $640,000. Tessmoor, on the other side, requires 8,000 sq ft. The planning department hears about 60 variance applications a year for homes on undersized lots and projects 400 to 700 split and subdivision applications a year under the new rules.

The ordinance was introduced on 15 November 2026, passed 7 to 2 on 10 March 2027, and takes effect on 10 September 2027, six months after passage. No referendum petition was filed. It has no expiry.

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| R1 Minimum lot | Removal of a `product_standard` (the specification is lot area per detached home) | New lots for detached homes in R-1 and R-2 | Owners and builders who subdivide or split | Minimum lot area falls from 6,000 to 1,500 sq ft, and minimum width from 50 to 20 feet. | None |
| R2 Split procedure | Change to an existing procedure | Splits into up to four lots | Planning department | Splits that meet the standards are approved administratively within 60 days (before: plat review of about five months for every split). Fee $4,800, set to recover review costs. Subdivisions of five or more lots still go through plat review. | — |
| R3 Pending applications | Transition rule | Applications filed after passage | Planning department | "Applications filed after the date of passage that are complete on the effective date shall be reviewed under the standards of this ordinance," in the order received. | — |
| R4 Existing homes | Saving clause | Existing lots and structures | — | "Nothing in this ordinance requires any change to an existing lot or structure." | — |

Existing rules, unchanged and in force on both paths: front setback 20 ft, side setbacks 5 ft, rear 15 ft; height 35 ft; lot coverage at most 50%; two off-street parking spaces per dwelling; one dwelling per lot. With these, the smallest practical detached lot is about 2,400 to 2,500 sq ft (25 by 100 feet).

Unclear provisions:
- **U1, covenants.** The ordinance does not mention private covenants. Reading U1-a: covenants requiring large lots or forbidding re-subdivision remain enforceable; the ordinance changes only what the city requires. Reading U1-b: the ordinance's stated purpose ("to allow lots down to 1,500 square feet throughout the residential zones") makes such covenants unenforceable as contrary to public policy. The state has no statute on the point and its courts have not ruled on it. Readings get no probability; where a sign depends on one, each reading's sign is reported.

## 2. Classification

| Component | Rothbard type | Binding? | Rule families |
|---|---|---|---|
| R1 | Removal of a triangular intervention: the 6,000 rule forbade exchanges between builders and buyers of detached homes on smaller lots. CR-1: adds an option (operation 2), dated 10 September 2027; before that date it acts only through expectations (CR-10a), while land values move at once (CR-7c; CR-1, 0.8 clarification on dated operations). The counterfactual law keeps the 6,000 minimum. | The old minimum binds on many lots of 6,000 to 12,000 sq ft (A-1). The new 1,500 minimum binds on almost no designs, because the existing setback and parking rules bind first (A-4): the repeal makes those existing rules the binding ones. | TS-3 (product standards), EN-14 (in reverse), CR-1, CR-4, CR-7c, RS-13, RS-16, RS-4, OC-4 in reverse, TS-1, TS-5, TS-6 |
| R2 | Lowers the cost of the newly added option (CR-1, operation 3, a burden reduced) for splits of up to four lots only; projects of five or more keep plat review, so the operation differs on either side of a size threshold (CR-1, 0.9) | Yes | CR-4, CR-6, OC-2, OC-3, RS-17 |
| R3 | Transition rule: improves filing in the window | Yes, for applications filed after passage | RS-8 (Unless clause) |
| R4 | Saving clause: no operation on existing lots | — | — |
| U1 | U1-a: covenant-bound lots stay unsplittable; the covenant, not the city, becomes the binding rule. Covenants are enforced only when an owner or HOA sues (RS-20). U1-b: covenants are voided. Every owner both held the right to enforce and was bound by it, so this is not a transfer between classes: each owner loses the right to enforce and gains freedom from enforcement, including the option of splitting (CR-8, 0.9, mutual rights). | Per reading | CR-1, CR-8, CR-7c, RS-7, RS-20 |

The ordinance collects no tax and pays no subsidy. Its transfers are revaluations of land (C-1, C-11, C-16, C-30, C-33), realized only when land is sold (C-24, C-25); application fees, paid by applicants (C-27) and received by the department (C-31); and property tax on the changed values, paid by owners (C-36, C-37) and received by the city (C-28). Under U1-b the voiding of the covenants is not a transfer between classes (CR-8, 0.9, mutual rights; section 5).

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `owners.splittable` (`factor_owners.specific`) | Owners of lots of about 5,000 sq ft or more, not covenant-bound, that can be split under the new rule but not the old | May split from the effective date; land value moves when the repeal becomes expected. |
| `owners.large_lot` | Owners of lots of 12,000 sq ft or more (could already split into two) | May now split into three or four. Included in `owners.splittable` below unless named. |
| `owners.covenant_bound` | Owners of the 14,500 lots under covenants | U1-a: cannot split; U1-b: may split, and lose the right to stop neighbors splitting. |
| `owners.non_splittable` | Owners of conforming homes on lots too narrow or oddly shaped to split | Nothing new for them; face more competing homes. |
| `owners.nonconforming` | Owners of the 4,500 lots under 6,000 sq ft (platted before 1962) that cannot be split | Their lots now conform: no variance needed to rebuild or enlarge; face more competing homes. |
| `applicants.variance` | Owners who would have applied for a variance to build on an undersized lot | No longer need one. |
| `applicants.splits` | Applicants for splits of up to four lots | Administrative approval within 60 days instead of plat review of about five months. |
| `builders` (`sellers.current`) | Firms building detached homes in Larkfield | May build on smaller lots. |
| `builders.small` (`sellers.prospective`) | Small and new builders | Two-to-four-lot splits with a 60-day approval suit small projects. |
| `buyers.prospective` | Households looking for a detached home in Larkfield | More, smaller, cheaper homes on offer. |
| `buyers.lots` | Builders and households who buy splittable lots after passage | Pay a price that reflects the option to split. |
| `renters` (`buyers.substitutes`) | Households renting apartments and townhouses in Larkfield | Some neighbors in the rental market move to small-lot homes. |
| `landlords` | Owners of rented apartments and townhouses in Larkfield | Some tenants move to small-lot homes. |
| `construction_input_suppliers` | Construction workers and materials suppliers | More homes built in Larkfield. |
| `neighboring_jurisdictions` | Builders, sellers and landowners in Brackwell and Tessmoor | Some buyers who would have gone there buy in Larkfield. |
| `neighbors` | Owners next to lots that are split, whether their own lots can be split or not | New homes next door: light, privacy, street parking (`proximity`, `shared_facility`). |
| `hoas` | Homeowners' associations that enforce covenants | U1-a: covenants now do what the city rule did; U1-b: covenants voided. |
| `homeowner_groups`, `builders` (as lobbies) | Organized interests on the minimum | Lobbied in both worlds. |
| `officials.enforcement` | Planning department | Reviews splits instead of variances; funded by fees. |
| City budget: `taxpayers`, recipients of city spending | Those who fund and receive city spending | More homes add to the tax base and to demand for services. |

## 4. Direct effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | `owners.splittable` | `asset_value` (land of lots splittable under the new rule; not counting effects through `proximity`) | increase | short (from November 2026, fully at passage) | CR-1, CR-7c, CR-10c, CR-12e | A-1, A-2, A-3 |
| C-2 | `builders` | `specification_level` (lot area of new detached lots) | decrease | medium | TS-3, CR-1, CR-4 | A-1, A-4 |
| C-3 | `builders` | `quantity_supplied` (new detached homes in R-1 and R-2, from the effective date) | increase | medium–long | CR-4, CR-7a, TS-1, TS-5 | A-1, A-3, A-5 |

The visible effects are that owners of splittable lots gain (C-1), and that new lots are smaller (C-2) and more homes are built (C-3). C-1 dates from when the repeal became expected: part of the way from the introduction in November 2026, as passage became likely, and the rest at passage in March 2027 (CR-7c's probability clause), not from the effective date. Its sign needs a dominance premise (section 7). It is signed at Tier B without the proximity chain; for owners next to split lots the combined sign is C-38, at Tier C (CR-12, 0.9).

**Binding, before and after (TS-3, product standards).** A minimum lot size has no clearing price to move past. It binds on the share of lots builders would choose to make below it (CR-1, CR-4 over the spread of designs). Builders in Brackwell pay about $95 a sq ft for small lots against about $70 in Larkfield, so a 9,000 sq ft lot is worth about $630,000 as one lot and up to about $855,000 as three of 3,000 (less demolition and fees), which is why the old rule binds on many lots (A-1). The new 1,500 minimum binds on almost no designs: with the setback and parking rules, which stay, the practical minimum is about 2,500 sq ft (A-4). So C-2 is the change in the lots builders choose, not a fall to the new minimum.

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-4 | `owners.splittable` | `quantity_supplied` (buildable lots from splits and subdivisions) | increase | short–medium (from the effective date) | CR-4, CR-7a | A-1, A-5 |
| C-5 | `builders` | `unit_size` (floor area per new detached home) | decrease | medium | CR-4, CR-5c | A-1, A-6 |
| C-6 | `builders.small` | `entry_rate` | increase | medium | CR-4, CR-7a | A-5, A-7 |
| C-7 | `owners.splittable`, `builders` | `quantity_traded` (split and subdivision applications filed, March to September 2027) | ambiguous | short (announcement window) | RS-8, CR-12b | A-8, A-9 |
| C-8 | `owners.splittable`, `builders` | `quantity_traded` (split and subdivision applications filed, from the effective date) | increase | short–medium | RS-8, CR-4, CR-12e | A-1, A-5 |
| C-9 | `owners.splittable`, `builders` | `quantity_supplied` (detached homes started on splittable lots, in the window) | decrease | short (announcement window) | RS-8, CR-10a | A-10 |
| C-10 | `owners.splittable` | `units_held_vacant` (older homes on splittable lots, awaiting the effective date and approval) | increase | short | CR-10a, CR-4 | A-10 |
| C-11 | `owners.covenant_bound` | `asset_value` (covenant-bound lots and homes) | ambiguous | short–medium | CR-7c, CR-10c, RS-13, RS-20, CR-8, CR-12b | A-3, A-11, A-13, A-27 |
| C-12 | `hoas`, `owners.covenant_bound` | `compliance_cost` (litigation over whether covenants survive) | increase | short–medium | CR-4, CR-8c | A-12 |
| C-13 | `owners.covenant_bound` | `lobbying_effort` (campaigns to amend or end covenants) | U1-a: increase; U1-b: no_change | medium | CR-4, RS-7 | A-13 |
| C-14 | `homeowner_groups`, `builders` | `lobbying_effort` (at the city: to restore or defend the repeal) | ambiguous | medium | RS-7 (repeal clause), CR-4 | A-14 |
| C-15 | `buyers.prospective` | `cross_border_purchases` (homes bought in Brackwell and Tessmoor by households working in Larkfield) | decrease | medium–long | RS-4 | A-15 |
| C-29 | `applicants.variance` | `compliance_cost` (variance applications for undersized lots) | decrease | short–medium (from the effective date) | CR-1, CR-8c | none |
| C-39 | `applicants.splits` | `wait_time` (approval of splits of up to four lots) | decrease | medium | CR-1, CR-6 | A-20, A-23, A-26 |
| C-40 | `owners.covenant_bound` | `legal_breach` (splits in breach of covenants that no owner or HOA challenges) | U1-a: increase; U1-b: no_change | medium | RS-20, CR-4 | A-12, A-27 |
| C-41 | `owners.large_lot`, `builders` | `reclassification` (projects kept at four lots or fewer, or divided into successive splits, to avoid plat review) | increase | short–medium | RS-17, CR-1, CR-4 | A-5, A-28 |

**Owners and builders (C-4 to C-6).** CR-4 (x: keep one lot, y: split): owners whose lots are worth more as several lots than as one, net of demolition, fees and the wait, split or sell to builders who do (C-4; A-5). Most splits of 6,000 to 9,000 sq ft lots need the existing house to be demolished, so the first to be split are older, smaller houses on wide lots and large lots with room beside the house. Buyers who could not obtain a detached home in Larkfield at any lot size below 6,000 can now trade land for price (CR-5c), so builders offer smaller homes on smaller lots: with coverage and height limits, a home on 2,500 sq ft carries about 1,400 to 1,800 sq ft of floor area, against 2,800 for the average new home now (C-5, A-6). Splits of two to four lots, approved in 60 days, suit small builders, who enter (C-6, A-7). Owners who would have split anyway under the old rule (about 120 two-lot splits a year) wait less for approval once the department's fee-funded capacity catches up with the new applications (C-39; CR-6's 0.9 clause on a public supplier whose capacity grows after a lag: until it does, the queue is rationed by waiting, and the first months are not signed). Owners who would have applied for a variance to build on an undersized lot no longer need one (C-29; CR-1, a burden removed). R2's threshold at four lots is a size threshold (RS-17): owners of parcels large enough for five or more lots keep projects at four, or divide them by successive splits, where plat review costs more than the extra lot is worth (C-41, A-28).

**Timing in the announcement window (C-7 to C-10).** Two timing chains reach the applications filed between passage and the effective date. Both are signed on the flow of filings in the window.
- (−) Applications that would have been filed in the window under the 6,000 rule (two-lot splits of large lots, subdivisions of large parcels) are held back to be redesigned for smaller lots (RS-8, x: file now under the old standard, y: file later under the new; A-9).
- (+) R3 decides applications filed in the window under the new standards, in the order received, if they are complete on the effective date. Filing in the window is therefore not worse than filing after it, and gets a place in the queue: applications that would have been filed after the effective date are pulled into the window (A-8). These filings exist only because of the repeal, so against the counterfactual they are an increase in the window (CR-12, 0.9, activities that exist only under the policy).

R3 improves the earlier window, which is RS-8's Unless case: the two chains oppose each other and there is no dominance premise, so C-7 is `ambiguous`. From the effective date the new option raises applications above the counterfactual (C-8). The pull-forward is drawn only from applications that exist because of the repeal, and the held-back old-standard ones are filed then too, so the pull-forward cannot bring filings after the effective date below the counterfactual (CR-12e, the response argument). The response is partial, as CR-12's 0.9 clarification requires for `increase`: only applications ready within six months can be pulled forward, while the department projects 400 to 700 a year from then on (A-23). Building permits are not covered by R3: an owner who would have built or rebuilt one house on a splittable lot in the window waits to split (C-9), and some older houses that would have been re-let are left empty until the split is approved (C-10; A-10). C-7, C-9 and C-10 exist only during the transition, so their `persistence` is `n/a` (CR-10b).

**Covenants (C-11 to C-13, C-40).** Under U1-a, covenant-bound owners get no new option now. Their homes compete with more homes elsewhere in the city (RS-13, C-16's chain; −). Against that, two chains push up. Ending a covenant at its renewal (2030 to 2045) or by petition now opens a split, where on the counterfactual path it opens nothing for most lots; that expected option is capitalized now (CR-7c, CR-10c; A-13, the same premise as C-13). And covenants are enforced only when an owner or HOA sues, so in subdivisions where no one is likely to sue, some lots can in practice be split (RS-20; A-27). These are kind (2) chains whose premises clear the cut-off, so the sign is `ambiguous` (C-11). The covenant, which duplicated the city rule for most lots, is now the rule that binds. Under U1-b each owner gains the option to split (+), faces the competition chain (−), and loses the right to stop neighbors splitting while gaining freedom from their enforcement: every owner both held the right and was bound by it, so this is not a transfer between classes, and its net value per owner needs a premise on which they value more (CR-8, 0.9, mutual rights). A-2, estimated for unbound lots, does not cover that item. No premise ranks these chains for the class, so the sign is `ambiguous` under both readings. Under either reading, owners who want to split test the covenants and HOAs sue to enforce them, until a court rules (C-12; A-12). Under U1-a, splits that no one challenges are breaches of the covenants within the legal market, concentrated where suits are least likely (C-40; RS-20), and neighbors who can sue gain a bargaining threat; owners who want to split campaign to end their covenants at the next renewal or by petition (C-13; A-13); under U1-b there is nothing to amend or breach.

**Lobbying (C-14).** RS-7's repeal clause applies, with CR-4's 0.9 clarification: the old rule was contested on the counterfactual path, so lobbying is signed against that path and needs a premise. Homeowner groups lobbied to keep the minimum on the counterfactual path, and builders and housing advocates to repeal it. After the repeal, homeowner groups lobby to restore it and builders to defend the repeal. Each class lobbied in both worlds, so the change in each is `ambiguous` without a premise.

**Relocation (C-15).** Some households who work in Larkfield bought in Brackwell, where small lots are allowed, or in Tessmoor, because Larkfield had no detached homes at their price (RS-4; A-15). Some now buy in Larkfield instead.

**Credibility (TS-5).** Splits of two to four lots, approved in 60 days and sold within a year, go ahead if owners expect the repeal to last a few years (A-3, p = 0.75). Larger subdivisions, which take a plat review and several years to sell out, would be held back further if developers feared the minimum's return; that premise is A-25 (p = 0.4), below the cut-off, so it is not reported.

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-16 | `owners.non_splittable` | `asset_value` (conforming homes on lots that cannot be split) | decrease | short–medium | EN-14, CR-7c, RS-13, CR-9 | small-lot homes and existing homes: `same_market_other_segment`, partial | A-3, A-11 |
| C-17 | `buyers.lots` | `price_paid` (splittable lots bought after passage) | increase | short–medium | SB-4, OC-7 | sale of lots | A-1, A-3 |
| C-18 | `buyers.prospective` | `price_paid` (entry-level detached homes in Larkfield, existing and new) | decrease | medium–long | RS-13, CR-12e | as C-16 | A-5, A-11, A-22 |
| C-19 | `renters` | `price_substitute` (rents of apartments and townhouses in Larkfield) | decrease | medium–long | RS-16 (mirror case), RS-13 | small-lot homes and rentals: `substitute`, partial | A-11, A-16 |
| C-20 | `neighboring_jurisdictions` | `quantity_supplied`, `net_price_received` (homes sold in Brackwell and Tessmoor to households working in Larkfield) | at_least_one_decrease | medium–long | RS-4, CR-9, CR-6 | Larkfield and neighbors: `across_border`, partial | A-15 |
| C-21 | `neighbors` (on lots that cannot be split) | `asset_value` (homes next to new small-lot homes) | decrease | medium | CR-9 | `proximity` (Tier C, Q20) | A-17 |
| C-22 | `neighbors` | `search_cost` (street parking near new small-lot homes) | increase | medium | CR-9 | `shared_facility` (Tier C, Q20) | A-18 |
| C-23 | `buyers.prospective`, `owners.splittable` | `quantity_traded` (sales of detached homes and lots in Larkfield) | increase | medium–long | OC-4 in reverse, CR-5 | — | A-1, A-5 |
| C-30 | `owners.nonconforming` | `asset_value` (lots under 6,000 sq ft that cannot be split, and their homes) | ambiguous | short–medium | CR-1, CR-3, CR-7c, RS-13, CR-12b | as C-16 | A-3, A-11 |
| C-32 | `landlords` | `net_price_received` (rents of apartments and townhouses in Larkfield) | decrease | medium–long | RS-16 (mirror case), CR-9, CR-6 | as C-19 | A-11, A-16 |
| C-33 | `neighboring_jurisdictions` (landowners in Brackwell and Tessmoor) | `asset_value` (land) | decrease | short–medium | CR-7c, CR-10c, CR-9 | as C-20 | A-3, A-15 |
| C-34 | `owners.splittable` (older modest homes) | `quantity_supplied` (older modest homes standing) | decrease | medium–long | EN-14, CR-4, CR-8a | — | A-5 |
| C-35 | `construction_input_suppliers` | `quantity_traded` (construction labor and materials used for homes in Larkfield) | increase | medium | CR-9 | construction labor and materials `input_to` new homes | A-5 |
| C-38 | `neighbors` (owners of splittable lots next to split lots) | `asset_value` (combined, counting effects through `proximity`) | ambiguous | medium | CR-9, CR-12b | `proximity` (Tier C, Q20) | A-2, A-17 |

**Capitalization (C-1, C-11, C-16, C-17).** The repeal changes the expected yields of land in three ways, and each is capitalized when the repeal becomes expected (CR-7c, CR-10c), not when it takes effect.
- *Splittable lots (C-1).* (+) The option to split is added. (−) Every owner faces more competing homes, as splits add supply (C-3, RS-13). For an owner who splits, the competition lowers the price of each small lot. For one who does not, it lowers the value of the home as it stands. CR-12e's response argument does not settle this. Splitting as a whole cannot close the gap between small-lot and large-lot land that drives it, but the 0.8 clarification says the argument binds the response as a whole, not each member: owners at the margin, who do not split, can end up worse off. The sign for the class rests on an empirical dominance premise (A-2): Larkfield's 400 to 700 extra homes a year are small against the region's 15,000, so the price effect is small, while land is more than half the value of these lots.
- *Conforming lots that cannot be split (C-16)*: only the competition chain applies, so values fall (A-11). This is EN-14 in reverse: the stock that the standard protected from cheaper new units now faces them.
- *Nonconforming lots (C-30)*: the 4,500 lots under 6,000 sq ft now conform, so owners can rebuild or enlarge without a variance (CR-1, operation 3, a burden removed; CR-3b), which raises their value, while the competition chain lowers it. No dominance premise: `ambiguous`.
- *Covenant-bound lots (C-11)*: section 5, `ambiguous` under both readings.
- *Land in Brackwell and Tessmoor (C-33)*: fewer Larkfield buyers lower the expected yield of land there, capitalized when the repeal became expected (CR-7c, CR-10c; A-15).
- *Buyers after passage (C-17)* pay the higher price for splittable lots, so they neither gain nor lose from the repeal as it stands (SB-4); the seller's gain is their outlay (OC-7, C-24, C-25).

**Entry-level prices (C-18).** Two chains. (−) New small-lot homes add supply (RS-13). (+) Each demolition removes an older, modest home, often among the cheapest detached homes in the city (C-34: the stock of older modest homes falls, the reverse of EN-14's clause that a standard keeps existing units in use longer). Each demolition makes room for two to four new homes, so the count of homes rises with every teardown-and-split. That is an accounting identity, and with the premise that the new small homes are close substitutes for the older modest ones (A-22), it decides the sign (CR-12e). Decrease.

**Rents and neighbors (C-19, C-20).** Some renters buy small-lot homes (RS-16, mirror case: the good becomes more available, so demand for its substitute falls); rents are lower than they would have been where rental supply cannot contract at once (A-16; rented buildings are durable, CR-10b), and landlords receive less (C-32). Builders in Brackwell and Tessmoor face fewer Larkfield buyers: by CR-6's 0.9 clarification, how that divides between fewer sales and lower prices needs a premise on their supply, so the two are recorded as a group (C-20).

**Proximity (C-21, C-22), Tier C.** New homes on split lots change the situation of the owners next door without any exchange with them: less light and privacy, more people using the street. CR-9's 0.7 clarification records this as `proximity` and, for street parking, `shared_facility`, and reports chains through them at Tier C until the experts decide Q20. The sign also needs a premise about what the neighbors value, which the rules never assume: that owners who chose large-lot zones rank lower density, light and privacy above their absence (A-17), and that some new residents park on the street despite two off-street spaces (A-18). Some neighbors may value the change the other way (more neighbors, more young families); the premise covers the class at the stated probability. Both are reported at Tier C. CR-12's 0.9 clarification on Tier C against Tier B decides how the proximity chain meets the Tier B chains on owners' values. For neighbors whose own lots cannot be split, it has the same sign as C-16, so C-21 is a decrease at Tier C and C-16 stands at Tier B. For neighbors whose own lots can be split, it opposes C-1: C-1 is kept at Tier B, qualified "not counting effects through `proximity`", and the combined sign is recorded at Tier C as `ambiguous` (C-38), since no premise ranks the option against the loss of light and privacy.

**Freed exchanges (C-23).** Sales of small lots and of homes on them, which the 6,000 rule prevented, now take place, and each party expects to gain from them (OC-4 in reverse, CR-5).

**Construction (C-35).** More homes built in Larkfield draw construction labor and materials there (CR-9 with LW-10, `input_to`, depth 2); where they are drawn from is not signed without a premise (CR-8a).

**Stopping points.** Schools, sewers and roads used by new residents are `shared_facility` relations, reported only as Tier C if signed; their capacity costs fall on the city budget (section 9), which is not netted against the added tax base (CR-12c). Furniture and moving services bought by new residents: depth 3, diffuse; stopped. Sellers of homes in Brackwell and Tessmoor (C-20) lead to their own buyers at depth 3; stopped.

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `owners.splittable`, `asset_value`, short | The option to split (CR-1, CR-3b, CR-7c). | More competing homes (RS-13; A-11). Tier C: proximity, for owners next to split lots (A-17). | A-2, an empirical premise (CR-12e). The response argument does not apply to each member (CR-12e, 0.8). Nothing covers the proximity chain. | **increase** (C-1), Tier B, not counting effects through `proximity`; without A-2, `ambiguous`. For owners next to split lots, counting proximity: **ambiguous**, Tier C (C-38). |
| `owners.covenant_bound`, `asset_value`, short–medium | U1-a: the option opened by ending a covenant at renewal or by petition (A-13); splits no one challenges (RS-20; A-27). U1-b: the option to split now; freedom from neighbors' enforcement. | Competition (both readings). U1-b: the right to stop neighbors splitting ends (CR-8, 0.9, mutual rights). | None: kind (2) chains with p of at least 0.5 under U1-a; under U1-b, A-2 does not cover the mutual right. | **ambiguous** (C-11), under both readings. |
| `owners.nonconforming`, `asset_value`, short–medium | Conforming status: no variance to rebuild or enlarge (CR-1, CR-3b). | Competition (A-11). | None | **ambiguous** (C-30). |
| `buyers.prospective`, `price_paid` (entry-level detached), medium–long | Teardowns remove older modest homes. | New small-lot homes add supply (RS-13). | Accounting identity: each teardown adds two to four homes for one removed; with A-22 (CR-12e). | **decrease** (C-18). |
| `owners.splittable`, `builders`, `quantity_traded` (applications filed), window | R3 pulls applications into the window to queue (A-8). | Old-standard applications held back to redesign (A-9). | None (RS-8, Unless clause) | **ambiguous** (C-7). |
| Same, from the effective date | The new option (CR-4); held-back applications filed. | Applications pulled into the window. | CR-12e, response argument: the pull-forward is drawn only from filings the repeal creates. | **increase** (C-8). |
| `officials.enforcement`, `enforcement_cost`, short–medium | Review of 400 to 700 split and subdivision applications a year. | About 60 variance hearings a year for undersized lots end (OC-3, the right baseline). | Arithmetic on the case's figures (CR-12e), with the department's projection (A-23). | **increase** (C-26). |
| `owners.splittable`, `builders`, `compliance_cost`, short–medium | Fees, surveys and plats for 400 to 700 splits a year. | Faster, administrative approval for the splits that would have been made anyway (about 120 a year). | Arithmetic on the case's figures (CR-12e), with A-23. The variance saving belongs to another class and is recorded on its own (C-29; CR-1, recording; CR-12c). | **increase** (C-27). |
| `officials.enforcement`, `non_tax_receipts` (fees), medium | Fees on 400 to 700 applications a year. | Fees on about 60 variance applications a year end. | Arithmetic on the case's figures (CR-12e), with A-23. | **increase** (C-31). |
| `applicants.splits`, `wait_time`, medium | More applications against the department's capacity. | The 60-day procedure; fee-funded staff added after a lag (CR-6, 0.9). | A-26, an empirical premise. | **decrease** (C-39). The first months are not signed. |
| `homeowner_groups`, `builders`, `lobbying_effort`, medium | Each lobbies for or against restoring the minimum. | Each lobbied over the minimum on the counterfactual path. | None (RS-7, repeal clause; CR-4, 0.9) | **ambiguous** (C-14). |
| `owners.splittable` who keep their lots, `resources_available_other_uses`, medium–long | — | Higher property tax on higher assessed values (A-21). | — | **decrease** (C-36). Sellers (C-24) are a different class. |

**A chain no rule derives.** That small-lot homes change "the character" of neighborhoods and so the demand for homes in Larkfield as a whole is suspected in the council debate, but it rests on what buyers value, which the rules never assume; it is not a chain (CR-12, 0.7). C-21 and C-22 state the part that can be derived, at Tier C.

**Different variables are not netted (CR-12c).** The lower floor area per new home (C-5) and the lower price of entry-level homes (C-18) are separate consequences: some of the lower price is a smaller home, which the method does not separate from a lower price for the same home. Nor are different classes: split applicants' costs (C-27) and the variance applicants' saving (C-29) are recorded separately, and so are non-splittable owners' lower values (C-16) and lower property tax (C-37).

### Metamorphic check against the original rule (derived)

There is no worked example of the 6,000 rule. Its consequences against a Larkfield that never had it are derived here from the core rules, using the same figures, as the original analysis would have found them (workflow, "Analyzing a repeal", 0.9); the rule is EN-14's case, a standard on new units with the stock exempt. Then each is compared with the repeal. "Reverses" means the repeal's sign is the opposite. **Persistence** (TS-6) is how much of the original's effect remains after the repeal, against the path on which the rule was never imposed.

| Original rule (derived) | Derivation | Repeal (this example) | Reverses? | Persistence (TS-6) | Reason |
|---|---|---|---|---|---|
| `builders`, `specification_level` (lot area of new lots): increase | TS-3 (product standards): binds on the share of lots that would have been made below 6,000; small in 1962, larger as land prices rose (CR-10a) | decrease (C-2) | Reverses | partial | Lots platted at 6,000 or more stay large until split; most are not (A-24). |
| `builders`, `unit_size` (floor area per new home): increase | CR-4: on a large lot, builders put the larger home buyers will pay for (A-6 mirrored) | decrease (C-5) | Reverses | partial | Homes built under the rule keep their size (A-24). |
| `builders`, `quantity_supplied` (detached homes): decrease | CR-1 (op 1), CR-5a, CR-4 | increase (C-3, C-4) | Reverses, slowly | partial (medium); partial (long) | New supply comes at the speed of splits and building (TS-1, upward clause); 65 years of large-lot platting are reversed lot by lot. |
| `buyers.prospective`, `price_paid` (detached homes): increase | RS-13 in reverse (supply withheld), CR-6 | decrease (C-18) | Reverses | partial | Follows the stock. |
| `owners` of conforming homes that cannot be split, `asset_value`: increase (protection from competing small-lot homes), captured in 1962 | EN-14, CR-7c, CR-10c | decrease (C-16) | Reverses for the asset | partial | The value follows the stock it depends on (CR-7, 0.9; EN-14): the stock of competing small-lot homes stays short of the never-imposed path for decades, so these homes stay worth more than on that path. (The persons also differ: the gain was captured in 1962, and the repeal's loss falls on owners now, SB-4.) |
| Owners of land that could have been split, `asset_value`: decrease (option removed), in 1962 | CR-1 (op 1), CR-7c | increase (C-1) | Reverses for the asset | none | The option is restored in full, and the shortfall in the stock of small-lot homes that persists raises what the option is worth rather than lowering it, so none of the original decrease remains. |
| Owners of nonconforming lots, `asset_value`: ambiguous (protection from competition against the variance burden) | CR-1 (op 3), CR-7c, CR-12b | ambiguous (C-30) | Ambiguous both ways | n/a | No sign to persist. |
| Covenant-bound lots, `asset_value`: increase as for other protected homes, the covenant being redundant | CR-7c | ambiguous (C-11) | Does not reverse in sign | U1-a: full until renewal votes, partial after; U1-b: none | Under U1-a the covenants carry the rule on until owners vote to end them. |
| `buyers.prospective`, `cross_border_purchases`: increase | RS-4 | decrease (C-15) | Reverses | partial | Households who moved to Brackwell and Tessmoor have bought there and mostly stay (A-24, `reversal_cost`). |
| `neighboring_jurisdictions`, `quantity_supplied`, `net_price_received`: at least one increase | RS-4, CR-9, CR-6 | at least one decrease (C-20) | Reverses | partial | As above. |
| `neighboring_jurisdictions` (landowners), `asset_value`: increase | CR-7c, CR-9 | decrease (C-33) | Reverses | partial | Follows the stock of Larkfield homes (CR-7, 0.9). |
| `renters`, `price_substitute`: increase; `landlords`, `net_price_received`: increase | RS-16 | decrease (C-19, C-32) | Reverses | partial | Follows the stock. |
| Older modest homes standing: increase (kept in use longer) | EN-14, CR-10b | decrease (C-34) | Reverses | partial | Demolitions follow splits, one lot at a time. |
| Construction labor and materials used in Larkfield: decrease | CR-9 | increase (C-35) | Reverses | none | A flow. |
| Property tax base: decrease; tax on non-splittable homes: increase | CR-8b, CR-9 (A-21 mirrored) | increase (C-28); owners keeping splittable lots pay more (C-36), non-splittable owners less (C-37) | Reverses | partial | Follows assessed values, which follow the stock. |
| `builders.small`, `entry_rate`: decrease | CR-4 (no small projects) | increase (C-6) | Reverses | none | A flow. |
| Small lots and homes on them, `quantity_traded`: decrease (prevented exchanges) | OC-4, CR-5a | increase (C-23) | Reverses | partial | Follows the stock. |
| `applicants.variance`, `compliance_cost` (variance applications): increase; `officials.enforcement`, `enforcement_cost` (variance hearings): increase | OC-2, OC-3 | decrease for variance applicants (C-29); the department's variance hearings end, inside C-26 | Reverses | none | A flow. Split review is a separate effect of the repeal (next to last row), not a failure of this item to reverse. |
| `homeowner_groups`, `lobbying_effort` (to keep the rule): increase | RS-7 | ambiguous (C-14) | Does not reverse | n/a | RS-7, repeal clause: each class lobbied in both worlds. |
| `neighbors`, `asset_value` (protection from small-lot homes next door): increase, Tier C | CR-9 (proximity) | decrease, Tier C, for neighbors who cannot split (C-21); ambiguous, Tier C, for neighbors who can (C-38) | Reverses for those who cannot split | partial | Applies only where lots next door are split. |
| Covenants requiring 7,500 sq ft or no re-subdivision: binding only between 6,000 and 7,500 sq ft, otherwise duplicating the rule | CR-1 | U1-a: covenants become the binding rule for 35% of lots, enforced only on suit; U1-b: voided | Per reading | U1-a: full until renewal votes, partial after (C-13); U1-b: none | Under U1-a the original rule's effect on these lots is carried on by private contract until owners vote to end it. |
| — | — | Split review and its fees, and the faster procedure (C-26, C-27, C-31, C-39; R2); projects kept at four lots (C-41) | No counterpart | n/a | Effects of the repeal's own procedure. |
| — | — | Window effects (C-7, C-9, C-10), covenant litigation and breach (C-12, C-13, C-40), lots bought after passage (C-17) | No counterpart | n/a | Transition effects and effects of the repeal's own terms. |

The check finds no sign that fails to reverse without a stated reason. What does not reverse is the stock: 65 years of large lots and large homes, and households who moved away. Asset values persist as far as the stock they depend on does (CR-7, 0.9): partly for homes that cannot be split, not at all for splittable land. That the capital gains and losses of 1962 fell on other persons than the repeal's do is a point about who bears them, not about persistence.

## 8. Time structure

- **Introduction to passage (November 2026 to March 2027).** Land values of splittable lots rise, and those of homes that cannot be split fall, part of the way as passage becomes likely (C-1, C-16; CR-7c). Covenant-bound lots move according to how buyers read U1 and the chance of ending covenants at renewal (C-11). Land in Brackwell and Tessmoor loses value (C-33).
- **Announcement window (March to September 2027).** Applications under the old standard are held back while applications under the new are filed early to queue (C-7, ambiguous). Owners who would have built one house on a splittable lot wait (C-9), and some leave older houses empty until a split is approved (C-10). These effects have no lasting stock: `persistence` `n/a` (CR-10b). Lots change hands at prices that already reflect the option (C-17).
- **From the effective date.** Applications rise (C-8); the first two-to-four-lot splits are approved within 60 days, and homes on them follow over one to two years (C-3, C-4). Covenant litigation runs until a court decides U1 (C-12); under U1-a, splits no one challenges go ahead in breach (C-40). The department's queue is longest in the first months; once fee-funded staff are added, splits are approved faster than under plat review (C-39). Variance applications end (C-29).
- **Medium to long run.** New homes are built at the speed of splits, demolitions and construction, not as a mirror of the 65 years in which large lots were platted (TS-1, upward clause; TS-6). Prices and rents fall below the counterfactual path as the stock grows (C-18, C-19, C-32), older modest homes are demolished (C-34), and construction in Larkfield rises (C-35).
- **Erosion and future binding (TS-3, product standards).** The share of lots on which the 6,000 rule bound grew over the decades as land prices rose. The new 1,500 minimum binds on almost no designs now (A-4); it would begin to bind if the parking or setback rules were relaxed, or as land prices keep rising and builders want narrower lots.
- **Costs already incurred.** Variance applications already paid for and homes already built under the 6,000 rule are the same with and without the repeal, so they are not consequences of it (CR-10b); they enter only through what they make cheaper or dearer next (the persistence column).

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-24 | `owners.splittable` (those who sell lots or part of a lot) | `resources_available_other_uses` | increase | Nothing given up: the gain in land value is realized when the land is sold. | OC-7, CR-8b |
| C-25 | `buyers.lots` | `resources_available_other_uses` | decrease | What the higher price of a splittable lot would otherwise have bought. | OC-7, CR-8b |
| C-26 | `officials.enforcement` | `enforcement_cost` (review of splits and subdivisions, net of variance hearings) | increase | Planning staff time, paid by application fees (A-20), so it reduces what the fees' payers have, not taxpayers' means. | OC-3, CR-12e |
| C-27 | `owners.splittable`, `builders` | `compliance_cost` (fees, surveys, plats for splits) | increase | The other uses of that money and time. | OC-2, CR-8c, CR-12e |
| C-28 | City budget | `tax_revenue` (property tax) | increase | Nothing given up by the city: new homes and higher land values add to the assessed base. | CR-8b, CR-9 |
| C-29 | `applicants.variance` | `compliance_cost` (variance applications) | decrease | Nothing given up: the burden is removed. | CR-1, CR-8c |
| C-31 | `officials.enforcement` | `non_tax_receipts` (application fees) | increase | Nothing given up by the department: the fees are applicants' outlay (C-27). | CR-8b, CR-12e |
| C-36 | `owners.splittable` (those who keep their lots) | `resources_available_other_uses` | decrease | Other purchases or saving: they pay property tax on the higher value, which they cannot avoid while holding the land. | CR-3, CR-8b |
| C-37 | `owners.non_splittable` | `resources_available_other_uses` | increase | Nothing given up: lower assessed values at a fixed rate. | CR-3, CR-8b |

C-24 and C-25 are the two sides of the revaluation when it is realized (CR-8b). A higher value owners do not realize is not means to spend (CR-3, note), but the property tax on it is a sum they cannot avoid while they hold the land, so owners who keep splittable lots are signed on that (C-36), and non-splittable owners the other way (C-37). Owners of new homes are not signed: on the counterfactual path they would have bought elsewhere and paid tax there. C-28, C-36 and C-37 rest on A-21. Fees paid (C-27) are received by the department (C-31) and used up in review (C-26). New residents also use schools, roads and sewers, which costs the city budget; that is not netted against C-28 (CR-12c), and whether recipients of city spending end up with more or less is not signed.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | The 6,000 rule binds: for many lots of 6,000 to 12,000 sq ft, land is worth more as small lots than as one lot. | binding | 0.85 | $95 a sq ft for small lots in Brackwell against $70 in Larkfield. | Almost every consequence weakens or vanishes. |
| A-2 | For splittable lots as a class, the value of the option to split exceeds the fall in their value from added supply. | other | 0.65 | 400 to 700 extra homes a year against 15,000 in the region; land is more than half the value of these lots. | C-1 becomes `ambiguous`. |
| A-3 | Owners and builders expect the repeal to last at least a few years. | expectations | 0.75 | 7 to 2 vote; no referendum petition. | C-1, C-3, C-11, C-16, C-17, C-30 and C-33 shrink. |
| A-4 | With the setback and parking rules, the practical minimum lot is about 2,500 sq ft, well below 6,000 and above 1,500. | binding | 0.9 | Setbacks, coverage and parking applied to a 25 by 100 foot lot. | If the practical minimum were near 6,000, C-2 would be small; if below 1,500, the new minimum would bind. |
| A-5 | At current land and home prices, splitting pays for some owners, after demolition, fees and the 60-day wait. | alternative_uses | 0.8 | The arithmetic in section 4; split costs. | C-3, C-4, C-6, C-8, C-18, C-23, C-34, C-35 and C-41 not reported. |
| A-6 | Coverage and height limits keep the floor area of homes on small lots below that of homes on large lots. | other | 0.75 | 50% coverage and 35 feet on 2,500 sq ft; Brackwell's 1,600 sq ft homes. | C-5 not reported. |
| A-7 | Small builders can carry out two-to-four-lot splits at costs close to those of larger firms. | other | 0.6 | Ministerial approval; small project sizes. | C-6 not reported. |
| A-8 | Applicants know R3 and that review is first-come, so some file early to queue. | expectations | 0.7 | The ordinance's text; builders' practice. | The (+) chain of C-7 fails; C-7 becomes a decrease. |
| A-9 | Some old-standard applications that would have been filed in the window are held back to redesign under the new standards. | expectations | 0.7 | About 120 two-lot splits a year under the old rule; a redesign gains lots. | The (−) chain of C-7 fails; C-7 becomes an increase. |
| A-10 | Some owners of splittable lots who would have built, rebuilt or re-let in the window wait for the effective date and approval. | expectations | 0.7 | Rebuilds and lettings each year on such lots; a few months' delay against the gain from splitting. | C-9 and C-10 not reported. |
| A-11 | Added detached homes lower the prices of existing homes in Larkfield somewhat: buyers do not absorb them at unchanged prices. | substitutability | 0.6 | Larkfield is a submarket with its own commuting and school ties. | C-16, C-18, C-19, C-32 and C-37 not reported; C-1's (−) chain vanishes and it needs no A-2; C-11 and C-30 lose their (−) chain and become increases. |
| A-12 | Some covenant-bound owners try to split, or HOAs sue, so the question is litigated. | other | 0.8 | 35% of lots under covenants; owners on both sides. | C-12 and C-40 not reported. |
| A-13 | In some covenant subdivisions, owners who want to split can organize a vote at renewal or a petition. | other | 0.6 | Renewal dates from 2030; majority rule. | C-13 not reported; C-11 under U1-a loses a (+) chain. |
| A-14 | Homeowner groups and builders can organize at a cost below their stake. | other | 0.85 | Their activity on the ordinance. | C-14 not reported. |
| A-15 | Some households who work in Larkfield bought in Brackwell or Tessmoor because Larkfield had no detached homes at their price, and commuting is practical. | mobility | 0.7 | Commuting data; price gaps. | C-15, C-20 and C-33 not reported. |
| A-16 | Small-lot detached homes and rented apartments and townhouses are substitutes for some households. | substitutability | 0.7 | Household sizes and incomes of renters. | C-19 and C-32 not reported. |
| A-17 | Owners next to new small-lot homes rank light, privacy and lower density above their absence. | other | 0.6 | Their choice of large-lot zones; comments at the hearings. | C-21 not reported (Tier C); C-38 becomes C-1's increase. |
| A-18 | Some residents of new small-lot homes park on the street despite two off-street spaces. | other | 0.55 | Car ownership per household; driveway sizes on narrow lots. | C-22 not reported (Tier C). |
| A-19 | Some owners realize their gain by selling a lot or part of one. | other | 0.8 | Builders buy lots to split. | C-24 and C-25 not reported. |
| A-20 | Application fees are set to recover review costs. | revenue_use | 0.8 | R2. | The review is paid from the city's general budget; its payers are a group (OC-3). C-31 and C-39 lose their premise. |
| A-21 | Property tax is charged at a fixed rate on assessed value, and new homes and higher land values add more to the base than lower values of non-splittable homes remove. | other | 0.6 | State assessment rules; the count of new homes against the size of C-16's fall. | C-28, C-36 and C-37 not reported. |
| A-22 | New small-lot homes are close substitutes for the older modest homes demolished to make room. | substitutability | 0.7 | Prices of Brackwell's new small homes against older Larkfield homes. | C-18 becomes `ambiguous`. |
| A-23 | Split and subdivision applications (400 to 700 a year) far exceed the 60 variance applications a year they replace, with similar review work each. | other | 0.75 | Planning department projection and caseload. | C-26, C-27 and C-31 become `ambiguous`; C-8 loses its partial-response premise; C-39 loses a premise. |
| A-24 | Lots and homes made under the 6,000 rule cost a demolition or a re-plat to change, and households who moved away have bought homes there. | reversal_cost | 0.85 | Ages and values of homes on large lots; ownership of homes in neighboring cities. | More of the original's effects would reverse (persistence column). |
| A-25 | Developers of subdivisions of five or more lots fear the minimum's return within their payback period and hold back. | expectations | 0.4 | Long plat reviews; the two-vote minority on the council. | Below the cut-off; not reported. |
| A-26 | The planning department can use fee receipts to add review staff within months, so its capacity grows with applications. | revenue_use | 0.6 | Fees set to recover review costs (R2, A-20); hiring and contract reviewers take months, not years (the core-only re-run's A-N1). | C-39 not reported. |
| A-27 | The chance that an owner or HOA sues to enforce a covenant differs across subdivisions, so some splits go unchallenged (some HOAs are inactive, some neighbors absent or in favor). | enforcement | 0.6 | HOA activity varies; enforcement is by private suit only. | C-40 not reported; C-11 under U1-a loses a (+) chain. |
| A-28 | For some parcels large enough for five or more lots, plat review costs more than the fifth lot is worth, or the parcel can be divided by successive splits of up to four lots. | other | 0.6 | About five months of plat review against 60 days; 8,500 lots of 12,000 sq ft or more, some much larger. | C-41 not reported. |

## 11. Report

**The policy.** From September 2027, Larkfield allows detached homes on lots down to 1,500 sq ft (before: 6,000), with splits into up to four lots approved within 60 days. Existing homes and lots are not affected, and existing setback, height and parking rules stay. Applications filed after passage are decided under the new rules if complete on the effective date. The ordinance says nothing about private covenants that require large lots.

**Visible consequences.** Owners of lots that can now be split gain value, from the time the repeal became likely (C-1). New lots are smaller (C-2), and more homes are built (C-3).

**Invisible consequences.**
- *Homes and buyers.* New homes have less floor area (C-5). Entry-level detached homes cost less than they would have (C-18), as older modest homes are replaced by several smaller ones (C-34); rents are lower (C-19) and landlords receive less (C-32); more homes and lots change hands (C-23), and more construction work goes on in Larkfield (C-35). Fewer Larkfield workers buy in Brackwell and Tessmoor, whose builders sell fewer homes or at lower prices (C-15, C-20) and whose land is worth less (C-33). Small builders enter (C-6), and owners of large parcels keep projects to four lots to avoid plat review (C-41).
- *Owners who cannot split* see their home values fall as competing homes are built (C-16), and pay less property tax (C-37). For owners of the 4,500 undersized lots, which now conform, the gain from no longer needing a variance and the loss from competition push opposite ways (C-30). Lots bought after passage cost more (C-17); sellers' gains are buyers' outlays (C-24, C-25); owners who keep splittable lots pay more property tax (C-36).
- *Covenants.* Under either reading the effect on covenant-bound owners' values is ambiguous (C-11): competition lowers them, while the chance to end covenants at renewal, or to split where no one sues, or (if covenants are void) the option to split now, raises them. If covenants stay enforceable, some owners campaign to end them (C-13) and some splits go ahead unchallenged in breach of them (C-40). Either way the question goes to court (C-12).
- *The six months before the effective date.* Some old-standard applications wait while others are filed early to queue, so the net effect on filings is ambiguous (C-7); filings rise from the effective date (C-8). Owners hold off building single homes on splittable lots and leave some older houses empty (C-9, C-10). None of this lasts.
- *Neighbors* (Tier C). Owners next to new small-lot homes who cannot split their own lots value their homes less (C-21); for those who can, the option and the change next door push opposite ways (C-38). Street parking is harder to find (C-22).
- *Costs and receipts.* Review work rises, net of variance hearings that end (C-26); split applicants pay more in fees and surveys (C-27) while owners of undersized lots no longer pay for variances (C-29); the department collects more fees (C-31); once staff are added, splits are approved faster (C-39); property tax revenue rises (C-28).

**Ambiguous effects.** Covenant-bound owners' values under either reading (C-11); values of nonconforming lots (C-30); values of splittable lots next to split lots, counting proximity (C-38, Tier C); applications filed in the window (C-7); lobbying by homeowner groups and builders (C-14).

**What does not reverse.** Sixty-five years of large lots and large homes stay until owners choose to split them, lot by lot; households who moved away mostly stay; homes that cannot be split stay worth more than if the rule had never been imposed, for as long as the stock of small-lot homes stays short. Under one reading, covenants carry the old rule on for a third of the city's lots until owners vote to end them.

**Key conditions.** The old rule binds (A-1, p = 0.85). Splittable owners gain only if the option outweighs the competition from added homes (A-2, p = 0.65). The fall in existing home values and prices rests on added homes not being absorbed at unchanged prices (A-11, p = 0.6).

**What this analysis cannot say.** How many lots will be split or how fast; how large any price change is; whether neighbors' losses outweigh buyers' gains; whether the repeal is desirable; effects on traffic safety, trees, drainage and other environmental matters (out of scope for version 1); and, until Q20 is decided, whether proximity effects belong to the analysis at all.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions | Persistence |
|---|---|---|---|---|---|---|---|---|---|
| C-1 | owners.splittable | asset_value (land of splittable lots; not counting effects through proximity) | increase | short | visible | B | CR-1, CR-7c, CR-10c, CR-12e | A-1, A-2, A-3 | none (the persisting shortfall in the stock raises the option's value) |
| C-2 | builders | specification_level (lot area of new lots) | decrease | medium | visible | B | TS-3, CR-1, CR-4 | A-1, A-4 | partial (A-24) |
| C-3 | builders | quantity_supplied (new detached homes) | increase | medium–long | visible | B | CR-4, CR-7a, TS-1, TS-5 | A-1, A-3, A-5 | partial (medium); partial (long) |
| C-4 | owners.splittable | quantity_supplied (buildable lots) | increase | short–medium | invisible | B | CR-4, CR-7a | A-1, A-5 | partial (A-24) |
| C-5 | builders | unit_size (floor area per new home) | decrease | medium | invisible | B | CR-4, CR-5c | A-1, A-6 | partial (A-24) |
| C-6 | builders.small | entry_rate | increase | medium | invisible | B | CR-4, CR-7a | A-5, A-7 | none |
| C-7 | owners.splittable, builders | quantity_traded (applications filed, window) | ambiguous | short | invisible | B | RS-8, CR-12b | A-8, A-9 | n/a (transition) |
| C-8 | owners.splittable, builders | quantity_traded (applications filed, from the effective date) | increase | short–medium | invisible | B | RS-8, CR-4, CR-12e | A-1, A-5, A-23 | none |
| C-9 | owners.splittable, builders | quantity_supplied (homes started on splittable lots, window) | decrease | short | invisible | B | RS-8, CR-10a | A-10 | n/a (transition) |
| C-10 | owners.splittable | units_held_vacant (older homes awaiting splits) | increase | short | invisible | B | CR-10a, CR-4 | A-10 | n/a (transition) |
| C-11 | owners.covenant_bound | asset_value | ambiguous | short–medium | invisible | B | CR-7c, CR-10c, RS-13, RS-20, CR-8, CR-12b | A-3, A-11, A-13, A-27 | U1-a: full until renewal votes, partial after; U1-b: none |
| C-12 | hoas, owners.covenant_bound | compliance_cost (covenant litigation) | increase | short–medium | invisible | B | CR-4, CR-8c | A-12 | n/a (no counterpart) |
| C-13 | owners.covenant_bound | lobbying_effort (covenant amendment) | U1-a: increase; U1-b: no_change | medium | invisible | B | CR-4, RS-7 | A-13 | n/a (no counterpart) |
| C-14 | homeowner_groups, builders | lobbying_effort (at the city) | ambiguous | medium | invisible | B | RS-7 (repeal clause), CR-4 | A-14 | n/a |
| C-15 | buyers.prospective | cross_border_purchases | decrease | medium–long | invisible | B | RS-4 | A-15 | partial (A-24) |
| C-16 | owners.non_splittable (conforming) | asset_value | decrease | short–medium | invisible | B | EN-14, CR-7c, RS-13, CR-9 | A-3, A-11 | partial (follows the stock of competing homes) |
| C-17 | buyers.lots | price_paid (splittable lots) | increase | short–medium | invisible | B | SB-4, OC-7 | A-1, A-3 | none |
| C-18 | buyers.prospective | price_paid (entry-level detached homes) | decrease | medium–long | invisible | B | RS-13, CR-12e | A-5, A-11, A-22 | partial |
| C-19 | renters | price_substitute (rents) | decrease | medium–long | invisible | B | RS-16, RS-13 | A-11, A-16 | partial |
| C-20 | neighboring_jurisdictions | quantity_supplied, net_price_received (homes sold to Larkfield workers) | at_least_one_decrease | medium–long | invisible | B | RS-4, CR-9, CR-6 | A-15 | partial (A-24) |
| C-21 | neighbors (on lots that cannot be split) | asset_value (homes next to new small-lot homes) | decrease | medium | invisible | C | CR-9 (proximity) | A-17 | partial |
| C-22 | neighbors | search_cost (street parking) | increase | medium | invisible | C | CR-9 (shared facility) | A-18 | n/a (no counterpart) |
| C-23 | buyers.prospective, owners.splittable | quantity_traded (sales of homes and lots) | increase | medium–long | invisible | B | OC-4 in reverse, CR-5 | A-1, A-5 | partial |
| C-24 | owners.splittable (sellers) | resources_available_other_uses | increase | medium | invisible | B | OC-7, CR-8b | A-1, A-19 | n/a (no counterpart) |
| C-25 | buyers.lots | resources_available_other_uses | decrease | medium | invisible | B | OC-7, CR-8b | A-1, A-19 | n/a (no counterpart) |
| C-26 | officials.enforcement | enforcement_cost (split review, net of variance hearings) | increase | short–medium | invisible | B | OC-3, CR-12e | A-20, A-23 | none |
| C-27 | owners.splittable, builders | compliance_cost (fees, surveys, plats for splits) | increase | short–medium | invisible | B | OC-2, CR-8c, CR-12e | A-5, A-23 | none |
| C-28 | city budget | tax_revenue (property tax) | increase | medium–long | invisible | B | CR-8b, CR-9 | A-5, A-21 | partial |
| C-29 | applicants.variance | compliance_cost (variance applications) | decrease | short–medium | invisible | A | CR-1, CR-8c | none | none |
| C-30 | owners.nonconforming | asset_value (lots under 6,000 sq ft that cannot be split) | ambiguous | short–medium | invisible | B | CR-1, CR-3, CR-7c, RS-13, CR-12b | A-3, A-11 | n/a (ambiguous in the original too) |
| C-31 | officials.enforcement | non_tax_receipts (application fees) | increase | medium | invisible | B | CR-8b, CR-12e | A-20, A-23 | none |
| C-32 | landlords | net_price_received (rents) | decrease | medium–long | invisible | B | RS-16, CR-9, CR-6 | A-11, A-16 | partial |
| C-33 | neighboring_jurisdictions (landowners) | asset_value (land in Brackwell and Tessmoor) | decrease | short–medium | invisible | B | CR-7c, CR-10c, CR-9 | A-3, A-15 | partial (follows the stock) |
| C-34 | owners.splittable (older modest homes) | quantity_supplied (older modest homes standing) | decrease | medium–long | invisible | B | EN-14, CR-4, CR-8a | A-5 | partial |
| C-35 | construction_input_suppliers | quantity_traded (construction labor and materials in Larkfield) | increase | medium | invisible | B | CR-9 | A-5 | none |
| C-36 | owners.splittable (those who keep their lots) | resources_available_other_uses | decrease | medium–long | invisible | B | CR-3, CR-8b | A-3, A-21 | partial |
| C-37 | owners.non_splittable | resources_available_other_uses | increase | medium–long | invisible | B | CR-3, CR-8b | A-11, A-21 | partial |
| C-38 | neighbors (owners of splittable lots next to split lots) | asset_value (combined, counting effects through proximity) | ambiguous | medium | invisible | C | CR-9 (proximity), CR-12b | A-2, A-17 | partial |
| C-39 | applicants.splits | wait_time (approval of splits) | decrease | medium | invisible | B | CR-1, CR-6 | A-20, A-23, A-26 | none |
| C-40 | owners.covenant_bound | legal_breach (unchallenged splits in breach of covenants) | U1-a: increase; U1-b: no_change | medium | invisible | B | RS-20, CR-4 | A-12, A-27 | n/a (no counterpart) |
| C-41 | owners.large_lot, builders | reclassification (projects kept at four lots or fewer) | increase | short–medium | invisible | B | RS-17, CR-1, CR-4 | A-5, A-28 | n/a (no counterpart) |

Final check (workflow): every (actor class, variable) reached by more than one chain is in section 7, including the proximity chain against C-1 (Tier B qualified, combined at Tier C in C-38). Group signs are used where only "at least one" follows: neighboring builders' sales or prices (C-20); every other margin has its own premise. Every sign is against Larkfield with the 6,000 rule in force, not against the situation before the repeal; persistence is against the path without the rule. Timing: the window is signed per window (C-7, C-9, C-10 against C-8 and C-3). Both sides of the revaluation are recorded when realized (C-24, C-25); unrealized gains are not signed as means, but the property tax on them is (C-36, C-37). Both sides of the fees (C-27, C-31) and of property tax (C-28, C-36, C-37) are recorded. Capitalization is recorded for each kind of lot (C-1, C-11, C-16, C-17, C-30) and for land across the border (C-33). Costs and savings of different classes are not netted (C-27, C-29). Enforcement is netted against the enforcement the repeal makes unnecessary (C-26). Every premise, including the Tier C neighbors' rankings, is in section 10.

## Corrections after the core-only comparison

The core-only re-run (`05_examples_core/WE-043_minimum_lot_size_repeal_core.md`) was compared with this example. Each conclusion was checked against the core rules and catalog 0.9 before it was applied.

**Changed.**
- C-11: U1-a decrease → `ambiguous` (now `ambiguous` under both readings). The option opened by ending a covenant at renewal (A-13), which C-13 already used, is capitalized now; RS-20 adds splits no one challenges (A-27). U1-b reworded under CR-8's 0.9 mutual-rights clause: not a transfer between classes. Persistence under U1-a: full until renewal votes, partial after.
- C-16: the 4,500 nonconforming lots moved out to C-30, since conforming status is an opposing chain; cites EN-14 (promoted in 0.9). Persistence reason: follows the stock (CR-7, 0.9).
- C-27: no longer netted against the variance applicants' saving, which belongs to another class (CR-1, recording; CR-12c); that saving is C-29.
- C-20: one margin → group of sales and price, `at_least_one_decrease` (CR-6, 0.9, splitting a shift).
- C-1: qualified "not counting effects through `proximity`" and kept at Tier B; the combined sign for owners next to split lots is C-38 at Tier C (CR-12, 0.9). Persistence partial → none (see rejections). C-21 restricted to neighbors who cannot split, where both chains agree.
- C-8: the partial-response premise CR-12's 0.9 clarification requires is stated (A-23). C-7: signed on the flow of filings, with the early filings an increase against none (CR-12, 0.9).
- C-14: cites CR-4's 0.9 clarification on lobbying in repeals; sign unchanged.
- Metamorphic table: variance work now reverses (C-29), with split review moved to a row with no counterpart; persistence of asset values given from the stock; covenant persistence under U1-a corrected; rows added for nonconforming lots, landlords, land across the border, older homes, construction, property tax, and the repeal's own procedure.

**Added.** C-29 variance applicants' cost falls (core C-5). C-30 nonconforming lots' value, `ambiguous` (core C-12). C-31 fee receipts (core C-24). C-32 landlords' rent (core C-27). C-33 land values in Brackwell and Tessmoor (core C-30). C-34 older modest homes standing (core C-31; EN-14 in reverse). C-35 construction inputs in Larkfield (core C-33). C-36 property tax paid by owners who keep splittable lots (core C-35, restricted). C-37 property tax of non-splittable owners (core C-36). C-38 combined value of splittable neighbors at Tier C (CR-12, 0.9). C-39 approval wait for splits (core C-4; CR-6's 0.9 clause on a public supplier whose capacity grows after a lag now covers it). C-40 unchallenged covenant breach under U1-a (RS-20, promoted in 0.9). C-41 projects kept at four lots (RS-17; R2's threshold). New assumptions A-26 (the core version's A-N1), A-27, A-28.

**Removed.** None.

**Comparison conclusions rejected or applied only in part.**
- Persistence of splittable land (C-1) as partial: rejected. The option is restored in full, and the stock shortfall that persists raises its value, so none of the original decrease remains (CR-7, 0.9); the comparison's "follows the stock" reasoning holds for homes that cannot be split (C-16), not for this row.
- Core C-35 for owners of new homes: not applied; on the counterfactual path they would have paid tax elsewhere, so only owners who keep splittable lots are signed.
- Core C-20 (enforcing owners' loss of the covenant right, cause J): not added; CR-8's 0.9 mutual-rights clause settles that it is not a transfer between classes, so it stays an item inside C-11.
- Core C-17 and C-18 (cause J): not added; nothing in 0.9 settles them, and C-7 already carries the held-back filings.


## Gaps found

**(a) Calculus gaps (a step no core rule covers).** None new. The proximity chains (C-21, C-22) are the open GAP-026-1, reported at Tier C under CR-9's 0.7 clarification pending Q20.

**(b) Unclear core rules.**
1. *CR-12e's response argument and the members of a class.* For splittable lots (C-1), the 0.8 clarification correctly blocks the argument for the class's owners one by one, but leaves no way to sign the class except an empirical premise (A-2). The same structure (an option added to all, used by some, whose use lowers everyone's value) will recur for any upzoning; a note on it in CR-7c would help.
2. *CR-8 voiding and mutual rights* (addressed in 0.9 by CR-8's mutual-rights clause). Under U1-b each covenant-bound owner both holds and is bound by the voided right. CR-8's voiding clause names a holder and another party; here the two are the same class, and the transfer nets within it only per owner. Recorded as `ambiguous` (C-11).
3. *CR-1 on dated operations.* Worked as written: the option is added on the effective date, acts before then through expectations, and land values move at once.

**(c) Missing or wrong patterns.**
1. *The repeal procedure assumes an original analysis* (addressed in 0.9 in the workflow). "Analyzing a repeal" (workflow) asks for a table against the original analysis. None existed; the original rule's effects were derived from the core rules in the metamorphic table. A sentence in the workflow allowing this, and requiring the derivation column, would help.
2. *Standard on new units, stock exempt* (promoted in 0.9 as EN-14; 06_gaps.md, 6.2e; proposed as EN-12 in WE-031) fits the original rule exactly: a minimum on new lots with existing lots grandfathered, existing homes gaining from protection (CR-7c) and land specific to new units losing. This is its second use, in reverse. Its repeal form adds the split between owners who can and cannot use the new option (C-1 against C-16).
3. *RS-13 in reverse for teardowns.* RS-13 covers added and withdrawn supply, but a teardown-and-split does both at once in one segment (C-18). The accounting identity decided it; RS-13 could say so.
4. No pattern gave a sign that had to be overridden.

**(d) Vocabulary.**
1. *Land per dwelling.* `unit_size` is defined as floor area; lot area per dwelling was recorded as `specification_level` (C-2), since the minimum is the specification. A variable or a note on whether `unit_size` covers land would help outcome cards.
2. *No instrument type for a saving clause or a transition rule* (R3, R4). They were recorded in the component table without a type; R3 matters (C-7).
3. *Applications filed* were recorded as `quantity_traded` with a qualifier; no variable fits a filing that is not an exchange.

**(e) Test of 0.8.**
- *Repeal analysis and the metamorphic check (workflow, TS-6) with no prior example.* Needed interpretation: the original rule's effects were derived in the table, which worked, but the workflow does not say this is allowed ((c) 1). Persistence and `n/a` were applied as written.
- *TS-3 0.8, product standards (lot size as a specification).* Worked as written for the old rule (binding on the share of lots that would have been made below 6,000, growing as land prices rose). For the new 1,500 minimum it needed interpretation: "the share of designs actors would choose below it" had to be read as the choice given the existing rules that stay, which bind first, so the new minimum binds on almost none (A-4).
- *CR-7c capitalization (splittable against other lots).* Worked as written for timing (from introduction, fully at passage) and for later buyers (C-17). The sign for splittable lots needed an empirical dominance premise (A-2), because the competition chain from others' splits opposes the option (CR-12e 0.8; (b) 1).
- *CR-10b, transition-only effects and persistence `n/a`.* Worked as written (C-7, C-9, C-10), as did the clause that costs already incurred under the rule are not consequences of the repeal (section 8).
- *CR-9 0.7, proximity effects at Tier C (Q20).* Worked as written for recording, but the sign needed a premise about neighbors' rankings (A-17, A-18) that CR-9 does not mention; the rules never assume a ranking, so even a Tier C proximity chain needs one.
- *RS-8 0.8, opposing timing chains in the announcement window.* Worked as written: R3 is the pending-applications case the Unless clause names, and C-7 is `ambiguous`. The window after the effective date was signed with CR-12e's response argument (C-8).
- *OC-3 0.8, the right baseline.* Worked as written: variance hearings the repeal makes unnecessary were netted against split review by arithmetic on the case's figures (C-26, A-23).
- *RS-7 repeal clause.* Worked as written (C-14).
- *`unit_size`.* Worked for floor area (C-5); land per dwelling did not fit ((d) 1).
- *Candidates from 06_gaps.md, 6.2e.* "Standard on new units, stock exempt" (WE-031) was needed, for the derivation of the original rule; this is its second use ((c) 2).

Re-run note: the core-only comparison contradicted parts of three verdicts above: CR-7c for covenant lots missed the renewal option (C-11 U1-a is `ambiguous`); OC-3's baseline was right for the department but C-27 netted another class's saving; and the metamorphic table misread variance work as not reversing and gave persistence reasons from who bore the change rather than from the stock.
