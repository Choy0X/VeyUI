# Discover the product and write the page that sells it

Use for a new public website, landing-page redesign, positioning or marketing-content request. This happens before page order and visual containers are fixed. A redesign includes reconsidering the message unless the user explicitly locks copy. Preserve product behavior, CMS and factual constraints; do not preserve weak copy merely because it exists.

For an internal/native task UI, use the same product understanding and precise microcopy, without imposing sales language or a marketing funnel. Keep one working brief using `templates/product-story.md`, not separate approval documents.

## 1. Map the whole relevant project, then investigate selectively

Do not ask the user to list features that are discoverable in the project. Start with `rg --files`, project instructions, workspace/package manifests, navigation/route maps and first-party documentation. Identify the product surfaces: public site, authenticated app, native clients, backend/services, integrations, billing/entitlements, support/help, release history and existing approved research. Inspect across these boundaries; the landing-page source is not the product inventory.

Exclude vendored dependencies, generated bundles, caches, secrets, credentials and real customer records. Read targeted files, not the entire repository into context. Build a compact coverage row per relevant area: `area | inspected entrypoints | what it established | missing/deferred evidence`. Stop discovery when the primary audience/task, differentiating capabilities, availability, proof and purchase path are sufficiently grounded—not after an arbitrary file count. Explain missing access rather than pretending to have inspected a private app.

For likely selling points, follow the actual chain: user-facing route/control → action/handler/service → data or integration → permissions/plan/platform restriction → release/configuration evidence. Inspect existing tests as supporting evidence, not proof of live deployment. A dependency, schema, unused function, mock route, disabled flag or roadmap sentence does not establish an available feature. Do not execute production actions, publish CMS content or reveal confidential internals just to research marketing copy.

Record a feature inventory with: `capability | source paths/symbols | audience/use case | availability evidence and limits | demonstrable result | unknowns`. Distinguish publicly available, implementation found/release unconfirmed, beta/limited, planned and stub/demo. Resolve contradictory docs against current implementation and release information; ask only for consequential facts the project cannot establish. Never turn a flag being enabled in a local default into a claim that every customer has it.

## 2. Find the strongest reasons to care

Identify the buyer and user, the situation that brings them here, their current workaround, desired result, key hesitation and appropriate next action. Use existing research or support language if available; otherwise label these as positioning hypotheses. Code shows what the software can do, not what customers value most.

Translate capabilities through this chain:

**verified mechanism → job it enables → friction it removes → meaningful outcome → proof the page can show**.

Example for an imaginary review tool: frame-attached comments → discuss the exact moment → avoid vague timestamp exchanges → review with shared context → show one comment attached to one recognizable frame. Do not inflate this to guaranteed faster approvals or a percentage saving without evidence.

Prioritize by audience relevance, importance to the buying decision, strength of proof, distinctive mechanism and availability. Use reasons, not fabricated numerical scores. Select a small number of lead promises; group related features underneath. Keep remaining useful capabilities in supporting sections, product pages or an expandable overview. Do not turn every route into an equal card.

Look for combinations that create a better story: capture + organize + act, or plan + execute + understand. That relationship may be stronger than any isolated feature. Explain the actual mechanism; do not invent a unique market position or competitor weakness. Ask what would remain product-specific if the logo disappeared.

## 3. Develop distinct messaging concepts

For the three visual concepts, draft distinct message angles from the same verified product facts. Examples of angle families are outcome-led, workflow-led and a supported differentiator-led argument; they are not mandatory labels or page templates. An angle changes the promise, evidence order and demonstration—not just synonyms in the headline.

Each angle needs actual working copy: hero headline, explanatory subhead, primary CTA/destination, leading proof scene, several section headlines and a reason this audience would care. Recommend the strongest angle based on product evidence. A chosen visual territory can contain multiple narrative angles. If positioning is already approved, keep it and explore presentation rather than reopening strategy.

