from simple import Scene, Cube, config

scene = Scene()
scene.background = (0.05, 0.05, 0.07)

# A small scene.
for i in range(8):
    c = Cube()
    c.position = ((i - 4) * 1.0, 0.0, -(i % 3) * 1.2)
    c.spin = (10 * (i + 1), 20 * (i + 1), 0)
    scene.add(c)

scene.camera.position = (0.0, 2.0, 9.0)
scene.camera.rotation = (-12.0, 0.0, 0.0)


def update(scene: Scene, dt: float) -> None:
    scene.draw_text("Simple Pro HUD Demo", 10, 10, 1.2, (1.0, 1.0, 1.0))
    scene.draw_text(f"FPS: {scene.fps:5.1f}", 10, 32, 1.0, (0.8, 1.0, 0.8))
    scene.draw_text(f"Time: {scene.time_seconds:6.2f}s", 10, 50, 1.0, (0.8, 0.9, 1.0))
    scene.draw_text(f"Frame: {scene.frame_index}", 10, 68, 1.0, (0.9, 0.9, 0.9))

    scene.draw_text("RMB+Mouse: orbit camera", 10, 95, 0.95, (1.0, 0.95, 0.7))
    scene.draw_text("ESC: quit", 10, 112, 0.95, (1.0, 0.95, 0.7))

    # Camera orbit.
    if scene.mouse_down(config.MOUSE_RIGHT):
        dx, dy = scene.mouse_delta()
        pitch, yaw, roll = scene.camera.rotation
        yaw += dx * 0.15
        pitch += dy * 0.15
        pitch = max(-80.0, min(80.0, pitch))
        scene.camera.rotation = (pitch, yaw, roll)


scene.on_update(update)
scene.run(title="Simple - Pro Debug HUD")

