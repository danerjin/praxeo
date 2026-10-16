# WE-016 / Core-only re-run: License requirement for interior designers, with grandfathering

Analyst: core-only re-run (Handbook 0.4)  |  Rules: core rules CR-1 to CR-12 only  |  Status: awaiting comparison

## 1. Policy record

**Arvane Interior Design Practice Act.** Interior design was previously unregulated in the State of Arvane: anyone could offer it for pay. About 6,000 people do, roughly 40% of whom hold a degree in interior design. About half the trade's revenue comes from commercial work (offices, shops, restaurants), half from homes. Two accredited degree programs in Arvane graduate about 300 students a year. Arvane's largest city, Corvan, is 20 km from the border with Velmark, which does not license interior designers. The Act was passed ten months before it took effect.

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 License requirement | `licensing_requirement` | Interior design for pay: space planning, and selection of interior finishes and furnishings, for homes or businesses in Arvane | Anyone offering it, and firms employing them | A four-year accredited degree in interior design; 3,500 hours of work supervised by a licensed designer or architect; a state exam ($1,200). License fee $250 a year; 12 hours of continuing education a year. | K2; architects; retail employees advising on goods sold by their employer; work on one's own home; unpaid work |
| K2 Grandfathering | Exemption from K1's entry conditions | Existing practitioners | — | Anyone who documents three years of paid practice in Arvane before the effective date and registers within 18 months receives a license without the degree, hours or exam. The license lapses if not renewed, and cannot then be regained without meeting K1. | — |
| K3 Stamped plans | Part of K1 | Building permits for commercial interior alterations | Permit applicants | Plans must be stamped by a licensed interior designer or an architect. Previously, non-structural interior plans by anyone were accepted. | Homes |
| K4 Enforcement | Enforcement | K1 to K3 | State Board of Interior Design | Complaint-driven; fines up to $2,500 per violation; contracts for unlicensed practice cannot be enforced in court. Funded by license fees and the general budget. | None |

Unclear provisions: whether choosing furnishings, finishes and colors without any space planning ("styling") is covered. The definition lists "selection of interior finishes and furnishings", so it is assumed covered. This analysis reports both readings where a sign depends on it: **U1-a** styling is covered; **U1-b** styling is not covered.

## 2. Classification

CR-1 applied to each component and each actor class (operations: 1 remove an option, 2 add an option, 3 change what an option brings, 4 transfer means).

| Component | Rothbard type | Binding? (assumption ID) | Core rules | CR-1 operations, by actor class |
|---|---|---|---|---|
| K1 | triangular (restricts exchanges between designers and clients) | Yes for the roughly 60% without a degree and for non-degree entrants (A-1) | CR-1, CR-3, CR-4, CR-5, CR-6, CR-7, CR-9, CR-11 | Unlicensed designers: 1 (paid practice), weakened to 3 where enforcement is imperfect (A-3). Would-be entrants: 3 (degree, hours, exam attached to entry). Licensed designers: 3 and 4 (fee, continuing education). Clients: 1 (hiring an unlicensed designer) or 3 (unenforceable contract, risk). Architects, retailers, own-home work: none (exempt; their options keep what they bring). |
| K2 | exemption from K1 (adds an option relative to K1) | Yes: binds for practitioners with three years' practice who would otherwise fall under K1 | CR-1, CR-3b, CR-4, CR-10 | Practitioners with three years: 2 relative to K1 (license without entry conditions), 3 (registration paperwork; lapse rule attaches a cost to leaving). Practitioners with less than three years: none (K1 applies in full). |
| K3 | triangular (restricts who may prepare plans accepted for permits) | Yes (A-5) | CR-1, CR-3a, CR-4, CR-9 | Commercial permit applicants: 1 (plans by unlicensed preparers no longer accepted). Licensed designers and architects: none directly; their service becomes required (felt through CR-9). |
| K4 | binary (budget) plus enforcement of K1 to K3 | Enforcement is complaint-driven (A-2, A-3) | CR-1, CR-8 | Unlicensed designers: 3 (fines up to $2,500, unenforceable contracts). Licensed designers: 4 (fees fund the Board). Taxpayers: 4 (general-budget share). |

## 3. Actor classes

