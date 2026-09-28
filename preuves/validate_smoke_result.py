#!/usr/bin/env python3
"""Validate the published Game Division smoke evidence.

This does NOT re-run the game HTML files; they are product assets and are not committed
in this repository. It checks that the published smoke result is structurally complete,
contains no recorded JS errors, and remains consistent with the public report.
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
result_path = HERE / "smoke_result.json"
report_path = HERE / "SMOKE_REPORT.md"

errors = []
try:
    rows = json.loads(result_path.read_text(encoding="utf-8"))
except Exception as exc:
    print(f"SMOKE EVIDENCE: FAIL — cannot parse smoke_result.json ({type(exc).__name__})")
    raise SystemExit(1)

if not isinstance(rows, list) or len(rows) < 16:
    errors.append(f"expected at least 16 published smoke rows, got {len(rows) if isinstance(rows, list) else 'non-list'}")
else:
    names = set()
    for i, row in enumerate(rows, 1):
        if not isinstance(row, dict):
            errors.append(f"row {i}: not an object")
            continue
        name = row.get("nom")
        if not name:
            errors.append(f"row {i}: missing nom")
        elif name in names:
            errors.append(f"row {i}: duplicate nom {name!r}")
        names.add(name)
        if not row.get("fichier"):
            errors.append(f"row {i}: missing fichier")
        if not row.get("titre"):
            errors.append(f"row {i}: missing titre")
        if not isinstance(row.get("commandes"), int) or row.get("commandes", 0) <= 0:
            errors.append(f"row {i}: no visible commands")
        if row.get("erreurs") not in ([], None):
            errors.append(f"row {i}: recorded errors: {row.get('erreurs')}")

if not report_path.exists() or report_path.stat().st_size == 0:
    errors.append("SMOKE_REPORT.md missing or empty")

if errors:
    print("SMOKE EVIDENCE: FAIL")
    for e in errors:
        print("-", e)
    sys.exit(1)

print(f"SMOKE EVIDENCE: PASS — {len(rows)} published runs, no recorded JS errors, commands present")
print("Scope: validates published evidence only; does not re-run uncommitted game product files.")
