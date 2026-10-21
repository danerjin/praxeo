# WE-011 / Analysis: Corvania Savings Income Tax Act (tax on interest income)

Analyst: core-only re-run (Handbook 0.4)  |  Rules: core rules CR-1 to CR-12 only  |  Status: awaiting comparison

Every derivation below cites only the core rules (CR-1 to CR-12, with clause), the foundations (AX-1, LW-1 to LW-10) and arithmetic. Assumptions A-1 to A-16 are the case assumptions as given; A-N1 and A-N2 are premises this re-run had to add.

## 1. Policy record

| Field | Value | Source sentence |
|---|---|---|
| Jurisdiction (and what lies just outside) | Corvania: own currency (the crown), open capital account, well-developed banking system. Just outside: the Federation of Quellan, with no tax on interest and no exchange of account information with Corvania; a Quellan account takes a short trip or an online application. | "The neighboring Federation of Quellan has no tax on interest and does not exchange account information with Corvania; opening a Quellan account takes a short trip or an online application." |
| Announced / enacted / effective / expires | Announced 15 March (budget speech); passed in June; applies to interest paid from 1 January of the following year; no expiry. | "The finance minister announced the tax in the budget speech on 15 March; parliament passed it in June; it applies to interest paid from 1 January of the following year." |
| Enforcement (who, penalties, resources) | Tax Agency; banks report totals withheld; audits of declared foreign income. Penalties not stated. | K4. |
| Starting conditions | Interest, dividends and capital gains on shares untaxed until now; rental income taxed under the ordinary income tax (unchanged). Deposit rates about 4%, ten-year government bonds about 5%, inflation about 3% for several years. | Policy record preamble. |

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Interest tax | `income_tax` on interest (`capital_tax` family) | Interest paid to resident individuals on bank deposits, government and corporate bonds, and distributions from money-market funds | Banks and paying agents withhold; savers bear it | 20% final withholding on nominal interest, including coupons on bonds already issued (no grandfathering). | First 1,000 crowns of interest per person per year (fixed in money terms, not indexed). Interest inside registered retirement accounts (contributions capped at 6,000 crowns a year). Interest paid to non-residents. |
| K2 Foreign interest | `income_tax` | Interest received by residents from foreign accounts and bonds | Resident savers | Same 20%, self-declared on the annual return. | Same allowance. |
| K3 Funds | Definition | Investment funds holding bonds | Fund managers | Tax is withheld on distributions only. Funds that accumulate income instead of distributing it are not mentioned. | Accumulating funds (by omission). |
| K4 Administration | Enforcement | K1 to K3 | Tax Agency | Banks report totals withheld; audits of declared foreign income. | None |

Revenue use: general budget. The minister said the revenue would "help close the pension deficit", but the act has no earmark. Spending is out of scope.

Existing rules: none recorded in the input beyond the starting conditions above (rental income taxed under the ordinary income tax, unchanged).

Unclear provisions: whether income accumulated inside a fund will later be taxed on sale of the fund units. The text taxes only distributions; analyzed as untaxed (A-3).

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | Core rules applied |
|---|---|---|---|
| K1 | Binary (the state takes part of each interest payment) | Binds on every resident saver whose interest exceeds 1,000 crowns a year; more savers cross the allowance as nominal interest grows (A-13) | CR-1, CR-3a, CR-4, CR-7, CR-8, CR-10 |
| K2 | Binary | Binds in law; in practice attaches only a risk to non-declaration, since detection is weak (A-6) | CR-1 (enforcement premise), CR-4 (x: comply, y: violate) |
| K3 | Definition (leaves an untaxed form open) | Opens an exit from K1 if accumulating funds stay untaxed (A-3) | CR-1, CR-4 (x: covered form, y: uncovered form) |
| K4 | Enforcement | Binds on banks (reporting) and the Tax Agency (audits) | CR-1 op 3, CR-8c |

**CR-1 operations by component and actor class.** Operations: (1) remove an option, (2) add an option, (3) change what an option brings, (4) transfer means.

