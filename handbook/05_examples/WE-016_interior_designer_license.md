# WE-016 License requirement for interior designers, with grandfathering

Analyst: draft (Handbook 0.5)  |  Rule catalog version: 0.5  |  Status: awaiting expert review

A stylized policy in a fictional state, modeled on a common type of occupational-licensing law. It is a companion to WE-003: here existing practitioners are grandfathered, which changes the time structure, and the required training is partly related to the quality some buyers care about, which changes the quality result. The probabilities are illustrative; the evidence column says what a real analysis would cite.

## 1. Policy record

**Arvane Interior Design Practice Act.** Interior design was previously unregulated in the State of Arvane: anyone could offer it for pay. About 6,000 people do, roughly 40% of whom hold a degree in interior design. About half the trade's revenue comes from commercial work (offices, shops, restaurants), half from homes. Two accredited degree programs in Arvane graduate about 300 students a year. Arvane's largest city, Corvan, is 20 km from the border with Velmark, which does not license interior designers. The Act was passed ten months before it took effect.

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 License requirement | `licensing_requirement` | Interior design for pay: space planning, and selection of interior finishes and furnishings, for homes or businesses in Arvane | Anyone offering it, and firms employing them | A four-year accredited degree in interior design; 3,500 hours of work supervised by a licensed designer or architect; a state exam ($1,200). License fee $250 a year; 12 hours of continuing education a year. | K2; architects; retail employees advising on goods sold by their employer; work on one's own home; unpaid work |
| K2 Grandfathering | Exemption from K1's entry conditions | Existing practitioners | — | Anyone who documents three years of paid practice in Arvane before the effective date and registers within 18 months receives a license without the degree, hours or exam. The license lapses if not renewed, and cannot then be regained without meeting K1. | — |
| K3 Stamped plans | Part of K1 | Building permits for commercial interior alterations | Permit applicants | Plans must be stamped by a licensed interior designer or an architect. Previously, non-structural interior plans by anyone were accepted. | Homes |
| K4 Enforcement | Enforcement | K1 to K3 | State Board of Interior Design | Complaint-driven; fines up to $2,500 per violation; contracts for unlicensed practice cannot be enforced in court. Funded by license fees and the general budget. | None |

Unclear provisions: U1, whether choosing furnishings, finishes and colors without any space planning ("styling") is covered. U1-a: covered (the definition lists "selection of interior finishes and furnishings"). U1-b: not covered (only space planning, or styling done with it, is covered). The consequences below concern design work that includes space planning, which is covered under both readings; where a sign depends on the reading (styling-only services, C-30), one sign per reading is given.

## 2. Classification

| Component | Rothbard type | Binding? | Rule families |
|---|---|---|---|
| K1 | Triangular: prohibits exchanges between clients and unlicensed designers; a grant of privilege to license holders | Yes, for the roughly 60% without a degree who are not grandfathered, and for most would-be entrants (A-1) | EN (including EN-9 for the supervised hours), RS, OC |
| K2 | Exemption: a boundary in time | Delays the effect on supply (EN-1, Unless clause) | EN-1, TS-1, RS-8, RS-11 |
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
| `officials.building_departments` | Plan reviewers | Must check stamps on commercial interior plans. |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | designers (legal market) | `share_of_sellers_licensed` | increase | short | K1, K2 | A-2 |

The visible, stated aim: everyone who offers interior design for pay in Arvane is licensed. For the first years most license holders are grandfathered practitioners whose training has not changed, so the license certifies little that is new about them. Whether quality received rises is the question in section 7.

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-2 | `designers.recent` | `number_of_sellers` (legal) | decrease | short | EN-1 | A-1, A-2 |
| C-3 | `designers.recent` | `informal_activity` | increase | short | RS-3, EN-3 | A-3 |
| C-4 | `designers.grandfathered` | `compliance_cost` (documenting practice, fees, continuing education) | increase | short | OC-2 | none |
| C-5 | `designers.prospective` | `entry_rate` | decrease | medium to long | EN-1, EN-9, TS-1 | A-1, A-2, A-15 |
| C-6 | `designers.prospective` (degree route) | `compliance_cost` (degree and 3,500 supervised hours, beyond what many residential clients would ask for) | increase | long | OC-2, EN-1 | A-1, A-6 |
| C-7 | `schools.design` | `quantity_demanded` (degree places) | ambiguous | medium | CR-4b both ways; CR-12b (section 7) | A-1 |
| C-8 | `retailers.furniture`, `designers.recent` | `reclassification` (full-room design offered as "free design help" with furniture sales; recent designers joining stores as employees) | increase | short to medium | RS-5 | A-7 |
| C-9 | `clients.commercial` | `quantity_traded` (commercial interior projects permitted in the announcement window) | increase | short | RS-8 | A-8 |
| C-10 | `designers.grandfathered`, `schools.design`, `retailers.furniture`, `architects` | `lobbying_effort` (license holders and schools to widen the scope and keep the rule; retailers to keep their exemption; architects over the boundary of their work) | increase | medium to long | RS-7, EN-5 | A-9 |
| C-30 | `designers.recent` | `number_of_sellers` (styling-only services) | U1-a: decrease; U1-b: increase | short | U1-a: EN-1; U1-b: RS-5 | A-1, A-2 |
| C-33 | `clients.commercial` | `quantity_traded` (commercial interior projects permitted in the first months after the effective date) | decrease | short | RS-8, CR-10a | A-8 |

