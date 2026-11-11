---
name: veyui
description: "Design, redesign, polish or audit user interfaces for web, mobile and desktop with reference-led art direction instead of generic AI-looking output. Use for landing pages, marketing sites, product apps, dashboards, native screens, design systems, motion and UX review. Researches precedents from an offline library of 580+ reviewed screens, builds three distinct hosted concepts for you to choose from, then implements the winner and verifies it in a real renderer. Includes product-specific copywriting, independent design critique and accessibility checks."
license: MIT
compatibility: "Any Agent Skills client (Claude Code, Codex, Cursor, Gemini CLI, GitHub Copilot, Windsurf, OpenCode and more). Python 3.10+ for the offline library. Node 22+ and Chrome, Edge or Chromium for the bundled web checks."
metadata:
  author: Choy0X
  version: "1.0.0"
  repository: https://github.com/Choy0X/VeyUI
  homepage: https://choy0x.github.io/VeyUI/
---

# veyUI

**One skill, one design owner, one coherent result.** All design instruction modules, reference retrieval, concept scaffolding and evidence checks are bundled here, together with the complete cloned Taste Skill web foundation. Do not install, invoke or fetch another design skill to complete a stage. Read only the applicable local modules. Project runtimes, a real renderer and a preview delivery route are still needed to build and inspect UI; this skill does not supply an IDE, browser or hosting account.

Own the result from product understanding through rendered visual review. Treat art direction, UX behavior, implementation and verification as distinct responsibilities that must agree. A long plan, famous reference, working build or list of skills does not establish design quality.

Use the [offline design library](references/offline-design-library.md) as the default source of pre-extracted screen knowledge. Use `scripts/design_library.py brief` to retrieve compact screen descriptions, documented flows and decision coaching by task and platform; do not repeatedly fetch source URLs or reopen reference images during implementation. The bounded live-link planning step below is an explicit exception. The preparation work has already recorded the screen anatomy. Read live coverage with `scripts/design_library.py stats`. The separate 200-card atlas supplies original pattern guidance, not additional shipped screens.

Keep the older [visual reference archive](references/reference-library.md) optional for human browsing or explicit source research. Its links and promotional previews do not satisfy the compiled screen count. No Mobbin MCP, paid catalog, embedding service or model training is required. Source URLs support attribution and the bounded recommendation shortlist; they are not instructions for repeated visual research.

## Use across agent hosts

This folder follows the Agent Skills format. Resolve bundled paths from this `SKILL.md` and select equivalent tools available in your host. Read [Agent portability](references/agent-portability.md) for global discovery, Python on Windows, and rendering and hosting fallbacks. Use the same design workflow in any Agent Skills client (for example Claude Code, Codex, Cursor, Gemini CLI, GitHub Copilot, Windsurf and OpenCode).

## Settled quality contract

Read [Quality contract](references/quality-contract.md) for the project's established requirements. The chosen project reference governs aesthetic decisions; quality, factual accuracy, accessibility and functional contracts remain strict. Do not turn a motif blacklist, an editorial recipe or an upstream random design draw into a universal style. Develop specific content with composition; use custom design on proven component foundations. Do not repeat the twelve-question preference interview on every project.

For material work, apply [Seven craft passes](references/seven-craft-passes.md) in planning, calibration, concept review and integration. Decide focal hierarchy, spacing relationships, text and color roles, credible content, component detail and motion connected to user intent. Keep the resulting decisions and rendered checks in the existing brief and review record.

For material work, read [Design coaching](references/design-coaching.md) to turn examples into explicit decisions and verification, then apply [Unslop workflow](references/unslop-workflow.md) to diagnose and repair genericness at the content, composition and craft levels. Use one design lead and independent reviewers when available, following [Review team](references/review-team.md).

## Start with references the user can see

For open art direction, offer **recommend directions for me**, **use my references**, or **combine both**. If references are absent, proactively recommend three project-fit directions using [Recommended directions](references/recommended-directions.md); do not ask the user to hunt for URLs. Each direction needs a checked, existing public example link, where to look, why it fits, what to adapt and a tradeoff. Present these concrete options before building concepts and record the user’s direction choice or existing delegation. A chosen reference territory does not select a finished prototype. Keep the user’s established design or explicit waiver without reopening it.

