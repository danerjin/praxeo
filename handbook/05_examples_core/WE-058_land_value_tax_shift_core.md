# WE-058 / Analysis: Revenue-neutral shift from a property tax to a land value tax, phased in over four years

Analyst: core-only re-run (Handbook 1.0)  |  Rules: core rules CR-1 to CR-12 only  |  Status: compared

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

The counterfactual law: Charter §8 levy, assessed on land and buildings together at a single rate (1.5% in 2027), with zoning and Ostbridge's tax unchanged.

| Component | Rothbard type | Binding? (assumption ID) | CR-1 operations | Core rules applied |
| --- | --- | --- | --- | --- |
| K1 Land tax | binary (state takes) | Yes: every owner of taxable land pays (A-1 fixes the levy) | 4 (a sum on each parcel that no choice of use avoids under §4(a)); 3 under §4(b), where the land value depends on current use | CR-3, CR-4 exception, CR-7c, CR-8b, CR-10c |
| K2 Building phase-out | binary (state takes less) | Yes: removes a charge on improvements in steps (2028 to 2031) | 3 (removes, in dated steps, a charge attached to the option 'build' or 'improve'; CR-1 0.7 dated operations) | CR-4, CR-6, CR-7a, CR-9, CR-10a, CR-10b |
| K3 Assessment of land | condition of K1 | Yes; U1 decides which method governs surface lots | 3 per reading: U1-a lots and vacant parcels at site value; U1-b lots at current-use value less paving. §4(b) makes the land tax on improved parcels depend on use, so building and paving change what the parcel pays (A-5, A-6, A-7) | CR-1 (per reading), CR-4 |
| K4 Revenue neutrality | rule on the levy | Yes (A-1) | none by itself; it fixes the sum K1 and K2 divide, so every change in one class's bill is a change in another's | CR-8b |
| K5 Administration | binary (budget used up) | Yes | 4 (about $14 million once and $9 million a year to the Assessor, from the general fund); 3 (yearly valuation and appeals attached to owning land) | CR-6 (0.7), CR-8c |

K1 with K2 is, for owners, a change in what share of a fixed sum they pay; for builders it is the removal of a charge on building. The direction of each class's share is arithmetic on the record's table, given A-1 and A-2.

## 3. Actor classes

| Actor class | Role | How its options change (CR-1) |
| --- | --- | --- |
| owners.surface_lots | 140 downtown lots, 97% land | Op 4: share of the levy changes per reading (U1-a up at once; U1-b down to 2030, up from 2031). Op 3: building no longer taxed. |
| owners.vacant_land | 2,300 parcels, all land | Op 4: share up. Op 3: building untaxed; under §4(b) a low-cost building (A-6) or, under U1-b, paving (A-7) lowers the land value. |
| owners.low_rise_commercial_industrial | Strip retail, dealers, warehouses; 62% land | Op 4: share up. Leased parcels: tenants pay during triple-net leases. |
| homeowners.high_land_share | About 38,000 homes on large lots | Op 4: share up. Some cannot pay from income (A-9). |
| homeowners.low_land_share | About 67,000 homes | Op 4: share down. |
| owners.apartments, owners.offices | Land shares 30% and 26% | Op 4: share down; op 3: improvements untaxed by 2031. |
| tenants (residential; commercial, including triple-net) | Rent space | Through CR-9 (lease contract) during existing leases; through CR-6 in the rental market. |
| sellers.prospective (developers) | Build on vacant, lot and improved sites | Op 3: no tax on what they build by 2031; under §4(b) a tax on the rise in current-use value. |
| input_suppliers.construction_trades | Labor for building | Through CR-9 (input_to). |
| buyers.substitutes (other construction buyers) | Renovation and Ostbridge projects | Through CR-9: compete for the same trades. |
| buyers.substitutes (drivers parking downtown), sellers.substitutes (garage owners) | Parking market | Through CR-9 (substitute) as lots are built on. |
| sellers.complements (downtown shops) | Trip complement of parking | Through CR-9. |
| neighboring_jurisdictions (Ostbridge developers, landowners, city) | Just outside the city line; keeps its tax on buildings | Through CR-9 (across_border). |
| officials.assessor, Board of Equalization | Valuation and appeals | Op 4 (Assessor budget up); Board budget unchanged with more appeals. |
| taxpayers, recipients of other city spending | Fund the Assessor's added budget | Op 4 through the general fund (CR-8 0.7). |
| buyers.prospective (of property) | Buy after the measure is expected | Pay prices that capitalize it (CR-7c). |

## 4. Direct effect

CR-1 and CR-2: the change in each class's bill out of a fixed levy (A-1), signed against the property tax staying as it is. Shares are from the record's static table; A-2 holds their direction under revaluation.

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-1 | owners.surface_lots | tax_share_borne (share of the levy) | U1-a: increase; U1-b: decrease | short (2028 to 2030) | CR-1, CR-8b | A-1, A-2 |
| C-2 | owners.surface_lots | tax_share_borne (share of the levy) | increase | long (2031 on) | CR-1, CR-8b | A-1, A-2 |
| C-3 | owners.vacant_land | tax_share_borne (share of the levy) | increase | short; medium; long | CR-1, CR-8b | A-1, A-2 |
| C-4 | owners.low_rise_commercial_industrial | tax_share_borne (share of the levy) | increase | short; medium; long | CR-1, CR-8b | A-1, A-2 |
| C-5 | homeowners.high_land_share (about 38,000 homes, land share above 40%) | tax_share_borne (share of the levy) | increase | short; medium; long | CR-1, CR-8b | A-1, A-2 |
| C-6 | homeowners.low_land_share (about 67,000 homes) | tax_share_borne (share of the levy) | decrease | short; medium; long | CR-1, CR-8b | A-1, A-2 |
| C-7 | owners.apartments | tax_share_borne (share of the levy) | decrease | short; medium; long | CR-1, CR-8b | A-1, A-2 |
| C-8 | owners.offices | tax_share_borne (share of the levy) | decrease | short; medium; long | CR-1, CR-8b | A-1, A-2 |
| C-9 | officials.city_budget | tax_revenue (property levy collected) | no_change | short; medium; long | CR-1, CR-8b | A-1 |
| C-10 | owners.vacant_land, owners.low_rise_commercial_industrial (owner-occupiers, and lessors once triple-net leases end), homeowners.high_land_share | resources_available_other_uses | decrease | short; medium; long | CR-3, CR-7c, CR-8b, CR-3c | A-1, A-2 |
| C-11 | owners.apartments, owners.offices (owner-occupiers, and lessors once triple-net leases end), homeowners.low_land_share | resources_available_other_uses | increase | short; medium; long | CR-8b, CR-1 | A-1, A-2 |
| C-12 | owners.surface_lots | resources_available_other_uses | U1-a: decrease; U1-b: increase | short (2028 to 2030) | CR-3, CR-8b | A-1, A-2 |
| C-13 | owners.surface_lots | resources_available_other_uses | decrease | long (2031 on) | CR-3, CR-8b | A-1, A-2 |

## 5. Responses

CR-4 applied to every pair of options of every class: build or hold (C-14 to C-16), the assessed form of a parcel (C-17 to C-19), the date of completion (C-20, C-21), lobbying (C-22, C-23), appealing (C-24 to C-26), paying or selling (C-29). Relocation by owners is not a response to K1: the land tax is capitalized into the parcel's price (CR-7c), so selling and moving does not avoid it. Evasion: delinquency is covered by C-29; no other evasion margin is open, since land cannot be hidden.

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-14 | sellers.prospective (developers and owners of developable sites) | applications (dwelling and commercial building permits) | increase | short (from June 2026) | CR-10a, CR-4 | A-3, A-20 |
| C-15 | sellers.prospective (developers and owners of developable sites) | investment_target (new buildings in Vellmoor) | increase | medium; long | CR-1, CR-4, CR-7a, CR-6 | A-3, A-20 |
| C-16 | owners.vacant_land, owners.surface_lots | units_held_vacant (parcels held unbuilt: vacant land and surface lots) | decrease | medium; long | CR-4, CR-10b | A-3, A-20 |
| C-17 | owners.vacant_land | reclassification (low-cost buildings put up so that the parcel is assessed under §4(b)) | increase | short; medium | CR-4 | A-6 |
| C-18 | owners.surface_lots | reclassification (low-cost buildings put up so that the lot is assessed under §4(b)) | U1-a: increase; U1-b: no_change | short; medium | CR-4, CR-1 | A-6 |
| C-19 | owners.vacant_land | reclassification (parcels paved and run as parking) | U1-a: no_change; U1-b: increase | short | CR-4, CR-1 | A-7 |
| C-20 | sellers.prospective (developers) | quantity_supplied (building completions in the last weeks of December, 2027 to 2030) | increase | short; medium | CR-10a, CR-4, CR-12h | A-8 |
| C-21 | sellers.prospective (developers) | quantity_supplied (building completions in the first weeks of January, 2028 on) | decrease | short; medium; long | CR-10a, CR-4 | A-8 |
| C-22 | owners.surface_lots, owners.low_rise_commercial_industrial, homeowners.high_land_share | lobbying_effort (for repeal, deferral, a deferral programme, and the U1-b reading) | increase | short; medium | CR-4, CR-12, CR-8c | A-10 |
| C-23 | sellers.prospective (developers), owners.offices, owners.apartments | lobbying_effort (to keep the measure and for the U1-a reading) | increase | short; medium | CR-4, CR-8c | A-10 |
| C-24 | owners.all_classes (appellants) | applications (valuation appeals to the Board of Equalization) | increase | short | CR-4 | A-11 |
| C-25 | owners.all_classes (appellants) | compliance_cost (preparing and arguing appeals) | increase | short; medium | CR-8c | A-11 |
| C-26 | owners.all_classes (appellants) | wait_time (decision on an appeal) | increase | short; medium | CR-6 | A-11 |
| C-27 | officials.assessor | enforcement_cost | increase | short; medium; long | CR-1, CR-8c | - |
| C-28 | taxpayers, recipients of other city spending | resources_available_other_uses | at_least_one_decrease | short; medium; long | CR-8b, CR-8, CR-8a | A-1 |
| C-29 | homeowners.high_land_share, owners.low_rise_commercial_industrial | turnover (sales by owners whose bills rise), legal_breach (tax delinquency) | at_least_one_increase | short; medium | CR-4, CR-3 | A-9, A-1, A-2 |

