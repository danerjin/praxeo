import json
p = "cases/we064_tarnesse/loop_r2/rounds/r3.json"
d = json.load(open(p))
d["input_suppliers.towers#2"] = [{"part": "links", "fact": {"source_actor": "input_suppliers.towers", "source_variable": "quantity_demanded", "relation": "input", "actor": "workers.riggers", "variable": "employment"}, "premises": [], "source": "About 1,400 certified tower riggers do about 3,000 site installations a year ... 4,000 to 5,000 a year, beside the existing 3,000."}]
d["workers.riggers"][0]["fact"]["source_variable"] = "employment"
json.dump(d, open(p, "w"), indent=1)
