# WE-044 Saltmere, expand loop (blind run)

Read: section 1 and the assumption table only (the extracted files). Note: a bare `ls cases/we044_saltmere` once listed the
file names already in that folder (answers.json, out_of_sample.md, policy.txt); none was opened. The policy text used is
`policy.txt` in this folder (a copy of section 1). `tools/` holds the scripts that wrote seed.json, proposals.json and
answers.json (facts are written there with the sentence they rest on in `src=`).

Result: DONE in 3 rounds, 40 nodes (10 + 19 + 11, revisits counted), 59 proposed facts, 32 questions (32 from the table, 0 judged).
No `off-list:` lines. Final engine output is in `final_output.txt`, the situation in `situation.json`.

## Seed (policy's own facts, CR-1)
- e1 non-primary whole-unit lets (buyers.short_stay / owners.non_primary), `banned` k1 (premises: a1 binding, a2 platforms comply). 
- e2 primary-residence lets (owners.primary_residence), `capped` k1_cap (90 nights; unsatisfied seller owners.over_90_nights; premises j1, a2) and `charge` k3 ($250, operating, receiver general_fund, a2).
- e3 two-unit buildings (owners.two_unit) under `unclear` U1: U1-a gives `capped` k1_cap_u1a + `charge` k3_u1a (unsatisfied owners.two_unit_over_90); U1-b gives `banned` k1_ban_u1b.
- `announced` k1 (a30); `compliance` k2 platforms, k3 owners.primary_residence; `enforcers` k2/k3 officials.registry, k4 officials.enforcement; `funded` k3 by general_fund (a20); `fixed_budget` k4 (j3).
- Judged seed premises (not asked as questions, written into the seed): j1 and j2 (the 90-night cap binds on some hosts; from the counts of 140 and 120 hosts above 90 nights, p 0.95), j3 (K4 is within Code Enforcement's existing fixed budget; "No new appropriation", p 0.9).
- Table premises in the seed: a1, a2, a20, a30.

## Round 1 (depth 1, 10 nodes)
- buyers.short_stay: alternatives hotels (a8), Elsdon (a10, a39), 30-night stays (a31), rooms in occupied homes (a32), primary-residence lets (a32), skipping or shortening trips (a11, `inverse` on trips); outside margin direct booking (a4); timing bring_forward of trips before July (a17) and of bookings (a15); link trips to retailers.neighbors (a12).
- owners.non_primary: alternatives 12-month lease (a5, landlords.long_term quantity_supplied), 30-night lets (a7, owners.mid_term), hold vacant (a6), sell (a37, `turnover`), reshape into nominal 30-night contracts (a38, reclassification), claim primary residence (a38, owners.primary_residence number_of_sellers); outside margins informal_activity (a3) and screening of guests (a27, a3); stake (a14); timing carry_over of summer lets (a16); asset (a30) and yield (a1) of the banned side; links to cleaning labor (a26), Code Enforcement's complaint work (a18), TOT (no premise: R2 is in section 1), R1 fees (a34), home values both ways (a21 investor demand through `yield`; a23 fewer transient neighbors through `substitute`), home prices through sales (a37).
- owners.primary_residence: outside margin (a3, a4). owners.over_90_nights and owners.two_unit_over_90: legal_breach through multi-platform lets (a22), outside margin (a3). owners.two_unit: alternatives under k1_ban_u1b (a5, a7), outside margin (a3). platforms: stake (a14). general_fund: receipts paid_into fund_balance (a20). officials.registry: spending paid_from fund_balance (a20). officials.enforcement: empty.

## Round 2 (depth 2, 19 nodes)
Revisits of round-1 nodes got empty lists (nothing new to add); general_fund#2 got tax_revenue paid_into fund_balance. New nodes: landlords.long_term (supply to renters' rent, a13; residents' spending near home, a33), owners.elsdon (long-term supply in Elsdon falls, a29; Elsdon home values, a30; spending, a12), owners.occupant and owners.primary_residence#2 (supply_price, a35; higher price brings more nights, a36), retailers.neighbors (labor group, no premise), sellers.hotels (supply_price a9; TOT from hotels; labor; stake a14). Empty: buyers.mid_term, homebuyers, homeowners, input_suppliers.cleaning, owners.mid_term.

## Round 3 (depth 3, 11 nodes)
Only landlords.elsdon (Elsdon rents) and sellers.hotels#2 (price to return_on_capital, to asset_value with a30, to capital_stock_target in the long run with a25) got facts; the rest were empty.

## Answers
All 32 asked questions match a table statement exactly (a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a21, a22, a23, a25, a26, a27, a29, a31, a32, a33, a34, a35, a36, a37, a38, a39), p taken from the table. None was judged. Table assumptions not used anywhere: a19 (complaints lead to fines), a24 (pre-introduction bookings), a28 (rivals file complaints). a1, a2, a20, a30 were already in the seed, so they were not asked again.

## What the format could not hold
- Fines as a risk on breach: K4 fines ($2,500, $5,000) and K2 fines on platforms are not a charge on a lawful trade; only `outside` margins and `compliance` stand in for them. Where the fine goes (general fund) is lost, so a19 and a28 had no place.
- The transition rule (stays booked before 1 July completed to 30 September, later ones cancelled and refunded; a24) and the 45-night cap for July to December 2027.
- A cap on a rate per host (90 nights a year) is a `capped` on the exchange; the share of hosts above it is only carried by a premise and an unsatisfied subclass.
- K3 "replaces R1": the fee is a charge, but the removal of R1 for whole units (a34) could only be a link from lost non-primary lets to receipts, not a replacement.
- The Registry Unit deciding which reading of U1 applies (discretion over a reading) is not a fact kind.
- Stakes for actors the effects never reach (neighborhood associations) cannot be proposed; actors only appear through derived effects.
- Hosts screening guests (a27) was put as an `outside` margin on allocation_by_non_price_criteria; the margin kinds for criteria need a held price.
- Owners holding back summer lets (a16) was recorded as timing `carry_over` of quantity_supplied.
- Opposed chains with no dominance premise (home values a21 against a23; retail sales a12 against a33; TOT receipts from STRs against hotels) end `ambiguous`; the table gives no dominance premise and the section 1 figures were not enough to state one as arithmetic.
- Mixed nodes: general_fund and officials.enforcement are reported ambiguous because one class holds several opposed chains (fixed-budget displacement against new complaints).
