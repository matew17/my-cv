# Resume Agent Rules

This repository is the source of truth for Mateo Castaño's resume. These instructions apply to Codex, Claude Code, ChatGPT, and any other agent working in this repository.

## 1. Non-negotiable factual rules

- Never invent experience, dates, technologies, metrics, responsibilities, clients, job titles, certifications, outcomes, or business impact.
- Treat files under `data/` as the authoritative factual source. `master/resume.md` is the canonical narrative derived from those facts.
- A quantitative metric may be used only when it exists in `data/verified-metrics.yaml` and is marked `verified: true`.
- If a fact is missing, contradictory, or ambiguous, do not infer it. Flag it for Mateo instead.
- If Mateo corrects a fact, update `data/` first, then update the canonical resume and derived outputs.
- Never strengthen causality beyond what the facts support. Prefer wording such as "associated with" when causation was not directly measured.
- Do not fabricate work to fill employment or client-engagement gaps.
- SoftServe reserve/bench periods between client engagements are legitimate periods used for research and study. They do not need to be highlighted on the resume unless Mateo explicitly asks for a complete month-by-month timeline.
- Payworks may be named publicly in the resume.

## 2. Resume language and format

- The resume itself must always be written in English.
- Repository documentation may be in English; generated resume artifacts must be English.
- Default length: maximum two pages unless Mateo explicitly requests otherwise.
- Optimize for ATS parsing and human scanning.
- Use one column and normal document flow.
- Use standard headings such as `PROFESSIONAL SUMMARY`, `CORE EXPERTISE`, `PROFESSIONAL EXPERIENCE`, `TECHNICAL SKILLS`, and `EDUCATION`.
- Do not use layout tables, sidebars, text boxes, icons, profile photos, progress bars, skill ratings, decorative graphics, or multi-column layouts.
- Prefer concise accomplishment bullets using: action + scope + technical approach + outcome.
- Prefer production evidence, technical ownership, reliability, modernization, business impact, and leadership over generic responsibilities or long tool inventories.

## 3. Professional positioning

### Primary identity

Position Mateo primarily as:

**Staff Software Engineer | Agentic AI | AI-Native SDLC | Software Modernization**

The strategic narrative is:

> A staff-level, hands-on software engineer with 10+ years of experience building and modernizing production software, whose current specialization is applying Agentic AI and AI-native engineering practices to real software delivery.

### Primary target roles

- Staff Software Engineer - Agentic AI / AI-Native Engineering
- Staff Software Engineer with significant AI integration responsibilities
- Staff Applied AI Engineer when the role is product/software-engineering oriented rather than ML research oriented

### Adjacent targets

- AI Platform Engineer
- Agentic Systems Engineer
- Staff Software Engineer - Developer Productivity
- Staff Software Engineer - Software Modernization
- Selected Software Architect / AI Solutions Architect roles when they remain hands-on, product-oriented, and delivery-oriented

### Do not make these the default identity

- Frontend-only Engineer
- AI Architect as the primary title
- ML Researcher
- Data Scientist
- Staff ML Engineer
- "Claude Code Expert"

Mateo's frontend background is important evidence of architecture, platform engineering, modernization, and product delivery, but it should not dominate the first impression of the current resume.

Do not make Claude Code the professional identity. Claude Code is an implementation tool inside a larger engineering system. Emphasize the architecture, orchestration, verification, guardrails, and production delivery around it.

The resume should remain broad enough to support roles involving Agentic AI, AI integration into existing products, AI-native development, software modernization, developer productivity, and hands-on staff-level product engineering.

## 4. Job-title integrity

- Mateo's current SoftServe title is `Front-End - Lead Software Engineer - R&D Team`.
- The resume may simplify that title to `Lead Software Engineer - R&D Team` for clarity, but must not claim that `Staff Software Engineer` is his contractual SoftServe title.
- At Payworks, Mateo operates with Staff-level scope and leadership responsibilities, but `Staff Software Engineer` must not be presented as an official Payworks employment title unless Mateo later confirms that explicitly.
- Staff-level positioning should be demonstrated through scope, ownership, architecture, leadership, and outcomes.
- Preserve confirmed historical role titles such as the Staff Software Engineer role on Atlassian c360.

## 5. Current Payworks evidence - highest-priority experience

Payworks is the most important and differentiating current experience and should normally receive the most space in the first page.

Confirmed facts:

- Client: Payworks, Canadian company.
- Engagement: April 2026 - Present.
- Mateo personally designed the agentic engineering system/harness from scratch.
- Primary agentic tool/runtime: Claude Code.
- Harness capabilities include specialized Skills, Agents, Hooks, Commands, Workflows, MCP integrations, worktrees, guardrails, security controls, and deterministic execution patterns.
- The system is designed for semi-autonomous, human-in-the-loop software delivery.
- Legacy estate includes Classic ASP, VBScript, Visual Basic, SQL Server, multiple applications, multiple repositories, and 300+ screens.
- Payworks has many SQL Server databases, including separate databases for different clients.
- Modernization target: .NET 10 backend and Vue 3 frontend.
- The workflow analyzes legacy code, recovers business rules, logic, constraints, and expected behavior, then drives test creation and implementation.
- Engineering methodology includes TDD and automated verification.
- Backend unit testing: xUnit.
- Frontend unit testing: Vitest.
- API testing: Bruno.
- End-to-end testing: Playwright with JavaScript.
- Humans remain responsible for supervision, analysis/decision making, business clarification, resolving ambiguity, reviewing PRs, and approving outputs.
- Do not describe the system as fully autonomous.
- Do not use the literal phrase "humans never write code" in the resume. The preferred framing is `human-in-the-loop AI-native SDLC`, where agents perform much of the operational implementation and verification work while engineers provide governance and judgment.
- Mateo leads six developers and remains hands-on.
- Client-side collaboration includes a Product Manager, Architect, QA, and automation engineering functions.
- 8 migrated screens have been released to production.
- 20 additional migrated screens are pending deployment.
- Delivery velocity is approximately one migrated screen per engineer every one to two sprints.
- The team entered the engagement without prior Payworks business-domain knowledge.
- The engagement started as a five-week Jumpstart and was extended through December 2026 following successful results.

When tailoring the Payworks section, prioritize this hierarchy:

1. Architecture and ownership of the agentic system.
2. Production-grade AI-native SDLC and human-in-the-loop governance.
3. Legacy business-rule recovery and modernization architecture.
4. Automated quality and verification.
5. Staff-level technical leadership while remaining hands-on.
6. Production results and commercial validation of the engagement.

## 6. Confirmed SoftServe engagement dates

- SailPoint: Apr 2023 - Dec 2023
- Trello: Dec 2023 - Dec 2024
- Atlassian Elevate: Mar 2025 - Dec 2025
- Atlassian c360: Dec 2025 - Apr 2026
- Payworks: Apr 2026 - Present

Atlassian c360 was a focused engagement intended to bring the described enterprise sales platform to production. Preserve that production-readiness context when useful.

## 7. Career narrative to preserve

The resume should tell a coherent progression rather than presenting AI as an abrupt career pivot.

Mateo has repeatedly modernized production systems throughout his career, including:

- Visual Basic desktop applications to web solutions at Somer Clinic.
- AngularJS and older frontend stacks to modern Angular.
- Large-scale Micro Frontends and platform architecture at EPAM.
- Backbone to React modernization at Trello.
- Enterprise architecture work across Atlassian engagements.
- Agentic legacy modernization at Payworks.

This trajectory supports the current Staff + Agentic AI positioning. Use earlier frontend experience selectively as evidence of modernization, architecture, leadership, and production delivery.

## 8. Claims that deserve special care

- Never state that a manual migration "takes two months" as a measured baseline. Mateo described this as practitioner judgment, not a measured comparison.
- The verified delivery velocity is approximately one screen per engineer every one to two sprints.
- The Trello Card Repeater efficiency metric is 65% to 90%.
- The Trello User Limits work is associated with 40%+ revenue growth; do not silently rewrite that as sole or directly measured causation.
- Do not claim that the Payworks engagement extension happened for a different reason than the verified successful early results.
- Do not imply the agentic system is an unsupervised autonomous coding system.

## 9. Tailoring strategy

There is one canonical resume initially. Job-specific resumes are variants generated from the canonical facts.

For a job-specific variant:

1. Save the job description under `jobs/`.
2. Read this `AGENTS.md`, all files under `data/`, and `master/resume.md`.
3. Identify the job requirements that are directly supported by verified experience.
4. Reorder and rewrite emphasis to match supported requirements.
5. Never introduce a skill or claim merely because it appears in the job description.
6. Keep Payworks prominent for Agentic AI / AI-native / Applied AI / modernization roles.
7. Keep architectural and full-stack evidence prominent for general Staff Software Engineer roles.
8. Preserve the canonical source files; create a target-specific Markdown variant rather than overwriting the master unless Mateo explicitly asks to change the canonical resume.
9. Run factual validation before building output artifacts.

Primary market context: Colombia-based companies serving international clients, plus direct international contractor opportunities. Keep the resume internationally readable and do not over-localize the wording.

## 10. Repository architecture and build behavior

- `data/` contains verified facts and structured source data.
- `data/verified-metrics.yaml` controls which quantitative claims may be used.
- `master/resume.md` is the canonical narrative resume.
- `targets/` contains positioning notes for reusable variants.
- `jobs/` contains job descriptions used for tailoring.
- `prompts/` contains reusable agent workflows.
- `scripts/build_resume.py` builds an ATS-safe DOCX from Markdown.
- PDF is generated from DOCX when LibreOffice is available so both outputs remain aligned.
- `scripts/validate_data.py` must pass before final artifacts are considered valid.
- Generated resume files belong in `output/` and are intentionally ignored by Git.

Before finalizing any resume change, run:

```bash
make validate
make build
```

If a generated DOCX/PDF is being delivered externally, visually inspect the final two pages after rendering; do not assume that successful generation guarantees correct layout.

## 11. Dependency-management note

The repository currently uses `requirements.txt` / pip for the initial build tooling. Mateo plans to migrate it to `uv` himself later. Do not perform that migration unless explicitly requested.
