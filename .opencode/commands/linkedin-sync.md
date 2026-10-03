---
description: Refresh LinkedIn copy from verified facts and review current visuals through the project browser
agent: build
---

Update Mateo's LinkedIn drafts in this repository. Additional direction: $ARGUMENTS

## Read first

Read AGENTS.md, every file under data/, master/resume.md, and linkedin/README.md.
Read linkedin/current-profile.md, linkedin/profile-draft.md, linkedin/change-summary.md,
linkedin/visual-review.md, linkedin/automation-follow-up.md, and linkedin/automation-research.md if they exist.
Inspect linkedin/assets/ for supplied profile photos, banners, and screenshots.

## Factual and positioning rules

- data/ is authoritative; the current LinkedIn snapshot is comparison material, not verified evidence.
- Write profile copy in English, using a natural first-person About and concise experience descriptions.
- Lead with hands-on Staff-level software engineering, Agentic AI, AI-native SDLC, and modernization.
- Keep SoftServe as the employer. Present Payworks, Atlassian, Trello, and SailPoint as client engagements inside its description, not separate employment.
- Use the confirmed SoftServe title; never convert Staff-level scope into an official employment title.
- Use quantitative accomplishment claims only from verified: true entries in data/verified-metrics.yaml.
- Preserve Trello's revenue association rather than implying sole causation.
- Describe human-in-the-loop engineering, never an unsupervised or fully autonomous delivery system.
- Respect project_specific_exposure in data/skills.yaml. C#, .NET 10, and xUnit may describe Payworks' stack, but must not appear as core skills or imply strong proficiency.
- Do not invent motivations, availability, endorsements, certifications, public projects, preferences, or proficiency levels.
- Flag discrepancies rather than silently treating old profile claims as verified facts.

## Update outputs

1. Rewrite linkedin/profile-draft.md with clearly delimited copy-ready sections:
   headline, About, each employer's title/dates/description, education, languages,
   prioritized skills, and Featured suggestions. Recommendations must be outside profile copy.
   Check the actual headline text is at most 220 characters, About at most 2,600,
   and each experience description at most 2,000. Count characters, not tokens;
   do not count file headings or editorial notes. Recheck platform limits if publishing later.
2. Update linkedin/change-summary.md with source references for major claims and every metric,
   differences from the prior draft, differences from the current profile when supplied,
   unresolved facts, and sections needing input. If the current profile is missing,
   explicitly call this a source-derived draft, not a live-profile audit.
3. Retrieve the current profile photo and banner through the project-scoped browser
   integration when available; load the linkedin-browser skill for live browser work. Capture
   rendered crops automatically and retrieve displayed image files where accessible.
   Update linkedin/visual-review.md after inspecting the retrieved images/captures
   with an image-capable tool. Supplied assets may supplement this review.
   Assess photo lighting, sharpness, background, circular crop, and approachable presentation.
   Assess banner contrast, readability, desktop/mobile cropping, avatar overlap, and alignment
   with the professional narrative. State which images were actually inspected.
   Do not infer personal traits or protected attributes from appearance.
   Do not require Mateo to supply screenshots of existing visuals. If no browser
   integration is configured or authentication/access fails, mark the assessment
   pending with that specific blocker. Continue the text work independently.
   Keep suggested banner copy grounded in the verified positioning.
4. Preserve linkedin/current-profile.md as the recorded live snapshot. A generated draft is
   not evidence that LinkedIn changed; never replace the snapshot with unposted draft text.
5. Preserve the direct-update investigation in linkedin/automation-follow-up.md.
   When explicitly asked to investigate publishing, consult current primary documentation
   and assess actual read/write capabilities and authentication before installing a connector.
   Publishing uses /linkedin-publish; this sync command generates drafts and reviews
   visuals but does not save live edits. Do not claim a live update occurred.

## Verify and report

Run make validate. Review the draft against the factual sources and character limits;
the existing validator does not validate LinkedIn prose. Build resume artifacts only if
resume source files were also changed, following AGENTS.md.

Summarize changed files, the proposed headline, verification results, and missing inputs.
Report separately whether content was drafted, visuals were inspected, or LinkedIn was
actually updated. Do not commit or push unless requested.
