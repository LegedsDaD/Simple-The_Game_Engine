# Backwards-compatible wrapper spec.
# The canonical specs now live in `editor/specs/`.
from __future__ import annotations

import os
import sys
from pathlib import Path

root = Path(os.environ.get("SIMPLE_REPO_ROOT", os.getcwd())).resolve()

if os.name == "nt":
    target = root / "editor" / "specs" / "windows.spec"
elif sys.platform == "darwin":
    target = root / "editor" / "specs" / "macos.spec"
else:
    target = root / "editor" / "specs" / "linux.spec"

spec_code = target.read_text(encoding="utf-8")
exec(compile(spec_code, str(target), "exec"), globals(), globals())