Write confidently and specifically. Emotional relevance, memorable phrasing and concise brand language are allowed when grounded in the product and understandable in context. A benefit-led headline is valid when the first screen also makes the product category, audience and mechanism clear. Do not force every heading into a feature noun or strip personality out of the page to pass a style preference. Avoid empty superlatives, repeated slogan fragments, forced metaphors and unsupported promises.

## 4. Build the argument before the section list

For each proposed section record: `visitor question | belief/decision it advances | actual headline and body | evidence or demonstration | next action | reason it belongs here`. Design the section from that job. Change the existing order when the buyer's understanding demands it. A familiar sequence is acceptable if justified; a mandatory hero/trust/steps/six-cards/pricing/FAQ formula is not.

Possible buyer questions—not compulsory sections—include:

- Is this for me, and what useful result does it deliver?
- What does it actually do in a situation I recognize?
- Why choose this approach over my current workaround?
- Can I trust the demonstration and the company?
- Will it work with my devices, tools, team and existing process?
- What effort, cost or commitment comes next?

Usually establish value and credible product proof before detailed installation instructions. Setup earns substantial space when it removes a real adoption objection or is itself a demonstrated advantage. Do not make installation, pairing or account creation the main sales story merely because those screens are easy to draw. Keep critical eligibility and purchase information near the decision it affects; do not bury material limitations for persuasion.

Pair every lead promise with meaningful proof: an accurate product scenario, authorized sample output, a real customer story, documented capability or relevant measured result. If testimonials or traction are absent, use honest product proof or omit the section. Never add invented customer logos, urgency, ratings, before/after results, security assurances or numerical gains to fill a template.

The feature explanation and visual must tell the same story. A time-saving headline above an empty dashboard supplies no evidence. Write the demonstration's actor, input, action and outcome, then use `visual-medium.md` to compose it. Keep public copy free of internal requirement IDs, engineering implementation notes and source-path citations; retain traceability in the private design brief.

## 5. Write complete, usable content with the design

Produce the page's real draft, not “benefits here” or directions for another agent to write later. Cover navigation, hero, section copy, demonstration labels/captions, CTAs, objections/FAQ, purchase qualifications and footer as applicable. Give each section new information; merge repeated reassurance and repeated feature descriptions. Plain factual labels and expressive headlines can coexist.

Make CTA wording match the next real step. Inspect signup, download, pricing, booking and contact paths. Do not promise a free trial, instant access, no card required, cancellation terms or integrations unless verified. Preserve CMS replacement/fallback behavior and existing localization structure; improve both CMS defaults and built-in text only within the authorized scope. Do not alter published customer content without authorization.

Match depth to buyer complexity and page purpose. A homepage may guide several audiences to deeper pages; a campaign page should follow its specific offer and traffic intent. Neither an arbitrary word ceiling nor maximal detail defines quality. Fit meaningful copy to the layout; refine both together rather than cutting the central benefit to fit a preset card.

## 6. Review persuasion, truth and presentation separately

Read the headings alone: do they explain a coherent argument? Read the page in order: does each section answer the next question? Name the strongest reason to choose the product and point to its supporting evidence. If the page remains a list of installation instructions and menu labels, revisit discovery and prioritization rather than polishing adjectives.

Trace major claims back to the feature inventory, including release, plan and platform limits. Review omissions as well as exaggerations. Confirm the hero does not hide what the product is. Inspect actual line breaks and proof scenes at wide and compact sizes; copy lint is a diagnostic, not an assessment of customer appeal.

Use an independent editorial pass when available, otherwise disclose self-review. Ask the reviewer to identify unclear value, repetition, unsupported claims, missing objections and weak proof. An expert walkthrough is not customer research, and a model's predicted preference is not conversion evidence. If analytics/user testing is available and authorized, define a real comprehension or conversion measure and evaluate it separately. Do not claim this process guarantees sales.

## Research-backed precedents

Read `landing-page-precedents.md` for compact observations from public product pages and usability guidance. Apply their reasoning, not their copy, brand, customer logos or entire page structure. Refresh source claims when current detail matters; routine drafting can use these recorded lessons offline.
