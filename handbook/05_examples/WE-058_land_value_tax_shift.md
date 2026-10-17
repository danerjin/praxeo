# WE-058 Revenue-neutral shift from a property tax to a land value tax, phased in over four years

Analyst: draft (Handbook 1.0 held-out test, corrected under 1.1)  |  Rule catalog version: 1.1  |  Status: awaiting expert review

A stylized policy in a fictional city. Several cities tax land at a higher rate than buildings; this one is not modeled on any of them. It is a held-out test of catalog 1.0 on a kind of policy none of the 1.0 changes were drawn from. It probes TX-2 and TX-3 incidence where one taxed factor is fixed in supply (land) and the other is not (buildings), DM-1, CR-7c capitalization and CR-7's 1.0 clause on "which stock" (the tax on land follows the land; the relief on buildings follows the stock of buildings), CR-12's 1.0 note on what the response argument needs (constant cost of building), a revenue-neutral shift in which two taxes move in opposite directions (CR-12, two items, and CR-12f), RS-8 and TS-10 over a four-step phase-in, RS-9's 0.9 clause on location complements (shops near surface parking lots that are built on), RS-4 at the city line, and OC-3 on the cost of assessing land separately. The unclear provision is whether surface parking lots are assessed as vacant land or as improved parcels. The counterfactual throughout is **Vellmoor keeping its property tax on land and buildings together**, with the same levy each year. The probabilities are illustrative; the evidence column says what a real analysis would cite.

## 1. Policy record

**Vellmoor Measure L (Land Value Tax Charter Amendment).** Vellmoor is a city of about 420,000. Its downtown (about 3 km²) is zoned for buildings of up to 12 storeys and has 140 surface parking lots (about 38 ha, 9,800 spaces at about $12 a day, about 85% occupied on weekdays) beside 6,500 spaces in structured garages at about $16 a day. Just outside the city line lies Ostbridge, a growing suburb of 90,000 with a regional shopping mall; its property tax is 1.4% of the assessed value of land and buildings, and Measure L does not touch it. Beyond Ostbridge is unincorporated county land.

**The tax now.** Under Charter §8 the council adopts a levy (a sum of money) in each year's budget; the rate is the levy divided by the assessed value of all taxable property, land and buildings together, assessed at market value every two years. The 2027 levy is $600 million and the rate 1.5%. The levy has grown by about 3% a year. Delinquency is about 1.2% of the levy; unpaid taxes carry a 10% penalty and 1% a month interest, and a parcel may be sold for taxes after three years.

**Assessed values (2026 roll, $ billion).**

| Class | Parcels | Land | Buildings | Total | Land share |
|---|---|---|---|---|---|
| Surface parking lots | 140 | 0.60 | 0.02 (paving, booths) | 0.62 | 97% |
| Other vacant land | 2,300 | 0.40 | 0 | 0.40 | 100% |
| Single-family homes | 105,000 | 6.00 | 10.00 | 16.00 | 37.5% |
| Apartment buildings | 3,200 | 2.40 | 5.60 | 8.00 | 30% |
| Offices and other high-rise commercial | 410 | 2.00 | 5.60 | 7.60 | 26% |
| Low-rise commercial and industrial (strip retail, car dealers, warehouses) | 4,100 | 4.60 | 2.78 | 7.38 | 62% |
| **All** | | **16.00** | **24.00** | **40.00** | **40%** |

About 36% of homes (38,000, mostly on large lots in the older hill districts) have a land share above 40%; the rest are below it. The assessor estimates that the market value of the surface lots in their current use (capitalized parking income) less the depreciated cost of their paving is about $0.30 billion, against $0.60 billion as development sites. The assessor also estimates the ratio of building value to site value for the building that zoning permits and the market would put up: about 3 downtown, about 1.7 in single-family zones (close to what is built there now) and about 0.6 for industrial and outlying commercial sites. Downtown, about 70% of commercial leases are "triple net": the tenant pays the parcel's property tax. Building completions are assessed as they stand on 1 January; a building finished on 2 January pays nothing for that year. The city issues about 1,800 dwelling permits and 60,000 m² of commercial permits a year; Ostbridge about 900 dwellings. Construction trades in the region have about 3% unemployment. A typical new building earns a net rent of about 6% of its value a year.

**Timing.** Measure L qualified for the ballot on 10 June 2026, with polls at 55% to 60% in favor, and passed on 3 November 2026 with 58%. It applies from tax year 2028 (assessment date 1 January 2028). No expiry.

| Field | Value | Source sentence |
|---|---|---|
| Jurisdiction (and what lies just outside) | City of Vellmoor. Just outside: Ostbridge (property tax 1.4% on land and buildings), then county land. | §1: "This chapter applies to all taxable real property in the City." |
| Announced / enacted / effective / expires | Expected from 10 June 2026 (qualified); enacted 3 November 2026; effective tax year 2028; phase-in 2028 to 2031; no expiry. | §1, §9. |
| Enforcement (who, penalties, resources) | City Assessor (valuation), County Treasurer (collection), Board of Equalization (appeals). Penalties as for the property tax now. Assessor's budget rises by about $9 million a year from the general fund, plus about $14 million once in 2027 for a land valuation system; the Board's budget is unchanged. | §6, §7. |

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Land tax | `ad_valorem_tax` (annual, on assessed land value) | Land, whether used or not | Every owner of taxable land | One rate on the taxable value of each parcel; the rate is the levy divided by the city's total taxable value (§3). | As now (public and religious land). |
| K2 Building phase-out | `ad_valorem_tax` (annual, on improvements), reduced in steps | Buildings and other improvements | Every owner of improvements | Improvements count in taxable value at 75% (2028), 50% (2029), 25% (2030) and 0% (2031 and after) (§3). | As now. |
| K3 Assessment of land | Valuation rule | Land value of each parcel, assessed every year | City Assessor | §4(a): "The land value of a vacant parcel is its market value as a site for its highest and best use permitted by zoning." §4(b): "The land value of an improved parcel is the market value of the parcel in its current use, less the depreciated replacement cost of its improvements." | — |
| K4 Revenue neutrality | Rule on the levy | The levy | Council | "The levy shall be set as under §8 and shall not be increased by reason of this chapter." | — |
| K5 Administration | Enforcement | K1 to K3 | Assessor (budget up, general fund), Board of Equalization (budget unchanged) | About $9 million a year more for the Assessor (against about $21 million now for biennial whole-parcel valuation); about $14 million once. Appeals forecast: 9,000 to 12,000 in 2028 against about 6,000 now. | — |

Existing rules that stay in the counterfactual: Charter §8 (the levy) and the council's budget process; zoning, including the downtown height limit and single-family zones; Ostbridge's property tax.

Unclear provisions:
- **U1, surface parking lots.** §2(e): "'Improvements' means buildings, structures and other works affixed to land, including paving." §2(f): "'Vacant parcel' means a parcel on which there is no building." §4 assigns a method to "vacant parcels" (a) and to "improved parcels" (b) without saying which governs a parcel that has improvements but no building. A surface lot is paved and run as a parking business but has no building (apart from a booth on some). Reading U1-a: lots are vacant parcels (no building) and are assessed under §4(a), at their value as development sites (about $0.60 billion in all). Reading U1-b: lots are improved parcels (paving is an improvement) and are assessed under §4(b), at their value as parking businesses less paving (about $0.30 billion). The Assessor has issued no guidance.

Readings get no probability; where a sign depends on U1, one sign per reading is given.

**Figures (static: 2026 values, the 2027 levy of $600 million, no response).**

| Year | Taxable base ($bn) U1-a | Rate U1-a | Rate U1-b | Rate on buildings U1-a (rate × share) |
|---|---|---|---|---|
| Counterfactual (every year) | 40.0 | 1.500% | 1.500% | 1.500% |
| 2028 | 16.0 + 0.75 × 24.0 = 34.0 | 1.765% | 1.780% | 1.324% |
| 2029 | 28.0 | 2.143% | 2.166% | 1.071% |
| 2030 | 22.0 | 2.727% | 2.765% | 0.682% |
| 2031 on | 16.0 | 3.750% | 3.822% | 0 |

Under U1-b the lots' land counts at $0.30 billion, so the land base is $15.70 billion and the rates are slightly higher.

Share of the levy borne by each class (static), against its share without the measure:

| Class | Without (all years) | 2028 U1-a | 2031 U1-a | 2031 U1-b |
|---|---|---|---|---|
| Surface lots | 1.55% | 1.81% | 3.75% | 1.91% (2028: 0.93%) |
| Other vacant land | 1.00% | 1.18% | 2.50% | 2.55% |
| Homes | 40.0% | 39.7% | 37.5% | 38.2% |
| Apartments | 20.0% | 19.4% | 15.0% | 15.3% |
| Offices | 19.0% | 18.2% | 12.5% | 12.7% |
| Low-rise commercial and industrial | 18.45% | 19.7% | 28.75% | 29.3% |

Under U1-b the lots' share is 0.93% in 2028, 1.12% in 2029 and 1.41% in 2030 (all below 1.55%), and 1.91% from 2031 (above it). In every year of the phase-in, a parcel's share rises if its land share (land over land and buildings together, on the 2026 roll) exceeds the city-wide 40% (about 39% under U1-b), and falls if it is below. The Assessor's static projection, which ignores capitalization, puts the 2031 rate at 3.75%; its own capitalization estimate (land values about 15% below the static figure by 2031) puts it nearer 4.4%.

Per downtown site, with a building worth three times the site: without the measure, putting up the building adds about 1.5% × 3 = 4.5% of the site's value a year in tax. Under U1-a it adds nothing from 2031 (land is assessed at site value whether built on or not). Under U1-b a lot that is built on moves from current-use value (about half its site value) to full site value, which adds about 3.8% × 0.5 = 1.9% of site value a year from 2031. Paving a vacant parcel costs about 3% of its site value once; under U1-b it would cut the parcel's land value by about half, saving about 0.9% (2028) to 1.9% (2031 on) of site value a year.

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | Rule families |
|---|---|---|---|
| K1 | Binary: a transfer of means from every landowner to the city, attached to holding land, not to any use of it (CR-1, operation 4 for a given parcel: no choice about its use avoids it; operation 3 only on the option of holding land at all). | Yes: the land rate rises above the counterfactual rate in every year (figures; A-1). | TX-1, TX-2 (read for a tax on a fixed factor), DM-1, CR-7b, CR-7c, CR-10c, SB-4, TS-10, CR-4 exception |
| K2 | Binary: a reduction, in steps, of a tax attached to the option of having improvements (CR-1, operation 3, dated: each step is performed on 1 January of its year). | Yes (figures). | TX-3 (in reverse), RS-6 (in reverse), RS-8, RS-13, RS-4, TS-1, CR-7 (1.0: which stock), CR-12 (1.0: response argument) |
| K3 | Part of the definition of the tax base. §4(b) attaches a burden to raising a parcel's current-use value, and so works partly as a tax on developing an improved parcel; §4(a) does not. | Under U1, decides the lots' base. | RS-5, CR-4, OC-2, OC-3 |
| K4 | Binary: fixes the sum taken; the two taxes move in opposite directions so that the levy is the same as in the counterfactual. | Yes, if the council's levy is unchanged (A-1). | CR-8b, CR-12 (0.8: two items; f) |
| K5 | Binary: administration from the general fund within an unchanged levy (Assessor) and from an unchanged budget (Board). | Yes. | OC-3 (general budget; 0.9 fixed budget; right baseline) |

