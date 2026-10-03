# LinkedIn change summary

## Scope

Latest status: subsequent default-scope publication changed and verified the
headline, About, and Somer description. SoftServe, Globant, EPAM, and Yuxi description
updates were blocked by the discrepancies below. See `publish-report.md` for
per-field results and saved-state evidence. `current-profile.md` now reflects the
actually saved values. The review findings below describe the pre-publication state.

Source-derived draft with a live-profile comparison, reviewed October 2, 2026,
Colombia time (October 3 UTC). `data/` remains authoritative. During the earlier
sync, only the headline/visible About and visuals were compared. This review now
records actually observed profile values in `current-profile.md`: headline, expanded
About, ten experience positions, all 55 displayed skill labels, education/language
previews, and two certification previews. No Featured section was displayed after
the profile's lower sections loaded. Full certifications and credential links were
not reviewed. No live profile fields were saved or images uploaded.

Evidence in ignored `output/linkedin/`: `review-profile.yml`,
`review-experience.yml`, `review-skills.yml`, and the six `review-*.jpg/png` files
listed in `visual-review.md`. Browser snapshots/DOM text establish the comparison;
they do not verify career claims. The initial sync evidence remains separate.

## Editorial decisions

- Use hands-on Staff-level positioning in the headline while preserving the exact confirmed SoftServe employment title, `Front-End - Lead Software Engineer - R&D Team`.
- Make About a first-person modernization narrative, with Payworks as the current differentiator.
- Keep client engagements inside SoftServe rather than representing clients as employers.
- Emphasize engineering-system ownership, human judgment, quality, and production delivery over a tool inventory.
- Keep C#, .NET 10, and xUnit contextual, reflecting Mateo's confirmed limited proficiency.
- Give earlier roles concise, relevant descriptions rather than fitting the LinkedIn profile to the resume's two-page constraint.

## Claim sources

| Claim | Authoritative reference |
|---|---|
| Identity, location, headline positioning, languages | `data/profile.yaml` → name/location/positioning/languages; `AGENTS.md` §3 |
| Employment titles, dates, client relationships | `data/experience.yaml` employer and engagement entries |
| Personally built the harness, capabilities, human-in-the-loop workflow | `data/experience.yaml` → SoftServe → Payworks → architecture/workflow |
| Payworks stack and test tools | `data/experience.yaml` → Payworks → source_stack/target_stack/testing |
| Leadership of six developers | `data/verified-metrics.yaml` → payworks.team.developers (`payworks.team.verified: true`) |
| 300+ legacy screens | `data/verified-metrics.yaml` → payworks.legacy_screens |
| 8 released; 20 pending | `data/verified-metrics.yaml` → payworks.released_screens/additional_screens_pending_deployment |
| Approximately one screen per engineer every one to two sprints | `data/verified-metrics.yaml` → payworks.delivery_velocity |
| Five-week Jumpstart and extension through December 2026 | `data/verified-metrics.yaml` → payworks.initial_engagement/engagement_extension; successful-results context in `data/experience.yaml` |
| Trello efficiency from 65% to 90% | `data/verified-metrics.yaml` → trello.card_repeater_efficiency |
| Trello work associated with 40%+ revenue growth | `data/verified-metrics.yaml` → trello.user_limits_revenue_impact; association in `data/experience.yaml` |
| Somer delivery of 15+ systems | `data/verified-metrics.yaml` → somer_clinic.internal_systems_delivered |
| c360 enterprise sales architecture, React/TypeScript/GraphQL/Node.js BFF, production readiness | `data/experience.yaml` → SoftServe → Atlassian/c360 → accomplishments/engagement_context |
| Elevate enterprise HR architecture, domain boundaries, accessibility, performance budgets | `data/experience.yaml` → SoftServe → Atlassian/Elevate → accomplishments |
| Backbone-to-React and Node.js work queue; User Limits subscription/billing work | `data/experience.yaml` → SoftServe → Trello.com → accomplishments |
| SailPoint AngularJS-to-Angular component-library migration, quality, UX, reviews | `data/experience.yaml` → SoftServe → SailPoint → accomplishments |
| EPAM Micro Frontends, Webpack 5 Module Federation, independent deployments, shared library, Kantar | `data/experience.yaml` → EPAM → accomplishments |
| Globant Disney delivery, Angular reservation SPA, stakeholder collaboration | `data/experience.yaml` → Globant → accomplishments |
| Yuxi production AngularJS/Angular features and English-language client collaboration | `data/experience.yaml` → Yuxi Global → accomplishments |
| Somer Project Engineer/Scrum Master, Visual Basic-to-PHP/jQuery modernization, SQL Server | `data/experience.yaml` → Somer Clinic → title/accomplishments |
| Core skills and limited C#/.NET/xUnit proficiency | `data/skills.yaml`, especially project_specific_exposure |
| Education | `data/education.yaml` |

