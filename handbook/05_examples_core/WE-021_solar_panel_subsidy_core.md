# WE-021 / Analysis: Per-watt subsidy for rooftop solar, funded by an electricity surcharge

Analyst: core-only re-run (Handbook 0.4)  |  Rules: core rules CR-1 to CR-12 only  |  Status: awaiting comparison

## 1. Policy record

**Calvera Rooftop Solar Incentive.** Calvera is a state of about 5 million people and 1.8 million households, about 60% of whom own their homes. Electricity is sold by three utilities whose rates are set by the state Utility Commission to recover their costs, almost entirely through per-kWh charges; the fixed monthly charge is small. Retail electricity costs about 20 cents per kWh. Existing law already credits rooftop solar owners for power they export at the full retail rate (net metering); this policy does not change that. Panels and inverters are imported; Calvera buys well under 1% of world output. Before the policy, about 900 installers put up about 15,000 systems a year (about 105 MW) at about $2.80 per watt, of which hardware is about $1.00 and labor, permits, sales and margin about $1.80.

The governor's bill was introduced on 1 September of Year 0 with enough support to be expected to pass. It was enacted on 1 November and takes effect on 1 January of Year 1. It ends when 900 MW has been funded, or on 31 December of Year 5, whichever comes first.

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Subsidy | `per_unit_subsidy` | Rooftop solar systems on residential buildings in Calvera | Building owners who install, through a certified installer | $0.50 per watt of panel nameplate capacity for the first 300 MW funded statewide; $0.35 for the next 300 MW; $0.20 for the next 300 MW; then none. At most 10 kW per building. Paid to the installer after the utility approves connection, and deducted on the customer's invoice. Funded capacity is published weekly. | Commercial and ground-mounted systems. |
| K2 Surcharge | `per_unit_tax` | Retail electricity sales | All utility customers (households, businesses, public bodies), collected by utilities | 0.12 cents per kWh, about $60 million a year (about $10 a year for a typical household); paid into a state Solar Fund. The Commission resets it each year to match projected payments. | None |
| K3 Certification | Condition of K1 | Installers who claim the subsidy | Installers | A licensed electrician on staff, a three-day course and a $500 fee. | — |
| K4 Administration | Enforcement | K1 to K3 | State Energy Office, funded from 5% of the Solar Fund | Checks claims against utility connection records; inspects 5% of systems; clawback and loss of certification for false claims. | — |

Unclear provisions: what happens to money left in the fund when the program ends; whether the surcharge stops at once. Assumed it stops at once and any balance is credited back on bills.

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | CR-1 operations | Core rules applied |
| --- | --- | --- | --- | --- |
| K1 Subsidy | binary (state gives) | Yes for marginal adopters (A-2); a pure transfer for adopters who would have installed anyway | 3 (a payment is attached to the option 'install a residential rooftop system through a certified installer'); 4 (means transferred from the Solar Fund to the buyer or installer) | CR-4, CR-5c, CR-6, CR-7, CR-9, CR-10a, CR-10c |
| K2 Surcharge | binary (state takes) | Yes: collected on every kWh (A-3) | 4 (means transferred from every electricity customer to the Solar Fund); 3 (a charge attached to each kWh bought) | CR-4c, CR-5c, CR-8a, CR-8b |
| K3 Certification | condition of K1 (attaches a burden to claiming) | Yes for installers without a licensed electrician (A-N2); a fixed cost for all claimants | 3 (course, fee and staff requirement attached to the option 'claim the subsidy'); 1 (claiming is removed for installers who cannot meet it) | CR-3a, CR-4, CR-8c |
| K4 Administration | binary (5% of the fund used up) | Yes | 4 (means transferred to the Energy Office); 3 (risk of clawback and decertification attached to false claims) | CR-8c, CR-4 (x: claim honestly, y: claim falsely) |

All four components are binary in Rothbard's terms: the state takes (K2) and gives (K1). K3 and K4 are conditions on the giving. The policy does not fix any price; CR-6 enters only where installation capacity is fixed in the short run.

## 3. Actor classes

| Actor class | Role | How its options change (CR-1) |
| --- | --- | --- |
| households.adopting.marginal | Building owners who install because of K1 | Option 'install' brings a payment (op 3); they switch from buying only grid power (CR-4). |
| households.adopting.inframarginal | Building owners who would have installed in the same period anyway | Same op 3; no change of action, so K1 is a transfer to them and their installer (op 4). |
| households.adopting.pulled_forward | Owners who would have installed later without K1 (A-15) | Op 3 on 'install now' relative to 'install later' (CR-4, x: later, y: now). |
| electricity_customers | Every household, business and public body that buys grid power | Op 4 (surcharge paid); op 3 on each kWh bought. |
| electricity_customers.non_adopting | Customers who do not install, including most renters | Pay K2 and any rate reset caused by lower sales; receive no K1 payment. |
| installers.certified | Current installers who certify | Op 3: selling residential systems brings a payment, conditional on K3; op 3: course, fee, staff requirement, inspections. |
| installers.uncertified | Installers who cannot or do not certify (A-N2) | Op 1: they cannot offer the subsidized price. |
| installers.prospective | Would-be entrants | Entry now brings the subsidized demand (CR-4, x: stay out, y: enter). |
| workers.electricians_roofers | Owners of the labor installers need | Through CR-9 (input_to): more bids for their labor. |
| buyers.electrical_roofing_work | Households and builders who buy electrical and roofing work for other ends | Through CR-9: compete with installers for the same labor. |
| buyers.commercial_solar | Buyers of commercial and ground-mounted systems (exempt) | Through CR-9 (same_market_other_segment): compete for the same installer capacity. |
| hardware_suppliers | Importers and distributors of panels and inverters | Through CR-9 (input_to): more orders; world price set elsewhere (A-11 false). |
| utilities | Sellers of grid power; collect K2 | Op 3: collection duty; through CR-9 (substitute): lower sales to adopters. |
| generators.wholesale | Sellers of wholesale power | Through CR-9 (substitute): rooftop output displaces midday purchases (A-14). |
| officials.energy_office | Administers K1 to K4 | Op 4: 5% of the fund; tasks of checking and inspecting. |
| large_electricity_users | Businesses with large bills | Op 4 via K2; lobbying against it becomes worth more (CR-4, x: accept, y: lobby). |