**Why land and buildings differ.** Land in Vellmoor cannot be produced or moved; buildings can be added (and, slowly, not replaced). K1 is levied on assessed land value whether the land is built on, paved or empty, so no use of a parcel lowers it (under U1-a, and for all land assessed under §4(a)). It changes no owner's ranking of one use of land against another (CR-4: it is paid under every option), apart from CR-4's exception: an owner short of means may have to sell or borrow (C-22). K2 lowers a tax that was paid only by those who chose to put up and keep improvements, so it makes that option better (CR-4b). §4(b) reintroduces a smaller burden on developing an improved parcel, because developing raises its value in current use; which parcels it reaches depends on U1.

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `owners.lots` (`factor_owners.specific`) | Owners of downtown surface lots | Land taxed at the land rate; under U1-a on site value, under U1-b on current-use value until built on. |
| `owners.vacant` | Owners of other vacant land, mostly outlying | Land taxed at the land rate on site value. |
| `owners.homes.high_land_share`, `owners.homes.low_land_share` | Owner-occupiers of single-family homes, split at a 40% land share | Land taxed more, the house less; the net depends on the land share. |
| `owners.apartments` | Owners of apartment buildings | Large building relief; land taxed more. |
| `owners.offices` | Owners of offices and high-rise commercial buildings | Large building relief; land taxed more. |
| `owners.lowrise` | Owners of strip retail, car dealers, warehouses, light industry | Land taxed much more; small building relief. |
| `developers` (`sellers.prospective` of floor space) | Builders of new floor space in Vellmoor and Ostbridge | New buildings in Vellmoor are taxed less, then not at all. |
| `tenants.commercial.nnn` | Commercial tenants on triple-net leases | Pay the parcel's tax during the lease. |
| `tenants` (residential and commercial) | Renters of floor space | Market rents follow the stock of floor space. |
| `construction_workers` (`input_suppliers`) | Trades and laborers | More building in Vellmoor, less in Ostbridge. |
| `parking_users`, `parking_operators` | Drivers parking downtown; lot and garage operators | Lots may be built on (U1-a) or vacant land paved (U1-b). |
| `businesses.downtown` | Shops and cafés near the lots | Customers who park on lots; new occupants of buildings on former lots. |
| `owners.ostbridge` (`neighboring_jurisdictions`) | Landowners and builders in Ostbridge | Building moves across the line. |
| `officials.enforcement` | City Assessor and County Treasurer | Land assessed separately each year; levy collected from a different base. |
| `officials.adjudication`, `appellants` | Board of Equalization and those who appeal | More appeals on an unchanged budget. |
| `taxpayers`, recipients of other city spending | Funders and beneficiaries of the general fund | Pay for the Assessor's added cost within an unchanged levy. |
| `buyers.prospective` (land) | Later buyers of land | Pay the capitalized price (SB-4). |
| `lobbying groups` | Lot owners, low-rise owners, homeowner groups, developers | Concentrated stakes in U1, §4(b) and relief. |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | `officials.enforcement` | `tax_revenue` (item: tax on buildings and other improvements) | decrease | short (2028) to long | CR-1, CR-12 (0.8: two items; 1.1: items that cancel), arithmetic on the figures | A-1 |
| C-2 | `officials.enforcement` | `tax_revenue` (item: tax on land) | increase | short (2028) to long | CR-1, CR-12 (0.8: two items; 1.1: items that cancel), TX-1 (1.1: rate rises), arithmetic on the figures | A-1 |
| C-3 | `owners.offices` | `tax_share_borne` (share of the levy, against the share without the measure) | decrease | short to long | CR-8b, CR-12e (arithmetic) | A-1, A-2 |
| C-4 | `owners.apartments` | `tax_share_borne` | decrease | short to long | CR-8b, CR-12e (arithmetic) | A-1, A-2 |
| C-5 | `owners.homes.low_land_share` | `tax_share_borne` | decrease | short to long | CR-8b, CR-12e (arithmetic) | A-1, A-2 |
| C-6 | `owners.homes.high_land_share` | `tax_share_borne` | increase | short to long | CR-8b, CR-12e (arithmetic) | A-1, A-2 |
| C-7 | `owners.lowrise` | `tax_share_borne` | increase | short to long | CR-8b, CR-12e (arithmetic) | A-1, A-2 |
| C-8 | `owners.vacant` | `tax_share_borne` | increase | short to long | CR-8b, CR-12e (arithmetic) | A-1, A-2 |
| C-9 | `owners.lots` | `tax_share_borne` (2028 to 2030) | U1-a: increase; U1-b: decrease | short to medium | CR-8b, CR-12e (arithmetic; 1.1: ratios) | A-1, A-2 |
| C-10 | `owners.lots` | `tax_share_borne` (2031 on) | U1-a: increase; U1-b: increase | medium to long | CR-8b, CR-12e (arithmetic; 1.1: ratios) | A-1, A-2 |

**Two taxes in opposite directions (C-1, C-2; CR-12, two items).** The measure moves two named items of one variable, the city's tax revenue, in opposite directions: the tax on buildings falls in every year from 2028 (2028: about $318 million on buildings at 1.324% against $360 million at 1.5%) and the tax on land rises. CR-12's 0.8 note says to record each item and the total separately. The total levied is fixed by K4 and Charter §8 to be the levy the council would have set: the two items cancel by construction and nothing else moves the levy, so under CR-12f and CR-12's 1.1 note on items that cancel the total is not recorded (section 7; Gaps found, b1). A-1 is the premise that the levy itself is the same. The land item rises although the land base falls as values capitalize the tax (C-35): under a levy the rate, not the revenue, absorbs a fall in the base, so TX-1's 1.1 premise on rate rises (the base does not fall enough to offset the rate) is met by arithmetic with A-1.

**Who pays more (C-3 to C-10).** Because the levy is fixed, each class's bill is its share of the levy, and each share moves by arithmetic on the roll: a parcel's share rises in every year if its land share exceeds the city-wide 40% (about 39% under U1-b), and falls if below. This is CR-12e's arithmetic on the case's figures, by class, on a ratio (CR-12, 1.1: ratios); it is a count over a distribution only where the distribution is in the figures (CR-12e, 0.8), which it is for the classes in the roll and for the split of homes at 40%. Each class's bill has the same two items as the city's revenue: its land part rises and its building part falls; the class sign is their total, settled by the arithmetic. The surface lots are the one class whose sign depends on U1 and on the window (C-9, C-10): under U1-a the lots' base is unchanged and the rate rises, so their share rises at once; under U1-b their base halves at once while the rate rises in steps, so their share falls in 2028 to 2030 and rises from 2031. These are per-window signs on a share paid in each year (02_ontology.md, 2.5), not a timing shift. A class's position against the 40% line could be crossed by moving either term of its land share (CR-1, 1.1): by adding building (C-12, untaxed under K2) or by lowering assessed land value (only under §4(b), C-13); A-2 is the premise that neither reverses a class's position over the phase-in.

**TX-2 for a tax on land.** TX-2's If clause is a tax "on the sale of a good"; K1 is levied on holding land, whatever is done with it. Its 1.1 clause on a fixed factor covers the case: where the base is a factor in fixed supply, quantity does not fall, and the tax is capitalized into the factor's value and borne by its owner when it becomes expected. That is also what the core rules give: neither side can reduce the tax by changing quantity (the stock of land is fixed, and an owner who leaves land empty pays the same tax under §4(a)), so the land tax gives no change in the land in use (CR-4: it is paid under every option), and owners, who have no alternative use that escapes it, bear it (CR-7b). It is capitalized into land values when it becomes expected (CR-7c; C-34 to C-38), and the rent users pay for land is not raised by the land tax's own chain (C-29, where the building relief is the other chain). TX-2's main quantity conclusion is not used. DM-1 is not cited: its If clause asks that TX-2's main clause or SB-2 apply, and incidence here rests on CR-7b and TX-2's fixed-factor clause. Under §4(b) the land tax does depend on current use (C-11, C-13), which the fixed-factor clause does not cover; there it is derived from CR-1 and CR-4.

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-11 | `developers`, `owners.lots` | `investment_target` (new buildings on downtown surface lots) | U1-a: increase; U1-b: increase | medium | TX-3 (in reverse), RS-6 (in reverse), CR-4b, CR-12e (arithmetic) | A-3, A-4 |
| C-12 | `developers` | `investment_target` (new buildings and additions on other sites in Vellmoor, including redevelopment of improved parcels) | increase | medium to long | TX-3 (in reverse), RS-6 (in reverse), CR-4b, CR-12h, CR-12e (arithmetic) | A-3, A-5 |
| C-13 | `owners.vacant`, `owners.lots` | `reclassification` (works on vacant sites whose purpose is assessment under §4(b): low-cost buildings; under U1-b also paving for parking) | U1-a: increase; U1-b: increase | short to medium | RS-5, CR-4 | A-6, A-7 |
| C-14 | `parking_operators` | `quantity_supplied` (surface parking spaces downtown) | U1-a: decrease; U1-b: ambiguous | medium | RS-13, CR-4, CR-12b | A-3, A-4, A-7 |
| C-15 | `developers` | `quantity_supplied` (buildings completed in the weeks just before 1 January, each year from 2028 on) | increase | short to long | RS-8, CR-10a, CR-4 | A-8 |
| C-16 | `developers` | `quantity_supplied` (buildings completed in the weeks just after 1 January, each year from 2028 on) | decrease | short to long | RS-8, CR-10a, CR-4 | A-8 |
| C-17 | `developers`, `owners.ostbridge` | `quantity_supplied` (new buildings in Ostbridge) | decrease | medium to long | RS-4, CR-7a | A-3, A-12 |
| C-18 | `tenants.commercial.nnn` (on low-rise parcels) | `price_paid` (occupancy cost including the passed-through tax, during existing leases) | increase | short | CR-9 (`contract`: the lease), CR-6 (0.7: existing contracts), CR-5c | A-1, A-2, A-13 |
| C-19 | `tenants.commercial.nnn` (in offices) | `price_paid` (occupancy cost including the passed-through tax, during existing leases) | decrease | short | CR-9 (`contract`), CR-6 (0.7: existing contracts), CR-5c | A-1, A-2, A-13 |
| C-20 | `owners.lowrise` | `net_price_received` (rent net of tax, on leases renewed after 2028) | decrease | short to medium | CR-7b, TX-2 (1.1: a fixed factor), CR-5c | A-1, A-13, A-14 |
| C-21 | `owners.offices` | `net_price_received` (rent net of tax, on leases renewed after 2028, before the stock grows) | increase | short to medium | CR-7b, CR-5c | A-1, A-13, A-14 |
| C-22 | `owners.homes.high_land_share`, `owners.lowrise`, `owners.vacant` (those short of means) | `turnover` (sales of parcels) (+), `legal_breach` (property tax unpaid when due) (+) | at_least_one_increase | short to medium | CR-4 (exception: a change in means), CR-3a | A-9 |
| C-24 | `lobbying groups` | `lobbying_effort` (on questions that exist only under the measure: the reading of U1, §4(b), a delay of the steps, deferral or relief for homeowners) | increase | short to medium | RS-7 (1.0, 1.1), CR-4 (1.0; 1.1: the same question), CR-12 (0.9: activities that exist only under the policy) | A-10 |
| C-25 | owners of all classes | `compliance_cost` (appeals of land valuations, private appraisals) | increase | short to medium | OC-2, CR-8c | A-11 |
| C-51 | `developers`, owners of developable sites | `applications` (dwelling and commercial building permits) | increase | short (from 10 June 2026) | CR-10a, CR-4, CR-12h | A-3, A-20 |

