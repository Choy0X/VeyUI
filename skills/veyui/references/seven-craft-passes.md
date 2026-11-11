# Seven craft passes for a finished interface

Apply these passes when planning, constructing and inspecting material UI work. For a settled small correction, use the affected passes and states. Keep decisions and evidence in the existing brief and review record. Start with the screen's purpose and actual content, then resolve geometry and material, then motion. Recheck earlier decisions when a later change alters them.

A maintainer supplied a design talk and a paired landing-page image on 11 November 2026. This module synthesizes its seven concerns into project decisions and checks. The image is catalog entry R031. Its visible comparison supports hierarchy and composition observations. The talk's references to other products and animation behavior are supplied examples, with their current implementation unverified.

## 1. Focal hierarchy

Write one sentence naming the user's immediate goal, the content that proves or enables it, and the next action. Choose a dominant area through position, scale and contrast. In marketing this can be a headline/action group connected to product proof. In a work tool it may be the selected object, editing canvas or decision panel.

Assign supporting navigation, labels, proof and secondary actions quieter roles. Remove a redundant badge, statistic or repeated action when it competes without answering a useful question. Preserve important alternatives and task controls. A dense table can have clear hierarchy without a giant headline or a single button across the whole application.

Inspect the first viewport at readable size and as a small overview. Name what draws attention first and compare it with the intended task. Then inspect the real task state with an open menu, error or active selection. A prominent decorative object must still lead into a comprehensible product story.

## 2. Spacing that communicates relationships

Choose a small scale and assign semantic relationships to it. A web starting set is 4, 8, 12, 16, 24, 32, 48 and 64 CSS px. Existing tokens, density and platform logical units determine actual values. Use small intentional optical or stroke corrections where needed.

Keep label/control/helper relationships tighter than separate field groups. Keep related rows tighter than sections, and give a section heading a clear relationship to its own content. Set shared edges and horizontal insets. Equal padding on every element does not establish grouping.

Inspect the actual rectangles, baselines and text. Check repeated gaps with rendered measurements when useful. A gap on the token scale can still be wrong for the relationship. Include long values, compact widths, open overlays and text enlargement. Keep exact control variants and sizing in Component craft.

## 3. Typography with clear roles

Assign a small set of roles for display, headings, body, labels, secondary metadata and numbers. Use the project's family and fallbacks, usually one primary family with a deliberate display or technical companion when useful. Native text styles follow the host.

Build local hierarchy with weight, tone, position and spacing as well as size. Maintain readable contrast for supporting text. Reserve large display scale for compositions that need it. Use tracking appropriate to the typeface and script. Preserve readable line length and line height, actual heading breaks, font loading and numeric alignment.

Inspect a card, form or toolbar at normal scale. Simplify competing local roles before increasing its container. Check the longest meaningful heading and labels with the real font. Large text, translated copy and fallback fonts must preserve task order and content access.

## 4. Color with semantic intent

Map canvas, surfaces, primary and secondary text, borders, focus, accent and status to named roles. Start task-heavy surfaces with a restrained neutral foundation and a clear dominant accent when the brand permits. Introduce tinted neutrals only when they help the chosen material and contrast.

Use emphasis where it carries a decision or state. Preserve distinct status, categorical data and accessibility needs. An approved multicolor identity or expressive marketing scene can have a wider range. Define its emphasis and quieter regions explicitly. The source palette remains excluded from adaptation by default.

Inspect the full screen and component states in each supported theme. Check that hover, focus, selection, disabled and error treatments remain distinct. Verify foreground/background pairs, including text over changing imagery. Fix competing emphasis before removing an intentional brand color.

## 5. Product-specific content and credible proof

Use Product story to discover real capabilities before writing public-page copy. Name the audience's problem, a concrete benefit, how the product delivers it, and the actual next action. Source prices, entitlements, limits and destinations from their authoritative project data.

Use approved product content and media. For prototypes, create plausible fictional fixtures with coherent names, dates, units, statuses and totals, then disclose the simulation appropriately. Make available evidence persuasive through selection and composition. Keep unsupported outcomes, customer quotes, logos and popularity claims out of the product story.

