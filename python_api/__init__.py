"""
Simple Engine (Python API).

Visible results in under 10 lines:

    from simple import Scene, Cube
    scene = Scene()
    cube = Cube()
    scene.add(cube)
    scene.run()
"""

from .engine import __version__
from .scene import Scene
from .objects import Cube
from .camera import Camera
from . import config
from . import tools

__all__ = ["Scene", "Cube", "Camera", "config", "tools", "__version__"]
