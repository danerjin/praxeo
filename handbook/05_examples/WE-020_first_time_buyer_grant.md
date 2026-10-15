# WE-020 Grant to first-time homebuyers

Analyst: draft (Handbook 0.2)  |  Rule catalog version: 0.2  |  Status: awaiting expert review

A stylized policy in a fictional state. Grants of this kind are common, but this one is not modeled on any particular program. The probabilities are illustrative; the evidence column says what a real analysis would cite.

## 1. Policy record

**Merrow Home Start Grant.** Merrow is a state of about 3 million people. About 60,000 homes are sold there in a normal year, roughly a third of them for $450,000 or less, and first-time buyers account for about 18,000 purchases. Builders complete about 12,000 new homes a year; zoning approval and permits take 12 to 24 months and construction another 9 to 15, so the stock of homes responds slowly to prices. Merrow's largest city, Kessford, sits on the border with the state of Lowen, whose suburbs are within a 30-minute commute and which has no comparable grant. Entry-level home prices in Merrow have been rising about 4% a year.

The governor announced the grant in the budget speech on 10 March of Year 1. The legislature enacted it on 15 May. It applies to purchase contracts signed from 1 July of Year 1 to 30 June of Year 4, with a legislative review in Year 3. Renewal is possible but not promised.

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Grant | `purchase_rebate` | Purchase of a home in Merrow | First-time buyers who apply | $15,000, paid at settlement and usable toward the deposit. Contract price must be $450,000 or less (fixed in money terms). The home must be the buyer's principal residence for 24 months; otherwise the full grant is repaid. | — |
| K2 Eligibility | Condition of K1 | Applicants | Applicants | Neither the applicant nor the applicant's spouse or declared partner has ever owned residential property, anywhere. Ownership in Merrow is checked against the land register; ownership elsewhere and partner status are by sworn declaration. One grant per household. | — |
| K3 Funding | Funding of K1 and K4 | — | State budget | Annual appropriation from general revenue, about $300 million a year (20,000 grants). The law does not say what happens if applications exceed the appropriation. | — |
| K4 Administration | Enforcement | K1 and K2 | State Revenue Office | Checks land register and declarations; checks occupancy against driver's license and electoral roll addresses; clawback and fines for false declarations. | — |

Unclear provisions: whether the price cap will be indexed if prices rise (the text fixes it in dollars); whether the grant will be renewed after Year 4. Both are treated as expectations (A-3, A-15).

## 2. Classification

| Component | Rothbard type | Binding? | Rule families |
|---|---|---|---|
| K1 | Binary: a transfer from the state to buyers (and, through prices, to sellers) | Yes for first-time buyers in the segment under the cap | SB, RS, TS |
| K2 | Binary: a condition on the transfer that draws a line between eligible and ineligible buyers | Yes | SB-5, RS-5 |
| K3 | Binary: taxes now | Yes | SB-1, TX-1, OC-1 |
| K4 | Binary: funded by taxpayers | Yes | OC-3 |

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `buyers.first_time` | First-time buyers of homes under the cap, including renters who would not otherwise buy yet | $15,000 toward a purchase, if they buy under the cap, in the window, and stay 24 months. |
| `buyers.other` | Repeat buyers, investors and anyone else buying homes under the cap | No grant; compete with grant holders for the same homes. |
| `owners.entry_level` (`sellers.current`, `factor_owners.specific`) | Owners of existing homes worth around $450,000 or less | More buyers with more to spend. |
| `builders` (`sellers.prospective`) | Builders of new homes | Higher prices for homes under the cap; a reason to design homes to sell just under it. |
| `landowners.developable` (`factor_owners.specific`) | Owners of land zoned for housing | Builders bid for land for entry-level homes. |
| `landlords.entry_level` | Owners of rental homes in the segment | Can sell to grant holders at higher prices. |
| `renters` (`buyers.substitutes`) | Households that rent | Some leave renting; some rental homes are sold. |
| `intermediaries` | Agents, conveyancers, mortgage brokers | More and pricier transactions in the segment. |
| `neighboring_jurisdictions` | Sellers of homes in Lowen's commuter suburbs | Some Kessford-area buyers now buy in Merrow. |
| `taxpayers`, `officials.enforcement` | Funders (including renters and existing owners) and the Revenue Office | Pay for the grant and its administration. |

