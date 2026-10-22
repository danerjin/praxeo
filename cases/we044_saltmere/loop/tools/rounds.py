def alt(node, comp, actor, vars_, prem, chooser=None, inverse=False, src=None):
    f = {"component": comp, "chooser": chooser or node.split("#")[0], "actor": actor, "variables": vars_}
    if inverse:
        f["inverse"] = True
    add(node, "alternatives", f, prem, src)


def link(node, var, rel, actor, v, prem=(), horizon=None, src=None):
    f = {"source_actor": node.split("#")[0], "source_variable": var, "relation": rel, "actor": actor, "variable": v}
    if horizon:
        f["horizon"] = horizon
    add(node, "links", f, prem, src)


def outside(node, ex, actor, v, prem, src=None):
    add(node, "margins", {"exchange": ex, "kind": "outside", "actor": actor, "variables": [v]}, prem, src)


def stake(node, comp, prem, src=None):
    add(node, "stakes", {"component": comp, "actor": node.split("#")[0]}, prem, src)


def timing(node, comp, v, mode, prem, src=None):
    add(node, "timing", {"component": comp, "actor": node.split("#")[0], "variable": v, "mode": mode}, prem, src)


def asset(node, ex, side, prem, src=None):
    add(node, "assets", {"exchange": ex, "side": side, "actor": node.split("#")[0]}, prem, src)


def yld(node, ex, side, prem, src=None):
    add(node, "yields", {"exchange": ex, "side": side, "actor": node.split("#")[0]}, prem, src)


# ===================================================================== round 1
S_BAN = "From 1 July 2027, no whole unit may be let for under 30 nights unless it is the owner's primary residence"
S_ANN = "Introduced 3 November 2026 by six of nine council members (announced). Enacted 8 December 2026. Effective 1 July 2027"

# ---- guests: the buyers of the banned and capped lets
n = "buyers.short_stay"
alt(n, "k1", "sellers.hotels", ["quantity_traded"], ["a8"], src="Hotels: about 7,400 rooms ... average daily rate $180")
alt(n, "k1", "owners.elsdon", ["quantity_traded"], ["a10", "a39"], src="the town of Elsdon, 12 km from the Harbor district, has about 420 STR listings and no rules beyond county registration")
alt(n, "k1", "buyers.mid_term", ["quantity_demanded"], ["a31"], src="Furnished lets of 30 nights or more ... are a small segment of about 900 units")
alt(n, "k1", "owners.occupant", ["quantity_traded"], ["a32"], src="Rooms in a home where the owner lives and is present ... Not covered by K1")
alt(n, "k1", "owners.primary_residence", ["quantity_traded"], ["a32"], src="Whole units, the owner's primary residence, let while the owner is away")
alt(n, "k1", "buyers.short_stay", ["trips"], ["a11"], inverse=True, src="the old price")
outside(n, "e1", "buyers.short_stay", "informal_activity", ["a4"], src="Some guests keep wanting whole units in Saltmere enough to book them directly")
timing(n, "k1", "quantity_traded", "bring_forward", ["a17"], src=S_ANN)
timing(n, "k1", "quantity_demanded", "bring_forward", ["a15"], src="Stays booked and confirmed before 1 July 2027 may be completed if they end by 30 September 2027")
link(n, "trips", "complement", "retailers.neighbors", "quantity_traded", ["a12"], src="Visitors buy meals and goods near their lodging")

