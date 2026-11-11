# Finish the controls people actually use

Read before constructing fields, menus, dialogs, sheets, navigation or other repeated interactive components, and whenever feedback identifies spacing, sizing or generic controls. This is construction guidance. Use the actual project system and choose the component anatomy before multiplying screens. A good hero and working click path do not establish component craft.

## 1. Design anatomy and relationships

For each relevant component family specify the label, trigger/control, displayed value, icon/affordance, helper/error, selected state and overlay. Name their sizes, spacing and behavior in context. Use `templates/component-specimen.md` within the existing brief; do not add another approval ceremony.

A field is a group, not adjacent text and a generic input. A practical web starting point is a stacked label/control/helper group with an explicit 8px gap and a 44–48px control hit area, adjusted to density and context after rendering. Native units and text scaling follow the host. These are proposed defaults, not reference measurements or mandatory universal values.

```css
.field-group { display: grid; gap: .5rem; min-inline-size: 0; }
.field-control { inline-size: 100%; min-inline-size: 0; }
.field-value { flex: 1; min-inline-size: 0; }
.field-affordance { flex: none; }
```

The pattern establishes the grouping; it is not a complete visual design. Resolve actual padding, type, surface, border, focus treatment, helper spacing, icon clearance and open-state material against the selected concept. A horizontal label/control layout needs an intentional gap, aligned baselines and a compact reflow rule.

## 2. Separate variants by context

Header utility, form field and dialog picker may share behavior but need explicit layout variants. Do not reuse a header's narrow max-width or pill styling for a full-width dialog field. Avoid global selectors that accidentally impose one context's geometry on every select, button or input.

A reported defect in a client dashboard was specific: an inline “Preview as” label sat beside a picker reusing the narrow header account class. The placeholder was clipped and the control looked unrelated to the dialog. The correct repair is a grouped label and full-width field variant with reserved chevron space, coherent material and the complete placeholder visible. Merely adding margin or a new animation would leave other faults intact.

Size to actual content. Inspect the placeholder, longest supported value, long/error helper and relevant localization. Reserve the affordance width and its gap independently of the value. Do not make essential choice text fit by shrinking its font. Use wrapping, a wider bounded field, an appropriate compact layout or intentionally disclosed truncation for genuinely long values. A normal short placeholder such as “Choose an account” should fit without truncation. Test text enlargement and zoom when the task requires accessibility coverage.

## 3. Choose custom presentation with reliable behavior

For a deliberately art-directed web concept, use project-styled controls rather than leave browser-default select chrome as an accidental fallback. Prefer the project's existing accessible/headless foundation and customize its anatomy. Native controls are still valid for appropriate platform behavior, an existing system or an explicitly chosen tradeoff; do not impose a universal ban. Native Android/iOS/desktop UI should respect its toolkit instead of importing web widgets.

A custom select is a value picker; an action menu is a different semantic pattern. Implement or preserve the right roles, accessible name, selected/active option, keyboard navigation, typeahead, focus return, disabled states and form value. Decorative divs and chevrons are not a finished replacement. Do not rebuild complex accessible behavior from scratch just to avoid a dependency.

Menus need a stable trigger, deliberate minimum width, bounded height/scroll, viewport collision handling and the correct layer inside dialogs. The overlay may exceed a short trigger's width when labels require it. Keep the control anchor stable during press. On touch, avoid sticky hover and tiny targets. Verify that Escape dismisses the picker first and preserves the enclosing dialog, that Tab proceeds naturally, and that an outside press does not select an option.

## 4. Resolve the overlay as a complete composition

Inspect title, description, content, dividers, grouped fields, totals, helper copy, primary/secondary actions and close affordance together. Make spacing communicate these groups; do not distribute equal padding everywhere. Match trigger/menu/dialog materials to the active concept's palette, radius and typography. A dark concept needs its actual default, open, focus, selected and disabled colors inspected.

Constrain height to the usable viewport and scroll the appropriate body. Keep the primary action reachable, the close control visible and focus unclipped. A menu in a scrolling dialog must escape clipping and track, reposition or close on scroll/resize. Do not shrink the whole dialog to fit more content. Compact layouts may recompose imagery and actions, or use an appropriate sheet, while preserving the task.

## 5. Give interaction states intentional motion

Read `motion-design.md`. Pick motion for the actual relationship: anchored menu opening, active option feedback, selected label change, dialog/backdrop entrance and exit, tab indicator travel, layout/content replacement and pending/result feedback. Hero reveals and hover lifts alone do not satisfy a request for a motion-rich interface.

When the user requests Motion, use the compatible Motion package for the coordinated web interactions and verify the real code path runs. Other ordinary projects can use their existing engine; native apps use host animation APIs. CSS remains suitable for simple feedback. Installing a dependency, adding duration tokens or writing a storyboard does not implement motion.

Keep entering and exiting surfaces mounted for their transitions, while preserving correct interaction/focus behavior. Handle rapid reversal, resize and new intent. A menu opened while its parent dialog is still transforming must measure a settled anchor or continuously correct its placement; otherwise its size/position drifts. Do not scale text, move the hit target on press, wait for animation before accepting input or replay the entire page entrance after every selection.

## 6. Inspect details at their delivered size

For each material family, render its default, focus and open/active states with real content, plus relevant error, loading, disabled, long-value and compact cases. Prioritize the components this task actually uses, not an exhaustive unrelated specimen gallery. Inspect close detail in context, not only a zoomed-out whole-page image. Review the weakest control independently.

Record observable evidence: label/control gap, trigger/value/icon relationship, full text fit, menu bounds, overlay clipping, action clearance and compact reflow. DOM measurements can confirm suspected spacing/overflow; they do not judge taste. A useful field check compares the real label/trigger rectangles and displayed value's text extent to the available space after padding/icon reservation. Do not assert universal pixels or a visual PASS from source selectors alone.

Verify keyboard/pointer behavior and then re-render the corrected component. Include open and closed states, changes between them and reduced-motion behavior. An actual screenshot with the field open is required before calling it visually reviewed. If temporal inspection is unavailable, distinguish implemented motion from motion actually observed. Do not call a field finished because its value changes in a functional test.

## Reference lessons, not mandatory vendors

Reviewed 2026-11-08: [Arc Select](https://uiarc.dev/components/select), [Arc Dropdown](https://uiarc.dev/components/dropdown-menu), [beUI Animated Dropdown](https://pro.beui.dev/components/animated-dropdown), [beUI Animated Modal](https://pro.beui.dev/components/animated-modal). Arc select and beUI modal were interacted with in the browser; related descriptions/docs were reviewed. This was focused inspection, not a complete accessibility/performance audit.

Arc documents stable anchored triggers, keyboard selection, separate animated/semantic values and reduced-motion treatment. beUI describes related surface/focus transitions; its modal specimen visually separates heading, field and footer actions. The original synthesis here is to treat geometry, semantics and state choreography as one component design problem. Do not install either library by default or copy restricted source. Public demos and documentation do not grant source rights. If current vendor details matter, verify them again.
