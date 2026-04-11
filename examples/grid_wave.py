from simple import Scene, Cube

scene = Scene()

grid = []
size = 9
spacing = 0.8

for z in range(size):
    for x in range(size):
        c = Cube()
        c.scale = (0.35, 0.35, 0.35)
        c.spin = (0, 0, 0)
        c.position = ((x - size // 2) * spacing, 0.0, (z - size // 2) * spacing)
        scene.add(c)
        grid.append(c)

scene.camera.position = (0.0, 6.0, 10.0)
scene.camera.rotation = (-25.0, 0.0, 0.0)

t = 0.0


def update(scene: Scene, dt: float) -> None:
    global t
    t += dt
    import math

    for i, c in enumerate(grid):
        x, _, z = c.position
        y = math.sin(t * 2.0 + x * 1.2) * 0.4 + math.cos(t * 1.6 + z * 1.2) * 0.4
        c.position = (x, y, z)

        # Color as a function of height (simple "heatmap").
        v = max(-0.8, min(0.8, y))
        u = (v + 0.8) / 1.6
        c.color = (0.2 + 0.8 * u, 0.3 + 0.5 * (1.0 - u), 1.0 - 0.7 * u)


scene.on_update(update)
scene.run(title="Simple - Grid Wave")

