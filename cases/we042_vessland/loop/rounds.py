# ---------------------------------------------------------------- round 1 (depth 1 nodes)
IMP = "Imports of unwrought aluminum and semi-finished products"
# importers
add("importers", "alternatives", {"component": "k1", "chooser": "importers", "actor": "importers", "variables": ["reclassification"]},
    [A(7)], source="Finished goods and parts containing aluminum (...) are exempt; K1 targets only unwrought and semi-finished forms")
add("importers", "timing", {"component": "k1", "actor": "importers", "variable": "quantity_traded", "mode": "bring_forward"},
    [A(21)], source="The trade minister announced the measure on 3 February 2027 ... it applies to aluminum entered on or after 1 September 2027")
link("importers", "price_paid", "substitute", "producers.domestic", "net_price_received", [A(1)],
     source="Two domestic smelters ... produce about 400,000 t; the other 600,000 t is imported (domestic price at import parity)")
link("importers", "price_paid", "substitute", "producers.domestic", "quantity_supplied", [A(4)],
     source="produce about 400,000 t (85% of capacity)")
link("importers", "price_paid", "substitute", "producers.secondary", "quantity_supplied", [A(5)],
     source="Secondary producers (remelters) make about 120,000 t a year from scrap")
link("importers", "quantity_traded", "same_act", "sellers.foreign", "quantity_traded", [],
     source="The other 600,000 t is imported")
link("importers", "quantity_traded", "currency", "export_industries", "quantity_supplied", [A(13)],
     source="Vessland ... with its own currency, the crown, and a floating exchange rate")

# sellers.foreign, sellers.reexport, buyers.foreign, officials.revenue: nothing the policy text lets me propose
props["sellers.foreign"] = []
props["sellers.reexport"] = []
props["buyers.foreign"] = []
props["officials.revenue"] = []

# importers.reimport
add("importers.reimport", "margins", {"exchange": "e_reimp", "kind": "outside", "actor": "importers.reimport", "variables": ["informal_activity"]},
    [A(9), A(10)], source="undeclared re-imports found on audit repay it plus 20%")

# exporters using imported metal
for ex in ("exporters.imported_metal", "exporters.table_claimants"):
    link(ex, "quantity_traded", "input", "workers.export_industries", "employment,hours_worked", [],
         source="The aluminum content of their exports is about 250,000 t a year")
    link(ex, "quantity_traded", "input", "importers", "quantity_traded", [],
         source="about 100,000 t of it imported metal")
    add(ex, "stakes", {"component": "k2", "actor": ex}, [A(11)], source="K2 Drawback: Refund of K1, conditional on export")
    add(ex, "parts", {"part": ex, "whole": "export_industries"}, [], source="employing about 60,000 people ... exports")
    add(ex, "dominance", {"actor": ex, "variable": "resources_available_other_uses", "direction": "increase", "kind": "empirical"},
        [A(26)], source="99% of the tariff paid on the aluminum used in manufacturing the exported goods")
link("exporters.imported_metal", "quantity_traded", "same_act", "exporters.imported_metal", "legal_breach", [A(25)],
     source="count process scrap as used (for machined parts, 1.35 t of metal per tonne of product)")
link("exporters.table_claimants", "quantity_traded", "same_act", "exporters.table_claimants", "legal_breach", [A(25)],
     source="count process scrap as used (for machined parts, 1.35 t of metal per tonne of product)")

# exporters using domestic metal (their grant exists only under U1-b)
link("exporters.domestic_metal", "quantity_traded", "input", "workers.export_industries", "employment,hours_worked", [],
     source="U1-b ... domestic metal can stand in for imported metal; exports with 150,000 t domestic metal")
link("exporters.domestic_metal", "quantity_traded", "input", "producers.domestic", "quantity_supplied", [A(4)],
     source="150,000 t domestic metal in exports; The smelters ... produce about 400,000 t (85% of capacity)")
add("exporters.domestic_metal", "stakes", {"component": "k2b", "actor": "exporters.domestic_metal"}, [A(11)],
    source="Customs has not issued guidance and no court has ruled")
add("exporters.domestic_metal", "parts", {"part": "exporters.domestic_metal", "whole": "export_industries"}, [],
    source="employing about 60,000 people ... exports")

# general fund
link("general_fund", "tax_revenue", "paid_into", "general_fund", "fund_balance", [],
     source="Tariff receipts go to the general fund")
link("general_fund", "subsidy_outlay", "paid_from", "general_fund", "fund_balance", [],
     source="drawback is paid out of them")
add("general_fund", "dominance", {"actor": "general_fund", "variable": "fund_balance", "direction": "increase", "kind": "arithmetic"},
    [A(3)], source="600,000 t x $500 = $300 million a year, less drawback of at most about 250,000 t x $495 = $124 million")
link("general_fund", "fund_balance", "same_act", "taxpayers", "resources_available_other_uses", [A(24)],
     source="Tariff receipts go to the general fund")

