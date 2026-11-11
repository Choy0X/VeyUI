# Platform and tool routing

## Common design, appropriate implementation

Share product meaning, brand relationships and semantic token roles across platforms. Adapt navigation, input, density, presentation and motion to the host. Do not make a phone app a miniature desktop dashboard or a desktop app a stretched phone screen.

| Target | Design and implementation route | Evidence needed |
|---|---|---|
| Web marketing | Existing web stack; semantic HTML; CSS/Tailwind when already appropriate; Motion only for justified coordinated behavior | Real browser renders, content loading, CTA destinations, compact reflow, keyboard and reduced motion |
| Web application | Existing primitives or a deliberate choice among shadcn, Radix, Base UI, React Aria and project components; one coherent styling system | Real task states, keyboard/focus, data boundaries, long content, responsiveness and interaction evidence |
| Android / Compose | Current Android guidance, existing Material theme or intentional custom system, adaptive window/pane patterns, Compose semantics and state-based animation | Emulator/device renders, Back, insets, IME, text scaling, touch and other supported inputs; physical-device-only evidence labeled |
| iOS / iPadOS / SwiftUI | Current Apple HIG, native navigation/presentation, Dynamic Type and accessible system behavior; custom visual language within host conventions | Simulator/device renders, accessibility sizes, safe areas, keyboard, dismissal and interruption behavior |
| React Native / Expo | Existing platform components and animation stack; follow each host's navigation, accessibility and input rules | Native runtime evidence per target; a responsive website does not establish native correctness |
| Windows / macOS / Linux desktop | Existing native, Compose, Qt, Flutter, Electron or Tauri framework; host menus, shortcuts, windows and focus; Fluent or Apple guidance as appropriate | Minimum/wide windows, display scaling, keyboard, pointer, menus, dialogs and multi-window behavior where supported |
| Webview shell | Web semantics and rendering plus explicit native shell integration | Browser checks and native lifecycle, permissions, navigation, shortcuts and window behavior |

Verify exact framework/package APIs against official documentation matching the project's versions before writing code. Resolve overlapping Android concerns using the existing project architecture and version-matched official APIs. Do not add a new framework merely because the reference used it.

## Tool capability preflight

Identify available tools at the beginning, not after producing an unreviewed artifact. Record what can actually render, capture, inspect, interact, measure and persist. Prefer installed project tooling. Respect the host's tool-use policy and access boundaries.

| Need | Free/local route when available | Limit |
|---|---|---|
| Pattern retrieval | Bundled `design_atlas.py` or direct JSON reads | Text guidance and source discovery, not visual evidence |
| Reference knowledge | Compiled ready-screen descriptions through design_library.py | No source-image or URL retrieval during normal design; new-source ingestion is separate |
| Design composition | Code prototype in the isolated concept workspace or an available design editor | A design editor account is optional; never require paid Figma features or MCP |
| Web render and input | Existing browser tooling or Playwright | Launch failure means checks did not run; do not bypass environment restrictions |
| Isolated component states | Existing Storybook or a lightweight route in the isolated concept workspace | Do not add Storybook for a one-off if an existing preview suffices |
| Accessibility | axe-core where appropriate plus manual keyboard and assistive-technology checks | Automated findings do not certify accessibility |
| Performance | Browser profiling and Lighthouse where available | Lab results do not prove field performance or aesthetic quality |
| Native review | Platform previews, emulator/simulator, screenshots, accessibility tools, device testing | Static previews and web surrogates do not verify host behavior |
| Evidence completeness | Bundled `check_evidence.py` | Checks files and declarations only; cannot inspect visual quality or validate truthful claims |
| Imagery | Approved existing assets or an available generation tool after explicit permission | Generation may have costs; avoid inaccessible or unlicensed asset dependencies |

Do not claim a tool ran without a result. If the exact tool is unavailable but an authorized equivalent satisfies the criterion, record the substitution. Otherwise complete unaffected work and mark the relevant evidence blocked. Do not fabricate a tool named after a design skill.

## Built-in guidance and optional host tools

All design guidance is bundled. Use Planning, Craft, Component selection, Motion design, Product demonstrations and Interface audit as the task requires. Missing third-party skills never block veyUI. Missing runtime or rendering capability can block a specific verification claim.

Use additional available host capabilities only when useful: design-system extraction for existing approved visual language; shadcn guidance for its registry and components; Compose guidance for native Android; framework performance guidance for material rendering cost; image-generation guidance after asset permission. Discover exact installed names. Do not invent availability, bundle third-party skill text without rights, or silently install global hooks.

Use one lead with independent visual and UX/engineering reviewers when delegation is available and authorized, as specified in Review team. When unavailable or prohibited, perform the same perspectives sequentially and disclose self-review. Pass actual artifacts, references and review scope without the lead's desired verdict. Multiple agents cannot replace seeing the rendered work.
