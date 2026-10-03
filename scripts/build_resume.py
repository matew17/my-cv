#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt

ROOT = Path(__file__).resolve().parents[1]
MASTER = ROOT / "master" / "resume.md"
OUTPUT = ROOT / "output"
OUTPUT.mkdir(exist_ok=True)
DOCX_PATH = OUTPUT / "Mateo_Castano_Staff_Agentic_AI.docx"
PDF_PATH = OUTPUT / "Mateo_Castano_Staff_Agentic_AI.pdf"


def font_run(run, size: float, bold: bool = False, italic: bool = False):
    run.font.name = "Arial"
    run._element.rPr.rFonts.set(qn("w:eastAsia"), "Arial")
    run.font.size = Pt(size)
    run.bold = bold
    run.italic = italic


def keep_with_next(paragraph):
    pPr = paragraph._p.get_or_add_pPr()
    if pPr.find(qn("w:keepNext")) is None:
        pPr.append(OxmlElement("w:keepNext"))


def keep_lines(paragraph):
    pPr = paragraph._p.get_or_add_pPr()
    if pPr.find(qn("w:keepLines")) is None:
        pPr.append(OxmlElement("w:keepLines"))


def format_paragraph(p, before=0, after=0, line=1.0):
    pf = p.paragraph_format
    pf.space_before = Pt(before)
    pf.space_after = Pt(after)
    pf.line_spacing = line


def add_inline_markdown(p, text: str, size: float, base_bold: bool = False):
    # Supports **bold** inline spans. URLs remain visible plain text for ATS parsing.
    parts = re.split(r'(\*\*.*?\*\*)', text)
    for part in parts:
        if not part:
            continue
        is_bold = part.startswith('**') and part.endswith('**')
        content = part[2:-2] if is_bold else part
        r = p.add_run(content)
        font_run(r, size, bold=(base_bold or is_bold))


def find_libreoffice():
    executable = shutil.which("libreoffice") or shutil.which("soffice")
    if executable:
        return executable
    mac_executable = Path("/Applications/LibreOffice.app/Contents/MacOS/soffice")
    if mac_executable.is_file():
        return str(mac_executable)
    return None


def build_pdf(require_pdf=False):
    soffice = find_libreoffice()
    if not soffice:
        # A previous build's PDF must not appear to match the new DOCX.
        PDF_PATH.unlink(missing_ok=True)
        message = "LibreOffice not found. Install it to generate PDF (macOS: brew install --cask libreoffice)."
        if require_pdf:
            raise SystemExit(message)
        print(f"PDF skipped: {message}")
        return

    PDF_PATH.unlink(missing_ok=True)
    # Isolate the conversion from any open LibreOffice session and stale outputs.
    with tempfile.TemporaryDirectory(prefix="resume-pdf-") as temporary:
        conversion_dir = Path(temporary)
        profile = (conversion_dir / "profile").as_uri()
        try:
            result = subprocess.run(
                [soffice, f"-env:UserInstallation={profile}", "--headless",
                 "--convert-to", "pdf", "--outdir", str(conversion_dir), str(DOCX_PATH)],
                check=True,
                capture_output=True,
                text=True,
                timeout=120,
            )
        except (OSError, subprocess.SubprocessError) as error:
            details = getattr(error, "stderr", None) or str(error)
            raise SystemExit(f"PDF conversion failed: {details}") from error
        generated = conversion_dir / f"{DOCX_PATH.stem}.pdf"
        if not generated.is_file() or generated.stat().st_size == 0:
            raise SystemExit(f"LibreOffice produced no PDF.\n{result.stdout}\n{result.stderr}")
        if not generated.read_bytes().startswith(b"%PDF-"):
            raise SystemExit("LibreOffice output is not a PDF file.")
        shutil.move(str(generated), PDF_PATH)
    print(f"Wrote {PDF_PATH}")


