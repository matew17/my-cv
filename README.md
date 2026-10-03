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

Generated output files are ignored by Git.

## First-time setup in the existing empty clone

The intended local repository is already:

```bash
git clone https://github.com/matew17/my-cv.git
cd my-cv
```

If the clone already exists, copy the contents of this project into that repository root. Then verify the remote:

```bash
git remote -v
```

If `origin` is missing:

```bash
git remote add origin https://github.com/matew17/my-cv.git
```

If `origin` points somewhere else:

```bash
git remote set-url origin https://github.com/matew17/my-cv.git
```

Create a virtual environment and install the current build dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

Validate the source data:

```bash
make validate
```

Build the resume:

```bash
make build
```

The generated files will appear under `output/`.

> Dependency management intentionally remains on `requirements.txt` / pip for this version. Mateo plans to migrate the project to `uv` separately.

## Initial Git commit

After validating and building locally:

```bash
git status
git add .
git commit -m "Initialize version-controlled resume project"
git push -u origin main
```

If the default branch is not `main`, use the branch configured in the GitHub repository.

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