## Default delivery contract: concepts before integration

For a new UI or substantial redesign, automatically create **three distinct, high-fidelity runnable concepts covering complete representative experiences**, render and inspect them, make them available through a verified review gallery and direct preview links, and present them **before changing application implementation**. The user must not have to ask for concepts or hosting separately. Read [Automatic concept delivery](references/concept-delivery.md) immediately, including its environment-specific hosting routes and blockers. For a landing page, finish the full page in each concept. For apps, finish a representative end-to-end task with key states, adaptive layouts and relevant motion. Native concepts run in their native environment; host an accurately labeled evidence gallery with build/preview access, not a claimed interactive website substitute. A hero-only slice is an internal calibration step, not the selection deliverable.

Keep production source unchanged during exploration. Use a separate preview workspace with truthful fixtures. Keep previews available during review. A generic request to “rework” or “implement” is not a concept selection. Wait for a selection before integration unless the user explicitly delegated selection; then make the evidenced choice and continue within authorization. Honor a specified concept count, an already approved concrete design, an explicit exploration waiver, or an exact small edit. Do not create alternatives for a typo correction.

When inspiration is unresolved, the first planning deliverable is the linked direction shortlist above. After that choice or delegation, the next design deliverable is **working review links plus inspected concepts**, not a plan promising to make them later. If runtime or hosting is unavailable, report the actual blocker and retain draft status; do not silently skip to production. This is an agent workflow, not a capability to create hosting tools that the environment lacks.

## Operating rules

- Honor the user's actual visual ambition and reference examples. Resolve concrete composition, typography, palette, geometry, assets and motion before multiplying pages.
- Inspect project context before asking questions. Ask for consequential missing product facts or preferences, not arbitrary font/hex choices or skill-author disagreements. Preserve prior answers, approvals and delegated choices.
- Apply the built-in modules below to concrete decisions and actual artifacts. Record decisions and findings, not a ceremonial checklist of skill names. No external skill is a prerequisite.
- Use the existing platform and components where they meet the chosen design. Explore authorized visual changes instead of treating inherited styling as immutable. Do not impose no-images, no-dependencies or static-only rules for convenience.
- Before recommending a visual candidate, render it, personally inspect its frames, exercise its relevant interactions, fix material defects and recheck. Source checks and generated-but-unviewed screenshots do not pass.
- If rendering is blocked, label the artifact **draft — visual review blocked** or **specification only**, explain the actual gap, and continue unaffected authorized work. Do not present an uninspected visual winner as ready for approval.
- Use free, accessible components and tools by default. Public previews do not grant source or asset rights. The user's agent/model, image generation and hosting may have separate costs.
- Get explicit permission for proposed model-generated or model-edited imagery before any generation call, including concept drafts. Describe the asset, placement, variants and fallback. Design approval alone does not authorize image generation.

## 1. Discover the task and finish line

Route an exact small correction with a settled design directly to the scoped edit and affected-state verification; do not run the exploration phases or reopen decisions. The specialist design sequence below applies to material design work.

For material design work, start with the built-in discovery and planning protocol in [Planning](references/planning.md). Identify audience, task, current friction, intended outcome, platform, available content, technical constraints and what the user wants delivered. Separate hard rules, inherited defaults, authorized exceptions and your proposals.

| Scope | Finish line |
|---|---|
| New design | Reviewed directions and selected coherent visual/experience contract |
| Redesign | Baseline, justified changes, preserved behavior and reviewed replacement |
| Prototype comparison | Comparable reviewable artifacts at requested fidelity, tested relevant interactions and evidence-based choice |
| Implementation | Actual integrated UI with real data/actions and scoped runtime verification |
| Design system | Tokens, anatomy, variants, states and representative consumers |
| Exact small change | Authorized change and a focused affected-state check |

Use the compact path for exact small edits that leave design and interaction contracts intact. Do not launch a research campaign or rebuild a design system for a label correction. For material work, inspect the relevant baseline and identify available render/input tools using [Platform and tool routing](references/platforms-and-tools.md). A prototype milestone is not completed production implementation.

## 2. Research relevant precedents and model the experience

