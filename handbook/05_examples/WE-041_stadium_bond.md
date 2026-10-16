# WE-041 Stadium financed by city bonds and leased below market

Analyst: draft (Handbook 0.8, held-out test)  |  Rule catalog version: 0.8  |  Status: awaiting expert review

A stylized policy in a fictional city. It resembles real publicly financed stadium deals but is not modeled on any one of them. It was written as a held-out test of catalog 0.8: none of the 0.7 and 0.8 changes were drawn from it. It probes public borrowing that crowds out other borrowing, including the city's own (OC-8), who pays from a general fund and the rule that saving is a use (OC-1, 0.7 and 0.8), Hazlitt's tailor for spending at the stadium against spending elsewhere (OC-5, including its 0.8 clause on new activities), an in-kind subsidy to a private team and its capitalization (CR-7c, CR-4 0.8 on fixed costs), effects through a shared road network and proximity, reported at Tier C (CR-9, 0.7), the three kinds of opposing chain (CR-12, 0.8), and a sign over the whole period of the lease alongside the per-horizon signs (CR-12g, 0.7). The probabilities are illustrative; the evidence column says what a real analysis would cite.

## 1. Policy record

**Merrowgate Riverside Stadium Agreement.** The City of Merrowgate has about 610,000 people in a metropolitan area of about 1.5 million. Its general fund spends about $1.9 billion a year. The city charter caps general-obligation (GO) debt at 3% of assessed property value, which is $2.4 billion; outstanding GO debt is $1.55 billion, leaving $850 million of headroom. The city's five-year capital plan lists $620 million of projects awaiting GO financing in 2027 to 2031 (school roof replacements, road resurfacing, a branch library). Merrowgate levies a local sales tax of 1%.

The Merrowgate Herons are a privately owned professional team in a league of 20 franchises; new franchises and relocations need a three-quarters vote of the owners. The Herons play at the Halcourt Bowl (35,000 seats, built in 1978, owned by the team) in Halcourt, a separate town on Merrowgate's eastern edge, 14 km from the Riverside district. About half of the Herons' home games sold out in the last three seasons. In 2024 the team said the Bowl needed a $210 million renovation, and held talks with Selwick, a city 400 km away, which ended without an offer. The Bowl pays Halcourt about $1.6 million a year in property tax.

The Riverside site is a 22-acre former rail yard owned by the city. In 2025 a developer offered $38 million for it, for a mixed-use project of about 1,100 dwellings; the city was negotiating when the stadium deal was announced, and the developer withdrew.

The deal was announced on 14 April 2026, approved by the city council on 9 September 2026, and the bonds were sold in January 2027. Construction runs from 2027 to mid-2029; the stadium opens in August 2029. The lease runs for 30 years from opening, to 2059.

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Bonds | `government_borrowing` | Stadium construction | City | $480 million of 30-year GO bonds at 4.2%, level debt service of about $28.4 million a year from 2027 to 2056 (about $853 million in all), paid from the general fund. No new tax is named. | — |
| K2 Construction | `public_supply` of a facility (built and owned by the city) | A 42,000-seat stadium on the Riverside site | City | Built on the city's land, which is not sold. | — |
| K3 Lease | `lump_sum_subsidy` (in kind: use of the stadium below market rent) | The Herons | City and team | Rent $1 million a year, fixed for 30 years. The city's consultant estimated an arm's-length rent of about $19 million a year. The team keeps all revenue from tickets, concessions, naming rights, parking and other events, and pays operating costs and routine maintenance (estimated at $4 million a year). Major capital repairs in lease years 1 to 15 are the team's (estimated at $1 million a year); for lease years 16 to 30, see U1 (estimated at $9 million a year). | — |
| K4 Non-relocation | `mandated_contract_term` (agreed in the lease) | Home games | Team | All home games at the Riverside stadium for 30 years. If the team relocates, it pays the outstanding bond principal plus $50 million. | — |
| K5 Administration | Administration | K1 to K4 | City finance and property departments | Bond issuance costs of about $3.1 million; lease administration about $0.4 million a year, from the general fund. | — |

Unclear provisions:
- U1, major capital repairs in lease years 16 to 30 (2044 to 2059). Lease clause 12.3 says: "From the sixteenth Lease Year, responsibility for Major Capital Repairs shall be allocated as the parties shall agree, acting in good faith, having regard to the Landlord's ownership of the Premises." Reading U1-a: the city, as owner, pays them. Reading U1-b: the team pays them, because its general covenant in clause 9 to "keep the Premises in good repair" continues when no other agreement is reached. No court has construed similar language, so these are readings, not assumptions.

The counterfactual is Merrowgate without the agreement. On the evidence, the Herons would then have stayed at the Halcourt Bowl and renovated it at their own cost (A-1, p = 0.7), and the city would have sold the Riverside site to the developer (A-12, p = 0.6). Every sign below is against that path.

## 2. Classification

| Component | Rothbard type | Binding? | Rule families |
|---|---|---|---|
| K1 | Binary: the city borrows from lenders (a voluntary exchange) and repays from the general fund, which compels payment by taxpayers or forgone spending (CR-5b) | Yes | OC-8, OC-1, SB-1, CR-8 (0.7 borrowing; 0.8 contingent payers) |
| K2 | Binary: resources directed to building a facility the city owns. By CR-1, the city's land and borrowed means are directed to one use (CR-8a). | Yes | OC-1, OC-5, CR-8a, CR-9 |
| K3 | Binary: a transfer in kind to the team. By CR-1, it adds an option (a new stadium at a low rent, operation 2) and transfers means (operation 4): the gap between the arm's-length rent and $1 million a year. For the team, the rent is a cost fixed per firm, not per ticket (CR-4, 0.8). | Yes | SB-1, SB-4, CR-7b, CR-7c, CR-4 (0.8) |
| K4 | Triangular in form, but agreed by the team in exchange for K3: it removes the team's option to move (operation 1). Under A-1 the team would have stayed anyway, so it binds only in the 30% of cases where it would have left. | Not binding under A-1 | CR-1, CR-5 |
| K5 | Binary: administration from the general fund | Yes | OC-3, OC-1 |

