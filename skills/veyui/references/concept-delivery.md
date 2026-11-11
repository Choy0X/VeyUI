# Automatic concept delivery

Read this before any new UI or substantial redesign. This is the default execution path, not an optional service the user must request. A request such as “rework my landing page” authorizes isolated exploratory prototypes. It does not select their visual direction. A written plan, moodboard, screenshots alone, or files the user must launch themselves do not satisfy the runnable-preview milestone.

Before construction, resolve open inspiration through Recommended directions and its verified existing-example links. Honor an existing direction or delegated choice. External reference links do not fulfill the generated-concept milestone below.

## Execution boundary

1. Read the project and baseline without modifying production routes, screens, shared styles, assets, dependencies, or configuration. Record the current working-tree state so existing user changes are not mistaken for your changes.
2. Create a separate concept workspace outside the application source tree. In a repository-backed preview, use an isolated branch/worktree or the host's separate preview project. Never test a new concept by first replacing the real landing page. A read-only reference to existing source is fine. An isolated worktree may contain a copied application and exploratory changes, while the user's original application checkout remains unchanged. Do not merge or copy the exploratory changes back before selection.
3. Briefly state that you are preparing three runnable directions and will present the previews before integrating a choice. Do not ask whether the user wants concepts. Use the count they explicitly request. Existing approval of a specific design, an explicit instruction to skip exploration, or an exact small correction can bypass exploration; a general “implement/rework/redesign” request cannot. Fixed branding still permits different compositions or interaction structures.
4. Build three credible candidates by default. Give them comparable scope and fidelity: the complete landing page or a representative end-to-end application task with key states, adaptive layouts and relevant motion. Do not present a polished opening with unfinished lower sections. Do not include the unchanged incumbent as one of the three. Build all directions in the preview workspace, including any candidate based on the incumbent. Avoid one integrated candidate and two disconnected mockups.
5. Render, inspect, repair, host and verify access using the steps below. Only then present the actual decision. Do not stop at “next I can build the concepts.”
6. Keep previews available while the user reviews. Wait for their selection before application integration unless they already explicitly delegated that selection. Approval to make prototypes is not approval of a winner. If selection is delegated, still create/review/link the concepts, record the reason for your choice, and continue within existing implementation authorization without asking again.

## Establish the delivery route before building

Inventory the actual host tools, their documentation, runtime and network access. Select one supported route. Do not assume a provider, MCP, paid account or URL exists.

| Environment | Delivery route |
|---|---|
| Agent on the user's computer | Start the isolated preview server in a persistent process/session; verify the actual localhost gallery and every candidate URL in the browser. Local hosting is sufficient when the user shares that machine. |
| Remote workspace with forwarded ports | Start the preview server with the host-required binding and use the documented port-forward URL. Open the returned user-facing URL, not only container localhost. |
| Managed preview/hosting tool | Use that tool's current instructions to create a separate review preview, obtain its actual URL, then open and inspect it. Do not deploy over the production site. |
| Native/mobile/desktop project | Build isolated native candidates in the appropriate preview/emulator/runtime. Provide a hosted review gallery of actual captures/recordings plus available native builds/preview access. Label a browser simulation as a simulation; hosting screenshots does not make native behavior browser-interactive. |
| No usable hosting/rendering route | State the exact missing capability. Continue research/design or prepare draft files, but keep the concept milestone blocked. Do not call a ZIP “hosted,” fabricate URLs, bypass a rejected tool restriction, or silently proceed to production integration. |

“Free” means use existing local/forwarded/free preview capabilities first. Do not purchase hosting, establish public tunnels, expose private source, or publish confidential material merely to satisfy the milestone. An access blocker changes delivery status, not the design requirements.

## Build the review surface

The optional stdlib utility `scripts/concept_studio.py` creates an empty three-direction workspace and a gallery from its manifest. It supplies review infrastructure, not a landing-page design template. Resolve its installed path and execute:

```sh
python3 /path/to/veyui/scripts/concept_studio.py init /absolute/isolated/concepts --kind landing
# Author each candidate independently; replace manifest draft labels and fill real review evidence.
python3 /path/to/veyui/scripts/concept_studio.py build /absolute/isolated/concepts
python3 /path/to/veyui/scripts/concept_studio.py check /absolute/isolated/concepts
```

For a static gallery on the user's machine, a supported persistent process can serve only its public folder:

```sh
python3 -m http.server 4173 --bind 127.0.0.1 --directory /absolute/isolated/concepts/public
```

Use the actual project stack for interactive fidelity when needed; static HTML is not mandatory. Its build output may be placed in the public folder, or the gallery may link to separately hosted candidate routes. Resolve nested assets, client routes and reload behavior. Do not proxy arbitrary gallery requests into the live app or depend on its authenticated/backend runtime for a candidate to be visible.