**For public landing pages, discover the product before drafting the page.** Read [Product discovery and persuasive content](references/product-story.md). Map the whole relevant project—app/native surfaces, services, integrations, entitlements, help and releases—then investigate the strongest capabilities. Translate supported features into customer benefits and proof, prioritize them, and write distinct messaging angles plus complete copy before fixing section order. Existing landing copy is input, not the feature inventory or a mandatory structure. Use [Product story](templates/product-story.md) in the main brief and [Landing-page precedents](references/landing-page-precedents.md) for researched examples. Preserve approved positioning and factual limits; creative, benefit-led advertising is allowed.


Read [Precedent selection](references/precedent-selection.md) and [Offline design library](references/offline-design-library.md). Build a compact brief from the compiled knowledge for the task, platform, composition and risky decision. It combines up to three screen references, one documented flow, two original decision guides and up to two relevant concept studies within the character budget. For art direction alone, use `scripts/design_library.py concepts` and the [Concept collection](references/concept-collection.md). Keep visual studies separate from shipped-screen and behavior evidence. Narrow tasks can use screen-only search. Use the local pattern atlas only as complementary authored guidance. Translate the returned anatomy into explicit project decisions and record rejected mismatches. [Research and retrieval](references/research-and-retrieval.md) governs optional source-ingestion work, not a mandatory browsing phase.

Use `scripts/design_library.py brief`, `search`, `flows`, `decisions` and `get` for normal work. They return self-contained design facts and implementation guidance without URLs or images. The current collection contains 583 reviewed UI-state descriptions across mobile, desktop and web, plus eight documented flows and 19 decision guides; inspect `stats` and the coverage section before claiming breadth. Use `guidance` for clearly labeled original recipes when a category is missing. Do not load the whole collection. Consult `provenance` when auditing, refreshing sources or resolving exact source links for the recommended-direction shortlist; never promote old archive leads into compiled evidence automatically.

For newly supplied, unprocessed inspiration links, screenshots or clips, use the built-in **concept-extraction workflow** in [Concept extraction](references/concept-extraction.md). Capture design principles without the source palette, then translate them into an original project direction. Keep source inspiration separate from the target project's authoritative `DESIGN.md`; never apply a reference site's token dump to the project. Use [Inspiration brief](templates/inspiration-brief.md) for the reusable description. This workflow is entirely local.

```sh
python3 /path/to/veyui/scripts/design_library.py brief "pricing failed payment" --platform web
python3 /path/to/veyui/scripts/design_library.py search "calendar event editing" --platform mobile
python3 /path/to/veyui/scripts/design_library.py search "project workspace overview" --platform web
python3 /path/to/veyui/scripts/design_library.py stats
```

Resolve the real installed path. Direct JSON reads are the fallback when Python is unavailable. Use `data/patterns.json`, `data/sources.json` and `data/user-benchmarks.json` selectively. Those older benchmark records are qualitative observations. The separate reference library (384 records) ships no images: its 31 concept studies are text-only with images withheld, and external publisher images remain linked. A private local gallery can be built from your own catalog (see the reference library module).

Read [Experience design](references/experience-design.md) for meaningful product flows. Define information architecture, primary and important alternate/recovery paths, real content, state transitions, persistence, permissions and feedback. Distinguish actual user research from expert walkthroughs or assumptions. Use [Concept adaptation](references/adaptation.md) for redesigns and imported concepts.

## 3. Establish art direction and the visual system

**Choose the visual medium before the component.** For image-led work or weak product illustrations, read [Visual medium and scene direction](references/visual-medium.md) before page construction. Plan the subject, settled outcome, image/render/code/hybrid choice and composition for each important section, not only the hero. Ask for important missing imagery during planning; do not quietly replace it with generic UI fragments. Use [Visual direction](templates/visual-direction.md) inside the main brief. Working application controls stay semantic/native.

For material web marketing work, read [Web foundation](references/foundation.md) and apply the locally bundled foundation, including its actual layout, asset, motion and inspection tools. Follow the adapter before reading its preserved original guide. This is the primary web construction engine, not an optional inspiration link. Use it inside each isolated candidate; do not integrate a candidate before selection.

