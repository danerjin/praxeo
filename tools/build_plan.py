"""Build the project-plan .docx from its Markdown source, in the house style of v2.

Usage: python3 tools/build_plan.py Praxeology_AI_Project_Plan_v3.md [out.docx]

Supports the small Markdown subset the plan uses: a `%` title block, # / ## / ###
headings, paragraphs with **bold**, *italic* and `code`, "- " bullets, "1. " numbered
lists, pipe tables, ``` code fences, "> " callouts and ![caption](image) figures.
"""
import os
import re
import sys

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor, Twips

FONT = "Calibri"
MONO = "Consolas"
GREEN = "2E7D32"
DARK_GREEN = "1B5E20"
H2_GREEN = "2E4A2F"
FOOTER = "Praxeological Policy Analysis System"
TABLE_WIDTH = 9360  # dxa, 6.5 inches


def rgb(hex_):
    return RGBColor.from_string(hex_)


def set_run(run, size=11, bold=None, italic=None, color=None, font=FONT):
    run.font.name = font
    rpr = run._element.get_or_add_rPr()
    fonts = rpr.find(qn("w:rFonts"))
    if fonts is None:
        fonts = OxmlElement("w:rFonts")
        rpr.insert(0, fonts)
    for attr in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        fonts.set(qn(attr), font)
    run.font.size = Pt(size)
    if bold is not None:
        run.bold = bold
    if italic is not None:
        run.italic = italic
    if color:
        run.font.color.rgb = rgb(color)


def spacing(par, before=0, after=140, line=None):
    pf = par.paragraph_format
    pf.space_before = Pt(before / 20)
    pf.space_after = Pt(after / 20)
    if line:
        pf.line_spacing = line / 240


def border(par, side, color, sz, space):
    ppr = par._p.get_or_add_pPr()
    bdr = ppr.find(qn("w:pBdr"))
    if bdr is None:
        bdr = OxmlElement("w:pBdr")
        ppr.append(bdr)
    el = OxmlElement(f"w:{side}")
    for k, v in (("val", "single"), ("color", color), ("sz", str(sz)), ("space", str(space))):
        el.set(qn(f"w:{k}"), v)
    bdr.append(el)


def shade(el_pr, fill):
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:fill"), fill)
    el_pr.append(shd)


INLINE = re.compile(r"(\*\*[^*]+\*\*|\*[^*]+\*|`[^`]+`)")


def add_inline(par, text, size=11, color=None, bold=False):
    for part in INLINE.split(text):
        if not part:
            continue
        if part.startswith("**"):
            set_run(par.add_run(part[2:-2]), size, bold=True, color=color)
        elif part.startswith("`"):
            set_run(par.add_run(part[1:-1]), size - 1, bold=bold, color=color, font=MONO)
        elif part.startswith("*"):
            set_run(par.add_run(part[1:-1]), size, bold=bold, italic=True, color=color)
        else:
            set_run(par.add_run(part), size, bold=bold, color=color)


def heading(doc, text, level):
    par = doc.add_paragraph(style=f"Heading {level}")
    par.paragraph_format.keep_with_next = True
    if level == 1:
        spacing(par, 360, 140)
        border(par, "bottom", GREEN, 6, 2)
        set_run(par.add_run(text), 16, bold=True, color=DARK_GREEN)
    elif level == 2:
        spacing(par, 260, 100)
        set_run(par.add_run(text), 13, bold=True, color=H2_GREEN)
    else:
        spacing(par, 200, 80)
        set_run(par.add_run(text), 11.5, bold=True, color=H2_GREEN)


def body(doc, text):
    par = doc.add_paragraph()
    spacing(par, 0, 140, 276)
    add_inline(par, text)


