# WE-045 Universal recognition of out-of-state occupational licenses

Analyst: draft (Handbook 0.8 held-out test, corrected under 0.9)  |  Rule catalog version: 0.9  |  Status: awaiting expert review

A stylized policy in a fictional state. It resembles real "universal license recognition" laws but is not modeled on any one of them. It was written as a held-out test of catalog 0.8, which was tuned on WE-026 to WE-035. It probes: the partial removal of an entry barrier (the EN family applied in reverse, for one class of entrant only); a metamorphic check against WE-024, the full abolition of a license, derived here rather than copied; a license as a signal (EN-11) when what the license certifies now depends on the state that issued it; CR-7c and CR-10c for incumbents' license values and school enrollment; relocation across borders (RS-4) when the benefit is tied to residence; self-selection under a term that is the same for every applicant (the candidate "selection under a uniform term", 06_gaps.md 6.2e); RS-8's 0.8 clause on pending applications; OC-3's right baseline; and CR-12's three kinds of opposing chain. Health and safety effects of practitioners' competence are outside the scope of version 1. The probabilities are illustrative; the evidence column says what a real analysis would cite.

## 1. Policy record

**Halvoran Occupational Mobility Act.** The State of Halvoran has about 5.4 million people. It licenses about 70 occupations; the Act covers 40 of them (about 260,000 active licensees), among them cosmetologists, barbers, nail technicians, massage therapists, electricians, plumbers, HVAC technicians, residential contractors, real estate salespersons and brokers, home inspectors, appraisers, pest control applicators, private investigators, dental hygienists, pharmacy technicians, interior designers and dietitians. It does not cover physicians, nurses, lawyers, teachers or accountants.

To the east, the State of Vennick licenses nearly the same occupations at similar or higher requirements. The Brasholt metropolitan area straddles the border; about 60,000 people commute across it each day, and the Vennick side (East Brasholt) has about 4,000 licensees in covered occupations. To the south, the State of Orlesk licenses fewer occupations at lower requirements, and offers voluntary state certificates (exam plus experience, issued by a state board) in some occupations it does not license, including interior design and dietetics.

| Occupation (examples) | Halvoran | Vennick | Orlesk | Range across states |
|---|---|---|---|---|
| Cosmetologist | 1,600 hours, two exams | 1,500 hours | 1,000 hours | 1,000–2,100 hours |
| Massage therapist | 750 hours | 750 hours | 500 hours | 500–1,000 hours |
| Journeyman electrician | 8,000 apprenticeship hours, exam | 8,000 hours | 4,000 hours | 4,000–8,000 hours |
| Real estate salesperson | 90 hours, national and state exam | 75 hours | 60 hours | 40–180 hours |
| Interior designer | License: degree, experience, exam | License | No license; voluntary certificate | Licensed in a minority of states |

Under the law now in force, an out-of-state licensee is licensed by endorsement only if the Halvoran board finds the origin state's requirements "substantially equivalent". In 2024–2026, on average each year: about 7,800 out-of-state licensees in the covered occupations applied; about 3,500 were endorsed directly; about 4,300 had to complete added training or Halvoran exams (on average four months and $2,800); about 650 abandoned the process. Boards spend about 6 staff hours on an equivalency review and about 2 on administering a top-up exam; a recognition check (license status, duration, discipline) would take about 1.5 hours. Boards are funded by fees, set to cover their costs ($120 per application; $150 per top-up exam). About 1,900 of the 14,000 yearly enrollments at Halvoran's private schools in covered occupations are out-of-state licensees doing top-up hours. Cosmetology tuition is about $15,000 in Halvoran and $9,000 in Orlesk; Orlesk's cosmetology and massage schools admit non-residents and Orlesk licenses their graduates; its electrical apprenticeships require an Orlesk employer. Electrical and HVAC contractors in Halvoran report waits of three to six weeks for non-emergency work.

| Field | Value | Source sentence |
|---|---|---|
| Jurisdiction (and what lies just outside) | State of Halvoran. Vennick (Brasholt metropolitan area across the border); Orlesk to the south. | §1 |
| Announced / enacted / effective / expires | Introduced 12 January 2027 with the governor's support and majorities on record in both chambers (announced). Signed 30 April 2027. Effective 1 January 2028. No expiry. | §12 |
| Enforcement (who, penalties, resources) | The occupational boards issue licenses and discipline licensees as before; recognized licensees are subject to the same discipline. Within existing, fee-funded budgets. | §8 |
| Existing rules | The licensing laws for the 40 occupations, including endorsement by "substantial equivalence"; practising without a Halvoran license is an offense (fine up to $1,000). | Occupational Code |

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Recognition | Removal, for one class of entrant, of the training and exam conditions of a `licensing_requirement` | Out-of-state licensees in the 40 occupations | Boards | An applicant who has held for at least one year, in good standing, a license issued by another state for a similar scope of practice, and who establishes residence in Halvoran, is issued a Halvoran license without further education, experience or examination, on the usual fee and a background check, within 30 days. | Applicants with discipline pending. |
| K2 Law exam | Remaining condition | Seven occupations in Schedule B (real estate salesperson and broker, home inspector, residential contractor, appraiser, pest control applicator, private investigator) | Recognized applicants in those occupations | Must pass the Halvoran law portion of the exam only (two hours, $60). | — |
| K3 Status | Rule on the license | Recognized licenses | — | A recognized license is identical to any other Halvoran license; the wall certificate does not show how it was obtained. The online registry records "issued by recognition" and the origin state. | — |
| K4 Administration | Administration | K1, K2 | Boards | Within existing, fee-funded budgets. | — |
| K5 Pending applications | Transition | Endorsement applications pending on 1 January 2028 | Boards | At the applicant's request, decided under K1 and K2. | — |

Unclear provisions:
- **U1, voluntary certificates.** K1 requires "a license issued by another state". Orlesk does not license interior designers or dietitians, but its boards issue voluntary state certificates (exam and experience) that are not required to practise there. Reading U1-a: a state-issued certificate in an occupation Halvoran licenses counts as a license, so a holder of an Orlesk certificate for a year is recognized. Reading U1-b: only a credential required to practise in the issuing state counts, so certificate holders must qualify by Halvoran's own route. Readings get no probability; where a sign depends on U1, one sign per reading is given. Practitioners from states with neither a license nor a certificate are not recognized under either reading.

The counterfactual is Halvoran without the Act: the 40 licensing laws stay in force with endorsement by substantial equivalence. Every sign is relative to that, not to the situation before the Act and not to a Halvoran that never licensed these occupations. Because the Act is a partial repeal, `persistence` is recorded on each consequence, compared with a path on which out-of-state licensees had never faced the barrier (TS-6; workflow, "Analyzing a repeal").

## 2. Classification

