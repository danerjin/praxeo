# WE-038 / Analysis: Municipal fiber network funded by revenue bonds

Analyst: core-only re-run (Handbook 0.8)  |  Rules: core rules CR-1 to CR-12 only  |  Status: compared

## 1. Policy record

**Calderby Community Fiber Ordinance.** Calderby, in the State of Merrin, has about 180,000 people in 72,000 households and about 6,000 business premises. About 64,000 households (89%) buy home broadband from two private incumbents: a cable company (about 60% of subscribers) and a telephone company (about 40%, half of them on older copper lines). Their price for 1 Gbps, or the nearest offer, is about $80 a month and has risen about 3% a year for five years. A private fiber builder applied in 2025 for permits in two newer neighborhoods (about 9,000 homes) and has not started.

The city owns its electric utility, Calderby Light and Power (CLP): about 84,000 accounts, 72,000 inside the city and 12,000 in the townships of Orvel and Dunmere, which the network will not serve. CLP's revenue is about $150 million a year. Its rates are set by the council on cost of service, including interest on CLP's own debt. CLP transfers 6% of revenue (about $9 million) to the general fund, spends about $18 million on distribution maintenance and about $25 million on capital work from rates. Merrin law lets cities charge private telecom providers a right-of-way fee of 4% of gross revenue earned in the city (about $2.5 million a year from the incumbents); the city's own network does not pay it.

Proposed with a feasibility study on 3 March 2026, introduced 14 April 2026, adopted 9 June 2026; bonds sold 15 September 2026. Construction from October 2026; service opens zone by zone from 1 July 2027 and reaches the whole city by December 2029. No expiry.

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 City service | `public_supply` | Home and small-business broadband (1 Gbps symmetric) | City, through a broadband division of CLP | $55 a month, no installation charge, fixed by ordinance until 30 June 2032, then the council may change it. Offered to every premises passed, without limit on subscribers. The network passes all 78,000 premises and is sized for 100% take-up at the projected 2030 peak. | Not offered outside the city limits. |
| K2 Revenue bonds | `government_borrowing` | Construction | City | $150 million tax-exempt revenue bonds, 25 years, 4.5%, sold nationally. Includes $12 million capitalized interest (to 30 September 2029) and a $10 million reserve. Level debt service from fiscal 2030 about $10.1 million a year. Payable solely from network revenues, subject to K3. | — |
| K3 Backstop | Contingent transfer (no instrument type in 2.3) | Debt service on K2 | CLP | "Any shortfall in the revenues of the network available for debt service shall be made good by the Calderby Light and Power from its rates." A drawn reserve is replenished by CLP within twelve months. | — |
| K4 Administration | Administration | K1 to K3 | CLP broadband division; bond trustee; city auditor | Operating costs (about $4 million a year fixed plus about $150 per subscriber a year), trustee fees and audits paid from network revenue before debt service. | — |

Unclear provision:
- U1, what "from its rates" requires of CLP. U1-a: CLP may raise electricity rates to cover a shortfall. U1-b: CLP must cover it from the revenue its existing rates bring in, by cutting other spending (the general-fund transfer, maintenance or capital work).

Figures: revenue at $55 is $660 per subscriber a year; network revenue covers operating cost and debt service at about 27,700 subscribers (36% of premises). At 30% take-up the shortfall is about $3.2 million a year: 2.1% of CLP revenue, about $38 per electricity account, about a third of the general-fund transfer.

Counterfactual law: no network, no bonds, no backstop; the incumbents' prices follow their trend (A-1); the private builder decides on its own; the right-of-way fee applies to the incumbents' whole Calderby revenue.

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | CR-1 operations | Core rules applied |
| --- | --- | --- | --- | --- |
| K1 City service | binary (the state supplies) and, through competition, a change in the options of private sellers | Yes for households who rank $55 above the incumbents' offers (A-2); not quantity-rationed while capacity exceeds demand (A-3) | 2 (adds the option "buy 1 Gbps at $55, no installation charge" for every premises in the city); for incumbents and the builder, 3 (what selling broadband brings falls, since buyers have a new alternative) | CR-2, CR-4, CR-5c, CR-6, CR-7b, CR-7c, CR-9, CR-10a, CR-10c |
| K2 Revenue bonds | binary (the state borrows) | Yes: sold 15 September 2026 | 4 for the city (means borrowed); for lenders, 2 (a new asset to buy) | CR-5, CR-8a, CR-8b, CR-4 (0.7: means over time) |
| K3 Backstop | binary, contingent (the state takes from CLP's customers or from CLP's other uses) | Contingent on a shortfall (A-6); as an obligation, binding at once on how lenders see CLP (A-13) | 4, dated and contingent: transfers means from CLP to bondholders in shortfall years. U1-a: through a rate rise, op 3 on every kWh bought; U1-b: op 4 on the general fund, or a cut in CLP maintenance or capital | CR-1, CR-8b, CR-8 (0.8 contingent payers), CR-9 (contract), CR-5c |
| K4 Administration | binary (means used up) | Yes | 4 (network revenue used for administration) | CR-8c |