| Actor class | K1 | K2 | K3 | K4 |
|---|---|---|---|---|
| `savers.taxable` (residents with interest above the allowance) | 3 (holding deposits and bonds now brings 20% less interest); 4 (the withheld tax is a transfer of their means to the state) | 3 (foreign interest now brings a tax if declared, or a risk of penalty if not) | none directly; the untaxed accumulating form keeps its old yield, so the taxed forms are worse relative to it (3, relative) | 3 (audit risk on foreign income) |
| `savers.below_allowance` | none now; 3 later, as nominal interest crosses the fixed allowance (A-13) | same | none | none |
| `bondholders.existing` (anyone holding crown bonds when the tax becomes expected) | 3 (coupons on bonds already issued are taxed for residents; no grandfathering) | none | none | none |
| `banks` (deposit-takers and paying agents) | 3 (withholding attached to paying interest) | none | none | 3 (reporting of totals withheld) |
| `fund_managers` | 3 (withholding on distributions of distributing funds) | none | 3, relative: the accumulating form is now the untaxed one | none |
| `retirement_account_providers` | none directly; their product is exempt, so it improves relative to taxed accounts | none | none | none |
| `lenders.non_resident` | none (exempt) | none | none | none |
| `banks.quellan` (`neighboring_jurisdictions`) | none directly | none | none | none |
| `officials.enforcement` (Tax Agency) | none | 3 (must process declarations) | none | 3 (audits; means used up, CR-8c) |
| `government.budget` | 4 (receives the revenue) | 4 | none | none |
| Borrowers, owners of untaxed assets, buyers of untaxed assets | none directly; their situations change only through CR-9 | none | none | none |

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `savers.taxable` | Resident individuals whose interest exceeds 1,000 crowns a year | Taxed interest assets bring 20% less net interest; untaxed alternatives unchanged. Split below where the split matters: |
| `savers.taxable_diversified` | Taxable savers who hold or can easily hold shares, property, accumulating funds, retirement accounts or a Quellan account (A-2, A-5) | Can move to untaxed forms (CR-4) |
| `savers.taxable_undiversified` | Taxable savers who hold mainly deposits and lack practical untaxed alternatives (A-N1) | Bear the tax with little room to move (CR-4b, CR-7b) |
| `savers.below_allowance` | Residents whose interest is under 1,000 crowns | Untaxed now; face higher gross rates (CR-9) and, over time, fiscal drag (A-13) |
| `bondholders.existing` | Holders of crown bonds when the tax becomes expected | Bond prices reprice at announcement (CR-7c) |
| `banks` | Take deposits, lend, withhold and report | Compliance burden; lose deposits; must pay more for funds |
| `fund_managers` | Run distributing and accumulating bond funds | Can reshape distributing funds into accumulating ones (A-3) |
| `retirement_account_providers` | Run registered retirement accounts | Their exempt product gains relative to taxed ones |
| `lenders.non_resident` | Foreign holders of crown deposits and bonds | Exempt; face higher gross crown yields if residents withdraw (A-8, A-9) |
| `banks.quellan` | Banks across the border | Receive deposits moved out of Corvania (A-5, A-6) |
| `borrowers.bank_dependent` | Small firms and households that rely on bank credit (A-10) | Banks' cost of funds rises (CR-9) |
| `borrowers.government` | The Treasury as issuer of new bonds | Yields on new issues may rise (A-8, A-9) |
| `firms.investing` | Firms whose investment depends on debt finance (A-11) | Dearer credit |
| `owners.untaxed_assets` | Owners of shares and property | Demand for their assets rises (CR-9, substitute) |
| `buyers.untaxed_assets` | Prospective buyers of shares and property | Pay more for them |
| `lobby.savings` | Banks, retirement-account providers and retiree groups (A-7) | New concentrated stake in exemptions and allowance |
| `officials.enforcement` | Tax Agency | Audits and declarations to process |
| `government.budget` | General budget | Receives revenue; no earmark (CR-8d) |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | savers.taxable | net_price_received (after-tax interest on deposits and bonds) | decrease | short | CR-1 op 3 and op 4; CR-7b (borrowers can turn to untaxed non-resident lenders, savers have fewer alternatives, so savers bear at least part); arithmetic | A-1 |
| C-2 | government.budget | tax_revenue | increase | short | CR-1 op 4; CR-8b | none |
| C-3 | banks | compliance_cost | increase | short | CR-1 op 3 (withholding and reporting attached to paying interest); CR-8c | none |

Arithmetic on C-1: a 4% deposit rate taxed at 20% pays 3.2%. With inflation at 3%, the real return before tax is about 1% and after tax about 0.2%, so the tax takes about 80% of the real return, because it is levied on nominal interest. The same arithmetic on a 5% bond: real 2% before tax, 1% after.

## 5. Responses

CR-4 applied to every pair of options each class has.

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-4 | savers.taxable_diversified | quantity_demanded (taxed deposits, bonds and distributing funds held) | decrease | short | CR-4b (x: taxed interest asset, y: untaxed asset); CR-7a | A-2 |
| C-5 | savers.taxable_diversified | quantity_substitute (shares, property, accumulating funds, retirement accounts held) | increase | medium | CR-4b (x: taxed interest asset, y: untaxed asset); CR-7a | A-2 |
| C-6 | retirement_account_providers | quantity_traded (contributions to registered retirement accounts) | increase | short | CR-4b (x: taxed account, y: exempt retirement account, up to the 6,000-crown cap) | A-2 |
| C-7 | fund_managers | reclassification (distributing funds reshaped or replaced by accumulating funds) | increase | short | CR-4b (x: covered form, y: uncovered form); CR-7a | A-3 |
| C-8 | savers.taxable_diversified | cross_border_purchases (deposits and bonds held in Quellan) | increase | short | CR-4b (x: here, y: there), which pays only together with CR-4b (x: comply, y: violate), since declared foreign interest bears the same 20% (K2) | A-5, A-6 |
| C-9 | savers.taxable_diversified | informal_activity (undeclared foreign interest) | increase | short | CR-4b (x: comply, y: violate); CR-1 premise (weak enforcement turns K2 into a risk, op 3) | A-5, A-6 |
| C-10 | lobby.savings | lobbying_effort (for a higher or indexed allowance, wider exemptions) | increase | short | CR-4b (x: accept, y: lobby) | A-7 |
| C-11 | savers.taxable | saving | ambiguous | medium | Chain (−): CR-4b and CR-4c (x: save, y: consume now; saving now brings less). Chain (+): CR-4 exception (savers toward a fixed future sum must save more to reach it at a lower net return). CR-12b: no premise says which dominates | A-1, A-15 |
| C-12 | savers.taxable_undiversified | tax_share_borne | increase | medium | CR-7b (the burden settles on those without alternatives; diversified savers escape through C-4 to C-9) | A-2, A-N1 |
| C-13 | government.budget | tax_revenue_vs_static_projection | decrease | short | CR-4b (substitution C-4, reclassification C-7, relocation C-8); CR-10a (accrued interest credited before 1 January where A-4 holds) | A-2 |
| C-14 | government.budget | tax_revenue_vs_static_projection | decrease | medium | CR-4b, CR-7a (base shrinks as diversified savers move) | A-2 |

