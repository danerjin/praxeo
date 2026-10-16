# WE-051 / Analysis: Tax-exempt revenue bonds for private rental housing, allocated by lottery

Analyst: core-only re-run (Handbook 0.9)  |  Rules: core rules CR-1 to CR-12 only  |  Status: compared

## 1. Policy record

**Aldmere Rental Housing Bond Act.** Aldmere is a state of about 6.2 million people with about 120 cities (largest: Pellmouth, Marrowby, Fennick). It has about 950,000 rental homes, vacancy about 4%, average rent about $1,900 a month. About 14,000 rental homes are completed a year, mostly in buildings of 50 or more units in the three largest cities. A unit costs about $330,000 (land about $50,000), financed about 65% with taxable construction-to-permanent loans from banks and insurers at about 6.5%, the rest with equity. Comparable exempt revenue bonds yield about 4.7% (marginal national buyer at a 28% tax rate). Aldmere's cities and the state issue about $3.5 billion of exempt bonds a year (about $45 billion outstanding), mostly bought by residents for the double exemption; the national exempt market issues about $400 billion a year. Developers deduct interest at about 25% (national) and 5% (state).

| Field | Value | Source sentence |
|---|---|---|
| Jurisdiction (and what lies just outside) | Aldmere. Other states' bonds are taxed by Aldmere's 5% income tax; the national exemption and volume cap apply to every state. | Existing rules. |
| Announced / enacted / effective / expires | Introduced 10 January 2027; passed 20 April 2027; effective 1 January 2028; first lottery March 2028; no expiry. | Policy record. |
| Enforcement (who, penalties, resources) | State Bond Commission runs the draws and checks eligibility and completion, funded by $15,000 application fees. Forfeiture of allocations not issued by 31 December. | K2, K5. |
| Existing rules (both paths) | National exemption of interest on city bonds for private rental projects, up to $800 million a year for Aldmere; unallocated volume lapses (before the Act it lapsed every year). Aldmere's 5% income tax exempts interest on Aldmere city and state bonds. A city's general obligation debt is capped at 5% of assessed value; conduit bonds and pledges in their support are not counted. | Existing rules. |

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Authority to issue | `government_borrowing` (conduit revenue bonds) | New rental projects of 50 or more units | Cities that choose to sponsor | Special obligations payable solely from project revenues and any additional security under s. 7; interest exempt under existing national and state rules. | — |
| K2 State cap and lottery | `rights_allocation` (lottery) | The national volume, $800 million a year | State Bond Commission | Applications by 31 January; eligible: any developer of a new project of 50 or more units with site control and a sponsoring city resolution; one application per site; fee $15,000; allocations drawn in March in the amount requested until the cap is used; issue by 31 December or forfeit (forfeited volume lapses); losers may reapply. | — |
| K3 Additional security (s. 7) | Rule on the bonds' security | Bonds under K1 | Issuing cities | "An issuing city may provide such additional security for the bonds as its council deems appropriate." | — |
| K4 Issuer fee | Fee | Bonds under K1 | Developers | Up to 0.5% of bonds issued, once. | — |
| K5 Administration | Enforcement | K2 | State Bond Commission | Draws and checks, funded by application fees. | — |

Unclear provisions:
- **U1, the city's general revenues (s. 7 against s. 3).** U1-a: "payable solely from the revenues of the project" limits additional security to project-specific security; a city may not pledge its general revenues. U1-b: additional security is not limited, so a city may, but need not, pledge its general revenues. No probability; signs that depend on it are reported per reading.

**Counterfactual.** Aldmere without the Act: the national volume lapses, rental projects are financed with taxable loans at about 6.5%, about 14,000 rental homes are completed a year. Counterfactual law: no city may issue bonds for private projects. **Horizons used:** short = 2027 to 2029 (announcement to the first bond-financed completions); medium = 2030 to 2037; long = after 2037.

**Figures (arithmetic used below).** The cap finances about 3,700 units a year (about 26% of counterfactual completions). The bonds save about 1.8 points on about $214,500 of debt per unit, about $50,000 per unit in present value (about 15% of cost). Requests are about three times the cap, so an entry is worth about $17,000 per unit before entry costs (about $1,000 to $2,000 per unit). Each year's issue costs the national budget about $11 million a year and the state about $1.9 million a year.

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | CR-1 operations | Core rules applied |
|---|---|---|---|---|
| K1 Authority to issue | binary (the state, through its cities, grants a tax privilege on borrowing) | Yes: requests exceed the cap (A-2) | 2 for cities (option of issuing conduit bonds); 2 for winning developers (option of exempt financing); 2 for bond buyers (a new exempt asset). Through the existing exemption, a transfer from national and state budgets (op 4 on taxpayers, via CR-8 0.9) | CR-4, CR-5c, CR-7, CR-8b, CR-8 0.9, CR-9 |
| K2 Lottery | binary (rights_allocation) | Yes: the cap rations about one entry in three (A-2) | 2 (option of entering); 3 ($15,000 fee and preparation attached to entering); the right drawn is a created asset transferred to the winner (op 4) | CR-6 (fixed quantity, zero price), CR-7c, CR-7 0.7 (claims before creation), CR-8c, CR-10a |
| K3 Additional security | binary | Per reading | U1-a: no operation on city taxpayers. U1-b: 2 for councils (option of pledging general revenues); contingent op 4 on city taxpayers where a pledged project falls short | CR-1 per reading, CR-8 0.8 (contingent payers), CR-8 0.9 (a reading that permits) |
| K4 Issuer fee | binary (fee) | Yes where charged (A-13) | 3 on developers (a charge attached to using the bonds); receipt to cities | CR-5c, CR-8b |
| K5 Administration | binary | Yes | Commission spends fees | CR-8b, CR-8c |

## 3. Actor classes

