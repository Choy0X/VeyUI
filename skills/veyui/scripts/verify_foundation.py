#!/usr/bin/env python3
"""Check the bundled upstream snapshot. Does not certify rendered UI quality."""
import hashlib
import json
from pathlib import Path
import sys


def verify(root):
    manifest = json.loads((root / "data/foundation-manifest.json").read_text(encoding='utf-8'))
    failures = []
    paths = set()
    for entry in manifest["files"]:
        rel = entry["path"]
        path = root / rel
        if not rel.startswith("foundation/") or ".." in Path(rel).parts:
            failures.append(f"invalid path: {rel}")
            continue
        if rel in paths:
            failures.append(f"duplicate path: {rel}")
        paths.add(rel)
        if not path.is_file():
            failures.append(f"missing: {rel}")
        elif hashlib.sha256(path.read_bytes()).hexdigest() != entry["sha256"]:
            failures.append(f"changed: {rel}")
    actual = {p.relative_to(root).as_posix() for p in (root / "foundation").rglob("*") if p.is_file()}
    failures.extend(f"untracked snapshot file: {p}" for p in sorted(actual - paths))
    print(json.dumps({"commit": manifest["commit"], "files": len(paths),
                      "intact": not failures, "failures": failures,
                      "notice": "Source integrity only; no browser or design-quality claim."}, indent=2))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(verify(Path(__file__).resolve().parents[1]))