The city's land is not sold, so the agreement also directs a city asset to the stadium (CR-8a): what the site would otherwise have yielded is part of the cost (C-23, C-24). The debt limit is an existing rule (the charter) that the bonds make bind on other projects (C-28).

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `team.owners` | Owners of the Herons franchise | Gain a new stadium at $1 million a year; give up the option to move; no longer need to renovate the Bowl. |
| `fans` (`buyers.current`) | Buyers of Herons tickets | A newer, larger stadium in another place. |
| `players` | The team's players | Payroll may depend on team revenue. |
| `sellers.substitutes` | Other entertainment in the metro (cinemas, concerts, other sports, bars and restaurants away from the stadium) | Compete with a better game-day option. |
| `riverside_businesses` | Bars, restaurants and shops near the new stadium | Fans' trips now pass them. |
| `halcourt_businesses` | Bars, restaurants and shops near the Bowl | Fans' trips no longer pass them. |
| `neighbors` (Riverside residents) | Live near the new stadium | Share roads and parking with game-day crowds. |
| `riverside_property`, `halcourt_property` | Owners of commercial property near each stadium | Expected rents change. |
| `halcourt` | The town of Halcourt | Loses the Bowl's property tax and game-day sales. |
| `officials.city` | Merrowgate's finance and property departments | Borrow, build, administer the lease. |
| `taxpayers`, recipients of other general-fund spending, future taxpayers | Fund debt service | One or more gives up what it would otherwise have had. |
| `residents.capital_projects` | Users of the projects in the capital plan | Projects compete for the debt headroom. |
| `bondholders` (lenders) | Buyers of the bonds | Lend to the city. |
| `borrowers.other` | Other borrowers in the national loan market | Compete for the same saving. |
| `construction_firms` | Builders in the metro | Gain the stadium contract; may lose city projects and the housing project. |
| `developer`, `buyers.prospective` (housing) | The developer of the Riverside site and would-be residents of its dwellings | The site is not sold. |
| `stadium_workers` | Game-day and operations staff | Their workplace moves from Halcourt to Riverside. |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | `team.owners` | `resources_available_other_uses` | increase | medium (2027–2031: the Bowl's renovation is not needed) | CR-1, CR-8b, SB-1 | A-1, A-17 |
| C-2 | `fans` | `quality_per_unit` (the stadium: newer, larger, closer to transit) | increase | medium–long (from August 2029) | CR-1 | A-1, A-2 |
| C-3 | `construction_firms` (the stadium project) | `employment`, `hours_worked` | at_least_one_increase | short–medium (2027–2029) | OC-5, CR-8b | A-7 |

C-1 to C-3 are what the agreement's supporters point to: the team stays in a new stadium, fans get a better one, builders get the work. "The team stays" is not itself a consequence here: under A-1 (p = 0.7) it would have stayed without the agreement. The case where it would have left is a conditional possibility (section 10).

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-4 | `team.owners` | `asset_value` (the franchise) | increase | short (from April 2026, fully at the council vote) | SB-4, CR-7c, CR-10c | A-1, A-3 |
| C-5 | `team.owners` | `subsidy_share_received` (owners compared with fans) | increase | medium–long | CR-4 (0.8 fixed cost per firm), CR-7b | A-1, A-3 |
| C-6 | `fans` | `quantity_demanded` (attendance at Herons games) | increase | medium–long | CR-4 | A-1, A-2 |
| C-7 | `fans` | `price_paid` (tickets) | ambiguous | medium–long | CR-6, CR-4 (0.8), CR-12b | A-1, A-2, A-5 |
| C-8 | `sellers.substitutes` | `quantity_traded` (other entertainment in the metro) | decrease | medium–long | RS-16 (mirror case), CR-4, CR-9 | A-2, A-6 |
| C-9 | `sellers.substitutes` | `employment`, `hours_worked` | at_least_one_decrease | medium–long | OC-5 | A-2, A-6, A-7 |
| C-10 | `team.owners`, `officials.city` | `lobbying_effort` (negotiating and litigating capital repairs) | increase | long (2042–2046, around lease year 15) | RS-7, CR-4 | A-4 |
| C-11 | `stadium_workers` | `employment` (at the Riverside stadium) | increase | medium–long (from 2029) | OC-5 (0.8 new activities), CR-9 | A-1 |
| C-12 | `stadium_workers` | `employment` (at the Halcourt Bowl) | decrease | medium–long (from 2029) | CR-9, CR-4 | A-1 |

**The subsidy and who keeps it (C-4, C-5).** K3 gives the team the use of a stadium for $1 million a year where an arm's-length rent would be about $19 million. The rent is a cost fixed per firm: it is the same however many tickets are sold. By CR-4's 0.8 clarification, such a cost bears on whether the team operates here, not on the price of each unit, and a unit price is signed only with a premise about entry and exit. Under A-1 the team would have operated here anyway, so the subsidy changes no ticket price on its own account: fans receive none of it through prices, and the owners keep it (C-5; CR-7b, the scarce side keeps it). Franchises are fixed in number by the league (A-3), so the expected stream is capitalized into the franchise's value when the agreement becomes expected (C-4, CR-7c): part of the way at the announcement in April 2026, as approval became likely, and the rest at the council vote. Later buyers of the franchise pay the capitalized price and gain nothing from the subsidy. How much is capitalized depends on how buyers read U1 (section 8).

**Fans (C-6, C-7).** The new stadium is better for fans than the renovated Bowl would have been (A-2): an option improved, so some fans at the margin move to it from other outings (CR-4, mirror case). For ticket prices, demand rises with quality (+), while capacity rises from 35,000 to 42,000 seats, and where games sold out, the added seats push the other way (−, A-5). Both chains are derived and both premises are at least 0.5, so by CR-12's 0.8 clarification (kind 2) the sign is `ambiguous`. The subsidy itself is not a chain here (CR-4, 0.8).

**Other entertainment (C-8, C-9).** RS-16's mirror case: a better game-day option pulls fans from substitutes, so other entertainment sells less, and labor there falls in at least one of employment or hours (OC-5, existing activities). This chain needs no premise about what fans would have done with money they now spend at games: it is substitution, CR-4 for each fan, not a change in means.

**Capital repairs (C-10).** Under either reading of U1, the clause invites a dispute: each side gains from its reading, and the stake (about $135 million over 15 years) is concentrated (RS-7, A-4).

**Workers (C-11, C-12).** The stadium's operations are new at Riverside, so OC-5's 0.8 clause on new activities gives `employment` increase alone there (C-11). But the activity is not new to the metro: it moves from the Bowl, where employment falls (C-12). OC-5's clause was applied per location; see Gaps found (e).

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-13 | `riverside_businesses` | `quantity_traded` (sales to fans on game days) | increase | medium–long | RS-9, CR-9 | game tickets and food and drink: `complement` (trip) | A-1, A-8 |
| C-14 | `halcourt_businesses` | `quantity_traded` (sales to fans on game days) | decrease | medium–long | RS-9, CR-9 | as C-13 | A-1, A-8 |
| C-15 | `riverside_businesses` | `quantity_traded` (sales to regular customers on game days) | decrease | medium–long | CR-9 (0.7 shared facility), CR-4 | Riverside roads and parking: `shared_facility` | A-9 |
| C-16 | `riverside_businesses` | `quantity_traded` (total) | ambiguous | medium–long | CR-12b (0.8), CR-12d | as C-13 and C-15 | A-1, A-8, A-9 |
| C-17 | `neighbors` (Riverside residents) | `travel_time` (on game days) | increase | medium–long | CR-9 (0.7 shared facility) | as C-15 | A-9 |
| C-18 | `riverside_property` (commercial, near the stadium) | `asset_value` | ambiguous | short (from April 2026) | CR-7c, CR-10c, CR-12b, CR-12d | as C-13 and C-15; `proximity` | A-1, A-8, A-9, A-10 |
| C-19 | `halcourt_property` (commercial, near the Bowl) | `asset_value` | ambiguous | short (from April 2026) | CR-7c, CR-10c, CR-12b, CR-12d | as C-14; `shared_facility` (less congestion) | A-1, A-8, A-9, A-10 |
| C-20 | `halcourt` | `tax_revenue` (property tax on the Bowl, game-day sales tax) | decrease | medium (2029–2034) | TX-10, CR-9 | as C-14 | A-1, A-8, A-11 |
| C-21 | `halcourt` | `tax_revenue` | ambiguous | long (after 2034) | TX-10, CR-12b, CR-12g | as C-14; the Bowl site redeveloped | A-1, A-8, A-13 |
| C-22 | `officials.city` | `tax_revenue` (sales tax on Riverside game-day sales) | increase | medium–long | TX-10, CR-9 | as C-13 | A-1, A-8 |
| C-23 | `officials.city` | `non_tax_receipts` (sale of the Riverside site) | decrease | short (2026–2027) | CR-8a, OC-1 | — | A-12 |
| C-24 | `developer`, `buyers.prospective` (housing) | `quantity_supplied` (dwellings on the Riverside site) | decrease | medium–long | CR-8a, CR-9 | — | A-12 |
| C-25 | `team.owners` and buyers of the Bowl site | `quantity_supplied` (land for redevelopment in Halcourt) | increase | long | CR-7a, CR-4 | — | A-1, A-13 |
| C-26 | `borrowers.other` | `interest_rate` | increase | short–long | OC-8, CR-6 | national loan market | A-14 |
| C-27 | `borrowers.other` | `quantity_traded` (loans to other borrowers) | decrease | short–long | OC-8, CR-6, CR-4 | as C-26 | A-14 |
| C-28 | `residents.capital_projects` | `quantity_supplied` (GO-financed city projects: school roofs, roads, library) | decrease | medium (2027–2031) | OC-8, CR-8a, CR-1 | the charter's debt limit (existing rule) | A-15 |
| C-29 | `officials.city` | `interest_rate` (on the city's later GO borrowing) | increase | medium–long | OC-8, CR-6 | as C-26 | A-16 |
| C-30 | `construction_firms` (all work in the metro) | `employment`, `hours_worked` | ambiguous | short–medium | CR-12b (0.8, kind 2) | stadium against deferred projects and the housing site | A-7, A-12, A-15 |

**Trips (C-13, C-14).** Fans buy food and drink on the way to and from games (A-8). The games move from Halcourt to Riverside, and the trips carry those purchases with them (RS-9): sales near the new stadium rise and sales near the Bowl fall. Both are exchange relations and Tier B. Under A-1 most of this is a move within the metro, not new spending.

**Roads and neighbors (C-15, C-17), at Tier C.** On game days, 42,000 people share Riverside's roads and parking with residents and with other businesses' regular customers. That is a `shared_facility` relation, not an exchange (CR-9, 0.7). Residents' travel time rises (C-17), and some regular customers stay away on game days (C-15, A-9). Until the experts decide Q20, these chains are reported at Tier C.

**Combining a Tier B chain with a Tier C chain (C-16, C-18, C-19).** Riverside businesses gain fans' trips (C-13, Tier B) and lose some regulars on game days (C-15, Tier C). Both are items of `quantity_traded`, so each is recorded with a qualifier and the total separately (CR-12, 0.8, two items in one variable): the total has opposite chains, both derived, both premises at least 0.5 (CR-12 0.8, kind 2), so it is `ambiguous`, and by CR-12d it takes the lowest tier in its chains, C (C-16). Commercial property values near each stadium have no items to separate: near Riverside, expected trip sales push values up (Tier B) and congestion pushes them down (Tier C); near the Bowl, the reverse. Both totals are `ambiguous` at Tier C (C-18, C-19). The Tier B part is still reported, through the items C-13 and C-14. Whether this is what CR-12 0.8 intends is in Gaps found (b).

**Two kinds of suspected effect that are not chains.** Supporters say the stadium will "anchor" the regeneration of Riverside beyond game days, and that a team the city "owns a stake in" raises civic pride and spending. No rule derives either: the first needs a premise about investment by others that no relation in the record carries, and the second has no relation at all. By CR-12's 0.8 clarification (kind 1), they are Tier C notes, not opposing chains, and no sign is changed by them.

**Halcourt (C-20, C-21).** Halcourt loses the Bowl's property tax and game-day sales tax (TX-10) at once. Over the long run the team sells the Bowl site, which is redeveloped (C-25, A-13), adding to Halcourt's base. CR-12g keeps the horizons apart: a decrease in the medium run (C-20) and an ambiguous total in the long run (C-21). In the long run, the decrease is itself a kind 2 chain against redevelopment, so the sign is `ambiguous`.

**Merrowgate's sales tax (C-22).** Sales tax on Riverside game-day sales is new revenue for Merrowgate, but the city's total sales tax is not signed: some of the spending is drawn from other Merrowgate sellers (C-8). It is recorded as an item.

**The site (C-23, C-24).** Without the agreement, the city would have sold the site for $38 million and the developer would have built about 1,100 dwellings (A-12). Both are forgone (CR-8a). The site's price is a receipt the city does not get; the dwellings are supply that does not appear.

**Crowding out (C-26 to C-29).** The $480 million lent to the city is not lent to anyone else (CR-8a). OC-8 gives two channels. In the national loan market, the rate other borrowers pay rises and their borrowing falls (C-26, C-27), on the premise that the bonds are bought out of domestic saving that would otherwise have been lent at home (A-14); since the city borrows a very small share of that market, the rise may be negligible, which this method cannot measure. Within the city, the charter's debt limit is a rule already in force, and the bonds use 56% of the remaining headroom ($480 million of $850 million) while $620 million of planned projects await financing. Those projects are deferred (C-28, A-15), and a higher debt ratio raises the rate on the city's later borrowing (C-29, A-16). The second channel is the more concrete one; OC-8 does not mention it (Gaps found, c).

**Construction (C-30).** The stadium contract adds work (C-3), but the deferred city projects (C-28) and the housing that is not built (C-24) would have employed the same trades, and other borrowers' investment falls (C-27). Opposite chains, both derived, premises at least 0.5: `ambiguous` (CR-12 0.8, kind 2). The visible jobs at the stadium site are an item; the total for the trade is not signed.

Stopping points: spending by fans' households elsewhere (depth 3, diffuse); suppliers of bars near each stadium (depth 3, diffuse); prices of homes near the stadium (depth 3 through `proximity`, Tier C, and diffuse; stopped).

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `fans`, `price_paid`, medium–long | Higher demand for a better stadium (A-2) | More seats where games sold out (A-5) | None. The rent subsidy is not a chain (CR-4, 0.8). | **ambiguous** (C-7). Kind 2. |
| `riverside_businesses`, `quantity_traded` (total), medium–long | Fans' trips (C-13, Tier B) | Regulars deterred by congestion (C-15, Tier C) | None | **ambiguous**, Tier C (C-16). Item C-13 stays at Tier B. |
| `riverside_property`, `asset_value`, short | Expected trip sales (A-8, A-10) | Expected congestion (A-9) | None | **ambiguous**, Tier C (C-18). |
| `halcourt_property`, `asset_value`, short | Less congestion (A-9) | Lost trip sales (A-8) | None | **ambiguous**, Tier C (C-19). |
| `halcourt`, `tax_revenue`, long | Redevelopment of the Bowl site (A-13) | Lost Bowl tax and game-day sales | None | **ambiguous** (C-21). Medium run: **decrease** (C-20), not combined with the long run (CR-12g). |
| `construction_firms`, `employment`, `hours_worked`, short–medium | Stadium contract (C-3) | Deferred city projects (C-28), housing not built (C-24), less private borrowing (C-27) | None | **ambiguous** (C-30). |
| `team.owners`, `resources_available_other_uses`, medium (2027–2031) | No renovation of the Bowl ($210 million); rent $1 million a year | — | — | **increase** (C-1). |
| `team.owners`, `resources_available_other_uses`, long (2032–2044, lease years 3–15) | Counterfactual upkeep about $7 million a year | Rent, routine maintenance and repairs about $6 million a year | Arithmetic on the case's figures (A-17) | **increase** (C-31). The margin is thin; the repayment of the counterfactual renovation's financing in these years widens it. |
| `team.owners`, `resources_available_other_uses`, long (2044–2059, lease years 16–30) | U1-a: outlays about $5 million a year against $7 million | U1-b: outlays about $14 million a year against $7 million | Arithmetic per reading (A-17) | **U1-a: increase; U1-b: decrease** (C-32). |
| `team.owners`, `resources_available_other_uses`, whole period (2027–2059) | Counterfactual outlays about $420 million ($210 million renovation, $7 million a year upkeep) | Outlays under the agreement about $165 million (U1-a) or $300 million (U1-b) | CR-12e, arithmetic; CR-12g (0.7, whole period) | **increase** under both readings (C-33). Discounting strengthens it, since the saved renovation comes first. |
| Payers from the general fund, `resources_available_other_uses`, medium–long (2027–2056) | Rent $1 million a year; new sales tax on Riverside game-day sales, at most about $2.8 million a year (C-22) | Debt service $28.4 million a year | CR-12e, arithmetic (A-19) | **at_least_one_decrease** (C-34). |
| Payers, whole period (2026–2059) | Rent about $30 million; sales tax at most about $84 million | Debt service about $853 million; the site's forgone $38 million (C-23); administration; under U1-a, repairs about $135 million (C-35) | CR-12e, arithmetic; CR-12g (0.7) | **at_least_one_decrease** under both readings (C-36). |
| `bondholders`, `resources_available_other_uses` | Interest received from the city (CR-8b) | Interest they would have earned on other loans | — | **Not signed.** Against the right baseline, lenders would have lent elsewhere; OC-8's "lenders receive the interest" is a receipt, not a gain against the counterfactual. |

The sign over the whole period is the 0.7 clarification to CR-12g at work: for the team under U1-b, the per-horizon signs differ (an increase to 2044, a decrease after) while the whole-period sign is an increase, established by arithmetic on the case's figures. The figures are themselves estimates, so the dominance premise is A-17, with a probability, and the arithmetic is done on them (CR-12e names both kinds; here they combine).

Final check (workflow): (1) every key with opposite chains is ambiguous or has a stated dominance premise (arithmetic for the team and the payers); (2) groups are used for labor (C-3, C-9, C-38) and for the payers (C-34 to C-36); (3) every sign is against the counterfactual in which the team stays at the Bowl and the site is sold, not against the agreement under the other reading of U1 (see section 8 on maintenance); (4) `resources_available_other_uses` is signed for the team (a transfer), the payers (sums they cannot avoid), and not for fans, whose spending at games is chosen; (5) the timing of debt service against the stadium's use is recorded per window (section 8); (6) both sides: the subsidy (team C-1, C-31 to C-33; payers C-34 to C-36), the site (city C-23), the loan (city and lenders, not signed for lenders), the move of trips (C-13, C-14), of employment (C-11, C-12) and of tax base (C-20, C-22); (7) capitalization checked for the franchise (C-4), property near each stadium (C-18, C-19) and the Bowl site (C-25); (8) every premise is in section 10.

## 8. Time structure

- **Announcement to council vote (April to September 2026).** The franchise's value rises part of the way as approval becomes likely, and the rest at the vote (C-4, CR-7c's probability clause). Commercial property near each stadium is repriced on the same path (C-18, C-19). The developer withdraws (C-23, C-24).
- **Two windows of a debt-funded transfer (2027 to 2029, then 2029 to 2056).** In the first window the transfer is paid for by lenders' saving: other borrowers are crowded out (C-26 to C-29), the stadium is built (C-3), and the payers already meet debt service from 2027, two years before anyone uses the stadium. In the second window the team uses the stadium and the payers keep paying (C-34). The payers' outlay is a decrease in every window; this is a path note on how the outlay is spread, not a timing shift.
- **The capital plan (2027 to 2031).** Deferred projects wait for headroom as other debt is repaid (C-28); some are done later, so part of C-28 is a delay rather than a loss, which this method signs per window (decrease in 2027–2031) and does not net.
- **Around lease year 15 (2042 to 2046).** The dispute over U1 (C-10). Under U1-a, the team's routine-maintenance obligation continues, but major repairs it can put off past year 15 will be paid by the city: CR-4 (x: repair now, y: defer) gives deferral of major repairs in lease years 11 to 15. This cannot be signed against the counterfactual, in which there is no such stadium; the only comparison is with the agreement under U1-b, which the final check forbids as a baseline. It is recorded here as a path note (Gaps found, b).
- **After 2056 and at 2059.** Debt service ends in 2056; the lease runs to 2059. At its end the stadium is about 30 years old, the team's option to move returns, and the same bargaining can begin again; that is beyond the record.
- **The value of U1 over time.** As the courts or a negotiation settle U1, the franchise value moves again: up if the reading moves toward U1-a, down if toward U1-b, borne by whoever owns the franchise then (CR-7c).

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-34 | `taxpayers`, recipients of other general-fund spending, future taxpayers | `resources_available_other_uses` | at_least_one_decrease | What $28.4 million a year of debt service would otherwise have funded, 2027–2056. No tax is named, so the payers are a group. | OC-1 (0.8 who pays), SB-1, OC-8, CR-8b, CR-12e |
| C-35 | `taxpayers`, recipients of other general-fund spending | `resources_available_other_uses` (major repairs, lease years 16–30) | U1-a: at_least_one_decrease; U1-b: no_change | About $9 million a year of repairs, paid by the general fund only under U1-a. | CR-8 (0.8 contingent payers), OC-1 |
| C-36 | `taxpayers`, recipients of other general-fund spending, future taxpayers | `resources_available_other_uses` (whole period) | at_least_one_decrease | All of the above. | CR-12g (0.7), CR-12e |
| C-37 | `officials.city` | `enforcement_cost` (bond issuance, lease administration, monitoring the non-relocation clause) | increase | Staff time and fees: about $3.1 million at issue and $0.4 million a year, against the one-time administration of a land sale in the counterfactual. | OC-3 (0.8 right baseline), CR-12e |
| C-38 | Sellers in markets where the payers would have spent or invested | `employment`, `hours_worked` | at_least_one_decrease | The work the payers' forgone purchases or investment would have bought. | OC-5, OC-1 (0.7 saving is a use), CR-8a, CR-9 |

**Who pays and what they give up (C-34, C-38).** The record names no tax, so OC-1's 0.8 clause gives the payers as a group: taxpayers, recipients of other general-fund spending, and future taxpayers if the city borrows more instead. The 0.7 clause, saving is a use, applies to the taxpayers among them: some may cut saving rather than purchases, so no named market is signed (no "local shops sell less"). OC-5 still applies to the unnamed group: whether the payers cut purchases or saving, some sellers lose sales or some borrowers lose loans and so investment goods go unbought (CR-8a, CR-9), and labor there falls in at least one of employment or hours (C-38, A-7). This is Hazlitt's tailor: the stadium's jobs are visible (C-3, C-11); the work not done elsewhere is not.

**Spending at the stadium against spending elsewhere.** Fans' spending at the new stadium is mostly spending moved: from the Bowl to Riverside (C-11 to C-14), and from other outings (C-8, C-9). The added attendance at Herons games is matched by less spending elsewhere, by CR-4 for each fan, not by new means. Supporters' figures that count all stadium-area spending as a gain count only the seen side.

**Lenders.** OC-8 says lenders receive the interest (CR-8b). That is a receipt, but against the right baseline they would have lent the same means elsewhere at a similar rate; no gain or loss is signed for them (section 7).

**Administration (C-37).** OC-3's 0.8 clause asks for the right baseline: without the agreement, the city would have administered the sale of the site. Arithmetic on the figures (about $3.1 million at issue and $0.4 million a year for 30 years, against a single sale) establishes the increase (CR-12e).

The site's forgone price (C-23) and dwellings (C-24) are in section 6; the deferred capital projects (C-28) are the most concrete thing given up for the stadium within the city.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | Without the agreement, the Herons would have stayed at the Bowl and renovated it at their own cost ($210 million in 2027–28). | counterfactual_trend | 0.7 | Talks with Selwick ended without an offer; the league's three-quarters vote on relocation; the team's own renovation plan. | If the team would have left (p = 0.3), the agreement keeps it: the team's presence, attendance (C-6), trips (C-13) and Merrowgate's game-day tax (C-22) become increases against an empty metro, C-12, C-14 and C-20 are not consequences, and C-1 compares with a move rather than a renovation. |
| A-2 | Fans value the new stadium above the renovated Bowl. | other | 0.75 | Fan surveys; attendance after comparable moves; transit access. | C-2, C-6, C-8, C-9 are not reported; C-7 becomes a decrease where A-5 holds. |
| A-3 | The number of franchises is fixed by the league, so the expected subsidy is capitalized into the franchise's value. | other | 0.85 | League rules on new franchises. | C-4 and C-5 weaken; part of the subsidy is competed away. |
| A-4 | The parties dispute U1 as lease year 15 approaches. | other | 0.7 | Stake of about $135 million; the clause's wording. | C-10 is not reported. |
| A-5 | Games at the Bowl often sold out, so added seats go to buyers who were turned away. | other | 0.6 | About half of home games sold out. | One chain of C-7 fails; C-7 becomes an increase. |
| A-6 | Some fans are at the margin between a Herons game and other outings in the metro. | substitutability | 0.85 | Entertainment spending surveys. | C-8 and C-9 are not reported. |
| A-7 | Sellers adjust their labor to their sales. | alternative_uses | 0.8 | Staffing practice in construction and hospitality. | C-3, C-9, C-30 and C-38 are not reported. |
| A-8 | Fans eat and drink near the stadium before and after games. | other | 0.85 | Game-day sales near the Bowl. | C-13, C-14, C-20, C-22 are not reported; C-16, C-18, C-19 lose a chain. |
| A-9 | Game-day congestion on Riverside's roads and parking deters some regular customers and slows residents. | other | 0.65 | Traffic studies around comparable stadiums. | C-15 and C-17 are not reported; C-16 and C-18 become increases and C-19 a decrease (Tier B). |
| A-10 | Expected sales near each stadium are capitalized into commercial property values from the announcement. | expectations | 0.75 | Commercial rents near the Bowl. | C-18 and C-19 are not reported. |
| A-11 | The Bowl site is redeveloped only over several years. | other | 0.7 | Size of the site; Halcourt's planning process. | C-20 is shorter; the long-run row C-21 begins earlier. |
| A-12 | Without the agreement, the city would have sold the site to the developer, who would have built about 1,100 dwellings. | counterfactual_trend | 0.6 | The 2025 offer and negotiations. | C-23, C-24 are not reported; C-30 loses a (−) chain. |
| A-13 | The team sells the Bowl site, and its redevelopment adds to Halcourt's tax base in the long run. | other | 0.75 | Value of 60 acres of suburban land. | C-25 is not reported; C-21 becomes a decrease. |
| A-14 | The bonds are bought mainly out of domestic saving that would otherwise have been lent to other domestic borrowers. | other | 0.6 | Holders of the city's earlier bonds. | C-26 and C-27 are not reported. |
| A-15 | The city uses debt headroom for the stadium that it would otherwise have used for projects in its capital plan, and those projects are deferred, not financed another way. | other | 0.7 | The charter limit; the capital plan's $620 million queue. | C-28 is not reported; C-30 loses a (−) chain. |
| A-16 | Rating agencies and bond buyers weigh the higher debt ratio, so the city's later borrowing costs more. | other | 0.55 | Rating agencies' published criteria. | C-29 is not reported. |
| A-17 | The cost figures hold well enough for the comparisons: team routine maintenance $4 million a year; major repairs $1 million a year in lease years 1–15 and $9 million a year after; counterfactual upkeep of the renovated Bowl $7 million a year. | other | 0.75 | City consultant's report; the team's renovation plan. | C-31 and C-33 may fail; C-32 under each reading may change. |
| A-18 | Debt service is paid from the general fund on schedule; the debt is repaid, not rolled over. | revenue_use | 0.9 | K1; the charter. | C-34, C-36 and C-38 shift to later payers. |
| A-19 | New sales tax on Riverside game-day sales is far smaller than debt service. | other | 0.9 | City projection of $2.8 million a year against $28.4 million. | The payers' dominance premise fails; C-34 and C-36 become `ambiguous`. |
| A-20 | The league's collective agreement ties player payroll to a share of team revenue, including stadium revenue. | other | 0.45 | League agreement. Below the cut-off. | Not reported. If true, `players` `wage_rate` increases and the owners' share in C-5 is smaller. |

**Conditional possibilities (below the cut-off).** Under not-A-1 (p = 0.3), the agreement keeps a team that would have left: that is the claim the agreement's supporters make, and in this method it is a conditional possibility, not a reported consequence. Under A-20 (p = 0.45), players capture part of the stadium's revenue through payroll.

## 11. Report

**The policy.** Merrowgate borrows $480 million for 30 years to build a 42,000-seat stadium on city land in Riverside and leases it to the privately owned Herons for $1 million a year for 30 years, against an estimated arm's-length rent of $19 million. Debt service of about $28.4 million a year comes from the general fund. The team keeps all stadium revenue, pays routine upkeep, and must play its home games there. Who pays major repairs after year 15 is unclear (U1).

**Visible consequences.** The team no longer has to renovate its old stadium (C-1); fans get a better stadium (C-2); builders get the stadium contract (C-3).

**Invisible consequences.**
- *The subsidy.* The owners keep it: the rent is a fixed cost, so ticket prices do not fall on its account (C-5), and the franchise's value rises from the announcement (C-4). Over the whole lease the team's means rise under either reading of U1 (C-33), though after year 15 they fall under the reading that makes the team pay for repairs (C-32).
- *Who pays.* Taxpayers, recipients of other general-fund spending or future taxpayers pay about $853 million of debt service, far more than the rent and new sales tax (C-34, C-36), and possibly major repairs after year 15 (C-35). The city forgoes the $38 million sale of the site (C-23), and about 1,100 dwellings are not built there (C-24). Planned school, road and library projects wait for debt headroom (C-28), and the city's later borrowing may cost more (C-29). Other borrowers face a higher rate and borrow less (C-26, C-27), by an amount that may be negligible.
- *Jobs and spending moved, not created.* Stadium jobs appear in Riverside and disappear in Halcourt (C-11, C-12). Bars near the new stadium gain game-day sales and those near the old one lose them (C-13, C-14). Other entertainment in the metro sells less and employs less (C-8, C-9). Sellers wherever the payers would have spent or invested lose work (C-38). Whether construction work in the metro rises at all is ambiguous (C-30).
- *Halcourt.* Loses tax revenue in the medium run (C-20); the long run depends on redevelopment of the old site (C-21, C-25).
- *Tier C (shared roads, not exchange).* Riverside residents spend longer travelling on game days (C-17), and some regular customers of Riverside businesses stay away (C-15).
- *Disputes.* The repairs clause leads to negotiation or litigation around year 15 (C-10). Administration of the bonds and lease (C-37).

**Ambiguous effects.** Ticket prices (C-7); total sales of Riverside businesses and commercial property values near each stadium, at Tier C (C-16, C-18, C-19); Halcourt's long-run tax revenue (C-21); total construction employment (C-30). Not signed: lenders' means; Merrowgate's total sales-tax revenue.

**Key conditions.** That the team would have stayed anyway (A-1, p = 0.7): if not, the agreement's main claim, keeping the team, holds, and several signs change. That the site would have been sold and built on (A-12, p = 0.6). That the capital plan is crowded out within the debt limit (A-15, p = 0.7). The team's whole-period gain and the per-horizon signs after year 15 rest on the cost figures (A-17, p = 0.75).

**What this analysis cannot say.** How large any effect is; whether residents value having the team, or a new stadium, more than what they give up for it; the value of the non-relocation promise, which matters only if the team would otherwise have left; effects on traffic safety or the environment (out of scope for version 1); whether the agreement is desirable.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | team.owners | resources_available_other_uses | increase | medium (2027–2031) | visible | B | CR-1, CR-8b, SB-1 | A-1, A-17 |
| C-2 | fans | quality_per_unit (stadium) | increase | medium–long | visible | B | CR-1 | A-1, A-2 |
| C-3 | construction_firms (stadium project) | employment, hours_worked | at_least_one_increase | short–medium | visible | B | OC-5, CR-8b | A-7 |
| C-4 | team.owners | asset_value (franchise) | increase | short | invisible | B | SB-4, CR-7c, CR-10c | A-1, A-3 |
| C-5 | team.owners | subsidy_share_received (owners compared with fans) | increase | medium–long | invisible | B | CR-4, CR-7b | A-1, A-3 |
| C-6 | fans | quantity_demanded (attendance) | increase | medium–long | invisible | B | CR-4 | A-1, A-2 |
| C-7 | fans | price_paid (tickets) | ambiguous | medium–long | invisible | B | CR-6, CR-4, CR-12b | A-1, A-2, A-5 |
| C-8 | sellers.substitutes | quantity_traded (other entertainment) | decrease | medium–long | invisible | B | RS-16, CR-4, CR-9 | A-2, A-6 |
| C-9 | sellers.substitutes | employment, hours_worked | at_least_one_decrease | medium–long | invisible | B | OC-5 | A-2, A-6, A-7 |
| C-10 | team.owners, officials.city | lobbying_effort (capital repairs) | increase | long (2042–2046) | invisible | B | RS-7, CR-4 | A-4 |
| C-11 | stadium_workers | employment (Riverside) | increase | medium–long | visible | B | OC-5, CR-9 | A-1 |
| C-12 | stadium_workers | employment (Halcourt Bowl) | decrease | medium–long | invisible | B | CR-9, CR-4 | A-1 |
| C-13 | riverside_businesses | quantity_traded (sales to fans on game days) | increase | medium–long | invisible | B | RS-9, CR-9 | A-1, A-8 |
| C-14 | halcourt_businesses | quantity_traded (sales to fans on game days) | decrease | medium–long | invisible | B | RS-9, CR-9 | A-1, A-8 |
| C-15 | riverside_businesses | quantity_traded (regular customers on game days) | decrease | medium–long | invisible | C | CR-9, CR-4 | A-9 |
| C-16 | riverside_businesses | quantity_traded (total) | ambiguous | medium–long | invisible | C | CR-12b, CR-12d | A-1, A-8, A-9 |
| C-17 | neighbors (Riverside residents) | travel_time (game days) | increase | medium–long | invisible | C | CR-9 | A-9 |
| C-18 | riverside_property | asset_value | ambiguous | short | invisible | C | CR-7c, CR-10c, CR-12b, CR-12d | A-1, A-8, A-9, A-10 |
| C-19 | halcourt_property | asset_value | ambiguous | short | invisible | C | CR-7c, CR-10c, CR-12b, CR-12d | A-1, A-8, A-9, A-10 |
| C-20 | halcourt | tax_revenue | decrease | medium (2029–2034) | invisible | B | TX-10, CR-9 | A-1, A-8, A-11 |
| C-21 | halcourt | tax_revenue | ambiguous | long | invisible | B | TX-10, CR-12b, CR-12g | A-1, A-8, A-13 |
| C-22 | officials.city | tax_revenue (sales tax on Riverside game-day sales) | increase | medium–long | invisible | B | TX-10, CR-9 | A-1, A-8 |
| C-23 | officials.city | non_tax_receipts (sale of the site) | decrease | short | invisible | B | CR-8a, OC-1 | A-12 |
| C-24 | developer, buyers.prospective (housing) | quantity_supplied (dwellings on the site) | decrease | medium–long | invisible | B | CR-8a, CR-9 | A-12 |
| C-25 | team.owners and buyers of the Bowl site | quantity_supplied (land for redevelopment in Halcourt) | increase | long | invisible | B | CR-7a, CR-4 | A-1, A-13 |
| C-26 | borrowers.other | interest_rate | increase | short–long | invisible | B | OC-8, CR-6 | A-14 |
| C-27 | borrowers.other | quantity_traded (loans) | decrease | short–long | invisible | B | OC-8, CR-6, CR-4 | A-14 |
| C-28 | residents.capital_projects | quantity_supplied (GO-financed city projects) | decrease | medium (2027–2031) | invisible | B | OC-8, CR-8a, CR-1 | A-15 |
| C-29 | officials.city | interest_rate (later GO borrowing) | increase | medium–long | invisible | B | OC-8, CR-6 | A-16 |
| C-30 | construction_firms (metro) | employment, hours_worked | ambiguous | short–medium | invisible | B | CR-12b | A-7, A-12, A-15 |
| C-31 | team.owners | resources_available_other_uses | increase | long (2032–2044) | invisible | B | CR-8b, CR-12e | A-1, A-17 |
| C-32 | team.owners | resources_available_other_uses | U1-a: increase; U1-b: decrease | long (2044–2059) | invisible | B | CR-8b, CR-12e | A-1, A-17 |
| C-33 | team.owners | resources_available_other_uses | increase | whole period (2027–2059) | invisible | B | CR-12g, CR-12e | A-1, A-17 |
| C-34 | taxpayers, recipients of other general-fund spending, future taxpayers | resources_available_other_uses | at_least_one_decrease | medium–long (2027–2056) | invisible | B | OC-1, SB-1, OC-8, CR-8b, CR-12e | A-18, A-19 |
| C-35 | taxpayers, recipients of other general-fund spending | resources_available_other_uses (major repairs) | U1-a: at_least_one_decrease; U1-b: no_change | long (2044–2059) | invisible | B | CR-8b, OC-1 | A-17 |
| C-36 | taxpayers, recipients of other general-fund spending, future taxpayers | resources_available_other_uses | at_least_one_decrease | whole period (2026–2059) | invisible | B | CR-12g, CR-12e | A-18, A-19 |
| C-37 | officials.city | enforcement_cost (bonds and lease administration) | increase | short–long | invisible | B | OC-3, CR-12e | A-12 |
| C-38 | sellers where payers would have spent or invested | employment, hours_worked | at_least_one_decrease | medium–long | invisible | B | OC-5, OC-1, CR-8a, CR-9 | A-7, A-18 |

## Gaps found

**(a) Calculus gaps (a step no core rule covers).**
- GAP-041-1 (open, for the experts; related to Q20). Residents who value having the team in their city without buying a ticket. Supporters cite this as the main benefit. It travels through no exchange, and through neither `shared_facility` nor `proximity`: no core rule propagates it (CR-9 follows recorded relations only), so the method records nothing, and the report says so. Whether such valuations belong in the analysis at all, and under what relation, is for the experts.

**(b) Unclear core rules.**
1. *CR-12 0.8 and CR-9 0.7: a Tier C chain opposing a Tier B chain.* The three kinds of opposing chain say nothing about tiers. Treating the `shared_facility` chain as kind 2 (derived, premise at least 0.5) made the totals `ambiguous` and, by CR-12d, Tier C (C-16, C-18, C-19), which removes Tier B claims about property values that the exchange chain alone would support. For `quantity_traded` the 0.8 "two items in one variable" clause kept the Tier B item (C-13); for `asset_value` there is no item to keep. Suggest: say whether a Tier C chain can make a Tier B consequence ambiguous, or whether it is recorded beside it.
2. *CR-12g 0.7, whole period: arithmetic on estimated figures.* The whole-period sign for the team (C-33) rests on arithmetic, but the figures are estimates and the counterfactual itself is an assumption (A-1). CR-12e lists "an empirical premise" and "arithmetic on the case's figures" as alternatives; here they combine. Worked, with A-17 as the premise behind the figures.
3. *The baseline for a thing the policy creates.* Deferral of major repairs before year 15 under U1-a (section 8) is derived (CR-4, CR-10a), but the counterfactual has no such stadium, and the only comparison is with U1-b, which the final check rules out. It is recorded as a path note. The method has no way to sign a response on an asset that exists only under the policy, compared with how that asset would otherwise be kept.
4. *A counterfactual that is itself uncertain.* The agreement's main stated effect, keeping the team, is a change in the probability that the team leaves (from about 0.3 to near zero). The method requires one counterfactual premise (A-1) and so reports the effect only as a conditional possibility. CR-7c handles a change in probability for asset prices (C-4); nothing handles it for actions.
5. *CR-8 0.7, borrowing: the lenders' side.* "The means they lend are not available to other borrowers" worked (C-26, C-27). OC-8's "Lenders receive the interest (CR-8b)" did not yield a sign against the right baseline, since lenders would have lent elsewhere (section 7).

**(c) Missing or wrong patterns.**
1. *OC-8 lacks two clauses.* (i) A borrower small in its loan market: the direction of `interest_rate` holds, but the effect may be negligible; EN-6's 0.8 Unless clause has the right form ("record it with a premise that the effect is not negligible, or note it as negligible"), and OC-8 should borrow it. (ii) A debt limit already in force: the most concrete crowding out here was the city's own capital plan within its charter limit (C-28), not other borrowers in the national market. OC-8 should name it.
2. *OC-8, "Lenders receive the interest".* As written it reads as a gain for lenders; against the right baseline it is a receipt they would have had elsewhere. Suggest adding "compared with lending elsewhere, no sign".
3. *Below-market lease of a public asset.* No pattern covers an in-kind subsidy of a cost fixed per firm. SB-2 and DM-1 are for per-unit subsidies and do not apply. Derived here from CR-4 (0.8: a fixed cost bears on whether the firm operates, so no unit-price sign), CR-7b (the scarce side keeps it) and CR-7c (capitalized at announcement) (C-4, C-5). Candidate pattern.
4. *RS-9 for a move within a metro.* RS-9 fit as written: the games' trips move from Halcourt to Riverside and carry purchases with them (C-13, C-14).
5. *"Debt-funded transfer in two windows"* (candidate in `06_gaps.md`, 6.2e, from WE-033): needed here (section 8). Second use; proposed for promotion.

**(d) Vocabulary.**
1. *Horizons for a 30-year lease.* `short`, `medium` and `long` cannot separate lease years 3–15 from 16–30; qualifiers with dates were used, and `whole period` as CR-12g's 0.7 clarification allows.
2. *Public capital projects.* No variable for public works the state supplies (school roofs, roads); `quantity_supplied` with a qualifier was used (C-28).
3. *A firm's location.* No variable records where a seller operates or whether it stays in a market; this is why "the team stays" could not be written as a consequence even conditionally.
4. *Instrument for an in-kind lease subsidy.* `lump_sum_subsidy` was used for K3; the in-kind, below-market form deserves a note in 2.3.

**(e) Test of 0.8.**
- *OC-8 (0.7):* needed interpretation. Its direction held (C-26, C-27) on a domestic-saving premise (A-14); it lacked a clause for a borrower small in its market and for an existing debt limit, and its lenders' clause did not survive the right baseline ((c)1, (c)2).
- *OC-1 0.8, who pays:* worked as written. Payers recorded as a group with `at_least_one_decrease` (C-34 to C-36).
- *OC-1 0.7, saving is a use:* worked as written. It kept any named market out of the payers' consequences, and OC-5 still signed an unnamed group (C-38).
- *OC-5 (Hazlitt's tailor):* worked as written for spending moved between stadium and other entertainment (C-8, C-9) and for the payers (C-38).
- *OC-5 0.8, new activities:* needed interpretation. The stadium's operations are new at Riverside but moved from Halcourt; the clause was applied per location (C-11 `employment` alone; C-12 the matching fall). The clause should say "new to the market considered, not moved from another location".
- *CR-7c, capitalization of the subsidy, with its probability clause:* worked as written (C-4, dated from announcement to council vote; C-18, C-19).
- *CR-4 0.8, a cost fixed per firm bears on operation, not on unit price:* worked as written. It stopped the subsidy from being read as lower ticket prices and gave the owners' share (C-5, C-7).
- *CR-9 0.7, shared facilities and proximity at Tier C:* worked as written for travel time (C-17) and regulars deterred (C-15); needed interpretation where a Tier C chain opposes a Tier B one ((b)1).
- *CR-12 0.8, three kinds of opposing chain:* worked as written. Kind 1 (regeneration "anchor", civic pride) became Tier C notes; kind 2 at or above 0.5 gave `ambiguous` (C-7, C-16, C-21, C-30); kind 2 below 0.5 (A-20, players' pay) was recorded and not reported; no kind 3 arose. Silent on tiers ((b)1).
- *CR-12 0.8, two items in one variable:* worked as written (C-13, C-15, C-16; C-22 as an item of Merrowgate's sales tax).
- *CR-12g 0.7, whole-period sign:* worked as written, and showed its value: for the team under U1-b the long-run window is a decrease and the whole period an increase (C-32, C-33). Its dominance premise combined arithmetic with an estimate ((b)2).
- *CR-8 0.8, contingent payers:* worked as written; the general fund pays major repairs only under U1-a, recorded per reading (C-35).
- *OC-3 0.8, right baseline:* worked as written; the counterfactual land sale's administration was the baseline, and arithmetic on the figures signed the increase (C-37).
- *Candidate patterns from `06_gaps.md`, 6.2e:* "Debt-funded transfer in two windows" (WE-033) was needed (section 8); second use, which promotes it.
