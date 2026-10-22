# ---------------------------------------------------------------- round 2 (depth 2 nodes)
N1 = "The metal imported for goods sold in Vessland falls by more than the metal imported for exports rises."
JUDGED[N1] = (0.75, "other")
for k in ("export_industries", "exporters.domestic_metal#2", "exporters.imported_metal#2", "exporters.table_claimants#2", "general_fund#2",
          "importers.reimport#2", "taxpayers", "workers.export_industries"):
    props[k] = []
# importers#2: the tariff cuts imports for goods sold at home; the drawback and the exporters' own demand raise those for exports
add("importers#2", "dominance", {"actor": "importers", "variable": "quantity_traded", "direction": "decrease", "kind": "empirical"}, [N1],
    source="750,000 t is used in goods sold in Vessland (500,000 t imported); the aluminum content of exports is about 250,000 t, 100,000 t of it imported")
link("importers#2", "reclassification", "substitute", "manufacturers.home", "quantity_supplied", [A(7), A(15)],
     source="Finished goods and parts containing aluminum (...) are exempt (uncovered fabricated forms compete with home fabricators)")
add("sellers.foreign#2", "dominance", {"actor": "sellers.foreign", "variable": "quantity_traded", "direction": "decrease", "kind": "empirical"}, [N1],
    source="The other 600,000 t is imported")

# producers.domestic
link("producers.domestic", "quantity_supplied", "input", "workers.smelters", "employment,hours_worked", [],
     source="Two domestic smelters ... with about 3,800 employees")
link("producers.domestic", "quantity_supplied", "input", "input_suppliers.electricity", "quantity_demanded", [],
     source="electricity is about 35% of their cost and is bought from the state grid")
link("producers.domestic", "net_price_received", "same_act", "manufacturers.home", "price_paid", [A(1)],
     source="About 1,200 firms use aluminum (...); 750,000 t is used in goods sold in Vessland (500,000 t imported, 250,000 t domestic)")
link("producers.domestic", "net_price_received", "same_act", "exporters.domestic_metal", "price_paid", [A(1)],
     source="150,000 t domestic metal in the aluminum content of exports")
link("producers.domestic", "net_price_received", "yield", "owners.smelters", "asset_value", [A(12)],
     source="The tariff expires on 31 August 2031 unless Parliament extends it after a review in 2030")
link("producers.domestic", "net_price_received", "yield", "producers.domestic", "investment_target", [A(19)],
     source="Two domestic smelters, with a combined capacity of 470,000 t ... produce about 400,000 t (85% of capacity)")
add("producers.domestic", "stakes", {"component": "k1", "actor": "producers.domestic"}, [A(11)],
    source="The tariff expires on 31 August 2031 unless Parliament extends it after a review in 2030")

# producers.secondary: scrap
link("producers.secondary", "quantity_supplied", "supply_price", "sellers.scrap", "net_price_received", [A(6)],
     source="Secondary producers (remelters) make about 120,000 t a year from scrap, and Vessland exports about 60,000 t of scrap")
