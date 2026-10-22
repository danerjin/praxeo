"""Builds proposals.json and answers.json (the proposer's and decider's stand-in output), round by round."""
import json
from pathlib import Path

HERE = Path(__file__).parent
T = {  # statement texts: the assumption table's wording where a statement matches an assumption
 "A3": ("Some owners prefer independent or self repair at the new terms.", "substitutability", 0.9),
 "A4": ("Dealers' and authorized providers' repair capacity cannot contract at once.", "durability", 0.75),
 "A5": ("Independent shops can open or expand once inputs are available.", "mobility", 0.75),
 "A7": ("Some repairs can be deferred for months.", "other", 0.6),
 "A8": ("Phone makers extend their parts and tool programs to owners in all states rather than only Kestrava.", "other", 0.6),
 "A9": ("Some compact tractors can be designed and marketed for grounds care at a cost below the burden of coverage.", "other", 0.55),
 "A12": ("Investors value makers' expected repair-input margins in Kestrava.", "other", 0.85),
 "A14": ("More repairers and self-repair shorten waits at harvest.", "other", 0.75),
 "A15": ("Some buyers of used phones check the part notices and pay less for phones with unpaired parts.", "other", 0.6),
 "A16": ("Owners could not read fault codes or documentation before, and some use them to diagnose or to shop for repairs.", "other", 0.85),
 "A19": ("Dealers' capital and locations are tied to their territory, while makers sell in many states at national prices.", "mobility", 0.75),
 "A20": ("Makers, dealers and investors expect the Act to stay in force.", "expectations", 0.8),
 "A21": ("Salvaged and non-genuine parts compete with makers' genuine parts once independents can buy both.", "substitutability", 0.6),
 "A23": ("Makers, dealers, farm groups and repair associations can organize at a cost below their stakes.", "other", 0.85),
 "A24": ("Some makers respond by integrating components or (under U1-b) by pairing more parts, to keep control of which parts work.", "other", 0.55),
 "A25": ("For each maker, the lost margin on repair inputs, the voided terms and the costs of compliance outweigh any gain from every rival being bound at once and from buyers' higher valuation of covered units.", "other", 0.7),
 # statements with no matching assumption: judged from section 1
 "J1": ("Some farms near the state line buy new equipment from Darnholt dealers when Kestrava prices rise.", "substitutability", 0.7),
}


def P(part, fact, prem=(), src=None):
    return {"part": part, "fact": fact, "premises": [T[k][0] for k in prem],
            "premise_class": T[prem[0]][1] if prem else "other", "source": src}


def alt(comp, ch, actor, vars_, prem, src, **kw):
    return P("alternatives", {"component": comp, "chooser": ch, "actor": actor, "variables": vars_, **kw}, prem, src)


def link(sa, sv, rel, a, v, prem, src, **kw):
    return P("links", {"source_actor": sa, "source_variable": sv, "relation": rel, "actor": a, "variable": v, **kw}, prem, src)


def stake(comp, actor, src):
    return P("stakes", {"component": comp, "actor": actor}, ["A23"], src)


