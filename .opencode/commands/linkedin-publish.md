---
description: Apply verified LinkedIn draft fields to the live profile and verify saved changes
agent: build
---

Publish Mateo's verified LinkedIn draft using this project's `linkedin-browser` MCP.
Requested scope: $ARGUMENTS

Load the linkedin-browser skill and follow its factual checks, identity verification,
field matching, publishing, and saved-state verification workflow.

Read linkedin/profile-draft.md and the authoritative sources. By default update the
headline, About, and descriptions of confidently matched existing employer entries.
If arguments specify a narrower scope, apply only that scope. Explicit requests may
include skills, education, languages, new entries, Featured items, or replacement
images when the required confirmed values/assets are available.

Run make validate and check character limits. Read current values first; skip matching
values. Preserve unrelated profile information and client/employer/title integrity.
Use actual editing dialogs, then reload/reopen to verify each saved field. Stop and
report specific authentication or ambiguous-entry blockers instead of guessing.

Retrieve the current photo/banner and capture rendered crops automatically when
reviewing or changing visuals. Do not require manually supplied screenshots.

Update linkedin/current-profile.md from observed saved values and write
linkedin/publish-report.md with per-field outcomes and evidence. Summarize what was
actually changed, unchanged, blocked, or uncertain. Do not commit or push unless asked.
