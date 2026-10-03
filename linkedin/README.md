# LinkedIn workflow

LinkedIn copy is derived from the same verified facts as the CV. Browser automation
uses project-local Playwright MCP, a dedicated Chrome profile, and OpenCode commands.

## Setup and login

From the repository root, with Node.js 18+ and Google Chrome installed:

```bash
npm ci
npm run linkedin:check
npm run linkedin:login
```

The check connects to MCP and starts the dedicated Chrome profile on a blank page.
For login, sign in yourself in the opened Chrome window, including any MFA, then
press Enter in the terminal. The helper closes the browser and preserves its session.
Do not run the login helper while OpenCode's dedicated browser is open; the same
profile cannot be used by two browser processes simultaneously.

Quit and restart OpenCode from this repository to load the MCP, skill, and commands.
Alternatively, `/linkedin-review` can open the browser and let you sign in there.
No LinkedIn API key, global npm package, or global OpenCode configuration is required.
Python resume dependencies continue to use uv.

## Commands

```text
/linkedin-sync
/linkedin-review
/linkedin-publish
```

- **sync:** refresh drafts from `AGENTS.md`, `data/`, and `master/resume.md`; review
  visuals through the browser when authenticated. Does not save live profile edits.
- **review:** retrieve the actual profile text and current photo/banner automatically,
  inspect desktop/narrow-viewport captures, and record comparisons and recommendations.
- **publish:** apply the draft headline, About, and confidently matched existing
  employer descriptions, then verify saved values. Arguments can narrow the scope.
  Other sections or replacement image uploads can be explicitly requested.

Examples:

```text
/linkedin-sync Emphasize modernization.
/linkedin-review Focus on the current photo and banner.
/linkedin-publish Update only the headline and About.
```

The shared `.opencode/skills/linkedin-browser/SKILL.md` covers factual checks, identity,
image retrieval, entry matching, and saved-state verification. Commands use the
`linkedin-browser` MCP registered in this project's `opencode.json`.

## Files

| File | Purpose |
|---|---|
| `current-profile.md` | Actually observed live profile text, including unknown/partial sections |
| `profile-draft.md` | Suggested fields and separate skills/Featured recommendations |
| `change-summary.md` | Claim sources, changes, comparisons, and missing information |
| `visual-review.md` | Assessment of automatically retrieved photo/banner and rendered crops |
| `publish-report.md` | Created during publishing; actual per-field outcomes |
| `assets/` | Optional replacement images or additional context |
| `automation-research.md` | API/MCP/browser findings and platform constraints |
| `automation-follow-up.md` | Implementation and live-verification status |

Only text inside COPY markers in the draft is intended for that profile field.
The markers, editorial headings, and recommendations are not profile copy.

## Current visuals

Run `/linkedin-review` after login. The agent identifies the current photo and banner,
retrieves displayed images where accessible, and captures their actual displayed crops.
You do not need to provide screenshots. If full-size images cannot be retrieved,
element screenshots are the fallback and their resolution limits are reported.
Narrow-browser-viewport review is not a native-mobile-app test.

## After career updates

Update `data/` and `master/resume.md`, run `/linkedin-sync`, then `/linkedin-publish`.
Editing the generated DOCX alone does not update these factual sources. The snapshot
is updated only from observed profile values, never merely from generated draft text.

## Scope and troubleshooting

- `scripts/linkedin_mcp.mjs` resolves all runtime paths from this repository root.
- `.local/linkedin/browser-profile/` stores the dedicated session and is ignored by Git.
- `output/linkedin/` stores images and captures and is ignored by Git.
- `package.json` and `package-lock.json` pin local browser dependencies. npm/uv may
  still use normal shared package caches; project scoping is not an OS sandbox.
- MCP connectivity and Chrome startup are checked by `npm run linkedin:check`.
  Actual profile access, image retrieval, edits, and saved-state verification occur
  through the corresponding commands after login.

If MCP is unavailable, rerun `npm ci`, check `opencode mcp list`, and restart OpenCode
from this project. If Chrome reports a profile lock, close the other dedicated browser.
`npm run linkedin:status` checks whether a session cookie exists without printing it;
it does not establish that the session is still accepted by LinkedIn.
Expired sessions require login again. To reset authentication, close the dedicated
browser and remove only `.local/linkedin/browser-profile/`, then sign in again.

Never paste passwords or cookies into chat or commit session files. LinkedIn checkpoints
remain interactive. See `automation-research.md` for platform/reliability constraints.
