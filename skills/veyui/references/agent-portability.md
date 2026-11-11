# Run the same skill across agent hosts

Use this directory as one Agent Skills package. Resolve every resource path from the loaded `SKILL.md` directory. Resolve project files from the project root. Do not assume the shell starts inside the skill directory or that a ChatGPT-specific capability exists.

## Install and discovery

Install with the `skills` CLI and name the target agent:

```sh
npx skills add Choy0X/VeyUI -a <agent>
```

| Agent (`-a` value) | Project skills directory | How to invoke |
|---|---|---|
| `claude-code` | `.claude/skills/` | Use `/veyui` or ask for veyUI by name |
| `codex` | `.agents/skills/` | Use `$veyui` or ask for veyUI by name |
| `cursor` | `.agents/skills/` | Ask for veyUI by name or load the skill |
| `gemini-cli` | `.agents/skills/` | Ask for veyUI by name or load the skill |
| `github-copilot` | `.agents/skills/` | Ask for veyUI by name or load the skill |
| `windsurf` | `.windsurf/skills/` | Ask for veyUI by name or load the skill |
| `kiro-cli` | `.kiro/skills/` | Ask for veyUI by name or load the skill |
| `roo` | `.roo/skills/` | Ask for veyUI by name or load the skill |
| `goose` | `.goose/skills/` | Ask for veyUI by name or load the skill |
| `cline`, `opencode`, `amp`, `trae`, `antigravity`, `continue`, `junie`, `qwen-code`, `openhands`, `augment` and others | The directory the `skills` CLI reports for that agent | Ask the agent to load the `veyui` skill |

The universal project path is `.agents/skills/`. Global (user-level) per-agent paths are listed in docs/platforms.md in the repository. Use the host's documented overrides where configured. Keep one version of veyUI in each discovery scope; a host-specific or project copy can take precedence over a global one, and some hosts also read other agents' skill directories. `agents/openai.yaml` adds optional display metadata. The instructions and local resources are shared.

## Agents without skill support

If a client has no skill discovery, give the agent the complete skill folder and ask it to read `skills/veyui/SKILL.md` (or `AGENTS.md` at the repository root, where present), then open the relevant bundled references from there. Resolve all relative links from the directory that holds `SKILL.md`.

## Capabilities, not product names

- Select the installed Python 3.10+ launcher. On Windows try `py -3` or `python`. On macOS and Linux try `python3`. Use quoted paths and the active shell's syntax. Offline retrieval uses UTF-8 files and the standard library. If Python is missing, search the bundled JSON and read the matching records directly.
- Use a supported browser, native preview or emulator to render and operate the candidate. Use the host's available visual inspection tools. If it cannot see pixels, record which aesthetic checks remain blocked.
- Use the available hosting or preview route and verify that the user can open it. Local preview is useful during construction. A loopback URL on the agent's machine is not automatically reachable from the user's device. Follow the delivery contract and report the actual availability.
- Use delegated review only when the host supports it and authorization allows it. Otherwise review visual craft and task behavior as separate passes.
- Resolve project runtime, animation APIs and external assets separately. No host extension, MCP server or image generator is a prerequisite for reading the design workflow. Request image generation permission as specified in the main instructions.

Official discovery documentation for some hosts: [Codex](https://developers.openai.com/codex/skills), [Claude Code](https://code.claude.com/docs/en/skills), [OpenCode](https://opencode.ai/docs/skills). Other hosts document their own skills locations.