| Actor class | Role | How its options change (CR-1) |
|---|---|---|
| designers.grandfathered | Existing practitioners with three years' paid practice who register | Keep practicing (2 relative to K1); fee and continuing education (3, 4); lapse rule makes a temporary exit cost the license (3). |
| designers.excluded | Existing practitioners with less than three years' practice and no license, or who fail to register | Legal paid practice removed (1); practice continues only with risk of fines and unenforceable contracts (3). Exempt uses (retail employment, unpaid work) stay open. |
| designers.licensed | All license holders (grandfathered and newly licensed) | Fee and continuing education (3, 4); fewer competitors (felt through CR-9). |
| sellers.prospective (would-be designers) | People who would have entered the trade | Entry now requires the degree, 3,500 supervised hours and the exam (3). |
| entrants.graduates | Degree holders not yet licensed | Must find supervised positions and pass the exam (3). |
| clients.commercial | Firms commissioning commercial interiors | Unlicensed preparers' plans rejected (1, K3); hiring unlicensed designers removed or risky (1, 3). |
| clients.residential | Households commissioning home design | Hiring unlicensed designers removed or risky (1, 3); exempt substitutes unchanged. |
| architects | Exempt competitors and permitted supervisors | No direct change; demand for their interior work rises (CR-9). |
| retailers.with_design_help, retail_design_staff | Stores that give design help with furniture sales (exempt), and their staff | No direct change; demand for exempt design help and supply of staff rise (CR-9, CR-7). |
| furniture_stores.without_design_help | Competing furnishing retailers | No direct change; customers move to stores with design help (CR-9). |
| degree programs | Two accredited schools (input suppliers) | No direct change; the degree becomes a condition of entry (CR-9). |
| sellers.complements (fit-out contractors) | Builders and fitters of commercial interiors | No direct change; demand follows the number of alterations (CR-9). |
| officials.enforcement (State Board), officials.building_departments | Administer K1 to K4 | New duties (CR-8c). |
| taxpayers | Fund part of the Board | Transfer (4). |
| neighboring_jurisdictions (Velmark designers) | Unlicensed designers just across the border | No direct change; serving Arvane homes is covered by K1 (A-17, p 0.4: not reported). |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | sellers.current (interior designers, legal) | number_of_sellers | decrease | short | CR-1 op. 1 (unlicensed paid practice removed); CR-2; CR-4b (x: practice, y: exit) for practitioners neither grandfathered nor licensed | A-1, A-2 |
| C-2 | sellers.prospective (would-be designers) | entry_rate | decrease | medium | CR-1 op. 3 (degree, 3,500 supervised hours and exam attached to entry); CR-4b (x: enter, y: another occupation) | A-1, A-2 |
| C-3 | designers.licensed | compliance_cost | increase | short | CR-1 op. 3 and 4 ($250 annual fee, 12 hours of continuing education, registration paperwork); CR-3a; CR-8c |  |
| C-4 | clients.commercial (permit applicants) | compliance_cost | increase | short | CR-1 op. 1 (unstamped plans no longer accepted, K3); CR-3a; CR-8c | A-5 |

The direct effect is the one the Act's supporters point to: fewer legal sellers, harder entry, and a new license cost for those who remain, plus stamped plans for commercial permits.

## 5. Responses

Each actor class, with CR-4 applied to every pair of options it has.

