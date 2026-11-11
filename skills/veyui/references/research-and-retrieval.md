# Research and the local design atlas

**Default policy:** Use [pre-extracted offline screen knowledge](offline-design-library.md) during ordinary design work. A bounded live-link shortlist during Recommended directions is an additional planning route. The broader source-inspection instructions below apply to explicit new-reference ingestion, refresh or image-matching tasks. Do not reopen already compiled sources or load their images by default.
## What the atlas contains

Use the atlas as a searchable design playbook and source index. It contains 200 original text pattern cards across 20 categories, 52 external source records, and qualitative observations from eight user-supplied concept images. It contains no copied Mobbin collection, third-party screenshot corpus, learned model weights, embeddings, or model training. External source records distinguish text access from visual inspection and unavailable pages. The cards' related sources are further-study leads, not claims that those products implement those patterns.

Never describe authored cards as hundreds of observed screens. Never infer a current visual design from a product name or text-only page extraction. A model's familiarity with a famous product is not current visual evidence.

The separate [App and site reference library](reference-library.md) contains image records, text-only concept studies and source links. Search it for actual material before using the pattern cards to interpret the task. Report its counts separately. An App Store promotional frame, an official documentation screenshot, a concept and a live tested flow are different evidence types.

## Retrieve a small relevant working set

Use Python 3 and the bundled standard-library script. Resolve the skill directory from its actual installation. Commands are shown relative to that directory; do not assume it is the project working directory.

```sh
python3 scripts/design_atlas.py search "mobile onboarding permissions" --platform mobile --limit 6
python3 scripts/design_atlas.py search "editorial product hero" --platform web --limit 6
python3 scripts/design_atlas.py search "resizable inspector keyboard" --platform desktop --limit 6
python3 scripts/design_atlas.py show P001 P003 --format json
python3 scripts/design_atlas.py sources --ids lapa curated apple-hig
python3 scripts/design_atlas.py benchmarks
python3 scripts/design_atlas.py stats
```

Without Python, read the matching JSON records using available file tools. Do not load all 200 cards into every task. Search separately for the main job, visual composition and high-risk interaction. Review roughly 4–8 relevant cards, discard mismatches and record why the selected patterns fit. Ranking measures lexical relevance, not design quality. No embeddings, server, account, API key or network are required for local retrieval.

## Research live visual precedents

For a substantial design, use this balanced working set unless a supplied approved design already settles it.

1. Inspect the user's supplied references first. Follow [Concept extraction](concept-extraction.md) for composition, type, spacing, functional emphasis, surface hierarchy, asset and observed motion principles without exporting the source palette. Use saved benchmark notes only as qualitative reminders when original images are unavailable; their historical color descriptions are not adoption instructions.
2. Inspect a few relevant live or publicly visible product examples for the task and platform. Prefer actual screens, public demos, official product tours and official help documentation over a marketing homepage when researching an application flow.
3. Inspect a few concept references for art direction. Lapa Ninja, Curated, Awwwards and Dribbble offer discovery routes. Their accessible pages are leads; public preview does not imply a free source license. Do not depend on advanced filters, paid collections, paid MCPs or accounts.
4. Consult the relevant platform system and component documentation. Separate verified interaction requirements from aesthetic hypotheses.
5. Stop collecting when you can explain the useful contrasts and make a concrete proposal. Research hundreds of references over the life of the atlas, not hundreds per button or task. If the brief requires broader exploration, expand purposefully by missing category rather than quantity alone.

Record each selected precedent as **exact source | access date | surface/state | observed visual or interaction fact | evidence type/capture | transferable principle | what not to copy**. Label text-only access, historical references, inaccessible pages and untested behavior explicitly. Search snippets establish discovery, not pixel observations.

Create an original composition from principles. Use one primary visual reference and a few complementary references for typography, interactions or assets. Do not collage unrelated branded components. Preserve product facts and native expectations. Gallery recognition or awards do not establish usability, accessibility, conversion performance or suitability.

## Free operation and source access

The bundled atlas and Python helpers are local and require no paid service. The user's coding agent, model inference, image generation, hosting or optional third-party services may have their own costs. Do not describe those as free merely because this package is free to use.

Mobbin is a comparison reference only. Do not call its MCP, require its API, scrape its restricted catalog, or reproduce its private screens. If a discovery source is blocked or paid, record that and use accessible public examples or original design work. Do not bypass access controls. No vendor account or purchase is necessary for the core workflow.

All nine requested component sources remain in Component catalog. In free mode, adopt only exact items with accessible source and suitable free usage rights. Treat beUI Pro and other premium items as visual study leads unless the user already has authorized access. Never assume a free homepage means free components. Do not install paid dependencies or consume paid services without the user's authorization.

## Grow a project-owned reference library

Keep project research under the project's chosen design-document location, outside the installed skill. Use `templates/reference-record.json` as a starting record. Add only sources actually inspected. Record screenshots only when permitted and useful, with source, date, platform and state. Do not publish or redistribute captured third-party imagery by default. Prefer links plus original observations in a shareable archive.

Separate these evidence levels: **discovery lead**, **text inspected**, **image inspected**, **interaction observed**, **implemented and tested in this project**. Promotion requires new evidence. Keep rejected references and the short rejection reason when they prevent repeated bad choices. Updating a reference file changes retrieval context; it does not train the model.
