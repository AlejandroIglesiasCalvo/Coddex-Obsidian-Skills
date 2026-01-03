#!/usr/bin/env python3
"""Append a read-log entry to cache/lecturas.json.

Usage:
  python scripts/log_read.py --vault /path/to/vault --path "ruta/nota.md" --followed "[[a]]" "[[b#Sec]]"
  python scripts/log_read.py --vault /path/to/vault --path "ruta/nota.md" --cache-dir "context/cache"

Notes:
- Creates cache/lecturas.json if missing.
- Stores sha256 of file bytes.
"""

from __future__ import annotations
import argparse
import hashlib
import json
from datetime import datetime
from pathlib import Path

def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return "sha256:" + h.hexdigest()

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--vault", required=True, help="Ruta a la raíz del vault")
    ap.add_argument("--path", required=True, help="Ruta del archivo relativa al vault")
    ap.add_argument("--followed", nargs="*", default=[], help="Wikilinks seguidos (texto)")
    ap.add_argument("--cache-dir", default="context/cache", help="Directorio de cache relativo al vault (default: context/cache)")
    args = ap.parse_args()

    vault = Path(args.vault).expanduser().resolve()
    target = (vault / args.path).resolve()
    if not target.exists():
        raise SystemExit(f"Archivo no encontrado: {target}")

    rel = str(target.relative_to(vault))
    entry = {
        "ruta": rel.replace('\\', '/'),
        "timestamp": datetime.utcnow().isoformat(timespec="seconds") + "Z",
        "tamano": target.stat().st_size,
        "hash": sha256_file(target),
        "origen": "filesystem",
        "enlaces_seguidos": list(args.followed),
    }

    cache_dir = (vault / args.cache_dir).resolve()
    cache_dir.mkdir(parents=True, exist_ok=True)
    out = cache_dir / "lecturas.json"

    data = []
    if out.exists():
        try:
            data = json.loads(out.read_text(encoding="utf-8") or "[]")
            if not isinstance(data, list):
                data = []
        except Exception:
            data = []

    data.append(entry)
    out.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(entry, ensure_ascii=False, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())


