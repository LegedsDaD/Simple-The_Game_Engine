"""
Compatibility layer.

The editor + tooling moved to `simple.editor.*`, but we keep `simple.tools`
to avoid breaking early users.
"""

from .blueprint import Blueprint, CubeSpec, load_blueprint, save_blueprint

__all__ = ["Blueprint", "CubeSpec", "load_blueprint", "save_blueprint"]

