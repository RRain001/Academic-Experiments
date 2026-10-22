#!/usr/bin/env python3
"""Download *reference copies* to an IGNORED LOCAL CACHE, validate and hash.

No files are committed, redistributed or uploaded by this script. The public
Academic-Experiments repository stores source metadata only.
Usage:
  python3 scripts/fetch_reference_materials.py --list
  python3 scripts/fetch_reference_materials.py --default
  python3 scripts/fetch_reference_materials.py --id prairie-grass-epa
  python3 scripts/fetch_reference_materials.py --id chalk-river-1994-database --acknowledge-rights
  python3 scripts/fetch_reference_materials.py --id copenhagen-riso-1054 --acknowledge-rights
Restricted MUST report cannot be downloaded by this script.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import shutil
import sys
import tempfile
import time
import urllib.error
import urllib.request
import zipfile

REPO = Path(__file__).resolve().parents[1]
REGISTRY = REPO / "sources" / "binary_sources.json"
CACHE = REPO / ".cache" / "reference_materials"
UA = "Academic-Experiments/1.0 (research-provenance archive)"

def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda: f.read(1024 * 1024), b""):
            h.update(b)
    return h.hexdigest()

def inspect(path: Path, item: dict):
    typ = item["type"]
    with path.open("rb") as f:
        sig = f.read(12)
    if typ == "pdf":
        if not sig.startswith(b"%PDF-"):
            raise ValueError("Unexpected magic: not a PDF")
        try:
            import fitz
            with fitz.open(str(path)) as d:
                n = len(d)
        except ImportError:
            n = None
        return {"type": "pdf", "pages": n}
    if typ == "zip":
        if not zipfile.is_zipfile(path):
            raise ValueError("Unexpected magic: not ZIP")
        with zipfile.ZipFile(path) as z:
            bad = z.testzip()
            if bad:
                raise ValueError("CRC failure in " + bad)
            members = z.namelist()
        return {"type": "zip", "members": len(members), "sample_names": members[:20]}
    raise ValueError("Unknown type " + typ)

def download(item: dict, dest: Path, timeout: int, tries: int):
    if item["id"] == "must-report":
        raise PermissionError("MUST 2001 report states US government agencies only on cover; contact DTRA.")
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists():
        info = inspect(dest, item)
        digest = sha256(dest)
        if item.get("expected_sha256") and digest != item["expected_sha256"]:
            raise ValueError("Existing copy checksum mismatch; refusing to overwrite")
        return {"status": "ALREADY_PRESENT_VERIFIED", "sha256": digest, **info}
    last_error = None
    for i in range(tries):
        temp = None
        try:
            req = urllib.request.Request(item["url"], headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=timeout) as response:
                with tempfile.NamedTemporaryFile(dir=str(dest.parent), delete=False) as f:
                    temp = Path(f.name)
                    size = 0
                    while True:
                        part = response.read(1024 * 1024)
                        if not part:
                            break
                        size += len(part)
                        if size > 200 * 1024 * 1024:
                            raise ValueError("Download >200MB; stop for manual review")
                        f.write(part)
            info = inspect(temp, item)
            digest = sha256(temp)
            expected = item.get("expected_sha256")
            if expected is not None and digest != expected:
                raise ValueError(f"SHA256 mismatch: expected {expected}, got {digest}")
            shutil.move(str(temp), str(dest))
            return {"status": "DOWNLOADED_AND_VERIFIED", "sha256": digest, "size_bytes": size, **info}
        except Exception as exc:
            last_error = repr(exc)
            if temp is not None:
                temp.unlink(missing_ok=True)
            if i+1 < tries:
                time.sleep(i+1)
    raise RuntimeError(last_error)

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    group = ap.add_mutually_exclusive_group(required=True)
    group.add_argument("--list", action="store_true")
    group.add_argument("--default", action="store_true")
    group.add_argument("--id", action="append", dest="ids")
    ap.add_argument("--acknowledge-rights", action="store_true", help="For personal lawful source downloads; DOES NOT authorize GitHub upload")
    ap.add_argument("--timeout", type=int, default=45)
    ap.add_argument("--tries", type=int, default=3)
    args = ap.parse_args()
    items = json.loads(REGISTRY.read_text(encoding="utf-8"))["items"]
    if args.list:
        for it in items:
            print(f"{it['id']:<30s} default={str(it['default_download']):<5s} public_upload={it['public_repo_upload']} {it['url']}")
        return 0
    chosen = [it for it in items if it["default_download"]] if args.default else [it for it in items if it["id"] in args.ids]
    if args.ids and len(chosen) != len(set(args.ids)):
        print("Unknown requested ID", file=sys.stderr)
        return 2
    CACHE.mkdir(parents=True, exist_ok=True)
    failures = []
    for it in chosen:
        target = CACHE / it["experiment"] / it["filename"]
        result = {"id": it["id"], "source": it["url"], "checked_utc": datetime.now(timezone.utc).isoformat()}
        try:
            if not it["default_download"] and not args.acknowledge_rights:
                raise PermissionError("Requires --acknowledge-rights; public upload still forbidden")
            result.update(download(it, target, args.timeout, args.tries))
        except Exception as exc:
            result.update(status="FAILED_OR_RESTRICTED", error=str(exc))
            failures.append(it["id"])
        # Sidecars stored in ignored local cache; no claims written to source registry.
        sidecar = target.with_name(target.name + ".acquisition.json")
        sidecar.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
        print(it["id"], result["status"], result.get("sha256", result.get("error", "")))
    return 1 if failures else 0

if __name__ == "__main__":
    raise SystemExit(main())
