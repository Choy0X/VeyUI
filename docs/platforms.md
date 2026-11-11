# Supported platforms

veyUI is a standard Agent Skill, so it runs anywhere the format is supported. The `skills` CLI knows each agent's folder, so `npx skills add Choy0X/VeyUI -a <id>` is the simplest route. This table lists the folders it uses.

`.agents/skills/` is the shared, universal project folder. Codex, Cursor, Gemini CLI, GitHub Copilot, Cline, OpenCode, Amp and others read it.

| Agent | `-a` id | Project folder | User folder |
|---|---|---|---|
| Claude Code | `claude-code` | `.claude/skills/` | `~/.claude/skills/` |
| Codex | `codex` | `.agents/skills/` | `~/.agents/skills/` |
| Cursor | `cursor` | `.agents/skills/` | `~/.cursor/skills/` |
| Gemini CLI | `gemini-cli` | `.agents/skills/` | `~/.gemini/skills/` |
| GitHub Copilot | `github-copilot` | `.agents/skills/` | `~/.copilot/skills/` |
| Windsurf | `windsurf` | `.windsurf/skills/` | `~/.codeium/windsurf/skills/` |
| Cline | `cline` | `.agents/skills/` | `~/.agents/skills/` |
| OpenCode | `opencode` | `.agents/skills/` | `~/.config/opencode/skills/` |
| Amp | `amp` | `.agents/skills/` | `~/.config/agents/skills/` |
| Antigravity | `antigravity` | `.agents/skills/` | `~/.gemini/config/skills/` |
| Kiro CLI | `kiro-cli` | `.kiro/skills/` | `~/.kiro/skills/` |
| Roo Code | `roo` | `.roo/skills/` | `~/.roo/skills/` |
| Goose | `goose` | `.goose/skills/` | `~/.config/goose/skills/` |
| Trae | `trae` | `.trae/skills/` | `~/.trae/skills/` |
| Kilo Code | `kilo` | `.agents/skills/` | `~/.kilo/skills/` |
| Droid | `droid` | `.agents/skills/` | `~/.factory/skills/` |
| Continue | `continue` | `.continue/skills/` | `~/.continue/skills/` |
| Junie | `junie` | `.junie/skills/` | `~/.junie/skills/` |
| Qwen Code | `qwen-code` | `.qwen/skills/` | `~/.qwen/skills/` |
| OpenHands | `openhands` | `.openhands/skills/` | `~/.openhands/skills/` |
| Augment | `augment` | `.augment/skills/` | `~/.augment/skills/` |
| Mistral Vibe | `mistral-vibe` | `.vibe/skills/` | `~/.vibe/skills/` |
| Zed, Warp | `zed`, `warp` | `.agents/skills/` | `~/.agents/skills/` |

The `skills` CLI supports many more agents. Run `npx skills add Choy0X/VeyUI --list` or see the [CLI docs](https://github.com/vercel-labs/skills). Folders can change between agent releases, so treat this table as a snapshot and prefer the CLI. `python install.py --list` prints the same table.

## Native packaging

| Ecosystem | File in this repo | How users install |
|---|---|---|
| Claude Code plugin | `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json` | `/plugin marketplace add Choy0X/VeyUI` |
| Gemini CLI extension | `gemini-extension.json`, `GEMINI.md` | `gemini extensions install https://github.com/Choy0X/VeyUI` |
| Cursor plugin | `.cursor-plugin/plugin.json` | `npx skills add Choy0X/VeyUI -a cursor` |
| GitHub Copilot | `.github/copilot-instructions.md` | `npx skills add Choy0X/VeyUI -a github-copilot` |
| AGENTS.md readers (Codex, Cursor, Copilot, Windsurf, Amp, Zed, Warp, Roo, Kilo, Junie, Augment, Aider, Goose, OpenCode and more) | `AGENTS.md` | Open the repository, or install the skill |

## Agents without skill support

Tell the agent: "Read `skills/veyui/SKILL.md` and follow it. Resolve relative paths from that file." This works in any agent that can read files. It can run the Python helpers and the web checks if it can execute commands.

## Capability notes

- **Invocation.** Claude Code: `/veyui`. Codex: `$veyui`. Elsewhere, ask in plain language and the skill's description triggers it.
- **Rendering and hosting.** Concept building needs a way to serve files and render them. veyUI uses what your agent has and says plainly when a route is missing.
- **Independent review.** Where the agent supports subagents the skill uses them for critique. Where it does not, it runs the same review as separate passes.
- **Tested on.** Windows 11 with Python 3.13 and Node 25. The folder layout follows the shared Agent Skills format. Other agents and operating systems have not each been exercised end to end. Please open an issue if one misbehaves.
