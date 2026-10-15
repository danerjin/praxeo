"""Consistency checks for the Method Handbook's worked examples.

Usage: python3 tools/check_handbook.py [example files...]

It first checks the pattern catalog (04_rules.md): every pattern has a derivation from the core rules
and cites only defined rules. With no arguments, it then checks every file in handbook/05_examples/.
For each example it checks:
- the required sections are present, in order;
- every rule ID cited (RS-1, PC-4, CR-7b, LW-3, ...) is defined in 04_rules.md, 04a_core_rules.md
  or 01_foundations.md;
- every variable in the consequence list is in the controlled list (02_ontology.md, 2.4);
- no consequence is recorded as a bare "(loss)" instead of a signed variable;
- every sign is increase, decrease, ambiguous, a group sign (at_least_one_increase or
  at_least_one_decrease), or one of these per reading ("U1-a: increase; U1-b: ambiguous");
- every assumption cited in the consequence list is defined in section 10.
Open local gaps (a GAP-005-1 not marked closed, resolved or out of scope under "Gaps found") are
reported, not failed. Rule IDs proposed under "Gaps found" are not checked against the catalog.
Exits non-zero if any example has errors.
"""
import glob
import os
import re
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "handbook")
SECTIONS = [
    "## 1. Policy record", "## 2. Classification", "## 3. Actor classes", "## 4. Direct effect",
    "## 5. Responses", "## 6. Second-order effects", "## 7. Combined effects", "## 8. Time structure",
    "## 9. Opportunity costs", "## 10. Assumptions", "## 11. Report",
    "## Consequence list (normal form)", "## Gaps found",
]
RULE_ID = re.compile(r"\b((?:RS|OC|TS|PC|TX|SB|EN|DM|AX|LW|CR)-\d+)[a-d]?\b")


def read(name):
    with open(os.path.join(ROOT, name), encoding="utf-8") as f:
        return f.read()


def defined_rules():
    rules = set(re.findall(r"^### ((?:RS|OC|TS|PC|TX|SB|EN|DM)-\d+)", read("04_rules.md"), re.M))
    rules |= set(re.findall(r"^### (CR-\d+)", read("04a_core_rules.md"), re.M))
    return rules | set(re.findall(r"^## ((?:AX|LW)-\d+)", read("01_foundations.md"), re.M))


def controlled_variables():
    text = read("02_ontology.md")
    section = text[text.index("## 2.4"):text.index("## 2.5")]
    names = set(re.findall(r"^\| `([a-z_]+)`", section, re.M))
    for pair in re.findall(r"^\| `([a-z_]+)`, `([a-z_]+)`", section, re.M):
        names.update(pair)
    return names


def table_rows(block):
    rows = []
    for line in block.splitlines():
        line = line.strip()
        if line.startswith("|") and not re.fullmatch(r"\|[\s\-:|]+\|", line):
            rows.append([c.strip() for c in line.strip("|").split("|")])
    return rows[1:]  # drop header


SIGNS = {"increase", "decrease", "ambiguous", "at_least_one_increase", "at_least_one_decrease"}


def valid_sign(sign):
    """A plain sign, or one sign per reading of an unclear provision: 'U1-a: increase; U1-b: ambiguous'."""
    if sign in SIGNS:
        return True
    parts = [p.strip() for p in sign.split(";")]
    return len(parts) > 1 and all(re.fullmatch(r"U\d+-[a-z]: (\S+)", p) and p.split(": ")[1] in SIGNS
                                  for p in parts)


def check(path, rules, variables):
    text = open(path, encoding="utf-8").read()
    errors, notes = [], []

    positions = [text.find(s) for s in SECTIONS]
    for s, p in zip(SECTIONS, positions):
        if p < 0:
            errors.append(f"missing section '{s}'")
    found = [p for p in positions if p >= 0]
    if found != sorted(found):
        errors.append("sections out of order")

    # Proposed new rules may be named in "Gaps found"; only the analysis must cite defined rules.
    analysis = text.split("## Gaps found")[0]
    unknown = sorted(set(RULE_ID.findall(analysis)) - rules)
    if unknown:
        errors.append(f"undefined rule IDs: {', '.join(unknown)}")

    gaps = set(re.findall(r"GAP-\d{3}-\d+", text))
    gap_section = text[text.find("## Gaps found"):] if "## Gaps found" in text else ""
    resolved = set()
    for line in gap_section.splitlines():
        if re.search(r"\((closed|resolved|out of scope)", line):
            resolved.update(re.findall(r"GAP-\d{3}-\d+", line))
    still_open = sorted(gaps - resolved)
    if still_open:
        notes.append(f"open gaps: {', '.join(still_open)}")

    if "(loss)" in text:
        errors.append("bare '(loss)' entry; record opportunity costs as signed variables")

    if "## Consequence list" in text:
        block = text[text.index("## Consequence list"):text.index("## Gaps found")] \
            if "## Gaps found" in text else text[text.index("## Consequence list"):]
        assumptions = set(re.findall(r"^\| (A-\d+) \|", text, re.M))
        for row in table_rows(block):
            if len(row) < 9:
                continue
            cid, variable, sign, assumed = row[0], row[2], row[3], row[8]
            names = re.findall(r"[a-z]+(?:_[a-z]+)+|\b[a-z]{4,}\b", variable.split("(")[0])
            if names and not any(n in variables for n in names):
                notes.append(f"{cid}: variable '{variable}' not in the controlled list")
            if not valid_sign(sign):
                errors.append(f"{cid}: sign '{sign}' is not a valid sign")
            for a in re.findall(r"A-\d+", assumed):
                if a not in assumptions:
                    errors.append(f"{cid}: assumption {a} not defined in section 10")
    return errors, notes


def check_catalog(rules):
    """Every pattern in 04_rules.md has a derivation, and cites only defined rules."""
    errors = []
    text = read("04_rules.md")
    for block in re.split(r"(?m)^(?=### )", text)[1:]:
        rid = block.split()[1]
        if "**Derivation:**" not in block:
            errors.append(f"{rid}: no derivation from the core rules")
        unknown = sorted(set(RULE_ID.findall(block)) - rules)
        if unknown:
            errors.append(f"{rid}: cites undefined rules {', '.join(unknown)}")
    return errors


def main(argv):
    files = argv or sorted(glob.glob(os.path.join(ROOT, "05_examples", "WE-*.md")))
    rules, variables = defined_rules(), controlled_variables()
    catalog_errors = check_catalog(rules)
    print("FAIL  04_rules.md" if catalog_errors else "ok    04_rules.md (every pattern derived)")
    for e in catalog_errors:
        print(f"      error: {e}")
    failed = bool(catalog_errors)
    for path in files:
        errors, notes = check(path, rules, variables)
        status = "FAIL" if errors else "ok"
        print(f"{status:4}  {os.path.basename(path)}")
        for e in errors:
            print(f"      error: {e}")
        for n in notes:
            print(f"      note:  {n}")
        failed += bool(errors)
    print(f"\n{len(files) + 1 - failed}/{len(files) + 1} files pass (catalog and examples)")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