# ---- owners of non-primary units: the sellers whose lets are banned
n = "owners.non_primary"
alt(n, "k1", "landlords.long_term", ["quantity_supplied"], ["a5"], src="The same unit let on a 12-month lease earns about $24,000 gross, about $20,000 net")
alt(n, "k1", "owners.mid_term", ["quantity_supplied"], ["a7"], src="Furnished lets of 30 nights or more (traveling nurses, university visitors, relocations)")
alt(n, "k1", "owners.non_primary", ["units_held_vacant"], ["a6"], src="about 450 second homes the owner uses some weeks a year")
alt(n, "k1", "owners.non_primary", ["turnover"], ["a37"], src="Whole units, not the owner's primary residence")
alt(n, "k1", "owners.non_primary", ["reclassification"], ["a38"], src="Primary residence: the dwelling in which the owner resides at least 270 days a year")
alt(n, "k1", "owners.primary_residence", ["number_of_sellers"], ["a38"], src="registered under K3 ... with proof of residence (driver's license, voter registration, homestead tax exemption)")
outside(n, "e1", "owners.non_primary", "informal_activity", ["a3"], src="K4: on complaint only; no proactive inspection")
outside(n, "e1", "owners.non_primary", "allocation_by_non_price_criteria", ["a27", "a3"], src="K4: on complaint only; no proactive inspection")
stake(n, "k1", ["a14"], src="neighborhood associations, hosts, platforms, hotels")
timing(n, "k1", "quantity_supplied", "carry_over", ["a16"], src="the August-September leasing season")
asset(n, "e1", "seller", ["a30"], src="In 2023 to 2025, about 30% of home purchases in the beach districts were by buyers who did not occupy the home")
yld(n, "e1", "seller", ["a1"], src="A whole-unit STR earns on average $235 a night at 60% occupancy, about $51,000 a year gross")
link(n, "quantity_traded", "complement", "input_suppliers.cleaning", "employment,hours_worked", ["a26"], src="after cleaning, platform fees, furnishing and management (about 40% of gross)")
link(n, "quantity_traded", "complement", "officials.enforcement", "enforcement_cost", ["a18"], src="about 1,500 of them about STR units (about one a year for every two whole-unit listings), at about 2.5 staff hours each")
link(n, "quantity_traded", "complement", "general_fund", "tax_revenue", [], src="R2 Transient occupancy tax (TOT) of 12% on stays under 30 nights ... about $18.7 million a year from whole-unit STRs")
link(n, "quantity_traded", "complement", "general_fund", "non_tax_receipts", ["a34"], src="R1 STR registration ($150 a year; about 65% of hosts registered) ... Replaces R1 for whole units")
link(n, "quantity_traded", "substitute", "homeowners", "asset_value", ["a23"], src="about 30% of home purchases in the beach districts were by buyers who did not occupy the home")
link(n, "asset_value", "yield", "homeowners", "asset_value", ["a21"], src="about 30% of home purchases in the beach districts were by buyers who did not occupy the home")
link(n, "turnover", "supply", "homebuyers", "price_paid", ["a37"], src="Whole units, not the owner's primary residence")

# ---- hosts of primary residences: registration under K3 and the 90-night cap
n = "owners.primary_residence"
outside(n, "e2", "owners.primary_residence", "informal_activity", ["a3", "a4"], src="Registration $250 a year, with proof of residence")

# ---- hosts who would let beyond the cap
n = "owners.over_90_nights"
alt(n, "k1_cap", "owners.over_90_nights", ["legal_breach"], ["a22"], src="report nights booked per registration number each quarter")
outside(n, "e2", "owners.over_90_nights", "informal_activity", ["a3"], src="K4: on complaint only; no proactive inspection")
n = "owners.two_unit_over_90"
alt(n, "k1_cap_u1a", "owners.two_unit_over_90", ["legal_breach"], ["a22"], src="report nights booked per registration number each quarter")
outside(n, "e3", "owners.two_unit_over_90", "informal_activity", ["a3"], src="K4: on complaint only; no proactive inspection")

# ---- hosts in two-unit buildings (U1)
n = "owners.two_unit"
alt(n, "k1_ban_u1b", "landlords.long_term", ["quantity_supplied"], ["a5"], src="U1-b: the dwelling is the unit ... may not be let for under 30 nights at all")
alt(n, "k1_ban_u1b", "owners.mid_term", ["quantity_supplied"], ["a7"], src="Lets of 30 nights or more")
outside(n, "e3", "owners.two_unit", "informal_activity", ["a3"], src="K4: on complaint only; no proactive inspection")

# ---- platforms
n = "platforms"
stake(n, "k1", ["a14"], src="Hosts, platforms, hotels and neighborhood associations can organize at a cost below their stake")

# ---- the city
link("general_fund", "non_tax_receipts", "paid_into", "general_fund", "fund_balance", ["a20"], src="fines go to the general fund")
link("officials.registry", "enforcement_cost", "paid_from", "general_fund", "fund_balance", ["a20"], src="K3: a new Registry Unit of five staff, $520,000 a year, new appropriation from the general fund")
