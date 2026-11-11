# Concept adaptation and redesign

Use this to rework existing UI, translate outside references, or turn a selected prototype into a design that fits the host project. The chosen concept sets a direction. The design contract specifies the working result.

## Start from the incumbent and the references

- Capture representative before views at the sizes and states affected. Trace real routes or navigation, role and permission behavior, data, validation, focus, and the success and recovery paths. If the UI cannot run, use source or user-provided evidence and label the gap. Identify shared components and downstream consumers that can regress.
- Record what must be preserved, what the redesign may change, and what is explicitly in scope. Give each proposed change a reason tied to the user's task, a known defect, or the approved direction. Keep a note for each deliberate change to behavior or design tokens.
- Retrieve compiled screen knowledge and extract the useful principle; inspect an outside reference only for explicit ingestion or a newly supplied image-matching task. Examples include how a sidebar groups destinations, how a hero alternates density, or how motion communicates a state change. Record measured values, visual observations, and inferences separately. Adapt the principle to the host's context. Verify rights before reusing source or visual assets.

## Map the concept to the host

For each material part, record **source cue or prototype decision | retain, translate, or drop | target rule or component | reason | verification**.

| Area | Translate into the real project |
|---|---|
| Layout and navigation | Map sections to real pages or screens, actual destinations, reading order, safe areas, and resize or reflow behavior. Preserve the context a user needs when returning from details. |
| Visual identity | Map the reference's design principle to the project's semantic colors, type, spacing, density, shapes, and icons. Document the intended exceptions and affected consumers. |
| Components and data | Replace illustrative interactions with existing or approved primitives and real state handling. Map demo objects to the actual data model and permission checks. Keep mocks identified in prototype handoffs. |
| Assets and motion | Choose the actual asset, provenance, crop, loading behavior, and fallback. Adapt the motion to input methods, native conventions, reduced-motion preferences, and performance budgets. |
| Content and controls | Use accurate labels, product claims, validation, next steps, focus behavior, and recovery. Fit realistic and localized content to the composition when relevant. |

## Review and hand off

1. Build the smallest representative frame or prototype that tests the adaptation. Include the same baseline view and state for comparison when available. Review first for task completion, then for visual continuity and craft.
2. Confirm each material deviation from the chosen concept or existing behavior. Treat a materially changed primary action, navigation model, brand direction, or critical state as a design decision to reopen.
3. Hand off the selected concept link, the adapted target views, approved tokens and components, state and motion notes, asset sources, unresolved dependencies, and the requirement-to-check mapping. For code, implement against this contract and revisit the affected baseline flows before calling the redesign complete.
