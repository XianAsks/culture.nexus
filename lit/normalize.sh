#!/bin/sh
# Normalize lit/ after any retrieval run. Idempotent — safe to re-run.
# Thin wrapper; all logic lives in normalize.py (stdlib only).
exec uv run --no-project python3 "$(dirname "$0")/normalize.py" "$@"
