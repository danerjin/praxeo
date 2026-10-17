# WE-059 / Analysis: Right to repair for farm equipment and phones

Analyst: core-only re-run (Handbook 1.0)  |  Rules: core rules CR-1 to CR-12 only  |  Status: compared

## 1. Policy record

**Kestrava Fair Repair Act.** Kestrava is a state of about 6.2 million. To its west lies Darnholt, which has no such law; about 3,000 Kestrava farms lie within 30 km of the state line, and six farm equipment dealers operate on the Darnholt side within 30 km of it. Similar bills were introduced in Kestrava in 2023 and 2025 and failed after campaigns on both sides.

**Phones.** About 5.4 million phones are in use in Kestrava and about 1.9 million are sold a year (about 60% online, delivered to Kestrava addresses); three makers sell about 90% of them, at the same prices in every state. About 1.1 million phone repairs are made a year: about 60% by makers' stores and authorized providers (a screen repair with a genuine part costs about $280), about 40% by some 900 independent shops using non-genuine or salvaged parts (about $160). On recent models makers pair screens, batteries and cameras to the device: a replacement part not paired by the maker's server works with warnings (battery health hidden, "unknown part" notices) or with some features disabled (face unlock). One maker already sells genuine parts and rents tools to owners in all states at the prices its authorized providers pay, and pairs the part through its server after the repair. About 40,000 phones are reported stolen in Kestrava each year; activation locks and parts pairing now keep most parts of reported phones from working in other devices.

**Farm equipment.** About 38,000 farms run about 95,000 tractors and 12,000 combines with electronic controls; about 30% of the tractors were sold on or after 1 January 2023. Four makers sell through 140 authorized dealer locations, which are independent businesses under dealer agreements; about 260 independent shops repair farm equipment. Dealers' service revenue is about $520 million a year ($330 million parts, $190 million labor at about $165 an hour; independents charge about $95). Dealers subscribe to each maker's diagnostic software (about $8,000 a year per location) and buy parts at 25% below list. Independents can buy many mechanical parts at list from dealers but cannot buy the software, without which many electronic parts cannot be calibrated or paired. Farm surveys put the average wait for a dealer technician at harvest at 2.5 days. New equipment sales in Kestrava are about $1.1 billion a year; 14 specialty models sell fewer than 20 units a year each in the state.

**Timing.** The bill passed the legislature on 18 February 2027 and was signed on 1 March 2027; it takes effect on 1 September 2028 (18 months). No expiry.

| Field | Value | Source sentence |
|---|---|---|
| Jurisdiction (and what lies just outside) | Covered equipment sold or leased to a purchaser in Kestrava. Just outside: Darnholt (no law), with dealers near the line; phones are sold nationally at one price. | §2(b): "'Covered equipment' means a mobile phone, or agricultural equipment designed primarily for agricultural use and containing electronic controls, sold or leased to a purchaser in Kestrava on or after 1 January 2023." |
| Announced / enacted / effective / expires | Passed 18 February 2027; signed 1 March 2027; effective 1 September 2028; no expiry. | §9. |
| Enforcement (who, penalties, resources) | Attorney General under the Unfair Trade Practices Act, on complaint; civil penalty up to $10,000 per violation; no private right of action. No new appropriation: the Consumer Protection Division's budget (about $14 million, about 22,000 complaints a year) is unchanged. | §8. |

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Duty to supply | `mandated_contract_term` (a term of every sale of covered equipment, owed to the owner and to any independent repair provider) | Parts, tools, documentation and diagnostic software, including the means to reset, calibrate and pair parts | Makers of covered equipment | "On fair and reasonable terms", defined in §2(d) as "terms, including price, no less favorable than the most favorable terms on which the manufacturer offers the item to an authorized repair provider, net of any discount, rebate or incentive." | Parts no longer made; information not given to authorized providers. |
| K2 Void terms | `term_prohibition` | Terms in contracts for the sale, lease or license of covered equipment (including software licenses) that prohibit or restrict repair by the owner or a person of the owner's choice, or that void a warranty because of such repair | Makers, dealers, lessors; existing and new contracts, from 1 September 2028 | "Any such term is void." A warranty may still exclude damage caused by the repair itself (§4(b)). | — |
| K3 Software locks | `product_standard` (a rule on the software of covered equipment) | Software that pairs parts to a device | Makers | §5(c): "A manufacturer shall not use a software lock to prevent the functioning of a part supplied, repaired or replaced in accordance with this Act." | — |
| K4 Enforcement | Enforcement | K1 to K3 | Attorney General, on complaint, from an unchanged budget | Penalty up to $10,000 per violation. | — |

The counterfactual law, which K1 to K3 change: a maker may refuse to sell parts, tools and software to anyone but its authorized repairers; contract and license terms restricting repair are enforceable; parts pairing is lawful.

Unclear provisions:
- **U1, parts pairing.** §5(c) forbids "a software lock to prevent the functioning of a part supplied, repaired or replaced in accordance with this Act". §2(f): "'Software lock' means any technical measure that restricts the functioning of a part unless the manufacturer authorizes it." §3(a)(iv) lists among what makers must supply "the means to pair a part to the equipment". Reading U1-a: pairing that needs the maker's authorization is itself the lock §5(c) forbids; any part installed, genuine, salvaged or non-genuine, must work fully without contacting the maker, and makers must remove pairing from covered devices and leave it out of new ones. Reading U1-b: §3(a)(iv) presupposes that pairing continues; a lock is lawful if the owner (or a repairer acting for the owner) can pair a genuine part using a tool the maker supplies on fair and reasonable terms. Makers may then refuse to pair parts reported stolen and need not pair non-genuine parts. The Attorney General has issued no guidance.

Readings get no probability; where a sign depends on U1, one sign per reading is given.

**Figures.** If independents' share of phone repairs and their prices stayed as they are, and dealers' farm service revenue fell by a fifth, about $100 million a year of dealer service would move to independents and owners. The maker's existing national phone program already matches K1 on price and meets U1-b's pairing condition. Phones in use are replaced about every three years, so by 2030 nearly all phones in use will be covered; about 70% of tractors in use were sold before 2023 and are not covered, and tractors last 15 to 25 years.

## 2. Classification

The counterfactual law (stated in the record): makers may refuse to sell parts, tools and software to anyone but authorized repairers; anti-repair contract and license terms are enforceable; parts pairing is lawful.

| Component | Rothbard type | Binding? (assumption ID) | CR-1 operations | Core rules applied |
| --- | --- | --- | --- | --- |
| K1 Duty to supply | triangular (forces exchanges between makers and owners or independents on set terms) | Yes for makers who did not offer such terms (A-2), where they comply (A-1); not for the phone maker whose programme already matches | For owners and independents: 2 (an option to buy inputs on authorized terms). For makers: 3 (a duty attached to selling covered equipment); 1 (the option of refusing is removed) | CR-4, CR-5b, CR-5c, CR-6, CR-7b, CR-9, CR-10a |
| K2 Void terms | triangular | Yes where such terms were in use (A-2) | 1 for makers, dealers and lessors (the option of agreeing on, or enforcing, the term); 2 for owners (repair by a person of their choice without losing the warranty); a transfer of the contract right (CR-8 0.7) | CR-1, CR-7c, CR-8b |
| K3 Software locks | triangular (product standard) | Per reading: U1-a removes authorization-based pairing; U1-b allows it if the tool is supplied on fair terms | U1-a: 1 (pairing that needs authorization); U1-b: 3 (pairing must be open through a tool) | CR-1 per reading, CR-4, CR-11 |
| K4 Enforcement | enforcement on complaint | Partial (A-10) | 3 (a risk of penalty up to $10,000 per violation attached to failing to comply) | CR-4 (x: comply, y: violate), CR-6 0.7, CR-8a |

Coverage is by date of sale (on or after 1 January 2023), so for farm equipment the Act binds on about 30% of tractors now and grows as the fleet turns over; for phones nearly all in use are covered by 2030.

## 3. Actor classes

