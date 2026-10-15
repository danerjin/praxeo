# WE-011 Tax on interest income from savings and bonds

Analyst: draft (Handbook 0.2)  |  Rule catalog version: 0.2  |  Status: awaiting expert review

A stylized policy in a fictional country. Its main lessons are time preference and the return to saving (LW-7, TX-6), the long horizon, substitution into untaxed assets, and incidence between savers and borrowers. It also shows a case where the catalog's TX-6 conclusion meets an opposing chain the catalog does not cover. The probabilities are illustrative; the evidence column says what a real analysis would cite.

## 1. Policy record

**Corvania Savings Income Tax Act.** Corvania is a mid-sized country with its own currency (the crown), an open capital account and a well-developed banking system. Until now, interest received by individuals has been untaxed, as have dividends and capital gains on shares; rental income is taxed under the ordinary income tax, unchanged by this act. Bank deposit rates are about 4%, ten-year government bonds pay about 5%, and inflation has run at about 3% for several years. The neighboring Federation of Sarn has no tax on interest and does not exchange account information with Corvania; opening a Sarn account takes a short trip or an online application. The finance minister announced the tax in the budget speech on 15 March; parliament passed it in June; it applies to interest paid from 1 January of the following year.

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Interest tax | `income_tax` on interest (`capital_tax` family) | Interest paid to resident individuals on bank deposits, government and corporate bonds, and distributions from money-market funds | Banks and paying agents withhold; savers bear it | 20% final withholding on nominal interest, including coupons on bonds already issued (no grandfathering). | First 1,000 crowns of interest per person per year (fixed in money terms, not indexed). Interest inside registered retirement accounts (contributions capped at 6,000 crowns a year). Interest paid to non-residents. |
| K2 Foreign interest | `income_tax` | Interest received by residents from foreign accounts and bonds | Resident savers | Same 20%, self-declared on the annual return. | Same allowance. |
| K3 Funds | Definition | Investment funds holding bonds | Fund managers | Tax is withheld on distributions only. Funds that accumulate income instead of distributing it are not mentioned. | Accumulating funds (by omission). |
| K4 Administration | Enforcement | K1 to K3 | Tax Agency | Banks report totals withheld; audits of declared foreign income. | None |

Revenue use: general budget. The minister said the revenue would "help close the pension deficit", but the act has no earmark. Spending is out of scope; OC-1 is applied to the payers.

Unclear provisions: whether income accumulated inside a fund will later be taxed on sale of the fund units. The text taxes only distributions; analyzed as untaxed (A-3).

## 2. Classification

| Component | Rothbard type | Binding? | Rule families |
|---|---|---|---|
| K1 | Binary: a forced payment to the state out of the return on saving | Yes, for savers above the allowance | TX-1, TX-2, TX-6, TX-9, DM-1, RS |
| K2 | Binary | Only as far as it is enforced (A-6) | RS-3, RS-4 |
| K3 | Definition creating an untaxed category | Yes | RS-5 |
| K4 | Binary: funded by taxpayers | Yes | TX-5, OC-3 |

Treating interest as a price: interest is the price of present money in terms of future money, so a tax on it works like an ad valorem tax on that price. TX-2 is applied with savers as sellers of present money and borrowers as buyers: the gross rate paid by borrowers rises, the net rate received by savers falls, or both.

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `savers.small` | Residents whose interest is under the 1,000-crown allowance (about 25,000 crowns of deposits at 4%) | Untaxed for now; more of them cross the allowance over time. |
| `savers.deposit` | Residents above the allowance who hold mainly bank deposits and bonds, including many retirees living on interest | Net interest falls by a fifth; few alternatives they know or trust. |
| `savers.diversified` | Wealthier residents with advisers, shares, property and access to foreign accounts | Net interest falls; can move into untaxed assets or abroad. |
| `bondholders.existing` (`factor_owners.specific`) | Residents holding bonds already issued | Coupons fixed, now taxed. |
| `banks` | Deposit-takers and withholding agents | Must withhold and report; may lose deposits. |
| `borrowers.small` | Households and small firms that borrow from banks | Face banks whose deposit funding costs more. |
| `borrowers.large` | Large firms that issue bonds or shares, or borrow abroad | More alternatives. |
| `taxpayers` (as government borrower) | The state, which issues bonds held partly by residents | Its bonds are less attractive to residents. |
| `sellers.substitutes` | Issuers and sellers of untaxed assets: shares, property, gold, retirement accounts, accumulating funds | More demand. |
| `homebuyers` | Buyers of residential property for their own use | Compete with savers buying property as an investment. |
| `neighboring_jurisdictions` | Banks in Sarn | Gain Corvanian deposits. |
| `officials.enforcement` | Tax Agency | New withholding and audit work. |