def list_item(doc, text, marker):
    par = doc.add_paragraph()
    spacing(par, 0, 70, 270)
    pf = par.paragraph_format
    indent = 360 if marker == "•" else 420
    pf.left_indent = Twips(indent)
    pf.first_line_indent = Twips(-indent + 60)
    pf.tab_stops.add_tab_stop(Twips(indent))
    set_run(par.add_run(f"{marker}\t"), 11, color=GREEN if marker == "•" else None,
            bold=marker != "•")
    add_inline(par, text)


def callout(doc, text):
    par = doc.add_paragraph()
    spacing(par, 140, 180, 270)
    par.paragraph_format.left_indent = Twips(300)
    par.paragraph_format.right_indent = Twips(100)
    border(par, "left", GREEN, 20, 10)
    shade(par._p.get_or_add_pPr(), "F1F8F1")
    add_inline(par, text)


def code_block(doc, lines):
    for i, line in enumerate(lines):
        par = doc.add_paragraph()
        spacing(par, 80 if i == 0 else 0, 80 if i == len(lines) - 1 else 0, 240)
        par.paragraph_format.left_indent = Twips(200)
        shade(par._p.get_or_add_pPr(), "F3F6F3")
        set_run(par.add_run(line if line else " "), 9, font=MONO, color="2E4A2F")


def figure(doc, caption, path):
    par = doc.add_paragraph()
    par.alignment = WD_ALIGN_PARAGRAPH.CENTER
    spacing(par, 160, 60)
    par.add_run().add_picture(path, width=Inches(6.2))
    cap = doc.add_paragraph()
    cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    spacing(cap, 0, 220)
    set_run(cap.add_run(caption), 9.5, italic=True, color="555555")


def col_widths(rows):
    ncol = len(rows[0])
    weights = []
    for c in range(ncol):
        lens = [len(r[c]) for r in rows if c < len(r)]
        avg = sum(lens) / len(lens)
        weights.append(max(min(avg, 160), 6) ** 0.8)
    total = sum(weights)
    widths = [w / total * TABLE_WIDTH for w in weights]
    # Never let a column be narrower than its longest word, or Word breaks it mid-word.
    floors = []
    for c in range(ncol):
        longest = max(len(word) for r in rows if c < len(r) for word in (r[c].split() or [""]))
        floors.append(max(900, longest * 110 + 260))
    widths = [max(w, f) for w, f in zip(widths, floors)]
    scale = TABLE_WIDTH / sum(widths)
    return [int(w * scale) for w in widths]


def table(doc, rows):
    ncol = len(rows[0])
    widths = col_widths(rows)
    tbl = doc.add_table(rows=len(rows), cols=ncol)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    tbl_pr = tbl._tbl.tblPr
    layout = OxmlElement("w:tblLayout")
    layout.set(qn("w:type"), "fixed")
    tbl_pr.append(layout)
    grid = tbl._tbl.tblGrid
    for gc, w in zip(grid.findall(qn("w:gridCol")), widths):
        gc.set(qn("w:w"), str(w))
    for r, row in enumerate(rows):
        tr = tbl.rows[r]
        tr_pr = tr._tr.get_or_add_trPr()
        tr_pr.append(OxmlElement("w:cantSplit"))
        if r == 0:
            tr_pr.append(OxmlElement("w:tblHeader"))
        for c in range(ncol):
            cell = tr.cells[c]
            cell.width = Twips(widths[c])
            tc_pr = cell._tc.get_or_add_tcPr()
            borders = OxmlElement("w:tcBorders")
            for side in ("top", "left", "bottom", "right"):
                el = OxmlElement(f"w:{side}")
                el.set(qn("w:val"), "single")
                el.set(qn("w:color"), "BFC9BF")
                el.set(qn("w:sz"), "4")
                borders.append(el)
            tc_pr.append(borders)
            shade(tc_pr, GREEN if r == 0 else ("F6F9F6" if r % 2 else "FFFFFF"))
            mar = OxmlElement("w:tcMar")
            for side, v in (("top", 70), ("left", 110), ("bottom", 70), ("right", 110)):
                el = OxmlElement(f"w:{side}")
                el.set(qn("w:w"), str(v))
                el.set(qn("w:type"), "dxa")
                mar.append(el)
            tc_pr.append(mar)
            par = cell.paragraphs[0]
            spacing(par, 0, 40, 250)
            text = row[c] if c < len(row) else ""
            if r == 0:
                set_run(par.add_run(text), 9.5, bold=True, color="FFFFFF")
            else:
                add_inline(par, text, size=9.5, bold=(c == 0 and ncol > 2 and len(text) < 40))
    spacer = doc.add_paragraph()
    spacing(spacer, 0, 120)


