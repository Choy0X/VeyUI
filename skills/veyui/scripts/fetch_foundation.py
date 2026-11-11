#!/usr/bin/env python3
"""Fetch the pinned Taste Skill web foundation and verify it byte for byte.

veyUI does not store the foundation in this repository. It records the exact upstream commit and
the SHA-256 of every file in data/foundation-manifest.json. This script downloads that commit's
archive from GitHub, rebuilds the foundation/ folder (upstream skills/taste-skill, with SKILL.md
renamed to upstream-guide.md, plus the upstream LICENSE), checks every file against the manifest
and only then puts it in place. Nothing unverified is ever left on disk.

Usage:
    python scripts/fetch_foundation.py            fetch if missing or damaged, then verify
    python scripts/fetch_foundation.py --check    verify the existing copy only, no network
    python scripts/fetch_foundation.py --force    download again even if the copy verifies
    python scripts/fetch_foundation.py --root DIR put foundation/ inside DIR instead of next to SKILL.md

The one network call is a download from codeload.github.com. Needs only the Python standard library.
"""
import argparse
import hashlib
import io
import json
import os
import shutil
import sys
import tarfile
import tempfile
import urllib.error
import urllib.request
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parents[1]
MAX_ARCHIVE_BYTES = 120 * 1024 * 1024
MAX_FILE_BYTES = 20 * 1024 * 1024


def load_manifest():
    return json.loads((SKILL_ROOT / "data" / "foundation-manifest.json").read_text(encoding="utf-8"))


def expected_files(manifest):
    return {entry["path"]: entry["sha256"] for entry in manifest["files"]}


def verify_dir(root, want):
    """Return a list of problems for root/foundation compared with the manifest."""
    problems = []
    base = root / "foundation"
    if not base.is_dir():
        return ["foundation/ is not present"]
    seen = set()
    for rel, digest in want.items():
        path = root / rel
        seen.add(rel)
        if not path.is_file():
            problems.append("missing: " + rel)
        elif hashlib.sha256(path.read_bytes()).hexdigest() != digest:
            problems.append("changed: " + rel)
    for path in base.rglob("*"):
        if path.is_file():
            rel = path.relative_to(root).as_posix()
            if rel not in seen:
                problems.append("unexpected file: " + rel)
    return problems


def download(manifest):
    repo = manifest["repository"].rstrip("/")
    owner_repo = "/".join(repo.split("/")[-2:])
    url = "https://codeload.github.com/%s/tar.gz/%s" % (owner_repo, manifest["commit"])
    print("downloading " + url, file=sys.stderr)
    request = urllib.request.Request(url, headers={"User-Agent": "veyui-fetch-foundation"})
    with urllib.request.urlopen(request, timeout=180) as response:
        data = response.read(MAX_ARCHIVE_BYTES + 1)
    if len(data) > MAX_ARCHIVE_BYTES:
        raise SystemExit("archive is larger than the %d MiB safety limit" % (MAX_ARCHIVE_BYTES // 1048576))
    return data


def build_files(data, manifest):
    """Map manifest paths to bytes taken from the archive."""
    source_dir = manifest["source_directory"].strip("/") + "/"
    files = {}
    with tarfile.open(fileobj=io.BytesIO(data), mode="r:gz") as archive:
        for member in archive.getmembers():
            if not member.isfile() or member.size > MAX_FILE_BYTES:
                continue
            parts = member.name.split("/", 1)
            if len(parts) < 2 or ".." in Path(parts[1]).parts:
                continue
            rel = parts[1]
            if rel == "LICENSE":
                files["foundation/LICENSE"] = archive.extractfile(member).read()
            elif rel.startswith(source_dir):
                sub = rel[len(source_dir):]
                if sub == "SKILL.md":
                    sub = "upstream-guide.md"
                files["foundation/" + sub] = archive.extractfile(member).read()
    return files


def install(root, manifest, force=False):
    want = expected_files(manifest)
    if not force and not verify_dir(root, want):
        return 0, "already present and verified"
    files = build_files(download(manifest), manifest)
    bad = [p for p in want if p not in files or hashlib.sha256(files[p]).hexdigest() != want[p]]
    extra = [p for p in files if p not in want]
    if bad or extra:
        print(json.dumps({"verified": False, "mismatched_or_missing": bad[:20], "unexpected": extra[:20]}, indent=2))
        return 1, "downloaded archive does not match the manifest; nothing was installed"
    root.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix=".foundation-", dir=str(root)))
    try:
        for rel, content in files.items():
            target = staging / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(content)
        final = root / "foundation"
        if final.exists():
            shutil.rmtree(final)
        os.replace(str(staging / "foundation"), str(final))
    finally:
        shutil.rmtree(staging, ignore_errors=True)
    problems = verify_dir(root, want)
    if problems:
        print(json.dumps({"verified": False, "problems": problems[:20]}, indent=2))
        return 1, "verification failed after writing"
    return 0, "fetched and verified %d files" % len(want)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--check", action="store_true", help="verify the existing copy only (no network)")
    parser.add_argument("--force", action="store_true", help="download again even if the copy verifies")
    parser.add_argument("--root", help="directory that holds foundation/ (default: next to SKILL.md)")
    args = parser.parse_args()
    manifest = load_manifest()
    root = Path(args.root).resolve() if args.root else SKILL_ROOT
    if args.check:
        problems = verify_dir(root, expected_files(manifest))
        print(json.dumps({"commit": manifest["commit"], "intact": not problems, "problems": problems[:20]}, indent=2))
        return 1 if problems else 0
    try:
        code, message = install(root, manifest, force=args.force)
    except (OSError, urllib.error.URLError) as error:
        print("Could not fetch the foundation: %s" % error, file=sys.stderr)
        print("The offline library, concept studio and design modules work without it. "
              "Only the web construction tools need it. Connect to the internet and run this script again, "
              "or copy a verified foundation/ folder into %s." % root, file=sys.stderr)
        return 2
    print(json.dumps({"commit": manifest["commit"], "foundation": str(root / "foundation"), "result": message}, indent=2))
    return code


if __name__ == "__main__":
    sys.exit(main())
