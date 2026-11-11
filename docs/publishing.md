# Publishing notes (maintainers)

## skills.sh

skills.sh has no submission form. A skill appears automatically when people install it with the `skills` CLI, and it ranks by install count. Once indexed it appears under skills.sh/Choy0X/VeyUI. Until it shows up there, do not link or badge it. To be discoverable:

- Keep `skills/veyui/SKILL.md` valid: lowercase `name` equal to the folder, `description` of 1 to 1024 characters.
- Keep the repository public.
- Share `npx skills add Choy0X/VeyUI` in the README, release notes and the website.

## GitHub Pages

The landing page in `site/` deploys through `.github/workflows/pages.yml`. In the repository settings, set Pages source to GitHub Actions. URL: https://choy0x.github.io/VeyUI/.

After the first deploy, submit `https://choy0x.github.io/VeyUI/sitemap.xml` in Google Search Console and Bing Webmaster Tools. A `robots.txt` inside a project Pages site is not read by crawlers (only the one at the domain root is), so the sitemap submission is what counts.

## Distribution status (as of 2026-11-11)

| Channel | What was done | Status |
|---|---|---|
| skills.sh | One real `npx skills add Choy0X/VeyUI` install on 2026-11-11 (telemetry on). There is no submission form. | Not listed yet. Check https://skills.sh/Choy0X/VeyUI again; add the link and badge to README, the site and `llms.txt` only after it exists. |
| Anthropic plugin directory | Form at https://claude.ai/directory/manage/new/plugin, repo URL entered. The validation step timed out three times ("the directory service didn't answer in time"). | Blocked on the service. Retry later. |
| Cursor marketplace | https://cursor.com/marketplace/publish needs a signed-in Cursor account. | Waiting for a Cursor sign-in. Reviews take weeks; do not resubmit, it creates duplicates. |
| Gemini CLI extensions gallery | Public repo, `gemini-extension.json` and the `gemini-cli-extension` topic are in place. | Indexed automatically; check https://geminicli.com/extensions in a few days. |
| BehiSecc/awesome-claude-skills | PR https://github.com/BehiSecc/awesome-claude-skills/pull/1286 | Open. |
| kodustech/awesome-agent-skills | PR https://github.com/kodustech/awesome-agent-skills/pull/196 | Open. |

Lists not entered yet, with their stated rules (revisit when the repo qualifies):
- hesreallyhim/awesome-claude-code: at least 14 days of history with active development, or 100 stars; recommendations go through the issue form, not a PR.
- heilcheng/awesome-agent-skills: at least 20 stars and older than 14 days.
- philipbankier/awesome-agent-skills: at least 10 stars.
- VoltAgent/awesome-agent-skills: needs real community usage, brand new skills are not accepted.
- ComposioHQ/awesome-claude-skills and the Codex skills list: they host skill folders, not links, so a copy of this skill would be needed; not a good fit for a skill this size.

## Repository metadata

- Description and website URL: set in the repository header.
- Topics: agent-skills, claude-code, codex, cursor, gemini-cli, github-copilot, ai-agents, skills-sh, ui-design, ux-design, design-system, landing-page, frontend.
- Social preview: upload `site/assets/social-preview.png` (1280x640) under Settings > General > Social preview. GitHub has no API for this step.

## Landing page maintenance

- Static checks: `python tools/check_site.py` (also run by the Validate workflow).
- Preview images are generated, not hand-edited: `PUPPETEER_CORE=<path to puppeteer-core> node tools/previews/generate.cjs`. Edit `tools/previews/previews.html` to change them, then re-upload the social preview.
- The logo source is `site/assets/logo.svg`. After changing it, run `PUPPETEER_CORE=<path to puppeteer-core> node tools/brand/generate-icons.cjs`, then regenerate the previews.
- The page loads only local files. Keep it that way: no CDN scripts, fonts or analytics.

## Releasing

1. Update `CHANGELOG.md` and versions in `skills/veyui/SKILL.md` (metadata), `.claude-plugin/*.json`, `.cursor-plugin/plugin.json`, `gemini-extension.json`.
2. Run the checks in `CONTRIBUTING.md`.
3. Tag and publish: `git tag v1.x.y && git push --tags && gh release create v1.x.y`.
