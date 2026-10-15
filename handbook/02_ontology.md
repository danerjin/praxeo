# 2. Ontology

The vocabulary every analysis uses. The plan (Section 4.2) defines the concepts; this file fixes their fields and the controlled lists for version 1. The outcome cards in Phase 4 use the same lists, which is what makes predictions and observations comparable.

## 2.1 Policy record

The structured statement of what the policy does (workflow step 1).

| Field | Content |
|---|---|
| `policy_id` | Short identifier. |
| `jurisdiction` | Where it applies. Note the nearest places where it does not apply. |
| `announced`, `enacted`, `effective`, `expires` | Dates. `announced` is when the policy became publicly expected (a bill's introduction, a credible campaign promise); it drives announcement effects (RS-8). `expires` may be none. |
| `components` | One entry per distinct instrument (a policy with a cap and an exemption has two components). |
| `component.instrument` | One of the instrument types in 2.3. |
| `component.target` | The good, service, activity or factor affected. |
| `component.bound` | Who must comply. |
| `component.parameters` | The cap, rate, requirement or quantity, as stated. |
| `component.exemptions` | Who or what is excluded, and the conditions. |
| `component.enforcement` | Who enforces, with what penalties and powers. |
| `component.revenue_use` | For taxes: where the money goes, if the policy says. |
| `component.funding` | For subsidies and spending: where the money comes from. |
| `existing_rules` | Rules already in force that the policy interacts with or makes binding (a council-set meter rate that a license cap makes bind). Same sub-fields as a component. They stay in place in the counterfactual. |
| `source_text` | For each field, the sentence of the policy it comes from. Fields that the text leaves unclear are marked `unclear`, never guessed. |

## 2.2 Actor class

A group defined by its role in the situation, not by identity. Name actor classes by role plus market, for example `tenants.controlled_units`, `landlords.controlled_units`, `prospective_tenants`, `braiders.unlicensed`. Always consider these generic classes, even when the policy does not mention them:

| Class | Who |
|---|---|
| `buyers.current` | People who buy the target good now. |
| `buyers.prospective` | People who would buy it in future, or who would enter the market. |
| `sellers.current` | People and firms who supply the target good now. |
| `sellers.prospective` | Would-be entrants. |
| `factor_owners.specific` | Owners of resources that are hard to move to other uses (land, licenses, specialized equipment, specialized skills). |
| `buyers.substitutes`, `sellers.substitutes` | Participants in markets for substitutes. |
| `sellers.complements` | Suppliers of goods used together with the target good. |
| `input_suppliers` | Suppliers of inputs to the target good. |
| `taxpayers` | Those who fund the policy, directly or through the budget. |
| `officials.enforcement` | The agency that administers and enforces the policy. |
| `intermediaries` | Brokers, agents, black-market sellers, compliance consultants. |
| `neighboring_jurisdictions` | Buyers and sellers just across the boundary. |

## 2.3 Intervention instrument types (version 1)

| Instrument | Rothbard type | Rule family |
|---|---|---|
| `price_ceiling` | triangular | PC |
| `price_floor` (including minimum wage) | triangular | PC |
| `per_unit_tax`, `ad_valorem_tax` | binary | TX |
| `lump_sum_tax` (a fixed sum per household or person) | binary | TX: TX-1 and OC-1 apply; TX-2, TX-9 and DM-1 do not, because no one can reduce it by changing behavior |
| `income_tax`, `profit_tax`, `capital_tax` | binary | TX |
| `tariff` | binary (tax) and triangular (privilege) | TX |
| `per_unit_subsidy`, `lump_sum_subsidy`, `purchase_rebate` | binary | SB |
| `licensing_requirement` | triangular | EN |
| `quota` | triangular | EN |
| `prohibition` (of a good or service) | triangular | EN |

## 2.4 Variables (controlled list, version 1)

Every consequence names one variable from this list. Add a variable only by editing this file, so that predictions and outcome cards stay comparable.

**Prices and quantities**

| Variable | Meaning |
|---|---|
| `price_paid` | Money price paid by buyers, including taxes. |
| `net_price_received` | Money price received by sellers, after taxes and including subsidies. |
| `quality_adjusted_price` | Price per unit of quality, where quality is variable. |
| `quantity_demanded` | Amount buyers wish to buy at the prevailing price. |
| `quantity_supplied` | Amount sellers offer at the prevailing price. |
| `quantity_traded` | Amount actually exchanged in the legal market. |
| `excess_demand` | Shortage: quantity demanded minus quantity supplied, at a controlled price. |
| `excess_supply` | Surplus: quantity supplied minus quantity demanded, at a controlled price. |
| `price_substitute`, `quantity_substitute` | Price and quantity in the market for a named substitute. |
| `price_complement`, `quantity_complement` | Same, for a named complement. |
| `asset_value` | Market value of a durable asset tied to the target (land, building, license, quota right, shares in a firm). |
| `full_cost_per_unit` | Money price plus the value the buyer places on the wait, search and side payments needed to obtain a unit. Usually `ambiguous` under a ceiling. |
| `inventory_held` | Stocks of a good held by an actor class at a named time (sellers' stocks before a season; an agency's surplus stocks). |
| `transaction_size` | Typical amount per exchange (loan size, order size). |

**Allocation, quality and non-price terms**

| Variable | Meaning |
|---|---|
| `wait_time` | Time spent queuing or on waiting lists. |
| `search_cost` | Time and money spent finding a seller or buyer. |
| `side_payments` | Payments outside the controlled price (key money, bribes, tie-in purchases). |
| `quality_per_unit` | Quality of each unit sold (including maintenance and service). |
| `quality_variability` | Spread of quality between units bought in a market (for a drug, potency and purity). |
| `quality_information` | How easily buyers can judge a seller's quality before buying: reviews, brands, certification, legal recourse. |
| `share_concentrated_forms` | Share of sales in concentrated, high-potency forms of a good. |
| `allocation_by_non_price_criteria` | Use of connections, discrimination or favoritism in deciding who gets the good. |
| `turnover` | Rate at which holders of the good change (tenant moves, job changes). |
| `variety` | Number of distinct versions of the good offered. |
| `share_of_sellers_licensed` | Share of active legal sellers who hold the required license or permit. |
| `job_changes` | Rate at which members of an actor class change jobs, including moves that require changing home. |

**Production, capital and entry**

| Variable | Meaning |
|---|---|
| `investment_target` | New investment in producing the target good. |
| `maintenance_spending` | Spending on keeping existing capital in use. |
| `capital_stock_target` | Existing productive capacity for the target good. |
| `capital_stock_economy` | Capital across the economy, not only in the target activity. |
| `saving` | Income not consumed, by actor class. |
| `return_on_capital` | Net money return per unit of capital invested, for a named actor class. |
| `units_held_vacant` | Units of a durable good kept out of use by their owners: neither occupied, rented nor offered. |
| `number_of_sellers` | Count of active sellers. |
| `entry_rate` | Rate at which new sellers enter. |
| `employment` | Number of people employed in the named activity. |
| `hours_worked` | Hours per worker. |
| `non_wage_compensation` | Benefits, training, flexibility and other non-money terms of employment. |
| `wage_rate` | Money wage per hour. |
| `earnings` | Total money earnings of a group (wage times hours times employment). |

**Avoidance and the state**

| Variable | Meaning |
|---|---|
| `informal_activity` | Trade in the target outside the legal market (black or grey market). |
| `cross_border_purchases` | Purchases made just outside the jurisdiction. |
| `reclassification` | Reshaping of goods or contracts to fall outside the policy's definitions. |
| `compliance_cost` | Resources spent by those bound to comply. |
| `enforcement_cost` | Resources spent by the state to enforce. |
| `tax_revenue` | Revenue collected. |
| `tax_revenue_vs_static_projection` | Revenue collected compared with a projection that multiplies the rate by the pre-tax base (ignoring responses). |
| `subsidy_share_received` | Share of a subsidy's benefit received by a subgroup, signed relative to the nominal recipients (sellers or asset owners who capture part of it: increase). |
| `disputes_settled_outside_courts` | Share of disputes in a market settled without legal recourse. Any violence used in such settlement is a safety effect and out of scope for version 1. |
| `tax_share_borne` | Share of a tax's burden borne by a subgroup, signed relative to the other subgroups in the same market (increase means it bears more than they do). |
| `lobbying_effort` | Resources spent seeking to change, extend or keep the policy. |
| `resources_available_other_uses` | Resources available to actors for uses outside the target (the "unseen" bucket). |

**Out of scope for version 1.** Health, safety, environmental quality and nutrient intake have no variables. Reports say explicitly that these are not analyzed, rather than leaving them out silently.

## 2.5 Consequence (normal form)

```
consequence:
  id:            C-<n>
  actor_class:   from 2.2
  variable:      from 2.4 (with a named market where needed)
  sign:          increase | decrease | ambiguous
  horizon:       short | medium | long
  visibility:    visible | invisible
  tier:          A | B | J | C
  derivation:    [rule IDs in order]
  assumptions:   [assumption IDs]
  reversal:      what would make the sign flip or the effect vanish
  chains:        for ambiguous consequences, the opposing derivations
  components:    for multi-component policies, which components the chain runs through
  reading:       optional; where a sign depends on how an unclear provision is read,
                 one entry per reading, such as "U1-a: increase; U1-b: ambiguous"
  persistence:   for repeals only: none | partial | full, compared with the path on
                 which the original policy was never imposed (TS-6); may be given per
                 horizon, such as "partial (medium); none (long)"
```

**Group consequences.** Some rules conclude that at least one of several variables moves, without saying which (PC-10's weaker form: employment, hours or non-wage compensation; EN-3; RS-2). Record these as one consequence with the variables listed together and the sign `at_least_one_decrease` or `at_least_one_increase`. It is scored as correct if at least one member moves as predicted and none moves the other way. Writing each variable as its own "decrease" would overclaim.

**Timing shifts.** A response that moves an action in time (RS-8, SB-6) is written as signed consequences per time window, each against the counterfactual ("purchases in the window: increase; in the year after: decrease"). Where there is no counterfactual comparison to make, because without the policy the action would not happen at all, the shift is a note on the path in section 8, not a consequence.

**Readings.** Readings of an unclear provision are not given probabilities (workflow step 10); each reading's sign is reported, and the policy text, not the analyst, decides between them.

Every consequence, including an opportunity cost, is a signed change in a variable from 2.4. There is no separate "loss" entry: a forgone purchase is `resources_available_other_uses` decrease, prevented exchanges are `quantity_traded` decrease, time spent queuing is `wait_time` increase. This keeps every consequence scorable in the same way.

The sign is always relative to the counterfactual (the same place and time without the policy), not to the situation before the policy. "Rents rise more slowly than they would have" is a decrease in `price_paid`, even if rents still rise.

## 2.6 Assumption

```
assumption:
  id:        A-<n>
  text:      plain statement, such as "the cap is enforced against most landlords"
  type:      enforcement | binding | substitutability | mobility | alternative_uses
             | durability | expectations | revenue_use | reversal_cost | other
  p:         probability it holds in this case, 0 to 1, stated before any outcome is known
  evidence:  what the estimate rests on
  if_false:  which consequences fail or reverse
```

## 2.7 Visibility

A consequence is **visible** if it is intended, immediate and concentrated on an identifiable group, so that it is the kind of thing a supporter of the policy would point to. It is **invisible** if it is indirect, delayed, spread thinly over many people, or a forgone alternative. When unsure, ask: would the consequence appear in a news story about the policy's passage? If so, it is visible.

## 2.8 Market relations

Second-order effects travel only along recorded relations between markets.

```
relation:
  from:      good or market
  to:        good or market
  type:      substitute | complement | input_to | same_market_other_segment | across_border
  strength:  close | partial | weak
  source:    evidence for the relation
```

Two relation types need care:
- **Trip complements.** Goods bought on the same shopping trip are complements in where they are bought, even if they are unrelated in use. Record them as `complement` with a note `trip`. RS-9 uses them.
- **Secondary use.** A good that came free with something else and was reused for another end (carryout bags reused as bin liners) is tied to the goods it substituted for in that end. Record as `substitute` with a note `secondary_use`, so that RS-1 applies and the reason is visible.
- **Location ties to other markets.** Holding a good tied to a place (a controlled tenancy) links the holder's housing market to their labor market. Record as `complement` with a note `location`. RS-11 uses them.

Example: `controlled_rental_units` and `uncontrolled_rental_units` are `same_market_other_segment`, `close`. `sweetened_drinks_in_city` and `sweetened_drinks_outside_city` are `across_border`, with strength depending on distance.
