# WE-003 Cosmetology license required for hair braiding

Analyst: draft (Handbook 0.5)  |  Rule catalog version: 0.5  |  Status: awaiting expert review

A stylized policy in a fictional state, modeled on a common type of occupational-licensing rule. The probabilities are illustrative.

## 1. Policy record

**Westmark State Cosmetology Act, amendment 7.** Hair braiding (braids, twists and locs, with no cutting or chemicals) was previously unregulated in Westmark. About 2,000 people braid for pay, mostly self-employed, many working from home or in small shops. Two neighboring states do not license braiding; their borders are a long drive from the main cities.

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 License requirement | `licensing_requirement` | Braiding hair for pay | Anyone who braids for pay, and any business that employs them | A full cosmetology license: 1,500 hours at a licensed cosmetology school (typical tuition $12,000 to $18,000) and a state exam. The curriculum covers cutting, coloring and chemical treatments; braiding is a small part or absent. | None. Existing braiders have 12 months to comply. |
| K2 Penalties and enforcement | Enforcement | K1 | State Board of Cosmetology | Fines for unlicensed practice and for businesses that employ unlicensed braiders. Inspections are complaint-driven. | None |

Unclear provisions: whether unpaid braiding for family and friends is covered. Assumed not covered (only braiding for pay is).

## 2. Classification

| Component | Rothbard type | Binding? | Rule families |
|---|---|---|---|
| K1 | Triangular: prohibits exchanges between customers and unlicensed braiders; a grant of privilege to license holders | Yes: almost no current braiders hold a cosmetology license (A-1) | EN, RS, OC |
| K2 | Binary: funded by taxpayers and license fees; the board's budget rises with the new task (A-8, OC-3 first funding case). Also attaches fines to businesses that employ unlicensed braiders (CR-1 op 3). | Yes | OC-3 |

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `braiders.current` | People who braid for pay now | Must spend 1,500 hours and the tuition to keep working legally; or stop; or work without a license. |
| `braiders.prospective` | People who would have started braiding | Entry now costs a cosmetology education. |
| `cosmetologists.licensed` | Existing license holders | Face less competition in braiding, if they offer it. |
| `businesses.braiding` | Shops that employ braiders | Fined if they employ unlicensed braiders. |
| `schools.cosmetology` (`input_suppliers`) | Licensed schools | New demand for their programs. |
| `customers.braiding` | People who pay for braiding | Fewer legal providers; higher prices; informal providers. |
| `officials.enforcement`, `taxpayers` | Board of Cosmetology and its funders | More enforcement work. |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | braiders in the legal market | `share_of_sellers_licensed` | increase | short | K1 | A-2 |

The visible, stated aim is that everyone who braids for pay is trained and licensed. Whether this raises the quality customers receive is the open question in section 7.

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-2 | `braiders.current`, `braiders.prospective` | `number_of_sellers` (legal), `entry_rate` | decrease | short to medium | EN-1 | A-1, A-2 |
| C-3 | `braiders.current` who complete the license | `compliance_cost` (tuition, 1,500 hours away from paid work) | increase | short | OC-2, EN-1 | A-1, A-10 |
| C-4 | `braiders.current` who do not qualify | `employment` (people braiding for pay, legal and informal) | decrease | short to medium | EN-3, OC-4: those at the margin move to their next-best occupation; those who violate stay (C-5) | A-1, A-2 |
| C-18 | `businesses.braiding` | `employment` (unlicensed braiders employed in shops) | decrease | short to medium | CR-1 (op 3, K2: fines on employers) → CR-4 (x: employ an unlicensed braider, y: stop or hire a licensed one) | A-1, A-2 |
| C-5 | `braiders.current` who keep working without a license | `informal_activity` | increase | short | RS-3, EN-3 | A-3 |
| C-6 | `schools.cosmetology` | `quantity_demanded` for programs | increase | short | EN-1 | A-1, A-10 |
| C-8 | `schools.cosmetology`, `cosmetologists.licensed`, `braiders.current` | `lobbying_effort` (schools and licensees to keep the rule; braiders for an exemption) | increase | medium | RS-7, EN-5 | A-1, A-9 |

