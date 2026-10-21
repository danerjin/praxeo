# WE-044 Ban on short-term rentals of whole homes, with a primary-residence exception

Analyst: draft (Handbook 0.8 held-out test, corrected under 0.9)  |  Rule catalog version: 0.9  |  Status: awaiting expert review

A stylized policy in a fictional city. It resembles real short-term rental ordinances but is not modeled on any one of them. It was written as a held-out test of catalog 0.8, which was tuned on WE-026 to WE-035. It probes: a prohibition that removes a use of one's own property (CR-1, with an autistic element for owners who combined their own use with letting), operations dated in two steps (CR-1, 0.8), effects on neighbors through `proximity` at Tier C (CR-9, 0.7) and their use in asset values, spillover to hotels and to long-term and mid-term rentals (RS-16 with its Unless clause, RS-13, PC-8 by analogy), opposing timing chains in the announcement window (RS-8, 0.8), enforcement against the right baseline (OC-3, 0.8), enforcement that waits for complaints (then the candidate pattern "complaint-only enforcement", 06_gaps.md 6.2e; promoted in 0.9 as RS-20), and the boundary between `legal_breach` and `informal_activity`. Noise, safety and neighborhood character as such are outside the scope of version 1. The probabilities are illustrative; the evidence column says what a real analysis would cite.

## 1. Policy record

**Saltmere Housing Preservation Ordinance (Ordinance 2026-31).** Saltmere is a coastal city of about 310,000 people with about 128,000 dwellings, of which about 60,000 are rented long-term (median rent $1,850 a month, vacancy about 3%). Tourism is concentrated in three districts near the beach (Harbor, Dunes and Old Town). The city's 2026 platform report counts about 4,300 active short-term rental (STR) listings:

| Listing type | Listings | Notes |
|---|---|---|
| Rooms in a home where the owner lives and is present | 1,250 | Not covered by K1. |
| Whole units, not the owner's primary residence | 2,150 | About 1,700 never used by the owner (investor units); about 450 second homes the owner uses some weeks a year. About 70% are in the three beach districts. |
| Whole units, the owner's primary residence, let while the owner is away | 550 | About 140 let more than 90 nights a year. |
| Whole units in two-unit buildings whose owner lives in the other unit | 350 | About 120 let more than 90 nights a year. Subject to U1. |

A whole-unit STR earns on average $235 a night at 60% occupancy, about $51,000 a year gross; after cleaning, platform fees, furnishing and management (about 40% of gross), about $30,000 net. The same unit let on a 12-month lease earns about $24,000 gross, about $20,000 net. Hotels: about 7,400 rooms, average occupancy 79% (94% in July and August), average daily rate $180; about 2.1 million room-nights a year, against about 0.67 million whole-unit STR nights. Hotel construction takes three to five years from site to opening. Furnished lets of 30 nights or more (traveling nurses, university visitors, relocations) are a small segment of about 900 units, rented at about $3,200 a month. About 6% of a year's whole-unit STR nights are booked more than nine months ahead. In 2023 to 2025, about 30% of home purchases in the beach districts were by buyers who did not occupy the home.

Outside the city: the town of Elsdon, 12 km from the Harbor district, has about 420 STR listings and no rules beyond county registration.