**Building on the lots (C-11).** Before the measure, putting a building on a downtown lot added about 4.5% of the site's value a year in tax (1.5% on a building worth three times the site). K2 removes that by 2031. K1 does not reach the choice under U1-a: the lot pays the land rate on its site value whether it is parked on or built on. Some projects that do not pay without the measure pay with it (A-3), so building on lots increases (TX-3 in reverse; RS-6 in reverse; CR-4b, x: keep parking, y: build). Under U1-b, building moves the lot from current-use value to site value and so adds about 1.9% of site value a year from 2031 (§4(b)); that is still less than the 4.5% it adds without the measure (A-4, arithmetic on the case's figures and the assessor's ratio). The sign is `increase` under both readings, by a smaller margin under U1-b. In 2028 alone, under U1-b, the added tax (about 4.0% for the building at the 2028 rate plus 0.9% for the uplift) is close to the counterfactual 4.5%; a building lasts decades, so the comparison that decides the choice is the stream from 2031 on (A-4).

**Building elsewhere (C-12).** The same relief reaches every site. On improved parcels, §4(b) taxes the rise in current-use value that redevelopment brings, under both readings; for typical projects this is below the building tax without the measure (A-5). Building rises in every window against the counterfactual, since the building tax is lower in every year from 2028 (CR-12h; the path is in section 8).

**Assessment by current use invites reclassification (C-13).** §4(b) values improved parcels in their current use, so an owner of a vacant site can lower its land value by putting it to a low-yield use that counts as an improvement (RS-5; CR-4, x: leave vacant, y: improve cheaply). Under U1-a this takes a building (A-6: some owners can put up a low-cost building at a cost below the tax saved). Under U1-b paving is enough: paving costs about 3% of site value once and saves about 0.9% to 1.9% of site value a year (A-7). Against the counterfactual, where no such work pays (assessment at market value), both are `increase`. The works are an activity that would not happen without the measure; their timing before the first assessment date is a path note (section 8), not a consequence (02_ontology.md, 2.5).

**Parking spaces (C-14).** Under U1-a lots are built on (C-11) and no paving pays, so surface spaces downtown fall. Under U1-b lots are built on (−) and vacant parcels are paved for parking (C-13, +); no premise ranks them, so `ambiguous` (CR-12b).

**Completions around 1 January (C-15, C-16).** Without the measure, a building finished just after 1 January escapes a year's tax at 1.5% of its value, so some completions are delayed past the date. Under the measure the year's tax escaped is smaller (1.32% in 2028, 1.07%, 0.68%, then nothing), so fewer are delayed: completions in the weeks just before 1 January rise and those just after fall, each window signed against the counterfactual (RS-8; 02_ontology.md, 2.5; A-8). From 2031 the measure leaves no incentive to delay, while the counterfactual's 1.5% building tax rewards a January completion every year, so the two windows stay signed in every year from 2028 on, not only during the phase-in. A longer delay, to wait for a lower step, does not pay for most projects: a year's delay saves at most 1.32% of the building's value in tax and forgoes about 6% in net rent (arithmetic on the figures), so no larger shift between years is signed (section 8).

**Ostbridge (C-17).** K2 favors building on the Vellmoor side of the line; Ostbridge keeps its 1.4% tax on buildings. Projects that could go either side move to Vellmoor (RS-4: where the policy favors activity inside, `quantity_supplied` decreases just outside; A-12). The effect on Ostbridge land is C-40.

**Leases (C-18 to C-21).** A triple-net lease passes the parcel's tax to the tenant while it runs (`contract`; CR-6 0.7: terms fixed by existing contracts count as regulated while they last). So, during existing leases, tenants of low-rise parcels pay more and office tenants pay less (C-18, C-19; A-13); tenants of lot operators follow the lots' per-reading signs (C-9) and are not recorded separately. On renewal, the rent for space is set by the stock and by tenants' demand, neither of which the land tax changes (section 6), so the total a tenant pays returns to the market level and the change in tax settles on the owner (CR-7b; TX-2, 1.1: a fixed factor): owners of low-rise parcels receive less net of tax (C-20), office owners more (C-21), until the stock of space grows (C-30).

**Owners short of means (C-22).** K1 is paid whatever the owner does, so it changes no ranking among uses (CR-4), except through CR-4's exception: it takes means. Owners whose bills rise and who cannot pay from income (retired owners on large lots, marginal low-rise businesses) sell sooner than they would have, or fall behind (A-9). The measure has no deferral. A-9 says only that they do one or the other (or neither, paying from savings or a loan), so the two margins are one group, `at_least_one_increase`; neither is signed alone. RS-3 is not cited: arrears from a want of means are not evasion that pays. For classes whose bills fall, a fall in delinquency would need a premise the case lacks, and is not signed.

**Lobbying (C-24).** The shift itself was contested on the counterfactual path: Measure L was a ballot campaign, and opponents could have pursued the question again with or without it. By CR-4's 1.0 and 1.1 notes (the same question is the policy field contested on the counterfactual path, the taxation of land against buildings) and RS-7 (1.0), lobbying on the shift as such is signed only against that contest and needs a premise the case lacks, so it is not signed. The questions C-24 names exist only under the measure: lobbying on them is an `increase` against none (CR-12, 0.9; A-10).

