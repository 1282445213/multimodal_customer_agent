#!/usr/bin/env bash
set -euo pipefail

CODE_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$CODE_ROOT"

PYTHON_BIN="${PYTHON_BIN:-python}"
HOST="${HOST:-0.0.0.0}"
PORT="${PORT:-8000}"
export PYTHONPATH="$CODE_ROOT/src${PYTHONPATH:+:$PYTHONPATH}"

exec "$PYTHON_BIN" -m customer_agent
