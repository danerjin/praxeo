"""Build a PDF of the Phase 2 progress report (PHASE2_REPORT.md).

Usage: python3 tools/build_report_pdf.py [out.pdf]
Uses the handbook PDF's pipeline (pandoc to HTML, headless Chromium to PDF).
"""
import os
import re
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_handbook_pdf import CHROMIUM, CSS, ROOT, read  # noqa: E402


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "Phase2_Progress_Report.pdf")
    text = read(os.path.join(ROOT, "PHASE2_REPORT.md"))
    first, _, rest = text.partition("\n")
    md = re.sub(r"(?m)^## ", "# ", rest)  # each section on its own page, like the handbook's chapters
    title = ('<div class="title-page"><h1 class="main">Phase 2 Progress Report</h1>'
             "<p>Praxeological policy analysis: the analyser</p>"
             "<p>Thin slice, rule base, LLM stages, controls, mathematical annex</p></div>")
    with tempfile.TemporaryDirectory() as tmp:
        src, css, before, html = (os.path.join(tmp, n) for n in ("r.md", "s.css", "t.html", "r.html"))
        open(src, "w", encoding="utf-8").write(md)
        open(css, "w").write(CSS + "\nh1 { page-break-before: auto; }\n")
        open(before, "w").write(title)
        subprocess.run(["pandoc", src, "-f", "gfm", "-t", "html5", "-s", "--toc", "--toc-depth=1",
                        "--metadata", "title=Phase 2 Progress Report", "--metadata", "pagetitle=Phase 2 Progress Report",
                        "-V", "title=", "--css", css, "--embed-resources", "--include-before-body", before, "-o", html],
                       check=True)
        page = re.sub(r'<header id="title-block-header">.*?</header>', "", read(html), flags=re.S)
        open(html, "w", encoding="utf-8").write(page)
        chrome = next(p for p in CHROMIUM if os.path.exists(p))
        subprocess.run([chrome, "--headless", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                        f"--print-to-pdf={out}", "file://" + html],
                       check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(out)


if __name__ == "__main__":
    main()