C-7: EN-1 does not say how demand for the qualifying input moves, and a direct derivation gives two opposing chains (section 7). Entrants who would have practiced without a degree now need one (CR-4b, x: enter without a degree, now removed; y: take the degree): up. Those who would have taken the degree anyway now face 3,500 supervised hours and an exam on top of it, and some choose another career (CR-4b, x: degree route, y: another career): down.

C-30: under U1-a, styling for pay needs a license, so recent designers without one stop offering it or offer it informally (EN-1). Under U1-b, styling is the uncovered form of the service, and some recent designers reshape their work to offer styling without space planning (RS-5).

C-9 and C-33 are one timing shift (RS-8; `02_ontology.md`, 2.5): projects moved into the window are not started again after it, so permitted commercial projects rise in the window and fall in the first months after the effective date, compared with the counterfactual.

C-2 and C-5 are EN-1 with its grandfathering exception. In the short run only the recent, non-degreed practitioners are excluded; the restriction on new entry shows up later (section 8).

Not reported: Velmark-based designers serving Arvane homes without an Arvane license (RS-4). Corvan is close to the border, but Arvane projects need an Arvane license whoever does them; A-17 is below the cut-off (p = 0.4).

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
| C-28 | `clients.residential` (using unlicensed designers) | `quality_information` | decrease | short to medium | RS-10 | | A-3 |
| C-29 | `clients.residential` (using unlicensed designers) | `disputes_settled_outside_courts` (fee disputes) | increase | short to medium | RS-10 | | A-3 |
| C-19 | `clients.commercial` | `quality_per_unit` | increase | long | EN-4, DM-2 | | A-5, A-13 |
| C-20 | `clients.residential` | `quality_per_unit` | ambiguous | medium to long | EN-4 | | A-10 |
| C-21 | `apprentices` | `wage_rate` | decrease | medium | EN-9 | | A-15 |
| C-31 | `apprentices` | `wait_time` (from graduation to license) | increase | medium | EN-9, CR-1, CR-6 | | A-1, A-15 |
| C-22 | `designers.grandfathered` | `job_changes` (leaving the occupation for a time) | decrease | medium | RS-11 | | A-16 |
| C-32 | `designers.grandfathered` | `compliance_cost` (fees and continuing education kept up while partly inactive, only to hold the license) | increase | medium to long | RS-11, OC-2 | | A-16 |
| C-34 | `architects` | `price_substitute` (architects' fees for interior work) | increase | medium | CR-9, CR-6 | interior designers and architects: `substitute`, close for commercial work | A-1, A-11, A-18 |

C-16, C-17: a household that takes a store's free design help buys most of the furnishings from that store. Purchases that independent designers would have placed with trade showrooms move to the stores (RS-9).

C-18, C-28, C-29: RS-10 applies to the informal practice in C-3. Unlicensed designers cannot advertise as designers (C-18), clients cannot check them (C-28), and since their contracts cannot be enforced in court, fee disputes are settled privately or not at all (C-29).

C-21: the 3,500 hours must be supervised by a licensed designer or architect, so incumbents' willingness to supervise limits entry (EN-9; also C-5). Supervised positions are scarce relative to graduates in the medium horizon (A-15), so graduates accept lower pay to get them, and incumbents capture part of the value of the license through their trainees' pay. The comparison is with what the same graduates would earn as junior designers without the requirement.

C-31: the 3,500 hours stand between graduation and practice (CR-1, operation 3), and where supervised places are scarce (A-15), graduates also wait for one, allocated by the supervisors' choice among them (CR-6).

C-34: commercial clients turn to architects (C-15). Architects are themselves licensed, so their capacity for interior work cannot grow at unchanged fees in the medium run (A-18); at the old fees more is asked of them than they offer, and their fees rise (CR-9, then CR-6 in that market). No pattern outside price controls gives a substitute's price after a demand shift; RS-1 gives only the quantity.

C-22: a grandfathered license lost by lapsing cannot be regained without the degree, and it cannot be transferred. Designers who would have left the trade for a few years (to raise children, to try other work) now keep renewing and working instead (A-16). This is the lock-in of RS-11, which since catalog 0.3 covers a benefit lost by a change of status as well as of location. Those who stay mainly to keep the license pay its fees and continuing education in years when they work little (C-32, OC-2).

Stopping points: lower sales at trade showrooms (C-17) would reach their suppliers at depth 4, a diffuse group; stopped. RS-11 in its location form does not apply, since the license is valid anywhere in Arvane; its status form is C-22.

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `schools.design`, `quantity_demanded` (degree places), medium | Entrants who would have practiced without a degree now need one (CR-4b). | Those who would have taken the degree anyway now also face 3,500 supervised hours and an exam, and some choose another career (CR-4b). | None | **ambiguous** (C-7). Enrollment rises if the first group is larger; the method cannot say which is. |
| `clients.commercial`, `quality_per_unit`, long | New entrants are trained and examined in building codes, egress, accessibility and plan preparation, which commercial clients need to get permits approved (EN-4, up chain; A-13, p = 0.75). | Higher prices (C-12) push some clients toward cheaper options (EN-3, down chain). | DM-2: stamped plans are required for permits (A-5, p = 0.85), so no close unlicensed substitute exists for permit work, and architects, the exempt alternative, are themselves licensed. The down chain has no lower-quality alternative to move to for permit work, so it gives no sign there. | **increase** (C-19), mostly in the long run, once new entrants are a large share of the trade. In the short run the licensed pool is the grandfathered pool, and quality is close to unchanged. If the curriculum did not cover what commercial clients need (A-13 false), the sign would be **ambiguous**. |
| `clients.residential`, `quality_per_unit`, medium to long | New entrants know space planning and materials; some of this matters to homeowners (EN-4, up chain). Its premise is that the training bears on what residential clients value, the negation of A-14 (p = 0.55). | Higher prices (C-11) push clients toward store design help, online services and doing it themselves (C-14), and toward unlicensed designers they cannot check (C-28) (EN-3, down chain; A-10, p = 0.85). Its premise is that these alternatives give lower quality than the designer they replace (A-20, p = 0.7). | DM-2 does not settle it. Both chains have their premises above the cut-off. Whether the up chain is weak depends on whether the training is unrelated to what residential clients value (taste, coordination, responsiveness): A-14 (largely unrelated) is put at p = 0.45, which decides only dominance, not whether the consequence is reported. | **ambiguous** (C-20). If evidence raised A-14 above 0.5 (for example, client ratings showing no difference between degreed and non-degreed residential designers), DM-2 would make the sign **decrease**, as in WE-003, given A-20. If evidence showed degreed designers clearly better at what homeowners value, the sign would stay ambiguous, because the down chain remains. |
| `designers.prospective` who take the degree route, `earnings`, long | Higher fees once licensed (C-11, C-12). | A degree and 3,500 supervised hours at low pay first (C-6, C-21). | DM-3 | **ambiguous** by design (C-23). Those who choose the route expect it to pay (LW-5); those who turn away expected it not to. |
| `designers.grandfathered`, `earnings`, medium | Higher fees as competition thins (C-13); staying in the trade instead of taking breaks (C-22) adds working time. | None on `earnings`. License fees and continuing education are `compliance_cost` (C-4, C-32), a different variable, and are not netted against earnings (CR-12c). Continuing-education hours would cut earnings only if they displaced billable hours, which is not established: by CR-4 the 12 hours come from the lowest-ranked use of time, which may be leisure. | None needed | **increase** (C-24). That they are better off on balance is not claimed: the fees and hours are a separate cost, and the method does not net them. |

## 8. Time structure

Grandfathering (K2) turns EN-1's supply effect into a slow, growing one. The trade's skills are a durable stock that wears out as people leave, and the license now limits what replaces them (TS-1).

- **Announcement window (ten months).** Commercial clients bring alterations forward to file permits before stamped plans are required (C-9), and file correspondingly fewer in the first months after the effective date (C-33). Students who now need a degree enroll, while some who would have taken it turn away from the longer route (C-7, ambiguous).
- **Short run (first 18 months).** Grandfathered practitioners register (C-4); recent practitioners without a degree leave, join stores, or carry on informally (C-2, C-3, C-8). Apart from them, supply is nearly unchanged, so prices move little and quality is unchanged: the licensed pool is the old pool.
- **Medium run (years 2 to 6): the tightest period.** Grandfathered designers leave at about 3 to 5% a year (A-4). New entrants arrive only after a degree and 3,500 hours, about two years after graduation; someone who starts a degree on the effective date is licensed around year 6. Supply falls fastest relative to the counterfactual here, and prices (C-11, C-12), architects' fees (C-34), grandfathered designers' fees and earnings (C-13, C-24), and the shortage of supervised places (C-21, C-31) are greatest. Lock-in (C-22) matters most while the grandfathered are still a large share.
- **Long run (beyond year 6).** The pipeline flows, at the pace set by supervised places (C-31). Supply settles below the counterfactual, since entry costs more (C-5). New entrants become a growing share of the trade, so the quality effects in section 7 appear mostly now. Non-degreed practitioners disappear from the legal market over about a working lifetime.
- **Expectations.** If students expect the scope to be widened or the rule relaxed (C-10), enrollment decisions are delayed or brought forward accordingly (TS-2).

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-25 | `clients.residential`, `clients.commercial`, `designers.recent`, `designers.prospective` | `quantity_traded` (legal interior design services) | decrease | Design work that clients would have bought and non-degreed designers would have done. Both sides lose the gain they expected. | OC-4 |
| C-26 | `designers.recent` | `earnings` | decrease | The earnings of practice, for those who leave for their next-best work, which pays less in money (A-19). | EN-3, OC-4 |
| C-35 | `officials.enforcement` (State Board) | `enforcement_cost` | increase | Board staff, investigations and hearings. | OC-3 |
| C-36 | `officials.building_departments` | `enforcement_cost` | increase | Checking stamps in commercial plan review. | OC-3, CR-1 |
| C-27 | `taxpayers` | `resources_available_other_uses` | decrease | What the general-budget share of the Board's costs would otherwise have funded. | OC-3, OC-1 |

C-35, C-27: OC-3's funding cases. The Board is funded by license fees and the general budget (K4). The fee-funded part is paid by license holders and is already recorded as their `compliance_cost` (C-4, C-32); the general-budget part comes from a budget that rises with the new task, so it falls on taxpayers (C-27). C-36: the record does not say how building departments fund the added check. If from a fixed budget, other plan review is slower; if from permit fees, permit applicants pay. Neither is signed.

C-26: by EN-3 (catalog 0.5), excluded designers are worse off by their own ranking; that their money earnings fall needs the premise that their next-best work pays less (A-19).

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
| A-8 | Commercial clients can bring projects forward into the ten-month window. | expectations | 0.6 | Lease and fit-out cycles; permit processing times. | C-9 and C-33 not reported. |
| A-9 | License holders, schools, retailers and architects can organize at a cost below their stake. | other | 0.8 | Existing associations. | C-10 weakens. |
| A-10 | Residential clients have close exempt or unlicensed substitutes: store design help, online services, doing it themselves. | substitutability | 0.85 | Size of retail design services; use of online design tools. | C-14 weakens; the down chain in C-20 weakens. |
| A-11 | Architects take on more commercial interior work. | substitutability | 0.7 | Architects' current share of interior fit-outs; capacity. | C-15 and C-34 weaken. |
| A-12 | Households that use a store's design help buy most furnishings from that store. | other | 0.75 | Store sales data; design-help conversion rates. | C-16, C-17 not reported. |
| A-13 | The degree and exam cover code, egress, accessibility and plan preparation, which commercial clients need. | other | 0.75 | Curriculum hours by topic; exam blueprint; permit rejection rates by preparer. | C-19 becomes ambiguous. |
| A-14 | For homes, the training is largely unrelated to what clients value. | other | 0.45 | Client ratings and complaints by designer education; curriculum content. | Below cut-off. If it rose above 0.5, C-20 would become a decrease. |
| A-15 | Supervision is costly or limited per supervisor, so supervised positions are scarce relative to graduates in the medium run (the assumption of EN-9). | other | 0.6 | Number of licensed supervisors willing to take apprentices; graduates per year. | C-21 and C-31's wait for a place not reported (the 3,500 hours themselves remain); C-5 rests on EN-1 alone. |
| A-16 | Some grandfathered designers would otherwise leave the trade for a time and return. | other | 0.65 | Career-break rates in the trade; age and family profile. | C-22 and C-32 not reported. |
| A-17 | Velmark-based designers serve Arvane homes without an Arvane license on a meaningful scale. | mobility | 0.4 | Distance from Corvan to the border; Board enforcement across the line. | Below cut-off; not reported. |
| A-18 | Architects' capacity for interior work cannot expand at unchanged fees in the medium run (they are licensed, and their own training pipeline is long). | other | 0.7 | Number of architects; their current workload and share of fit-outs; fee trends. | C-34 not reported. |
| A-19 | The next-best work of recent designers who leave (store design jobs, other occupations) pays less in money than their design practice. | other | 0.65 | Pay of retail design staff against independent practice; prior occupations of recent entrants. | C-26 not reported (they are still worse off by their own ranking). |
| A-20 | For homes, store design help, online services, doing it oneself and unlicensed designers who cannot be checked give lower quality than hiring the designer they replace. | other | 0.7 | Clients who hired designers when these alternatives were open revealed that they valued the designer more; client ratings by type of service. | The down chain in C-20 gives no sign; C-20 would rest on the up chain alone. |

## 11. Report

**The policy.** Arvane now requires a license to practice interior design for pay: a degree, 3,500 supervised hours and an exam. Anyone with three years' paid practice who registers within 18 months is licensed without them. Commercial interior plans need a licensed designer's or architect's stamp for a permit. Store staff advising on their store's goods, architects, and work on one's own home are exempt.

**Visible consequences.** Everyone practicing interior design legally is licensed (C-1).

**Invisible consequences.**
- *Recent practitioners without a degree* must leave, join stores, or work informally (C-2, C-3, C-8), and those who leave earn less in money if their next work pays less (C-26). Whether they can still offer styling alone depends on how the definition is read (C-30).
- *Grandfathered practitioners* bear fees and continuing education (C-4), charge more and earn more as competition thins (C-13, C-24), and stay in the trade rather than take breaks they would otherwise have taken, because a lapsed license cannot be regained (C-22), paying fees in years when they work little (C-32).
- *Would-be designers* face a degree and supervised hours (C-5, C-6). Graduates wait longer to practice (C-31), compete for scarce supervised places, and accept lower pay than they would have earned as junior designers (C-21).
- *Clients* pay more, increasingly so in the medium run (C-11, C-12). Households turn to store design help, online services or doing it themselves (C-14), and those who use unlicensed designers find them harder to find and check, and have no recourse in court over fees (C-18, C-28, C-29). Businesses use architects more (C-15), whose fees rise (C-34). Fewer design services are bought and sold overall (C-25).
- *Furniture stores* sell more furniture through their design help, and trade showrooms less (C-16, C-17).
- *Commercial clients* rushed projects into the announcement window (C-9) and filed fewer just after it (C-33). Interest groups lobby over the rule's scope (C-10). The Board and building departments spend on enforcement (C-35, C-36); *taxpayers* fund part of the Board (C-27).

**Ambiguous effects.** The quality homeowners receive (C-20): the evidence assumed here does not show which chain dominates. Whether new degree-route entrants end up earning more (C-23). Whether more or fewer students take interior design degrees (C-7): the degree is now required, but the route to practice is now longer.

**Key conditions.** Quality for commercial clients rises in the long run because the training covers what they need for permits (A-13, p = 0.75) and stamped plans leave no unlicensed alternative (A-5, p = 0.85). For homes, the answer turns on A-14 (p = 0.45), given that the alternatives homeowners turn to are worse than a designer (A-20, p = 0.7). Grandfathering means the main supply effect comes in years 2 to 6, at a pace set by how fast grandfathered designers leave (A-4).

**What this analysis cannot say.** How much prices rise; whether better commercial plans are worth the costs to clients and excluded designers; building safety outcomes such as fire egress and accessibility (out of scope for version 1); whether the policy is desirable.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | designers (legal market) | share_of_sellers_licensed | increase | short | visible | B | K1, K2 | A-2 |
| C-2 | designers.recent | number_of_sellers (legal) | decrease | short | invisible | B | EN-1 | A-1, A-2 |
| C-3 | designers.recent | informal_activity | increase | short | invisible | B | RS-3, EN-3 | A-3 |
| C-4 | designers.grandfathered | compliance_cost | increase | short | invisible | A | OC-2 | none |
| C-5 | designers.prospective | entry_rate | decrease | medium–long | invisible | B | EN-1, EN-9, TS-1 | A-1, A-2, A-15 |
| C-6 | designers.prospective (degree route) | compliance_cost | increase | long | invisible | B | OC-2, EN-1 | A-1, A-6 |
| C-7 | schools.design | quantity_demanded (degree places) | ambiguous | medium | invisible | B | CR-4b (+, entrants now needing the degree; −, degree-takers facing the hours and exam); CR-12b | A-1 |
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
| C-28 | clients.residential (informal) | quality_information | decrease | short–medium | invisible | B | RS-3, RS-10 | A-3 |
| C-29 | clients.residential (informal) | disputes_settled_outside_courts | increase | short–medium | invisible | B | RS-3, RS-10 | A-3 |
| C-19 | clients.commercial | quality_per_unit | increase | long | visible | B | EN-4, DM-2 | A-5, A-13 |
| C-20 | clients.residential | quality_per_unit | ambiguous | medium–long | invisible | B | EN-4 (DM-2 not decisive) | A-10, A-20 |
| C-21 | apprentices | wage_rate | decrease | medium | invisible | B | EN-9 | A-15 |
| C-22 | designers.grandfathered | job_changes | decrease | medium | invisible | B | RS-11 | A-16 |
| C-23 | designers.prospective (degree route) | earnings | ambiguous | long | invisible | B | C-11, C-12 vs C-6, C-21; DM-3 | A-1, A-6 |
| C-24 | designers.grandfathered | earnings | increase | medium | invisible | B | EN-2, CR-9; fees are compliance_cost, not netted (CR-12c) | A-1, A-2, A-4 |
| C-25 | clients, designers.recent, designers.prospective | quantity_traded (legal services) | decrease | medium–long | invisible | B | OC-4 | A-1, A-2 |
| C-26 | designers.recent | earnings | decrease | short–medium | invisible | B | EN-3, OC-4 | A-1, A-2, A-19 |
| C-27 | taxpayers | resources_available_other_uses | decrease | short | invisible | A | OC-3, OC-1 | none |
| C-30 | designers.recent | number_of_sellers (styling-only services) | U1-a: decrease; U1-b: increase | short | invisible | B | U1-a: EN-1; U1-b: RS-5 | A-1, A-2 |
| C-31 | apprentices | wait_time (graduation to license) | increase | medium | invisible | B | EN-9, CR-1, CR-6 | A-1, A-15 |
| C-32 | designers.grandfathered | compliance_cost (fees while partly inactive) | increase | medium–long | invisible | B | RS-11, OC-2 | A-16 |
| C-33 | clients.commercial | quantity_traded (first months after effective date) | decrease | short | invisible | B | RS-8, CR-10a | A-8 |
| C-34 | architects | price_substitute (interior work) | increase | medium | invisible | B | RS-1, CR-9, CR-6 | A-1, A-11, A-18 |
| C-35 | officials.enforcement | enforcement_cost | increase | short | invisible | A | OC-3 | none |
| C-36 | officials.building_departments | enforcement_cost | increase | short | invisible | B | OC-3, CR-1 | A-5 |

## Gaps found

- GAP-016-1 (closed in catalog 0.3: EN-9). C-21 is now Tier B, resting on A-15; EN-9 also enters C-5.
- GAP-016-2 (closed in catalog 0.3: RS-11 widened to a benefit lost by a change of status). C-22 is now Tier B, resting on A-16.

Review corrections on the update to catalog 0.3: C-20 listed A-14 (p = 0.45) as an assumption; A-14 is what would decide the ambiguity, not an assumption the ambiguous sign rests on, so it is removed from C-20's list. The RS-10 effects of unlicensed practice are split into their own variables (C-18, C-28, C-29). Two place names that exist in the real world were replaced with fictional ones.
- Catalog 0.5: corrected after the core-only comparison (see ../05_examples_core/WE-016_interior_designer_license_core.md): degree places (C-7) made ambiguous (EN-1 misapplied); grandfathered earnings (C-24) made an increase (fees are compliance_cost, CR-12c); added the styling readings (C-30), trainees' wait (C-31), fees kept up while inactive (C-32), the dip after the announcement window (C-33), architects' fees (C-34) and enforcement costs with OC-3's funding cases (C-35, C-36); EN-3's earnings premise (A-19), EN-4's down-chain premise (A-20) and A-18 added.