## 4. Direct effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | `savers.deposit`, `savers.diversified` | `net_price_received` (interest after tax) | decrease | short | TX-1, TX-2, DM-1 | A-1 |
| C-2 | `officials.enforcement` | `tax_revenue` (interest tax) | increase | short | TX-1 | none |

The visible effects: savers receive less interest, and the state collects the tax.

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-3 | `savers.diversified` | `quantity_substitute` (shares, property, gold, retirement accounts) | increase | short to medium | RS-1, TX-6 | A-2 |
| C-4 | `savers.diversified` | `quantity_supplied` (funds lent through taxed deposits and bonds) | decrease | medium | TX-6, RS-1, RS-4 | A-2 |
| C-5 | `banks`, fund managers | `reclassification` (accumulating bond funds; deposit products paying returns as prizes or bonuses) | increase | medium | RS-5 | A-3 |
| C-6 | `banks`, bond issuers | `reclassification` (crediting accrued interest before 1 January) | increase | short | RS-8 | A-4 |
| C-7 | `savers.diversified` | `cross_border_purchases` (deposits and bonds in Sarn) | increase | short to medium | RS-4, TX-4 | A-5 |
| C-8 | `savers.diversified` | `informal_activity` (foreign interest not declared) | increase | medium | RS-3 | A-5, A-6 |
| C-9 | `banks` | `compliance_cost` (withholding systems, reporting) | increase | short | TX-5 | none |
| C-10 | `savers.diversified` | `compliance_cost` (advice, restructuring, foreign accounts) | increase | short | OC-2 | A-2 |
| C-11 | `banks`, retirement-account providers, `savers.deposit` | `lobbying_effort` (higher allowance, higher retirement cap, exemption for deposits) | increase | medium | RS-7 | A-7 |

C-4 applies TX-6 to the group for which every chain points the same way. Diversified savers who still want to save the same amount can do it in untaxed forms, so their funds leave taxed deposits and bonds whichever way their total saving moves. For `savers.deposit`, who have few alternatives, the direction is not settled (section 7).

Not reported: savers expecting the rate to rise once the withholding system exists, and moving more money now (TS-2); A-14 is below the cut-off (p = 0.45).

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-12 | `bondholders.existing` | `asset_value` (bonds already issued) | decrease | short (at announcement) | GAP-011-2 | | A-8 |
| C-13 | `borrowers.small`, `borrowers.large` | `price_paid` (gross interest rate on loans and bonds) | increase | medium | TX-2, DM-1 | taxed deposits and bonds: `input_to` bank lending and business borrowing | A-1, A-9 |
| C-14 | `borrowers.small` | `tax_share_borne` (relative to `borrowers.large`) | increase | medium | DM-1 | | A-9, A-10 |
| C-15 | `savers.deposit` | `tax_share_borne` (relative to `savers.diversified`) | increase | short | DM-1 | | A-2 |
| C-16 | `borrowers.small`, `borrowers.large` | `investment_target` (business investment financed by loans and bonds) | decrease | medium to long | TX-6, TX-2 | | A-9, A-11 |
| C-17 | `taxpayers` | `price_paid` (gross yield on new government borrowing) | increase | medium | TX-2, DM-1 | | A-1, A-9 |
| C-18 | `homebuyers`, buyers of shares | `price_substitute` (residential property, listed shares) | increase | medium | RS-1 | taxed deposits and property or shares: `substitute`, partial | A-2, A-12 |
| C-19 | `neighboring_jurisdictions` (Sarn banks) | `quantity_traded` (deposits from Corvanian residents) | increase | short to medium | RS-4 | Corvanian and Sarn deposits: `across_border`, close for diversified savers | A-5 |
| C-20 | `savers.small` | `net_price_received` (interest after tax) | decrease | long | TS-3 | | A-13 |

