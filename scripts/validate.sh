#!/usr/bin/env bash
# Structural checks only. Behavioral evaluation is documented in tests/behavioral.md.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
if ! command -v python3 >/dev/null 2>&1; then
  echo "ERROR: Python 3.9+ is required for validation." >&2
  exit 1
fi
exec python3 "$ROOT/scripts/validate.py" "$@"
