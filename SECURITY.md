# Security policy

## Reporting a vulnerability

Please report security issues privately through GitHub: **Security > Report a vulnerability** on https://github.com/Choy0X/VeyUI. Do not open a public issue for a vulnerability. You can expect an acknowledgement within a few days.

## Scope

veyUI is a set of instructions, data and local helper scripts that an AI agent reads and runs on your machine.

- The Python scripts under `skills/veyui/scripts/` and the Node tools under `skills/veyui/foundation/scripts/` run locally and make no network calls on their own.
- The installer (`install.py`) only copies files into skills directories.
- Skills are executable guidance for your agent. Review any skill before installing it, including this one, and prefer pinning a release tag.

Issues in the vendored Taste Skill code should also be reported upstream: https://github.com/Leonxlnx/taste-skill.