| Actor class | Role | How its options change (CR-1, CR-9) |
|---|---|---|
| developers.winners.inframarginal | Winners whose projects would have been built with taxable loans (A-12) | Op 2 and op 4: cheaper debt on a project they would have built; a transfer. |
| developers.winners.marginal | Winners whose projects are viable only at the lower rate (A-7) | Op 2: projects built that would not have been. |
| developers.losers | Entrants who lose a draw | Op 3: entry costs used up; may hold for the next draw (A-8). |
| developers.unsubsidized | Developers who do not enter or do not win, and builders of other construction | Through CR-9: compete for the same sites, labor and inputs (A-10); face lower rents (A-14). |
| site_owners | Owners of sites able to host a project of 50 or more units | Through CR-9 and CR-7 0.7: site control is required to enter, so the entry's value travels with the site. |
| cities.sponsoring | Cities that pass resolutions and issue | Op 2 (issue), receipt of fees (K4); discretion over which projects to sponsor (A-24); under U1-b, the option of pledging. |
| city_taxpayers | Residents and recipients of other city spending | Under U1-b, contingent payers of shortfalls on pledged projects (A-21, A-22). |
| bond_buyers | Buyers of exempt bonds, in-state and national | Op 2: a new exempt asset at about 4.7%. |
| issuers.aldmere | Aldmere cities and the state as issuers of their own exempt bonds | Through CR-9 (substitute: added in-state exempt supply, A-19). |
| holders.existing_aldmere_bonds | Holders of the $45 billion outstanding | Through CR-7c if in-state yields rise (A-19). |
| lenders.taxable | Banks and insurers lending to rental projects | Through CR-9 (substitute): lose loans to inframarginal winners (A-12). |
| borrowers.other | Other borrowers from the same lenders and savers | Through CR-8 0.9: the lenders' and bond buyers' funds move between uses. |
| renters | Current and prospective renters | Through CR-9 (more homes in the long run, delays at the start; A-14). |
| landlords.existing | Owners of existing rental buildings | Through CR-9 and CR-7c (rents). |
| workers.construction, input_suppliers | Construction labor and materials | Through CR-9 (input_to): more projects (A-7, A-18). |
| taxpayers.national, taxpayers.state | Those who make up forgone receipts, or recipients of other spending | Through CR-8 0.9 (interest exempt from tax reduces receipts). |
| officials.commission | State Bond Commission | Runs draws and checks; funded by fees. |
| lobby_groups | Developers, cities, housing groups | CR-4 (x: accept, y: lobby) on keeping or enlarging the program (A-11). |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | developers.winners | interest_rate (project debt) | decrease | short; medium; long | CR-1 op 2, CR-5c, CR-7a | A-1, A-2, A-3 |
| C-2 | bond_buyers | quantity_traded (exempt conduit bonds for rental projects) | increase | short; medium; long | CR-1 op 2, CR-5, CR-12 0.9 (activity exists only under the policy) | A-1, A-2 |
| C-3 | developers.winners | asset_value (projects with an allocation) | increase | short (at each draw) | CR-7c (created asset captured at creation), CR-10c, CR-12e (arithmetic against the fee; A-17 against the rent fall) | A-1, A-2, A-3, A-17 |
| C-4 | taxpayers.national | tax_revenue (national income tax) | decrease | medium; long | CR-8 0.9 (exempt interest reduces receipts), CR-8b, CR-12e arithmetic | A-20, A-1, A-2 |
| C-5 | taxpayers.state | tax_revenue (state income tax) | decrease | medium; long | CR-8 0.9, CR-8b, CR-12e arithmetic | A-20, A-1, A-2 |
| C-6 | cities.sponsoring | non_tax_receipts (issuer fees) | increase | short; medium; long | CR-1 (K4), CR-8b, CR-12 0.9 | A-13, A-2 |

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-7 | developers.winners, developers.losers | compliance_cost (applications: fees, site control, city resolutions) | increase | short; medium; long | CR-4 (x: stay out, y: enter), CR-8c, CR-12 0.9 | A-4, A-2 |
| C-8 | officials.commission | enforcement_cost | increase | short; medium; long | CR-1 (K5), CR-8c | A-2 |
| C-9 | developers.winners, developers.losers | reclassification (projects split or redesigned to qualify or to gain entries) | increase | short; medium; long | CR-4 (x: one project, y: split or redesign), CR-6 (pressure on the margins of a fixed quantity) | A-5, A-4 |
| C-10 | developers.unsubsidized (would-be 2027 borrowers) | quantity_traded (taxable rental project loans closed, 2027) | decrease | short (2027) | CR-10a, CR-4 (x: close now, y: wait for the first draw) | A-6 |
| C-11 | developers | investment_target (rental construction started, 2027) | decrease | short (2027) | CR-10a, CR-4 | A-6 |
| C-12 | developers | investment_target (rental construction started, 2028 to 2037) | ambiguous | medium | CR-12b: (+) A-7; (−) A-8 holding, A-10 crowding out | A-7, A-8, A-10 |
| C-13 | developers | investment_target (rental construction started, after 2037) | increase | long | CR-4, CR-12b with CR-12e response argument and CR-12 0.9 (partial, A-9) | A-7, A-9, A-10 |
| C-14 | developers.unsubsidized | investment_target (projects without an allocation) | decrease | medium; long | CR-9, CR-7a, CR-4 | A-10, A-7 |
| C-15 | developers.unsubsidized | return_on_capital | decrease | medium; long | CR-9, CR-7a | A-10, A-7, A-14 |
| C-16 | cities.sponsoring | allocation_by_non_price_criteria (which projects get a resolution) | increase | short; medium; long | CR-6 (criteria by which the scarce side chooses), CR-2 | A-24, A-4 |
| C-17 | developers | lobbying_effort (seeking city resolutions) | increase | short; medium; long | CR-4 (x: no approach, y: lobby the council), CR-6, CR-8c | A-24, A-4, A-11 |
| C-18 | lobby_groups | lobbying_effort (to keep or enlarge the program) | increase | medium; long | CR-4 (x: accept, y: lobby), CR-8c | A-11 |
| C-19 | cities.sponsoring | interest_rate (own general obligation debt) | U1-a: no_change; U1-b: increase | medium; long | CR-7c, CR-10c, CR-1 per reading | A-21, A-N1 |
| C-20 | city_taxpayers, recipients_of_other_city_spending | resources_available_other_uses | U1-a: no_change; U1-b: at_least_one_decrease | long | CR-8 0.8 (contingent payers), CR-8 0.9 (a reading that permits) | A-21, A-22 |

## 6. Second-order effects

