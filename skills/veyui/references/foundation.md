# The built-in web foundation

veyUI uses the complete Taste Skill 2.5.1 skill directory from Leonxlnx/taste-skill, pinned to one commit in `data/foundation-manifest.json` together with the SHA-256 of every file. To keep the installed skill small, the foundation is not stored in this repository or in the installed skill folder. It is fetched once, on first use, with `scripts/fetch_foundation.py`, which downloads that exact commit from GitHub, rebuilds `foundation/` next to this SKILL.md and refuses to place anything that does not match the manifest byte for byte. After that it is runnable local code and assets. `foundation/upstream-guide.md` preserves the original entrypoint as documentation; veyUI remains the only activatable SKILL.md. Preserve `foundation/LICENSE` and item-level asset credits. No upstream installer, account, MCP or global hook is necessary.

## Get the foundation first

Before any web construction work, run `python scripts/fetch_foundation.py` from this skill's folder (use the host's Python launcher, see `agent-portability.md`). It is idempotent: when `foundation/` already verifies it does nothing. It needs internet once (about 30 MB from codeload.github.com) and only the Python standard library. If it cannot download, say so plainly, continue with the parts of veyUI that do not need the foundation (offline library, concept studio, design modules, copy and review), and report the web tools as unavailable and the rendering as unverified. Never fabricate a gate result and never write foundation files by hand. `python scripts/verify_foundation.py` re-checks integrity at any time. If the skill folder is read-only, pass `--root DIR` to place `foundation/` elsewhere and use the path the script prints.

