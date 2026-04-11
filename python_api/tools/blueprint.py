"""
Backwards-compatible re-export.

Editor code lives under `simple.editor.*` now; keep `simple.tools.blueprint`
as an import-stable alias for users.
"""

from simple.editor.blueprint import Blueprint, CubeSpec, load_blueprint, save_blueprint  # noqa: F401
