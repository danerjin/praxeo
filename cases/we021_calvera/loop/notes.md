# WE-021 Calvera rooftop solar: expand loop, blind run (notes)

Inputs read: handbook/04a_core_rules.md, praxeo/core/{core.lp,situation.py,expand.py}, we001 and we013 situation records (we009 not opened), section 1 of WE-021 and its assumption table. Nothing under handbook/05_*, cases/we021_calvera/ (other than loop/) or tests/ was read. Names come from `--vocab --exclude WE-021`; the final run prints no `off-list:` lines.

## Seed (policy's own facts)
- Exchanges: e_install (homeowners buy, contractors.certified sell; price_paid / net_price_received), e_elec (customers buy, producers.utilities sell).
- K1: grant on e_install to the seller side (paid to the installer, deducted on the invoice), paid from treasury.solar_fund; announced (premise A-8, "households knew from September"); expires (the program ends at 900 MW or Year 5).
- K2: charge on e_elec, buyer pays, receiver treasury.solar_fund, tax_revenue and its static-projection shortfall.
- moves: e_install buyer (A-1 installers do not capture it all), e_install seller (A-4 labor cannot grow in year one), e_elec buyer (A-3 pass-through).
- K3 as compliance (contractors.certified); K2 collection as compliance (producers.utilities); K4 enforcer (officials.enforcement); K1 and K4 funded by customers (the surcharge feeds the fund).
- The seed run printed the first six nodes; I added the K2 compliance and K1 funded facts to the seed before round 1 (found on the first PENDING listing: the utilities collect the surcharge, the fund's payers are the surcharge payers).

## Round 1 (depth 1): 6 nodes
- contractors.certified: entry link (yield to entrants' entry_rate, A-5); input links to workers.electricians (quantity_demanded, and employment,hours_worked as a group; "licensed electrician on staff") and to input_suppliers (hardware); link to its own legal_breach (A-16); yield and asset (entrants, A-17) and incidence on seller (A-18); stake in K1 (A-9); dominance on resources_available_other_uses (subsidy kept exceeds certification cost; judged).
- customers: stake in K2 (A-9, "large users").
- homeowners: alternative of buying grid power (A-2, A-10); alternative of a smaller system, inverse unit_size (A-6); timing bring_forward (A-15; with A-8 as announced gives the announcement, deadline and after-expiry windows); crowding link to wait_time (A-7); supply link to customers' price_paid (A-14, midday wholesale price).
- officials.enforcement: paid_from link to fund_balance (K4 "funded from 5% of the Solar Fund").
- producers.utilities: supply link quantity_traded to customers' price_paid (A-13, fixed costs recovered per kWh).
- treasury.solar_fund: paid_from (subsidy_outlay) and paid_into (tax_revenue) links to fund_balance.
Questions: 13 (12 from the table: A-5, A-16, A-17, A-18, A-9, A-2, A-10, A-6, A-15, A-7, A-14, A-13; 1 judged: "The part of the subsidy that installers keep exceeds what certification costs them", 0.8, from $0.50/W on a ~7 kW system (105 MW / 15,000) and ~17 systems per installer against a one-time $500 fee and a three-day course).

## Round 2 (depth 2): 7 nodes
- entrants: link entry_rate to contractors.certified number_of_sellers (same act), and to electricians' demand (each entrant needs a licensed electrician).
- contractors.certified#2: supply link number_of_sellers to its own net_price_received (entry lowers the price), and a dominance fact (kind response, premises A-4 and A-12) so entry is a response that cannot reverse the rise (CR-12e, 0.9 and 1.0 notes).
- homeowners#2: unit_size links to input_suppliers' quantity_demanded and to the fund's subsidy_outlay (same act); no premises.
- input_suppliers: supply_price link to world panel price (A-11); stake in K1 (A-9).
- workers.electricians: supply_price to wage_rate (A-12, A-4); cost link to contractors.other_trades quantity_supplied (A-12).
- customers#2, treasury.solar_fund#2: empty (price_paid ambiguous between the surcharge and A-13 against A-14; fund_balance ambiguous between payments and receipts).
Questions: 2 (A-12, A-11, both from the table).

## Round 3 (depth 3): 3 nodes, all empty
input_suppliers#2, contractors.other_trades, workers.electricians#2: nothing further without inventing.

## Answers
Total 15 questions: 14 from the table (A-2, A-5, A-6, A-7, A-9, A-10, A-11, A-12, A-13, A-14, A-15, A-16, A-17, A-18) and 1 judged (the dominance premise above). Seed premises A-1, A-3, A-4, A-8 carry their table p (0.85, 0.95, 0.7, 0.8) and were not asked. A-1 is used for moves (buyer side), not as a separate question.

## Final engine output
DONE in 3 rounds, 15 questions. Reported: installers net price, quantity, return on capital, resources, subsidy share, lobbying up; homeowners price_paid down, installs up with announcement window down, deadline window up, after-expiry down, unit_size and wait_time up; customers price_paid ambiguous (surcharge and A-13 up, A-14 down), quantity down, resources down; utilities quantity down, compliance cost up, resources down; fund balance ambiguous, outlay up, tax revenue up, revenue below static projection; electricians' wage and employment/hours up; other trades' supply down; entrants entry and asset value up. Not reported (below cut-off): legal_breach (A-16, 0.2), world panel price (A-11, 0.05).

## What the format could not hold
- K3 as a charge: a $500 fee attached to an option that exists only under the policy (CR-3 1.1) would sign number_of_sellers down through the `operating` rule, against entry. Recorded as compliance only; the fee as a receipt of the Energy Office is not held.
- Step-downs ($0.50 / $0.35 / $0.20 by funded MW): no scheduled-decline component. The bunching before each step and the backlog (A-7) are held only through the final-expiry timing windows and a crowding link, which do not carry windows.
- The 10 kW limit: `thresholds` is a line above which a measure binds; here the subsidy stops above the line. Held as an inverse-unit_size alternative (A-6), which gives only the direction toward the limit.
- The fund cap (900 MW) and first-come funding: `capped` fixes the quantity traded, not the subsidised quantity.
- Fraud (A-16): `outside` fires only with a held, capped, banned or charged exchange, not a grant; held as a yield link into legal_breach, which is a stretch of `yield`.
- The unclear end-of-program provision (surplus balance, surcharge stops, credit back on bills): components have no dates, so a reading that applies only after expiry cannot be given; no `unclear` entry was made. A credit back to customers as `means in` would net against the surcharge with no window.
- A-17 (entrants' specific investments lose value when the program ends): the asset fact gives asset_value up during the program; the fall at expiry has no rule.
- A-13 uses relation `supply` (less sold, higher rate per kWh) as the nearest relation to cost recovery on a falling base; the chain also starts from the surcharge's own small fall in kWh.
- A-1 appears only as the premise of `moves` on the buyer side; share captured (incidence, A-18) is signed as a rank, not a size.