## 4. Direct effect

CR-1 and CR-2: the immediate change for those whose options K1 and K2 alter.

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-1 | households.adopting | price_paid (rooftop systems, net of subsidy) | decrease | short; medium | CR-1 op 3, CR-5c, CR-7b | A-1 |
| C-2 | installers.certified | net_price_received (per watt, including subsidy) | increase | short; medium | CR-5c, CR-6, CR-7b, CR-9 | A-2, A-4, A-18, A-12 |
| C-3 | installers.certified | subsidy_share_received | increase | short | CR-7b | A-18, A-4 |
| C-4 | electricity_customers | price_paid (electricity) | increase | short | CR-1 op 4, CR-5c | A-3 |
| C-5 | officials.energy_office (Solar Fund) | tax_revenue | increase | short; medium | CR-1 op 4, CR-8b | - |

## 5. Responses

CR-4 applied to every pair of options each actor class has; CR-5 for exchanges that now take place; CR-10a for timing.

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-6 | households.adopting.marginal | quantity_demanded (residential rooftop systems) | increase | short; medium | CR-4 (x: grid power only, y: install), CR-4c | A-2 |
| C-7 | installers.certified | quantity_traded (residential rooftop systems) | increase | short; medium | CR-4, CR-5, CR-6 | A-2, A-4 |
| C-8 | households.adopting | transaction_size (kW per system) | increase | short; medium | CR-4c (x: smaller system, y: larger system) | A-6 |
| C-9 | households.adopting | quantity_traded (installations, 1 Sep to 31 Dec of Year 0) | decrease | short (announcement window) | CR-10a, CR-4 (x: install now, y: install after 1 January) | A-8 |
| C-10 | households.adopting | wait_time (installation backlog) | increase | short; medium | CR-10a, CR-4 (x: install after a step-down, y: before), CR-6 | A-7, A-4 |
| C-11 | households.adopting.pulled_forward | quantity_traded (residential rooftop systems after the program ends) | decrease | long (after the program ends) | CR-10a, CR-4 (x: install later unsubsidized, y: install now subsidized) | A-15 |
| C-12 | households.adopting | reclassification (systems designed to fit the residential rooftop definition) | increase | short; medium | CR-4 (x: exempt form, y: covered form) | A-N1 |
| C-13 | installers.certified | compliance_cost | increase | short | CR-1 op 3, CR-8c | - |
| C-14 | installers.uncertified | quantity_supplied (residential rooftop systems) | decrease | short; medium | CR-1 op 1, CR-4 (x: uncertified seller, y: certified seller) | A-N2 |
| C-15 | installers.prospective | entry_rate | increase | medium | CR-4 (x: stay out, y: enter), CR-7a | A-5, A-2 |
| C-16 | installers.certified | asset_value (installer businesses) | increase | short (from announcement) | CR-7c, CR-10c | A-18, A-4 |
| C-17 | installers.certified, hardware_suppliers | lobbying_effort (to extend or enlarge the program) | increase | medium; long | CR-4 (x: accept the end, y: lobby), CR-10a, CR-8c | A-9, A-17 |
| C-18 | large_electricity_users | lobbying_effort (against the surcharge) | increase | short; medium | CR-4 (x: accept, y: lobby), CR-8c | A-9, A-3 |
| C-19 | electricity_customers | quantity_demanded (grid electricity) | decrease | short; medium | CR-4c | A-3 |
| C-20 | officials.energy_office | enforcement_cost | increase | short; medium | CR-1 op 4, CR-8c | - |
| C-21 | utilities | compliance_cost (collecting the surcharge, connection records) | increase | short | CR-1 op 3, CR-8c | - |

## 6. Second-order effects

CR-9 along named relations, then CR-5 to CR-7 in each market reached. Depth limit 4; diffuse effects on customers of businesses that pay the surcharge (relation: electricity input_to their goods) are pruned at depth 3 as diffuse bystander effects. Rows marked with an opportunity cost also appear in section 9.

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C-22 | workers.electricians_roofers | wage_rate | increase | short; medium | CR-9, LW-10, CR-7a | electrician and roofer labor input_to rooftop installation (close) | A-12, A-2 |
| C-23 | buyers.electrical_roofing_work | price_paid (electrical and roofing work outside rooftop solar) | increase | short; medium | CR-9, CR-7a | same labor input_to other electrical and roofing work (close) | A-12, A-2 |
| C-24 | buyers.electrical_roofing_work | quantity_traded (electrical and roofing work outside rooftop solar) | decrease | short; medium | CR-4c, CR-8a | as above | A-12, A-2 |
| C-25 | buyers.commercial_solar | price_paid (commercial and ground-mounted installation) | increase | short | CR-7a, CR-9 | commercial solar same_market_other_segment of residential rooftop solar (close in installer capacity) | A-4, A-2 |
| C-26 | buyers.commercial_solar | quantity_traded (commercial and ground-mounted systems) | decrease | short | CR-4c, CR-8a | as above | A-4, A-2 |
| C-27 | hardware_suppliers | quantity_traded (imported panels and inverters) | increase | short; medium | CR-9, LW-10 | panels and inverters input_to rooftop installation (close) | A-2 |
| C-28 | households.adopting | quantity_substitute (grid electricity bought) | decrease | medium; long | CR-4 (x: grid power, y: own output), CR-10b | rooftop output substitute for grid electricity (close) | A-10, A-2 |
| C-29 | utilities | quantity_traded (grid electricity) | decrease | medium; long | CR-9, CR-10b | rooftop output substitute for grid electricity (close) | A-10, A-2 |
| C-30 | electricity_customers.non_adopting | price_paid (electricity) | ambiguous | medium; long | CR-12b over three chains | rooftop output substitute for grid electricity; wholesale power input_to retail electricity | A-3, A-10, A-13, A-14 |
| C-31 | generators.wholesale | net_price_received (midday wholesale power) | decrease | medium; long | CR-9, CR-6 | rooftop output substitute for wholesale power (partial) | A-14, A-10 |
| C-32 | workers.installers | employment (residential solar installation) | increase | medium | CR-9, LW-10, CR-7a | installation labor input_to rooftop installation (close) | A-2, A-5 |
| C-33 | workers.installers | employment (residential solar installation) | decrease | long (after the program ends) | CR-10a, CR-9, LW-10 | installation labor input_to rooftop installation (close) | A-15 |
| C-34 | installers.certified | net_price_received (per watt) | decrease | long (after the program ends) | CR-10b, CR-10a, CR-6 | - | A-15, A-17 |
| C-35 | installers.certified | asset_value (installer businesses) | decrease | long (as the end approaches and after) | CR-7c, CR-10c, CR-10b | - | A-15, A-17 |
| C-36 | electricity_customers | resources_available_other_uses | decrease | short; medium | CR-8a, CR-8b, CR-3c | - | - |
| C-37 | households.adopting.inframarginal | resources_available_other_uses | increase | short; medium | CR-8b, CR-7b | - | A-1 |
| C-38 | households.adopting.marginal | resources_available_other_uses | decrease | short | CR-3c, CR-8a | - | A-2 |
| C-39 | households.adopting.marginal | resources_available_other_uses | increase | long | CR-2, CR-4, CR-10b | - | A-2, A-10 |

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (-) | Dominance premise | Combined sign |
| --- | --- | --- | --- | --- |
| electricity_customers.non_adopting, price_paid, medium; long | K2 surcharge (CR-1, medium only); fixed costs over fewer kWh and full-retail export credits (CR-9, arithmetic, A-13) | lower midday wholesale prices passed to retail (CR-9, CR-6, A-14) | None stated | ambiguous (C-30) |
| installers.certified, net_price_received, short; medium | higher demand at fixed capacity (CR-6, CR-7b); higher wage costs (CR-9, medium) | entry (CR-7a, medium) brings the price back toward cost, but cost itself is higher | Not needed for the sign relative to the counterfactual: cost per watt is higher (A-12), so the price received stays above it | increase (C-2) |
| installers.certified, net_price_received, long | - | excess capacity and pulled-forward demand (CR-10a, CR-10b) | - | decrease (C-34) |
| households.adopting.marginal, resources_available_other_uses | long: bill savings (C-39) | short: own outlay (C-38) | Different horizons: not netted (CR-12c by horizon); a one-time cost against a later stream is not combined | decrease (short); increase (long) |
| workers.installers, employment | medium (C-32) | long (C-33) | Different horizons | increase (medium); decrease (long) |