## 6. Second-order effects

Depth counted in links from the policy. Market relations: `deposits_and_bonds_taxed` and `untaxed_assets` (shares, property, accumulating funds, retirement accounts): `substitute`, partial to close for diversified savers. `deposits` and `bank_loans`: `input_to` (deposits fund loans), close. `bank_loans` and `business_investment`: `input_to`, partial. `crown_deposits` and `quellan_deposits`: `across_border`, close for those who can open an account (A-5). `resident_holdings_of_crown_bonds` and `non_resident_holdings`: `same_market_other_segment`, partial (A-8, A-9).

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-15 | bondholders.existing | asset_value (crown bonds already issued) | decrease | short | CR-7c and CR-10c (the lower expected net yield to the marginal resident buyer is capitalized when the tax becomes expected, 15 March, and borne by whoever then owns the bond, resident or not); CR-10a | same_market_other_segment (resident and non-resident holders); depth 2 | A-8, A-16 |
| C-16 | banks | quantity_traded (deposits taken from residents) | decrease | medium | CR-9 (savers are banks' suppliers of funds); CR-4b via C-4 and C-8 | input_to; depth 2 | A-2 |
| C-17 | banks | price_paid (gross interest rate offered on deposits) | increase | medium | CR-9; CR-6 (planned supply of funds at the old rate falls short of planned borrowing, so the rate moves toward the new clearing level); CR-7a | input_to; depth 2 | A-1, A-9 |
| C-18 | savers.below_allowance | net_price_received (interest on deposits) | increase | medium | CR-9 (same deposit market as taxed savers); CR-7a (a higher gross rate reaches them untaxed); premise that banks do not price by tax status | same_market_other_segment; depth 3 | A-9, A-N2 |
| C-19 | savers.below_allowance | net_price_received (interest on deposits) | ambiguous | long | Chain (+): C-18. Chain (−): the 1,000-crown allowance is fixed in money terms while nominal interest grows, so more of these savers' interest becomes taxed (CR-10, arithmetic). CR-12b | same_market_other_segment; depth 3 | A-9, A-13, A-N2 |
| C-20 | borrowers.bank_dependent | price_paid (interest rate on bank loans) | increase | medium | CR-9 (deposits are an input to lending; LW-10); CR-7a (banks bring lending margins back into line after their cost of funds rises) | input_to; depth 3 | A-9, A-10 |
| C-21 | borrowers.bank_dependent | quantity_traded (bank loans) | decrease | medium | CR-4c (the last unit of borrowing, valued least, is given up first); CR-5a (loans that would have been made are not) | input_to; depth 3 | A-9, A-10 |
| C-22 | firms.investing | capital_stock_economy | decrease | long | CR-4b (x: invest with debt, y: not invest), CR-10b (the stock changes only through reduced investment flows) | input_to; depth 4 | A-9, A-10, A-11 |
| C-23 | borrowers.government | price_paid (yield on new bond issues) | increase | medium | CR-9; CR-7a (the government must offer a yield that the marginal buyer, partly resident, accepts) | same_market_other_segment; depth 2 | A-8, A-9 |
| C-24 | lenders.non_resident | net_price_received (yield on crown deposits and bonds) | increase | medium | CR-7a (exempt lenders earn the higher gross rate untaxed); CR-9 | same_market_other_segment; depth 3 | A-8, A-9 |
| C-25 | lenders.non_resident | quantity_supplied (funds lent in crowns) | increase | medium | CR-4b (x: other markets, y: crown bonds and deposits at the higher yield); CR-7a | same_market_other_segment; depth 3 | A-8, A-9 |
| C-26 | owners.untaxed_assets | asset_value (shares and property) | increase | short | CR-9 (substitute); CR-7c (higher demand for assets in slowly growing supply is capitalized into their price); CR-10a (at announcement) | substitute; depth 2 | A-2, A-12 |
| C-27 | buyers.untaxed_assets | price_paid (shares and property) | increase | medium | CR-9 (substitute); CR-6 (prices move toward the level at which planned purchases and sales are compatible) | substitute; depth 3 | A-2, A-12 |
| C-28 | banks.quellan | quantity_traded (deposits from Corvanian residents) | increase | short | CR-9 (across_border) via C-8 | across_border; depth 2 | A-5, A-6 |

Interaction of components. K3 opens an exit from K1 (accumulating funds, A-3). K2 is meant to close the Quellan exit from K1, but with weak detection (A-6) it attaches only a risk, so the exit stays open (C-8, C-9). K1's exemption for non-residents gives exempt foreign lenders the higher gross yield (C-24). K1's retirement exemption opens an exit capped at 6,000 crowns a year (C-6).

Stopping points. The property chain stops at C-27 (depth 3): effects on renters through property prices would be a diffuse bystander effect after depth 3. The investment chain stops at C-22 (depth 4).

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance premise | Combined sign |
|---|---|---|---|---|
| savers.taxable, saving, medium | CR-4 exception: target savers save more (A-15) | CR-4b/c: saving brings less, so marginal savers consume more | None stated. CR-12b | ambiguous (C-11) |
| savers.below_allowance, net_price_received, long | Higher gross rate untaxed (C-18) | Fixed allowance erodes as nominal interest grows (A-13) | None stated. CR-12b | ambiguous (C-19) |
| savers.taxable, net_price_received, short | none | Tax withheld (C-1); gross rate rises only in part (A-1) | CR-7b: borrowers' untaxed alternatives (non-resident lenders, share issues) make savers the side with fewer alternatives, so the net return falls even after the gross rate rises (A-1) | decrease (C-1) |
| banks, deposits and rates | — | — | Different variables (C-16 quantity, C-17 price); not netted (CR-12c) | separate |
| government.budget, tax_revenue vs tax_revenue_vs_static_projection | — | — | Different variables (CR-12c) | separate |

## 8. Time structure

Horizons: short = from the 15 March announcement to the end of the first year of the tax; medium = years 2 to 5; long = beyond 5 years.

- **Announcement (CR-10a, CR-7c).** Bond prices fall when the tax becomes expected (15 March; firmly after passage in June), not on 1 January (C-15). The loss falls on whoever holds the bonds then, because later buyers pay the lower price (CR-7c). Shares and property can rise at announcement for the same reason (C-26).
- **Window before 1 January (CR-10a).** Savers open Quellan accounts, move into accumulating funds and fill this year's retirement-account allowance before the tax starts. Where account terms and indentures allow (A-4, p 0.6), banks and issuers credit accrued interest before 1 January: interest credited in the last weeks before 1 January rises, interest credited early in the following year falls. Without the policy there would be no reason to bring the crediting forward, so this is recorded here as a note on the path, and its effect on revenue is part of C-13.
- **Stocks and flows (CR-10b).** The capital stock responds to dearer credit only through reduced investment, so C-22 is long. The supply of property and listed shares grows slowly (A-12), so their prices carry the shift for years.
- **Growing bite (CR-10, arithmetic).** The allowance is fixed in money terms. With inflation at 3% and growing balances (A-13), each year more savers cross 1,000 crowns of interest, so the share of savers taxed rises over time (C-19).
- **Expected rate rises.** If savers expected the rate to rise (A-14, p 0.45), they would move faster and further now. Not reported.

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-29 | savers.taxable | resources_available_other_uses | decrease | The tax paid, plus the time, fees and advice spent restructuring savings, opening foreign accounts and filing; none of this serves another end of theirs | CR-8a, CR-8b, CR-8c; CR-3a |
| C-30 | officials.enforcement | enforcement_cost | increase | Staff time on audits of foreign income and on processing bank reports | CR-1 op 3; CR-8c |
| C-21 | borrowers.bank_dependent | quantity_traded (bank loans) | decrease | Loans that would have been made, and the gain each party expected from them (listed in section 6) | CR-5a; CR-4c |
| C-31 | lobby.savings | resources_available_other_uses | decrease | Resources spent lobbying (C-10) | CR-8c |

Revenue: the act has no earmark, so the revenue joins the general budget (CR-8d: money is fungible, so the minister's statement about the pension deficit fixes nothing). What it is spent on is out of scope. The revenue is a receipt to the budget exactly equal to what savers pay (CR-8b); both sides appear (C-2, C-29).

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | Gross interest rates do not rise by the full amount of the tax, so savers bear at least part of it. | other | 0.9 | Open capital account; non-resident exemption; size of the market relative to foreign lenders. | C-1 fails (borrowers bear all of it); C-11, C-17, C-29 change. |
| A-2 | Diversified savers have and use untaxed alternatives. | substitutability | 0.85 | Share ownership and property investment by income group; adviser networks; size of retirement-account caps relative to their wealth. | C-4 to C-6, C-12 to C-14, C-16, C-26, C-27 fail. |
| A-3 | Accumulating funds stay untaxed and banks can offer them. | other | 0.7 | Text of K3; Tax Agency guidance; whether parliament closes the omission. | C-7 fails. |
| A-4 | Banks and issuers can credit accrued interest before 1 January. | other | 0.6 | Account terms; bond indentures. | Timing note in section 8 fails; C-13 rests on A-2 alone. |
| A-5 | Moving deposits to Quellan is practical for many diversified savers. | mobility | 0.75 | Online account opening; distance; Quellan banks' minimum balances. | C-8, C-9, C-28 fail. |
| A-6 | The Tax Agency detects little undeclared foreign interest. | enforcement | 0.8 | No information exchange with Quellan; audit rates. | C-8, C-9, C-28 fail (declared foreign interest is taxed the same). |
| A-7 | Banks, retirement-account providers and retiree groups organize. | other | 0.75 | Existing associations; past lobbying on savings rules. | C-10, C-31 fail. |
| A-8 | Resident savers are the marginal buyers for a meaningful part of the bond market, so non-residents do not absorb the selling at the old price. | substitutability | 0.6 | Share of bonds held by residents; non-resident demand for crown bonds. | C-15, C-23 to C-25 fail. |
| A-9 | Non-resident lenders and share issues replace only part of the funds residents withdraw, at the old gross rate. | substitutability | 0.65 | Non-resident share of the crown bond market; bank access to foreign funding. | C-17 to C-25 fail. |
| A-10 | Small firms and households rely mainly on bank credit. | other | 0.85 | Credit statistics by borrower size. | C-20 to C-22 fail. |
| A-11 | Firms' investment responds at the margin to the cost of debt finance. | other | 0.8 | Investment surveys; share of investment financed by debt. | C-22 fails. |
| A-12 | The supply of property and listed shares is slow to expand. | durability | 0.8 | Building permits and construction times; new listings. | C-26, C-27 weaken (more of the demand is met by new supply). |
| A-13 | Nominal interest incomes keep rising (inflation, growth of balances). | other | 0.8 | Inflation trend; growth of household deposits. | C-19 becomes increase. |
| A-14 | Savers expect the rate to be raised within a few years. | expectations | 0.45 | Government statements; history of other capital taxes. | Below cut-off; not used in reported consequences. |
| A-15 | A meaningful share of savers save toward a fixed future sum. | other | 0.7 | Household surveys of saving motives. | C-11 becomes decrease. |
| A-16 | Bond buyers expect the tax to stay in force for much of the remaining life of the bonds already issued. | expectations | 0.8 | Passed by parliament with no sunset; government's stated revenue need; history of capital taxes once introduced. | C-15 weakens to a small fall. |
| A-N1 | Many taxable savers hold mainly deposits and lack practical untaxed alternatives (minimum investment sizes, advice costs, no Quellan account, retirement-account cap already used or unaffordable). | substitutability | 0.75 | Distribution of household financial assets by wealth; share of deposits in the portfolios of middle-income and older savers. | C-12 fails. |
| A-N2 | Banks set deposit rates by account type and balance, not by whether a depositor's interest is above the allowance, so higher gross rates reach small depositors too. | other | 0.6 | Banks' rate schedules; whether banks know depositors' total interest across banks. | C-18, C-19 fail. |

## 11. Report

**The policy:** From 1 January, Corvania withholds 20% of the nominal interest that resident individuals receive on deposits, bonds (including bonds already issued) and money-market fund distributions, after a fixed allowance of 1,000 crowns a year. Interest in retirement accounts (up to 6,000 crowns of contributions a year) and interest paid to non-residents is exempt. Foreign interest is taxed at the same rate but only on self-declaration. Funds that accumulate income are not mentioned and are taken to be untaxed. The tax was announced on 15 March.

**Visible consequences:** Taxable savers receive less interest after tax (C-1); because the tax falls on nominal interest, it takes about 80% of the real return on a 4% deposit when inflation is 3%. The budget collects revenue (C-2). Banks carry new withholding and reporting work (C-3).

**Invisible consequences:**
- *Savers who can move.* Diversified savers shift out of taxed deposits and bonds (C-4) into shares, property, accumulating funds and retirement accounts (C-5, C-6, C-7), and some move deposits to Quellan without declaring the interest (C-8, C-9). Revenue falls short of the rate times the old base (C-13, C-14). Their restructuring costs are used up (C-29).
- *Savers who cannot move.* Those with mainly deposits and no practical alternative bear a larger share of the tax (C-12, assumption A-N1).
- *Small savers.* As banks pay more for deposits, savers under the allowance earn more than they would have (C-18); over the long run the fixed allowance draws more of them into the tax, so the long-run direction is ambiguous (C-19).
- *Bondholders.* Holders of existing bonds when the tax was announced lose value at once (C-15); later buyers do not.
- *Borrowers and investment.* Banks lose resident deposits (C-16) and pay more for funds (C-17); small firms and households pay more for loans and borrow less (C-20, C-21); over time the economy's capital stock is smaller than otherwise (C-22). The government pays more on new bond issues (C-23). Exempt non-resident lenders earn more and lend more (C-24, C-25).
- *Asset markets.* Owners of shares and property gain as savers move into them (C-26); buyers of those assets pay more (C-27).
- *Across the border.* Quellan banks take in deposits (C-28).
- *Lobbying and enforcement.* Banks, retirement-account providers and retiree groups lobby (C-10, C-31); the Tax Agency spends more on audits (C-30).

**Ambiguous effects:** Saving by taxable savers (C-11): a lower return leads some to consume more now, while those saving toward a fixed sum must save more. What would decide it: the share of target savers and how much of their wealth the tax touches. Small savers' long-run interest (C-19): higher gross rates against fiscal drag on the fixed allowance. What would decide it: the size of the gross-rate rise compared with growth of nominal interest.

**Key conditions:** Most consequences rest on A-2 (diversified savers have alternatives, 0.85), A-1 (savers bear part, 0.9) and A-6 (weak detection of foreign interest, 0.8). The borrowing-cost chain rests on A-8 (0.6) and A-9 (0.65), the two least certain premises reported. The small-saver result needs a new premise, A-N2 (0.6).

**What this analysis cannot say:** How large any of these effects are; how the burden splits in numbers between savers and borrowers; whether the revenue is worth the costs; whether the policy is good. It does not analyze how the revenue is spent (out of scope), nor health, safety or environmental effects. Not reported (an assumption below 0.5): faster and larger flight now because savers expect the rate to rise (A-14, p 0.45).

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | savers.taxable | net_price_received (after-tax interest on deposits and bonds) | decrease | short | visible | B | CR-1 op 3, op 4; CR-7b (borrowers have untaxed foreign lenders, so the burden settles at least partly on savers); arithmetic | A-1 |
| C-2 | government.budget | tax_revenue | increase | short | visible | A | CR-1 op 4; CR-8b | none |
| C-3 | banks | compliance_cost | increase | short | visible | A | CR-1 op 3; CR-8c | none |
| C-4 | savers.taxable_diversified | quantity_demanded (taxed deposits, bonds, distributing funds) | decrease | short | invisible | B | CR-4b (x: taxed interest asset, y: untaxed asset); CR-7a | A-2 |
| C-5 | savers.taxable_diversified | quantity_substitute (shares, property, accumulating funds, retirement accounts) | increase | medium | invisible | B | CR-4b (x: taxed interest asset, y: untaxed asset); CR-7a | A-2 |
| C-6 | retirement_account_providers | quantity_traded (contributions to registered retirement accounts) | increase | short | invisible | B | CR-4b (x: taxed account, y: exempt retirement account) | A-2 |
| C-7 | fund_managers | reclassification (distributing to accumulating funds) | increase | short | invisible | B | CR-4b (x: covered form, y: uncovered form); CR-7a | A-3 |
| C-8 | savers.taxable_diversified | cross_border_purchases (deposits and bonds held in Quellan) | increase | short | invisible | B | CR-4b (x: here, y: there) jointly with CR-4b (x: comply, y: violate) | A-5, A-6 |
| C-9 | savers.taxable_diversified | informal_activity (undeclared foreign interest) | increase | short | invisible | B | CR-1 (enforcement premise: K2 becomes a risk, op 3); CR-4b (x: comply, y: violate) | A-5, A-6 |
| C-10 | lobby.savings | lobbying_effort | increase | short | visible | B | CR-4b (x: accept, y: lobby) | A-7 |
| C-11 | savers.taxable | saving | ambiguous | medium | invisible | B | (−) CR-4b, CR-4c (x: save, y: consume now); (+) CR-4 exception (fixed-sum savers); CR-12b | A-1, A-15 |
| C-12 | savers.taxable_undiversified | tax_share_borne | increase | medium | invisible | B | CR-4b (others move away); CR-7b (burden settles on those without alternatives) | A-2, A-N1 |
| C-13 | government.budget | tax_revenue_vs_static_projection | decrease | short | invisible | B | CR-4b (substitution, reclassification, relocation); CR-10a (crediting brought forward, where A-4 holds) | A-2 |
| C-14 | government.budget | tax_revenue_vs_static_projection | decrease | medium | invisible | B | CR-4b; CR-7a | A-2 |
| C-15 | bondholders.existing | asset_value (crown bonds already issued) | decrease | short | invisible | B | CR-9 (same_market_other_segment); CR-7c; CR-10a, CR-10c | A-8, A-16 |
| C-16 | banks | quantity_traded (resident deposits) | decrease | medium | invisible | B | CR-4b (savers); CR-9 (input_to) | A-2 |
| C-17 | banks | price_paid (gross deposit rate) | increase | medium | invisible | B | CR-9 (input_to); CR-6 (price tends to the clearing level); CR-7a | A-1, A-9 |
| C-18 | savers.below_allowance | net_price_received (deposit interest) | increase | medium | invisible | B | CR-9 (same_market_other_segment); CR-7a | A-9, A-N2 |
| C-19 | savers.below_allowance | net_price_received (deposit interest) | ambiguous | long | invisible | B | (+) CR-9, CR-7a; (−) CR-10 with arithmetic (fixed allowance, rising nominal interest); CR-12b | A-9, A-13, A-N2 |
| C-20 | borrowers.bank_dependent | price_paid (bank loan rates) | increase | medium | invisible | B | CR-9 (input_to; LW-10); CR-7a | A-9, A-10 |
| C-21 | borrowers.bank_dependent | quantity_traded (bank loans) | decrease | medium | invisible | B | CR-9 (input_to); CR-4c; CR-5a | A-9, A-10 |
| C-22 | firms.investing | capital_stock_economy | decrease | long | invisible | B | CR-9 (input_to); CR-4b (x: invest, y: not invest); CR-10b | A-9, A-10, A-11 |
| C-23 | borrowers.government | price_paid (yield on new bond issues) | increase | medium | invisible | B | CR-9 (same_market_other_segment); CR-7a | A-8, A-9 |
| C-24 | lenders.non_resident | net_price_received (yield on crown assets) | increase | medium | invisible | B | CR-9 (same_market_other_segment); CR-7a | A-8, A-9 |
| C-25 | lenders.non_resident | quantity_supplied (funds lent in crowns) | increase | medium | invisible | B | CR-4b (x: other markets, y: crown assets); CR-7a | A-8, A-9 |
| C-26 | owners.untaxed_assets | asset_value (shares and property) | increase | short | invisible | B | CR-9 (substitute); CR-7c; CR-10a | A-2, A-12 |
| C-27 | buyers.untaxed_assets | price_paid (shares and property) | increase | medium | invisible | B | CR-9 (substitute); CR-6 | A-2, A-12 |
| C-28 | banks.quellan | quantity_traded (deposits from Corvanian residents) | increase | short | invisible | B | CR-9 (across_border) | A-5, A-6 |
| C-29 | savers.taxable | resources_available_other_uses | decrease | short | invisible | B | CR-8a, CR-8b, CR-8c; CR-3a | A-1 |
| C-30 | officials.enforcement | enforcement_cost | increase | short | invisible | A | CR-1 op 3; CR-8c | none |
| C-31 | lobby.savings | resources_available_other_uses | decrease | short | invisible | B | CR-8c | A-7 |

## Gaps found

**(a) Calculus gaps.** None. Every step was derived from CR-1 to CR-12, the foundations and arithmetic. One limitation of the ontology rather than the calculus: there is no variable for "interest credited in a window", so the pre-1 January crediting shift (A-4) is recorded as a note in section 8 and through C-13 rather than as per-window consequences.

**(b) New premises.**
- A-N1 (p 0.75): C-12 applies CR-7b to split taxable savers. CR-7b puts the burden on those without alternatives, but A-2 only says that diversified savers *have* alternatives; it says nothing about the others. A premise that a meaningful group lacks practical alternatives was needed to conclude that they bear a larger share.
- A-N2 (p 0.6): C-18 and C-19 follow the higher gross deposit rate (C-17) to savers under the allowance. CR-9 carries the rate along the deposit market only if banks cannot pay different rates to taxed and untaxed depositors, which is a fact about bank pricing, not a consequence of any core rule.

**(c) Unclear core rules.**
- CR-1: a tax on an option's yield is both op 3 (the option brings less) and op 4 (means transferred). The rule does not say whether a single provision should be recorded under one operation or both; recorded under both here.
- CR-7b: "the lasting gain or loss settles on the means that cannot move" reads as all-or-nothing. When both sides have some alternatives (savers and borrowers here), the rule does not say whether it licenses "the less mobile side bears more" or only "at least part". A-1 had to fix this.
- CR-4 exception: applied to saving (C-11) as instructed. The exception's wording ("a lower return on something they save toward a fixed sum") fits saving directly, but it does not say whether it also covers C-4 (the choice among assets), where a change in total means could in principle also alter the mix. Treated as not biting there, because the choice between taxed and untaxed assets of similar risk does not change with wealth in any direction the rule names.
- CR-12b refers to "a dominance pattern" for a dominance claim. In a core-only run the dominance premise in section 7 had to be stated directly from CR-7b and A-1; the core rules do not say what form such a premise should take.

## Comparison with the pattern-based analysis

**Summary.** The two versions agree on the core of the case: savers bear the tax at least in part and diversified savers move to untaxed forms, Quellan and undeclared foreign interest; bonds already issued lose value at announcement; gross rates rise for borrowers and the government; untaxed assets rise in price. Both treat total saving as `ambiguous` under CR-4's exception, so neither overclaims on saving. Neither commits an incidence error: the pattern version's DM-1 claim (savers bear the larger part) and the core version's CR-7b reading (savers bear at least part, A-1) point the same way, and the pattern version's stronger claim is not separately listed as a consequence. There are three sign differences. Two are errors in the core version, which failed to compose chains it had itself derived (CR-12b): it signs `capital_stock_economy` as a decrease although its own C-11 (saving ambiguous), C-5 (funds into shares) and C-25 (non-resident lenders lend more) push the other way, and it signs revenue against a static projection as a decrease in the medium run although its own C-17 raises the gross rate on the remaining base. The third goes the other way: the pattern version applied TS-3 to small savers (fiscal drag) without the opposing chain that its own C-13 implies, namely that higher gross deposit rates reach savers under the allowance. The core version found this chain, which needs a new premise (A-N2), and is right to report `ambiguous`. No pattern is wrong. No limit of the core rules was found.

**Counts.** M 11, V 11, S 3, OP 4, OC 2. Causes over S, OP and OC (9 items): P 0, K 0, A 2, E 7, J 0.

**Pattern version → core version**

| Pattern ID | Matched core ID(s) | Class | Cause | Note |
|---|---|---|---|---|
| C-1 | C-1 | M | | Same claim. Pattern horizon short–long, core short. TX-11's arithmetic appears in both. |
| C-2 | C-2 | V | | Actor class `officials.enforcement` vs `government.budget`. |
| C-3 | C-5, C-6 | M | | The core version splits off retirement-account contributions (C-6). |
| C-4 | C-4, C-16 | V | | Pattern: funds supplied through taxed forms (`quantity_supplied`, medium). Core: taxed assets held (`quantity_demanded`, short); C-16 records the banks' side. Both rest on CR-4 between assets of similar risk. Neither version applies CR-4's exception to the asset mix, and the core version records why. |
| C-5 | C-7 | V | | The core version omits banks' prize and bonus deposit products, a minor omission. |
| C-6 | (section 8 note) | OC | E (core) | Early crediting of interest before 1 January. The core version derives it (CR-10a) but keeps it as a path note, on the ground that "without the policy there would be no reason" to move it. That misreads 2.5: crediting happens in the counterfactual too, so per-window signed consequences are required. The pattern version's recording as `reclassification` is loose but scorable. |
| C-7 | C-8 | M | | |
| C-8 | C-9 | V | | Horizon medium vs short. |
| C-9 | C-3 | M | | |
| C-10 | C-29 | V | | The core version folds advice and restructuring costs into `resources_available_other_uses`, not `compliance_cost`. |
| C-11 | C-10 | M | | |
| C-12 | C-15 | M | | Both versions date it to the announcement (CR-7c / SB-4). |
| C-13 | C-17, C-20 | V | | The core version covers bank-dependent borrowers and banks' deposit rates. Large corporate bond issuers are not separately signed. |
| C-14 | none | OC | E (core) | `borrowers.small` bear more than `borrowers.large`. CR-7b with A-9 and A-10 derives it (large firms can issue bonds or shares and borrow abroad). The core version did not split borrowers. |
| C-15 | C-12 | V | | The core version needed A-N1 (a group lacking alternatives). The pattern version built that premise into the definition of `savers.deposit`. The core version's point is fair: A-2 alone does not establish it. |
| C-16 | C-22 | V | | Debt-financed investment falls: the pattern version records `investment_target`; the core version records it under `capital_stock_economy`, which is the wrong variable (see the next-to-last row). |
| C-17 | C-23 | M | | |
| C-18 | C-26, C-27 | V | | The core version adds the owners' gain (C-26), the CR-8 counterpart of the buyers' higher price. |
| C-19 | C-28 | M | | |
| C-20 | C-19 | S | A | Pattern: `savers.small` net interest decreases (long, TS-3). Core: ambiguous. The core version adds the chain in which higher gross deposit rates reach savers under the allowance untaxed (CR-9, CR-7a), which needs A-N2 (banks do not price by tax status, p 0.6). **Core right**: with A-N2 above the cut-off, CR-12b requires `ambiguous`. The pattern version's own C-13 (gross rates rise) implies the + chain, so the pattern version should have found it. |
| C-22 | C-29 | M | | |
| C-23 | C-21, C-16 | M | | |
| C-24 | C-30 | V | | Pattern: taxpayers' resources (funding side, CR-8a). Core: `enforcement_cost` (spending side). These are the two halves of the same CR-8 link. |
| — (`savers.deposit` quantity_supplied, ambiguous) | C-11 | V | | The core version merges this into saving by all taxable savers. |
| — (`saving`, ambiguous) | C-11 | M | | Both apply CR-4's exception (TX-6's Unless clause) correctly. |
| — (`capital_stock_economy`, ambiguous) | C-22 | S | E (core) | Core: decrease. **Pattern right.** By CR-12b the economy-wide stock is `ambiguous`: the core version's own C-11 (saving ambiguous), C-5 (funds into shares, which finance equity investment) and C-25 (exempt foreign lenders supply more) oppose the debt-finance chain. The core version also attaches an economy-wide variable to `firms.investing`. The correct core consequence is `investment_target` (debt-financed) decrease, with `capital_stock_economy` ambiguous. |
| — (`tax_revenue_vs_static_projection`, ambiguous) | C-13, C-14 | S | E (core) | Core: decrease (short and medium). **Pattern right for the medium run**: an ad valorem tax on a price the tax itself raises gives a + chain (the core version's own C-17) against base erosion, so CR-12b requires `ambiguous` (TX-9's Unless clause is pure arithmetic). In the short run the core version's decrease is defensible: coupons on bonds already issued are fixed, gross rates move only over the medium run, and early crediting (A-4) lowers first-year collections. |

**Core-only consequences**

| Core ID | Class | Cause | Note |
|---|---|---|---|
| C-18 | OP | A | Savers under the allowance earn more in the medium run (higher gross rate, untaxed). Needs A-N2. The pattern version omitted it although its C-13 implies it. |
| C-24 | OP | E (pattern) | Exempt non-resident lenders earn a higher net yield (CR-9, CR-7a). The pattern version mentions foreign lenders only as an offsetting chain in section 7. |
| C-25 | OP | E (pattern) | Non-resident lenders supply more crown funds. Same omission as C-24; it is what makes the pattern version's own `capital_stock_economy` row ambiguous. |
| C-31 | OP | E (pattern) | Resources used up in lobbying (CR-8c / OC-1). A minor omission. |

**Findings**
- No pattern is wrong here. TX-6's Unless clause gives the same answer as CR-4's exception: both versions report saving as `ambiguous`. TX-9's Unless clause is sound arithmetic, and the core version should have reached it through CR-12b.
- Errors in the core version: C-22 signs `capital_stock_economy` (economy-wide) as a decrease against its own opposing chains, using the wrong variable for a debt-finance effect. C-13 and C-14 ignore the gross-rate chain in the medium run. C-14 of the pattern version (split among borrowers) is omitted. The early-crediting shift is kept as a path note through a misreading of 2.5's timing-shift rule.
- Errors in the pattern version: C-20 applies TS-3 without composing it with the gross-rate chain (CR-12b). It omits non-resident lenders' gain and response (core C-24, C-25) and the cost of lobbying.
- Limits of the core rules: none that changed a sign. The core version's notes are fair: CR-7b's "settles on" does not say whether it licenses "more" or only "at least part", and CR-4's exception does not say whether it reaches the choice among assets. The lack of a per-window variable for interest crediting is a limit of the ontology, not of the calculus.
