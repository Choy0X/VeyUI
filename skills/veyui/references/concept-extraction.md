# Concept extraction without a source palette

Use this only for a newly supplied unprocessed reference, explicit refresh or image-matching task. Existing compiled descriptions are ready to use; do not re-extract their source images or URLs.
This workflow merges the useful extraction and application principles from the design-md skill it was derived from. It deliberately replaces exact reproduction with concept inspiration. It is internal to this pipeline, not a dependency on a separately installed skill.

## 1. Establish evidence and scope

For a URL, inspect the actual rendered page through available browser tools. Review the complete relevant page or flow, representative interactions and compact adaptation. For a broader system, sample relevant page archetypes until the useful patterns repeat; record visited routes and omissions. Do not crawl an entire unrelated site by default. Do not submit forms or perform transactions just to inspect a reference.

Source text or search snippets can establish facts, but cannot establish rendered composition or animation. Computed styles may supplement visual inspection with permitted tools. If rendering is unavailable, record the link as unverified and continue with available supplied images or other inspectable references. Do not invent visual observations or claim a live-site analysis from source code.

For screenshots, describe only visible states. Label dimensions as measured or estimated; do not assert a font identity or exact breakpoint from pixels alone. For video, inspect actual frames and playback when tools allow, and record the observed segment. A still cannot establish timing, triggers, interruption or reduced-motion behavior. Keep unobserved behavior unknown; place a proposed adaptation in a separate column.

## 2. Extract generative rules

Use `templates/inspiration-brief.md`. Describe what creates the concept and why it works, rather than listing attractive objects. Include:

- Essence and the few signature composition moves that organize attention.
- Layout proportions, focal hierarchy, reading order, alignment anchors, container logic and whitespace rhythm.
- Typography character, relative scale, line length and wrapping relationships. A source font is an observation, not a required dependency.
- Component anatomy, grouping, control priority, density, geometry and state relationships.
- Section sequencing or task-flow progression: what each step communicates and why its arrangement changes.
- Asset framing, crop, layering and relation to product evidence, without reproducing the source's distinctive artwork.
- Depth mechanisms and contrast hierarchy described by function, without source colors.
- Observed responsive and motion rules, limits of evidence and proposed platform adaptations.

Give concrete non-color measurements where verified and useful. Otherwise give supported spatial relationships or labeled estimates. Do not fabricate precise values to fill a template or impose a document-length quota.

## 3. Exclude source identity and palette

Do not sample, export or prescribe source hue names, hex/RGB/HSL/OKLCH values, gradient stops, brand color variables, colored shadow stacks or color-bearing CSS snippets. Describe roles such as primary-action emphasis, quiet supporting surface and separated content layers without assigning the source's hues. Rebuild any required target shadow or gradient later from target tokens.

Keep URLs, titles, access dates and capture references in a provenance section or companion reference record; do not erase attribution. Keep the reusable design description brand-neutral. Do not copy logos, slogans, proprietary assets, testimonials or distinctive decorative artwork. The supplied reference images may retain their colors as evidence, but their palettes are not adoption instructions. Historical atlas notes naming colors do not override this rule.

## 4. Translate into an original project

For each useful principle, record **observed cue | underlying purpose | retain/translate/drop | target decision | deliberate difference | review evidence**. Account for the project's audience, content, tasks and platform. Select a coherent lead concept; use secondary references for compatible details rather than combining incompatible systems.

Preserve the source's craft and useful spatial logic while developing original content, composition and identity. A recolored clone is not the objective. Conversely, originality does not excuse discarding the reference's useful hierarchy. Use the existing project palette when it remains authoritative, or propose an original palette during concept development. Only an explicit later request to reproduce source colors overrides this default.

## 5. Apply the target contract

Locate and read the project's actual `DESIGN.md` or equivalent before styling. Store source analyses under a clearly labeled reference location, for example `design/references/<slug>/INSPIRATION.md`, inside the isolated concept workspace during exploration. Do not overwrite the production design contract before selection. The source brief is evidence, not an implementation mandate.

After selection, update the target contract with adopted principles, original palette, type, spacing, components, states and motion. Map tokens to the project's current framework or native theme APIs; do not force a particular Tailwind configuration format. Reuse this contract on later screens and check rendered output against it. Concept extraction never replaces the three complete hosted candidates, review, selection or implementation verification required by the pipeline.
