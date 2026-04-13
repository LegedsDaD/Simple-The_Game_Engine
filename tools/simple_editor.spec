# PyInstaller spec for Simple Editor
from __future__ import annotations

import os
from pathlib import Path

from PyInstaller.utils.hooks import collect_data_files, collect_dynamic_libs, collect_submodules

def _find_repo_root(start: Path) -> Path:
    for candidate in [start, *start.parents]:
        if (candidate / "pyproject.toml").exists() and (candidate / "CMakeLists.txt").exists():
            return candidate
    return start


def _detect_repo_root() -> Path:
    # Prefer an explicit environment variable (set by tools/build_editor.py and CI).
    env_root = os.environ.get("SIMPLE_REPO_ROOT")
    if env_root:
        return _find_repo_root(Path(env_root).resolve())

    # PyInstaller defines `SPECPATH` as the directory containing this spec file.
    spec_dir = globals().get("SPECPATH")
    if spec_dir:
        return _find_repo_root(Path(spec_dir).resolve())

    # Last resort: walk up from current working directory.
    return _find_repo_root(Path(os.getcwd()).resolve())


root = _detect_repo_root()

hiddenimports = collect_submodules("simple")

datas = []
datas += collect_data_files("simple", includes=["assets/**", "templates/**"])

binaries = []
binaries += collect_dynamic_libs("simple")

a = Analysis(
    [str(root / "tools" / "simple_editor_entry.py")],
    pathex=[str(root)],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="SimpleEditor",
    console=True,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=False,
    name="SimpleEditor",
)
