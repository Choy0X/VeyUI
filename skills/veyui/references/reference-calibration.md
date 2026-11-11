# Reference calibration and rejection

**Default policy:** Use [pre-extracted offline screen knowledge](offline-design-library.md) during ordinary design work. The source-inspection instructions below apply only to explicit new-reference ingestion, refresh or image-matching tasks. Do not reopen already compiled sources or load their images by default.
Use this before building concepts and again before presenting them. A concept can be coherent, accessible and different from its siblings while still being the wrong design for the brief. Treat user references as a visual target, not merely evidence that the user likes “modern UI.”

For inspiration inputs, follow [Concept extraction](concept-extraction.md): preserve useful design principles while excluding the source palette. The historical examples below describe supplied images, not colors to adopt. Evaluate reference fit through composition and craft; evaluate target colors against the project's independently established palette.

## Separate the product story from the visual direction

Determine both independently:

- **Product story:** what the product does, who uses it, why it matters, truthful proof and the next action.
- **Visual direction:** contemporary or traditional type, contrast distribution, composition, material/image treatment, control geometry, density and motion.

Do not translate “family” into childish illustration, “trust” into a printed contract, “calm” into beige, or “creative” into serif headlines by default. A clever metaphor is not evidence the user wants that aesthetic. When the references consistently favor polished contemporary product design, every default candidate stays within that broad visual territory. Explore genuinely different compositions within it. An intentional outlier needs a reason grounded in the user's brief and must not displace the requested direction.

## Make a compact visual target before code

Read two to four directly relevant compiled reference descriptions, or one when it settles the target. Inspect a new external reference only during explicit ingestion or image-matching work. For each, identify its role: aesthetic direction, composition, component craft, interaction or content. Do not average incompatible aesthetics. Select a lead reference for the candidate's visual language, with secondary references contributing specific compatible details.

Write a table: **visible reference trait | candidate decision | where visible | unacceptable substitution**. Describe spatial relationships, not only colors. Include:

1. Focal composition and ratio of headline, artwork/product proof and whitespace.
2. Type character, scale contrast, line breaks and supporting-copy measure.
3. Emphasis distribution and surface separation without exporting source hues or color tokens.
4. Asset fidelity: photo/3D/illustration/product render, crop, lighting, masking and integration.
5. Component craft: readable detail, consistent edges, optical alignment, subtle boundaries and meaningful states.
6. Motion behavior where observed: trigger, progression, settling, interruption and static equivalent. Do not infer video behavior from stills.

Estimate values from screenshots honestly; propose exact implementation tokens separately. Do not claim pixel measurements you did not take. The compiled ready-screen descriptions are the intended substitute for repeating source-image inspection. The older authored pattern atlas is guidance, not image evidence.

## Calibrate against the user's supplied examples

Apply the Quality contract priority: a chosen project reference overrides default editorial layouts and typography recipes. Match its visual language closely while using original product content. For this user's original concept collection, useful observations include:

| Reference | What to carry into a suitable original concept | What does not meet that intention |
|---|---|---|
| Liquid Brokers | Deliberate high-contrast opening, large clean type, integrated dimensional focal artwork, restrained floating proof | A generic dark panel with a gradient blob and several unrelated stat cards |
| ProFinance | Bold concentrated lime accent, crisp black type, confident scale, carefully layered readable product mockups, varied section composition | Random bright cards or tiny entire dashboards stacked down a page |
| Juris AI / Quick Actions | Precise shell, quiet neutral layers, consistent icon/label alignment, clear toolbar and empty-state hierarchy | Giant marketing whitespace inside a frequent-use product flow or arbitrary nested cards |
| Assistant panel | Purposeful dimensional focal asset and carefully balanced input/suggestion geometry | A random glowing circle over generic chat controls |
| Twinkle / Zentro | Crafted landscape/material imagery supporting readable product UI, disciplined layering and page rhythm | A crude code-drawn landscape used because obtaining a quality asset takes effort |
| Galileo | Controlled amber accents, varied yet coherent feature compositions, thoughtful dark/light transitions and product diagrams | A uniform grid with the same reveal effect on every card |

These are observations about supplied references, not universal mandatory styles. For other projects, replace the target with their actual references and platform conventions. Do not add glowing visuals, imagery or marketing motion to native/product tasks that do not benefit from them.

## Asset quality is a design dependency

Read [Visual medium and scene direction](visual-medium.md) to choose and compose imagery, captures and hybrids by section. Translate the lower-page reference regions as carefully as the hero. Plan missing body imagery explicitly; a hero image plus generic setup cards is not reference fidelity.


Use existing appropriate assets, licensed/free assets whose terms are checked, or propose generated assets for explicit permission. When generation is proposed, describe purpose, visual treatment, dimensions/crop, variants and fallback during planning. Never generate before permission, including prototype assets. Continue unaffected layout work while permission is pending.

Do not silently replace a required high-quality image with elementary SVG scenery, a CSS blob, emoji or a low-detail fake dashboard. Code-native icons, diagrams and illustrations are excellent when their rendered craft actually serves the chosen direction. The failure is unsuitable execution, not the file format. If the defining asset remains unavailable, the concept remains an asset-blocked draft; do not sell it as equally finished.

## Review the actual candidates side by side with references

Inspect the produced candidate at readable scales and compare its hero/task, details and whole-flow rhythm with the compiled reference decisions. Open source images side by side only for explicitly image-based matching work. Write **target trait → observed candidate evidence → gap → repair** for each material mismatch. If the user references contemporary sans-serif product design and every candidate has cream paper, serif type and retro imagery, reject the set before selection; different stories have not solved visual fit.

Inspect particularly:

- Does the dominant visual look crafted at the size it is shown, or expose primitive geometry/low-resolution/detail mismatch?
- Does product proof explain one useful outcome at a readable size, or does an oversized full dashboard overwhelm the opening and create multiple mobile screenfuls before the next message?
- Are loading states, blank diagrams, repeated mock cards or placeholder bars being presented as finished content?
- Are the logo, headline, CTA and product evidence a deliberate hierarchy, or competing layers?
- Is motion stable at rest and in between states? Clipped rolling numbers, jumping layout and clipped text are defects, even if one selected frame looks fine.
- Does each direction vary at least two meaningful dimensions while remaining within the intended aesthetic and product truth? Changing only palette is insufficient for broad redesign exploration.

A useful concept must pass both **fit** and **craft**. Mark each material trait `meets`, `needs work` or `unverified` with an observation. Do not invent numeric taste scores or call three mediocre choices a successful exploration. Fix the largest mismatch before adding animation or polishing secondary details. Do not call the set professional until actual rendered evidence supports that judgment; even then, distinguish expert review from user approval.