**Permits from the announcement (C-51).** Buildings started in 2026 and 2027 are finished two to four years later, when the building tax is 25% to 75% lower or nil, so some projects that would not have been started without the measure start once it is expected (CR-10a; CR-4, x: hold, y: build; A-3, A-20). Permits are an activity that also happens without the measure, so this is signed in its window against the counterfactual; since building is higher in every window (CR-12h, section 8), the rise is not taken from a later window. Starting later to finish under a lower step does not pay (a year's delay forgoes about 6% of net rent to save at most 1.32%).

**Appeals (C-25).** Each parcel's land value is now assessed every year and separately from its buildings, and the land share decides the bill. Owners who expect to gain from an appeal file one (A-11; OC-2, CR-8c). Under U1-b, current-use values of lots and paved parcels are a further subject of appeal; the sign is the same under both readings.

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-26 | `tenants` | `price_paid` (market rent per m² of floor space of a given quality) | no_change | short | CR-6, CR-7b, TX-2 (1.1: a fixed factor), TS-1 | land and buildings: `input_to` floor space | A-14 |
| C-27 | `tenants` | `price_paid` (market rent per m² of floor space of a given quality) | decrease | long | RS-13, CR-6 (0.9: splitting a shift), CR-12e, CR-12 (1.0: what the response argument needs) | new buildings add to the stock of floor space: `same_market_other_segment` | A-3, A-15 |
| C-28 | `developers` | `capital_stock_target` (floor space in Vellmoor) | increase | long | TS-1 (in the other direction), RS-6 (in reverse), CR-10b | — | A-3, A-15 |
| C-29 | `tenants` (users of land) | `price_paid` (rent for land as such: ground rents on new ground leases) | increase | short to medium | CR-7b, TX-2 (1.1: a fixed factor), CR-5c, CR-12a | ground lease: `contract`; building `input_to` the yield of a site | A-14, A-21 |
| C-30 | `developers` | `return_on_capital` (new buildings in Vellmoor) | increase | short to medium | CR-7a, CR-4b | — | A-3, A-14 |
| C-31 | `developers` | `return_on_capital` (new buildings in Vellmoor) | no_change | long | CR-7a, CR-12e (response argument), CR-12 (1.0: constant cost) | — | A-15, A-16 |
| C-32 | owners of existing buildings (`owners.offices`, `owners.apartments`, `owners.homes.*`) | `asset_value` (item: existing buildings) | increase | short (from 10 June 2026) | CR-7b, CR-7c, CR-10c, SB-4, TS-10 (1.1: taxes), CR-12 (1.1: the response argument in every direction) | — | A-14, A-20, A-23 |
| C-33 | owners of existing buildings | `asset_value` (item: existing buildings, per m² of a given age and quality) | no_change | long | CR-7 (1.0: which stock), CR-12e, CR-12 (1.0: constant cost) | — | A-15, A-16 |
| C-34 | `owners.lots`, owners of downtown sites (including `owners.vacant` downtown), `owners.homes.*` | `asset_value` (item: land, sites whose permitted building is worth more than about 1.5 times the site: downtown, single-family) | ambiguous | short (from 10 June 2026) | CR-7b, CR-7c, CR-10c, LW-9, LW-10, CR-12b | building `input_to` the yield of a site | A-1, A-20, A-21 |
| C-35 | `owners.vacant` (outlying), `owners.lowrise` | `asset_value` (item: land, sites whose permitted building is worth less than about 1.5 times the site: industrial, outlying) | decrease | short (from 10 June 2026) | CR-7b, CR-7c, CR-10c, SB-4, CR-12e (arithmetic), TS-10 (1.1: taxes) | as C-34 | A-1, A-17, A-20 |
| C-36 | `owners.lowrise`, `owners.vacant` (outlying) | `asset_value` (parcels) | decrease | short (from 10 June 2026) | CR-7c, CR-10c, SB-4, CR-12e (arithmetic), TS-10 (1.1: taxes) | — | A-1, A-2, A-17, A-20 |
| C-37 | `owners.offices`, `owners.apartments`, `owners.homes.low_land_share`, `owners.homes.high_land_share` | `asset_value` (parcels) | ambiguous | short (from 10 June 2026) | CR-7c, CR-10c, CR-12b | — | A-1, A-2, A-15, A-20, A-21 |
| C-38 | `owners.lots` | `asset_value` (parcels) | U1-a: ambiguous; U1-b: ambiguous | short (from 10 June 2026) | CR-7c, CR-10c, CR-12b | as C-34 | A-1, A-4, A-20, A-21 |
| C-39 | `owners.offices`, `owners.apartments`, `owners.homes.low_land_share` | `return_on_capital` (net of tax, 2028 to 2030, before the stock grows) | increase | short to medium | CR-7b, CR-12e (arithmetic) | — | A-1, A-2, A-14 |
| C-40 | `owners.ostbridge` | `asset_value` (land in Ostbridge) | decrease | short to medium | CR-9, CR-7c, CR-6 (1.0: small effects are signed) | Ostbridge sites and Vellmoor sites: `substitute` | A-12, A-20 |
| C-41 | `construction_workers` | `employment` (in Vellmoor) (+), `hours_worked` (+) | at_least_one_increase | medium | CR-9, LW-10, CR-6 (1.1: labor demand), OC-5 | labor `input_to` building | A-3 |
| C-42 | `construction_workers` | `wage_rate` (construction trades in the region) | increase | short to medium | CR-9, CR-6 (0.9: splitting a shift) | labor `input_to` building | A-3, A-18 |
| C-43 | `parking_users` | `price_paid` (surface and garage parking downtown) | U1-a: increase; U1-b: ambiguous | medium | RS-13, RS-16, CR-6 (0.9: splitting a shift), CR-12b | lots and garages: `substitute` | A-3, A-7, A-22 |
| C-44 | `businesses.downtown` | `quantity_traded` (sales near former lots) | U1-a: ambiguous; U1-b: ambiguous | medium | RS-9 (0.9: location complements, new occupants), CR-9, CR-12b | purchases downtown: `complement` (note `location`) to parking and to occupying space downtown | A-3, A-19 |
| C-52 | `sellers.substitutes` (owners of downtown garages) | `net_price_received` (garage parking) | U1-a: increase; U1-b: ambiguous | medium | CR-9, CR-6 (0.9: splitting a shift), RS-16 | lots and garages: `substitute` | A-3, A-7, A-22 |
| C-53 | `sellers.substitutes` (owners of downtown garages) | `asset_value` (garages) | ambiguous | short (from 10 June 2026) | CR-7c, CR-10c, CR-12b | lots and garages: `substitute` | A-3, A-15, A-20, A-22 |
| C-54 | `buyers.substitutes` (buyers of other construction work: renovation and building outside the new projects, including in Ostbridge) | `price_paid` (construction work) | increase | short | CR-9, CR-7a, CR-6 (0.9: splitting a shift) | the same regional trades `input_to` other construction | A-3, A-18 |
| C-55 | `buyers.substitutes` (buyers of construction work outside Vellmoor that the measure does not touch: renovation and other work in Ostbridge and the county) | `quantity_traded` (construction work) | decrease | short | CR-4c, CR-8a, CR-9 | as C-54 | A-3, A-18 |

**Rents for space (C-26 to C-29).** In the short run the stock of floor space is fixed (A-14). The land tax does not change it, nor tenants' demand, so it cannot raise rents: by CR-7b and TX-2's 1.1 clause on a fixed factor the owners of the fixed factor bear it (rents for land as such do not change on its account, at any horizon; C-29 combines this chain with the building relief). The building relief does not lower rents either until the stock grows: a fixed stock keeps the relief (CR-7b; C-26, `no_change`, signed only with A-14). As new buildings are added (C-11, C-12, C-28), the stock grows and rents fall against the counterfactual (C-27; RS-13: added supply at an unchanged rent leaves owners unsatisfied; CR-6 0.9: the split between rent and quantity needs a premise that demand is not perfectly elastic, A-15).

**What the response argument gives here (C-27, C-31, C-32, C-33; CR-12, 1.0 and 1.1).** The change is a higher net yield on new building (K2). The response is more building, which lowers rents and with them the yield on new building. The response cannot push yields on new building below what capital earns elsewhere, for building stops there (CR-7a, CR-12e). CR-12's 1.0 note says what follows. (1) The argument shows that yields are equalized, not where rents end: so builders' return is `increase` while the stock is adjusting (C-30) and `no_change` in the long run (C-31). (2) The total it bounds is all floor space of a given quality in Vellmoor, existing and new together, since they are let in one market. (3) The constant-cost premise: if the cost per m² of building does not change as building expands (A-16), equal yields are restored at a rent lower than the counterfactual by about the building tax removed, and the value of existing buildings per m² returns to the cost of replacing them, as without the measure (C-33). With rising cost (scarce trades, C-42) rents fall by less; with falling cost, by more. The sign of C-27 needs only that the stock grows and demand is not perfectly elastic (A-15); the constant-cost premise fixes the size, which is why C-31 and C-33, and not C-27, cite A-16. CR-12's 1.1 note states the mirror case: an expansion that lowers a price is bounded by the old price, with a premise that cost per unit does not fall as the activity expands (A-23). That premise is what keeps long-run net rents on existing buildings at or above the counterfactual (rents fall by no more than the tax removed), and so what C-32's rise at expectation needs; with falling cost, rents could fall by more than the tax removed and C-32 would be `ambiguous` (Gaps found, b2). (4) Second responses: people and firms drawn into Vellmoor by lower rents raise demand, but they respond to the rent fall itself and cannot reverse it; the reclassification works of C-13 add nothing to floor space of value and are not a chain here.

**Which stock (CR-7, 1.0; C-32 to C-35).** The measure changes the yield of two durable means owned together on most parcels, and their values follow different stocks. The relief on buildings raises the net yield of existing buildings; while their stock is fixed, owners keep it (CR-7b) and their value rises when the measure becomes expected (C-32; CR-7c, CR-10c). As the stock grows, the relief passes to tenants and the value per m² returns to replacement cost (C-33, with A-16). The tax on land falls on a stock that cannot grow: it is capitalized when expected and stays (C-35). CR-7c's note on probability applies: values moved part of the way from 10 June 2026, when the measure qualified with majority support in polls, and the rest on 3 November (A-20); the loss on land is shared among those who held it over those months. Later buyers pay the capitalized price and neither gain nor lose from the measure as it stands (SB-4).

**Land values: two chains (C-34, C-35).** The extra land tax lowers every site's value (−). The building relief raises the value of a site as far as developers' bids for it include the tax they save on the building they would put up (A-21), and land works with more capital per m² (LW-9, LW-10) (+). The most the relief can add to a site's yearly yield is the building tax removed on its permitted building, 1.5% × (building value / site value) of site value. The land tax adds about 2.25% of site value a year from 2031 at the static rate, more with capitalization (figures). For sites whose permitted building is worth less than about 1.5 times the site (industrial and outlying commercial land at about 0.6, outlying vacant land), the most the relief can add (about 0.9% a year) is less than what the tax takes: CR-12e by arithmetic on the case's figures, `decrease` (C-35; A-17). For downtown sites (ratio about 3) the relief can add up to about 4.5% a year against the tax's 2.25% to 2.9%, and for single-family sites (about 1.7) up to about 2.55%, close to the tax; how much of it a site keeps, rather than tenants (C-27), depends on demand for space, which no premise in the case settles: `ambiguous` (C-34).

**Parcels (C-36 to C-39).** For a whole parcel, the net yield changes by the change in its bill (C-3 to C-10), plus any change in the rent it earns. For low-rise and outlying vacant parcels, whose bills rise, rents for their space cannot rise on account of the measure (C-26, C-27) and the relief on what could be built on their sites is small (C-35): their values fall (C-36; arithmetic on the figures, A-2, A-17). For classes whose bills fall, net yields rise until the stock grows (C-39), but the value at expectation also capitalizes the later fall in rents (C-27): two chains, no premise ranks them, `ambiguous` (C-37). Homes on large lots pay more (C-6), but zoning lets a larger house be built on most of them, and the relief on that house raises what the site is worth to a buyer (A-21): also `ambiguous` (C-37).

**The lots (C-38).** A downtown lot is all land with a high permitted building, so C-34's two chains apply in full. Under U1-a the lot pays the land rate on its site value whether parked or built on; under U1-b it pays on current-use value until built on, and building raises its base (§4(b), A-4). U1-b leaves more value with a lot held as parking than U1-a does, but neither reading settles the sign: `ambiguous` under both.

**Ground rents (C-29).** Two chains reach what users pay for land as such. The land tax's own chain gives no change (above). The building relief raises what a lessee who builds will pay for a site, since part of the building tax saved enters bids for sites (A-21; CR-5c: the bargaining range of the ground lease moves). No chain lowers ground rents while the stock of space is still adjusting (A-14; TS-1), so by CR-12a the sign is `increase` in the short to medium run. In the long run the fall in rents for space (C-27) passes part of the relief to tenants and opposes it; the response argument bounds yields on building, not ground rents, so no long-run sign is recorded.

**Garages (C-52, C-53).** Under U1-a lots are built on and surface spaces fall (C-14), so demand turns to garages, which cannot be added within a few years (A-22): their owners receive more (C-52; CR-9 along the `substitute` relation, CR-6). Under U1-b the spaces are `ambiguous`, so the garages' receipts are too. Their value at expectation has two chains: the higher receipts (U1-a) and, if their land share is low, a lower tax share (+); and the expected entry of new garages and other buildings that K2 untaxes, which lowers later receipts, as for C-37 (−). No premise ranks them: `ambiguous` under both readings (C-53).

**Ostbridge (C-40).** Building that moves to Vellmoor (C-17) lowers demand for Ostbridge sites, whose stock is fixed, so their value falls (CR-9 along the `substitute` relation; CR-7c). The effect may be small; by CR-6's 1.0 note it is signed, and its size goes in the evidence column (A-12).

**Builders and trades (C-41, C-42, C-54, C-55).** More building in Vellmoor raises demand for trades there (CR-9, LW-10); part of it is drawn from Ostbridge (C-17) and from other work (OC-5, 0.9: new to the place, lost at the origin). Construction in Vellmoor is an existing activity, so the labor it hires moves as a group of `employment` and `hours_worked` (C-41; CR-6, 1.1: labor demand). The regional wage rises where the trades cannot expand at once (C-42; CR-6 0.9; A-18), and the wage rise reaches every buyer of the same trades: other construction costs more (C-54; CR-7a). Where that work gains nothing from the measure (renovation and other work outside Vellmoor), less of it is done (C-55; CR-4c, CR-8a); renovation inside Vellmoor is left out of C-55, since K2 also untaxes what it adds, an opposing chain.

**Parking (C-43).** Under U1-a surface spaces fall (C-14) while drivers' demand is unchanged, and garages cannot be added at once (A-22), so the price of parking downtown rises (RS-13, withdrawn supply; RS-16 for the garages as the substitute). Under U1-b the spaces are `ambiguous` (C-14), so the price is too.

**Shops near the lots (C-44; RS-9, 0.9).** Purchases made by drivers who park on downtown lots are tied to parking there. Under U1-a fewer and dearer spaces cut those purchases (−; A-19). RS-9's 0.9 clause adds the opposing chain: the measure changes who occupies the location, and the residents and workers in buildings put up on former lots buy nearby (+). No premise ranks them, so `ambiguous`. Under U1-b, lots are built on as well (the new occupants chain stands), while the parking chain is itself ambiguous (C-14, kind 3): `ambiguous`.

Stopping points. The spending of owners whose bills change (other than as `resources_available_other_uses`), the suppliers of downtown shops, Ostbridge's own levy and rate (set by its council: a fall in its base raises its rate, which is depth 4 and diffuse), and lenders whose collateral loses value: stopped. Traffic and environmental effects of fewer surface lots: out of scope.

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `officials.enforcement`, `tax_revenue` (total levied), all years | Land item (C-2). | Building item (C-1). | Cancel by construction: K4 fixes the levy, and nothing else moves it (CR-12f; CR-12, 1.1: items that cancel). | Not reported. |
| Each owner class, `tax_share_borne`, short to long | Land part of its bill. | Building part of its bill. | Arithmetic on the roll, on a ratio (CR-12e; 1.1: ratios), class by class. | C-3 to C-10 as stated. |
| `owners.lots`, `tax_share_borne`, 2028 to 2030 | Rate rises (both readings). | Under U1-b, base halves at once. | Arithmetic per reading. | U1-a **increase**; U1-b **decrease** (C-9). |
| `developers`, `investment_target` on lots, medium | Building relief (K2). | Under U1-b, §4(b) taxes the uplift when built on. | Arithmetic (A-4): uplift tax below the building tax removed. | **increase** under both readings (C-11). |
| `parking_operators`, `quantity_supplied` (surface spaces), medium | Under U1-b, paving of vacant parcels (C-13). | Lots built on (C-11). | None under U1-b. | U1-a **decrease**; U1-b **ambiguous** (C-14). |
| `tenants`, `price_paid` (space), long | People and firms drawn in by lower rents (a response to the fall). | More floor space (C-28). | CR-12e response argument: the inflow cannot reverse the fall that drew it. | **decrease** (C-27). |
| Owners of downtown sites, `asset_value` (land), short | Building relief captured by sites (A-21; LW-9). | Extra land tax. | None: share kept by sites unknown. | **ambiguous** (C-34). |
| Owners of low-intensity sites, `asset_value` (land), short | Building relief on a small permitted building. | Extra land tax. | Arithmetic (A-17): the most the relief can add is below what the tax takes. | **decrease** (C-35). |
| Low-rise and outlying vacant owners, `asset_value` (parcels), short | Small relief on what could be built. | Bill rises; rents cannot rise. | Arithmetic (A-2, A-17). | **decrease** (C-36). |
| Homes on large lots, `asset_value` (parcels), short | Relief on a larger permitted house (A-21). | Bill rises (C-6). | None. | **ambiguous** (C-37). |
| Bill-falling classes, `asset_value` (parcels), short | Bill falls. | Expected fall in rents as stock grows (C-27). | None. | **ambiguous** (C-37). |
| `businesses.downtown`, `quantity_traded`, medium | New occupants of built-on lots. | Fewer, dearer spaces (U1-a); ambiguous spaces (U1-b). | None. | **ambiguous** under both readings (C-44). |
| `developers`, `return_on_capital`, short to medium / long | Building relief. | Rents fall as stock grows. | CR-12e response argument with A-16 (CR-12g: horizons separate). | **increase** (C-30) / **no_change** (C-31). |
| Owners of existing buildings, `asset_value` (buildings), short | Building relief while the stock is fixed. | Expected fall in rents as the stock grows. | Response argument (CR-12, 1.1, an expansion): with cost per m² not falling as building expands (A-23), rents fall by no more than the tax removed. | **increase** (C-32). |
| `tenants` (users of land), `price_paid` (ground rents), short to medium | Building relief entering bids for sites (A-21). | None: the land tax's own chain gives no change. | CR-12a. | **increase** (C-29); long run not signed. |
| Garage owners, `asset_value`, short | Higher receipts (U1-a); possibly a lower tax share. | Expected entry of untaxed new garages and buildings. | None. | **ambiguous** (C-53). |

**The levy total.** The measure is revenue-neutral by construction: K4 and Charter §8 set the levy; the rate adjusts to the base. CR-12f applies (the land item and the building item cancel by construction), so no consequence is reported for the total levied. Two things around it are not "by construction": collections and the rate itself. Arrears on land-heavy parcels are one member of a group (C-22) and so cannot be used as a signed chain on collections (CR-12, 1.1: group members are not chains); no third item of revenue is signed, and no total is recorded. The rate rises above the static path as land values fall (C-35, C-36). The ontology has no variable for a tax rate (Gaps found, d1).

The transfers are recorded on both sides: bill-rising classes pay more (C-6 to C-10, C-45, C-47) and bill-falling classes pay less (C-3 to C-5, C-46); the city's two revenue items (C-1, C-2); the Assessor's added cost and its payers (C-48, C-49).

**Final check** (`03_workflow.md`).
1. Uncombined chains: lots' tax share (C-9, C-10) is signed per reading and window; building on lots (C-11) combines the relief with §4(b); land values (C-34, C-35), parcel values (C-36 to C-38), existing buildings (C-32, with A-23), ground rents (C-29), garages (C-52, C-53) and parking (C-14, C-43) combine their chains; rents are split by horizon (C-26, C-27, CR-12g); the response argument is applied to an expansion as CR-12's 1.1 note states it.
2. Group signs: sales or arrears by owners short of means (C-22), labor hired in construction (C-41; CR-6, 1.1), the Assessor's payers (C-49) and the Board (C-50) are groups. No group member is used as a chain elsewhere (CR-12, 1.1): arrears are not used to sign collections.
3. Baseline: every sign is against Vellmoor keeping its property tax with the same levy; the lots' shares are against 1.55%, not against each other's readings.
4. Worse off is not poorer: `resources_available_other_uses` is signed for classes that keep paying a sum they cannot avoid while they hold the parcel (C-45, C-47), and for those whose bills fall (C-46).
5. Timing shifts: completions around 1 January are signed per window in every year from 2028 (C-15, C-16); permits from the announcement are signed in their window (C-51); reclassification works before the first assessment date are a path note, since they would not happen without the measure.
6. Both sides of every transfer: above.
7. Every actor class, every core rule: CR-7c for land, buildings, lots, garages (C-53) and Ostbridge land; CR-9 to other buyers of the trades (C-54, C-55) and to garage owners (C-52); enforcement costs and the payer's side (C-48, C-49, C-50); CR-6 for rents, parking and the Board (C-50: a fixed quantity of hearings at a zero price).
8. Unstated premises: the levy (A-1), the class positions (A-2), the arithmetic premises (A-4, A-5, A-17), the response argument's premises (A-15, A-16, A-23).
9. Baseline of every pattern: TX-2 is used through its 1.1 clause on a fixed factor, and its main quantity conclusion is not used (Gaps found, c1); DM-1 is no longer cited (its If clause is not met); TX-3 and RS-6 are used through their 1.1 mirror clauses, and TS-1 in the other direction, against the counterfactual tax on buildings; TX-1's 1.1 clause on rate rises is met by arithmetic under the levy (C-2); RS-4, RS-5, RS-8, RS-9, RS-13, RS-16 and SB-4 are signed against no measure (SB-4's 1.1 clause: the measure does not tax buyers' alternatives to land, so land's value moves with its own return); RS-7 is re-signed against the counterfactual contest (C-24; CR-4, 1.1: the same question); OC-3's right baseline is used (C-48); TS-10 is used through its 1.1 clause on taxes, for capitalization of the whole schedule only (no bunching before a step is claimed); OC-5 is used per location. The re-based and corrected patterns of 1.1 not listed here (RS-17, RS-23, PC-17, EN-13, PC-1, PC-16, PC-20, TX-7, TX-9, EN-14, SB-8, RS-24) are not cited.

