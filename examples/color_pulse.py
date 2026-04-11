from simple import Scene, Cube

scene = Scene()

cube = Cube()
cube.scale = (1.2, 1.2, 1.2)
cube.spin = (30, 45, 15)
scene.add(cube)

scene.camera.position = (0.0, 0.5, 4.0)
scene.camera.rotation = (-5.0, 0.0, 0.0)

t = 0.0


def update(scene: Scene, dt: float) -> None:
    global t
    t += dt
    import math

    r = 0.5 + 0.5 * math.sin(t * 1.3)
    g = 0.5 + 0.5 * math.sin(t * 1.7 + 1.0)
    b = 0.5 + 0.5 * math.sin(t * 2.1 + 2.0)
    cube.color = (r, g, b)


scene.on_update(update)
scene.run(title="Simple - Color Pulse")

