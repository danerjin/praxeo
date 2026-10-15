# WE-016 License requirement for interior designers, with grandfathering

Analyst: draft (Handbook 0.2)  |  Rule catalog version: 0.2  |  Status: awaiting expert review

A stylized policy in a fictional state, modeled on a common type of occupational-licensing law. It is a companion to WE-003: here existing practitioners are grandfathered, which changes the time structure, and the required training is partly related to the quality some buyers care about, which changes the quality result. The probabilities are illustrative; the evidence column says what a real analysis would cite.

## 1. Policy record

**Arden Interior Design Practice Act.** Interior design was previously unregulated in the State of Arden: anyone could offer it for pay. About 6,000 people do, roughly 40% of whom hold a degree in interior design. About half the trade's revenue comes from commercial work (offices, shops, restaurants), half from homes. Two accredited degree programs in Arden graduate about 300 students a year. Arden's largest city, Corvan, is 20 km from the border with Belmar, which does not license interior designers. The Act was passed ten months before it took effect.

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 License requirement | `licensing_requirement` | Interior design for pay: space planning, and selection of interior finishes and furnishings, for homes or businesses in Arden | Anyone offering it, and firms employing them | A four-year accredited degree in interior design; 3,500 hours of work supervised by a licensed designer or architect; a state exam ($1,200). License fee $250 a year; 12 hours of continuing education a year. | K2; architects; retail employees advising on goods sold by their employer; work on one's own home; unpaid work |
| K2 Grandfathering | Exemption from K1's entry conditions | Existing practitioners | — | Anyone who documents three years of paid practice in Arden before the effective date and registers within 18 months receives a license without the degree, hours or exam. The license lapses if not renewed, and cannot then be regained without meeting K1. | — |
| K3 Stamped plans | Part of K1 | Building permits for commercial interior alterations | Permit applicants | Plans must be stamped by a licensed interior designer or an architect. Previously, non-structural interior plans by anyone were accepted. | Homes |
| K4 Enforcement | Enforcement | K1 to K3 | State Board of Interior Design | Complaint-driven; fines up to $2,500 per violation; contracts for unlicensed practice cannot be enforced in court. Funded by license fees and the general budget. | None |

Unclear provisions: whether choosing furnishings, finishes and colors without any space planning ("styling") is covered. The definition lists "selection of interior finishes and furnishings", so it is assumed covered.

## 2. Classification

| Component | Rothbard type | Binding? | Rule families |
|---|---|---|---|
| K1 | Triangular: prohibits exchanges between clients and unlicensed designers; a grant of privilege to license holders | Yes, for the roughly 60% without a degree who are not grandfathered, and for most would-be entrants (A-1) | EN, RS, OC |
| K2 | Exemption: a boundary in time | Delays the effect on supply (EN-1, Unless clause) | EN-1, TS-1, RS-8 |
| K3 | Triangular: commercial clients may not use unlicensed plans for permits | Yes (A-5) | EN-1, EN-4 |
| K4 | Binary: funded by fees and taxpayers | Yes | OC-3 |

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `designers.grandfathered` | Practitioners with three years' paid practice who register | Keep working, with fees and continuing education; face less new competition. |
| `designers.recent` | Practitioners with less than three years' practice and no degree | Must earn a degree and 3,500 hours, stop, or work without a license. |
| `designers.prospective` (`sellers.prospective`) | People who would have entered the trade | Entry now takes a degree, supervised hours and an exam. |
| `apprentices` | Graduates working toward the 3,500 supervised hours | Need a licensed supervisor. |
| `clients.commercial` | Businesses buying interior design | Must use licensed designers or architects for permit work; fewer providers over time. |
| `clients.residential` | Households buying interior design | Fewer licensed providers over time; exempt and informal options remain. |
| `retailers.furniture` (`sellers.substitutes`) | Furniture and home stores offering design help | Their staff are exempt when advising on goods the store sells. |
| `showrooms.trade` (`sellers.complements`) | Showrooms and suppliers selling mainly through independent designers | Their channel shrinks. |
| `architects` (`sellers.substitutes`) | Licensed architects | Exempt; can take commercial interior work. |
| `schools.design` (`input_suppliers`) | Accredited degree programs | New demand. |
| `officials.enforcement`, `taxpayers` | Board and its funders | New administrative task. |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | designers (legal market) | `share_of_sellers_licensed` | increase | short | K1, K2 | A-2 |