Technology versions and employment dates describe verified context, not accomplishment metrics.
All quantitative accomplishments retained in the draft appear in the metric rows
above and have `verified: true` in `data/verified-metrics.yaml`. Team size, production
counts, pending counts, estate size, delivery velocity, Jumpstart duration, extension,
Trello efficiency/revenue, and Somer delivery count were checked individually.
The extension's successful-results rationale comes from `data/experience.yaml`, not
the metric value alone. Pending screens are not described as production releases.
No manual-migration baseline or speedup is asserted. Earlier team sizes without
verified metric entries are omitted.

The prior About's “10+ years” is removed to avoid introducing an accomplishment
quantity outside the metric ledger; the modernization progression is retained through
named, verified work. No strong C#/.NET/xUnit proficiency is asserted: .NET 10 and
xUnit occur only in the Payworks stack, and C# is excluded from profile copy.

## Differences from the prior draft

- Headline now explicitly leads with hands-on Staff-level engineering and uses
  separate Agentic AI / AI-Native SDLC keywords (93 characters rather than 116).
- About starts with the intended engineering identity, gives human supervision and
  decision-making explicit space, adds verified client collaboration, and connects
  Somer's desktop modernization to the current work. Removed subjective “deeper
  technical background” wording and the numerical tenure shorthand.
- SoftServe uses the exact official title rather than its resume simplification.
  The description remains a single employer entry, with all five client engagements,
  confirmed historical client role labels, and Payworks receiving the most space.
- Shortened SoftServe copy while retaining every previously included verified metric
  and the revenue-association qualifier. Earlier employer descriptions retain their
  factual scope and concise wording.
- Delimited each employer's title, dates, and location separately; added delimited
  education and languages. Skills, entry-mapping advice, and Featured suggestions
  are clearly outside profile copy.
- Featured suggestions distinguish proposed new material from verified public assets;
  the observed talk preview is a confirmation lead, not a new career claim.
- Replaced the pending visual brief with observations from retrieved files and actual
  desktop/narrow-browser crops. Direct-update research is preserved.

## Comparison with the current live profile

Observed headline: `Lead Software Engineer - R&D Team at SoftServe`.
The proposed headline adds Staff-level scope, Agentic AI, AI-native SDLC, and
modernization. Staff-level is positioning, not a substituted SoftServe employment title.

The expanded About begins:

> I am a passionate Front-end Developer and Tech Lead with over 9 years of experience in building modern, scalable, and high-performance web applications. My expertise lies in TypeScript, Angular, and front-end architecture, ensuring seamless user experiences and maintainable codebases.

Further paragraphs describe thriving in fast-paced environments, mentoring,
optimizing workflows, exploring technologies, and an invitation to connect. The
“… more” expansion succeeded in this review and the full displayed text is recorded
in `current-profile.md`. This supersedes the earlier sync's timed-out expansion.
The draft replaces frontend-first and motivational phrasing with verified ownership,
governance, modernization, and production evidence. The old tenure claim is not
adopted as an authoritative fact.

### Experience comparison and publication matching

