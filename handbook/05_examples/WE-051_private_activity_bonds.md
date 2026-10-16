# WE-051 Tax-exempt revenue bonds for private rental housing, allocated by lottery

Analyst: draft (Handbook 0.9 held-out test, corrected under 1.0)  |  Rule catalog version: 1.0  |  Status: awaiting expert review

A stylized policy in a fictional state. It resembles the use of tax-exempt "private activity" bonds for rental housing, but it is not modeled on any one state's program. It is part of a held-out test of catalog 0.9: the 0.9 changes were drawn from WE-036 to WE-045, and this case asks whether they work, as written, on a case they were not drawn from. It probes OC-8's 0.9 clause (baseline borrowing, revenue bonds, tax-exempt interest and those who make up the receipts, a borrower too small to move its loan market, the lenders' side), CR-8's 0.9 clauses (the borrowing baseline; a reading that permits a source of funds) with its 0.8 clause on contingent payers, allocation of a created right by lottery with open eligibility (EN-12's last sentence) and the question, raised in the core-only re-run of WE-039 as GAP-039-C2, of how a lottery entry is valued, SB-4 capitalization, RS-13 (added rental supply), and CR-12's notes on the three kinds of opposing chain (0.8, with 0.9's note on kind 3). The unclear provision is whether a city may pledge its general revenues if a project defaults. Effects on health, safety and the environment are outside the scope of version 1. The probabilities are illustrative; the evidence column says what a real analysis would cite. It has since been compared with a blind core-only re-run and corrected under catalog 1.0; the corrections are listed before "Gaps found", and the record of the 0.9 test in Gaps found (e) is kept as written.

## 1. Policy record

**Aldmere Rental Housing Bond Act.** Aldmere is a state of about 6.2 million people with about 120 cities; the largest are Pellmouth, Marrowby and Fennick. It has about 950,000 rental homes, with a vacancy rate of about 4% and an average rent of about $1,900 a month. About 14,000 new rental homes are completed a year, most in buildings of 50 or more units in the three largest cities. A new unit costs about $330,000 to build, of which land is about $50,000. Such projects are financed with taxable construction-to-permanent loans from banks and insurers for about 65% of cost, at about 6.5%, and equity for the rest.

**Existing rules, in force on both paths.** National law exempts from the national income tax the interest on bonds that a city issues to finance a private rental project, up to an annual volume the national law grants each state; Aldmere's is $800 million a year. Volume a state does not allocate lapses. Before the Act, Aldmere law did not allow its cities to issue bonds for private projects, so the volume lapsed each year. Aldmere's own income tax (a flat 5%) exempts interest on bonds issued by Aldmere cities and the state, and taxes interest on other states' bonds. The state's debt-limit law caps a city's general obligation debt at 5% of assessed value; conduit bonds and any pledge in support of them are not counted against the limit.

**Bond markets.** Comparable taxable project debt yields about 6.5%. The marginal buyer of exempt bonds nationally pays national tax at about 28%, so exempt revenue bonds of similar risk yield about 4.7%. Aldmere's cities and the state issue about $3.5 billion of exempt bonds a year (about $45 billion outstanding), mostly bought by Aldmere residents for the double exemption; the national exempt market issues about $400 billion a year. A project developer deducts interest from taxable income at about 25% (national) and 5% (state).

The Act was introduced on 10 January 2027, passed on 20 April 2027 and takes effect on 1 January 2028. The first lottery is in March 2028. No expiry.

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Authority to issue | `government_borrowing` (conduit revenue bonds) | New rental projects of 50 or more units | Cities that choose to sponsor | A city "may issue bonds to finance a qualified rental project. The bonds shall be special obligations of the city, payable solely from the revenues of the project and any additional security provided under section 7." Interest is exempt under the existing national and state rules. | — |
| K2 State cap and lottery | `rights_allocation` (lottery) | The national volume, $800 million a year | State Bond Commission | Complete applications by 31 January each year. Eligible: any developer of a new rental project of at least 50 units in Aldmere with site control (deed, lease or option) and a resolution of the city where it lies agreeing to issue. One application per site; fee $15,000. Allocations drawn by lottery in March, in the amount each application requests, until the cap is used. Winners must issue by 31 December or forfeit (forfeited volume lapses). Losers may apply again. | — |
| K3 Additional security (s. 7) | Rule on the bonds' security | Bonds issued under K1 | Issuing cities | "An issuing city may provide such additional security for the bonds as its council deems appropriate." | — |
| K4 Issuer fee | Fee | Bonds issued under K1 | Developers | A city may charge up to 0.5% of the bonds issued, once. | — |
| K5 Administration | Enforcement | K2 | State Bond Commission | Draws, checks of eligibility and completion; funded by application fees. | — |

Unclear provision:
- **U1, the city's general revenues (s. 7 against s. 3).** Reading U1-a: "payable solely from the revenues of the project" limits "additional security" to project-specific security (reserve funds, letters of credit, the mortgage); a city may not pledge its general revenues. Reading U1-b: "additional security" is not limited, so a city may, but need not, pledge its general revenues to cover a shortfall in debt service. The Act's history is silent; no court has ruled. Readings get no probability; where a sign depends on one, each reading's sign is reported.

**Figures.** At 65% of $330,000, the cap finances about 3,700 units a year (about 26% of counterfactual completions). The bonds save about 1.8 percentage points of interest on about $214,500 of debt per unit, about $3,900 a year, worth about $50,000 per unit over 30 years at 6.5% (about 15% of cost). The developers' association expects requests of about $2.4 billion in the first year, about three times the cap, so an entry wins about one time in three and is worth, before the cost of entering, about $17,000 per unit. If about a third of financed units are added projects that would not otherwise be built (A-7), the stock is about 1,200 units a year larger, about 1.3% of the stock after ten years; a rent about 1% to 2% lower is worth about $5,000 per unit in present value. Each year's bonds cost the national budget about 1.8% of principal a year in tax holders do not pay on interest they would otherwise have earned taxably (6.5% at 28%), less about 0.45% from developers' smaller interest deductions (1.8 points at 25%): about $11 million a year for each year's issue. The state loses about 0.33% less 0.09%: about $1.9 million a year per year's issue.

The counterfactual is Aldmere without the Act: the national volume lapses, rental projects are financed with taxable loans, and about 14,000 rental homes are completed a year.

## 2. Classification

| Component | Rothbard type | Binding? | Rule families |
|---|---|---|---|
| K1 | Binary: the national and state budgets forgo tax on the bonds' interest, a transfer to borrowers and holders (CR-1, operation 2 for developers: a cheaper option of borrowing). The borrowing is the developers' in substance; the city is a conduit. | Yes, for projects that win (A-1). | OC-8 (0.9, 1.0), CR-8 (0.9: borrowing baseline), CR-6 (1.0: small effects are signed), CR-5c, CR-7b, SB-4, RS-13 (1.0), TX-1, OC-1 |
| K2 | Binary: a created right (an allocation) given by lottery among open applicants | Yes: requests exceed the cap (A-2). | EN-12 (open eligibility), CR-7a, CR-7c, CR-10c, CR-8c, CR-6, RS-5, RS-8, RS-15 (city resolutions) |
| K3 | A permission to the city | Under U1-b only | CR-8 (0.8: contingent payers; 0.9: a reading that permits) |
| K4 | Binary: a fee for issuing, paid by developers | Yes | CR-8b |
| K5 | Binary: funded from the program's own fees | Yes | OC-3 (own revenue), OC-1 (1.0: receipts into the same budget), CR-8 (1.0), CR-8c |

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `developers.winners` | Developers whose projects win an allocation | Borrow at about 4.7% instead of 6.5%. |
| `lottery.entrants` | All developers who apply | Pay to enter; one chance in about three. |
| `developers.rental` | All developers of rental projects | May wait for a draw; face rivals with cheaper money. |
| `developers.other` | Builders of unsubsidized rental, condominium and smaller projects | Compete with winners for sites and builders. |
| `landowners.qualifying_sites` | Owners of sites where a 50-unit rental project can be built | Site control is a condition of entry. |
| `renters` (`buyers.current`, `buyers.prospective`) | Tenants of rental homes | More rental homes in the long run. |
| `landlords.existing` | Owners of existing rental buildings | More competing supply. |
| `bondholders` | Buyers of the bonds | A new exempt asset. |
| `lenders.taxable` | Banks and insurers who would have made the project loans | Lose those loans to the bonds. |
| `borrowers.taxable` | Other borrowers in the taxable loan market | Face a market with less project borrowing and less lending by those who buy the bonds. |
| `issuers.aldmere` | Aldmere cities and the state as issuers of their own exempt bonds | Compete with the new bonds for in-state buyers. |
| `holders.aldmere_bonds` | Holders of existing Aldmere exempt bonds | Their bonds compete with new supply. |
| `issuers.national_exempt`, `holders.national_exempt` | Other issuers and holders of exempt bonds nationally | The new bonds add about 0.2% to national exempt issuance. |
| `builders.other_construction` | Builders of owner-occupied and commercial buildings | Compete with rental projects for sites and inputs. |
| `cities.issuing` | Cities that sponsor and issue | Receive fees; under U1-b may pledge general revenues, which their own lenders may count. |
| `taxpayers.city` | Taxpayers of issuing cities and recipients of city spending | Under U1-b, contingent payers. |
| `taxpayers.national`, `taxpayers.state` | Those who make up national and state receipts | Receipts fall. |
| `input_suppliers` | Construction labor and materials in Aldmere | More rental building in the long run. |
| `construction_workers` | Workers on building sites | As above. |
| `intermediaries` | Underwriters, bond counsel, trustees, rating agencies | A new line of work. |
| `officials.enforcement` | State Bond Commission | Runs the lottery. |
| Interest groups | Developers, cities, housing groups | Stakes in the cap and the rules. |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | `developers.winners` | `interest_rate` (on their projects' debt) | decrease | short to long (from 2028) | CR-1, CR-5c, OC-8, CR-7b | A-1, A-2 |
| C-2 | `cities.issuing`, `bondholders` | `quantity_traded` (tax-exempt rental housing bonds issued) | increase | short to long | CR-1, CR-12 (0.9: an activity that exists only under the policy) | A-2 |
| C-3 | `developers.winners` | `asset_value` (projects with an allocation) | increase | short (at each draw) | SB-4, CR-7c, CR-10c, CR-12e (arithmetic) | A-1, A-2, A-3 |

C-1 is the purpose: winners borrow at about 4.7% instead of about 6.5%, because holders accept a lower yield on interest they need not pay tax on (A-1). Under U1-b a city's pledge makes some bonds safer and so cheaper still; the sign is the same under both readings. C-2 is an activity that exists only under the Act, signed `increase` against none (CR-12, 0.9). The allocation is a right the Act creates; its value, the present value of the interest saved, is captured by whoever receives it at the draw (C-3; CR-7c), to the extent it is not already paid away in entering (section 5) or to landowners (C-21). For a winner three chains oppose it: the issuer fee (about $1,100 a unit at 0.5%), the other costs of issuing (about $4,000 a unit on A-27; C-34) and the fall in rents the project will earn (about $5,000 a unit); against about $50,000 a unit, arithmetic on the case's figures gives dominance (CR-12e).

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-4 | `lottery.entrants` | `compliance_cost` (application fees, site options, design and legal work, city resolutions) | increase | short (each year from 2028) | EN-12 (open eligibility), CR-7a, CR-8c, OC-2 | A-4 |
| C-5 | `lottery.entrants` | `reclassification` (large projects split into several applications; condominium or smaller projects redesigned as 50-unit rentals) | increase | short to medium | RS-5, SB-5, EN-12 | A-5 |
| C-6 | `developers.rental` | `investment_target` (rental homes started, 2027) | decrease | short (2027) | RS-8, CR-10a | A-6 |
| C-37 | `lenders.taxable`, `developers.rental` | `quantity_traded` (taxable loans closed for rental projects, 2027) | decrease | short (2027) | RS-8, CR-10a, CR-4 | A-6 |
| C-7 | `developers.rental` | `investment_target` (rental homes started, 2028) | ambiguous | short (2028) | RS-8, CR-10a, CR-12b, CR-12 (0.9: kind 3) | A-6, A-7, A-8 |
| C-8 | `developers.rental` | `investment_target` (rental homes started, 2029 to 2032) | ambiguous | medium | CR-4, CR-10a, CR-12b, CR-12 (0.8: kind 2) | A-7, A-8 |
| C-9 | `developers.rental` | `investment_target` (rental homes started a year, after 2032) | increase | long | CR-4, RS-13 (1.0), CR-12e (response argument, bounding all construction that draws on the same sites and inputs), CR-12 (0.9: partial response, A-9; 1.0: what the response argument needs) | A-1, A-2, A-7, A-9, A-10 |
| C-10 | `developers.other` | `investment_target` (unsubsidized rental, condominium and smaller projects) | decrease | medium to long | CR-9, CR-6, CR-4 | A-7, A-10 |
| C-11 | Developers, cities, housing groups | `lobbying_effort` (of city councils, for sponsorship resolutions) | increase | medium | RS-7, RS-15, CR-12 (0.9: an activity that exists only under the policy) | A-11 |
| C-46 | Developers, housing groups | `lobbying_effort` (state and national: to keep the program, enlarge the cap, widen eligibility) | ambiguous | medium | RS-7 (1.0: Unless), CR-4 (1.0: lobbying, generally), CR-12b | A-11, A-29 |
| C-12 | `lenders.taxable` | `quantity_traded` (taxable loans to rental projects) | decrease | short to long | CR-5 (0.7: a better offer elsewhere), CR-9, OC-4 (Unless) | A-1, A-12 |
| C-13 | `cities.issuing` | `non_tax_receipts` (issuer fees) | increase | short to long | CR-8b | A-2, A-13 |
| C-14 | `officials.enforcement` (State Bond Commission) | `non_tax_receipts` (application fees) | increase | short to long | CR-8b | A-4 |
| C-15 | `lottery.entrants` | `allocation_by_non_price_criteria` (which projects cities agree to sponsor) | increase | short to medium | RS-15, CR-6 | A-24 |

**Entering the lottery (C-4, C-5, C-14, C-15; EN-12, open eligibility).** The allocation is worth about $50,000 a unit and is given by chance among complete applications, for a $15,000 fee. EN-12's last sentence: a share allocated by lottery with open eligibility draws entry to qualify. Every developer with a qualifying site gains by entering while an entry's expected value (about one chance in three of the allocation) exceeds the cost of entering (A-4). Entries rise until, for the marginal site, they are equal (CR-7a, applied to entries). The cost of entering is partly used up (design, legal work, city process, the fee's use in administration: CR-8c, C-4) and partly a payment to landowners for site options (a transfer: C-21). Some developers split large projects to hold several entries, or redesign projects to qualify (C-5; RS-5; A-5). A city resolution is a condition of entry and is granted at the council's discretion, so sponsorship is rationed by non-price criteria and lobbied for (C-15, C-11; RS-15; A-24). Lobbying councils for resolutions exists only under the Act (C-11). Lobbying at the state and national level to keep or enlarge the program is another matter: CR-4's 1.0 clause signs it against the contest the counterfactual path would have had, and without the Act developers and housing groups would have kept campaigning for authority to use the lapsing volume (A-29, p = 0.6). For a class that lobbies in both worlds, on different questions, the sign is `ambiguous` (C-46; RS-7, 1.0). Application fees are the Commission's receipts (C-14), which fund its work (C-33).

**How a lottery entry is valued (GAP-039-C2).** An entry is a chance at a created right. Its value is the expected yield of the right, weighted by the chance of winning (CR-10c), less the cost of entering, and it is captured by whoever holds what entry requires, here a qualifying site (CR-7c). With open eligibility, the chance of winning is itself set by entry, so the entry's value is bid toward the cost of entering (CR-7a). No new rule is needed; but CR-7c's probability clause speaks of the probability that a measure passes, not of the odds of a draw, and EN-12 does not say where the value of an entry settles (Gaps found, b1, c2).

**Construction starts per window (C-6 to C-9).** From April 2027 developers know that projects which start in 2028 or later can apply, and those which start in 2027 cannot. Some who would have closed taxable financing in late 2027 wait for the first draw (C-6; RS-8; A-6), so taxable loans closed in 2027 fall too (C-37). In each later year two derived chains meet: (+) projects viable only at the lower rate start when they win (A-7); (−) developers who lose a draw hold their project for the next draw rather than proceed with taxable financing (A-8, p = 0.55). The second chain needs a premise the case does not settle; since p ≥ 0.5, the combined sign is `ambiguous` (C-8; CR-12, 0.8, kind 2). In 2028 the projects held back from 2027 add a (+) chain; the per-year chain is itself ambiguous, so it is a kind 3 chain (CR-12, 0.9), and no dominance premise covers the (+) chain against both of its directions: `ambiguous` (C-7). In the long run the pool of waiting projects stops growing, and a constant delay does not reduce the flow, so the (−) chain lapses. The (+) chain is then opposed only by the response of other builders (C-10): subsidized projects bid up sites and construction inputs, and some unsubsidized projects are not built. That response cannot reverse the added building that causes it, since input prices rise only because more is built (CR-12e). CR-12's 1.0 clause asks which total the argument bounds and on what cost premise. The total is all construction that draws on the same sites and inputs: rental projects, subsidized and not, and other building (C-40), which is crowded out too (RS-13, 1.0). The crowding out stops once yields are equal, and it cannot take that total below its counterfactual level as long as cost per unit built does not fall as other building contracts: here it rises, since sites and inputs cannot expand at unchanged cost (A-10). Rental starts are a part of that total, and the crowding out falls partly on other building, so rental starts are not taken below their counterfactual level either. To report `increase` rather than an increase or no change, the response must be partial. CR-12's 1.0 clause says that, where the response is a contraction by rivals, partial means their inputs can be shifted to other uses only gradually; that holds during the transition, but in the long run the rivals' inputs have moved, and partiality rests on the inputs' supply: sites and construction inputs can expand somewhat over the long horizon, so their prices do not rise far enough to crowd out every added project (A-9). Note that here "partial" requires that the inputs' supply *can* expand (Gaps found, b2). Holding for later draws (A-8) is a second response to the same change, which the argument does not cover (CR-12, 1.0); it lapses in the long run, as above. So starts a year rise in the long run (C-9).

**Lenders who lose the loans (C-12).** For projects that would have been built anyway (A-12), the bonds replace bank and insurer loans. Those lenders lose the business to a better offer the Act creates (CR-5, 0.7; OC-4, Unless), and lend elsewhere. This is a decrease in one line of their lending, not a sign on lenders as a class (OC-8, 0.9: lenders).

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-38 | `renters` | `price_paid` (rents, 2029) | increase | short (2029) | RS-13 (withdrawn supply), RS-8, CR-6, CR-10b | new and existing rental homes: `same_market_other_segment`, close | A-6, A-14, A-25 |
| C-16 | `renters` | `price_paid` (rents, 2030 to 2032) | ambiguous | medium | RS-13, CR-6, CR-12 (0.9: kind 3) | new and existing rental homes: `same_market_other_segment`, close | A-7, A-8, A-14, A-25 |
| C-17 | `renters` | `price_paid` (rents; not counting effects through proximity) | decrease | long | RS-13 (1.0), CR-6, CR-12e (response argument), CR-12 (0.9: partial response; Tier C against Tier B; 1.0: what the response argument needs) | as C-16 | A-1, A-2, A-7, A-9, A-10, A-14 |
| C-18 | `renters` | `price_paid` (rents) | ambiguous | long | as C-17; CR-9 (`proximity`; Tier C), CR-12b, CR-12 (0.9: Tier C against Tier B) | as C-16; new buildings and nearby blocks: `proximity` | A-1, A-2, A-7, A-9, A-10, A-14, A-15 |
| C-19 | `landlords.existing` | `net_price_received` (rents; not counting effects through proximity) | decrease | long | RS-13, CR-8b, CR-12 (0.9, 1.0) | as C-16 | A-1, A-2, A-7, A-9, A-10, A-14 |
| C-20 | `landlords.existing` | `asset_value` (existing rental buildings; not counting effects through proximity) | decrease | short (from April 2027) | SB-4, CR-7c, CR-10c, CR-12e (dominance, A-16), CR-12 (0.7: an underivable chain) | as C-16 | A-7, A-9, A-10, A-14, A-16 |
| C-35 | `landlords.existing` | `net_price_received` (rents) | ambiguous | long | as C-19; CR-9 (`proximity`; Tier C), CR-12b, CR-12 (0.9) | as C-18 | A-7, A-9, A-14, A-15 |
| C-36 | `landlords.existing` | `asset_value` (existing rental buildings) | ambiguous | short | as C-20; CR-9 (`proximity`; Tier C), CR-12b, CR-12 (0.9) | as C-18 | A-7, A-9, A-14, A-15, A-16 |
| C-21 | `landowners.qualifying_sites` | `asset_value` (sites for 50-unit rental projects) | increase | short (from April 2027) | SB-4, CR-7c, CR-10c, EN-12, CR-7a, CR-12e (dominance, A-17) | sites `input_to` rental projects | A-4, A-17 |
| C-22 | `renters`, `landlords.existing` | `capital_stock_target` (rental homes in Aldmere) | increase | long | RS-13, CR-10b, CR-12e, CR-12 (0.9: partial response; 1.0) | — | A-1, A-2, A-7, A-9, A-10 |
| C-23 | `input_suppliers` | `price_paid` (construction labor and materials), `quantity_traded` | at_least_one_increase | long | CR-9, CR-6 (0.9: splitting a shift) | labor and materials `input_to` rental projects | A-7, A-9 |
| C-24 | `construction_workers` | `employment`, `hours_worked` | at_least_one_increase | long | OC-5, CR-9 | labor `input_to` building | A-7, A-9, A-18 |
| C-39 | `developers.rental`, `developers.other` | `price_paid` (sites for building in Aldmere) | increase | medium to long | CR-9, CR-6, RS-13 (1.0), EN-12 | sites `input_to` building | A-4, A-7, A-10 |
| C-40 | `builders.other_construction` | `quantity_traded` (owner-occupied and commercial buildings started) | decrease | long | CR-9, CR-6, CR-4c, CR-8a, RS-13 (1.0: crowding out of other output) | sites, labor and materials `input_to` building | A-7, A-9, A-10 |
| C-25 | `issuers.aldmere` | `interest_rate` (on Aldmere cities' and the state's own exempt bonds) | increase | medium | OC-8 (1.0: segments), RS-13, CR-6, CR-7a | Aldmere-exempt bonds: `same_market_other_segment`, partial | A-19 |
| C-26 | `holders.aldmere_bonds` | `asset_value` (existing Aldmere exempt bonds) | decrease | short (from April 2027) | OC-8 (1.0: segments), SB-4, CR-7c, CR-10c | as C-25 | A-19 |
| C-41 | `issuers.national_exempt` | `interest_rate` (exempt bonds nationally) | increase | medium | OC-8 (1.0: small borrowers are signed), CR-6 (1.0: small effects are signed), RS-13, CR-7a | exempt bonds nationally: `same_market_other_segment`, partial | A-2, A-28 |
| C-42 | `holders.national_exempt` | `asset_value` (existing exempt bonds nationally) | decrease | short (from April 2027) | OC-8 (1.0), CR-6 (1.0), CR-7c, CR-10c | as C-41 | A-2, A-28 |
| C-43 | `borrowers.taxable` | `interest_rate` (taxable loans) | ambiguous | medium | CR-8 (0.9: the borrowing baseline), OC-8 (0.9, 1.0), CR-6 (1.0: small effects are signed), CR-12b | taxable and exempt debt: `substitute`, partial | A-2, A-12 |
| C-27 | `taxpayers.national` (national budget) | `tax_revenue` (national income tax) | decrease | short to long | OC-8 (0.9: tax-exempt interest; 1.0: interest deductions), CR-8 (0.9), CR-8b, CR-12e (arithmetic, A-20) | — | A-1, A-2, A-20 |
| C-28 | `taxpayers.national`, recipients of national spending, future national taxpayers | `resources_available_other_uses` | at_least_one_decrease | short to long | OC-8 (0.9), OC-1 (Who pays), CR-8 (0.7: payers from the general budget) | — | A-1, A-2, A-20 |
| C-29 | `taxpayers.state` (state budget) | `tax_revenue` (Aldmere income tax) | decrease | short to long | OC-8 (0.9; 1.0: interest deductions), CR-8b, CR-12e (arithmetic, A-20) | — | A-1, A-2, A-20 |
| C-30 | `taxpayers.state`, recipients of state spending, future state taxpayers | `resources_available_other_uses` | at_least_one_decrease | short to long | OC-8 (0.9), OC-1 (Who pays) | — | A-1, A-2, A-20 |
| C-31 | `taxpayers.city`, recipients of city spending (cities that pledge) | `resources_available_other_uses` (covering defaulted debt service) | U1-a: no_change; U1-b: at_least_one_decrease | long | CR-8 (0.8: contingent payers; 0.9: a reading that permits), OC-8 (0.9: revenue bonds), CR-12 (0.8: kind 2) | pledge: `contract` | A-21, A-22 |
| C-44 | `cities.issuing` (pledging cities) | `interest_rate` (on the city's own general obligation debt) | U1-a: no_change; U1-b: increase | medium to long | CR-6, CR-7a, CR-8 (0.9: a reading that permits) | pledge: `contract`; the city's own debt priced by the same lenders | A-21, A-26 |
| C-32 | `intermediaries` | `quantity_traded` (underwriting, bond counsel, trustee and rating services) | increase | short to long | CR-9, CR-12 (0.9: an activity that exists only under the policy) | services `input_to` bond issues | A-2 |
| C-45 | `officials.enforcement` (State Bond Commission) | `fund_balance` (application fees less the cost of the draws) | ambiguous | short to long | CR-8 (1.0: receipts into the same budget), OC-1 (1.0), CR-12b | — | A-4 |

**Rents (C-16 to C-19, C-22, C-38).** RS-13: added supply in the rental market lowers rents against the counterfactual, if renters do not absorb it at an unchanged rent (A-14); withdrawn supply raises them. The added supply is only the projects that would not otherwise be built (A-7); the rest of the bonds replace taxable loans for projects built anyway and add nothing to supply (CR-8, 0.9: the borrowing baseline applies to the homes as well as the loans). Rents follow the stock, which follows completions about two years after starts (A-25). Completions in 2029 come from the starts of 2027, which fall (C-6): fewer homes than on the counterfactual path, so rents in 2029 rise (C-38). From 2030 completions follow the starts of 2028 onward, which are ambiguous (C-7, C-8), on top of a stock already short from 2027: a kind 3 chain, so rents in 2030 to 2032 are `ambiguous` (C-16). In the long run the stock is larger (C-22), the crowding out of other builders being a partial response that cannot reverse it (CR-12e; A-9). For a price, CR-12's 1.0 clause asks for a cost premise: rents could stay up only if cost per unit built fell as other building contracted, and it rises instead (A-10). So rents fall (C-17) and landlords receive less (C-19; CR-8b).

**A Tier C chain against the rents (C-18, C-35, C-36).** New buildings bring shops and services that may make nearby blocks more desirable (A-15): a `proximity` relation, Tier C (CR-9, 0.7). Under CR-12's 0.9 rule, the Tier B signs stand, qualified "not counting effects through proximity" (C-17, C-19, C-20), and the combined signs at Tier C are `ambiguous` (C-18, C-35, C-36), since no premise compares the two.

**Existing rental buildings (C-20).** Their value reflects expected rents (CR-10c), so the lasting rent fall is capitalized from passage (CR-7c), borne by those who own them then. The medium-run delay in building is temporary and the long-run addition lasting; A-16 states that the lasting addition dominates in the buildings' value. A suspected opposing chain, that the program makes rent control less likely and so raises buildings' values, cannot be derived: it needs a premise about how political decisions respond to housing outcomes, which TS-4 records as not derivable. Under CR-12's 0.7 and 0.8 notes (kind 1) it is a Tier C note, not a chain, and the derived sign stands.

**Qualifying sites (C-21).** Site control is required to enter, and the stock of sites zoned for 50-unit rentals is fixed in the short run, so the expected value of an entry is capitalized into those sites (SB-4, CR-7c, CR-10c) and paid as higher option and sale prices. Two chains meet: (+) the entry's expected value, about $17,000 a unit at one-in-three odds, less the used-up cost of entering; (−) the lower rents a site will earn, about $5,000 a unit in present value. A-17 (arithmetic on the case's figures, with an empirical premise on the rent effect) gives dominance: `increase`. Owners at passage capture it. SB-4's "later buyers pay it" compares with the capitalized price (CR-12, 1.0: the baseline of patterns); against the no-Act path, later buyers pay more for a site and hold a chance at an allocation that the site carries, so their position is not signed. Developers in general pay more for sites (C-39): entrants bid for qualifying sites from passage (A-4), and in the medium and long run subsidized projects add to the demand for sites, which cannot expand at unchanged cost (A-10; CR-9, CR-6).

**Inputs and workers (C-23, C-24, C-40).** More building in the long run shifts demand for construction labor and materials. How the shift divides between price and quantity needs a premise on the inputs' supply (CR-6, 0.9); A-9 says only that they can expand partly, so price and quantity are recorded as a group (C-23). Workers: employment or hours (C-24; A-18). RS-13's 1.0 clause: the added rental building draws sites and inputs from other uses, so other building, owner-occupied and commercial, is crowded out too (C-40; CR-9, CR-8a, A-10).

**The bond market (C-25, C-26; OC-8, 0.9).** OC-8's clauses, one at a time:
- *Baseline borrowing.* Most bonds finance projects that would have been built with taxable loans (A-12). Against that baseline, the Act moves borrowing from the taxable to the exempt market; only the added projects add borrowing. In the taxable market, project borrowing falls, but so does the lending of those who buy the bonds instead of taxable assets: the effect on other borrowers' taxable rates is `ambiguous` without a premise on the difference (CR-8, 0.9). $800 million a year is small against the national loan market, but CR-6's and OC-8's 1.0 clauses require a small effect to be recorded by its sign: `ambiguous` (C-43).
- *A borrower too small to move its loan market.* Against the counterfactual the national volume lapses, so the bonds are added exempt supply, about 0.2% of national exempt issuance. OC-8's 1.0 clause signs the small-borrower case: if the national exempt market does not absorb the added bonds at an unchanged yield (A-28), other exempt issuers pay slightly more (C-41) and holders of existing exempt bonds lose slightly from passage (C-42); the size goes in the evidence. The effect is larger in the market the state exemption creates (OC-8, 1.0: segments): Aldmere residents get the double exemption only on Aldmere bonds, and the new bonds add about 23% to in-state exempt issuance. If in-state buyers are the marginal buyers of Aldmere bonds (A-19), the added supply lowers their price (RS-13 in the bond market): Aldmere's cities and the state pay more on their own exempt borrowing (C-25), and holders of existing Aldmere bonds lose value from passage (C-26; CR-7c). Under U1-b, cities that pledge take on contingent liabilities. If their lenders count a pledge in the city's credit risk, although the debt limit does not (A-26, p = 0.7), the rate on the pledging city's own general obligation debt rises (C-44; under U1-a, `no_change`), and so does C-25 through those cities' exempt bonds (same sign).
- *Revenue bonds.* Repaid from rents only, so no later taxes, except for a shortfall where a city has pledged (C-31).
- *Tax-exempt interest.* The receipts forgone are a cost to whoever makes them up (C-27 to C-30). The national budget loses the tax holders would have paid on taxable interest and gains on developers' smaller interest deductions; the first is far larger (A-20, arithmetic: about 1.8% against 0.45% of principal a year). The payers are groups (OC-1, Who pays). Aldmere's income tax loses the same way, on in-state holders (C-29, C-30).
- *Lenders.* Bondholders would have lent elsewhere: no sign against the counterfactual. The lenders who lose the project loans are recorded as a line of business (C-12); holders of existing Aldmere bonds are recorded as asset holders (C-26). Neither is "the lenders' side" of the new borrowing.
- *A legal debt limit.* Not applicable: conduit bonds and pledges are not counted against the city limit.

**The city's general revenues (C-31; CR-8, 0.9 and 0.8).** Under U1-b a city may pledge its general revenues but need not. CR-8's 0.9 clause on a reading that permits: record the payers under that reading as a group that includes the permitted source. CR-8's 0.8 clause on contingent payers: the general fund pays only if a pledged project falls short, so the sign needs premises on the contingency. Here two are needed: that some cities pledge (A-21, p = 0.6) and that some pledged projects fall short during the bonds' 30-year life (A-22, p = 0.6). Under U1-b the payers are city taxpayers or recipients of city spending (a group, `at_least_one_decrease`). Under U1-a no city may pledge; the derived sign is `no_change`. A city might still cover a default without a legal duty, to protect its name with lenders: a chain the rules derive (CR-2 applied to the council) but whose premise is below the cut-off (A-23, p = 0.25), so under CR-12's 0.8 kind 2 note the derived sign stands and the chain is recorded in section 10.

**Intermediaries (C-32).** Each issue needs underwriting, counsel, a trustee and often a rating: a new line of work (CR-12, 0.9).

**The Commission's account (C-45).** Application fees (C-14) go into the budget that pays for the draws (C-33). CR-8's and OC-1's 1.0 clauses record both items and the net. The record gives the fee but not the number of applications or the Commission's costs, so the net is `ambiguous` (C-45).

Stopping points: spending by construction workers and by the payers of the national budget (depth 3, diffuse); owner-occupied home prices, reached by two opposing chains (lower rents pull some buyers into renting; higher site and input prices raise the cost of new homes), not followed (depth 3), though the quantity of other building is recorded (C-40); retailers near new buildings (Tier C, proximity, not followed beyond C-18).

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `developers.rental`, `investment_target`, 2028 | Projects held from 2027 start (A-6). | — | The per-year chain is itself ambiguous (kind 3, CR-12, 0.9); no premise covers it in both directions. | **ambiguous** (C-7) |
| `developers.rental`, `investment_target`, 2029 to 2032 | Added projects (A-7). | Losers wait for the next draw (A-8, p = 0.55; kind 2). | None | **ambiguous** (C-8) |
| `developers.rental`, `investment_target`, after 2032 | Added projects (A-7). | Crowding out of other builders (a response). | CR-12e, bounding all construction on the same sites and inputs, with rising cost (A-10) and partial with A-9 | **increase** (C-9); `capital_stock_target` likewise (C-22) |
| `renters`, `price_paid`, 2029 | Fewer completions from the 2027 dip in starts (A-6, A-25). | — | — | **increase** (C-38) |
| `renters`, `price_paid`, 2030 to 2032 | — | — | Follows the stock, a kind 3 chain. | **ambiguous** (C-16) |
| `renters`, `price_paid`, long | Proximity amenity (Tier C, A-15). | Added supply (RS-13). | None for the Tier C chain | Tier B: **decrease** (C-17). Tier C: **ambiguous** (C-18). Landlords' receipts and values likewise (C-19, C-20; C-35, C-36). |
| `landlords.existing`, `asset_value`, short | Underivable: less risk of rent control (kind 1, Tier C note only). | Capitalized lower rents. | A-16 for the temporary delay against the lasting addition | Tier B: **decrease** (C-20). |
| `landowners.qualifying_sites`, `asset_value`, short | Expected value of entries. | Lower rents. | A-17 (arithmetic on the figures) | **increase** (C-21) |
| `taxpayers.national`, `tax_revenue`, short to long | Smaller interest deductions by developers. | Tax not paid on exempt interest. | A-20 (arithmetic) | **decrease** (C-27); the state likewise (C-29) |
| `taxpayers.city`, `resources_available_other_uses`, long | — | U1-b: covering defaulted debt service (A-21, A-22). Under U1-a, a voluntary bailout (A-23, p = 0.25; kind 2 below the cut-off). | — | U1-a: **no_change**; U1-b: **at_least_one_decrease** (C-31) |
| `issuers.aldmere`, `interest_rate`, medium | Added in-state supply (A-19); under U1-b, contingent liabilities (A-26). | — | — | **increase** (C-25) |
| `borrowers.taxable`, `interest_rate`, medium | Bond buyers lend less in the taxable market. | Projects borrow less in the taxable market. | None | **ambiguous** (C-43) |
| Developers and housing groups, `lobbying_effort` on the program, medium | Lobbying to keep and enlarge the program. | Lobbying on the counterfactual path for authority to use the volume (A-29). | None | **ambiguous** (C-46) |
| `officials.enforcement`, `fund_balance`, short to long | Application fees (C-14). | Cost of the draws (C-33). | None (the record gives no count of applications) | **ambiguous** (C-45) |

## 8. Time structure

- **April 2027 to March 2028: announcement.** Sites, existing rental buildings, existing Aldmere bonds and, slightly, existing exempt bonds nationally revalue at passage (C-21, C-20, C-26, C-42). Some developers hold projects for the first draw (C-6), closing fewer taxable loans (C-37). Developers secure site options and city resolutions for January 2028 (C-4, C-15).
- **2028: the first draw.** Projects held from 2027 start, and the per-year chains begin (C-7). Winners must issue by 31 December, so issues bunch late in the year: a path note, since without the Act no such bonds are issued at all.
- **2029: the 2027 dip completes.** Completions reflect the 2027 starts (A-25), so rents are higher than on the counterfactual path (C-38).
- **2029 to 2032: the waiting pool.** Losers may wait for later draws (C-8), so starts, and rents in 2030 to 2032, are ambiguous (C-16). The in-state bond market absorbs about $800 million a year more (C-25).
- **After 2032: steady state.** The pool of waiting projects stops growing; added projects raise the flow of starts and the stock (C-9, C-22), lowering rents (C-17). Tax receipts forgone cumulate with each year's issue, about $11 million a year nationally and $1.9 million in the state for each vintage, for 30 years (C-27, C-29).
- **Defaults.** Shortfalls, if any, come years after issue, when rents fall short of debt service; under U1-b they then fall on pledging cities' general funds (C-31).
- **The cap is fixed in money (TS-3).** As construction costs rise, $800 million finances fewer units each year; the program's effects shrink in units unless the national volume is raised.

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-4 | `lottery.entrants` | `compliance_cost` | increase | Design, legal and city-process work and fees spent to hold a chance at an allocation; most entries lose. | EN-12, CR-8c, OC-2 |
| C-33 | `officials.enforcement` (State Bond Commission) | `enforcement_cost` | increase | Staff and systems for the draws and checks, paid from application fees (own revenue), so not from general taxpayers. | OC-3, CR-8c |
| C-34 | `developers.winners` | `compliance_cost` (issuance costs: underwriting, counsel, trustee, rating, issuer fee) | increase | Costs of issuing bonds beyond those of arranging a bank loan, about 1.5% to 2% of each issue in comparable programs (A-27). | CR-8c |
| C-40 | `builders.other_construction` | `quantity_traded` (other buildings started) | decrease | Owner-occupied and commercial building that the added rental projects' sites and inputs would otherwise have served. | CR-8a, RS-13 (1.0) |
| C-28 | `taxpayers.national` (group) | `resources_available_other_uses` | at_least_one_decrease | What those who make up the national receipts would have done with them. | OC-1, OC-8 |
| C-30 | `taxpayers.state` (group) | `resources_available_other_uses` | at_least_one_decrease | The same for the state. | OC-1, OC-8 |

Transfers, both sides: interest saved by winners (C-1, C-3) against receipts forgone and their payers (C-27 to C-30); issuer fees paid (part of C-34) and received (C-13); application fees paid (C-4) and received (C-14); site options paid (part of C-4) and received (C-21); site prices paid by developers (C-39) and received by site owners (C-21). The Commission's fees and costs are two items of one budget, with the net recorded separately (C-14, C-33, C-45). The intermediaries' fees (C-34) are receipts to them (C-32), for work that is used up (CR-8c).

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | Buyers accept yields on the bonds well below comparable taxable yields (about 4.7% against 6.5%) because the interest is exempt. | other | 0.9 | Yields on comparable exempt revenue bonds. | C-1, C-3 and every consequence that follows shrink toward nothing. |
| A-2 | Developers apply, cities sponsor and issue, and the cap is used. | other | 0.9 | Developers' survey: about $2.4 billion of requests. | Consequences scale down with the volume issued. |
| A-3 | Holders expect the exemption on issued bonds to last for their term. | expectations | 0.85 | No retroactive change in the national rule's history. | C-3 is smaller. |
| A-4 | For many qualifying sites, an entry's expected value exceeds the cost of entering. | other | 0.85 | About $17,000 a unit at one-in-three odds, against entry costs of about $1,000 to $2,000 a unit. | C-4, C-14 and the (+) chain of C-21 shrink; C-39 loses its medium-run chain. |
| A-5 | Splitting or redesigning projects to qualify costs less than the extra entries are worth for some developers. | other | 0.6 | One application per site; lot splits; redesign costs. | C-5 is not reported. |
| A-6 | Some developers who would have closed taxable financing in 2027 wait for the first draw. | expectations | 0.75 | The allocation is worth about 15% of cost. | C-6, C-37, C-38 and the (+) chain of C-7 are not reported. |
| A-7 | Some projects are viable only at the lower rate and are built only if they win. | other | 0.75 | Projects' returns near the hurdle at 6.5%. | No added supply: C-9, C-17, C-19 to C-24, C-39 (long run) and C-40 are not reported; C-16 has no basis. |
| A-8 | Some developers who lose a draw hold their project for the next one rather than proceed with taxable financing. | other | 0.55 | Carrying costs of land options against the expected value of a later entry. | C-7 and C-8 become `increase`; C-16 follows them. |
| A-9 | Over the long horizon, sites and construction inputs can expand partly, so higher input prices do not crowd out every added project (the crowding-out response is partial). | other | 0.7 | Rezoning pace; construction labor inflows. | C-9, C-17, C-19, C-20, C-22 to C-24 are an increase (decrease) or no change, not reported; C-40 holds. |
| A-10 | In the medium and long run, sites and inputs cannot expand at unchanged cost, so their prices rise and some unsubsidized projects are not built. | other | 0.7 | Construction cost indexes; site scarcity in the three largest cities. | C-10, C-39 and C-40 are not reported; the response argument for C-9, C-17, C-19, C-20 and C-22 loses its cost premise, and they become an increase (decrease) or no change. |
| A-11 | Developers, cities and housing groups can organize at a cost below their stake. | other | 0.85 | Existing associations. | C-11 is not reported. |
| A-12 | Some winners' projects would have been financed with bank or insurer loans. | counterfactual_trend | 0.8 | Open eligibility: projects already planned apply. | C-12 is not reported; more of the bonds are added borrowing, and C-43 loses its (−) chain. |
| A-13 | Cities that sponsor charge the issuer fee. | other | 0.8 | Fees in other conduit programs. | C-13 is not reported. |
| A-14 | Renters do not absorb added units at an unchanged rent. | substitutability | 0.8 | Vacancy at 4%; local rent responses to new supply. | C-17, C-19, C-20 and C-38 are not reported. |
| A-15 | New buildings bring shops and services that make nearby blocks more desirable to renters. | other | 0.55 | Retail openings near new buildings. | C-18, C-35, C-36 become `decrease` at Tier C. |
| A-16 | In the value of existing rental buildings, the lasting addition to the stock dominates the temporary delay in building. | other | 0.65 | The delay lasts a few years; the addition lasts for the buildings' lives. | C-20 becomes `ambiguous`. |
| A-17 | An entry's expected value per unit (about $17,000) exceeds the present value of the rent fall per unit (about $5,000). | other | 0.75 | Section 1 figures; the rent effect is an empirical estimate. | C-21 becomes `ambiguous`. |
| A-18 | Construction employers adjust labor to volume. | alternative_uses | 0.75 | Labor per unit built. | C-24 is not reported. |
| A-19 | The market for Aldmere exempt bonds is partly segmented: in-state buyers are marginal, so added supply raises in-state yields. | other | 0.6 | Share held in-state; spreads between Aldmere and other states' bonds. | C-25 and C-26 hold only as the small national effect (C-41, C-42, on A-28). |
| A-20 | Net national and state receipts fall: tax forgone on exempt interest exceeds tax gained on developers' smaller deductions. | other | 0.85 | About 1.8% against 0.45% of principal (national), 0.33% against 0.09% (state). | C-27 to C-30 become `ambiguous`. |
| A-21 | Under U1-b, some cities pledge general revenues. | other | 0.6 | Cities compete for projects; a pledge lowers yields. | C-31 under U1-b is not reported. |
| A-22 | Some pledged projects fall short of debt service during the bonds' life. | other | 0.6 | Default rates on comparable revenue bonds over 30 years. | C-31 under U1-b is not reported. |
| A-23 | Under U1-a, a city would cover a defaulted project's debt service without a legal duty. | expectations | 0.25 | No such practice in Aldmere; councils' budgets are tight. | Below the cut-off. If true, C-31 under U1-a is `at_least_one_decrease` (CR-12, 0.8, kind 2). |
| A-24 | Cities choose at their discretion which projects to sponsor. | other | 0.7 | The Act sets no criteria for resolutions. | C-15 is not reported. |
| A-25 | Rental projects of 50 or more units take about two years from start to completion. | other | 0.8 | Construction schedules for buildings of that size. | C-38 is not reported; the window of C-16 shifts. |
| A-26 | Lenders count a city's pledge of general revenues in the city's own credit risk, although the debt limit does not. | other | 0.7 | Rating agencies' treatment of contingent obligations. | C-44 under U1-b is not reported; C-25 loses its U1-b chain (still `increase` on A-19). |
| A-27 | Issuing bonds costs more than arranging a comparable bank loan: underwriting, counsel, trustee and rating, about 1.5% to 2% of each issue in comparable programs. | other | 0.8 | Issuance costs in conduit programs elsewhere (not in the policy record). | C-34 is not reported; C-3's dominance arithmetic is unchanged. |
| A-28 | The national exempt market does not absorb the added bonds at an unchanged yield. | other | 0.7 | Yields respond to issuance volume; the marginal buyer's tax rate varies. | C-41 and C-42 are `no_change`. |
| A-29 | Without the Act, developers and housing groups would have kept campaigning for authority to use the lapsing volume. | other | 0.6 | The bill of 2027 followed years of lapsed volume; existing associations. | C-46 becomes `increase` (lobbying on the program signed against none). |

**Final check before the report** (`03_workflow.md`).
1. *Uncombined chains.* Section 7 combines every key reached by opposing chains, including the timing chains (C-6 to C-9), rents per window (C-38, C-16, C-17), the Tier C proximity chain (C-18, C-35, C-36), the kind 1 note on existing buildings, the deductions against the forgone tax (C-27, C-29), the taxable market (C-43), the Commission's account (C-45) and lobbying against the counterfactual contest (C-46). The allocation's value (C-3) is combined with the issuer fee, issuance costs and the rent fall by arithmetic. Holding for later draws is a second response the response argument does not cover (CR-12, 1.0); it is combined per window.
2. *Group signs.* Payers of national, state and city budgets are groups (C-28, C-30, C-31); construction inputs and workers are groups (C-23, C-24).
3. *Baseline.* Every sign is against the path where the volume lapses and projects borrow taxably (CR-8, 0.9). C-31 and C-44 are signed per reading against that path; under U1-a their `no_change` is against the counterfactual, not against U1-b. Against that path the bonds are added exempt supply, which is why the national exempt yield is signed (C-41).
4. *Worse off is not poorer.* `resources_available_other_uses` is signed only for budget payers, who make up receipts they cannot avoid, and for pledging cities under U1-b.
5. *Timing shifts.* Starts, taxable loans and rents are signed per window (C-6 to C-9, C-37, C-38, C-16, C-17); the late-year bunching of issues is a path note, since without the Act there are no such issues.
6. *Both sides of transfers.* Listed under section 9.
7. *Every class, every core rule.* CR-7c applied to allocations, sites, existing buildings, existing Aldmere bonds and existing exempt bonds nationally (C-3, C-21, C-20, C-26, C-42); CR-6 to inputs (group), sites (C-39), the bond segment, the national exempt market (C-41), the taxable market (C-43) and pledging cities' own debt (C-44); CR-9 to other building (C-40); enforcement and its funding, with the net (C-33, C-14, C-45). No lasting change in unsubsidized developers' return on capital is signed: their capital can move (CR-7a).
8. *Unstated premises.* Lobbying (A-11, and A-29 for the counterfactual contest), every margin (A-5 to A-8), the baseline (A-12), the construction lag (A-25), segmentation (A-19) and the national market's response (A-28), the contingency premises (A-21, A-22, A-26), issuance costs (A-27), the response argument's cost premise (A-10) and the dominance premises (A-16, A-17, A-20) are in the table.
9. *The baseline of every pattern (1.0).* OC-8, OC-1, OC-2, OC-3, OC-4, OC-5, RS-5, RS-7, RS-8, RS-13, RS-15, SB-5, EN-12 and TX-1 are signed against the no-Act path. SB-4's "later buyers pay it" (sites, C-21) compares with the capitalized price; against the no-Act path later buyers are not signed (section 6). RS-7's Unless is applied to an imposition (C-46; A-29). OC-8's small-borrower clause is applied in its 1.0 form: the national effect is signed, not noted as negligible (C-41, C-42, C-43).

## 11. Report

**The policy.** From 2028 Aldmere lets its cities issue bonds on behalf of private developers of rental buildings of 50 or more units. The bonds are repaid only from the projects' rents, and their interest is exempt from national and state income tax. The state allocates up to $800 million a year by lottery among developers who have a site and their city's agreement. Whether a city may also pledge its general revenues if a project defaults is unclear.

**Visible consequences.** Winning developers borrow at about 4.7% instead of 6.5% (C-1); about $800 million of bonds is issued a year (C-2); allocations are worth about $50,000 a unit to winners (C-3).

**Invisible consequences.**
- *Entering the lottery.* Developers spend on applications, site options and city approvals, and most entries lose (C-4); projects are split or redesigned to qualify (C-5); cities' discretion over sponsorship is lobbied for (C-15, C-11).
- *Building.* Projects are held back in 2027 for the first draw (C-6), so fewer taxable loans are closed that year (C-37). In the long run more rental homes are started and the stock is larger (C-9, C-22), though some unsubsidized rental building and some other building are crowded out (C-10, C-40) and sites cost developers more (C-39). Construction inputs and work rise (C-23, C-24).
- *Rents and property.* Rents are higher in 2029, when the projects held back in 2027 would have been completed (C-38). In the long run rents are lower (C-17) and existing landlords receive less (C-19); their buildings lose value from passage (C-20); owners of sites suitable for such projects gain (C-21). These Tier B signs do not count effects through proximity.
- *Money.* National and state tax receipts fall (C-27, C-29), and those who make them up have less (C-28, C-30). Aldmere's own cities and the state pay more to borrow (C-25), and holders of existing Aldmere bonds lose value (C-26); nationally, other exempt issuers pay slightly more and holders of exempt bonds lose slightly (C-41, C-42). Banks and insurers lose these loans (C-12); underwriters and counsel gain work (C-32); cities and the Commission receive fees (C-13, C-14). Issuing bonds costs winners more than a bank loan would (C-34).
- *Per reading of U1.* If a city may pledge its general revenues (U1-b), its taxpayers or the recipients of its spending bear defaults on pledged projects (C-31), and pledging cities pay more on their own debt (C-44); if it may not (U1-a), neither follows.

**Ambiguous effects.** Starts in 2028 to 2032 (C-7, C-8) and rents in 2030 to 2032 (C-16), since some losers wait for later draws; rents and landlords' positions counting effects through proximity (C-18, C-35, C-36, Tier C); other borrowers' taxable rates (C-43); the Commission's fees net of its costs (C-45); lobbying on the program, which would have been contested without the Act too (C-46).

**Key conditions.** That some projects are built only with the bonds (A-7, p = 0.75); that losers wait (A-8, p = 0.55); that inputs can expand partly over the long run (A-9, p = 0.7) but not at unchanged cost (A-10, p = 0.7); that the in-state bond market is segmented (A-19, p = 0.6); and, under U1-b, that cities pledge and pledged projects fall short (A-21, A-22).

**What this analysis cannot say.** How large any effect is; how the interest subsidy divides among developers, landowners, renters and the cost of entering; whether the rental homes added are worth the tax receipts forgone; whether the policy is desirable.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | developers.winners | interest_rate (projects' debt) | decrease | short–long | visible | B | CR-1, CR-5c, OC-8, CR-7b | A-1, A-2 |
| C-2 | cities.issuing, bondholders | quantity_traded (exempt rental housing bonds) | increase | short–long | visible | B | CR-1, CR-12 | A-2 |
| C-3 | developers.winners | asset_value (projects with an allocation) | increase | short | visible | B | SB-4, CR-7c, CR-10c | A-1, A-2, A-3 |
| C-4 | lottery.entrants | compliance_cost (entering the lottery) | increase | short | invisible | B | EN-12, CR-7a, CR-8c, OC-2 | A-4 |
| C-5 | lottery.entrants | reclassification (split or redesigned projects) | increase | short–medium | invisible | B | RS-5, SB-5, EN-12 | A-5 |
| C-6 | developers.rental | investment_target (starts, 2027) | decrease | short | invisible | B | RS-8, CR-10a | A-6 |
| C-7 | developers.rental | investment_target (starts, 2028) | ambiguous | short | invisible | B | RS-8, CR-10a, CR-12b, CR-12 | A-6, A-7, A-8 |
| C-8 | developers.rental | investment_target (starts, 2029–2032) | ambiguous | medium | invisible | B | CR-4, CR-10a, CR-12b, CR-12 | A-7, A-8 |
| C-9 | developers.rental | investment_target (starts a year, after 2032) | increase | long | invisible | B | CR-4, RS-13, CR-12e, CR-12 | A-1, A-2, A-7, A-9 |
| C-10 | developers.other | investment_target (unsubsidized projects) | decrease | medium–long | invisible | B | CR-9, CR-6, CR-4 | A-7, A-10 |
| C-11 | developers, cities, housing groups | lobbying_effort | increase | medium | invisible | B | RS-7, RS-15 | A-11 |
| C-12 | lenders.taxable | quantity_traded (taxable loans to rental projects) | decrease | short–long | invisible | B | CR-5, CR-9, OC-4 | A-1, A-12 |
| C-13 | cities.issuing | non_tax_receipts (issuer fees) | increase | short–long | invisible | B | CR-8b | A-2, A-13 |
| C-14 | officials.enforcement (State Bond Commission) | non_tax_receipts (application fees) | increase | short–long | invisible | B | CR-8b | A-4 |
| C-15 | lottery.entrants | allocation_by_non_price_criteria (city sponsorship) | increase | short–medium | invisible | B | RS-15, CR-6 | A-24 |
| C-16 | renters | price_paid (rents, 2029–2032) | ambiguous | medium | invisible | B | RS-13, CR-6, CR-12 | A-7, A-8, A-14 |
| C-17 | renters | price_paid (rents; not counting effects through proximity) | decrease | long | invisible | B | RS-13, CR-6, CR-12e, CR-12 | A-1, A-2, A-7, A-9, A-14 |
| C-18 | renters | price_paid (rents) | ambiguous | long | invisible | C | RS-13, CR-9 (proximity), CR-12b, CR-12 | A-1, A-2, A-7, A-9, A-14, A-15 |
| C-19 | landlords.existing | net_price_received (rents; not counting effects through proximity) | decrease | long | invisible | B | RS-13, CR-8b, CR-12 | A-1, A-2, A-7, A-9, A-14 |
| C-20 | landlords.existing | asset_value (existing buildings; not counting effects through proximity) | decrease | short | invisible | B | SB-4, CR-7c, CR-10c, CR-12e, CR-12 | A-7, A-9, A-14, A-16 |
| C-21 | landowners.qualifying_sites | asset_value (sites for 50-unit rentals) | increase | short | invisible | B | SB-4, CR-7c, CR-10c, EN-12, CR-7a, CR-12e | A-4, A-17 |
| C-22 | renters, landlords.existing | capital_stock_target (rental homes) | increase | long | invisible | B | RS-13, CR-10b, CR-12e, CR-12 | A-1, A-2, A-7, A-9 |
| C-23 | input_suppliers | price_paid (construction labor and materials), quantity_traded | at_least_one_increase | long | invisible | B | CR-9, CR-6 | A-7, A-9 |
| C-24 | construction_workers | employment, hours_worked | at_least_one_increase | long | invisible | B | OC-5, CR-9 | A-7, A-9, A-18 |
| C-25 | issuers.aldmere | interest_rate (own exempt bonds) | increase | medium | invisible | B | OC-8, RS-13, CR-6, CR-7a | A-19 |
| C-26 | holders.aldmere_bonds | asset_value (existing Aldmere exempt bonds) | decrease | short | invisible | B | SB-4, CR-7c, CR-10c | A-19 |
| C-27 | taxpayers.national (national budget) | tax_revenue (national income tax) | decrease | short–long | invisible | B | OC-8, CR-8, CR-8b, CR-12e | A-1, A-2, A-20 |
| C-28 | taxpayers.national, recipients of national spending, future taxpayers | resources_available_other_uses | at_least_one_decrease | short–long | invisible | B | OC-8, OC-1, CR-8 | A-1, A-2, A-20 |
| C-29 | taxpayers.state (state budget) | tax_revenue (Aldmere income tax) | decrease | short–long | invisible | B | OC-8, CR-8b, CR-12e | A-1, A-2, A-20 |
| C-30 | taxpayers.state, recipients of state spending, future taxpayers | resources_available_other_uses | at_least_one_decrease | short–long | invisible | B | OC-8, OC-1 | A-1, A-2, A-20 |
| C-31 | taxpayers.city, recipients of city spending (pledging cities) | resources_available_other_uses (defaulted debt service) | U1-a: no_change; U1-b: at_least_one_decrease | long | invisible | B | CR-8, OC-8, CR-12 | A-21, A-22 |
| C-32 | intermediaries | quantity_traded (underwriting, counsel, trustee, rating) | increase | short–long | invisible | B | CR-9, CR-12 | A-2 |
| C-33 | officials.enforcement (State Bond Commission) | enforcement_cost | increase | short–long | invisible | A | OC-3, CR-8c | none |
| C-34 | developers.winners | compliance_cost (issuance costs) | increase | short–long | invisible | B | CR-8c | A-2 |
| C-35 | landlords.existing | net_price_received (rents) | ambiguous | long | invisible | C | RS-13, CR-9 (proximity), CR-12b, CR-12 | A-7, A-9, A-14, A-15 |
| C-36 | landlords.existing | asset_value (existing buildings) | ambiguous | short | invisible | C | SB-4, CR-9 (proximity), CR-12b, CR-12 | A-7, A-9, A-14, A-15, A-16 |

## Gaps found

**(a) Calculus gaps (a step no core rule covers).** None. The value of a lottery entry (the point raised as GAP-039-C2) was derived from CR-10c, CR-7c and CR-7a (b1).

**(b) Unclear core rules.**
1. *Valuing a lottery entry (CR-7c, CR-10c; GAP-039-C2).* CR-10c (value reflects expected yields) covers the odds of a draw if "expected" is read as including chance; CR-7c's probability clause speaks only of the probability that a measure passes or is renewed. Two further steps were needed: where the entry's value settles (on whatever entry requires, here a qualifying site: C-21), and that with open eligibility entry continues until the marginal entry's expected value equals its cost (CR-7a applied to entries). Both follow from the core rules, but neither is stated; a clause in CR-7c would make them explicit.
2. *CR-12, 0.9 (what the response argument gives).* The clause says that to report an increase "the response must be partial: state that supply cannot fully expand at the old cost". Here the response that might undo the added building is a contraction by other builders through higher input prices; it is partial if the inputs' supply *can* expand (A-9). The principle held; the wording, which assumes the response is an expansion, had to be inverted.
3. *CR-8, 0.9 (a reading that permits) with CR-8, 0.8 (contingent payers).* Together they need two premises under U1-b (that the source is used, and that the contingency occurs), and the clauses do not say what the sign is if either is below the cut-off. Read as: not reported under that reading.
4. *CR-8, 0.9 (borrowing baseline).* Stated for borrowing; it was needed for the homes as well. Only projects that would not have been built add supply (A-7), so RS-13's added supply is measured against the same baseline.

**(c) Missing or wrong patterns.**
1. *OC-8, 0.9, "a borrower too small to move its loan market".* Applied as written it would have recorded the rate effect as negligible. That is right for the national market, but the state exemption creates a segment (Aldmere-exempt bonds) in which the new bonds are about a quarter of issuance; with A-19 the in-state rate rises (C-25) and existing holders lose (C-26). The clause should say: small relative to the market in which the borrowing's terms are set, which a tax exemption may confine to a segment.
2. *OC-8, 0.9, tax-exempt interest.* It names those who make up the receipts as payers, but not the opposing chain from borrowers' smaller interest deductions, which raises receipts. The sign needed arithmetic on the case's figures (A-20). The clause should say that net receipts are signed only with that comparison.
3. *EN-12, open-eligibility branch.* "Draws entry to qualify" was right, but the pattern does not say where the right's value goes: partly used up in entering (C-4), partly to owners of what entry requires (C-21), the rest to winners (C-3). A sentence citing CR-7a and CR-7c would close this.
4. *RS-13.* Its assumption that added supply "is not offset by withdrawal elsewhere" is exactly the crowding-out chain (C-10). The response argument (CR-12e) bounds it, but only with a partial-response premise (A-9); RS-13 could point to CR-12e and its 0.9 note.
5. No candidate pattern from 6.2e was needed.

**(d) Vocabulary.**
1. No actor class for a conduit issuer, whose borrowing is another's in substance; used `cities.issuing` with the note in section 2.
2. No variable for a contingent liability before it is called (a pledge's expected cost); C-31 is signed only on the contingency.
3. No variable for the odds of a lottery or the number of entries; used `compliance_cost` and `reclassification`.

**(e) Test of 0.9.**
- *OC-8 0.9, baseline borrowing.* Worked as written: bonds for projects built anyway replace taxable loans; the effect on others' taxable rates is ambiguous and, nationally, negligible, so not recorded.
- *OC-8 0.9, revenue bonds.* Worked as written: later taxes only for a shortfall, which needed U1 per reading (C-31).
- *OC-8 0.9, tax-exempt interest and its payers.* Worked with an addition: the payers are recorded as groups (C-28, C-30), but the sign of net receipts needed arithmetic against developers' smaller deductions, which the clause does not mention (c2).
- *OC-8 0.9, small borrower.* Needed interpretation: small nationally, not small in the segment the state exemption creates (c1; C-25, C-26).
- *OC-8 0.9, lenders.* Worked as written for bondholders (no sign). The class had to be split: lenders who lose the project loans (C-12) and holders of existing in-state bonds (C-26) are signed, but neither is the lenders' side of the new borrowing.
- *OC-8 0.9, legal debt limit.* Not exercised: the record excludes conduit bonds and pledges from the limit.
- *CR-8 0.9, borrowing baseline.* Worked as written for the loans; needed extending to the homes (b4).
- *CR-8 0.9, a reading that permits.* Worked as written: under U1-b the payers are a group including city general revenues (C-31). With CR-8 0.8's contingent payers it needed two premises (A-21, A-22) (b3).
- *EN-12, open-eligibility branch (promoted in 0.9).* Worked for entry (C-4, C-5), incomplete on where the value settles (c3).
- *GAP-039-C2, value of a lottery entry.* Resolved within the core rules (CR-10c, CR-7c, CR-7a), with interpretation (b1). It changed a sign here: it is what makes qualifying sites gain (C-21).
- *SB-4.* Worked as written for allocations, sites, existing rental buildings and existing Aldmere bonds (C-3, C-21, C-20, C-26); sites needed a dominance premise (A-17).
- *RS-13.* Worked with CR-12e and a partial-response premise (c4).
- *CR-12 0.9, what the response argument gives.* Needed interpretation: "partial" here required that inputs can expand (b2).
- *CR-12 0.8 and 0.9, kinds of opposing chain.* Worked as written for all three: kind 1, an underivable rent-control chain on existing buildings, recorded as a Tier C note (C-20); kind 2 with p ≥ 0.5 (A-8, C-8 `ambiguous`) and with p < 0.5 (A-23, C-31 under U1-a `no_change`, chain kept in section 10); kind 3 (C-7, and rents in the medium run, C-16).
- *CR-12 0.9, Tier C against Tier B.* Worked as written: Tier B rent and landlord signs qualified, Tier C combined signs `ambiguous` (C-17 to C-20, C-35, C-36).
- *CR-6 0.9, splitting a shift.* Worked as written: construction inputs recorded as a group (C-23).
- *RS-8.* Worked as written: starts signed per window (C-6, C-7); late-year bunching of issues is a path note.
