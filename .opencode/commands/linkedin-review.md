---
description: Read the live LinkedIn profile and automatically inspect its current photo and banner
agent: build
---

Review Mateo's live LinkedIn profile through this project's `linkedin-browser` MCP.
Additional direction: $ARGUMENTS

Load the linkedin-browser skill and follow its identity, profile-reading, and automatic
visual-retrieval workflow. Read verified factual sources before making recommendations.

Retrieve the current headline, About, experience, skills, and Featured sections where
accessible. Update linkedin/current-profile.md with the real observed text, including
any partial/missing sections, and compare it with linkedin/profile-draft.md.

Retrieve/capture the current profile photo and banner automatically. Inspect image
files and desktop/narrow-viewport captures and update linkedin/visual-review.md.
Do not ask Mateo to supply screenshots of existing visuals. If login is required,
let him sign in to the dedicated browser and report that blocker accurately.

Update linkedin/change-summary.md with the live comparison and evidence. This command
reviews the profile; it does not save profile edits. Run make validate and report the
actual sections/images inspected, recommendations, and unresolved issues.