| Observed live value | Verified source / draft | Recommendation or unresolved issue |
|---|---|---|
| SoftServe has `Lead Software Engineer - R&D Team` (Jan 2026–Present), `Software Development Lead` (Nov 2023–Present), and `Software Development Lead` (Apr–Nov 2023) | `data/experience.yaml` confirms employer tenure Apr 2023–Present and current official title `Front-End - Lead Software Engineer - R&D Team`; draft represents one employer entry | Current role start date and historical title periods are not verified in `data/`. The two open-ended live roles overlap. Confirm intended role history before matching the single draft description to an existing entry; do not merge/delete/create entries automatically. |
| Current SoftServe role has no displayed description; middle role says only `Senior developer at trello.com` | Verified Payworks, c360, Elevate, Trello, SailPoint client engagements inside SoftServe | Add the verified engineering-system ownership and client progression in the intended SoftServe description after matching is resolved. The Trello-only line does not represent current scope. |
| EPAM Anywhere, Lead Software Engineer, Sep 2021–Apr 2023; no displayed description | Verified company `EPAM`, Sep 2021–Mar 2023 | One-month end-date discrepancy and employer naming need confirmation. Proposed description adds verified Module Federation/Micro Frontends, shared library, and Kantar work. |
| Huge, Associate tech lead, Jun–Sep 2021 | No entry in `data/experience.yaml` | Unverified additional role. Ask Mateo to confirm employer, title, dates, and scope in `data/` if it should enter the narrative. Preserve live entry during future scoped publishing. |
| Globant has Technical Lead (Jun 2019–Jun 2021) and Web UI Developer (Feb 2018–Jul 2019); both have no displayed description | Verified combined title `Web UI Developer and Technical Leader`, Feb 2018–Jun 2021 | Individual promotion dates/titles are not independently verified. Live roles overlap in Jun/Jul 2019. Confirm split-role mapping before applying the single draft description; add Disney/architecture evidence to the appropriate role without duplicating it. |
| Yuxi Global, Software Developer, Feb 2017–Feb 2018 | Verified title `Front End Developer`, same dates | Resolve title-label difference. The draft turns generic/motivational description into verified production AngularJS/Angular and English-language client collaboration evidence. |
| Clínica Somer, Ingeniero de proyectos, Sep 2015–Feb 2017 | Verified Somer Clinic, Project Engineer, same dates | Spanish/English labels need field mapping, not a fabricated title change. Draft adds verified desktop-to-web modernization and 15+ systems, with metric source above. Live SQL Server 2012 version is not adopted from the snapshot. |
| Unisys, TECH SUPPORT REP 2, Aug 2012–Sep 2015 | No entry in `data/experience.yaml` | Unverified additional role and client/support claims. Keep snapshot text separate; confirm in `data/` before using it in the draft. Preserve live entry during future scoped publishing. |

No observed experience description mentions the verified Payworks harness, production
results, Atlassian architectural scope, or Trello accomplishment metrics. Their proposed
inclusion is source-derived, not evidence that the profile has already changed.

### Skills and Featured

All 55 displayed skill labels were retrieved. The detail list starts with Artificial
Intelligence (AI), Spec-Driven Development, TypeScript, Agile Methodologies, and
Technical Leadership, while the About top-skill selection still shows only Angular.
The list is broader than the About suggests, but lacks the exact draft priority labels
Software Architecture, Legacy Modernization, Agent Orchestration, and AI-Assisted SDLC.
Consider supported additions/reordering using actual available LinkedIn picker labels;
do not assume a draft label is available. Technical Leadership, TypeScript, JavaScript,
React.js, Angular, Node.js, GraphQL, REST APIs, Code Review, and Microsoft SQL Server
already provide overlap with verified sources.

Spec-Driven Development, Graphic Design Principles, `Docks`, Express.js, and other
observed labels not explicitly established in `data/skills.yaml` should not be promoted
as new verified specializations. `Docks` is recorded exactly as displayed; do not infer
it means Docker. C#, .NET, and xUnit were not among the observed 55 labels and remain
excluded from recommended core skills. Existing endorsements are preserved and are
not evidence of verified proficiency.

No Featured heading, card, or link appeared even after loading lower profile sections.
No current Featured item could be compared. This is non-display in this session, not
proof that none exists in stored data or other views. Activity is a separate section.
A visible talk preview may be a future Featured lead after verification, not a verified
public recording or an existing Featured entry. The draft's proposed article/diagram
are suggestions to prepare, not assets confirmed to exist.

### Education, languages, and credential previews

Main-profile education reads `Corporacion Universitaria Remington` / `Engineer’s
Degree, Ingenieria de sistemas` / 2010–2015, and `sena` / `Especializacion tecnologica,
Seguridad informatica` / 2015–2016. Verified `data/education.yaml` supplies UNIREMINGTON /
Systems Engineer / June 2015 and SENA / Technology Specialist in Computer Network
Security / March 2016. Completion years align, but study start years and LinkedIn
degree equivalence are not verified; retain confirmed credential wording and resolve
picker mappings rather than importing the old start dates.