## 8. Time structure

- **10 June to 3 November 2026: rising probability.** Land values begin to fall and values of existing buildings to rise as passage becomes likely (CR-7c, probability clause); the rest moves on 3 November (C-32, C-34 to C-38, C-40). Holders over those months share the loss or gain.
- **November 2026 to December 2027: before the first assessment date.** No bill changes. Developers apply for permits and begin projects whose stream from 2031 now pays (C-51, C-11, C-12); the trades' wage and the price of other construction rise first (C-42, C-54, C-55). Owners of vacant sites put up low-cost buildings or, under U1-b, pave and open parking before 1 January 2028, when the first land assessment is made (C-13). These works would not happen without the measure, so their bunching before the date is a path note, not a timing consequence (02_ontology.md, 2.5); the works themselves are C-13. The Assessor spends $14 million on the valuation system (C-48).
- **2028 to 2030: the steps (TS-10).** Each 1 January the share of buildings in the taxable base falls by a quarter and the rate rises. Land values capitalized the whole schedule when it became expected (CR-7c; TS-10, 1.1: taxes), so the steps move bills, not values. Bills rise each year for land-heavy classes and fall for building-heavy ones (C-3 to C-8); under U1-b the lots' share falls at first and rises from 2031 (C-9, C-10). Completions are delayed past 1 January less than without the measure (C-15, C-16). Construction is higher than without the measure in every window, and the incentive grows with each step, so more of the added building falls in the later windows: a path note (CR-12h), since no window falls below the counterfactual (a year's delay saves at most 1.32% of a building's value against about 6% of net rent forgone). Triple-net tenants bear the change until their leases end (C-18, C-19), then owners do (C-20, C-21). Appeals peak in 2028 (C-25, C-50).
- **2031 on.** Land is taxed at the full land rate; buildings not at all. Completions are still moved from early January into December against the counterfactual, every year (C-15, C-16). The stock of floor space grows at the speed of planning and construction (TS-1, in the other direction), so rents fall slowly (C-27, C-28) and the gain on existing buildings erodes (C-33). Parking downtown thins under U1-a (C-14, C-43).
- **What does not erode.** The fall in land values persists as long as the measure does, because the stock of land cannot grow (CR-7, 1.0, which stock).

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-45 | `owners.lowrise`, `owners.vacant`, `owners.homes.high_land_share` | `resources_available_other_uses` (money) | decrease | What the higher bill would otherwise have bought or saved. Paid as long as they hold the parcel, whatever its use (CR-3, note: a sum they cannot avoid). | TX-1, OC-1, CR-3, CR-8b |
| C-46 | `owners.offices`, `owners.apartments`, `owners.homes.low_land_share` | `resources_available_other_uses` (money) | increase | Means freed by lower bills; the other side of C-45 (CR-8b). | TX-1, CR-8b |
| C-47 | `owners.lots` | `resources_available_other_uses` (money; 2028 to 2030 / 2031 on) | U1-a: decrease; U1-b: increase | 2028 to 2030; from 2031 decrease under both readings (C-10). | TX-1, OC-1, CR-3, CR-8b |
| C-48 | `officials.enforcement` (Assessor) | `enforcement_cost` | increase | About $9 million a year more than biennial whole-parcel valuation (the right baseline, about $21 million), and $14 million once. | OC-3, CR-8c |
| C-49 | `taxpayers`, recipients of other city spending | `resources_available_other_uses` | at_least_one_decrease | The Assessor's added cost comes from the general fund within an unchanged levy: other services, reserves, or other city taxes and fees. | OC-3, OC-1 (Who pays), CR-8 (0.7: payers from the general budget) |
| C-50 | `officials.adjudication`, `appellants` | `wait_time` (decisions on appeals) (+), `enforcement_cost` (time per appeal) (−) | at_least_one_as_stated | The Board's budget is unchanged and its caseload rises by half or more. | OC-3 (0.9: fixed budget), CR-6 (public supply: a fixed quantity of hearings), CR-8a |

**Who pays and who receives (C-45 to C-47).** The levy is the same, so every dollar a bill-rising class pays more is a dollar a bill-falling class pays less (CR-8b). The payers are worse off by their own ranking (CR-3a) and, because the tax is due while they hold the parcel whatever they do with it, they have less to spend on other things (CR-3, note). Each class's two changes in means (more land tax, less building tax) are netted first, by the arithmetic on the roll, and only the net is signed (CR-4, 1.1: several changes in means). Under U1-b the lots' owners pay less until 2031 and more after.

**OC-3 (C-48 to C-50).** The Assessor's added work is a cost of the measure; the right baseline is the valuation the Assessor does without it (OC-3), not zero, so only the difference is counted. It is funded from the general fund within a levy that K4 holds fixed, so its payers are a group (C-49; OC-3, general budget). The Board's budget is unchanged: its added hearings come from some other use of its time, as a group (C-50; OC-3, 0.9). Its hearings are a fixed quantity at a zero price, so CR-6's public-supply clause applies and gives the margins as a group.

