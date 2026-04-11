"""
Beginner-friendly key/mouse constants.

These match GLFW's values (Simple uses GLFW internally).
"""

from ._simple_core import (
    KEY_ESCAPE,
    KEY_W,
    KEY_A,
    KEY_S,
    KEY_D,
    KEY_P,
    KEY_V,
    KEY_R,
    KEY_SPACE,
    MOUSE_LEFT,
    MOUSE_RIGHT,
)

def asset_path(relative: str) -> str:
    """
    Returns an absolute path to a file inside the installed `simple/assets/` directory.

    Example:
        cube.texture = config.asset_path("checker.ppm")
    """

    import importlib.resources as res

    return str(res.files("simple").joinpath("assets").joinpath(relative))

__all__ = [
    "KEY_ESCAPE",
    "KEY_W",
    "KEY_A",
    "KEY_S",
    "KEY_D",
    "KEY_P",
    "KEY_V",
    "KEY_R",
    "KEY_SPACE",
    "MOUSE_LEFT",
    "MOUSE_RIGHT",
    "asset_path",
]
