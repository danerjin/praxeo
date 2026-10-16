# WE-020 / Core-only re-run: Grant to first-time homebuyers

Analyst: core-only re-run (Handbook 0.4)  |  Rules: core rules CR-1 to CR-12 only  |  Status: awaiting comparison

## 1. Policy record

**Tamberlay Home Start Grant.** Tamberlay is a state of about 3 million people. About 60,000 homes are sold there in a normal year, roughly a third of them for $450,000 or less, and first-time buyers account for about 18,000 purchases. Builders complete about 12,000 new homes a year; zoning approval and permits take 12 to 24 months and construction another 9 to 15, so the stock of homes responds slowly to prices. Tamberlay's largest city, Kessford, sits on the border with the state of Lowen, whose suburbs are within a 30-minute commute and which has no comparable grant. Entry-level home prices in Tamberlay have been rising about 4% a year.

The governor announced the grant in the budget speech on 10 March of Year 1. The legislature enacted it on 15 May. It applies to purchase contracts signed from 1 July of Year 1 to 30 June of Year 4, with a legislative review in Year 3. Renewal is possible but not promised.

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Grant | `purchase_rebate` | Purchase of a home in Tamberlay | First-time buyers who apply | $15,000, paid at settlement and usable toward the deposit. Contract price must be $450,000 or less (fixed in money terms). The home must be the buyer's principal residence for 24 months; otherwise the full grant is repaid. | — |
| K2 Eligibility | Condition of K1 | Applicants | Applicants | Neither the applicant nor the applicant's spouse or declared partner has ever owned residential property, anywhere. Ownership in Tamberlay is checked against the land register; ownership elsewhere and partner status are by sworn declaration. One grant per household. | — |
| K3 Funding | Funding of K1 and K4 | — | State budget | Annual appropriation from general revenue, about $300 million a year (20,000 grants). The law does not say what happens if applications exceed the appropriation. | — |
| K4 Administration | Enforcement | K1 and K2 | State Revenue Office | Checks land register and declarations; checks occupancy against driver's license and electoral roll addresses; clawback and fines for false declarations. | — |

Unclear provisions: whether the price cap will be indexed if prices rise (the text fixes it in dollars); whether the grant will be renewed after Year 4. Both are treated as expectations (A-3, A-15).

## 2. Classification

CR-1 operations: 1 remove an option, 2 add an option, 3 change what an option brings, 4 transfer means.

| Component | Rothbard type | Binding? (assumption ID) | Core rules | CR-1 operations, by actor class |
|---|---|---|---|---|
| K1 | binary (a transfer from the state, conditional on a purchase) | Yes: the deposit binds for many first-time buyers (A-4) | CR-1, CR-4, CR-6, CR-7, CR-9, CR-10 | First-time buyers: 4 ($15,000) and 3 (attached to buying a home at or under $450,000, and a repayment attached to moving within 24 months). Owners under the cap, builders, landlords: none directly (felt through CR-9). |
| K2 | condition of K1 | Yes | CR-1, CR-4 | Households with a prior owner: none (excluded); applicants: 3 (declarations). |
| K3 | binary (general revenue) | Yes | CR-1, CR-8 | Taxpayers: 4. |
| K4 | enforcement | Routine checks; nominee buying not reported (A-14) | CR-1, CR-8c | Applicants: 3 (clawback, fines). |

## 3. Actor classes

