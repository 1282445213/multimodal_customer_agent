"""Shared code and external asset paths.

The personal directory intentionally contains code only. Runtime datasets can
be selected with ``KBRAG_ASSET_ROOT``. When it is unset, the package reuses the
original sibling ``V6_submit_code`` directory if that directory exists.
"""

from __future__ import annotations

import os
from pathlib import Path


PACKAGE_DIR = Path(__file__).resolve().parent
CODE_ROOT = PACKAGE_DIR.parents[1]
ORIGINAL_ASSET_ROOT = CODE_ROOT.parent / "V6_submit_code"
DEFAULT_ASSET_ROOT = ORIGINAL_ASSET_ROOT if ORIGINAL_ASSET_ROOT.is_dir() else CODE_ROOT
ASSET_ROOT = Path(os.getenv("KBRAG_ASSET_ROOT", str(DEFAULT_ASSET_ROOT))).expanduser().resolve()

DATA_DIR = ASSET_ROOT / "data"
MANUAL_DIR = ASSET_ROOT / "手册_v4"
IMAGE_DIR = ASSET_ROOT / "手册" / "插图"
SUBMISSIONS_DIR = ASSET_ROOT / "submissions"
VALIDATION_OUTPUT_DIR = ASSET_ROOT / "validation_outputs"
