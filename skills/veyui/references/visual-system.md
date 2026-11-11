# Build a coherent visual system

## Translate references into relationships

Use reference analysis to define scale, proportion, grouping, contrast, density, material and rhythm. Choose actual values for this project after rendering them. Do not treat a screenshot as an exact token specification or apply a generic preset solely because it looks fashionable.

Use the eight user concept observations in `data/user-benchmarks.json` as a quality target for composition and craft. They represent different useful directions, not one style to blend indiscriminately. Liquid Brokers suggests a luminous focal object; ProFinance concentrates bold color; Juris and Quick Actions demonstrate restrained operational hierarchy; Twinkle and Zentro integrate environmental imagery; Galileo varies compositional scale. Their presentation framing is not necessarily product UI.

## Construct and inspect the system

| Layer | Decisions and checks |
|---|---|
| Content hierarchy | Prioritize one main message/task, supporting evidence and secondary action. Make dominance visible through scale, position and contrast rather than adding badges everywhere. |
| Typography | Choose display, heading, body, label and numeric roles. Specify family/fallback, size, weight, line height, measure and tracking. Inspect actual words, font loading and scripts/locales. Do not impose a fashionable font on every platform. |
| Color | Define canvas, surfaces, text, muted text, borders, accent, focus and status roles. Test actual pairs and states. Distribute accent intentionally. Preserve brand colors unless change is authorized. |
| Spacing | Define a small scale and relationship-specific use for label/value, control groups, sections and page margins. Optical corrections are allowed when intentional. Avoid one large padding value repeated everywhere. |
| Geometry | Define grid edges, content widths, row heights, control hit areas, icon proportions, radius hierarchy and overlay layers. Adapt composition at content-driven breakpoints. |
| Materials | Choose when a border, surface tint, shadow, blur or transparency establishes hierarchy. Avoid stacking all effects. Verify readability over changing backgrounds. |
| Assets | Define subject, crop, focal point, aspect ratio, palette, lighting, source and fallback. Design imagery into the composition before filling leftover boxes. |
| Motion | Define purpose, trigger, phases, timing/easing or spring behavior, interruption and reduced-motion equivalent. Scope expressive motion to places where it helps. |

Use semantic token names whose values can differ by theme or platform. Keep a shared product meaning while allowing platform-specific values. Map tokens to CSS variables/Tailwind, Compose theme roles, SwiftUI styles or the actual framework. Do not export web pixels as universal native dimensions.

Use [Component craft](component-craft.md) for context variants and detail checks; do not reuse a header max-width for a full dialog field.

Create a representative specimen using real content: headline, body, action group, input with error/focus, populated collection, empty state and one relevant overlay or transition. Inspect the specimen in context; a token JSON alone cannot establish a visual system. For a marketing-only scope use relevant sections and interactions rather than inventing a dashboard specimen.

## Avoid predictable generic output

Identify the mechanism causing genericness before changing it. Typical causes include identical card proportions for unrelated content, every section using the same split layout, uniform visual intensity, unrelated glowing effects, arbitrary gradients, excessive rounded pills, tiny low-contrast text, fake product chrome, decorative metrics and stock phrases.

None of those visual techniques is universally forbidden. Use a card when grouping helps, a gradient when it supports the concept, and a pill when its role benefits. Remove the automatic repetition and unsupported meaning. Distinctiveness should survive removal of the logo and decorative effects, while core task clarity survives removal of animation.

## Art direction without losing usability

Give expressive compositions a quiet counterpart for task-intensive areas. A marketing site may use a wider visual range than its embedded dashboard. A native app may use a characteristic illustration, color relationship and type treatment while retaining familiar navigation. A desktop editor can express craft through density, alignment, selection feedback and spatial continuity.

For an ambitious visual brief, first build a high-fidelity representative section or task at wide and compact sizes. Compare it directly with the selected references for hierarchy, balance, detail, imagery quality and rhythm. Record the biggest visible gap and fix it before expanding. Do not judge fidelity from source code or a reduced-size full-page thumbnail alone.

Preserve intentional variation. Consistency means shared rules and relationships, not making every section identical. Document the few exceptions that create the concept's identity and test their adaptive behavior.
