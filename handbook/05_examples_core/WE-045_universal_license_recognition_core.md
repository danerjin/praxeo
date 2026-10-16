# WE-045 / Analysis: Universal recognition of out-of-state occupational licenses

Analyst: core-only re-run (Handbook 0.8)  |  Rules: core rules CR-1 to CR-12 only  |  Status: compared

## 1. Policy record

**Halvoran Occupational Mobility Act.** Halvoran (about 5.4 million people) licenses about 70 occupations; the Act covers 40 of them (about 260,000 active licensees), including cosmetologists, barbers, massage therapists, electricians, plumbers, HVAC technicians, residential contractors, real estate salespersons and brokers, home inspectors, appraisers, pest control applicators, private investigators, dental hygienists, pharmacy technicians, interior designers and dietitians. Vennick, to the east, licenses nearly the same occupations at similar or higher requirements; the Brasholt metropolitan area straddles the border (about 60,000 daily commuters; about 4,000 covered licensees on the Vennick side). Orlesk, to the south, licenses fewer occupations at lower requirements (for example cosmetology 1,000 hours against Halvoran's 1,600; electricians 4,000 apprenticeship hours against 8,000) and issues voluntary state certificates in some occupations it does not license, including interior design and dietetics.

Under the law now in force, an out-of-state licensee is endorsed only if the board finds the origin state's requirements "substantially equivalent". Each year in 2024–2026: about 7,800 applied; about 3,500 were endorsed directly; about 4,300 had to complete added training or Halvoran exams (on average four months and $2,800); about 650 abandoned. Boards spend about 6 staff hours on an equivalency review and 2 on a top-up exam; a recognition check would take about 1.5. Boards are fee-funded ($120 per application; $150 per top-up exam). About 1,900 of 14,000 yearly enrollments at Halvoran's private schools in covered occupations are out-of-state licensees doing top-up hours. Cosmetology tuition is about $15,000 in Halvoran and $9,000 in Orlesk; Orlesk's cosmetology and massage schools admit non-residents and Orlesk licenses their graduates; its electrical apprenticeships require an Orlesk employer. Electrical and HVAC contractors report waits of three to six weeks.

| Field | Value | Source sentence |
|---|---|---|
| Jurisdiction (and what lies just outside) | State of Halvoran. Vennick (Brasholt metropolitan area across the border); Orlesk to the south. | §1 |
| Announced / enacted / effective / expires | Introduced 12 January 2027 with the governor's support and majorities on record (announced). Signed 30 April 2027. Effective 1 January 2028. No expiry. | §12 |
| Enforcement (who, penalties, resources) | Boards issue licenses and discipline as before; recognized licensees subject to the same discipline. Within existing fee-funded budgets. | §8 |
| Existing rules (stay in the counterfactual) | Licensing laws for the 40 occupations, with endorsement by substantial equivalence; practising without a Halvoran license is an offense (fine up to $1,000). | Occupational Code |

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Recognition | Removal, for one class of entrant, of the training and exam conditions of a `licensing_requirement` | Out-of-state licensees in the 40 occupations | Boards | Applicant who has held another state's license for a similar scope for at least one year, in good standing, and establishes residence in Halvoran, is licensed without further education, experience or exam, on the usual fee and a background check, within 30 days. | Discipline pending. |
| K2 Law exam | Remaining condition | Seven Schedule B occupations | Recognized applicants in them | Halvoran law portion only (two hours, $60). | — |
| K3 Status | Rule on the license | Recognized licenses | — | Identical to any other license; the wall certificate does not show how it was obtained; the online registry records "issued by recognition" and the origin state. | — |
| K4 Administration | Administration | K1, K2 | Boards | Within existing fee-funded budgets. | — |
| K5 Pending applications | Transition | Endorsement applications pending on 1 January 2028 | Boards | Decided under K1 and K2 at the applicant's request. | — |

Unclear provisions:
- **U1, voluntary certificates.** U1-a: a state-issued voluntary certificate counts as "a license issued by another state", so a holder of an Orlesk certificate for a year is recognized. U1-b: only a credential required to practise in the issuing state counts. No probability; one sign per reading.

Counterfactual: Halvoran without the Act; the 40 licensing laws stay in force with endorsement by substantial equivalence. Because the Act is a partial repeal, each consequence also carries `persistence`, compared with a path on which out-of-state licensees had never faced the barrier.

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | CR-1 operations | Core rules applied |
| --- | --- | --- | --- | --- |
| K1 Recognition | triangular (removes a restraint on exchanges between out-of-state licensees and Halvoran buyers) | Yes: the top-up bound about 4,300 a year and deterred others (A-1) | 3 (removes the top-up burden from the option "move and practise" for those who would have needed it); 2 (adds that option for those who would have abandoned or not moved); 2 (adds a route for Halvoran residents: train and license in Orlesk, hold one year, apply, A-5); per U1: U1-a op 2 for Orlesk certificate holders, U1-b none | CR-3b, CR-4, CR-5, CR-6, CR-7a, CR-7 (0.7: a policy that makes a means mobile), CR-9, CR-10, CR-11c |
| K2 Law exam | triangular (condition kept) | Yes for Schedule B applicants | 3 (two hours and $60 attached to recognition); relative to the counterfactual, a smaller burden than a top-up and, for applicants who would have been endorsed directly, a burden added if the law now in force sets no exam for them (A-N1) | CR-3, CR-8c |
| K3 Status | triangular (bears on what the license tells buyers) | — | No operation on options; changes what the license conveys (CR-11c) | CR-11c |
| K4 Administration | binary (fee-funded board time) | — | 3 (changes boards' tasks: recognition checks replace equivalency reviews and top-up exams) | CR-8c, arithmetic |
| K5 Pending applications | transition | — | 2 (adds the K1 route to applicants pending on 1 January 2028) | CR-10a |

The counterfactual law requires a top-up of out-of-state licensees whose state is not found substantially equivalent (CR-1 recording note). K1 removes that burden only for those who meet the one-year and residence conditions; the barrier stays for commuters who do not move (residence), for licensees with less than a year, and, under U1-b, for certificate holders.

## 3. Actor classes

| Actor class | Role | How its options change (CR-1) |
| --- | --- | --- |
| movers.would_top_up | Out-of-state licensees who would have moved and completed a top-up (about 4,300 a year) | Op 3: four months and $2,800 removed (Schedule B: $60 law exam added). |
| movers.would_abandon_or_stay_out | Licensees who would have abandoned (about 650) or not applied | Op 2: moving and practising is now open on usual fees. |
| movers.endorsed_directly | Licensees who would have been endorsed directly (about 3,500) | Review by recognition check; Schedule B: law exam (A-N1). |
| movers.pending | Applicants pending on 1 January 2028 | Op 2 (K5). |
| halvoran_residents.prospective_trainees | Residents who would train in a covered occupation | Op 2: train and license in Orlesk, hold one year, apply (A-5). |
| orlesk_certificate_holders | Interior designers and dietitians with Orlesk voluntary certificates | U1-a: op 2; U1-b: none. |
| incumbents | Halvoran licensees in the covered occupations | Through CR-9: more competitors for the same buyers. |
| employers | Salons, contractors and firms that employ licensees | Through CR-9: more workers available; recognized licensees setting up on their own (A-18). |
| buyers.current, buyers.prospective | Households and firms buying covered services | Through CR-9: more sellers; the license no longer signals Halvoran training (CR-11c). |
| buyers.substitutes | Households that do the work themselves or use unlicensed providers | Through CR-9: licensed services become cheaper (A-16). |
| schools.halvoran | Private schools in covered occupations | Through CR-9: lose top-up enrollments and some resident trainees. |
| schools.orlesk | Orlesk schools | Through CR-9 (`across_border`): more Halvoran trainees (A-5). |
| officials.boards | Occupational boards | Op 3: recognition checks replace reviews and top-ups; more licensees to discipline. |
| neighboring_jurisdictions | Buyers and remaining licensees in East Brasholt and Orlesk | Through CR-9 (`across_border`): licensees leave for Halvoran (A-20). |
| tenants.border_areas | Renters on the Halvoran side of Brasholt | Through CR-9 (`complement`, location): movers must establish residence (A-9). |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-1 | movers.would_top_up | compliance_cost (training and exams to be licensed) | decrease | short; medium; long | CR-1 op 3, CR-3b, CR-8c | A-1 |
| C-2 | movers.would_top_up | wait_time (from arrival to licensed practice) | decrease | short; medium; long | CR-1 op 3, CR-3b | A-1 |
| C-3 | movers.would_top_up | resources_available_other_uses | increase | short; medium; long | CR-3 note, CR-8a | A-1 |
| C-4 | movers.would_top_up | earnings (first year in Halvoran) | increase | short; medium; long | CR-1 op 3, CR-5c | A-1 |
| C-5 | officials.boards | enforcement_cost (application review and top-up exams) | decrease | short; medium; long | CR-8c, arithmetic | A-22 |

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-6 | movers.would_abandon_or_stay_out | entry_rate (licensees moving into Halvoran and practising) | increase | medium; long | CR-4 (x: stay or abandon, y: move and practise), CR-7a, CR-7 (0.7) | A-2 |
| C-7 | movers (recent) | informal_activity (unlicensed practice while awaiting a license) | decrease | medium; long | CR-4 (x: comply, y: violate) | A-7 |
| C-8 | halvoran_residents.prospective_trainees | cross_border_purchases (training in Orlesk) | increase | medium; long | CR-4 (x: Halvoran school, y: Orlesk school plus one-year hold) | A-5 |
| C-9 | movers.would_top_up | quantity_traded (top-up enrollments and exams, 2027) | decrease | short (announcement window) | CR-10a, CR-4 (x: top up now, y: wait for recognition) | A-4 |
| C-10 | movers (all) | entry_rate (moves into Halvoran, 2027) | ambiguous | short (announcement window) | CR-10a, CR-12b | A-3, A-4 |
| C-11 | movers (all) | entry_rate (moves into Halvoran, 2028) | increase | short (first year in force) | CR-10a, CR-4, CR-12d | A-4 or A-2 |
| C-12 | movers (arrived early, waiting) | informal_activity (unlicensed practice, 2027) | increase | short (announcement window) | CR-10a, CR-4 (x: comply, y: violate) | A-3, A-7 |
| C-13 | movers.would_top_up (delaying) | earnings (2027) | decrease | short (announcement window) | CR-10a, CR-2, CR-4 | A-4 |
| C-14 | movers.pending | wait_time | decrease | short | CR-1 op 2 (K5), CR-3b | A-1 |
| C-15 | orlesk_certificate_holders | entry_rate (into Halvoran practice) | U1-a: increase; U1-b: no_change | medium; long | CR-1 op 2 per reading, CR-4 | A-6 |
| C-16 | movers.endorsed_directly (Schedule B) | compliance_cost (law exam) | increase | short; medium; long | CR-1 op 3, CR-8c | A-N1 |
| C-17 | incumbents | lobbying_effort (against the Act, then to restore the barrier) | increase | short; medium | CR-4 (x: accept, y: lobby), CR-8c | A-8 |
| C-18 | schools.halvoran | lobbying_effort (against the Act) | increase | short; medium | CR-4 (x: accept, y: lobby), CR-8c | A-8, A-1 |
| C-19 | recognized licensees | entry_rate (self-employment) | increase | medium; long | CR-4 (x: employee, y: own business) | A-18, A-2 |

## 6. Second-order effects

CR-9 along named relations, then CR-5 to CR-7. Depth limit 4. Diffuse effects on suppliers of salons and contractors are pruned at depth 3.

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C-20 | officials.boards | non_tax_receipts (top-up exam fees) | decrease | short; medium; long | CR-8b | — | A-1 |
| C-21 | officials.boards | non_tax_receipts (application fees) | increase | medium; long | CR-8b | — | A-2 |
| C-22 | officials.boards | non_tax_receipts (total fees) | ambiguous | medium; long | CR-12b | — | A-1, A-2 |
| C-23 | officials.boards | enforcement_cost (discipline of added licensees) | increase | medium; long | CR-8c | — | A-2 |
| C-24 | officials.boards | enforcement_cost (total) | ambiguous | medium; long | CR-12b | — | A-22, A-2 |
| C-25 | buyers.current, buyers.prospective | price_paid (covered services) | decrease | medium; long | CR-9, CR-6 | entrants and incumbents sellers in the same market (close) | A-2 |
| C-26 | buyers.current, buyers.prospective | quantity_traded (licensed covered services) | increase | medium; long | CR-9, CR-5, CR-4c | as above | A-2 |
| C-27 | buyers (electrical and HVAC work) | wait_time | decrease | medium | CR-6 | as above | A-2, A-17 |
| C-28 | buyers.substitutes | home_production (covered work done by households) | decrease | medium; long | CR-4 (x: do it oneself, y: hire licensed) | licensed service substitute for home production | A-2, A-16 |
| C-29 | buyers.substitutes | informal_activity (use of unlicensed providers) | decrease | medium; long | CR-4 (x: unlicensed, y: licensed) | licensed substitute for unlicensed provision | A-2, A-16 |
| C-30 | buyers (varied-standard occupations) | quality_information | decrease | medium; long | CR-11c | — | A-12, A-13 |
| C-31 | buyers (varied-standard occupations) | quality_variability (among licensed providers) | increase | medium; long | CR-9, CR-11c | — | A-13, A-14 |
| C-32 | buyers (varied-standard occupations) | quality_per_unit (licensed provision) | decrease | medium; long | CR-9, CR-11c | — | A-12, A-13, A-14 |
| C-33 | incumbents | wage_rate | decrease | medium; long | CR-9, CR-6, CR-7a, CR-7 (0.7) | as for C-25 | A-2, A-10 |
| C-34 | incumbents | employment (incumbents in covered occupations), hours_worked | at_least_one_decrease | medium; long | CR-4 (x: stay, y: leave or cut hours) | as above | A-2, A-11, A-10 |
| C-35 | employers | return_on_capital | ambiguous | medium; long | CR-9, CR-12b | labor input_to covered services; self-employed recognized licensees compete with employers | A-10, A-18, A-2 |
| C-36 | schools.halvoran | quantity_traded (top-up enrollments) | decrease | medium; long | CR-9, LW-10 | top-up training input_to licensing of movers | A-1 |
| C-37 | schools.halvoran | quantity_traded (enrollments by Halvoran residents) | decrease | medium; long | CR-9, CR-12d | Orlesk training substitute for Halvoran training (A-5); training input_to occupations whose wage falls (A-10) | A-5 or A-10 (independent chains) |
| C-38 | schools.halvoran | asset_value (schools) | decrease | short (from 12 January 2027) | CR-7c, CR-10c | as above | A-19, A-1 |
| C-39 | schools.orlesk | quantity_traded (enrollments by Halvoran residents) | increase | medium; long | CR-9 | across_border | A-5 |
| C-40 | tenants.border_areas | price_paid (rent, Halvoran side of Brasholt) | increase | medium | CR-9, CR-6 | residence complement (location) of recognition | A-9 |
| C-41 | neighboring_jurisdictions (buyers in East Brasholt and Orlesk) | price_paid (covered services) | increase | medium; long | CR-9, CR-6 | across_border: sellers leave | A-20 |
| C-42 | neighboring_jurisdictions (licensees who stay) | wage_rate | increase | medium; long | CR-9, CR-7a | across_border | A-20 |
| C-43 | incumbents (interior design and dietetics) | wage_rate | U1-a: decrease; U1-b: decrease | medium; long | CR-9, CR-6 | as for C-33 | A-2, A-10, A-6 |

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance premise | Combined sign |
| --- | --- | --- | --- | --- |
| movers, entry_rate, 2027 | Movers who move early to settle before the school year and wait (A-3) | Movers who would have topped up in 2027 delay their move into 2028 (A-4) | None | ambiguous (C-10) |
| movers, entry_rate, 2028 | Delayed moves land in 2028 (A-4); added movers (A-2) | none | — | increase (C-11), two independent chains (CR-12d) |
| officials.boards, non_tax_receipts | More applications at $120 (A-2) | No top-up exams at $150 for about 4,300 (A-1) | None: the number of added applications is a projection (9,500 to 14,000), so arithmetic does not settle it ($516,000 lost against $204,000 to $744,000 gained) | ambiguous (C-22); the two items are recorded separately (C-20, C-21) under CR-12 (0.8) |
| officials.boards, enforcement_cost | Discipline of more licensees (A-2) | Application review: about 7,800 × 6 + 4,300 × 2 = 55,400 hours now; at most about 14,000 × 1.5 = 21,000 hours plus law exams under K1 (A-22) | Arithmetic settles the review item only; discipline hours are not in the case | ambiguous total (C-24); review item decrease (C-5); discipline item increase (C-23) |
| employers, return_on_capital | Lower wage costs (A-10, A-2) | Recognized licensees compete as self-employed (A-18); lower output prices (C-25) | None | ambiguous (C-35) |
| buyers (varied-standard), quality_per_unit (licensed provision) | — | Lower-trained entrants (A-13, A-14) where training bears on quality (A-12) | — | decrease (C-32). The opposing chain on quality of what buyers receive overall, through buyers moving from home production and unlicensed providers to licensed ones, needs A-15 (p 0.45): below the cut-off, so the derived sign is reported and the chain is listed in section 10 (CR-12, 0.8 kind 2). It is also a different item (all provision, not licensed provision) |
| incumbents, wage_rate | — | More sellers in the same market (A-2), wages adjust (A-10) | — | decrease (C-33) |
| schools.halvoran, quantity_traded (residents) | — | Orlesk route (A-5); lower expected wages (A-10) | — | decrease (C-37) |
| buyers, price_paid (covered services) | Lower quality signal could raise search costs; no rule derives a price rise from it | Added sellers (A-2) | CR-12 (0.7): an underivable opposing effect is a Tier C note, not a chain | decrease (C-25) |
| orlesk_certificate_holders, entry_rate | — | — | — | U1-a: increase; U1-b: no_change (C-15) |

No chains cancel by construction (CR-12f).

## 8. Time structure

- **Announcement (12 January 2027 to 31 December 2027).** Passage was likely from introduction (governor's support, majorities on record), so school values fall then (C-38, CR-7c, CR-10c). Licensees who would have topped up in 2027 wait for recognition (C-9, A-4) and some delay their move into 2028 (C-10, C-11); their 2027 earnings fall (C-13). Others move early and wait (A-3), and some of them practise unlicensed in the meantime (C-12, A-7). These are signed per window. Pending applications on 1 January 2028 switch to K1 (C-14).
- **The one-year hold.** K1 requires a year of holding the out-of-state license. A Halvoran resident who trains in Orlesk (A-5) gains nothing in Halvoran until the year has passed, so the Orlesk route (C-8, C-37, C-39) builds up from 2029. Whether those residents practise in Orlesk during that year is A-21 (p 0.35); not used.
- **Gradual stock adjustment (CR-10b).** Licensed labor in Halvoran is a stock that changes through moves, training and retirement. Wages (C-33), prices (C-25) and waits (C-27) change as entrants arrive, not at once. Schools' capacity built for top-ups is a stock that persists until it wears out or is converted.
- **Expectations of return.** Incumbents and schools lobby (C-17, C-18). If movers believe recognition may be withdrawn, quick-payback moves go ahead and long-payback ones (buying a business, a home) are held back (CR-10a). No premise in the case says how likely reversal is, so no sign is given.

### Metamorphic check (the original barrier, and what the repeal does to it)

Derived for the barrier by the same rules, against a path with no barrier: (1) a top-up burden on about 4,300 movers a year (CR-1 op 3) and fewer movers (CR-4, about 650 abandoning); (2) top-up demand for Halvoran schools (CR-9) and higher school values (CR-7c); (3) higher incumbent wages and prices and longer waits for buyers (CR-6, CR-7b, by fewer sellers); (4) more home production and unlicensed provision (CR-4); (5) unlicensed practice by movers while waiting (CR-4); (6) board time on equivalency reviews and top-up exams (CR-8c); (7) a license that conveyed Halvoran-standard training (CR-11c); (8) Halvoran residents trained in Halvoran rather than Orlesk (CR-4).

| Effect of the barrier | Repeal consequence | Persistence |
| --- | --- | --- |
| (1) Burden on movers | C-1 to C-4 | none for new movers; costs already paid by past movers are the same with and without the repeal (CR-10b), so they are not consequences |
| (1) Fewer movers | C-6, C-11 | partial (medium): licensees who settled elsewhere in past years do not all come back; none (long) for new flows |
| (2) School demand and values | C-36 to C-38 | partial (medium): capacity built for top-ups remains (CR-10b); none (long) |
| (3) Higher wages, prices, waits | C-25, C-27, C-33, C-34 | partial (medium): the stock of licensees adjusts gradually; none (long) |
| (4) Home production and unlicensed provision | C-28, C-29 | partial (medium); none (long) |
| (5) Unlicensed practice while waiting | C-7 | none |
| (6) Board time | C-5 | none |
| (7) License as a signal of Halvoran training | C-30 to C-32 | partial: buyers' belief formed under the barrier persists after the fact it reflected has changed (A-13: most buyers do not check the registry). No long-run sign without a premise on how fast buyers learn |
| (8) Training location | C-8, C-37, C-39 | none (from 2029, after the one-year hold) |

**Not reversed by the repeal (the barrier persists):** commuters who do not establish residence (most of the 60,000 Brasholt commuters) still face substantial equivalence; licensees with less than a year of holding; Schedule B applicants face a law exam (K2); under U1-b, certificate holders. For these, persistence is full, and no consequence is recorded because their situation does not change.

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
| --- | --- | --- | --- | --- | --- |
| C-1 | movers.would_top_up | compliance_cost | decrease | Four months and $2,800 no longer used up on a top-up | CR-3b, CR-8c |
| C-5 | officials.boards | enforcement_cost (review) | decrease | Board hours freed for other uses | CR-8c |
| C-13 | movers.would_top_up (delaying) | earnings (2027) | decrease | Practice forgone while waiting for recognition | CR-3a (chosen by them as the better of two costly options) |
| C-16 | movers.endorsed_directly (Schedule B) | compliance_cost (law exam) | increase | Two hours and $60 | CR-8c |
| C-17, C-18 | incumbents, schools.halvoran | lobbying_effort | increase | Time and money spent on lobbying | CR-8c |
| C-23 | officials.boards | enforcement_cost (discipline) | increase | Board time on discipline of added licensees | CR-8c |
| C-41 | neighboring_jurisdictions (buyers) | price_paid | increase | Services bought at higher prices or not bought | CR-9, CR-6 |

CR-8b check (both sides of every transfer): fees no longer paid for top-up exams (C-20) are means kept by movers (C-3); application fees paid (C-21) are received by the boards; the tuition no longer paid to Halvoran schools for top-ups (C-36) is part of movers' gain (C-3); tuition paid to Orlesk schools (C-39) is withdrawn from Halvoran schools (C-37). Lower prices to buyers (C-25) are lower receipts to sellers, borne by incumbents (C-33) and employers in part (C-35). No general-fund budget is involved: the boards are fee-funded (K4).

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
| --- | --- | --- | --- | --- | --- |
| A-1 | The top-up binds: about 4,300 movers a year needed it, and about 650 abandoned. | binding | 0.9 | Board records, 2024–2026. | C-1 to C-4, C-14, C-18, C-20, C-36, C-38 fail. |
| A-2 | Some licensees who would not have moved, or would have abandoned, now move and practise. | mobility | 0.75 | Surveys; abandonment records; inflows elsewhere. | C-6, C-19, C-21, C-23, C-25 to C-29, C-33 to C-35, C-43 fail; C-11 keeps the A-4 chain. |
| A-3 | Some new movers can wait without practising and move in 2027 to settle before the school year. | other | 0.55 | School calendars; household moves. | C-10 becomes decrease; C-12 fails. |
| A-4 | Some movers who would have topped up in 2027 wait for recognition, and some delay their move into 2028. | expectations | 0.7 | Cost of the top-up against months of waiting; publicity. | C-9, C-13 fail; C-10 becomes increase; C-11 keeps the A-2 chain. |
| A-5 | Orlesk schools admit and license non-residents in school-based occupations, and some Halvoran residents choose that route. | alternative_uses | 0.6 | Orlesk rules; tuition gap; distance. | C-8, C-39 fail; C-37 keeps the A-10 chain. |
| A-6 | Some holders of Orlesk voluntary certificates would move if recognized. | mobility | 0.6 | Count of certificate holders; demand for interior designers. | C-15 becomes no_change under U1-a. |
| A-7 | Some movers practised without a Halvoran license while waiting. | enforcement | 0.6 | Board complaints. | C-7, C-12 fail. |
| A-8 | Incumbents' associations and schools can organize at a cost below their stake. | other | 0.85 | Their lobbying on the bill. | C-17, C-18 fail. |
| A-9 | Some East Brasholt licensees move to the Halvoran side, and its rental market is not slack. | mobility | 0.55 | Licensee counts; vacancy. | C-40 fails. |
| A-10 | Incumbents' wages can adjust over the medium run. | other | 0.8 | Wage growth in these occupations. | C-33, C-43 become employment and hours only (C-34); C-35 loses its (+) chain; C-37 keeps the A-5 chain. |
| A-11 | Some incumbents are at the margin of leaving the occupation or cutting hours. | alternative_uses | 0.6 | Exit rates; part-time shares. | C-34 fails. |
| A-12 | In the varied-standard occupations, buyers treated a Halvoran license as a sign of Halvoran training, and that training bears on quality they value and cannot judge. | other | 0.6 | Buyer surveys; curricula; discipline rates by training. | C-30, C-32 fail. |
| A-13 | The inflow includes licensees trained to lower requirements, and most buyers do not check the registry. | other | 0.55 | Origin of past applicants; registry searches. | C-30 to C-32 fail. |
| A-14 | Applicants from lower-requirement states are a larger share of recognized licensees than of endorsement applicants before. | other | 0.7 | The 4,300 who needed a top-up came mostly from such states. | C-31, C-32 fail. |
| A-15 | What buyers leave when they move to licensed providers (home production, unlicensed providers) is of lower quality than licensed provision. | other | 0.45 | Self-provision mostly for simple work; unlicensed providers often trained. | Below cut-off: see below. |
| A-16 | Some buyers do the work themselves or use unlicensed providers because licensed services cost too much. | substitutability | 0.75 | Household surveys. | C-28, C-29 fail. |
| A-17 | Waiting lists in electrical and HVAC work reflect a shortage of licensed workers. | other | 0.6 | Contractors' reports of three to six weeks. | C-27 fails. |
| A-18 | Some recognized licensees set up on their own and compete with employers. | other | 0.6 | Self-employment shares. | C-19 fails; C-35 loses its (−) chain from self-employment. |
| A-19 | Schools' values rest on expected enrollment, and passage was likely from introduction. | expectations | 0.7 | Sale prices of schools; legislative support. | C-38 moves later or fails. |
| A-20 | Licensees near the borders are at the margin of moving into Halvoran. | mobility | 0.65 | 4,000 covered licensees in East Brasholt; Orlesk wage gaps. | C-41, C-42 fail. |
| A-21 | Halvoran residents who train in Orlesk work there during the holding year. | other | 0.35 | Commuting distances. | Below cut-off: see below. |
| A-22 | Applications and added discipline cases stay well below four times the present level. | other | 0.9 | Boards' projection (9,500 to 14,000 applications). | C-5 loses its arithmetic. |
| A-23 | Buyers do not distinguish between occupations when they learn that some recognized licenses certify less. | other | 0.3 | None. | Below cut-off: see below. |
| A-N1 | Under the law now in force, applicants endorsed directly in Schedule B occupations sit no Halvoran law exam. | other | 0.5 | NEW. The record lists added training or exams only for applicants not found substantially equivalent; K2 is stated as a new condition. | C-16 fails. |

**Not reported** (an assumption below 0.5):
- Buyers who move from home production and unlicensed providers to licensed ones receive higher quality than before (CR-4, CR-9): needs A-15 (p 0.45). This is the opposing chain to a quality claim for all provision; C-32 (licensed provision only) keeps its derived sign (CR-12, 0.8 kind 2).
- Orlesk employment of Halvoran residents during the holding year, and the Orlesk wage effect of it (CR-9, CR-6): needs A-21 (p 0.35).
- A fall in buyers' willingness to pay for licensed services in occupations without a quality difference, through distrust spreading across occupations (CR-11c): needs A-23 (p 0.3).

### Final check before the report

1. *Uncombined chains.* Every key with opposing chains is in section 7: 2027 moves, board fees, board costs, employers' returns. Licensed-provision quality has no derived opposing chain above the cut-off.
2. *Single signs for a group.* Incumbents' employment and hours are a group (C-34). The review and discipline items of board cost are recorded separately with their total.
3. *Baseline.* All signs are against the barrier staying in force, not against no licensing at all and not against the situation before 2027.
4. *Worse off is not poorer.* `resources_available_other_uses` is signed only for movers who would have paid the top-up anyway (C-3), a sum they could not avoid if they moved.
5. *Timing shifts.* 2027 and 2028 moves, top-up enrollments and unlicensed practice are signed per window (C-9 to C-13).
6. *Both sides of every transfer.* Checked in section 9.
7. *Every class, every rule.* CR-4 for each mover class (move, wait, top up, practise unlicensed, train in Orlesk, self-employment), for incumbents (stay, leave, lobby), for buyers (licensed, home production, unlicensed); CR-6 in covered services, rentals and neighboring markets; CR-7c for schools (the only durable tradable asset tied to the barrier; licenses are not tradable); CR-9 along same-market, input_to, substitute, across_border and complement (location) relations. No `contract`, `currency`, `shared_facility`, `proximity` or `gift` relation carries a chain. CR-11c for what the license conveys.
8. *Unstated premises.* A-N1 added.

## 11. Report

**The policy:** From 1 January 2028, anyone who has held another state's license in one of 40 occupations for at least a year, in good standing, and moves to Halvoran, receives a Halvoran license within 30 days without further training or exams. Seven occupations keep a two-hour law exam. The license looks the same as any other; the online registry shows how it was obtained. Whether Orlesk's voluntary certificates count as licenses is unclear (U1).

**Visible consequences:** Out-of-state licensees who would have had to top up save about four months and $2,800 and practise sooner (C-1 to C-4). More licensees move and practise (C-6). Boards spend less time reviewing applications (C-5).

**Invisible consequences:**
- *Incumbents and employers:* Incumbents' wages fall and some leave or cut hours (C-33, C-34); employers' returns move both ways (C-35); incumbents lobby (C-17).
- *Buyers:* Pay less, buy more licensed work, wait less for electricians and HVAC technicians, and do less themselves or through unlicensed providers (C-25 to C-29). In occupations whose standards differ between states, buyers learn less from the license (C-30), quality among licensed providers varies more (C-31) and is lower on average (C-32).
- *Schools:* Halvoran schools lose top-up and resident enrollments and value (C-36 to C-38) and lobby (C-18); Orlesk schools gain Halvoran residents (C-39), who train there and return after a year (C-8).
- *Movers:* Fewer practise unlicensed while waiting (C-7); recognized licensees set up on their own (C-19); Schedule B applicants who would have been endorsed directly now sit a law exam (C-16).
- *Transition:* In 2027, top-ups fall (C-9), some movers delay their move or practice (C-13) and some who arrive early practise unlicensed (C-12); moves rise in 2028 (C-11).
- *Neighbors:* Rents rise on the Halvoran side of Brasholt (C-40); buyers in East Brasholt and Orlesk pay more, and the licensees who stay there earn more (C-41, C-42).

**Ambiguous effects:** Moves in 2027 (C-10): early settling against delay. Boards' fee receipts (C-22) and total costs (C-24): fewer top-up exams and reviews against more applications and discipline. Employers' returns (C-35): cheaper labor against new self-employed rivals and lower prices.

**Key conditions:** The top-up binds (A-1, 0.9) and some licensees respond by moving (A-2, 0.75); wages adjust (A-10, 0.8); the quality chain rests on A-12 (0.6), A-13 (0.55) and A-14 (0.7); the Orlesk route on A-5 (0.6); Brasholt rents on A-9 (0.55). One premise was added, on whether directly endorsed Schedule B applicants sat a law exam before (A-N1, 0.5). Whether buyers who leave home production gain quality (A-15, 0.45) is below the cut-off.

**What this analysis cannot say:** How many licensees move, how far wages and prices fall, or how much quality falls in any occupation. It does not weigh movers' and buyers' gains against incumbents' and schools' losses, or say whether the Act is good. Health and safety effects of differences in training are out of scope; only quality as buyers value it is analyzed.

## Consequence list (normal form)

Persistence is compared with a path on which out-of-state licensees never faced the barrier (see the metamorphic check in section 8).

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions | Persistence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C-1 | movers.would_top_up | compliance_cost (training and exams to be licensed) | decrease | short; medium; long | visible | B | CR-1 (op 3: K1 removes the top-up burden); CR-3b; CR-8c (resources no longer used up on qualifying) | A-1 | none |
| C-2 | movers.would_top_up | wait_time (from arrival to licensed practice) | decrease | short; medium; long | visible | B | CR-1 (op 3: about four months replaced by at most 30 days); CR-3b | A-1 | none |
| C-3 | movers.would_top_up | resources_available_other_uses | increase | short; medium; long | invisible | B | CR-3 note (a sum they kept paying to move and practise, $2,800, is no longer taken); CR-8a | A-1 | none |
| C-4 | movers.would_top_up | earnings (first year in Halvoran) | increase | short; medium; long | visible | B | CR-1 (op 3); CR-5c (months of licensed practice, previously spent qualifying, become available for exchange) | A-1 | none |
| C-5 | officials.boards | enforcement_cost (application review and top-up exams) | decrease | short; medium; long | invisible | B | CR-8c; arithmetic on the case figures: about 55,400 hours a year now against at most about 21,000 under K1 at the boards' upper projection (A-22) | A-22 | none |
| C-6 | movers.would_abandon_or_stay_out | entry_rate (licensees moving into Halvoran and practising) | increase | medium; long | visible | B | CR-4 (x: stay out or abandon, y: move and practise; y made better by removing a lumpy cost, CR-4 units note); CR-7a; CR-7 (0.7: a policy that makes a means mobile, the gain goes to the owner of the means) | A-2 | partial (medium); none (long) |
| C-7 | movers (recent) | informal_activity (unlicensed practice while awaiting a license) | decrease | medium; long | invisible | B | CR-4 (x: wait unlicensed, y: practise unlicensed; the wait falls from months to at most 30 days, so fewer movers face the choice for less time, A-7) | A-7 | none |
| C-8 | halvoran_residents.prospective_trainees | cross_border_purchases (training in Orlesk) | increase | medium; long | invisible | B | CR-1 (op 2: an Orlesk license held a year now leads to a Halvoran license); CR-4 (x: Halvoran school at $15,000 and 1,600 hours, y: Orlesk at $9,000 and 1,000 hours plus a year's hold, A-5) | A-5 | none |
| C-9 | movers.would_top_up | quantity_traded (top-up enrollments and exams, 2027) | decrease | short (announcement window) | invisible | B | CR-10a; CR-4 (x: top up in 2027, y: wait for recognition in 2028, A-4) | A-4 | n/a |
| C-10 | movers (all) | entry_rate (moves into Halvoran, 2027) | ambiguous | short (announcement window) | invisible | B | CR-10a; CR-12b: (+) movers who settle early and wait (A-3); (−) movers who delay into 2028 (A-4). No dominance premise | A-3, A-4 | n/a |
| C-11 | movers (all) | entry_rate (moves into Halvoran, 2028) | increase | short (first year in force) | invisible | B | CR-12d, two independent chains: CR-10a and CR-4 (delayed moves land in 2028, A-4); CR-4 (added movers, A-2) | A-4 or A-2 | n/a |
| C-12 | movers (arrived early, waiting) | informal_activity (unlicensed practice, 2027) | increase | short (announcement window) | invisible | B | CR-10a (early moves, A-3); CR-4 (x: wait unlicensed, y: practise unlicensed; A-7) | A-3, A-7 | n/a |
| C-13 | movers.would_top_up (delaying) | earnings (2027) | decrease | short (announcement window) | invisible | B | CR-10a; CR-2 (they rank waiting for recognition above topping up); CR-4 (months without licensed practice in 2027, A-4) | A-4 | n/a |
| C-14 | movers.pending | wait_time | decrease | short | invisible | B | CR-1 (op 2: K5 lets pending applicants switch to K1); CR-3b | A-1 | n/a |
| C-15 | orlesk_certificate_holders | entry_rate (into Halvoran practice) | U1-a: increase; U1-b: no_change | medium; long | invisible | B | U1-a: CR-1 op 2 and CR-4 (x: stay, y: move; A-6). U1-b: no operation on their options | A-6 | none |
| C-16 | movers.endorsed_directly (Schedule B) | compliance_cost (law exam) | increase | short; medium; long | invisible | B | CR-1 (op 3: two hours and $60 attached, if no exam applied to them before, A-N1); CR-8c | A-N1 | n/a |
| C-17 | incumbents | lobbying_effort (against the Act, then to restore the barrier) | increase | short; medium | invisible | B | CR-4 (x: accept, y: lobby; their wage loss, C-33, gives them a stake); CR-8c | A-8 | n/a |
| C-18 | schools.halvoran | lobbying_effort (against the Act) | increase | short; medium | invisible | B | CR-4 (x: accept, y: lobby; their enrollment loss, C-36); CR-8c | A-8, A-1 | n/a |
| C-19 | recognized licensees | entry_rate (self-employment) | increase | medium; long | invisible | B | CR-4 (x: work as an employee, y: set up on one's own; more licensees are now able to choose y, A-18) | A-18, A-2 | none |
| C-20 | officials.boards | non_tax_receipts (top-up exam fees) | decrease | short; medium; long | invisible | B | CR-8b (fees no longer paid are no longer received; $150 for about 4,300) | A-1 | none |
| C-21 | officials.boards | non_tax_receipts (application fees) | increase | medium; long | invisible | B | CR-8b ($120 per added application, A-2) | A-2 | none |
| C-22 | officials.boards | non_tax_receipts (total fees) | ambiguous | medium; long | invisible | B | CR-12b and CR-12 (0.8, two items): C-20 against C-21; the number of added applications is a projection, so no arithmetic settles it | A-1, A-2 | none |
| C-23 | officials.boards | enforcement_cost (discipline of added licensees) | increase | medium; long | invisible | B | CR-8c (more licensees subject to the same discipline, A-2) | A-2 | none |
| C-24 | officials.boards | enforcement_cost (total) | ambiguous | medium; long | invisible | B | CR-12b and CR-12 (0.8, two items): C-5 against C-23; discipline hours are not in the case | A-22, A-2 | none |
| C-25 | buyers.current, buyers.prospective | price_paid (covered services) | decrease | medium; long | visible | B | CR-9 (entrants compete with incumbents for the same buyers, A-2); CR-6 (more sellers at each price move the price to a lower clearing level) | A-2 | partial (medium); none (long) |
| C-26 | buyers.current, buyers.prospective | quantity_traded (licensed covered services) | increase | medium; long | invisible | B | CR-9; CR-4c (at a lower price, units not bought before are bought); CR-5 | A-2 | partial (medium); none (long) |
| C-27 | buyers (electrical and HVAC work) | wait_time | decrease | medium | invisible | B | CR-6 (the waits reflect excess demand at prevailing prices, A-17; more licensed workers close part of the gap) | A-2, A-17 | partial (medium) |
| C-28 | buyers.substitutes | home_production (covered work done by households) | decrease | medium; long | invisible | B | CR-9 (licensed service substitute for home production); CR-4 (x: do it oneself, y: hire licensed; y made cheaper, C-25, A-16) | A-2, A-16 | partial (medium); none (long) |
| C-29 | buyers.substitutes | informal_activity (use of unlicensed providers) | decrease | medium; long | invisible | B | CR-9; CR-4 (x: unlicensed provider, y: licensed provider; y cheaper, A-16) | A-2, A-16 | partial (medium); none (long) |
| C-30 | buyers (varied-standard occupations) | quality_information | decrease | medium; long | invisible | B | CR-11c (0.7: what buyers believed before, that a Halvoran license meant Halvoran training, A-12; the direction: a license now held by some trained to lower requirements, A-13, while the certificate does not show it, K3, and most buyers do not check the registry) | A-12, A-13 | partial (belief formed under the barrier persists) |
| C-31 | buyers (varied-standard occupations) | quality_variability (among licensed providers) | increase | medium; long | invisible | B | CR-9 (entrants from lower-requirement states join the licensed pool, A-13, in a larger share than before, A-14); CR-11c | A-13, A-14 | none |
| C-32 | buyers (varied-standard occupations) | quality_per_unit (licensed provision) | decrease | medium; long | invisible | B | CR-9 (the licensed pool now includes more providers trained to lower requirements, A-13, A-14); training bears on quality buyers value (A-12); CR-11c (buyers cannot sort by training without checking the registry). Opposing chain on all provision needs A-15 (p 0.45): not a chain above the cut-off | A-12, A-13, A-14 | none |
| C-33 | incumbents | wage_rate | decrease | medium; long | invisible | B | CR-9 (competitors for the same buyers and employers); CR-6; CR-7a (wages for the same labor brought into line as entrants arrive; adjusts as raises are set, A-10); CR-7 (0.7: loss falls on those who held the restraint) | A-2, A-10 | partial (medium); none (long) |
| C-34 | incumbents | employment (incumbents in covered occupations), hours_worked | at_least_one_decrease | medium; long | invisible | B | CR-4 (x: stay in the occupation at the old hours, y: leave or cut hours; x made worse by C-33, A-11). Group sign: the rule does not say which | A-2, A-11, A-10 | partial (medium); none (long) |
| C-35 | employers | return_on_capital | ambiguous | medium; long | invisible | B | CR-12b: (+) CR-9 (labor input_to their services is cheaper, C-33); (−) CR-9 (recognized licensees set up on their own and compete, A-18) and lower output prices (C-25). No dominance premise | A-10, A-18, A-2 | partial (medium); none (long) |
| C-36 | schools.halvoran | quantity_traded (top-up enrollments) | decrease | medium; long | invisible | B | CR-9 and LW-10 (top-up training was an input to licensing movers, now not required; about 1,900 a year) | A-1 | none |
| C-37 | schools.halvoran | quantity_traded (enrollments by Halvoran residents) | decrease | medium; long | invisible | B | CR-12d, two independent chains: CR-9 (Orlesk training substitute for Halvoran training, A-5); CR-9 and LW-10 (demand for training follows the expected wage of the occupation, C-33, A-10) | A-5 or A-10 (independent chains) | none |
| C-38 | schools.halvoran | asset_value (schools) | decrease | short (from 12 January 2027) | invisible | B | CR-10c, CR-7c (lower expected enrollment, C-36, C-37, borne by owners as passage became likely, A-19) | A-19, A-1 | partial (medium: capacity built for top-ups persists, CR-10b); none (long) |
| C-39 | schools.orlesk | quantity_traded (enrollments by Halvoran residents) | increase | medium; long | invisible | B | CR-9 (across_border: the other side of C-8) | A-5 | none |
| C-40 | tenants.border_areas | price_paid (rent, Halvoran side of Brasholt) | increase | medium | invisible | B | CR-9 (residence is a condition of K1, so recognition and a Halvoran residence are complements, location; East Brasholt licensees move, A-9); CR-6 (rental market not slack, A-9) | A-9 | none |
| C-41 | neighboring_jurisdictions (buyers in East Brasholt and Orlesk) | price_paid (covered services) | increase | medium; long | invisible | B | CR-9 (across_border: licensees at the margin leave for Halvoran, A-20); CR-6 (fewer sellers at each price) | A-20 | none |
| C-42 | neighboring_jurisdictions (licensees who stay) | wage_rate | increase | medium; long | invisible | B | CR-9 (fewer competitors); CR-7a | A-20 | none |
| C-43 | incumbents (interior design and dietetics) | wage_rate | U1-a: decrease; U1-b: decrease | medium; long | invisible | B | U1-b: CR-9, CR-6 (entrants from states that license these occupations, A-2, A-10). U1-a: the same chain plus Orlesk certificate holders (A-6); same sign, wider inflow | A-2, A-10, A-6 | partial (medium); none (long) |

## Gaps found

**(a) Steps no core rule covers.**
- GAP-045-C1: Persistence of a belief. When a rule that made a credential convey something is repealed, buyers' belief formed under the old rule persists until they learn otherwise (C-30). CR-10b covers stocks that change through flows, and CR-11c covers information a policy conveys, but no core rule states how beliefs adjust after the policy stops conveying something. The persistence entry for C-30 to C-32 is therefore given as partial with no long-run sign.
- No other step lacked a core rule.

**(b) Core-rule wording that was hard to apply.**
- CR-7 (0.7, "a policy that makes a means mobile") says the gain goes to the owner of the means and the loss to those who held the restraint. Here the restraint was held by no one contractually; incumbents and schools gained from it indirectly. The clause was applied by reading "held the restraint" as "gained from it", which the wording does not say.
- CR-12 (0.8, two items in one variable) for board costs and fees: arithmetic settles one item (review hours) but not the total. The rule does not say whether a partial arithmetic dominance can be recorded on the total.
- CR-1 for K2: whether the law exam is a burden added or a burden reduced depends on what the counterfactual law required of each applicant subclass, which the case does not state (A-N1). The recording note says to state the counterfactual law; the case left it open.
- CR-10b with "persistence" for a repeal: the rule distinguishes costs already incurred (not consequences) from transition effects (`n/a`), but not past exits from the market (licensees who settled elsewhere). Recorded as partial persistence of entry.
- CR-4 units note (lumpy costs) and the one-year hold: the Orlesk route pays only after a year, so whether a resident is "at the margin" depends on time preference over a year's delay (LW-7). CR-4 and CR-10 together cover it, but A-5 had to carry the whole premise.

**(c) Vocabulary missing from the ontology.**
- No variable for enrollments or training purchased; `quantity_traded` with a qualifier was used.
- No variable for buyers' beliefs or for the signal content of a credential distinct from `quality_information`.
- No actor class for training providers (schools) or for licensees as a class split by how they obtained the license.
- No variable for the number of moves into a jurisdiction (migration); `entry_rate` was used.
- The persistence field allows none, partial, full or n/a, but has no value for "partial, with no long-run sign", which C-30 needed.

## Comparison with the pattern-based analysis

**Summary.** The two versions agree on the main structure of the Halvoran case. Movers who would have topped up save the cost and keep the money. More licensees move in and practise. Licensed services become cheaper, with shorter waits and less self-provision and unlicensed work. Incumbents' wages fall, and some incumbents leave or cut hours. Employers' returns are ambiguous. Schools lose value from the introduction, residents train in Orlesk, and Orlesk schools gain. Across the border, prices and Brasholt rents rise. In occupations whose standards vary by state, the license tells buyers less, training varies more among licensed providers and quality falls. Moves in 2027 and boards' fee receipts are ambiguous. Both versions derive the signal results from CR-11c, the core version without the prompt of any pattern. That confirms the pattern version's finding that EN-11, applied as written, would give the wrong sign. The differences: the pattern version signs lobbying `ambiguous` on an unstated premise that the counterfactual has lobbying on the same question (C-11); it signs incumbents' money `earnings` (C-15) and total `employment` alone (C-17), where only a loss by their own ranking and a group are derivable; and it rests a decrease in total board cost on a premise that does not bound discipline hours (C-32). The core version signs quantity traded `increase` for all buyers without examining the information chain the pattern records as kind (3) (C-19), signs unlicensed practice in 2027 `increase` while ignoring the counterfactual's informal practice during top-ups (C-12), and omits several derivable consequences: buyers' information about formerly informal practitioners, `share_of_sellers_licensed`, buyers' means, and neighbors' quantity supplied. The pattern version omits enrollment losses, the separate fee and cost items that CR-12 (0.8) asks for, and pending applicants' wait.

Counts: M 19, V 6, S 3, OP 12, OC 7.

### Pattern version → core version

| Pattern ID | Matched core ID(s) | Class | Cause | Note |
| --- | --- | --- | --- | --- |
| C-1 | C-1, C-2 | M | | The pattern puts the wait inside `compliance_cost`; the core records it separately as `wait_time` (C-2). |
| C-2 | C-6, C-11 | M | | |
| C-3 | C-6, C-11 | V | | `job_changes` (moves) in the pattern; `entry_rate` (moves and practice) in the core. |
| C-4 | C-10 | V | | Same chains (A-3, A-4) and sign (ambiguous); `job_changes` against `entry_rate`. |
| C-5 | C-9, C-13 | V | | Entry into practice in 2027 decreases (A-4). The core records the same chain on top-up enrollments (C-9) and delayers' 2027 earnings (C-13), not on entry. |
| C-6 | C-8 | M | | |
| C-7 | C-15 | M | | |
| C-8 | none | OC | E | Under U1-a, demand for Orlesk certificates rises among practitioners in non-licensing states (CR-4, CR-10a). Derivable; core-version omission. The pattern cites only A-6 (holders would move), but the claim also needs a premise that non-holders can obtain the certificate (exam and experience). |
| C-9 | C-7 | M | | |
| C-10 | none | OC | E | Buyers of formerly informal practitioners gain `quality_information`. CR-11b: where an exchange moves back into the legal market, the means of learning (advertising, reputation, courts) become available again. Core-version omission. |
| C-11 | C-17, C-18 | S | P | Pattern: lobbying by incumbents and schools `ambiguous`, by RS-7's Unless clause, on the ground that a reintroduced bill would be lobbied against without the Act. Core: increase (CR-4, x: accept, y: lobby). The counterfactual is Halvoran without the Act, and nothing in the record puts a bill or a contest on this question there. Lobbying in the counterfactual is an empirical premise, and the pattern states none. In WE-044 the same catalog version reached the opposite conclusion on the same point ("without the ordinance there would be no contest"). Partly a pattern problem: RS-7's Unless, with its parenthetical "(a repeal, where the policy's beneficiaries would lobby to keep it in force)", reads as if every repeal's counterfactual has such lobbying. Partly an analyst misapplication: no premise was stated. |
| C-12 | C-25 | M | | |
| C-13 | C-25, C-33 | V | | Self-employed incumbents' `net_price_received` decrease. The core records it through buyers' price (C-25) and its CR-8b check ("lower prices to buyers are lower receipts to sellers"), not as a row. |
| C-14 | C-33 | M | | |
| C-15 | none | OC | P | Incumbents' money `earnings` decrease, derived by CR-12a from a lower wage and price. CR-12c forbids netting different variables. Earnings also depend on hours, and CR-4's exception allows hours offered to rise when the wage falls. Leavers' earnings depend on their next-best occupation (the point of EN-3's 0.5 revision). What CR-7b and CR-10c do give is a fall in the expected yield of incumbents' training and license, a loss by their own ranking with no variable in 2.4 (the pattern's Gaps d3). The core rightly does not sign money earnings. Analyst misapplication. |
| C-16 | C-34 | M | | |
| C-17 | none | OC | E | Total `employment` in covered occupations increase, by CR-12e. The response argument binds total licensed supply: incumbents' cuts cannot push the price back up past the counterfactual. It does not bind heads: if leavers are part-timers and entrants full-time, heads can fall while hours rise. Derivable form: `employment`, `hours_worked` `at_least_one_increase`. Pattern-version overclaim of one member (final check 2). The core version records services traded (C-26) but omits the labor total altogether. |
| C-18 | C-26 | M | | The core signs all buyers. For uniform-standard occupations it agrees with the pattern. |
| C-19 | C-26 | S | J | Varied-standard occupations. Pattern: `quantity_traded` `ambiguous`, since a lower price (+) meets an information chain whose own direction CR-11 (0.7) leaves open, kind (3). Core: `increase` for all buyers; the information chain is not discussed for quantity, only as a Tier C note for price. Both readings of CR-12 (0.8) are defensible: an information chain with no derivable direction can be read as kind (3) (ambiguous) or kind (1) (a Tier C note, derived sign kept). The core version should at least have recorded the chain and its classification, since its own C-30 establishes the information change. |
| C-20 | C-30 | M | | |
| C-21 | C-31 | M | | |
| C-22 | C-32 | V | | Same sign and premises. The pattern signs quality received by varied-standard buyers, with the opposing A-15 chain below the cut-off. The core restricts the row to licensed provision and records the A-15 chain as concerning all provision. |
| C-23 | C-28, C-29 | V | | The core splits the pattern's `quantity_substitute` into `home_production` and `informal_activity` (unlicensed providers). |
| C-24 | C-27 | M | | |
| C-25 | none | OC | E | Buyers who keep buying have more for other uses (CR-8b; the mirror of the CR-3 note). Derivable for buyers who keep buying the same amount. Those who buy more may spend more, so the pattern's qualifier should say "the same amount". Core-version omission (its final check 4 considered only movers). |
| C-26 | C-35 | M | | |
| C-27 | C-38 | M | | |
| C-28 | none | OC | E | Neighbors' `quantity_supplied` of licensed services decreases (CR-4 for licensees at the margin of moving, A-20). The core's C-41 and C-42 rest on this chain ("fewer sellers at each price") but do not record it. Core-version omission. |
| C-29 | C-41 | M | | |
| C-30 | C-40 | M | | |
| C-31 | C-39 | M | | |
| C-32 | C-5, C-24 | S | A | Pattern: total licensing administration `decrease`. Core: the review item decreases (C-5, by the same arithmetic), discipline of added licensees increases (C-23), and the total is `ambiguous` (C-24). The pattern's dominance premise A-22 ("applications and added discipline cases stay well below four times the present level") bounds the number of applications but does not compare discipline hours with the roughly 32,000 review hours saved. The stock of recognized licensees, and so discipline, grows every year. A premise stated as a bound on discipline hours would be a valid CR-12e dominance premise, at least at the short horizon. Difference of premises; A-22 as worded does not do the work. |
| C-33 | C-22 | M | | The core's arithmetic understates the lost top-up fees: about 4,300 × $150 = $645,000, not $516,000 (which is 4,300 × $120). The sign is unaffected. |
| C-34 | none | OC | E | `share_of_sellers_licensed` `no_change`, Tier A. CR-1: every legal seller must still hold a Halvoran license, and K3 makes a recognized license one. Trivially derivable; core-version omission (as in WE-003). |
| C-35 | C-3 | M | | |

### Core-only consequences

| Core ID | Class | Cause | Note |
| --- | --- | --- | --- |
| C-4 | OP | J | Earnings in the first year in Halvoran rise for movers who would have topped up anyway: about four months of licensed practice replace training (A-1). The pattern declines money earnings for marginal movers (C-3 discussion), a different class. Defensible with A-1, though movers who worked during top-ups gain less. |
| C-12 | OP | E | Unlicensed practice in 2027 `increase`. The core cites A-3, which is stated for movers who "can wait without practising". It also ignores the counterfactual: movers who would have topped up in 2027 would have practised unlicensed while doing so (A-7), and some now delay their move (A-4). That is a (−) chain at p ≥ 0.5, so the sign is `ambiguous` (CR-12b). Core-version error. |
| C-14 | OP | E | Pending applicants' wait falls (K5, CR-1 op 2). Derivable. The pattern discusses K5 only for its timing effects. Pattern-version omission. |
| C-16 | OP | A | A law exam added for Schedule B applicants who would have been endorsed directly, if none applied before (A-N1, p 0.5). The core adds the premise; the pattern did not consider that subclass. CR-1's recording note asks for the counterfactual law for each subclass. |
| C-19 | OP | E | Recognized licensees set up on their own (CR-4; A-18). The pattern states A-18 and uses it inside C-26 but records no row. Pattern-version omission. |
| C-20 | OP | E | Top-up exam fees decrease. CR-12 (0.8, two items in one variable) asks for each item as its own consequence, with the total separately. The pattern records only the total (C-33). Pattern-version omission. |
| C-21 | OP | E | Application fees increase. As C-20. |
| C-23 | OP | E | Discipline of added licensees increases (CR-8c). The pattern folds it into C-32's total; CR-12 (0.8, two items) asks for it separately. Pattern-version omission. |
| C-36 | OP | E | Top-up enrollments at Halvoran schools decrease (about 1,900 a year). Stated in the pattern's prose (section 6) but not recorded. Pattern-version omission. |
| C-37 | OP | E | Residents' enrollments at Halvoran schools decrease, through two independent chains (Orlesk route, A-5; lower expected wages, A-10). Stated in prose, not recorded. Pattern-version omission. |
| C-42 | OP | E | Licensees who stay in East Brasholt and Orlesk earn higher wages (CR-9, CR-7a; A-20). Derivable; the pattern records only buyers' prices there. Pattern-version omission. |
| C-43 | OP | J | Interior design and dietetics wages decrease under both readings: a subset of C-33, split by reading. Adds no sign. |

### Findings

- **Pattern overclaims or hidden premises.** RS-7's Unless clause, applied without a premise, gave `ambiguous` lobbying (C-11). The clause's parenthetical invites the reading that every repeal's counterfactual has lobbying on the same question, which is an empirical matter. Incumbents' money `earnings` (C-15) were signed by netting wage and price (contrary to CR-12c) with no premise on hours or on leavers' next-best occupation; EN-3's 0.5 revision states that very premise. Total `employment` alone (C-17) was signed where CR-12e binds total supply only, and the group is the derivable form. The total board cost decrease (C-32) rests on A-22, which does not bound discipline hours. C-8 needs a premise that practitioners can obtain the Orlesk certificate.
- **Errors in the core version.** Unlicensed practice in 2027 (C-12) leaves an opposing chain uncombined (top-up movers who would have practised unlicensed and now delay) and should be `ambiguous`. Quantity traded for varied-standard buyers (C-26) is signed without recording the information chain; this is a judgment call, but the chain belongs in section 7. Omissions: buyers' `quality_information` for formerly informal practitioners (CR-11b), `share_of_sellers_licensed` `no_change` (CR-1), buyers' means (CR-8b), neighbors' quantity supplied, demand for Orlesk certificates under U1-a, and the labor total as a group. Arithmetic slip: lost top-up fees are about $645,000, not $516,000 (no sign change).
- **Errors in the pattern version (omissions).** Halvoran schools' top-up and resident enrollments (core C-36, C-37); the separate fee and cost items CR-12 (0.8) asks for (C-20, C-21, C-23); pending applicants' wait (C-14); self-employment entry (C-19); stayers' wages across the border (C-42); and the Schedule B subclass endorsed directly (C-16, on A-N1).
- **Test of 0.8 verdicts.** *EN-11 for a license whose content varies by issuer (failed):* confirmed. Without EN-11, the core version derived `quality_information` decrease (C-30), `quality_variability` increase (C-31) and `quality_per_unit` decrease (C-32) from CR-11c with the same premises, the opposite of what EN-11 as written gives for recognized licensees' buyers. *CR-12 0.8, three kinds of opposing chain (needed interpretation at the line between kinds 1 and 2):* confirmed, and the core version shows the same uncertainty in a second place. It treated the information chain on price as a kind (1) Tier C note, and did not classify the chain on quantity at all, where the pattern version used kind (3) (C-19). The line between kinds (1), (2) and (3) is unclear for an information chain whose direction CR-11 (0.7) leaves open.
- **Limits of the core rules.** None produced a difference: no S, OP or OC row has cause K. Unclear core-rule wording: (1) CR-11 (0.7) with CR-12 (0.8): whether a chain the rules derive but whose direction is open counts as kind (1), (2) or (3) (C-19). (2) CR-7c for a non-tradable license or training: both versions found that the loss falls on holders when the Act becomes expected, and neither had a variable or a clause to record it, so the pattern pushed it into `earnings` and the core left it out. (3) CR-12e (0.8): the response argument binds "the response as a whole", but the text does not say in which variable (supply in units, not heads) (C-17). (4) CR-7 (0.7): "those who held the restraint" when no one held it contractually (the core's Gaps b). (5) No core rule says how beliefs formed under a repealed rule decay (the core's GAP-045-C1), which leaves the persistence of C-30 to C-32 without a long-run sign.
