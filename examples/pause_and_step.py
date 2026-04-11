from simple import Scene, Cube, config

scene = Scene()
scene.background = (0.03, 0.03, 0.05)

cube = Cube()
cube.spin = (0, 0, 0)
cube.color = (0.3, 0.9, 1.0)
scene.add(cube)

scene.camera.position = (0.0, 1.2, 6.0)
scene.camera.rotation = (-10.0, 0.0, 0.0)

paused = False
step_one = False


def update(scene: Scene, dt: float) -> None:
    global paused, step_one

    if scene.key_pressed(config.KEY_P):
        paused = not paused

    if scene.key_pressed(config.KEY_SPACE):
        step_one = True

    do_update = (not paused) or step_one
    step_one = False

    if do_update:
        rx, ry, rz = cube.rotation
        cube.rotation = (rx + 60 * dt, ry + 90 * dt, rz)

    scene.draw_text("Pause + Step Demo", 10, 10, 1.2, (1, 1, 1))
    scene.draw_text("P: pause/resume   Space: step one frame", 10, 32, 0.95, (1.0, 0.95, 0.7))
    scene.draw_text(f"Paused: {paused}", 10, 55, 1.0, (1.0, 0.6, 0.6) if paused else (0.7, 1.0, 0.7))
    scene.draw_text(f"FPS: {scene.fps:5.1f}", 10, 76, 1.0, (0.8, 1.0, 0.8))


scene.on_update(update)
scene.run(title="Simple - Pause & Step")