C-4: braiders who leave the trade are worse off by their own ranking (CR-3a): they chose braiding over the alternatives still open to them. That does not mean they earn less money. Their next-best occupation may pay more and be valued less for other reasons (flexible hours, home-based work), so their `earnings` are not signed (EN-3, 0.5: that needs a premise that the next-best occupation pays less, which the record does not support). Catalog 0.3 signed `earnings` decrease; that overclaimed.

C-3: the tuition is a payment to the schools (CR-8b), whose side is C-6.

Not reported: relocation to neighboring states (RS-4). The borders are far from the main cities, and braiders' customers are local; A-6 is below the cut-off (p = 0.3).

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-9 | `customers.braiding` | `price_paid` (legal braiding) | increase | short to medium | EN-1 | | A-1, A-2 |
| C-10 | `cosmetologists.licensed` who braid, and newly licensed braiders | `net_price_received` | increase | short to medium | EN-2 | | A-1, A-2 |
| C-11 | `customers.braiding` | `quantity_substitute` (braiding by family and friends, or not having braids done) | increase | short | EN-3, RS-1 | paid and home braiding: `substitute`, partial | A-4 |
| C-12 | `customers.braiding` using unlicensed braiders | `search_cost` (informal providers cannot advertise openly) | increase | short | RS-3, RS-10 | | A-3 |
| C-17 | `customers.braiding` using unlicensed braiders | `quality_information` | decrease | short | RS-10 | | A-3 |
| C-19 | `customers.braiding` using unlicensed braiders | `disputes_settled_outside_courts` | increase | short | RS-10 (no recourse to the courts for an illegal service) | legal and informal braiding: `same_market_other_segment` | A-3 |
| C-20 | `customers.braiding` who keep buying legal braiding | `resources_available_other_uses` | decrease | short to medium | CR-8b: the higher price (C-9) is a sum they pay as long as they keep buying, received by licensed braiders (C-10) | the braiding exchange | A-1, A-2 |
| C-13 | `customers.braiding` | `quality_per_unit` received | not reported (see section 7) | medium | EN-4, DM-2 | | A-5, A-7 |

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `customers.braiding`, `quality_per_unit` received, medium | Licensed providers have completed formal training (EN-4, "up" chain). Inactive: the curriculum covers cutting, color and chemicals and little or no braiding (A-5, p = 0.85). | Higher prices push customers toward home braiding and unlicensed providers (EN-3, C-11, C-5). Active only if what they move to is of lower quality than the paid braiding it replaces (A-7, p = 0.45): informal braiders are largely the same people as before. | DM-2 (0.5): each chain needs its own premise. | **Not reported.** With A-5 the up chain is inactive; the down chain rests on A-7, below the cut-off. Conditional possibility: a decrease if A-7 holds. If the curriculum taught braiding (A-5 false) and A-7 held, the sign would be **ambiguous**. |
| `braiders.current` who obtain the license, `earnings`, medium | Higher price per service (C-10). | Time spent in training rather than working (C-3); some customers lost to home braiding (C-11). | None | **ambiguous** during and just after training. A one-time cost against a later stream of gains is ambiguous by design (DM-3). Braiders who chose to train expected it to pay; those who left expected it not to. |

## 8. Time structure

- The 12-month compliance window concentrates exits and enrollments around the deadline (RS-8). This is a note on the path, not a consequence: without the act, braiders would not enroll at all, so there is no counterfactual timing to compare with. Draft 0.2 listed it as C-7; the ID is retired.
- Fewer legal providers (C-2) appear at the deadline; fewer new braiders (lower entry) shows up over the following years.
- Braiding skill is specific and often learned informally. Braiders who leave the trade lose the use of that skill in paid work (C-4); by their own ranking they are worse off, which is not a claim about their money earnings.
- Expectations: if braiders expect an exemption to be won soon (C-8), more of them wait it out informally instead of enrolling (TS-2).

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-15 | `customers.braiding`, `braiders` who exit | `quantity_traded` (legal braiding services) | decrease | Braiding services that would have been bought and sold at the old prices and no longer are. Both sides lose the gain they expected. | OC-4 |
| C-16 | `taxpayers` | `resources_available_other_uses` | decrease | What the added board budget would otherwise have funded (OC-3, first funding case, A-8). | OC-3, OC-1 |
| C-21 | `officials.enforcement` | `enforcement_cost` | increase | Board inspection time and budget, used up (CR-8c). | OC-3 |