The visible, stated aim: everyone who offers interior design for pay in Arden is licensed. For the first years most license holders are grandfathered practitioners whose training has not changed, so the license certifies little that is new about them. Whether quality received rises is the question in section 7.

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-2 | `designers.recent` | `number_of_sellers` (legal) | decrease | short | EN-1 | A-1, A-2 |
| C-3 | `designers.recent` | `informal_activity` | increase | short | RS-3, EN-3 | A-3 |
| C-4 | `designers.grandfathered` | `compliance_cost` (documenting practice, fees, continuing education) | increase | short | OC-2 | none |
| C-5 | `designers.prospective` | `entry_rate` | decrease | medium to long | EN-1, TS-1 | A-1, A-2 |
| C-6 | `designers.prospective` (degree route) | `compliance_cost` (degree and 3,500 supervised hours, beyond what many residential clients would ask for) | increase | long | OC-2, EN-1 | A-1, A-6 |
| C-7 | `schools.design` | `quantity_demanded` (degree places) | increase | medium | EN-1 | A-1 |
| C-8 | `retailers.furniture`, `designers.recent` | `reclassification` (full-room design offered as "free design help" with furniture sales; recent designers joining stores as employees) | increase | short to medium | RS-5 | A-7 |
| C-9 | `clients.commercial` | `quantity_traded` (commercial interior projects permitted in the announcement window) | increase | short | RS-8 | A-8 |
| C-10 | `designers.grandfathered`, `schools.design`, `retailers.furniture`, `architects` | `lobbying_effort` (license holders and schools to widen the scope and keep the rule; retailers to keep their exemption; architects over the boundary of their work) | increase | medium to long | RS-7, EN-5 | A-9 |

C-2 and C-5 are EN-1 with its grandfathering exception. In the short run only the recent, non-degreed practitioners are excluded; the restriction on new entry shows up later (section 8).

Not reported: Belmar-based designers serving Arden homes without an Arden license (RS-4). Corvan is close to the border, but Arden projects need an Arden license whoever does them; A-17 is below the cut-off (p = 0.4).

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-11 | `clients.residential` | `price_paid` (licensed design) | increase | medium to long | EN-1, TS-1 | | A-1, A-2, A-4 |
| C-12 | `clients.commercial` | `price_paid` (licensed design) | increase | medium to long | EN-1, TS-1 | | A-1, A-4, A-5 |
| C-13 | `designers.grandfathered` | `net_price_received` | increase | medium | EN-2 | | A-1, A-2, A-4 |
| C-14 | `clients.residential` | `quantity_substitute` (retail design help, online services, doing it themselves) | increase | medium | EN-3, RS-1 | licensed design and retail design help: `substitute`, partial | A-7, A-10 |
| C-15 | `clients.commercial` | `quantity_substitute` (architect-led interiors) | increase | medium | RS-1 | interior designers and architects: `substitute`, close for commercial work | A-11 |
| C-16 | `retailers.furniture` | `quantity_traded` (furniture) | increase | medium | RS-5, RS-9 | design help and furniture bought in the same store: `complement`, note `trip` | A-7, A-12 |
| C-17 | `showrooms.trade` | `quantity_traded` | decrease | medium | RS-5, RS-9 | as C-16 | A-7, A-12 |
| C-18 | `clients.residential` (using unlicensed designers) | `search_cost` | increase | short to medium | RS-10 | | A-3 |
| C-19 | `clients.commercial` | `quality_per_unit` | increase | long | EN-4, DM-2 | | A-5, A-13 |
| C-20 | `clients.residential` | `quality_per_unit` | ambiguous | medium to long | EN-4 | | A-10, A-14 |
| C-21 | `apprentices` | `wage_rate` | decrease | medium | GAP-016-1 | | A-15 |
| C-22 | `designers.grandfathered` | `job_changes` (leaving the occupation for a time) | decrease | medium | GAP-016-2 | | A-16 |

