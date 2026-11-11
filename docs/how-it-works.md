# How it works

## Layout

```
skills/veyui/
  SKILL.md              entry point (frontmatter plus the workflow)
  references/           design modules, loaded only when needed
  templates/            brief, review and evidence templates
  data/                 offline library: screens, patterns, flows, decision guides, catalog
  scripts/              Python tools: retrieval, atlas, concept studio, evidence checks
  foundation/           pinned Taste Skill, fetched on first use (not stored in git)
  agents/openai.yaml    optional Codex display metadata
  assets/               icon and gallery template
  tests/                regression tests
```

The skill uses progressive disclosure. `SKILL.md` stays short and links to modules, so an agent reads only what the current task needs.

## The offline library

Pre-extracted screen descriptions, patterns, flows and decision guides live in `data/`. `scripts/design_library.py` retrieves compact, relevant facts by task and platform. Retrieval needs no network, no account and no embedding service, and it does not train any model.

Records carry evidence levels (for example `image_inspected`, `text_inspected`, `discovery_lead`) and rights notes, so the agent can tell observed facts from leads. Third-party images are linked, not copied. 31 concept studies are text only (`asset_withheld: true`).

To build your own private gallery, add records with an `asset` image and its `sha256` to a catalog and run:

```sh
python skills/veyui/scripts/reference_library.py --catalog my.json --asset-root my_images gallery --output gallery.html
```

## The web foundation and credits

For marketing sites, veyUI drives **Taste Skill by Leonxlnx** (https://github.com/Leonxlnx/taste-skill, MIT) at a pinned commit, unmodified. It is not stored in this repository: `skills/veyui/scripts/fetch_foundation.py` downloads that exact commit once, on first use, into `skills/veyui/foundation/` (about 30 MB, internet needed once). It provides layout recipes, effects, scenes, copy linting, and the screenshot and consistency checks. The upstream `SKILL.md` is kept as `foundation/upstream-guide.md` so that only veyUI activates in an agent. `skills/veyui/references/foundation.md` is the adapter that resolves conflicts between the two.

Every foundation file is hashed in `data/foundation-manifest.json`. The fetch script refuses to keep anything that does not match, and `scripts/verify_foundation.py` re-checks it at any time. The offline library, concept studio and design modules work without it; only the web construction tools need it. veyUI is independent and not endorsed by the Taste Skill author. Full notices: [THIRD-PARTY-NOTICES.md](../THIRD-PARTY-NOTICES.md).

### Updating the pin

1. Pick the upstream commit. Download its archive, take `skills/taste-skill` (renaming `SKILL.md` to `upstream-guide.md`) plus the root `LICENSE` as `foundation/LICENSE`.
2. Regenerate the file hashes in `data/foundation-manifest.json` and update the commit id there, in `THIRD-PARTY-NOTICES.md`, `README.md`, `site/` and `references/source-provenance.md`.
3. Run `python skills/veyui/scripts/fetch_foundation.py --force` and the checks in [CONTRIBUTING.md](../CONTRIBUTING.md).

## The concept studio

`scripts/concept_studio.py` scaffolds three candidate workspaces, builds a review gallery and checks that the declared evidence exists before handoff. `scripts/check_evidence.py` validates evidence receipts. Each candidate keeps its own gate reports so one candidate's pass never stands in for another's.

## No background services

Everything is plain files. The skill reads them when needed. There is nothing to run in the background and no service to keep alive.
