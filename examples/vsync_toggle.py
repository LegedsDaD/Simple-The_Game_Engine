from simple import Scene, Cube, config

scene = Scene()

cube = Cube()
cube.spin = (20, 45, 0)
cube.texture = config.asset_path("checker.ppm")
scene.add(cube)

scene.camera.position = (0.0, 0.8, 4.8)
scene.camera.rotation = (-6.0, 0.0, 0.0)

vsync = True
scene.set_vsync(True)

title_accum = 0.0


def update(scene: Scene, dt: float) -> None:
    global vsync, title_accum

    if scene.key_pressed(config.KEY_V):
        vsync = not vsync
        scene.set_vsync(vsync)

    title_accum += dt
    if title_accum >= 0.25:
        title_accum = 0.0
        scene.set_title(f"Simple - VSync {'ON' if vsync else 'OFF'}  ({scene.fps:0.0f} FPS)")

    scene.draw_text("VSync Toggle", 10, 10, 1.2, (1, 1, 1))
    scene.draw_text("V: toggle vsync", 10, 32, 0.95, (1.0, 0.95, 0.7))
    scene.draw_text(f"VSync: {'ON' if vsync else 'OFF'}", 10, 55, 1.0, (0.7, 1.0, 0.7) if vsync else (1.0, 0.7, 0.7))
    scene.draw_text(f"FPS: {scene.fps:5.1f}", 10, 76, 1.0, (0.8, 1.0, 0.8))


scene.on_update(update)
scene.run(title="Simple - VSync Toggle (press V)")

