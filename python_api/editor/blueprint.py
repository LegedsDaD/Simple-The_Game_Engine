from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Tuple

Vec3 = Tuple[float, float, float]


@dataclass
class CubeSpec:
    name: str = "Cube"
    position: Vec3 = (0.0, 0.0, 0.0)
    rotation: Vec3 = (0.0, 0.0, 0.0)
    scale: Vec3 = (1.0, 1.0, 1.0)
    color: Vec3 = (0.2, 0.6, 1.0)
    texture: str = ""
    spin: Vec3 = (0.0, 45.0, 0.0)
    behaviors: List[Dict[str, Any]] = field(default_factory=list)


@dataclass
class Blueprint:
    """
    Data-driven scene description.

    This is intentionally JSON-friendly and editor-focused.
    """

    background: Vec3 = (0.06, 0.06, 0.08)
    camera_position: Vec3 = (0.0, 0.0, 3.5)
    camera_rotation: Vec3 = (0.0, 0.0, 0.0)
    cubes: List[CubeSpec] = field(default_factory=list)
    lines: List[dict] = field(default_factory=list)  # {"name":str, "a":[x,y,z], "b":[x,y,z], "color":[r,g,b]}


def load_blueprint(path: str | Path) -> Blueprint:
    p = Path(path)
    data = json.loads(p.read_text(encoding="utf-8"))
    bp = Blueprint(
        background=tuple(data.get("background", Blueprint().background)),  # type: ignore[arg-type]
        camera_position=tuple(data.get("camera_position", Blueprint().camera_position)),  # type: ignore[arg-type]
        camera_rotation=tuple(data.get("camera_rotation", Blueprint().camera_rotation)),  # type: ignore[arg-type]
        cubes=[],
        lines=list(data.get("lines", [])),
    )
    for c in data.get("cubes", []):
        bp.cubes.append(
            CubeSpec(
                name=str(c.get("name", "Cube")),
                position=tuple(c.get("position", (0, 0, 0))),  # type: ignore[arg-type]
                rotation=tuple(c.get("rotation", (0, 0, 0))),  # type: ignore[arg-type]
                scale=tuple(c.get("scale", (1, 1, 1))),  # type: ignore[arg-type]
                color=tuple(c.get("color", (0.2, 0.6, 1.0))),  # type: ignore[arg-type]
                texture=str(c.get("texture", "")),
                spin=tuple(c.get("spin", (0, 45, 0))),  # type: ignore[arg-type]
                behaviors=list(c.get("behaviors", [])),
            )
        )
    return bp


def save_blueprint(bp: Blueprint, path: str | Path) -> None:
    p = Path(path)
    data = asdict(bp)
    p.write_text(json.dumps(data, indent=2), encoding="utf-8")

