from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

from . import _simple_core as core


@dataclass
class Cube:
    _core: core.Cube = core.Cube()

    @property
    def position(self) -> Tuple[float, float, float]:
        return tuple(self._core.position)  # type: ignore[arg-type]

    @position.setter
    def position(self, v) -> None:
        self._core.position = v

    @property
    def rotation(self) -> Tuple[float, float, float]:
        return tuple(self._core.rotation)  # type: ignore[arg-type]

    @rotation.setter
    def rotation(self, v) -> None:
        self._core.rotation = v

    @property
    def scale(self) -> Tuple[float, float, float]:
        return tuple(self._core.scale)  # type: ignore[arg-type]

    @scale.setter
    def scale(self, v) -> None:
        self._core.scale = v

    @property
    def color(self) -> Tuple[float, float, float]:
        return tuple(self._core.color)  # type: ignore[arg-type]

    @color.setter
    def color(self, v) -> None:
        self._core.color = v

    @property
    def spin(self) -> Tuple[float, float, float]:
        return tuple(self._core.spin)  # type: ignore[arg-type]

    @spin.setter
    def spin(self, v) -> None:
        self._core.spin = v

    @property
    def texture(self) -> str:
        return str(self._core.texture)

    @texture.setter
    def texture(self, path: str) -> None:
        self._core.texture = str(path)
