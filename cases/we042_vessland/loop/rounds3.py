# ---------------------------------------------------------------- round 3 (depth 3 nodes; the loop stops after this)
for k in ("importers#3", "input_suppliers.electricity", "owners.smelters", "producers.domestic#2", "sellers.foreign#3", "sellers.scrap",
          "workers.smelters"):
    props[k] = []

# manufacturers.home: users who sell in Vessland, now paying import parity for domestic metal
link("manufacturers.home", "price_paid", "cost", "manufacturers.home", "quantity_supplied", [A(15)],
     source="Buyers of uncovered finished goods can buy tariff-free imports; Finished goods and parts containing aluminum are exempt")
link("manufacturers.home", "price_paid", "cost", "owners.manufacturers", "asset_value", [A(12), A(15)],
     source="home fabricators' capital is specific; The tariff expires on 31 August 2031")
link("manufacturers.home", "quantity_supplied", "substitute", "buyers.substitutes", "quantity_substitute", [A(15)],
     source="About 1,200 firms use aluminum (...); 750,000 t is used in goods sold in Vessland")
link("manufacturers.home", "quantity_supplied", "input", "workers.manufacturers", "employment,hours_worked", [],
     source="About 1,200 firms use aluminum ..., employing about 60,000 people")
link("manufacturers.home", "price_paid", "output", "buyers", "price_paid", [A(16)],
     source="Some aluminum goods have no close imported substitute")
link("manufacturers.home", "quantity_supplied", "supply", "buyers", "price_paid", [A(27)],
     source="Machined and stamped parts are cut from plate and billet")
add("manufacturers.home", "alternatives", {"component": "k1", "chooser": "manufacturers.home", "actor": "export_industries",
                                           "variables": ["quantity_supplied"]}, [A(8)],
    source="K2 pays on goods ... exported; mixed fabricators and makers of parts sell at world prices")
add("manufacturers.home", "alternatives", {"component": "k1", "chooser": "manufacturers.home", "actor": "manufacturers.home",
                                           "variables": ["investment_target"], "inverse": True}, [A(23)],
    source="Vessland's main industrial region lies 30 to 60 km from the border with Ostrel, which has no tariff on aluminum")
add("manufacturers.home", "stakes", {"component": "k1", "actor": "manufacturers.home"}, [A(11)],
    source="About 1,200 firms use aluminum")

# export_industries#2: the exchange-rate chain (fewer imports) against the shift of mixed fabricators' sales to exports
add("export_industries#2", "dominance", {"actor": "export_industries", "variable": "quantity_supplied", "direction": "increase", "kind": "empirical"},
    [A(29)], source="K2 refunds 99% of the tariff on exported goods; home sales bear about $500 a tonne of metal")

# exporters.domestic_metal#3: under U1-a the domestic-metal exporter, now paying parity for domestic metal, can use traced imported metal
add("exporters.domestic_metal#3", "alternatives", {"component": "k1", "chooser": "exporters.domestic_metal", "actor": "importers",
                                                   "variables": ["quantity_traded"], "reading": "U1-a"}, [A(20)],
    source="U1-a (direct identification): the claimant must show that the metal on which the tariff was paid ... went into the exported goods")