The 1,500 hours and tuition are already recorded as C-3 (`compliance_cost`), so the separate draft 0.1 entry for training time is dropped.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | Few current braiders already hold a cosmetology license, so the requirement binds. | binding | 0.95 | Board license records against a census of braiders. | Almost every consequence fails. |
| A-2 | The board enforces the requirement often enough that many braiders comply or stop. | enforcement | 0.7 | Board inspection budget; complaint volumes; fines. | C-2, C-9, C-10 weaken; C-5 grows. |
| A-3 | Some braiders keep working without a license and are not caught. | enforcement | 0.8 | Complaint-driven enforcement; home-based work. | C-5, C-12, C-17 and C-19 not reported. |
| A-4 | Home braiding by family or friends is a feasible substitute for some customers. | substitutability | 0.75 | Prevalence of home braiding. | C-11 weakens. |
| A-5 | The required training is largely unrelated to braiding quality. | other | 0.85 | Curriculum hours by topic; exam content. | EN-4's up chain becomes active; with A-7, C-13 would be ambiguous. |
| A-6 | Braiders relocate to neighboring states on a meaningful scale. | mobility | 0.3 | Distance from cities to the borders; local customer base. | Below cut-off; not reported. |
| A-7 | What customers move to (home braiding by family and friends, unlicensed braiders) is of lower quality than the paid braiding it replaces. | other | 0.45 | Informal braiders are largely the same people who braided legally before; home braiding is used mainly for simpler styles. | Below cut-off: C-13 not reported. If above, C-13 is a decrease. |
| A-8 | The board's budget is raised for the new enforcement task (appropriation and fees), rather than the task being absorbed within a fixed budget. | revenue_use | 0.6 | Amendment's fiscal note; the board's budget history. | C-16 is replaced by less enforcement of other cosmetology rules (OC-3, second funding case). |
| A-9 | Schools, licensed cosmetologists and braiders can organize and spend to change or defend the requirement at a cost below their stakes. | other | 0.7 | Existing cosmetology trade associations; braiders are dispersed and mostly self-employed, which lowers but does not remove their capacity. | C-8 not reported. |
| A-10 | Some current braiders or new entrants choose to obtain the full license. | alternative_uses | 0.8 | Some braiders earn enough to justify $12,000 to $18,000 and 1,500 hours; some may already be partway through training. | C-3 and C-6 not reported; C-10 holds only for existing cosmetologists. |

## 11. Report

**The policy.** Westmark now requires anyone who braids hair for pay to hold a full cosmetology license: 1,500 hours of schooling, mostly in skills other than braiding, plus tuition and an exam. Current braiders have a year to comply.

**Visible consequences.** Everyone who braids legally for pay is now a licensed cosmetologist (C-1).

**Invisible consequences.**
- *Braiders* face a large cost to keep working legally (C-3). Some train and later charge more (C-10); fewer people braid for pay, as some leave for work they value less (C-4), though not necessarily for less money; some carry on without a license, at risk of fines (C-5). Fewer people take up braiding (C-2). Shops employ fewer unlicensed braiders (C-18).
- *Customers* pay more for legal braiding and have less to spend on other things (C-9, C-20), turn more often to family and friends or go without (C-11), find it harder to locate and judge informal braiders (C-12, C-17), and have no recourse to the courts when an informal service goes wrong (C-19).
- *Cosmetology schools* gain students and their tuition (C-6); schools and existing licensees have a stake in keeping the rule (C-8).
- *Taxpayers* fund the added enforcement (C-16), whose staff time is used up (C-21).

**Ambiguous effects.** Whether braiders who obtain the license end up earning more or less, once training time is counted.

**Not determined.** Whether the quality of braiding customers receive changes. The training is largely unrelated to braiding (A-5), so licensing does not raise it; whether it falls depends on whether home and informal braiding is worse than the paid braiding it replaces (A-7, p = 0.45), which the evidence does not establish.

