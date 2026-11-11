# Contributing to veyUI

Thanks for helping. Small, focused pull requests are easiest to review.

## Setup

Clone the repository:

```sh
git clone https://github.com/Choy0X/VeyUI.git
```

Then work from the skill folder:

```sh
cd VeyUI/skills/veyui
```

Requirements: Python 3.10+, Node 22+, and Chrome, Edge or Chromium for browser checks.

## Before you open a pull request

```sh
python -I tests/test_concept_references.py
python -I tests/test_design_library.py
python -I tests/test_reference_library.py
node tests/reference_gallery_dom_regression.cjs .
python -I scripts/fetch_foundation.py
python -I scripts/verify_foundation.py
```

## Rules

- Keep the skill name `veyui`. `SKILL.md` stays under 500 lines and its `description` under 1024 characters.
- Do not commit `skills/veyui/foundation/`. It is fetched by `scripts/fetch_foundation.py`, git-ignored, and pinned to a Taste Skill commit by Leonxlnx. See `docs/how-it-works.md` for how to update the pin.
- Do not submit screenshots or images you do not have the right to redistribute. Link public pages instead, and record rights in the catalog entry.
- Write original guidance. Do not paste proprietary kits, catalogs or paid content.
- Claims must be true. If you did not render or test something, say so.

## Adding references

See `docs/contributing-references.md`.