## 8. Time structure

- **Announcement (1 September to 31 December of Year 0).** The payment was expected four months before it started. Owners who would have installed in that window wait (CR-10a; C-9), and installer business values rise when the payment becomes expected (CR-7c; C-16). In early Year 1, the deferred demand and the new demand meet fixed capacity (A-4), which feeds C-10 and C-2.
- **Step-downs.** The rate falls at 300 MW and 600 MW of funded capacity, and the count is published weekly (CR-11c: the policy conveys when the step comes). Demand bunches before each step-down (CR-10a, CR-4 with x: install after, y: install before). Relative to the counterfactual both windows have more installations; the bunching is a note on the path, recorded as a consequence only through C-10.
- **Capacity.** Installer capacity is fixed in year 1 (A-4, A-18) and grows by entry in later years (A-5, CR-7a). The share of the payment kept by installers (C-3) is therefore largest at the start and falls as entry proceeds; no sign is claimed for it after year 1.
- **Surcharge reset.** The Commission resets K2 each year to match projected payments, so faster adoption and larger systems (C-8) raise later surcharges (arithmetic on the policy text).
- **End of program.** The program ends at 900 MW or on 31 December of Year 5. A dated end, and a capacity end that is published weekly, bring purchases forward (CR-10a). After the end, purchases are lower than they would have been (C-11), and capacity built for the program persists (CR-10b; A-17), which pushes down prices, employment and installer business values (C-34, C-33, C-35). Those with a stake in the program lobby to extend it (C-17).
- **Durability.** Panels last decades (CR-10b), so the effects on grid purchases, utility sales and electricity rates (C-28, C-29, C-30) continue after the subsidy and the surcharge stop.

## 9. Opportunity costs

Each is written as a signed change in a variable.

| ID | Actor class | Variable | Sign | What is given up | Rules |
| --- | --- | --- | --- | --- | --- |
| C-13 | installers.certified | compliance_cost | increase | Course time, fees, staff and paperwork that would have served other ends of installers | CR-1 op 3, CR-8c |
| C-17 | installers.certified, hardware_suppliers | lobbying_effort (to extend or enlarge the program) | increase | Staff time and money spent seeking an extension | CR-4 (x: accept the end, y: lobby), CR-10a, CR-8c |
| C-18 | large_electricity_users | lobbying_effort (against the surcharge) | increase | Staff time and money spent opposing the surcharge | CR-4 (x: accept, y: lobby), CR-8c |
| C-20 | officials.energy_office | enforcement_cost | increase | 5% of the fund, which electricity customers would otherwise have kept | CR-1 op 4, CR-8c |
| C-21 | utilities | compliance_cost (collecting the surcharge, connection records) | increase | Billing and records work that would have served other ends | CR-1 op 3, CR-8c |
| C-24 | buyers.electrical_roofing_work | quantity_traded (electrical and roofing work outside rooftop solar) | decrease | Renovation and repair work not done because the labor was drawn into installations | CR-4c, CR-8a |
| C-26 | buyers.commercial_solar | quantity_traded (commercial and ground-mounted systems) | decrease | Commercial and ground-mounted systems not installed while capacity is drawn to the subsidized segment | CR-4c, CR-8a |
| C-36 | electricity_customers | resources_available_other_uses | decrease | About $60 million a year of purchases customers would have made | CR-8a, CR-8b, CR-3c |
| C-38 | households.adopting.marginal | resources_available_other_uses | decrease | Other purchases or saving forgone by owners who install because of the payment | CR-3c, CR-8a |