Read every visible string. Check that a feature scene answers a buying or task question and that numbers reconcile across views. Replace a vague setup caption with a meaningful outcome and a legible usage moment. A missing fact stays a tracked gap, with truthful copy or a focused question when it is consequential.

## 6. Geometry, materials and small details

Define related radius roles, border strength, elevation levels and icon geometry. For a concentric inset surface, use outer radius minus the actual inset as a construction starting point, adjusted for borders, rounding and the native mask. Match the relationship rather than assigning the same radius to every nested shape.

Use a thin subtle divider or border where it clarifies structure. Use a soft shadow or surface contrast where elevation needs it. The chosen art direction can justify harder edges and stronger materials. Normalize imported components to the same roles. Keep icon family, optical size, stroke weight, baseline and target clearance coherent.

Inspect the weakest component closely at its delivered size. Check nested corners, border intersections, shadow clipping, icon/text alignment, focus clearance, full value fit and hit targets. Inspect open as well as closed states. Verify whole-screen relationships again after local repairs.

## 7. Motion connected to user intent

Name the trigger and persistent object before choosing an effect. Anchor a menu to its trigger and adjust the origin when collision handling flips its placement. A dismissing surface should clear the task promptly. A first web menu trial might enter over 180 ms and exit over 120 ms, then change after inspection. These are proposals, not measured source timings.

Keep notification entry and stacking spatially coherent, preserve a readable lifetime and actions, and handle a new notification during an exit. A draggable sheet follows the pointer or finger during the gesture, then settles to the chosen state using the host's interaction model. Provide equivalent keyboard or explicit controls. Immediate input feedback stays available during motion.

Choose easing or spring behavior by relationship. Keep routine movement efficient and give a deliberate marketing sequence enough time for its message. Test rapid reversal, interruptions, resizing, scroll, changed content and reduced motion. Preserve text geometry and semantic state through transitions. Use the compatible Motion package when requested and native animation APIs on native targets.

Observe playback at actual placement size. A static screenshot establishes settled appearance only. Record implemented code separately from motion actually observed, and resolve material drift, lost focus or wrong endpoints before calling the transition reviewed. Detailed state choreography belongs in Motion design.

## Use the passes in the existing workflow

| Stage | Required result |
|---|---|
| Before construction | Record the primary task and focal area, spacing relationships, text roles, color roles, content/proof sources, geometry/material rules and relevant motion relationships in the main brief. Resolve ordinary choices as the design lead. |
| Calibration | Build the opening and hardest supporting scene or representative task. Apply the seven passes to its rendered wide and compact states before repetition. |
| Concept selection | Review complete candidates against all applicable passes. For each material issue record location, observed defect, concrete repair and current-version recheck. Preserve differences between concepts. |
| Integration | Compare the selected and integrated versions at matched sizes and states. Recheck changed content, real controls and actual data behavior. |

Use the existing statuses of meets, needs work and unverified, with a reason for an inapplicable check. Record actual observations rather than seven unchecked labels or a numeric taste score. A missing rendering or motion observation remains unverified. Keep structural, accessibility, functional and performance checks alongside this visual review.

## Apply the principles across different visual directions

- For an expressive workflow landing such as R015 or R017, protect the message and action, stage a readable workflow above the imagery and set a compact proof crop. Preserve its visual ambition while reducing competing badges or redundant fragments. Add motion between actual input and result states with an effective still composition.
- For a dense desktop tool such as R014, emphasize selected identity and the relevant inspector. Use consistent row rhythm, aligned metric columns and restrained status cues. Preserve scan stability during refresh. A spacious marketing layout is a different task.
- For a mobile assistant such as R028, keep the input and next useful action accessible through keyboard, voice and response states. Review safe areas, text scaling, information hierarchy and interruption. Lighting around a visual anchor must preserve content readability.
- For the R031 landing comparison, adapt the specific benefit, primary versus secondary action, quieter supporting text and relevant invoice proof. Treat pictured prices, customer details and claims as illustrative content whose production truth needs separate evidence.
