# WE-044 Ban on short-term rentals of whole homes, with a primary-residence exception

Analyst: draft (Handbook 0.8, held-out test)  |  Rule catalog version: 0.8  |  Status: awaiting expert review

A stylized policy in a fictional city. It resembles real short-term rental ordinances but is not modeled on any one of them. It was written as a held-out test of catalog 0.8, which was tuned on WE-026 to WE-035. It probes: a prohibition that removes a use of one's own property (CR-1, with an autistic element for owners who combined their own use with letting), operations dated in two steps (CR-1, 0.8), effects on neighbors through `proximity` at Tier C (CR-9, 0.7) and their use in asset values, spillover to hotels and to long-term and mid-term rentals (RS-16 with its Unless clause, RS-13, PC-8 by analogy), opposing timing chains in the announcement window (RS-8, 0.8), enforcement against the right baseline (OC-3, 0.8), enforcement that waits for complaints (candidate pattern "complaint-only enforcement", 06_gaps.md 6.2e), and the boundary between `legal_breach` and `informal_activity`. Noise, safety and neighborhood character as such are outside the scope of version 1. The probabilities are illustrative; the evidence column says what a real analysis would cite.

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
| K1 | Triangular: it prohibits an exchange (a stay under 30 nights) between owners and guests. By CR-1: for owners of non-primary units, operation 1 (the option of letting short-term is removed) from a date (0.8 clarification: the operation is dated 1 July 2027 for new bookings and 1 October 2027 for stays already booked); for primary-residence owners, operation 1 above 90 nights and operation 3 (registration, K3) below; for guests, operation 1 on whole-unit stays outside the exception. **Autistic element:** for second-home owners, what is removed is a way of using their own property, combining their own weeks in the home with lets in the other weeks. Their own use is not forbidden, but every remaining way of letting the home (a lease of 30 nights or more, a 12-month lease) displaces their own use. The restriction therefore works partly on the owner's own action, with no exchange in the option that is left (C-7). The counterfactual law allows lets of any length. | Yes for most non-primary units (net $30,000 against $20,000 long-term; A-1). For primary-residence hosts, only above 90 nights. For two-unit buildings, per reading of U1. | CR-1, CR-4, CR-5a, RS-1, RS-3 to RS-8, RS-10, RS-13, RS-16, EN-7 (in part), OC-4, SB-4 |
| K2 | Triangular: it attaches a penalty to platforms for intermediating a prohibited exchange (CR-1, operation 3) | Yes, if platforms comply (A-2) | CR-1, CR-4, CR-8c |
| K3 | A licensing requirement on the exempt use; binary in its fee | Yes for primary-residence hosts | CR-1, CR-4 (0.8 fixed cost per outlet), CR-8b |
| K4 | Binary in its funding (fixed budget, OC-3); complaint-only, so for hosts who list off-platform it attaches a risk rather than removing the option (CR-1, Premises) | Yes | OC-3 (fixed budget, right baseline), RS-3, candidate "complaint-only enforcement" |

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `hosts.non_primary` (`sellers.current`) | Owners of the 2,150 non-primary whole units | Short lets removed from July 2027. Split by response (CR-1, 0.7): `hosts.converting` (to 12-month leases), `hosts.mid_term` (to lets of 30 nights or more), `hosts.selling`, `hosts.in_breach` (keep letting short, off-platform). |
| `hosts.second_home` | The 450 second-home owners among them | Their own weeks plus lets in the other weeks is no longer possible. |
| `hosts.primary_over90`, `hosts.primary_under90` | Owners letting their primary residence while away | Registration ($250) for all; nights above 90 removed. |
| `hosts.duplex` | Owners letting the second unit of a two-unit building they live in | Per reading of U1: up to 90 nights (U1-a) or none (U1-b). |
| `hosts.lawful` | Rooms in occupied homes; primary-residence lets within the cap | Face less competition. |
| `guests.whole_unit` (`buyers.current`) | Visitors who would have stayed in a whole unit | Lose that option in Saltmere; can switch to hotels, rooms, Elsdon, off-platform lets, or not come. |
| `guests.prebooked` | Guests with bookings for stays after 30 September 2027 | Bookings cancelled and refunded. |
| `guests.off_platform` | Guests booking unlawful lets directly | Trade without platform reviews, payment protection or legal recourse. |
| `platforms` (`intermediaries`) | Booking platforms | Must check registration numbers, remove on notice and report nights. |
| `hotels` (`sellers.substitutes`), `buyers.substitutes` (hotel guests) | Hotel owners and their guests | More demand; fixed rooms in the short run. |
| Mid-term segment: `hosts.mid_term` and `guests.extended` | Furnished lets of 30 nights or more | Sellers and buyers both pushed in. |
| `tenants.prospective`, `landlords.long_term` | Long-term rental market | Converted units add supply. |
| `buyers.prospective` (homes) | Would-be buyers of homes in the beach districts | Investors' demand falls. |
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
| C-4 | `hosts.duplex` (letting 90 nights or fewer) | `quantity_supplied` (STR nights) | U1-a: no_change; U1-b: decrease | short | CR-1 | A-2 |
| C-5 | `hosts.duplex` (letting more than 90 nights) | `quantity_supplied` (STR nights) | decrease | short | CR-1, CR-4 | A-2 |