def footer(doc):
    sec = doc.sections[0]
    par = sec.footer.paragraphs[0]
    par.alignment = WD_ALIGN_PARAGRAPH.CENTER
    set_run(par.add_run(f"{FOOTER}  |  Page "), 9, color="777777")
    run = par.add_run()
    set_run(run, 9, color="777777")
    for kind, text in (("begin", None), (None, "PAGE"), ("separate", None), ("end", None)):
        if kind:
            el = OxmlElement("w:fldChar")
            el.set(qn("w:fldCharType"), kind)
        else:
            el = OxmlElement("w:instrText")
            el.set(qn("xml:space"), "preserve")
            el.text = text
        run._r.append(el)


def split_row(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def build(src, out):
    base = os.path.dirname(os.path.abspath(src))
    lines = open(src, encoding="utf-8").read().splitlines()
    doc = Document()
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Inches(8.5), Inches(11)
    for side in ("left_margin", "right_margin"):
        setattr(sec, side, Inches(1))
    sec.top_margin = sec.bottom_margin = Inches(0.9)
    footer(doc)

    title = [l[2:] for l in lines if l.startswith("% ")]
    if title:
        par = doc.add_paragraph()
        spacing(par, 200, 80)
        set_run(par.add_run(title[0]), 24, bold=True, color=DARK_GREEN)
        if len(title) > 1:
            par = doc.add_paragraph()
            spacing(par, 0, 80)
            set_run(par.add_run(title[1]), 14, color="444444")
        if len(title) > 2:
            par = doc.add_paragraph()
            spacing(par, 0, 240)
            border(par, "bottom", GREEN, 8, 6)
            set_run(par.add_run(title[2]), 10, color="666666")

    i = 0
    while i < len(lines):
        line = lines[i]
        s = line.strip()
        if not s or s.startswith("% "):
            i += 1
        elif s.startswith("```"):
            j = i + 1
            while not lines[j].strip().startswith("```"):
                j += 1
            code_block(doc, lines[i + 1:j])
            i = j + 1
        elif s.startswith("#"):
            level = len(s) - len(s.lstrip("#"))
            heading(doc, s[level:].strip(), level)
            i += 1
        elif s.startswith("!["):
            m = re.match(r"!\[(.*)\]\((.*)\)", s)
            figure(doc, m.group(1), os.path.join(base, m.group(2)))
            i += 1
        elif s.startswith(">"):
            callout(doc, s.lstrip("> ").strip())
            i += 1
        elif s.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                row = split_row(lines[i])
                if not all(re.fullmatch(r":?-+:?", c) for c in row):
                    rows.append(row)
                i += 1
            table(doc, rows)
        elif s.startswith("- "):
            list_item(doc, s[2:], "•")
            i += 1
        elif re.match(r"\d+\. ", s):
            num, text = s.split(". ", 1)
            list_item(doc, text, f"{num}.")
            i += 1
        else:
            para = [s]
            i += 1
            while i < len(lines) and lines[i].strip() and not re.match(
                    r"(#|- |\d+\. |\||>|!\[|```)", lines[i].strip()):
                para.append(lines[i].strip())
                i += 1
            body(doc, " ".join(para))
    doc.save(out)


if __name__ == "__main__":
    source = sys.argv[1]
    target = sys.argv[2] if len(sys.argv) > 2 else os.path.splitext(source)[0] + ".docx"
    build(source, target)
    print(target)
