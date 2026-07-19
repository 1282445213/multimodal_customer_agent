"""Validate the personal code-only directory without contacting remote APIs."""

from __future__ import annotations

import re
from pathlib import Path

from customer_agent.paths import CODE_ROOT


ALLOWED_SUFFIXES = {".py", ".sh", ".ps1", ".toml", ".txt"}
ALLOWED_FILENAMES = {".gitignore", "README.md"}
SECRET_RE = re.compile(r"sk-[A-Za-z0-9][A-Za-z0-9_-]{18,}")
REQUIRED_FILES = {
    "pyproject.toml",
    "requirements.txt",
    "src/customer_agent/__init__.py",
    "src/customer_agent/__main__.py",
    "src/customer_agent/paths.py",
    "src/customer_agent/api_server.py",
    "src/customer_agent/agent.py",
    "src/customer_agent/retrieval_engine.py",
}


def main() -> int:
    errors: list[str] = []
    files = [path for path in CODE_ROOT.rglob("*") if path.is_file()]

    present = {path.relative_to(CODE_ROOT).as_posix() for path in files}
    for required in sorted(REQUIRED_FILES - present):
        errors.append(f"缺少文件: {required}")

    for path in files:
        relative = path.relative_to(CODE_ROOT).as_posix()
        if "__pycache__" in path.parts or path.suffix in {".pyc", ".pyo"}:
            errors.append(f"包含 Python 缓存: {relative}")
        elif path.suffix.lower() not in ALLOWED_SUFFIXES and path.name not in ALLOWED_FILENAMES:
            errors.append(f"包含非代码资产: {relative}")
        if path.suffix == ".py":
            try:
                source = path.read_text(encoding="utf-8")
                compile(source, str(path), "exec")
                if SECRET_RE.search(source):
                    errors.append(f"包含疑似明文密钥: {relative}")
            except Exception as exc:  # noqa: BLE001
                errors.append(f"Python 语法错误: {relative}: {exc}")

    if errors:
        for error in errors:
            print(f"FAIL {error}")
        return 1

    print(f"code_layout=OK files={len(files)} python_files={sum(path.suffix == '.py' for path in files)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