- **Excluded designers.** CR-4 (x: comply, y: violate): some keep practicing, mainly for homes, where there is no permit trail (C-5). CR-4 (x: practice, y: exit): others stop, and their earnings fall (C-6). CR-4 (x: here, y: there): serving Arvane from Velmark is still covered by K1; not reported (A-17). CR-4 (x: covered form, y: uncovered form): styling-only work depends on the reading (C-7); retail employment is an exempt form (see section 6).
- **Would-be entrants.** CR-4 (x: stay out, y: enter): entry costs a degree, supervised hours and an exam, so some stay out (C-2); others get the degree, which pushes demand for degree places up, while the added hours and exam push it down (C-8).
- **Graduates.** CR-1 op. 3 and CR-5c: they wait for supervised positions and accept lower pay in them (C-9, C-10).
- **Grandfathered designers.** CR-4 (x: leave for a time, y: stay and renew): the lapse rule keeps some in the trade who would have taken a break, and they keep paying fees while partly inactive (C-13, C-14).
- **Clients.** CR-4 (x: licensed designer, y: substitute): households turn to store design help, online services and their own work (C-11); firms turn to architects (C-12). CR-4 (x: later, y: now) under CR-10a: firms bring projects forward into the ten-month window, followed by a dip (C-15, C-16).
- **Organized interests.** CR-4 (x: accept, y: lobby) (C-17).

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-5 | designers.excluded (no license, no grandfathering) | informal_activity | increase | short | CR-4b (x: comply, y: violate), mainly residential work; CR-1 op. 3 (complaint-driven enforcement attaches a risk rather than removing the option) | A-1, A-3 |
| C-6 | designers.excluded (no license, no grandfathering) | earnings | decrease | short | CR-3a (chosen option removed or burdened); CR-4b (those who stop fall back to a lower-ranked use of their labor) | A-1, A-2 |
| C-7 | designers.excluded (no license, no grandfathering) | number_of_sellers (unlicensed styling-only services) | U1-a: decrease; U1-b: increase | short | U1-a (styling covered): CR-1 op. 1, CR-4b (x: offer styling, y: stop). U1-b (styling not covered): CR-4b (x: the covered form, y: the uncovered form), reclassifying full design as styling | A-1, A-2 |
| C-8 | sellers.prospective (would-be designers) | quantity_demanded (interior design degree places) | ambiguous | medium | (+) CR-4b (x: enter without a degree, now removed; y: get the degree) for entrants who still want to practice; (+) CR-9 and CR-6 price formation, higher expected earnings of licensed designers (C-21); (-) CR-4b (x: degree route, y: another career), since 3,500 hours and the exam are attached to the degree route; CR-12b | A-1, A-2 |
| C-9 | entrants.graduates | wait_time (from graduation to license) | increase | medium | CR-1 op. 3 (3,500 supervised hours and exam before practice); CR-6 (supervised positions are scarce and allocated by the supervisors' choice among graduates) | A-1, A-15 |
| C-10 | entrants.graduates (in supervised positions) | wage_rate | decrease | medium | CR-5c (supervised hours now bring credit toward the license, so the range of terms a trainee accepts moves down); CR-6 price formation (graduates compete for scarce supervised positions) | A-1, A-15 |
| C-11 | clients.residential | quantity_substitute (store design help, online design services, own work) | increase | medium | CR-4b (x: hire a designer, y: an exempt or unlicensed substitute), after the price of licensed design rises (C-20) | A-10, A-7 |
| C-12 | clients.commercial | quantity_substitute (architects' interior work) | increase | medium | CR-4b (x: licensed interior designer, y: architect, who is exempt and may stamp plans) | A-11, A-5 |
| C-13 | designers.grandfathered | job_changes (temporary exits from the trade) | decrease | long | CR-1 op. 3 (the license lapses if not renewed and cannot be regained without meeting K1); CR-4b (x: leave for a time, y: stay and renew) | A-16 |
| C-14 | designers.grandfathered | compliance_cost | increase | long | CR-4b (x: let the license lapse, y: keep renewing while partly inactive); CR-8c (fees and continuing education kept up only to hold the license) | A-16 |
| C-15 | clients.commercial | quantity_traded (commercial interior design, ten-month announcement window) | increase | short | CR-10a; CR-4b (x: start the project after the effective date, y: start it now) | A-8 |
| C-16 | clients.commercial | quantity_traded (commercial interior design, first months after the effective date) | decrease | short | CR-10a (projects moved into the window are not repeated after it); arithmetic | A-8 |
| C-17 | designers.licensed, degree programs, retailers, architects | lobbying_effort | increase | medium | CR-4b (x: accept the rules as written, y: lobby to keep, extend or widen them, or to keep the retail exemption); each now has a concentrated stake | A-9 |

## 6. Second-order effects

Depth limit 4; prune diffuse bystander effects after depth 3. Each link names its relation (02_ontology 2.8). Relations used: interior design (licensed) and architects' interior work: substitute, close for commercial; licensed residential design and store design help, online services, own work: substitute, close (A-10); store design help and the same store's furnishings: complement (A-12); design and stamped plans to commercial alterations: input_to; alterations and fit-out work: complement; licensed and unlicensed residential design: same market, other segment.

Chains, with depth:
1. K1 (1) excluded designers exit (2) fewer sellers, price of licensed design rises (3) commercial alterations fall (4) fit-out work falls (C-18, C-23, C-33). Stopped at depth 4.
2. K1 (1) residential price rises (2) households take store design help (3) furnishings move to stores with design help and away from other stores (4) (C-20, C-11, C-31, C-32). Stopped at depth 4.
3. K1 (1) excluded designers move to exempt retail jobs (2) retail design labor market (3) (C-29, C-30).
4. K1 and K4 (1) informal residential practice (2) no advertising or courts (3) (C-27, C-28).
5. K1 (1) fewer competitors (2) licensed designers' earnings and architects' fees rise (3) (C-21, C-25).
6. K1 and K2 over time (CR-10b): grandfathered designers leave and are replaced only through the degree route (2), so the number of sellers falls further and commercial prices rise further (3) (C-22, C-19).

Component interactions: K2 opens an exit from K1 for existing practitioners but closes it again after any lapse; K3 extends K1's reach to every commercial permit, removing the substitute (unlicensed preparers) that the commercial segment would otherwise use; K4's unenforceable-contract clause changes what informal practice brings (CR-1 op. 3) beyond the fines.

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-18 | clients.commercial | price_paid (commercial interior design) | increase | medium | CR-4b exits and lower entry (C-1, C-2); CR-6 first paragraph (at the old price planned purchases exceed planned sales, so the price rises); CR-9 (competitors removed); K3 removes unlicensed preparers | same market (fewer sellers) | A-1, A-2, A-5 |
| C-19 | clients.commercial | price_paid (commercial interior design) | increase | long | CR-10b (the grandfathered stock leaves through exits and is replaced only through the degree route); CR-6 first paragraph | same market (fewer sellers) | A-1, A-2, A-4, A-5, A-15 |
| C-20 | clients.residential | price_paid (licensed residential design) | increase | medium | CR-4b exits; CR-6 first paragraph; CR-7b (residential clients have close substitutes, so the rise is limited by them; direction only) | same market (fewer sellers) | A-1, A-2, A-10 |
| C-21 | designers.licensed | earnings | increase | medium | CR-9 (competitors removed); CR-6 first paragraph (C-18); CR-7b (the lasting gain from restricted entry settles on the means that cannot be added to: licenses held when the rule took effect) | same market (competitors) | A-1, A-2, A-5 |
| C-22 | sellers.current (interior designers, legal) | number_of_sellers | decrease | long | CR-10b (grandfathered designers leave at 3 to 5% a year and the license cannot be regained); CR-4b at entry (C-2); arithmetic against the counterfactual, in which non-degree entrants also replace them | same market | A-1, A-2, A-4 |
| C-23 | clients.commercial | quantity_traded (commercial interior alterations) | decrease | medium | CR-4c (a higher price of plans makes the least valued projects the first given up) after C-18 and C-4 | input_to (design and stamped plans are inputs to alterations) | A-1, A-5, A-N1 |
| C-24 | clients.residential | quantity_traded (residential design by designers, legal) | decrease | medium | CR-5a (exchanges with non-degreed designers that would have taken place are prevented); CR-4c after C-20 | same market | A-1, A-2, A-6 |
| C-25 | architects | price_substitute (architects' interior design fees) | increase | medium | CR-9 (demand for a competing good moves with the target's price); CR-6 first paragraph in the architects' market | substitute (close, commercial) | A-1, A-11 |
| C-26 | clients.commercial | quality_information | increase | medium | CR-11c (the license conveys that its holder was trained in code, egress, accessibility and plan preparation) | same market | A-13 |
| C-27 | clients.residential (using unlicensed designers) | quality_information | decrease | medium | CR-11b (unlicensed designers cannot advertise openly, build public reputations or use the courts) | same market, informal segment | A-3 |
| C-28 | clients.residential (using unlicensed designers) | disputes_settled_outside_courts | increase | medium | CR-11b; CR-1 op. 3 (K4 makes contracts for unlicensed practice unenforceable) | same market, informal segment | A-3 |
| C-29 | retail_design_staff | employment | increase | medium | CR-7a (excluded designers move their labor to the exempt use); CR-9 (demand for store design help rises with C-11) | substitute (retail design help, close for homes) | A-7, A-10, A-N2 |
| C-30 | retail_design_staff | wage_rate | ambiguous | medium | (+) CR-9, LW-10 (demand for store design help rises, so demand for the labor that provides it rises); (-) CR-7a (added labor from excluded designers lowers the yield of that use); CR-12b | substitute (retail design help) | A-7, A-10, A-N2 |
| C-31 | retailers.with_design_help | quantity_traded (furnishings sold by stores with design help) | increase | medium | CR-9 (households who take a store's design help buy most furnishings from it); after C-11 | complement (store design help and the same store's furnishings) | A-7, A-10, A-12 |
| C-32 | furniture_stores.without_design_help | quantity_traded (furnishings) | decrease | medium | CR-9 (competitors of the stores in C-31 lose the sales that move to them) | same market, other segment (furnishing retail) | A-7, A-10, A-12 |
| C-33 | sellers.complements (fit-out contractors) | quantity_complement (commercial fit-out work) | decrease | medium | CR-9, LW-10 (demand for fit-out work follows the number of alterations, C-23) | complement (design and fit-out of the same project) | A-1, A-5, A-N1 |
| C-34 | officials.building_departments | enforcement_cost | increase | short | CR-1 op. 3 (stamp check added to plan review); CR-8c | none (administration) | A-5 |

## 7. Combined effects

CR-12 applied to every (actor class, variable, horizon) key reached by more than one chain.

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance premise | Combined sign |
|---|---|---|---|---|
| sellers.prospective, quantity_demanded (degree places), medium | Non-degree entrants who still want to practice must now get the degree (CR-4b); higher expected earnings of license holders (CR-9) | Hours and exam attached to the degree route (CR-4b) | None stated; no core rule gives one | ambiguous (CR-12b) |
| retail_design_staff, wage_rate, medium | Demand for store design help rises (CR-9, LW-10) | Excluded designers add labor to the exempt use (CR-7a) | None | ambiguous (CR-12b) |
| clients.commercial, price_paid, medium | Fewer sellers (CR-4b, CR-6); K3 makes stamps necessary | None found (architects as substitutes limit the rise but do not reverse it) | Not needed | increase (CR-12a) |
| designers.licensed, earnings, medium | Fewer competitors and higher prices (CR-9, CR-6) | The fee and continuing education are costs, not a fall in money earnings, and are recorded separately (C-3); CR-12c | Not needed | increase |
| clients.residential, resources_available_other_uses, medium | None | Higher fees, fallback to lower-ranked substitutes, own time | Not needed | decrease (CR-12a) |

No other key is reached by opposing chains. Different variables are never netted (CR-12c): the licensed designers' earnings gain and the clients' outlays are kept as separate consequences, as CR-8's symmetry requires.

## 8. Time structure

- **Announcement window (CR-10a).** The Act passed ten months before it took effect. Commercial clients who can bring projects forward do so (A-8), so commercial design work rises in the window and dips in the first months after (C-15, C-16). Practitioners just short of three years' practice cannot qualify by acting sooner, because the three years must be documented before the effective date; no consequence is recorded for them beyond C-6.
- **Registration window.** Grandfathered designers have 18 months to register; this is a one-time paperwork cost included in C-3.
- **Stock of licensed designers (CR-10b).** The licensed stock changes only through flows: grandfathered designers leave at 3 to 5% a year (A-4), and entry is limited to degree holders who complete 3,500 supervised hours (A-15). The restriction therefore bites more over time: C-22 and C-19 are long-run consequences that grow.
- **Lapse rule.** Because a lapsed license cannot be regained without meeting K1, temporary exits fall (C-13). The effect persists for as long as grandfathered designers remain in the trade.
- **Earnings capture (CR-7b).** The gain from restricted entry settles on those holding licenses when the rule takes effect; it is not resold, because the license cannot be sold. It shows up in earnings, not in an asset price.

## 9. Opportunity costs

CR-3 and CR-8. The symmetry requirement of CR-8 is applied: the licensed designers' earnings gain (C-21) is matched by clients' outlays (C-37, C-38); license fees paid by designers (C-3) are receipts of the Board and reduce what taxpayers fund.

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-35 | officials.enforcement (State Board) | enforcement_cost | increase | Staff time and funds that would have served other public uses | CR-8c (Board staff, investigations and hearings); K4 |
| C-36 | taxpayers | resources_available_other_uses | decrease | Other public spending or lower taxes | CR-8a, CR-8b (the general-budget share of the Board's cost is withdrawn from other uses) |
| C-37 | clients.commercial | resources_available_other_uses | decrease | Other spending by firms paying higher fees for plans | CR-8b (the higher fees counted as designers' gain in C-21 are the clients' matching outlay); CR-3a |
| C-38 | clients.residential | resources_available_other_uses | decrease | Time and money households would have spent on other ends | CR-3a (fallback to a lower-ranked substitute or own work); CR-8b (higher fees); CR-8c (own time spent on design) |
| C-39 | entrants.graduates | resources_available_other_uses | decrease | Earnings and time in the use graduates would have chosen | CR-8c (exam fee, study time and supervised hours spent only to qualify); CR-3c |

Prevented exchanges (CR-5a) between clients and non-degreed designers are recorded as C-24; those between firms and unlicensed plan preparers as part of C-23.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | Many practitioners and would-be entrants lack the degree and would not otherwise get it, so the requirement binds. | binding | 0.9 | Share without a degree (about 60%); graduates per year against entry into the trade. | Most consequences vanish. |
| A-2 | The Board enforces often enough, with unenforceable contracts as a further deterrent, that many comply or stop. | enforcement | 0.7 | Board budget; complaint volumes; fines issued. | Exits and price rises shrink; informal practice grows. |
| A-3 | Some unlicensed practice continues undetected, mainly in homes. | enforcement | 0.8 | Complaint-driven enforcement; residential work leaves no permit trail. | Informal-market consequences vanish. |
| A-4 | Grandfathered designers leave the trade at about 3 to 5% a year. | durability | 0.85 | Age profile of practitioners; exit rates in comparable trades. | Long-run fall in sellers is slower. |
| A-5 | Building departments reject commercial interior plans without a stamp. | enforcement | 0.85 | Permit procedures; plan-review checklists. | K3 consequences vanish. |
| A-6 | The degree and 3,500 hours go beyond what many residential clients would ask of a designer. | other | 0.7 | Share of residential work now done by non-degreed designers; client surveys. | Fewer prevented residential exchanges. |
| A-7 | The retail exemption can be used for full-room design given with furniture sales. | other | 0.75 | Wording of the exemption; Board guidance; current store practice. | Retail chains weaken. |
| A-8 | Commercial clients can bring projects forward into the ten-month window. | expectations | 0.6 | Lease and fit-out cycles; permit processing times. | No window rise or dip. |
| A-9 | License holders, schools, retailers and architects can organize at a cost below their stake. | other | 0.8 | Existing associations. | No lobbying consequence. |
| A-10 | Residential clients have close exempt or unlicensed substitutes: store design help, online services, doing it themselves. | substitutability | 0.85 | Size of retail design services; use of online design tools. | Residential price rise larger; substitution chains vanish. |
| A-11 | Architects take on more commercial interior work. | substitutability | 0.7 | Architects' current share of interior fit-outs; capacity. | Architect chains vanish. |
| A-12 | Households that use a store's design help buy most furnishings from that store. | other | 0.75 | Store sales data; design-help conversion rates. | Furnishing-retail chains vanish. |
| A-13 | The degree and exam cover code, egress, accessibility and plan preparation, which commercial clients need. | other | 0.75 | Curriculum hours by topic; exam blueprint; permit rejection rates by preparer. | License conveys little to commercial clients. |
| A-14 | For homes, the training is largely unrelated to what clients value. | other | 0.45 | Client ratings and complaints by designer education; curriculum content. | Below cut-off; not used in a reported consequence. |
| A-15 | Supervision is costly or limited per supervisor, so supervised positions are scarce relative to graduates in the medium run. | other | 0.6 | Number of licensed supervisors willing to take apprentices; graduates per year. | No wait or trainee wage effect beyond the hours themselves. |
| A-16 | Some grandfathered designers would otherwise leave the trade for a time and return. | other | 0.65 | Career-break rates in the trade; age and family profile. | Lapse-rule consequences vanish. |
| A-17 | Velmark-based designers serve Arvane homes without an Arvane license on a meaningful scale. | mobility | 0.4 | Distance from Corvan to the border; Board enforcement across the line. | Below cut-off; not used. |
| A-N1 | Some commercial clients are at the margin of undertaking an interior alteration, so that a higher cost of plans leads some to defer, shrink or cancel projects. | other | 0.7 | Discretionary share of fit-outs (refreshes rather than lease-required work); fee share of project cost. | C-23 and C-33 vanish. |
| A-N2 | Some designers excluded by K1 take jobs as retail design staff under the retail exemption rather than leave design work. | mobility | 0.7 | Current movement between independent practice and store design jobs; store hiring. | C-29 vanishes; C-30 becomes an increase. |

**Not reported** (an assumption below 0.5):
- Velmark designers serving Arvane homes: `cross_border_purchases` increase for residential clients, and a share of the informal market served from across the line (A-17, p 0.4).
- Residential clients' `quality_information` from the license as a signal, and any change in residential `quality_per_unit`: whether the license tells home clients anything they value depends on A-14 (p 0.45).

## 11. Report

**The policy:** From the effective date, interior design for pay in Arvane (space planning and selection of finishes and furnishings) requires a license: a four-year degree, 3,500 supervised hours and a $1,200 exam, then $250 a year and 12 hours of continuing education. Practitioners with three years' documented practice get a license without these conditions if they register within 18 months, but lose it for good if it lapses. Commercial interior permits need plans stamped by a licensed designer or an architect. Architects, retail staff advising on their employer's goods, own-home and unpaid work are exempt. The Board enforces on complaint, with fines up to $2,500 and unenforceable contracts.

**Visible consequences:** Fewer legal sellers (C-1) and fewer entrants (C-2); license fees and continuing education for those who remain (C-3); a stamp cost for commercial permit applicants (C-4); new Board spending (C-35); a rush of commercial projects into the ten-month window (C-15).

**Invisible consequences:**
- *Excluded designers:* lower earnings (C-6); some keep working informally, mainly in homes (C-5), where clients lose reviews and courts (C-27, C-28); some move into exempt store design jobs (C-29).
- *Licensed designers:* higher earnings from fewer competitors (C-21); grandfathered designers stay in the trade and keep renewing rather than take breaks (C-13, C-14).
- *Graduates:* longer wait to practice and lower pay in supervised positions (C-9, C-10), plus fees and time spent only to qualify (C-39).
- *Commercial clients:* higher prices for plans, rising further over time as grandfathered designers leave (C-18, C-19); fewer alterations (C-23) and so less fit-out work (C-33); more work for architects at higher fees (C-12, C-25); the license tells them something about plan-preparation training (C-26); a dip in projects after the window (C-16); money that would have gone to other uses (C-37).
- *Households:* higher prices for licensed design (C-20), fewer exchanges with the non-degreed designers many of them used (C-24), more use of store design help, online services and their own time (C-11, C-38).
- *Retailers:* stores with design help sell more furnishings and those without sell less (C-31, C-32).
- *Others:* more lobbying by those with a stake (C-17); building departments' added plan checks (C-34); taxpayers fund part of the Board (C-36); the long-run number of designers falls further (C-22).

**Ambiguous effects:** Demand for degree places (more entrants need the degree; the added hours and exam make the route less attractive) (C-8); wages of retail design staff (more demand for store design help; more excluded designers seeking those jobs) (C-30). Whether styling-only services grow or shrink depends on the reading of the definition (C-7).

**Key conditions:** That the requirement binds (A-1, 0.9) and is enforced enough to matter (A-2, 0.7); that some unlicensed residential practice continues (A-3, 0.8); that permit offices reject unstamped plans (A-5, 0.85); and that households have close exempt substitutes (A-10, 0.85). Two new premises were needed: that some commercial projects are at the margin (A-N1, 0.7) and that some excluded designers move to retail design jobs (A-N2, 0.7).

**What this analysis cannot say:** how large any of these changes are; whether the gains to license holders and the information the license conveys outweigh the losses to clients, excluded designers and entrants; whether the policy is good. Health and safety effects of interior design (code, egress, accessibility, fire) are out of scope for version 1 and are not analyzed here.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | sellers.current (interior designers, legal) | number_of_sellers | decrease | short | visible | B | CR-1 op. 1 (unlicensed paid practice removed); CR-2; CR-4b (x: practice, y: exit) for practitioners neither grandfathered nor licensed | A-1, A-2 |
| C-2 | sellers.prospective (would-be designers) | entry_rate | decrease | medium | visible | B | CR-1 op. 3 (degree, 3,500 supervised hours and exam attached to entry); CR-4b (x: enter, y: another occupation) | A-1, A-2 |
| C-3 | designers.licensed | compliance_cost | increase | short | visible | A | CR-1 op. 3 and 4 ($250 annual fee, 12 hours of continuing education, registration paperwork); CR-3a; CR-8c |  |
| C-4 | clients.commercial (permit applicants) | compliance_cost | increase | short | visible | B | CR-1 op. 1 (unstamped plans no longer accepted, K3); CR-3a; CR-8c | A-5 |
| C-5 | designers.excluded (no license, no grandfathering) | informal_activity | increase | short | invisible | B | CR-4b (x: comply, y: violate), mainly residential work; CR-1 op. 3 (complaint-driven enforcement attaches a risk rather than removing the option) | A-1, A-3 |
| C-6 | designers.excluded (no license, no grandfathering) | earnings | decrease | short | invisible | B | CR-3a (chosen option removed or burdened); CR-4b (those who stop fall back to a lower-ranked use of their labor) | A-1, A-2 |
| C-7 | designers.excluded (no license, no grandfathering) | number_of_sellers (unlicensed styling-only services) | U1-a: decrease; U1-b: increase | short | invisible | B | U1-a (styling covered): CR-1 op. 1, CR-4b (x: offer styling, y: stop). U1-b (styling not covered): CR-4b (x: the covered form, y: the uncovered form), reclassifying full design as styling | A-1, A-2 |
| C-8 | sellers.prospective (would-be designers) | quantity_demanded (interior design degree places) | ambiguous | medium | invisible | B | (+) CR-4b (x: enter without a degree, now removed; y: get the degree) for entrants who still want to practice; (+) CR-9 and CR-6 price formation, higher expected earnings of licensed designers (C-21); (-) CR-4b (x: degree route, y: another career), since 3,500 hours and the exam are attached to the degree route; CR-12b | A-1, A-2 |
| C-9 | entrants.graduates | wait_time (from graduation to license) | increase | medium | invisible | B | CR-1 op. 3 (3,500 supervised hours and exam before practice); CR-6 (supervised positions are scarce and allocated by the supervisors' choice among graduates) | A-1, A-15 |
| C-10 | entrants.graduates (in supervised positions) | wage_rate | decrease | medium | invisible | B | CR-5c (supervised hours now bring credit toward the license, so the range of terms a trainee accepts moves down); CR-6 price formation (graduates compete for scarce supervised positions) | A-1, A-15 |
| C-11 | clients.residential | quantity_substitute (store design help, online design services, own work) | increase | medium | invisible | B | CR-4b (x: hire a designer, y: an exempt or unlicensed substitute), after the price of licensed design rises (C-20) | A-10, A-7 |
| C-12 | clients.commercial | quantity_substitute (architects' interior work) | increase | medium | invisible | B | CR-4b (x: licensed interior designer, y: architect, who is exempt and may stamp plans) | A-11, A-5 |
| C-13 | designers.grandfathered | job_changes (temporary exits from the trade) | decrease | long | invisible | B | CR-1 op. 3 (the license lapses if not renewed and cannot be regained without meeting K1); CR-4b (x: leave for a time, y: stay and renew) | A-16 |
| C-14 | designers.grandfathered | compliance_cost | increase | long | invisible | B | CR-4b (x: let the license lapse, y: keep renewing while partly inactive); CR-8c (fees and continuing education kept up only to hold the license) | A-16 |
| C-15 | clients.commercial | quantity_traded (commercial interior design, ten-month announcement window) | increase | short | visible | B | CR-10a; CR-4b (x: start the project after the effective date, y: start it now) | A-8 |
| C-16 | clients.commercial | quantity_traded (commercial interior design, first months after the effective date) | decrease | short | invisible | B | CR-10a (projects moved into the window are not repeated after it); arithmetic | A-8 |
| C-17 | designers.licensed, degree programs, retailers, architects | lobbying_effort | increase | medium | invisible | B | CR-4b (x: accept the rules as written, y: lobby to keep, extend or widen them, or to keep the retail exemption); each now has a concentrated stake | A-9 |
| C-18 | clients.commercial | price_paid (commercial interior design) | increase | medium | invisible | B | CR-4b exits and lower entry (C-1, C-2); CR-6 first paragraph (at the old price planned purchases exceed planned sales, so the price rises); CR-9 (competitors removed); K3 removes unlicensed preparers | A-1, A-2, A-5 |
| C-19 | clients.commercial | price_paid (commercial interior design) | increase | long | invisible | B | CR-10b (the grandfathered stock leaves through exits and is replaced only through the degree route); CR-6 first paragraph | A-1, A-2, A-4, A-5, A-15 |
| C-20 | clients.residential | price_paid (licensed residential design) | increase | medium | invisible | B | CR-4b exits; CR-6 first paragraph; CR-7b (residential clients have close substitutes, so the rise is limited by them; direction only) | A-1, A-2, A-10 |
| C-21 | designers.licensed | earnings | increase | medium | invisible | B | CR-9 (competitors removed); CR-6 first paragraph (C-18); CR-7b (the lasting gain from restricted entry settles on the means that cannot be added to: licenses held when the rule took effect) | A-1, A-2, A-5 |
| C-22 | sellers.current (interior designers, legal) | number_of_sellers | decrease | long | invisible | B | CR-10b (grandfathered designers leave at 3 to 5% a year and the license cannot be regained); CR-4b at entry (C-2); arithmetic against the counterfactual, in which non-degree entrants also replace them | A-1, A-2, A-4 |
| C-23 | clients.commercial | quantity_traded (commercial interior alterations) | decrease | medium | invisible | B | CR-4c (a higher price of plans makes the least valued projects the first given up) after C-18 and C-4 | A-1, A-5, A-N1 |
| C-24 | clients.residential | quantity_traded (residential design by designers, legal) | decrease | medium | invisible | B | CR-5a (exchanges with non-degreed designers that would have taken place are prevented); CR-4c after C-20 | A-1, A-2, A-6 |
| C-25 | architects | price_substitute (architects' interior design fees) | increase | medium | invisible | B | CR-9 (demand for a competing good moves with the target's price); CR-6 first paragraph in the architects' market | A-1, A-11 |
| C-26 | clients.commercial | quality_information | increase | medium | invisible | B | CR-11c (the license conveys that its holder was trained in code, egress, accessibility and plan preparation) | A-13 |
| C-27 | clients.residential (using unlicensed designers) | quality_information | decrease | medium | invisible | B | CR-11b (unlicensed designers cannot advertise openly, build public reputations or use the courts) | A-3 |
| C-28 | clients.residential (using unlicensed designers) | disputes_settled_outside_courts | increase | medium | invisible | B | CR-11b; CR-1 op. 3 (K4 makes contracts for unlicensed practice unenforceable) | A-3 |
| C-29 | retail_design_staff | employment | increase | medium | invisible | B | CR-7a (excluded designers move their labor to the exempt use); CR-9 (demand for store design help rises with C-11) | A-7, A-10, A-N2 |
| C-30 | retail_design_staff | wage_rate | ambiguous | medium | invisible | B | (+) CR-9, LW-10 (demand for store design help rises, so demand for the labor that provides it rises); (-) CR-7a (added labor from excluded designers lowers the yield of that use); CR-12b | A-7, A-10, A-N2 |
| C-31 | retailers.with_design_help | quantity_traded (furnishings sold by stores with design help) | increase | medium | invisible | B | CR-9 (households who take a store's design help buy most furnishings from it); after C-11 | A-7, A-10, A-12 |
| C-32 | furniture_stores.without_design_help | quantity_traded (furnishings) | decrease | medium | invisible | B | CR-9 (competitors of the stores in C-31 lose the sales that move to them) | A-7, A-10, A-12 |
| C-33 | sellers.complements (fit-out contractors) | quantity_complement (commercial fit-out work) | decrease | medium | invisible | B | CR-9, LW-10 (demand for fit-out work follows the number of alterations, C-23) | A-1, A-5, A-N1 |
| C-34 | officials.building_departments | enforcement_cost | increase | short | invisible | B | CR-1 op. 3 (stamp check added to plan review); CR-8c | A-5 |
| C-35 | officials.enforcement (State Board) | enforcement_cost | increase | short | visible | A | CR-8c (Board staff, investigations and hearings); K4 |  |
| C-36 | taxpayers | resources_available_other_uses | decrease | short | invisible | A | CR-8a, CR-8b (the general-budget share of the Board's cost is withdrawn from other uses) |  |
| C-37 | clients.commercial | resources_available_other_uses | decrease | medium | invisible | B | CR-8b (the higher fees counted as designers' gain in C-21 are the clients' matching outlay); CR-3a | A-1, A-2, A-5 |
| C-38 | clients.residential | resources_available_other_uses | decrease | medium | invisible | B | CR-3a (fallback to a lower-ranked substitute or own work); CR-8b (higher fees); CR-8c (own time spent on design) | A-1, A-2, A-10 |
| C-39 | entrants.graduates | resources_available_other_uses | decrease | medium | invisible | B | CR-8c (exam fee, study time and supervised hours spent only to qualify); CR-3c | A-1 |

## Gaps found

**(a) Calculus gaps.** None. Every step was derived from CR-1 to CR-12, LW-10 and arithmetic.

**(b) New premises.**
- A-N1 (some commercial projects at the margin, p 0.7): CR-4c gives the direction of the response to a higher price of plans a priori, but whether any project is actually given up is the empirical margin premise CR-4 names; none of the case assumptions covers commercial clients' project decisions, and the fit-out chain depends on it.
- A-N2 (excluded designers move to retail design jobs, p 0.7): A-7 says the retail exemption can be used, not that excluded designers will take such jobs; CR-7a needs the mobility premise to put labor into that use.

**(c) Unclear core rules.**
- CR-7b and CR-7c: the gain from restricted entry settles on license holders, but the license cannot be sold, so CR-7c's "price of a durable asset" has no market price here. The analysis recorded the gain as `earnings` rather than `asset_value`; CR-7 does not say how to record capitalization into a non-transferable right.
- CR-6: its first paragraph (price formation) was used for a price that is free to move after supply falls, while its second part (displaced pressure) applies only where a price is held fixed. Using CR-6 as the general rule for price rises after an entry restriction is a reading, not an explicit statement; a sentence saying that CR-6's first paragraph covers any change in planned sales would settle it.
- CR-5c for supervised positions: the trainee's lower money wage follows from CR-5c only if the supervised hours are treated as part of what the trainee "may receive"; the rule does not say that a non-money benefit counts as part of the terms.
