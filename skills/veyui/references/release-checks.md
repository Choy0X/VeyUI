# Release checks

## Scope the audit

Apply Visual review before a visual-readiness claim. Code quality, accessibility checks, and visual craft are independent requirements. A checked box for a named skill is not evidence.

List the changed screens, states, source paths, and shared components. Run the project in a browser, emulator, simulator, or installed desktop app as appropriate. Review representative screenshots or recordings against the accepted design. Review visual spacing, color and contrast, alignment, type wrapping, shape consistency, focus visibility, imagery, responsive layouts, and motion in context. Use Playwright or the project's existing browser tooling on web. Use platform-native screenshot, interaction, and accessibility tooling for native apps. A webview needs web checks plus its relevant native shell checks.

## Verify the behavior

| Surface | Minimum evidence for the scope |
|---|---|
| Web or webview | Run the bundled Interface audit and capture source findings with file and line. Inspect desktop, narrow/mobile, and affected intermediate widths. Check keyboard/focus, semantics, CTA/form behavior, zoom or reflow, reduced motion, overflow, and console errors. Check rendering and loading budgets for major imagery or motion changes. |
| Native mobile | Map the Interface audit’s applicable intent to the OS. Inspect compact and expanded layouts where shipped. Test screen reader labels/order, large text, insets, system back, keyboard/IME, system motion settings, and representative flow completion and failure states. |
| Native desktop | Map applicable Interface audit intent to the OS. Inspect minimum and wide sizes and relevant scaling. Test keyboard navigation, focus, shortcuts, menus, dialogs, screen reader semantics, and pointer states. |
| Design or prototype | Compare the artifact with the brief and review representative screens, input paths, and applicable failure or recovery states. Exercise the promised prototype interactions, state what is simulated, and record native or web implementation checks separately. |

For native mappings, use these examples as starting points. HTML label and ARIA rules map to platform accessibility labels, roles, states, and announcements. CSS focus rules map to visible native focus and traversal. Web reflow rules map to text scaling and supported window or device sizes. Reduced-motion and keyboard rules map to system preferences and input methods. DOM-, HTML-, browser-history-, and CSS-specific rules can be marked inapplicable with a reason. Never mark a web rule as tested on native unless there is a corresponding native check and evidence.

## Decide readiness

Recheck the [seven craft passes](seven-craft-passes.md) on the integrated version. Preserve the selected concept’s task hierarchy, grouped spacing, typography, color roles, credible content, component detail and motion relationships. Resolve material regressions and distinguish implemented behavior from visually or temporally inspected evidence.

For staged product scenes, apply the rehearsal in [Product demonstrations](product-demonstrations.md) on the integrated page. Verify the final scene version, compact composition, reduced-motion still and applicable playback controls. Keep this evidence separate from functional tests of real app actions; a simulated cursor sequence cannot pass the primary user-flow check.

- Run the repository checks relevant to the diff. Exercise the primary flow and any material regression risk. Distinguish manual checks, automated checks, and claims supported only by inspection.
- Fix in-scope failures that block the primary task, accessibility, integrity of the layout, or the agreed performance and motion budgets. Re-run affected checks. Carry minor residual findings forward with the impact and rationale.
- Mark a required step as passed only when evidence exists. Mark absent tools, inaccessible rules, unavailable devices, and missing approved assets explicitly. Use an equivalent check only when it satisfies the same criterion, and record how. An unavailable external skill is not a blocker; an unavailable required render or interaction check is.
- Give a compact handoff with the delivered scope, preview or captures where available, review outcomes, release status, and any unresolved findings. For each required stage record **stage | result | evidence or reason**. Use **ready for release**, **implementation complete with verification pending**, **blocked**, **prototype reviewed**, **design reviewed**, **draft — visual review blocked**, or **specification only** as supported. Readiness does not imply deployment.
