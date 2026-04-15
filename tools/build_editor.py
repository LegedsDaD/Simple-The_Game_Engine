from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path


def main() -> None:
    """
    Builds a standalone Simple Editor executable using PyInstaller.

    Output:
      dist/SimpleEditor/ (one-folder build)
    """

    root = Path(__file__).resolve().parents[1]
    if sys.platform.startswith("win"):
        spec = root / "editor" / "specs" / "windows.spec"
    elif sys.platform == "darwin":
        spec = root / "editor" / "specs" / "macos.spec"
    else:
        spec = root / "editor" / "specs" / "linux.spec"
    dist = root / "dist"
    build = root / "build"

    if dist.exists():
        shutil.rmtree(dist)
    if build.exists():
        shutil.rmtree(build)

    env = dict(**os.environ)
    env["SIMPLE_REPO_ROOT"] = str(root)
    env["SIMPLE_SPEC_DIR"] = str(spec.parent)
    cmd = [sys.executable, "-m", "PyInstaller", "--noconfirm", str(spec)]
    print("$", " ".join(cmd))
    subprocess.check_call(cmd, cwd=str(root), env=env)


if __name__ == "__main__":
    main()