R1 = {
 "repair_shops.independent_farm": [
  link("repair_shops.independent_farm", "quantity_traded", "input", "repair_shops.independent_farm", "quantity_supplied", ["A5"],
       "Independents can buy many mechanical parts at list from dealers but cannot buy the software, without which many electronic parts cannot be calibrated or paired."),
  link("repair_shops.independent_farm", "quantity_supplied", "yield", "repair_shops.independent_farm", "entry_rate", ["A5"],
       "about 260 independent shops repair farm equipment"),
  link("repair_shops.independent_farm", "quantity_supplied", "substitute", "distributors.farm_equipment", "quantity_demanded", ["A3"],
       "dealers' service revenue ... $190 million labor at about $165 an hour; independents charge about $95"),
  stake("k1", "repair_shops.independent_farm", "Similar bills were introduced in Kestrava in 2023 and 2025 and failed after campaigns on both sides."),
 ],
 "repair_shops.independent_phone": [
  link("repair_shops.independent_phone", "quantity_traded", "input", "repair_shops.independent_phone", "quantity_supplied", ["A5"],
       "about 40% by some 900 independent shops using non-genuine or salvaged parts (about $160)"),
  link("repair_shops.independent_phone", "quantity_supplied", "yield", "repair_shops.independent_phone", "entry_rate", ["A5"],
       "some 900 independent shops"),
  link("repair_shops.independent_phone", "quantity_supplied", "substitute", "repair_shops.authorized_phone", "quantity_demanded", ["A3"],
       "about 60% by makers' stores and authorized providers (a screen repair with a genuine part costs about $280)"),
  link("repair_shops.independent_phone", "quantity_traded", "substitute", "sellers.substitutes", "quantity_substitute", ["A21"],
       "independents using non-genuine or salvaged parts"),
  stake("k1", "repair_shops.independent_phone", "Similar bills were introduced in Kestrava in 2023 and 2025 and failed after campaigns on both sides."),
 ],
 "growers": [
  alt("k1", "growers", "distributors.farm_equipment", ["quantity_demanded"], ["A3"],
      "Independents can buy many mechanical parts at list from dealers but cannot buy the software"),
  link("growers", "quantity_traded", "input", "growers", "home_production", ["A3", "A16"],
       "a term of every sale of covered equipment, owed to the owner and to any independent repair provider: parts, tools, documentation and diagnostic software"),
  P("timing", {"component": "k1", "actor": "growers", "variable": "quantity_demanded", "mode": "bring_forward"}, ["A7"],
    "The bill passed the legislature on 18 February 2027 and was signed on 1 March 2027; it takes effect on 1 September 2028 (18 months)."),
  stake("k1", "growers", "Similar bills were introduced in Kestrava in 2023 and 2025 and failed after campaigns on both sides."),
 ],
 "owners.phones": [
  alt("k1", "owners.phones", "repair_shops.authorized_phone", ["quantity_demanded"], ["A3"],
      "about 60% by makers' stores and authorized providers (a screen repair with a genuine part costs about $280)"),
  link("owners.phones", "quantity_traded", "input", "owners.phones", "home_production", ["A3", "A16"],
       "One maker already sells genuine parts and rents tools to owners in all states at the prices its authorized providers pay"),
  P("timing", {"component": "k1", "actor": "owners.phones", "variable": "quantity_demanded", "mode": "bring_forward"}, ["A7"],
    "it takes effect on 1 September 2028 (18 months)"),
 ],
 "growers.new_buyers": [
  alt("k1_term", "growers.new_buyers", "growers.near_border", ["cross_border_purchases"], ["J1"],
      "about 3,000 farms lie within 30 km of the state line, and six farm equipment dealers operate on the Darnholt side within 30 km of it"),
  P("dominance", {"actor": "growers.new_buyers", "variable": "quantity_traded", "direction": "decrease", "kind": "empirical"}, ["A25"],
    "'On fair and reasonable terms', defined in §2(d) as terms no less favorable than the most favorable terms on which the manufacturer offers the item to an authorized repair provider"),
 ],
 "buyers.new_phones": [
  P("dominance", {"actor": "buyers.new_phones", "variable": "quantity_traded", "direction": "decrease", "kind": "empirical"}, ["A25"],
    "§2(d) 'on fair and reasonable terms'"),
 ],
 "manufacturers.farm": [
  alt("k1", "manufacturers.farm", "manufacturers.farm", ["reclassification"], ["A9"],
      "agricultural equipment designed primarily for agricultural use and containing electronic controls"),
  alt("k1", "manufacturers.farm", "manufacturers.farm", ["product_attribute"], ["A24"],
      "§5(c): A manufacturer shall not use a software lock to prevent the functioning of a part supplied, repaired or replaced in accordance with this Act."),
  P("assets", {"exchange": "e3", "side": "seller", "actor": "manufacturers.farm"}, ["A12", "A20"],
    "Dealers' service revenue is about $520 million a year ($330 million parts ...); no expiry"),
  P("yields", {"exchange": "e3", "side": "seller", "actor": "manufacturers.farm"}, ["A12"],
    "Dealers ... buy parts at 25% below list."),
  stake("k1", "manufacturers.farm", "Similar bills were introduced in Kestrava in 2023 and 2025 and failed after campaigns on both sides."),
  stake("k2", "manufacturers.farm", "Similar bills were introduced in Kestrava in 2023 and 2025 and failed after campaigns on both sides."),
 ],
 "manufacturers.phone": [
  alt("k1", "manufacturers.phone", "manufacturers.phone", ["quantity_supplied"], ["A8"],
      "One maker already sells genuine parts and rents tools to owners in all states at the prices its authorized providers pay; makers sell ... at the same prices in every state"),
  alt("k1", "manufacturers.phone", "manufacturers.phone", ["product_attribute"], ["A24"],
      "On recent models makers pair screens, batteries and cameras to the device"),
  P("assets", {"exchange": "e1", "side": "seller", "actor": "manufacturers.phone"}, ["A12", "A20"],
    "about 60% by makers' stores and authorized providers"),
  stake("k1", "manufacturers.phone", "Similar bills were introduced in Kestrava in 2023 and 2025 and failed after campaigns on both sides."),
  stake("k2", "manufacturers.phone", "Similar bills were introduced in Kestrava in 2023 and 2025 and failed after campaigns on both sides."),
 ],
 "distributors.farm_equipment": [
  stake("k1", "distributors.farm_equipment", "Four makers sell through 140 authorized dealer locations, which are independent businesses under dealer agreements"),
  stake("k2", "distributors.farm_equipment", "K2 binds 'Makers, dealers, lessors'"),
 ],
 "officials.enforcement": [],
 "sellers.stolen_parts": [],
 "treasury": [],
}