**Key conditions.** That the training is unrelated to braiding (A-5, p = 0.85) means the license itself does not raise quality. That the rule is enforced (A-2, p = 0.7) governs how much of the trade moves out of the legal market versus into the informal one.

**What this analysis cannot say.** How many braiders will leave, how much prices will rise, whether those who leave earn more or less money, or whether the rule's aims justify its costs. Health and safety effects are out of scope in version 1.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | braiders (legal market) | share_of_sellers_licensed | increase | short | visible | B | K1 | A-2 |
| C-2 | braiders | number_of_sellers (legal), entry_rate | decrease | short–medium | invisible | B | EN-1 | A-1, A-2 |
| C-3 | braiders (training) | compliance_cost | increase | short | invisible | B | OC-2, EN-1 | A-1, A-10 |
| C-4 | braiders.current | employment (paid braiding, legal and informal) | decrease | short–medium | invisible | B | EN-3, OC-4 | A-1, A-2 |
| C-5 | braiders (unlicensed) | informal_activity | increase | short | invisible | B | RS-3, EN-3 | A-3 |
| C-6 | schools.cosmetology | quantity_demanded | increase | short | invisible | B | EN-1 | A-1, A-10 |
| C-8 | schools, licensees, braiders | lobbying_effort | increase | medium | invisible | B | RS-7, EN-5 | A-1, A-9 |
| C-9 | customers.braiding | price_paid | increase | short–medium | invisible | B | EN-1 | A-1, A-2 |
| C-10 | licensed braiders | net_price_received | increase | short–medium | invisible | B | EN-2 | A-1, A-2 |
| C-11 | customers.braiding | quantity_substitute (home braiding) | increase | short | invisible | B | EN-3, RS-1 | A-4 |
| C-12 | customers.braiding | search_cost | increase | short | invisible | B | RS-3, RS-10 | A-3 |
| C-17 | customers.braiding (informal) | quality_information | decrease | short | invisible | B | RS-10 | A-3 |
| C-15 | customers, braiders | quantity_traded (legal services) | decrease | short–medium | invisible | B | OC-4 | A-1, A-2 |
| C-16 | taxpayers | resources_available_other_uses | decrease | short | invisible | B | OC-3, OC-1 | A-8 |
| C-18 | businesses.braiding | employment (unlicensed braiders in shops) | decrease | short–medium | invisible | B | CR-1, CR-4 | A-1, A-2 |
| C-19 | customers.braiding (informal) | disputes_settled_outside_courts | increase | short | invisible | B | RS-10 | A-3 |
| C-20 | customers.braiding (legal) | resources_available_other_uses | decrease | short–medium | invisible | B | EN-1, CR-8b | A-1, A-2 |
| C-21 | officials.enforcement | enforcement_cost | increase | short | invisible | B | OC-3 | A-2 |
| — | licensed braiders | earnings | ambiguous | medium | invisible | B | C-10 vs C-3, C-11; DM-3 | A-1, A-4 |


## Gaps found

- GAP-8 (closed in catalog 0.2): RS-10 informal trade; C-12 now Tier B.
- GAP-9 (closed in catalog 0.2): `share_of_sellers_licensed`; C-1 now a signed consequence.
- GAP-10 (resolved as ambiguous by design, DM-3): pending expert confirmation.
- Catalog 0.3: RS-10 now names `quality_information`; C-17 added. C-7 (timing around the deadline) moved to section 8 under the timing convention in 2.5 (closed in catalog 0.3: GAP-024-4).
- Catalog 0.5: corrected after the core-only comparison (see ../05_examples_core/WE-003_braiding_license_core.md): C-4 re-recorded as employment in paid braiding (EN-3 0.5: exiting braiders' money earnings not signed); C-13 quality no longer reported (EN-4/DM-2 0.5: the down chain needs A-7, p 0.45); added employers' response to K2 fines (C-18), disputes outside courts (C-19), customers' loss of means (C-20) and enforcement cost (C-21); premises for lobbying (A-9), licensing take-up (A-10) and the board's funding (A-8, OC-3).