def build_docx(require_pdf=False):
    lines = MASTER.read_text(encoding="utf-8").splitlines()
    doc = Document()
    sec = doc.sections[0]
    sec.top_margin = Inches(0.48)
    sec.bottom_margin = Inches(0.48)
    sec.left_margin = Inches(0.58)
    sec.right_margin = Inches(0.58)
    sec.header_distance = Inches(0.2)
    sec.footer_distance = Inches(0.2)

    normal = doc.styles["Normal"]
    normal.font.name = "Arial"
    normal._element.rPr.rFonts.set(qn("w:eastAsia"), "Arial")
    normal.font.size = Pt(9.0)
    normal.paragraph_format.space_after = Pt(0)
    normal.paragraph_format.line_spacing = 1.0

    first_nonempty_after_h1 = True
    pending_para: list[str] = []

    def flush_paragraph():
        nonlocal pending_para
        if not pending_para:
            return
        text = " ".join(x.strip() for x in pending_para).strip()
        p = doc.add_paragraph()
        format_paragraph(p, after=1.6, line=1.02)
        keep_lines(p)
        add_inline_markdown(p, text, 9.2)
        pending_para = []

    for raw in lines:
        line = raw.rstrip()
        stripped = line.strip()

        if not stripped:
            flush_paragraph()
            continue

        if stripped == "<!-- PAGEBREAK -->":
            flush_paragraph()
            doc.add_page_break()
            continue

        if stripped.startswith("# "):
            flush_paragraph()
            p = doc.add_paragraph()
            format_paragraph(p, after=0.4)
            r = p.add_run(stripped[2:].upper())
            font_run(r, 18.0, bold=True)
            first_nonempty_after_h1 = True
            continue

        if stripped.startswith("## "):
            flush_paragraph()
            p = doc.add_paragraph()
            format_paragraph(p, before=4.2, after=2.2)
            keep_with_next(p)
            r = p.add_run(stripped[3:].upper())
            font_run(r, 10.2, bold=True)
            continue

        if stripped.startswith("### "):
            flush_paragraph()
            p = doc.add_paragraph()
            format_paragraph(p, before=3.5, after=0.6)
            keep_with_next(p)
            add_inline_markdown(p, stripped[4:], 9.6, base_bold=True)
            continue

        if stripped.startswith("#### "):
            flush_paragraph()
            p = doc.add_paragraph()
            format_paragraph(p, before=2.4, after=0.4)
            keep_with_next(p)
            add_inline_markdown(p, stripped[5:], 9.5, base_bold=True)
            continue

        if stripped.startswith("- "):
            flush_paragraph()
            p = doc.add_paragraph()
            format_paragraph(p, after=0.8)
            keep_lines(p)
            pf = p.paragraph_format
            pf.left_indent = Inches(0.16)
            pf.first_line_indent = Inches(-0.12)
            r = p.add_run("• ")
            font_run(r, 9.0)
            add_inline_markdown(p, stripped[2:], 9.0)
            continue

        # Headline directly after H1.
        if first_nonempty_after_h1 and stripped.startswith("**") and stripped.endswith("**"):
            flush_paragraph()
            p = doc.add_paragraph()
            format_paragraph(p, after=1.2)
            r = p.add_run(stripped[2:-2])
            font_run(r, 10.6, bold=True)
            first_nonempty_after_h1 = False
            continue

        # Contact line follows the headline and is intentionally compact.
        if not pending_para and ("@" in stripped and "LinkedIn" in stripped and "GitHub" in stripped):
            flush_paragraph()
            p = doc.add_paragraph()
            format_paragraph(p, after=2.6)
            add_inline_markdown(p, stripped, 8.5)
            continue

        # Compact bold-label lines used for expertise, skills, education, and earlier experience.
        if stripped.startswith("**") and "**" in stripped[2:]:
            flush_paragraph()
            p = doc.add_paragraph()
            format_paragraph(p, after=0.8)
            add_inline_markdown(p, stripped, 8.9)
            continue

        pending_para.append(stripped)
        first_nonempty_after_h1 = False

    flush_paragraph()

    props = doc.core_properties
    props.title = "Mateo Castano - Staff Software Engineer - Agentic AI"
    props.subject = "Resume"
    props.author = "Mateo Castano"
    props.keywords = "Staff Software Engineer, Agentic AI, AI-Native SDLC, Software Modernization, Claude Code, .NET 10, Vue 3"
    doc.save(DOCX_PATH)
    print(f"Wrote {DOCX_PATH}")

    build_pdf(require_pdf=require_pdf)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build the canonical resume as DOCX and optionally PDF.")
    parser.add_argument("--require-pdf", action="store_true", help="Fail if PDF generation is unavailable.")
    args = parser.parse_args()
    build_docx(require_pdf=args.require_pdf)
