# WE-021 Per-watt subsidy for rooftop solar, funded by an electricity surcharge

Analyst: draft (Handbook 0.3)  |  Rule catalog version: 0.3  |  Status: awaiting expert review

A stylized policy in a fictional state. Many places have subsidized rooftop solar; this program is not modeled on any one of them. The probabilities are illustrative; the evidence column says what a real analysis would cite. **Environmental effects (emissions, air quality, climate) are out of scope for version 1 and are not analyzed here.** The analysis covers only the market consequences of the subsidy and its funding.

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

| Component | Rothbard type | Binding? | Rule families |
|---|---|---|---|
| K1 | Binary: a transfer from the Solar Fund to installers and their customers | Yes, for households at the margin of installing (A-2) | SB, RS, TS |
| K2 | Binary: a forced payment by all electricity customers | Yes | TX, OC |
| K3 | Triangular in form (only certified installers can offer the subsidy), but the requirement is light | Barely; most installers already employ an electrician (A-5) | SB-5 |
| K4 | Binary: funded from the surcharge | Yes | OC-3 |

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `buyers.adopters` | Building owners who install rooftop solar | System up to about 18% cheaper, with the subsidy falling at each step. |
| `installers` (`sellers.current`, `sellers.prospective`) | Firms that sell and install systems | More customers; the subsidy flows through their invoices. |
| `electricians` (`factor_owners.specific`) | Licensed electricians and roofers | More demand for their labor. |
| `panel_suppliers` (`input_suppliers`) | Importers and distributors of panels and inverters | More orders; world prices set elsewhere. |
| `customers.electricity` | Everyone who buys power from the utilities | Pay the surcharge. |
| `customers.non_adopters` | Customers who do not install, including renters, apartment dwellers and businesses | Pay the surcharge on all their power, receive no subsidy. |
| `utilities` (`sellers.substitutes`) | Sellers of grid electricity | Sell less power to adopters. |
| `buyers.other_electrical_work` (`buyers.substitutes` for electricians' time) | People who need other electrical or roofing work | Compete with solar installers for the same workers. |
| `officials.enforcement` | State Energy Office | New administrative task, paid from the fund. |

## 4. Direct effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | `buyers.adopters` | `price_paid` (installed system, net of subsidy) | decrease | short to medium | SB-2 | A-1 |
| C-2 | `installers` | `quantity_traded` (rooftop installations) | increase | short to medium | SB-2 | A-1, A-2 |
| C-3 | `customers.electricity` | `price_paid` (electricity, including surcharge) | increase | short | TX-2, DM-1 | A-3 |
| C-4 | `customers.electricity` | `resources_available_other_uses` | decrease | short to medium | SB-1, TX-1, OC-1 | A-3 |

Both sides of the budget are visible on paper: the subsidy on the installer's invoice (C-1, C-2) and the surcharge on every bill (C-3). C-4 records what customers would have bought with the surcharge. By DM-1, customers bear nearly all of the surcharge: their demand for electricity changes little with price, and the Commission lets utilities pass it through in full (A-3).

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-5 | `installers` | `net_price_received` (per watt installed) | increase | short | SB-2, DM-1 | A-4, A-18 |
| C-23 | `installers` | `subsidy_share_received` (share of the subsidy kept by installers) | increase | short | SB-2, DM-1 | A-4, A-18 |
| C-6 | `installers` | `entry_rate` | increase | short to medium | SB-3, LW-4 | A-5 |
| C-7 | `installers`, `buyers.adopters` | `reclassification` (systems sized to the 10 kW limit; more panel capacity per inverter than the home needs) | increase | short to medium | SB-5, RS-5 | A-6 |
| C-8 | `buyers.adopters` | `quantity_traded` (contracts signed in the weeks before each step-down) | increase | short to medium | RS-8 | A-7 |
| C-9 | `buyers.adopters` | `wait_time` (installer backlogs around each step-down) | increase | short to medium | RS-8 | A-7 |
| C-10 | `buyers.adopters` | `quantity_traded` (contracts between 1 September and 31 December of Year 0) | decrease | short | RS-8 | A-8 |
| C-11 | `installers`, `panel_suppliers`; large electricity users | `lobbying_effort` (installers to extend or raise the subsidy; large users to cut the surcharge) | increase | medium | RS-7, SB-5 | A-9 |
| C-12 | `customers.non_adopters` | `tax_share_borne` (relative to adopters) | increase | short to medium | RS-1, TX-4 | A-10 |

C-5: SB-2 says only that buyers pay less and/or sellers receive more. Panels are bought on a world market in which Calvera is tiny (A-11), so panel prices do not absorb the subsidy. Installer labor, by contrast, cannot grow quickly, because electricians take years to license (A-4). DM-1, which in catalog 0.3 covers subsidies, decides the split: in the first year installers have clearly fewer alternatives than households, which can wait or keep buying grid power (A-18). So installers receive the larger part of the subsidy at first (C-23, recorded with `subsidy_share_received`), and their net price per watt rises (C-5). They do not receive all of it (A-1), so C-1 still holds. By DM-1's time note, the share shifts toward buyers as new installers certify and electricians are trained (C-6, section 8).

C-12: adopters buy less grid power, so they pay less surcharge, while every non-adopter, including renters who have no roof of their own, pays it on all their power.

Not reported:
- A rise in panel and inverter prices. This would need Calvera to be a large buyer in the world market; A-11 is far below the cut-off (p = 0.05).
- Fraudulent claims for systems that were never installed. Claims are checked against utility connection records; A-16 is below the cut-off (p = 0.2).
- Relocation (RS-4): rooftops cannot move, and the subsidy is paid only for Calvera buildings. No chain to follow.
- SB-7 (earmark fungibility): the Solar Fund pays for something the state budget did not fund before. Not applicable.

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-13 | `electricians` | `wage_rate` | increase | short to medium | SB-3 | electricians' labor: `input_to` installations and other electrical work | A-12 |
| C-14 | `buyers.other_electrical_work` | `price_paid` (other electrical and roofing work) | increase | short to medium | SB-3 | as C-13 | A-12 |
| C-15 | `panel_suppliers` | `quantity_traded` (panels and inverters sold in Calvera) | increase | short to medium | SB-2 | panels: `input_to` installations, close | A-2 |
| C-16 | `utilities` | `quantity_traded` (grid electricity) | decrease | medium | SB-3, TX-2 | rooftop power and grid power: `substitute`, close | A-2, A-10 |
| C-17 | `customers.non_adopters` | `price_paid` (grid electricity, before surcharge) | see section 7 | medium to long | PC-15 vs RS-13 | as C-16; rooftop exports and wholesale power: `same_market_other_segment`, partial | A-13, A-14 |
| C-18 | `installers` | `quantity_traded` (installations after the program ends) | decrease | medium to long | SB-6 | — | A-15 |

C-17 is at depth 3 (subsidy → adoption → less grid power sold → regulated rates reset) and reaches every non-adopting customer, so the chain stops there. The further effects of higher or lower power prices on businesses that use electricity are diffuse and are not traced.

Second-order checks:
- **RS-9 (bundled trips).** No buyer changes where they buy the target good. Not applicable.
- **RS-10 (informal trade).** No trade is driven out of the legal market: the subsidy pulls installation into it, since only certified, connected systems qualify. Not applicable.
- **RS-11 (lock-in).** The subsidy is not repaid on moving and does not tie anyone to a place. Not applicable.

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| Split of the subsidy between `buyers.adopters` and `installers`, short | — | — | DM-1 (A-4, A-18) | **Installers receive the larger part in the first year** (C-23); buyers still receive some of it (C-1, A-1). The share shifts toward buyers as new installers enter (C-6). |
| `customers.non_adopters`, `price_paid` (grid electricity, before surcharge), medium to long | Utilities sell fewer kWh (C-16) but their grid costs are largely fixed; at the next rate case the Commission spreads those costs over fewer kWh, and net metering credits adopters' exports at the full retail rate (PC-15, A-13). | Rooftop output, including exports, adds supply to the midday wholesale market and lowers its price, which the utilities pass through (RS-13, A-14). | None | **ambiguous** (C-17, Tier B). Decided by how much of the retail rate is fixed grid cost recovered per kWh, against how much rooftop output lowers wholesale prices. |
| `customers.non_adopters`, total cost of electricity (`price_paid` including surcharge), medium | Surcharge (C-3); rate reset (PC-15). | Wholesale price effect (RS-13). | None | **ambiguous** (Tier B) once both C-17 chains act; **increase** while only the surcharge applies (C-3). |
| `installers` that entered because of the program, `earnings`, medium to long | Higher margins and volumes while the subsidy lasts (C-2, C-5). | Certification, vans, training and staff taken on for the program lose value when it ends and installations dip (C-18). | DM-3 | **ambiguous by design** (DM-3). Entrants who invested expected the program to pay; firms that stayed out did not. |

## 8. Time structure

- **Announcement.** The subsidy was expected four months before it began. Households who would have installed in late Year 0 wait for January (C-10), and installers see a slow autumn followed by a January surge.
- **Step-downs.** Each step is triggered by funded capacity, published weekly, not by a date. As a threshold approaches, households race to sign (C-8) and backlogs build (C-9); just after it, demand falls back. The steps therefore produce three surges and dips over the life of the program, not one.
- **Who gets the subsidy changes over time.** In the first year, installation labor is the bottleneck and installers keep part of the subsidy (C-5). As new installers certify (C-6) and electricians are trained, more of it passes to buyers (A-4 weakens). Electricians' wages (C-13) follow the same path: up at first, easing as supply of labor grows.
- **Program end.** The program is temporary, so SB-6 applies: some households who would have installed in Year 6 to Year 8 install earlier, and installations after the program are lower than they would have been (C-18). Installers who expanded for the program shrink or exit then (section 7, DM-3).
- **Rates.** The Commission resets rates every two to three years, so the rate effect in C-17 appears with a lag and grows as adoption accumulates. Adopters' systems last 20 to 25 years, so lower grid sales to them persist long after the subsidy has ended.
- **Counterfactual trend.** World panel prices have been falling for years, and adoption was already rising. Every sign here is relative to that trend, not to the pre-policy level.

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-19 | `officials.enforcement` | `enforcement_cost` | increase | Claim checks and inspections, paid from 5% of the fund (and so by surcharge payers, C-4). | OC-3 |
| C-20 | `buyers.other_electrical_work` | `wait_time` (for electricians and roofers) | increase | Time other customers wait for repairs, renovations and new wiring, while workers are drawn to subsidized installations. | SB-3, OC-1 |
| C-21 | `customers.electricity` (businesses) | `quantity_traded` (goods and services they would have produced or bought with the surcharge) | decrease | Spending crowded out by the surcharge in firms' budgets. Not traced further: diffuse. | OC-1, TX-1 |

The surcharge's forgone uses for all customers are recorded as C-4. The power purchases that the surcharge prices out are so few (demand changes little, A-3) that they get no separate OC-4 entry; they are part of C-16. The adopters' own spending on systems is their voluntary choice (LW-5) and is not counted as a cost to them.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | Installers do not capture the whole subsidy. | other | 0.85 | About 900 competing installers; subsidy shown on the invoice; quotes before and after the start. | C-1 fails; the whole subsidy goes to installers. |
| A-2 | Some households at the margin install because of the subsidy. | substitutability | 0.9 | The subsidy is about 18% of installed cost; surveys of intentions; payback periods. | C-2, C-15, C-16 shrink to timing shifts. |
| A-3 | The surcharge is passed through to customers in full, and their demand changes little. | other | 0.95 | Commission order; studies of electricity demand response. | C-3 weakens; part falls on utilities. |
| A-4 | Installation labor cannot grow much within the first year. | other | 0.7 | Electrician licensing time; installer job vacancies; backlog data. | C-5 and C-23 not reported; buyers get most of the subsidy. |
| A-5 | Certification is easy enough that new installers enter. | other | 0.8 | Requirements of K3; supply of licensed electricians in related trades. | C-6 weakens; C-5 persists longer. |
| A-6 | Oversizing toward the 10 kW limit is feasible and pays under net metering. | other | 0.65 | Roof sizes; inverter ratios in claim data; retail-rate export credit. | C-7 not reported. |
| A-7 | Installer capacity is limited near step-downs, so backlogs form. | other | 0.75 | Weekly capacity dashboard; installer staffing. | C-8, C-9 weaken. |
| A-8 | Households knew of the subsidy from September and could wait. | expectations | 0.8 | Publicity; installers' reports of deferred contracts. | C-10 not reported. |
| A-9 | Installers, suppliers and large users can organize to lobby. | other | 0.85 | Existing solar trade association; industrial users' group. | C-11 weakens. |
| A-10 | Adopters buy less grid power after installing. | substitutability | 0.95 | Utility billing data for existing solar customers. | C-12, C-16 fail. |
| A-11 | Calvera's purchases are large enough to raise world panel prices. | other | 0.05 | Share of world shipments. | Below cut-off; not reported. |
| A-12 | Electricians and roofers are scarce and fully used elsewhere. | other | 0.8 | Trade employment and wage data; job vacancies. | C-13, C-14, C-20 fail. |
| A-13 | The Commission recovers fixed grid costs mainly per kWh, those costs do not fall with sales, and net metering credits exports at the full retail rate. | other | 0.8 | Rate design; net metering statute; utilities' cost structure. | The + chain in C-17 fails. |
| A-14 | Rooftop output is large enough to lower midday wholesale prices (it is not offset by withdrawal of other supply), and the reduction reaches retail rates. | substitutability | 0.55 | 900 MW against a state peak of about 9 GW; wholesale market design; pass-through rules. | The − chain in C-17 fails; C-17 becomes an increase (Tier B). |
| A-15 | Some adopters would have installed later without the subsidy. | expectations | 0.8 | Adoption trend; falling panel prices. | C-18 not reported. |
| A-16 | Fraudulent claims are made on a meaningful scale. | enforcement | 0.2 | Connection-record checks; inspection rate. | Below cut-off; not reported. |
| A-17 | Entrants make investments specific to solar installation that lose value when the program ends. | durability | 0.7 | Certification, vehicles, training; experience of installers after other programs ended. | The − chain in the DM-3 row weakens. |
| A-18 | In the first year, installers have clearly fewer alternatives than households: their capacity is fixed by the number of licensed electricians (A-4), while households can wait or keep buying grid power. | substitutability | 0.65 | Backlogs and quotes after the start; electrician licensing time; share of households who defer installation. | DM-1 does not apply; the split is open; C-5 and C-23 not reported. |

## 11. Report

**The policy.** Calvera pays installers 50 cents per watt (later 35 and 20 cents) for rooftop solar systems on homes, deducted from the customer's bill, until 900 MW has been funded or five years have passed. It is paid for by a surcharge of 0.12 cents per kWh on every electricity customer's bill.

**Visible consequences.** Rooftop systems cost adopters less (C-1), and more are installed (C-2). Every electricity customer pays a little more per kWh (C-3) and has that much less to spend on other things (C-4).

**Invisible consequences.**
- *Installers* keep the larger part of the subsidy at first, while installation labor is scarce (C-5, C-23), and new firms enter (C-6). Systems are sized to collect as much subsidy as allowed (C-7). Sales surge before each step-down and dip after it, with backlogs at the peaks (C-8, C-9), and dip before the program starts (C-10) and after it ends (C-18).
- *Electricians and roofers* earn more (C-13). *People who need other electrical or roofing work* pay more and wait longer (C-14, C-20).
- *Non-adopters*, including renters and apartment dwellers who cannot install, pay a larger share of the surcharge than adopters do (C-12).
- *Utilities* sell less power (C-16). *Panel suppliers* sell more in Calvera (C-15), but world panel prices are not affected.
- Installers and suppliers lobby to extend the subsidy; large power users lobby against the surcharge (C-11).

**Ambiguous effects.** Whether grid electricity becomes more or less expensive for non-adopters over the medium term: fixed grid costs spread over fewer kWh push it up; lower midday wholesale prices push it down (C-17). Whether firms that entered for the program end up better or worse off, once its end is counted (DM-3).

**Key conditions.** How the subsidy splits between buyers and installers depends on how fast installation labor can grow (A-4, p = 0.7; A-18, p = 0.65). The effect on other customers' electricity rates depends on rate design and net metering (A-13, p = 0.8) and on the wholesale market (A-14, p = 0.55).

**What this analysis cannot say.** How large any effect is; whether the gains to adopters and installers outweigh the costs to surcharge payers and other customers of electricians; environmental effects (out of scope for version 1); whether the policy is desirable.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | buyers.adopters | price_paid (net of subsidy) | decrease | short–medium | visible | B | SB-2 | A-1 |
| C-2 | installers | quantity_traded (installations) | increase | short–medium | visible | B | SB-2 | A-1, A-2 |
| C-3 | customers.electricity | price_paid (incl. surcharge) | increase | short | visible | B | TX-2, DM-1 | A-3 |
| C-4 | customers.electricity | resources_available_other_uses | decrease | short–medium | invisible | B | SB-1, TX-1, OC-1 | A-3 |
| C-5 | installers | net_price_received | increase | short | invisible | B | SB-2, DM-1 | A-4, A-18 |
| C-6 | installers | entry_rate | increase | short–medium | invisible | B | SB-3, LW-4 | A-5 |
| C-7 | installers, buyers.adopters | reclassification | increase | short–medium | invisible | B | SB-5, RS-5 | A-6 |
| C-8 | buyers.adopters | quantity_traded (before step-downs) | increase | short–medium | invisible | B | RS-8 | A-7 |
| C-9 | buyers.adopters | wait_time | increase | short–medium | invisible | B | RS-8 | A-7 |
| C-10 | buyers.adopters | quantity_traded (September to December, Year 0) | decrease | short | invisible | B | RS-8 | A-8 |
| C-11 | installers, panel_suppliers, large users | lobbying_effort | increase | medium | invisible | B | RS-7, SB-5 | A-9 |
| C-12 | customers.non_adopters | tax_share_borne | increase | short–medium | invisible | B | RS-1, TX-4 | A-10 |
| C-13 | electricians | wage_rate | increase | short–medium | invisible | B | SB-3 | A-12 |
| C-14 | buyers.other_electrical_work | price_paid | increase | short–medium | invisible | B | SB-3 | A-12 |
| C-15 | panel_suppliers | quantity_traded (in Calvera) | increase | short–medium | invisible | B | SB-2 | A-2 |
| C-16 | utilities | quantity_traded (grid electricity) | decrease | medium | invisible | B | SB-3, TX-2 | A-2, A-10 |
| C-17 | customers.non_adopters | price_paid (grid electricity, before surcharge) | ambiguous | medium–long | invisible | B | C-16, PC-15 vs RS-13 | A-2, A-10, A-13, A-14 |
| C-18 | installers | quantity_traded (after program ends) | decrease | medium–long | invisible | B | SB-6 | A-15 |
| C-19 | officials.enforcement | enforcement_cost | increase | short–medium | invisible | A | OC-3 | none |
| C-20 | buyers.other_electrical_work | wait_time | increase | short–medium | invisible | B | SB-3, OC-1 | A-12 |
| C-21 | customers.electricity (businesses) | quantity_traded (forgone purchases) | decrease | short–medium | invisible | B | OC-1, TX-1 | A-3 |
| C-22 | installers (entrants) | earnings | ambiguous | medium–long | invisible | B | C-2, C-5 vs C-18; DM-3 | A-4, A-15, A-17, A-18 |
| C-23 | installers | subsidy_share_received | increase | short | invisible | B | SB-2, DM-1 | A-4, A-18 |

## Gaps found

- GAP-021-1 (closed in catalog 0.3: DM-1 extended to SB-2; variable `subsidy_share_received`). C-5 now Tier B, with the comparison of alternatives as A-18; the split is recorded as C-23. C-22 rises to Tier B with it.
- GAP-021-2 (closed in catalog 0.3: PC-15). The + chain of C-17 now rests on PC-15, with A-13.
- GAP-021-3 (closed in catalog 0.3: RS-13). The − chain of C-17 now rests on RS-13, with A-14. C-17 is Tier B, still ambiguous.