CR-9 along named relations, then CR-5 to CR-7 in each market reached. Depth limit 4. The chain from in-state yields to the taxpayers of other issuers stops at depth 4 (C-31). The national exempt market is recorded with its CR-6 direction only (C-32).

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-21 | site_owners | asset_value (sites able to host 50 or more units) | increase | short (from introduction, January 2027) | CR-7 0.7 (claims before creation), CR-7c, CR-10c, CR-8c | input_to: sites input_to rental projects; contract: site control (option or lease) | A-4, A-2, A-17 |
| C-22 | site_owners | subsidy_share_received | increase | short; medium | CR-7b (the gain settles on means that cannot move: scarce sites) | input_to (as C-21) | A-4, A-10 |
| C-23 | site_owners (three largest cities) | price_paid (sites, paid by all developers) | increase | medium; long | CR-9, CR-6, CR-7a | input_to; same_market_other_segment (sites for subsidized and other projects) | A-10, A-7 |
| C-24 | workers.construction | employment (construction) | increase | medium; long | CR-9, LW-10 | input_to: labor input_to construction | A-18, A-7 |
| C-25 | workers.construction, input_suppliers | wage_rate (+), price_paid (construction inputs) (+) | at_least_one_increase | medium | CR-9, CR-6 0.9, CR-7a | input_to (as C-24) | A-10, A-7 |
| C-26 | buyers.other_construction | quantity_traded (other construction: owner-occupied, commercial) | decrease | medium; long | CR-9, CR-4c, CR-8a | same inputs input_to other construction | A-10, A-7 |
| C-27 | renters | price_paid (rent) | increase | short (2028 to 2030) | CR-9, CR-10a, CR-6 | substitute: new rental homes and existing ones (close) | A-6, A-14 |
| C-28 | renters | price_paid (rent) | ambiguous | medium | CR-12b (follows C-12) | as C-27 | A-7, A-8, A-10, A-14 |
| C-29 | renters | price_paid (rent) | decrease | long | CR-9, CR-6, CR-10b | as C-27 | A-7, A-9, A-10, A-14 |
| C-30 | landlords.existing | asset_value (rental buildings; not counting effects through proximity) | decrease | short (from enactment) | CR-7c, CR-10c, CR-12b with A-16 | as C-27 | A-16, A-14, A-7, A-9 |
| C-31 | issuers.aldmere, taxpayers.state | interest_rate (Aldmere cities' and state's own exempt bonds) | increase | medium; long | CR-9, CR-6 | substitute: conduit bonds and other Aldmere exempt bonds for in-state buyers (partial) | A-19, A-2 |
| C-32 | holders.existing_aldmere_bonds | asset_value (outstanding Aldmere exempt bonds) | decrease | short (from enactment) | CR-7c, CR-10c | as C-31 | A-19, A-2 |
| C-33 | issuers.national_exempt | interest_rate (national exempt bonds) | increase | medium; long | CR-6 0.7 (a wider market moves by as much as the added quantity matters: $800 million against $400 billion) | substitute: conduit bonds and other exempt bonds (weak) | A-2, A-1 |
| C-34 | lenders.taxable | quantity_traded (taxable loans to rental projects) | decrease | medium; long | CR-9, CR-4 | substitute: exempt bonds for taxable loans (close) | A-12, A-2 |
| C-35 | borrowers.other | interest_rate | ambiguous | medium; long | CR-8 0.9 (the borrowing baseline), CR-12b | contract: loanable funds shared (partial) | A-12, A-7 |
| C-36 | taxpayers.national, recipients_of_other_national_spending | resources_available_other_uses | at_least_one_decrease | medium; long | CR-8 0.7 (payers from the general budget), CR-8 0.9 | — | A-20, A-1, A-2 |
| C-37 | taxpayers.state, recipients_of_other_state_spending | resources_available_other_uses | at_least_one_decrease | medium; long | CR-8 0.7, CR-8 0.9 | — | A-20, A-1, A-2 |
| C-38 | renters | quantity_traded (rental homes occupied) | increase | long | CR-9, CR-10b | as C-27 | A-7, A-9, A-10, A-14 |
| C-39 | landlords.existing (near new projects) | asset_value (rental buildings) | ambiguous | short (from enactment) | CR-12 0.9 (Tier C against Tier B): (−) C-30; (+) proximity (A-15) | proximity: new buildings and nearby blocks | A-16, A-15 |

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance premise | Combined sign |
|---|---|---|---|---|
| developers.winners, asset_value | exempt financing worth about $50,000 a unit (C-1) | issuer fee 0.5% of bonds (about $1,100 a unit); rent fall (about $5,000 a unit) | Arithmetic for the fee; A-17 (empirical, p 0.75) for the rent fall | increase (C-3) |
| rental construction started, 2027 | — | waiting for the first draw (A-6) | — | decrease (C-11) |
| rental construction started, 2028 to 2037 | added projects (A-7) | losers hold for the next draw (A-8); higher input prices crowd out unsubsidized projects (A-10) | Response argument covers crowding out only (a response cannot reverse the demand that causes it), and gives only "not below" without partiality; A-9 covers the long horizon only; holding is a second change, not covered | ambiguous (C-12) |
| rental construction started, after 2037 | added projects (A-7) | crowding out (A-10); holding is a one-time shift of the queue, not a lasting fall in the flow | CR-12e response argument with A-9 (crowding out is partial) | increase (C-13) |
| renters, price_paid | long: more homes (C-38) | short: delayed starts (C-10, C-11) | Different horizons not combined (CR-12g) | increase (short); ambiguous (medium); decrease (long) |
| landlords.existing, asset_value, short | delay raises rents for a few years | lasting addition to the stock lowers rents for the buildings' lives | A-16 (empirical, p 0.65) | decrease (C-30), Tier B, not counting effects through proximity |
| landlords.existing near new projects, asset_value | proximity: shops and services (A-15, Tier C) | C-30 | None for the Tier C chain | ambiguous at Tier C (C-39) |
| site_owners, asset_value, short | expected value of an entry carried by the site (A-4) | expected rent fall on the project built there (about $5,000 a unit) | A-17 (empirical): $17,000 against $5,000 | increase (C-21) |
| national and state tax_revenue | developers' smaller interest deductions | interest exempt that holders would have earned taxably | A-20 and arithmetic (1.8% against 0.45%; 0.33% against 0.09%) | decrease (C-4, C-5) |
| borrowers.other, interest_rate | bond buyers' funds withdrawn from other uses (CR-8a); added projects' borrowing (A-7) | lenders' funds freed from inframarginal projects (A-12) | none (CR-8 0.9: ambiguous without a premise on the difference) | ambiguous (C-35) |

## 8. Time structure

- **Announcement (January 2027 to March 2028).** The allocation is worth about 15% of cost, so some developers who would have closed taxable financing in 2027 wait (C-10, C-11). Site prices move from introduction, as the right to enter travels with site control (C-21). Existing landlords' and existing bondholders' values move when the Act becomes expected (C-30, C-32), partly at introduction and more at passage in April 2027 (CR-7c).
- **Timing shifts (CR-12h).** Construction starts: 2027 decrease (C-11); 2028 to 2037 ambiguous (C-12); after 2037 increase (C-13). Rents follow with a construction lag: short increase (C-27); medium ambiguous (C-28); long decrease (C-29). Holding by losers (A-8) is a shift of projects from one year to a later one; in a steady state it is a one-time enlargement of the queue, which is why it does not enter the long-run sign. Its persistence: n/a once the queue stops growing.
- **Annual cycle.** Applications by 31 January, draws in March, issuance by 31 December. Issuance bunches before the forfeiture deadline (CR-10a), and forfeited volume lapses, so volume actually used can fall short of the cap. Not recorded as a consequence: without the Act there is no issuance to compare with.
- **Durability (CR-10b).** Bonds run about 30 years; the exemption on issued bonds is expected to last (A-3), so the budget cost of each year's issue (C-4, C-5) and the lower interest on each project (C-1) persist for the bonds' life. Homes added (C-38) persist for the buildings' life, which is what A-16 relies on.
- **Expanding inputs.** Sites and inputs cannot expand at unchanged cost in the medium run (A-10), so crowding out is strongest then; over the long horizon they expand partly (A-9).
- **Contingent payments (U1-b).** Pledges made under U1-b bind for the bonds' life; shortfalls (A-22) arise over decades, so city taxpayers' payments (C-20) are long-run and contingent.

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-7 | developers.winners, developers.losers | compliance_cost (applications) | increase | $15,000 fees, site options, design and city approvals for about three applications per allocation | CR-8c |
| C-8 | officials.commission | enforcement_cost | increase | Staff time on draws and checks, paid from fees | CR-8c |
| C-9 | developers | reclassification (split or redesigned projects) | increase | Design and legal costs that serve only to qualify or gain entries | CR-8c |
| C-17 | developers | lobbying_effort (seeking city resolutions) | increase | Time and money spent winning councils' support | CR-8c |
| C-18 | lobby_groups | lobbying_effort (to keep or enlarge the program) | increase | Time and money | CR-8c |
| C-26 | buyers.other_construction | quantity_traded (other construction) | decrease | Homes and buildings not built because inputs moved to subsidized projects | CR-8a |
| C-14 | developers.unsubsidized | investment_target (projects without an allocation) | decrease | Rental projects crowded out by higher site and input prices | CR-8a |
| C-36 | taxpayers.national, recipients_of_other_national_spending | resources_available_other_uses | at_least_one_decrease | About $11 million a year per year's issue in national receipts that must be made up or not spent | CR-8b, CR-8 0.9 |
| C-37 | taxpayers.state, recipients_of_other_state_spending | resources_available_other_uses | at_least_one_decrease | About $1.9 million a year per year's issue | CR-8b, CR-8 0.9 |
| C-20 | city_taxpayers, recipients_of_other_city_spending | resources_available_other_uses | U1-a: no_change; U1-b: at_least_one_decrease | Shortfalls on pledged projects paid from general revenues | CR-8 0.8, CR-8 0.9 |

