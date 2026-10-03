# Mateo Castaño - Resume Project

Version-controlled, ATS-safe resume project designed to be maintained with Git and AI coding assistants without allowing invented claims.

Repository: `https://github.com/matew17/my-cv.git`

## Architecture

- `AGENTS.md` - mandatory rules and career-positioning context for Codex/Claude/other agents
- `data/profile.yaml` - contact details and professional positioning
- `data/experience.yaml` - verified employment and engagement facts
- `data/verified-metrics.yaml` - quantitative facts allowed in resume variants
- `data/skills.yaml` - verified technologies and capability areas
- `data/education.yaml` - education
- `master/resume.md` - canonical two-page narrative
- `targets/` - reusable positioning notes
- `jobs/` - job descriptions for targeted variants
- `prompts/` - reusable tailoring and validation prompts
- `scripts/build_resume.py` - Markdown -> ATS-safe DOCX/PDF build
- `scripts/validate_data.py` - source-data validation

## Generated outputs

The default build generates:

- `output/Mateo_Castano_Staff_Agentic_AI.docx`
- `output/Mateo_Castano_Staff_Agentic_AI.pdf` when LibreOffice is available

New generated output files are ignored by Git. Artifacts already tracked in the initial repository remain tracked until explicitly removed from Git's index.

## Quick start (macOS)

### 1. Install uv

If you use [Homebrew](https://brew.sh/):

```bash
brew install uv
```

Already installed? Check with `uv --version`. For other installation methods and operating systems, see the [uv installation guide](https://docs.astral.sh/uv/getting-started/installation/).

### 2. Open the repository

If you already have this project, open a terminal in its folder. Otherwise:

```bash
git clone https://github.com/matew17/my-cv.git
cd my-cv
```

Run all subsequent commands from the repository root, where `Makefile` lives.

### 3. Install the Python environment

```bash
uv sync
```

uv downloads Python 3.12 if needed, creates `.venv`, and installs the versions recorded in `uv.lock`. Dependencies are declared in `pyproject.toml`. You do not need to activate the environment or run pip manually.

### 4. Build the resume

```bash
make build
```

This validates the source data first, then creates the DOCX in `output/`. It also creates the PDF if LibreOffice is installed; otherwise it prints a clear skip message.

## Generate and verify the PDF

PDF conversion requires LibreOffice, installed separately from Python dependencies:

```bash
brew install --cask libreoffice
make pdf
```

The builder checks both your command path and the standard macOS application location, so no manual PATH change is needed for a normal Homebrew installation.

`make pdf` validates the data, rebuilds the DOCX, and **fails if LibreOffice is missing or conversion fails**. Conversion uses a temporary directory and an isolated LibreOffice profile, checks for a nonempty PDF with a PDF header, and only then publishes the result. A stale PDF is removed before conversion so it cannot be mistaken for a fresh build.

Open the result on macOS:

```bash
open output/Mateo_Castano_Staff_Agentic_AI.pdf
```

Before sending it, check that:

- It contains at most two pages, with no extra blank page.
- Headings, bullets, and contact details are readable and not clipped.
- Page breaks are sensible and all expected sections are present.
- You can select/copy text, including the contact details.

Successful conversion does not enforce the two-page limit or prove factual accuracy. If conversion fails, read the terminal error, check that LibreOffice can open the DOCX, and rerun `make pdf` after addressing the issue.

## Everyday workflow

```bash
make validate  # Check dates and metric verification flags
make build     # Validate and generate DOCX; also PDF when LibreOffice is installed
make pdf       # Validate and build, requiring successful PDF generation
make clean     # Remove generated DOCX/PDF files and _build/
```

The builder reads `master/resume.md`, not the YAML data directly. After changing facts under `data/`, update the Markdown narrative as needed. The validator checks dates and verification flags; it does not compare every resume claim against the source facts.

If `make` is unavailable, the equivalent commands are:

```bash
uv run python scripts/validate_data.py
uv run python scripts/build_resume.py --require-pdf
```

Run validation first when invoking the scripts directly. Commit `pyproject.toml` and `uv.lock` together when changing dependencies.

## Using Codex / Claude Code in this repository

Open the repository root so the agent can discover `AGENTS.md`.

A safe first request is:

```text
Read AGENTS.md first, then inspect data/ and master/resume.md.
Validate that the canonical resume uses only verified facts.
Do not invent or infer missing information.
If changes are required, update the source data first when facts change,
then update master/resume.md, run make validate, and run make build.
```

To improve the canonical resume without changing facts:

```text
Read AGENTS.md and all files under data/.
Review master/resume.md for Staff Software Engineer roles focused on
Agentic AI, AI-native software engineering, software modernization,
and hands-on product delivery. Improve wording and prioritization only.
Do not add unsupported technologies, dates, metrics, titles, or outcomes.
Keep the result to two ATS-safe pages. Run make validate and make build.
```

## Tailoring for a job

1. Save the full job description as, for example:

```text
jobs/company-staff-ai.md
```

2. Ask the agent:

```text
Read AGENTS.md, all files under data/, master/resume.md,
and jobs/company-staff-ai.md.
Create a job-specific Markdown resume variant using only verified facts.
Match supported requirements from the job description without keyword stuffing
or inventing experience. Keep Payworks prominent when the role involves
Agentic AI, Applied AI, AI-native development, developer productivity,
or modernization. Keep the output to two ATS-safe pages.
Validate all claims before building.
```

3. Use `prompts/tailor-resume.md` and `prompts/validate-claims.md` as reusable agent instructions.

## Editing facts

When a real career fact changes:

1. Update the appropriate file under `data/`.
2. Add or update metrics in `data/verified-metrics.yaml` only when they are verified.
3. Update `master/resume.md` if the canonical narrative should change.
4. Run:

```bash
make validate
make build
```

Do not edit the DOCX as the source of truth. DOCX and PDF are build artifacts.
