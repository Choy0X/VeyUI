#!/usr/bin/env sh
# Thin wrapper: installs veyUI for your coding agents. Pass any install.py option.
set -eu
here="$(cd "$(dirname "$0")" && pwd)"
if command -v python3 >/dev/null 2>&1; then exec python3 "$here/install.py" "$@"; fi
if command -v python >/dev/null 2>&1; then exec python "$here/install.py" "$@"; fi
echo "Python 3.10+ is required. Install it, or run: npx skills add Choy0X/VeyUI" >&2
exit 1