## 4. Direct effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | `buyers.first_time` | `price_paid` (homes under the cap, net of the grant) | decrease | short to medium | SB-2 | A-1 |
| C-2 | `buyers.first_time` | `quantity_traded` (first-time purchases under the cap) | increase | short to medium | SB-2, RS-1 | A-1, A-4 |

The visible claim is that first-time buyers can afford homes more easily (C-1) and that more of them buy (C-2). C-1 holds only to the extent the grant is not absorbed by higher prices (section 7).

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-3 | `buyers.first_time` | `quantity_traded` (first-time purchases between 10 March and 1 July of Year 1) | decrease | short | RS-8 | A-5 |
| C-4 | `owners.entry_level` | `quantity_supplied` (listings between 10 March and 1 July of Year 1) | decrease | short | RS-8, TS-2 | A-6 |
| C-5 | `buyers.first_time` | `reclassification` (purchases titled in the name of the partner who has never owned; partners not declared) | increase | short to medium | SB-5, RS-5 | A-7 |
| C-6 | `owners.entry_level` selling just above the cap, `buyers.first_time` | `side_payments` (value moved outside the contract price: furniture, seller-paid costs, separate agreements) | increase | short to medium | SB-5, RS-5 | A-8 |
| C-7 | `buyers.first_time` (recipients) | `job_changes` (in the first 24 months of ownership) | decrease | short to medium | RS-11 | A-9 |
| C-8 | `buyers.first_time` (recipients) | `turnover` (sales in the first 24 months of ownership) | decrease | short to medium | RS-8 | A-9 |
| C-9 | `owners.entry_level`, `builders`, `intermediaries`, would-be buyers | `lobbying_effort` (for renewal and a higher cap) | increase | medium | RS-7, SB-5 | A-17 |
| C-10 | `buyers.first_time` | `quantity_traded` (first-time purchases in the months before 30 June of Year 4) | increase | medium | RS-8 | A-16 |

C-7 and C-8: the grant is lost if the buyer moves within 24 months, so it works like a benefit tied to a location (RS-11). Recipients turn down job moves that would require selling, and sales by recipients are pushed past the 24-month mark.

C-10: whether the grant will be renewed is not known before the deadline (A-15). Buyers who can sign a few months earlier do so rather than risk losing $15,000.

