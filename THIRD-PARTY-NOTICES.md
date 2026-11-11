# Third-party notices

veyUI is released under the MIT License (see `LICENSE`). It bundles and builds on the work below. The MIT license of this repository does not replace the licenses of third-party material.

## Taste Skill by Leonxlnx (the web construction foundation)

veyUI's marketing-site construction engine is a pinned, unmodified copy of Taste Skill by **Leonxlnx**. veyUI would not exist in its current form without that work, and we are grateful to its author.

| | |
|---|---|
| Project | Taste Skill |
| Author | Leonxlnx |
| Repository | https://github.com/Leonxlnx/taste-skill |
| License | MIT, Copyright (c) 2026 Leonxlnx |
| Pinned commit | `f6b76575f949707b4e3c37cd86cb44b0b98643e8` (directory `skills/taste-skill`) |
| Location here | `skills/veyui/foundation/` |
| Integrity | `skills/veyui/data/foundation-manifest.json` (SHA-256 of every file), checked by `skills/veyui/scripts/verify_foundation.py` |

What is bundled: layout recipes, typography and palette tools, effects, scenes, product fragments, copy linting, consistency and layout checks, and screenshot and performance tools.

What veyUI changed: nothing inside `foundation/`. The upstream `SKILL.md` was renamed `foundation/upstream-guide.md` so that only the veyUI skill activates in an agent. The upstream installer, plugin manifests and global hooks are not included. veyUI's adapter rules live in `skills/veyui/references/foundation.md`.

veyUI is an independent project. It is not affiliated with or endorsed by the author of Taste Skill. To update the pin, replace `foundation/` from the upstream commit you choose and regenerate the manifest.

The upstream license text is preserved at `skills/veyui/foundation/LICENSE`:

```
MIT License

Copyright (c) 2026 Leonxlnx

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

### Item-level asset licenses inside the foundation

Some assets inside `foundation/assets/` carry their own licenses, recorded in the upstream credit files. Keep those files intact and follow each item's terms before you ship an asset in a project.

| Credit file | Items | Licenses recorded |
|---|---|---|
| `foundation/assets/layout/img/credits.json` | Photographs from Unsplash and Wikimedia Commons | Unsplash License, CC0, CC BY 2.0, CC BY 4.0, CC BY-SA 4.0 |
| `foundation/assets/scenes/_demo/credits.json` | Scene photographs and stills | Unsplash License, CC BY-SA 3.0, CC BY-SA 4.0 |
| `foundation/assets/moments/_demo/credits.json` | Moment photographs | Unsplash License |
| `foundation/assets/ui/icons/icons-credits.json` | Brand and file-type icons (vscode-icons, gilbarbara/logos, Simple Icons) | MIT, CC0-1.0 |

CC BY and CC BY-SA items require attribution, and CC BY-SA items require share-alike on adaptations. Brand logos and marks remain the property of their owners. Do not present them as your own.

## Landing page (site/)

The landing page in `site/` is original HTML, CSS and JavaScript made for veyUI. It does not use any Taste Skill kit file. It ships these third-party pieces locally and makes no third-party network requests.

| Item | Version | License | Where |
|---|---|---|---|
| GSAP, ScrollTrigger and Flip | 3.15.1 | GSAP Standard "No Charge" License, https://gsap.com/standard-license (free where end users are not charged; not for tools that compete with Webflow) | `site/assets/vendor/`, notice in `site/assets/vendor/LICENSE-gsap.txt` |
| Anybody, Familjen Grotesk, Spline Sans Mono | Latin subsets | SIL Open Font License 1.1 | `site/assets/fonts/`, texts in `site/assets/fonts/LICENSE.txt` |
| Onest, Azeret Mono | Latin subsets | SIL Open Font License 1.1 | `site/assets/fonts/`, texts in `site/assets/fonts/LICENSE.txt` (used by the Slackwater before and after example) |

The before and after example (Slackwater) is a fictional product designed with veyUI for this site. Its name is coined and has not been searched for trademarks, and all of its tide data is sample data. All of its visuals are made in code (HTML, CSS, SVG). It uses no third-party images or logos. The After design was developed from a private reference study and is original work; no reference image is distributed.

## Other sources that informed original guidance

These sources shaped original veyUI text. Their kits, catalogs and proprietary material are not redistributed. See `skills/veyui/references/source-provenance.md` for details.

| Source | Use in veyUI |
|---|---|
| StageShow | Original product-scene guidance |
| transitions.dev | Original motion-selection guidance. Its library license restricts redistribution, so no library code is included |
| pick-ui-library | Original component-selection guidance |
| Vercel Web Interface Guidelines | Original interface-audit checklist, adapted with judgment |
| Mobbin skills | Original job-based reference search method. No Mobbin content, account or API is used |
| Iconly | Visual inspiration for the veyUI app icon (a bold single glyph on a solid rounded tile). The mark is original and copies no Iconly or third-party logo |

## Reference catalog

`skills/veyui/data/reference-library.json` holds original study notes and links to public pages and publisher previews. Third-party images are linked, not copied. A set of 31 concept studies is recorded as text only. Their source images are not distributed, because redistribution rights are unverified. Product names and screenshots referred to in the catalog belong to their respective owners.