| Actor class | Role | How its options change (CR-1) |
|---|---|---|
| buyers.first_time | Households that have never owned | Buying under the cap now brings $15,000 (3, 4); moving within 24 months brings repayment (3). |
| buyers.non_grant | Repeat buyers and investors buying under the cap | No direct change; compete with grant holders (CR-9). |
| buyers.above_cap | Buyers of homes above $450,000, including owners trading up | No direct change (CR-9). |
| owners.under_cap, owners.just_above_cap | Owners who may sell | No direct change; demand for their homes changes (CR-9). |
| households with a prior owner | Excluded by K2 | Option to qualify by arranging title or declarations (CR-4). |
| builders, construction_labor, buyers of other construction | New supply | No direct change; yield of entry-level building rises (CR-7). |
| landlords of entry-level homes, renters | Rental market | No direct change; owner-occupation becomes cheaper for some tenants (CR-9). |
| intermediaries (real estate agents) | Paid on sales | No direct change (CR-9). |
| neighboring_jurisdictions (Lowen home sellers) | Suburbs within a 30-minute commute | No direct change (CR-9). |
| taxpayers, officials.enforcement | Fund and administer | Transfer (4); new duties. |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | buyers.first_time (grant recipients) | price_paid (homes under the cap, net of the grant) | decrease | short | CR-1 op. 4 ($15,000 paid at settlement); CR-12b resolved by A-1 against the contract-price rise (C-16) | A-1 |
| C-2 | buyers.first_time (grant recipients) | quantity_traded (first-time purchases under the cap) | increase | short | CR-4b (x: keep renting or saving, y: buy now with the grant toward the deposit) | A-1, A-4 |

## 5. Responses

CR-4 for each pair of options:

- **First-time buyers.** (x: keep renting, y: buy now) (C-2); (x: buy in Lowen, y: buy in Tamberlay) (C-6); (x: buy before July, y: wait) under CR-10a (C-3); (x: sign after the deadline, y: sign before) (C-5); (x: take a job requiring a move, y: stay) (C-10). Their saving changes in both directions under CR-4's exception for changes in total means (C-7).
- **Households with a prior owner.** (x: covered form, y: uncovered form): arrange title or declarations (C-8).
- **Owners.** Some hold listings until July (CR-10a) (C-4); owners just above the cap move value outside the contract price (CR-4b) (C-9).
- **Builders and landlords.** Builders move means to entry-level homes (CR-7a) (C-11); landlords sell to grant holders (CR-4b) (C-12).
- **Organized interests.** (x: accept, y: lobby) (C-13).

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-3 | buyers.first_time (prospective) | quantity_traded (first-time purchases, 10 March to 30 June of Year 1) | decrease | short | CR-10a; CR-4b (x: buy before 1 July, y: wait for the grant) | A-5 |
| C-4 | owners.under_cap (sellers.current) | quantity_supplied (listings under the cap, 10 March to 30 June of Year 1) | decrease | short | CR-10a; CR-4b (x: list now, y: list after 1 July, when buyers have the grant) | A-6 |
| C-5 | buyers.first_time (prospective) | quantity_traded (first-time purchases, months before 30 June of Year 4) | increase | medium | CR-10a (renewal uncertain at the deadline, so buyers who can sign earlier do) | A-16 |
| C-6 | buyers.first_time (prospective) | cross_border_purchases (homes in Lowen suburbs) | decrease | medium | CR-4b (x: buy in Lowen, y: buy in Tamberlay with the grant) | A-12 |
| C-7 | buyers.first_time (prospective) | saving | ambiguous | medium | CR-4 exception (the grant changes total means toward a fixed deposit sum): (-) the deposit target is reached with less own saving; (+) buying sooner raises the payoff to saving now; CR-12b | A-4 |
| C-8 | households with a prior owner | reclassification (title and partner declarations arranged to qualify) | increase | short | CR-4b (x: the covered form, a household with a prior owner; y: the uncovered form, title or declarations arranged to show none) | A-7 |
| C-9 | owners.just_above_cap | reclassification (value moved outside the contract price) | increase | medium | CR-4b (x: contract above the cap, y: contract at the cap with other items paid separately); grows as prices rise against a cap fixed in money (CR-10) | A-8 |
| C-10 | buyers.first_time (grant recipients) | job_changes | decrease | medium | CR-1 op. 3 (the grant is repaid if the home stops being the principal residence within 24 months); CR-4b (x: take a job that needs a move, y: stay) | A-9 |
| C-11 | builders (sellers.prospective) | investment_target (homes under the cap) | increase | long | CR-7a (means move toward the use whose yield rose); CR-4b (x: build above the cap or other projects, y: build entry-level homes) | A-3, A-10 |
| C-12 | landlords of entry-level homes | quantity_supplied (rental units, entry-level) | decrease | medium | CR-4b (x: keep renting the home out, y: sell it to a grant holder at the higher price); CR-7a | A-13, A-2 |
| C-13 | owners, builders and agents | lobbying_effort | increase | medium | CR-4b (x: accept expiry or a fixed cap, y: lobby for renewal or indexation), at the Year 3 review | A-17 |