Attribution: the web foundation is the vendored [Taste Skill](https://github.com/Leonxlnx/taste-skill) by Leonxlnx, used under the MIT license (license preserved in `foundation/LICENSE`). veyUI is an independent project and is not endorsed by the Taste Skill author. For application and native work, use the applicable craft and component techniques without importing a marketing page structure.

Read [Craft and composition](references/craft.md), then [Reference calibration](references/reference-calibration.md), [Art direction](references/art-direction.md), [Visual system](references/visual-system.md) and the applicable [Design decisions](references/design-decisions.md). Interpret the project's chosen reference closely in visual character and craft, with original content and composition. The selected reference overrides default aesthetic recipes; do not merely borrow its color or decorative object.

For each open direction, specify one organizing idea, a focal composition, actual type/color/spacing/shape decisions, truthful product proof, asset treatment, motion storyboard and compact adaptation. Differentiate the concept set across composition, visual identity and UX with a concrete comparison matrix. Vary appropriate open decisions without making familiar interactions unnecessarily novel. Equal comparison inputs do not require identical palettes and fonts. When identity is fixed, vary only legitimate open decisions.

Choose target colors from the project's existing brand or an original proposed palette, independently of the inspiration source. The palette exclusion applies to source extraction, not to the finished UI. After concept selection, document the target's actual tokens and rules in its existing design contract or `DESIGN.md`; apply that same contract throughout implementation and review.

**Finish the component anatomy before multiplying it.** Read [Component craft](references/component-craft.md) for fields, pickers, overlays and repeated controls. Build the relevant specimen in context with full placeholder/selected text, explicit label gaps, context-specific sizing, open states and compact reflow. Header utility and dialog-field variants must not accidentally share restrictive widths. Inspect the open control at readable size. Use [Component specimen](templates/component-specimen.md) in the existing brief.

For every product surface, apply [Component selection](references/component-selection.md) to a concrete need and [Motion design](references/motion-design.md) to relevant state changes. Consult [Component catalog](references/component-catalog.md) for the nine requested vendors when useful. Record existing/native alternatives, the exact adopted item, access/license, dependencies and normalization into the selected visual system. Preserve proven behavior and accessibility while customizing visual anatomy. Do not stack libraries or effects to manufacture distinctiveness.

Assess the built-in product-demonstration workflow for every material design task. Apply it whenever a concept includes a product illustration, staged app/browser/phone shot or authored demo; otherwise record why it is inapplicable. Read [Product demonstrations](references/product-demonstrations.md) before designing those scenes. Keep staged proof truthful and aligned with the chosen reference. A miniature demonstration is one part of a complete concept, never its replacement.

Make a high-fidelity representative composition as an internal calibration step before expanding the full design. Use a hero plus the hardest supporting scene (often setup or feature proof) for marketing, or a real task with populated and alternate state for product UI. Design wide and compact/native equivalents. Propose important missing imagery and request its explicit generation permission rather than silently substituting arbitrary shapes.

## 4. Prototype, critique and choose

Read [Concepts and prototypes](references/concepts-and-prototypes.md) and [Visual review](references/visual-review.md). Execute [Automatic concept delivery](references/concept-delivery.md): build and host three candidates by default in an isolated review workspace, with truthful equivalent content and equal fidelity. Honor an explicitly requested count or already approved concrete choice. Use `scripts/concept_studio.py` for review scaffolding when suitable; it supplies no default product aesthetic.

Render and personally inspect the opening view, representative details and whole-page/task rhythm. Exercise relevant inputs and motion. Compare against the brief, compiled reference decisions and baseline using the reference-fit table. Reopen already compiled reference images only for an explicitly image-based task or a necessary focused verification in Recommended directions; inspect the actual concepts you produced in every material design task. A creative story with the wrong visual language fails. Reject material aesthetic mismatch, placeholder-heavy scenes and weak asset substitutes before selection. Inspect the weakest important body section independently; a strong hero cannot compensate for unfinished setup/feature scenes. Run the macro, component and finishing passes in Unslop workflow and recheck the seven craft decisions against the rendered candidate, including its weakest relevant component and actual motion. Have the independent visual and UX/engineering reviewers inspect the same actual candidate versions; fix material findings and recheck corrected artifacts before asking the user to choose. If all candidates are weak, improve them. With unavailable delegation, disclose self-review and keep the same evidence requirements. A materially new hybrid needs its own rendered review.

Keep **artifact/version | runtime | viewport/state | capture | observation | correction | recheck**. Include whole-page/task coverage, not only opening screenshots. Record reviewer findings using `templates/concept-review.md` when useful. Use `templates/review-evidence.json` if useful and run `scripts/check_evidence.py` against the project copy to find missing declared evidence. This script checks coverage declarations and file presence only. It does not inspect pixels or certify design quality.

For ordinary interactive controls, inspect closed, focus and open/active states and relevant long/error/loading/compact cases. A working state change does not establish spacing, text fit, overlay craft or motion. Check the weakest relevant component explicitly using Component craft.

For staged product scenes, inspect the still composition and full playback at their actual placement sizes, including the compact layout and reduced-motion poster. Keep scene rehearsal evidence separate from tests of working product controls. A scripted cursor pressing a button does not prove that button works.

Present the verified gallery and direct candidate links, readable captures, specific visible differences, a recommendation and tradeoff. Keep the preview server running while the user reviews. File paths or screenshots alone do not satisfy a runnable hosted-concept handoff. Make a delegated choice when authorized. Ask only for the material decision still owned by the user. Preserve approval already supplied. Reopen only changes that materially alter the approved scope or direction.

## 5. Lock and implement the design

Use `templates/design-brief.md` and `templates/reference-record.json` as optional scaffolds in the project's design-document location. Keep one decision record and one adopted design source of truth. Lock the selected frames, UX paths, tokens, components, states, copy, assets, motion and testable requirement IDs.

Confirm the reviewed candidate/version and recorded selection or explicit delegation before editing application implementation. When implementation is requested, write the concrete integration plan using Planning after the applicable concept selection or delegation. Map tasks to exact existing/proposed files, dependencies, requirements and verification. Follow existing authorization without repeating equivalent approval questions.

Implement a representative slice through the actual project entry point and compare it with the selected concept before scaling. Preserve the approved proportions, tokens, content, asset treatment and motion through integration. Keep real CMS slots, routes, data, billing, permissions and persistence contracts intact. Label simulations and prototypes accurately. Adapt controls, density and navigation to the actual host, using current official documentation for the installed versions. Implement loading, empty, error, focus, disabled and recovery states that the task requires.

## 6. Verify and hand off

Apply [Release checks](references/release-checks.md), the craft review, and the built-in [Interface audit](references/interface-audit.md) before a release-ready implementation. Map applicable principles to native behavior with native evidence. Run current checks against the actual changed version before any completion claim; logs, captures and unresolved findings must agree.

Review the integrated result with the same visual and UX/engineering perspectives. Keep visual craft, behavior, accessibility and engineering checks separate. Correct in-scope material failures and recheck affected views. Report what was delivered, actual evidence, unresolved blockers and the next authorized action. Do not claim production integration from a static mock or field performance from a lab score. Publish, deploy or merge only within user authorization.

## Local resources and validation

- `foundation/`, `data/foundation-manifest.json` — complete pinned web foundation and per-file integrity records; read its adapter before use.
- `data/ready-screens.json`, `data/screen-recipes.json`, `scripts/design_library.py` — default offline screen descriptions, original implementation guidance and bounded retrieval.
- `data/documented-flows.json`, `data/decision-guides.json`, `references/design-coaching.md` — documented transitions and original decision/tradeoff/failure/check coaching.
- `data/flow-provenance.json` — first-party documentation evidence, excluded from default retrieval.
- `data/screen-provenance.json` — attribution and ingestion evidence, excluded from default retrieval.
- `data/patterns.json` — original task/composition cards with pitfalls and review prompts.
- `data/sources.json` — attributed source leads with access status and evidence limitations.
- `data/user-benchmarks.json` — observations from the user's eight concept images and an unreviewed video lead.
- `scripts/design_atlas.py` — offline search, record retrieval, source lookup and structural validation.
- `data/reference-library.json`, `scripts/reference_library.py` — app/site image and flow index, evidence-aware filters, shortlists, portable gallery and review-date checks.
- `scripts/concept_studio.py` — isolated review scaffold, gallery builder and declared handoff/selection coverage check; not a hosting service or aesthetic evaluator.
- `scripts/check_evidence.py` — declared review coverage check, not an aesthetic evaluator.
- `templates/design-brief.md`, `templates/reference-record.json`, `templates/review-evidence.json` — optional project-owned working records.

Run `python3 scripts/verify_foundation.py` after importing or updating the foundation; it checks snapshot integrity, not UI quality. Run `python3 scripts/design_library.py validate` after changing compiled screens. Run `python3 scripts/design_atlas.py validate` after changing the atlas and `python3 scripts/reference_library.py validate` after changing the reference collection. Grow project reference records only from actual inspection. No tool or volume of reference data guarantees excellent taste; the reviewed artifact is the evidence of the result.

## Built-in module map

These are parts of veyUI, not separate skills. Read at the named stage; do not load the whole package into context.

| Stage or need | Local module | Concrete output |
|---|---|---|
| Understand and scope | [Planning](references/planning.md), [Quality contract](references/quality-contract.md) | Evidence ledger, preserve list, open choices, task and preview scope |
| Recommend inspectable directions | [Recommended directions](references/recommended-directions.md), [Shortlist template](templates/direction-shortlist.md) | Three tailored directions with verified existing live links and recorded choice/delegation |
| Discover and communicate product value | [Product story](references/product-story.md), [Working brief](templates/product-story.md), [Researched precedents](references/landing-page-precedents.md) | Feature evidence, prioritized benefits, distinct narrative angles and complete persuasive copy |
| Learn from shipped interfaces | [Precedent selection](references/precedent-selection.md), [Offline library](references/offline-design-library.md), [Coaching](references/design-coaching.md) | Small evidence packet and decisions with tradeoffs |
| Construct a marketing website | [Web foundation](references/foundation.md) | Real bundled recipes, assets, motion, copy lint and browser checkers |
| Create an original direction | [Craft](references/craft.md), [Art direction](references/art-direction.md), [Calibration](references/reference-calibration.md) | Distinct compositions and resolved visual values |
| Design a complete experience | [Experience design](references/experience-design.md), [Adaptation](references/adaptation.md) | Task, states, recovery, navigation and preserve contract |
| Construct a coherent system | [Visual system](references/visual-system.md), [Design decisions](references/design-decisions.md) | Tokens, component anatomy and adaptive behavior |
| Finish controls and overlays | [Component craft](references/component-craft.md), [Specimen](templates/component-specimen.md) | Context-specific anatomy, full text fit, open-state review and state choreography |
| Select reusable foundations | [Component selection](references/component-selection.md), [Catalog](references/component-catalog.md) | One justified implementation choice per need |
| Choreograph real states | [Motion](references/motion-design.md) | Trigger/state/interruption/reduced-motion specification |
| Choose visual medium and compose scenes | [Medium and scenes](references/visual-medium.md), [Working visual direction](templates/visual-direction.md) | Per-section medium decisions, concrete asset request and composed proof |
| Explain the product visually | [Product demonstrations](references/product-demonstrations.md) | Composition, storyboard, poster and rehearsal evidence |
| Deliver a choice | [Concept delivery](references/concept-delivery.md), [Prototypes](references/concepts-and-prototypes.md) | Three inspected, hosted, comparable candidates |
| Establish and verify craft | [Seven craft passes](references/seven-craft-passes.md) | Project decisions and rendered evidence across hierarchy, spacing, type, color, content, detail and motion |
| Repair and finish | [Unslop](references/unslop-workflow.md), [Visual review](references/visual-review.md), [Review perspectives](references/review-team.md) | Fixed findings and matched rechecks |
| Integrate and release | [Interface audit](references/interface-audit.md), [Release checks](references/release-checks.md), [Platforms](references/platforms-and-tools.md) | Actual implementation and scoped evidence |
| Extract new supplied references | [Concept extraction](references/concept-extraction.md) | Palette-independent inspiration brief |
| Adapt an uploaded visual direction | [Concept collection](references/concept-collection.md) | Observations, a target adaptation and a rendered check |
| Maintain the collection | [Research/ingestion](references/research-and-retrieval.md), [Archive](references/reference-library.md) | Verified additions with honest provenance |
| Audit this skill's influences | [Source provenance](references/source-provenance.md) | Source revisions and integration boundaries; not runtime dependencies |

User-facing modes: `veyUI design`, `redesign`, `prototype`, `polish`, `audit`, `motion`, `system`, and `references` are natural-language routes through this workflow, not invented shell commands. A prototype-only or audit-only request stops at its requested deliverable. A material redesign uses the concept path; a settled small edit uses focused verification.
