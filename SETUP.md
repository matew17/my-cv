# Setup Checklist

Run commands from the repository root. See [README.md](README.md) for the full workflow and PDF troubleshooting.

## 1. Install uv (macOS with Homebrew)

```bash
brew install uv
```

If already installed, check with `uv --version`. Other platforms: [uv installation guide](https://docs.astral.sh/uv/getting-started/installation/).

## 2. Open the project

Open a terminal in your existing checkout, or clone it:

```bash
git clone https://github.com/matew17/my-cv.git
cd my-cv
```

## 3. Install Python and dependencies

```bash
uv sync
```

uv manages Python 3.12 and `.venv` automatically. No manual environment activation is needed.

## 4. Validate and build

```bash
make validate
make build
```

Expected validation message: `Data validation passed with no warnings.`

The DOCX appears in `output/`. PDF generation is skipped with a message if LibreOffice is unavailable.

## 5. Generate and inspect the PDF

```bash
brew install --cask libreoffice
make pdf
open output/Mateo_Castano_Staff_Agentic_AI.pdf
```

Skip the installation command if LibreOffice is already installed. `make pdf` fails if conversion is unavailable or unsuccessful. Check the result has at most two pages, readable/selectable text, no clipped content, and sensible page breaks before sharing it.

## 6. Try the agent-driven workflow

Open the repository with your AI coding assistant and start with:

```text
Read AGENTS.md before doing anything else.
Inspect data/ and master/resume.md.
Explain any factual inconsistency you find instead of guessing.
Then run make validate and make build without changing verified facts.
```

For a job application, save the job description under `jobs/` and use `prompts/tailor-resume.md`. The current builder only builds `master/resume.md`; it does not accept a variant path.