**Prevented exchanges.** K1 prevents no exchange: land is let and sold as before. K2 adds exchanges (construction, leases of new space), and §4(b) prevents a few that would happen under §4(a) alone (the development the uplift tax deters under U1-b, A-4); the latter is not signed against the counterfactual, where the building tax deterred more.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | The council sets the same levy each year as it would have under the property tax. | revenue_use | 0.8 | K4; the budget process is unchanged; levy growth about 3% a year. | Class signs still follow the arithmetic of shares; C-1, C-2 and the bills' sizes change; a lower levy would make C-1 larger and C-2 smaller. |
| A-2 | Changes in assessed values over the phase-in do not reverse a class's position against the city-wide land share (classes far from 40%; homes split at 40% on the 2026 roll). | other | 0.75 | Class land shares of 26% to 62% against 40%; capitalization of the land tax is proportional to land value. | The affected class's tax share and parcel value become `ambiguous`; homes near the line move first. |
| A-3 | Some projects that do not pay without the measure pay once the building tax is removed (some owners and developers are at the margin). | alternative_uses | 0.85 | Downtown lots zoned for 12 storeys and unbuilt; building tax of about 4.5% of site value a year on a typical project. | C-11, C-12, C-14, C-17, C-27, C-28, C-30, C-41 to C-44, C-51, C-52, C-54, C-55 are not reported. |
| A-4 | Under U1-b, for downtown lots the land tax on the uplift from current use to site value (about 1.9% of site value a year from 2031) is below the building tax a project would pay without the measure (about 4.5%). | other | 0.8 | Assessor's ratio of about 3 for downtown; current-use value about half site value. | C-11 under U1-b becomes `ambiguous`. |
| A-5 | For typical redevelopment of improved parcels, the tax on the rise in current-use value under §4(b) is below the building tax without the measure. | other | 0.7 | Building values of new projects against the rise in land value; assessor's estimates. | C-12 is reported for new building on vacant sites only. |
| A-6 | Under §4(b), some owners of vacant sites (and of lots under U1-a) can lower their land value by putting up a low-cost building, at a cost below the tax saved. | other | 0.55 | Current-use values of one-storey uses on downtown-fringe sites; construction costs. | C-13 under U1-a is not reported. |
| A-7 | Under U1-b, some owners of vacant parcels can pave them and run parking at a cost below the tax saved. | other | 0.7 | Paving about 3% of site value once; saving about 0.9% to 1.9% of site value a year. | C-13 under U1-b rests on A-6; C-14 and C-43 under U1-b become `decrease` and `increase`, and C-52 under U1-b `increase`. |
| A-8 | Completion dates of some buildings can be moved by a few weeks around 1 January. | other | 0.7 | Completion certificates cluster in early January now. | C-15 and C-16 are not reported. |
| A-9 | Some owners whose bills rise cannot pay from income and have no deferral; they sell sooner or fall behind. | other | 0.6 | Retired owners on large lots; marginal low-rise businesses; no deferral in Measure L. | C-22 is not reported. |
| A-10 | Lot owners, low-rise owners, homeowner groups and developers can organize at a cost below their stakes. | other | 0.85 | Campaign committees on both sides of Measure L. | C-24 is not reported. |
| A-11 | Some owners appeal land valuations. | other | 0.85 | Assessor's forecast of 9,000 to 12,000 appeals in 2028 against about 6,000 now. | C-25 and C-50 are not reported. |
| A-12 | Some projects could be sited in Vellmoor or Ostbridge; Ostbridge keeps its tax on buildings. | mobility | 0.7 | Ostbridge permits 900 dwellings a year; shared regional builders. | C-17 and C-40 are not reported. |
| A-13 | Many commercial leases pass the property tax through to the tenant (about 70% downtown). | other | 0.8 | Lease survey. | C-18 and C-19 are not reported; C-20 and C-21 start in 2028. |
| A-14 | The stock of floor space cannot change materially within a year or two, and the measure does not change tenants' demand in that time. | durability | 0.8 | Planning and construction take two to four years. | C-26 becomes a decrease where space is added quickly; C-30, C-32, C-39 shrink; C-29 holds for a shorter time. |
| A-15 | The stock of floor space grows in response to the higher yield on new building, and demand for space in Vellmoor is not perfectly elastic. | other | 0.7 | Permits, vacancy rates, rents against Ostbridge. | C-27, C-28, C-31, C-33 are not reported; C-37 loses its (−) chain and becomes `increase`; C-53 keeps its (−) chain through new garages only. |
| A-16 | In the long run new floor space can be added at roughly constant cost per m² (trades and materials drawn from the wider region). | other | 0.6 | Regional construction market; C-42 is a short-run effect. | C-31 and C-33 are not reported (rising cost: builders' returns and existing values stay above the counterfactual). C-27 still holds on A-15. |
| A-17 | For industrial and outlying commercial sites and outlying vacant land, the permitted building is worth less than about 1.5 times the site, so the building tax removed on it is less than the extra land tax. | other | 0.8 | Assessor's ratio of about 0.6 for these sites. | C-35 and C-36 become `ambiguous` for the affected sites. |
| A-18 | Construction trades in the region cannot expand at once. | durability | 0.75 | Unemployment in the trades about 3%. | C-42, C-54 and C-55 are not reported; the added demand shows in employment and hours only (C-41). |
| A-19 | Some drivers who park on downtown lots shop less downtown when parking is scarcer or dearer; new occupants of buildings on former lots shop nearby. | other | 0.65 | Shopper surveys; mix of downtown shops. | C-44 has one chain; its sign follows that chain. |
| A-20 | Buyers of property expect the measure to last. | expectations | 0.8 | Charter amendment; no expiry. | C-32, C-34 to C-38, C-40 and C-53 shrink; C-51 is not reported. |
| A-21 | Buyers' and developers' bids for sites reflect part of the building tax they save on what they would build (downtown buildings; larger houses on large residential lots). | other | 0.7 | Residual land valuation practice; sales of large lots for rebuilding. | C-34 and C-38 become `decrease`; homes on large lots move from C-37 to C-36; C-29 becomes `no_change`. |
| A-22 | Downtown garages cannot be added or extended within a few years. | durability | 0.75 | Garage occupancy; planning times. | C-43 and C-52 under U1-a shrink; the shift goes to garage quantity. |
| A-23 | The cost per m² of building in Vellmoor does not fall as building expands (constant or rising cost). | other | 0.8 | Trades at about 3% unemployment; land and permits limited by zoning; no sign of economies of scale in the regional construction market. A weaker premise than A-16. | C-32 becomes `ambiguous` (with falling cost, long-run rents could fall by more than the tax removed). |

## 11. Report

**The policy.** From 2028 Vellmoor taxes buildings less each year and from 2031 not at all, and raises the same levy from land alone, assessed every year. Vacant land is valued as a development site; improved parcels at their value in current use less their buildings. It is unclear whether surface parking lots count as vacant or improved.

**Visible consequences.** The city collects less from buildings and more from land (C-1, C-2), with the same total. Owners of offices, apartments and homes on small lots pay a smaller share (C-3 to C-5); owners of low-rise commercial and industrial property, vacant land and homes on large lots pay a larger one (C-6 to C-8). Lot owners pay more from 2028 if lots count as vacant, and from 2031 either way (C-9, C-10).

**Invisible consequences.**
- *Building.* More is built on downtown lots under either reading (C-11) and elsewhere in Vellmoor (C-12), and less in Ostbridge (C-17); the stock of floor space grows (C-28), trades' wages rise (C-42), and builders' returns rise while the stock adjusts, then return to what capital earns elsewhere (C-30, C-31). Fewer completions are delayed past 1 January, in every year from 2028 (C-15, C-16). Permit applications rise from the announcement (C-51). Other construction costs more, and outside Vellmoor less of it is done (C-54, C-55); construction work in Vellmoor rises in jobs or hours (C-41).
- *Rents.* Rents for space do not change at first (C-26); they fall in the long run as the stock grows (C-27). The land tax is not passed to tenants; ground rents on new ground leases rise for some years, since lessees who build no longer pay the building tax (C-29). Tenants on triple-net leases bear the change until their leases end (C-18, C-19); then owners of land-heavy parcels receive less, and office owners more (C-20, C-21).
- *Values.* Land with little building potential loses value (C-35); downtown land may gain or lose (C-34). Low-rise and vacant parcels lose value (C-36); for parcels whose bills fall, and for homes on large lots, the value may go either way (C-37), though returns on the former rise for some years (C-39). Existing buildings gain at first, provided building costs do not fall as building expands, and lose the gain as the stock grows (C-32, C-33). Outlying vacant land is among the land that loses value; downtown vacant land may gain or lose. Lot values may rise or fall under both readings (C-38). Ostbridge land loses value (C-40). These values moved between June and November 2026.
- *Owners.* Owners whose bills rise have less to spend (C-45); those whose bills fall have more (C-46). Some cash-poor owners sell sooner or fall behind on their taxes, one or the other (C-22). Owners spend more on appeals (C-25). Assessment by current use leads owners of vacant sites to put up low-cost buildings or, if lots count as improved, to pave (C-13).
- *Parking and shops.* If lots count as vacant, surface parking downtown thins and costs more (C-14, C-43); if improved, either may go either way. Garage owners receive more if lots count as vacant (C-52); garage values may go either way (C-53). Sales at shops near the lots may rise or fall under both readings (C-44).
- *The city.* Valuing land separately costs the Assessor more (C-48), paid from other city spending, reserves or other taxes (C-49); appeals wait longer at the Board (C-50). Lobbying on the reading of U1, §4(b) and relief rises (C-24).

**Per reading of U1.** If lots count as vacant (U1-a), their owners pay more from 2028 (C-9), surface spaces fall and parking costs more (C-14, C-43). If lots count as improved (U1-b), their owners pay less until 2030 and more from 2031 (C-9, C-10), and vacant parcels are paved for parking, so spaces and parking prices may go either way.

**Ambiguous effects.** Downtown land values and lot values (C-34, C-38): whether sites keep the relief on what can be built on them or tenants receive it in lower rents. Values of building-heavy parcels (C-37): lower bills against lower future rents. Garage values (C-53): higher receipts against untaxed new garages. Parking spaces and prices under U1-b (C-14, C-43). Sales near the lots (C-44).

**Key conditions.** That the levy is unchanged (A-1); that building responds to the relief (A-3, p = 0.85); that the stock of space grows and rents respond (A-15, p = 0.7); that building costs are roughly constant in the long run (A-16, p = 0.6), on which only the long-run return of values and builders' returns to the counterfactual rests; and that they do not fall as building expands (A-23, p = 0.8), on which the gain to existing buildings rests.

**What this analysis cannot say.** How large any effect is; how much of the building relief ends with tenants rather than landowners; whether the city as a whole is better off; traffic, environmental and health effects (out of scope for version 1); whether the measure is desirable.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | officials.enforcement | tax_revenue (item: buildings) | decrease | short–long | visible | B | CR-1, CR-12 (0.8, 1.1) | A-1 |
| C-2 | officials.enforcement | tax_revenue (item: land) | increase | short–long | visible | B | CR-1, CR-12 (0.8, 1.1), TX-1 (1.1) | A-1 |
| C-3 | owners.offices | tax_share_borne | decrease | short–long | visible | B | CR-8b, CR-12e | A-1, A-2 |
| C-4 | owners.apartments | tax_share_borne | decrease | short–long | visible | B | CR-8b, CR-12e | A-1, A-2 |
| C-5 | owners.homes.low_land_share | tax_share_borne | decrease | short–long | visible | B | CR-8b, CR-12e | A-1, A-2 |
| C-6 | owners.homes.high_land_share | tax_share_borne | increase | short–long | visible | B | CR-8b, CR-12e | A-1, A-2 |
| C-7 | owners.lowrise | tax_share_borne | increase | short–long | visible | B | CR-8b, CR-12e | A-1, A-2 |
| C-8 | owners.vacant | tax_share_borne | increase | short–long | visible | B | CR-8b, CR-12e | A-1, A-2 |
| C-9 | owners.lots | tax_share_borne (2028–2030) | U1-a: increase; U1-b: decrease | short–medium | visible | B | CR-8b, CR-12e | A-1, A-2 |
| C-10 | owners.lots | tax_share_borne (2031 on) | U1-a: increase; U1-b: increase | medium–long | visible | B | CR-8b, CR-12e | A-1, A-2 |
| C-11 | developers, owners.lots | investment_target (buildings on downtown lots) | U1-a: increase; U1-b: increase | medium | invisible | B | TX-3, RS-6, CR-4b, CR-12e | A-3, A-4 |
| C-12 | developers | investment_target (other sites in Vellmoor) | increase | medium–long | invisible | B | TX-3, RS-6, CR-4b, CR-12h, CR-12e | A-3, A-5 |
| C-13 | owners.vacant, owners.lots | reclassification (works to be assessed under §4(b)) | U1-a: increase; U1-b: increase | short–medium | invisible | B | RS-5, CR-4 | A-6, A-7 |
| C-14 | parking_operators | quantity_supplied (surface spaces downtown) | U1-a: decrease; U1-b: ambiguous | medium | invisible | B | RS-13, CR-4, CR-12b | A-3, A-4, A-7 |
| C-15 | developers | quantity_supplied (completions just before 1 January, 2028 on) | increase | short–long | invisible | B | RS-8, CR-10a, CR-4 | A-8 |
| C-16 | developers | quantity_supplied (completions just after 1 January, 2028 on) | decrease | short–long | invisible | B | RS-8, CR-10a, CR-4 | A-8 |
| C-17 | developers, owners.ostbridge | quantity_supplied (new buildings in Ostbridge) | decrease | medium–long | invisible | B | RS-4, CR-7a | A-3, A-12 |
| C-18 | tenants.commercial.nnn (low-rise parcels) | price_paid (occupancy cost, existing leases) | increase | short | invisible | B | CR-9, CR-6, CR-5c | A-1, A-2, A-13 |
| C-19 | tenants.commercial.nnn (offices) | price_paid (occupancy cost, existing leases) | decrease | short | invisible | B | CR-9, CR-6, CR-5c | A-1, A-2, A-13 |
| C-20 | owners.lowrise | net_price_received (net of tax, renewed leases) | decrease | short–medium | invisible | B | CR-7b, TX-2, CR-5c | A-1, A-13, A-14 |
| C-21 | owners.offices | net_price_received (net of tax, renewed leases) | increase | short–medium | invisible | B | CR-7b, CR-5c | A-1, A-13, A-14 |
| C-22 | owners.homes.high_land_share, owners.lowrise, owners.vacant | turnover (sales of parcels) (+), legal_breach (tax unpaid when due) (+) | at_least_one_increase | short–medium | invisible | B | CR-4, CR-3a | A-9 |
| C-24 | lobbying groups | lobbying_effort (questions only under the measure) | increase | short–medium | invisible | B | RS-7, CR-4 (1.0, 1.1), CR-12 | A-10 |
| C-25 | owners (all classes) | compliance_cost (appeals, appraisals) | increase | short–medium | invisible | B | OC-2, CR-8c | A-11 |
| C-26 | tenants | price_paid (rent per m² of space) | no_change | short | invisible | B | CR-6, CR-7b, TX-2, TS-1 | A-14 |
| C-27 | tenants | price_paid (rent per m² of space) | decrease | long | invisible | B | RS-13, CR-6, CR-12e, CR-12 | A-3, A-15 |
| C-28 | developers | capital_stock_target (floor space in Vellmoor) | increase | long | invisible | B | TS-1, RS-6, CR-10b | A-3, A-15 |
| C-29 | tenants (users of land) | price_paid (ground rents on new ground leases) | increase | short–medium | invisible | B | CR-7b, TX-2, CR-5c, CR-12a | A-14, A-21 |
| C-30 | developers | return_on_capital (new buildings) | increase | short–medium | invisible | B | CR-7a, CR-4b | A-3, A-14 |
| C-31 | developers | return_on_capital (new buildings) | no_change | long | invisible | B | CR-7a, CR-12e, CR-12 | A-15, A-16 |
| C-32 | owners of existing buildings | asset_value (item: existing buildings) | increase | short | invisible | B | CR-7b, CR-7c, CR-10c, SB-4, TS-10, CR-12 (1.1) | A-14, A-20, A-23 |
| C-33 | owners of existing buildings | asset_value (item: existing buildings, per m²) | no_change | long | invisible | B | CR-7, CR-12e, CR-12 | A-15, A-16 |
| C-34 | owners.lots, owners of downtown sites (incl. owners.vacant downtown), owners.homes | asset_value (item: land, high permitted building) | ambiguous | short | invisible | B | CR-7b, CR-7c, CR-10c, LW-9, LW-10, CR-12b | A-1, A-20, A-21 |
| C-35 | owners.vacant (outlying), owners.lowrise | asset_value (item: land, low permitted building) | decrease | short | invisible | B | CR-7b, CR-7c, CR-10c, SB-4, CR-12e, TS-10 | A-1, A-17, A-20 |
| C-36 | owners.lowrise, owners.vacant (outlying) | asset_value (parcels) | decrease | short | invisible | B | CR-7c, CR-10c, SB-4, CR-12e, TS-10 | A-1, A-2, A-17, A-20 |
| C-37 | owners.offices, owners.apartments, owners.homes (both) | asset_value (parcels) | ambiguous | short | invisible | B | CR-7c, CR-10c, CR-12b | A-1, A-2, A-15, A-20, A-21 |
| C-38 | owners.lots | asset_value (parcels) | U1-a: ambiguous; U1-b: ambiguous | short | invisible | B | CR-7c, CR-10c, CR-12b | A-1, A-4, A-20, A-21 |
| C-39 | owners.offices, owners.apartments, owners.homes.low_land_share | return_on_capital (net of tax, 2028–2030) | increase | short–medium | invisible | B | CR-7b, CR-12e | A-1, A-2, A-14 |
| C-40 | owners.ostbridge | asset_value (land in Ostbridge) | decrease | short–medium | invisible | B | CR-9, CR-7c, CR-6 | A-12, A-20 |
| C-41 | construction_workers | employment (in Vellmoor) (+), hours_worked (+) | at_least_one_increase | medium | invisible | B | CR-9, LW-10, CR-6 (1.1), OC-5 | A-3 |
| C-42 | construction_workers | wage_rate (regional trades) | increase | short–medium | invisible | B | CR-9, CR-6 | A-3, A-18 |
| C-43 | parking_users | price_paid (parking downtown) | U1-a: increase; U1-b: ambiguous | medium | invisible | B | RS-13, RS-16, CR-6, CR-12b | A-3, A-7, A-22 |
| C-44 | businesses.downtown | quantity_traded (sales near former lots) | U1-a: ambiguous; U1-b: ambiguous | medium | invisible | B | RS-9, CR-9, CR-12b | A-3, A-19 |
| C-45 | owners.lowrise, owners.vacant, owners.homes.high_land_share | resources_available_other_uses (money) | decrease | short–long | invisible | B | TX-1, OC-1, CR-3, CR-8b | A-1, A-2 |
| C-46 | owners.offices, owners.apartments, owners.homes.low_land_share | resources_available_other_uses (money) | increase | short–long | invisible | B | TX-1, CR-8b | A-1, A-2 |
| C-47 | owners.lots | resources_available_other_uses (money, 2028–2030) | U1-a: decrease; U1-b: increase | short–medium | invisible | B | TX-1, OC-1, CR-3, CR-8b | A-1, A-2 |
| C-48 | officials.enforcement (Assessor) | enforcement_cost | increase | short–long | invisible | A | OC-3, CR-8c | none |
| C-49 | taxpayers, recipients of other city spending | resources_available_other_uses | at_least_one_decrease | short–long | invisible | A | OC-3, OC-1, CR-8 | none |
| C-50 | officials.adjudication, appellants | wait_time (appeals) (+), enforcement_cost (time per appeal) (−) | at_least_one_as_stated | short–medium | invisible | B | OC-3, CR-6, CR-8a | A-11 |
| C-51 | developers, owners of developable sites | applications (building permits) | increase | short | visible | B | CR-10a, CR-4, CR-12h | A-3, A-20 |
| C-52 | sellers.substitutes (garage owners) | net_price_received (garage parking) | U1-a: increase; U1-b: ambiguous | medium | invisible | B | CR-9, CR-6, RS-16 | A-3, A-7, A-22 |
| C-53 | sellers.substitutes (garage owners) | asset_value (garages) | ambiguous | short | invisible | B | CR-7c, CR-10c, CR-12b | A-3, A-15, A-20, A-22 |
| C-54 | buyers.substitutes (other construction work) | price_paid (construction work) | increase | short | invisible | B | CR-9, CR-7a, CR-6 | A-3, A-18 |
| C-55 | buyers.substitutes (construction outside Vellmoor) | quantity_traded (construction work) | decrease | short | invisible | B | CR-4c, CR-8a, CR-9 | A-3, A-18 |

## Corrections after the core-only comparison

Made after the blind core-only re-run (`05_examples_core/WE-058_land_value_tax_shift_core.md`) and its comparison, and under catalog 1.1. Each comparison row with cause P or E against this version, each valid OP omission, and each correction in the Findings was checked against the core rules before it was applied.

**Changed.**
- C-22: sales and arrears by owners short of means are now one group (`turnover`, `legal_breach`, `at_least_one_increase`), with `owners.vacant` included; A-9 says only that owners do one or the other, so neither member is signed alone. RS-3 is no longer cited (arrears from a want of means are not evasion that pays).
- C-29: ground rents on new ground leases change from `no_change` ("from the land tax alone", one chain) to `increase`, short to medium, on A-21: the building relief enters bids for sites and no chain lowers ground rents while the stock adjusts (CR-12a). The long run is not signed.
- C-32: the rise in existing buildings' value now rests also on A-23 (new): cost per m² does not fall as building expands, which is the premise CR-12's 1.1 note gives the response argument in an expansion.
- C-35, C-36: `owners.vacant` restricted to outlying vacant land, which is all A-17 covers; downtown vacant land is added to C-34 (`ambiguous`).
- C-15, C-16: the completion windows are signed in every year from 2028 on (horizon short to long), not only during the phase-in, since the counterfactual building tax rewards a January completion every year.
- C-20, C-26: DM-1 replaced by TX-2's 1.1 clause on a fixed factor (DM-1's If clause is not met); the section 4 note on TX-2 rewritten accordingly.
- C-41: construction labor in Vellmoor is now a group of `employment` and `hours_worked`, `at_least_one_increase` (CR-6, 1.1: labor demand).
- C-1, C-2: cite CR-12's 1.1 note on items that cancel (no total recorded); C-2 cites TX-1's 1.1 clause on rate rises, met by arithmetic under a levy.
- C-3 to C-10: cite CR-12's 1.1 note on ratios; TS-10 removed from C-9 and C-10, whose signs rest on arithmetic; TS-10 kept, through its 1.1 clause on taxes, only for capitalization of the schedule (C-32, C-35, C-36).
- C-24: cites CR-4's 1.1 note on "the same question"; sign unchanged.
- C-45 to C-47: text notes that each class's two changes in means are netted before signing (CR-4, 1.1).
- Section 7 and the final check: collections are not signed, since arrears are a group member and not a chain (CR-12, 1.1); the response argument is applied to an expansion as the 1.1 note states it; item 9 re-checked against the 1.1 catalog.

