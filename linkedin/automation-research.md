# Automatic LinkedIn updates: research and options

Research date: October 2, 2026.

## Conclusion

Recommend a project-local Playwright MCP with a dedicated persistent browser profile
for the first integration. It has the primitives to read profile text, inspect editing
dialogs, fill fields, upload images, and verify saved results. LinkedIn-specific editing
still needs live testing; generic browser capabilities are not proof that each field works.

Mateo also wants the integration to retrieve the current profile photo and banner
automatically. Manually supplied screenshots are not a prerequisite for this workflow.

The two LinkedIn MCPs reviewed expose profile reading, not personal-profile editing.
The reviewed public LinkedIn API permissions do not offer the desired profile writes.
No connector was installed and no live profile was accessed or changed during research.

## Official API

[Getting Access](https://learn.microsoft.com/en-us/linkedin/shared/authentication/getting-access)
lists consumer permissions for authentication/profile retrieval, email, and
`w_member_social` for posts/comments/likes. Social posting permission does not allow
editing a personal profile.

The [Profile API](https://learn.microsoft.com/en-us/linkedin/shared/integrations/people/profile-api)
documents retrieval and restricted developer access. Neither source establishes a
self-service write route for headline, About, experience, skills, photo, or banner.
This finding concerns the reviewed public route, not all private partner agreements.

## LinkedIn-specific MCPs reviewed

### stickerdaniel/linkedin-mcp-server

- [README and tool inventory](https://github.com/stickerdaniel/linkedin-mcp-server)
- [Person tools implementation](https://github.com/stickerdaniel/linkedin-mcp-server/blob/main/linkedin_mcp_server/tools/person.py)
- [Tool package](https://github.com/stickerdaniel/linkedin-mcp-server/blob/main/linkedin_mcp_server/tools/__init__.py)

`get_my_profile` and `get_person_profile` read profile sections. Other actions cover
connections and messaging. The reviewed inventory and person implementation contain
no headline/About/experience editor or profile-photo/banner uploader. Text/profile
data retrieval also does not establish full image retrieval or visual cropping review.

Its defaults use home-directory session/cache paths and automatic session import
from everyday browsers. Scoping would require a dedicated profile and disabled
auto-import. Its documented cleanup can delete the profile's parent directory, so
that parent would need to be dedicated too. It adds little value for the required writes.

### eliasbiondo/linkedin-mcp-server

- [README and tool inventory](https://github.com/eliasbiondo/linkedin-mcp-server)
- [Person tools implementation](https://github.com/eliasbiondo/linkedin-mcp-server/blob/main/src/linkedin_mcp_server/adapters/driving/mcp_tools/person.py)

The inventory covers people, companies, jobs, and browser closing; person tools are
profile scraping and search. The README includes a profile image in retrieved data,
but no banner-review or editing capability. Session location can be configured via
`LINKEDIN_USER_DATA_DIR`. It does not solve publishing.

These are specific reviewed candidates, not a claim that every LinkedIn MCP is read-only.

## Capability matrix

**UI candidate** means generic tools exist but the actual LinkedIn flow is untested.

| Capability | Public API route reviewed | LinkedIn MCPs reviewed | Playwright MCP | Custom Playwright Python | Chrome DevTools MCP |
|---|---|---|---|---|---|
| Read full profile text | Limited/restricted | Section-reading tools | Browser snapshots; access untested | Implement locators | Browser snapshots; access untested |
| Edit headline | No public write found | No tool found | UI candidate | UI candidate | UI candidate |
| Edit About | No public write found | No tool found | UI candidate | UI candidate | UI candidate |
| Edit experience | No public write found | No tool found | UI candidate | UI candidate | UI candidate |
| Add/reorder skills | No public write found | No tool found | UI candidate | UI candidate | UI candidate |
| Retrieve current photo | Limited photo retrieval | Image metadata varies | DOM/image retrieval + screenshots; untested | Implement image retrieval + screenshots | DOM/image retrieval + screenshots; untested |
| Retrieve current banner | No complete route established | Not established | DOM/image retrieval + screenshots; untested | Implement image retrieval + screenshots | DOM/image retrieval + screenshots; untested |
| Upload photo/banner | No profile write found | No tool found | Upload primitive; crop UI untested | File-input API; implement crop UI | Upload primitive; crop UI untested |
| Verify saved edits | No complete read/write route | Can read but not apply | Implement reload + comparison | Implement reload + assertions | Implement reload + comparison |

## Option 1: Project-local Playwright MCP — recommended first

Source: [Microsoft Playwright MCP](https://github.com/microsoft/playwright-mcp).
Documented tools include navigation, snapshots, clicks, form filling, file uploads,
screenshots, browser evaluation, and viewport changes. Supports a visible browser
and persistent login via `--user-data-dir`.

Proposed installation, not performed:

- Add an exact-version `@playwright/mcp` project dev dependency and lockfile.
  npm metadata returned version `0.0.83`, binary `playwright-mcp`, Node requirement >=18.
- Add only a repository `opencode.json` local stdio MCP entry; launch the local
  `./node_modules/.bin/playwright-mcp` from the project root.
- Use `--browser chrome`, explicit project-local `--user-data-dir`, and `--output-dir`.
- Log in interactively in the dedicated browser, then reuse its session.
- Extend the workflow with `/linkedin-publish` and live visual retrieval/review.

Advantages: quickest agent-driven route to editing and visual inspection; adapts to
live dialogs without implementing all selectors upfront. No paid connector required.

Tradeoff: UI changes and expired sessions can interrupt runs. This is on-demand
automation, not guaranteed unattended background publishing.

## Option 2: Custom Playwright Python workflow, managed by uv

Sources: [authentication](https://playwright.dev/python/docs/auth) and
[persistent contexts](https://playwright.dev/python/docs/api/class-browsertype#browser-type-launch-persistent-context).

- Add Playwright to an optional uv dependency group.
- Implement project scripts for login, snapshot/image retrieval, apply, and verification.
- Parse existing draft copy markers and map them to LinkedIn editing fields.
- Reuse a project-local persistent profile; expose scripts through slash commands.

Advantages: fits the existing Python/uv tooling; explicit field matching and repeatable
verification. No Node browser MCP required for this script workflow.

Tradeoff: more implementation and selector maintenance. Skill pickers and image
cropping need dedicated code. Best after inspecting the real editing UI.

## Option 3: Project-local Chrome DevTools MCP

Sources: [repository](https://github.com/ChromeDevTools/chrome-devtools-mcp),
[configuration](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/configuration.md),
[tool reference](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/tool-reference.md).

- Install an exact-version local npm dependency and repository MCP configuration.
  npm metadata returned `1.10.1`; installed Node satisfies its declared requirement.
- Use a dedicated `--user-data-dir` and workspace roots, rather than everyday Chrome tabs.
- Disable usage statistics and performance CrUX reporting for this workflow.
- Use fill/click/upload/screenshot/evaluation tools and saved-state comparisons.

Advantages: strong Chrome inspection/debugging, with primitives for the same profile
editing and automated visual-review workflow.

Tradeoff: broader debugging surface than needed. Connecting to regular Chrome is
convenient but gives weaker session separation than a dedicated project profile.

## Additional option: Playwright CLI plus a project skill

[Microsoft Playwright CLI](https://github.com/microsoft/playwright-cli) documents named
sessions, persistence, snapshots, fill/click/upload, screenshots, and output paths.
It can be installed locally instead of following its global-install example.
npm metadata returned `@playwright/cli` version `0.1.22` and binary `playwright-cli`.

Useful if avoiding MCP schema/context overhead is important. A project-local skill
and wrapper would drive the same UI through shell commands. Login, editor behavior,
and saved-state verification still need live testing.

## Automatic photo and banner retrieval — required

For the browser options, the proposed agent workflow is:

1. Navigate to Mateo's own authenticated profile using `data/profile.yaml`.
2. Wait for images to load and identify the displayed avatar and banner using the
   DOM/accessibility tree. Inspect `img.currentSrc`, `src`, or relevant CSS backgrounds.
3. Retrieve accessible displayed image files using the current session when needed,
   saving them under ignored `output/linkedin/`. A CDN URL alone is not proof that
   an image has been downloaded and inspected. Signed URLs may expire.
4. Capture the rendered profile header and image-element screenshots automatically.
   These captures show the actual circular crop, avatar overlap, and banner composition.
5. Inspect both downloaded assets (when available) and rendered captures with an
   image-capable tool. Capture a narrow viewport for crop comparison, clearly labeling
   it as browser viewport inspection rather than the native mobile app.
6. Record observations and actual files inspected in `visual-review.md`.

Do not require Mateo to upload screenshots of existing visuals. If original/full-size
images cannot be retrieved, use agent-captured displayed-image screenshots and report
their resolution limits. If LinkedIn blocks access or asks for login, report that
specific blocker. Replacement photo/banner assets are a separate matter from retrieving
the existing ones; do not assume new uploads are needed.

## Project scoping

Proposed layout, not installed:

```text
opencode.json                         # Repository-only MCP entry, if using MCP
.opencode/commands/linkedin-publish.md
.opencode/skills/linkedin-browser/    # Optional skill
.local/linkedin/browser-profile/      # Dedicated session; ignored by Git
output/linkedin/                      # Retrieved images/captures; ignored by Git
linkedin/current-profile.md           # Verified profile text snapshot
```

Ignore runtime profiles, auth state, node_modules, and private run evidence before
creating them. Version reusable configuration and lockfiles. Resolve paths from the
project root; do not modify `~/.config/opencode/` or import everyday-browser cookies.

Project scoping is configuration/session separation, not an OS sandbox. npm/uv and
browser downloads may still use normal shared caches unless explicitly redirected.
Remote MCP OAuth tokens can use OpenCode's global auth storage, another reason to
prefer local browser-session authentication for this requested scope.

Node `v24.13.1` and npm `11.8.0` are available here and satisfy the reviewed packages'
engine requirements. No runtime installation was performed.

## Platform constraints and remaining verification

LinkedIn's [User Agreement](https://www.linkedin.com/legal/user-agreement), section 8.2,
restricts unauthorized automated access and scraping. Browser automation is not an
officially supported public profile-editing API and can carry account-restriction risk.
Project-local configuration does not remove that constraint.

Login/MFA/checkpoints remain interactive when LinkedIn requests them.

First implementation should retrieve the real profile and images, then exercise text
editing and reload verification, followed by skill/image dialogs. Match experience
entries by employer/title/dates, preserve unrelated fields, and update the snapshot
only from observed saved state. Avoid claiming success based only on clicking Save.

Untested: dedicated-browser login, current LinkedIn selectors, actual image retrieval,
field limits in live dialogs, skill ordering, crop controls, saved-state persistence,
and resulting desktop/narrow-viewport appearance.