CR-8's symmetry: the transfer to winners (C-1, C-3) is matched by forgone national and state receipts (C-4, C-5, C-36, C-37); the issuer fee is paid by developers and received by cities (C-6); site owners' gain (C-21) is paid by developers through option prices; part of the value of each allocation is used up in entry costs (C-7, C-9, C-17; CR-7 0.7, competition to qualify). Inputs drawn into added projects are withdrawn from other construction (C-14, C-26).

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | Buyers accept yields on the bonds well below comparable taxable yields (about 4.7% against 6.5%) because the interest is exempt. | other | 0.9 | Yields on comparable exempt revenue bonds. | C-1 to C-5 and everything downstream fail. |
| A-2 | Developers apply, cities sponsor and issue, and the cap is used. | other | 0.9 | Developers' survey: about $2.4 billion of requests. | Most consequences fail. |
| A-3 | Holders expect the exemption on issued bonds to last for their term. | expectations | 0.85 | No retroactive change in the national rule's history. | C-1, C-3 weaken (holders demand higher yields). |
| A-4 | For many qualifying sites, an entry's expected value exceeds the cost of entering. | other | 0.85 | About $17,000 a unit at one-in-three odds against $1,000 to $2,000 a unit. | C-7, C-9, C-16, C-17, C-21, C-22 fail. |
| A-5 | Splitting or redesigning projects to qualify costs less than the extra entries are worth for some developers. | other | 0.6 | One application per site; lot splits; redesign costs. | C-9 fails. |
| A-6 | Some developers who would have closed taxable financing in 2027 wait for the first draw. | expectations | 0.75 | The allocation is worth about 15% of cost. | C-10, C-11, C-27 fail. |
| A-7 | Some projects are viable only at the lower rate and are built only if they win. | other | 0.75 | Projects' returns near the hurdle at 6.5%. | C-12, C-13, C-29, C-38 fail; C-24 to C-26 lose their chain. |
| A-8 | Some developers who lose a draw hold their project for the next one rather than proceed with taxable financing. | other | 0.55 | Carrying costs of land options against a later entry's value. | C-12 loses a (−) chain. |
| A-9 | Over the long horizon, sites and construction inputs can expand partly, so crowding out is partial. | other | 0.7 | Rezoning pace; construction labor inflows. | C-13 becomes "increase or no change"; C-29, C-38 likewise. |
| A-10 | In the medium and long run, sites and inputs cannot expand at unchanged cost, so their prices rise and some unsubsidized projects are not built. | other | 0.7 | Construction cost indexes; site scarcity. | C-14, C-15, C-22, C-23, C-25, C-26 fail; C-12 loses a (−) chain. |
| A-11 | Developers, cities and housing groups can organize at a cost below their stake. | other | 0.85 | Existing associations. | C-17, C-18 fail. |
| A-12 | Some winners' projects would have been financed with bank or insurer loans. | counterfactual_trend | 0.8 | Open eligibility: projects already planned apply. | C-34 fails; C-35 loses a chain. |
| A-13 | Cities that sponsor charge the issuer fee. | other | 0.8 | Fees in other conduit programs. | C-6 fails. |
| A-14 | Renters do not absorb added units at an unchanged rent. | substitutability | 0.8 | Vacancy at 4%; local rent responses to new supply. | C-15, C-27 to C-30, C-38 fail. |
| A-15 | New buildings bring shops and services that make nearby blocks more desirable to renters. | other | 0.55 | Retail openings near new buildings. | C-39 becomes decrease at Tier B only. |
| A-16 | In the value of existing rental buildings, the lasting addition to the stock dominates the temporary delay in building. | other | 0.65 | The delay lasts a few years; the addition lasts for the buildings' lives. | C-30 becomes ambiguous. |
| A-17 | An entry's expected value per unit (about $17,000) exceeds the present value of the rent fall per unit (about $5,000). | other | 0.75 | Section 1 figures; the rent effect is an empirical estimate. | C-3, C-21 become ambiguous. |
| A-18 | Construction employers adjust labor to volume. | alternative_uses | 0.75 | Labor per unit built. | C-24 fails. |
| A-19 | The market for Aldmere exempt bonds is partly segmented: in-state buyers are marginal, so added supply raises in-state yields. | other | 0.6 | Share held in-state; spreads between Aldmere and other states' bonds. | C-31, C-32 fail. |
| A-20 | Net national and state receipts fall: tax forgone on exempt interest exceeds tax gained on developers' smaller deductions. | other | 0.85 | About 1.8% against 0.45% of principal (national), 0.33% against 0.09% (state). | C-4, C-5, C-36, C-37 fail. |
| A-21 | Under U1-b, some cities pledge general revenues. | other | 0.6 | Cities compete for projects; a pledge lowers yields. | C-19, C-20 become no_change under U1-b. |
| A-22 | Some pledged projects fall short of debt service during the bonds' life. | other | 0.6 | Default rates on comparable revenue bonds over 30 years. | C-20 becomes no_change under U1-b. |
| A-23 | Under U1-a, a city would cover a defaulted project's debt service without a legal duty. | expectations | 0.25 | No such practice in Aldmere; councils' budgets are tight. | Below cut-off (see Not reported). |
| A-24 | Cities choose at their discretion which projects to sponsor. | other | 0.7 | The Act sets no criteria for resolutions. | C-16, C-17 fail. |
| A-N1 | Lenders to a city that pledges its general revenues count the pledge in the risk of the city's own general obligation bonds, although the debt-limit law does not count it. | other | 0.6 | NEW, flagged. Contingent pledges are a call on the same general revenues that secure the city's own bonds; buyers price that call whatever the legal limit says. Not among the case assumptions. | C-19 becomes no_change under U1-b. |

**Not reported** (an assumption below 0.5):
- Under U1-a, cities cover defaulted projects' debt service without a legal duty, so city taxpayers pay under both readings (CR-8 0.8, contingent payers): needs A-23 (p 0.25).

### Final check before the report

