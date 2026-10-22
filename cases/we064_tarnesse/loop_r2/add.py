"""python add.py FRAGMENT.json : merge a round's proposals into proposals.json (keys new or '#n' revisits)."""
import json, sys
p = "cases/we064_tarnesse/loop_r2/proposals.json"
d = json.load(open(p)); d.update(json.load(open(sys.argv[1]))); json.dump(d, open(p, "w"), indent=1)