C-12: a bond's price is the value today of its future coupons. Taxing those coupons lowers what a resident buyer will pay, so the price of bonds already issued falls when the tax becomes expected, in March, not in January. Non-residents are exempt and may buy some of these bonds, which limits the fall (A-8). The catalog has SB-4 for gains capitalized into asset prices but no rule for losses, so C-12 is Tier C (GAP-011-2).

C-13 and C-17: by DM-1, savers have fewer alternatives than borrowers, who can turn to exempt non-resident lenders and to shares, so savers bear the larger part (C-1), and gross rates rise by the smaller part. C-14: small firms and households cannot issue bonds or borrow abroad, so within the borrowers' side they bear more. C-17 grows as the state's existing debt (average maturity about six years) is refinanced; part of what the tax collects on government bond interest is paid back out in higher yields.

C-18 is at depth 3 (tax, substitution into property and shares, their prices); homebuyers are an identifiable group, but the chain stops here. C-20: the 1,000-crown allowance is fixed in money terms; as nominal balances and interest grow, more small savers cross it (TS-3).

Checks. RS-9: there are no shopping trips; a saver who opens a Sarn account may move other banking business too, but no such relation is recorded, so this is not followed. RS-10: undeclared foreign interest (C-8) is evasion, not a trade moved underground: Sarn's banks are legal and advertise openly, so RS-10's effects do not apply. RS-11: retirement accounts lock money in until retirement, but the benefit is not tied to a place, so RS-11 does not apply.

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `savers.deposit`, `quantity_supplied` (funds lent through taxed deposits), medium | Savers aiming at a fixed future sum (a retirement income, a down payment) must put aside more to reach it at the lower net rate (GAP-011-4; Tier C). | The net reward for waiting is lower, so at the margin some saving gives way to present consumption (TX-6, LW-7); some funds move to the few untaxed options these savers use, such as retirement accounts (RS-1). | None | **ambiguous**. What would decide it: the share of these savers who save toward a fixed target, against those who save less when the reward falls. |
| All resident savers, `quantity_substitute` (present consumption), medium | Lower net reward for waiting (TX-6, LW-7, RS-1). | Target savers consume less to reach their goal (GAP-011-4; Tier C). | None | **ambiguous**, for the same reason. |
| Economy-wide capital stock, long | — | Less saving and more expensive debt finance mean less investment (C-16), and a smaller capital stock over time (TX-6). | — | **Not determined.** The minus chain rests on TX-6, but the total saving that would feed it is ambiguous (the two rows above), and the variable list has no economy-wide capital stock (GAP-011-1). What can be said: investment financed by interest-bearing debt falls (C-16). |
| `officials.enforcement`, `tax_revenue_vs_static_projection`, short to medium | Gross rates on the taxed instruments that remain rise (C-13), so each crown of the base earns more taxable interest. | The base shrinks: substitution, reclassification and flight abroad (C-3 to C-8). | None | **ambiguous**. TX-9 says revenue falls short of the static projection, but it is written for taxes whose base is a quantity; here the tax also raises the price in the base (GAP-011-5). |
| Split of the tax between savers and borrowers, short to medium | — | — | DM-1 | **Savers bear the larger part** (C-1); borrowers bear the rest (C-13). Within savers, `savers.deposit` bear more (C-15); within borrowers, `borrowers.small` bear more (C-14). Rothbard's view that a general tax falls on factor owners rather than being shifted (DM-1 note, Q3) bears on this tax, which falls on almost all interest: on that view the savers' share would be larger still. Not resolved. |

## 8. Time structure

The policy works over all three horizons, and the long one matters most.