For app tasks use `--kind app`. The generated manifest requests full-page or task-state captures, scope completion and review records. Keep its required view set aligned with the actual scope for every candidate; do not remove required coverage to hide missing work. Under independent review, record both visual and UX/engineering findings for the current version. If delegation is unavailable, record `self-review` with the reason and the same review perspectives.

For native candidates, `--kind app` is a review-gallery scaffold, not a native application generator. Each candidate's `entry` is an HTML review page containing actual native captures/recordings and links or access instructions for its isolated runnable build/emulator preview. Its HTTP `preview_url` opens that review page, not an interactive web replacement. Set `runtime` to the actual native environment. Record native execution under `runtime_reviewed` and gallery access under `access_checked`; neither substitutes for the other. If only an emulator can run it, disclose that limitation and the available review/build access. If native execution is blocked, retain draft status even when the evidence page is hosted.

Record current versions on captures and review records. The checker compares these declarations; it cannot establish capture provenance from pixels. Rebuild the gallery after changing concept or review metadata; its receipt detects a stale generated gallery. The receipt is a local file-freshness check, not a signed review approval or proof that a deployed remote copy matches it.

For each candidate, include a separately labeled existing-example link and adaptation note from the planning shortlist (or the supplied reference), alongside the generated preview link. If the source is unavailable, disclose that status; never fabricate a replacement claim.

The gallery must show the real title, one-sentence premise, inspected wide/compact captures, scope and limitations, and direct “Open concept” links. Keep review chrome outside the designed page. Each candidate has a stable independent URL, not merely a screenshot or labels that toggle CSS variables. Provide restart/reset and an obvious way back to compare without overlaying controls on the hero.

Serve an explicit public directory. Exclude browser profiles, cookies, databases, caches, `.git`, credentials, recordings with private data and unrelated repository files from both hosting and exports. The supplied failed archive included browser profiles; they have no place in concept deliverables.

## Ready-to-review contract

For each actual version:

- The gallery and direct candidate URL open from the user's review surface. Check HTTP access plus a real render; a 200 response may be an error shell. Record local-only or session-limited access honestly.
- Fonts, illustrations, images and components load at initial render. Lazy/scroll-revealed content is checked throughout the page. The primary content and CTA remain discoverable without waiting for an animation.
- Wide and compact/native captures are personally inspected at readable scale. Include full-page/flow rhythm and critical details, not just the top viewport. Test the user's actual narrow target; a 500px render does not establish 390px behavior.
- Requested motion is implemented, observed over time and checked with reduced motion. A frozen screenshot or animation code does not prove choreography works.
- The main action and one relevant alternate state work or clearly disclose their simulation boundary. Essential screen/section composition is populated. Missing prices can use verified sample fixtures labeled illustrative, or a deliberately designed unavailable/see-plans state; permanent skeleton cards are not high-fidelity pricing design.
- The reference-fit review in `reference-calibration.md` finds no unresolved material mismatch. Strong implementation mechanics cannot compensate for the wrong art direction.

The utility checks file/manifest coverage only. It cannot establish that a human or agent actually inspected pixels, that declarations are true, or that a design is good. Never mark a view reviewed simply to pass it.

## Handoff and continuation

Present one gallery URL, the direct candidate URLs, the visible differences, one recommendation with tradeoff, and the selection needed. Keep technical logs out of the product preview. Do not shut down a local preview server immediately after sharing its URL. State its lifetime when session-based. If it expires before selection, restore and verify it rather than switching straight to implementation.

After selection, record the candidate version and exact approval/delegation, then produce the integration plan and implement that version. Run `check --stage implement` when using the utility. Preserve existing approval; do not add a redundant plan-approval ceremony. A materially altered hybrid goes back through visual review. Compare the integrated render against the selected preview to catch quality lost during integration.

Record selection in `studio.json` as `{"id":"b","version":"1","authority":"user-selected","evidence":"Actual user choice and its scope"}`; use `explicitly-delegated` only for actual prior delegation. Never manufacture an approval quote. Change the candidate version and repeat affected review when its design changes.

## Existing-example links in the gallery manifest

New studios set `reference_links_required: true`. Each candidate has `reference_links`, a list of records with `title`, `url`, `surface`, `where_to_look`, `adaptation`, `evidence_basis`, `checked_at` and `access_checked`. Fill these from actual source checks, using the final public destination and real check date. `surface` distinguishes a live page/demo from a tour or documentation screen; `evidence_basis` distinguishes current visual inspection from compiled observations and link-only checks.

The gallery renders these as **View existing example** links separately from **Open concept**. The checker rejects missing links or check declarations for new studios; it does not perform network requests or verify that the declarations are true. Unsafe/non-HTTP URLs and embedded credentials are rejected during generation. Rebuild after changing records. Existing older manifests remain readable. If the user explicitly waives references or a settled scope makes them inapplicable, set `reference_links_required: false` with `reference_exception_reason`; a blocked URL is not itself an authorization to waive the requirement.
