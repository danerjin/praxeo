import json
T={ "a1":("For most non-primary units, short lets yield more than any lawful alternative (about $30,000 net against about $20,000).","binding",0.9),
"a2":("Platforms comply with K2: they display numbers, remove listings on notice and report nights.","enforcement",0.85),
"a20":("The $520,000 is new general-fund money.","revenue_use",0.9),
"a30":("Values of STR units, hotels and Elsdon homes rest on expected yields, and passage was likely from the introduction (six of nine sponsors).","expectations",0.8),
"j1":("Some primary-residence hosts would let more than 90 nights a year, so the 90-night cap binds on them.","binding",0.95),
"j2":("Some hosts in two-unit buildings would let more than 90 nights a year, so the 90-night cap binds on them.","binding",0.95),
"j3":("Code Enforcement takes K1 complaints within its existing fixed budget, with no new appropriation.","revenue_use",0.9)}
s={"name":"WE-044 Saltmere short-term rental ordinance (loop)",
"exchanges":[
{"id":"e1","buyer":"buyers.short_stay","seller":"owners.non_primary","buyer_price_var":"price_paid","seller_price_var":"net_price_received"},
{"id":"e2","buyer":"buyers.short_stay","seller":"owners.primary_residence","unsatisfied_seller":"owners.over_90_nights","buyer_price_var":"price_paid","seller_price_var":"net_price_received"},
{"id":"e3","buyer":"buyers.short_stay","seller":"owners.two_unit","unsatisfied_seller":"owners.two_unit_over_90","buyer_price_var":"price_paid","seller_price_var":"net_price_received"}],
"banned":[{"component":"k1","exchange":"e1","premises":["a1","a2"]},
{"component":"k1_ban_u1b","exchange":"e3","premises":["a1","a2"]}],
"capped":[{"component":"k1_cap","exchange":"e2","premises":["j1","a2"]},
{"component":"k1_cap_u1a","exchange":"e3","premises":["j2","a2"]}],
"charges":[
{"component":"k3","exchange":"e2","payer_side":"seller","receiver":"general_fund","receipt_variable":"non_tax_receipts","basis":"operating","premises":["a2"]},
{"component":"k3_u1a","exchange":"e3","payer_side":"seller","receiver":"general_fund","receipt_variable":"non_tax_receipts","basis":"operating","premises":["a2"]}],
"unclear":[{"id":"U1","text":"Whether K1's exception for the dwelling in which the owner resides covers the second unit of a two-unit building whose owner lives in the other unit.",
"readings":["U1-a: the dwelling is the building, so the second unit is part of the primary residence and may be let up to 90 nights a year, with registration",
"U1-b: the dwelling is the unit, so the second unit is not the owner's primary residence and may not be let for under 30 nights"],
"components":{"U1-a":["k1_cap_u1a","k3_u1a"],"U1-b":["k1_ban_u1b"]}}],
"announced":[{"component":"k1","premises":["a30"]}],
"compliance":[{"component":"k2","actor":"platforms"},{"component":"k3","actor":"owners.primary_residence"}],
"enforcers":[{"component":"k2","actor":"officials.registry"},{"component":"k3","actor":"officials.registry"},{"component":"k4","actor":"officials.enforcement"}],
"funded":[{"component":"k3","actor":"general_fund","premises":["a20"]}],
"fixed_budget":[{"component":"k4","actor":"officials.enforcement","premises":["j3"]}],
"assumptions":{k:{"text":v[0],"class":v[1],"p":v[2]} for k,v in T.items()}}
json.dump(s,open("seed.json","w"),indent=1)