- **At announcement (March).** Prices of bonds already issued fall as soon as the tax is expected (C-12): owners of those bonds bear a loss before any tax is paid. Savers and banks have nine months to restructure, and some interest is credited early (C-6).
- **Short run (the first year).** Diversified savers move into untaxed assets and abroad (C-3, C-7). Deposit savers mostly stay where they are and bear the tax (C-15).
- **Medium run.** Banks raise deposit rates to keep funding, and the higher cost reaches borrowers (C-13), first small firms and households (C-14). New products avoid the tax (C-5). The state's borrowing cost rises as its debt is refinanced over six years or so (C-17). Asset prices of untaxed substitutes are higher than they would have been (C-18).
- **Long run.** The cumulative effect of a lower net reward for waiting on investment financed by debt (C-16) compounds year after year (TX-6, LW-7): the capital it would have financed is never built, and the gap with the counterfactual widens rather than closing. Whether the economy's total capital stock is smaller cannot be settled here (section 7). Meanwhile the allowance erodes (C-20).
- **Inflation.** The tax falls on nominal interest. With 4% interest and 3% inflation, the real return is about 1%; the tax takes 0.8 points of it, about 80% of the real return, not 20%. If inflation rises in both worlds and nominal rates follow, the share of the real return taken rises further and can exceed all of it (C-21; Tier C, GAP-011-3). The TX-6 response is correspondingly stronger when inflation is higher.

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-21 | `savers.deposit`, `savers.diversified` | `net_price_received` (real interest after tax and inflation) | decrease | Real return on saving, by a larger share than the statutory 20%. | GAP-011-3 |
| C-22 | `savers.deposit`, `savers.diversified` | `resources_available_other_uses` | decrease | The consumption or further saving the tax would otherwise have paid for. | TX-1, OC-1 |
| C-23 | Savers and borrowers | `quantity_traded` (loans and deposits at pre-tax terms) | decrease | Loans that would have been made at the old rates and are not: both lender and borrower lose the gain they expected. | OC-4, TX-2 |
| C-24 | `taxpayers` | `resources_available_other_uses` | decrease | What the Tax Agency's new withholding and audit work would otherwise have funded. | OC-3, OC-1 |

Restructuring time and advice are already C-10. The general budget's use of the revenue is out of scope.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | Gross interest rates do not rise by the full amount of the tax, so savers bear at least part of it. | other | 0.9 | Open capital account; non-resident exemption; size of the market relative to foreign lenders. | C-1 shrinks; incidence falls more on borrowers. |
| A-2 | Diversified savers have and use untaxed alternatives. | substitutability | 0.85 | Share ownership and property investment by income group; adviser networks; size of retirement-account caps relative to their wealth. | C-3, C-4, C-10, C-15, C-18 fail or weaken. |
| A-3 | Accumulating funds stay untaxed and banks can offer them. | other | 0.7 | Text of K3; Tax Agency guidance; whether parliament closes the omission. | C-5 weakens. |
| A-4 | Banks and issuers can credit accrued interest before 1 January. | other | 0.6 | Account terms; bond indentures. | C-6 not reported. |
| A-5 | Moving deposits to Sarn is practical for many diversified savers. | mobility | 0.75 | Online account opening; distance; Sarn banks' minimum balances. | C-7, C-8, C-19 not reported. |
| A-6 | The Tax Agency detects little undeclared foreign interest. | enforcement | 0.8 | No information exchange with Sarn; audit rates. | C-8 not reported. |
| A-7 | Banks, retirement-account providers and retiree groups organize. | other | 0.75 | Existing associations; past lobbying on savings rules. | C-11 not reported. |
| A-8 | Resident savers are the marginal buyers for a meaningful part of the bond market, so non-residents do not absorb the selling at the old price. | other | 0.6 | Share of bonds held by residents; non-resident demand for crown bonds. | C-12 shrinks toward nothing. |
| A-9 | Non-resident lenders and share issues replace only part of the funds residents withdraw, at the old gross rate. | substitutability | 0.65 | Non-resident share of the crown bond market; bank access to foreign funding. | C-13, C-14, C-16, C-17 not reported; savers bear the whole tax. |
| A-10 | Small firms and households rely mainly on bank credit. | other | 0.85 | Credit statistics by borrower size. | C-14 not reported. |
| A-11 | Firms' investment responds at the margin to the cost of debt finance. | other | 0.8 | Investment surveys; share of investment financed by debt. | C-16 not reported. |
| A-12 | The supply of property and listed shares is slow to expand. | durability | 0.8 | Building permits and construction times; new listings. | C-18 weakens. |
| A-13 | Nominal interest incomes keep rising (inflation, growth of balances). | other | 0.8 | Inflation trend; growth of household deposits. | C-20 not reported. |
| A-14 | Savers expect the rate to be raised within a few years. | expectations | 0.45 | Government statements; history of other capital taxes. | Below cut-off; not reported. |
| A-15 | A meaningful share of savers save toward a fixed future sum. | other | 0.7 | Household surveys of saving motives. | The plus chains in section 7 vanish; the deposit-saver rows become **decrease** (Tier B). |

