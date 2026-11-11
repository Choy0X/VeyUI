# AGENTS.md

This repository publishes **veyUI**, a design-led UI/UX skill for AI coding agents (Agent Skills format, MIT).

## Using the skill

If the user asks you to design, redesign, polish or audit a UI, read `skills/veyui/SKILL.md` and follow it. Resolve every relative path from that file. Load only the modules it points to. The skill's workflow is: discover the product, propose references, build three hosted concepts, let the user choose, implement, then verify in a real renderer.

Install it for the user with one of:

```sh
npx skills add Choy0X/VeyUI
python install.py --all        # offline, any platform
```

Agents without native skill support can be pointed at `skills/veyui/SKILL.md` directly. See `docs/platforms.md`.

## Working on this repository

- The skill lives in `skills/veyui/`. The skill name must stay `veyui` and match its folder name.
- Do not edit `skills/veyui/foundation/`. It is a pinned, hash-verified copy of Taste Skill by Leonxlnx (MIT). Run `python skills/veyui/scripts/verify_foundation.py` after any change nearby. To update the pin, see `docs/how-it-works.md`.
- Do not add private screenshots or third-party images. The 31 concept studies in `skills/veyui/data/reference-library.json` are text only (`asset_withheld: true`).
- Keep `SKILL.md` under 500 lines and its frontmatter `description` under 1024 characters.
- Landing page: `site/`. Docs: `docs/`. Manifests: `.claude-plugin/`, `.cursor-plugin/`, `gemini-extension.json`.

## Checks

Run from `skills/veyui/`:

```sh
python -I tests/test_concept_references.py
python -I tests/test_design_library.py
python -I tests/test_reference_library.py
node tests/reference_gallery_dom_regression.cjs .
python -I scripts/verify_foundation.py
```

Requirements: Python 3.10+, Node 22+. Browser checks need Chrome, Edge or Chromium.

## Credits

The web construction engine is Taste Skill by Leonxlnx (https://github.com/Leonxlnx/taste-skill). See `THIRD-PARTY-NOTICES.md`. veyUI is independent and not endorsed by that author.
