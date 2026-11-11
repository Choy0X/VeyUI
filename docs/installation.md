# Installation

veyUI is one folder, `skills/veyui/`, in the open [Agent Skills](https://agentskills.io/specification) format. Pick the route that fits your setup.

## 1. The `skills` CLI (recommended)

Needs Node.js.

```sh
npx skills add Choy0X/VeyUI
```

The CLI detects the coding agents on your machine and installs veyUI into each one's skills folder. Useful options:

```sh
npx skills add Choy0X/VeyUI --list               # show what it found, install nothing
npx skills add Choy0X/VeyUI -a claude-code       # one agent
npx skills add Choy0X/VeyUI -a claude-code -a codex
npx skills add Choy0X/VeyUI -g                   # user-level instead of this project
```

Agent ids are listed in [platforms.md](platforms.md). The CLI sends anonymous install telemetry, which is how skills.sh builds its listing. Set `DISABLE_TELEMETRY=1` to turn it off.

## 2. Claude Code plugin

```text
/plugin marketplace add Choy0X/VeyUI
/plugin install veyui@veyui
```

## 3. Gemini CLI extension

```sh
gemini extensions install https://github.com/Choy0X/VeyUI
```

## 4. Offline installer (Python 3.10+, no dependencies)

```sh
git clone https://github.com/Choy0X/VeyUI.git
cd VeyUI
python install.py              # universal folder plus every agent it detects
python install.py --all        # every supported agent location
python install.py --agent claude-code --agent cursor
python install.py --project    # into this project's skills folders
python install.py --skills-dir ~/some/skills
python install.py --dry-run --all
python install.py --list
```

Windows: `py -3 install.py` or `.\install.ps1`. macOS and Linux: `./install.sh`.

The installer stages a clean copy, moves any existing `veyui` folder aside, places the new one and removes the old one. If placing the new copy fails it restores the original.

## 5. Manual

Copy `skills/veyui/` into your agent's skills directory so the result is `<skills-dir>/veyui/SKILL.md`. Directories are in [platforms.md](platforms.md). For an agent with no skill support, give it the path to `skills/veyui/SKILL.md` and ask it to follow that file.

## Verify the install

Start a **new** agent session in a project and ask:

> Use veyUI to design a pricing section for this app.

The agent should read `veyui/SKILL.md` and start with discovery. In Claude Code you can also type `/veyui`; in Codex use `$veyui`.

## Requirements

- Python 3.10+ for the offline library and concept scaffolding.
- Node 22+ and Chrome, Edge or Chromium for the bundled web checks (screenshots, consistency and layout checks).
- A way to run and preview your project.

Use WSL or a remote terminal? Install inside the environment where your agent runs.

## Update and uninstall

Update: re-run the install command. The CLI and `install.py` both replace the old copy. Uninstall: delete the `veyui` folder from the skills directory (or run `npx skills remove veyui`).