C-1 and C-2 are what the ordinance's supporters point to: about 2,150 whole units leave the short-let market. The exchanges no longer made are prevented exchanges (OC-4): both the owner and the guest lose the gain each expected (CR-5a). C-4 is the only place where U1 changes a sign from a decrease to no change: under U1-a a two-unit owner letting 90 nights or fewer carries on as before, apart from registration (C-17).

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-6 | `hosts.converting` | `quantity_supplied` (units offered on 12-month leases) | increase | short–medium | RS-6, CR-4, CR-7a | A-1, A-5 |
| C-7 | `hosts.second_home` | `units_held_vacant` | increase | short–medium | CR-1, CR-4 | A-1, A-6 |
| C-8 | `hosts.mid_term` | `reclassification` (lets reshaped to 30 nights or more) | increase | short | RS-5 | A-1, A-7 |
| C-9 | `hosts.primary_over90`, hosts listing under another unit's registration | `legal_breach` (on-platform lets beyond the cap or the exception) | increase | short–medium | RS-3, CR-1, CR-4 | A-3, A-22 |
| C-10 | `hosts.in_breach` | `informal_activity` (whole-unit lets booked off-platform) | increase | short–medium | RS-3, EN-7, CR-1, CR-4 | A-3, A-4 |
| C-11 | `guests.off_platform` | `search_cost` | increase | short | RS-10 | A-3, A-4 |
| C-12 | `guests.off_platform` | `quality_information` | decrease | short | RS-10, CR-11b | A-3, A-4 |
| C-13 | `guests.off_platform` | `disputes_settled_outside_courts` | increase | short | RS-10 | A-3, A-4 |
| C-14 | `guests.off_platform` | `allocation_by_non_price_criteria` (hosts screen guests for quietness) | increase | short–medium | CR-4, CR-6 | A-3, A-4, A-27 |
| C-15 | hosts, `platforms`, `hotels`, neighborhood associations | `lobbying_effort` (hosts and platforms to adopt U1-a, raise the cap or repeal; hotels and associations for proactive enforcement) | increase | medium | RS-7 | A-14 |
| C-16 | `platforms` | `compliance_cost` (registration checks, notices, quarterly reports) | increase | short | CR-1, CR-8c | A-2 |
| C-17 | `hosts.primary_over90`, `hosts.primary_under90`, `hosts.duplex` (U1-a) | `compliance_cost` (registration fee and proof of residence) | increase | short | CR-1, CR-8c, CR-4 | none |
| C-18 | `guests.whole_unit`, `hosts.non_primary` | `quantity_traded` (bookings made 3 November 2026 to 30 June 2027 for stays 1 July to 30 September 2027) | ambiguous | short | RS-8 (Unless), CR-10a, CR-12b | A-15, A-16 |
| C-19 | `guests.whole_unit`, `hosts.non_primary` | `quantity_traded` (whole-unit stays before 1 July 2027) | ambiguous | short | RS-8, CR-10a, CR-12b | A-16, A-17 |
| C-20 | `guests.whole_unit`, `hosts.non_primary` | `quantity_traded` (bookings made from 1 July 2027 for stays to 30 September 2027) | decrease | short | RS-8, CR-1 | A-2 |
| C-21 | `guests.prebooked` | `search_cost` (rebooking after cancellation) | increase | short | CR-1, CR-5a | A-24 |

**What owners do (C-6 to C-10).** For an owner of a non-primary unit, K1 removes the best option (CR-1, operation 1) and the owner falls back to the next-best (CR-3a), which differs from owner to owner (CR-1, 0.7: split the class by response). The pairs are CR-4's: x: a short let, y: a 12-month lease (C-6), a let of 30 nights or more (C-8, RS-5), a sale (section 6, C-40 and C-42), or keeping the short let in breach (C-9, C-10). A second-home owner has one more option: keep the home for their own weeks and leave it empty the rest of the year (C-7). That is the autistic element of K1: no exchange is forced or prevented in the option chosen; what is lost is a way of combining one's own use with other people's.

**Two kinds of breach (C-9, C-10).** The ordinance prohibits a trade for most units and allows it, within a cap, for others. A breach can therefore take two forms. A primary-residence host who lists on two platforms, each of which reports only its own nights, can exceed 90 nights while every listing carries a valid number (A-22); a host who lists a second unit under the registration of the home they live in does the same. These trades run through the legal market's channels (platforms, reviews, payment, TOT collected), so they are `legal_breach` (C-9). A non-primary owner who cannot get a number lets off-platform, to repeat guests and through social media and their own website: trade outside the legal market, `informal_activity` (C-10, RS-3, EN-7), to which RS-10 applies (C-11 to C-13). The boundary between the two variables is not drawn by the ontology for a prohibition with a permitted sub-class; this analysis draws it at the channel (Gaps found, d).

**Complaint-only enforcement (C-9, C-10, C-14).** Code Enforcement acts only on complaints, and complaints come mostly from neighbors. The expected penalty for an unlawful let is therefore the probability of a complaint times the fine (CR-1: the rule attaches a risk; CR-4, x: comply, y: violate). Against a gain of about $10,000 a year over a long-term lease, a $2,500 fine deters only where a complaint is likely. That probability differs by unit: lowest for detached homes, for units whose neighbors are themselves second homes or STRs, and for units let to guests who make no noise (A-3). Breach is therefore concentrated where neighbors are fewest or absent, and hosts in breach screen guests on what predicts a complaint (families, couples, older guests; no groups or parties), since the price cannot be set to cover the risk guest by guest when the risk is not observed in advance (C-14, CR-6: the scarce side chooses by other criteria, A-27). This is the derivation listed in 06_gaps.md, 6.2e as the candidate "complaint-only enforcement" (CR-4, the expected cost of breach differs by counterparty), here needed a second time; it is also what makes K4's ban bind least where neighbors were least affected.

**The cost of registering (C-17).** The $250 fee and the proof of residence are a cost fixed per host, not per night. By CR-4's 0.8 clarification on fixed costs per outlet, it bears on whether a primary-residence host lists at all (some who let a few nights a year stop), not on the nightly price. C-17 is Tier A: everyone who keeps listing pays it.

**Timing in the announcement window (C-18 to C-20).** Under RS-8 every provision is checked for whether it improves an earlier window (0.8 Unless clause). The transition clause does: a stay booked before 1 July 2027 may go ahead if it ends by 30 September 2027. So:
- *Bookings in the window for July to September stays (C-18).* (+) Guests and hosts who would have booked those summer stays in June, July or August (most whole-unit stays are booked within 60 days) book them before 1 July, while that still protects them (A-15). (−) Owners who plan to convert to a 12-month lease time the conversion to the leasing season (leases in Saltmere start in August and September, around the university year) or plan to sell over the summer; they stop accepting summer bookings, so bookings they would have taken in the window are not made (A-16). Both are timing chains in the same window, pushing opposite ways: **ambiguous** without a dominance premise, which the case does not supply.
- *Stays before 1 July 2027 (C-19).* (+) Some guests who prefer whole units move a planned later trip forward (A-17). (−) Owners converting for an early lease start, or selling with vacant possession, end short lets before July (A-16). **Ambiguous.**
- *Bookings after 1 July for stays to 30 September (C-20).* The other side of the first chain of C-18, and the ban itself: such bookings are no longer lawful for non-primary units, so they fall.