K1 is a public supply at a fixed price with no fixed quantity: CR-6's 0.7 public-supply clause covers rationing only when quantity is fixed; here capacity exceeds demand (A-3), so the price-setting effect runs through the incumbents' prices (CR-4, CR-5c, CR-6 in the incumbents' market).

## 3. Actor classes

| Actor class | Role | How its options change (CR-1) |
| --- | --- | --- |
| subscribers.switching | Households and small businesses that leave an incumbent for the city service | Op 2: a $55 option; they take it (CR-4, A-2). |
| subscribers.staying | Subscribers who stay with an incumbent | Op 2 unused; incumbents' offers improve (CR-9, A-4). |
| subscribers.new | Premises without broadband that subscribe | Op 2 and the incumbents' lower prices (A-5). |
| subscribers.builder_neighborhoods | About 9,000 homes where the private builder planned to build | As above; lose the builder's possible entry (A-11). |
| incumbents (cable, telephone) | sellers.current; owners of sunk local plant (factor_owners.specific) | Op 3: each price now brings fewer buyers; options to cut price, offer term contracts, upgrade, lobby. |
| workers.incumbents | Incumbents' local staff | Through CR-9 (input_to): demand for their work follows incumbents' subscribers (A-12). |
| private_fiber_builder | sellers.prospective | Op 3 on "build": a $55 rival at every premises. |
| clp.broadband_division | Public supplier | Op 2/4: builds and runs the network with K2 money; bears K4 costs. |
| clp | Electric utility; backstop payer | Op 4 (contingent): pays shortfalls; its own lenders reprice it (A-13). |
| electricity_customers (city and township accounts) | Buyers of CLP electricity; payers under U1-a | Op 3 on each kWh under U1-a; cost-of-service rates pass on CLP's interest (A-14). |
| electricity_customers.not_served | Township accounts and city accounts that buy no broadband | Pay any electricity rise; receive nothing from K1. |
| city_general_fund; general_fund_recipients; city_taxpayers | Receive the CLP transfer and right-of-way fees | Lose right-of-way fees (CR-9); under U1-b, may lose part of the transfer. |
| bond_buyers | Lenders | Op 2: a tax-exempt bond to buy (CR-5). |
| borrowers.other_domestic | Other borrowers at home | Through CR-9 (competing for the same saving, A-7). |
| officials.treasury (federal and state) | Collect income tax on interest | Tax-exempt interest replaces taxable interest (A-N1). |
| taxpayers.other; recipients_other_spending | Pay for or receive other public spending | Through CR-8b (who makes up lost tax revenue). |
| construction_contractors | Builders of the network | Through CR-9 (input_to): added contracts (A-17). |
| buyers.other_construction_work | Others who hire the same crews | Through CR-9 (competing for the same means). |
| sellers.complements | Sellers of home-network equipment and streaming | Through CR-9 (complement): more subscribers (A-18). |

## 4. Direct effect

CR-1 and CR-2: the immediate change for those whose options K1 to K3 alter.

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-1 | subscribers.switching | price_paid (broadband) | decrease | medium | CR-1 op 2, CR-2, CR-4b | A-1, A-2 |
| C-2 | clp.broadband_division | quantity_traded (city broadband subscriptions) | increase | medium; long | CR-1 op 2, CR-4b, CR-5 | A-2, A-3 |
| C-3 | clp.broadband_division | investment_target (fiber network) | increase | short; medium | CR-1 op 4, CR-8a | - |
| C-4 | clp | subsidy_outlay (shortfall payments to network debt service) | increase | medium (fiscal 2030 to 2034) | CR-1 op 4, CR-8b, CR-8 (0.8 contingent payers) | A-6 |

## 5. Responses

CR-4 applied to every pair of options each class has; CR-5c and CR-6 in the incumbents' market; CR-7 for who bears the change; CR-10a for timing.

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-5 | subscribers.staying | price_paid (incumbents' broadband) | decrease | medium; long | CR-4 (incumbent x: hold $80, y: cut price), CR-5c, CR-6, CR-7b | A-1, A-2, A-4 |
| C-6 | incumbents | net_price_received (broadband in Calderby) | decrease | medium; long | CR-4, CR-5c, CR-6, CR-7b | A-1, A-2, A-4 |
| C-7 | incumbents | quantity_traded (incumbent subscriptions in Calderby) | decrease | medium; long | CR-4a, CR-4b, CR-9, CR-12e (arithmetic) | A-2, A-N4 |
| C-8 | subscribers.new | quantity_demanded (broadband) | increase | medium | CR-4 (x: no broadband, y: subscribe), CR-4c | A-5 |
| C-9 | incumbents | term_prevalence (term contracts with early-termination fees) | increase | short; medium | CR-10a, CR-4 (x: month-to-month, y: term offer), CR-5c | A-15, A-9 |
| C-10 | incumbents | asset_value (Calderby plant; shares) | decrease | short (from 3 March 2026) | CR-7c, CR-10c, CR-7b | A-9, A-4, A-2 |
| C-11 | incumbents | lobbying_effort | increase | short; medium | CR-4 (x: accept, y: lobby), CR-8c | A-10 |
| C-12 | incumbents | investment_target (fiber upgrade of older plant in Calderby) | ambiguous | medium | CR-12b over CR-4 and CR-7c chains | A-23, A-4, A-2 |
| C-13 | private_fiber_builder | entry_rate (the two neighborhoods) | decrease | medium | CR-4 (x: build, y: stay out), CR-4a | A-11, A-N5 |
| C-14 | incumbents | return_on_capital (Calderby plant) | decrease | medium; long | CR-7b, CR-3a | A-1, A-2, A-4 |
| C-15 | clp.broadband_division | enforcement_cost (trustee fees, audits, administration) | increase | short; medium; long | CR-1 op 4, CR-8c | - |
| C-16 | clp | interest_rate (CLP's own borrowing) | increase | short; medium | CR-9 (contract), CR-5c, CR-10c | A-13 |
| C-17 | electricity_customers | price_paid (electricity) | U1-a: increase; U1-b: increase | medium | CR-12d over two chains | A-6, A-14, A-13, A-N2 |
| C-18 | city_general_fund; clp | non_tax_receipts (transfer to general fund) (−), maintenance_spending (−), investment_target (electric capital work) (−) | U1-a: no_change; U1-b: at_least_one_decrease | medium | CR-8b, CR-8 (0.8 contingent payers) | A-6, A-14 |
| C-19 | electricity_customers | quantity_demanded (electricity) | decrease | medium | CR-4c | A-13, A-14, A-N2, A-N9 |

## 6. Second-order effects

CR-9 along named relations, then CR-5 to CR-7 in each market reached. Depth limit 4. The tax-revenue chain (C-24, C-25) stops at depth 3, a diffuse effect on bystanders. The pole relation (shared_facility: CLP poles carry incumbents' lines) is not followed: its only chain needs A-22 (p 0.35).

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C-20 | workers.incumbents | employment (incumbents' local staff) | decrease | medium; long | CR-9, LW-10, CR-7a | local labor input_to incumbents' service (close) | A-12, A-2, A-N4 |
| C-21 | city_general_fund | non_tax_receipts (right-of-way fees) | decrease | medium; long | CR-9, CR-8b, arithmetic | incumbents' gross revenue is the fee base (rule in force) | A-2, A-4, A-N4 |
| C-22 | general_fund_recipients; city_taxpayers | resources_available_other_uses | at_least_one_decrease | medium; long | CR-8b, CR-8 (0.7 payers from the general budget) | general fund pays for city spending | A-2, A-4, A-N4 |
| C-23 | borrowers.other_domestic | interest_rate (+), quantity_traded (loans to them) (−) | at_least_one_as_stated | short | CR-8a, CR-6, CR-7a | same saving lent to the city or to them (substitute, weak) | A-7 |
| C-24 | officials.treasury (federal and state) | tax_revenue (income tax on interest) | decrease | short; medium; long | CR-8b, CR-4 (lender x: taxable asset, y: tax-exempt bond) | tax-exempt bond substitute for taxable lending | A-7, A-N1 |
| C-25 | taxpayers.other; recipients_other_spending | resources_available_other_uses | at_least_one_decrease | medium; long | CR-8b, CR-8 (0.7 payers from the general budget) | treasury pays for other spending | A-7, A-N1 |
| C-26 | construction_contractors | employment (+), hours_worked (+) (fiber construction) | at_least_one_increase | short; medium | CR-9, LW-10, CR-7a | construction labor input_to the network (close) | A-17 |
| C-27 | buyers.other_construction_work | price_paid (+), quantity_traded (−) (other construction work) | at_least_one_as_stated | short; medium | CR-9, CR-7a, CR-6, CR-8a | same crews input_to other work (partial) | A-17, A-N7 |
| C-28 | sellers.complements | quantity_complement (home-network equipment, streaming) | increase | medium | CR-9, LW-10 | complement of broadband (partial) | A-5, A-18 |
| C-29 | subscribers.switching | resources_available_other_uses | increase | medium | CR-3 (note), CR-8b, CR-12e (A-N8) | broadband and electricity bought by the same household | A-1, A-2, A-N8 |
| C-30 | subscribers.staying | resources_available_other_uses | ambiguous | medium | CR-12b | as above | A-1, A-4, A-13, A-14, A-N2, A-6 |
| C-31 | electricity_customers.not_served | resources_available_other_uses | decrease | medium | CR-3 (note), CR-8b | contract: CLP service at cost-of-service rates | A-13, A-14, A-N2, A-24 |
| C-32 | subscribers.new | resources_available_other_uses | decrease | medium | CR-3c, CR-8a | - | A-5 |
| C-33 | subscribers.builder_neighborhoods | price_paid (broadband) | decrease | medium | CR-4, CR-5c, CR-12 (0.8 kind 2) | builder's service substitute for city and incumbent service | A-1, A-2, A-4 |

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance premise | Combined sign |
| --- | --- | --- | --- | --- |
| electricity_customers, price_paid, medium | U1-a: shortfall recovered in cost-of-service rates (A-6, A-14); both readings: higher interest on CLP's debt passed into rates (A-13, A-14, A-N2) | Network pays CLP for shared costs, lowering electricity's cost of service (needs A-N3, p 0.35) | Opposing chain is kind (2) of CR-12 0.8 with p below 0.5: derived sign reported, chain recorded in section 10 | U1-a: increase; U1-b: increase (C-17) |
| subscribers.switching, resources_available_other_uses, medium | $25 a month less for broadband (C-1) | electricity rate rise (C-17) | A-N8 (empirical, with arithmetic: a $3.2 million shortfall is about $38 a year per account against $300 a year saved) | increase (C-29) |
| subscribers.staying, resources_available_other_uses, medium | incumbents' lower price (C-5) | electricity rate rise (C-17) | None: the size of the incumbents' cut is not in the case's figures | ambiguous (C-30) |
| incumbents, investment_target (upgrade), medium | upgrading keeps subscribers who would leave copper for city fiber (CR-4, x: keep copper, y: upgrade; A-23) | lower expected price in Calderby lowers the yield on any new local investment (CR-7c, CR-4, x: invest here, y: elsewhere; A-4) | None | ambiguous (C-12) |
| subscribers.builder_neighborhoods, price_paid, medium | builder stays out (C-13), so households lose a rival that might have priced below what they now pay (needs A-N6, p 0.4) | city's $55 and incumbents' cuts (C-1, C-5) | Opposing chain is kind (2) with p below 0.5 | decrease (C-33) |
| incumbents, quantity_traded, medium | new subscribers who choose an incumbent at its lower price (A-5) | switchers to the city (A-2) | CR-12e arithmetic with A-N4: households without broadband number about 8,000, so if the city signs more than that, incumbents' count falls even if every new subscriber chose an incumbent | decrease (C-7) |
| general_fund_recipients; city_taxpayers, resources, medium | - | lost right-of-way fees (C-21); U1-b: smaller transfer (C-18) | same direction | at_least_one_decrease (C-22) |

No chain was found that would raise the incumbents' price above the counterfactual (such as higher prices for loyal customers after a loss of scale); the rules derive none, so it is a Tier C note, not an ambiguity (CR-12, 0.7).

## 8. Time structure

- **Proposal to service (3 March 2026 to 30 June 2027).** Investors in the incumbents mark down the Calderby plant from the proposal on, partly at proposal and more at adoption and at the bond sale, as the network becomes more likely (CR-7c, CR-10c; C-10). Incumbents offer term contracts with early-termination fees before zones open (CR-10a; C-9); households who sign them switch later than they otherwise would. Without the policy there is no city service to switch to, so the delay is a path note, not a per-window consequence.
- **Zone rollout (July 2027 to December 2029).** Price effects (C-1, C-5) arrive zone by zone. Capitalized interest pays debt service until 30 September 2029, so no backstop payment is needed before fiscal 2030 (C-4, C-17, C-18 are medium-horizon only).
- **Shortfall years (fiscal 2030 to 2034).** If take-up stays under about 36% (A-6), CLP pays shortfalls each year and replenishes any drawn reserve within twelve months.
- **Price review (from 1 July 2032).** The $55 is fixed in money; the council may change it after June 2032. Expectations of a change bear on incumbents' and the builder's choices from earlier (CR-10a), but no premise in the case says which way the council will move, so no sign is given.
- **Durability.** The network and the incumbents' plant are durable (CR-10b): incumbents' losses settle on sunk plant (C-14) and persist while the network operates.

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
| --- | --- | --- | --- | --- | --- |
| C-3 | clp.broadband_division | investment_target (fiber network) | increase | The $150 million of saving the bonds draw would otherwise have financed other borrowers' projects (C-23) | CR-8a |
| C-11 | incumbents | lobbying_effort | increase | Staff time and money spent opposing the network | CR-4, CR-8c |
| C-15 | clp.broadband_division | enforcement_cost | increase | Trustee, audit and administration resources paid from network revenue | CR-8c |
| C-18 | city_general_fund; clp | non_tax_receipts (−), maintenance_spending (−), investment_target (−) | U1-a: no_change; U1-b: at_least_one_decrease | General-fund services, line maintenance or capital work not done | CR-8b |
| C-22 | general_fund_recipients; city_taxpayers | resources_available_other_uses | at_least_one_decrease | Spending financed by lost right-of-way fees | CR-8b |
| C-23 | borrowers.other_domestic | interest_rate (+), quantity_traded (−) | at_least_one_as_stated | Loans to other borrowers not made | CR-8a |
| C-25 | taxpayers.other; recipients_other_spending | resources_available_other_uses | at_least_one_decrease | Tax that would have been collected on taxable interest | CR-8b |
| C-27 | buyers.other_construction_work | price_paid (+), quantity_traded (−) | at_least_one_as_stated | Other construction not done while crews build the network | CR-8a |
| C-31 | electricity_customers.not_served | resources_available_other_uses | decrease | Purchases forgone to pay higher electricity bills | CR-8b, CR-3 |

Both sides of every transfer (CR-8b): the backstop (C-4) is paid by electricity customers (U1-a, C-17) or by general-fund recipients, maintenance or capital work (U1-b, C-18), and received by bondholders, which lets the network keep charging $55, a transfer to subscribers (C-1, C-29). Lower incumbent prices (C-5) are a receipt to staying subscribers and a loss to incumbents (C-6). The right-of-way fee falls on both sides at once (incumbents pay less, the city receives less, C-21). Bond buyers chose the bonds over their alternatives, so by CR-5 they expected to gain; the other side of their purchase is C-23 and C-24.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
| --- | --- | --- | --- | --- | --- |
| A-1 | Without the network, incumbents' prices for comparable service would have stayed near $80, following their trend. | counterfactual_trend | 0.75 | Five years of about 3% rises; no other entrant built. | C-1, C-5, C-6, C-14, C-29, C-30, C-33 fail or lose this chain. |
| A-2 | Some households rank the $55 service above the incumbents' offers, and switch. | substitutability | 0.9 | Take-up of public fiber elsewhere; the $25 gap. | C-1, C-2, C-5, C-6, C-7, C-10, C-12, C-14, C-20, C-21, C-22, C-29, C-33 fail. |
| A-3 | Network capacity exceeds peak demand through the medium horizon, so no one who asks is refused. | binding | 0.8 | Sized for 100% take-up at the 2030 peak. | C-2 loses this chain; waiting and crowding would need recording. |
| A-4 | The incumbents' networks are sunk and their cost per subscriber is far below $55, so they keep serving and cut prices rather than withdraw. | durability | 0.75 | Plant in place; retention offers elsewhere. | C-5, C-6, C-10, C-12, C-14, C-21, C-22, C-30, C-33 fail or lose this chain. |
| A-5 | Some households without broadband buy at $55 or at the incumbents' lower prices. | substitutability | 0.8 | Surveys give price as the main reason for not subscribing. | C-8, C-28, C-32 fail. |
| A-6 | Network revenue falls short of debt service in at least one fiscal year from 2030 to 2034. | other | 0.6 | Break-even about 36%; study's 45% assumes incumbents stay at $80. | C-4, C-18 fail; C-17 loses its U1-a shortfall chain. |
| A-7 | The bonds are bought from saving that would otherwise have been lent to other borrowers at home. | other | 0.8 | Tax-exempt bonds held mainly by domestic households and funds. | C-23, C-24, C-25 fail. |
| A-8 | The debt is expected to be repaid on schedule, not rolled over. | expectations | 0.85 | Level amortization; K3. | Not used for a reported sign; it supports reading K3 as a live obligation (C-16). |
| A-9 | Investors value the incumbents on expected earnings and treat the network as likely from the proposal on. | expectations | 0.8 | Analyst coverage; local press. | C-9, C-10 fail. |
| A-10 | The incumbents can organize lobbying at a cost below their stake. | other | 0.9 | Trade association activity. | C-11 fails. |
| A-11 | The private builder would have built in at least one of its two neighborhoods without the network. | other | 0.55 | 2025 permit applications; build-outs elsewhere. | C-13 fails. |
| A-12 | Incumbents adjust their local staff to the subscribers they serve. | alternative_uses | 0.6 | Staffing ratios. | C-20 fails. |
| A-13 | Lenders and rating agencies treat K3 as a contingent liability of CLP. | other | 0.65 | Rating criteria for utility guarantees. | C-16 fails; C-17, C-19, C-31 lose this chain. |
| A-14 | CLP's rates are set on cost of service, including interest on its debt. | other | 0.85 | Council rate ordinance. | C-17, C-18, C-19, C-30, C-31 fail or lose this chain. |
| A-15 | Incumbents can offer term contracts with early-termination fees, and some households sign them. | other | 0.6 | Practice in markets with announced entrants. | C-9 fails. |
| A-17 | Construction contractors hire or add hours for the build. | alternative_uses | 0.8 | Contract volume against local crews. | C-26, C-27 fail. |
| A-18 | Broadband and streaming or home-network equipment are used together by marginal subscribers. | substitutability | 0.6 | Surveys of new subscribers. | C-28 fails. |
| A-20 | Under U1-b, the council later restores spending cut to cover a shortfall through a general rate rise. | revenue_use | 0.45 | Record of deferring rate rises before elections. | Not reported (below 0.5). |
| A-21 | Peak demand reaches network capacity before 2033. | binding | 0.3 | Traffic forecasts. | Not reported (below 0.5). |
| A-22 | CLP uses its control of poles to slow incumbents' work on them. | other | 0.35 | State pole-attachment rules enforced on complaint. | Not reported (below 0.5). |
| A-23 | For an incumbent with older plant, upgrading to fiber keeps enough subscribers to pay. | other | 0.55 | Half the telephone incumbent's subscribers on copper. | C-12 loses its (+) chain and becomes decrease. |
| A-24 | Almost all electricity customers keep buying from CLP when rates rise slightly. | substitutability | 0.9 | No competing supplier; little self-generation. | C-31 loses this chain (customers who leave pay less, not more). |
| A-N1 | Bond buyers would otherwise have held assets whose interest is taxed. | other | 0.6 | NEW. A-7 says the saving would have been lent to other domestic borrowers, mostly through taxable bank, corporate and mortgage lending; some would have gone to other tax-exempt bonds. | C-24, C-25 fail. |
| A-N2 | CLP borrows or refinances debt during the medium horizon, so a change in its borrowing cost reaches its cost of service. | other | 0.7 | NEW. CLP carries debt whose interest is in its rates; a $25 million a year capital program. | C-17, C-19, C-30, C-31 lose this chain. |
| A-N3 | The broadband division pays CLP for shared poles, staff and systems in a way that lowers the costs recovered from electricity rates. | other | 0.35 | NEW. K4 charges operating costs to network revenue, but the ordinance says nothing about cost allocation; network revenue is pledged to bondholders first. | Below 0.5: the opposing chain on C-17 is not reported. |
| A-N4 | City take-up exceeds the number of premises now without broadband (about 8,000) by the medium horizon. | substitutability | 0.85 | NEW. Break-even is 27,700; even the shortfall case (A-6) assumes about 23,400. | C-7, C-20, C-21, C-22 fail. |
| A-N5 | Building in the two neighborhoods does not pay for the private builder against a $55 city service offered at every premises. | alternative_uses | 0.7 | NEW. The builder planned against $80 incumbents; the city offers a comparable service $25 lower with no installation charge. | C-13 fails. |
| A-N6 | Had it built, the private builder would have offered comparable service at or below $55. | other | 0.4 | NEW. Private fiber entrants often price below incumbents but rarely below $60 for 1 Gbps. | Below 0.5: the opposing chain on C-33 is not reported. |
| A-N7 | Local construction labor and equipment are not idle, so added network work raises their price or displaces other work. | other | 0.6 | NEW. A-17's evidence (contract volume relative to local crews). | C-27 fails. |
| A-N8 | For a household that switches, the $25 a month saved exceeds any rise in its electricity bill caused by K3. | other | 0.85 | NEW. Shortfall at 30% take-up is about $38 a year per account against $300 saved; a rating change on CLP's debt is bounded by a contingent liability of about $10 million a year. | C-29 becomes ambiguous. |
| A-N9 | Some electricity customers use less electricity at the margin when its price rises. | substitutability | 0.7 | NEW. Thermostat, appliance and lighting choices; A-24 says they keep buying, not that they buy as much. | C-19 fails. |

**Not reported** (an assumption below 0.5):
- Under U1-b, the council restores cut spending through a later general rate rise, so electricity customers pay after all (A-20, 0.45).
- Congestion at peak and rationing by speed (CR-6 0.7 public supply: crowding margins) if demand reaches capacity (A-21, 0.3). The fixed $55 would then stop conveying that scarcity (CR-11a).
- CLP slows incumbents' work on its poles (CR-4, x: neutral pole access, y: delay; relation shared_facility), raising incumbents' costs (A-22, 0.35).
- Electricity rates fall because the network pays for shared CLP costs (A-N3, 0.35): an opposing chain on C-17.
- Households in the builder's neighborhoods pay more than with the builder, because the builder would have undercut $55 (A-N6, 0.4): an opposing chain on C-33.

## 11. Report

**The policy:** From mid-2027 the city, through its electric utility's new broadband division, offers 1 Gbps service at $55 a month with no installation charge to every premises in Calderby, with the price fixed until mid-2032. The $150 million network is financed by tax-exempt revenue bonds. If network revenue does not cover debt service, the electric utility must make up the difference "from its rates", which may mean raising electricity rates (U1-a) or cutting its other spending (U1-b).

**Visible consequences:** Households that switch pay less for broadband (C-1); the city signs subscribers (C-2) and builds the network (C-3). If take-up stays under about 36%, the electric utility pays shortfalls from 2030 (C-4) and, under U1-a, electricity rates rise (C-17). Incumbents cut prices for those who stay (C-5).

**Invisible consequences:**
- *Incumbents:* lower prices and fewer subscribers (C-6, C-7), a lower return on their sunk local plant (C-14) and a fall in its value from the proposal on (C-10); they lock in subscribers with term contracts before service opens (C-9) and lobby against the network (C-11). Their local staff shrinks (C-20).
- *Would-be entrant:* the private fiber builder stays out (C-13).
- *Electric utility and its customers:* the backstop raises CLP's own borrowing cost (C-16), which passes into electricity rates under either reading (C-17), so electricity use falls slightly (C-19). Under U1-b the shortfall instead comes out of the general-fund transfer, maintenance or capital work (C-18). Township customers and city customers who buy no broadband pay more for electricity and get nothing from the network (C-31).
- *City budget:* right-of-way fees fall with the incumbents' revenue (C-21), so general-fund recipients or city taxpayers lose (C-22).
- *Capital markets and taxpayers elsewhere:* other borrowers pay more or borrow less (C-23); income tax on interest falls (C-24), borne by other taxpayers or recipients of other spending (C-25).
- *Other markets:* construction crews gain work (C-26) while other construction costs more or is delayed (C-27); sellers of home-network equipment and streaming sell more (C-28).
- *Households:* switchers have more to spend on other things (C-29); new subscribers spend on broadband what they spent elsewhere (C-32); households in the builder's neighborhoods pay less than without the policy (C-33).

**Ambiguous effects:** Whether households that stay with an incumbent have more or less to spend (C-30): lower broadband prices against higher electricity rates, with no figure for the incumbents' cut. Whether the telephone incumbent upgrades its copper plant (C-12): upgrading keeps subscribers, but a lower local price lowers the yield on any new investment.

**Key conditions:** Switching (A-2, 0.9) and incumbents' price cuts rather than exit (A-4, 0.75) drive most of the market consequences; the shortfall itself (A-6, 0.6) drives the backstop consequences; lenders' treatment of the backstop (A-13, 0.65) drives the electricity-rate effect that holds under both readings. Nine premises were added (A-N1 to A-N9), two of them below 0.5 and used only to record opposing chains that were not reported.

**What this analysis cannot say:** How large any effect is, so not whether the incumbents' cuts outweigh the electricity rise for staying households, nor whether the network breaks even. Which reading of "from its rates" applies; the text and the city attorney leave it open. Whether the policy is good, or how gains to subscribers weigh against losses to incumbents, electricity customers and taxpayers. Effects on health, safety and the environment are out of scope.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C-1 | subscribers.switching | price_paid (broadband) | decrease | medium | visible | B | CR-1 (op 2: K1 adds a $55 option); CR-2 (those who take it ranked it above the incumbents' offer); CR-4b (switchers were narrowly at the margin); against the counterfactual $80 trend (A-1) | A-1, A-2 |
| C-2 | clp.broadband_division | quantity_traded (city broadband subscriptions) | increase | medium; long | visible | B | CR-1 (op 2); CR-4b (switchers and new subscribers take the new option); CR-5 (exchanges that did not exist take place); no one asking is refused (A-3) | A-2, A-3 |
| C-3 | clp.broadband_division | investment_target (fiber network) | increase | short; medium | visible | A | CR-1 (op 4: K2 puts $150 million at the division's disposal for construction); CR-8a (the resources are directed to the network) | none |
| C-4 | clp | subsidy_outlay (shortfall payments to network debt service) | increase | medium (fiscal 2030 to 2034) | visible | B | CR-1 (op 4, dated and contingent: K3 transfers CLP means to bondholders in shortfall years); CR-8b (every payment is a receipt: bondholders are paid, and the network can keep charging $55); CR-8 0.8 (contingent payer recorded with a premise on the contingency, A-6) | A-6 |
| C-5 | subscribers.staying | price_paid (incumbents' broadband) | decrease | medium; long | visible | B | CR-4 applied to incumbents (x: hold $80 and lose subscribers, y: cut price and keep them; y made relatively better because buyers now have a $55 alternative, A-2); CR-5c (the range of acceptable terms moves down for buyers); CR-6 (with fewer buyers at each price the price moves toward a lower clearing level); CR-7b (the loss settles on the sunk plant, which cannot move, A-4) | A-1, A-2, A-4 |
| C-6 | incumbents | net_price_received (broadband in Calderby) | decrease | medium; long | invisible | B | As C-5, from the seller's side (CR-5c, CR-6, CR-7b) | A-1, A-2, A-4 |
| C-7 | incumbents | quantity_traded (incumbent subscriptions in Calderby) | decrease | medium; long | invisible | B | CR-4a (no subscriber moves to an incumbent because the city offers $55) and CR-4b (switchers leave); CR-9 (substitute); new subscribers who choose an incumbent cannot offset the loss: CR-12e arithmetic with A-N4 (about 8,000 premises lack broadband) | A-2, A-N4 |
| C-8 | subscribers.new | quantity_demanded (broadband) | increase | medium | invisible | B | CR-4 (x: no broadband, y: subscribe; y made better by $55 and by incumbents' cuts); CR-4c | A-5 |
| C-9 | incumbents | term_prevalence (term contracts with early-termination fees) | increase | short; medium | invisible | B | CR-10a (the expected entry alters incumbents' choices before service opens); CR-4 (x: month-to-month, y: term contract that raises the cost of switching later); CR-5c (security of tenure is part of the terms; households accept it for a lower price or a credit) | A-15, A-9 |
| C-10 | incumbents | asset_value (Calderby plant; shares) | decrease | short (from 3 March 2026) | invisible | B | CR-10c (value reflects expected yields); CR-7c (the expected fall in yield, C-6 and C-7, is borne by whoever owns the plant when the network becomes expected, in part at the proposal and more as passage became likely); CR-7b (sunk plant cannot move, A-4) | A-9, A-4, A-2 |
| C-11 | incumbents | lobbying_effort | increase | short; medium | invisible | B | CR-4 (x: accept the network, y: lobby against it or for state limits; y gains because x became worse); CR-8c (resources used up) | A-10 |
| C-12 | incumbents | investment_target (fiber upgrade of older plant in Calderby) | ambiguous | medium | invisible | B | CR-12b: (+) CR-4 (x: keep copper and lose its subscribers to city fiber, y: upgrade and keep them; A-23); (−) CR-7c and CR-4 (x: invest in Calderby, y: invest elsewhere; the lower expected local price, A-4, lowers the yield of any local investment). No premise says which dominates | A-23, A-4, A-2 |
| C-13 | private_fiber_builder | entry_rate (the two neighborhoods) | decrease | medium | invisible | B | CR-4 (x: build, y: stay out; x made worse by a $55 rival at every premises, so a builder narrowly ranking x above y switches; A-N5); CR-4a (no builder enters because of the city's offer); counterfactual entry needs A-11 | A-11, A-N5 |
| C-14 | incumbents | return_on_capital (Calderby plant) | decrease | medium; long | invisible | B | CR-3a (the incumbents' chosen option, selling at about $80, brings less); CR-7b (the loss settles on the sunk local plant) | A-1, A-2, A-4 |
| C-15 | clp.broadband_division | enforcement_cost (trustee fees, audits, administration) | increase | short; medium; long | invisible | A | CR-1 (op 4: K4 charges administration to network revenue); CR-8c (resources spent on administering are used up) | none |
| C-16 | clp | interest_rate (CLP's own borrowing) | increase | short; medium | invisible | B | CR-9 (relation: contract, K3 obliges CLP to pay network shortfalls); CR-5c (lenders who see a new contingent claim on CLP's revenue, A-13, accept its debt only on better terms); CR-10c (the expected burden is priced when the obligation becomes expected, at the bond sale) | A-13 |
| C-17 | electricity_customers | price_paid (electricity) | U1-a: increase; U1-b: increase | medium | visible | B | CR-12d, two independent chains with the same sign. Chain 1 (U1-a only): K3 (CR-1 op 4 on CLP) makes shortfalls a cost of CLP, and cost-of-service rates recover it (A-6, A-14); CR-8 0.8 (contingent payer). Chain 2 (both readings): higher interest on CLP's debt (C-16) enters its cost of service (A-14, A-N2). Opposing chain via shared-cost payments (A-N3, 0.35) is below the cut-off (CR-12 0.8 kind 2) | A-6, A-14, A-13, A-N2 |
| C-18 | city_general_fund; clp | non_tax_receipts (transfer to general fund) (−), maintenance_spending (−), investment_target (electric capital work) (−) | U1-a: no_change; U1-b: at_least_one_decrease | medium | invisible | B | CR-8b (the shortfall paid to bondholders is taken from someone); CR-8 0.8 (record payers per reading). U1-b: rates cannot rise for it, so at least one of CLP's other uses of its existing revenue falls (CR-8a), which one unspecified. U1-a: the shortfall is recovered through rates (A-14), so these uses need not change | A-6, A-14 |
| C-19 | electricity_customers | quantity_demanded (electricity) | decrease | medium | invisible | B | CR-4c (the last kWh, valued least, is the first given up when each kWh costs more; LW-3); some customers are at the margin (A-N9); the rate rise from C-17 chain 2 holds under both readings | A-13, A-14, A-N2, A-N9 |
| C-20 | workers.incumbents | employment (incumbents' local staff) | decrease | medium; long | invisible | B | CR-9 and LW-10 (relation: local labor input_to incumbents' service; fewer subscribers, C-7, lower demand for it, A-12); CR-7a (staff move to other uses) | A-12, A-2, A-N4 |
| C-21 | city_general_fund | non_tax_receipts (right-of-way fees) | decrease | medium; long | invisible | B | CR-9 (relation: incumbents' gross revenue is the base of a 4% fee in force); arithmetic: revenue is price times subscribers, both lower (C-6, C-7), and the city network pays no fee on the revenue it takes over; CR-8b (incumbents pay less, the city receives less) | A-2, A-4, A-N4 |
| C-22 | general_fund_recipients; city_taxpayers | resources_available_other_uses | at_least_one_decrease | medium; long | invisible | B | CR-8b and CR-8 0.7 (a fall in general-fund receipts, C-21, is borne by recipients of city spending or by city taxpayers, which group unspecified). Under U1-b, C-18 adds a second chain in the same direction | A-2, A-4, A-N4 |
| C-23 | borrowers.other_domestic | interest_rate (+), quantity_traded (loans to them) (−) | at_least_one_as_stated | short | invisible | B | CR-8a (saving lent to the city is not available to other borrowers, A-7); CR-6 (with less saving offered to them, at least one margin moves: the rate they pay rises or less is lent to them); CR-7a. Diffuse; chain stops | A-7 |
| C-24 | officials.treasury (federal and state) | tax_revenue (income tax on interest) | decrease | short; medium; long | invisible | B | CR-4 (lender x: taxable asset, y: tax-exempt bond; buyers chose y); CR-8b (interest that would have been taxed, A-N1, is now untaxed under a rule in force, so the treasuries receive less) | A-7, A-N1 |
| C-25 | taxpayers.other; recipients_other_spending | resources_available_other_uses | at_least_one_decrease | medium; long | invisible | B | CR-8b and CR-8 0.7 (lower treasury revenue is made up by other taxpayers or by less spending for others, which group unspecified). Depth 3, diffuse: chain stops | A-7, A-N1 |
| C-26 | construction_contractors | employment (+), hours_worked (+) (fiber construction) | at_least_one_increase | short; medium | visible | B | CR-9 and LW-10 (relation: construction labor input_to the network; C-3 raises demand for it); CR-7a (labor drawn from other uses); A-17 | A-17 |
| C-27 | buyers.other_construction_work | price_paid (+), quantity_traded (−) (other construction work) | at_least_one_as_stated | short; medium | invisible | B | CR-9 (competing for the same crews); CR-7a (crews move to the network until yields equalize, A-N7); CR-6 (at least one margin: price up or work displaced); CR-8a | A-17, A-N7 |
| C-28 | sellers.complements | quantity_complement (home-network equipment, streaming) | increase | medium | invisible | B | CR-9 and LW-10 (relation: complement; more subscribers, C-8, raise demand for goods used with broadband, A-18) | A-5, A-18 |
| C-29 | subscribers.switching | resources_available_other_uses | increase | medium | invisible | B | CR-3 (note: they keep buying broadband and pay $25 a month less); CR-8b (the saving is the incumbents' lost receipt or, in shortfall years, paid by CLP's payers); CR-12e (the opposing electricity chain, C-17, is dominated by A-N8, an empirical premise resting on the case's figures) | A-1, A-2, A-N8 |
| C-30 | subscribers.staying | resources_available_other_uses | ambiguous | medium | invisible | B | CR-12b: (+) CR-3 note and CR-8b (they keep buying from an incumbent at a lower price, C-5, A-1, A-4); (−) CR-3 note (they keep buying electricity at a higher price, C-17: A-13, A-14, A-N2, or U1-a with A-6). No figure for the incumbents' cut, so no dominance premise | A-1, A-4, A-13, A-14, A-N2, A-6 |
| C-31 | electricity_customers.not_served | resources_available_other_uses | decrease | medium | invisible | B | CR-3 note (they keep buying electricity, A-24, at a higher price, C-17, and buy nothing from K1); CR-8b. Holds under both readings through chain 2 of C-17; under U1-a the shortfall chain adds to it | A-13, A-14, A-N2, A-24 |
| C-32 | subscribers.new | resources_available_other_uses | decrease | medium | invisible | B | CR-3c and CR-8a (what they now spend on broadband is withdrawn from other uses; by CR-2 they rank the service above those uses) | A-5 |
| C-33 | subscribers.builder_neighborhoods | price_paid (broadband) | decrease | medium | invisible | B | CR-4 and CR-5c (the city's $55 and incumbents' cuts reach these homes as everywhere, C-1, C-5); opposing chain through the builder's absence (C-13) needs A-N6 (0.4): CR-12 0.8 kind 2, derived sign reported | A-1, A-2, A-4 |

## Gaps found

**(a) Steps no core rule covers.**
- GAP-038-C1: How an incumbent with sunk plant responds to a lower-priced public rival (cut price, harvest, or withdraw) is not decided by the core rules; CR-4 gives each direction once the options are stated, and CR-7b says the loss settles on the sunk plant, but the choice between cutting price and harvesting rests wholly on the case premise A-4. This is a premise, not a missing rule, and is recorded here only because every price consequence (C-5, C-6, C-21, C-30) hangs on it.
- No other step needed more than CR-1 to CR-12, LW-3, LW-10 and arithmetic.

**(b) Core-rule wording that was hard to apply.**
- CR-6, 0.7 "public supply": the clause covers a public supplier with a fixed quantity. K1 has a fixed price and no quantity limit, with spare capacity, and competes with private sellers; its effect runs through the private sellers' prices (CR-4, CR-5c, CR-6 in their market), which the clause does not mention.
- CR-8, 0.8 contingent payers: under U1-a the backstop "may" be met by a rate rise, but nothing stops the council from cutting other spending instead. Recording U1-a as `no_change` for the other uses (C-18) needed the cost-of-service premise A-14; the rule does not say how to treat a reading that permits but does not require a source.
- CR-12e dominance by arithmetic: the case gives the shortfall per electricity account but not the rating effect, so dominance for switchers (C-29) needed an empirical premise (A-N8) built on partial arithmetic. The rule does not say whether a premise that bounds one chain by arithmetic and the other by judgment counts as arithmetic or as empirical; treated as empirical.
- CR-10a and the normal form: term contracts signed before service opens delay switching, but since there is no switching to the city in the counterfactual, the delay is only a path note; its cost to households who later pay a termination fee has no consequence row.

**(c) Vocabulary missing from the ontology.**
- No instrument type for a contingent transfer or guarantee (K3); recorded as text.
- No variable for an obligation or contingent liability, or for a credit rating; C-16 uses `interest_rate` for its effect.
- No variable for a seller's gross revenue; C-21 records the fee base change only through `non_tax_receipts`.
- No variable for the reliability of a utility service; a maintenance cut under U1-b (C-18) could lower it, but `quality_per_unit` is defined for units sold and no premise links maintenance to outages.
- No generic actor class for lenders or rating agencies (`bond_buyers`, `borrowers.other_domestic` were added by role).

## Comparison with the pattern-based analysis

**Summary.** The two versions agree on the market structure of the case: switchers pay less, the city's quantity is set by buyers while capacity is ample, the incumbents lose subscribers, cut prices to those who stay, lose return and asset value from the proposal on, sign more term contracts before the zones open, lobby, and shed local staff; their investment in upgrades is ambiguous; the private builder stays out; other borrowers are crowded out; construction work rises; right-of-way fees fall and general-fund recipients or taxpayers bear it; CLP's own borrowing costs more; and under U1-b the shortfall comes out of CLP's transfer, maintenance or capital work. Both versions reach the open-quantity public supplier without PC-19, from CR-4, CR-5 and CR-6's main clause in the incumbents' market, and both drop OC-8's "repayment implies taxes later" for revenue bonds. The sign differences all come from one place: the pattern version puts the pass-through of CLP's higher interest into electricity rates at the long horizon (its C-25) with no stated premise, though it dates the interest rise itself short to medium (C-19), while the core version puts it in the medium horizon on a stated premise that CLP borrows or refinances then (A-N2, p 0.7). So under U1-b the core signs the electricity price `increase` where the pattern has `no_change`, and the ratepayers who buy no broadband `decrease` where the pattern has `no_change`. The pattern version also lumps switchers and stayers into one household class and leaves a single-chain sign (its C-20, `increase`) next to a combined sign for the same key (its C-26), where CR-1's recording rule asks for a split by response and CR-12 for one combined sign per key. The core splits the class: switchers `increase`, with a dominance premise the case's figures support (A-N8), and stayers `ambiguous`. Most of the eight core-only claims are pattern-version omissions: the lost income tax on tax-exempt interest and who makes it up, CLP's shortfall outlay as the payer side of the backstop, and the electricity customers' smaller use. The core version omitted the incumbents' loss of means, and it signs incumbents' staff `employment` alone where only the group is licensed.

Counts: M 14, V 10, S 4, OP 8, OC 1.

### Pattern version → core version

| Pattern ID | Matched core ID(s) | Class | Cause | Note |
| --- | --- | --- | --- | --- |
| C-1 | C-1 | M | | Pattern horizon "short to medium" from the first zone; core "medium". Same window. |
| C-2 | C-2 | V | | Pattern: `quantity_supplied`; core: `quantity_traded`. Both rest on A-2 and A-3. Pattern cites CR-6's 0.8 public-buyer clause by analogy; the core needs only CR-4 and CR-5, which is enough. |
| C-3 | C-7 | M | | The core adds CR-12e arithmetic with A-N4 to rule out new subscribers who choose an incumbent offsetting the loss. That premise is not needed: the incumbents' price cut is a response to the lost demand and cannot raise their count above the counterfactual (CR-12e, response argument). Harmless. |
| C-4 | C-5 | M | | |
| C-5 | C-6 | M | | |
| C-6 | C-8 | V | | Pattern: `quantity_traded` (households buying); core: `quantity_demanded`. Same A-5. |
| C-7 | C-12 | M | | Both `ambiguous` on A-23 (p 0.55) under CR-12 0.8 kind 2. |
| C-8 | C-11 | M | | |
| C-9 | C-13 | M | | The core adds A-N5 (building does not pay against a $55 city service). That makes explicit the margin premise CR-4b needs; the pattern version rests on A-11 alone. |
| C-10 | C-9 | V | | Pattern class `subscribers.incumbent`; core `incumbents`. The pattern horizon "short (2026 to 2029)" equals the core's "short; medium". |
| C-11 | C-20 | V | | Pattern: `employment`, `hours_worked`, `at_least_one_decrease` (RS-6). Core: `employment` decrease alone. CR-9 with LW-10 gives a fall in demand for incumbents' local labor, not whether staff or hours fall. A-12 ("adjust their local staff") does not separate the two, so the group is what the rules give. Core-version overclaim. |
| C-12 | C-10 | M | | Both date the fall from the 3 March 2026 proposal, in steps as passage becomes likely. |
| C-13 | C-14 | M | | Short to medium. On the long horizon see the last row. |
| C-14 | C-23 | V | | The pattern signs `interest_rate` increase (C-14) and `quantity_traded` decrease (C-15) separately. The core records them as one group, `at_least_one_as_stated`. With a rising supply of saving both move together. Under CR-6's 0.8 clause the rate is a free price, and its rise is enough on its own. The quantity then falls by CR-4c for the other borrowers, so the pattern's separate signs are derivable. The core's group is weaker but valid. Pattern horizon "short to long"; core "short". |
| C-15 | C-23 | V | | As C-14. |
| C-16 | C-26 | M | | |
| C-17 | C-21 | V | | Pattern: `tax_revenue` (TX-10); core: `non_tax_receipts`. The right-of-way fee is a fee on gross revenue, so the core's variable fits the ontology better. |
| C-18 | C-22 | M | | |
| C-19 | C-16 | M | | Both on A-13. |
| C-20 | C-29, C-30 | V | | Single-chain item (cheaper broadband) for switchers and stayers together. The core splits the class and combines the chains: switchers C-29 `increase`, stayers C-30 `ambiguous`. The combined sign is compared under C-26. The pattern version leaves C-20 (`increase`) standing beside C-26 for the same key. That breaks CR-12 (one combined sign per key) and is an analyst error (final check, item 1). |
| C-21 | C-28 | M | | |
| C-22 | C-17 | S | A | Under U1-a both `increase`. Under U1-b the pattern has `no_change`, the core `increase`. The core's second chain (CLP's higher interest, C-16, passed into cost-of-service rates, A-14) reaches the medium horizon on A-N2 (p 0.7: CLP borrows or refinances in that period). The pattern version records the same chain only at the long horizon (C-25). It states no premise for the delay, and dates the interest rise itself "short to medium" (C-19) and its pass-through at "the next rate reviews". The difference is the timing premise. The core states it; the pattern leaves it implicit. |
| C-23 | C-18 | V | | Same per-reading signs. Pattern: general fund as `resources_available_other_uses`; core: `non_tax_receipts` of the general fund, with CLP's maintenance and capital work in both. The core's note (b) adds that U1-a permits but does not require cuts; it relies on A-14 for `no_change`. |
| C-24 | C-31 (with C-29, C-30) | S | A | Under U1-a both `decrease`. Under U1-b the pattern has `no_change`; the core signs non-subscribers and township accounts `decrease` (C-31) through the same interest chain as C-22, on A-N2. Same cause as C-22. |
| C-25 | C-17 | V | | The same interest chain. Pattern: long horizon, `increase`. Core: medium horizon, inside C-17 (chain 2). The core records no separate long-horizon row; nothing is contradicted. |
| C-26 | C-29, C-30 | S | E, A | Pattern: one class of "households buying broadband anyway and paying CLP", U1-a `ambiguous`, U1-b `increase`. Core: switchers `increase` under both readings (C-29, on A-N8: about $300 a year saved against about $38 per account in a 30% take-up year); stayers `ambiguous` under both readings (C-30). Switchers under U1-a: analyst error in the pattern version. CR-1's recording rule asks for a class to be split where responses differ. The pattern version cites the same figures and then declines a dominance premise; CR-12e admits one, with the figures as evidence. Stayers under U1-b: cause A, from the timing premise of C-22. |
| C-27 | C-15 | M | | Both Tier A. The pattern version checks OC-3's baseline (no enforcement made unnecessary); the core does not need to. |
| C-28 | none | OC | E | Incumbents' `resources_available_other_uses` decrease: lower receipts on retained subscribers and lost margin on the rest, on sunk costs. CR-8b gives it with A-1 and A-4; the incumbents keep selling, so the CR-3 note's condition holds. Core-version omission. Its C-6 and C-14 carry the price and return but not the means. |
| — (incumbents' `return_on_capital`, long: "not signed", CR-7a) | C-14 (long) | S | J | The pattern version says returns are equalized in the long run. The core signs a long-run `decrease` on the sunk Calderby plant (CR-7b). Both are defensible, depending on the base of `return_on_capital` ("per unit of capital invested"). On the original outlay, the loss on immobile plant lasts (CR-7b). On the written-down market value, a buyer earns the going rate (CR-7c). CR-7a, which the pattern version cites, applies to means that can move, and the Calderby plant cannot. If anything, the pattern's reason is the weaker one. |

### Core-only consequences

| Core ID | Class | Cause | Note |
| --- | --- | --- | --- |
| C-3 | OP | E | The broadband division's `investment_target` (the network) increase, Tier A (CR-1 op 4, CR-8a). The pattern version records the construction work (C-16) and the crowding out (C-15), but not the investment itself. Minor pattern-version omission. |
| C-4 | OP | E | CLP's `subsidy_outlay` to network debt service, increase in shortfall years (A-6). This is the payer side of K3, with bondholders and, through them, subscribers as recipients. The pattern version records who ultimately bears it (C-22 to C-24) but not CLP's outlay. Pattern-version omission (final check, item 6). |
| C-19 | OP | E | Electricity `quantity_demanded` decrease (CR-4c; A-N9). The pattern version's A-24 says customers keep buying, which does not mean they buy as much. Derivable once a rate rise is signed. Pattern-version omission. Like C-17, it holds under U1-b only on the core's timing premise A-N2. |
| C-24 | OP | E | Federal and state `tax_revenue` (income tax on interest) decrease. Lenders switch from taxable assets to tax-exempt bonds (CR-4, CR-8b; A-7, A-N1). The pattern version's record says the bonds are "tax-exempt" but follows only the crowding-out chain. OC-8 has no clause for it. Pattern-version omission. |
| C-25 | OP | E | Other taxpayers or recipients of other spending, `at_least_one_decrease` (CR-8b and CR-8's 0.7 clause on payers from a general budget). This follows C-24. Pattern-version omission. |
| C-27 | OP | J | Other buyers of construction work pay more or get less done (CR-9, CR-6; A-N7). The pattern version names the forgone uses of the $150 million only through the loan market (C-15; OC-1, "naming the forgone uses"). The core adds a second, real-resource channel for the crews themselves. Both are defensible; the core's adds a premise (A-N7). |
| C-32 | OP | J | New subscribers' `resources_available_other_uses` decrease (CR-3c, CR-8a). This is valid but trivial for a purchase the buyer chose (CR-2). The pattern version did not record it. Depth choice. |
| C-33 | OP | J | Households in the builder's neighborhoods pay less (C-1 and C-5 reach them), with the opposing chain from the builder's absence below the cut-off (A-N6, 0.4). It adds a split of C-1 and C-4 by place; the pattern version stopped at "the unseen supply" (C-9). Defensible either way. |

### Findings

- **Pattern overclaims or hidden premises.** No pattern, applied as written, produced a wrong sign here. The pattern version did hide one premise: it puts the pass-through of CLP's higher interest into electricity rates at the long horizon (C-25) with no premise, though its own C-19 dates the interest rise short to medium and its text says "the next rate reviews". That unstated timing choice is what gives `no_change` under U1-b in C-22, C-24 and C-26. As written, OC-8 adds a taxpayer group for repayment, which is wrong for revenue bonds; the pattern version overrode it, rightly. OC-8 also lacks the tax-exemption chain (core C-24, C-25): tax-exempt public borrowing moves lenders out of taxed assets, and the treasuries' loss is a CR-8b transfer with a payer group to name.
- **Errors in the core version.** Overclaim: incumbents' local staff signed `employment` decrease alone (C-20), where CR-9 gives only the `employment`, `hours_worked` group. Omission: the incumbents' loss of means (pattern C-28). Weak evidence: A-N2 cites "a $25 million a year capital program", but the record says that program is paid from rates, not borrowed. The premise rests instead on CLP's existing debt being refinanced in the period, which the record does not date. Unneeded premise: A-N4 for C-7 (the response argument of CR-12e already bounds it).
- **Errors in the pattern version.** Recording: switchers and stayers lumped into one class, and C-20 left beside C-26 with two signs for one key (CR-1 recording, CR-12). Combination: C-26 under U1-a left `ambiguous` for switchers, though the figures it quotes support a dominance premise. Omissions: CLP's shortfall outlay (C-4), the treasuries' lost tax on tax-exempt interest and its payers (C-24, C-25), electricity use (C-19) and the broadband investment itself (C-3). Weak reason: the long-run `return_on_capital` is left unsigned on CR-7a, which applies to mobile means.
- **Limits of the core rules.** None produced a difference: no row needed cause K. The open-quantity public supplier is derived in both versions from CR-4, CR-5c and CR-6's main clause in the incumbents' market. The core version's GAP-038-C1 (cut price or harvest) is a premise (A-4), as it says. Unclear core-rule wording, all noted by one or both versions: CR-6's public-supply clauses state the fixed-quantity supplier and the open-quantity buyer, but not the open-quantity seller. CR-8's 0.8 contingent-payer clause says "per reading or with a premise" where both are needed, and it does not say how to treat a reading that permits a source but does not require it (U1-a). CR-12e does not say whether a premise that bounds one chain by arithmetic and the other by judgment counts as arithmetic or as empirical (A-N8). CR-10a gives a path note but no consequence row for the termination fees households pay under contracts signed because of the policy.
- **Test of 0.8 verdicts.** *PC-19 (partial: correct refusal, no coverage):* confirmed. The core version reached C-2 and C-5 to C-7 without it and found no rationing while capacity is ample. *CR-6 0.7/0.8 public supply (needed interpretation, applied by analogy):* confirmed that the clauses do not cover a public seller with an open quantity (core gap b, first item). The core shows the analogy is not needed, though: CR-4 and CR-5 set the city's quantity, and CR-6's main clause, in the incumbents' market, sets the price. So the clause needs one sentence, not a new mirror case. *OC-8 (needed interpretation and one override):* confirmed. The core records no later taxes and finds a further omission (the tax-exemption chain). *CR-8 0.8 contingent payers (one interpretation, "or" read as "and"):* confirmed. Core C-4 and C-18 carry both A-6 and per-reading signs, and the core adds a second unclear point (a permissive reading). *OC-3 funding bullet read with CR-8 0.8:* neither confirmed nor contradicted. The core records administration as used up (C-15) and does not trace its payers separately, which is consistent with the pattern version's reading.