Not reported:
- Nominee purchases by investors (a never-owner relative buys and the investor rents the home out), RS-3. Occupancy is checked against license and electoral addresses; A-14 is below the cut-off (p = 0.3).
- A dip in purchases after 30 June of Year 4, and the fall in home values when the grant ends. Both rest on the grant not being renewed (A-15, p = 0.4), below the cut-off. The second also needs a rule the catalog does not have (GAP-020-1).

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-11 | `owners.entry_level` | `asset_value` (homes under the cap) | increase | short to medium | SB-4 | — | A-2, A-3 |
| C-12 | `buyers.other` | `price_paid` (homes under the cap) | increase | short to medium | SB-4 | grant holders and other buyers: same market | A-2, A-3 |
| C-13 | `buyers.other` | `quantity_traded` (homes under the cap) | decrease | short to medium | SB-3, LW-3 | as C-12 | A-2, A-3 |
| C-14 | `builders` | `investment_target` (new homes under the cap) | increase | medium | LW-4, TS-1 | — | A-3, A-10 |
| C-15 | `builders` | `reclassification` (new homes designed and priced just under $450,000) | increase | medium | SB-5, RS-5 | — | A-3, A-10 |
| C-16 | `buyers.other` above the cap | `quantity_substitute` (new homes above the cap, and renovation work) | decrease | medium | SB-3 | entry-level and other building: compete for the same builders and labor | A-10, A-11 |
| C-17 | `landowners.developable` | `asset_value` (land suited to entry-level homes) | increase | medium | SB-4 | land: `input_to` new homes, close | A-2, A-3 |
| C-18 | `renters` | `price_substitute` (rents for entry-level homes) | see section 7 | medium | RS-1, SB-3 | renting and buying: `substitute`, close | A-4, A-13 |
| C-19 | `intermediaries` | `earnings` (fees in the segment) | increase | short to medium | SB-2, SB-4 | brokerage and conveyancing: `input_to` home sales | A-1, A-2 |
| C-20 | Kessford-area `buyers.first_time` | `cross_border_purchases` (homes bought in Lowen) | decrease | short to medium | RS-4 | Merrow and Lowen suburbs: `across_border`, partial | A-12 |
| C-21 | `neighboring_jurisdictions` (sellers in Lowen's suburbs) | `quantity_traded` (homes sold to Merrow-employed buyers) | decrease | short to medium | RS-4 | as C-20 | A-12 |
| C-22 | `owners.entry_level` who sell and buy a larger home | `price_paid` (homes above the cap) | increase | medium | GAP-020-2 | entry-level and larger homes: `same_market_other_segment`, partial | A-2, A-18 |

C-11 is the core of SB-4: the grant goes to buyers, but the homes they buy are in slowly changing supply (A-2), so much of it is bid into prices and captured by whoever owns those homes when the grant becomes expected (from the March announcement, not the July start). C-12 and C-13 follow: buyers who get no grant pay those higher prices and buy fewer of these homes.

C-22 is at depth 3: sellers whose homes rose in value (C-11) have more equity to bid for larger homes. The catalog has no rule for spending out of asset gains (GAP-020-2), so it is Tier C. The chain stops here; effects on the rest of the housing ladder are diffuse.

Second-order checks:
- **RS-9 (bundled trips).** Buyers who switch from Lowen to Merrow (C-20) do not bundle other purchases with a house purchase. Their later everyday spending moves with their residence, but that is a change of residence, not a trip, and is not traced. Not applicable.
- **RS-10 (informal trade).** Side payments around the price cap (C-6) are off-contract but not illegal trade in the usual sense; they make the recorded price less informative and disputes over them harder to enforce. Nominee fraud is not reported (A-14).
- **RS-11 (lock-in).** Applies through the 24-month clawback (C-7).

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `buyers.first_time`, `price_paid` (net of grant), short to medium | Capitalization raises the price before the grant (C-11, SB-4). | The $15,000 grant (SB-2). | None in the catalog. A-1 selects the branch of SB-2 ("buyers pay less and/or sellers receive more"); it is not a dominance rule. | **decrease**, by less than $15,000. SB-2 and SB-4 describe how one subsidy is split between buyers and sellers, not two independent forces; given A-1 (prices rise by less than the grant, p = 0.7), the net price still falls. If A-1 were false (full capitalization), recipients would pay the same as without the grant and the whole of it would go to sellers. |
| Split of the grant between `buyers.first_time` and `owners.entry_level`, medium | — | — | None | **Not expressible as one variable** (GAP-020-3). SB-4 says owners at announcement capture "much" of it; A-1 says not all. Reported only through C-1, C-11 and C-12. Tier C. |
| `renters`, `price_substitute` (rents for entry-level homes), medium | Landlords sell rental homes to grant holders at the higher prices (SB-3, C-11; A-13), so fewer homes are for rent. | Renters at the margin buy instead of renting (RS-1, C-2), so fewer households compete for rentals. | None | **ambiguous**. Each home a landlord sells to a former renter removes one rental and one renting household, so these two partly cancel. The sign depends on how many grant buyers come from outside the rental market (from living with parents, from Lowen) compared with how many rental homes are sold to them. |
| `builders`, `quantity_traded` (all new homes), medium | More entry-level building (C-14). | Builders and labor drawn from above-cap building and renovation (C-16). | None | **ambiguous**. The subsidy changes the mix of building; whether total building rises depends on whether the industry's labor and approvals can grow or are only moved. |

## 8. Time structure

- **Announcement.** The grant was expected from 10 March. Home values in the segment begin to rise then (C-11), before any grant is paid. First-time buyers wait for July (C-3), and some owners hold back listings to sell into the expected rise (C-4).
- **During the window.** Supply under the cap responds slowly (A-2): planning and building take two to four years. Capitalization is therefore largest in the first two years and shrinks as new entry-level homes arrive (C-14). Because the cap is fixed in dollars while prices rise about 4% a year (TS-3), the share of homes under it falls over time, and the bunching of prices and new builds just under it (C-6, C-15) grows.
- **24-month clawback.** Recipients' sales and job moves are held back for two years after each purchase (C-7, C-8). Sales by recipients then bunch just after the 24-month mark.
- **End of the window.** Uncertainty about renewal brings purchases forward into the last months (C-10). If the grant is not renewed (A-15, p = 0.4, not reported), purchases dip afterwards and home values in the segment fall back, leaving recent recipients holding homes bought at capitalized prices (GAP-020-1).
- **Expectations.** SB-4 needs the grant to be expected to last. A three-year statutory window and a likely renewal (A-3) are enough for builders and landowners to respond; lobbying for renewal (C-9) makes renewal more likely, which makes capitalization larger.

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-23 | `officials.enforcement` | `enforcement_cost` | increase | Register checks, occupancy checks, clawbacks. | OC-3 |
| C-24 | `taxpayers` (including renters and existing owners) | `resources_available_other_uses` | decrease | What taxpayers would have bought with about $300 million a year plus administration, or what other state spending it would have funded. | SB-1, TX-1, OC-1, OC-3 |
| C-25 | `buyers.other` | `resources_available_other_uses` | decrease | The extra paid for the same homes because of capitalization (C-12): money no longer available for other purposes. | OC-1, SB-4 |

Purchases that other buyers no longer make are already recorded as C-13, and the building moved away from other projects as C-16.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | Prices under the cap rise by less than the grant, because many buyers in the segment get no grant and some supply responds. | other | 0.7 | Share of segment purchases by first-time buyers; listings and price data after the announcement; studies of comparable grants. | C-1 and C-2 fail: the whole grant goes to sellers. |
| A-2 | The supply of homes under the cap responds slowly. | durability | 0.85 | Approval and build times; vacancy rate; pipeline of approved projects. | C-11 to C-13, C-17, C-22 weaken; more of the grant stays with buyers. |
| A-3 | Buyers, sellers and builders expect the grant to last at least through Year 4. | expectations | 0.75 | Statutory window; budget commitment; political support. | SB-4 weakens; C-11 to C-15, C-17 shrink. |
| A-4 | Some renters at the margin buy sooner because of the grant. | substitutability | 0.85 | Rent-to-price ratios; deposit as the binding constraint for first-time buyers (mortgage data). | C-2 shrinks to inframarginal buyers; the renter chain in C-18 fails. |
| A-5 | First-time buyers knew of the grant from March and could delay. | expectations | 0.85 | Publicity of the budget speech; agents' reports. | C-3 not reported. |
| A-6 | Some owners delay listing to sell after July. | expectations | 0.55 | Listings data around comparable announcements. | C-4 not reported. |
| A-7 | Couples can arrange title or partner declarations so that a prior owner's household qualifies. | enforcement | 0.6 | Declaration-based partner check; no register outside Merrow. | C-5 not reported. |
| A-8 | Sellers just above the cap can move value outside the contract price. | other | 0.6 | Legal definition of contract price; bunching at price thresholds in transfer data. | C-6 not reported. |
| A-9 | Some recipients receive job offers in the first 24 months that would require moving. | mobility | 0.7 | Job-change rates of young households; size of labor markets within commuting distance. | C-7, C-8 weaken. |
| A-10 | Builders can obtain approvals for entry-level projects within a few years. | alternative_uses | 0.65 | Zoning capacity; approval rates. | C-14, C-15 and the + chain on building fail. |
| A-11 | Construction labor and builders are scarce and fully used elsewhere. | other | 0.8 | Construction employment and vacancy rates. | C-16 fails. |
| A-12 | Many Kessford-area buyers can choose between Merrow and Lowen suburbs. | mobility | 0.7 | Commute times; existing cross-border home buying. | C-20, C-21 not reported. |
| A-13 | Some landlords of entry-level homes sell to grant holders. | alternative_uses | 0.7 | Share of segment homes owned by small landlords; rental yields against sale prices. | The + chain in C-18 fails; rents fall. |
| A-14 | Investors use nominee buyers on a meaningful scale. | enforcement | 0.3 | Occupancy checks; penalties. | Below cut-off; not reported. |
| A-15 | The grant is not renewed after Year 4. | expectations | 0.4 | Budget pressure; lobbying; legislative review. | Below cut-off; dip and fall in values not reported. |
| A-16 | Renewal is uncertain at the deadline, and some buyers can sign a few months earlier. | expectations | 0.7 | Timing of the Year 3 review; flexibility of purchase timing. | C-10 not reported. |
| A-17 | Owners, builders and agents can organize to lobby. | other | 0.85 | Existing builders' and agents' associations. | C-9 weakens. |
| A-18 | Owners whose homes rise in value use part of the gain to bid for larger homes. | other | 0.6 | Trade-up rates; equity-financed deposits. | C-22 not reported. |

## 11. Report

**The policy.** Merrow pays $15,000 at settlement to first-time buyers of homes costing $450,000 or less, for three years, if they live in the home for two years. It is funded from general revenue.

**Visible consequences.** First-time buyers pay less, net of the grant, for homes under the cap (C-1), and more of them buy (C-2).

**Invisible consequences.**
- *Existing owners of entry-level homes* gain: their homes are worth more from the day the grant is announced (C-11). Landowners gain too (C-17).
- *Other buyers* of the same homes (repeat buyers, investors) pay more and buy fewer of them (C-12, C-13, C-25).
- *First-time buyers* get less than $15,000 of benefit, because part of it is in the price (section 7). Those who would have bought in spring wait until July (C-3), and some sellers hold back (C-4). Recipients move jobs and homes less for two years (C-7, C-8). Some households arrange title or declarations to qualify (C-5); some sales just above the cap move value outside the contract (C-6). Many rush to buy before the deadline in Year 4 (C-10).
- *Builders* build more homes just under the cap (C-14, C-15), drawing labor away from other building and renovation (C-16).
- *Lowen's commuter suburbs* lose some buyers to Merrow (C-20, C-21). *Agents and conveyancers* earn more (C-19). Owners who trade up push up prices of larger homes (C-22, Tier C).
- Owners, builders and agents lobby for renewal and a higher cap (C-9).
- *Taxpayers*, renters among them, fund the grant and its administration (C-23, C-24).

**Ambiguous effects.** Whether rents rise or fall (landlords selling to grant holders against renters leaving to buy). Whether total home building rises or only shifts toward homes under the cap. How the grant splits between buyers and sellers cannot be stated as a single variable.

**Key conditions.** How much the grant helps buyers depends on capitalization being less than full (A-1, p = 0.7) and on supply being slow (A-2, p = 0.85); in a market where builders could add homes quickly, more of the grant would stay with buyers. If the grant is not renewed (A-15, p = 0.4, not reported), recent recipients would see the value of their homes fall back.

**What this analysis cannot say.** How large any effect is; how the grant is divided between buyers and sellers in dollars; whether the transfer from taxpayers to first-time buyers and existing owners is desirable.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | buyers.first_time | price_paid (net of grant) | decrease | short–medium | visible | B | SB-2, SB-4 | A-1 |
| C-2 | buyers.first_time | quantity_traded (first-time purchases) | increase | short–medium | visible | B | SB-2, RS-1 | A-1, A-4 |
| C-3 | buyers.first_time | quantity_traded (March to June, Year 1) | decrease | short | invisible | B | RS-8 | A-5 |
| C-4 | owners.entry_level | quantity_supplied (listings, March to June) | decrease | short | invisible | B | RS-8, TS-2 | A-6 |
| C-5 | buyers.first_time | reclassification | increase | short–medium | invisible | B | SB-5, RS-5 | A-7 |
| C-6 | owners.entry_level, buyers.first_time | side_payments | increase | short–medium | invisible | B | SB-5, RS-5 | A-8 |
| C-7 | buyers.first_time (recipients) | job_changes | decrease | short–medium | invisible | B | RS-11 | A-9 |
| C-8 | buyers.first_time (recipients) | turnover (first 24 months) | decrease | short–medium | invisible | B | RS-8 | A-9 |
| C-9 | owners, builders, intermediaries | lobbying_effort | increase | medium | invisible | B | RS-7, SB-5 | A-17 |
| C-10 | buyers.first_time | quantity_traded (before end of Year 4 window) | increase | medium | invisible | B | RS-8 | A-16 |
| C-11 | owners.entry_level | asset_value | increase | short–medium | invisible | B | SB-4 | A-2, A-3 |
| C-12 | buyers.other | price_paid (homes under cap) | increase | short–medium | invisible | B | SB-4 | A-2, A-3 |
| C-13 | buyers.other | quantity_traded (homes under cap) | decrease | short–medium | invisible | B | SB-4, SB-3, LW-3 | A-2, A-3 |
| C-14 | builders | investment_target (new homes under cap) | increase | medium | invisible | B | SB-4, LW-4, TS-1 | A-3, A-10 |
| C-15 | builders | reclassification (pricing under cap) | increase | medium | invisible | B | SB-5, RS-5 | A-3, A-10 |
| C-16 | buyers.other (above cap) | quantity_substitute (other building) | decrease | medium | invisible | B | SB-3 | A-10, A-11 |
| C-17 | landowners.developable | asset_value (land) | increase | medium | invisible | B | SB-4 | A-2, A-3 |
| C-18 | renters | price_substitute (rents) | ambiguous | medium | invisible | B | RS-1 vs SB-3 | A-4, A-13 |
| C-19 | intermediaries | earnings | increase | short–medium | invisible | B | SB-2, SB-4 | A-1, A-2 |
| C-20 | buyers.first_time (Kessford area) | cross_border_purchases | decrease | short–medium | invisible | B | RS-4 | A-12 |
| C-21 | neighboring_jurisdictions | quantity_traded (homes in Lowen suburbs) | decrease | short–medium | invisible | B | RS-4 | A-12 |
| C-22 | owners.entry_level (trading up) | price_paid (homes above cap) | increase | medium | invisible | C | SB-4, GAP-020-2 | A-2, A-18 |
| C-23 | officials.enforcement | enforcement_cost | increase | short | invisible | A | OC-3 | none |
| C-24 | taxpayers | resources_available_other_uses | decrease | short–medium | invisible | A | SB-1, TX-1, OC-1, OC-3 | none |
| C-25 | buyers.other | resources_available_other_uses | decrease | short–medium | invisible | B | SB-4, OC-1 | A-2, A-3 |
| C-26 | builders | quantity_traded (all new homes) | ambiguous | medium | invisible | B | C-14 vs C-16 | A-10, A-11 |

## Gaps found

- **GAP-020-1. No rule for the end of a capitalized subsidy.** SB-4 says a lasting subsidy is capitalized into the value of a fixed-supply asset when it becomes expected. Nothing states the reverse: when the subsidy ends, or comes to be expected to end, the asset value falls, and those who bought at capitalized prices bear the loss. The chain is not reported here only because non-renewal is below the cut-off (A-15). **Proposed fix:** an SB rule (ID to be assigned) "Decapitalization": if a subsidy that was capitalized under SB-4 ends or is expected to end, `asset_value` of the asset decreases from the time the end becomes expected; holders who bought during the subsidy bear it; Tier B, assumes `expectations` and the same slow supply as SB-4.
- **GAP-020-2. No rule for spending out of asset gains.** Owners whose homes rise in value (C-11) use the extra equity to bid for larger homes, carrying part of the price rise up the housing ladder (C-22). The catalog has no rule linking a rise in `asset_value` to the holders' later purchases. Tier C. **Proposed fix:** a rule "Revaluation changes holders' means" (family OC or SB): if `asset_value` of an asset held by an actor class rises (falls), their `resources_available_other_uses` rises (falls) when they sell or borrow against it, and their purchases in linked markets rise (fall); assumes the gain can be realized (sale or borrowing) and is not offset by an equal rise in what they must buy.
- **GAP-020-3. No variable for the split of a subsidy.** `tax_share_borne` records how a tax divides among subgroups, but there is no counterpart for how a subsidy divides between its nominal recipients and the sellers or asset owners who capture part of it. This example's central question ("who actually gains") can only be answered indirectly through C-1, C-11 and C-12. **Proposed fix:** add `subsidy_share_received` to 2.4 (share of a subsidy's benefit received by a subgroup, signed relative to the nominal recipients), with SB-4 and a subsidy version of DM-1 as the rules that set it.
