# Pre-extracted design library: default reference workflow

Use the compiled screen descriptions in `data/ready-screens.json` as the default precedent source. They contain original, palette-free observations extracted during library preparation from identifiable interfaces in released-product publisher screenshots or official documentation screenshots. They are ready to use as layout knowledge. They are not links that require the project agent to repeat visual research.

## Coverage in this edition

583 reviewed UI-state descriptions across 130 product labels: 268 mobile, 195 desktop and 120 web. The latest addition contains 174 reviewed views: 57 screens, 27 dialogs and 90 contextual panels; do not describe these as 174 full application screens. The previous 409 records were not separately classified by crop type. Each record is counted once, even if several sources reuse its image.

Web coverage now includes Linear, Proton Account/Mail, GitHub, Nextcloud Files, Bitwarden, Metabase and Grafana. Desktop additions include Visual Studio Code, OBS Studio, GitHub Desktop, Raycast and clearly identified operating-system dialogs. Eight flows summarize official documented behavior; none claims independently operated runtime evidence. Nineteen original decision guides cover difficult implementation choices.

The library now includes observed plan comparison, payment review, sharing controls and a field-validation error. It does not establish a complete payment-failure flow, comprehensive KYC, every product's current UI, or universal category coverage. Report a specific gap rather than using an unrelated error screenshot to imply payment-failure evidence.

## Token and network contract

- Retrieve three relevant screen descriptions initially. Do not read the entire dataset into context.
- Use `brief` for a combined coaching packet, `search` or `get` for screen-only evidence, and `flows` or `decisions` for focused lookup. These commands perform no network requests, load no images and emit no source URLs.
- The default combined brief is bounded to 7,500 Unicode characters and labels its three evidence types. The default search output is bounded to 5,000 Unicode characters. This is a character budget, not an exact tokenizer guarantee. Reduce the limit or budget for smaller tasks. Request up to eight records only when the design question benefits.
- Keep attribution and evidence in `data/screen-provenance.json` and `data/flow-provenance.json`. Read it for an explicit provenance audit, source refresh, evidence dispute or to resolve existing-example links for Recommended directions. Verify only that shortlist during planning; ordinary implementation stays offline.
- Do not reopen reference screenshots merely because a record is selected. The preparation work has already extracted the layout facts. Exact reproduction, a newly supplied unprocessed reference or an explicit request for current live behavior is a separate task.
- A missing category is a coverage gap. Broaden the local query, use the original pattern atlas as explicitly authored guidance, or explain the gap. Do not silently launch a web/image research campaign or invent an observed screen.

```sh
python3 scripts/design_library.py stats
python3 scripts/design_library.py concepts "workflow canvas inspector" --platform web
python3 scripts/design_library.py brief "pricing failed payment" --platform web
python3 scripts/design_library.py flows "settings search" --platform desktop
python3 scripts/design_library.py decisions "sharing permissions"
python3 scripts/design_library.py search "calendar event editing" --platform mobile
python3 scripts/design_library.py search "search filters results" --limit 3 --budget-chars 4500
python3 scripts/design_library.py search "workspace project overview" --platform web
python3 scripts/design_library.py get M003 M031 --budget-chars 6000
python3 scripts/design_library.py guidance pricing payment
python3 scripts/design_library.py provenance M003
```

Resolve the real installed path. Python's standard library is sufficient; no server, API key, MCP, embedding service or paid source is required. When Python is unavailable, use local text search to select IDs and read just those JSON objects. Do not replace the local lookup with browsing.

## Turn evidence into project decisions

1. Infer the user's task, platform, primary object, relevant state and information density from project context. Search by these needs, not a fashionable brand name alone.
2. Read the returned screen anatomy, any optional synthesis lesson, and the associated implementation guidance. Prefer examples that solve the same information or interaction problem. A mobile banking summary does not establish SaaS pricing-table design.
3. Record a short comparison: **screen ID | useful decision | mismatch | target adaptation**. Select one coherent structural lead and a few complementary details.
4. Translate observations into target decisions for content order, navigation, focal hierarchy, grouping, geometry, typography roles, spacing relationships and component states. Define actual target tokens from the target brand and platform; do not infer source fonts or copy source colors.
5. Apply the linked implementation recipe. Its responsive, accessibility, motion and state advice is original guidance, not evidence that the source application implements those behaviors. Verify actual component APIs with technical documentation when needed; that is separate from reference research.
6. Build the default three complete concepts, render them, inspect their actual output and compare them against the compiled design decisions. Offline reference retrieval does not remove the need to test the UI being produced.

Search returns relevance-ranked records and unmatched query terms. Purpose terms such as authentication, permissions, pricing, onboarding and errors require explicit matching tags; a credential detail does not become a login form because it contains the word “login.” If no exact precedent exists, `guidance` lists or returns up to three original recipes without claiming shipped-screen evidence.

For a multi-screen flow, retrieve by each necessary stage, then write a compact transition table: **entry condition | user action | next state | failure/recovery | evidence or proposed rule**. A set of screenshots is not a recorded flow. Preserve the distinction between an observed screen, a documented transition and an original proposed transition. Do not infer validation timing or navigation from App Store screenshot order.

For small decisions, retrieve a narrow working set: editing a date, revealing a row action, grouping settings, placing an attachment, presenting a selected result or handling an empty collection. Do not redesign an entire product from one attractive screen.

## Evidence boundaries

Each counted record has a unique source image hash, a named product/state and a reviewed layout description. Do not count promotional artwork, brand-only frames, unreviewed previews, hypothetical states, concept art, recipes or source links toward the shipped-product screen total. Publisher screenshots may include device framing or promotional surroundings; observations describe only the visible interface. They are publisher evidence of a released product, not independent session recordings.

The collection supports useful original adaptation, not pixel-perfect reconstruction. Static images do not establish timing, gestures, validation rules, accessibility compliance, conversion uplift or optimality. Do not invent such facts. Describe unknown behavior as a target design decision and test it. A photographed, angled or partly cropped screen can support hierarchy observations without supporting exact geometry.

Keep the coaching inside this skill; do not create a separate training dataset or fine-tuning workflow unless the user explicitly requests it. Keep `layout` as observation, `lesson` as synthesis and `implementation_rules` as proposed target guidance. Source UI may be historical; the capture date and exact app version are unknown unless evidence establishes them. The inspection date is not a release date. This package does not retrain model weights or refresh itself weekly.

## Supporting material

The visual gallery is for browsing and comparing examples. Use [Concept collection](concept-collection.md) and the `concepts` command for compact, pre-extracted art direction. The default `brief` adds up to two relevant studies in a separately labeled field. Use `reference_library.py stats` for current gallery counts. The 200-card pattern atlas supplies original design guidance. Concept and atlas counts are separate from shipped-screen counts.

When explicitly updating the collection, inspect new source material once, record screen-specific observations and provenance, reject duplicates and unsupported claims, then run `design_library.py validate`. Future projects consume the compiled descriptions; they should not repeat ingestion.