**Cancelled bookings (C-21).** Bookings made before the announcement for stays after 30 September 2027 (about 6% of a year's nights are booked more than nine months ahead, A-24) must be cancelled and refunded. The refund returns the guest's money (CR-8b), so the guest's means are unchanged; what is lost is the stay itself (CR-5a) and the time spent finding another (C-21).

**Lobbying (C-15).** Hosts (with a concentrated loss), platforms, and the beneficiaries (hotels, neighborhood associations) have stakes that depend on the reading of U1, the cap and enforcement (RS-7; A-14). Without the ordinance there would be no contest over these terms, so RS-7's repeal clause does not apply and the sign is an increase.

Not reported:
- Owner-occupiers who start letting rooms because room prices rise (C-39): a supply response to the price, not a separate consequence of the policy.
- Strategic complaints (rivals or hotels reporting lawful hosts to raise their costs). CR-4 derives it (x: no complaint, y: complain), but it needs a premise that complaints cost the complainant less than the expected gain from a rival's lost bookings (A-28, p = 0.3).

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-22 | `buyers.substitutes` (hotel guests) | `price_paid` (hotel rooms, peak season) | increase | short–medium | RS-16, CR-9, CR-6 | whole-unit STR and hotel rooms: `substitute`, partial | A-8, A-9 |
| C-23 | `hotels` | `quantity_traded` (room-nights, mainly outside peak season) | increase | short–medium | RS-1, RS-16 | as C-22 | A-8 |
| C-24 | `hotels` (owners) | `asset_value` | increase | short (from 3 November 2026) | CR-7c, CR-10c, SB-4 | as C-22 | A-8, A-9, A-30 |
| C-25 | `hotels` | `investment_target` (new rooms) | increase | long | CR-7a, CR-4 | as C-22 | A-8, A-25 |
| C-26 | `guests.whole_unit` | `cross_border_purchases` (whole-unit stays in Elsdon) | increase | short | RS-4 | Saltmere and Elsdon STRs: `across_border`, partial | A-10 |
| C-27 | `neighboring_jurisdictions` (Elsdon hosts) | `quantity_supplied` (STR nights) | increase | short–medium | RS-4, CR-7a | as C-26 | A-10 |
| C-28 | `neighboring_jurisdictions` (Elsdon owners) | `asset_value` (homes suited to STR) | increase | short | CR-7c, CR-10c | as C-26 | A-10, A-30 |
| C-29 | `neighboring_jurisdictions` (Elsdon tenants) | `price_paid` (long-term rent) | increase | medium | RS-13, CR-9 | Elsdon long-term and STR uses: `same_market_other_segment`, partial | A-10, A-29 |
| C-30 | `guests.whole_unit` | `quantity_traded` (visitor trips to Saltmere) | decrease | short–medium | RS-1, CR-4c | — | A-11 |
| C-31 | `sellers.complements` (beach-district restaurants, shops, tour operators) | `quantity_traded` | decrease | short–medium | CR-9, RS-9 | visitors' lodging and nearby purchases: `complement`, location | A-11, A-12 |
| C-32 | `input_suppliers` (cleaners, linen services, STR managers) | `employment`, `hours_worked` | at_least_one_decrease | short–medium | CR-9, RS-6 | cleaning and management `input_to` STR | A-1, A-26 |
| C-33 | `hotels` (staff) | `employment`, `hours_worked` | at_least_one_increase | short–medium | OC-5, CR-9 | hotel labor `input_to` room-nights | A-8 |
| C-34 | `tenants.prospective` | `price_paid` (long-term rent) | decrease | medium | RS-13, CR-6 | STR and long-term uses of the same units: `same_market_other_segment`, close | A-5, A-13 |
| C-35 | `tenants.prospective` | `quantity_traded` (12-month leases) | increase | medium | RS-13, CR-4c | as C-34 | A-5, A-13 |
| C-36 | `landlords.long_term` | `net_price_received` | decrease | medium | RS-13, CR-6 | as C-34 | A-5, A-13 |
| C-37 | `landlords.long_term` (owners) | `asset_value` (rental buildings) | decrease | short–medium | CR-7c, CR-10c | as C-34 | A-5, A-13, A-30 |
| C-38 | `guests.extended` | `price_paid` (furnished lets of 30 nights or more) | ambiguous | short–medium | RS-16 (Unless), RS-13, CR-12b | STR and mid-term lets: `substitute`, partial | A-7, A-31 |
| C-39 | `hosts.lawful` | `net_price_received` | increase | short–medium | RS-16, CR-6 | whole-unit STR and rooms or capped primary lets: `substitute`, partial | A-32 |
| C-40 | `hosts.non_primary` (owners when the ban became expected) | `asset_value` | decrease | short (part from 3 November, the rest at 8 December 2026) | CR-1, CR-7c, CR-10c, SB-4 | — | A-1, A-30 |
| C-41 | `hosts.duplex` (owners) | `asset_value` (two-unit buildings with a let second unit) | decrease | short | CR-1, CR-7c, CR-10c | — | A-30 |
| C-42 | `buyers.prospective` (homes in the beach districts) | `price_paid` (home purchases) | decrease | short–medium | CR-7c, CR-8b, OC-7 | — | A-21, A-30 |
| C-43 | `homeowners.str_districts` | `asset_value` | ambiguous | short–medium | CR-7c, CR-10c, CR-9 (proximity), CR-12b, CR-12d | `proximity` (STR guests next door), Tier C | A-21, A-23 |
| C-44 | `hosts.non_primary` (owners who keep their units) | `return_on_capital` | decrease | short–medium | CR-3a, CR-7b | — | A-1, A-5 |

**Hotels and the other lodging segments (C-22 to C-25, C-34 to C-39).** This is PC-8's question asked of a prohibition rather than a price control: where does the excluded demand go, and does the policy also push sellers into the segment it goes to? RS-16 asks it directly, and its Unless clause (RS-13) is the PC-8 Unless. The answer differs by segment:
- *Hotels.* Guests move from whole units to hotels (RS-1; CR-9). The policy pushes no sellers into hotels: an STR unit cannot become a hotel room. In peak season occupancy is 94% and rooms cannot be added for years (A-9), so the price rises (C-22, RS-16, CR-6). Off-peak, at about 65% occupancy, spare rooms can take guests at little added cost, so room-nights rise (C-23) but the off-peak price is not signed. RS-1's 0.8 clause asks for a supply premise before signing a traded quantity: off-peak spare capacity supplies it. The expected rise in yield is capitalized in hotel values from the introduction (C-24), and in the long run draws new rooms (C-25, A-25).
- *Long-term rentals.* Converting owners add units (C-6); no excluded guest wants a 12-month lease. Only RS-13 operates, so rent falls (C-34), more leases are signed (C-35), and incumbent landlords receive less (C-36) and see their buildings' value fall (C-37). Arithmetic for scale only: if half the 2,150 units convert, the long-term stock rises by about 1.8%.
- *Furnished lets of 30 nights or more.* Both chains operate: guests on stays of two to four weeks move up to 30-night lets (RS-16, A-31), and owners reshape lets to 30 nights (C-8, A-7), adding supply (RS-13). With 900 units in the segment and perhaps several hundred more pushed in, neither chain clearly dominates: RS-16's Unless clause gives **ambiguous** (C-38).
- *Rooms and primary-residence lets within the cap.* Guests turn to them (A-32), and no sellers are pushed in by the policy itself; their nightly price is free, and its rise is enough (CR-6, 0.8) (C-39).

**Elsdon (C-26 to C-29).** RS-4: the ban burdens letting inside the line, so stays move outside (C-26), Elsdon hosts let more (C-27), Elsdon homes suited to STR gain value from the introduction (C-28), and as Elsdon owners move units from long-term leases into STR (A-29), Elsdon's long-term rents rise (C-29, RS-13 for withdrawn supply). C-29 is at depth 3 and is the last link followed there.

**Visitors and the businesses near them (C-30, C-31).** Some groups and families have no close substitute at the old price (A-11): they shorten or skip the trip (C-30, CR-4c). Visitors buy meals and goods near where they stay (A-12): those who move to hotels move that spending to the hotel districts, and those who stay away take it out of the city, so beach-district businesses sell less (C-31, CR-9 along the location complement, RS-9 by analogy: the lodging decision carries the nearby purchases with it). Hotel-district businesses gain part of it; that chain is not followed (depth 3).

**Labor (C-32, C-33).** Cleaning and management are inputs to STR nights (CR-9): at least one of employment or hours falls (RS-6 group). Hotel staff gain at least one of them (OC-5). The hotel side is an existing activity, so the group form applies (OC-5, 0.8).

**Values and both sides of the revaluation (C-40 to C-44).** The yield of a non-primary unit falls from STR net to its next-best use (about $30,000 to $20,000 a year for most). By CR-1's 0.8 clarification, the operation is dated July 2027, but the asset's value moves when the ban becomes expected (CR-7c, CR-10c): part of the way when six of nine members sponsored it, the rest at enactment (C-40, A-30). The loss is borne by owners at that time; later buyers pay the lower price (C-42), which is the other side of the revaluation (CR-8b, OC-7). Owners who keep their units earn less on the capital they put in (C-44); in the long run, returns on capital are equalized and no lasting change is signed. Two-unit buildings lose value under both readings of U1 (C-41): under U1-b the second unit loses its short-let use; under U1-a it keeps 90 nights, but buyers who would have let it for more lose that option. The size differs by reading; the sign does not.

**Neighbors and owner-occupied homes (C-43).** Two chains reach the value of owner-occupied homes in the beach districts:
- (−) CR-7c: every home there loses the option of being let short-term, valued by the investors who made about 30% of recent purchases (A-21). Tier B.
- (+) A home whose neighbor would have been an STR unit is now more likely to have a long-term tenant or an owner next door. Some buyers value fewer transient neighbors (A-23). The relation is `proximity`: the change reaches the neighbor through physical nearness, not exchange. CR-9's 0.7 clarification admits it at Tier C, pending Q20.

CR-12's 0.8 clarification classes the second as kind (2): a chain the rules derive, with a premise at p ≥ 0.5. The sign is **ambiguous**, and the consequence takes the lowest tier in its chains, C (CR-12d). The amenity itself (quieter streets) has no variable in 2.4 and is out of scope; it is a Tier C note, not a consequence. The 1,500 nuisance complaints a year about STR units are a record of neighbors acting (CR-2), which is evidence that the proximity chain has a sign for some of them; CR-9 gives no way for such evidence to raise the chain's tier (Gaps found, b).

Stopping points: C-29 (depth 3, Elsdon tenants); hotel-district businesses (depth 3); buyers of the homes sold by converting owners beyond C-42 (OC-7's further chain needs a premise on what they would have bought, not followed); the university's housing office (diffuse).

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `guests.whole_unit`, `hosts.non_primary`, `quantity_traded` (bookings in the window for July–September stays), short | Pull-forward into the protected window (K1 transition clause; A-15). | Owners converting or selling refuse summer bookings (A-16). | None | **ambiguous** (C-18). RS-8's 0.8 Unless clause: the policy improves the earlier window, and a second timing chain opposes it. |
| `guests.whole_unit`, `hosts.non_primary`, `quantity_traded` (stays before 1 July 2027), short | Guests move later trips forward (A-17). | Owners end short lets early for a lease or a sale (A-16). | None | **ambiguous** (C-19). |
| `guests.extended`, `price_paid` (30-night-plus lets), short–medium | Extended-stay guests move in (RS-16, A-31). | Owners reshape lets to 30 nights (RS-13, C-8, A-7). | None | **ambiguous** (C-38). RS-16 Unless. |
| `homeowners.str_districts`, `asset_value`, short–medium | Fewer transient neighbors (`proximity`, Tier C; A-23). | Loss of the option to let short-term (CR-7c; A-21). | None | **ambiguous**, Tier C (C-43). CR-12 (0.8), kind (2). |
| `officials.enforcement` (Code Enforcement), `enforcement_cost`, short | Complaints about unlawful lets investigated (K4; A-19). | Fewer nuisance complaints about STR units under R3, as units leave (A-18). | Arithmetic attempted, not decisive (section 9) | **ambiguous** (C-47). OC-3 (0.8), right baseline. |
| `neighbors`, `compliance_cost` (time filing complaints), short | Complaints about unlawful lets (A-19). | Fewer nuisance complaints (A-18). | None | **ambiguous** (C-48). |
| `taxpayers`, recipients of other general-fund spending, `tax_revenue` (TOT), short–medium | Hotel room-nights and rates rise (C-22, C-23). | STR TOT lost (C-2); stays moved to Elsdon (C-26) and trips not taken (C-30) are not taxed by Saltmere. | None (TX-10: part of the spending moves to taxed hotels) | **ambiguous** (C-49). |
| `buyers.substitutes`, `price_paid` (hotels), long | — | New rooms (C-25). | CR-12g | **Not signed** at the long horizon; C-22 is short–medium only. |
| `tenants.prospective`, `price_paid` (long-term rent), medium | None found. Checked: no chain moves guests or tenants into 12-month leases; sales to owner-occupiers (C-42) lower rental demand too. | Converted units (C-6). | None needed | **decrease** (C-34). |
| `hosts.non_primary`, `asset_value`, short | None found. | Loss of short-let yield (C-40). | None needed | **decrease** (C-40). |

The final check before the report (workflow) was run on every consequence:
1. *Uncombined chains:* the rows above; in addition, `quantity_supplied` of non-primary units (C-1) has no (+) chain, and `hotels`' `quantity_traded` has no (−) chain (fewer visitors in C-30 were STR guests, not hotel guests).
2. *Groups:* C-32, C-33 recorded as groups.
3. *Baseline:* every sign is against Saltmere without the ordinance, with R1 to R3 in force. Enforcement (C-47) is compared with R3 enforcement, not with zero.
4. *Worse off is not poorer:* hosts' loss is recorded as `return_on_capital` and `asset_value`, not `resources_available_other_uses`; only fines (C-51) and the appropriation (C-46) are signed on means.
5. *Timing shifts:* C-18 to C-20 per window.
6. *Both sides:* registration fees (C-17, C-50), fines (C-50, C-51), the appropriation (C-45, C-46), the revaluation (C-40, C-42), refunds (C-21: the money is returned, so neither side's means change).
7. *Every core rule for every class:* CR-7c on hosts, hotels, Elsdon owners, landlords, homeowners, two-unit owners (C-24, C-28, C-37, C-40 to C-43); CR-6 in hotels, rooms, mid-term and long-term segments; CR-9 to inputs, complements, neighbors.
8. *Unstated premises:* the "some actors at the margin" premise for each response is in section 10 (A-5, A-6, A-7, A-15 to A-17, A-27).

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
| C-50 | `officials.enforcement` (general fund) | `non_tax_receipts` (registration fees, fines) | increase | Nothing; receipts. | CR-8b |
| C-51 | `hosts.fined` | `resources_available_other_uses` | decrease | What the fines would have bought; a sum they cannot avoid once imposed. | CR-8b, CR-3c |

**Enforcement against the right baseline (C-47).** OC-3's 0.8 clause asks for the comparison with enforcement without the policy. Without the ordinance, Code Enforcement investigates about 1,500 nuisance complaints a year about STR units, about 3,750 staff hours. With it:
- (−) As non-primary units leave, nuisance complaints about them fall. If the rate per operating unit holds (A-18) and about 70% of whole-unit listings stop, about 1,050 fewer complaints, about 2,600 hours saved.
- (+) Complaints about unlawful lets must be investigated (A-19): the city projects 400 to 1,200 a year, at about 3 hours each (requests for platform data, site visits, hearings), 1,200 to 3,600 hours.

The break-even is about 870 complaints, inside the projected range. The figures do not settle it, so arithmetic supplies no dominance premise (CR-12e) and the sign is **ambiguous**. On a fixed budget (OC-3), the burden on other code enforcement has the same ambiguous sign; it is not recorded separately.

**Neighbors' time (C-48).** The same two chains apply to the complainants: complaint-only enforcement moves the work of detection to neighbors (CR-8c), while fewer STR units mean fewer nuisance complaints. OC-3's right-baseline clause is written for officials; it is applied here to complainants by the same derivation (CR-8c against the counterfactual's use of the same means).

**TOT (C-49).** About $18.7 million a year of STR TOT is lost as whole units stop. Part of the spending moves to hotels, taxed at the same 12% and at higher peak prices; part goes to Elsdon or is not spent in Saltmere. TX-10: where part moves to taxed goods, the combined sign is ambiguous. Hotels' peak capacity limits the gain, but the higher peak rate applies to every hotel night, so no arithmetic on the record's figures settles it.

**Prevented exchanges.** The stays no longer made are C-2 (OC-4); the trips not taken are C-30. They are not listed again.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | For most non-primary units, short lets yield more than any lawful alternative (about $30,000 net against about $20,000). | binding | 0.9 | Platform revenue data; long-term rents for comparable units. | Most consequences shrink; owners would already have converted. |
| A-2 | Platforms comply with K2: they display numbers, remove listings on notice and report nights. | enforcement | 0.85 | The fine per listing per day exceeds a platform's fee per listing (about $7,600 a year); compliance with similar rules elsewhere. | C-1 to C-5, C-16 and C-20 shrink; C-9 grows. |
| A-3 | For some units, complaints are unlikely (detached homes, neighbors who are absent or also let), so the expected fine is below the gain from breach. | enforcement | 0.75 | Share of STR units in detached homes; complaint rates by building type under R3. | C-9 to C-14 and C-51 are not reported. |
| A-4 | Some guests keep wanting whole units in Saltmere enough to book them directly. | substitutability | 0.7 | Repeat-guest shares; direct-booking sites. | C-10 to C-14 are not reported. |
| A-5 | Most non-primary units can be let on 12-month leases, and some owners choose that over sale, vacancy or mid-term lets. | alternative_uses | 0.85 | Unit types; condominium rules; long-term demand. | C-6, C-34 to C-37 and C-44 are not reported. |
| A-6 | Some second-home owners value their own weeks enough to keep the home and leave it empty the rest of the year. | other | 0.7 | Owners' use patterns in the platform data (blocked calendar weeks). | C-7 is not reported. |
| A-7 | Some owners can let for 30 nights or more (traveling nurses, university visitors, relocations). | substitutability | 0.75 | Mid-term listings and hospital and university demand. | C-8 and the (−) chain of C-38 fail. |
| A-8 | Hotels are a substitute for whole units for some guests. | substitutability | 0.8 | Guest surveys; group sizes. | C-22 to C-25 and C-33 are not reported. |
| A-9 | Hotel rooms cannot be added in the short to medium run, and peak-season occupancy is near capacity (94%). | durability | 0.85 | Occupancy data; planning times of three to five years. | C-22 and part of C-24 fail. |
| A-10 | Elsdon is near enough for some guests (12 km from Harbor). | mobility | 0.7 | Travel times; Elsdon listings near the city line. | C-26 to C-29 are not reported. |
| A-11 | Some visitors (large groups, families) have no close substitute at the old price and shorten or skip trips. | substitutability | 0.65 | Group sizes in STR bookings; hotel suites available. | C-30 and C-31 are not reported. |
| A-12 | Visitors buy meals and goods near their lodging. | other | 0.7 | Card-spending data by district. | C-31 is not reported. |
| A-13 | Units added to the long-term market are not offset by withdrawals elsewhere. | substitutability | 0.75 | No other policy change in the long-term market. | C-34 to C-37 weaken. |
| A-14 | Hosts, platforms, hotels and neighborhood associations can organize at a cost below their stake. | other | 0.85 | Their activity on the ordinance. | C-15 is not reported. |
| A-15 | Guests can book summer stays earlier than they otherwise would. | expectations | 0.7 | Booking lead times. | The (+) chain of C-18 fails; C-18 would be a decrease. |
| A-16 | Some owners planning to convert or sell end or refuse summer lets to have the unit free for the August–September leasing season or a sale. | other | 0.6 | Leasing-season timing; listing data for sales. | The (−) chains of C-18 and C-19 fail; C-18 and C-19 would be increases. |
| A-17 | Some guests who prefer whole units move a later trip to before 1 July 2027. | other | 0.55 | Share of trips with flexible dates. | The (+) chain of C-19 fails; C-19 would be a decrease. |
| A-18 | Nuisance complaints per operating STR unit stay near the 2025 rate. | other | 0.75 | R3 complaint records, 2022–2025. | The (−) chains of C-47 and C-48 weaken. |
| A-19 | Neighbors file complaints about unlawful lets in meaningful numbers; some lead to fines. | enforcement | 0.8 | The city's projection of 400 to 1,200 a year; neighborhood associations' support. | C-47 and C-48 become decreases; C-50 (fines) and C-51 are not reported. |
| A-20 | The $520,000 is new general-fund money. | revenue_use | 0.9 | §8. | C-46 is not reported; other spending in the department falls instead. |
| A-21 | Investors are a material part of demand for homes in the beach districts. | other | 0.8 | About 30% of 2023–2025 purchases by non-occupants. | C-42 and the (−) chain of C-43 weaken. |
| A-22 | Hosts listing on more than one platform can exceed 90 nights without the per-platform reports revealing it. | enforcement | 0.6 | K2 reports are per platform; the city has no plan to aggregate them. | C-9 weakens to listings under another unit's registration. |
| A-23 | Some buyers value fewer transient neighbors (the `proximity` chain). | other | 0.6 | Neighborhood associations' support; the complaint record (R3). | C-43 becomes a decrease (Tier B). |
| A-24 | Bookings exist for stays after 30 September 2027 made before the introduction. | other | 0.9 | About 6% of a year's nights are booked more than nine months ahead. | C-21 is not reported. |
| A-25 | Hotels can obtain sites and permits to add rooms in the long run. | alternative_uses | 0.55 | Zoning for hotels in the beach districts. | C-25 is not reported. |
| A-26 | Cleaning and management firms adjust their labor to the nights they service. | alternative_uses | 0.8 | Staffing practice. | C-32 is not reported. |
| A-27 | Hosts in breach can screen guests on traits that predict complaints, and do not set prices to cover the risk guest by guest. | other | 0.6 | Off-platform booking practice; hosts' house rules. | C-14 is not reported. |
| A-28 | Rivals file complaints against lawful hosts to raise their costs. | other | 0.3 | Complaint records give no evidence of it. | Below the cut-off; not reported. |
| A-29 | Some Elsdon owners move units from long-term leases into STR. | alternative_uses | 0.6 | Elsdon's ratio of STR to long-term returns. | C-29 is not reported. |
| A-30 | Values of STR units, hotels and Elsdon homes rest on expected yields, and passage was likely from the introduction (six of nine sponsors). | expectations | 0.8 | Sale prices as multiples of earnings; sponsors' count. | C-24, C-28, C-37, C-40 to C-42 move later (at enactment) or not at all. |
| A-31 | Some guests on stays of two to four weeks can extend to 30 nights. | substitutability | 0.6 | Stay-length distribution; who those guests are (contract workers, relocations). | The (+) chain of C-38 fails; C-38 would be a decrease. |
| A-32 | Rooms in occupied homes and primary-residence lets are a substitute for whole units for some guests. | substitutability | 0.75 | Guest overlap on platforms. | C-39 is not reported. |

## 11. Report

**The policy.** From 1 July 2027, Saltmere bans letting whole homes for under 30 nights, except a registered owner's primary residence for up to 90 nights a year. Stays booked before July may go ahead until 30 September 2027; later bookings are cancelled and refunded. Platforms must show a registration number on each listing, remove listings the city flags, and report nights, or pay $1,000 per listing per day. Hosts are fined only when someone complains. A new registry costs $520,000 a year from the general fund. Whether the second unit of a two-unit building whose owner lives in the other counts as the owner's residence is unclear.

**Visible consequences.** About 2,150 whole homes stop being let to visitors (C-1, C-2), and primary-residence hosts who let more than 90 nights cut back (C-3, C-5).

**Invisible consequences.**
- *Owners.* Most convert to long-term leases (C-6), some to lets of a month or more (C-8); second-home owners who keep their own weeks leave the home empty the rest of the year (C-7). Owners when the ban became expected bear a fall in their units' value (C-40, C-41) and earn less on their capital (C-44). Primary-residence hosts pay to register (C-17).
- *Breach.* Some hosts exceed the cap on platforms or list under another unit's number (C-9); others let off-platform (C-10), where guests search harder, know less about what they book and settle disputes outside the courts (C-11 to C-13). Because only complaints trigger enforcement, breach concentrates where neighbors are absent, and hosts screen guests for quietness (C-14).
- *Guests and visitors.* Some guests switch to hotels, where peak-season prices rise (C-22, C-23), or to Elsdon (C-26); some skip or shorten trips (C-30), and beach-district shops and restaurants sell less (C-31). Guests with bookings after September 2027 must rebook (C-21).
- *Other lodging.* Hotels gain value from the introduction (C-24) and add rooms in the long run (C-25); their staff work more (C-33). Rooms in occupied homes and capped primary lets fetch more (C-39). Elsdon hosts let more, Elsdon homes gain value, and Elsdon tenants pay more (C-27 to C-29). STR cleaners and managers lose work (C-32).
- *Housing.* Long-term rents are lower than they would have been (C-34) and more leases are signed (C-35); incumbent landlords receive less (C-36) and their buildings are worth less (C-37). Buyers of homes in the beach districts pay less (C-42).
- *The city.* Registry costs, paid by taxpayers or recipients of other general-fund spending (C-45, C-46); registration fees and fines received (C-50) from those fined (C-51); lobbying over the cap, the reading of U1 and enforcement (C-15); platforms' compliance work (C-16).

**Ambiguous effects.** Bookings and stays in the eight-month window (C-18, C-19): the transition clause pulls summer bookings forward while converting owners withdraw. The price of month-long furnished lets (C-38): demand and supply both move in. Values of owner-occupied homes in the beach districts (C-43, Tier C): the lost option to let against fewer transient neighbors. Code Enforcement's workload and neighbors' complaint time (C-47, C-48): new complaints about unlawful lets against fewer nuisance complaints. TOT revenue (C-49).

**Per reading of U1.** Two-unit owners who let 90 nights or fewer: no change if the building is the residence (U1-a), a ban if the unit is (U1-b) (C-4). Two-unit buildings lose value under both readings, more under U1-b (C-41).

**Key conditions.** That short lets pay more than any lawful use (A-1, p = 0.9) and that platforms comply (A-2, p = 0.85) drive the direct effects. Breach rests on complaints being unlikely for some units (A-3, p = 0.75). The effect on long-term rents rests on owners converting rather than selling or leaving units empty (A-5, p = 0.85).

**What this analysis cannot say.** How many units convert, how much rents fall or hotel prices rise; whether neighbors' gain in quiet outweighs owners' and guests' losses; noise, safety and neighborhood character as such (out of scope for version 1); whether the ordinance is desirable.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | hosts.non_primary | quantity_supplied (lawful whole-unit STR nights) | decrease | short | visible | B | CR-1, CR-4 | A-1, A-2 |
| C-2 | guests.whole_unit, hosts.non_primary, platforms | quantity_traded (whole-unit STR nights via platforms) | decrease | short | visible | B | CR-5a, OC-4 | A-1, A-2 |
| C-3 | hosts.primary_over90 | quantity_supplied (nights above 90) | decrease | short | visible | B | CR-1, CR-4 | A-2 |
| C-4 | hosts.duplex (90 nights or fewer) | quantity_supplied (STR nights) | U1-a: no_change; U1-b: decrease | short | visible | B | CR-1 | A-2 |
| C-5 | hosts.duplex (more than 90 nights) | quantity_supplied (STR nights) | decrease | short | visible | B | CR-1, CR-4 | A-2 |
| C-6 | hosts.converting | quantity_supplied (units on 12-month leases) | increase | short–medium | invisible | B | RS-6, CR-4, CR-7a | A-1, A-5 |
| C-7 | hosts.second_home | units_held_vacant | increase | short–medium | invisible | B | CR-1, CR-4 | A-1, A-6 |
| C-8 | hosts.mid_term | reclassification (lets of 30 nights or more) | increase | short | invisible | B | RS-5 | A-1, A-7 |
| C-9 | hosts.primary_over90, hosts using another unit's registration | legal_breach (on-platform lets beyond the cap or exception) | increase | short–medium | invisible | B | RS-3, CR-1, CR-4 | A-3, A-22 |
| C-10 | hosts.in_breach | informal_activity (off-platform whole-unit lets) | increase | short–medium | invisible | B | RS-3, EN-7, CR-1, CR-4 | A-3, A-4 |
| C-11 | guests.off_platform | search_cost | increase | short | invisible | B | RS-10 | A-3, A-4 |
| C-12 | guests.off_platform | quality_information | decrease | short | invisible | B | RS-10, CR-11b | A-3, A-4 |
| C-13 | guests.off_platform | disputes_settled_outside_courts | increase | short | invisible | B | RS-10 | A-3, A-4 |
| C-14 | guests.off_platform | allocation_by_non_price_criteria (screening for quietness) | increase | short–medium | invisible | B | CR-4, CR-6 | A-3, A-4, A-27 |
| C-15 | hosts, platforms, hotels, neighborhood associations | lobbying_effort | increase | medium | invisible | B | RS-7 | A-14 |
| C-16 | platforms | compliance_cost | increase | short | invisible | B | CR-1, CR-8c | A-2 |
| C-17 | hosts.primary_over90, hosts.primary_under90, hosts.duplex (U1-a) | compliance_cost (registration) | increase | short | invisible | A | CR-1, CR-8c, CR-4 | none |
| C-18 | guests.whole_unit, hosts.non_primary | quantity_traded (window bookings for July–September stays) | ambiguous | short | invisible | B | RS-8, CR-10a, CR-12b | A-15, A-16 |
| C-19 | guests.whole_unit, hosts.non_primary | quantity_traded (stays before 1 July 2027) | ambiguous | short | invisible | B | RS-8, CR-10a, CR-12b | A-16, A-17 |
| C-20 | guests.whole_unit, hosts.non_primary | quantity_traded (bookings from 1 July for stays to 30 September) | decrease | short | invisible | B | RS-8, CR-1 | A-2 |
| C-21 | guests.prebooked | search_cost (rebooking) | increase | short | invisible | B | CR-1, CR-5a | A-24 |
| C-22 | buyers.substitutes (hotel guests) | price_paid (hotel rooms, peak season) | increase | short–medium | invisible | B | RS-16, CR-9, CR-6 | A-8, A-9 |
| C-23 | hotels | quantity_traded (room-nights) | increase | short–medium | invisible | B | RS-1, RS-16 | A-8 |
| C-24 | hotels (owners) | asset_value | increase | short | invisible | B | CR-7c, CR-10c, SB-4 | A-8, A-9, A-30 |
| C-25 | hotels | investment_target (new rooms) | increase | long | invisible | B | CR-7a, CR-4 | A-8, A-25 |
| C-26 | guests.whole_unit | cross_border_purchases (stays in Elsdon) | increase | short | invisible | B | RS-4 | A-10 |
| C-27 | neighboring_jurisdictions (Elsdon hosts) | quantity_supplied (STR nights) | increase | short–medium | invisible | B | RS-4, CR-7a | A-10 |
| C-28 | neighboring_jurisdictions (Elsdon owners) | asset_value (homes suited to STR) | increase | short | invisible | B | CR-7c, CR-10c | A-10, A-30 |
| C-29 | neighboring_jurisdictions (Elsdon tenants) | price_paid (long-term rent) | increase | medium | invisible | B | RS-13, CR-9 | A-10, A-29 |
| C-30 | guests.whole_unit | quantity_traded (trips to Saltmere) | decrease | short–medium | invisible | B | RS-1, CR-4c | A-11 |
| C-31 | sellers.complements (beach districts) | quantity_traded | decrease | short–medium | invisible | B | CR-9, RS-9 | A-11, A-12 |
| C-32 | input_suppliers (cleaners, managers) | employment, hours_worked | at_least_one_decrease | short–medium | invisible | B | CR-9, RS-6 | A-1, A-26 |
| C-33 | hotels (staff) | employment, hours_worked | at_least_one_increase | short–medium | visible | B | OC-5, CR-9 | A-8 |
| C-34 | tenants.prospective | price_paid (long-term rent) | decrease | medium | invisible | B | RS-13, CR-6 | A-5, A-13 |
| C-35 | tenants.prospective | quantity_traded (12-month leases) | increase | medium | invisible | B | RS-13, CR-4c | A-5, A-13 |
| C-36 | landlords.long_term | net_price_received | decrease | medium | invisible | B | RS-13, CR-6 | A-5, A-13 |
| C-37 | landlords.long_term (owners) | asset_value (rental buildings) | decrease | short–medium | invisible | B | CR-7c, CR-10c | A-5, A-13, A-30 |
| C-38 | guests.extended | price_paid (lets of 30 nights or more) | ambiguous | short–medium | invisible | B | RS-16, RS-13, CR-12b | A-7, A-31 |
| C-39 | hosts.lawful | net_price_received | increase | short–medium | invisible | B | RS-16, CR-6 | A-32 |
| C-40 | hosts.non_primary (owners at introduction) | asset_value | decrease | short | invisible | B | CR-1, CR-7c, CR-10c, SB-4 | A-1, A-30 |
| C-41 | hosts.duplex (owners) | asset_value (two-unit buildings) | decrease | short | invisible | B | CR-1, CR-7c, CR-10c | A-30 |
| C-42 | buyers.prospective (homes, beach districts) | price_paid (home purchases) | decrease | short–medium | invisible | B | CR-7c, CR-8b, OC-7 | A-21, A-30 |
| C-43 | homeowners.str_districts | asset_value | ambiguous | short–medium | invisible | C | CR-7c, CR-10c, CR-9 (proximity), CR-12b, CR-12d | A-21, A-23 |
| C-44 | hosts.non_primary (keeping units) | return_on_capital | decrease | short–medium | invisible | B | CR-3a, CR-7b | A-1, A-5 |
| C-45 | officials.enforcement (Registry Unit) | enforcement_cost | increase | short | invisible | A | OC-3 | none |
| C-46 | taxpayers, recipients of other general-fund spending | resources_available_other_uses | at_least_one_decrease | short | invisible | B | OC-3, OC-1 | A-20 |
| C-47 | officials.enforcement (Code Enforcement) | enforcement_cost (complaint investigations) | ambiguous | short | invisible | B | OC-3, CR-12b | A-18, A-19 |
| C-48 | neighbors | compliance_cost (time spent complaining) | ambiguous | short | invisible | B | OC-2, CR-8c, CR-12b | A-18, A-19 |
| C-49 | taxpayers, recipients of other general-fund spending | tax_revenue (TOT) | ambiguous | short–medium | invisible | B | TX-10, CR-8b, CR-12b | A-8, A-10, A-11 |
| C-50 | officials.enforcement (general fund) | non_tax_receipts (registration fees, fines) | increase | short | invisible | B | CR-8b | A-19 |
| C-51 | hosts.fined | resources_available_other_uses | decrease | short–medium | invisible | B | CR-8b, CR-3c | A-3, A-19 |

## Gaps found

**(a) Calculus gaps (a step no core rule covers).** None. Every step was derived from CR-1 to CR-12 or from a pattern whose preconditions held. The step nearest to a gap was the neighbors' amenity (quieter streets): CR-9 (0.7) derives it along `proximity`, at Tier C pending Q20, so it is an open expert question already recorded (GAP-026-1), not a new gap.

**(b) Unclear core rules, including the 0.7 and 0.8 clarifications.**
1. *Rothbard type of a ban on letting one's own home.* The typology in 01_foundations.md calls an intervention autistic when it restricts "a person's own action, with no exchange involved". K1 prohibits an exchange (triangular), yet for second-home owners what it removes is a way of combining their own use with other people's, and the option they fall back to (own weeks, empty the rest) involves no exchange (C-7). CR-1 records the operation correctly (operation 1, dated); the typology has no word for "triangular in form, autistic in what the owner is left with". It did not change any sign.
2. *Proximity evidence and tier.* CR-9 (0.7) holds every `proximity` chain at Tier C. Here the record contains 1,500 complaints a year about STR units, which are actions by neighbors and so, by CR-2, demonstrated evidence that the chain has a sign for some of them. CR-9 gives no route by which such evidence lifts a chain's tier. C-43 stays Tier C.
3. *OC-3's right baseline runs through proximity.* The 0.8 clause's own example (complaints about backyard flocks) and C-47 here both depend on nuisance complaints falling when the activity falls, which is a `proximity` chain. This analysis kept C-47 at Tier B by treating the complaint rate per operating unit as an empirical premise (A-18) rather than deriving it from neighbors' rankings. The catalog should say whether that is allowed, or whether OC-3's right-baseline chain is Tier C whenever the old enforcement was complaint-driven.
4. *`legal_breach` against `informal_activity` under a prohibition with a permitted sub-class.* For lets beyond the cap or under another unit's number made through platforms, the trade runs through the legal market's channels; for lets off-platform, it does not. The analysis split them at the channel (C-9, C-10). 2.4 does not say where the line is.

**(c) Missing or wrong patterns.**
1. *Complaint-only enforcement* (candidate, 06_gaps.md 6.2e, from WE-029). Needed a second time here (C-9, C-10, C-14): CR-1 (a risk equal to the probability of a complaint times the fine) and CR-4 (x: comply, y: violate) unit by unit, with the probability falling where complainants are absent. By the catalog's rule, this second use promotes it. Two additions this case suggests: (i) where the complainants are the people the rule protects, breach concentrates where they are absent, so the rule binds least where it protects least; (ii) the violator can lower the complaint probability by choosing counterparties (screening quiet guests, C-14), which is a non-price allocation of the illegal good. Also (iii) fines fixed in money erode against the gain from breach (TS-3).
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
