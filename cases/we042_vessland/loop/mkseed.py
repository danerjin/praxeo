import json
T = {
 "a1": ("Imports remain a material share of supply, so the domestic price is set at import parity.", "binding", 0.9),
 "a2": ("Most covered imports pay the tariff; misdeclaration is limited.", "enforcement", 0.85),
 "a14": ("Foreign smelters have far better alternatives than Vessland's users.", "substitutability", 0.9),
 "a17": ("Customs' appropriation does not rise with the new work.", "revenue_use", 0.8),
 "a18": ("Vessland's purchases are large enough to lower the world price.", "other", 0.15),
 "a21": ("Users expect the tariff and can import and store metal ahead of 1 September at a cost below $500 a tonne.", "expectations", 0.8),
 "a22": ("Some home users keep buying covered aluminum at the higher price.", "other", 0.95),
 "a26": ("Exporters with qualifying content file claims; for most, the paperwork costs less than the refund.", "other", 0.9),
 "a28": ("Some claimants' actual metal use per tonne of exported product is below Customs' yield tables, so they claim by the tables, as K2 allows at their option.", "other", 0.6),
}
s = {
 "name": "WE-042 aluminum tariff with drawback (expand loop)",
 "exchanges": [
  {"id": "e_imp", "buyer": "importers", "seller": "sellers.foreign", "buyer_price_var": "price_paid", "seller_price_var": "net_price_received"},
  {"id": "e_exp", "buyer": "buyers.foreign", "seller": "exporters.imported_metal", "seller_price_var": "net_price_received"},
  {"id": "e_exp_tab", "buyer": "buyers.foreign", "seller": "exporters.table_claimants", "seller_price_var": "net_price_received"},
  {"id": "e_exp_dom", "buyer": "buyers.foreign", "seller": "exporters.domestic_metal", "seller_price_var": "net_price_received"},
  {"id": "e_reimp", "buyer": "importers.reimport", "seller": "sellers.reexport", "buyer_price_var": "price_paid"},
 ],
 "charges": [
  {"component": "k1", "premises": ["a1", "a2", "a22"], "exchange": "e_imp", "payer_side": "buyer", "receiver": "general_fund",
   "receipt_variable": "tax_revenue", "projection_variable": "tax_revenue_vs_static_projection"},
  {"component": "k3", "exchange": "e_reimp", "payer_side": "buyer", "receiver": "general_fund", "receipt_variable": "tax_revenue"},
 ],
 "moves": [
  {"exchange": "e_imp", "side": "buyer", "premises": ["a14"]},
  {"exchange": "e_imp", "side": "seller", "premises": ["a18"]},
 ],
 "incidence": [{"component": "k1", "exchange": "e_imp", "side": "buyer", "premises": ["a14"]}],
 "grants": [
  {"component": "k2", "premises": ["a26"], "exchange": "e_exp", "recipient_side": "seller", "payer": "general_fund"},
  {"component": "k2", "premises": ["a26", "a28"], "exchange": "e_exp_tab", "recipient_side": "seller", "payer": "general_fund"},
  {"component": "k2b", "premises": ["a26"], "exchange": "e_exp_dom", "recipient_side": "seller", "payer": "general_fund"},
 ],
 "unclear": [{"id": "U1", "text": "K2 pays on goods made \"using imported aluminum on which the tariff was paid\".",
   "readings": ["U1-a: direct identification: the claimant must show that the metal on which the tariff was paid, or metal traced to it by lot, went into the exported goods",
                "U1-b: substitution: aluminum of the same grade used in the exported goods within three years of an import qualifies against that import's entry, whatever its origin, so domestic metal can stand in for imported metal"],
   "components": {"U1-a": [], "U1-b": ["k2b"]}}],
 "announced": [{"component": "k1", "premises": ["a21"]}],
 "compliance": [{"component": "k1", "actor": "importers"}, {"component": "k2", "actor": "exporters.imported_metal"},
                {"component": "k2", "actor": "exporters.table_claimants"}, {"component": "k2b", "actor": "exporters.domestic_metal"},
                {"component": "k3", "actor": "importers.reimport"}],
 "enforcers": [{"component": c, "actor": "officials.revenue"} for c in ("k1", "k2", "k2b", "k3")],
 "fixed_budget": [{"component": c, "actor": "officials.revenue", "premises": ["a17"]} for c in ("k1", "k2", "k2b", "k3")],
 "assumptions": {k: {"text": t, "class": c, "p": p} for k, (t, c, p) in T.items()},
}
json.dump(s, open("cases/we042_vessland/loop/seed.json", "w"), indent=1)