C-16, C-17: a household that takes a store's free design help buys most of the furnishings from that store. Purchases that independent designers would have placed with trade showrooms move to the stores (RS-9).

C-18: RS-10 applies to the informal practice in C-3. Unlicensed designers cannot advertise as designers, clients cannot check them, and since their contracts cannot be enforced in court, fee disputes are settled privately or not at all.

C-21 (Tier C): the 3,500 hours must be supervised by a licensed designer or architect. Supervised positions are scarce relative to graduates in the medium horizon, so graduates accept lower pay to get them. No rule covers supervised-experience requirements (GAP-016-1).

C-22 (Tier C): a grandfathered license lost by lapsing cannot be regained without the degree. Designers who would have left the trade for a few years (to raise children, to try other work) now keep renewing and working instead. This is the lock-in of RS-11, but tied to an occupation, not a place, so RS-11's precondition is not met (GAP-016-2).

Stopping points: lower sales at trade showrooms (C-17) would reach their suppliers at depth 4, a diffuse group; stopped. RS-11 in its own terms (a location-tied benefit) does not apply: the license is valid anywhere in Arden.

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `clients.commercial`, `quality_per_unit`, long | New entrants are trained and examined in building codes, egress, accessibility and plan preparation, which commercial clients need to get permits approved (EN-4, up chain; A-13, p = 0.75). | Higher prices (C-12) push some clients toward cheaper options (EN-3, down chain). | DM-2: stamped plans are required for permits (A-5, p = 0.85), so no close unlicensed substitute exists for permit work, and architects, the exempt alternative, are themselves licensed. The down chain is weak. | **increase** (C-19), mostly in the long run, once new entrants are a large share of the trade. In the short run the licensed pool is the grandfathered pool, and quality is close to unchanged. If the curriculum did not cover what commercial clients need (A-13 false), the sign would be **ambiguous**. |
| `clients.residential`, `quality_per_unit`, medium to long | New entrants know space planning and materials; some of this matters to homeowners (EN-4, up chain). | Higher prices (C-11) push clients toward store design help, online services and doing it themselves (C-14), and toward unlicensed designers they cannot check (C-18) (EN-3, down chain; A-10, p = 0.85). | DM-2 does not settle it. The down chain is active, because close exempt and unlicensed substitutes exist (A-10). Whether the up chain is weak depends on whether the training is unrelated to what residential clients value (taste, coordination, responsiveness). The evidence is mixed: A-14 (largely unrelated) is put at p = 0.45, below the cut-off, and its negation is not established either. | **ambiguous** (C-20). If evidence raised A-14 above 0.5 (for example, client ratings showing no difference between degreed and non-degreed residential designers), DM-2 would make the sign **decrease**, as in WE-003. If evidence showed degreed designers clearly better at what homeowners value, the sign would stay ambiguous, because the down chain remains. |
| `designers.prospective` who take the degree route, `earnings`, long | Higher fees once licensed (C-11, C-12). | A degree and 3,500 supervised hours at low pay first (C-6, C-21). | DM-3 | **ambiguous** by design (C-23). Those who choose the route expect it to pay (LW-5); those who turn away expected it not to. |
| `designers.grandfathered`, `earnings`, medium | Higher fees as competition thins (C-13). | Fees and continuing-education hours every year (C-4). | None | **ambiguous** (C-24). The method cannot compare the two. That nearly all eligible practitioners register shows they expected registration to be worth its cost; it does not compare their earnings with the counterfactual. |

## 8. Time structure

Grandfathering (K2) turns EN-1's supply effect into a slow, growing one. The trade's skills are a durable stock that wears out as people leave, and the license now limits what replaces them (TS-1).

