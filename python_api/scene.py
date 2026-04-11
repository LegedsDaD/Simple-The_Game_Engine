from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, Optional, Tuple

from . import _simple_core as core
from .camera import Camera
from .objects import Cube


UpdateFn = Callable[["Scene", float], None]


@dataclass
class Scene:
    _core: core.Scene = field(default_factory=core.Scene)

    def add(self, obj) -> None:
        if isinstance(obj, Cube):
            self._core.add(obj._core)
            return
        self._core.add(obj)

    def remove(self, obj) -> None:
        if isinstance(obj, Cube):
            self._core.remove(obj._core)
            return
        self._core.remove(obj)

    def clear(self) -> None:
        self._core.clear()

    @property
    def camera(self) -> Camera:
        return Camera(self._core.camera)

    def disable_branding(self) -> None:
        self._core.disable_branding()

    @property
    def background(self) -> Tuple[float, float, float]:
        return tuple(self._core.background)  # type: ignore[arg-type]

    @background.setter
    def background(self, rgb) -> None:
        self._core.background = rgb

    def on_update(self, fn: Optional[UpdateFn]) -> None:
        if fn is None:
            self._core.set_update_callback(lambda dt: None)
            return

        def _cb(dt: float) -> None:
            try:
                fn(self, float(dt))
            except TypeError:
                fn(float(dt))  # type: ignore[misc]

        self._core.set_update_callback(_cb)

    def run(self, width: int = 900, height: int = 600, title: str = "Simple") -> None:
        self._core.run(int(width), int(height), str(title))

    @property
    def time_seconds(self) -> float:
        return float(self._core.time_seconds)

    @property
    def fps(self) -> float:
        return float(self._core.fps)

    @property
    def frame_index(self) -> int:
        return int(self._core.frame_index)

    def draw_text(
        self,
        text: str,
        x: float = 10.0,
        y: float = 10.0,
        size: float = 1.0,
        color=(1.0, 1.0, 1.0),
    ) -> None:
        self._core.draw_text(str(text), float(x), float(y), float(size), color)

    def set_title(self, title: str) -> None:
        self._core.set_title(str(title))

    def set_vsync(self, enabled: bool) -> None:
        self._core.set_vsync(bool(enabled))

    def draw_line3d(self, a, b, color=(1.0, 1.0, 1.0)) -> None:
        self._core.draw_line3d(a, b, color)

    def screenshot(self, path: str) -> None:
        """
        Request a screenshot of the next rendered frame.

        Saves as a binary PPM (P6).
        """

        self._core.screenshot(str(path))

    # Input helpers
    def key_down(self, key: int) -> bool:
        return bool(self._core.key_down(int(key)))

    def key_pressed(self, key: int) -> bool:
        return bool(self._core.key_pressed(int(key)))

    def mouse_down(self, button: int) -> bool:
        return bool(self._core.mouse_down(int(button)))

    def mouse_pressed(self, button: int) -> bool:
        return bool(self._core.mouse_pressed(int(button)))

    def mouse_position(self) -> Tuple[float, float]:
        x, y = self._core.mouse_position()
        return float(x), float(y)

    def mouse_delta(self) -> Tuple[float, float]:
        dx, dy = self._core.mouse_delta()
        return float(dx), float(dy)