## 11. Report

**The policy.** Corvania taxes interest received by residents on deposits, bonds and money-market funds at 20%, withheld at source, including on bonds already issued. The first 1,000 crowns a year are exempt, as are retirement accounts and non-residents. Dividends, capital gains and accumulating funds stay untaxed. The revenue goes to the general budget.

**Visible consequences.** Savers receive a fifth less interest (C-1), and the state collects the tax (C-2).

**Invisible consequences.**
- *Owners of bonds already issued* lose part of their value as soon as the tax is announced (C-12).
- *Wealthier savers* move into shares, property, gold, retirement accounts and accumulating funds (C-3, C-5), and abroad (C-7), sometimes without declaring the interest (C-8); their funds leave taxed deposits and bonds (C-4). They spend time and money doing it (C-10).
- *Savers who hold mainly deposits*, many of them retirees, bear more of the tax (C-15), and over time more small savers cross the allowance (C-20). Because the tax falls on nominal interest, it takes a much larger share of the real return than its 20% rate suggests (C-21).
- *Borrowers* pay higher gross rates (C-13), small firms and households most (C-14), and investment financed by loans and bonds is lower, by a growing amount over the long run (C-16). The state's own borrowing costs more as its debt is refinanced (C-17). Property and share prices are higher than they would have been (C-18), which homebuyers pay. Some loans are never made (C-23). Banks in Sarn gain deposits (C-19).
- *Banks and taxpayers* bear compliance and administration costs (C-9, C-24); everyone who pays the tax gives up what it would have bought (C-22). Banks, pension providers and retirees lobby for changes (C-11).

**Ambiguous effects.** Whether deposit savers save less or more: those saving toward a fixed sum must save more, others save less. For the same reason, whether total consumption rises and whether the economy's capital stock ends up smaller. Whether revenue falls short of a static projection.

**Key conditions.** That savers bear most of the tax (A-1, p = 0.9) and that foreign funds do not fully replace residents' (A-9, p = 0.65) govern how far the tax reaches borrowers and investment. Whether savers save toward fixed targets (A-15, p = 0.7) is what keeps the saving response open.

**What this analysis cannot say.** How large any effect is; whether the economy's capital stock and wages end up lower; whether the policy is desirable.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | savers.deposit, savers.diversified | net_price_received (interest after tax) | decrease | short | visible | B | TX-1, TX-2, DM-1 | A-1 |
| C-2 | officials.enforcement | tax_revenue | increase | short | visible | A | TX-1 | none |
| C-3 | savers.diversified | quantity_substitute (untaxed assets) | increase | short–medium | invisible | B | RS-1, TX-6 | A-2 |
| C-4 | savers.diversified | quantity_supplied (taxed deposits and bonds) | decrease | medium | invisible | B | TX-6, RS-1, RS-4 | A-2 |
| C-5 | banks, fund managers | reclassification (product design) | increase | medium | invisible | B | RS-5 | A-3 |
| C-6 | banks, bond issuers | reclassification (early crediting) | increase | short | invisible | B | RS-8 | A-4 |
| C-7 | savers.diversified | cross_border_purchases | increase | short–medium | invisible | B | RS-4, TX-4 | A-5 |
| C-8 | savers.diversified | informal_activity | increase | medium | invisible | B | RS-3 | A-5, A-6 |
| C-9 | banks | compliance_cost | increase | short | invisible | A | TX-5 | none |
| C-10 | savers.diversified | compliance_cost | increase | short | invisible | B | OC-2 | A-2 |
| C-11 | banks, providers, savers.deposit | lobbying_effort | increase | medium | invisible | B | RS-7 | A-7 |
| C-12 | bondholders.existing | asset_value | decrease | short | invisible | C | GAP-011-2 | A-8 |
| C-13 | borrowers.small, borrowers.large | price_paid (gross interest) | increase | medium | invisible | B | TX-2, DM-1 | A-1, A-9 |
| C-14 | borrowers.small | tax_share_borne | increase | medium | invisible | B | DM-1 | A-9, A-10 |
| C-15 | savers.deposit | tax_share_borne | increase | short | invisible | B | DM-1 | A-2 |
| C-16 | borrowers.small, borrowers.large | investment_target (debt-financed) | decrease | medium–long | invisible | B | TX-6, TX-2 | A-9, A-11 |
| C-17 | taxpayers | price_paid (government borrowing) | increase | medium | invisible | B | TX-2, DM-1 | A-1, A-9 |
| C-18 | homebuyers, buyers of shares | price_substitute (property, shares) | increase | medium | invisible | B | RS-1 | A-2, A-12 |
| C-19 | neighboring_jurisdictions | quantity_traded (deposits from Corvania) | increase | short–medium | invisible | B | RS-4 | A-5 |
| C-20 | savers.small | net_price_received | decrease | long | invisible | B | TS-3 | A-13 |
| C-21 | savers.deposit, savers.diversified | net_price_received (real, after inflation) | decrease | short–long | invisible | C | GAP-011-3 | none |
| C-22 | savers.deposit, savers.diversified | resources_available_other_uses | decrease | short | invisible | A | TX-1, OC-1 | none |
| C-23 | savers, borrowers | quantity_traded (loans at pre-tax terms) | decrease | medium | invisible | B | OC-4, TX-2 | A-1, A-9 |
| C-24 | taxpayers | resources_available_other_uses | decrease | short | invisible | A | OC-3, OC-1 | none |
| — | savers.deposit | quantity_supplied (taxed deposits) | ambiguous | medium | invisible | C | TX-6 vs GAP-011-4 | A-15 |
| — | all resident savers | quantity_substitute (present consumption) | ambiguous | medium | invisible | C | TX-6, RS-1 vs GAP-011-4 | A-15 |
| — | officials.enforcement | tax_revenue_vs_static_projection | ambiguous | short–medium | invisible | C | TX-9 vs C-13; GAP-011-5 | A-1, A-2, A-9 |