- **Announcement window (ten months).** Commercial clients bring alterations forward to file permits before stamped plans are required (C-9). Students who were undecided enroll in degree programs (C-7 starts).
- **Short run (first 18 months).** Grandfathered practitioners register (C-4); recent practitioners without a degree leave, join stores, or carry on informally (C-2, C-3, C-8). Apart from them, supply is nearly unchanged, so prices move little and quality is unchanged: the licensed pool is the old pool.
- **Medium run (years 2 to 6): the tightest period.** Grandfathered designers leave at about 3 to 5% a year (A-4). New entrants arrive only after a degree and 3,500 hours, about two years after graduation; someone who starts a degree on the effective date is licensed around year 6. Supply falls fastest relative to the counterfactual here, and prices (C-11, C-12), grandfathered designers' fees (C-13), and the shortage of supervised places (C-21) are greatest. Lock-in (C-22) matters most while the grandfathered are still a large share.
- **Long run (beyond year 6).** The pipeline flows, and degree programs expand (C-7). Supply settles below the counterfactual, since entry costs more (C-5). New entrants become a growing share of the trade, so the quality effects in section 7 appear mostly now. Non-degreed practitioners disappear from the legal market over about a working lifetime.
- **Expectations.** If students expect the scope to be widened or the rule relaxed (C-10), enrollment decisions are delayed or brought forward accordingly (TS-2).

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-25 | `clients.residential`, `clients.commercial`, `designers.recent`, `designers.prospective` | `quantity_traded` (legal interior design services) | decrease | Design work that clients would have bought and non-degreed designers would have done. Both sides lose the gain they expected. | OC-4 |
| C-26 | `designers.recent` | `earnings` | decrease | The earnings of practice, for those who leave for their next-best work. | EN-3, OC-4 |
| C-27 | `taxpayers` | `resources_available_other_uses` | decrease | What the general-budget share of the Board's costs would otherwise have funded. | OC-3, OC-1 |

The degree and supervised hours are already recorded as C-6, and grandfathered practitioners' fees and hours as C-4, so they are not listed again here.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | Many practitioners and would-be entrants lack the degree and would not otherwise get it, so the requirement binds. | binding | 0.9 | Share without a degree (about 60%); graduates per year against entry into the trade. | Almost every consequence fails. |
| A-2 | The Board enforces often enough, with unenforceable contracts as a further deterrent, that many comply or stop. | enforcement | 0.7 | Board budget; complaint volumes; fines issued. | C-2, C-5, C-11, C-13 weaken; C-3 grows. |
| A-3 | Some unlicensed practice continues undetected, mainly in homes. | enforcement | 0.8 | Complaint-driven enforcement; residential work leaves no permit trail. | C-3, C-18 not reported. |
| A-4 | Grandfathered designers leave the trade at about 3 to 5% a year. | durability | 0.85 | Age profile of practitioners; exit rates in comparable trades. | The medium-run tightening is weaker. |
| A-5 | Building departments reject commercial interior plans without a stamp. | enforcement | 0.85 | Permit procedures; plan-review checklists. | C-12, C-19 weaken. |
| A-6 | The degree and 3,500 hours go beyond what many residential clients would ask of a designer. | other | 0.7 | Share of residential work now done by non-degreed designers; client surveys. | C-6 is weaker as a cost beyond demand. |
| A-7 | The retail exemption can be used for full-room design given with furniture sales. | other | 0.75 | Wording of the exemption; Board guidance; current store practice. | C-8, C-16, C-17 weaken. |
| A-8 | Commercial clients can bring projects forward into the ten-month window. | expectations | 0.6 | Lease and fit-out cycles; permit processing times. | C-9 not reported. |
| A-9 | License holders, schools, retailers and architects can organize at a cost below their stake. | other | 0.8 | Existing associations. | C-10 weakens. |
| A-10 | Residential clients have close exempt or unlicensed substitutes: store design help, online services, doing it themselves. | substitutability | 0.85 | Size of retail design services; use of online design tools. | C-14 weakens; the down chain in C-20 weakens. |
| A-11 | Architects take on more commercial interior work. | substitutability | 0.7 | Architects' current share of interior fit-outs; capacity. | C-15 weakens. |
| A-12 | Households that use a store's design help buy most furnishings from that store. | other | 0.75 | Store sales data; design-help conversion rates. | C-16, C-17 not reported. |
| A-13 | The degree and exam cover code, egress, accessibility and plan preparation, which commercial clients need. | other | 0.75 | Curriculum hours by topic; exam blueprint; permit rejection rates by preparer. | C-19 becomes ambiguous. |
| A-14 | For homes, the training is largely unrelated to what clients value. | other | 0.45 | Client ratings and complaints by designer education; curriculum content. | Below cut-off. If it rose above 0.5, C-20 would become a decrease. |
| A-15 | Supervised positions are scarce relative to graduates in the medium run. | other | 0.6 | Number of licensed supervisors willing to take apprentices; graduates per year. | C-21 not reported. |
| A-16 | Some grandfathered designers would otherwise leave the trade for a time and return. | other | 0.65 | Career-break rates in the trade; age and family profile. | C-22 not reported. |
| A-17 | Belmar-based designers serve Arden homes without an Arden license on a meaningful scale. | mobility | 0.4 | Distance from Corvan to the border; Board enforcement across the line. | Below cut-off; not reported. |