| Component | Rothbard type | Binding? | Rule families |
|---|---|---|---|
| K1 | Removal, for one class of seller, of a triangular intervention. By CR-1: for out-of-state licensees who move, operation 3 removed (the burden of top-up training and exams is lifted from the option of practising in Halvoran) and, for those who would have abandoned, operation 2 (an option added); for incumbents, no operation on them directly; their situation changes through competition (CR-9). The operation is dated 1 January 2028 (CR-1, 0.8): before it, it acts only through expectations. The license requirement itself stays: no one may practise without a Halvoran license. | Yes for the 4,300 a year who needed top-up and the 650 who abandoned (A-1); not for the 3,500 endorsed directly. | EN-1 to EN-4 and EN-11 in reverse, RS-4, RS-5, RS-8, RS-10, RS-11 in reverse, CR-7 (0.7, a means made mobile), CR-7c, CR-10 |
| K2 | Keeps part of the triangular intervention for Schedule B | Yes, but light (two hours) | EN-1 |
| K3 | Shapes the information the license conveys | — | CR-11c, EN-11 |
| K4 | Binary in its funding (fee-funded boards) | — | OC-3 (right baseline) |
| K5 | Transition: improves the window before the effective date for applicants | — | RS-8 (0.8 Unless) |

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `licensees.out_of_state` (`sellers.prospective`) | Licensees elsewhere who would move to Halvoran, or now might | Practising in Halvoran no longer needs top-up training or exams; needs a year's licensure and Halvoran residence. |
| `licensees.voluntary_cert` | Holders of Orlesk voluntary certificates (interior design, dietetics) | Recognized under U1-a only. |
| `licensees.incumbent` (`sellers.current`) | Halvoran licensees, including those now in training | Face more licensed competitors. |
| `students.halvoran` | Halvoran residents who would train for a covered occupation | Can train in Orlesk instead and be recognized after a year. |
| `schools.halvoran` (`input_suppliers`) | Private schools in covered occupations | Lose top-up students and some resident students. |
| `schools.orlesk` (`neighboring_jurisdictions`) | Orlesk schools that admit non-residents | Gain Halvoran students. |
| `buyers.licensed_services` (`buyers.current`) | Buyers of covered services | More licensed sellers. Split: `buyers.uniform_standard` (occupations where origin requirements are close to Halvoran's, or the training tests nothing buyers value) and `buyers.varied_standard` (occupations where the training bears on quality buyers value and origin requirements differ widely: electrical, massage, dental hygiene, cosmetology chemical services). |
| `employers.licensed_services` | Salons, contractors, brokerages, clinics | More licensed applicants; more self-employed competitors. |
| `neighboring_jurisdictions` | Vennick and Orlesk sellers and buyers near the border | Licensees drawn across the line. |
| `tenants.brasholt` | Renters on the Halvoran side of Brasholt | Licensees from East Brasholt move a few kilometres to qualify. |
| `officials.enforcement` | Occupational boards | Recognition checks and law exams replace equivalency reviews and top-up exams. |
| Incumbents' associations, schools | Lobby | Stake in narrowing recognition. |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | `licensees.out_of_state` (movers) | `compliance_cost` (top-up training, exams, waiting) | decrease | short (from 2028) | CR-1, CR-3b, OC-2 | A-1 |
| C-2 | `licensees.out_of_state` | `entry_rate` (licensed practice in Halvoran) | increase | short–medium | EN-1 (in reverse), RS-4, CR-4 | A-1, A-2 |

C-1 is what the Act's supporters point to: about 4,300 movers a year no longer spend about four months and $2,800 on top-up training and exams. C-2: CR-4 with a lumpy cost (CR-4, units and lumpy costs): the top-up was a one-time cost attached to practising in Halvoran; removing it reverses the ranking for every licensee for whom it was decisive, including the 650 a year who abandoned and others who never applied (A-2). The entry is by relocation, since K1 requires Halvoran residence: RS-4 applies in the direction that favors the inside (`entry_rate` increase inside, `quantity_supplied` decrease just outside, C-28).

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-3 | `licensees.out_of_state` | `job_changes` (moves into Halvoran) | increase | medium | CR-7 (0.7), RS-11 (in reverse), CR-4 | A-2 |
| C-4 | `licensees.out_of_state` | `job_changes` (moves into Halvoran during 2027) | ambiguous | short | RS-8 (Unless), CR-10a, CR-12b | A-3, A-4 |
| C-5 | `licensees.out_of_state` | `entry_rate` (licensed practice in Halvoran during 2027) | decrease | short | RS-8, CR-10a | A-4 |
| C-6 | `students.halvoran` | `cross_border_purchases` (training bought in Orlesk) | increase | medium | RS-4, RS-5, CR-4 | A-5 |
| C-7 | `licensees.voluntary_cert` | `entry_rate` (into Halvoran) | U1-a: increase; U1-b: no_change | short–medium | CR-1, CR-4 | A-6 |
| C-8 | practitioners in states without a license requirement | `quantity_demanded` (Orlesk voluntary certificates) | U1-a: increase; U1-b: no_change | medium | CR-4, CR-10a | A-6, A-26 |
| C-9 | `licensees.out_of_state` (practising informally in Halvoran while awaiting a license) | `informal_activity` | decrease | short | RS-3 (in reverse), CR-1 | A-7 |
| C-10 | buyers of those practitioners | `quality_information` | increase | short | RS-10 (reverse clause) | A-7 |
| C-11 | Incumbents' associations, `schools.halvoran` | `lobbying_effort` | ambiguous | medium | RS-7 (Unless; Repeals, 0.9), CR-4 (0.9), EN-5, CR-12b | A-8, A-24 |
| C-36 | `licensees.out_of_state` (applications pending on 1 January 2028) | `wait_time` (to a Halvoran license) | decrease | short | CR-1, CR-3b | A-1 |

**A means made mobile (C-3).** A license tied to a state is a restraint on moving one's skill between states: moving to Halvoran used to cost the top-up. CR-7's 0.7 clarification applies to the removal of such a restraint: the gain from mobility goes to the owner of the means, here the licensee. They move more often, at the margin where the top-up decided against a move (RS-11 in reverse: the benefit lost on moving, an unrecognized license, is no longer lost). They are better off by their own ranking (CR-3b); money earnings would need a premise and are not signed.

**Timing (C-4, C-5).** Under RS-8 every provision is checked for whether it improves the earlier window. K5 does: an application filed in 2027 is decided under recognition, so moving and applying before the effective date is already protected. Two chains then oppose for moves in 2027 (C-4):
- (−) Licensees who would have moved in 2027 and done the top-up now wait for recognition; some of those for whom moving early without practising costs more than moving later delay the move into 2028 (A-4).
- (+) Licensees for whom recognition now makes the move worthwhile, and who can wait without practising, move in 2027 to settle before the school year and file under K5 (A-3).
The sign is **ambiguous** (RS-8 0.8 Unless), with no dominance premise in the case. Entry into practice in 2027 (C-5) is different: nobody can enter by recognition before 1 January 2028, and movers who would have finished a top-up within 2027 now wait for recognition instead, so 2027 entry falls; the other side of that shift is part of C-2 in 2028.

**License shopping (C-6).** A Halvoran resident who wants to become a cosmetologist can train for 1,000 hours in Orlesk ($9,000) rather than 1,600 in Halvoran ($15,000), hold the Orlesk license for a year, and be recognized (CR-4, x: train in Halvoran, y: train in Orlesk and wait a year; RS-4 for the purchase across the border; RS-5 for the reshaping of the route into the license). The residence condition does not block it: K1 asks for Halvoran residence at application, not for residence elsewhere when the license was obtained. It needs Orlesk to admit and license non-residents (A-5); for electricians it does not (an Orlesk employer is required), so this channel is limited to occupations with school-based training.

**Voluntary certificates (C-7, C-8).** Under U1-a, an Orlesk interior designer with the voluntary certificate is recognized after a year; under U1-b, not, and nothing changes for them. Under U1-a, practitioners in non-licensing states also have a new reason to obtain the Orlesk certificate (C-8, CR-10a), provided some of them can meet its exam and experience conditions (A-26).

**Informal practice (C-9, C-10).** Some licensees who moved and were waiting out a top-up practised without a Halvoran license (A-7). Recognition within 30 days removes most of that wait; once licensed there is nothing to evade (RS-3 in reverse), and their buyers can use reviews, advertising and the courts (C-10; RS-10's reverse clause). Unlicensed practitioners who hold no license anywhere gain nothing from the Act.

**Lobbying (C-11).** Incumbents' associations and schools lobbied against the bill; with the Act in force they lobby to widen Schedule B, lengthen the holding period or exclude states with low requirements. The counterfactual is the old rule in force. Whether it would have stayed contested there (a bill reintroduced, and lobbied against) is a premise, not a given (RS-7, Repeals, 0.9; CR-4, 0.9: lobbying in repeals is signed against the counterfactual path). The 0.8 version took it as given; it is now stated as A-24 (p = 0.6: the bill had the governor's support and majorities on record, so a reintroduction is likely on the path without the Act). With that premise at p ≥ 0.5, RS-7's Unless clause applies: each lobbied in both worlds on the same question, and the sign for each is `ambiguous` (CR-12b; kind 2). Out-of-state licensees are dispersed and not organized; no sign is given for them.

**Pending applications (C-36).** K5 also adds an option for applicants pending on 1 January 2028 (CR-1, operation 2): they may switch to recognition, decided within 30 days, instead of finishing a top-up of about four months. Those who switch obtain the license sooner (CR-3b).

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-12 | `buyers.licensed_services` | `price_paid` | decrease | medium | EN-1 (in reverse), CR-6 | — | A-1, A-2, A-27 |
| C-13 | `licensees.incumbent` (self-employed) | `net_price_received` | decrease | medium | EN-2 (in reverse), CR-6, CR-7b | — | A-1, A-2, A-27 |
| C-14 | `licensees.incumbent` (employed) | `wage_rate` | decrease | medium | CR-6, CR-7b | licensed labor `input_to` licensed services | A-1, A-2, A-10, A-27 |
| C-16 | `licensees.incumbent` | `employment`, `hours_worked` (incumbents in the occupation) | at_least_one_decrease | medium–long | RS-6, CR-4 | — | A-1, A-2, A-11 |
| C-17 | all licensed sellers in Halvoran | `employment`, `hours_worked` (total in covered occupations) | at_least_one_increase | medium | CR-4, CR-12e | — | A-1, A-2, A-25 |
| C-18 | `buyers.uniform_standard` | `quantity_traded` | increase | medium | CR-4c, OC-4 (in reverse) | — | A-1, A-2 |
| C-19 | `buyers.varied_standard` | `quantity_traded` | ambiguous | medium | CR-4c, CR-11c, CR-12b | — | A-1, A-2, A-12, A-13 |
| C-20 | `buyers.varied_standard` | `quality_information` | decrease | short–medium | CR-11c, EN-11 (Unless, 0.9) | — | A-12, A-13 |
| C-21 | `buyers.varied_standard` | `quality_variability` (among licensed sellers) | increase | medium | CR-4, CR-11c | — | A-12, A-14 |
| C-22 | `buyers.varied_standard` | `quality_per_unit` | decrease | medium | EN-4 (in reverse), CR-4, CR-12b | — | A-12, A-14 |
| C-23 | `buyers.licensed_services` | `quantity_substitute` (doing it themselves, unlicensed providers) | decrease | medium | EN-3 (in reverse), RS-1 | licensed and unlicensed or home provision: `substitute`, partial | A-1, A-2, A-16 |
| C-24 | `buyers.licensed_services` (electrical, HVAC) | `wait_time` | decrease | short–medium | CR-6, EN-1 (in reverse) | — | A-17 |
| C-25 | `buyers.licensed_services` (who keep buying the same amount) | `resources_available_other_uses` | increase | medium | CR-8b, CR-3b | — | A-1, A-2 |
| C-26 | `employers.licensed_services` | `return_on_capital` | ambiguous | medium | CR-7b, CR-12b | — | A-10, A-18 |
| C-40 | `licensees.out_of_state` (recognized) | `entry_rate` (self-employed practices) | increase | medium | CR-4 | — | A-2, A-18 |
| C-27 | `schools.halvoran` (owners) | `asset_value` | decrease | short (from 12 January 2027) | CR-7c, CR-10c | top-up and resident training `input_to` licensed practice | A-1, A-5, A-19 |
| C-37 | `schools.halvoran` | `enrollment` (top-up enrollments) | decrease | short–medium | CR-9, LW-10 | top-up training `input_to` licensing of movers | A-1 |
| C-38 | `schools.halvoran` | `enrollment` (Halvoran residents) | decrease | short–medium | CR-9, LW-10, CR-12d | Orlesk training `substitute` for Halvoran training; training `input_to` occupations whose pay falls | A-5 or A-10 (independent chains) |
| C-28 | `neighboring_jurisdictions` (Vennick and Orlesk sellers near the border) | `quantity_supplied` (licensed services) | decrease | medium | RS-4, CR-12b | Halvoran and neighbors' licensed services: `across_border`, close in Brasholt | A-2, A-20 |
| C-29 | `neighboring_jurisdictions` (buyers near the border) | `price_paid` (licensed services) | increase | medium | RS-13, CR-6 | as C-28 | A-2, A-20, A-27 |
| C-39 | `neighboring_jurisdictions` (licensees who stay near the borders) | `wage_rate` | increase | medium | CR-9, CR-7a, CR-6 | as C-28 | A-2, A-20, A-27 |
| C-30 | `tenants.brasholt` | `price_paid` (rent, Halvoran side) | increase | medium | CR-9, RS-4 | moves of licensees and housing: `complement`, location | A-9 |
| C-31 | `schools.orlesk` | `quantity_traded` (enrollment) | increase | medium | CR-9, RS-4 | as C-6 | A-5 |

**Prices, incumbents and the right comparison (C-12 to C-17).** More licensed sellers at the old price leave some unsatisfied, so the price falls (CR-6), and incumbents receive less (C-13; EN-2 in reverse). CR-6's 0.9 clause on splitting a shift asks for a premise about the other side before the price is signed: buyers do not absorb the added sellers at an unchanged price (A-27). Employed licensees face more licensed applicants for the same posts, so their wage grows less than it would have, as raises are set (C-14, A-10). The 0.8 version went on to sign incumbents' money `earnings` down (then C-15) by combining the lower wage and the lower price. That netted different variables (CR-12c), and it needed premises it did not state: hours offered can rise when the wage falls (CR-4's exception), and leavers' earnings depend on their next-best occupation (EN-3). C-15 is withdrawn. What the rules do give is a loss by incumbents' own ranking: the license and the training cannot be sold, and CR-7's 0.9 clause on assets without a market price says that a change in such an asset's expected yield is a loss by the holder's own ranking (CR-3a), borne by whoever holds the license, or is committed to the training, when the Act becomes expected (CR-7c, CR-10c); a change in money earnings would need a premise about the holder's next-best use. Students in training in January 2027 are among those who bear it. The training they paid for was paid in both worlds, so it is not a consequence of the Act (CR-10b); only the lower stream of returns is (no DM-3 trade-off arises). The loss has no variable in 2.4 (Gaps found, d3), so it is stated here and in the report, not in the consequence list. Some incumbents at the margin leave or cut hours (C-16, RS-6 group, A-11). Total licensed labor in the occupations still rises (C-17): incumbents leave only because the price falls, and the price falls only if licensed supply, net, has risen; the response cannot reverse the change that causes it (CR-12e, 0.8: this binds the response as a whole, not each incumbent). Two corrections under 0.9. The argument binds total licensed supply, not heads: if leavers are part-timers and entrants full-time, heads can fall while hours rise, so the derivable form is the group `employment`, `hours_worked` with `at_least_one_increase`, not `employment` alone. And CR-12's 0.9 clause on what the response argument gives says it shows only that supply is not reversed; a strict increase needs the response to be partial, here the premise that incumbents, whose training is sunk and specific, do not leave fast enough to offset the entry in the period (A-25).

**The license as a signal when its content varies (C-19 to C-22).** EN-11 says that where a license tests something buyers care about but cannot judge, licensed sellers' buyers have better `quality_information`. Under the Act the Halvoran license certifies something different depending on where its holder trained: 1,600 hours or 1,000 for a cosmetologist, 8,000 hours or 4,000 for an electrician. The wall certificate is the same (K3). Under 0.8 the pattern had no clause for that, and the analysis derived from CR-11c; EN-11's 0.9 Unless clause (a license issued on different requirements conveys less) now gives the same sign directly. The CR-11c derivation, with its 0.7 requirement of two premises:
- *What buyers believed before.* That a Halvoran license meant Halvoran training, in occupations where that training bears on quality they value and cannot judge (A-12, p = 0.6).
- *Which way those who learn move.* Buyers who do not check the registry now learn less from a license than before: `quality_information` decreases (C-20), given that the inflow includes licensees trained to lower requirements (A-13, p = 0.55; see C-21 for why the inflow is weighted toward them). Buyers who check the registry can still see the origin state. By CR-11's 0.9 clause on a signal that becomes noisier, buyers' beliefs adjust as they learn, at a speed that is empirical: C-20 is recorded with `persistence` partial and no long-run sign.

*Selection (C-21).* Recognition is the same term for every applicant, but what it saves depends on the origin state: nothing for a licensee from Vennick who would have been endorsed directly, the whole difference for one from Orlesk. By CR-4 applied to each applicant (x: stay, or move with a top-up; y: move by recognition), the rankings reversed are those of applicants whose avoided cost was largest, so recognized licensees are drawn disproportionately from states with lower requirements (A-14). Among licensed sellers in those occupations, the spread of training rises: `quality_variability` increases (C-21), with A-12's premise that training bears on quality.

*Quality received (C-22).* EN-4 in reverse gives two chains. (−) Movers who would have done the top-up now practise without it, and the inflow is weighted toward lower-requirement states (A-12, A-14). (+) As prices fall, some buyers move from doing it themselves or from unlicensed providers to licensed ones (C-23); this raises quality only if what they leave is worse (A-15, p = 0.45). Under CR-12's 0.8 clarification the (+) chain is kind (2) with its premise below the cut-off: the derived sign, a **decrease**, is reported and the (+) chain is recorded in section 10. DM-2 requires each chain's premise; here the (−) chain's premises clear the cut-off and the (+) chain's does not.

*Quantity traded (C-18, C-19).* In occupations where origin requirements are close to Halvoran's, or the training tests nothing buyers value (EN-11's Unless), only the price chain operates: more is bought (C-18, CR-4c; the exchanges the barrier prevented now take place, OC-4 in reverse). In the varied-standard occupations a second chain runs through information (C-20): buyers who learn that a Halvoran license no longer implies Halvoran training value licensed services differently, but CR-11's 0.7 clarification gives no direction for those who learn; they may buy less, search more, or move among licensed sellers. That chain's own sign is ambiguous, so CR-12's 0.8 clarification (kind 3) makes the combined sign **ambiguous** unless a dominance premise covers the price chain against both directions; the case has none (C-19).

**Self-provision, waiting and means (C-23 to C-25).** As the price falls, some buyers who did the work themselves or used unlicensed providers buy from licensed ones (C-23, A-16). In the trades with waiting lists, more licensed sellers shorten the wait (C-24, CR-6: the margin buyers were using). Buyers who keep buying the same amount pay less, the other side of incumbents' lower receipts (C-25, CR-8b); those who buy more may spend more, not less (CR-3, note).

**Employers and self-employment (C-26, C-40).** Some recognized licensees set up on their own rather than work for an employer (C-40, CR-4: x: employee, y: own practice; A-18). Employers gain from lower wages (C-14, A-10), and lose from a lower output price when recognized licensees set up on their own (C-12, A-18, p = 0.6). Both chains are derived and their premises clear the cut-off: CR-12 kind (2), **ambiguous**.

**Schools (C-27, C-31, C-37, C-38).** Top-up enrollment (about 1,900 a year) ends (C-37, CR-9 with LW-10: the top-up was an input to licensing movers, no longer required). Enrollment by Halvoran residents falls through two independent chains (C-38, CR-12d): some train in Orlesk instead (C-6, A-5), and the lower expected pay of the occupations lowers the value of training for them (A-10). Enrollment falls from the introduction, since students deciding in 2027 know the top-up will not be needed (CR-10a), and the schools' value falls when the Act becomes expected (C-27, CR-7c, CR-10c; A-19). Orlesk schools gain those students (C-31).

**Across the borders (C-28 to C-30).** Licensees from East Brasholt and Orlesk move into Halvoran (RS-4): the supply of licensed services just outside falls, prices there rise (C-28, C-29; RS-13 for withdrawn supply; A-27), and licensees who stay there face fewer competitors for the same posts, so their wages rise (C-39, CR-9, CR-7a). An opposing chain: Halvoran residents who train in Orlesk may work there during the holding year (A-21, p = 0.35); it is kind (2) below the cut-off, so the derived sign for Orlesk stands. Licensees from East Brasholt need move only a few kilometres to qualify, which adds to rental demand on the Halvoran side (C-30, A-9).

Not reported:
- *Incumbents compete by improving their service.* Suspected but not derivable: no core rule states how a seller's choice of quality responds to a lower price received with no rule fixing the price. CR-12 0.7 (kind 1): a Tier C note, not a chain.
- *Distrust of all licenses.* That buyers, learning that some licenses certify less, trust Halvoran licenses less in every occupation, including uniform-standard ones. It would need a premise that buyers do not distinguish occupations (A-23, p = 0.3).

Stopping points: C-29 and C-30 (depth 3); Orlesk's own licensing board (diffuse); landlords on the Halvoran side of Brasholt (the other side of C-30, not followed).

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `licensees.out_of_state`, `job_changes` (moves during 2027), short | New movers who can wait move early under K5 (A-3). | Movers who would have done a top-up delay into 2028 (A-4). | None | **ambiguous** (C-4). RS-8 0.8 Unless. |
| `buyers.varied_standard`, `quantity_traded`, medium | Lower price (CR-4c, A-1, A-2). | Information chain of ambiguous sign (CR-11c, A-12, A-13). | None covering both directions | **ambiguous** (C-19). CR-12 0.8, kind (3). |
| `buyers.varied_standard`, `quality_per_unit`, medium | Buyers leave self-provision and unlicensed providers (A-15, p = 0.45, below the cut-off). | No top-up; inflow weighted to lower-requirement states (A-12, A-14). | — | **decrease** (C-22). CR-12 0.8, kind (2), opposing premise below 0.5. |
| `employers.licensed_services`, `return_on_capital`, medium | Lower wages (A-10). | Lower output price from self-employed recognized licensees (A-18). | None | **ambiguous** (C-26). Kind (2). |
| `neighboring_jurisdictions` (Orlesk), `quantity_supplied`, medium | License shoppers working in Orlesk during the holding year (A-21, p = 0.35). | Orlesk licensees move to Halvoran (A-20). | — | **decrease** (C-28). Kind (2), opposing premise below 0.5. |
| All licensed sellers, `employment`, `hours_worked` (group), medium | Recognized entrants (C-2). | Incumbents who leave or cut hours (C-16). | CR-12e (the response cannot reverse its cause), with the partial-response premise CR-12 (0.9) requires (A-25) | **at_least_one_increase** (C-17). |
| `officials.enforcement`, `enforcement_cost`, short–medium | Discipline of added licensees (C-42; A-2). | Processing: recognition checks and law exams in place of equivalency reviews and top-up exams (C-41). | Arithmetic on the record's figures with a premise (A-22) | **decrease** (C-32). Each item signed separately (CR-12, 0.8, two items). |
| `officials.enforcement`, `non_tax_receipts` (fees), short–medium | Application and law-exam fees from more applications (C-43; A-2). | No top-up exam fees (C-44; A-1). | Arithmetic not decisive | **ambiguous** (C-33). Each item signed separately (CR-12, 0.8, two items). |
| `buyers.varied_standard`, `quality_information`, short–medium | — (buyers of formerly informal practitioners, C-10, are a different class) | Dilution of the license's content (A-12, A-13). | None needed | **decrease** (C-20). |
| Incumbents' associations, schools, `lobbying_effort`, medium | Lobbying to narrow the Act. | Lobbying against a reintroduced bill in the counterfactual (A-24, p = 0.6). | RS-7 Unless; Repeals (0.9) | **ambiguous** (C-11). Kind (2). |

**Kinds of opposing chain (CR-12, 0.8).** This case produced one of each: kind (1), a suspected chain no rule derives (incumbents improving quality; section 6, Tier C note); kind (2) with p at least 0.5 (C-26 and, under 0.9 with its premise stated, C-11: ambiguous) and below 0.5 (C-22, C-28, derived sign kept); kind (3), an opposing chain whose own sign is ambiguous (C-19).

### Metamorphic check against WE-024

WE-024 abolished a license for one occupation; this Act keeps every license and removes its training and exam conditions for one class of entrant. The expected relation, derived before comparing: where the effect runs through more legal sellers, the signs match WE-024's; where it runs through the license itself (its information, the share licensed, quality), they can differ, because here the license survives with changed content. The table compares the derived signs.

| Variable | WE-024 (abolition) | WE-045 (recognition) | Relation | Reason |
|---|---|---|---|---|
| `share_of_sellers_licensed` | decrease | no_change (C-34) | Differs, as derived | Abolition removes the requirement; recognition keeps it, so every legal seller is still licensed. |
| `informal_activity` | decrease | decrease (C-9) | Same, narrower class | Only out-of-state licensees waiting for a license come into the open; practitioners licensed nowhere gain nothing. |
| `number_of_sellers`, `entry_rate` | increase | increase (C-2) | Same | Different channel: relocation (RS-4), not entry at home. |
| Schools, `quantity_demanded` | decrease | decrease (C-37, C-38; value C-27) | Same | Different chains: top-up students and license shopping, not students who trained only to practise legally. |
| `price_paid` | decrease | decrease (C-12) | Same | |
| Incumbents, `net_price_received` | decrease | decrease (C-13) | Same | |
| Incumbents, `earnings` | decrease | not signed (the 0.8 version's C-15 withdrawn) | Not comparable as signed | Training is sunk in both worlds (CR-10b), so only the lower yield of the license and training is a consequence: a loss by incumbents' own ranking (CR-7, 0.9), with money earnings needing premises on hours and next-best use. WE-024's sign predates that clause. |
| `quantity_substitute` (self-provision) | decrease | decrease (C-23) | Same | |
| `quantity_traded` | increase | increase (C-18); ambiguous (C-19) | Same where the license carries no varied content; differs where it does | The information chain (kind 3) exists only where the license survives as a diluted signal. In WE-024 the training was unrelated to braiding quality (its A-10), so no such chain arose. |
| `quality_information` | increase | increase for buyers of formerly informal practitioners (C-10); decrease for buyers in varied-standard occupations (C-20) | Same for the shared channel; a second channel opposite | WE-024's increase came from hidden sellers coming into the open (RS-10); that channel is here too, for a small class. The decrease comes from the license's content changing, which abolition does not do. |
| `quality_variability` | ambiguous | increase (C-21) | Differs, as derived | In WE-024 better screening opposed untrained entrants. Here information falls and entrants are self-selected toward lower requirements, so both push the same way. |
| `quality_per_unit` | not reported | decrease (C-22) in varied-standard occupations; not reported elsewhere | Consistent given the premises | WE-024: training unrelated to quality (A-10, p = 0.85). Here: training bears on quality in those occupations (A-12, p = 0.6). The opposing chain has the same premise and probability (p = 0.45) in both. |
| `lobbying_effort` | ambiguous | ambiguous (C-11) | Same | RS-7 Unless in both. |
| `enforcement_cost` | decrease | decrease (C-32) | Same sign, different route | WE-024: enforcement against unlicensed braiding ended. Here: processing work, against the right baseline (OC-3), with arithmetic. |
| Customers' `resources_available_other_uses` | increase | increase (C-25) | Same | |
| Neighbors across the border | not reported (little relocation, its A-14) | `quantity_supplied` decrease (C-28) | Differs, as derived | Recognition is tied to residence, so it works only through relocation. |
| Incumbents shift to other licensed services | increase (its C-8) | — | Not comparable | Incumbents' licenses keep their scope. |

No sign in the comparison had to be changed after the check. (The earnings row was changed under 0.9, after the core-only comparison, not by the check.) Every difference traces to one of three features WE-024 lacks: the license survives with varied content, the benefit is tied to residence, and the entrants select themselves by origin.

## 8. Time structure

- **Introduction to the effective date (January–December 2027).** School enrollment falls from the introduction (C-27): residents choosing a school know they could train in Orlesk, and movers stop top-ups. The schools' value falls part of the way at introduction and the rest at signing (CR-7c's probability clause). Moves in 2027 are ambiguous under K5 (C-4); entry into practice in 2027 falls as movers wait for recognition (C-5). The operation itself is dated 1 January 2028 (CR-1, 0.8).
- **2028.** Pending applications convert (K5), shortening those applicants' wait (C-36), and recognized licensees enter (C-2). Prices and incumbents' receipts begin to fall (C-12, C-13); wages fall as raises are set (C-14).
- **2029 on.** The first license shoppers arrive: 1,000 hours in Orlesk (about eight months) plus a year's holding (C-6). Under U1-a, the first Orlesk certificate holders recognized because of the Act arrive at the same lag (C-8).
- **Stocks.** The number of licensees adjusts through flows of movers, entrants and leavers (CR-10b); incumbents leave mainly as the price stays lower over years (C-16). The trained stock of incumbents does not change; its returns do.
- **Expectations of reversal (TS-5).** Moves are costly to undo, so a mover's decision depends on recognition lasting. Incumbents' lobbying (C-11) keeps a narrowing possible; that slows moves but does not change their sign.
- **Erosion.** The one-year holding period and the fee are fixed; neither erodes in a way that changes a sign.

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-32 | `officials.enforcement` (boards) | `enforcement_cost` (licensing administration) | decrease | Nothing given up; staff time freed. | OC-3, CR-12e |
| C-33 | `officials.enforcement` (boards) | `non_tax_receipts` (application and exam fees) | ambiguous | — | CR-8b, CR-12b |
| C-41 | `officials.enforcement` (boards) | `enforcement_cost` (processing applications: reviews, checks, exams) | decrease | Nothing given up; staff time freed. | OC-3, CR-12e |
| C-42 | `officials.enforcement` (boards) | `enforcement_cost` (discipline of added licensees) | increase | Board time on other work. | OC-3, CR-8c |
| C-43 | `officials.enforcement` (boards) | `non_tax_receipts` (application and law-exam fees) | increase | — | CR-8b |
| C-44 | `officials.enforcement` (boards) | `non_tax_receipts` (top-up exam fees) | decrease | — | CR-8b |
| C-35 | `licensees.out_of_state` (movers) | `resources_available_other_uses` | increase | Nothing given up: the $2,800 top-up is no longer spent; it was a sum they could not avoid if they wanted to practise. | CR-3b, CR-8a |

**Administration against the right baseline (C-32).** OC-3 (0.8) compares with administration without the Act, not with zero. Without it: about 7,800 equivalency reviews at 6 hours (about 46,800 hours) and about 4,300 top-up exams at 2 hours (about 8,600 hours), about 55,000 hours a year. With it: about 1.5 hours per recognition check, plus an hour per law exam for the Schedule B share (about 15%), about 1.65 hours per application. The break-even is about 33,000 applications a year, more than four times the present 7,800. Processing alone therefore falls (C-41). Recognized licensees are subject to the same discipline as others, so discipline work rises with their number (C-42, CR-8c; A-2); CR-12's 0.8 note on two items in one variable asks for both items as consequences, with the total separately. With the premise that applications, together with any added discipline cases, stay well below that (A-22, p = 0.9), arithmetic supplies the dominance premise for the total (CR-12e) and the sign is a **decrease** (C-32). Unlike WE-044's C-47, the figures here settle it.

**Fees (C-33).** Without the Act, fees bring about $936,000 from applications and $645,000 from top-up exams, about $1.58 million. With it, about $129 per application (fee plus law exams). Application and law-exam fees rise with the number of applications (C-43, A-2); top-up exam fees, about $645,000 a year, are no longer received (C-44, A-1). The break-even for the total is about 12,250 applications; the boards project 9,500 to 14,000. Arithmetic does not settle it: **ambiguous** (C-33). Because fees are set to cover costs, and costs fall (C-32), fees per application may be cut over time; that chain is not followed.

**Movers' means (C-35).** The top-up was an outlay movers could not avoid if they wanted to practise; it is no longer made, and the schools that received it lose those receipts (C-27; CR-8b, both sides).

**Freed exchanges.** The services now bought that the barrier prevented (OC-4 in reverse) are C-18.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | The top-up binds: about 4,300 movers a year needed it, and about 650 abandoned. | binding | 0.9 | Board records, 2024–2026. | Most consequences shrink to the abandoned share. |
| A-2 | Some licensees who would not have moved, or would have abandoned, now move and practise. | mobility | 0.75 | Surveys of out-of-state licensees; abandonment records; inflows after recognition laws elsewhere. | C-2, C-3 and every price and quantity consequence weaken to the effect of skipping the top-up for those who would have moved anyway. |
| A-3 | Some new movers can wait without practising and move in 2027 to settle before the school year. | other | 0.55 | School calendars; household moves. | The (+) chain of C-4 fails; C-4 would be a decrease. |
| A-4 | Some movers who would have done a top-up in 2027 wait for recognition, and some of them delay their move into 2028. | expectations | 0.7 | The top-up's cost against months of waiting; publicity of the Act. | C-5 is not reported; the (−) chain of C-4 fails. |
| A-5 | Orlesk schools admit and Orlesk licenses non-residents in school-based occupations, and some Halvoran residents choose that route. | alternative_uses | 0.6 | Orlesk rules; tuition gap ($9,000 against $15,000); distance from southern Halvoran. | C-6 and C-31 are not reported; one chain of C-27 fails; C-38 keeps the A-10 chain. |
| A-6 | Some holders of Orlesk voluntary certificates would move if recognized. | mobility | 0.6 | Count of certificate holders; Halvoran demand for interior designers. | C-7 and C-8 are not reported. |
| A-7 | Some movers practised without a Halvoran license while waiting. | enforcement | 0.6 | Board complaints about unlicensed practice by recent movers. | C-9 and C-10 are not reported. |
| A-8 | Incumbents' associations and schools can organize at a cost below their stake. | other | 0.85 | Their lobbying on the bill. | C-11 is not reported. |
| A-9 | Some East Brasholt licensees move to the Halvoran side, and its rental market is not slack. | mobility | 0.55 | Licensee counts; vacancy in Brasholt. | C-30 is not reported. |
| A-10 | Incumbents' wages can adjust over the medium run, as raises are set. | other | 0.8 | Wage growth in these occupations. | C-14 is not reported; the (+) chain of C-26 fails; C-38 keeps the A-5 chain. |
| A-11 | Some incumbents are at the margin of leaving the occupation or cutting hours. | alternative_uses | 0.6 | Exit rates; part-time shares. | C-16 is not reported. |
| A-12 | In the varied-standard occupations, buyers treated a Halvoran license as a sign of Halvoran training, and that training bears on quality they value and cannot judge. | other | 0.6 | Buyer surveys; curricula by topic; complaint and discipline rates by training level. | C-19 becomes an increase; C-20 to C-22 are not reported. |
| A-13 | The inflow includes licensees trained to lower requirements, and most buyers do not check the registry for the origin state. | other | 0.55 | Origin of past applicants; registry search counts. | C-20 is not reported; C-19 becomes an increase. |
| A-14 | Applicants from lower-requirement states make up a larger share of recognized licensees than of the endorsement applicants before. | other | 0.7 | Avoided top-up by origin; the 4,300 who needed it came mostly from such states. | C-21 and C-22 are not reported. |
| A-15 | What buyers leave when they move to licensed providers (doing it themselves, unlicensed providers) is of lower quality than licensed provision. | other | 0.45 | Self-provision is used mostly for simple work; unlicensed providers are often trained. | Below the cut-off: the (+) chain of C-22 is recorded here, not reported. If above, C-22 becomes ambiguous. |
| A-16 | Some buyers do the work themselves or use unlicensed providers because licensed services cost too much. | substitutability | 0.75 | Household surveys; unlicensed electrical and cosmetology work. | C-23 is not reported. |
| A-17 | Waiting lists in electrical and HVAC work reflect a shortage of licensed workers. | other | 0.6 | Contractors' reports of three to six weeks. | C-24 is not reported. |
| A-18 | Some recognized licensees set up on their own and compete with employers. | other | 0.6 | Self-employment shares in these occupations. | The (−) chain of C-26 fails; C-26 becomes an increase; C-40 is not reported. |
| A-19 | Schools' values rest on expected enrollment, and passage was likely from the introduction. | expectations | 0.7 | Sale prices of schools; legislative support on record. | C-27 moves to signing or is not reported. |
| A-20 | Licensees near the borders are at the margin of moving into Halvoran. | mobility | 0.65 | 4,000 covered licensees in East Brasholt; Orlesk wage gaps. | C-28, C-29 and C-39 are not reported. |
| A-21 | Halvoran residents who train in Orlesk work there during the holding year. | other | 0.35 | Commuting distances from southern Halvoran. | Below the cut-off: the (+) chain of C-28 is recorded here, not reported. If above, C-28 becomes ambiguous. |
| A-22 | Applications and added discipline cases stay well below four times the present level. | other | 0.9 | The boards' projection (9,500 to 14,000 applications). | C-41 is not signed; C-32 becomes ambiguous. |
| A-23 | Buyers do not distinguish between occupations when they learn that some recognized licenses certify less. | other | 0.3 | None. | Below the cut-off; not reported. |
| A-24 | Without the Act, recognition would have stayed contested: a bill reintroduced and lobbied against by incumbents' associations and schools. | other | 0.6 | The bill's support (the governor, majorities on record); recognition bills in other states reintroduced after defeat. | C-11 becomes an increase (no contest on the counterfactual path). |
| A-25 | Incumbents leave or cut hours too slowly to offset the entry in the medium run (their training is sunk and specific). | durability | 0.8 | Exit rates in these occupations; the size of the inflow against incumbents' numbers. | C-17 holds only as "not below the counterfactual" (CR-12e), not as an increase. |
| A-26 | Some practitioners in non-licensing states can meet the Orlesk certificate's exam and experience conditions. | other | 0.6 | The certificate's conditions; practitioners' experience. | C-8 is not reported. |
| A-27 | Demand for licensed services and licensed labor, in Halvoran and near its borders, is not perfectly elastic: a change in licensed supply is not absorbed at an unchanged price or wage. | substitutability | 0.85 | Local service markets; waiting lists (A-17). | C-12 to C-14, C-29 and C-39 hold only as a group with quantity (CR-6, 0.9). |

## 11. Report

**The policy.** From 1 January 2028, Halvoran licenses anyone who has held a license in another state for at least a year and moves to Halvoran, in 40 occupations, without further training or exams. In seven occupations with state-specific law, they must pass a two-hour law exam. The license looks the same as any other; the online registry shows where it came from. Applications pending at the start may be decided under the new rules. Whether a voluntary state certificate counts as a license is unclear.

**Visible consequences.** Licensees moving to Halvoran no longer spend months and about $2,800 on added training and exams (C-1), and more of them practise there (C-2).

**Invisible consequences.**
- *Movers.* Licensees elsewhere move to Halvoran more often (C-3) and keep the money the top-up would have cost (C-35); those with applications pending at the start get their license sooner (C-36), and some set up on their own (C-40). Some who were practising informally while waiting come into the open (C-9), which helps their customers judge them (C-10).
- *Buyers.* Prices of licensed services fall (C-12); buyers who keep buying the same amount have more left for other things (C-25); fewer do the work themselves or use unlicensed providers (C-23); waits for electricians and HVAC shorten (C-24). Where the license tests little that buyers value, or training is similar across states, they buy more (C-18).
- *The license as a signal.* In occupations where training matters and differs a lot between states, a Halvoran license now tells buyers less (C-20), the spread of training among licensed sellers widens (C-21), because licensees from states with the lowest requirements gain most from recognition and come in the largest numbers, and the quality buyers receive falls (C-22).
- *Incumbents.* They receive less (C-13) and their wages grow less (C-14); some leave or work fewer hours (C-16), though total licensed labor in the occupations, in heads or hours, rises (C-17). Their training is sunk in both worlds; the loss is the lower stream of returns from their license and training, a loss by their own ranking borne by those who held or were training for a license when the Act became expected (no variable records it; whether their money earnings fall is not signed).
- *Schools.* Halvoran schools lose top-up students (C-37) and resident students (C-38), some of them to Orlesk (C-6, C-31), and lose value (C-27).
- *Across the borders.* Licensed services become scarcer and dearer just outside Halvoran (C-28, C-29), and licensees who stay there earn higher wages (C-39); rents rise a little on the Halvoran side of Brasholt (C-30).
- *Timing.* Entry into practice dips in 2027 as movers wait for recognition (C-5).
- *Administration.* Boards spend less staff time in total (C-32): less on processing applications (C-41), more on disciplining added licensees (C-42). They receive more application and law-exam fees (C-43) and no top-up exam fees (C-44).

**Ambiguous effects.** Moves during 2027 (C-4): some wait for recognition, others move early under the pending-application clause. How much is bought in occupations where the license's content now varies (C-19): lower prices against a less informative license whose effect on demand has no derivable direction. Employers' returns (C-26): lower wages against new self-employed competitors. Boards' fee receipts in total (C-33). Lobbying by incumbents and schools (C-11), given that recognition would likely have stayed contested without the Act (A-24).

**Per reading of U1.** If voluntary certificates count, Orlesk certificate holders enter (C-7) and more people seek the certificate (C-8); if not, nothing changes for them.

**Key conditions.** That the top-up deterred movers (A-1, p = 0.9; A-2, p = 0.75) drives every price and quantity result. The signal and quality results rest on training bearing on quality in the varied-standard occupations (A-12, p = 0.6) and on the inflow including licensees trained to lower requirements whom buyers do not check (A-13, p = 0.55).

**What this analysis cannot say.** How many will move, how far prices fall, or how much quality changes; health and safety effects of practitioners' competence (out of scope for version 1); whether gains to movers and buyers outweigh losses to incumbents, schools and buyers who valued the old signal; whether the Act is desirable.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions | Persistence |
|---|---|---|---|---|---|---|---|---|---|
| C-1 | licensees.out_of_state (movers) | compliance_cost (top-up training, exams) | decrease | short | visible | B | CR-1, CR-3b, OC-2 | A-1 | none |
| C-2 | licensees.out_of_state | entry_rate (practice in Halvoran) | increase | short–medium | visible | B | EN-1 (in reverse), RS-4, CR-4 | A-1, A-2 | partial (the stock of movers who went elsewhere earlier does not return) |
| C-3 | licensees.out_of_state | job_changes (moves into Halvoran) | increase | medium | invisible | B | CR-7, RS-11 (in reverse), CR-4 | A-2 | none |
| C-4 | licensees.out_of_state | job_changes (moves during 2027) | ambiguous | short | invisible | B | RS-8, CR-10a, CR-12b | A-3, A-4 | n/a (transition) |
| C-5 | licensees.out_of_state | entry_rate (practice during 2027) | decrease | short | invisible | B | RS-8, CR-10a | A-4 | n/a (transition) |
| C-6 | students.halvoran | cross_border_purchases (training in Orlesk) | increase | medium | invisible | B | RS-4, RS-5, CR-4 | A-5 | n/a (no counterpart) |
| C-7 | licensees.voluntary_cert | entry_rate (into Halvoran) | U1-a: increase; U1-b: no_change | short–medium | invisible | B | CR-1, CR-4 | A-6 | none |
| C-8 | practitioners in non-licensing states | quantity_demanded (Orlesk voluntary certificates) | U1-a: increase; U1-b: no_change | medium | invisible | B | CR-4, CR-10a | A-6, A-26 | n/a (no counterpart) |
| C-9 | licensees.out_of_state (practising while waiting) | informal_activity | decrease | short | invisible | B | RS-3 (in reverse), CR-1 | A-7 | none |
| C-10 | buyers of those practitioners | quality_information | increase | short | invisible | B | RS-10 (reverse clause) | A-7 | none |
| C-11 | incumbents' associations, schools.halvoran | lobbying_effort | ambiguous | medium | invisible | B | RS-7, CR-4, EN-5, CR-12b | A-8, A-24 | n/a |
| C-12 | buyers.licensed_services | price_paid | decrease | medium | invisible | B | EN-1 (in reverse), CR-6 | A-1, A-2, A-27 | partial (medium); none (long) |
| C-13 | licensees.incumbent (self-employed) | net_price_received | decrease | medium | invisible | B | EN-2 (in reverse), CR-6, CR-7b | A-1, A-2, A-27 | none |
| C-14 | licensees.incumbent (employed) | wage_rate | decrease | medium | invisible | B | CR-6, CR-7b | A-1, A-2, A-10, A-27 | none |
| C-16 | licensees.incumbent | employment, hours_worked | at_least_one_decrease | medium–long | invisible | B | RS-6, CR-4 | A-1, A-2, A-11 | n/a |
| C-17 | all licensed sellers in Halvoran | employment, hours_worked (total in covered occupations) | at_least_one_increase | medium | invisible | B | CR-4, CR-12e | A-1, A-2, A-25 | partial |
| C-18 | buyers.uniform_standard | quantity_traded | increase | medium | invisible | B | CR-4c, OC-4 (in reverse) | A-1, A-2 | none |
| C-19 | buyers.varied_standard | quantity_traded | ambiguous | medium | invisible | B | CR-4c, CR-11c, CR-12b | A-1, A-2, A-12, A-13 | n/a |
| C-20 | buyers.varied_standard | quality_information | decrease | short–medium | invisible | B | CR-11c, EN-11 | A-12, A-13 | partial (beliefs adjust as buyers learn; no long-run sign) |
| C-21 | buyers.varied_standard | quality_variability (among licensed sellers) | increase | medium | invisible | B | CR-4, CR-11c | A-12, A-14 | n/a (no counterpart) |
| C-22 | buyers.varied_standard | quality_per_unit | decrease | medium | invisible | B | EN-4 (in reverse), CR-4, CR-12b | A-12, A-14 | n/a (no counterpart) |
| C-23 | buyers.licensed_services | quantity_substitute (self-provision, unlicensed providers) | decrease | medium | invisible | B | EN-3 (in reverse), RS-1 | A-1, A-2, A-16 | none |
| C-24 | buyers.licensed_services (electrical, HVAC) | wait_time | decrease | short–medium | invisible | B | CR-6, EN-1 (in reverse) | A-17 | none |
| C-25 | buyers.licensed_services (who keep buying the same amount) | resources_available_other_uses | increase | medium | invisible | B | CR-8b, CR-3b | A-1, A-2 | partial (medium); none (long) |
| C-26 | employers.licensed_services | return_on_capital | ambiguous | medium | invisible | B | CR-7b, CR-12b | A-10, A-18 | n/a |
| C-27 | schools.halvoran (owners) | asset_value | decrease | short | invisible | B | CR-7c, CR-10c | A-1, A-5, A-19 | full for losses already capitalized |
| C-28 | neighboring_jurisdictions (sellers near the borders) | quantity_supplied (licensed services) | decrease | medium | invisible | B | RS-4, CR-12b | A-2, A-20 | n/a (no counterpart) |
| C-29 | neighboring_jurisdictions (buyers near the borders) | price_paid (licensed services) | increase | medium | invisible | B | RS-13, CR-6 | A-2, A-20, A-27 | n/a (no counterpart) |
| C-30 | tenants.brasholt | price_paid (rent, Halvoran side) | increase | medium | invisible | B | CR-9, RS-4 | A-9 | n/a (no counterpart) |
| C-31 | schools.orlesk | quantity_traded (enrollment) | increase | medium | invisible | B | CR-9, RS-4 | A-5 | n/a (no counterpart) |
| C-32 | officials.enforcement (boards) | enforcement_cost (licensing administration) | decrease | short–medium | invisible | B | OC-3, CR-12e | A-22 | none |
| C-33 | officials.enforcement (boards) | non_tax_receipts (fees) | ambiguous | short–medium | invisible | B | CR-8b, CR-12b | A-2, A-22 | n/a |
| C-34 | legal sellers in covered occupations | share_of_sellers_licensed | no_change | short | invisible | A | CR-1 | none | n/a |
| C-35 | licensees.out_of_state (movers) | resources_available_other_uses | increase | short | invisible | B | CR-3b, CR-8a | A-1 | none |
| C-36 | licensees.out_of_state (pending on 1 January 2028) | wait_time (to a Halvoran license) | decrease | short | invisible | B | CR-1, CR-3b | A-1 | n/a (transition) |
| C-37 | schools.halvoran | enrollment (top-up enrollments) | decrease | short–medium | invisible | B | CR-9, LW-10 | A-1 | none |
| C-38 | schools.halvoran | enrollment (Halvoran residents) | decrease | short–medium | invisible | B | CR-9, LW-10, CR-12d | A-5 or A-10 (independent chains) | n/a (no counterpart) |
| C-39 | neighboring_jurisdictions (licensees who stay near the borders) | wage_rate | increase | medium | invisible | B | CR-9, CR-7a, CR-6 | A-2, A-20, A-27 | n/a (no counterpart) |
| C-40 | licensees.out_of_state (recognized) | entry_rate (self-employed practices) | increase | medium | invisible | B | CR-4 | A-2, A-18 | none |
| C-41 | officials.enforcement (boards) | enforcement_cost (processing applications) | decrease | short–medium | invisible | B | OC-3, CR-12e | A-22 | none |
| C-42 | officials.enforcement (boards) | enforcement_cost (discipline of added licensees) | increase | medium | invisible | B | OC-3, CR-8c | A-2 | n/a (no counterpart) |
| C-43 | officials.enforcement (boards) | non_tax_receipts (application and law-exam fees) | increase | short–medium | invisible | B | CR-8b | A-2 | n/a |
| C-44 | officials.enforcement (boards) | non_tax_receipts (top-up exam fees) | decrease | short | invisible | B | CR-8b | A-1 | none |

C-34 is recorded because the derivation establishes it: the requirement that every legal seller hold a Halvoran license is unchanged, and K3 makes a recognized license a Halvoran license. It is the clearest place where recognition and abolition (WE-024, C-1) differ.

## Corrections after the core-only comparison

The core-only re-run (`05_examples_core/WE-045_universal_license_recognition_core.md`) was compared with this analysis. Each correction below was checked against the core rules before it was applied; the catalog is now 0.9.

**Changed.**
- C-11: sign kept (`ambiguous`), but now on a stated premise (A-24, p = 0.6) that recognition would have stayed contested without the Act. RS-7's 0.9 clause on repeals and CR-4's 0.9 clause make that a premise, not a given; the 0.8 version assumed it.
- C-17: `employment` `increase` → `employment`, `hours_worked` `at_least_one_increase`. CR-12e binds total licensed supply, not heads; and under CR-12's 0.9 clause on what the response argument gives, a strict increase needs the partial-response premise A-25.
- C-25: qualifier narrowed to buyers who keep buying the same amount (CR-3, note: those who buy more may spend more).
- C-8: premise A-26 added (non-holders can meet the certificate's conditions).
- C-12, C-13, C-14, C-29: premise A-27 added (demand not perfectly elastic), which CR-6's 0.9 clause on splitting a shift requires before a price or wage is signed alone.
- C-20: EN-11's 0.9 Unless clause now gives the sign directly; `persistence` changed from "n/a" to "partial" under CR-11's 0.9 clause on a signal that becomes noisier.
- C-32, C-33: sign and premises unchanged; their items are now recorded separately (C-41 to C-44).

**Added.** C-36 (pending applicants' wait, decrease), C-37 (top-up enrollments, decrease), C-38 (residents' enrollments, decrease, two independent chains), C-39 (wages of licensees who stay near the borders, increase), C-40 (self-employed practices of recognized licensees, increase), C-41 (processing time, decrease), C-42 (discipline of added licensees, increase), C-43 (application and law-exam fees, increase), C-44 (top-up exam fees, decrease). New assumptions A-24 to A-27.

**Removed.** C-15 (incumbents' money `earnings`, decrease). It netted a lower wage and a lower price (CR-12c) without premises on hours (CR-4's exception) or on leavers' next-best occupation. Under CR-7's 0.9 clause on assets without a market price, what is derivable is a loss by incumbents' own ranking, which has no variable in 2.4. It is stated in section 6 and the report. The ID is retired, not reused.

**Comparison conclusions rejected or not applied.**
- C-32 (A-22 does not bound discipline hours, cause A): not changed. CR-12's 0.9 clauses do not settle what the premise must bound, so the total keeps its sign on A-22 as worded. The discipline item is now recorded separately (C-42).
- C-19 (kind 1 or kind 3 for the information chain, cause J): not changed. CR-12's 0.9 note on kind (3) covers a chain whose parts push in opposite directions. It does not settle whether a chain with no derivable direction is such a chain.
- Core C-16 (law exam for Schedule B applicants endorsed directly, cause A): not added. It rests on a premise at p = 0.5 about the old law, and 0.9 does not settle it.
- Core C-4 and C-43 (cause J): not added. 0.9 does not change the choice of class or the split by reading.

## Gaps found

**(a) Calculus gaps (a step no core rule covers).** None. Every step was derived from CR-1 to CR-12 or from a pattern whose preconditions held, read in reverse where the text says so.

**(b) Unclear core rules, including the 0.7 and 0.8 clarifications.**
1. *CR-7c for a non-tradable license.* CR-7c is stated for "the price of a durable asset". A Halvoran license cannot be sold, so it has no price, yet the conclusion the brief expects (the loss is borne by holders, and by those committed to training, when the Act becomes expected) is plainly right. The analysis reached it through CR-7b and CR-10c (then C-15) and kept CR-7c for priced assets (schools, C-27). CR-7c could say that for a non-tradable asset the same capitalization falls on the holder's expected yield, with no market price to observe. (Settled in 0.9: CR-7's clause on assets without a market price says this, and that a change in money earnings needs a premise; C-15 was withdrawn.)
2. *CR-11's 0.7 "what a sign needs" for a pooled signal.* The two premises (prior belief; direction of those who learn) were enough to sign `quality_information` (C-20), but not the demand response, since the clarification gives no direction for those who learn that a signal has become noisier. That turned C-19 into a kind (3) chain. The rule worked as written; it may be stricter than intended for a chain whose direction is open and whose size the method cannot weigh.
3. *The line between CR-12's kinds (1) and (2).* "Incumbents compete by raising quality" was classed as kind (1) (no rule derives it). One could argue it is kind (2): CR-4 with a premise about sellers' quality choices. The 0.8 text does not say whether a chain that needs a premise about how a seller chooses quality, with no rule fixing the price, is "derived".
4. *CR-12e's response argument (0.8).* Worked as written for total employment (C-17). It is the clause that keeps C-16 (incumbents leave) from making C-17 ambiguous.

**(c) Missing or wrong patterns.**
1. *EN-11 when the license's content varies by issuer.* EN-11 is written for licensed against unlicensed sellers. Applied as written to recognized licensees it would sign `quality_information` up for their buyers (they are now licensed), which is wrong for buyers who read the license as a sign of Halvoran training: the signal is now a mixture. The pattern's preconditions were met (the license tests something buyers care about and is visible), but its conclusion does not hold for the pooled case. The sign was derived from CR-11c instead (C-20). (Adopted in 0.9 as EN-11's Unless clause.) Proposed clause: "Where the same license is issued on different requirements (recognition, grandfathering, alternative routes) and buyers cannot see which, the license conveys less: `quality_information` decreases for buyers who relied on it, and `quality_variability` among license holders increases, with a premise that the requirements bear on quality."
2. *EN-1 to EN-4 "in reverse" for a partial repeal.* The catalog's reverse clauses (RS-10, RS-7) are written for full repeal. For a removal that applies to one class of entrant and keeps the license, EN-1 and EN-2 reversed as expected, EN-3 and EN-4 needed the class split, and EN-11 failed (c1). A note in the EN family that partial repeals keep the license as a signal would prompt C-20 to C-22.
3. *Selection under a uniform term* (candidate, 06_gaps.md 6.2e, from WE-029). Relevant, but as a mirror case: in WE-029 the side that provides a uniform term (the employer) screens counterparties whose cost to it differs; here the side that takes a uniform term (the applicant) selects itself, because the term's value differs by origin (C-21). The derivation is CR-4 per counterparty in both. It counts as a second use only if the pattern is written to cover both self-selection by takers and screening by providers; as recorded in 6.2e it covers the second.
4. *RS-4 in the inside-favoring direction.* Worked as written: `entry_rate` up inside, `quantity_supplied` down just outside (C-2, C-28). It does not mention residence conditions, which here make relocation the only channel.

**(d) Vocabulary the ontology lacks.**
1. *Composition of an inflow.* No variable for the make-up of a group of entrants (share from lower-requirement states). C-21 records its consequence for buyers (`quality_variability`); the selection itself has no variable.
2. *Moving home.* `job_changes` covers "moves that require changing home"; a move of residence to qualify for a license, with the same job, fits it only loosely (C-3, C-4).
3. *Training as an asset.* No variable for the value of a non-tradable license or of training in progress. The 0.8 version let `earnings` carry it (C-15, withdrawn under 0.9); it is now stated without a variable (section 6), see b1.

**(e) Test of 0.8.**
- *CR-12 0.8, three kinds of opposing chain.* Worked as written for all three kinds, one of each (section 7): kind (1) a Tier C note; kind (2) ambiguous at p ≥ 0.5 (C-26) and the derived sign kept at p < 0.5 (C-22, C-28); kind (3) ambiguous (C-19). Needed interpretation only at the line between kinds (1) and (2) (b3).
- *CR-12e 0.8, the response argument binds the response as a whole.* Worked (C-17).
- *OC-3 0.8, right baseline.* Worked as written, and here the record's figures supplied a dominance premise (C-32, break-even at more than four times current applications); for fees they did not (C-33). The contrast with WE-044 C-47 shows the clause's arithmetic route doing its job in both directions.
- *RS-8 0.8, opposing timing chains (Unless, pending cases).* Worked as written: K5 is the pending-case clause the Unless describes; moves in 2027 are ambiguous (C-4) while entry in 2027 is a decrease (C-5).
- *CR-1 0.8, dated operations.* Worked: the operation is dated 1 January 2028, while schools' values and enrollment move from the introduction (C-27).
- *CR-7 0.7, a policy that makes a means mobile.* Worked: the gain from mobility goes to the licensee (C-3, C-35).
- *EN-11 (0.6) for a license whose content varies by issuer.* Failed as written: preconditions met, conclusion wrong for the pooled case (c1); derived from CR-11c instead.
- *RS-4 0.7, widened.* Worked in the inside-favoring direction (C-2, C-28).
- *RS-7 Unless (0.5).* Worked (C-11).
- *CR-6 0.8, a free price's rise is enough.* Not exercised as a rise; the mirror (a fall in a free price, C-12) needed no clause.
- *Candidate patterns.* "Selection under a uniform term": relevant as a mirror case (self-selection by takers, C-21); a second use only if the pattern is written to cover both sides (c3). "Complaint-only enforcement": not exercised.
- Re-run note: the comparison contradicted two "Worked" verdicts. RS-7 Unless (C-11) was applied without a premise that the counterfactual was contested (now A-24). CR-12e (C-17) bound total supply, not heads, and gave a strict increase without a partial-response premise (now the group with A-25).
