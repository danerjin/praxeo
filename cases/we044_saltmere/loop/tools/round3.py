# ===================================================================== round 3
for _n in ("officials.enforcement#2", "general_fund#3", "owners.elsdon#2", "owners.occupant#2", "owners.primary_residence#3", "renters",
           "retailers.elsdon", "retailers.neighbors#2", "workers.hotels", "workers.retail"):
    PROPS.setdefault(_n, [])

link("landlords.elsdon", "quantity_supplied", "supply", "renters.elsdon", "price_paid", [], src="Some Elsdon owners move units from long-term leases into STR")
n = "sellers.hotels#2"
link(n, "net_price_received", "yield", "sellers.hotels", "return_on_capital", [], src="average daily rate $180")
link(n, "return_on_capital", "yield", "sellers.hotels", "asset_value", ["a30"], src="Values of STR units, hotels and Elsdon homes rest on expected yields")
link(n, "return_on_capital", "yield", "sellers.hotels", "capital_stock_target", ["a25"], horizon="long", src="Hotel construction takes three to five years from site to opening")