## 6. Second-order effects

CR-9 along named relations, then CR-5 to CR-7 in each market reached. Depth limit 4. Effects on neighbors of new buildings through `proximity` (light, congestion) are Tier C and outside version-1 variables; not pursued.

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C-30 | input_suppliers.construction_trades | wage_rate | increase | short | CR-9, LW-10, CR-6 | construction labor input_to new buildings (close) | A-3, A-18 |
| C-31 | buyers.substitutes (renovation and construction outside the new projects, including Ostbridge) | price_paid (construction work) | increase | short | CR-9, CR-7a | same regional trades input_to other construction (close) | A-3, A-18 |
| C-32 | buyers.substitutes (renovation and construction outside the new projects, including Ostbridge) | quantity_traded (construction work) | decrease | short | CR-4c, CR-8a | as C-31 | A-3, A-18 |
| C-33 | input_suppliers.construction_trades | employment (construction in Vellmoor) | increase | medium; long | CR-9, LW-10, CR-7a | construction labor input_to new buildings (close) | A-3, A-16 |
| C-34 | tenants (residential, and commercial tenants not on triple-net leases) | price_paid (rent) | no_change | short | CR-6, CR-7b | - | A-14 |
| C-35 | tenants.commercial_triple_net (offices and other high-rise commercial) | price_paid (rent plus the tax passed through) | decrease | short (remaining term of existing leases) | CR-9, CR-1, CR-7b | triple-net lease (contract) | A-13, A-1, A-2 |
| C-36 | tenants.commercial_triple_net (low-rise commercial and industrial) | price_paid (rent plus the tax passed through) | increase | short (remaining term of existing leases) | CR-9, CR-1, CR-7b | triple-net lease (contract) | A-13, A-1, A-2 |
| C-37 | owners.all_classes | capital_stock_target (floor space in Vellmoor) | increase | medium; long | CR-10b | - | A-3, A-15 |
| C-38 | tenants (residential and commercial) | price_paid (rent) | decrease | medium; long | CR-6, CR-7a, CR-7b | new space same_market_other_segment of existing space (close) | A-3, A-15 |
| C-39 | owners.apartments, owners.offices, homeowners.low_land_share | asset_value (property) | ambiguous | short (from June 2026; fully from 3 November 2026) | CR-12b, CR-7c, CR-10c, CR-6 | - | A-2, A-20, A-15 |
| C-40 | homeowners.high_land_share | asset_value (property) | ambiguous | short (from June 2026) | CR-12b, CR-7c, CR-10c | - | A-2, A-20, A-15, A-21 |
| C-41 | owners.low_rise_commercial_industrial, owners.vacant_land (outlying) | asset_value (land and property) | decrease | short (from June 2026) | CR-7c, CR-10c, CR-12e | - | A-2, A-17, A-20 |
| C-42 | owners.surface_lots | asset_value (land) | ambiguous | short (from June 2026) | CR-12b, CR-7c | - | A-20, A-21 |
| C-43 | owners.all_classes | asset_value (taxable land, city-wide) | ambiguous | short (from June 2026) | CR-12b, CR-7c, CR-10c | - | A-20, A-21 |
| C-44 | buyers.prospective (of property after November 2026) | return_on_capital | no_change | long | CR-7c, CR-10c | - | A-20 |
| C-45 | owners.surface_lots (parking operators) | quantity_supplied (surface parking spaces downtown) | U1-a: decrease; U1-b: ambiguous | medium; long | CR-4, CR-10b, CR-12b | - | A-3, A-4, A-7 |
| C-46 | buyers.substitutes (drivers parking downtown) | price_paid (downtown parking) | U1-a: increase; U1-b: ambiguous | medium; long | CR-9, CR-6, CR-12 | surface lot spaces substitute for garage spaces (close) | A-3, A-22, A-7 |
| C-47 | sellers.substitutes (owners of downtown garages) | net_price_received (garage parking) | U1-a: increase; U1-b: ambiguous | medium; long | CR-9, CR-6 | surface lot spaces substitute for garage spaces (close) | A-3, A-22, A-7 |
| C-48 | sellers.substitutes (owners of downtown garages) | asset_value (garages) | U1-a: increase; U1-b: ambiguous | short (from June 2026) | CR-7c, CR-10c, CR-12 | as C-47 | A-3, A-20, A-22, A-N1, A-7 |
| C-49 | sellers.complements (downtown shops) | quantity_traded (downtown retail sales) | ambiguous | medium; long | CR-9, CR-12b | parking complement (trip) downtown shopping; new floor space input_to local custom | A-19, A-3 |
| C-50 | neighboring_jurisdictions (developers in Ostbridge) | investment_target (new buildings in Ostbridge) | decrease | medium; long | CR-9, CR-4, CR-7a | Ostbridge sites across_border substitute for Vellmoor sites (partial) | A-12, A-3 |
| C-51 | neighboring_jurisdictions (owners of development land in Ostbridge) | asset_value (land) | decrease | short (from June 2026) | CR-7c, CR-10c | as C-50 | A-12, A-20 |
| C-52 | officials.ostbridge | tax_revenue | decrease | medium; long | CR-9 | as C-50 | A-12, A-3, A-N2 |

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance premise | Combined sign |
| --- | --- | --- | --- | --- |
| owners.surface_lots, tax_share_borne, short | U1-a: assessed at site value under a rising land rate | U1-b: assessed at half that; share below 1.55% to 2030 | Per reading, not combined | U1-a: increase; U1-b: decrease (C-1) |
| owners.surface_lots, tax_share_borne, long | Both readings above 1.55% | - | - | increase (C-2) |
| tenants, price_paid (rent), short | triple-net low-rise (C-36) | triple-net offices (C-35) | Different classes, split | no_change for other tenants (C-34) |
| tenants, price_paid (rent), medium; long | - | more space (C-37, A-15) | - | decrease (C-38) |
| owners.apartments, offices, low-land-share homes, asset_value | lower tax share (A-2, A-20) | expected added space (A-15) | none | ambiguous (C-39) |
| homeowners.high_land_share, asset_value | rebuilding bids (A-21) | higher tax share; added housing | none | ambiguous (C-40) |
| low-rise and outlying vacant, asset_value | rebuilding bids (A-21) | higher tax share; added commercial space | A-17 (empirical, CR-12e): building tax removed below extra land tax | decrease (C-41) |
| owners.surface_lots, asset_value | A-21 bids; U1-b lower tax to 2030 | higher land tax (U1-a at once, U1-b from 2031) | none | ambiguous (C-42) |
| all land, asset_value | A-21 bids | capitalized land tax | none | ambiguous (C-43) |
| sellers.prospective, investment_target, medium; long | building tax removed (all parcels) | U1-b lots: 1.9% uplift tax; §4(b): tax on rise in use value | A-4 and A-5 (empirical): the opposing charge is below the building tax removed | increase (C-15) |
| parking spaces, medium; long | U1-b: paving vacant parcels (A-7) | lots built on | none under U1-b | U1-a: decrease; U1-b: ambiguous (C-45) |
| garages, asset_value | parking price (U1-a); own tax cut (A-N1) | U1-b: parking chain kind 3 | under U1-b the kind-3 chain is not covered | U1-a: increase; U1-b: ambiguous (C-48) |
| downtown shops, quantity_traded | new occupants shop nearby (A-19) | drivers deterred (A-19) | none | ambiguous (C-49) |
| completions, timing | late December (C-20) | early January (C-21) | different windows, not combined (CR-12g, h) | per window |
| construction labor, wage_rate | short: demand up, trades fixed (A-18) | - | long: not signed (A-16: constant cost) | increase (short) (C-30) |
| owners' resources_available_other_uses | classes whose share falls (C-11) | classes whose share rises (C-10) | different classes; CR-8b: they sum to zero with the levy fixed | per class |

CR-12f: K4 makes the sum of the classes' changes in bills zero by construction; the total is therefore not reported as a consequence, only each class's side.

## 8. Time structure

