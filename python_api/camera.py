from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

from . import _simple_core as core


@dataclass
class Camera:
    _core: core.Camera

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
    def fov(self) -> float:
        return float(self._core.fov_degrees)

    @fov.setter
    def fov(self, degrees: float) -> None:
        self._core.fov_degrees = float(degrees)

    @property
    def near(self) -> float:
        return float(self._core.z_near)

    @near.setter
    def near(self, v: float) -> None:
        self._core.z_near = float(v)

    @property
    def far(self) -> float:
        return float(self._core.z_far)

    @far.setter
    def far(self, v: float) -> None:
        self._core.z_far = float(v)

