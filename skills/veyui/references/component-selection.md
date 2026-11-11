# Component selection and integration

Choose for a specific behavior in the actual platform. Read the project's dependencies, component source, theme and versions first. Reuse a sound existing foundation. A new package must solve a gap worth its integration cost; a curated name is not a mandate to migrate.

Read [Component craft](component-craft.md) before choosing the visual presentation. Preserve accessible behavior while deliberately designing the control's trigger, value, affordance, label, open surface and state transitions. For an art-directed web concept, browser-default select chrome is not an automatic finished result. A native control can still be a deliberate appropriate choice; do not introduce a universal ban or force a particular vendor.

## Decision procedure

1. State the job and difficult states: for example searchable multi-select with async results, keyboard selection, empty/error and many items.
2. Check the existing component and native platform facility. Prefer extending a sound component over introducing a second behavior system.
3. If there is a gap, select one suitable candidate from the task map or Component catalog. Check current official docs for the installed or proposed version, source/license, framework and rendering compatibility, accessibility behavior and runtime cost. This focused API check is distinct from reference-image research.
4. Inspect the source/registry changes before writing: dependencies, CSS resets, theme variables, aliases, generated paths, client boundaries and overwrite scope. Do not run a blanket initializer over a designed application.
5. Keep behavior, replace demo styling with approved tokens and anatomy, wire real data, then inspect all affected states in context.
6. Record `need | existing option | chosen solution | reason | exact version/item | license | changed files | behavior and visual checks`.

## Web task map

These are starting candidates adapted from the researched sources, not claims that one package is always best. Verify compatibility before adoption. Equivalent existing libraries are valid.

| Need | Candidate / preferred starting point | Selection detail |
|---|---|---|
| Basic links, buttons, inputs, disclosure | Semantic HTML and existing components | Do not add a library for a simple element |
| Dialogs, menus, selects, popovers | Existing shadcn primitives; Base UI, Radix or React Aria when a gap exists | Keep a coherent focus, dismissal and portal model; shadcn is editable source, not a complete design direction |
| Command palette | cmdk or the project's current palette | Commands, navigation, shortcuts, empty results and focus restoration |
| Toast | Sonner or the existing notification layer | Use local errors for corrections; do not make transient toasts the sole record of failure |
| Verification code | input-otp or an accessible existing input | Paste/autofill, keyboard, retry and expiry; never six independently hostile fields |
| Coordinated layout/exit/gesture motion | Motion or the existing animation library | CSS is sufficient for ordinary hover/fade; preserve reduced motion |
| Changing numeric values | NumberFlow or restrained native text update | Align digits/units and preserve readable final values |
| General charts | Existing chart library or Recharts | Units, baseline, missing data, contrast, keyboard/table alternative |
| Continuous streaming chart | Liveline if its model fits | Bound history and re-render cost; make pause and time domain clear |
| Drag and drop | dnd kit or existing solution | Keyboard and menu alternatives, optimistic rollback, target feedback |
| Long lists/tables | Virtuoso or current virtualization | Measure the actual workload; preserve focus, selection and reading semantics |
| Code syntax | Shiki | Language, theme, contrast, server/build rendering cost |
| Share images | Satori if supported by the pipeline | Verify fonts, supported styling and output dimensions |
| Shared client state | Existing state model; Zustand if justified | Local state remains local; do not install global state for a simple toggle |
| Class/variant composition | clsx; CVA for real variants | Match current CSS/Tailwind architecture rather than rewriting it |
| Web theme switching | Existing provider; next-themes for compatible projects | Initial theme, hydration, native controls and persisted/system preference |
| Specialized expression | Cobe, torph, Leva/dialkit or catalog item when its task exists | An effect is not a reason to create a product requirement |

## Native and desktop mapping

Android: existing Compose/Material or custom theme, native state and accessibility semantics, adaptive pane/navigation behavior. iOS: SwiftUI/UIKit or existing framework, native presentations, Dynamic Type and system interactions. Desktop: current toolkit's focus traversal, menus, shortcuts, resizable panes and window lifecycle. Cross-platform frameworks still need target-specific review. Do not install React, Tailwind, shadcn or a browser motion library into a native screen merely because its visual reference was web-based.

Use semantic tokens across platforms, not a universal pixel export. Distinguish visual row size from touch hit area. A touch-first compact view may need larger targets while a pointer workspace retains efficient density.

## Integration acceptance

Test keyboard order, focus return, accessible names, pointer/touch, long content, loading/error/empty states, overlays, themes and reduced motion as relevant. Inspect lazy-loading and actual client cost for large effects. Confirm imported styles do not alter unrelated routes. The component must look like part of this product, not a vendor demo pasted into it.