1. **Uncombined chains.** Construction starts, rents, existing landlords' values, site values, winners' values, tax receipts and other borrowers' rates are combined in section 7. The timing chains in section 8 are signed per window.
2. **Group signs.** Input prices (C-25) are a group: wages or material prices. Payers from budgets (C-36, C-37, C-20) are groups of actor classes. The lottery's displaced pressure (CR-6) is recorded on margins each with its own premise: site prices (a free price, C-21), entries (C-7), splitting (C-9), council criteria (C-16, C-17).
3. **Baseline.** Against Aldmere with the volume lapsing: the whole budget cost is added, and the rent effect is against 14,000 completions a year, not against today's rents.
4. **Worse off is not poorer.** `resources_available_other_uses` is signed only for payers of sums they cannot avoid (taxpayers through the budgets; city taxpayers under U1-b), not for unsubsidized developers or renters.
5. **Timing shifts.** 2027 starts and loans (C-10, C-11), later windows (C-12, C-13), rents (C-27 to C-29).
6. **Both sides of every transfer.** Exempt interest (C-1 against C-4, C-5, C-36, C-37); issuer fee (C-6, paid by winners: inside C-3's arithmetic); application fees (C-7 against C-8); site value (C-21, paid by developers); landlords' loss (C-30) against renters' long-run gain (C-29).
7. **Every actor class, every core rule.** CR-4: entry, splitting, waiting, holding, lobbying, pledging (per reading), lenders' and buyers' switching. CR-6: the lottery's fixed quantity (margins as above), rents, sites, inputs, bond yields. CR-7c: winners' allocations, sites, existing buildings, existing bonds, cities' own bonds under U1-b. CR-9: inputs, other construction, renters, lenders, other borrowers, other issuers, national market. CR-11: the Act conveys no information that changes rankings; no consequence recorded.
8. **Unstated premises.** A-N1 added for C-19. Organization (A-11), margins (A-4 to A-8) and the comparison of alternatives (A-17) are in the table.

## 11. Report

**The policy:** From 2028 Aldmere cities may issue bonds, payable from a private rental project's revenues, to finance new projects of 50 or more units. The interest is exempt from national and state income tax under existing law, up to $800 million a year, which before the Act lapsed unused. The state allocates that volume each March by lottery among developers with site control and a city resolution, in the amount each requests; each application costs $15,000, and cities may charge up to 0.5% of the bonds. It is unclear whether a city may pledge its general revenues as additional security.

**Visible consequences:** Developers who win borrow at about 4.7% instead of about 6.5% (C-1), and their projects gain value at each draw (C-3). Bond buyers get a new exempt asset (C-2). National and state receipts fall each year by about $11 million and $1.9 million for each year's issue (C-4, C-5), made up by other taxpayers or by less spending (C-36, C-37). Sponsoring cities collect fees (C-6).

**Invisible consequences:**
- *Developers and site owners:* each allocation draws about three applications, whose costs are used up (C-7), with projects split or redesigned to qualify (C-9) and councils lobbied for resolutions (C-16, C-17). Owners of qualifying sites gain from the Act's introduction and capture part of the subsidy (C-21, C-22). Unsubsidized developers face higher site and input prices, build less and earn less (C-14, C-15, C-23).
- *Timing:* rental starts and taxable loans fall in 2027 as developers wait for the first draw (C-10, C-11), so rents are higher in 2028 to 2030 (C-27). In the long run more rental homes are built and occupied (C-13, C-38) and rents are lower (C-29).
- *Landlords:* existing rental buildings lose value when the Act becomes expected (C-30).
- *Credit markets:* banks and insurers make fewer loans to rental projects (C-34); in-state exempt yields rise, raising other Aldmere issuers' borrowing costs and lowering existing bonds' values (C-31, C-32); national exempt yields rise slightly (C-33).
- *Construction:* more construction employment and higher wages or input prices (C-24, C-25); less other construction (C-26).
- *The state:* the Commission spends application fees on administration (C-8); developers, cities and housing groups lobby to keep or enlarge the program (C-18).

**Ambiguous effects:** Rental construction and rents in 2030 to 2037 (C-12, C-28): added projects push up the stock; projects held for the next draw and projects crowded out by higher input prices push down. Other borrowers' interest rates (C-35). Values of existing buildings near new projects, at Tier C (C-39). Per reading: under U1-a, city taxpayers bear nothing and cities' own borrowing costs are unchanged; under U1-b, pledging cities' own borrowing costs rise (C-19) and their taxpayers or other spending bear shortfalls on pledged projects (C-20).

**Key conditions:** Buyers accept exempt yields (A-1, p 0.9); the cap is used (A-2, p 0.9); some projects are built only if they win (A-7, p 0.75); inputs cannot expand at unchanged cost in the medium run (A-10, p 0.7) but partly can in the long run (A-9, p 0.7); the addition to the stock dominates the delay in landlords' values (A-16, p 0.65); in-state segmentation (A-19, p 0.6). One premise was added: lenders count pledges in a city's risk (A-N1, p 0.6).

**What this analysis cannot say:** How many homes are added, how far rents fall, or how the subsidy divides among site owners, developers and renters beyond the directions above. It does not weigh the gains to winners, site owners and renters against the costs to taxpayers and other builders, or say whether the policy is good. Health, safety and environmental effects are out of scope.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | developers.winners | interest_rate (project debt) | decrease | short; medium; long | visible | B | CR-1 (op 2: K1 adds the option of exempt bond financing to winners); CR-5c (buyers accept a lower yield because the interest is exempt, A-1, A-3); CR-7a (exempt yields settle about 1.8 points below taxable ones) | A-1, A-2, A-3 |
| C-2 | bond_buyers | quantity_traded (exempt conduit bonds for rental projects) | increase | short; medium; long | visible | B | CR-1 (op 2: a new exempt asset); CR-5 (exchanges take place that could not before); CR-12 0.9 (an activity that exists only under the policy) | A-1, A-2 |
| C-3 | developers.winners | asset_value (projects with an allocation) | increase | short (at each draw) | visible | B | CR-7c (an asset the policy creates is captured by whoever receives it at creation: the allocation is worth about $50,000 a unit); CR-10c; CR-12b and CR-12e: against the issuer fee (arithmetic: 0.5% of bonds, about $1,100 a unit) and against the rent fall on the project (A-17, empirical) | A-1, A-2, A-3, A-17 |
| C-4 | taxpayers.national | tax_revenue (national income tax) | decrease | medium; long | invisible | B | CR-8 0.9 (interest exempt from tax reduces receipts); CR-8b; CR-12b and CR-12e with A-20 and arithmetic (1.8% forgone against 0.45% from smaller deductions; the volume would otherwise lapse) | A-20, A-1, A-2 |
| C-5 | taxpayers.state | tax_revenue (state income tax) | decrease | medium; long | invisible | B | CR-8 0.9; CR-8b; CR-12e with A-20 and arithmetic (0.33% against 0.09%) | A-20, A-1, A-2 |
| C-6 | cities.sponsoring | non_tax_receipts (issuer fees) | increase | short; medium; long | invisible | B | CR-1 (K4 attaches a fee to using the bonds); CR-8b (developers' payment is the cities' receipt); CR-12 0.9 | A-13, A-2 |
| C-7 | developers.winners, developers.losers | compliance_cost (applications: fees, site control, city resolutions) | increase | short; medium; long | invisible | B | CR-4 (x: stay out, y: enter; an entry's value exceeds its cost, A-4); CR-8c (resources spent qualifying and entering are used up); CR-12 0.9 (exists only under the policy) | A-4, A-2 |
| C-8 | officials.commission | enforcement_cost | increase | short; medium; long | invisible | B | CR-1 (K5); CR-8c; CR-8b (funded by applicants' fees) | A-2 |
| C-9 | developers.winners, developers.losers | reclassification (projects split or redesigned to qualify or to gain entries) | increase | short; medium; long | invisible | B | CR-4 (x: one project on one site, or under 50 units; y: split into separately controlled sites, or enlarged to 50, gaining entries, A-5); CR-6 (the pressure from a fixed quantity at a zero price goes to the margins still open) | A-5, A-4 |
| C-10 | developers.unsubsidized (would-be 2027 borrowers) | quantity_traded (taxable rental project loans closed, 2027) | decrease | short (2027) | invisible | B | CR-10a (a change expected in 2028 alters choices in 2027); CR-4 (x: close now, y: wait for the first draw, A-6) | A-6 |
| C-11 | developers | investment_target (rental construction started, 2027) | decrease | short (2027) | invisible | B | CR-10a, CR-4 (as C-10); counterfactual: those projects start in 2027 | A-6 |
| C-12 | developers | investment_target (rental construction started, 2028 to 2037) | ambiguous | medium | invisible | B | CR-12b: (+) CR-4 (projects viable only at the lower rate are built, A-7); (−) CR-4 (losers hold for the next draw, A-8, a timing shift that the response argument does not cover); (−) CR-9 and CR-7a (higher site and input prices crowd out unsubsidized projects, A-10; the response argument gives only "not below" without partiality, which A-9 states for the long horizon only) | A-7, A-8, A-10 |
| C-13 | developers | investment_target (rental construction started, after 2037) | increase | long | invisible | B | CR-4 (A-7); CR-12e (crowding out is a response to the added demand for inputs and cannot reverse it); CR-12 0.9 (partial: inputs expand partly, A-9); holding (A-8) is a one-time shift in the queue, not a lasting fall in the flow (CR-10b) | A-7, A-9, A-10 |
| C-14 | developers.unsubsidized | investment_target (projects without an allocation) | decrease | medium; long | invisible | B | CR-9 (relation: same sites and inputs; the added projects bid for them, A-7); CR-7a; CR-4 (projects near the hurdle at the higher input price are dropped, A-10) | A-10, A-7 |
| C-15 | developers.unsubsidized | return_on_capital | decrease | medium; long | invisible | B | CR-9 and CR-7a (higher input costs, A-10, and lower rents in the long run, A-14, both lower the return on projects without exempt financing) | A-10, A-7, A-14 |
| C-16 | cities.sponsoring | allocation_by_non_price_criteria (which projects get a resolution) | increase | short; medium; long | invisible | B | CR-6 (a fixed quantity at a zero price: the pressure goes to the criteria by which the scarce side chooses; a city resolution is required and is given at the council's discretion, A-24); CR-2 | A-24, A-4 |
| C-17 | developers | lobbying_effort (seeking city resolutions) | increase | short; medium; long | invisible | B | CR-4 (x: apply for a resolution without effort, y: lobby the council; the resolution gates an entry worth more than its cost, A-4, A-24; A-11: they can organize); CR-8c | A-24, A-4, A-11 |
| C-18 | lobby_groups | lobbying_effort (to keep or enlarge the program) | increase | medium; long | invisible | B | CR-4 (x: accept, y: lobby; winners, site owners and cities have a stake, C-3, C-6, C-21; A-11); CR-8c | A-11 |
| C-19 | cities.sponsoring | interest_rate (own general obligation debt) | U1-a: no_change; U1-b: increase | medium; long | invisible | B | CR-1 per reading (U1-a: no pledge is allowed; U1-b: councils may pledge, A-21); CR-7c and CR-10c (a pledge is a contingent call on the revenues that secure the city's own bonds, so their expected yield to holders falls and the rate demanded rises, A-N1) | A-21, A-N1 |
| C-20 | city_taxpayers, recipients_of_other_city_spending | resources_available_other_uses | U1-a: no_change; U1-b: at_least_one_decrease | long | invisible | B | CR-8 0.8 (contingent payers recorded per reading); CR-8 0.9 (a reading that permits a source of funds: the payers are a group); U1-b: some cities pledge (A-21) and some pledged projects fall short (A-22); CR-8b | A-21, A-22 |
| C-21 | site_owners | asset_value (sites able to host 50 or more units) | increase | short (from introduction, January 2027) | invisible | B | CR-7 0.7 (claims before creation: the right to enter travels with site control, one application per site, so its value is capitalized into qualifying sites when the Act becomes expected, CR-7c, CR-10c); part of the value is used up in the competition to qualify (CR-8c); CR-12b with A-17 (entry value exceeds the rent fall) | A-4, A-2, A-17 |
| C-22 | site_owners | subsidy_share_received | increase | short; medium | invisible | B | CR-7b (the lasting gain settles on means that cannot move: qualifying sites are scarce, A-10, while developers' capital and skills can move to other projects) | A-4, A-10 |
| C-23 | site_owners (three largest cities) | price_paid (sites, paid by all developers) | increase | medium; long | invisible | B | CR-9 (relation: sites input_to rental projects; the added projects, A-7, raise demand for sites); CR-6 (with supply that cannot expand at unchanged cost, A-10, the price rises); CR-7a (sites for subsidized and other projects are the same market) | A-10, A-7 |
| C-24 | workers.construction | employment (construction) | increase | medium; long | invisible | B | CR-9 and LW-10 (relation: labor input_to construction; more projects, A-7, employers adjust labor to volume, A-18) | A-18, A-7 |
| C-25 | workers.construction, input_suppliers | wage_rate (+), price_paid (construction inputs) (+) | at_least_one_increase | medium | invisible | B | CR-9 (input_to); CR-6 0.9 (the shift in demand for inputs divides between price and quantity; supply cannot expand at unchanged cost, A-10, so at least one of the input prices rises) | A-10, A-7 |
| C-26 | buyers.other_construction | quantity_traded (other construction: owner-occupied, commercial) | decrease | medium; long | invisible | B | CR-9 (relation: same inputs input_to other construction); CR-4c (at higher input prices, the last units are given up); CR-8a (inputs directed to added projects are withdrawn from other uses) | A-10, A-7 |
| C-27 | renters | price_paid (rent) | increase | short (2028 to 2030) | invisible | B | CR-9 (relation: new rental homes substitute for existing ones); CR-10a (starts delayed in 2027, C-11, mean fewer completions about two years later); CR-6 (fewer homes than on the counterfactual path; renters do not absorb the difference at an unchanged rent, A-14) | A-6, A-14 |
| C-28 | renters | price_paid (rent) | ambiguous | medium | invisible | B | CR-12b (follows C-12: the stock is pushed up by added projects and down by holding and crowding out); CR-6 | A-7, A-8, A-10, A-14 |
| C-29 | renters | price_paid (rent) | decrease | long | invisible | B | CR-9 (relation: substitute); CR-10b (the stock grows through the added flow, C-13); CR-6 (more homes move the rent to a lower clearing level, A-14) | A-7, A-9, A-10, A-14 |
| C-30 | landlords.existing | asset_value (rental buildings; not counting effects through proximity) | decrease | short (from enactment) | invisible | B | CR-10c and CR-7c (the expected rent path, C-27 to C-29, is capitalized when the Act becomes expected); CR-12b with A-16 (empirical: the lasting addition dominates the temporary delay); CR-12 0.9 (Tier B sign not counting proximity) | A-16, A-14, A-7, A-9 |
| C-31 | issuers.aldmere, taxpayers.state | interest_rate (Aldmere cities' and state's own exempt bonds) | increase | medium; long | invisible | B | CR-9 (relation: conduit bonds substitute for other Aldmere exempt bonds for in-state buyers, who are marginal, A-19); CR-6 (added supply to a partly segmented market moves its yield up). Chain stops here at depth 4 (the issuers' taxpayers pay the higher interest) | A-19, A-2 |
| C-32 | holders.existing_aldmere_bonds | asset_value (outstanding Aldmere exempt bonds) | decrease | short (from enactment) | invisible | B | CR-7c and CR-10c (a rise in in-state yields, C-31, lowers the price of bonds already held, borne by holders when it becomes expected) | A-19, A-2 |
| C-33 | issuers.national_exempt | interest_rate (national exempt bonds) | increase | medium; long | invisible | B | CR-6 0.7 (a wider market moves in the CR-6 direction by as much as the added quantity matters: $800 million a year against $400 billion; the size is likely negligible, which this method does not measure) | A-2, A-1 |
| C-34 | lenders.taxable | quantity_traded (taxable loans to rental projects) | decrease | medium; long | invisible | B | CR-9 (relation: exempt bonds substitute for taxable loans); CR-4 (inframarginal winners switch, A-12; added projects borrow through bonds; crowded-out projects do not borrow) | A-12, A-2 |
| C-35 | borrowers.other | interest_rate | ambiguous | medium; long | invisible | B | CR-8 0.9 (the borrowing baseline: the counterfactual also borrows for inframarginal projects, so the effect on other borrowers is ambiguous without a premise on the difference); CR-12b: (−) lenders' funds freed (A-12); (+) bond buyers' funds withdrawn from other uses (CR-8a) and added projects' borrowing (A-7) | A-12, A-7 |
| C-36 | taxpayers.national, recipients_of_other_national_spending | resources_available_other_uses | at_least_one_decrease | medium; long | invisible | B | CR-8 0.9 (those who make up exempt interest's forgone receipts are payers); CR-8 0.7 (payers from the general budget are a group); CR-8b | A-20, A-1, A-2 |
| C-37 | taxpayers.state, recipients_of_other_state_spending | resources_available_other_uses | at_least_one_decrease | medium; long | invisible | B | CR-8 0.9; CR-8 0.7; CR-8b | A-20, A-1, A-2 |
| C-38 | renters | quantity_traded (rental homes occupied) | increase | long | invisible | B | CR-9 (relation: substitute); CR-10b (the stock grows by the added projects, C-13); CR-6 (at a lower rent more homes are taken, A-14) | A-7, A-9, A-10, A-14 |
| C-39 | landlords.existing (near new projects) | asset_value (rental buildings) | ambiguous | short (from enactment) | invisible | C | CR-12 0.9 (Tier C against Tier B): (−) C-30; (+) CR-9 through proximity (new buildings bring shops and services that make nearby blocks more desirable, A-15). No dominance premise; Tier C because the chain runs through a proximity relation | A-16, A-15 |

## Gaps found

**(a) Steps no core rule covers.**
- GAP-051-C1: Holding a project for a later draw in a repeated lottery. Whether losers who wait (A-8) lower the long-run flow of construction or only shift it once depends on a steady-state argument about the queue (inflow equals outflow once the queue stops growing). CR-10b and CR-12h cover timing shifts against a counterfactual, but no core rule states how a repeated, probabilistic allocation shifts a flow in the steady state; the argument was made from CR-10b by analogy.

**(b) Core-rule wording that was hard to apply.**
- CR-6 with a lottery: the main clause covers a fixed quantity at a free price; here the quantity is fixed and the price of the right is zero, set by rule. The "at least one margin" conclusion applies, but the free prices that absorb the pressure (site options, C-21) sit in a different market from the right itself; it is unclear whether that counts as the free price's rise under the 0.8 note or as a separate margin needing its own premise. Each margin was given its own premise.
- CR-12e response argument with two opposing responses: in the medium run (C-12), crowding out is covered by the response argument but holding (A-8) is not, and A-9 states partiality for the long horizon only. The 0.8 note covers a second change "the policy also causes", but holding is a response to the same change; the rule does not say whether a second response to the same change is covered.
- CR-8 0.9, the borrowing baseline: the note gives `ambiguous` for other borrowers' rates; it does not say whether the in-state segmentation premise (A-19) can sign the rate for a named subset of borrowers (other Aldmere exempt issuers) while the general rate stays ambiguous. Both were recorded (C-31, C-35).
- CR-7 0.7, claims before creation: the claim travels with site control, but the policy gives the right only with a winning draw and a city resolution. The note does not say how a claim conditional on a third party's discretion (A-24) divides between the site owner and the city.

**(c) Vocabulary missing from the ontology.**
- No variable for the number of applications or entries to an allocation; `compliance_cost` stood in for it.
- No variable for a contingent liability (a pledge not yet called); C-19 and C-20 used `interest_rate` and `resources_available_other_uses` per reading.
- No actor class for bond holders as a class distinct from `buyers.current`; `bond_buyers` and `holders.existing_aldmere_bonds` were introduced.
- No variable for the stock of housing as such; `quantity_traded (rental homes occupied)` stood in for it.

## Comparison with the pattern-based analysis

**Summary.** The two versions agree on the main structure of the Aldmere case. Winners borrow at the exempt rate and gain an allocation worth about $50,000 a unit. Bonds are issued, entry costs are used up, and projects are split or redesigned. Cities ration sponsorship by non-price criteria and collect fees. Rental starts fall in 2027 as developers wait for the first draw, are ambiguous for some years while losers hold projects, and rise in the long run once the crowding out of other builders is partial (A-9). Rents are lower in the long run, and existing landlords lose value from enactment, at Tier B. Qualifying sites gain (A-17). Taxable lenders lose these loans. In-state exempt yields rise and existing Aldmere bonds lose value (A-19). National and state receipts fall, net of developers' smaller deductions, and the payers are groups. City taxpayers are contingent payers under U1-b only. Both versions derive the value of a lottery entry and where it settles from the core rules: the core version does so through CR-7 0.7 (claims before creation) and CR-7b. That confirms the pattern version's finding that EN-12 is silent on it. The differences: the pattern version leaves the national exempt market's yield unrecorded as negligible where CR-6 asks for a sign (core C-33). It omits the short-run rise in rents that its own 2027 fall in starts implies, site prices paid by all developers, and other construction crowded out. Its windows for starts end the waiting period in 2032, where the core's end it in 2037. The core version signs construction labor alone where the derivable form is a group (C-24). It signs a lasting fall in unsubsidized developers' `return_on_capital` (C-15), which CR-7a rules out for mobile capital. It omits the Tier C rent and receipts consequences that CR-12 0.9 asks for, the intermediaries' new work and winners' issuance costs.

Counts: M 21, V 9, S 2, OP 9, OC 4.

### Pattern version → core version

| Pattern ID | Matched core ID(s) | Class | Cause | Note |
| --- | --- | --- | --- | --- |
| C-1 | C-1 | M | | |
| C-2 | C-2 | M | | |
| C-3 | C-3 | M | | The core combines the allocation with the issuer fee (arithmetic) and the rent fall on the project (A-17); the pattern signs it without either. For a winner the comparison is about $50,000 against about $1,100 and $5,000, so the sign holds. The pattern's dominance premise is implicit. |
| C-4 | C-7 | M | | |
| C-5 | C-9 | M | | |
| C-6 | C-11 | M | | The core also records taxable loans closed in 2027 (C-10). |
| C-7 | C-12 | V | | 2028 `ambiguous`. The core folds 2028 into one window, 2028 to 2037. |
| C-8 | C-12 | V | | 2029 to 2032 `ambiguous`; same chains (A-7 against A-8). The core adds crowding out (A-10) as a (−) chain in the medium run. |
| C-9 | C-12, C-13 | S | J | After 2037 both sign `increase` (core C-13). For 2033 to 2037 the pattern signs `increase` and the core `ambiguous`. Two questions are open: when the pool of waiting projects stops growing, and from when A-9 ("over the long horizon") makes crowding out partial. Each version defined its own horizons, and neither date follows from the record. Both are defensible; the core's GAP-051-C1 records that the steady-state argument is made by analogy. |
| C-10 | C-14 | M | | The core also records other construction (C-26). |
| C-11 | C-17, C-18 | V | | Split into lobbying councils for resolutions (C-17) and lobbying to keep or enlarge the program (C-18). |
| C-12 | C-34 | M | | |
| C-13 | C-6 | M | | |
| C-14 | C-8 | V | | The Commission's fee receipts. The core records them in C-8's derivation (CR-8b, "funded by applicants' fees") and in the final check (C-7 against C-8), not as a row. |
| C-15 | C-16 | M | | |
| C-16 | C-28 | V | | Rents `ambiguous` in the medium run; windows differ (2029 to 2032 against 2030 to 2037). See core C-27 for 2029 to 2030. |
| C-17 | C-29 | M | | The core does not qualify C-29 "not counting effects through proximity". See C-18. |
| C-18 | none | OC | E | Rents at Tier C `ambiguous` (proximity, A-15). CR-12 0.9 (Tier C against Tier B) asks for two consequences, the Tier B sign qualified and the combined Tier C sign. The core applied this only to landlords' value near new projects (C-39). Core-version omission. |
| C-19 | C-30, C-29 | V | | Landlords' `net_price_received` decrease. The core records it through the CR-8b pairing in its final check (landlords' loss against renters' gain), not as a row. |
| C-20 | C-30 | M | | |
| C-21 | C-21 | M | | The pattern dates it from passage, the core from introduction (CR-7c probability clause). Both are defensible. |
| C-22 | C-38 | V | | `capital_stock_target` (rental homes) in the pattern; `quantity_traded` (rental homes occupied) in the core, for lack of a stock variable (core Gaps c). |
| C-23 | C-25 | V | | Construction inputs as a group. The pattern groups price and quantity in the long run (CR-6 0.9 with A-9). The core groups the wage and input prices in the medium run (A-10), with quantity in C-24. Both are derivable with their premises. |
| C-24 | C-24 | S | E | Pattern: `employment`, `hours_worked` `at_least_one_increase`. Core: `employment` `increase`. A-18 ("adjust labor to volume") does not say heads rather than hours; CR-9 and LW-10 give only more demand for the labor. The derivable form is the group. Core-version error. |
| C-25 | C-31 | M | | |
| C-26 | C-32 | M | | |
| C-27 | C-4 | M | | |
| C-28 | C-36 | M | | |
| C-29 | C-5 | M | | |
| C-30 | C-37 | M | | |
| C-31 | C-20 | M | | |
| C-32 | none | OC | E | Underwriting, counsel, trustee and rating services rise (CR-9 input_to; CR-12 0.9, an activity that exists only under the policy). Derivable. Core-version omission. |
| C-33 | C-8 | M | | |
| C-34 | none | OC | E | Winners' issuance costs (CR-8c). Derivable as an item against a counterfactual with no issuance. Core-version omission; the core counts only the issuer fee, inside C-3. The pattern's figure (1.5% to 2% of each issue) is not in the policy record and no assumption carries it. The claim that these costs exceed those of arranging a bank loan needs a premise. |
| C-35 | none | OC | E | Landlords' receipts at Tier C `ambiguous`. As C-18: CR-12 0.9 asks for it. Core-version omission. |
| C-36 | C-39 | V | | Landlords' value at Tier C `ambiguous`. The pattern covers all existing landlords; the core restricts the row to buildings near new projects. |

### Core-only consequences

| Core ID | Class | Cause | Note |
| --- | --- | --- | --- |
| C-10 | OP | E | Taxable loans closed in 2027 decrease (CR-10a, CR-4, A-6). Derivable; the pattern records only starts. Pattern-version omission. |
| C-15 | OP | E | Unsubsidized developers' `return_on_capital` `decrease` in the medium and long run. CR-7a: the yields on means that can move are brought back into line. CR-7b: the lasting loss settles on means that cannot move, here sites, existing buildings and their owners. The core's own C-22 says developers' capital and skills can move to other projects. At most a transitional fall is derivable, and only with a premise on the speed of exit. Core-version error. |
| C-19 | OP | A | Pledging cities' own general obligation rate, per reading: U1-a `no_change`, U1-b `increase`. The core added A-N1 (lenders count a pledge in the city's risk although the debt limit does not). The pattern uses the same chain without a premise, as a "further (+) chain" on in-state exempt yields inside its C-25, and records no key for it. A difference of premises. The core's A-N1 is the premise the chain needs. |
| C-22 | OP | J | Site owners' `subsidy_share_received` `increase` (CR-7b). Against a counterfactual with no subsidy, any share is an increase, so this restates C-21. The pattern declined to say how the subsidy divides. Adds no sign. |
| C-23 | OP | E | Site prices paid by all developers rise in the medium and long run (CR-9, CR-6, A-10). The pattern uses the chain inside C-10 and C-21 but records no row, and its input group (C-23) leaves out sites. Pattern-version omission. |
| C-26 | OP | E | Other construction (owner-occupied, commercial) decreases (CR-9 through shared inputs, CR-4c, CR-8a, A-10). The pattern stopped at owner-occupied prices (depth 3) and did not record the quantity. Derivable; pattern-version omission. |
| C-27 | OP | E | Rents `increase` in the short run (fewer completions after the 2027 dip in starts, A-6, A-14). The pattern's own C-6 implies it, and its C-16 starts the medium window in 2029 at `ambiguous`. Pattern-version omission. The core version's derivation, though, rests on a construction lag ("about two years later") that no assumption carries. Its window also runs to 2030, when projects held back from 2027 and started in 2028 are completing, so 2030 belongs with the `ambiguous` window. The sign is derivable for about 2029 with a stated lag premise. |
| C-33 | OP | P | The national exempt market's yield rises (CR-6 0.7: a wider-market price moves in the CR-6 direction; record its sign, with a premise if it may be negligible). Against the counterfactual the volume lapses, so this is added exempt supply, not a baseline swap. OC-8 0.9's small-borrower clause, applied as written, records the effect "as negligible". That departs from CR-6, which asks for the sign. |
| C-35 | OP | J | Other borrowers' rate `ambiguous` (CR-8 0.9, borrowing baseline). The pattern reaches the same sign and leaves it unrecorded as negligible, which is defensible for an `ambiguous` sign. |

### Findings

- **Pattern overclaims or hidden premises.** No pattern claim was found unsupported by the core rules. The pattern's signs for allocations (C-3) rest on an implicit dominance over the issuer fee and the rent fall, which the figures supply. Its issuance costs (C-34) use a figure absent from the record. Its "further (+) chain" from city pledges onto the rates of in-state exempt bonds (C-25) needs a premise like the core's A-N1. Left unsigned: the national exempt yield (core C-33), recorded as negligible under OC-8 0.9's small-borrower clause, which conflicts with CR-6 0.7 and 0.8.
- **Errors in the core version.** Construction labor signed as `employment` alone (C-24), where the group is the derivable form. A lasting fall in unsubsidized developers' `return_on_capital` (C-15) contradicts CR-7a and the core's own C-22. The short-run rent rise (C-27) rests on an unstated lag and runs one year too long. Omissions: the Tier C rent and receipts consequences (pattern C-18, C-35) that CR-12 0.9 asks for; intermediaries' work (C-32); winners' issuance costs (C-34).
- **Errors in the pattern version (omissions).** Taxable loans closed in 2027 (core C-10); the short-run rent rise (C-27); site prices paid by all developers (C-23); other construction crowded out (C-26); the national exempt yield (C-33, a pattern-as-written cause); pledging cities' own borrowing rate as a key with its premise (C-19).
- **Test of 0.9 verdicts.** No item was marked "failed". The "needed interpretation" verdicts and their equivalents: *OC-8 0.9, small borrower (needed interpretation: small nationally, not in the in-state segment):* confirmed. The core version signed in-state yields and existing bonds (C-31, C-32) from CR-6 and CR-9 with A-19, and did not need the clause. It also shows a second defect: the clause's "recorded as negligible" conflicts with CR-6, which records the national exempt yield's sign (C-33). *CR-12 0.9, what the response argument gives (needed interpretation: partial means that inputs can expand):* confirmed. The core version used the same inverted premise (A-9) for C-13, and its Gaps (b) found a further problem: the response argument covers crowding out but not a second response to the same change (holding, A-8). *GAP-039-C2, value of a lottery entry (resolved with interpretation):* confirmed as resolvable from the core rules. The core version reached C-21 through CR-7 0.7 (claims before creation) rather than CR-7c's probability clause. It raised a point the pattern version did not: how a claim conditional on a third party's discretion (the city's resolution) divides between the site owner and the city. *EN-12, open eligibility (incomplete on where the value settles):* confirmed. Without EN-12 the core version derived the split among entry costs (C-7, C-9, C-17), site owners (C-21, C-22) and winners (C-3). *CR-8 0.9, borrowing baseline (needed extending to the homes):* confirmed in effect. The core version applied the same baseline to the homes through A-7 (C-12, C-13), without comment. *OC-8 0.9, tax-exempt interest (worked with an addition: developers' smaller deductions):* confirmed. The core version needed the same arithmetic (A-20) for C-4 and C-5. *CR-8 0.9 with CR-8 0.8 (two premises under U1-b):* confirmed; the same two premises (A-21, A-22) were used for C-20.
- **Limits of the core rules.** None produced a difference: no S, OP or OC row has cause K. Unclear core-rule wording: (1) CR-12e 0.9: "the response must be partial: state that supply cannot fully expand" assumes the response is an expansion. Where the response is a contraction by rivals through input prices, partiality needs inputs that can expand (A-9). (2) CR-12e with two responses to the same change: crowding out is covered and holding is not (core Gaps b). (3) No rule states how a repeated, probabilistic allocation shifts a flow in the steady state (GAP-051-C1). It was argued from CR-10b, and the two versions placed the end of the waiting period five years apart (C-9). (4) CR-7 0.7, claims before creation, where the claim also needs a third party's discretionary approval. (5) CR-6 0.8, "a free price's rise is enough", where the free price (site options) sits in a different market from the rationed right. (6) CR-7a against CR-7b for a lasting `return_on_capital` sign on mobile capital: the text is clear, but nothing in the workflow's final check prompts the analyst to test it (C-15).
