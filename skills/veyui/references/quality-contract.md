# Design quality contract

Apply these settled preferences to material UI work. They carry forward the project's established requirements; do not repeat a generic preference questionnaire on every project. Discover only missing project facts. This is a reusable design workflow with no fixed product name or industry.

## Decision priority

Follow higher-priority host instructions and current explicit user requirements. Preserve factual accuracy, accessibility, functional contracts and the quality safeguards below. For aesthetic choices, the project's chosen reference and approved brand take priority over the default recipes in this file and a generic house style. Resolve ordinary conflicts as the design lead and record the decision. Ask only when the user owns an unresolved material choice.

For example, a chosen reference with a centered sans-serif hero overrides the default editorial split hero. It does not override readable text, working controls or truthful claims. Do not force serif italics, a particular font, a color ban, random palette selection, fixed screen-height sections or minimum effect counts onto that reference.

## Settled operating preferences

| Concern | Required behavior |
|---|---|
| Quality failures | Address generic composition, weak visual craft and artificial identity together. Improving only palette or imagery is insufficient. |
| Proactive recommendations | Offer recommendations, supplied references or both. With open direction and no references, present three project-fit directions with checked existing example links before building; preserve prior choice/delegation. |
| References | Extract the selected reference's concept, spatial logic and craft through Concept extraction. Develop original product content, composition and identity. Exclude the source palette by default; use the project's brand or an independently developed palette. |
| Alternatives | Explore composition, identity and UX together. Make three meaningful directions within the reference territory; do not deliver three recolors. Keep product facts and scope comparable. |
| Motifs | Cards, pills, bento layouts, gradients and dimensional assets are not inherently defective. Reject their careless repetition, weak execution or lack of purpose. |
| Content | Develop messaging and composition together from verified product facts. Ask only about consequential unknowns. |
| Components | Custom design on proven foundations: retain reliable semantics, behavior and accessibility while tailoring visual treatment. |
| Motion | Expressive marketing moments; efficient, restrained app interactions. Reduced motion and immediate task access remain necessary. |
| Iteration | Critique, fix and re-render autonomously before presenting. Do not make the user select among known weak candidates. |
| Fidelity | Finish a complete landing page, or a representative end-to-end app task with important states, responsive variants and relevant motion, for every concept. |
| Team | One lead owns composition and integration. Use independent visual and UX/engineering reviewers when authorized tools are available; report a single-agent fallback honestly. |
| Delivery | Automatically host three isolated concepts before integration. Keep them available during selection. Respect existing explicit selection/delegation. |
| Imagery | Propose needed generated/edited imagery during planning and obtain explicit permission before any generation call. |

## Strict quality safeguards

### Composition and content

- Do not repeat the same three-column card grid in consecutive marketing sections. Give every section its own communication job and appropriately distinct composition; do not alternate backgrounds to disguise identical structure.
- Avoid mechanically equal vertical spacing. Use intentional compact and expansive relationships. Keep repeated controls, collection rows and related product screens consistent; section variation is not an instruction to make navigation unpredictable.
- Exclude arbitrary floating shapes, meaningless sparkles, unrelated background grids and generic placeholder cards. A visual's purpose may be explanation, identity or atmosphere, but name that purpose and evaluate its execution against the reference.
- No fabricated testimonials, customer logos, metrics, certifications or claims. When evidence is absent, design a truthful demonstration or omit the proof section. Do not generate reassuring statistics to populate a bento grid.

### Typography and spacing

- Establish visibly different display, section-title, body, label and numeric roles across the page. Avoid flat, identical headline treatment. Preserve shared roles rather than using a new font for each heading.
- Use deliberate size/line-height tokens; no arbitrary fractional literal sizes. Fluid interpolation may compute fractional pixels normally. Review the resulting line breaks at real widths.
- Use at most three distinct type-size roles inside a single component module. A complete page or compound application shell is not one component module; judge meaningful local units such as a card, form group or toolbar.
- For substantial marketing sections, start with spacing tokens equivalent to at least 4rem vertical padding on compact screens and 6rem on wide screens, then compose rhythm around content. Do not apply these section values to navigation, app rows or small controls. A chosen reference can override aesthetic rhythm, with the reason recorded.

### Responsiveness and interaction

- Do not give page containers fixed desktop widths. Use fluid width, maximum-width constraints, responsive gutters, flexible grids and content-driven adaptation.
- Prevent page-level horizontal overflow on compact viewports, including below 768 CSS pixels. Do not conceal inaccessible content with a blanket overflow rule. Intentionally scrollable tables/canvases need a discoverable contained scroll region.
- Provide mobile touch hit areas at least 44 by 44 CSS pixels, or the native platform's larger minimum in its own logical units. The visible icon may be smaller than its hit area. This is this workflow's requirement, not a claim that every accessibility standard uses that minimum.
- Handle long titles, multi-line labels, realistic data volume, localization, missing content and text scaling. Do not break the layout when the ideal demo copy changes.

### Semantics and implementation

- Use actual buttons for actions and anchors/links for navigation. Use semantic landmarks and content elements. Do not replace controls with clickable generic containers or nest conflicting interactive controls.
- Preserve visible keyboard focus, understandable labels, logical heading/order, readable contrast, error recovery and appropriate accessibility states. Use native semantics first and explicit ARIA where needed; redundant or incorrect ARIA is not an improvement. Use native accessibility APIs on native platforms.
- Put visual values into structured tokens, shared styles or clean framework utilities. Do not scatter literal styling values across markup. Runtime data/geometry belongs to component data handling; it does not justify arbitrary aesthetic constants.

## Choose the visual vocabulary from the brief

There is no default serif, indigo, asymmetry, bento, dark mode, pill or cinematic effect. Use the original references as a quality bar: their composition, asset quality, hierarchy and consistency matter more than their motifs. Match the reference territory, build independent target colors, and make each concept coherent. Product and native screens prioritize task structure and platform conventions. Marketing permits expressive composition without imposing it on frequent app tasks.
