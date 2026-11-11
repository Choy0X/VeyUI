# Contributing references

The catalog at `skills/veyui/data/reference-library.json` stores study notes, not copies of other people's work.

## Rules

- **Link, do not copy.** Reference public pages or publisher previews by URL (HTTPS only). Do not add screenshots you do not have the right to redistribute.
- **Write original observations.** Describe composition, hierarchy and task flow in your own words. Exclude the source palette.
- **Record evidence honestly.** Use `image_inspected`, `image_overview_inspected`, `text_inspected`, `discovery_lead` or `unreviewed`. A `shipped_screen` record needs `image_inspected`.
- **Record rights.** Fill the `rights` field. If you inspected an image that cannot be redistributed, set `asset_withheld: true` and omit `asset`.
- **No scraping of restricted catalogs.** Do not reproduce paid or private libraries.

## Record fields

Required: `id` (letter plus 3 to 6 digits, unique), `title`, `kind`, `platforms` (`web`, `mobile`, `desktop`), `patterns`, `evidence`, `source`, `observations`, `adaptation`, `limitations`, `rights`, `checked_on` (ISO date). Optional: `url`, `image_url`, `category`, `app`, `content_role`, `transfer_check`.

## Validate

```sh
python skills/veyui/scripts/reference_library.py validate
python -I skills/veyui/tests/test_reference_library.py
```

## Private galleries

For images you own, keep a separate catalog and build a local gallery. See `how-it-works.md`.