CR-8's symmetry is applied throughout: the surcharge paid (C-36) is matched by the payments received by adopters (C-37) and installers (C-3); the labor drawn into installations (C-22) is matched by work not done elsewhere (C-24, C-26); administration, compliance and lobbying (C-20, C-21, C-13, C-17, C-18) are used up (CR-8c).

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
| --- | --- | --- | --- | --- | --- |
| A-1 | Installers do not capture the whole subsidy. | other | 0.85 | About 900 competing installers; subsidy shown on the invoice; quotes before and after the start. | These consequences fail or lose this chain: C-1, C-37. |
| A-2 | Some households at the margin install because of the subsidy. | substitutability | 0.9 | The subsidy is about 18% of installed cost; surveys of intentions; payback periods. | These consequences fail or lose this chain: C-2, C-6, C-7, C-15, C-22, C-23, C-24, C-25, C-26, C-27, C-28, C-29, C-32, C-38, C-39. |
| A-3 | The surcharge is passed through to customers in full, and their demand changes little. | other | 0.95 | Commission order; studies of electricity demand response. | These consequences fail or lose this chain: C-4, C-18, C-19, C-30. |
| A-4 | Installation labor cannot grow much within the first year. | other | 0.7 | Electrician licensing time; installer job vacancies; backlog data. | These consequences fail or lose this chain: C-2, C-3, C-7, C-10, C-16, C-25, C-26. |
| A-5 | Certification is easy enough that new installers enter. | other | 0.8 | Requirements of K3; supply of licensed electricians in related trades. | These consequences fail or lose this chain: C-15, C-32. |
| A-6 | Oversizing toward the 10 kW limit is feasible and pays under net metering. | other | 0.65 | Roof sizes; inverter ratios in claim data; retail-rate export credit. | These consequences fail or lose this chain: C-8. |
| A-7 | Installer capacity is limited near step-downs, so backlogs form. | other | 0.75 | Weekly capacity dashboard; installer staffing. | These consequences fail or lose this chain: C-10. |
| A-8 | Households knew of the subsidy from September and could wait. | expectations | 0.8 | Publicity; installers' reports of deferred contracts. | These consequences fail or lose this chain: C-9. |
| A-9 | Installers, suppliers and large users can organize to lobby. | other | 0.85 | Existing solar trade association; industrial users' group. | These consequences fail or lose this chain: C-17, C-18. |
| A-10 | Adopters buy less grid power after installing. | substitutability | 0.95 | Utility billing data for existing solar customers. | These consequences fail or lose this chain: C-28, C-29, C-30, C-31, C-39. |
| A-11 | Calvera's purchases are large enough to raise world panel prices. | other | 0.05 | Share of world shipments. | No reported consequence rests on it (see Not reported). |
| A-12 | Electricians and roofers are scarce and fully used elsewhere. | other | 0.8 | Trade employment and wage data; job vacancies. | These consequences fail or lose this chain: C-2, C-22, C-23, C-24. |
| A-13 | The Commission recovers fixed grid costs mainly per kWh, those costs do not fall with sales, and net metering credits exports at the full retail rate. | other | 0.8 | Rate design; net metering statute; utilities' cost structure. | These consequences fail or lose this chain: C-30. |
| A-14 | Rooftop output is large enough to lower midday wholesale prices (it is not offset by withdrawal of other supply), and the reduction reaches retail rates. | substitutability | 0.55 | 900 MW against a state peak of about 9 GW; wholesale market design; pass-through rules. | These consequences fail or lose this chain: C-30, C-31. |
| A-15 | Some adopters would have installed later without the subsidy. | expectations | 0.8 | Adoption trend; falling panel prices. | These consequences fail or lose this chain: C-11, C-33, C-34, C-35. |
| A-16 | Fraudulent claims are made on a meaningful scale. | enforcement | 0.2 | Connection-record checks; inspection rate. | No reported consequence rests on it (see Not reported). |
| A-17 | Entrants make investments specific to solar installation that lose value when the program ends. | durability | 0.7 | Certification, vehicles, training; experience of installers after other programs ended. | These consequences fail or lose this chain: C-17, C-34, C-35. |
| A-18 | In the first year, installers have clearly fewer alternatives than households: their capacity is fixed by the number of licensed electricians (A-4), while households can wait or keep buying grid power. | substitutability | 0.65 | Backlogs and quotes after the start; electrician licensing time; share of households who defer installation. | These consequences fail or lose this chain: C-2, C-3, C-16. |
| A-N1 | Some owners who would have installed a ground-mounted or commercial system can install a residential rooftop system instead, or describe the building so that it qualifies. | substitutability | 0.55 | NEW. Rural lots with both options; mixed-use buildings; K1 excludes commercial and ground-mounted systems by form, not by owner. | These consequences fail or lose this chain: C-12. |
| A-N2 | Some current installers lack a licensed electrician on staff and do not certify, at least in the first year. | other | 0.6 | NEW. K3 requires an electrician on staff; small installers and roofers who subcontract electrical work; electrician scarcity (A-12). | These consequences fail or lose this chain: C-14. |

**Not reported** (an assumption below 0.5):
- World panel and inverter prices rise because of Calvera's purchases (CR-9, CR-6): needs A-11 (p 0.05).
- False claims on a meaningful scale, with clawbacks and decertification (CR-4, x: claim honestly, y: claim falsely; CR-8c): needs A-16 (p 0.2). The direction of the incentive is a priori (CR-4a: no installer becomes more honest because of a payment for claims), but the scale is not.
- Installers capture the whole payment, so adopters' price does not fall: needs the negation of A-1 (p 0.15).

## 11. Report

**The policy:** From 1 January of Year 1, owners of residential buildings in Calvera who have a rooftop solar system installed by a certified installer receive $0.50 per watt (falling to $0.35 and $0.20 as funded capacity passes 300 MW and 600 MW, up to 10 kW per building), deducted on the invoice. The money comes from a surcharge of 0.12 cents on every kWh of electricity sold, about $60 million a year. Installers must certify to claim. The program ends at 900 MW or at the end of Year 5.

**Visible consequences:** Owners who install pay less for a system (C-1), and more systems are installed (C-6, C-7). Every electricity customer pays more per kWh in the short run (C-4), and the Solar Fund collects the surcharge (C-5). Employment in installation rises while the program runs (C-32).

