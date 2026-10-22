"""Fill answers.json from the assumption table where a question's statement matches; print the others for judgement."""
import json, re, subprocess, sys
TABLE = "/tmp/claude-0/-home-user-praxeo/6d563eb7-45da-5432-b932-3230b691929b/scratchpad/blind/WE-064_assumptions.txt"
tab = {}
for line in open(TABLE):
    p = [x.strip() for x in line.split("|")]
    if len(p) >= 4: tab[p[1]] = float(p[3])
out = subprocess.run(["bash", "cases/we064_tarnesse/loop_r2/run.sh"], capture_output=True, text=True).stdout
qs = [l[len("question: "):] for l in out.splitlines() if l.startswith("question: ")]
ans = json.load(open("cases/we064_tarnesse/loop_r2/answers.json"))
for q in qs:
    if q in tab: ans[q] = tab[q]; print("TABLE", tab[q], q)
    else: print("JUDGE", q)
json.dump(ans, open("cases/we064_tarnesse/loop_r2/answers.json", "w"), indent=1)