**Added.**
- C-51: building permit applications rise from the announcement (CR-10a, CR-4; comparison, core C-14).
- C-52: garage owners' receipts, U1-a `increase`, U1-b `ambiguous` (CR-9, CR-6; core C-47).
- C-53: garage values, `ambiguous` under both readings (see rejections).
- C-54: the price of construction work to other buyers rises in the short run (CR-9, CR-7a; core C-31).
- C-55: construction work outside Vellmoor that the measure does not touch falls in the short run (CR-4c, CR-8a; the valid part of core C-32).
- A-23: cost per m² of building does not fall as building expands (p 0.8).

**Removed.**
- C-23 (arrears signed alone), merged into C-22.

**Comparison conclusions rejected or not applied.**
- Core C-9 (the total levy recorded as `no_change`): rejected; CR-12's 1.1 note on items that cancel now settles that no total is recorded where nothing else moves the variable, and arrears, a group member, cannot be a third item.
- Core C-48 (garage values `increase` under U1-a, with A-N1): rejected as an increase; K2 also untaxes new garages and buildings, whose expected entry opposes the gain at expectation as in C-37, so it is recorded as `ambiguous` (C-53) and A-N1 is not needed.
- Comparison on C-29 (ground rents `increase` at every horizon, the later fall in space rents being unable to reverse it): rejected for the long run; the response argument bounds yields on building, not ground rents, so only the short to medium run is signed.
- Core C-32 (other construction `decrease` including renovation in Vellmoor): applied only outside Vellmoor (C-55); inside, K2 favors renovation too, an opposing chain, as the comparison itself notes.
- Findings on TS-10 (its use a stretch): not applied as a removal; TS-10's 1.1 clause covers taxes, and it is kept for capitalization of the whole schedule, with no bunching before a step claimed.
- Core C-22, C-23 (lobbying "for repeal" and "to keep the measure"): not adopted; under CR-4's 1.0 and 1.1 notes the shift was contested on the counterfactual path and needs a premise the case lacks.
- J and A rows (core C-44, C-52; pattern C-30, C-32 and C-33 item split, C-39): unchanged; catalog 1.1 does not settle them.

