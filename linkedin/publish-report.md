# LinkedIn publish report

## Outcome

Partial publication completed on October 2, 2026, Colombia time (October 3,
approximately 03:39–03:47 UTC), through this project's `linkedin-browser` MCP.
Three fields changed and saved-state verified; four employer descriptions blocked
by source/matching discrepancies. No uncertain save outcomes remain.

Default requested scope: draft headline, About, and descriptions of confidently
matched existing employer entries. No skills, education, languages, Featured,
employment metadata, new entries, or replacement images were requested.

Identity confirmed: Mateo Castaño at the URL in `data/profile.yaml`, own activity
labeled You, `isSelfProfile=true`, and owner editing controls. Authentication was
accepted; no login/MFA/checkpoint blocker occurred.

## Preflight

- Read the draft and reviewed it against `AGENTS.md`, `data/profile.yaml`,
  `data/experience.yaml`, `data/skills.yaml`, `data/education.yaml`,
  `data/verified-metrics.yaml`, and the canonical resume, available in this session.
- `make validate` passed with no warnings. LinkedIn prose was separately reviewed.
- Character counts: headline 93/220; About 1,852/2,600; SoftServe 1,803/2,000;
  EPAM 378/2,000; Globant 357/2,000; Yuxi 136/2,000; Somer 216/2,000.
- Live About counter confirmed 1,852/2,600; Somer description control explicitly
  limits descriptions to 2,000 and showed 216/2,000 after reopening. The headline
  editor accepted 93 characters without a validation error; it did not display a
  numeric maximum in the inspected field. No larger test value was entered.
- All copied accomplishment metrics are verified entries in
  `data/verified-metrics.yaml`. Payworks human governance, employer/client integrity,
  limited .NET/xUnit exposure, and Trello revenue association are preserved.

## Per-field outcomes

| Field | Outcome | Details |
|---|---|---|
| Headline | Changed; verified | Replaced `Lead Software Engineer - R&D Team at SoftServe` with the exact 93-character draft. Saved in Edit intro; navigated back to reload; checked exact equality again after later edits. |
| About | Changed; verified | Replaced the frontend-focused About with the exact draft. Saved in Edit about; reloaded profile and reopened editor; rich-text paragraphs serialize to the exact 1,852-character draft. About top skill Angular remained unchanged. |
| Somer Clinic description | Changed; verified | Confident match to Clínica Somer / Ingeniero de proyectos / Sep 2015–Feb 2017 / Rionegro. Employer/title labels are Spanish equivalents of verified Somer Clinic / Project Engineer, with matching dates and existing PHP/SQL Server description. Saved 216-character draft; reloaded experience details and reopened position 790176477; exact equality confirmed. |
| SoftServe description | Blocked; untouched | Three existing roles: Jan 2026–Present R&D title, Nov 2023–Present Software Development Lead, and Apr–Nov 2023 Software Development Lead. Draft spans Apr 2023–Present under one employer/current title. Historical role periods and two overlapping active entries are unconfirmed. Cannot choose where to apply the aggregate description without guessing. |
| Globant description | Blocked; untouched | Draft covers Feb 2018–Jun 2021 with a combined title; live splits Web UI Developer (Feb 2018–Jul 2019) and Technical Lead (Jun 2019–Jun 2021). No verified split-role dates or confirmed destination for the aggregate description. |
| EPAM description | Blocked; untouched | Live EPAM Anywhere tenure ends Apr 2023; verified EPAM ends Mar 2023. Exact end-date/employer-label correspondence remains unresolved. No automatic correction or save performed. |
| Yuxi Global description | Blocked; untouched | Live Software Developer vs verified Front End Developer. Dates agree, but the title discrepancy remains unresolved; no automatic title equivalence asserted. |

No intended eligible field already matched before writing, so none was skipped as
already matching. Huge and Unisys remain untouched: they have no draft entries and
are absent from authoritative experience data. All other sections remained outside
the publishing scope. No positions were merged, removed, added, or retitled.

## Saved-state evidence

All runtime evidence is under ignored `output/linkedin/`:

- `publish-headline-before.yml` / `publish-headline-after.yml` — intro before and
  reloaded headline after save.
- `publish-profile-saved.json` — second reloaded profile observation; headline
  compared programmatically with the draft, exact match.
- `publish-about-before.yml` / `publish-about-filled.yml` — original editor and
  intended text entered, before save.
- `publish-about-saved.json` — reopened editor's rendered text.
- `publish-about-saved-normalized.json` — paragraph serialization, exact match to
  the draft; counter 1,852/2,600; top skill Angular.
- `publish-experience-before.yml` / `publish-experience-after.yml` — reloaded
  experience details before/after, including blocked entries.
- `publish-somer-before.json` / `publish-somer-saved.json` — description and other
  form values before/after reopening. Programmatic comparison confirmed exact
  description equality and unchanged inspected inputs/selects/switch values,
  including dates, title, employer, location, employment/location types, current-role
  checkbox, skill checkboxes, and existing Notify network setting (On).
- `publish-experience-saved.json` — displayed experience text after saving Somer.

LinkedIn offered upsell/next-action screens after Save. These were left by navigating
back to the profile/details page. No optional follow-up action was applied; success
is based on reloaded/reopened values rather than the Save click or redirect.

## Visual observations after publication

Automatically retrieved current displayed photo/banner (HTTP 200) and captured
desktop, narrow-browser, and element crops. Opened all six with an image-capable tool:

- `publish-photo-displayed.jpg`
- `publish-banner-displayed.jpg`
- `publish-photo-rendered.png`
- `publish-banner-rendered.png`
- `publish-profile-desktop.png` (1440 × 1000 browser viewport)
- `publish-profile-narrow.png` (390 × 844 browser viewport)

The newly saved headline is fully visible, wrapping to two desktop lines and three
narrow-browser lines in these captures. The current photo/banner appear unchanged.
The banner still says Front-end Developer | Tech Lead and its secondary text is tiny
at narrow width; no replacement asset was requested/uploaded. Photo lighting,
background, sharpness, and circular-crop findings remain as recorded in
`visual-review.md`. Narrow-browser review is not a native-mobile-app test.

## Remaining decisions

1. Confirm the intended SoftServe role history and which existing entry should
   receive the aggregate verified description; update historical facts in `data/`
   first if needed.
2. Confirm Globant's role split and the appropriate destination/scope for its copy.
3. Resolve EPAM's end month/naming and Yuxi's title before applying those descriptions.

`current-profile.md` now contains observed saved values for the three changed fields;
other experience entries retain their observed unchanged text. Earlier skills,
education, language, Featured, and certification observations are explicitly dated
as review evidence, not freshly verified writes. Source facts and resume files did
not change; resume artifacts were not rebuilt. No commit or push was performed.
