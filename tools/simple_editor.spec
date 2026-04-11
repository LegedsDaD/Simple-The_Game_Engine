# PyInstaller spec for Simple Editor
from __future__ import annotations

import os
from pathlib import Path

from PyInstaller.utils.hooks import collect_data_files, collect_dynamic_libs, collect_submodules

root = Path(__file__).resolve().parents[1]

hiddenimports = collect_submodules("simple")

datas = []
datas += collect_data_files("simple", includes=["assets/**", "templates/**"])

binaries = []
binaries += collect_dynamic_libs("simple")

a = Analysis(
    ["-m", "simple.editor.app"],
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

