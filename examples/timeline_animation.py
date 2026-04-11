from simple import Scene, Cube

scene = Scene()

cube = Cube()
cube.spin = (0, 0, 0)
scene.add(cube)

scene.camera.position = (0.0, 1.2, 6.0)
scene.camera.rotation = (-10.0, 0.0, 0.0)


def lerp(a: float, b: float, t: float) -> float:
    return a + (b - a) * t


def ease_in_out(t: float) -> float:
    t = max(0.0, min(1.0, t))
    return t * t * (3.0 - 2.0 * t)


time_s = 0.0


def update(scene: Scene, dt: float) -> None:
    global time_s
    time_s += dt

    # 3-stage "cutscene" loop, demonstrating high-level animation logic in Python.
    # Stage 0: move in, Stage 1: rotate, Stage 2: move out.
    phase = time_s % 6.0

    if phase < 2.0:
        t = ease_in_out(phase / 2.0)
        cube.position = (lerp(-2.5, 0.0, t), lerp(0.0, 0.5, t), lerp(-1.0, 0.0, t))
        cube.rotation = (0.0, 0.0, 0.0)
        cube.color = (0.2, 0.8, 1.0)
    elif phase < 4.0:
        t = ease_in_out((phase - 2.0) / 2.0)
        cube.position = (0.0, 0.5, 0.0)
        cube.rotation = (lerp(0.0, 360.0, t), lerp(0.0, 360.0, t), 0.0)
        cube.color = (1.0, 0.6, 0.2)
    else:
        t = ease_in_out((phase - 4.0) / 2.0)
        cube.position = (lerp(0.0, 2.5, t), lerp(0.5, 0.0, t), lerp(0.0, -1.5, t))
        cube.rotation = (0.0, 0.0, 0.0)
        cube.color = (0.6, 1.0, 0.4)


scene.on_update(update)
scene.run(title="Simple - Timeline Animation")