**Invisible consequences:**
- *Installers:* In the first year, when capacity is fixed, installers keep part of the payment as a higher price (C-2, C-3), and their businesses gain value from the announcement (C-16). They bear certification and claim costs (C-13). New installers enter (C-15). Installers who do not certify lose customers (C-14). After the program ends, prices, employment and business values are lower than they would have been, because purchases were brought forward and capacity built for the program remains (C-34, C-33, C-35).
- *Owners who install:* Systems are larger (C-8); some designs are shaped to qualify (C-12); there is a wait before step-downs (C-10); purchases are held back in the announcement window (C-9) and are lower after the program ends (C-11). Marginal adopters give up other uses of their share of the cost now (C-38) and buy less grid power later (C-28, C-39). Owners who would have installed anyway receive a transfer (C-37).
- *Electricity customers:* They have less to spend on other things (C-36) and buy slightly less electricity (C-19). Large users lobby against the surcharge (C-18).
- *Other trades and markets:* Electricians' and roofers' wages rise (C-22); other electrical and roofing work costs more and less of it is done (C-23, C-24); commercial and ground-mounted solar buyers pay more and install less in the first year (C-25, C-26); more hardware is imported (C-27). Utilities sell less grid power (C-28, C-29); midday wholesale prices fall (C-31).
- *Administration:* the Energy Office and utilities use resources to run the program (C-20, C-21); installers and suppliers lobby to extend it (C-17).

**Ambiguous effects:** The electricity price paid by customers who do not install, in the medium and long run (C-30). The surcharge and the recovery of fixed grid costs over fewer kWh push it up; lower midday wholesale prices push it down. What would decide it: the size of fixed costs recovered per kWh against the pass-through of lower wholesale prices.

**Key conditions:** Marginal households respond to the payment (A-2, 0.9); installers have fewer alternatives than households in year 1 (A-18, 0.65) and labor is fixed in year 1 (A-4, 0.7), which decide who keeps the payment at first; some adopters would have installed later anyway (A-15, 0.8), which drives the post-program dip; entrants' investments are specific (A-17, 0.7); rate design recovers fixed costs per kWh (A-13, 0.8) and rooftop output lowers wholesale prices (A-14, 0.55), which pull the non-adopters' price in opposite directions. Two premises were added: some owners can reshape a project into the rooftop form (A-N1, 0.55) and some installers do not certify (A-N2, 0.6).

