from __future__ import annotations

import argparse
import importlib.util
import math
from pathlib import Path
from types import ModuleType

from .. import Cube, Scene, config
from .blueprint import load_blueprint


def _load_project_script(path: Path) -> ModuleType | None:
    if not path.exists():
        return None
    spec = importlib.util.spec_from_file_location("simple_project_game", str(path))
    if not spec or not spec.loader:
        return None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def run_project(project_dir: str) -> None:
    root = Path(project_dir)
    if root.suffix.lower() != ".sim":
        # Allow running by passing a folder that contains a .sim folder.
        if root.is_dir() and (root / "scene.simple.json").exists():
            pass
    bp_path = root / "scene.simple.json"
    if not bp_path.exists():
        raise SystemExit(f"Missing blueprint: {bp_path}")

    bp = load_blueprint(bp_path)

    scene = Scene()
    scene.background = bp.background
    scene.camera.position = bp.camera_position
    scene.camera.rotation = bp.camera_rotation

    # Instantiate cubes, keep by-name mapping for scripts.
    cube_by_name: dict[str, Cube] = {}
    cube_specs = []
    for spec in bp.cubes:
        c = Cube()
        c.position = spec.position
        c.rotation = spec.rotation
        c.scale = spec.scale
        c.color = spec.color
        tex = spec.texture or ""
        if tex.startswith("simple:"):
            tex = config.asset_path(tex.split(":", 1)[1])
        elif tex and not Path(tex).is_absolute():
            tex = str((root / tex).resolve())
        c.texture = tex
        c.spin = spec.spin
        scene.add(c)
        cube_by_name[spec.name] = c
        cube_specs.append((c, spec))

    blueprint_lines = list(bp.lines)

    # Optional Python gameplay script (editor-friendly).
    game_py = root / "game.py"
    game_mod = _load_project_script(game_py)
    if game_mod and hasattr(game_mod, "start"):
        try:
            game_mod.start(scene, cube_by_name)  # type: ignore[misc]
        except TypeError:
            game_mod.start(scene)  # type: ignore[misc]

    # IPC files for editor (screenshot request).
    ipc = root / ".simple_ipc"
    ipc.mkdir(parents=True, exist_ok=True)
    screenshot_req = ipc / "screenshot.request"
    screenshot_out = ipc / "screenshot.ppm"

    def apply_behaviors(dt: float) -> None:
        t = scene.time_seconds
        for cube, spec in cube_specs:
            for beh in spec.behaviors or []:
                kind = str(beh.get("type", "")).lower()
                if kind == "bob":
                    amp = float(beh.get("amplitude", 0.5))
                    freq = float(beh.get("frequency", 1.5))
                    x, y0, z = cube.position
                    cube.position = (x, math.sin(t * freq) * amp, z)
                elif kind == "orbit":
                    cx, cy, cz = beh.get("center", (0.0, 0.0, 0.0))
                    radius = float(beh.get("radius", 2.0))
                    speed = float(beh.get("speed_deg_s", 45.0))
                    ang = math.radians(t * speed)
                    cube.position = (float(cx) + math.cos(ang) * radius, float(cy), float(cz) + math.sin(ang) * radius)

    def update(scene: Scene, dt: float) -> None:
        apply_behaviors(dt)

        # Blueprint lines are per-frame gizmos.
        for ln in blueprint_lines:
            try:
                a = tuple(ln.get("a", (0, 0, 0)))
                b = tuple(ln.get("b", (0, 0, 0)))
                col = tuple(ln.get("color", (1, 1, 1)))
                scene.draw_line3d(a, b, col)
            except Exception:
                pass

        # Game script update hook.
        if game_mod and hasattr(game_mod, "update"):
            try:
                game_mod.update(scene, dt, cube_by_name)  # type: ignore[misc]
            except TypeError:
                game_mod.update(scene, dt)  # type: ignore[misc]

        # Screenshot request from editor.
        if screenshot_req.exists():
            try:
                screenshot_req.unlink(missing_ok=True)  # type: ignore[arg-type]
            except Exception:
                pass
            scene.screenshot(str(screenshot_out))

        # HUD: basic diagnostics.
        scene.draw_text(f"{root.name}", 10, 10, 1.15, (1, 1, 1))
        scene.draw_text(f"FPS: {scene.fps:0.1f}", 10, 30, 1.0, (0.8, 1.0, 0.8))

    scene.on_update(update)
    scene.run(title=root.name or "Simple Project")


def main() -> None:
    ap = argparse.ArgumentParser(prog="simple-editor-runtime")
    ap.add_argument("project_dir", help="Folder ending in .sim containing scene.simple.json")
    args = ap.parse_args()
    run_project(args.project_dir)


if __name__ == "__main__":
    main()