## 11. Report

**The policy.** Arden now requires a license to practice interior design for pay: a degree, 3,500 supervised hours and an exam. Anyone with three years' paid practice who registers within 18 months is licensed without them. Commercial interior plans need a licensed designer's or architect's stamp for a permit. Store staff advising on their store's goods, architects, and work on one's own home are exempt.

**Visible consequences.** Everyone practicing interior design legally is licensed (C-1).

**Invisible consequences.**
- *Recent practitioners without a degree* must leave, join stores, or work informally (C-2, C-3, C-8), and those who leave earn less (C-26).
- *Grandfathered practitioners* bear fees and continuing education (C-4), charge more as competition thins (C-13), and stay in the trade rather than take breaks they would otherwise have taken (C-22, Tier C).
- *Would-be designers* face a degree and supervised hours (C-5, C-6). Schools gain students (C-7). Graduates compete for scarce supervised places and accept lower pay (C-21, Tier C).
- *Clients* pay more, increasingly so in the medium run (C-11, C-12). Households turn to store design help, online services or doing it themselves (C-14), and those who use unlicensed designers find them harder to check (C-18). Businesses use architects more (C-15). Fewer design services are bought and sold overall (C-25).
- *Furniture stores* sell more furniture through their design help, and trade showrooms less (C-16, C-17).
- *Commercial clients* rushed projects into the announcement window (C-9). Interest groups lobby over the rule's scope (C-10). *Taxpayers* fund part of the Board (C-27).

**Ambiguous effects.** The quality homeowners receive (C-20): the evidence assumed here does not show which chain dominates. Whether grandfathered designers and new degree-route entrants end up earning more (C-23, C-24).

**Key conditions.** Quality for commercial clients rises in the long run because the training covers what they need for permits (A-13, p = 0.75) and stamped plans leave no unlicensed alternative (A-5, p = 0.85). For homes, the answer turns on A-14 (p = 0.45). Grandfathering means the main supply effect comes in years 2 to 6, at a pace set by how fast grandfathered designers leave (A-4).