Live English says `Full professional proficiency`; verified `data/profile.yaml` says
`Professional working proficiency`. Use the verified lower label in the draft unless
Mateo confirms an update in `data/`. Spanish's `Native or bilingual proficiency` is a
platform display label compatible with the verified Native entry. The skills page's
English association says `EF SET Certificate - C2 proficient`; the authoritative data
does not verify that credential or C2 level.

The main profile previews `Claude Code in Action` (Anthropic) and `Devin Foundations
Badge` (Cognition), issued March 2026. These and the unreviewed remainder of the nine
displayed licenses/certifications require factual confirmation before adding credential
claims. No proficiency upgrade or new certification was added to the draft.

The live banner says `Front-end Developer | Tech Lead`, which is narrower than the
verified current positioning. See `visual-review.md` for inspected images and crops.

## Unresolved facts and sections needing input

- Mateo's confirmation is needed for SoftServe's overlapping current roles and
  historical title periods, Globant's split roles, EPAM's end month/naming, Yuxi's
  title, and Huge/Unisys entries absent from verified sources. Future publishing
  cannot confidently match the single SoftServe/Globant draft entries yet.
- Education start dates and exact LinkedIn institution/credential picker mappings
  are not in `data/`; no dates or degree equivalences were invented.
- The live shortened headline/current-role title differs from the official title's
  formatting. This is a display comparison, not evidence of an employment-title change.
- English proficiency and observed credential labels need confirmation if Mateo
  wants to revise the authoritative language/credential data. Full certification
  details, credential destinations, and a native-mobile-app view were not inspected.
- Current production counts and engagement outcomes are taken as recorded in `data/`.
  Any later change must be confirmed there before refreshing the draft.
- Confirm an existing public article, diagram, repository, talk recording/slides, or
  reviewed resume PDF before selecting Featured items. A visible spec-driven AI talk
  preview is not yet verified in `data/`.
- No availability, work-location preference, motivation, new certification, endorsement,
  or proficiency claim is drawn from the profile. Observed recruiter settings were
  outside the requested copy scope.
- A replacement banner asset would need to be selected/created and crop-tested if
  Mateo decides to publish one; the present review proposes wording only.

Direct-update investigation is tracked in `automation-follow-up.md`.

## Verification

Publication preflight also passed `make validate` and character counts. Reopened
About and Somer values and a reloaded headline matched the draft exactly (rich-text
paragraph serialization used for About); Somer's inspected non-description form
values were unchanged. Partial publication is recorded separately in
`publish-report.md`; the historical review-only outcomes below are not the latest
publication status.

- `make validate` passed; source references above were reviewed separately because the validator does not check LinkedIn prose.
- Copy-field lengths, counting the actual field text with internal spaces, punctuation,
  and line breaks, excluding COPY markers, headings, and editorial notes:

  | Field | Characters | Limit |
  |---|---:|---:|
  | Headline | 93 | 220 |
  | About | 1,852 | 2,600 |
  | SoftServe description | 1,803 | 2,000 |
  | EPAM description | 378 | 2,000 |
  | Globant description | 357 | 2,000 |
  | Yuxi description | 136 | 2,000 |
  | Somer description | 216 | 2,000 |

- These are Unicode character counts for the revised draft, not token counts.
  Recheck actual platform field limits during `/linkedin-publish`.
- All 25 COPY blocks have unique delimiters. A separate source comparison confirmed
  every employer title, date range, and location against `data/experience.yaml`,
  checked the Trello revenue qualifier, and confirmed that .NET/xUnit appear only
  in the Payworks description. The remaining prose and metrics were reviewed against
  the source references above.
- No resume factual or narrative sources changed, so resume artifacts were not rebuilt.
- The live review confirmed ten displayed experience positions and all 55 skill
  labels; About expansion succeeded. Featured was not displayed. Factual discrepancies
  remain flagged, and the live snapshot does not override `data/`.
- All 55 snapshot skill labels were compared programmatically with
  `review-skills.yml` and match in order. Existing draft character counts were
  rechecked during this review and still pass the stated limits.
- Existing content draft retained: yes. Current visuals retrieved and inspected:
  yes. Observed snapshot refreshed: yes. LinkedIn updated: no.
