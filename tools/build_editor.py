from __future__ import annotations

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
    spec = root / "tools" / "simple_editor.spec"
    dist = root / "dist"
    build = root / "build"

    if dist.exists():
        shutil.rmtree(dist)
    if build.exists():
        shutil.rmtree(build)

    cmd = [sys.executable, "-m", "PyInstaller", "--noconfirm", str(spec)]
    print("$", " ".join(cmd))
    subprocess.check_call(cmd, cwd=str(root))


if __name__ == "__main__":
    main()