**What this analysis cannot say.** How much prices rise; whether better commercial plans are worth the costs to clients and excluded designers; building safety outcomes such as fire egress and accessibility (out of scope for version 1); whether the policy is desirable.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | designers (legal market) | share_of_sellers_licensed | increase | short | visible | B | K1, K2 | A-2 |
| C-2 | designers.recent | number_of_sellers (legal) | decrease | short | invisible | B | EN-1 | A-1, A-2 |
| C-3 | designers.recent | informal_activity | increase | short | invisible | B | RS-3, EN-3 | A-3 |
| C-4 | designers.grandfathered | compliance_cost | increase | short | invisible | A | OC-2 | none |
| C-5 | designers.prospective | entry_rate | decrease | medium–long | invisible | B | EN-1, TS-1 | A-1, A-2 |
| C-6 | designers.prospective (degree route) | compliance_cost | increase | long | invisible | B | OC-2, EN-1 | A-1, A-6 |
| C-7 | schools.design | quantity_demanded | increase | medium | invisible | B | EN-1 | A-1 |
| C-8 | retailers.furniture, designers.recent | reclassification | increase | short–medium | invisible | B | RS-5 | A-7 |
| C-9 | clients.commercial | quantity_traded (announcement window) | increase | short | invisible | B | RS-8 | A-8 |
| C-10 | designers.grandfathered, schools, retailers, architects | lobbying_effort | increase | medium–long | invisible | B | RS-7, EN-5 | A-9 |
| C-11 | clients.residential | price_paid | increase | medium–long | invisible | B | EN-1, TS-1 | A-1, A-2, A-4 |
| C-12 | clients.commercial | price_paid | increase | medium–long | invisible | B | EN-1, TS-1 | A-1, A-4, A-5 |
| C-13 | designers.grandfathered | net_price_received | increase | medium | invisible | B | EN-2 | A-1, A-2, A-4 |
| C-14 | clients.residential | quantity_substitute | increase | medium | invisible | B | EN-3, RS-1 | A-7, A-10 |
| C-15 | clients.commercial | quantity_substitute (architects) | increase | medium | invisible | B | RS-1 | A-11 |
| C-16 | retailers.furniture | quantity_traded (furniture) | increase | medium | invisible | B | RS-5, RS-9 | A-7, A-12 |
| C-17 | showrooms.trade | quantity_traded | decrease | medium | invisible | B | RS-5, RS-9 | A-7, A-12 |
| C-18 | clients.residential (informal) | search_cost | increase | short–medium | invisible | B | RS-3, RS-10 | A-3 |
| C-19 | clients.commercial | quality_per_unit | increase | long | visible | B | EN-4, DM-2 | A-5, A-13 |
| C-20 | clients.residential | quality_per_unit | ambiguous | medium–long | invisible | B | EN-4 (DM-2 not decisive) | A-10, A-14 |
| C-21 | apprentices | wage_rate | decrease | medium | invisible | C | GAP-016-1 | A-15 |
| C-22 | designers.grandfathered | job_changes | decrease | medium | invisible | C | GAP-016-2 | A-16 |
| C-23 | designers.prospective (degree route) | earnings | ambiguous | long | invisible | B | C-11, C-12 vs C-6, C-21; DM-3 | A-1, A-6 |
| C-24 | designers.grandfathered | earnings | ambiguous | medium | invisible | B | C-13 vs C-4 | A-1, A-2 |
| C-25 | clients, designers.recent, designers.prospective | quantity_traded (legal services) | decrease | medium–long | invisible | B | OC-4 | A-1, A-2 |
| C-26 | designers.recent | earnings | decrease | short–medium | invisible | B | EN-3, OC-4 | A-1, A-2 |
| C-27 | taxpayers | resources_available_other_uses | decrease | short | invisible | A | OC-3, OC-1 | none |

## Gaps found

- **GAP-016-1** (Tier C: C-21). No rule covers a requirement for experience supervised by incumbents. Such a requirement makes incumbents' willingness to supervise a bottleneck on entry, and lets them capture part of the rent through low apprentice pay. Proposed fix: a rule "EN-9 Supervised-practice requirement": if a license requires hours supervised by license holders, then `entry_rate` depends on the number of supervised places, and `apprentices.wage_rate` decreases where places are scarce relative to candidates; assumes supervision is costly or limited per supervisor (`other`).
- **GAP-016-2** (Tier C: C-22). RS-11 (lock-in) requires a benefit tied to a location. A grandfathered status that is lost by lapsing produces the same lock-in, tied to an occupation: holders turn down breaks and other work they would otherwise take. Proposed fix: widen RS-11's If clause to "a non-transferable benefit that is lost by a change of location or status (moving, leaving an occupation, letting a registration lapse)", with `job_changes` as the variable in both cases.