**Attribution:** the foundation is the [Taste Skill](https://github.com/Leonxlnx/taste-skill) by Leonxlnx, used under the MIT license (the fetch script restores `foundation/LICENSE`); its SKILL.md is kept as `foundation/upstream-guide.md` and all other files are unchanged and hash-checked. veyUI is an independent project and is not endorsed by the Taste Skill author.

## Read and apply it

For a new marketing website or material landing-page redesign, read `foundation/upstream-guide.md` after this adapter. Its `<skill>` means the absolute `foundation/` directory. Read its core `references/copy.md`, `copy-voice.md`, `system.md`, `layout-v4.md`, and `sections.md` before constructing the page. These detailed source references are part of veyUI. Follow their business-kind routing, product-specific composition, truthful copy, asset selection, shared system, motion, browser inspection and correction loop. Read other asset-family guides only when used.

For a web app, use the foundation's component, typography, motion and verification techniques selectively; use veyUI's Experience design and Component selection for the real task. A native application uses native controls and verification; it does not inherit HTML or a company-website section plan. A native product's marketing website can use the full web foundation.

Preserve the useful implementation, not only its adjectives: start matching web compositions from the bundled layout recipes; use the actual motion and asset modules where they suit the approved direction. Rewrite all example copy and data. Inspect asset licenses and credits before project export. Copy only runtime asset families that the resulting project uses; keep unused effects and sample content out of the app bundle.

## Integration precedence

veyUI's entrypoint, the user's task, project contracts and this adapter govern the copied guide. Apply these explicit adjustments consistently; do not ask the user to arbitrate upstream wording:

- Three complete isolated, hosted concepts precede integration by default. Upstream building instructions operate inside each candidate workspace. Keep each candidate's gate reports and history separate; never share one candidate's passing receipt with another.
- Start with the user's reference territory and genuine project assets. For an open marketing brief, use the bundled dealers to explore palette, type, layout and moments; choose coherent results that fit the brief. Randomness is a variation aid, not evidence of quality. A fixed approved brand remains fixed, including purple when legitimate. Source palette exclusion still applies to newly extracted references.
- Use the foundation's cinematic screen rhythm when suitable, but let real content, zoom, native layouts and compact reflow grow. Do not cut necessary content or hide overflow to satisfy exact screen-height rules. Keep strong shared edges and deliberate section rhythm.
- Preserve truthful sample-data disclosures, media accessibility descriptions, verified business contacts and required legal information. Upstream no-caption, synthetic-contact and placeholder rules apply to its demo context; they cannot remove information a real product needs. Never invent prices, hours or claims.
- Keep the actual project runtime. Do not force a working server-rendered application into static export. Run checkers on a supported local rendered URL or built output.
- Preserve image-generation permission. An asset recipe or a concept approval never authorizes model-generated imagery. Use approved assets or an explicitly described fallback until permission arrives.
- Deliberate hero and signature motion are desirable for a motion-led marketing brief. Their number follows the story and available assets. Do not require looping effects in a task app or turn off a requested meaningful sequence for convenience.
- Keep source tool diagnostics intact. Record an inapplicable house-style finding with the exact rule, project reason and replacement check. Never call a failed or unavailable upstream gate PASS. Never disable checks, hide content or fabricate receipts to manufacture success.

## Avoid the asset-background shortcut

Bundled assets and scene fragments are construction materials. Selecting a hero backdrop does not settle the medium or composition of setup, feature and proof sections. Apply `visual-medium.md` before choosing those fragments. Use accurate product UI where it explains a real capability; choose images/hybrid scenes when material, photographic or rendered relationships define the reference. Keep the imported source intact and resolve these decisions in the candidate.

## Persuasive content takes precedence over rigid house copy rules

Apply `product-story.md` before the bundled copy layer. Its cross-project discovery, supported benefits, narrative alternatives and proof determine what the page says. Preserve the source's specificity, understandable language and anti-fabrication discipline. Its blanket no-ad-wording/no-metaphor preference, mandatory category-only H1, one-brand-line quota, mandatory first-screen number/date/price and fixed word budgets are optional house style, not veyUI requirements. A clear benefit-led headline, memorable phrasing and appropriately sized argument are allowed. Explain the category and mechanism clearly in the first screen; never invent a fact to satisfy a quota.

Do not edit the pinned foundation to hide warnings. Run diagnostics when applicable and record the exact style-rule exception, product reason and replacement human check. Raw failures remain visible; an accepted style exception is not an upstream PASS. Unsupported claims, residue, broken behavior and unreadable content are real defects, not creative exceptions. This adapter governs the original guide even where that guide says its copy file wins.

## Run the actual tools

Python 3 runs veyUI retrieval and review scaffolding. Node 22+ and a supported Chrome/Edge/Chromium runtime run the copied web tools; ffmpeg is optional for applicable capture workflows. Verify installed executables and documented flags. These are tool requirements, not dependencies on other skills.

Resolve `FOUNDATION` to this skill's `foundation` path (the one `fetch_foundation.py` printed). Run commands with the candidate directory as the working directory. For example:

```sh
node "$FOUNDATION/scripts/start.mjs" deal --page software --trade "the actual product category" --history .taste-skill/history.json
node "$FOUNDATION/scripts/gate.mjs" --start http://localhost:5173/ --kind software --category "the actual product category" --primary "the actual action"
node "$FOUNDATION/scripts/consistency.mjs" http://localhost:5173/ --widths 1440,1024,768,390
node "$FOUNDATION/assets/layout/check.mjs" http://localhost:5173/ --sizes 1440x900,1024x768,768x1024,390x844
node "$FOUNDATION/scripts/shoot.mjs" --url http://localhost:5173/ --w 1440 --out shots/wide.png
node "$FOUNDATION/scripts/perf.mjs" http://localhost:5173/
node "$FOUNDATION/scripts/gate.mjs" http://localhost:5173/
```

Read each tool's source/help and applicable guide before executing; `consistency.mjs` and the gate have different coverage. The quick gate does not replace full motion, keyboard, form, performance and visual review. Its local-only URL rule does not verify that the user-facing hosted preview opens; perform that separate check with the actual browser route. Do not execute the original Stop hook automatically or install global hooks.

`GATE: OPEN`, `DONE`, `OFF`, `SETUP`, `ERROR` and a zero exit status without checks do not establish readiness. Retain the actual status and open findings. When browser automation is blocked, no fallback tool may bypass the restriction; report unverified rendering and continue unaffected work. For general app/native work, use the applicable interface checks rather than report irrelevant website rules as passed.

Inspect the actual captures and motion, fix the largest remaining defect and re-render. The foundation's clean checker output is one engineering input; the full concept still needs a good composition, complete content, functional controls and user review.
