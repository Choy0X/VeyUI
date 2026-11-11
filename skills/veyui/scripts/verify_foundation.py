#!/usr/bin/env python3
"""Check the fetched upstream foundation against the manifest. Does not certify rendered UI quality.

The foundation is not stored in the repository. Run `python scripts/fetch_foundation.py` first
(or pass --fetch here) to download the pinned Taste Skill commit. Source integrity only.
"""
import hashlib
import json
import subprocess
from pathlib import Path
import sys


def verify(root):
    manifest = json.loads((root / "data/foundation-manifest.json").read_text(encoding='utf-8'))
    failures = []
    paths = set()
    present = (root / "foundation").is_dir()
    if not present:
        failures.append("foundation/ has not been fetched; run scripts/fetch_foundation.py")
    for entry in manifest["files"]:
        rel = entry["path"]
        path = root / rel
        if not rel.startswith("foundation/") or ".." in Path(rel).parts:
            failures.append(f"invalid path: {rel}")
            continue
        if rel in paths:
            failures.append(f"duplicate path: {rel}")
        paths.add(rel)
        if present:
            if not path.is_file():
                failures.append(f"missing: {rel}")
            elif hashlib.sha256(path.read_bytes()).hexdigest() != entry["sha256"]:
                failures.append(f"changed: {rel}")
    if present:
        actual = {p.relative_to(root).as_posix() for p in (root / "foundation").rglob("*") if p.is_file()}
        failures.extend(f"unexpected file: {p}" for p in sorted(actual - paths))
    print(json.dumps({"commit": manifest["commit"], "files": len(paths),
                      "intact": not failures, "failures": failures[:25],
                      "notice": "Source integrity only; no browser or design-quality claim."}, indent=2))
    return 1 if failures else 0


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    if "--fetch" in sys.argv[1:]:
        code = subprocess.call([sys.executable, str(root / "scripts" / "fetch_foundation.py")])
        if code:
            sys.exit(code)
    sys.exit(verify(root))
