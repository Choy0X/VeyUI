# Usage

veyUI activates when you ask for UI design work. Say it by name to be sure, for example "Use veyUI to ...".

## Modes

These are natural-language routes through the workflow, not shell commands.

| Say | What happens |
|---|---|
| `veyUI design` | Full workflow for a new page, app or screen: discovery, directions, three concepts, choice, build, verify. |
| `veyUI redesign` | Same, starting from your existing UI and a feature-to-benefit inventory of the product. |
| `veyUI prototype` | Stops after the three hosted concepts and their review. |
| `veyUI polish` | Targeted craft pass: hierarchy, spacing, type roles, color, components, motion. |
| `veyUI audit` | Reviews an existing interface against the interface audit and reports findings. |
| `veyUI motion` | Chooses and implements purposeful motion, with reduced-motion handling. |
| `veyUI system` | Builds or documents a design system and tokens. |
| `veyUI references` | Searches the offline library and recommends directions with verified example links. |

Scope follows the request. A small, settled edit does not trigger a full redesign.

## Example prompts

> Use veyUI to inspect this project and recommend design directions with real examples I can open. After I choose, build three complete concepts in an isolated preview, critique them, and give me links before you touch the app.

> Use veyUI to audit the checkout flow for hierarchy, copy and accessibility.

> Use veyUI to redesign the dashboard for a dense, desktop-first monitoring tool. Keep our brand colors.

> Use veyUI to add motion to the onboarding steps. Respect reduced motion.

## The workflow

1. **Discover** the product from the project: features, plans, integrations, release notes. The existing page is not treated as the product inventory.
2. **Recommend** three project-fit directions, each with a checked public example, what to adapt and a tradeoff. You can supply your own references instead.
3. **Prototype** three distinct, complete concepts in an isolated workspace and host them. Each is rendered and reviewed.
4. **Choose.** You select, delegate the choice, or waive exploration. veyUI honors that.
5. **Implement** in your real stack, keeping your runtime and brand.
6. **Verify** with rendered inspection and the bundled checks. The report says what was and was not checked.

Image generation always needs your permission.

## Offline reference library

The scripts work without a network:

```sh
python skills/veyui/scripts/design_library.py stats
python skills/veyui/scripts/design_library.py brief "billing settings" --platform web
python skills/veyui/scripts/design_library.py search "empty state" --platform mobile
python skills/veyui/scripts/reference_library.py search "pricing" --limit 5
```

Run any script with `-h` for options.
