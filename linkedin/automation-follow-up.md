# Direct LinkedIn update investigation

## Requested outcome

Mateo wants the assistant to apply profile changes directly, rather than manually
copying drafts, and to retrieve and assess the current profile photo and banner
automatically. Manually supplied screenshots must not be required. Research findings
and project-local options are in `automation-research.md`.

## Research questions

1. Consult current official LinkedIn developer documentation for personal-profile
   write capabilities: headline, About, employment descriptions, skills, photo,
   and banner. Distinguish these from APIs for posting content or managing company pages.
2. Assess candidate MCP servers against their actual documented tools and implementation.
   A server that can read profiles or create posts is not necessarily able to edit a profile.
3. Evaluate browser automation, such as Playwright MCP, if an API/connector cannot
   perform the required edits. Test current selectors and authenticated-session handling;
   do not assume a generic browser MCP is a ready-made LinkedIn integration.
4. Determine how Mateo logs in interactively and how a session can be reused without
   placing credentials, tokens, or cookies in this repository.
5. Record reliability limits, platform constraints, and which fields can actually be updated.

## Evidence to return

- Dated findings with links to primary documentation or reviewed implementation.
- Capability matrix: read text, edit each text field, upload photo, upload banner,
  retrieve visuals, verify changes after saving.
- Recommended route, installation/configuration steps, and any access requirements.
- Clearly identified unsupported fields and untested assumptions.

## Proposed integration behavior, if feasible

Extend the workflow to compare the live profile with the verified draft, apply only
the intended changes, then reread the saved values and inspect the resulting visuals.
Update `current-profile.md` only from verified saved state. Report actual changes
separately from drafted or failed changes; do not report success merely because a
Save button was clicked. Preserve existing unrelated profile information.

For images, retrieve and review the current photo/banner through the authenticated
browser integration before considering an upload. Capture rendered crops automatically.
The brief does not presume the current photo or banner needs replacement.

## Implementation status before this draft-sync run

Research completed October 2, 2026; see `automation-research.md`. Recommended first
route: project-local Playwright MCP with a dedicated persistent session. The connector
is now installed/configured and MCP connectivity and Chrome startup passed verification.
Review/publish commands and a browser skill are available. Login and actual LinkedIn
reading/editing/image retrieval remain pending live verification. No profile edit or
image upload has been performed.

## Draft-sync verification — October 2, 2026

The existing project-scoped browser successfully accessed Mateo's profile with
owner controls and an authenticated session. The current displayed photo and banner
were downloaded (HTTP 200), rendered element/header captures were saved, and desktop
and narrow-browser views were inspected. See `visual-review.md` for the actual files.
The headline and visible About text were read for a limited comparison; expanding
About timed out, and full section retrieval was not completed. `current-profile.md`
was preserved unchanged during this sync.

This establishes live profile access and visual retrieval for this run; it does not
establish any text-field or image-write capability. Saved-state persistence, full
experience matching, skill dialogs, replacement-image crop controls, and live UI
limits remain untested. No connector was installed during this sync and the research
above is preserved. Publishing remains a separate `/linkedin-publish` action.
No live edits or image uploads occurred.

## Partial publication verification — October 2, 2026

The later requested publish run successfully saved the headline, About, and matched
Somer description through actual editing dialogs. Reload/reopen comparisons verified
the stored values against the draft; Somer's other inspected form values were
preserved. Photo/banner downloads and rendered desktop/narrow captures succeeded
again; no replacement image was uploaded. See `publish-report.md` for field evidence.

SoftServe/Globant aggregate descriptions could not be mapped to split live roles
without confirmation; EPAM's end month/naming and Yuxi's title remain discrepant.
Those descriptions were not saved. Skills, education, language, Featured, new-entry,
and replacement-image writes remain untested in this integration.
