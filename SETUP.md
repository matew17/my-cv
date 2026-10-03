# Setup Checklist

This project is intended to live at:

`https://github.com/matew17/my-cv.git`

## 1. Put the project in the existing clone

```bash
cd /path/to/my-cv
```

Copy all files and directories from this project into that repository root.

## 2. Verify Git remote

```bash
git remote -v
```

Expected origin:

```text
https://github.com/matew17/my-cv.git
```

If needed:

```bash
git remote add origin https://github.com/matew17/my-cv.git
# or
git remote set-url origin https://github.com/matew17/my-cv.git
```

## 3. Install current dependencies

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

`uv` migration is intentionally deferred for Mateo to do later.

## 4. Validate

```bash
make validate
```

Expected result:

```text
Data validation passed with no warnings.
```

## 5. Build

```bash
make build
```

Artifacts are written to `output/`.

## 6. Try the agent-driven workflow

Open the repository with Codex / Claude Code and start with:

```text
Read AGENTS.md before doing anything else.
Inspect data/ and master/resume.md.
Explain any factual inconsistency you find instead of guessing.
Then run make validate and make build without changing verified facts.
```

For an actual job application, save the job description under `jobs/` and use `prompts/tailor-resume.md`.

## 7. Commit

```bash
git add .
git commit -m "Initialize version-controlled resume project"
git push -u origin main
```
