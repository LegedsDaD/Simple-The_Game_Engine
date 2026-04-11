from __future__ import annotations

import random

from simple import Scene, Cube, config

scene = Scene()
scene.background = (0.04, 0.04, 0.06)

scene.camera.position = (0.0, 2.8, 8.5)
scene.camera.rotation = (-16.0, 0.0, 0.0)

spawned: list[Cube] = []


def spawn() -> None:
    c = Cube()
    c.scale = (0.45, 0.45, 0.45)
    c.spin = (random.uniform(0, 60), random.uniform(20, 120), 0)
    c.texture = config.asset_path("checker.ppm")
    c.position = (random.uniform(-3.0, 3.0), random.uniform(-0.2, 1.2), random.uniform(-3.0, 3.0))
    scene.add(c)
    spawned.append(c)


def update(scene: Scene, dt: float) -> None:
    if scene.mouse_pressed(config.MOUSE_LEFT):
        for _ in range(3):
            spawn()

    scene.draw_text("Click Spawn (Textured)", 10, 10, 1.2, (1, 1, 1))
    scene.draw_text("LMB: spawn 3 cubes", 10, 32, 0.95, (1.0, 0.95, 0.7))
    scene.draw_text(f"Count: {len(spawned)}", 10, 55, 1.0, (0.8, 1.0, 0.8))
    scene.draw_text(f"FPS: {scene.fps:5.1f}", 10, 76, 1.0, (0.8, 1.0, 0.8))


scene.on_update(update)
scene.run(title="Simple - Click Spawn Textured")