R2 = {
 "distributors.farm_equipment#2": [
  link("distributors.farm_equipment", "quantity_demanded", "supply_price", "distributors.farm_equipment", "net_price_received", ["A4"],
       "Dealers' service revenue is about $520 million a year ... labor at about $165 an hour; independents charge about $95", horizon="short"),
  link("distributors.farm_equipment", "quantity_demanded", "crowding", "growers", "wait_time", ["A14"],
       "Farm surveys put the average wait for a dealer technician at harvest at 2.5 days."),
  link("distributors.farm_equipment", "quantity_demanded", "yield", "distributors.farm_equipment", "asset_value", ["A19", "A20"],
       "Four makers sell through 140 authorized dealer locations, which are independent businesses under dealer agreements"),
 ],
 "growers.new_buyers#2": [
  link("growers.new_buyers", "price_paid", "own_price", "growers.new_buyers", "quantity_demanded", [],
       "New equipment sales in Kestrava are about $1.1 billion a year"),
  link("growers.new_buyers", "quantity_traded", "same_act", "distributors.farm_equipment", "quantity_traded", [],
       "Four makers sell through 140 authorized dealer locations"),
 ],
 "manufacturers.phone#2": [
  link("manufacturers.phone", "quantity_supplied", "supply", "owners.other_states", "price_paid", ["A8"],
       "One maker already sells genuine parts and rents tools to owners in all states at the prices its authorized providers pay"),
 ],
 "repair_shops.authorized_phone": [
  link("repair_shops.authorized_phone", "quantity_demanded", "supply_price", "repair_shops.authorized_phone", "net_price_received", ["A4"],
       "about 60% by makers' stores and authorized providers (a screen repair with a genuine part costs about $280)", horizon="short"),
 ],
 "repair_shops.independent_farm#2": [
  P("yields", {"exchange": "e3", "side": "buyer", "actor": "repair_shops.independent_farm"}, ["A20"],
    "Independents can buy many mechanical parts at list from dealers but cannot buy the software"),
 ],
 "repair_shops.independent_phone#2": [
  P("yields", {"exchange": "e1", "side": "buyer", "actor": "repair_shops.independent_phone"}, ["A20"],
    "about 40% by some 900 independent shops using non-genuine or salvaged parts"),
 ],
 "growers#2": [], "owners.phones#2": [], "buyers.new_phones#2": [], "manufacturers.farm#2": [],
 "growers.near_border": [], "sellers.substitutes": [],
}

R3 = {
 "repair_shops.independent_farm#3": [
  link("repair_shops.independent_farm", "return_on_capital", "yield", "repair_shops.independent_farm", "investment_target", ["A5"],
       "about 260 independent shops repair farm equipment", horizon="long"),
 ],
 "repair_shops.independent_phone#3": [
  link("repair_shops.independent_phone", "return_on_capital", "yield", "repair_shops.independent_phone", "investment_target", ["A5"],
       "some 900 independent shops", horizon="long"),
 ],
 "owners.other_states": [
  link("owners.other_states", "price_paid", "own_price", "owners.other_states", "quantity_demanded", [],
       "One maker already sells genuine parts and rents tools to owners in all states at the prices its authorized providers pay"),
 ],
 "distributors.farm_equipment#3": [], "growers#3": [], "growers.new_buyers#3": [], "repair_shops.authorized_phone#2": [],
}

ROUNDS = {1: R1, 2: R2, 3: R3}
ANSWERS = {}


def build(upto):
    props = {}
    for r in range(1, upto + 1):
        for k, v in ROUNDS.get(r, {}).items():
            props[k] = v
    (HERE / "proposals.json").write_text(json.dumps(props, indent=1))
    used = {t for ps in props.values() for p in ps for t in p["premises"]}
    seed = json.loads((HERE / "seed.json").read_text())
    seed_texts = {v["text"] for v in seed["assumptions"].values()}
    table = {v[0]: v[2] for v in T.values()}
    ans = {t: table[t] for t in used if t not in seed_texts}
    (HERE / "answers.json").write_text(json.dumps(ans, indent=1))


if __name__ == "__main__":
    import sys
    build(int(sys.argv[1]))
