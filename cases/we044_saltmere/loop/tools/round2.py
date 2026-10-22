# ===================================================================== round 2
for _n in ("officials.enforcement", "buyers.mid_term", "buyers.short_stay#2", "homebuyers", "homeowners", "input_suppliers.cleaning",
           "owners.mid_term", "owners.non_primary#2", "owners.over_90_nights#2", "owners.primary_residence#2", "owners.two_unit#2",
           "owners.two_unit_over_90#2", "platforms#2"):
    PROPS.setdefault(_n, [])

link("general_fund#2", "tax_revenue", "paid_into", "general_fund", "fund_balance", [], src="fines go to the general fund")
link("landlords.long_term", "quantity_supplied", "supply", "renters", "price_paid", ["a13"], src="about 60,000 are rented long-term (median rent $1,850 a month, vacancy about 3%)")
link("landlords.long_term", "quantity_supplied", "complement", "retailers.neighbors", "quantity_traded", ["a33"], src="Residents of units moved to 12-month leases buy some meals and goods near home")
n = "owners.elsdon"
link(n, "quantity_traded", "substitute", "landlords.elsdon", "quantity_supplied", ["a29"], src="the town of Elsdon ... has about 420 STR listings and no rules beyond county registration")
link(n, "quantity_traded", "yield", "owners.elsdon", "asset_value", ["a30"], src="Values of STR units, hotels and Elsdon homes rest on expected yields")
link(n, "quantity_traded", "complement", "retailers.elsdon", "quantity_traded", ["a12"], src="Visitors buy meals and goods near their lodging")
for n in ("owners.occupant", "owners.primary_residence#2"):
    base = n.split("#")[0]
    link(n, "quantity_traded", "supply_price", base, "net_price_received", ["a35"], src="owners must be present; the 90-night cap")
    link(n, "net_price_received", "yield", base, "quantity_supplied", ["a36"], src="Some owner-occupiers have rooms or nights they would let at a higher nightly price")
link("retailers.neighbors", "quantity_traded", "input", "workers.retail", "employment,hours_worked", [], src="Visitors buy meals and goods near their lodging")
n = "sellers.hotels"
link(n, "quantity_traded", "supply_price", "sellers.hotels", "net_price_received", ["a9"], src="Hotels: about 7,400 rooms, average occupancy 79% (94% in July and August); construction takes three to five years")
link(n, "quantity_traded", "complement", "general_fund", "tax_revenue", [], src="R2 Transient occupancy tax (TOT) of 12% on stays under 30 nights, hotels and STRs alike ... about $46 million from hotels")
link(n, "quantity_traded", "input", "workers.hotels", "employment,hours_worked", [], src="Hotels: about 7,400 rooms")
stake(n, "k1", ["a14"], src="Hosts, platforms, hotels and neighborhood associations can organize at a cost below their stake")
