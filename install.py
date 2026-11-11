#!/usr/bin/env python3
"""Install the veyUI skill for AI coding agents (offline, no dependencies).

Examples:
  python install.py                     # universal path plus every detected agent
  python install.py --agent claude-code --agent codex
  python install.py --all               # every supported agent location
  python install.py --project           # install into ./<agent skills dir> for this project
  python install.py --skills-dir ~/my-agent/skills
  python install.py --list

Prefer `npx skills add Choy0X/VeyUI` when Node is available. This script covers offline use.
"""
import argparse
import shutil
import sys
import tempfile
from pathlib import Path

SKILL_NAME = 'veyui'
REQUIRED = ['SKILL.md', 'assets/icon.svg', 'data/reference-library.json', 'scripts/design_library.py']

HOME = Path.home()

# agent id -> (project-relative skills dir, global skills dir)
AGENTS = {
    'universal':      ('.agents/skills',   HOME / '.agents/skills'),
    'claude-code':    ('.claude/skills',   HOME / '.claude/skills'),
    'codex':          ('.agents/skills',   HOME / '.agents/skills'),
    'cursor':         ('.agents/skills',   HOME / '.cursor/skills'),
    'gemini-cli':     ('.agents/skills',   HOME / '.gemini/skills'),
    'github-copilot': ('.agents/skills',   HOME / '.copilot/skills'),
    'windsurf':       ('.windsurf/skills', HOME / '.codeium/windsurf/skills'),
    'cline':          ('.agents/skills',   HOME / '.agents/skills'),
    'opencode':       ('.agents/skills',   HOME / '.config/opencode/skills'),
    'amp':            ('.agents/skills',   HOME / '.config/agents/skills'),
    'antigravity':    ('.agents/skills',   HOME / '.gemini/config/skills'),
    'kiro-cli':       ('.kiro/skills',     HOME / '.kiro/skills'),
    'roo':            ('.roo/skills',      HOME / '.roo/skills'),
    'goose':          ('.goose/skills',    HOME / '.config/goose/skills'),
    'trae':           ('.trae/skills',     HOME / '.trae/skills'),
    'kilo':           ('.agents/skills',   HOME / '.kilo/skills'),
    'droid':          ('.agents/skills',   HOME / '.factory/skills'),
    'continue':       ('.continue/skills', HOME / '.continue/skills'),
    'junie':          ('.junie/skills',    HOME / '.junie/skills'),
    'qwen-code':      ('.qwen/skills',     HOME / '.qwen/skills'),
    'openhands':      ('.openhands/skills', HOME / '.openhands/skills'),
    'augment':        ('.augment/skills',  HOME / '.augment/skills'),
    'mistral-vibe':   ('.vibe/skills',     HOME / '.vibe/skills'),
    'zed':            ('.agents/skills',   HOME / '.agents/skills'),
    'warp':           ('.agents/skills',   HOME / '.agents/skills'),
}
# These share the universal directory, so their presence cannot be detected from the folder alone.
SHARED_GLOBAL = {HOME / '.agents/skills', HOME / '.config/agents/skills'}


def install(source: Path, skills_dir: Path) -> Path:
    """Copy `source` to <skills_dir>/veyui, replacing any previous copy and restoring it on failure."""
    target = skills_dir / SKILL_NAME
    if target == source:
        return target
    if skills_dir.is_relative_to(source) or source.is_relative_to(target):
        raise OSError('The source folder and the installation folder must be separate.')
    skills_dir.mkdir(parents=True, exist_ok=True)

    temporary = Path(tempfile.mkdtemp(prefix='.veyui-stage-', dir=skills_dir))
    staged = temporary / 'incoming'
    previous = temporary / 'previous'
    installed = False
    try:
        shutil.copytree(source, staged, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
        if target.exists() or target.is_symlink():
            target.rename(previous)
        try:
            staged.rename(target)
        except OSError:
            if previous.exists() or previous.is_symlink():
                try:
                    previous.rename(target)
                except OSError as error:
                    raise OSError(f'Could not restore the previous installation from {previous}') from error
            raise
        installed = True
    finally:
        if installed or not (previous.exists() or previous.is_symlink()):
            shutil.rmtree(temporary, ignore_errors=True)
    return target


def detected_agents() -> list:
    found = []
    for agent, (_, global_dir) in AGENTS.items():
        if agent == 'universal' or global_dir in SHARED_GLOBAL:
            continue
        if global_dir.parent.exists():
            found.append(agent)
    return found


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--agent', action='append', choices=sorted(AGENTS), metavar='AGENT',
                        help='Install for this agent. Repeat for several. See --list.')
    parser.add_argument('--all', action='store_true', help='Install into every supported agent location.')
    parser.add_argument('--project', action='store_true',
                        help='Install into the current project (./.claude/skills, ./.agents/skills, ...) instead of your home directory.')
    parser.add_argument('--skills-dir', type=Path, action='append',
                        help='Install into this custom skills directory. Repeat for several.')
    parser.add_argument('--list', action='store_true', help='Show supported agents and their skills directories, then exit.')
    parser.add_argument('--dry-run', action='store_true', help='Show where the skill would be installed without writing anything.')
    args = parser.parse_args()

    if args.list:
        print(f'{"agent":<16} {"project path":<20} global path')
        for agent, (project, global_dir) in AGENTS.items():
            print(f'{agent:<16} {project:<20} {global_dir}')
        return

    source = Path(__file__).resolve().parent / 'skills' / SKILL_NAME
    if any(not (source / path).is_file() for path in REQUIRED):
        parser.error('Run this file from a complete clone of the repository (skills/veyui/ must sit beside it).')

    if args.skills_dir:
        directories = list(args.skills_dir)
    else:
        if args.all:
            agents = list(AGENTS)
        elif args.agent:
            agents = args.agent
        else:
            agents = ['universal', 'claude-code'] + [a for a in detected_agents() if a != 'claude-code']
        if args.project:
            directories = [Path.cwd() / AGENTS[a][0] for a in agents]
        else:
            directories = [AGENTS[a][1] for a in agents]

    status = 0
    for directory in dict.fromkeys(p.expanduser().resolve() for p in directories):
        if args.dry_run:
            print(f'Would install {directory / SKILL_NAME}')
            continue
        try:
            target = install(source, directory)
        except OSError as exc:
            print(f'Could not install into {directory}: {exc}', file=sys.stderr)
            status = 1
            continue
        print(f'Installed {target / "SKILL.md"}')
    if status == 0 and not args.dry_run:
        print('Start a new agent session and say: "Use veyUI to design this interface."')
    sys.exit(status)


if __name__ == '__main__':
    main()