| Field | Value | Source sentence |
|---|---|---|
| Jurisdiction (and what lies just outside) | City of Saltmere, all zones. Elsdon (no STR restriction) 12 km away. | §1: "This ordinance applies to every dwelling unit within the City." |
| Announced / enacted / effective / expires | Introduced 3 November 2026 by six of nine council members (announced). Enacted 8 December 2026. Effective 1 July 2027 (eight months after introduction); transition for booked stays to 30 September 2027. No expiry. | §9 |
| Enforcement (who, penalties, resources) | K2 against platforms: Registry Unit notices, fine per listing per day. K4 against hosts: Code Enforcement, on complaint only, fine $2,500 for a first violation and $5,000 for each later one, "within existing appropriations"; fines go to the general fund. K3: a new Registry Unit of five staff, $520,000 a year, new appropriation from the general fund. | §6, §7, §8 |
| Existing rules | R1 STR registration ($150 a year; about 65% of hosts registered; platforms not obliged to check). R2 Transient occupancy tax (TOT) of 12% on stays under 30 nights, hotels and STRs alike; platforms collect it for STRs (about $18.7 million a year from whole-unit STRs; about $46 million from hotels). R3 Noise and nuisance ordinance, enforced by Code Enforcement on complaint: in 2025, about 9,600 noise complaints, about 1,500 of them about STR units (about one a year for every two whole-unit listings), at about 2.5 staff hours each. Code Enforcement has a fixed budget of $6.1 million (48 staff). | Municipal Code §5.12, §3.30, §8.04 |

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Ban | `prohibition` (letting a whole dwelling unit for stays under 30 consecutive nights) | Whole-unit STR | Owners and anyone letting a unit | From 1 July 2027, no whole unit may be let for under 30 nights unless it is the owner's primary residence, registered under K3, and then for no more than 90 nights in a calendar year (45 nights for July to December 2027). "Primary residence": "the dwelling in which the owner resides at least 270 days a year". Stays booked and confirmed before 1 July 2027 may be completed if they end by 30 September 2027; all other bookings for later dates must be cancelled and refunded in full. | Rooms in a home that is the owner's primary residence, while the owner is present. Lets of 30 nights or more. |
| K2 Platform duty | Rule on intermediaries | Listings | Booking platforms | From 1 July 2027: display a valid K3 registration number on every whole-unit listing; remove a listing within 10 days of a city notice that it is non-compliant; report nights booked per registration number each quarter. Fine $1,000 per listing per day after the 10 days. | — |
| K3 Registry | Licensing of the exempt use | Primary-residence lets | Owners who let their primary residence | Registration $250 a year, with proof of residence (driver's license, voter registration, homestead tax exemption). Registry Unit, $520,000 a year. Replaces R1 for whole units. | — |
| K4 Host enforcement | Enforcement | K1 | Code Enforcement | On complaint only; no proactive inspection; fines above. No new appropriation. | — |

Unclear provisions:
- **U1, two-unit buildings.** K1's exception covers "the dwelling in which the owner resides". Reading U1-a: the dwelling is the building (one structure on one parcel), so the second unit of a two-unit building whose owner lives in the other unit is part of the primary residence and may be let up to 90 nights a year. Reading U1-b: the dwelling is the unit, so the second unit is not the owner's primary residence and may not be let for under 30 nights at all. About 350 listings are affected; about 120 of them let more than 90 nights a year. The Registry Unit will decide which reading it applies when it issues (or refuses) registration numbers, and K2 makes platforms follow the registry. Readings get no probability; where a sign depends on U1, one sign per reading is given.

The counterfactual is Saltmere without the ordinance: R1 to R3 stay in force, whole units may be let for any number of nights, and nuisance complaints are handled under R3.

## 2. Classification

| Component | Rothbard type | Binding? | Rule families |
|---|---|---|---|
| K1 | Triangular: it prohibits an exchange (a stay under 30 nights) between owners and guests. By CR-1: for owners of non-primary units, operation 1 (the option of letting short-term is removed) from a date (0.8 clarification: the operation is dated 1 July 2027 for new bookings and 1 October 2027 for stays already booked); for primary-residence owners, operation 1 above 90 nights and operation 3 (registration, K3) below; for guests, operation 1 on whole-unit stays outside the exception. **Autistic element:** for second-home owners, what is removed is a way of using their own property, combining their own weeks in the home with lets in the other weeks. Their own use is not forbidden, but every remaining way of letting the home (a lease of 30 nights or more, a 12-month lease) displaces their own use. The restriction therefore works partly on the owner's own action, with no exchange in the option that is left (C-7). The counterfactual law allows lets of any length. | Yes for most non-primary units (net $30,000 against $20,000 long-term; A-1). For primary-residence hosts, only above 90 nights. For two-unit buildings, per reading of U1. | CR-1, CR-4, CR-5a, RS-1, RS-3 to RS-10, RS-13, RS-16, RS-20, EN-7 (in part), OC-4, SB-4 |
| K2 | Triangular: it attaches a penalty to platforms for intermediating a prohibited exchange (CR-1, operation 3) | Yes, if platforms comply (A-2) | CR-1, CR-4, CR-8c |
| K3 | A licensing requirement on the exempt use; binary in its fee | Yes for primary-residence hosts | CR-1, CR-4 (0.8 fixed cost per outlet), CR-8b |
| K4 | Binary in its funding (fixed budget, OC-3); complaint-only, so for hosts who list off-platform it attaches a risk rather than removing the option (CR-1, Premises) | Yes | OC-3 (fixed budget, right baseline), RS-3, RS-20 |

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `hosts.non_primary` (`sellers.current`) | Owners of the 2,150 non-primary whole units | Short lets removed from July 2027. Split by response (CR-1, 0.7): `hosts.converting` (to 12-month leases), `hosts.mid_term` (to lets of 30 nights or more), `hosts.selling`, `hosts.in_breach` (keep letting short, off-platform). |
| `hosts.second_home` | The 450 second-home owners among them | Their own weeks plus lets in the other weeks is no longer possible. |
| `hosts.primary_over90`, `hosts.primary_under90` | Owners letting their primary residence while away | Registration ($250) for all; nights above 90 removed. |
| `hosts.duplex` | Owners letting the second unit of a two-unit building they live in | Per reading of U1: up to 90 nights (U1-a) or none (U1-b). |
| `hosts.lawful` | Rooms in occupied homes (`hosts.rooms`); primary-residence lets within the cap | Face less competition. |
| `guests.whole_unit` (`buyers.current`) | Visitors who would have stayed in a whole unit | Lose that option in Saltmere; can switch to hotels, rooms, Elsdon, off-platform lets, or not come. |
| `guests.prebooked` | Guests with bookings for stays after 30 September 2027 | Bookings cancelled and refunded. |
| `guests.off_platform` | Guests booking unlawful lets directly | Trade without platform reviews, payment protection or legal recourse. |
| `platforms` (`intermediaries`) | Booking platforms | Must check registration numbers, remove on notice and report nights. |
| `hotels` (`sellers.substitutes`), `buyers.substitutes` (hotel guests) | Hotel owners and their guests | More demand; fixed rooms in the short run. |
| Mid-term segment: `hosts.mid_term` and `guests.extended` | Furnished lets of 30 nights or more | Sellers and buyers both pushed in. |
| `tenants.prospective`, `landlords.long_term` | Long-term rental market | Converted units add supply. |
| `buyers.prospective` (homes) | Would-be buyers of homes in the beach districts | Investors' demand falls. |
| `investors.home_buyers` (`buyers.prospective`) | Would-be buyers of beach-district homes to let | The short-let use of a home they might buy is removed. |
| `sellers.prospective` (room lets) | Owner-occupiers who do not yet let rooms | Face a higher nightly price for rooms. |
| `homeowners.str_districts` | Owner-occupiers in the beach districts | Lose the option to let; fewer transient neighbors (`proximity`). |
| `neighbors` | Residents next to STR units | Changed through `proximity`, not exchange (CR-9). Also the complainants under K4. |
| `input_suppliers` | Cleaners, linen services, STR property managers | Less work. |
| `sellers.complements` | Restaurants, shops and tour operators in the beach districts | Visitors staying nearby are their customers (`complement`, location). |
| `neighboring_jurisdictions` | Elsdon hosts, owners and tenants | Guests drawn across the line. |
| `officials.enforcement` | Registry Unit (new); Code Enforcement (fixed budget) | New tasks; fewer nuisance complaints about STRs. |
| `taxpayers`, recipients of other general-fund spending | Fund the Registry Unit; receive TOT changes | One or more give up what the $520,000 would have funded. |
| `hosts.fined` | Hosts found in breach | Pay fines to the general fund. |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | `hosts.non_primary` | `quantity_supplied` (lawful whole-unit STR nights) | decrease | short (from 1 July 2027; fully from 1 October 2027) | CR-1, CR-4 | A-1, A-2 |
| C-2 | `guests.whole_unit`, `hosts.non_primary`, `platforms` | `quantity_traded` (whole-unit STR nights booked through platforms) | decrease | short | CR-5a, OC-4 | A-1, A-2 |
| C-3 | `hosts.primary_over90` | `quantity_supplied` (nights above 90 a year) | decrease | short | CR-1, CR-4 | A-2 |
| C-4 | `hosts.duplex` (letting 90 nights or fewer) | `quantity_supplied` (STR nights) | U1-a: ambiguous; U1-b: decrease | short | CR-1, CR-4, CR-9, CR-12b | A-2, A-32 |
| C-5 | `hosts.duplex` (letting more than 90 nights) | `quantity_supplied` (STR nights) | decrease | short | CR-1, CR-4 | A-2 |

C-1 and C-2 are what the ordinance's supporters point to: about 2,150 whole units leave the short-let market. The exchanges no longer made are prevented exchanges (OC-4): both the owner and the guest lose the gain each expected (CR-5a). C-4 is where U1 changes a sign most: under U1-b a two-unit owner letting 90 nights or fewer may not let short at all. Under U1-a the owner is a lawful host within the cap, and two derived chains oppose (section 7): the higher nightly price that displaced guests bring to lawful hosts (C-39, A-32) draws nights up toward 90 (CR-9, CR-4c), while K3's $250 fee and proof of residence, replacing R1's $150, is a cost fixed per outlet that can end the lightest lets (CR-4, 0.8; C-17). The sign under U1-a is therefore **ambiguous** (CR-12b), not `no_change`, which 2.5 reserves for a derivation that establishes no change.

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-6 | `hosts.converting` | `quantity_supplied` (units offered on 12-month leases) | increase | short–medium | RS-6, CR-4, CR-7a | A-1, A-5 |
| C-7 | `hosts.second_home` | `units_held_vacant` | increase | short–medium | CR-1, CR-4 | A-1, A-6 |
| C-8 | `hosts.mid_term` | `reclassification` (lets reshaped to 30 nights or more) | increase | short | RS-5 | A-1, A-7 |
| C-9 | `hosts.primary_over90`, hosts listing under another unit's registration | `legal_breach` (on-platform lets beyond the cap or the exception) | increase | short–medium | RS-3, RS-20, CR-1, CR-4 | A-3, A-22 |
| C-10 | `hosts.in_breach` | `informal_activity` (whole-unit lets booked off-platform) | increase | short–medium | RS-3, RS-20, EN-7, CR-1, CR-4 | A-3, A-4 |
| C-11 | `guests.off_platform` | `search_cost` | increase | short | RS-10 | A-3, A-4 |
| C-12 | `guests.off_platform` | `quality_information` | decrease | short | RS-10, CR-11b | A-3, A-4 |
| C-13 | `guests.off_platform` | `disputes_settled_outside_courts` | increase | short | RS-10 | A-3, A-4 |
| C-14 | `guests.off_platform` | `allocation_by_non_price_criteria` (hosts screen guests for quietness) | increase | short–medium | RS-20, CR-4, CR-6 | A-3, A-4, A-27 |
| C-15 | hosts, `platforms`, `hotels`, neighborhood associations | `lobbying_effort` (hosts and platforms to adopt U1-a, raise the cap or repeal; hotels and associations for proactive enforcement) | increase | medium | RS-7 | A-14 |
| C-16 | `platforms` | `compliance_cost` (registration checks, notices, quarterly reports) | increase | short | CR-1, CR-8c | A-2 |
| C-17 | `hosts.primary_over90`, `hosts.primary_under90`, `hosts.duplex` (U1-a) | `compliance_cost` (registration fee and proof of residence, against R1's $150) | increase | short | CR-1, CR-8c, CR-4 | A-2 |
| C-18 | `guests.whole_unit`, `hosts.non_primary` | `quantity_traded` (bookings made 3 November 2026 to 30 June 2027 for stays 1 July to 30 September 2027) | ambiguous | short | RS-8 (Unless, 0.9), CR-10a, CR-12b | A-15, A-16 |
| C-19 | `guests.whole_unit`, `hosts.non_primary` | `quantity_traded` (whole-unit stays before 1 July 2027) | ambiguous | short | RS-8, CR-10a, CR-12b | A-16, A-17 |
| C-20 | `guests.whole_unit`, `hosts.non_primary` | `quantity_traded` (bookings made from 1 July 2027 for stays to 30 September 2027) | decrease | short | RS-8, CR-1 | A-2 |
| C-21 | `guests.prebooked` | `search_cost` (rebooking after cancellation) | increase | short | CR-1, CR-5a | A-24 |
| C-59 | `hosts.non_primary` | `reclassification` (nominal 30-night contracts for shorter stays; claims of primary residence on documents the owner can change) | increase | short–medium | RS-5, CR-4 | A-1, A-38 |
| C-60 | `hosts.selling` | `quantity_supplied` (homes offered for sale, beach districts) | increase | short–medium | CR-4, CR-7c | A-1, A-37 |
| C-61 | `investors.home_buyers` | `quantity_demanded` (homes in the beach districts) | decrease | short–medium | CR-1, CR-4, CR-7c | A-1, A-21 |

**What owners do (C-6 to C-10).** For an owner of a non-primary unit, K1 removes the best option (CR-1, operation 1) and the owner falls back to the next-best (CR-3a), which differs from owner to owner (CR-1, 0.7: split the class by response). The pairs are CR-4's: x: a short let, y: a 12-month lease (C-6), a let of 30 nights or more (C-8, RS-5), a sale (C-60; its price is section 6, C-40 and C-42), or keeping the short let in breach (C-9, C-10). RS-5 also covers lets that only look like the exempt forms: a nominal 30-night contract for a stay of a week, or a claim of primary residence resting on documents an owner can change at low cost (a driver's license, a voter registration), which complaint-only enforcement rarely tests (C-59, A-38). On the buying side, would-be investors lose the short-let use of any home they might buy, so their demand for beach-district homes falls (C-61, CR-1, CR-4; A-21). A second-home owner has one more option: keep the home for their own weeks and leave it empty the rest of the year (C-7). That is the autistic element of K1: no exchange is forced or prevented in the option chosen; what is lost is a way of combining one's own use with other people's.

**Two kinds of breach (C-9, C-10).** The ordinance prohibits a trade for most units and allows it, within a cap, for others. A breach can therefore take two forms. A primary-residence host who lists on two platforms, each of which reports only its own nights, can exceed 90 nights while every listing carries a valid number (A-22); a host who lists a second unit under the registration of the home they live in does the same. These trades run through the legal market's channels (platforms, reviews, payment, TOT collected), so they are `legal_breach` (C-9). A non-primary owner who cannot get a number lets off-platform, to repeat guests and through social media and their own website: trade outside the legal market, `informal_activity` (C-10, RS-3, EN-7), to which RS-10 applies (C-11 to C-13). The boundary between the two variables is not drawn by the ontology for a prohibition with a permitted sub-class; this analysis draws it at the channel (Gaps found, d).

**Complaint-only enforcement (C-9, C-10, C-14).** Code Enforcement acts only on complaints, and complaints come mostly from neighbors. The expected penalty for an unlawful let is therefore the probability of a complaint times the fine (CR-1: the rule attaches a risk; CR-4, x: comply, y: violate). Against a gain of about $10,000 a year over a long-term lease, a $2,500 fine deters only where a complaint is likely. That probability differs by unit: lowest for detached homes, for units whose neighbors are themselves second homes or STRs, and for units let to guests who make no noise (A-3). Breach is therefore concentrated where neighbors are fewest or absent, and hosts in breach screen guests on what predicts a complaint (families, couples, older guests; no groups or parties), since the price cannot be set to cover the risk guest by guest when the risk is not observed in advance (C-14, CR-6: the scarce side chooses by other criteria, A-27). This is RS-20 (enforcement only on complaint; a candidate under 0.8, promoted in 0.9 after this second use): the expected cost of breach differs by counterparty, so breach concentrates where complaint is least likely. It is also what makes K4's ban bind least where neighbors were least affected.

**The cost of registering (C-17).** The $250 fee and the proof of residence are a cost fixed per host, not per night. By CR-4's 0.8 clarification on fixed costs per outlet, it bears on whether a primary-residence host lists at all (some who let a few nights a year stop), not on the nightly price. The baseline is R1, not no registration: for the hosts registered under R1 the cost rises from $150 to $250 plus the proof; for those who did not register under R1 it rises from nothing, but only where platforms require the number (A-2). C-17 is therefore Tier B on A-2, not Tier A.

**Timing in the announcement window (C-18 to C-20).** Under RS-8 every provision is checked for whether it improves an earlier window (0.8 Unless clause). The transition clause does: a stay booked before 1 July 2027 may go ahead if it ends by 30 September 2027. So:
RS-8's 0.9 clause on more timing chains covers this case directly: an opposing chain from a second incentive the policy meets (the leasing season), with each window signed by combining all the timing chains under CR-12b.
- *Bookings in the window for July to September stays (C-18).* (+) Guests and hosts who would have booked those summer stays in June, July or August (most whole-unit stays are booked within 60 days) book them before 1 July, while that still protects them (A-15). (−) Owners who plan to convert to a 12-month lease time the conversion to the leasing season (leases in Saltmere start in August and September, around the university year) or plan to sell over the summer; they stop accepting summer bookings, so bookings they would have taken in the window are not made (A-16). Both are timing chains in the same window, pushing opposite ways: **ambiguous** without a dominance premise, which the case does not supply.
- *Stays before 1 July 2027 (C-19).* (+) Some guests who prefer whole units move a planned later trip forward (A-17). (−) Owners converting for an early lease start, or selling with vacant possession, end short lets before July (A-16). **Ambiguous.**
- *Bookings after 1 July for stays to 30 September (C-20).* The other side of the first chain of C-18, and the ban itself: such bookings are no longer lawful for non-primary units, so they fall.

**Cancelled bookings (C-21).** Bookings made before the announcement for stays after 30 September 2027 (about 6% of a year's nights are booked more than nine months ahead, A-24) must be cancelled and refunded. The refund returns the guest's money (CR-8b), so the guest's means are unchanged; what is lost is the stay itself (CR-5a) and the time spent finding another (C-21).

**Lobbying (C-15).** Hosts (with a concentrated loss), platforms, and the beneficiaries (hotels, neighborhood associations) have stakes that depend on the reading of U1, the cap and enforcement (RS-7; A-14). Without the ordinance there would be no contest over these terms, so RS-7's repeal clause does not apply and the sign is an increase.

Not reported:
- Strategic complaints (rivals or hotels reporting lawful hosts to raise their costs; RS-20's last clause). CR-4 derives it (x: no complaint, y: complain), but it needs a premise that complaints cost the complainant less than the expected gain from a rival's lost bookings (A-28, p = 0.3).

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-22 | `buyers.substitutes` (hotel guests) | `price_paid` (hotel rooms, peak season) | increase | short–medium | RS-16, CR-9, CR-6 | whole-unit STR and hotel rooms: `substitute`, partial | A-8, A-9 |
| C-23 | `hotels` | `quantity_traded` (room-nights, mainly outside peak season) | increase | short–medium | RS-1, RS-16 | as C-22 | A-8 |
| C-24 | `hotels` (owners) | `asset_value` | increase | short (from 3 November 2026) | CR-7c, CR-10c, SB-4 | as C-22 | A-8, A-9, A-30 |
| C-25 | `hotels` | `investment_target` (new rooms) | increase | long | CR-7a, CR-4 | as C-22 | A-8, A-25 |
| C-26 | `guests.whole_unit` | `cross_border_purchases` (whole-unit stays in Elsdon) | increase | short | RS-4 | Saltmere and Elsdon STRs: `across_border`, partial | A-10 |
| C-27 | `neighboring_jurisdictions` (Elsdon hosts) | `quantity_supplied` (STR nights) | increase | short–medium | RS-4, CR-7a, CR-6 | as C-26 | A-10, A-39 |
| C-28 | `neighboring_jurisdictions` (Elsdon owners) | `asset_value` (homes suited to STR) | increase | short | CR-7c, CR-10c | as C-26 | A-10, A-30 |
| C-29 | `neighboring_jurisdictions` (Elsdon tenants) | `price_paid` (long-term rent) | increase | medium | RS-13, CR-9 | Elsdon long-term and STR uses: `same_market_other_segment`, partial | A-10, A-29 |
| C-30 | `guests.whole_unit` | `quantity_traded` (visitor trips to Saltmere) | decrease | short–medium | RS-1, CR-4c | — | A-11 |
| C-31 | `sellers.complements` (beach-district restaurants, shops, tour operators) | `quantity_traded` (visitors' purchases) | decrease | short–medium | CR-9, RS-9 | visitors' lodging and nearby purchases: `complement`, location | A-11, A-12 |
| C-52 | `sellers.complements` (beach-district restaurants, shops, tour operators) | `quantity_traded` (all purchases near the converted units, visitors and residents) | ambiguous | medium | CR-9, RS-9 (0.9), CR-12b | as C-31; residents' homes and nearby purchases: `complement`, location | A-5, A-12, A-33 |
| C-32 | `input_suppliers` (cleaners, linen services, STR managers) | `employment`, `hours_worked` | at_least_one_decrease | short–medium | CR-9, RS-6 | cleaning and management `input_to` STR | A-1, A-26 |
| C-33 | `hotels` (staff) | `employment`, `hours_worked` | at_least_one_increase | short–medium | OC-5, CR-9 | hotel labor `input_to` room-nights | A-8 |
| C-34 | `tenants.prospective` | `price_paid` (long-term rent) | decrease | medium | RS-13, CR-6 | STR and long-term uses of the same units: `same_market_other_segment`, close | A-5, A-13 |
| C-35 | `tenants.prospective` | `quantity_traded` (12-month leases) | increase | medium | RS-13, CR-4c | as C-34 | A-5, A-13 |
| C-36 | `landlords.long_term` | `net_price_received` | decrease | medium | RS-13, CR-6 | as C-34 | A-5, A-13 |
| C-37 | `landlords.long_term` (owners) | `asset_value` (rental buildings) | decrease | short–medium | CR-7c, CR-10c | as C-34 | A-5, A-13, A-30 |
| C-38 | `guests.extended` | `price_paid` (furnished lets of 30 nights or more) | ambiguous | short–medium | RS-16 (Unless), RS-13, CR-12b | STR and mid-term lets: `substitute`, partial | A-7, A-31 |
| C-39 | `hosts.lawful` | `net_price_received` | increase | short–medium | RS-16, CR-6 | whole-unit STR and rooms or capped primary lets: `substitute`, partial | A-32, A-35 |
| C-57 | `hosts.rooms` | `quantity_supplied` (room-nights) | increase | short–medium | CR-9, CR-4c, CR-6 | as C-39 | A-32, A-36 |
| C-58 | `sellers.prospective` (room lets) | `entry_rate` | increase | medium | CR-4, CR-7a | as C-39 | A-32, A-36 |
| C-40 | `hosts.non_primary` (owners when the ban became expected) | `asset_value` | decrease | short (part from 3 November, the rest at 8 December 2026) | CR-1, CR-7c, CR-10c, SB-4 | — | A-1, A-30 |
| C-41 | `hosts.duplex` (owners) | `asset_value` (two-unit buildings with a let second unit) | U1-a: ambiguous; U1-b: decrease | short | CR-1, CR-7c, CR-10c, CR-12b | — | A-30, A-32 |
| C-42 | `buyers.prospective` (homes in the beach districts) | `price_paid` (home purchases), not counting effects through `proximity` | decrease | short–medium | CR-7c, CR-8b, OC-7, CR-6 | investor and owner-occupier demand: `same_market_other_segment` | A-21, A-30, A-37 |
| C-53 | `buyers.prospective` (homes in the beach districts) | `price_paid` (home purchases), all chains | ambiguous | short–medium | CR-7c, CR-9 (proximity), CR-12b, CR-12d | as C-42; `proximity` (STR guests next door), Tier C | A-21, A-23, A-37 |
| C-43 | `homeowners.str_districts` | `asset_value` | ambiguous | short–medium | CR-7c, CR-10c, CR-9 (proximity), CR-12b, CR-12d | `proximity` (STR guests next door), Tier C | A-21, A-23 |
| C-54 | `homeowners.str_districts` | `asset_value`, not counting effects through `proximity` | decrease | short–medium | CR-1, CR-7c, CR-10c | — | A-21, A-30 |
| C-44 | `hosts.non_primary` (owners who keep their units) | `return_on_capital` | decrease | short–medium | CR-3a, CR-7b | — | A-1, A-5 |
| C-62 | `guests.whole_unit` (staying in Elsdon) | `travel_time` | increase | short–medium | CR-4, CR-3a | as C-26 | A-10 |
| C-63 | `buyers.substitutes` (guests who would have stayed in hotels anyway) | `quantity_traded` (their hotel room-nights, peak season) | decrease | short–medium | CR-4c, CR-6 | as C-22 | A-8, A-9 |
| C-64 | `guests.extended`, `hosts.mid_term` | `quantity_traded` (furnished lets of 30 nights or more) | increase | short–medium | RS-16, RS-13, CR-12d | as C-38 | A-7 or A-31 (independent chains) |

**Hotels and the other lodging segments (C-22 to C-25, C-34 to C-39).** This is PC-8's question asked of a prohibition rather than a price control: where does the excluded demand go, and does the policy also push sellers into the segment it goes to? RS-16 asks it directly, and its Unless clause (RS-13) is the PC-8 Unless. The answer differs by segment:
- *Hotels.* Guests move from whole units to hotels (RS-1; CR-9). The policy pushes no sellers into hotels: an STR unit cannot become a hotel room. In peak season occupancy is 94% and rooms cannot be added for years (A-9), so the price rises (C-22, RS-16, CR-6), and guests who would have stayed in hotels anyway at the old peak price take fewer peak nights (C-63, CR-4c: with rooms fixed, the higher price rations them out). Off-peak, at about 65% occupancy, spare rooms can take guests at little added cost, so room-nights rise (C-23) but the off-peak price is not signed. RS-1's 0.8 clause asks for a supply premise before signing a traded quantity: off-peak spare capacity supplies it. The expected rise in yield is capitalized in hotel values from the introduction (C-24), and in the long run draws new rooms (C-25, A-25).
- *Long-term rentals.* Converting owners add units (C-6); no excluded guest wants a 12-month lease. Only RS-13 operates, so rent falls (C-34), more leases are signed (C-35), and incumbent landlords receive less (C-36) and see their buildings' value fall (C-37). Arithmetic for scale only: if half the 2,150 units convert, the long-term stock rises by about 1.8%.
- *Furnished lets of 30 nights or more.* Both chains operate: guests on stays of two to four weeks move up to 30-night lets (RS-16, A-31), and owners reshape lets to 30 nights (C-8, A-7), adding supply (RS-13). With 900 units in the segment and perhaps several hundred more pushed in, neither chain clearly dominates: RS-16's Unless clause gives **ambiguous** (C-38). The quantity is another matter: both chains push the number of such lets traded up (more guests want them, more owners offer them), so it is an **increase** (C-64; RS-16's Then gives `quantity_substitute` increase, and by CR-12d it holds if either chain's premise holds).
- *Rooms and primary-residence lets within the cap.* Guests turn to them (A-32), and no sellers are pushed in by the policy itself. CR-6's 0.9 clause on splitting a shift asks for a premise before the price and the quantity are signed separately: the nightly price rises because this supply cannot expand at the old price in the period (owners must be present for room lets, and primary lets are capped at 90 nights; A-35) (C-39), and room-nights let rise because owner-occupiers have rooms and nights they would let at a higher price (A-36) (C-57, CR-4c), which over time also draws owner-occupiers who did not let rooms into the market (C-58, CR-4: x: stay out, y: enter). The 0.8 version of this analysis excluded C-57 as "a supply response to the price, not a separate consequence of the policy"; that reason was wrong, since a response to a price the policy moves is a consequence of the policy (CR-9, then CR-4). K3's fee is a cost on the substitute itself (RS-16, 0.9), but it is fixed per host, not per night (CR-4, 0.8), so it is not an opposing chain on the nightly net price; it bears on whether a primary-residence host lists (C-17), which is why entry is signed only for room lets (C-58).

**Elsdon (C-26 to C-29, C-62).** RS-4: the ban burdens letting inside the line, so stays move outside (C-26), and guests who stay there travel farther to the beach districts (C-62). Elsdon hosts let more (C-27): by CR-6's 0.9 clause, the quantity half of the shift is signed with a premise that Elsdon's supply can expand, which its spare occupancy outside the peak supplies (A-39); the price half is not signed. Elsdon homes suited to STR gain value from the introduction (C-28), and as Elsdon owners move units from long-term leases into STR (A-29), Elsdon's long-term rents rise (C-29, RS-13 for withdrawn supply). C-29 is at depth 3 and is the last link followed there.

**Visitors and the businesses near them (C-30, C-31).** Some groups and families have no close substitute at the old price (A-11): they shorten or skip the trip (C-30, CR-4c). Visitors buy meals and goods near where they stay (A-12): those who move to hotels move that spending to the hotel districts, and those who stay away take it out of the city, so beach-district businesses sell less to visitors (C-31, CR-9 along the location complement; RS-9, whose 0.9 clause covers purchases tied to a location: the lodging decision carries the nearby purchases with it). The same clause asks for the new occupants' purchases as the opposing chain: units converted to 12-month leases (C-6) house residents who buy meals and goods near home (A-33, with A-5). Total purchases near those units are therefore **ambiguous** (C-52); the visitors' item alone is a decrease (C-31), recorded separately (CR-12, 0.8, two items in one variable). Hotel-district businesses gain part of the visitors' spending; that chain is not followed (depth 3).

**Labor (C-32, C-33).** Cleaning and management are inputs to STR nights (CR-9): at least one of employment or hours falls (RS-6 group). Hotel staff gain at least one of them (OC-5). The hotel side is an existing activity, so the group form applies (OC-5, 0.8).

**Values and both sides of the revaluation (C-40 to C-44).** The yield of a non-primary unit falls from STR net to its next-best use (about $30,000 to $20,000 a year for most). By CR-1's 0.8 clarification, the operation is dated July 2027, but the asset's value moves when the ban becomes expected (CR-7c, CR-10c): part of the way when six of nine members sponsored it, the rest at enactment (C-40, A-30). The loss is borne by owners at that time; later buyers pay the lower price (C-42), which is the other side of the revaluation (CR-8b, OC-7). Some owners sell rather than lease, let mid-term or hold (C-60, CR-4, x: hold, y: sell; A-37), and investors' demand falls (C-61); both push the price of beach-district homes down. Owners who keep their units earn less on the capital they put in (C-44); in the long run, returns on capital are equalized and no lasting change is signed. Two-unit buildings (C-41): under U1-b the second unit loses its short-let use, and its value falls. Under U1-a it keeps 90 nights, at the higher nightly rate lawful lets now fetch (C-39, A-32), while buyers who would have let it for more than 90 nights lose that option and the owner pays K3's fee. Two derived chains oppose, so the sign under U1-a is **ambiguous** (CR-12b); the 0.8 version signed a decrease under both readings without combining the price chain it had itself recorded.

**Neighbors, owner-occupied homes and home prices (C-42, C-43, C-53, C-54).** Two chains reach the value of owner-occupied homes in the beach districts, and the same two reach the price buyers pay for them:
- (−) CR-7c: every home there loses the option of being let short-term, valued by the investors who made about 30% of recent purchases (A-21). Tier B.
- (+) A home whose neighbor would have been an STR unit is now more likely to have a long-term tenant or an owner next door. Some buyers value fewer transient neighbors (A-23). The relation is `proximity`: the change reaches the neighbor through physical nearness, not exchange. CR-9's 0.7 clarification admits it at Tier C, pending Q20.

CR-12's 0.9 clarification (Tier C against Tier B) settles how they combine: record two consequences per key. The Tier B chain's sign stays at Tier B, qualified "not counting effects through `proximity`": a **decrease** in owner-occupiers' home values (C-54) and in the price buyers pay (C-42, where more homes offered for sale, C-60, add to the fall in investor bids). The combined sign is recorded at Tier C: the proximity chain, with its premise at p ≥ 0.5 (A-23), opposes, and no dominance premise covers it, so it is **ambiguous** (C-43 for values, C-53 for prices). The Tier C chain does not lower the tier of C-42 or C-54, and is not raised by the combination. The 0.8 version signed the price (C-42) at Tier B without the proximity chain and the value (C-43) at Tier C with it, an inconsistency the 0.9 rule removes. The amenity itself (quieter streets) has no variable in 2.4 and is out of scope; it is a Tier C note, not a consequence. The 1,500 nuisance complaints a year about STR units are a record of neighbors acting (CR-2), which is evidence that the proximity chain has a sign for some of them; CR-9 gives no way for such evidence to raise the chain's tier (Gaps found, b).

Stopping points: C-29 (depth 3, Elsdon tenants); hotel-district businesses (depth 3); buyers of the homes sold by converting owners beyond C-42 (OC-7's further chain needs a premise on what they would have bought, not followed); the university's housing office (diffuse).

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `guests.whole_unit`, `hosts.non_primary`, `quantity_traded` (bookings in the window for July–September stays), short | Pull-forward into the protected window (K1 transition clause; A-15). | Owners converting or selling refuse summer bookings (A-16). | None | **ambiguous** (C-18). RS-8's Unless clause: the policy improves the earlier window, and a second timing chain opposes it (0.9: a second incentive the policy meets). |
| `guests.whole_unit`, `hosts.non_primary`, `quantity_traded` (stays before 1 July 2027), short | Guests move later trips forward (A-17). | Owners end short lets early for a lease or a sale (A-16). | None | **ambiguous** (C-19). |
| `guests.extended`, `price_paid` (30-night-plus lets), short–medium | Extended-stay guests move in (RS-16, A-31). | Owners reshape lets to 30 nights (RS-13, C-8, A-7). | None | **ambiguous** (C-38). RS-16 Unless. |
| `homeowners.str_districts`, `asset_value`, short–medium | Fewer transient neighbors (`proximity`, Tier C; A-23). | Loss of the option to let short-term (CR-7c; A-21). | None | **ambiguous**, Tier C (C-43). Not counting effects through `proximity`: **decrease**, Tier B (C-54). CR-12 (0.9), Tier C against Tier B. |
| `buyers.prospective`, `price_paid` (beach-district homes), short–medium | Buyers who value fewer transient neighbors bid more (`proximity`, Tier C; A-23). | Fewer investor bids (A-21, C-61); more homes offered (A-37, C-60). | None | **ambiguous**, Tier C (C-53). Not counting effects through `proximity`: **decrease**, Tier B (C-42). CR-12 (0.9). |
| `hosts.duplex` (90 nights or fewer), `quantity_supplied`, short, U1-a | Higher nightly price for lawful lets (C-39; A-32). | K3 fee and proof, a fixed cost per outlet above R1's (CR-4, 0.8; A-2). | None | U1-a: **ambiguous**; U1-b: **decrease** (C-4). |
| `hosts.duplex`, `asset_value`, short, U1-a | Higher nightly rate on up to 90 nights (A-32). | Nights above 90 removed; K3 fee (A-1, A-2). | None | U1-a: **ambiguous**; U1-b: **decrease** (C-41). |
| `sellers.complements` (beach districts), `quantity_traded`, medium | Residents of units moved to 12-month leases buy near home (A-33, A-5). | Fewer visitors buy near their lodging (A-12, with A-10 or A-11). | None | **ambiguous** (C-52). The visitors' item alone is **decrease** (C-31), recorded separately (CR-12, 0.8, two items). |
| `officials.enforcement` (general fund), `non_tax_receipts`, short | Fines (C-50; A-19). | Registration fees: K3's $250 from at most about 900 registrants replaces R1's $150 from the R1 registrants among about 3,050 whole-unit hosts (C-55; A-34). | None | **ambiguous** (C-56). Each item signed separately (CR-12, 0.8, two items). |
| `officials.enforcement` (Code Enforcement), `enforcement_cost`, short | Complaints about unlawful lets investigated (K4; A-19). | Fewer nuisance complaints about STR units under R3, as units leave (A-18). | Arithmetic attempted, not decisive (section 9) | **ambiguous** (C-47). OC-3 (0.8), right baseline. |
| `neighbors`, `compliance_cost` (time filing complaints), short | Complaints about unlawful lets (A-19). | Fewer nuisance complaints (A-18). | None | **ambiguous** (C-48). |
| `taxpayers`, recipients of other general-fund spending, `tax_revenue` (TOT), short–medium | Hotel room-nights and rates rise (C-22, C-23). | STR TOT lost (C-2); stays moved to Elsdon (C-26) and trips not taken (C-30) are not taxed by Saltmere. | None (TX-10: part of the spending moves to taxed hotels) | **ambiguous** (C-49). |
| `buyers.substitutes`, `price_paid` (hotels), long | — | New rooms (C-25). | CR-12g | **Not signed** at the long horizon; C-22 is short–medium only. |
| `tenants.prospective`, `price_paid` (long-term rent), medium | None found. Checked: no chain moves guests or tenants into 12-month leases; sales to owner-occupiers (C-42) lower rental demand too. | Converted units (C-6). | None needed | **decrease** (C-34). |
| `hosts.non_primary`, `asset_value`, short | None found. | Loss of short-let yield (C-40). | None needed | **decrease** (C-40). |

The final check before the report (workflow) was run on every consequence:
1. *Uncombined chains:* the rows above; in addition, `quantity_supplied` of non-primary units (C-1) has no (+) chain, and `hotels`' `quantity_traded` has no (−) chain (fewer visitors in C-30 were STR guests, not hotel guests). Rechecked under 0.9 after the core-only comparison: the 0.8 version left the higher nightly price (C-39) uncombined with two-unit owners under U1-a (C-4, C-41), the proximity chain uncombined with home prices (C-42), and residents' purchases uncombined with beach-district sales (C-31); all three are now in the table.
2. *Groups:* C-32, C-33 recorded as groups.
3. *Baseline:* every sign is against Saltmere without the ordinance, with R1 to R3 in force. Enforcement (C-47) is compared with R3 enforcement, not with zero.
4. *Worse off is not poorer:* hosts' loss is recorded as `return_on_capital` and `asset_value`, not `resources_available_other_uses`; only fines (C-51) and the appropriation (C-46) are signed on means.
5. *Timing shifts:* C-18 to C-20 per window.
6. *Both sides:* registration fees (C-17, C-55, against R1's fees, not against none), fines (C-50, C-51), the appropriation (C-45, C-46), the revaluation (C-40, C-42), refunds (C-21: the money is returned, so neither side's means change).
7. *Every core rule for every class:* CR-7c on hosts, hotels, Elsdon owners, landlords, homeowners, two-unit owners (C-24, C-28, C-37, C-40 to C-43); CR-6 in hotels, rooms, mid-term and long-term segments; CR-9 to inputs, complements, neighbors.
8. *Unstated premises:* the "some actors at the margin" premise for each response is in section 10 (A-5, A-6, A-7, A-15 to A-17, A-27, A-36 to A-38), and the supply premises CR-6 (0.9) asks for before a price or a quantity is signed alone (A-9, A-35, A-39).

## 8. Time structure

- **Introduction to enactment (November–December 2026).** Values of non-primary units fall part of the way when a majority sponsors the ordinance and the rest at enactment (C-40); hotel and Elsdon values rise at the same moments (C-24, C-28). The operation itself is dated 1 July 2027 (CR-1, 0.8): before then no option is removed, and no host's current lets are unlawful.
- **The window (to 30 June 2027).** Summer bookings are pulled into it under the transition clause while converting owners withdraw from summer lets, so bookings in the window and stays before July are both ambiguous (C-18, C-19). Owners plan conversions around the August–September leasing season; second-home owners decide whether to keep their weeks and leave the home empty (C-7).
- **1 July to 30 September 2027.** Only stays booked before 1 July for non-primary units continue (C-20). Primary-residence hosts register (C-17) and have a cap of 45 nights for the half-year. Platforms begin checks and reports (C-16).
- **From 1 October 2027.** The ban is complete for non-primary units (C-1). Converted units reach the long-term market over the following leasing seasons (C-6, C-34); hotel prices respond at once in peak seasons (C-22).
- **Erosion.** The fines are fixed in money (TS-3), while STR rates follow tourism prices, so the expected penalty under complaint-only enforcement falls relative to the gain from breach over time, and breach (C-9, C-10) grows in the long run unless fines are raised. The 90-night cap and the 30-night line are not money amounts and do not erode.
- **Long run.** Hotels add rooms if sites can be found (C-25), and the peak-season premium (C-22) narrows. Returns on capital in lodging and housing are equalized (CR-7a); the capital loss (C-40) and gain (C-24) stay with those who held the assets when the ban became expected.

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-45 | `officials.enforcement` (Registry Unit) | `enforcement_cost` | increase | What five staff and their systems would otherwise do. | OC-3 |
| C-46 | `taxpayers`, recipients of other general-fund spending | `resources_available_other_uses` | at_least_one_decrease | What the $520,000 a year would otherwise have funded. The record names no tax, so the payers are a group (OC-1, 0.8). | OC-3, OC-1 |
| C-47 | `officials.enforcement` (Code Enforcement) | `enforcement_cost` (complaint investigations) | ambiguous | On a fixed budget, any net increase is taken from other code enforcement (OC-3, fixed budget); a net decrease frees it. | OC-3, CR-12b |
| C-48 | `neighbors` | `compliance_cost` (time spent complaining) | ambiguous | Their time. | OC-2, CR-8c, CR-12b |
| C-49 | `taxpayers`, recipients of other general-fund spending | `tax_revenue` (TOT) | ambiguous | — | TX-10, CR-8b, CR-12b |
| C-50 | `officials.enforcement` (general fund) | `non_tax_receipts` (K4 fines) | increase | Nothing; receipts. | CR-8b |
| C-55 | `officials.enforcement` (general fund) | `non_tax_receipts` (registration fees for whole units, K3 against R1) | decrease | — | CR-8b, CR-12e |
| C-56 | `officials.enforcement` (general fund) | `non_tax_receipts` (fines and registration fees together) | ambiguous | — | CR-8b, CR-12b |
| C-51 | `hosts.fined` | `resources_available_other_uses` | decrease | What the fines would have bought; a sum they cannot avoid once imposed. | CR-8b, CR-3c |

**Enforcement against the right baseline (C-47).** OC-3's 0.8 clause asks for the comparison with enforcement without the policy. Without the ordinance, Code Enforcement investigates about 1,500 nuisance complaints a year about STR units, about 3,750 staff hours. With it:
- (−) As non-primary units leave, nuisance complaints about them fall. If the rate per operating unit holds (A-18) and about 70% of whole-unit listings stop, about 1,050 fewer complaints, about 2,600 hours saved.
- (+) Complaints about unlawful lets must be investigated (A-19): the city projects 400 to 1,200 a year, at about 3 hours each (requests for platform data, site visits, hearings), 1,200 to 3,600 hours.

The break-even is about 870 complaints, inside the projected range. The figures do not settle it, so arithmetic supplies no dominance premise (CR-12e) and the sign is **ambiguous**. On a fixed budget, OC-3's 0.9 clause says any net increase is taken from some other use of Code Enforcement's time (slower handling of other complaints, fewer other inspections), a group with `at_least_one_as_stated`, and not by default from less enforcement of other rules; a net decrease frees that time. With the net sign ambiguous, the burden on those other uses has the same ambiguous sign and is not recorded separately.

**Neighbors' time (C-48).** The same two chains apply to the complainants: complaint-only enforcement moves the work of detection to neighbors (CR-8c), while fewer STR units mean fewer nuisance complaints. OC-3's right-baseline clause is written for officials; it is applied here to complainants by the same derivation (CR-8c against the counterfactual's use of the same means).

**TOT (C-49).** About $18.7 million a year of STR TOT is lost as whole units stop. Part of the spending moves to hotels, taxed at the same 12% and at higher peak prices; part goes to Elsdon or is not spent in Saltmere. TX-10: where part moves to taxed goods, the combined sign is ambiguous. Hotels' peak capacity limits the gain, but the higher peak rate applies to every hotel night, so no arithmetic on the record's figures settles it.

**Registration fees and fines (C-50, C-55, C-56).** K3 replaces R1 for whole units, so the baseline for registration fees is R1's, not none. Without the ordinance, R1 collects $150 from each registered whole-unit host: about 1,980 of about 3,050 if the 65% registration rate holds for whole units, about $297,000. With it, K3 collects $250 from at most about 900 registrants (550 primary-residence hosts and, under U1-a, 350 two-unit owners), about $225,000, or about $137,500 under U1-b. Registration fees fall if more than about 49% of whole-unit hosts were registered under R1 (A-34): arithmetic on the case's figures with that premise, since the 65% is a rate for all hosts and its use for the whole-unit subclass is a premise (CR-12e, 0.8, counts over a distribution) (C-55). Fines are a new receipt (C-50). The two items push opposite ways, so total receipts are **ambiguous** (C-56). The 0.8 version signed fees and fines together as an increase against a baseline without R1.

**Prevented exchanges.** The stays no longer made are C-2 (OC-4); the trips not taken are C-30. They are not listed again.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | For most non-primary units, short lets yield more than any lawful alternative (about $30,000 net against about $20,000). | binding | 0.9 | Platform revenue data; long-term rents for comparable units. | Most consequences shrink; owners would already have converted. |
| A-2 | Platforms comply with K2: they display numbers, remove listings on notice and report nights. | enforcement | 0.85 | The fine per listing per day exceeds a platform's fee per listing (about $7,600 a year); compliance with similar rules elsewhere. | C-1 to C-5, C-16, C-17 and C-20 shrink; C-9 grows; C-17 holds only for R1 registrants. |
| A-3 | For some units, complaints are unlikely (detached homes, neighbors who are absent or also let), so the expected fine is below the gain from breach. | enforcement | 0.75 | Share of STR units in detached homes; complaint rates by building type under R3. | C-9 to C-14 and C-51 are not reported. |
| A-4 | Some guests keep wanting whole units in Saltmere enough to book them directly. | substitutability | 0.7 | Repeat-guest shares; direct-booking sites. | C-10 to C-14 are not reported. |
| A-5 | Most non-primary units can be let on 12-month leases, and some owners choose that over sale, vacancy or mid-term lets. | alternative_uses | 0.85 | Unit types; condominium rules; long-term demand. | C-6, C-34 to C-37 and C-44 are not reported; C-52 loses its (+) chain and becomes a decrease. |
| A-6 | Some second-home owners value their own weeks enough to keep the home and leave it empty the rest of the year. | other | 0.7 | Owners' use patterns in the platform data (blocked calendar weeks). | C-7 is not reported. |
| A-7 | Some owners can let for 30 nights or more (traveling nurses, university visitors, relocations). | substitutability | 0.75 | Mid-term listings and hospital and university demand. | C-8 and the (−) chain of C-38 fail; C-64 keeps the A-31 chain. |
| A-8 | Hotels are a substitute for whole units for some guests. | substitutability | 0.8 | Guest surveys; group sizes. | C-22 to C-25, C-33 and C-63 are not reported. |
| A-9 | Hotel rooms cannot be added in the short to medium run, and peak-season occupancy is near capacity (94%). | durability | 0.85 | Occupancy data; planning times of three to five years. | C-22, C-63 and part of C-24 fail. |
| A-10 | Elsdon is near enough for some guests (12 km from Harbor). | mobility | 0.7 | Travel times; Elsdon listings near the city line. | C-26 to C-29 and C-62 are not reported. |
| A-11 | Some visitors (large groups, families) have no close substitute at the old price and shorten or skip trips. | substitutability | 0.65 | Group sizes in STR bookings; hotel suites available. | C-30 and C-31 are not reported. |
| A-12 | Visitors buy meals and goods near their lodging. | other | 0.7 | Card-spending data by district. | C-31 is not reported; C-52 loses its (−) chain. |
| A-13 | Units added to the long-term market are not offset by withdrawals elsewhere. | substitutability | 0.75 | No other policy change in the long-term market. | C-34 to C-37 weaken. |
| A-14 | Hosts, platforms, hotels and neighborhood associations can organize at a cost below their stake. | other | 0.85 | Their activity on the ordinance. | C-15 is not reported. |
| A-15 | Guests can book summer stays earlier than they otherwise would. | expectations | 0.7 | Booking lead times. | The (+) chain of C-18 fails; C-18 would be a decrease. |
| A-16 | Some owners planning to convert or sell end or refuse summer lets to have the unit free for the August–September leasing season or a sale. | other | 0.6 | Leasing-season timing; listing data for sales. | The (−) chains of C-18 and C-19 fail; C-18 and C-19 would be increases. |
| A-17 | Some guests who prefer whole units move a later trip to before 1 July 2027. | other | 0.55 | Share of trips with flexible dates. | The (+) chain of C-19 fails; C-19 would be a decrease. |
| A-18 | Nuisance complaints per operating STR unit stay near the 2025 rate. | other | 0.75 | R3 complaint records, 2022–2025. | The (−) chains of C-47 and C-48 weaken. |
| A-19 | Neighbors file complaints about unlawful lets in meaningful numbers; some lead to fines. | enforcement | 0.8 | The city's projection of 400 to 1,200 a year; neighborhood associations' support. | C-47 and C-48 become decreases; C-50 (fines) and C-51 are not reported; C-56 becomes a decrease with A-34. |
| A-20 | The $520,000 is new general-fund money. | revenue_use | 0.9 | §8. | C-46 is not reported; other spending in the department falls instead. |
| A-21 | Investors are a material part of demand for homes in the beach districts. | other | 0.8 | About 30% of 2023–2025 purchases by non-occupants. | C-61 is not reported; C-42, C-54 and the (−) chains of C-43 and C-53 weaken. |
| A-22 | Hosts listing on more than one platform can exceed 90 nights without the per-platform reports revealing it. | enforcement | 0.6 | K2 reports are per platform; the city has no plan to aggregate them. | C-9 weakens to listings under another unit's registration. |
| A-23 | Some buyers value fewer transient neighbors (the `proximity` chain). | other | 0.6 | Neighborhood associations' support; the complaint record (R3). | C-43 and C-53 lose their (+) chain; with C-54 and C-42 they become decreases at Tier B. |
| A-24 | Bookings exist for stays after 30 September 2027 made before the introduction. | other | 0.9 | About 6% of a year's nights are booked more than nine months ahead. | C-21 is not reported. |
| A-25 | Hotels can obtain sites and permits to add rooms in the long run. | alternative_uses | 0.55 | Zoning for hotels in the beach districts. | C-25 is not reported. |
| A-26 | Cleaning and management firms adjust their labor to the nights they service. | alternative_uses | 0.8 | Staffing practice. | C-32 is not reported. |
| A-27 | Hosts in breach can screen guests on traits that predict complaints, and do not set prices to cover the risk guest by guest. | other | 0.6 | Off-platform booking practice; hosts' house rules. | C-14 is not reported. |
| A-28 | Rivals file complaints against lawful hosts to raise their costs. | other | 0.3 | Complaint records give no evidence of it. | Below the cut-off; not reported. |
| A-29 | Some Elsdon owners move units from long-term leases into STR. | alternative_uses | 0.6 | Elsdon's ratio of STR to long-term returns. | C-29 is not reported. |
| A-30 | Values of STR units, hotels and Elsdon homes rest on expected yields, and passage was likely from the introduction (six of nine sponsors). | expectations | 0.8 | Sale prices as multiples of earnings; sponsors' count. | C-24, C-28, C-37, C-40 to C-42 move later (at enactment) or not at all. |
| A-31 | Some guests on stays of two to four weeks can extend to 30 nights. | substitutability | 0.6 | Stay-length distribution; who those guests are (contract workers, relocations). | The (+) chain of C-38 fails; C-38 would be a decrease; C-64 keeps the A-7 chain. |
| A-32 | Rooms in occupied homes and primary-residence lets are a substitute for whole units for some guests. | substitutability | 0.75 | Guest overlap on platforms. | C-39, C-57 and C-58 are not reported; C-4 and C-41 under U1-a lose their (+) chain and become decreases. |
| A-33 | Residents of units moved to 12-month leases buy some meals and goods near home. | other | 0.8 | Card-spending data by district cover residents too; residents shop locally. | C-52 loses its (+) chain and becomes a decrease. |
| A-34 | More than about 49% of whole-unit hosts were registered under R1 (the rate for all hosts is about 65%), so R1's fees from whole units exceed the most K3 can raise. | other | 0.75 | R1 registration records by listing type. | C-55 is not signed; C-56 may become an increase. |
| A-35 | The supply of rooms in occupied homes and of primary-residence lets cannot expand at the old nightly price in the period (owners must be present; the 90-night cap). | durability | 0.7 | Occupancy of room listings; the cap. | C-39 is not signed; only the group (price or quantity) holds. |
| A-36 | Some owner-occupiers have rooms or nights they would let at a higher nightly price. | alternative_uses | 0.7 | Room listings' blocked nights; homes with spare rooms. | C-57 and C-58 are not reported. |
| A-37 | Some owners of non-primary units sell rather than lease, let mid-term or hold. | alternative_uses | 0.7 | Listings for sale in the beach districts; the investor share of purchases (A-21); the fall in yield (A-1). | C-60 is not reported; C-42 and C-53 lose part of their (−) chain. |
| A-38 | Some owners reshape short stays into nominal 30-night contracts, or claim primary residence on documents they can change at low cost. | substitutability | 0.6 | K1 defines the ban by contract length and residence; K3's proofs; K4 enforces only on complaint. | C-59 is not reported. |
| A-39 | Elsdon STR supply can expand at close to the old price for part of the year (spare occupancy outside the peak). | alternative_uses | 0.7 | Elsdon occupancy by season. | C-27 is not signed; only the group (Elsdon price or quantity) holds. |

## 11. Report

**The policy.** From 1 July 2027, Saltmere bans letting whole homes for under 30 nights, except a registered owner's primary residence for up to 90 nights a year. Stays booked before July may go ahead until 30 September 2027; later bookings are cancelled and refunded. Platforms must show a registration number on each listing, remove listings the city flags, and report nights, or pay $1,000 per listing per day. Hosts are fined only when someone complains. A new registry costs $520,000 a year from the general fund. Whether the second unit of a two-unit building whose owner lives in the other counts as the owner's residence is unclear.

**Visible consequences.** About 2,150 whole homes stop being let to visitors (C-1, C-2), and primary-residence hosts who let more than 90 nights cut back (C-3, C-5).

**Invisible consequences.**
- *Owners.* Most convert to long-term leases (C-6), some to lets of a month or more (C-8); second-home owners who keep their own weeks leave the home empty the rest of the year (C-7); some sell (C-60). Owners when the ban became expected bear a fall in their units' value (C-40) and earn less on their capital (C-44). Primary-residence hosts pay more to register than under the old registration (C-17).
- *Breach.* Some hosts exceed the cap on platforms or list under another unit's number (C-9); others let off-platform (C-10), where guests search harder, know less about what they book and settle disputes outside the courts (C-11 to C-13). Some dress short stays up as 30-night contracts or claim a residence they do not have (C-59). Because only complaints trigger enforcement, breach concentrates where neighbors are absent, and hosts screen guests for quietness (C-14).
- *Guests and visitors.* Some guests switch to hotels, where peak-season prices rise (C-22, C-23) and guests who would have stayed there anyway get fewer peak nights (C-63), or to Elsdon (C-26), where they travel farther (C-62); some skip or shorten trips (C-30), and beach-district shops and restaurants sell less to visitors (C-31). Guests with bookings after September 2027 must rebook (C-21).
- *Other lodging.* Hotels gain value from the introduction (C-24) and add rooms in the long run (C-25); their staff work more (C-33). Rooms in occupied homes and capped primary lets fetch more (C-39); more rooms are let (C-57) and more owner-occupiers start letting them (C-58). More furnished lets of a month or more are made (C-64). Elsdon hosts let more, Elsdon homes gain value, and Elsdon tenants pay more (C-27 to C-29). STR cleaners and managers lose work (C-32).
- *Housing.* Long-term rents are lower than they would have been (C-34) and more leases are signed (C-35); incumbent landlords receive less (C-36) and their buildings are worth less (C-37). Investors want fewer homes in the beach districts (C-61); not counting what buyers pay for fewer transient neighbors, buyers of homes there pay less (C-42) and owner-occupiers' homes are worth less (C-54).
- *The city.* Registry costs, paid by taxpayers or recipients of other general-fund spending (C-45, C-46); fines received (C-50) from those fined (C-51), while registration fees fall against the old registration (C-55); lobbying over the cap, the reading of U1 and enforcement (C-15); platforms' compliance work (C-16).

**Ambiguous effects.** Bookings and stays in the eight-month window (C-18, C-19): the transition clause pulls summer bookings forward while converting owners withdraw. The price of month-long furnished lets (C-38): demand and supply both move in. Values and prices of owner-occupied homes in the beach districts once fewer transient neighbors are counted (C-43, C-53, Tier C): the lost option to let against fewer transient neighbors. Total sales of beach-district businesses (C-52): fewer visitors against new residents of converted units. The city's fee and fine receipts together (C-56). Code Enforcement's workload and neighbors' complaint time (C-47, C-48): new complaints about unlawful lets against fewer nuisance complaints. TOT revenue (C-49).

**Per reading of U1.** Two-unit owners who let 90 nights or fewer: if the building is the residence (U1-a), a higher nightly price against a higher registration cost, so their nights are ambiguous; if the unit is (U1-b), a ban (C-4). The value of two-unit buildings is ambiguous under U1-a and falls under U1-b (C-41).

**Key conditions.** That short lets pay more than any lawful use (A-1, p = 0.9) and that platforms comply (A-2, p = 0.85) drive the direct effects. Breach rests on complaints being unlikely for some units (A-3, p = 0.75). The effect on long-term rents rests on owners converting rather than selling or leaving units empty (A-5, p = 0.85).

**What this analysis cannot say.** How many units convert, how much rents fall or hotel prices rise; whether neighbors' gain in quiet outweighs owners' and guests' losses; noise, safety and neighborhood character as such (out of scope for version 1); whether the ordinance is desirable.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | hosts.non_primary | quantity_supplied (lawful whole-unit STR nights) | decrease | short | visible | B | CR-1, CR-4 | A-1, A-2 |
| C-2 | guests.whole_unit, hosts.non_primary, platforms | quantity_traded (whole-unit STR nights via platforms) | decrease | short | visible | B | CR-5a, OC-4 | A-1, A-2 |
| C-3 | hosts.primary_over90 | quantity_supplied (nights above 90) | decrease | short | visible | B | CR-1, CR-4 | A-2 |
| C-4 | hosts.duplex (90 nights or fewer) | quantity_supplied (STR nights) | U1-a: ambiguous; U1-b: decrease | short | visible | B | CR-1, CR-4, CR-9, CR-12b | A-2, A-32 |
| C-5 | hosts.duplex (more than 90 nights) | quantity_supplied (STR nights) | decrease | short | visible | B | CR-1, CR-4 | A-2 |
| C-6 | hosts.converting | quantity_supplied (units on 12-month leases) | increase | short–medium | invisible | B | RS-6, CR-4, CR-7a | A-1, A-5 |
| C-7 | hosts.second_home | units_held_vacant | increase | short–medium | invisible | B | CR-1, CR-4 | A-1, A-6 |
| C-8 | hosts.mid_term | reclassification (lets of 30 nights or more) | increase | short | invisible | B | RS-5 | A-1, A-7 |
| C-9 | hosts.primary_over90, hosts using another unit's registration | legal_breach (on-platform lets beyond the cap or exception) | increase | short–medium | invisible | B | RS-3, RS-20, CR-1, CR-4 | A-3, A-22 |
| C-10 | hosts.in_breach | informal_activity (off-platform whole-unit lets) | increase | short–medium | invisible | B | RS-3, RS-20, EN-7, CR-1, CR-4 | A-3, A-4 |
| C-11 | guests.off_platform | search_cost | increase | short | invisible | B | RS-10 | A-3, A-4 |
| C-12 | guests.off_platform | quality_information | decrease | short | invisible | B | RS-10, CR-11b | A-3, A-4 |
| C-13 | guests.off_platform | disputes_settled_outside_courts | increase | short | invisible | B | RS-10 | A-3, A-4 |
| C-14 | guests.off_platform | allocation_by_non_price_criteria (screening for quietness) | increase | short–medium | invisible | B | RS-20, CR-4, CR-6 | A-3, A-4, A-27 |
| C-15 | hosts, platforms, hotels, neighborhood associations | lobbying_effort | increase | medium | invisible | B | RS-7 | A-14 |
| C-16 | platforms | compliance_cost | increase | short | invisible | B | CR-1, CR-8c | A-2 |
| C-17 | hosts.primary_over90, hosts.primary_under90, hosts.duplex (U1-a) | compliance_cost (registration, against R1) | increase | short | invisible | B | CR-1, CR-8c, CR-4 | A-2 |
| C-18 | guests.whole_unit, hosts.non_primary | quantity_traded (window bookings for July–September stays) | ambiguous | short | invisible | B | RS-8, CR-10a, CR-12b | A-15, A-16 |
| C-19 | guests.whole_unit, hosts.non_primary | quantity_traded (stays before 1 July 2027) | ambiguous | short | invisible | B | RS-8, CR-10a, CR-12b | A-16, A-17 |
| C-20 | guests.whole_unit, hosts.non_primary | quantity_traded (bookings from 1 July for stays to 30 September) | decrease | short | invisible | B | RS-8, CR-1 | A-2 |
| C-21 | guests.prebooked | search_cost (rebooking) | increase | short | invisible | B | CR-1, CR-5a | A-24 |
| C-22 | buyers.substitutes (hotel guests) | price_paid (hotel rooms, peak season) | increase | short–medium | invisible | B | RS-16, CR-9, CR-6 | A-8, A-9 |
| C-23 | hotels | quantity_traded (room-nights) | increase | short–medium | invisible | B | RS-1, RS-16 | A-8 |
| C-24 | hotels (owners) | asset_value | increase | short | invisible | B | CR-7c, CR-10c, SB-4 | A-8, A-9, A-30 |
| C-25 | hotels | investment_target (new rooms) | increase | long | invisible | B | CR-7a, CR-4 | A-8, A-25 |
| C-26 | guests.whole_unit | cross_border_purchases (stays in Elsdon) | increase | short | invisible | B | RS-4 | A-10 |
| C-27 | neighboring_jurisdictions (Elsdon hosts) | quantity_supplied (STR nights) | increase | short–medium | invisible | B | RS-4, CR-7a, CR-6 | A-10, A-39 |
| C-28 | neighboring_jurisdictions (Elsdon owners) | asset_value (homes suited to STR) | increase | short | invisible | B | CR-7c, CR-10c | A-10, A-30 |
| C-29 | neighboring_jurisdictions (Elsdon tenants) | price_paid (long-term rent) | increase | medium | invisible | B | RS-13, CR-9 | A-10, A-29 |
| C-30 | guests.whole_unit | quantity_traded (trips to Saltmere) | decrease | short–medium | invisible | B | RS-1, CR-4c | A-11 |
| C-31 | sellers.complements (beach districts) | quantity_traded (visitors' purchases) | decrease | short–medium | invisible | B | CR-9, RS-9 | A-11, A-12 |
| C-32 | input_suppliers (cleaners, managers) | employment, hours_worked | at_least_one_decrease | short–medium | invisible | B | CR-9, RS-6 | A-1, A-26 |
| C-33 | hotels (staff) | employment, hours_worked | at_least_one_increase | short–medium | visible | B | OC-5, CR-9 | A-8 |
| C-34 | tenants.prospective | price_paid (long-term rent) | decrease | medium | invisible | B | RS-13, CR-6 | A-5, A-13 |
| C-35 | tenants.prospective | quantity_traded (12-month leases) | increase | medium | invisible | B | RS-13, CR-4c | A-5, A-13 |
| C-36 | landlords.long_term | net_price_received | decrease | medium | invisible | B | RS-13, CR-6 | A-5, A-13 |
| C-37 | landlords.long_term (owners) | asset_value (rental buildings) | decrease | short–medium | invisible | B | CR-7c, CR-10c | A-5, A-13, A-30 |
| C-38 | guests.extended | price_paid (lets of 30 nights or more) | ambiguous | short–medium | invisible | B | RS-16, RS-13, CR-12b | A-7, A-31 |
| C-39 | hosts.lawful | net_price_received | increase | short–medium | invisible | B | RS-16, CR-6 | A-32, A-35 |
| C-40 | hosts.non_primary (owners at introduction) | asset_value | decrease | short | invisible | B | CR-1, CR-7c, CR-10c, SB-4 | A-1, A-30 |
| C-41 | hosts.duplex (owners) | asset_value (two-unit buildings) | U1-a: ambiguous; U1-b: decrease | short | invisible | B | CR-1, CR-7c, CR-10c, CR-12b | A-30, A-32 |
| C-42 | buyers.prospective (homes, beach districts) | price_paid (home purchases, not counting effects through proximity) | decrease | short–medium | invisible | B | CR-7c, CR-8b, OC-7, CR-6 | A-21, A-30, A-37 |
| C-43 | homeowners.str_districts | asset_value | ambiguous | short–medium | invisible | C | CR-7c, CR-10c, CR-9 (proximity), CR-12b, CR-12d | A-21, A-23 |
| C-44 | hosts.non_primary (keeping units) | return_on_capital | decrease | short–medium | invisible | B | CR-3a, CR-7b | A-1, A-5 |
| C-45 | officials.enforcement (Registry Unit) | enforcement_cost | increase | short | invisible | A | OC-3 | none |
| C-46 | taxpayers, recipients of other general-fund spending | resources_available_other_uses | at_least_one_decrease | short | invisible | B | OC-3, OC-1 | A-20 |
| C-47 | officials.enforcement (Code Enforcement) | enforcement_cost (complaint investigations) | ambiguous | short | invisible | B | OC-3, CR-12b | A-18, A-19 |
| C-48 | neighbors | compliance_cost (time spent complaining) | ambiguous | short | invisible | B | OC-2, CR-8c, CR-12b | A-18, A-19 |
| C-49 | taxpayers, recipients of other general-fund spending | tax_revenue (TOT) | ambiguous | short–medium | invisible | B | TX-10, CR-8b, CR-12b | A-8, A-10, A-11 |
| C-50 | officials.enforcement (general fund) | non_tax_receipts (K4 fines) | increase | short | invisible | B | CR-8b | A-19 |
| C-51 | hosts.fined | resources_available_other_uses | decrease | short–medium | invisible | B | CR-8b, CR-3c | A-3, A-19 |
| C-52 | sellers.complements (beach districts) | quantity_traded (all purchases near converted units, visitors and residents) | ambiguous | medium | invisible | B | CR-9, RS-9, CR-12b | A-5, A-12, A-33 |
| C-53 | buyers.prospective (homes, beach districts) | price_paid (home purchases, all chains) | ambiguous | short–medium | invisible | C | CR-7c, CR-9 (proximity), CR-12b, CR-12d | A-21, A-23, A-37 |
| C-54 | homeowners.str_districts | asset_value (not counting effects through proximity) | decrease | short–medium | invisible | B | CR-1, CR-7c, CR-10c | A-21, A-30 |
| C-55 | officials.enforcement (general fund) | non_tax_receipts (registration fees, K3 against R1) | decrease | short | invisible | B | CR-8b, CR-12e | A-34 |
| C-56 | officials.enforcement (general fund) | non_tax_receipts (fines and registration fees) | ambiguous | short | invisible | B | CR-8b, CR-12b | A-19, A-34 |
| C-57 | hosts.rooms | quantity_supplied (room-nights) | increase | short–medium | invisible | B | CR-9, CR-4c, CR-6 | A-32, A-36 |
| C-58 | sellers.prospective (room lets) | entry_rate | increase | medium | invisible | B | CR-4, CR-7a | A-32, A-36 |
| C-59 | hosts.non_primary | reclassification (nominal 30-night contracts; residence claims) | increase | short–medium | invisible | B | RS-5, CR-4 | A-1, A-38 |
| C-60 | hosts.selling | quantity_supplied (homes offered for sale, beach districts) | increase | short–medium | invisible | B | CR-4, CR-7c | A-1, A-37 |
| C-61 | investors.home_buyers | quantity_demanded (homes in the beach districts) | decrease | short–medium | invisible | B | CR-1, CR-4, CR-7c | A-1, A-21 |
| C-62 | guests.whole_unit (staying in Elsdon) | travel_time | increase | short–medium | invisible | B | CR-4, CR-3a | A-10 |
| C-63 | buyers.substitutes (hotel guests anyway) | quantity_traded (their peak hotel room-nights) | decrease | short–medium | invisible | B | CR-4c, CR-6 | A-8, A-9 |
| C-64 | guests.extended, hosts.mid_term | quantity_traded (furnished lets of 30 nights or more) | increase | short–medium | invisible | B | RS-16, RS-13, CR-12d | A-7 or A-31 (independent chains) |

## Corrections after the core-only comparison

The core-only re-run (`05_examples_core/WE-044_short_term_rental_ban_core.md`) was compared with this analysis. Each correction below was checked against the core rules before it was applied; the catalog is now 0.9.

**Changed.**
- C-4: U1-a `no_change` → `ambiguous`. Under U1-a two-unit owners are lawful hosts: the higher nightly price (C-39) pushes their nights up, K3's fee above R1's pushes them down (CR-4, 0.8; CR-12b). `no_change` needs a derivation of no change (2.5).
- C-41: U1-a `decrease` → `ambiguous`, by the same two chains on the value of the second unit (CR-7c, CR-12b).
- C-42: kept as `decrease` at Tier B, now qualified "not counting effects through `proximity`" (CR-12, 0.9), with sales (C-60, A-37) added to its chain; the combined sign is the new C-53.
- C-43: unchanged in sign and tier (ambiguous, Tier C); its Tier B counterpart is the new C-54 (CR-12, 0.9).
- C-31: narrowed to visitors' purchases (decrease); the total with residents of converted units is the new C-52 (RS-9, 0.9, location complements).
- C-17: Tier A → Tier B on A-2, against R1's $150 rather than against no registration.
- C-50: narrowed to fines; registration fees (C-55) and the total (C-56) are new. The 0.8 version signed fees and fines together as an increase against a baseline without R1.
- C-27: supply premise added (A-39), as CR-6 (0.9, splitting a shift) requires before the quantity is signed alone.
- C-39: supply premise added (A-35), for the same reason; RS-16 (0.9, costs on the substitute) checked: K3's fee is fixed per host, so it does not oppose the nightly price.
- C-9, C-10, C-14: RS-20 (enforcement only on complaint, promoted in 0.9) cited; C-18: RS-8's 0.9 clause on a second timing incentive cited. No sign changes.
- C-47: text only. OC-3's 0.9 clause on a fixed budget (a group of other uses of the agency's time) replaces "other code enforcement".

**Added.** C-52 (beach-district purchases in total, ambiguous), C-53 (home prices, all chains, ambiguous, Tier C), C-54 (owner-occupiers' home values not counting proximity, decrease, Tier B), C-55 (registration fees, decrease, A-34), C-56 (fees and fines together, ambiguous), C-57 (room-nights let, increase), C-58 (entry of room hosts, increase), C-59 (sham 30-night contracts and residence claims, `reclassification`, increase), C-60 (homes offered for sale, increase), C-61 (investors' demand for beach-district homes, decrease), C-62 (Elsdon guests' travel time, increase), C-63 (peak hotel nights of guests who would have stayed there anyway, decrease), C-64 (furnished lets of 30 nights or more traded, increase). New assumptions A-33 to A-39. The 0.8 exclusion of room hosts' supply ("a supply response to the price, not a separate consequence") was wrong and is removed.

**Removed.** None.

**Comparison conclusions rejected or not applied.**
- C-42 (pattern C-42 should be `ambiguous`, Tier C): rejected in part. Under CR-12's 0.9 rule the Tier B sign is kept, qualified, and the ambiguous Tier C sign is recorded beside it (C-53), not in its place.
- Core C-20 (entry of room and primary-residence hosts): applied to room hosts only (C-58). Prospective primary-residence hosts face K3's fee above R1's against the higher price, so their entry is not signed without a dominance premise.
- C-19 (A-16 stretched to stays before July, cause A): not changed. RS-8's 0.9 clause says how to combine timing chains, not which premise covers that window, so 0.9 does not settle it.
- Core C-19 (total nights of primary-residence hosts, cause J): not added; 0.9 does not settle the choice of key.
- Core C-48 (Elsdon hosts' price, cause J): not added. CR-6 (0.9) signs that half only with a premise that Elsdon supply cannot expand, and the case's spare occupancy points the other way.
- Core C-27, C-33 and C-53 (cause J): not added; they are subsets of C-2 and C-1, or a depth choice, which 0.9 does not change.

## Gaps found

**(a) Calculus gaps (a step no core rule covers).** None. Every step was derived from CR-1 to CR-12 or from a pattern whose preconditions held. The step nearest to a gap was the neighbors' amenity (quieter streets): CR-9 (0.7) derives it along `proximity`, at Tier C pending Q20, so it is an open expert question already recorded (GAP-026-1), not a new gap.

**(b) Unclear core rules, including the 0.7 and 0.8 clarifications.**
1. *Rothbard type of a ban on letting one's own home.* The typology in 01_foundations.md calls an intervention autistic when it restricts "a person's own action, with no exchange involved". K1 prohibits an exchange (triangular), yet for second-home owners what it removes is a way of combining their own use with other people's, and the option they fall back to (own weeks, empty the rest) involves no exchange (C-7). CR-1 records the operation correctly (operation 1, dated); the typology has no word for "triangular in form, autistic in what the owner is left with". It did not change any sign.
2. *Proximity evidence and tier.* CR-9 (0.7) holds every `proximity` chain at Tier C. Here the record contains 1,500 complaints a year about STR units, which are actions by neighbors and so, by CR-2, demonstrated evidence that the chain has a sign for some of them. CR-9 gives no route by which such evidence lifts a chain's tier. C-43 stays Tier C. (Under 0.9, CR-12's rule for Tier C against Tier B settles how the chain enters a combination, C-42, C-43, C-53, C-54, but not whether evidence can lift its tier.)
3. *OC-3's right baseline runs through proximity.* The 0.8 clause's own example (complaints about backyard flocks) and C-47 here both depend on nuisance complaints falling when the activity falls, which is a `proximity` chain. This analysis kept C-47 at Tier B by treating the complaint rate per operating unit as an empirical premise (A-18) rather than deriving it from neighbors' rankings. The catalog should say whether that is allowed, or whether OC-3's right-baseline chain is Tier C whenever the old enforcement was complaint-driven.
4. *`legal_breach` against `informal_activity` under a prohibition with a permitted sub-class.* For lets beyond the cap or under another unit's number made through platforms, the trade runs through the legal market's channels; for lets off-platform, it does not. The analysis split them at the channel (C-9, C-10). 2.4 does not say where the line is.

**(c) Missing or wrong patterns.**
1. *Complaint-only enforcement* (candidate, 06_gaps.md 6.2e, from WE-029; promoted in 0.9 as RS-20). Needed a second time here (C-9, C-10, C-14): CR-1 (a risk equal to the probability of a complaint times the fine) and CR-4 (x: comply, y: violate) unit by unit, with the probability falling where complainants are absent. By the catalog's rule, this second use promotes it. Two additions this case suggests: (i) where the complainants are the people the rule protects, breach concentrates where they are absent, so the rule binds least where it protects least; (ii) the violator can lower the complaint probability by choosing counterparties (screening quiet guests, C-14), which is a non-price allocation of the illegal good. Also (iii) fines fixed in money erode against the gain from breach (TS-3).
2. *RS-16's Unless clause as PC-8 for a prohibition.* Worked as written for all four lodging segments: increase where only demand moves in (hotels, rooms), decrease where only supply is pushed in (long-term), ambiguous where both are (30-night lets). No pattern applied as written gave a sign that had to be overridden. PC-8 itself names only price controls; RS-16 covered the case without it.
3. *OC-3's right baseline for complainants.* OC-3 is written for `officials.enforcement`; the same comparison applied to complainants' time (C-48). A sentence in OC-3 or OC-2 would prompt it.

**(d) Vocabulary the ontology lacks.**
1. *Amenity to neighbors.* No variable for the change in a neighbor's situation through proximity (noise, traffic, transient neighbors); C-43 records only its capitalized value. Out of scope for version 1, but the out-of-scope list in 2.4 names health, safety, environment and nutrient intake, not amenity.
2. *Bookings as distinct from stays.* `quantity_traded` was qualified to tell bookings made in a window from stays taken in it (C-18 to C-20). The timing convention in 2.5 assumes one action per window; here the contract and its performance fall in different windows.
3. *Complaints.* No variable for complaints filed (also noted in WE-026); C-48 records complainants' time as `compliance_cost`, which fits imperfectly.

**(e) Test of 0.8.**
- *CR-1 0.8, dated operations.* Worked as written. Two dates (1 July for new bookings, 1 October for booked stays), and values moving at the introduction (C-40, C-24, C-28), followed directly from the clause.
- *CR-1 0.7, split by response.* Worked: hosts split into converting, mid-term, selling, second-home vacant and in breach.
- *CR-4 0.8, fixed cost per outlet.* Worked: the $250 registration bears on whether a primary-residence host lists, not on the nightly price (C-17).
- *CR-9 0.7, proximity at Tier C, and its use for asset values.* Needed interpretation: C-43 combines a Tier B and a Tier C chain; the analysis treated the Tier C chain as CR-12 kind (2) and gave the result Tier C (CR-12d). The clause does not say that this is how proximity chains enter a combination, nor whether record evidence (complaints) can lift the tier (b2), nor how it bears on OC-3's own example (b3).
- *CR-12 0.8, three kinds of opposing chain.* Worked as written for C-43 (kind 2, p ≥ 0.5, ambiguous) and for strategic complaints (kind 2 with p below 0.5, A-28: derived sign kept, chain recorded in section 10).
- *RS-8 0.8, opposing timing chains.* Needed interpretation, then worked. The Unless clause describes a provision that improves the earlier window; here the transition clause does, but the opposing chain comes from a second timing incentive (the leasing season), which the clause does not name. The instruction "check every provision for this before signing" is what caught it (C-18, C-19).
- *RS-16 and RS-1 0.8 (supply premise before signing a traded quantity).* Worked: the hotel quantity (C-23) was signed only with off-peak spare capacity, and the off-peak price left unsigned.
- *OC-3 0.8, right baseline.* Worked as written: the comparison with R3 enforcement gave two chains, and the clause's "arithmetic may supply a dominance premise" was tried and failed honestly (break-even of about 870 complaints inside the projected range), giving ambiguous (C-47). But see (b3).
- *OC-1 0.8, payers from a general budget as a group.* Worked (C-46).
- *CR-6 0.8, a free price's rise is enough.* Worked for rooms and capped primary lets (C-39).
- *CR-12e 0.8, counts over a distribution.* Worked: the share of units that stop (about 70%) and the complaint projection were treated as premises, not arithmetic.
- *Candidate patterns used.* "Complaint-only enforcement" (second use; promotes it; see c1).
- Re-run note: the core-only comparison found that the "Worked" verdict on CR-6 0.8 (a free price's rise is enough) was too generous: C-39 (and C-27's quantity) were signed without the supply premise that CR-6's 0.9 clause on splitting a shift now requires; A-35 and A-39 supply it.