## Gaps found

**(a) Calculus gaps (a step no core rule covers).** None. Every step was derived from CR-1 to CR-12. No chain in this case runs through a `shared_facility` or `proximity` relation that was followed (traffic effects of fewer lots were stopped as out of scope).

**(b) Unclear core rules.**
1. *CR-12f against CR-12's 0.8 note on two items.* The 0.8 note says that where a policy moves two items of one variable in opposite directions, record each item and "record the total separately, combined under (b)". CR-12f says that where chains cancel exactly by construction, the consequence is not reported. A revenue-neutral shift meets both: the land item and the building item (C-1, C-2) move oppositely, and the total is fixed by K4. I followed (f) and did not report the total; the two clauses should say which governs (perhaps: record the total as `no_change` when construction fixes it, so that a reader sees it was checked). A related question: (f) is about chains that cancel "by construction"; here the total levied is fixed by construction but the total collected is not (delinquency, C-23), and nothing in (f) says which total is meant. *1.1:* settled by CR-12's 1.1 note on items that cancel: no total is recorded where nothing else moves the variable; the arrears are now one member of a group (C-22, formerly C-23) and are not a chain.
2. *CR-12's 1.0 note on the response argument, in an expansion.* The note says the argument gives a price sign "only with a premise that cost per unit does not fall as the activity contracts". Here the response is an expansion of building. Read in mirror, the premise that matters is that cost per unit does not change as building expands (constant cost); but the sign of the rent change (C-27) does not need it at all, only that the stock grows and demand is not perfectly elastic (CR-6, 0.9). What constant cost settles is the size (the rent falls by about the tax removed) and the long-run `no_change` of builders' returns and existing buildings' values (C-31, C-33). The note could say that in an expansion the premise bounds the size and the end state, not the direction. *1.1:* CR-12's 1.1 note now states the mirror case; on the re-check, the sign of existing buildings' value at expectation (C-32) does need its weak form (cost does not fall, A-23).
3. *CR-7c and CR-7's 1.0 "which stock" for two kinds of capital on one parcel.* The clause is written for a permission and the capital it allowed. Here there is no permission: the two stocks are land (fixed) and buildings (expandable), owned together and taxed oppositely. Applied by analogy it gave the right split (C-32 to C-35), but the clause could say that it covers any two durable means whose values a policy moves through different stocks.
4. *CR-1 operation 3 or 4 for a tax on holding.* A tax on land value is avoided by no use of the land (operation 4 for a given owner), but it is avoided by not owning land (operation 3 on the option of holding). Which applies changes whether CR-4 or "a change in means alone" governs owners' responses. I recorded both (section 2); the 0.7 clarification on charges could mention taxes on holding an asset.

**(c) Missing or wrong patterns.**
1. *TX-2 applied to a tax on a fixed factor.* TX-2's If clause is a tax on a sale; K1 is a tax on holding land, whatever its use. Read as a tax on land's yield, TX-2 gives `quantity_traded` decrease on the premise that one side can reduce its quantity. That premise fails for land (fixed stock; no use escapes the tax), and the conclusion would be wrong: the land in use does not change on account of the tax, and the rent for land does not rise (C-29). I overrode TX-2's quantity conclusion and took incidence from CR-7b and DM-1. A pattern for a tax on the value of a fixed factor (fully capitalized, borne by owners when expected, no change in use or rent; CR-4 only through its exception) is missing; Henry George's classic case is not in the catalog. *1.1:* TX-2 now has a clause on a fixed factor, used here; DM-1 is no longer cited, since its If clause is not met. Assessment by current use (§4(b)), where the tax does fall on use, is still outside that clause.
2. *TS-10 for a tax schedule.* TS-10's If clause is a standard, cap or ban that tightens on a schedule. A tax rate that steps up (and another that steps down) on an announced schedule fits its three conclusions: values capitalize the whole schedule when expected (C-32 to C-36), activity shifts around each step (C-15, C-16), and construction rises more in later windows (a path note under CR-12h). Needed interpretation to apply it to a tax; it could name taxes and subsidies explicitly. *1.1:* TS-10 now names taxes.
3. *TX-3 and RS-6 in reverse.* Neither states its mirror case (a tax removed: investment in the activity rises over time). Applied in mirror they gave C-11, C-12 and C-28; TS-1's "in the other direction" clause supplied the lag. *1.1:* both now state the mirror case.
4. *TX-9 for capitalization.* As land values capitalize the tax, the base falls and the rate rises above the static 3.75%; this is a shortfall against a static projection in the sense of TX-9, but TX-9's If clause asks for a fall in the taxed quantity, and under a levy system revenue does not fall: the rate rises. Not used; see (d) 1.
5. *SB-4* worked as written for a tax ("a tax, cap or competing entry that lowers them").
6. No pattern other than TX-2 gave a sign I had to override.

**(d) Vocabulary.**
1. No variable for a tax rate. Under a levy system the rate, not the revenue, absorbs the change in the base; the rise of the land rate above its static path could not be recorded.
2. `tax_share_borne` is defined relative to "other subgroups in the same market"; here it was used for each class's share of a fixed levy against its share without the measure, which is the natural reading for a revenue-neutral shift but not what the definition says.
3. No variable for a parcel's assessed value or assessment basis; the readings of U1 had to be described in text.
4. No actor class for owners of a parcel as distinct from owners of the land and of the building on it; the two items of `asset_value` (C-32 to C-35) had to be qualified by hand.

**(e) Test of 1.0.**
- *CR-7c (capitalization of a tax on a fixed factor).* Worked as written: land values fall when the measure becomes expected, from June 2026 by probability, and later buyers pay the capitalized price (C-35, C-36, C-40; SB-4).
- *CR-7 1.0, which stock.* Needed interpretation ((b) 3): written for a permission and its capital, applied to land against buildings. With that reading it gave the case's main split: the land tax persists on a stock that cannot grow; the building relief erodes as the building stock grows (C-32, C-33, C-35).
- *CR-12 1.0, what the response argument needs.* Needed interpretation ((b) 2). The three requirements were usable: the total bounded (all floor space of a given quality), the constant-cost premise (A-16), and second responses (inflow of tenants, a response to the fall itself). But in an expansion the constant-cost premise bounds the size and end state (C-31, C-33), not the sign of rents (C-27), which rests on A-15.
- *CR-12 0.8, two items in one variable, with CR-12f.* Needed interpretation ((b) 1): the two items were recorded (C-1, C-2); the total was not, by (f), which conflicts with the 0.8 note's "record the total separately".
- *TX-2 and TX-3 incidence (with DM-1).* TX-2 failed on a tax on a fixed factor ((c) 1): its quantity conclusion is wrong for land; incidence came from CR-7b and DM-1, which worked as written (owners of land bear it, C-20, C-29). TX-3 worked in reverse for buildings ((c) 3).
- *RS-8 (timing over the phase-in).* Worked as written for completions around each 1 January (C-15, C-16), signed per window; the claim that the steps would make builders wait for a lower step failed on arithmetic (a year's delay saves at most 1.32% against about 6% of rent), so no shift between years was signed. Reclassification before the first assessment date is a path note, not a consequence, under 02_ontology.md 2.5, since it would not happen without the measure.
- *TS-10 (scheduled steps).* Needed interpretation ((c) 2): written for standards, caps and bans; applied to a tax schedule, its three conclusions held.
- *CR-12h.* Worked as written: construction is higher in every window, with more in later windows as a path note (section 8).
- *RS-9 0.9, location complements.* Worked as written: shops near lots lose drivers' purchases and gain new occupants' (C-44), `ambiguous` under both readings; under U1-b the parking chain is itself ambiguous (kind 3).
- *OC-3 (assessment costs; general budget; 0.9 fixed budget; right baseline).* Worked as written: the Assessor's added cost against its baseline valuation work (C-48), its payers as a group (C-49), and the Board's fixed budget as a group (C-50).
- *RS-4 (favored inside).* Worked as written: building moves from Ostbridge (C-17).
- *CR-6 1.0, small effects are signed.* Worked as written for Ostbridge land (C-40).
- *RS-7 1.0 and CR-4 1.0, lobbying against a contested counterfactual.* Worked as written: the shift was contested on the counterfactual path (a ballot campaign), so lobbying on the shift as such is not signed; questions that exist only under the measure are (C-24).
- *CR-12 1.0, the baseline of patterns.* Applied to every pattern cited (final check, item 9). The one pattern whose conclusion failed against the counterfactual was TX-2, for a reason of preconditions rather than baseline.
- *CR-3 note (worse off is not poorer).* Worked as written: a tax on holding is a sum that cannot be avoided while the parcel is held (C-45, C-47).
- *Candidates from 06_gaps.md, 6.2e.* None needed. The case suggests a new one: a tax on the value of a fixed factor ((c) 1).

Re-run note: the comparison contradicts two verdicts above: TX-2 did not fail but did not apply (its If and Assumes clauses are unmet; 1.1 adds a fixed-factor clause), and DM-1 did not work as written (its If clause requires TX-2 or SB-2; incidence rests on CR-7b).
