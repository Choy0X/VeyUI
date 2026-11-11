# Design decisions

Use this as the design contract checklist. Fill decisions that affect the target and record exceptions. Anchor each choice in the user task, approved references, or the project system. Distinguish measured values and current behavior from proposals. Use semantic token names and real values or component references where implementers need them.

## Define the design keys

| Key | Resolve before handoff |
|---|---|
| Intent and content | Identify the intended user, main job, primary action, and success condition. Define the section or screen order, real CTA destinations, user-facing labels, supporting copy and proof, and the hierarchy of actions. Use realistic text and data lengths. |
| Composition and grid | Set the visual anchor, reading order, shared alignment edges, content width, gutters, columns or panes, and vertical rhythm. Distinguish content density from whitespace. Specify where layouts stack, hide, wrap, or change navigation and how focus or selection survives. |
| Typography | Choose type roles, family or system fallback, size, weight, line height, and treatment for numeric data where needed. Define wrapping or truncation on tight widths, larger text, and longer locales. |
| Color and hierarchy | Define background, surface, text, muted, border, accent, focus, and status roles. Check contrast in the actual adjacent pairs and interactive states. Where themes are in scope, verify each theme and status cues beyond color. |
| Geometry and depth | Set the spacing scale, common alignment, control and target sizes, radii by role, border weights, elevation, overlay layering, and consistent icon size and stroke. Prefer existing design tokens where they satisfy the intended visual effect. |
| Components and behavior | Define anatomy, variants, interaction contract, data needs, defaults, focus behavior, validation, and side effects. Cover applicable hover, focus, pressed, selected, disabled, loading, empty, error, permission, destructive, and success states. Include recovery and persistence where they affect the flow. |
| Assets and motion | Specify sources, rights, file treatments, aspect ratio, crops, responsive loading, alternative text or decorative treatment, and a fallback. Storyboard purposeful transitions and document performance constraints and reduced-motion behavior. |
| Accessibility and adaptation | Record applicable semantic roles, names, announcements, focus order and restoration, inputs, reflow or text scaling, insets, touch targets, and platform conventions. Define checks in actual target environments and distinguish host-dependent checks from prototype evidence. |

Make the result reproducible. Link the accepted visual frames, specify alignment and spacing by role, and give important actions and states the data that triggers them. Map the choices to the stack, such as CSS variables and Tailwind theme values, Compose theme roles, or SwiftUI styles. Keep one source of truth for adopted tokens and variants.

| Surface | Extra decisions to lock |
|---|---|
| Landing or marketing | Show the product and its primary action early. Give each section one job. Pick a signature visual composition, include authentic product evidence, and confirm the mobile crop and CTA destination. |
| Product or operational UI | Lock the main task path, information density, row and control alignment, navigation, feedback, and recovery. Exercise real data and long or missing values. |
| Native mobile | Keep system navigation and Back, safe areas, input method, text scaling, semantics, and touch behavior consistent with the OS. Plan compact and expanded layouts where shipped. |
| Native desktop | Define minimum and wide window behavior, resize or pane rules, keyboard shortcuts, focus, menus, dialogs, pointer behavior, and scaling. |
| Design system or shared component | Specify anatomy, variants, state transitions, accessibility contract, example usage, and adoption scope. Inspect representative consumers when changes propagate. |

## Route the implementation to the host

- For web, prefer existing semantic controls and primitives. Reuse shadcn/ui, Tailwind, or equivalent when already present. Start with the accessible behavior and add the project theme. Verify that menu, dialog, and combobox keyboard and focus behavior survives styling.
- For Android Compose, map semantic tokens to the existing theme, use adaptive navigation where appropriate, and pick animation APIs by state change. For SwiftUI, favor system navigation, presentation, and accessibility behaviors.
- For desktop, preserve the host conventions for menus, shortcuts, windows, and focus. Use the existing framework, whether it is native, Compose Multiplatform, or a webview shell. Plan verification for each rendering layer affected.

## Specify the motion

Apply this skill's division: expressive marketing, efficient apps. For marketing, design a composed opening and any justified signature sequence around the product narrative; a generic fade applied to every section is not choreography. For frequent app tasks, favor state continuity, spatial origin, prompt feedback and interruptibility over spectacle. Do not force an animation quota onto either surface.

Separate entrance, narrative and state-feedback motion. For each, identify what the user learns from movement, what remains visible before it starts, and the settled composition. Test first visit, return visit, fast scrolling or repeated input, touch and reduced motion. A delayed entrance must not keep an essential action unavailable. No scroll hijacking or indefinite decorative activity solely to make the page feel advanced. Use temporal evidence for a motion claim; still screenshots establish only their displayed frames.

For each meaningful transition, record **purpose → trigger → start and end state → timing and easing → input and reduced-motion behavior → verification**. Test interrupted or repeated interactions, focus timing, and whether the final state is correct when the transition is cancelled or skipped. Keep content, controls, and status feedback usable throughout.

Use CSS for straightforward web feedback. Reuse the project's motion library for coordinated layout and state changes where it helps. Consider scroll choreography when the approved design calls for it and the static, touch, and reduced-motion experiences remain coherent. Prefer native animation APIs on Android, iOS, and desktop. Keep shell or navigation behavior under the platform's control.
