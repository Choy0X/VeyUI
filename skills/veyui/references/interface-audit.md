# Interface audit before delivery

Apply this built-in review to changed files and their real rendered consumers. It integrates web interface concerns into veyUI without fetching another skill. It is a practical audit, not an exhaustive accessibility certification. Read current official APIs when implementation details depend on a version.

## Audit dimensions

| Dimension | Source and runtime checks |
|---|---|
| Semantics | Actual buttons for actions and links for navigation; meaningful landmarks, heading order and table semantics; named icon controls; decorative graphics hidden appropriately; informative media has equivalent descriptions |
| Keyboard and focus | Logical traversal and visible focus; no positive tabindex; overlays manage entry, containment, Escape and return; sticky layers do not cover focused items; keyboard alternatives for drag/gesture operations |
| Forms | Visible associated labels, useful names/types/input modes/autocomplete; allow paste and password managers; coherent required/help/error association; preserve input on failure; pending state prevents duplicate submissions; success reflects the actual response |
| Error recovery | Identify the affected field/action and useful next step; distinguish empty from failed, denied from unavailable and pending from success; reconcile uncertain mutations before retry |
| Content resilience | Short/long/empty data, long words, localization, real collection sizes, multiline controls, text scaling and zoom; flexible children can shrink appropriately; deliberate truncation retains a way to access essential content |
| Layout | Content-driven adaptation, stable shared edges, no accidental overlap or hidden overflow; legitimate scrollable tables/canvases are contained and discoverable; safe areas and on-screen keyboard do not obstruct actions |
| Touch/pointer | Adequate targets and spacing, hover/active/focus feedback, no hover-only essential action, deliberate gesture handling; preserve useful native scrolling and zoom |
| Navigation and state | Real destinations and standard link affordances; useful shareable filters/tab/page state belongs in the URL where appropriate; Back/Forward restore meaningful context; unsaved work is protected; destructive actions have proportionate confirmation or undo |
| Media | Correct aspect ratio and reserved dimensions; prioritize actual critical imagery, lazy-load genuinely offscreen assets; no broken posters or invisible fallback; loading choices verified in the actual page |
| Typography | Final font loaded with intentional fallback; readable measure and hierarchy; numbers/units align; awkward wrapping and isolated units fixed; typography/case follow the product and locale rather than universal title-case rules |
| Theme | Semantic roles, actual contrast pairs, focus and status differentiation; native input and scrollbar colors agree with theme; system/user preferences persist without a misleading flash |
| Motion | Explicit properties, meaningful origin, cancellation, reduced motion, static outcome and required playback control; no delayed essential task; no uncontrolled background animation |
| Performance | Profile actual long-list and input work; virtualization when it solves measured or credible scale issues while retaining semantics; batch layout reads/writes; avoid unnecessary per-frame layout and oversized assets; separate lab from field evidence |
| Localization | Locale-aware dates/numbers/currency, language and direction handling, pluralization, longer labels; preserve code/identifiers from inappropriate translation |
| Rendering | Server/client markup and theme agree; controlled inputs have valid handlers; no blanket hydration-warning suppression; verify route reloads and asset paths, not merely hot-reload behavior |
| Truthfulness | No invented metrics/reviews/prices; actual CMS/data/action contracts preserved; simulated proof and unshipped capabilities clearly bounded |

Use appropriate live-region announcements for important asynchronous status without reading every animation or stream token. Native semantic controls already implement keyboard behavior; do not duplicate handlers and trigger actions twice. Do not disable autocomplete universally, hide overflow to mask defects, virtualize every collection solely by item count or put every ephemeral state into the URL.

## Native mapping

Use the host accessibility tree, labels, roles, selected/disabled state and announcements. Review system Back/dismissal, safe areas, IME, font scaling, pointer/keyboard, min/wide windows, display scaling, host menu conventions and lifecycle. Mark HTML-only checks inapplicable; perform the corresponding native check rather than claiming a browser pass establishes native quality. Webview applications need both layers.

## Findings and readiness

Record `severity | file:line or screen/control | observed failure | user consequence | correction | evidence`. Separate observed defects, risks inferred from source and untested conditions. Include at least the task's primary path, important recovery, compact/wide layout and changed shared consumers. Run applicable project checks and capture current results. Fix in-scope major failures, repeat affected checks and keep residual limitations explicit.

Review visual craft separately. Passing this audit cannot establish aesthetic quality. Completion requires the actual version to meet the chosen design, functional task and relevant technical checks. Report unavailable verification honestly; never replace a failing test with an unsupported success claim.