**What this analysis cannot say:** How large any of these effects is, so it cannot say whether non-adopters' electricity prices end up higher or lower, or how the payment is split between owners and installers after year 1. It does not weigh the gains to adopters and installers against the losses to electricity customers and other buyers of labor, or say whether the policy is good. Environmental effects, including any effect on emissions, are out of scope, as are health and safety effects. Fraud is not reported because its premise is unlikely (A-16).

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C-1 | households.adopting | price_paid (rooftop systems, net of subsidy) | decrease | short; medium | visible | B | CR-1 (op 3: K1 attaches a payment to installing, deducted on the invoice); CR-5c (any change in what one party may receive moves the range of acceptable terms); CR-7b (the gain is split according to who has fewer alternatives; A-1: installers do not keep all of it) | A-1 |
| C-2 | installers.certified | net_price_received (per watt, including subsidy) | increase | short; medium | invisible | B | CR-5c (the range of acceptable terms moves up for the installer); CR-6 (more buyers at each net price while installation labor is fixed, A-4, pushes the price received toward a higher clearing level); CR-7b (in year 1 the gain settles on the side with fewer alternatives, A-18); medium: CR-9 (input_to: higher wages for electricians and roofers, A-12, raise the cost the price must cover) | A-2, A-4, A-18, A-12 |
| C-3 | installers.certified | subsidy_share_received | increase | short | invisible | B | CR-7b (the lasting gain settles on the means that cannot move: in year 1 installation capacity is fixed by the number of licensed electricians, while households can wait or keep buying grid power, A-18, A-4) | A-18, A-4 |
| C-4 | electricity_customers | price_paid (electricity) | increase | short | visible | B | CR-1 (op 4 and op 3: K2 adds 0.12 cents to every kWh); CR-5c (the charge moves the range of terms; A-3: passed through in full by Commission order) | A-3 |
| C-5 | officials.energy_office (Solar Fund) | tax_revenue | increase | short; medium | visible | A | CR-1 (op 4: K2 transfers about $60 million a year into the Solar Fund); CR-8b (every payment is a receipt to someone: the fund receives what customers pay) | none |
| C-6 | households.adopting.marginal | quantity_demanded (residential rooftop systems) | increase | short; medium | visible | B | CR-4 (x: buy grid power only, y: install; y made better by K1, so owners for whom y ranked narrowly below x switch); CR-4c (more units bought as each unit is cheaper) | A-2 |
| C-7 | installers.certified | quantity_traded (residential rooftop systems) | increase | short; medium | visible | B | CR-4 (marginal households install, C-6); CR-5 (exchanges take place that would not have); CR-6 (in year 1 the added demand meets fixed capacity, so the increase is limited and partly taken in price and waiting, A-4) | A-2, A-4 |
| C-8 | households.adopting | transaction_size (kW per system) | increase | short; medium | invisible | B | CR-4c (each added watt up to 10 kW brings $0.50, $0.35 or $0.20, so the last watt, valued least, is now cheaper and more watts are bought; x: smaller system, y: larger system); net metering credits the extra output at the retail rate (A-6) | A-6 |
| C-9 | households.adopting | quantity_traded (installations, 1 Sep to 31 Dec of Year 0) | decrease | short (announcement window) | invisible | B | CR-10a (a change expected in the future alters choices now); CR-4 (x: install in the window without the payment, y: wait until 1 January for it; y made better, so owners who would have installed in the window wait) | A-8 |
| C-10 | households.adopting | wait_time (installation backlog) | increase | short; medium | invisible | B | CR-10a and CR-4 (x: install after the next step-down, y: before it; the weekly count of funded capacity tells owners when the step-down comes, CR-11c); demand bunches before each step-down while capacity is fixed (A-7, A-4); CR-6 (where quoted prices do not rise at once, the gap is closed by queuing) | A-7, A-4 |
| C-11 | households.adopting.pulled_forward | quantity_traded (residential rooftop systems after the program ends) | decrease | long (after the program ends) | invisible | B | CR-4 (x: install later without the payment, y: install now with it); CR-10a (purchases that would have been made after the end are made during the program, so fewer remain after it) | A-15 |
| C-12 | households.adopting | reclassification (systems designed to fit the residential rooftop definition) | increase | short; medium | invisible | B | CR-4 (x: a ground-mounted or commercial form, which K1 excludes; y: a residential rooftop form, which K1 pays for; y made better, so owners for whom the two were close switch) | A-N1 |
| C-13 | installers.certified | compliance_cost | increase | short | invisible | A | CR-1 (op 3: K3 attaches a course, a $500 fee and a staff requirement to claiming; K4 attaches inspections and records); CR-2 (installers who would have sold to inframarginal adopters anyway certify to offer the payment); CR-8c (resources spent on complying are used up) | none |
| C-14 | installers.uncertified | quantity_supplied (residential rooftop systems) | decrease | short; medium | invisible | B | CR-1 (op 1: they cannot offer the subsidized price); CR-4 applied to their customers (x: buy from an uncertified installer, y: buy from a certified one; y made better by the payment, so customers switch; CR-4a: none switch the other way) | A-N2 |
| C-15 | installers.prospective | entry_rate | increase | medium | invisible | B | CR-4 (x: stay out, y: enter; y made better by the higher price received, C-2); CR-7a (means move toward the higher yield until it is brought back into line, net of the cost of certifying) | A-5, A-2 |
| C-16 | installers.certified | asset_value (installer businesses) | increase | short (from announcement) | invisible | B | CR-10c (the value of a durable means reflects expected yields); CR-7c (the expected rise in yield, C-2, is captured by whoever owns the business when it becomes expected, from 1 September of Year 0); the rise is limited while entry is slow (A-18, A-4) | A-18, A-4 |
| C-17 | installers.certified, hardware_suppliers | lobbying_effort (to extend or enlarge the program) | increase | medium; long | invisible | B | CR-4 (x: accept the program's end, y: lobby to extend it; their specific investments, A-17, make the end costly to them, so y gains); CR-10a (the dated end alters choices before it); CR-8c (resources spent lobbying are used up) | A-9, A-17 |
| C-18 | large_electricity_users | lobbying_effort (against the surcharge) | increase | short; medium | invisible | B | CR-4 (x: accept the surcharge, y: lobby against it; K2 makes x worse for large users, so lobbying gains); CR-8c (resources spent lobbying are used up) | A-9, A-3 |
| C-19 | electricity_customers | quantity_demanded (grid electricity) | decrease | short; medium | invisible | B | CR-4c (the last kWh, valued least, is the first given up when each kWh costs more; LW-3); A-3: the change is small, but its direction is not in doubt | A-3 |
| C-20 | officials.energy_office | enforcement_cost | increase | short; medium | invisible | A | CR-1 (op 4: 5% of the Solar Fund goes to administration); CR-8c (resources spent on administering and enforcing are used up) | none |
| C-21 | utilities | compliance_cost (collecting the surcharge, connection records) | increase | short | invisible | A | CR-1 (op 3: utilities must collect K2 and supply connection records to K4); CR-8c (resources spent on complying are used up) | none |
| C-22 | workers.electricians_roofers | wage_rate | increase | short; medium | invisible | B | CR-9 (installers' higher output raises their demand for the labor that produces it; relation: electricians' and roofers' labor input_to installations); LW-10 (the value of a means follows the value of what it produces); CR-7a (wages for the same labor in other uses are pulled up with it, since it is scarce and fully used, A-12) | A-12, A-2 |
| C-23 | buyers.electrical_roofing_work | price_paid (electrical and roofing work outside rooftop solar) | increase | short; medium | invisible | B | CR-9 (those who compete for the same means face a changed situation; relation: same labor input_to other electrical and roofing work); CR-7a (the wage rise, C-22, spreads to every use of the movable labor) | A-12, A-2 |
| C-24 | buyers.electrical_roofing_work | quantity_traded (electrical and roofing work outside rooftop solar) | decrease | short; medium | invisible | B | CR-4c (at a higher price the last unit, valued least, is given up; LW-3); CR-8a (labor directed to subsidized installations is withdrawn from the uses its owners would otherwise have served). Depth 4 from K1: chain stops here | A-12, A-2 |
| C-25 | buyers.commercial_solar | price_paid (commercial and ground-mounted installation) | increase | short | invisible | B | CR-9 (relation: commercial and ground-mounted systems are same_market_other_segment, sharing installer capacity); CR-7a (installer capacity moves from the exempt segment to the subsidized one until yields are equal, so the exempt segment pays more for it while capacity is fixed, A-4) | A-4, A-2 |
| C-26 | buyers.commercial_solar | quantity_traded (commercial and ground-mounted systems) | decrease | short | invisible | B | CR-4c (at a higher price the last unit is given up); CR-8a (capacity directed to the subsidized segment is withdrawn from the exempt one) | A-4, A-2 |
| C-27 | hardware_suppliers | quantity_traded (imported panels and inverters) | increase | short; medium | invisible | B | CR-9 and LW-10 (demand for the inputs follows demand for the installations; relation: panels and inverters input_to installations); the world price is set elsewhere (A-11 has p 0.05, so no price effect is reported) | A-2 |
| C-28 | households.adopting | quantity_substitute (grid electricity bought) | decrease | medium; long | invisible | B | CR-4 (x: buy grid power, y: use own output, which costs nothing at the margin once installed); relation: rooftop output substitute for grid electricity; CR-10b (the panels are a durable stock, so the effect lasts after the program ends) | A-10, A-2 |
| C-29 | utilities | quantity_traded (grid electricity) | decrease | medium; long | invisible | B | CR-9 (relation: rooftop output substitute for grid electricity; adopters buy less, C-28); CR-10b (durable panels keep the effect after the program) | A-10, A-2 |
| C-30 | electricity_customers.non_adopting | price_paid (electricity) | ambiguous | medium; long | invisible | B | CR-12b: (+) CR-1 (K2 surcharge, medium only); (+) CR-9 (relation: substitute; utility sales fall, C-29) then arithmetic: the Commission recovers fixed grid costs that do not fall with sales over fewer kWh, and exports credited at the full retail rate reduce the kWh billed (A-13); (-) CR-9 (relation: substitute) and CR-6: rooftop output lowers midday wholesale prices and the fall reaches retail rates (A-14). No premise says which dominates | A-3, A-10, A-13, A-14 |
| C-31 | generators.wholesale | net_price_received (midday wholesale power) | decrease | medium; long | invisible | B | CR-9 (relation: rooftop output substitute for wholesale purchases at midday); CR-6 (with less demand at each price, the price moves to a lower clearing level; A-14: not offset by withdrawal of other supply) | A-14, A-10 |
| C-32 | workers.installers | employment (residential solar installation) | increase | medium | visible | B | CR-9 and LW-10 (relation: installation labor input_to installations; more installations, C-7, raise demand for it); CR-7a (labor moves in from other uses as entry adds capacity, A-5) | A-2, A-5 |
| C-33 | workers.installers | employment (residential solar installation) | decrease | long (after the program ends) | invisible | B | CR-10a (purchases pulled forward leave fewer after the end, C-11); CR-9 and LW-10 (demand for installation labor follows installations) | A-15 |
| C-34 | installers.certified | net_price_received (per watt) | decrease | long (after the program ends) | invisible | B | CR-10b (capacity built for the program, A-17, changes only through flows and persists after the cause is removed); CR-10a (demand after the end is lower, C-11); CR-6 (more capacity and fewer buyers move the price to a lower clearing level) | A-15, A-17 |
| C-35 | installers.certified | asset_value (installer businesses) | decrease | long (as the end approaches and after) | invisible | B | CR-10c and CR-7c (the value of the business reflects expected yields: as the end approaches, the expected fall, C-34, is borne by whoever owns it then); CR-10b (specific investments lose value but persist, A-17) | A-15, A-17 |
| C-36 | electricity_customers | resources_available_other_uses | decrease | short; medium | invisible | A | CR-8b (the surcharge adds to the fund exactly what it takes from customers); CR-8a and CR-3c (money paid in is not available for anything else customers would have bought) | none |
| C-37 | households.adopting.inframarginal | resources_available_other_uses | increase | short; medium | invisible | B | CR-8b (the payment adds to the recipient what it takes from customers: CR-8's symmetry requires both sides, C-36); CR-7b (the part not kept by installers, A-1) | A-1 |
| C-38 | households.adopting.marginal | resources_available_other_uses | decrease | short | invisible | B | CR-3c and CR-8a (the owner's share of the installed cost is withdrawn from the other uses they would have chosen) | A-2 |
| C-39 | households.adopting.marginal | resources_available_other_uses | increase | long | invisible | B | CR-2 (they installed because they expected the system to serve them better than grid power alone); CR-4 (x: grid power, y: own output) with net metering crediting exports at the retail rate; CR-10b (the panels keep producing) | A-2, A-10 |

## Gaps found

**(a) Calculus gaps.** None. Every step was derived from CR-1 to CR-12, LW-3 and LW-10, and arithmetic. The utility rate reset (C-30) is an existing rule applied mechanically (fixed costs divided by fewer kWh), so it needed arithmetic rather than a new rule.

**(b) New premises.**
- A-N1 (p 0.55): needed for C-12. CR-4 gives the direction a priori (no one moves from the covered form to the exempt form because of K1), but that some owners actually have both forms open is empirical, and no case assumption states it.
- A-N2 (p 0.6): needed for C-14. CR-1 op 1 applies only to installers who do not certify; the case assumptions say entry is easy (A-5) but say nothing about whether all current installers can meet K3.

**(c) Unclear core rules.**
- CR-7b: "the means that cannot move" is relative and depends on the horizon. Both installers and households are partly mobile; deciding who keeps the payment in year 1 needed the comparative premise A-18, and no sign could be given for the split after year 1. The rule does not say how to state incidence when mobility changes over time.
- CR-12: it is unclear whether CR-12c's "never netted" also forbids combining a one-time outlay with a later stream for the same variable at different horizons (C-38, C-39). Treated as separate horizons, not combined.
- CR-10a with tiered payments: the bunching before each step-down raises installations in both windows relative to the counterfactual, so the per-window signs required by the normal form do not show it. The rule licenses the shift, but the representation records it only as C-10 and a note.

## Comparison with the pattern-based analysis

The two versions agree on every central claim: adopters pay less and more systems are installed; installers keep the larger share of the payment in year 1 (both rest on A-4 and A-18, by DM-1 in one version and CR-7b in the other); the surcharge raises customers' power price and takes means from them; electricians' wages and other trades' prices rise; utilities sell less; and the non-adopters' grid price is ambiguous for the same two opposing reasons. Most of the difference is breadth. The core version records many consequences the pattern version left out: commercial and ground-mounted buyers who are crowded out, installers' compliance cost and business values, the utilities' collection cost, the payment received by inframarginal adopters (CR-8 symmetry), wholesale generators, and installer employment. Two of these rest on new premises (A-N1, A-N2). The pattern version has three claims the core version lacks. One is a core omission: non-adopters bear a larger share of the surcharge, which follows from C-28 and arithmetic. One is a representation choice: bunching before step-downs. One is a pattern overreach: other customers' wait time for electricians (C-20), where SB-3 licenses only a quantity fall, and the pattern version's own C-14 has the price rising. The only sign difference is how installer entrants' earnings are combined over time. The pattern version calls them ambiguous by DM-3; the core version signs each horizon separately.

**Counts:** M 15, V 4, S 1, OP 16, OC 3. Causes over S, OP and OC: P 1, K 0, A 2, E 12, J 5.

### Pattern version → core version

| Pattern ID | Matched core ID(s) | Class | Cause | Note |
| --- | --- | --- | --- | --- |
| C-1 | C-1 | M | | |
| C-2 | C-7, C-6 | M | | Core splits demand (C-6) and trades (C-7). |
| C-3 | C-4 | M | | |
| C-4 | C-36 | M | | |
| C-5 | C-2 | M | | Core extends the increase to the medium horizon via higher wage costs (CR-9). The pattern version gives no medium sign. Not a conflict. |
| C-6 | C-15 | M | | |
| C-7 | C-8 | V | | Oversizing is a quantity response (CR-4c, `transaction_size`), not a reshaping of form. The pattern version files it under `reclassification` via SB-5/RS-5. Same claim, better variable in core. |
| C-8 | none (path note in core section 8; implied by C-7) | OC | J | Against the no-policy counterfactual, both windows have more installations, so the per-window sign adds nothing beyond C-7. Core gap (c) records this as a representation limit of the normal form. |
| C-9 | C-10 | M | | |
| C-10 | C-9 | M | | |
| C-11 | C-17, C-18 | V | | Split by side: installers and suppliers vs large users. |
| C-12 | none | OC | E (core) | Adopters buy less grid power (core C-28), and K2 is charged per kWh, so non-adopters bear a larger share by arithmetic (CR-1 op 4, CR-4). The core version had every step and did not record it. |
| C-13 | C-22 | M | | |
| C-14 | C-23 | M | | |
| C-15 | C-27 | M | | |
| C-16 | C-29, C-28 | M | | Core also records the adopters' side (C-28). |
| C-17 | C-30 | V | | Both ambiguous with the same opposing chains. The pattern version excludes the surcharge from the variable; the core version includes it in the medium horizon. |
| C-18 | C-11, C-33 | M | | Core records the dip on the buyer side and in installer employment. |
| C-19 | C-20 | M | | |
| C-20 | none (core C-24 records quantity, not wait time) | OC | P | SB-3 concludes that output elsewhere falls; it says nothing about queues. Under CR-6, waiting replaces price only where price cannot move, and the pattern version's own C-14 has the price of that work rising. A short-run backlog is plausible but needs a sticky-price premise that the pattern version does not state. |
| C-21 | C-36 | V | | Same opportunity cost as C-4, restated as forgone purchases. The pattern version counts it twice under two variables. |
| C-22 | C-2 (short; medium, +), C-34, C-35 (long, −) | S | J | The pattern version nets a one-time investment against a later stream over one "medium–long" horizon and gets ambiguous (DM-3, CR-12b). The core version keeps the horizons apart: increase while the program runs, decrease after it. Both are valid under CR-12. The core version is more informative, the pattern version more cautious. The difference comes from how wide a horizon is, not from a rule. |
| C-23 | C-3 | M | | |

### Core-only consequences

| Core ID | Class | Cause | Note |
| --- | --- | --- | --- |
| C-5 | OP | E (pattern) | Solar Fund revenue. TX-1/SB-1 would record it; trivial, Tier A. |
| C-12 | OP | A | Reshaping ground-mounted or commercial projects into the covered rooftop form. Rests on new premise A-N1 (0.55). |
| C-13 | OP | E (pattern) | Certification and claim costs. K3 is a cost on every claimant even if it is "barely" binding. The pattern version's classification noted K3 and then recorded nothing (TX-5/OC-3 analog). |
| C-14 | OP | A | Uncertified installers lose sales. Rests on new premise A-N2 (0.6). |
| C-16 | OP | E (pattern) | Installer business values rise from the announcement (CR-7c, CR-10c). SB-4 as worded requires a "lasting" policy, which is probably why the pattern version skipped it. A five-year expected yield still capitalizes. |
| C-19 | OP | J | Customers buy slightly less power because of the surcharge. The pattern version folded this into C-16 on purpose (section 9). |
| C-21 | OP | E (pattern) | Utilities' collection and records cost (TX-5). Tier A. |
| C-24 | OP | E (pattern) | Less other electrical and roofing work. This is SB-3's own conclusion, which the pattern version replaced with wait time (C-20). |
| C-25 | OP | E (pattern) | Commercial and ground-mounted buyers pay more in year 1. They compete for the same fixed installer capacity (CR-9 same_market_other_segment; SB-3 would also apply). |
| C-26 | OP | E (pattern) | As C-25, for quantity. |
| C-31 | OP | E (pattern) | Midday wholesale price falls. The pattern version uses RS-13 only as a chain inside C-17 and does not record RS-13's own conclusion. |
| C-32 | OP | E (pattern) | Installation employment rises (CR-9, LW-10). |
| C-33 | OP | E (pattern) | Installation employment falls after the program ends. Follows from the pattern version's own C-18. |
| C-37 | OP | E (pattern) | Inframarginal adopters receive a transfer. CR-8's symmetry clause requires counting the receipt. No pattern in the SB family records the recipient's side. |
| C-38 | OP | J | Marginal adopters' own outlay. The pattern version deliberately leaves out voluntary spending (LW-5). As a signed change in `resources_available_other_uses` it is valid. |
| C-39 | OP | J | Later bill savings for marginal adopters. Valid, but it is the expected return on a voluntary purchase; the pattern version's choice to omit it is also defensible. |

### Findings

- **Pattern misapplied (P):** C-20 draws `wait_time` from SB-3, which yields only a quantity fall elsewhere. It sits next to the pattern version's own price rise (C-14), which makes a queue unlikely under CR-6.
- **Pattern catalog, too narrow:** SB-4 is stated for a "lasting" policy. CR-7c and CR-10c capitalize any expected change in yield, including one expected for five years, so a temporary subsidy still moves installer business values (core C-16, C-35).
- **Pattern catalog, asymmetry:** SB-1 names the payers of a subsidy, but no SB pattern records the recipient's receipt. CR-8's symmetry clause requires both. The pattern version therefore records the surcharge's cost (C-4) but not inframarginal adopters' gain (core C-37).
- **Pattern version, variable choice:** C-7 records oversizing as `reclassification`. It is a CR-4c quantity response; `transaction_size` (core C-8) is the right variable.
- **Error in the core version (E):** it omitted the higher share of the surcharge borne by non-adopters (pattern C-12), although every step was present.
- **Limit of the core rules / normal form:** bunching before tiered step-downs cannot be shown as per-window signs against a no-policy counterfactual (core gap (c)). The same limit applies to the pattern version's C-8, which states a true sign that adds nothing beyond C-2. Neither version can tell bunching apart from a level shift; this is a limit of the representation, not of the calculus.
- **Agreement on incidence:** DM-1 and CR-7b give the same year-1 split (installers keep the larger share) from the same comparative premise (A-18). Neither can sign the split after year 1.