## 6. Second-order effects

Depth limit 4; prune diffuse bystander effects after depth 3. Relations used: grant and non-grant buyers of homes under the cap: same market, other segment; homes under and above the cap: same market, other segment; renting and owning an entry-level home: substitute; Tamberlay and Lowen suburbs: across_border, close for Kessford-area buyers (A-12); construction labor and agents' services: input_to.

Chains:
1. K1 (1) planned purchases under the cap rise against slow supply (2) contract prices and owners' asset values rise from March, part of the grant settling on owners (C-16, C-14, C-15) (3) non-grant buyers buy fewer homes under the cap and some move to Lowen (C-17, C-18).
2. K1 (1) owners' homes rise in value (2) some use the gain to bid for larger homes (3) prices above the cap rise (C-22).
3. K1 (1) renters buy and landlords sell to grant holders (2) fewer rental units let; rents pushed both ways (C-21, C-20).
4. K1 (1) first-time buyers move from Lowen and non-grant buyers move to Lowen (2) Lowen prices pushed both ways (C-19).
5. K1 (1) builders build more entry-level homes (2) construction labor is bid away from other uses (3) wages rise and other projects are given up (C-23, C-24).
6. K1 (1) more sales at higher prices (2) agents' earnings (C-25).

Component interactions: K2's declaration-based check leaves an exit from K2 for households with a prior owner (C-8); K3 funds K1 from general revenue, so every grant is a taxpayers' outlay (C-26); K3's silence on over-subscription means that if applications exceed 20,000 a year the allocation is unclear, and no sign is recorded for it.

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-14 | owners.under_cap (sellers.current) | asset_value (homes under the cap) | increase | short | CR-7c (a lasting rise in expected sale value is captured by owners when it becomes expected, from March); CR-7b (owners have fewer alternatives than first-time buyers while supply is slow) | same market | A-2, A-3, A-20 |
| C-15 | owners.under_cap (sellers.current) | subsidy_share_received | increase | short | CR-7b (the benefit of the grant settles on the side with fewer alternatives) | same market | A-2, A-20 |
| C-16 | buyers.non_grant (repeat buyers and investors in the segment) | price_paid (homes under the cap, contract price) | increase | short | CR-6 first paragraph (planned purchases rise against slow supply); CR-9 (they compete with grant holders for the same homes) | same_market_other_segment (grant and non-grant buyers) | A-2, A-20 |
| C-17 | buyers.non_grant (repeat buyers and investors in the segment) | quantity_traded (homes under the cap) | decrease | medium | CR-4c after C-16 | same_market_other_segment | A-2, A-20 |
| C-18 | buyers.non_grant (repeat buyers and investors in the segment) | cross_border_purchases (homes in Lowen suburbs) | increase | medium | CR-4b (x: buy in Tamberlay at the higher price, y: buy in Lowen) | across_border (Lowen suburbs within a 30-minute commute) | A-2, A-12, A-20 |
| C-19 | neighboring_jurisdictions (Lowen home sellers) | price_substitute (Lowen suburban homes) | ambiguous | medium | (-) CR-9: first-time buyers move to Tamberlay (C-6); (+) CR-9: non-grant buyers move to Lowen (C-18); CR-12b | across_border | A-2, A-12, A-20 |
| C-20 | renters (buyers of rental housing) | price_substitute (entry-level rents) | ambiguous | medium | (-) CR-9: renters who buy leave the rental market (substitute); (+) CR-9: landlords sell units to grant holders (C-12); CR-12b | substitute (renting and owning an entry-level home) | A-4, A-13 |
| C-21 | renters (buyers of rental housing) | quantity_substitute (entry-level rental units let) | decrease | medium | CR-9: both chains in C-20 reduce the number of units let; CR-12a | substitute (renting and owning) | A-4, A-13 |
| C-22 | buyers.above_cap (trade-up buyers) | price_paid (homes above the cap) | increase | medium | CR-4 exception (the rise in owners' means from C-14 shifts their choices); CR-6 first paragraph in the segment above the cap | same_market_other_segment (homes above the cap) | A-18, A-19, A-2, A-20 |
| C-23 | construction_labor | wage_rate | increase | long | CR-9, LW-10 (demand for construction labor follows entry-level building, C-11); CR-7a (labor drawn from other uses only at higher pay, since it is fully used) | input_to (construction labor to new homes) | A-10, A-11 |
| C-24 | buyers of other construction | quantity_traded (other construction projects) | decrease | long | CR-8a (labor and builders moved to entry-level homes are withdrawn from other projects); CR-7a | input_to (shared construction labor) | A-10, A-11 |
| C-25 | intermediaries (real estate agents) | earnings | increase | medium | CR-9, LW-10 (demand for agents' services follows the number and price of sales) | input_to (agents' services to home sales) | A-4, A-N1 |

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance premise | Combined sign |
|---|---|---|---|---|
| buyers.first_time, price_paid (net of grant), short | Contract price rises (CR-6, CR-7b with A-20) | $15,000 grant (CR-1 op. 4) | A-1: prices rise by less than the grant. CR-7b with A-20 says only that owners capture part; A-1 is an empirical premise | decrease |
| buyers.first_time, saving, medium | Buying sooner raises the payoff to saving now | Deposit target reached with less own saving | None (CR-4 exception) | ambiguous (CR-12b) |
| renters, price_substitute (rents), medium | Landlords sell units (CR-9) | Renters leave to buy (CR-9) | None | ambiguous (CR-12b) |
| renters, quantity_substitute (units let), medium | None | Both chains | Not needed | decrease (CR-12a) |
| neighboring_jurisdictions, price_substitute (Lowen homes), medium | Non-grant buyers move to Lowen | First-time buyers move from Lowen | None | ambiguous (CR-12b) |

The owners' gain (C-14) is matched by non-grant buyers' outlay (C-29) and, for grant holders, by taxpayers (C-26) (CR-8 symmetry). Different variables are not netted (CR-12c).

## 8. Time structure

- **Announcement to start (CR-10a).** Announced 10 March, applying from 1 July of Year 1: first-time purchases are held back (C-3) and some owners hold listings (C-4). Owners' asset values rise from the announcement, not from the start (CR-7c).
- **Slow supply (CR-10b).** Approval and construction take two to three years, so in the short and medium run the grant shows up in prices; the supply response (C-11) arrives in the long run, after the review in Year 3, and depends on builders expecting the grant to last (A-3).
- **Cap fixed in money terms.** With entry-level prices rising about 4% a year, and the grant itself pushing prices under the cap up, the share of homes under $450,000 shrinks each year (arithmetic), so the grant reaches fewer homes over time and bunching at the cap (C-9) grows.
- **Deadline.** With renewal uncertain at the Year 4 deadline (A-16), purchases are pulled into the months before 30 June of Year 4 (C-5). Whether a dip follows depends on non-renewal (A-15, p 0.4); not reported.
- **Lock-in.** The 24-month residence condition reduces job moves for two years after each purchase (C-10).

## 9. Opportunity costs

CR-3 and CR-8. Symmetry: grants are taxpayers' outlay; owners' gains from higher prices are non-grant buyers' outlay and, through the grant, taxpayers'.

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-26 | taxpayers | resources_available_other_uses | decrease | Other state spending or lower taxes | CR-8a, CR-8b (about $300 million a year from general revenue; every grant counted as a gain is matched here) |
| C-27 | officials.enforcement (State Revenue Office) | enforcement_cost | increase | Staff time for other public uses | CR-8c; K4 |
| C-28 | buyers.first_time (applicants) | compliance_cost | increase | Applicants' time | CR-1 op. 3; CR-8c (applications, sworn declarations, occupancy proof) |
| C-29 | buyers.non_grant (repeat buyers and investors in the segment) | resources_available_other_uses | decrease | Other spending by non-grant buyers | CR-8b (the owners' gain in C-14 is the matching outlay of buyers who pay the higher price without a grant); CR-3a |

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | Prices under the cap rise by less than the grant, because many buyers in the segment get no grant and some supply responds. | other | 0.7 | Share of segment purchases by first-time buyers; listings and price data after the announcement; studies of comparable grants. | Net price to grant holders ambiguous. |
| A-2 | The supply of homes under the cap responds slowly. | durability | 0.85 | Approval and build times; vacancy rate; pipeline of approved projects. | Little price or asset-value rise. |
| A-3 | Buyers, sellers and builders expect the grant to last at least through Year 4. | expectations | 0.75 | Statutory window; budget commitment; political support. | Smaller capitalization; no building response. |
| A-4 | Some renters at the margin buy sooner because of the grant. | substitutability | 0.85 | Rent-to-price ratios; deposit as the binding constraint for first-time buyers (mortgage data). | No added purchases. |
| A-5 | First-time buyers knew of the grant from March and could delay. | expectations | 0.85 | Publicity of the budget speech; agents' reports. | No pre-start dip. |
| A-6 | Some owners delay listing to sell after July. | expectations | 0.55 | Listings data around comparable announcements. | No listing dip. |
| A-7 | Couples can arrange title or partner declarations so that a prior owner's household qualifies. | enforcement | 0.6 | Declaration-based partner check; no register outside Tamberlay. | No title reclassification. |
| A-8 | Sellers just above the cap can move value outside the contract price. | other | 0.6 | Legal definition of contract price; bunching at price thresholds in transfer data. | No price reclassification. |
| A-9 | Some recipients receive job offers in the first 24 months that would require moving. | mobility | 0.7 | Job-change rates of young households; size of labor markets within commuting distance. | No lock-in. |
| A-10 | Builders can obtain approvals for entry-level projects within a few years. | alternative_uses | 0.65 | Zoning capacity; approval rates. | No building response. |
| A-11 | Construction labor and builders are scarce and fully used elsewhere. | other | 0.8 | Construction employment and vacancy rates. | No wage rise or crowding. |
| A-12 | Many Kessford-area buyers can choose between Tamberlay and Lowen suburbs. | mobility | 0.7 | Commute times; existing cross-border home buying. | No cross-border chains. |
| A-13 | Some landlords of entry-level homes sell to grant holders. | alternative_uses | 0.7 | Share of segment homes owned by small landlords; rental yields against sale prices. | Rents fall; no rental-supply chain. |
| A-14 | Investors use nominee buyers on a meaningful scale. | enforcement | 0.3 | Occupancy checks; penalties. | Below cut-off; not used. |
| A-15 | The grant is not renewed after Year 4. | expectations | 0.4 | Budget pressure; lobbying; legislative review. | Below cut-off; not used. |
| A-16 | Renewal is uncertain at the deadline, and some buyers can sign a few months earlier. | expectations | 0.7 | Timing of the Year 3 review; flexibility of purchase timing. | No deadline rush. |
| A-17 | Owners, builders and agents can organize to lobby. | other | 0.85 | Existing builders' and agents' associations. | No lobbying. |
| A-18 | Owners whose homes rise in value use part of the gain to bid for larger homes. | other | 0.6 | Trade-up rates; equity-financed deposits. | No above-cap chain. |
| A-19 | Owners can realize the gain by selling or borrowing against the home, and it is not offset by an equal rise in the price of what they buy next (the grant does not apply above the cap). | other | 0.75 | Home-equity lending terms; trade-up rates; price changes above and below the cap after the announcement. | No above-cap chain. |
| A-20 | While supply is slow, owners of homes under the cap have clearly fewer alternatives than first-time buyers, who can keep renting, wait, buy above the cap or buy in Lowen's suburbs. | substitutability | 0.7 | Approval and build times (A-2); rent-to-price ratios; cross-border buying (A-12). | Owners' share ambiguous. |
| A-N1 | Real estate agents are paid mainly by commission on each sale. | other | 0.85 | Agents' fee practice in Tamberlay; agents' association schedules. | C-25 becomes ambiguous. |

**Not reported** (an assumption below 0.5):
- Investors buying through nominees: `informal_activity` increase and higher `enforcement_cost` (A-14, p 0.3).
- A purchase dip after 30 June of Year 4 and a fall in owners' `asset_value` at non-renewal (A-15, p 0.4).

## 11. Report

**The policy:** From 1 July of Year 1 to 30 June of Year 4, a household that has never owned a home gets $15,000 at settlement toward buying a home in Tamberlay for $450,000 or less, provided it lives there for 24 months. Ownership elsewhere and partner status are by sworn declaration. About $300 million a year comes from general revenue.

**Visible consequences:** Grant holders pay less, net (C-1), and more first-time purchases happen (C-2); purchases pause between the March announcement and July (C-3); owners of homes under the cap see their values rise from March (C-14); the Revenue Office administers the grant (C-27).

**Invisible consequences:**
- *Owners and other buyers:* part of the grant settles on owners (C-15); repeat buyers and investors in the segment pay more, buy fewer homes there and some buy in Lowen (C-16, C-17, C-18, C-29); owners trading up push prices above the cap (C-22); some owners hold listings until July (C-4); owners just above the cap move value outside the contract price (C-9).
- *First-time buyers:* fewer buy in Lowen (C-6); recipients turn down job moves for two years (C-10); a rush before the Year 4 deadline (C-5); paperwork (C-28); some households with a prior owner arrange title or declarations to qualify (C-8).
- *Rental market:* fewer entry-level units let (C-21), as renters buy and landlords sell (C-12).
- *Construction:* in the long run, more entry-level building (C-11), higher construction wages (C-23) and fewer other projects (C-24).
- *Others:* agents earn more (C-25); owners, builders and agents lobby for renewal and indexation (C-13); taxpayers fund the grants (C-26).

**Ambiguous effects:** Entry-level rents (renters leave, but landlords sell) (C-20); Lowen home prices (first-time buyers leave, non-grant buyers arrive) (C-19); first-time buyers' saving (less is needed, but buying sooner pays more) (C-7).

**Key conditions:** Supply responds slowly (A-2, 0.85) and owners have fewer alternatives than first-time buyers (A-20, 0.7), so part of the grant goes to owners; prices rise by less than the grant (A-1, 0.7); the deposit binds for some renters (A-4, 0.85); actors expect the grant to last through Year 4 (A-3, 0.75). One new premise: agents are paid by commission (A-N1, 0.85).

**What this analysis cannot say:** how large any change is, including how much of the grant goes to owners; whether gains to grant holders and owners outweigh costs to taxpayers, non-grant buyers and renters; whether the policy is good. What happens if applications exceed the appropriation is not stated in the law and is not signed here. Health, safety and environmental effects are out of scope for version 1 and are not analyzed here.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | buyers.first_time (grant recipients) | price_paid (homes under the cap, net of the grant) | decrease | short | visible | B | CR-1 op. 4 ($15,000 paid at settlement); CR-12b resolved by A-1 against the contract-price rise (C-16) | A-1 |
| C-2 | buyers.first_time (grant recipients) | quantity_traded (first-time purchases under the cap) | increase | short | visible | B | CR-4b (x: keep renting or saving, y: buy now with the grant toward the deposit) | A-1, A-4 |
| C-3 | buyers.first_time (prospective) | quantity_traded (first-time purchases, 10 March to 30 June of Year 1) | decrease | short | visible | B | CR-10a; CR-4b (x: buy before 1 July, y: wait for the grant) | A-5 |
| C-4 | owners.under_cap (sellers.current) | quantity_supplied (listings under the cap, 10 March to 30 June of Year 1) | decrease | short | invisible | B | CR-10a; CR-4b (x: list now, y: list after 1 July, when buyers have the grant) | A-6 |
| C-5 | buyers.first_time (prospective) | quantity_traded (first-time purchases, months before 30 June of Year 4) | increase | medium | invisible | B | CR-10a (renewal uncertain at the deadline, so buyers who can sign earlier do) | A-16 |
| C-6 | buyers.first_time (prospective) | cross_border_purchases (homes in Lowen suburbs) | decrease | medium | invisible | B | CR-4b (x: buy in Lowen, y: buy in Tamberlay with the grant) | A-12 |
| C-7 | buyers.first_time (prospective) | saving | ambiguous | medium | invisible | B | CR-4 exception (the grant changes total means toward a fixed deposit sum): (-) the deposit target is reached with less own saving; (+) buying sooner raises the payoff to saving now; CR-12b | A-4 |
| C-8 | households with a prior owner | reclassification (title and partner declarations arranged to qualify) | increase | short | invisible | B | CR-4b (x: the covered form, a household with a prior owner; y: the uncovered form, title or declarations arranged to show none) | A-7 |
| C-9 | owners.just_above_cap | reclassification (value moved outside the contract price) | increase | medium | invisible | B | CR-4b (x: contract above the cap, y: contract at the cap with other items paid separately); grows as prices rise against a cap fixed in money (CR-10) | A-8 |
| C-10 | buyers.first_time (grant recipients) | job_changes | decrease | medium | invisible | B | CR-1 op. 3 (the grant is repaid if the home stops being the principal residence within 24 months); CR-4b (x: take a job that needs a move, y: stay) | A-9 |
| C-11 | builders (sellers.prospective) | investment_target (homes under the cap) | increase | long | invisible | B | CR-7a (means move toward the use whose yield rose); CR-4b (x: build above the cap or other projects, y: build entry-level homes) | A-3, A-10 |
| C-12 | landlords of entry-level homes | quantity_supplied (rental units, entry-level) | decrease | medium | invisible | B | CR-4b (x: keep renting the home out, y: sell it to a grant holder at the higher price); CR-7a | A-13, A-2 |
| C-13 | owners, builders and agents | lobbying_effort | increase | medium | invisible | B | CR-4b (x: accept expiry or a fixed cap, y: lobby for renewal or indexation), at the Year 3 review | A-17 |
| C-14 | owners.under_cap (sellers.current) | asset_value (homes under the cap) | increase | short | visible | B | CR-7c (a lasting rise in expected sale value is captured by owners when it becomes expected, from March); CR-7b (owners have fewer alternatives than first-time buyers while supply is slow) | A-2, A-3, A-20 |
| C-15 | owners.under_cap (sellers.current) | subsidy_share_received | increase | short | invisible | B | CR-7b (the benefit of the grant settles on the side with fewer alternatives) | A-2, A-20 |
| C-16 | buyers.non_grant (repeat buyers and investors in the segment) | price_paid (homes under the cap, contract price) | increase | short | invisible | B | CR-6 first paragraph (planned purchases rise against slow supply); CR-9 (they compete with grant holders for the same homes) | A-2, A-20 |
| C-17 | buyers.non_grant (repeat buyers and investors in the segment) | quantity_traded (homes under the cap) | decrease | medium | invisible | B | CR-4c after C-16 | A-2, A-20 |
| C-18 | buyers.non_grant (repeat buyers and investors in the segment) | cross_border_purchases (homes in Lowen suburbs) | increase | medium | invisible | B | CR-4b (x: buy in Tamberlay at the higher price, y: buy in Lowen) | A-2, A-12, A-20 |
| C-19 | neighboring_jurisdictions (Lowen home sellers) | price_substitute (Lowen suburban homes) | ambiguous | medium | invisible | B | (-) CR-9: first-time buyers move to Tamberlay (C-6); (+) CR-9: non-grant buyers move to Lowen (C-18); CR-12b | A-2, A-12, A-20 |
| C-20 | renters (buyers of rental housing) | price_substitute (entry-level rents) | ambiguous | medium | invisible | B | (-) CR-9: renters who buy leave the rental market (substitute); (+) CR-9: landlords sell units to grant holders (C-12); CR-12b | A-4, A-13 |
| C-21 | renters (buyers of rental housing) | quantity_substitute (entry-level rental units let) | decrease | medium | invisible | B | CR-9: both chains in C-20 reduce the number of units let; CR-12a | A-4, A-13 |
| C-22 | buyers.above_cap (trade-up buyers) | price_paid (homes above the cap) | increase | medium | invisible | B | CR-4 exception (the rise in owners' means from C-14 shifts their choices); CR-6 first paragraph in the segment above the cap | A-18, A-19, A-2, A-20 |
| C-23 | construction_labor | wage_rate | increase | long | invisible | B | CR-9, LW-10 (demand for construction labor follows entry-level building, C-11); CR-7a (labor drawn from other uses only at higher pay, since it is fully used) | A-10, A-11 |
| C-24 | buyers of other construction | quantity_traded (other construction projects) | decrease | long | invisible | B | CR-8a (labor and builders moved to entry-level homes are withdrawn from other projects); CR-7a | A-10, A-11 |
| C-25 | intermediaries (real estate agents) | earnings | increase | medium | invisible | B | CR-9, LW-10 (demand for agents' services follows the number and price of sales) | A-4, A-N1 |
| C-26 | taxpayers | resources_available_other_uses | decrease | short | invisible | A | CR-8a, CR-8b (about $300 million a year from general revenue; every grant counted as a gain is matched here) |  |
| C-27 | officials.enforcement (State Revenue Office) | enforcement_cost | increase | short | visible | A | CR-8c; K4 |  |
| C-28 | buyers.first_time (applicants) | compliance_cost | increase | short | invisible | A | CR-1 op. 3; CR-8c (applications, sworn declarations, occupancy proof) |  |
| C-29 | buyers.non_grant (repeat buyers and investors in the segment) | resources_available_other_uses | decrease | medium | invisible | B | CR-8b (the owners' gain in C-14 is the matching outlay of buyers who pay the higher price without a grant); CR-3a | A-2, A-20 |

## Gaps found

**(a) Calculus gaps.** None. Every step was derived from CR-1 to CR-12, LW-10 and arithmetic.

**(b) New premises.**
- A-N1 (agents paid by commission, p 0.85): CR-9 and LW-10 carry more and dearer sales to the demand for agents' services, but whether agents' money earnings follow depends on how they are paid; no case assumption states it.

**(c) Unclear core rules.**
- CR-4 exception (changes in total means): it is stated for a price rise or a lower return on saving toward a fixed sum, and says the direction is ambiguous "unless a premise says which effect dominates". Two uses here stretch it: the grant as a lump of means toward a deposit target (C-7), and owners' asset gains carried into demand for larger homes (C-22). The second is not a relative-price change at all; the rule does not say whether an increase in means alone licenses any direction, so the chain rests wholly on A-18 and A-19.
- CR-7b and CR-12b on incidence: as in other subsidy cases, CR-7b with A-20 gives owners a share, but whether grant holders' net price still falls needed A-1. The core rules do not say whether such a premise is a CR-12b dominance premise.
- CR-7c and an eligibility threshold: CR-7c capitalizes a lasting change in yield into an asset's price. Here the yield change applies only to homes that sell at or under a nominal cap, which a home can cross as prices rise; the rule does not say how to treat an asset whose eligibility for the change is itself expected to lapse.