- **Horizons.** Short: from qualification (10 June 2026) to 2028, the first phase-in year. Medium: 2029 to 2031. Long: 2031 on, with no building tax.
- **Announcement.** Measure L became likely from June 2026 (polls 55% to 60%) and certain on 3 November 2026. Land and property values move part of the way from June and fully at passage (CR-7c, CR-10c; C-39 to C-43, C-48, C-51): the gains and losses fall on owners at those dates, not on later buyers (C-44). Permits are brought forward from 2026 (C-14), since buildings started then are finished when the building tax is lower.
- **Phase-in.** The share of each class moves in four steps; for lots under U1-b the direction of the share changes between 2030 and 2031 (C-1, C-2, C-12, C-13). The yearly fall in the tax on buildings shrinks the reward for holding completions past 1 January, so completions move from early January back into December in each window (C-20, C-21). A building's tax for a year depends on the year, not its completion date, so there is no reason to delay completion from one year to the next (CR-4: the net rent of about 6% exceeds every year's building tax).
- **Stocks.** Floor space changes through completions (CR-10b): unchanged for a year or two (A-14, C-34), larger in the medium and long run (C-37, C-38). The trades cannot expand at once (A-18), so the first years' extra demand goes to wages and prices (C-30, C-31) and investment rises mainly from 2029 (C-15).
- **Capitalization and the rate.** As land values fall with the higher land tax (C-43, the Assessor's 15%), the rate needed to raise the same levy rises (about 4.4% in 2031 rather than 3.75%); with K4 and A-1 this changes no class's share in direction (A-2) and no total (C-9).
- **Persistence.** The measure has no expiry and is a charter amendment (A-20). K2 is in part the removal of an existing tax on buildings; this is not a repeal of a whole policy, so the brief's metamorphic check does not apply. The one effect of the old building tax that the measure undoes only gradually is the stock of unbuilt and underbuilt sites (C-16): it falls only as projects are completed (CR-10b).

## 9. Opportunity costs

Each is written as a signed change in a variable.

| ID | Actor class | Variable | Sign | What is given up | Rules |
| --- | --- | --- | --- | --- | --- |
| C-10 | owners.vacant_land, owners.low_rise_commercial_industrial, homeowners.high_land_share | resources_available_other_uses | decrease | Purchases and saving forgone to pay the larger share of the levy | CR-3 note, CR-8b |
| C-17 | owners.vacant_land | reclassification (low-cost buildings) | increase | Building materials and labor spent on structures put up to lower an assessment rather than to serve users | CR-4, CR-8c |
| C-19 | owners.vacant_land | reclassification (paving) | U1-b: increase | About 3% of site value per parcel spent on paving to lower an assessment | CR-4, CR-8c |
| C-22 | lot, low-rise and hill owners | lobbying_effort | increase | Time and money spent seeking repeal, deferral or the U1-b reading | CR-4, CR-8c |
| C-23 | developers, office and apartment owners | lobbying_effort | increase | Time and money spent defending the measure | CR-4, CR-8c |
| C-25 | appellants | compliance_cost | increase | Time and fees spent on appeals | CR-8c |
| C-26 | appellants | wait_time | increase | Time waiting for decisions with the Board's budget unchanged | CR-6, CR-8c |
| C-27 | officials.assessor | enforcement_cost | increase | About $14 million once and $9 million a year of resources | CR-1, CR-8c |
| C-28 | taxpayers, recipients of other city spending | resources_available_other_uses | at_least_one_decrease | Other city spending, or other revenue, that funds the Assessor | CR-8 0.7 |
| C-32 | other construction buyers | quantity_traded | decrease | Renovations and Ostbridge projects not done while the trades are drawn to Vellmoor | CR-4c, CR-8a |
| C-50 | Ostbridge developers | investment_target | decrease | Buildings that would have gone up in Ostbridge | CR-4, CR-9 |

CR-8b: every class whose share falls (C-11) is matched by a class whose share rises (C-10, C-12, C-13); the triple-net pass-through moves part of each side to tenants during leases (C-35, C-36); the Assessor's budget (C-27) is matched by its payers (C-28).

## 10. Assumptions

Case assumptions as given (same IDs and p); two added premises (A-N1, A-N2) are flagged NEW.

| ID | Statement | Type | p | Evidence | If false |
| --- | --- | --- | --- | --- | --- |
| A-1 | The council sets the same levy each year as it would have under the property tax. | revenue_use | 0.8 | K4; the budget process is unchanged; levy growth about 3% a year. | These consequences fail or lose this chain: C-1, C-2, C-3, C-4, C-5, C-6, C-7, C-8, C-9, C-10, C-11, C-12, C-13, C-28, C-29, C-35, C-36. |
| A-2 | Changes in assessed values over the phase-in do not reverse a class's position against the city-wide land share (classes far from 40%; homes split at 40% on the 2026 roll). | other | 0.75 | Class land shares of 26% to 62% against 40%; capitalization of the land tax is proportional to land value. | These consequences fail or lose this chain: C-1, C-2, C-3, C-4, C-5, C-6, C-7, C-8, C-10, C-11, C-12, C-13, C-29, C-35, C-36, C-39, C-40, C-41. |
| A-3 | Some projects that do not pay without the measure pay once the building tax is removed (some owners and developers are at the margin). | alternative_uses | 0.85 | Downtown lots zoned for 12 storeys and unbuilt; building tax of about 4.5% of site value a year on a typical project. | These consequences fail or lose this chain: C-14, C-15, C-16, C-30, C-31, C-32, C-33, C-37, C-38, C-45, C-46, C-47, C-48, C-49, C-50, C-52. |
| A-4 | Under U1-b, for downtown lots the land tax on the uplift from current use to site value (about 1.9% of site value a year from 2031) is below the building tax a project would pay without the measure (about 4.5%). | other | 0.8 | Assessor's ratio of about 3 for downtown; current-use value about half site value. | These consequences fail or lose this chain: C-45. |
| A-5 | For typical redevelopment of improved parcels, the tax on the rise in current-use value under §4(b) is below the building tax without the measure. | other | 0.7 | Building values of new projects against the rise in land value; assessor's estimates. | No reported consequence rests on it alone. |
| A-6 | Under §4(b), some owners of vacant sites (and of lots under U1-a) can lower their land value by putting up a low-cost building, at a cost below the tax saved. | other | 0.55 | Current-use values of one-storey uses on downtown-fringe sites; construction costs. | These consequences fail or lose this chain: C-17, C-18. |
| A-7 | Under U1-b, some owners of vacant parcels can pave them and run parking at a cost below the tax saved. | other | 0.7 | Paving about 3% of site value once; saving about 0.9% to 1.9% of site value a year. | These consequences fail or lose this chain: C-19, C-45, C-46, C-47, C-48. |
| A-8 | Completion dates of some buildings can be moved by a few weeks around 1 January. | other | 0.7 | Completion certificates cluster in early January now. | These consequences fail or lose this chain: C-20, C-21. |
| A-9 | Some owners whose bills rise cannot pay from income and have no deferral; they sell sooner or fall behind. | other | 0.6 | Retired owners on large lots; marginal low-rise businesses; no deferral in Measure L. | These consequences fail or lose this chain: C-29. |
| A-10 | Lot owners, low-rise owners, homeowner groups and developers can organize at a cost below their stakes. | other | 0.85 | Campaign committees on both sides of Measure L. | These consequences fail or lose this chain: C-22, C-23. |
| A-11 | Some owners appeal land valuations. | other | 0.85 | Assessor's forecast of 9,000 to 12,000 appeals in 2028 against about 6,000 now. | These consequences fail or lose this chain: C-24, C-25, C-26. |
| A-12 | Some projects could be sited in Vellmoor or Ostbridge; Ostbridge keeps its tax on buildings. | mobility | 0.7 | Ostbridge permits 900 dwellings a year; shared regional builders. | These consequences fail or lose this chain: C-50, C-51, C-52. |
| A-13 | Many commercial leases pass the property tax through to the tenant (about 70% downtown). | other | 0.8 | Lease survey. | These consequences fail or lose this chain: C-35, C-36. |
| A-14 | The stock of floor space cannot change materially within a year or two, and the measure does not change tenants' demand in that time. | durability | 0.8 | Planning and construction take two to four years. | These consequences fail or lose this chain: C-34. |
| A-15 | The stock of floor space grows in response to the higher yield on new building, and demand for space in Vellmoor is not perfectly elastic. | other | 0.7 | Permits, vacancy rates, rents against Ostbridge. | These consequences fail or lose this chain: C-37, C-38, C-39, C-40. |
| A-16 | In the long run new floor space can be added at roughly constant cost per m² (trades and materials drawn from the wider region). | other | 0.6 | Regional construction market; [a consequence] is a short-run effect. | These consequences fail or lose this chain: C-33. |
| A-17 | For industrial and outlying commercial sites and outlying vacant land, the permitted building is worth less than about 1.5 times the site, so the building tax removed on it is less than the extra land tax. | other | 0.8 | Assessor's ratio of about 0.6 for these sites. | These consequences fail or lose this chain: C-41. |
| A-18 | Construction trades in the region cannot expand at once. | durability | 0.75 | Unemployment in the trades about 3%. | These consequences fail or lose this chain: C-30, C-31, C-32. |
| A-19 | Some drivers who park on downtown lots shop less downtown when parking is scarcer or dearer; new occupants of buildings on former lots shop nearby. | other | 0.65 | Shopper surveys; mix of downtown shops. | These consequences fail or lose this chain: C-49. |
| A-20 | Buyers of property expect the measure to last. | expectations | 0.8 | Charter amendment; no expiry. | These consequences fail or lose this chain: C-14, C-15, C-16, C-39, C-40, C-41, C-42, C-43, C-44, C-48, C-51. |
| A-21 | Buyers' and developers' bids for sites reflect part of the building tax they save on what they would build (downtown buildings; larger houses on large residential lots). | other | 0.7 | Residual land valuation practice; sales of large lots for rebuilding. | These consequences fail or lose this chain: C-40, C-42, C-43. |
| A-22 | Downtown garages cannot be added or extended within a few years. | durability | 0.75 | Garage occupancy; planning times. | These consequences fail or lose this chain: C-46, C-47, C-48. |
| A-N1 | Structured downtown garages have a land share below the city-wide 40%, so their own tax share falls under the measure. | other | 0.7 | NEW. Multi-storey structures on small footprints; offices and high-rise commercial, the closest class, have a 26% land share. Needed for C-47 so that the garage owners' own tax change does not oppose the parking chain. | These consequences fail or lose this chain: C-48. |
| A-N2 | Ostbridge sets its property tax as a rate (1.4%) rather than as a levy that is spread over whatever base it has. | revenue_use | 0.6 | NEW. The record states Ostbridge's tax as a rate; Vellmoor's own charter uses a levy, so the form in Ostbridge is not certain. Needed for C-51. | These consequences fail or lose this chain: C-52. |

**Not reported** (an assumption below 0.5): none. All case assumptions have p of at least 0.5; A-6 (0.55) is the weakest.

### Final check before the report

1. *Uncombined chains.* Every key with chains of opposite sign is in section 7; asset values (C-39 to C-43), parking under U1-b (C-45 to C-48) and downtown shops (C-49) are ambiguous; C-41 rests on A-17 as an explicit dominance premise; C-15 rests on A-4 and A-5 for the opposing charges under §4(b).
2. *Group signs.* Sales or delinquency (C-29) and the general-fund payers (C-28) are groups.
3. *Baseline.* Every sign is against the property tax as it is (single rate on land and buildings, same levy), not against 2026 values or the static projection; the rent consequence C-38 is a decrease against the counterfactual even if rents rise.
4. *Worse off is not poorer.* `resources_available_other_uses` is signed only for classes paying an unavoidable sum (C-10, C-12, C-13) or receiving one (C-11); capitalization does not let the payer escape by selling.
5. *Timing shifts.* Completions are signed per window (C-20, C-21); permits brought forward are an increase in their window against the counterfactual (C-14).
6. *Both sides of every transfer.* Share changes (C-10, C-11), pass-through (C-35, C-36), Assessor budget (C-27, C-28), capitalization falls on owners when expected (C-44).
7. *Every class, every core rule.* CR-4 applied to every class (owners' reclassification, appeals, timing, lobbying, sale; developers' build or hold; Ostbridge siting); CR-6 to rents, construction, parking and appeals; CR-7c to every class owning land or buildings, including garages and Ostbridge; CR-9 along lease, input, substitute, trip and cross-border relations.
8. *Unstated premises.* Garage land share (A-N1) and Ostbridge's tax form (A-N2) added; lobbying uses A-10; every response uses a margin premise.
9. *Pattern baselines.* No patterns cited.

## 11. Report

**The policy:** From 2028 Vellmoor's property tax stops falling on buildings, in four steps (buildings counted at 75%, 50%, 25%, then 0% from 2031), and falls on land alone, assessed every year. The council raises the same sum as before; the rate rises from 1.5% to about 3.75% (more once land values adjust). Vacant parcels are assessed at their value as development sites; built parcels at their value in current use less the cost of their buildings. Whether paved surface lots count as vacant (U1-a) or improved (U1-b) is unsettled.

**Visible consequences:** Owners of land-heavy property pay a larger share of the levy: vacant land, low-rise commercial and industrial, about 38,000 homes on large lots (C-3 to C-5), and surface lots from 2031 under either reading and at once under U1-a (C-1, C-2). Apartments, offices and other homes pay less (C-6 to C-8). The levy itself is unchanged (C-9). Building permits rise from the announcement and building rises over the phase-in (C-14, C-15). Appeals rise (C-24) and the Assessor spends more (C-27).

**Invisible consequences:**
- *Owners:* those whose share rises have less for other uses, and some sell sooner or fall behind (C-10, C-12, C-13, C-29); the others have more (C-11). Low-rise and outlying land loses value (C-41). Some owners put up low-cost buildings, or under U1-b pave vacant land, to be assessed at current-use value (C-17 to C-19). Appeals cost time and money and take longer, with the Board's budget unchanged (C-25, C-26). Later buyers neither gain nor lose (C-44).
- *Builders and trades:* fewer parcels stay unbuilt (C-16); completions move from early January into December (C-20, C-21); trades' wages rise at first (C-30), and other construction, including in Ostbridge, costs more and less is done (C-31, C-32); construction employment rises later (C-33).
- *Tenants:* rents unchanged at first (C-34) except that triple-net office tenants pay less and low-rise tenants more until their leases end (C-35, C-36); lower rents as space is added (C-37, C-38).
- *Parking:* under U1-a fewer lot spaces and dearer parking, gaining garage owners (C-45 to C-48).
- *Ostbridge:* less building, lower land values, and less revenue at its fixed rate (C-50 to C-52).
- *The city:* the Assessor's added budget is paid by other spending or other revenue (C-28). Both sides lobby (C-22, C-23).

**Ambiguous effects:** Values of apartments, offices and smaller-lot homes (C-39): lower tax against expected added supply. Values of large-lot homes and of surface lots (C-40, C-42), and land values city-wide (C-43): capitalized land tax against the building tax buyers expect to save. Parking supply and prices under U1-b (C-45 to C-48): building on lots against paving of vacant land. Downtown shop sales (C-49): drivers deterred against new occupants.

**Key conditions:** The council keeps the levy (A-1, 0.8); class positions against 40% hold (A-2, 0.75); some projects are at the margin (A-3, 0.85); under §4(b) the charge on a better use stays below the building tax removed (A-4, 0.8; A-5, 0.7); outlying sites gain less from untaxed building than they pay in land tax (A-17, 0.8); space responds to the yield and demand is not perfectly elastic (A-15, 0.7). Added premises: garages have a low land share (A-N1, 0.7); Ostbridge taxes at a rate, not a levy (A-N2, 0.6).

**What this analysis cannot say:** How large any change is, so whether land values rise or fall overall, how much building is added, or whether the city's reliance on land-heavy owners is fair. It does not weigh owners who gain against owners who lose. Environmental effects of more building and less parking, and health and safety, are out of scope.

## Consequence list (normal form)


| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C-1 | owners.surface_lots | tax_share_borne (share of the levy) | U1-a: increase; U1-b: decrease | short (2028 to 2030) | visible | B | CR-1 (op 4: K1 and K2 together change the sum each parcel must pay out of a levy that K4 holds fixed; the land tax cannot be reduced by any choice of use under §4(a)); arithmetic on the record's share table (a parcel's share rises if its land share exceeds the city-wide 40%, about 39% under U1-b); CR-8b (with the levy fixed, every rise in one class's share is a fall in another's); U1-a: lots are vacant parcels assessed at site value ($0.60bn), share 1.81% in 2028 rising to 3.75%; U1-b: lots are improved parcels at current-use value less paving ($0.30bn), share 0.93%, 1.12%, 1.41% in 2028 to 2030, all below 1.55% | A-1, A-2 |
| C-2 | owners.surface_lots | tax_share_borne (share of the levy) | increase | long (2031 on) | visible | B | CR-1 (op 4: K1 and K2 together change the sum each parcel must pay out of a levy that K4 holds fixed; the land tax cannot be reduced by any choice of use under §4(a)); arithmetic on the record's share table (a parcel's share rises if its land share exceeds the city-wide 40%, about 39% under U1-b); CR-8b (with the levy fixed, every rise in one class's share is a fall in another's); from 2031 the share is 3.75% (U1-a) or 1.91% (U1-b), both above 1.55% | A-1, A-2 |
| C-3 | owners.vacant_land | tax_share_borne (share of the levy) | increase | short; medium; long | visible | B | CR-1 (op 4: K1 and K2 together change the sum each parcel must pay out of a levy that K4 holds fixed; the land tax cannot be reduced by any choice of use under §4(a)); arithmetic on the record's share table (a parcel's share rises if its land share exceeds the city-wide 40%, about 39% under U1-b); CR-8b (with the levy fixed, every rise in one class's share is a fall in another's); land share 100%: 1.00% rises to 1.18% (2028) and 2.50% to 2.55% (2031) | A-1, A-2 |
| C-4 | owners.low_rise_commercial_industrial | tax_share_borne (share of the levy) | increase | short; medium; long | visible | B | CR-1 (op 4: K1 and K2 together change the sum each parcel must pay out of a levy that K4 holds fixed; the land tax cannot be reduced by any choice of use under §4(a)); arithmetic on the record's share table (a parcel's share rises if its land share exceeds the city-wide 40%, about 39% under U1-b); CR-8b (with the levy fixed, every rise in one class's share is a fall in another's); land share 62%: 18.45% rises to 19.7% (2028) and 28.75% to 29.3% (2031) | A-1, A-2 |
| C-5 | homeowners.high_land_share (about 38,000 homes, land share above 40%) | tax_share_borne (share of the levy) | increase | short; medium; long | visible | B | CR-1 (op 4: K1 and K2 together change the sum each parcel must pay out of a levy that K4 holds fixed; the land tax cannot be reduced by any choice of use under §4(a)); arithmetic on the record's share table (a parcel's share rises if its land share exceeds the city-wide 40%, about 39% under U1-b); CR-8b (with the levy fixed, every rise in one class's share is a fall in another's); the split at 40% is on the 2026 roll and A-2 states it is not reversed | A-1, A-2 |
| C-6 | homeowners.low_land_share (about 67,000 homes) | tax_share_borne (share of the levy) | decrease | short; medium; long | visible | B | CR-1 (op 4: K1 and K2 together change the sum each parcel must pay out of a levy that K4 holds fixed; the land tax cannot be reduced by any choice of use under §4(a)); arithmetic on the record's share table (a parcel's share rises if its land share exceeds the city-wide 40%, about 39% under U1-b); CR-8b (with the levy fixed, every rise in one class's share is a fall in another's); homes as a class fall from 40.0% to 37.5% to 38.2% | A-1, A-2 |
| C-7 | owners.apartments | tax_share_borne (share of the levy) | decrease | short; medium; long | visible | B | CR-1 (op 4: K1 and K2 together change the sum each parcel must pay out of a levy that K4 holds fixed; the land tax cannot be reduced by any choice of use under §4(a)); arithmetic on the record's share table (a parcel's share rises if its land share exceeds the city-wide 40%, about 39% under U1-b); CR-8b (with the levy fixed, every rise in one class's share is a fall in another's); land share 30%: 20.0% falls to 19.4% (2028) and 15.0% to 15.3% (2031) | A-1, A-2 |
| C-8 | owners.offices | tax_share_borne (share of the levy) | decrease | short; medium; long | visible | B | CR-1 (op 4: K1 and K2 together change the sum each parcel must pay out of a levy that K4 holds fixed; the land tax cannot be reduced by any choice of use under §4(a)); arithmetic on the record's share table (a parcel's share rises if its land share exceeds the city-wide 40%, about 39% under U1-b); CR-8b (with the levy fixed, every rise in one class's share is a fall in another's); land share 26%: 19.0% falls to 18.2% (2028) and 12.5% to 12.7% (2031) | A-1, A-2 |
| C-9 | officials.city_budget | tax_revenue (property levy collected) | no_change | short; medium; long | visible | B | CR-1 (K4: the levy is set as under §8 and not increased by reason of the chapter); CR-8b (the rate is the levy over the base, so a smaller base raises the rate, not the levy: 1.5% becomes 1.765% to 3.75%, or about 4.4% with capitalization, while the sum stays the same); A-1 (the council sets the same levy) | A-1 |
| C-10 | owners.vacant_land, owners.low_rise_commercial_industrial (owner-occupiers, and lessors once triple-net leases end), homeowners.high_land_share | resources_available_other_uses | decrease | short; medium; long | invisible | B | CR-3 note (resources fall where the class pays a sum it cannot avoid: under §4(a) the land tax does not depend on use, and selling does not avoid it because it is capitalized, CR-7c); CR-8b (the rise in their bills, C-3 to C-5, is the counterpart of the fall in others', C-11); CR-3c | A-1, A-2 |
| C-11 | owners.apartments, owners.offices (owner-occupiers, and lessors once triple-net leases end), homeowners.low_land_share | resources_available_other_uses | increase | short; medium; long | invisible | B | CR-8b (the fall in their bills, C-6 to C-8, adds to them what C-10 takes from the classes whose share rises); CR-1 (op 4) | A-1, A-2 |
| C-12 | owners.surface_lots | resources_available_other_uses | U1-a: decrease; U1-b: increase | short (2028 to 2030) | invisible | B | CR-3 note and CR-8b, applied to C-1: under U1-a the lots' bill rises (an unavoidable sum); under U1-b it falls until 2030 | A-1, A-2 |
| C-13 | owners.surface_lots | resources_available_other_uses | decrease | long (2031 on) | invisible | B | CR-3 note and CR-8b, applied to C-2: under both readings the bill is above the counterfactual from 2031 | A-1, A-2 |
| C-14 | sellers.prospective (developers and owners of developable sites) | applications (dwelling and commercial building permits) | increase | short (from June 2026) | visible | B | CR-10a (a change expected in the future alters choices now: buildings started in 2026 and 2027 are finished two to four years later, when the building tax is 25% to 75% lower or nil); CR-4 (x: hold the site or keep its current use, y: build; K2 removes a charge attached to y, worth about 4.5% of site value a year downtown); A-20 (the measure is expected to last). The land tax under §4(a) attaches to a vacant parcel whatever is built, so it does not change the ranking of x and y (CR-4 needs a relative change) | A-3, A-20 |
| C-15 | sellers.prospective (developers and owners of developable sites) | investment_target (new buildings in Vellmoor) | increase | medium; long | visible | B | CR-1 (op 3: K2 removes the tax attached to the option 'build' in steps to 2031); CR-4 (x: hold, y: build; owners at the margin switch, A-3); for vacant parcels the land tax does not depend on use; for lots under U1-b building moves the land value from current use to site value, a charge of about 1.9% of site value a year, which is below the 4.5% building tax removed (A-4); for improved parcels under §4(b) the tax on the rise in current-use value is below the building tax removed (A-5); CR-7a (means move toward the higher yield). Three independent chains, each with its own premise; A-3 and A-20 are common to all. Medium and long only: A-18 limits what can be built in the short run (CR-6, 0.9) | A-3, A-20 |
| C-16 | owners.vacant_land, owners.surface_lots | units_held_vacant (parcels held unbuilt: vacant land and surface lots) | decrease | medium; long | invisible | B | CR-4 applied to C-15 (x: keep the parcel unbuilt, y: build); CR-10b (the stock of unbuilt parcels changes only as projects are completed) | A-3, A-20 |
| C-17 | owners.vacant_land | reclassification (low-cost buildings put up so that the parcel is assessed under §4(b)) | increase | short; medium | invisible | B | CR-4 (x: leave the parcel vacant and be assessed under §4(a) at its value as a site for its highest permitted use; y: put up a low-cost building and be assessed under §4(b) at current-use value less the building's depreciated cost; K3 makes y better for owners whose saving exceeds the building's cost, A-6). The direction is a priori; that some owners are at this margin is A-6 | A-6 |
| C-18 | owners.surface_lots | reclassification (low-cost buildings put up so that the lot is assessed under §4(b)) | U1-a: increase; U1-b: no_change | short; medium | invisible | B | CR-4 as in C-17. U1-a: a lot is a vacant parcel, so a building moves it from §4(a) to §4(b), A-6. U1-b: the lot is already an improved parcel under §4(b), so the option brings nothing new (CR-1: no operation) | A-6 |
| C-19 | owners.vacant_land | reclassification (parcels paved and run as parking) | U1-a: no_change; U1-b: increase | short | invisible | B | U1-b: CR-4 (x: leave vacant at site value, y: pave for about 3% of site value once and be assessed under §4(b) at about half, saving about 0.9% to 1.9% of site value a year, A-7). U1-a: paving leaves the parcel vacant (§2(f): no building), so it is still assessed under §4(a) and nothing changes (CR-1: no operation) | A-7 |
| C-20 | sellers.prospective (developers) | quantity_supplied (building completions in the last weeks of December, 2027 to 2030) | increase | short; medium | invisible | B | CR-10a and CR-4 (x: complete just before 1 January, y: just after it; y saves that year's tax on the building, 1.5% of its value without the measure, but only 1.324%, 1.071%, 0.682% and 0% for completions around 1 January 2028, 2029, 2030 and 2031 under the measure; y made worse relative to x, so some projects that would have been held into January finish in December, A-8). Signed per window against the counterfactual (CR-12h) | A-8 |
| C-21 | sellers.prospective (developers) | quantity_supplied (building completions in the first weeks of January, 2028 on) | decrease | short; medium; long | invisible | B | Mirror window of C-20: CR-10a, CR-4. From 2031 on there is no building tax, so the counterfactual January clustering does not occur at all (A-8) | A-8 |
| C-22 | owners.surface_lots, owners.low_rise_commercial_industrial, homeowners.high_land_share | lobbying_effort (for repeal, deferral, a deferral programme, and the U1-b reading) | increase | short; medium | invisible | B | CR-4 (x: accept, y: lobby; C-1 to C-5 make x worse for them); CR-4 1.0 (after the vote the question would not be open on the no-measure path, so lobbying over the measure's terms and the Assessor's reading exists only under the policy, CR-12 0.9); CR-8c (resources used up) | A-10 |
| C-23 | sellers.prospective (developers), owners.offices, owners.apartments | lobbying_effort (to keep the measure and for the U1-a reading) | increase | short; medium | invisible | B | CR-4 (x: accept attempts to repeal or narrow it, y: lobby to keep it; C-7, C-8 and C-15 give them a stake); CR-4 1.0 as in C-22; CR-8c | A-10 |
| C-24 | owners.all_classes (appellants) | applications (valuation appeals to the Board of Equalization) | increase | short | visible | B | CR-4 (x: accept the land valuation, y: appeal; from 2028 the land value carries a rising share of the tax, up to all of it, and is assessed every year under a new method, so a given error costs more, A-11) | A-11 |
| C-25 | owners.all_classes (appellants) | compliance_cost (preparing and arguing appeals) | increase | short; medium | invisible | B | CR-8c (resources spent on appeals are used up), applied to C-24 | A-11 |
| C-26 | owners.all_classes (appellants) | wait_time (decision on an appeal) | increase | short; medium | invisible | B | CR-6 (0.7, public supply: the Board decides appeals with an unchanged budget; with 9,000 to 12,000 appeals against about 6,000 its fixed capacity is rationed by waiting); CR-6 1.0 (the clause applies because demand exceeds a fixed quantity; the group of margins is collapsed to waiting since the Board sets no price and the record gives no other margin) | A-11 |
| C-27 | officials.assessor | enforcement_cost | increase | short; medium; long | visible | A | CR-1 (op 4: about $14 million once in 2027 and about $9 million a year more to the Assessor); CR-8c (resources spent administering the measure are used up) | none |
| C-28 | taxpayers, recipients of other city spending | resources_available_other_uses | at_least_one_decrease | short; medium; long | invisible | B | CR-8b and CR-8 0.7 (payers from the general budget: the Assessor's added budget, C-27, comes from the general fund and K4 forbids raising the levy because of the chapter, so it is paid by other spending forgone or other revenue; who is not established, so the payers are a group); CR-8a | A-1 |
| C-29 | homeowners.high_land_share, owners.low_rise_commercial_industrial | turnover (sales by owners whose bills rise), legal_breach (tax delinquency) | at_least_one_increase | short; medium | invisible | B | CR-4 exception (the rise in the bill, C-4 and C-5, reduces the means of owners who cannot pay it from income, and there is no deferral); CR-4 (x: keep paying from other means, y: sell sooner or fall behind, A-9); CR-3 note. Which response each takes is not established, so the two are a group | A-9, A-1, A-2 |
| C-30 | input_suppliers.construction_trades | wage_rate | increase | short | invisible | B | CR-9 and LW-10 (demand for the labor that builds follows demand for building, C-14 and C-15); CR-6 (0.9: the trades cannot expand at once, A-18, so the added demand is taken in price) | A-3, A-18 |
| C-31 | buyers.substitutes (renovation and construction outside the new projects, including Ostbridge) | price_paid (construction work) | increase | short | invisible | B | CR-9 (they compete with Vellmoor developers for the same trades); CR-7a (the wage rise, C-30, spreads to every use of the movable labor) | A-3, A-18 |
| C-32 | buyers.substitutes (renovation and construction outside the new projects, including Ostbridge) | quantity_traded (construction work) | decrease | short | invisible | B | CR-4c (at a higher price the last unit is given up); CR-8a (labor drawn into Vellmoor projects is withdrawn from other uses). Depth 4 from K2: chain stops | A-3, A-18 |
| C-33 | input_suppliers.construction_trades | employment (construction in Vellmoor) | increase | medium; long | invisible | B | CR-9 and LW-10 (more building, C-15); CR-7a (labor moves in from the wider region as it can, A-16) | A-3, A-16 |
| C-34 | tenants (residential, and commercial tenants not on triple-net leases) | price_paid (rent) | no_change | short | invisible | B | CR-6 (the rent is set where planned lettings and planned rentals are compatible; within a year or two the stock of space and tenants' demand are both unchanged, A-14, so the clearing rent is unchanged); CR-7b (the change in owners' tax settles on the owners of the fixed stock) | A-14 |
| C-35 | tenants.commercial_triple_net (offices and other high-rise commercial) | price_paid (rent plus the tax passed through) | decrease | short (remaining term of existing leases) | invisible | B | CR-9 (contract: the lease passes the parcel's tax to the tenant, A-13); CR-1 (op 4 reaches the tenant through the lease) applied to C-8; at renewal CR-7b and C-34 apply instead | A-13, A-1, A-2 |
| C-36 | tenants.commercial_triple_net (low-rise commercial and industrial) | price_paid (rent plus the tax passed through) | increase | short (remaining term of existing leases) | invisible | B | CR-9 (contract, A-13); CR-1 (op 4 through the lease) applied to C-4; at renewal CR-7b applies instead | A-13, A-1, A-2 |
| C-37 | owners.all_classes | capital_stock_target (floor space in Vellmoor) | increase | medium; long | invisible | B | CR-10b (the stock changes through flows: completions from C-15 add to it); A-15 | A-3, A-15 |
| C-38 | tenants (residential and commercial) | price_paid (rent) | decrease | medium; long | invisible | B | CR-6 (more space at each rent, C-37, with demand not perfectly elastic, A-15, moves the clearing rent down); in the long run, with roughly constant cost per m² (A-16), new space is added until its yield net of tax is back in line (CR-7a), and new space pays no building tax, so the rent stays below the counterfactual. Low-rise owners' higher land tax does not raise rents at renewal (CR-7b: land is fixed) | A-3, A-15 |
| C-39 | owners.apartments, owners.offices, homeowners.low_land_share | asset_value (property) | ambiguous | short (from June 2026; fully from 3 November 2026) | invisible | B | CR-12b over two chains: (+) CR-7c and CR-10c (the fall in their tax share, C-6 to C-8, raises expected net yield; captured by whoever owns at the time it becomes expected, part of the way from June as the polls rose, A-20); (−) CR-10c with CR-6 (expected added space, C-37, lowers expected rents and home prices, A-15). No premise says which dominates | A-2, A-20, A-15 |
| C-40 | homeowners.high_land_share | asset_value (property) | ambiguous | short (from June 2026) | invisible | B | CR-12b: (−) CR-7c, CR-10c (higher tax share, C-5, A-20); (−) expected added housing (A-15); (+) CR-7c (buyers who would rebuild larger houses on large lots bid in part of the building tax they save, A-21). No dominance premise | A-2, A-20, A-15, A-21 |
| C-41 | owners.low_rise_commercial_industrial, owners.vacant_land (outlying) | asset_value (land and property) | decrease | short (from June 2026) | invisible | B | CR-7c, CR-10c: (−) higher tax share, C-3 and C-4, capitalized (A-20); (+) bidders reflect the building tax they would save on what they would build (A-21), but on these sites the permitted building is worth less than about 1.5 times the site, so the building tax removed is less than the extra land tax (A-17: an empirical dominance premise under CR-12e); (−) expected added commercial space lowers rents (A-15), same direction | A-2, A-17, A-20 |
| C-42 | owners.surface_lots | asset_value (land) | ambiguous | short (from June 2026) | invisible | B | CR-12b. U1-a: (−) the land tax on the lots rises from 1.55% to 3.75% of the levy (C-1, C-2), capitalized (CR-7c, A-20); (+) developers' bids reflect the building tax they save, about 4.5% of site value a year downtown (A-21, A-3). U1-b: (+) lower tax to 2030; (−) higher tax from 2031; (+) A-21. No dominance premise under either reading | A-20, A-21 |
| C-43 | owners.all_classes | asset_value (taxable land, city-wide) | ambiguous | short (from June 2026) | invisible | B | CR-12b: (−) CR-7c and CR-10c: the tax on land rises from 1.5% to 3.75% of its value, and a buyer pays only what leaves them a normal return (the Assessor puts the fall at about 15% by 2031); (+) A-21: bids for developable sites include part of the building tax saved. No dominance premise for the city-wide total | A-20, A-21 |
| C-44 | buyers.prospective (of property after November 2026) | return_on_capital | no_change | long | invisible | B | CR-7c (a change in expected yield is borne or captured by whoever owns the asset when it becomes expected, not by later buyers, who pay a price that leaves them the return available elsewhere); CR-10c; A-20 | A-20 |
| C-45 | owners.surface_lots (parking operators) | quantity_supplied (surface parking spaces downtown) | U1-a: decrease; U1-b: ambiguous | medium; long | invisible | B | U1-a: CR-4 (lots built on, C-15, C-16) and CR-10b. U1-b: CR-12b: (−) lots built on (A-4); (+) vacant parcels paved and run as parking (C-19, A-7). No dominance premise | A-3, A-4, A-7 |
| C-46 | buyers.substitutes (drivers parking downtown) | price_paid (downtown parking) | U1-a: increase; U1-b: ambiguous | medium; long | invisible | B | U1-a: CR-9 (lot spaces are a substitute for garage spaces) and CR-6 (fewer spaces at each price, with lots about 85% full, moves the price up); CR-12 0.9 (the rise is not reversed by added garage supply, which cannot come within a few years, A-22). U1-b: the quantity is ambiguous (C-45), so the price is | A-3, A-22, A-7 |
| C-47 | sellers.substitutes (owners of downtown garages) | net_price_received (garage parking) | U1-a: increase; U1-b: ambiguous | medium; long | invisible | B | CR-9 (substitute) and CR-6, as C-46; A-22 (garages cannot be added at once) | A-3, A-22, A-7 |
| C-48 | sellers.substitutes (owners of downtown garages) | asset_value (garages) | U1-a: increase; U1-b: ambiguous | short (from June 2026) | invisible | B | CR-7c and CR-10c applied to C-47 (expected higher yield captured by owners when expected, A-20); their own tax share falls (A-N1), the same direction. U1-b: C-47 is ambiguous, and the garages' own tax cut is (+), but the parking chain can push either way (CR-12 0.8, kind 3) | A-3, A-20, A-22, A-N1, A-7 |
| C-49 | sellers.complements (downtown shops) | quantity_traded (downtown retail sales) | ambiguous | medium; long | invisible | B | CR-9 (trip complement: parking and shopping): (−) drivers who park on lots shop less downtown when parking is scarcer or dearer, C-46 (A-19); (+) CR-9 (proximity of buyers: new occupants of buildings on former lots shop nearby, A-19). CR-12b, no dominance premise | A-19, A-3 |
| C-50 | neighboring_jurisdictions (developers in Ostbridge) | investment_target (new buildings in Ostbridge) | decrease | medium; long | invisible | B | CR-9 (across_border: Vellmoor and Ostbridge sites are substitutes for some projects, A-12); CR-4 (x: build in Ostbridge, which keeps its building tax; y: build in Vellmoor, made better by K2); CR-7a; also CR-9 via C-31 (dearer trades), same direction | A-12, A-3 |
| C-51 | neighboring_jurisdictions (owners of development land in Ostbridge) | asset_value (land) | decrease | short (from June 2026) | invisible | B | CR-7c and CR-10c applied to C-50 (lower expected demand for Ostbridge sites) | A-12, A-20 |
| C-52 | officials.ostbridge | tax_revenue | decrease | medium; long | invisible | B | CR-9 and arithmetic: with a fixed rate of 1.4% on land and buildings (A-N2), fewer new buildings (C-50) and lower land values (C-51) give a smaller base than on the counterfactual path | A-12, A-3, A-N2 |

## Gaps found

**(a) Steps no core rule covers.**
- GAP-058-C1. The record's share table is a static arithmetic result; the direction of each class's share under revaluation needed A-2. No core rule says how a fixed levy divided over a changing base propagates capitalization back into rates; it was handled by arithmetic (section 8). Not a rule gap, but the calculus has no explicit statement that a revenue-neutral levy makes the classes' changes sum to zero (CR-8b was used, and CR-12f to suppress the total).
- GAP-058-C2. Under §4(b), the land tax on an improved parcel depends on its current use, so it is partly a tax on the use itself. CR-1 handles it as operation 3, but no core rule distinguishes a tax on a fixed stock (land at site value, which no choice avoids) from a tax whose base the owner moves by choosing a use. The distinction was decisive for C-15 to C-19 and was derived each time from CR-4 by hand.

**(b) Core-rule wording that was hard to apply.**
- CR-7c with competing expectations: an asset's value at announcement reflects both the owner's tax change and the expected supply response (C-39, C-40). CR-7c does not say whether an expected later response by others is a second chain to combine (treated as one, under CR-12b) or part of the same capitalization.
- CR-12e: whether A-17 ("building tax removed below the extra land tax") counts as an empirical dominance premise or as arithmetic on the record's ratio of 0.6 was unclear; treated as an empirical premise with its own p.
- CR-4 1.0 on lobbying: the measure was contested before the vote on both paths; after the vote only the policy path has a question open. The note does not say whether that split by date is the intended reading.
- CR-6 0.7 public supply applied to an appeals board: the clause speaks of a good supplied at a set price; an adjudicating body with a fixed budget fits by analogy only.

**(c) Vocabulary missing from the ontology.**
- No variable for a tax rate, or for the timing of completions; `quantity_supplied` with a dated qualifier was used for completions.
- No variable for a class's tax bill as distinct from its share; `tax_share_borne` with a fixed levy was used.
- No actor class for an adjudicating body (the Board of Equalization) separate from `officials.enforcement`.


## Comparison with the pattern-based analysis

**Summary.** The two versions agree on almost all of the land value tax shift: every class's share of the levy and the lots' per-reading, per-window shares; building on lots and elsewhere; the reclassification works that §4(b) invites; surface parking and its price under each reading; completions moved from early January into December; Ostbridge building and land; triple-net tenants during their leases; rents unchanged at first and lower as space is added; lower values for low-rise and outlying land and parcels and ambiguous values elsewhere; trades' wages and employment; downtown shops; who has more or less to spend; and the Assessor's cost and its payers. No key is signed in opposite directions. The differences are in recording and in a few claims. The pattern version signs sales and delinquency by owners short of means as two separate increases on a premise (A-9) that says only that they do one or the other, and reports ground rents as `no_change` "from the land tax alone", which is one chain, not the policy's consequence: the building relief raises what users will pay for sites (its own A-21). The core version collapses the Board's group of margins to waiting, against CR-6's 1.0 clause; it signs other construction as falling for a class that includes renovation in Vellmoor, which K2 itself favors; and it omits the two revenue items and the long-run return on new building, which the core rules derive. The pattern version omitted permits brought forward from the announcement, the rise in what other construction buyers pay, and the garage owners' side of the parking market. TX-2's "failure" is a pattern that does not apply, not one that was wrong.

Counts: M 32, V 7, S 3, OP 8, OC 8.

### Pattern version → core version

| Pattern ID | Matched core ID(s) | Class | Cause | Note |
| --- | --- | --- | --- | --- |
| C-1 | none | OC | E | Building item of `tax_revenue` decrease. Arithmetic on the record's figures with CR-1; CR-12's 0.8 note on two items says to record each item. Core-version omission (it recorded only the total, C-9). |
| C-2 | none | OC | E | Land item of `tax_revenue` increase. As C-1: core-version omission. |
| C-3 | C-8 | M | | Offices' share falls. |
| C-4 | C-7 | M | | Apartments' share falls. |
| C-5 | C-6 | M | | Low-land-share homes' share falls. |
| C-6 | C-5 | M | | High-land-share homes' share rises. |
| C-7 | C-4 | M | | Low-rise share rises. |
| C-8 | C-3 | M | | Vacant land's share rises. |
| C-9 | C-1 | M | | Lots 2028 to 2030: U1-a increase, U1-b decrease. |
| C-10 | C-2 | M | | Lots from 2031: increase under both readings (the core gives one sign). |
| C-11 | C-15, C-16 | V | | Building on lots: the core merges all new building in C-15 (its three chains, with A-4 for lots under U1-b) and records the fall in parcels held unbuilt (C-16). |
| C-12 | C-15 | V | | Building on other sites, including redevelopment under §4(b) (A-5): inside the core's C-15. |
| C-13 | C-17, C-18, C-19 | V | | The core splits reclassification by owner and work: vacant land builds (both readings), lots build only under U1-a (U1-b: `no_change`, already improved), vacant land paves only under U1-b. The pattern version's text gives the same split; its one row hides it. |
| C-14 | C-45 | M | | Surface spaces: U1-a decrease, U1-b ambiguous. |
| C-15 | C-20 | M | | Completions in late December rise. Both versions stop the window at 2030 or 2031; against the counterfactual, where the 1.5% building tax rewards a January completion every year, the shift continues indefinitely (the core gives C-21, but not C-20, a long horizon). |
| C-16 | C-21 | M | | Completions in early January fall. |
| C-17 | C-50 | M | | Less building in Ostbridge. |
| C-18 | C-36 | M | | Triple-net tenants of low-rise parcels pay more during their leases. |
| C-19 | C-35 | M | | Triple-net office tenants pay less during their leases. |
| C-20 | C-10, C-34 | V | | Low-rise owners' net rent falls on renewal: the core records the same incidence as lessors' means falling once leases end (C-10) with rents unchanged (C-34). |
| C-21 | C-11, C-34 | V | | Office owners' net rent rises on renewal: as C-20, mirrored. |
| C-22 | C-29 | S | E | Pattern: `turnover` increase. Core: `turnover` and `legal_breach` as a group, `at_least_one_increase`. Core right: CR-4's exception gives a change in means; which response each owner takes (sell sooner, fall behind, or pay from savings or a loan) is a premise per margin, and A-9 states only "they sell sooner or fall behind". Error in the pattern version (no pattern involved: CR-4 exception, CR-3a). |
| C-23 | C-29 | S | E | Pattern: `legal_breach` increase, also for `owners.vacant`. As C-22: one disjunctive premise cannot sign both members. The pattern's RS-3 citation also does not fit (RS-3 concludes `informal_activity`, for evasion that pays, not arrears from a want of means). Error in the pattern version. |
| C-24 | C-22, C-23 | V | | Lobbying increase. The pattern version signs only questions that exist under the measure; the core's qualifiers add lobbying "for repeal" and "to keep the measure", reasoning that after the vote the question is closed on the no-measure path. CR-4's 1.0 note says lobbying over a question contested on the counterfactual path needs a premise; whether a repeal campaign is the same question as the ballot fight is the analyst's reading (the core version flags it). Same sign; the core's wider qualifier is the weaker part. |
| C-25 | C-24, C-25 | M | | Appeals and their cost (the core adds the count of appeals, C-24). |
| C-26 | C-34 | M | | Rents unchanged in the short run. |
| C-27 | C-38 | M | | Rents fall as space is added; the core adds the medium horizon. |
| C-28 | C-37 | M | | Floor space grows. |
| C-29 | none | OC | P | Ground rents on new ground leases `no_change` "from the land tax alone". Analyst misapplied DM-1 and CR-7b: the land tax's own chain gives no change in rent for a fixed factor, but the policy also removes the tax on what a lessee builds, and the pattern version's own A-21 (bids for sites reflect part of the building tax saved) raises what lessees pay for sites. No chain lowers ground rent (the later fall in space rents dissipates the same relief and cannot reverse it, CR-12e). Under CR-12a the policy's sign is `increase` on A-21 (p 0.7), not `no_change`; a one-chain qualifier is not a consequence. DM-1's If clause (TX-2 or SB-2 applies) is also not met. The core version stated the land-tax chain in C-38's text only. |
| C-30 | none | OC | J | New buildings' `return_on_capital` increase while the stock adjusts (CR-7a, A-14). Derivable, but how much of it sites capture through their price (A-21) decides whether the builder's return or the land value carries it; a recording choice. |
| C-31 | none | OC | E | New buildings' `return_on_capital` `no_change` in the long run: CR-7a with A-16. Derivable from the core rules; core-version omission (it cites A-16 only for employment). |
| C-32 | C-39 (parcel) | OC | J | Existing buildings, as an item of `asset_value`, increase at expectation. Valid by CR-7b, CR-7c and CR-10c, with a premise the pattern version does not state: building cost does not fall as building expands (with falling cost, long-run rents fall by more than the tax removed). The core recorded parcels only; splitting land and building items of one parcel is a recording choice (the pattern version's own vocabulary gap, d4). |
| C-33 | none | OC | J | Existing buildings' value per m² `no_change` in the long run (A-16). Same item split as C-32; derivable from CR-7a with A-16. |
| C-34 | C-43, C-42 | V | | Land under high permitted building: ambiguous. The core groups all land city-wide (C-43) and the lots (C-42), both ambiguous. |
| C-35 | C-41 | M | | Low-intensity land: decrease on A-17. |
| C-36 | C-41 | M | | Low-rise and vacant parcels: decrease. The core restricts vacant land to outlying sites, which is all that A-17 covers; the pattern version's `owners.vacant` (mostly outlying) includes downtown vacant sites, where C-34's ambiguity applies. |
| C-37 | C-39, C-40 | M | | Bill-falling classes and large-lot homes: ambiguous. |
| C-38 | C-42 | M | | Lots: ambiguous under both readings. |
| C-39 | none (core C-11) | OC | J | Bill-falling owners' `return_on_capital` (net of tax) increase 2028 to 2030. Valid for owners who held when the measure became expected; a later buyer earns the normal return (core C-44). The core records the same gain as means (C-11). |
| C-40 | C-51 | M | | Ostbridge land falls. |
| C-41 | C-33 | M | | Construction employment in Vellmoor rises. |
| C-42 | C-30 | M | | Trades' wages rise in the short run. |
| C-43 | C-46 | M | | Parking price: U1-a increase, U1-b ambiguous. |
| C-44 | C-49 | M | | Downtown shops: ambiguous. |
| C-45 | C-10 | M | | Bill-rising classes have less for other uses. |
| C-46 | C-11 | M | | Bill-falling classes have more. |
| C-47 | C-12, C-13 | M | | Lots' means per reading and window. |
| C-48 | C-27 | M | | Assessor's cost. |
| C-49 | C-28 | M | | Its payers, a group. |
| C-50 | C-26 | S | E | Pattern: group (`wait_time` +, time per appeal −), `at_least_one_as_stated`. Core: `wait_time` increase. Pattern right: CR-6's 1.0 clause on public supply gives a group sign over the margins, "not any one of them alone", and the pattern names an open margin (less time per appeal) that the core version says the record lacks. Error in the core version. |

### Core-only consequences

| Core ID | Class | Cause | Note |
| --- | --- | --- | --- |
| C-9 | OP | J | Total levy `no_change`. CR-12's 0.8 note says to record the total; CR-12f says chains that cancel by construction are not reported; the versions read the conflict oppositely (the pattern version did not report it). The core's qualifier "collected" is also loose: its own C-29 raises delinquency, so collections can fall slightly; "levied" would be exact. |
| C-14 | OP | E | Permits rise from June 2026 (CR-10a, CR-4): projects started then are finished when the building tax is lower. The pattern version has this only as a path note (section 8). Pattern-version omission. |
| C-31 | OP | E | Other construction buyers pay more for the trades (CR-9, CR-7a, A-18). The pattern version mentions labor drawn from other work (OC-5) but records no price. Pattern-version omission. |
| C-32 | OP | E | Other construction `quantity_traded` decrease. Valid for construction outside Vellmoor and for work K2 does not touch; but the core's class includes renovation in Vellmoor, which K2 itself makes cheaper to keep (improvements untaxed), so for that part the chains oppose (CR-12b: ambiguous). Error in the core version (class too wide); the valid part is a pattern-version omission. |
| C-44 | OP | J | Later buyers' return `no_change`. The pattern version says the same in text (SB-4) without a row. |
| C-47 | OP | E | Garage owners' net price under U1-a increase (CR-9, CR-6, A-22). The pattern version cites RS-16 for garages as the substitute but records only drivers' side. Pattern-version omission. |
| C-48 | OP | E | Garage values under U1-a increase (CR-7c, with the new premise A-N1 that garages' own tax share falls). Pattern-version omission. |
| C-52 | OP | A | Ostbridge's revenue falls at a fixed rate. The core adds A-N2 (Ostbridge taxes at a rate, p 0.6); the pattern version stopped on the premise that Ostbridge, like Vellmoor, sets a levy and lets the rate absorb the base. The record states only "1.4% of the assessed value". |

### Findings

- **Pattern overclaims or hidden premises.** (1) Owners short of means (C-22, C-23): two members signed on one disjunctive premise; the correct record is the core's group. (2) Ground rents (C-29): one chain reported as the consequence; the policy's sign is `increase` on A-21. (3) Existing buildings' value at expectation (C-32) needs a premise that building cost does not fall as building expands. (4) C-36 extends A-17 to vacant sites it does not cover.
- **Errors in the core version.** The Board's margins collapsed to waiting (C-26), contrary to CR-6's 1.0 clause; other construction signed down for a class that includes Vellmoor renovation (C-32); "collected" in C-9 where its own C-29 lowers collections; lobbying for repeal and to keep the measure included without the premise CR-4's 1.0 note asks for (C-22, C-23). Omissions: the two revenue items (pattern C-1, C-2) and builders' long-run return (C-31). Its horizon labels (short "2028 to 2030", long "2031 on") do not match its own definitions in section 8.
- **Errors in the pattern version.** Beyond the overclaims above: omissions of permits from the announcement (core C-14), the price of construction to other buyers (C-31), garage owners' receipts and values (C-47, C-48). DM-1 is cited for incidence of a tax on holding although its If clause requires TX-2; CR-7b alone carries it. TS-10's "activity bunches before each step" does not describe what happens here (a counterfactual incentive to delay past 1 January shrinks); its use was a stretch the core rules did not need.
- **Limits of the core rules.** None that produced a difference: every claim in either version that holds was derived, or is derivable, from CR-1 to CR-12. The core version's GAP-058-C2 (a land tax that depends on use under §4(b)) was handled by CR-1 operation 3 and CR-4, as the pattern version handled it; it is a missing pattern, not a calculus gap.
- **The pattern version's "Test of 1.0".** *TX-2, failed:* the core version confirms the substance (under §4(a) the land tax changes no ranking of uses, C-14 to C-16; owners bear it, CR-7b and CR-7c) but contradicts the verdict as a pattern failure: TX-2's If clause (a tax on a sale) and its Assumes clause (one side can reduce its quantity) both fail, so TX-2 does not apply; nothing in it is wrong as written. A pattern for a tax on a fixed factor would also need a clause for assessment by current use (§4(b)), where the tax does fall on use. *RS-8, the claim that builders wait for a lower step failed on arithmetic:* confirmed (core section 8, same argument). *CR-7 1.0, which stock, needed interpretation:* neither confirmed nor contradicted; the core did not use the clause and reached parcel values and their persistence from CR-7c, CR-10b and CR-10c. *CR-12 1.0, response argument, needed interpretation:* confirmed; the core derived the long-run rent fall (C-38) from CR-6 with A-15 alone, so in an expansion the constant-cost premise bears only on the end state. *CR-12 0.8 two items with CR-12f, needed interpretation:* confirmed; the two analysts resolved it oppositely (pattern: items, no total; core: total, no items). *TS-10 for a tax schedule, needed interpretation:* confirmed that its If clause does not cover taxes; the core rules gave the same results without it.
