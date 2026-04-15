# Simple Editor (macOS) - PyInstaller spec
from __future__ import annotations

import importlib.util
import os
from pathlib import Path

spec_dir = Path(globals().get("SPECPATH", os.getcwd())).resolve()
os.environ["SIMPLE_SPEC_DIR"] = str(spec_dir)

common_path = spec_dir / "_common.py"
spec = importlib.util.spec_from_file_location("simple_editor_spec_common", str(common_path))
common = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(common)

a, pyz, exe, coll = common.build_spec(Analysis, PYZ, EXE, COLLECT, console=True, name="SimpleEditor")

