# Searchable app and site reference library

**Default policy:** Use [pre-extracted offline screen knowledge](offline-design-library.md) during ordinary design work. The source-inspection instructions below apply only to explicit new-reference ingestion, refresh or image-matching tasks. Do not reopen already compiled sources or load their images by default.
Use `data/reference-library.json` and `scripts/reference_library.py` alongside the original pattern atlas. This collection stores actual image locators, source identity, evidence level, platform, study tags and adaptation notes. It is a local reference index, not model training or a replacement for inspecting the chosen source. Read live counts with `stats`; never combine patterns, source links and images into a claimed shipped-screen count.

## Retrieve before designing

1. Identify the target platform, task, state and composition problem from project context. Search those terms first, then broaden by product category. Use a familiar brand as a secondary cue, not as proof of fit.
2. Prefer inspected relevant evidence. Distinguish the record types below. Open selected images at readable size; check the current live interface where behavior matters. A search result alone cannot approve a direction.
3. Select a coherent lead reference and compatible supporting details. Write the palette-free inspiration brief and source-to-target translation. Do not inherit a source palette or reproduce a whole branded screen.
4. Save a project shortlist with source IDs, actual inspection evidence and rejected mismatches. Use it during the three-concept comparison and final review.

```sh
python3 scripts/reference_library.py stats
python3 scripts/reference_library.py search "calendar" --platform mobile --limit 8
python3 scripts/reference_library.py search "metadata" --kind shipped_screen
python3 scripts/reference_library.py search "fintech" --kind concept
python3 scripts/reference_library.py search "Todoist" --kind app_store_preview
python3 scripts/reference_library.py show R007 S009
python3 scripts/reference_library.py shortlist R007 S009 --output /new/project/shortlist.json
python3 scripts/reference_library.py gallery --output /new/path/reference-library.html
python3 scripts/reference_library.py review-due --days 90
```

Resolve the installed script path. The helpers use Python's standard library. Exports refuse to overwrite existing files. Search is lexical and tag-based, not visual similarity or an embedding model. Observed pattern and interface notes rank above app-name-only matches, with evidence level contributing to order. JSON is the fallback when Python is unavailable.

The collection has 384 records: 291 publisher previews across 50 apps, 18 official documentation screenshots, 31 concept studies, 24 documentation study sources and 20 website study leads. Of the publisher previews, 99 were examined as reduced overviews; 192 remain unreviewed. Counts describe coverage, not quality scores. Use runtime statistics after updates. This is a mobile-heavy seed collection; website leads do not supply full-page screenshots, and native Android evidence still needs targeted collection.

The November collection adds 18 inspected concept studies from 20 source images (the 31 concept studies in total also include the 12 earlier concepts and the seven-pass craft study R031). Use the [concept map](concept-collection.md) or search by a visible pattern such as "workflow canvas", "process table", or "plan comparison". The compact design-library brief also retrieves these annotations for matching tasks.

Search understands app names and source-level categories as well as observed patterns. Category metadata does not establish the specific task shown in an unreviewed frame. `content_role=promotional_art` explicitly excludes that preview as interaction evidence. Publisher images may contain historical interfaces, mixed platforms or very small UI crops; do not derive target geometry from distorted device mockups. An impressive brand is not a universal recommendation.

## Evidence and record types

| Type | Meaning and use |
|---|---|
| `concept` | Maintainer-supplied art direction, published as a text-only study (image withheld); shipped status, accessibility and behavior are not established. |
| `shipped_screen` | An inspected screenshot published in official product documentation; not proof of current version, live interaction or usability. |
| `app_store_preview` | Publisher-provided App Store preview. It may combine UI, device framing, captions and promotional art; never count it as a raw shipped screen. |
| `site_reference` | A website/reference-page lead for later live or image inspection. A listing is not a captured page. |
| `documented_flow` | A task or behavior study source. Documentation does not constitute an observed end-to-end flow recording. |

`image_inspected` means the recorded visual observations were checked. `image_overview_inspected` means only a reduced overview was examined; re-open details before extracting geometry, copy or component rules. `text_inspected` establishes only text facts. `discovery_lead` and `unreviewed` must not be promoted automatically when downloaded or displayed. Publisher captions are marketing claims, not independent evidence. Preserve capture/preview ordering as publisher order, never an invented user-flow sequence.

## Browse and compare

The generated HTML works locally without an account. It provides search, platform/type/evidence/pattern filters, side-by-side shortlists and JSON export. Images from a catalog's own local assets are embedded; external images remain links and load only after the user chooses to load them. The bundled catalog ships no local images, so offline access covers metadata and text studies, not pixels. Selection lasts for the current page session; export it to retain it. Exported browser shortlists include original source locators, not embedded image data.

Publisher API image links are thumbnails; open the publisher source page to seek readable detail. Use the bundled-image enlargement control for local images in a private gallery. A blocked or expired image remains unavailable; record the failure and use another source. Do not bypass authentication or scrape restricted collections. The gallery's own colors are browsing chrome, never target-design recommendations.

## Images in the public release

- The 31 concept studies (R001-R031) are text-only. Their images are withheld because redistribution rights are unverified, and each record carries `asset_withheld: true`. `stats` reports `bundled_images: 0` and `withheld_images: 31`.
- Third-party app-store and site images are linked, not copied. They load only when the user chooses to load them.
- To browse images locally, build a private gallery from your own catalog, with records that have `asset` and `sha256`:

```sh
python scripts/reference_library.py --catalog my.json --asset-root my_dir gallery --output out.html
```

## Grow the collection deliberately

Add records to a project-owned copy of the catalog, or update the installed skill only when requested. Use stable IDs, exact source URLs, access dates, app/publisher identity, relevant task tags, image locators, evidence limits and rights notes. Hash local images and merge exact duplicates with their aliases. Separate app-store release metadata from the unknown capture date of each preview. Do not mark all platforms merely because the product supports them; classify the actual captured surface.

For a project-owned catalog, pass `--catalog /project/references.json --asset-root /project` before the subcommand. Local `asset` paths are relative to that root. The gallery template remains supplied by the installed tool. Keep existing asset paths valid when copying records; do not silently relabel missing images as reviewed links.

Before adding a public image, verify source/publisher identity and whether it is UI, promotional art or a concept. Keep third-party pixels linked unless redistribution is authorized. Images supplied for private study do not grant permission to publish them. Inspect selected frames and write specific observations; do not manufacture annotations to reach a numerical target. Reuse a documented flow record rather than inflating counts with hypothetical screens.

For coverage, seek mobile onboarding, permissions, authentication, browsing, search/filter, detail/edit, checkout, messaging, media, settings, loading, empty and recovery states; web application shells, tables, dashboards, collaboration and admin; desktop panes, command search, menus, inspectors and shortcuts; marketing openings, proof, features, pricing and conversion. Treat missing categories as research work, not invented examples.

Run `validate` after changes. Run `review-due` to identify dated records, then re-open relevant sources and record real changes. The date check does not fetch anything or refresh screenshots. There is no scheduled weekly job, paid service, Mobbin MCP or automatic model training. Keep previously reviewed versions when useful and label them historical.
