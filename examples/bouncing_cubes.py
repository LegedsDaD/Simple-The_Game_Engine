from simple import Scene, Cube

scene = Scene()

scene.camera.position = (0.0, 6.0, 10.0)
scene.camera.rotation = (-25.0, 0.0, 0.0)

bounds = 4.0
cubes = []
vel = []

for i in range(20):
    c = Cube()
    c.scale = (0.35, 0.35, 0.35)
    c.position = (-(bounds * 0.8) + (i % 5) * 1.6, 0.2 + (i // 5) * 0.4, -1.0)
    c.spin = (20 + i * 3, 30 + i * 5, 10)
    c.color = (0.2 + (i % 5) * 0.15, 0.4 + (i % 3) * 0.2, 1.0 - (i % 4) * 0.15)
    cubes.append(c)
    vel.append((0.6 + i * 0.03, 0.0, 0.8 + i * 0.02))
    scene.add(c)


def update(scene: Scene, dt: float) -> None:
    for i, c in enumerate(cubes):
        x, y, z = c.position
        vx, vy, vz = vel[i]
        x += vx * dt
        z += vz * dt

        if x < -bounds or x > bounds:
            vx = -vx
            x = max(-bounds, min(bounds, x))
        if z < -bounds or z > bounds:
            vz = -vz
            z = max(-bounds, min(bounds, z))

        vel[i] = (vx, vy, vz)
        c.position = (x, y, z)


scene.on_update(update)
scene.run(title="Simple - Bouncing Cubes")