| Actor class | Role | How its options change (CR-1) |
| --- | --- | --- |
| owners.covered_equipment (farm and phone) | About 38,000 farms, 5.4 million phones | Op 2: buy inputs, use independents or repair themselves without losing the warranty. |
| owners.farm_uncovered | Pre-2023 equipment | No operation; through CR-9 (shared repair capacity, substitute equipment). |
| makers.farm, makers.phone | Four farm makers, three phone makers | Op 1 and op 3: must supply on authorized terms; anti-repair terms void; locks restricted (per reading). |
| dealers.farm, authorized_providers.phone | 140 dealer locations; authorized phone repairers | Op 1 (K2 voids their anti-repair terms); through CR-9 they lose service and retail parts business. |
| independents.farm, independents.phone | About 260 and 900 shops | Op 2: buy software, parts and pairing on authorized terms. |
| sellers.prospective (independent shops) | Would-be entrants | Entry made better (CR-4). |
| input_suppliers (repair technicians) | Labor | Through CR-9 (input_to). |
| sellers.substitutes (non-genuine and salvaged parts) | Parts used by independents now | Through CR-9; under U1-a their parts work fully. |
| buyers.used_phones | Buy phones second-hand | Through CR-11 (notices), per reading. |
| informal sellers (stolen phones) | Thieves and their buyers | Under U1-a stolen parts work. |
| buyers.current (new equipment and phones) | Buyers of new covered goods | Through CR-5c (makers' terms) and the value of repair access. |
| farms.near_border, neighboring_jurisdictions (Darnholt dealers) | Six dealers within 30 km of the line | Through CR-4 (relocation of purchases). |
| buyers.foreign (phone owners in other states) | Same national phone market | Through CR-9 if makers extend programmes (A-8). |
| investors | Holders of makers' shares | Through CR-7c. |
| officials.attorney_general, complainants.other | Enforcement on complaint; other consumer complainants | Op 3 (new duties, unchanged budget); through CR-8a. |

## 4. Direct effect

CR-1 and CR-2: what K1 to K3 change at once for owners, independents and makers, against the counterfactual law.

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-1 | independents.farm | price_paid (diagnostic software, electronic parts and documentation) | decrease | medium; long (from 1 September 2028) | CR-1 | A-1, A-2 |
| C-2 | independents.phone, owners.phone | price_paid (genuine parts, tools and pairing) | decrease | medium; long | CR-1 | A-1, A-2 |
| C-3 | owners.covered_equipment (farm and phone) | term_prevalence (enforceable anti-repair and warranty-voiding terms) | decrease | short (from 1 September 2028) | CR-1 | A-2 |
| C-4 | makers.farm, makers.phone | compliance_cost | increase | short; medium; long | CR-1, CR-8c | - |
| C-5 | makers.phone | product_attribute (parts pairing that needs the maker's authorization, in covered phones) | U1-a: decrease; U1-b: no_change | medium | CR-1 | A-1 |
| C-6 | owners.covered_equipment (farm and phone) | asset_value (covered equipment) | increase | short (from passage, February 2027) | CR-8, CR-10c, CR-7c | A-1, A-3, A-20 |

## 5. Responses

CR-4 for every pair of options: dealer against independent or self repair (C-7, C-8); stay out against enter (C-11); repair now against defer (C-13, C-14); covered against uncovered form (C-15); offer against drop a model (C-16); modular against integrated design (C-17); comply against offer less (C-23); accept against lobby (C-22); buy here against across the line (C-21). CR-6 for dealer service with fixed capacity (C-10); CR-5c for makers' other terms of sale (C-18, C-19).

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-7 | owners.covered_equipment (farm and phone) | quantity_traded (repairs by independent shops) | increase | medium; long | CR-4, CR-4a | A-1, A-3, A-5 |
| C-8 | owners.covered_equipment (farm and phone) | home_production (self repair) | increase | medium; long | CR-4, CR-1 | A-1, A-3, A-16 |
| C-9 | dealers.farm, authorized_providers.phone | quantity_traded (repair service) | decrease | medium; long | CR-9, CR-4 | A-1, A-3 |
| C-10 | dealers.farm, authorized_providers.phone | net_price_received (repair service), wait_time (at dealers, for their customers) | at_least_one_decrease | medium | CR-6 | A-1, A-3, A-4 |
| C-11 | sellers.prospective (independent repair shops) | entry_rate | increase | medium | CR-4, CR-7a | A-1, A-3, A-5 |
| C-12 | independents.farm, independents.phone | investment_target (tools, software subscriptions, training before 1 September 2028) | increase | short (March 2027 to August 2028) | CR-10a, CR-4 | A-5, A-20 |
| C-13 | owners.covered_equipment (farm and phone) | quantity_traded (repairs at dealers and authorized providers, March 2027 to August 2028) | decrease | short (window before the effective date) | CR-10a, CR-4, CR-12h | A-7, A-3 |
| C-14 | owners.covered_equipment (farm and phone) | quantity_traded (repairs, all providers, from September 2028) | increase | medium | CR-10a, CR-4c | A-7, A-3, A-1 |
| C-15 | makers.farm | reclassification (compact tractors designed and marketed for grounds care) | increase | medium; long | CR-4 | A-6, A-9 |
| C-16 | makers.farm | variety (specialty farm models offered in Kestrava) | decrease | medium; long | CR-4 | A-11 |
| C-17 | makers.farm, makers.phone | product_attribute (integration of components; under U1-b, pairing of more parts) | increase | long | CR-4, CR-10b | A-24 |
| C-18 | makers.farm | price_paid (new covered farm equipment in Kestrava) | increase | medium; long | CR-5c, CR-9, LW-10 | A-6, A-18 |
| C-19 | buyers.current (phone buyers in all states) | price_paid (new phones) | increase | medium; long | CR-5c, CR-6 | A-6, A-19 |
| C-20 | buyers.current (farms buying new covered equipment in Kestrava) | quantity_traded (new covered farm equipment) | ambiguous | medium; long | CR-12b, CR-4c, CR-4 | A-6, A-18, A-22 |
| C-21 | farms.near_border (about 3,000 within 30 km), neighboring_jurisdictions (six Darnholt dealers) | cross_border_purchases (new farm equipment bought in Darnholt) | ambiguous | medium; long | CR-4 | A-18, A-22 |
| C-22 | makers, dealers, farm groups, repair associations | lobbying_effort (over the reading of U1, the scope of K1, and enforcement) | increase | short; medium | CR-4, CR-12, CR-8c | A-23 |
| C-23 | makers.farm, makers.phone | legal_breach (offers short of fair and reasonable terms) | increase | medium; long | CR-4, CR-12 | A-10 |

## 6. Second-order effects

CR-9 along named relations, then CR-5 to CR-7 in each market reached. Depth limit 4. Safety effects of self repair, and the value of data security, are outside version-1 variables; theft is recorded only as informal trade (C-38).

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C-24 | owners.covered_equipment (farm and phone) | full_cost_per_unit (repair of covered equipment) | decrease | medium | CR-4, CR-2, CR-9 | independent and self repair substitute for dealer repair (close) | A-1, A-3, A-14 |
| C-25 | owners.covered_equipment (farm and phone) | full_cost_per_unit (repair of new covered models) | ambiguous | long | CR-12b, CR-12 | as C-24 | A-1, A-3, A-24 |
| C-26 | owners.farm (covered and uncovered equipment) | wait_time (repair at harvest) | decrease | medium | CR-9 | independent repair substitute for dealer repair; dealer capacity shared by covered and uncovered owners (same_market_other_segment) | A-1, A-3, A-14 |
| C-27 | dealers.farm | asset_value (dealerships) | decrease | short (from passage, February 2027) | CR-7c, CR-10c, CR-7b | - | A-3, A-19, A-20 |
| C-28 | dealers.farm (relative to makers) | tax_share_borne (share of the Act's burden on the supply side) | increase | medium; long | CR-7b | dealer agreement (contract) | A-6, A-19 |
| C-29 | dealers.farm | quantity_traded (parts sold at retail to owners and independents) | decrease | medium; long | CR-9, CR-4 | maker supply substitute for dealer retail parts (close) | A-1, A-2 |
| C-30 | investors (holders of makers' shares) | asset_value (makers' shares) | decrease | short (from passage) | CR-7c, CR-10c | - | A-12, A-20, A-6 |
| C-31 | sellers.current (independent repair shops) | asset_value (shops) | increase | short (from passage) | CR-7c, CR-10c, CR-7a | - | A-1, A-3, A-20 |
| C-32 | input_suppliers (repair technicians) | employment (independent shops), employment (dealers and authorized providers) | at_least_one_as_stated | medium | CR-9, LW-10, CR-7a | technician labor input_to repair (close) | A-1, A-3, A-5 |
| C-33 | complainants.other (consumers with other unfair-practice complaints) | wait_time (handling of complaints), quality_per_unit (attention per complaint) | at_least_one_as_stated | medium | CR-8a, CR-6 | shared enforcement budget (same_market_other_segment) | A-10, A-N1 |
| C-34 | owners, independents (complainants) | applications (complaints to the Attorney General under the Act) | increase | medium | CR-4, CR-12 | - | A-10 |
| C-35 | makers.phone (genuine parts sales) | quantity_traded (genuine phone parts) | U1-a: ambiguous; U1-b: increase | medium | CR-9, LW-10, CR-4, CR-12b | genuine parts input_to repair; non-genuine parts substitute (partial) | A-1, A-3, A-21 |
| C-36 | sellers.substitutes (non-genuine and salvaged phone parts) | quantity_traded | ambiguous | medium | CR-12b | non-genuine parts substitute for genuine parts (partial) | A-1, A-3, A-21 |
| C-37 | independents.phone | quality_per_unit (repairs) | increase | medium | CR-1, CR-4 | - | A-1 |
| C-38 | informal sellers (thieves and buyers of stolen phones) | informal_activity (trade in stolen phones and their parts) | U1-a: increase; U1-b: no_change | medium | CR-4, CR-1 | stolen parts substitute for genuine parts (partial) | A-17 |
| C-39 | buyers.used_phones | quality_information (whether a used phone has non-genuine parts) | U1-a: decrease; U1-b: no_change | medium | CR-11 | - | A-15 |
| C-40 | owners.farm_uncovered (pre-2023 equipment, about 70% of tractors) | asset_value (equipment) | ambiguous | short (from passage) | CR-12b, CR-9 | covered equipment substitute for uncovered (close); same repair capacity | A-3, A-4, A-5, A-20 |
| C-41 | buyers.foreign (phone owners and independents in other states) | quantity_traded (genuine parts and tools bought outside Kestrava) | increase | medium | CR-9, CR-4, CR-1 | same national phone market (same_market_other_segment) | A-8 |

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance premise | Combined sign |
| --- | --- | --- | --- | --- |
| owners, full_cost_per_unit (repair), medium | - | access to inputs; shorter waits | - | decrease (C-24) |
| owners, full_cost_per_unit (repair of new models), long | integration and wider pairing (A-24) | access to inputs | none | ambiguous (C-25) |
| buyers of new farm equipment, quantity_traded | value of repair access (A-22) | higher price (A-6, A-18) | none | ambiguous (C-20) |
| farms near the line, cross_border_purchases | price gap (A-18) | loss of coverage, if purchases in Darnholt are not covered (A-22) | none | ambiguous (C-21) |
| makers.farm, price_paid (new equipment) | cost recovery (A-6, A-18); higher demand (A-22) | - | - | increase (C-18) |
| uncovered equipment, asset_value | more repairers, shorter waits | covered equipment worth more (substitute) | none | ambiguous (C-40) |
| genuine phone parts, quantity_traded | more repairs; U1-b switch from non-genuine | U1-a: non-genuine parts work fully | per reading | U1-a: ambiguous; U1-b: increase (C-35) |
| non-genuine parts, quantity_traded | more independent repair; U1-a full function | genuine parts available | none | ambiguous (C-36) |
| technicians, employment | independents | dealers | different items, not netted (CR-12c, 0.8 two items) | at_least_one_as_stated (C-32) |
| repairs at dealers, timing | from Sep 2028 (C-14) | window before (C-13) | different windows (CR-12g, h) | per window |
| makers' shares, asset_value | partial recovery through prices (A-6) | lost margins (A-12) | A-19: phone prices are national, so recovery from Kestrava buyers is spread; recovery is not full | decrease (C-30) |

The term_prevalence fall (C-3) and the owners' gain of the right (C-6) are two sides of one transfer (CR-8b), recorded on both sides, not netted.

## 8. Time structure

- **Horizons.** Short: passage (18 February 2027) to the effective date (1 September 2028). Medium: the first years after it. Long: as the covered share of the farm fleet grows (tractors last 15 to 25 years) and makers redesign.
- **Announcement.** From passage, the Act is expected (A-20): dealer values and makers' shares fall and independent shops gain value (C-27, C-30, C-31); owners' covered equipment gains (C-6). Earlier failed bills (2023, 2025) mean part of this may have been priced before as a probability (CR-7c).
- **Window before the effective date.** Repairs that can wait are deferred (C-13), then made (C-14); independents invest ahead (C-12).
- **Dealer capacity.** Dealers cannot contract at once (A-4): first prices or waits at dealers fall (C-10); later dealer employment falls (C-32).
- **Fleet turnover.** For phones the Act soon covers nearly every device. For farm equipment the covered share starts near 30% of tractors and grows; the effects on owners, dealers and independents grow with it (CR-10b).
- **Redesign.** New designs integrate components or pair more parts (C-17), which arrive only with new models and make the long-run repair cost ambiguous (C-25).
- **Persistence.** No expiry; the Act is not a repeal, so no metamorphic check is needed.

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
| --- | --- | --- | --- | --- | --- |
| C-4 | makers.farm, makers.phone | compliance_cost | increase | Staff, documentation, tool and software support that would have served other ends | CR-1, CR-8c |
| C-9 | dealers.farm, authorized_providers.phone | quantity_traded (repair service) | decrease | Service sales lost to independents and self repair | CR-9, CR-5a note (the seller who loses the sale loses; the buyer does not) |
| C-16 | buyers of specialty models | variety | decrease | Specialty models no longer offered in Kestrava | CR-4 0.7 |
| C-19 | phone buyers in all states | price_paid | increase | Part of makers' cost of the Act, paid in the price of new phones | CR-5c, CR-8b |
| C-22 | makers, dealers, farm groups, repair associations | lobbying_effort | increase | Time and money spent on the Act's reading and enforcement | CR-4, CR-8c |
| C-33 | complainants.other | wait_time, quality_per_unit | at_least_one_as_stated | Attention to other consumer complaints | CR-8a, CR-6 |

CR-8b: the margin dealers and makers lose on repair inputs (C-9, C-29, C-30) is matched by lower prices to owners and independents (C-1, C-2, C-24), less what makers recover from buyers of new equipment and phones (C-18, C-19). The voided contract right (C-3) is a transfer to owners (C-6).

## 10. Assumptions

Case assumptions as given (same IDs and p); one added premise (A-N1) flagged NEW.

| ID | Statement | Type | p | Evidence | If false |
| --- | --- | --- | --- | --- | --- |
| A-1 | Most makers comply with K1 in most cases. | enforcement | 0.7 | Penalty up to $10,000 per violation; reputational cost; organized complainants. | These consequences fail or lose this chain: C-1, C-2, C-5, C-6, C-7, C-8, C-9, C-10, C-11, C-14, C-24, C-25, C-26, C-29, C-31, C-32, C-35, C-36, C-37. |
| A-2 | Before the Act, makers did not offer independents and owners genuine parts, tools and software on the terms they gave authorized repairers (except one phone maker's national program, which matches on price and meets U1-b), and anti-repair terms were in use. | binding | 0.9 | Dealer agreements; independents' complaints; the existing program. | These consequences fail or lose this chain: C-1, C-2, C-3, C-29. |
| A-3 | Some owners prefer independent or self repair at the new terms. | substitutability | 0.9 | Labor rates of $95 against $165; distance to dealers; farmers' skills; 40% of phone repairs already independent. | These consequences fail or lose this chain: C-6, C-7, C-8, C-9, C-10, C-11, C-13, C-14, C-24, C-25, C-26, C-27, C-31, C-32, C-35, C-36, C-40. |
| A-4 | Dealers' and authorized providers' repair capacity cannot contract at once. | durability | 0.75 | Technicians on staff; bays and equipment. | These consequences fail or lose this chain: C-10, C-40. |
| A-5 | Independent shops can open or expand once inputs are available. | mobility | 0.75 | 260 farm and 900 phone independents; technicians trained by dealers. | These consequences fail or lose this chain: C-7, C-11, C-12, C-32, C-40. |
| A-6 | Makers bear costs from K1 and K2 (margin on repair inputs, supply and support) and seek to recover them through other terms of sale. | other | 0.85 | Dealer service margins; makers' statements. | These consequences fail or lose this chain: C-15, C-18, C-19, C-20, C-28, C-30. |
| A-7 | Some repairs can be deferred for months. | other | 0.6 | Share of phone repairs for cosmetic damage; off-season farm work. | These consequences fail or lose this chain: C-13, C-14. |
| A-8 | Phone makers extend their parts and tool programs to owners in all states rather than only Kestrava. | other | 0.6 | One maker already runs a national program; costs of checking where a phone was sold. | These consequences fail or lose this chain: C-41. |
| A-9 | Some compact tractors can be designed and marketed for grounds care at a cost below the burden of coverage. | other | 0.55 | Dual-use models; definitions in other laws. | These consequences fail or lose this chain: C-15. |
| A-10 | The Attorney General acts only on complaint, and some makers' offers fall short. | enforcement | 0.7 | §8; the Division's caseload. | These consequences fail or lose this chain: C-23, C-33, C-34. |
| A-11 | For some specialty farm models with fewer than 20 sales a year in Kestrava, the cost of supplying documentation, tools and software for the model there exceeds the margin on those sales. | other | 0.5 | 14 such models; makers' cost of per-model support. | These consequences fail or lose this chain: C-16. |
| A-12 | Investors value makers' expected repair-input margins in Kestrava. | other | 0.85 | Aftermarket shares of makers' profits. | These consequences fail or lose this chain: C-30. |
| A-13 | In the long run independent repair capacity can be added at roughly constant cost. | other | 0.6 | Premises, tools and training available. | No reported consequence rests on it alone. |
| A-14 | More repairers and self-repair shorten waits at harvest. | other | 0.75 | Survey: 2.5 days' average wait for a dealer technician. | These consequences fail or lose this chain: C-24, C-26. |
| A-15 | Some buyers of used phones check the part notices and pay less for phones with unpaired parts. | other | 0.6 | Used-phone dealers' grading practice. | These consequences fail or lose this chain: C-39. |
| A-16 | Owners could not read fault codes or documentation before, and some use them to diagnose or to shop for repairs. | other | 0.85 | Dealer-only software; farm surveys. | These consequences fail or lose this chain: C-8. |
| A-17 | Pairing and activation locks now keep most parts of reported stolen phones from working in other devices; under U1-a they would work. | other | 0.65 | Makers' theft data; resale prices of locked phones. | These consequences fail or lose this chain: C-38. |
| A-18 | Farm equipment makers raise list prices in Kestrava relative to Darnholt. | other | 0.55 | Regional pricing by dealers; makers' cost recovery. | These consequences fail or lose this chain: C-18, C-20, C-21. |
| A-19 | Dealers' capital and locations are tied to their territory, while makers sell in many states at national prices. | mobility | 0.75 | Dealer agreements; makers' pricing. | These consequences fail or lose this chain: C-19, C-27, C-28. |
| A-20 | Makers, dealers and investors expect the Act to stay in force. | expectations | 0.8 | No sunset; similar laws spreading. | These consequences fail or lose this chain: C-6, C-12, C-27, C-30, C-31, C-40. |
| A-21 | Salvaged and non-genuine parts compete with makers' genuine parts once independents can buy both. | substitutability | 0.6 | Independents' current use of salvaged parts; price gaps. | These consequences fail or lose this chain: C-35, C-36. |
| A-22 | Buyers of new covered equipment value access to repair inputs. | other | 0.7 | Farm surveys on repair access; buyers' stated reasons. | These consequences fail or lose this chain: C-20, C-21. |
| A-23 | Makers, dealers, farm groups and repair associations can organize at a cost below their stakes. | other | 0.85 | Campaigns on the 2023 and 2025 bills. | These consequences fail or lose this chain: C-22. |
| A-24 | Some makers respond by integrating components or (under U1-b) by pairing more parts, to keep control of which parts work. | other | 0.55 | Design trends; makers' statements on security and quality. | These consequences fail or lose this chain: C-17, C-25. |
| A-N1 | The Consumer Protection Division has no spare capacity: complaints under the Act take staff time from other complaints. | other | 0.6 | NEW. About 22,000 complaints a year on a $14 million budget, unchanged; no new appropriation (§8). Needed for C-33. | These consequences fail or lose this chain: C-33. |

**Not reported** (an assumption below 0.5): none. All case assumptions have p of at least 0.5; A-11 (0.5) is at the cut-off and C-16 is reported.

### Final check before the report

1. *Uncombined chains.* Repair cost (long), new equipment purchases, cross-border purchases, uncovered equipment values and parts markets are combined in section 7 and are ambiguous where chains oppose without a premise; makers' share value uses A-19 as an empirical dominance premise.
2. *Group signs.* Dealer price or waiting (C-10); technicians' employment (C-32); other complainants (C-33).
3. *Baseline.* Every sign is against the counterfactual law in section 2, not against the one maker's national programme (which is part of the counterfactual and accounts for the class signs resting on the other makers).
4. *Worse off is not poorer.* No `resources_available_other_uses` is signed: owners who switch repair choose to; no class pays an unavoidable sum.
5. *Timing shifts.* Deferred repairs signed per window (C-13, C-14); investment before the date is an increase in its window (C-12).
6. *Both sides of every transfer.* Voided terms (C-3, C-6); repair-input margins (C-9, C-29, C-30 against C-1, C-2, C-24); recovery (C-18, C-19).
7. *Every class, every core rule.* CR-4 for each class's pairs; CR-6 for dealer service and the Attorney General's fixed budget; CR-7c for owners, dealers, independents, investors, uncovered owners; CR-9 along substitute, input, contract, cross-border and national-market relations.
8. *Unstated premises.* Added A-N1 for displaced complaint handling; lobbying uses A-23; responses use A-3, A-5, A-7, A-9, A-11, A-24.
9. *Pattern baselines.* No patterns cited.

## 11. Report

**The policy:** From 1 September 2028, makers of phones and of electronic farm equipment sold in Kestrava from 2023 must sell parts, tools, documentation and diagnostic software to owners and independent repairers on terms no worse than they give their authorized repairers; contract terms that restrict repair, or void a warranty for it, are void; and makers may not use software locks to stop repaired parts working. Whether parts pairing as such is forbidden (U1-a) or allowed when owners can pair genuine parts with a supplied tool (U1-b) is unsettled. The Attorney General enforces on complaint, with no new budget.

**Visible consequences:** Independents pay less for, or can now buy, the inputs they need (C-1, C-2); anti-repair terms lose force (C-3); makers bear compliance costs (C-4) and, under U1-a, remove pairing (C-5). More repairs go to independents and dealers do fewer (C-7, C-9). Farm equipment costs more in Kestrava (C-18).

**Invisible consequences:**
- *Owners:* covered equipment is worth more (C-6); more self repair (C-8); repair costs less and waits at harvest are shorter in the medium run (C-24, C-26); repairs are deferred before the start date and made after it (C-13, C-14).
- *Dealers and authorized providers:* lower prices or shorter queues (C-10), lost retail parts sales (C-29), lower dealership values (C-27), and a larger share of the burden than makers (C-28).
- *Independents:* entry and investment before the date (C-11, C-12); higher shop values (C-31); better phone repairs (C-37).
- *Makers and investors:* compact tractors reshaped as grounds-care machines (C-15); fewer specialty models in Kestrava (C-16); more integrated designs (C-17); phone prices slightly higher everywhere (C-19); lower share values (C-30); some offers fall short of the Act (C-23); both sides lobby over its reading (C-22).
- *Others:* technicians move from dealers to independents (C-32); more complaints (C-34) take the Division's time from other complainants (C-33); under U1-a stolen phones' parts become worth more (C-38) and used-phone buyers lose the part notices (C-39); owners in other states gain access if makers extend programmes (C-41).

**Ambiguous effects:** Long-run repair cost of new models (C-25): access against integration. New farm equipment bought in Kestrava (C-20) and purchases across the line (C-21). Value of uncovered equipment (C-40). Phone parts markets (C-35 under U1-a, C-36).

**Key conditions:** Makers mostly comply (A-1, 0.7); owners prefer independent or self repair at the new terms (A-3, 0.9); independents can expand (A-5, 0.75); makers recover costs through other terms (A-6, 0.85) and dealers are less mobile than makers (A-19, 0.75); makers redesign (A-24, 0.55). Added premise: the Division has no spare capacity (A-N1, 0.6).

**What this analysis cannot say:** How much repair moves or prices fall, whether owners gain more than makers and dealers lose, or whether the Act is good. Safety, security and environmental effects (self-repair injuries, data security, e-waste) are out of scope; theft is recorded only as informal trade.

## Consequence list (normal form)


| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C-1 | independents.farm | price_paid (diagnostic software, electronic parts and documentation) | decrease | medium; long (from 1 September 2028) | visible | B | CR-1 (op 2: K1 adds the option of buying the software, which was not sold to them; op 3: parts at the terms given to dealers, 25% below list, instead of list); against the counterfactual law under which makers may refuse (A-2); A-1 (most makers comply) | A-1, A-2 |
| C-2 | independents.phone, owners.phone | price_paid (genuine parts, tools and pairing) | decrease | medium; long | visible | B | CR-1 (op 2 and op 3: K1 offers genuine parts and tools at authorized-provider terms; for the maker whose national programme already matches, no change, so the class sign rests on the other makers, A-2); A-1 | A-1, A-2 |
| C-3 | owners.covered_equipment (farm and phone) | term_prevalence (enforceable anti-repair and warranty-voiding terms) | decrease | short (from 1 September 2028) | visible | B | CR-1 (op 1: K2 voids, in existing and new contracts, terms restricting repair or voiding a warranty for it; a void term needs no enforcement agency, since courts will not enforce it); A-2 (such terms were in use) | A-2 |
| C-4 | makers.farm, makers.phone | compliance_cost | increase | short; medium; long | visible | A | CR-1 (op 3: K1 attaches to selling covered equipment a duty to supply parts, tools, documentation and software to owners and independents; K2 makes warranties cover equipment repaired by others, except damage caused by the repair; K3 restricts software locks, more under U1-a); CR-8c (resources spent complying are used up) | none |
| C-5 | makers.phone | product_attribute (parts pairing that needs the maker's authorization, in covered phones) | U1-a: decrease; U1-b: no_change | medium | visible | B | CR-1 per reading: U1-a, K3 removes the option of pairing that needs the maker's authorization (op 1), so it is removed from covered phones where makers comply (A-1); U1-b, pairing is lawful if owners can pair genuine parts with a tool on fair terms, so no operation on pairing as such | A-1 |
| C-6 | owners.covered_equipment (farm and phone) | asset_value (covered equipment) | increase | short (from passage, February 2027) | invisible | B | CR-8 0.7 (voiding a contract right is a transfer: the right to restrict repair moves from makers and dealers to owners, C-3); CR-10c and CR-7c (cheaper and nearer repair, C-24, raises the expected yield of the equipment, captured by its owners when it becomes expected, A-20); A-3 | A-1, A-3, A-20 |
| C-7 | owners.covered_equipment (farm and phone) | quantity_traded (repairs by independent shops) | increase | medium; long | visible | B | CR-4 (x: dealer or authorized repair, y: independent repair; y improved by K1 and K2 at $95 against $165 an hour, or $160 against $280 a screen; owners at the margin switch, A-3; CR-4a: none switch the other way); A-1; independents can expand (A-5) | A-1, A-3, A-5 |
| C-8 | owners.covered_equipment (farm and phone) | home_production (self repair) | increase | medium; long | invisible | B | CR-4 (x: buy repair, y: repair oneself; K1 gives owners the parts, tools, documentation and software, A-3; owners can read fault codes, A-16); CR-1 (op 2) | A-1, A-3, A-16 |
| C-9 | dealers.farm, authorized_providers.phone | quantity_traded (repair service) | decrease | medium; long | visible | B | CR-9 (independent and self repair are substitutes for dealer service; C-7, C-8 move demand away); CR-4 applied to owners; A-3, A-1. The record's illustration: about $100 million a year of farm service if dealer revenue fell by a fifth | A-1, A-3 |
| C-10 | dealers.farm, authorized_providers.phone | net_price_received (repair service), wait_time (at dealers, for their customers) | at_least_one_decrease | medium | invisible | B | CR-6 (less demand at each price while dealers' capacity cannot contract at once, A-4: the pressure goes to the price or to the waiting time, or both; which is not established, so they are a group) | A-1, A-3, A-4 |
| C-11 | sellers.prospective (independent repair shops) | entry_rate | increase | medium | invisible | B | CR-4 (x: stay out, y: open or expand a shop; y made better by access to inputs, C-1, C-2, and by demand, C-7); CR-7a; A-5 | A-1, A-3, A-5 |
| C-12 | independents.farm, independents.phone | investment_target (tools, software subscriptions, training before 1 September 2028) | increase | short (March 2027 to August 2028) | invisible | B | CR-10a (a change expected in the future alters choices now: the duty starts on a known date, so investment that pays only after it is made before it); CR-4 (x: wait, y: prepare); A-20, A-5 | A-5, A-20 |
| C-13 | owners.covered_equipment (farm and phone) | quantity_traded (repairs at dealers and authorized providers, March 2027 to August 2028) | decrease | short (window before the effective date) | invisible | B | CR-10a and CR-4 (x: repair now at dealer terms, y: defer until independent and self repair are open from 1 September 2028; y made better for repairs that can wait, A-7). Signed per window (CR-12h) | A-7, A-3 |
| C-14 | owners.covered_equipment (farm and phone) | quantity_traded (repairs, all providers, from September 2028) | increase | medium | invisible | B | Mirror window of C-13 (deferred repairs are made, CR-10a); CR-4c (repair is cheaper, so units of repair valued least, previously not bought, are bought, C-24) | A-7, A-3, A-1 |
| C-15 | makers.farm | reclassification (compact tractors designed and marketed for grounds care) | increase | medium; long | invisible | B | CR-4 (x: the covered form, 'designed primarily for agricultural use', y: a form outside the definition; K1 to K3 make x more costly, A-6; some makers can reshape at less cost than coverage, A-9) | A-6, A-9 |
| C-16 | makers.farm | variety (specialty farm models offered in Kestrava) | decrease | medium; long | invisible | B | CR-4 0.7 (a cost fixed per item offered bears on which items are offered: x: offer the model in Kestrava with documentation, tools and software, y: drop it; for some of the 14 low-volume models y is now better, A-11) | A-11 |
| C-17 | makers.farm, makers.phone | product_attribute (integration of components; under U1-b, pairing of more parts) | increase | long | invisible | B | CR-4 (x: modular design with separately replaceable parts, which K1 and K3 now require to be open to others, y: integrated assemblies or, under U1-b, more paired parts, which keep control of which parts work; y made relatively better, A-24); CR-10b (applies to new designs as they replace old ones) | A-24 |
| C-18 | makers.farm | price_paid (new covered farm equipment in Kestrava) | increase | medium; long | visible | B | CR-5c (any change in what one party must give moves the range of acceptable terms) with A-6 (makers recover the cost through other terms of sale) and A-18 (farm makers raise Kestrava list prices relative to Darnholt); CR-9 and LW-10 (buyers value repair access, A-22, so demand for covered equipment rises: same direction, as a second chain with its own premise) | A-6, A-18 |
| C-19 | buyers.current (phone buyers in all states) | price_paid (new phones) | increase | medium; long | invisible | B | CR-5c with A-6 (costs recovered through other terms); makers sell at one national price (A-19), so the recovery is spread over all states; CR-6 1.0 (a small effect in a wider market is signed) | A-6, A-19 |
| C-20 | buyers.current (farms buying new covered equipment in Kestrava) | quantity_traded (new covered farm equipment) | ambiguous | medium; long | invisible | B | CR-12b: (−) CR-4c (higher price, C-18); (+) CR-4 (repair access makes covered equipment worth more to buyers, A-22). No dominance premise | A-6, A-18, A-22 |
| C-21 | farms.near_border (about 3,000 within 30 km), neighboring_jurisdictions (six Darnholt dealers) | cross_border_purchases (new farm equipment bought in Darnholt) | ambiguous | medium; long | invisible | B | CR-4 (x: buy in Kestrava, y: buy across the line): (+) the Kestrava price rises relative to Darnholt (A-18); (−) where a purchase in Darnholt would fall outside 'sold or leased to a purchaser in Kestrava', buyers who value repair access (A-22) lose it by buying there. Whether such a purchase is covered is not settled by the record (see Gaps), so the second chain is kept and the sign is ambiguous | A-18, A-22 |
| C-22 | makers, dealers, farm groups, repair associations | lobbying_effort (over the reading of U1, the scope of K1, and enforcement) | increase | short; medium | invisible | B | CR-4 (x: accept, y: lobby; the Act gives each side a stake in how U1 and 'fair and reasonable terms' are read); CR-4 1.0 (the bill itself was contested on the counterfactual path too, in 2023 and 2025, so lobbying for or against such a law is not signed; lobbying over the Act's reading and enforcement exists only under the policy, CR-12 0.9); CR-8c | A-23 |
| C-23 | makers.farm, makers.phone | legal_breach (offers short of fair and reasonable terms) | increase | medium; long | invisible | B | CR-4 (x: comply, y: offer less; the Attorney General acts only on complaint, from an unchanged budget, A-10); CR-12 0.9 (a breach of a duty that exists only under the policy is an increase against none) | A-10 |
| C-24 | owners.covered_equipment (farm and phone) | full_cost_per_unit (repair of covered equipment) | decrease | medium | invisible | B | CR-4 and CR-2 (owners who switch, C-7, C-8, do so because they rank the new option higher; those who stay are unaffected or gain from shorter dealer waits, C-10); CR-9 (substitute); A-14 (shorter waits at harvest) | A-1, A-3, A-14 |
| C-25 | owners.covered_equipment (farm and phone) | full_cost_per_unit (repair of new covered models) | ambiguous | long | invisible | B | CR-12b: (−) access to inputs, as C-24; (+) integration and wider pairing (C-17, A-24) make each repair replace more and cost more. No dominance premise (CR-12 0.8, kind 2 with p 0.55) | A-1, A-3, A-24 |
| C-26 | owners.farm (covered and uncovered equipment) | wait_time (repair at harvest) | decrease | medium | invisible | B | CR-9 (more repairers and self repair, C-7, C-8, C-11, A-14); for owners of pre-2023 equipment, CR-9 (same dealer capacity: covered owners leave dealer queues while dealer capacity cannot contract at once, A-4) | A-1, A-3, A-14 |
| C-27 | dealers.farm | asset_value (dealerships) | decrease | short (from passage, February 2027) | invisible | B | CR-7c and CR-10c (the expected fall in service and parts income, C-9, C-29, is borne by whoever owns the dealership when it becomes expected, A-20); CR-7b (dealers' capital and locations are tied to their territory, A-19) | A-3, A-19, A-20 |
| C-28 | dealers.farm (relative to makers) | tax_share_borne (share of the Act's burden on the supply side) | increase | medium; long | invisible | B | CR-7b (the lasting loss settles on the means that cannot move: dealers are tied to Kestrava territories, while makers sell in many states at national prices, A-19; the ranking needs that comparative premise, which A-19 gives); A-6 | A-6, A-19 |
| C-29 | dealers.farm | quantity_traded (parts sold at retail to owners and independents) | decrease | medium; long | invisible | B | CR-9 (makers must now sell to owners and independents on the terms dealers get, so buyers who paid list at dealers can buy at dealer cost elsewhere); CR-4 applied to those buyers | A-1, A-2 |
| C-30 | investors (holders of makers' shares) | asset_value (makers' shares) | decrease | short (from passage) | invisible | B | CR-7c and CR-10c (expected repair-input margins in Kestrava, valued by investors, A-12, fall, C-29, net of what makers recover, A-6; captured when expected, A-20). The recovery (C-18, C-19) is partial by A-19 for phones and contested by C-20 for farm equipment; the sign rests on A-12 that the margins were valued | A-12, A-20, A-6 |
| C-31 | sellers.current (independent repair shops) | asset_value (shops) | increase | short (from passage) | invisible | B | CR-7c and CR-10c applied to C-7 and C-1 (higher expected yield, captured by owners when expected, A-20), until entry (C-11) brings yields back in line (CR-7a) | A-1, A-3, A-20 |
| C-32 | input_suppliers (repair technicians) | employment (independent shops), employment (dealers and authorized providers) | at_least_one_as_stated | medium | invisible | B | CR-9 and LW-10 (demand for technicians follows repairs: independent shops +, C-7; dealers −, C-9, once their capacity can contract, A-4 holds only in the short run); CR-7a (technicians trained by dealers move to independents). Each member's direction stated; total employment not signed | A-1, A-3, A-5 |
| C-33 | complainants.other (consumers with other unfair-practice complaints) | wait_time (handling of complaints), quality_per_unit (attention per complaint) | at_least_one_as_stated | medium | invisible | B | CR-8a (staff time spent on Act complaints, C-34, is withdrawn from other complaints); CR-6 0.7 and 1.0 (a fixed budget supplying a fixed quantity of handling: waiting rises or attention falls; A-N1 that there is no spare capacity) | A-10, A-N1 |
| C-34 | owners, independents (complainants) | applications (complaints to the Attorney General under the Act) | increase | medium | invisible | B | CR-4 (x: accept a short offer, y: complain; y exists only under the Act, A-10); CR-12 0.9 | A-10 |
| C-35 | makers.phone (genuine parts sales) | quantity_traded (genuine phone parts) | U1-a: ambiguous; U1-b: increase | medium | invisible | B | CR-9 and LW-10 (more repairs, C-14, raise demand for parts); under U1-b, genuine parts are now sold to independents and pair fully while non-genuine parts still give warnings, so independents switch toward genuine (CR-4, A-21): increase. Under U1-a, non-genuine and salvaged parts also work fully, removing the advantage of genuine parts (CR-4, A-21): CR-12b, ambiguous | A-1, A-3, A-21 |
| C-36 | sellers.substitutes (non-genuine and salvaged phone parts) | quantity_traded | ambiguous | medium | invisible | B | CR-12b. (+) more independent repair (C-7) raises demand for all parts; under U1-a their parts work fully. (−) genuine parts are now available to independents at authorized terms (A-21). Under both readings the chains oppose and no premise says which dominates | A-1, A-3, A-21 |
| C-37 | independents.phone | quality_per_unit (repairs) | increase | medium | invisible | B | CR-1 (op 2: genuine parts and the means to pair them are available, U1-b; or any part works fully, U1-a); CR-4 (independents who used parts that gave warnings switch where the better option is open, A-1) | A-1 |
| C-38 | informal sellers (thieves and buyers of stolen phones) | informal_activity (trade in stolen phones and their parts) | U1-a: increase; U1-b: no_change | medium | invisible | B | U1-a: pairing and locks no longer stop parts of reported phones from working (A-17), so the value of a stolen phone's parts rises; CR-4 (x: not steal or buy stolen, y: do so; y made better). U1-b: makers may refuse to pair parts reported stolen, so nothing changes (CR-1: no operation on that option) | A-17 |
| C-39 | buyers.used_phones | quality_information (whether a used phone has non-genuine parts) | U1-a: decrease; U1-b: no_change | medium | invisible | B | CR-11 (actors act on what they know): under U1-a the 'unknown part' notices disappear with pairing, and buyers who checked them (A-15) can no longer tell; under U1-b notices remain as before | A-15 |
| C-40 | owners.farm_uncovered (pre-2023 equipment, about 70% of tractors) | asset_value (equipment) | ambiguous | short (from passage) | invisible | B | CR-12b: (−) CR-9 (covered used equipment, C-6, is a substitute and is now worth more, so buyers move to it); (+) CR-9 (more independent shops and shorter dealer waits, C-11, C-26, serve uncovered equipment too, A-5, A-4). No dominance premise | A-3, A-4, A-5, A-20 |
| C-41 | buyers.foreign (phone owners and independents in other states) | quantity_traded (genuine parts and tools bought outside Kestrava) | increase | medium | invisible | B | CR-9 (makers extend their parts and tool programmes to all states rather than check where each phone was sold, A-8); CR-4 applied to owners elsewhere (an option is added, CR-1 op 2) | A-8 |

## Gaps found

**(a) Steps no core rule covers.**
- GAP-059-C1. Design responses (C-17): CR-4 gives the direction once A-24 is assumed, but no core rule addresses a seller changing the product so that a mandated term binds less. It was treated as reclassification-like CR-4 (x: modular, y: integrated); whether this is the same margin as reclassification is not stated.
- GAP-059-C2. Non-rival inputs: diagnostic software and documentation are knowledge (CR-8 0.7, non-rival means). Whether supplying them to independents creates repair capacity or only transfers it could not be signed by conservation of means; total repairs (C-14) were signed through CR-4c on the buyers' side instead.

**(b) Core-rule and record wording that was hard to apply.**
- §2(b) "sold or leased to a purchaser in Kestrava": whether a Kestrava farm buying from a Darnholt dealer is covered is not settled, and the record lists no reading for it. Kept as an opposing chain in C-21 rather than a reading.
- CR-7b ranking with three parties (makers, dealers, owners): A-19 compares makers and dealers only; no premise ranks owners against either, so only the dealers-versus-makers share (C-28) is signed.
- CR-6 0.7 public supply applied to complaint handling by an agency with a fixed budget (C-33): fits by analogy; the margins (waiting, attention per case) had to be stated as a group.
- CR-4 1.0 on lobbying where the bill was contested on the counterfactual path: the split between lobbying over the law (not signed) and over its reading (signed) is the analyst's.

**(c) Vocabulary missing from the ontology.**
- No variable for the share of repairs done by a class of repairer; `quantity_traded` per class was used.
- No variable for product design or modularity; `product_attribute` was used.
- No actor class for informal sellers of stolen goods distinct from `intermediaries`.


## Comparison with the pattern-based analysis

**Summary.** The two versions agree on the core of the right-to-repair case: independents and owners pay less for parts, tools and software; independent and self repair rise and authorized repair falls; anti-repair terms lose force; independents enter; dealers bear more of the burden than makers and their dealerships lose value; makers' shares fall and covered equipment gains; pairing, stolen parts and used-phone information per reading; deferred repairs in the window; compact tractors reshaped; specialty models withdrawn; breach of the new duty; lobbying over the Act's reading; shorter harvest waits; ambiguous values of exempt tractors, new farm sales, cross-border purchases and non-genuine parts. No key is signed in opposite directions. The differences: the pattern version signs dealers' price per job alone (RS-16's mirror case), where CR-6 leaves price and waiting as a group in a market the record shows was rationed by waiting; and it signs the average age of covered devices up without combining its own ambiguous new-sales chain. The core version is wrong on pairing under U1-b (`no_change`, against its own classification of K3 as operation 3), signs integration as rising without the buyers'-valuation chain it uses elsewhere, signs phone prices alone without a member premise, and under-signs technicians' employment. It omits makers' substitute terms, dealers' net parts price, owners' diagnostic information and independents' long-run return. The pattern version omits dealers' retail parts sales and genuine phone parts. EN-14's failure is confirmed.

Counts: M 23, V 6, S 6, OP 5, OC 7.

### Pattern version → core version

| Pattern ID | Matched core ID(s) | Class | Cause | Note |
| --- | --- | --- | --- | --- |
| C-1 | C-1, C-2 | M | | Inputs cheaper for independents and owners; the core splits farm and phone. Horizon labels differ only by definition (the core's "medium" starts at the effective date). |
| C-2 | C-7 | M | | Independent repairs rise. |
| C-3 | C-8 | M | | Self repair rises; the core adds phone owners and A-16. |
| C-4 | C-24 | V | | Pattern: owners' price per independent or self repair of a given kind falls. Core: owners' `full_cost_per_unit` of repair falls (medium). Both omit a chain: before entry (A-5) independents' capacity is short while demand for them rises (pattern C-24: returns rise), which pushes their price per job up against the cheaper inputs. For owners who already used independents the short-run sign is `ambiguous` (CR-12b); the decrease holds once capacity has grown. |
| C-5 | C-3 | M | | Enforceable anti-repair terms fall. |
| C-6 | C-9 | M | | Authorized repairs fall. |
| C-7 | C-10 | S | P | Pattern: dealers' price per job falls (RS-16, mirror). Core: price or wait at dealers, `at_least_one_decrease`. Core right: lower demand against fixed capacity (A-4) moves at least one margin (CR-6), and the record shows the dealer market was rationed partly by waiting (2.5 days at harvest), so the wait is an open margin; signing the price alone needs a premise (CR-6, 0.9: splitting a shift). RS-16's mirror case, applied as written, signs the substitute's price alone and does not consider a substitute market cleared partly by waiting. |
| C-8 | C-11 | M | | Entry of independents rises. |
| C-9 | C-16, C-18, C-19 | S | E | Pattern: group over new-equipment price (+), warranty and terms (−), variety (−). Core: farm price increase (C-18, on A-18), phone price increase in all states (C-19), variety decrease (C-16), each alone. For farm equipment the core is right: A-18 (p 0.55) is a member premise, and the pattern version itself uses it as a chain in C-17 while keeping the group (its gap b3). For phones the core is wrong: A-6 says makers recover costs "through other terms of sale", which names no member, and A-19 (national prices) says where a price change would fall, not that price is the margin used; C-19 should stay in the group. Errors in both versions. |
| C-10 | none | OC | E | Substitute terms (warranty exclusions for damage caused by repair, which §4(b) allows; service bundles; expiring subscriptions) rise, with price, as a group. CR-1 (K2 removes the term's protection), CR-5c and CR-6 (pressure moves to the open terms) derive it. Core-version omission. |
| C-11 | C-28 | M | | Dealers bear more than makers (CR-7b, A-19). |
| C-12 | C-5, C-17 | S | E | Pairing. U1-a: both decrease. U1-b: pattern `ambiguous`; core `no_change` (C-5) and, separately, more paired parts in the long run (C-17). Pattern right: under U1-b, K1 (§3(a)(iv)) and K3 attach to the option of pairing a duty to supply owners a pairing tool on dealer terms, an operation 3 that the core version itself records in section 2 ("U1-b: 3"), so by CR-4b some makers drop pairing; A-24 gives the opposing chain the core puts in C-17. CR-12b: `ambiguous`. Error in the core version (C-5 under U1-b contradicts its own classification, and C-17's chain was not combined with it). |
| C-13 | C-36 | M | | Non-genuine parts: ambiguous under both readings. |
| C-14 | C-38 | M | | Stolen parts: U1-a increase, U1-b `no_change`. |
| C-15 | C-13 | M | | Authorized repairs fall in the window before the effective date. |
| C-16 | C-14 | V | | Pattern: independent and self repairs in the first six months rise. Core: repairs by all providers rise from September 2028 (deferred repairs, and CR-4c on cheaper repair). Same timing chain, recorded wider. |
| C-17 | C-21 | M | | Cross-border farm purchases: ambiguous. The core notes that §2(b) may cover a Kestrava farm buying in Darnholt (an unrecorded reading); the pattern version assumes it does not. Same sign either way. |
| C-18 | C-41 | V | | Spillover to other states through national programmes (A-8): the pattern signs Darnholt owners' price of a genuine repair; the core signs quantity bought outside Kestrava. |
| C-19 | C-15 | M | | Compact tractors reclassified. |
| C-20 | C-23 | M | | Breach of the new duty rises from none. |
| C-21 | C-16 | M | | Specialty models withdrawn (CR-4 0.7, A-11). |
| C-22 | C-22 | M | | Lobbying over the Act's reading; both decline to sign lobbying over the law as such. |
| C-23 | C-27 | M | | Dealership values fall. |
| C-24 | C-31 | V | | Pattern: independents' `return_on_capital` rises until entry. Core: shops' `asset_value` rises at passage. Same chain (CR-7a, CR-7c). |
| C-25 | none | OC | E | Independents' return `no_change` in the long run (CR-7a with A-13). Derivable; the core says only in C-31's text that entry brings yields back in line. Core-version omission. The pattern version's citation of CR-7's 1.0 "which stock" clause is misplaced (there is no permission here) but harmless. |
| C-26 | C-30 | M | | Makers' share values fall. Both rest on more than CR-3a: the Act binds every rival at once and changes each maker's situation through the others (CR-9), so a fall needs the premise that the lost repair margins outweigh any gain from all rivals being bound and from buyers valuing the term (A-22). A-12 does not state that; the pattern version flags it (its gap b2), the core version leans on "recovery is partial". |
| C-27 | C-6 | M | | Covered equipment gains value. |
| C-28 | C-40 | M | | Exempt tractors: ambiguous. The core misses EN-14's (+) chain (new covered units dearer, its own C-18, so exempt units face less competition), but the sign is the same. |
| C-29 | none | OC | E | `stock_age` of covered devices increase. Longer lives (CR-4) raise average age, but the pattern version's own C-30 leaves new covered sales ambiguous, with a (+) chain from buyers valuing the term (A-22); more new units lower the average age. CR-12b gives `ambiguous` for the average; the retention claim alone ("kept longer") is valid. Error in the pattern version (chain not combined). |
| C-30 | C-20 | M | | New covered sales: ambiguous (the core records farm equipment only). |
| C-31 | none | OC | E | Dealers' net parts price: ambiguous. The "most favorable terms" tie makes each dealer discount cost the maker more (CR-4, CR-5c: +), against competition from salvaged and non-genuine parts (A-21: −). Derivable; core-version omission. |
| C-32 | C-26 | M | | Harvest waits fall (A-14). |
| C-33 | C-32 | S | E | Pattern: dealers' technicians, employment or hours, `at_least_one_decrease`. Core: one group over employment at independents and at dealers, `at_least_one_as_stated`. Pattern right: each side has its own derivation (CR-9 with LW-10 on the core's own C-9 and C-7), so two signs are warranted where the core gives only "at least one of the two". Error in the core version (under-signing). |
| C-34 | C-32 | S | E | Pattern: employment at independents increase. Entry of new shops (core C-11, A-5) adds employment that cannot be hours in an existing shop (OC-5's new-activity clause, here CR-9 with entry). Pattern right; error in the core version. |
| C-35 | none | OC | J | Technicians' wage: ambiguous. Not recorded by the core; nothing scorable lost. |
| C-36 | C-39 | M | | Used-phone buyers' information: U1-a decrease, U1-b `no_change`. |
| C-37 | none | OC | E | Owners' information about faults increases (CR-11c with A-16, both premises CR-11 0.7 asks for). The core uses A-16 only inside C-8. Core-version omission. |
| C-38 | C-17 | S | E | Pattern: separately replaceable parts in new models `ambiguous` ((−) integration, A-24; (+) buyers value repairable designs, A-22). Core: integration increase (long), on A-24 alone. Pattern right: the core uses A-22 (p 0.7) for C-18 and C-20 but not here; under CR-12 (0.8, kind 2) a chain with p ≥ 0.5 makes the sign `ambiguous`. Error in the core version. |
| C-39 | none | OC | J | Owners who repair anyway have more for other uses. The mirror of the CR-3 note holds for owners who keep buying the same repairs at a lower price; for owners who buy more repairs (CR-4c) spending on repair may rise. The core version declined it ("owners who switch choose to"). Both defensible; it rests also on C-4 and C-7, whose short-run price signs are questioned above. |
| C-40 | C-4 | M | | Makers' compliance cost. |
| C-41 | C-33 | V | | Other complainants: a group with `wait_time` in both; the pattern's second member is time per complaint, the core's attention per complaint (`quality_per_unit`), with the new premise A-N1. |
| C-42 | C-12 | V | | Independents' outlays on software and tools: the pattern records them as `compliance_cost` (a voluntary input purchase, not compliance; CR-8c does not fit), the core as investment before the effective date. |

### Core-only consequences

| Core ID | Class | Cause | Note |
| --- | --- | --- | --- |
| C-25 | OP | J | Long-run repair cost of new models: ambiguous (access against integration). The pattern version records the design side (C-38) but not this key; nothing scorable lost. |
| C-29 | OP | E | Dealers' retail parts sales to owners and independents fall: K1 lets those buyers buy at dealer terms from the maker (CR-9, CR-4). Pattern-version omission. |
| C-34 | OP | E | Complaints under the Act rise from none (CR-4, CR-12 0.9). The pattern version uses them in C-41 but records no row. Pattern-version omission. |
| C-35 | OP | E | Genuine phone parts: U1-a ambiguous, U1-b increase. Under U1-b, more repairs and independents' switch from warning-giving parts raise demand; no one switches toward non-genuine parts on account of the change, since that option is unchanged under U1-b (CR-4a). Pattern-version omission (it analyzed only the non-genuine side, C-13). |
| C-37 | OP | J | Quality of independents' phone repairs increases. Defensible by CR-4a for existing customers (no one moves to a worse part on account of the change), but the class's average also depends on new entrants and on the jobs moving from authorized providers, which no premise covers; the pattern version declined to say whether independent repairs are better or worse done. |

### Findings

- **Pattern overclaims or hidden premises.** (1) Dealers' price per job (C-7) signed alone where waiting is an open margin; RS-16's mirror case as written invites this. (2) `stock_age` (C-29) signed without combining the version's own ambiguous new-sales chain. (3) Owners' price per independent repair (C-4) and owners' means (C-39) omit the short-run demand pressure on independents' prices before entry. (4) Makers' share values (C-26) need a premise that binding every rival at once does not raise each maker's value; CR-3a alone does not give it (shared with the core version).
- **Errors in the core version.** Pairing under U1-b `no_change` (C-5) against its own operation 3 for K3, and its (+) chain left in C-17 uncombined; integration (C-17) signed without the A-22 chain it uses for C-18 and C-20; phone prices (C-19) signed alone without a member premise; technicians (C-32) under-signed as one group. Omissions: substitute terms (pattern C-10), dealers' net parts price (C-31), diagnostic information (C-37), independents' long-run return (C-25), and EN-14's dearer-new-units chain inside C-40 (sign unaffected).
- **Errors in the pattern version.** Beyond the overclaims: farm list prices kept inside the group (C-9) although the version signs them on A-18 elsewhere; omissions of dealers' retail parts sales (core C-29), genuine phone parts (C-35) and the complaints count (C-34); `compliance_cost` used for a voluntary purchase (C-42); CR-7's 1.0 clause cited where no permission exists (C-25).
- **Limits of the core rules.** None that produced a difference: every difference above is an analyst's error or omission, or a judgment, and every valid claim of either version is derivable from CR-1 to CR-12. The core version's GAP-059-C1 (design changes that make a mandated term bind less) was handled by CR-4 in both versions; GAP-059-C2 (non-rival diagnostic knowledge) is the existing Q21 and no consequence turned on it. Where the core rules are thin is wording, not reach: CR-3a for a firm when the rule binds all its rivals; CR-1 for a term owed to third parties; CR-7b with three parties.
- **The pattern version's "Test of 1.0".** *EN-14, failed:* confirmed. The core version, without the pattern, reached `ambiguous` for exempt tractors (C-40) from CR-9 chains, and the reason is the one the pattern version gives: the standard is something buyers value, so covered units draw demand from exempt ones. EN-14 needs an Unless clause for a standard that raises buyers' valuation of the new units. *PC-17, needed interpretation:* confirmed. The core built the product-side adjustment from CR-5c and CR-6 and still went wrong on it (phone prices alone, substitute terms omitted), which shows that PC-17's employment-only group gives no help for a product sale; who bears it needed CR-7b with A-19 in the core too (C-28). *RS-4, needed interpretation:* confirmed; the core reached `ambiguous` for cross-border purchases (C-21) from CR-4 with two chains, as the pattern version did from CR-12, and found a further unrecorded reading of §2(b) that RS-4 would not prompt.
