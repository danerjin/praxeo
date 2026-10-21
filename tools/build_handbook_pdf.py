"""Build a PDF of the Method Handbook.

Usage: python3 tools/build_handbook_pdf.py [out.pdf]

Concatenates the handbook chapters (README, 01 to 08, the template) and a few
sample worked examples into one document, converts it to HTML with pandoc and
prints it to PDF with headless Chromium. The full set of worked examples and
core-only re-runs stays in handbook/05_examples and handbook/05_examples_core.
"""
import os
import re
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
H = os.path.join(ROOT, "handbook")

CHAPTERS = [
    "01_foundations.md",
    "02_ontology.md",
    "03_workflow.md",
    "04a_core_rules.md",
    "04_rules.md",
    "06_gaps.md",
    "08_core_rerun_report.md",
    "07_sources.md",
]
SAMPLES = [
    "WE-001_rent_freeze.md",
    "WE-022_rent_freeze_repeal.md",
    "WE-046_congestion_charge.md",
]
CHROMIUM = [
    "/opt/pw-browsers/chromium-1194/chrome-linux/chrome",
    "/opt/pw-browsers/chromium/chrome-linux/chrome",
]

CSS = """
@page { size: A4; margin: 20mm 17mm 20mm 17mm; }
body { font-family: "DejaVu Sans", "Liberation Sans", Arial, sans-serif; font-size: 9.5pt;
       line-height: 1.42; color: #1a1a1a; background: #fff; max-width: none; }
h1 { color: #1B5E20; font-size: 20pt; border-bottom: 2px solid #2E7D32; padding-bottom: 4px;
     page-break-before: always; margin-top: 0; }
h2 { color: #2E4A2F; font-size: 13.5pt; margin-top: 18px; }
h3 { color: #2E4A2F; font-size: 11pt; margin-top: 14px; }
h4 { font-size: 10pt; }
h1, h2, h3, h4 { page-break-after: avoid; }
table { border-collapse: collapse; width: 100%; margin: 8px 0; font-size: 8pt; }
th, td { border: 1px solid #c8d5c8; padding: 3px 5px; vertical-align: top; text-align: left; }
th { background: #e8f1e8; }
tr { page-break-inside: avoid; }
code { font-family: "DejaVu Sans Mono", monospace; font-size: 8.5pt; background: #f3f5f3; padding: 0 2px; }
pre { background: #f3f5f3; padding: 6px; font-size: 8pt; white-space: pre-wrap; }
blockquote { border-left: 3px solid #2E7D32; margin: 8px 0; padding: 2px 10px; background: #f6faf6; }
.title-page { text-align: center; padding-top: 70mm; page-break-after: always; }
.title-page h1.main { border: none; page-break-before: avoid; font-size: 30pt; }
.title-page p { font-size: 12pt; color: #2E4A2F; }
nav#TOC { page-break-after: always; }
nav#TOC ul { list-style: none; padding-left: 14px; }
nav#TOC > ul > li { margin-top: 4px; font-weight: bold; }
nav#TOC li li { font-weight: normal; }
a { color: #1B5E20; text-decoration: none; }
"""


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def demote(text, by=1):
    """Shift every Markdown heading down one level, outside code fences."""
    out, fence = [], False
    for line in text.splitlines():
        if line.startswith("```"):
            fence = not fence
        if not fence and re.match(r"#{1,5} ", line):
            line = "#" * by + line
        out.append(line)
    return "\n".join(out)


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "Method_Handbook.pdf")
    status = re.search(r"\*\*Status:\*\*\s*([^\n]+)", read(os.path.join(H, "README.md")))
    parts = []
    readme = read(os.path.join(H, "README.md"))
    readme = re.sub(r"^# Method Handbook\s*", "# Introduction\n\n", readme, count=1)
    parts.append(readme)
    for name in CHAPTERS:
        text = read(os.path.join(H, name))
        # later top-level sections of a chapter (the re-run report's rounds) sit under its title
        first, _, rest = text.partition("\n")
        rest = re.sub(r"(?m)^# ", "## ", rest)
        parts.append(first + "\n" + rest)
    parts.append("# Appendix A. Analysis template\n\n" + demote(read(os.path.join(H, "templates", "analysis_template.md"))))
    n = len([f for f in os.listdir(os.path.join(H, "05_examples")) if f.startswith("WE-")])
    samples = [f"# Appendix B. Sample worked examples\n\nThree of the {n} worked examples, printed in full: a price control (WE-001), its repeal with the metamorphic check (WE-022), and a held-out case corrected under catalog 1.0 (WE-046). The others are in `handbook/05_examples/`, and the blind core-only re-runs in `handbook/05_examples_core/`."]
    for name in SAMPLES:
        samples.append(demote(read(os.path.join(H, "05_examples", name))))
    parts.append("\n\n".join(samples))
    md = "\n\n".join(p.strip() for p in parts) + "\n"

    title = (
        '<div class="title-page"><h1 class="main">Method Handbook</h1>'
        "<p>Praxeological policy analysis</p>"
        "<p>Phase 1 deliverable of the Praxeology AI project</p>"
        f"<p style='font-size:10pt;color:#555'>{status.group(1).split('(')[0].strip() if status else ''}</p>"
        "</div>"
    )
    with tempfile.TemporaryDirectory() as tmp:
        src = os.path.join(tmp, "handbook.md")
        css = os.path.join(tmp, "style.css")
        before = os.path.join(tmp, "title.html")
        html = os.path.join(tmp, "handbook.html")
        open(src, "w", encoding="utf-8").write(md)
        open(css, "w").write(CSS)
        open(before, "w").write(title)
        subprocess.run(
            ["pandoc", src, "-f", "gfm", "-t", "html5", "-s", "--toc", "--toc-depth=2",
             "--metadata", "title=Method Handbook", "--metadata", "pagetitle=Method Handbook",
             "-V", "title=", "--css", css, "--embed-resources", "--include-before-body", before,
             "-o", html],
            check=True,
        )
        # pandoc's default template adds its own title block; drop it, keep ours
        page = read(html)
        page = re.sub(r'<header id="title-block-header">.*?</header>', "", page, flags=re.S)
        open(html, "w", encoding="utf-8").write(page)
        chrome = next(p for p in CHROMIUM if os.path.exists(p))
        subprocess.run(
            [chrome, "--headless", "--no-sandbox", "--disable-gpu",
             "--no-pdf-header-footer", f"--print-to-pdf={out}", "file://" + html],
            check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        )
    print(out)


if __name__ == "__main__":
    main()