## Gaps found

- GAP-011-1: TX-6 concludes that "saving" falls and "the capital stock is smaller over time", but neither has a variable: `capital_stock_target` covers only the target good's capacity. The economy-wide capital stock could not be entered, and the next link (less capital per worker, lower wages; Mises, *Human Action*, ch. XXI) has no rule. Proposed fix: add variables `saving` (income not consumed, by actor class) and `capital_stock_economy`; add a rule linking `capital_stock_economy` decrease to `wage_rate` decrease over the long horizon, Tier B, assuming no offsetting inflow of foreign capital.
- GAP-011-2: SB-4 covers capitalization of lasting gains into the price of durable assets, but not the mirror case: a lasting tax on an asset's return lowers its price, and the loss falls on whoever owns it when the tax becomes expected. Needed for C-12. Proposed fix: extend SB-4 (or add a new TX rule) so that a lasting tax on the return of a durable asset in fixed or slowly expanding supply gives `asset_value` decrease, at announcement, for its owners. Assumes: the marginal buyer is taxed (`substitutability`), and the tax is expected to last (`expectations`).
- GAP-011-3: No rule covers a tax on nominal returns under inflation. The share of the real return taken exceeds the statutory rate and rises with inflation. Needed for C-21. Proposed new TX rule "Tax on nominal returns": where a tax falls on nominal interest or gains and inflation is positive, the after-tax real return falls by more than the statutory rate times the real return; TX-6 responses are stronger the higher the inflation. Tier A for the arithmetic, B for the response.
- GAP-011-4: TX-6 has no exception for savers who save toward a fixed future sum, for whom a lower net return calls for more saving, not less. This chain was used (Tier C) and made the saving rows ambiguous. Proposed fix: add to TX-6 an "Unless" and a note: total saving by a group is `ambiguous` where some savers aim at a fixed target, and TX-6's sign holds unambiguously only for saving in the taxed forms by savers with untaxed alternatives. Expert decision needed on how Mises's and Rothbard's treatments of time preference bear on this.
- GAP-011-5: TX-9 states that revenue falls short of the static projection whenever the base shrinks. That is right for per-unit taxes, but for an ad valorem tax on a price the tax itself raises (here, the gross interest rate), the value of the remaining base rises, so the sign is open. Proposed fix: add to TX-9 an "Unless: ad valorem tax whose gross price rises with the tax; then combine the chains (workflow step 7)".
