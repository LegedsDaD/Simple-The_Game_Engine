from simple import Scene, Cube

scene = Scene()

sun = Cube()
sun.scale = (1.2, 1.2, 1.2)
sun.color = (1.0, 0.7, 0.15)
sun.spin = (0, 20, 0)
scene.add(sun)

planets = []
params = [
    # (radius, speed_deg_s, size, color)
    (2.3, 80, 0.35, (0.4, 0.8, 1.0)),
    (3.6, 55, 0.50, (0.2, 1.0, 0.6)),
    (5.0, 35, 0.65, (0.9, 0.3, 1.0)),
]

for r, speed, size, col in params:
    p = Cube()
    p.scale = (size, size, size)
    p.color = col
    p.spin = (0, speed * 0.5, 0)
    scene.add(p)
    planets.append((p, r, speed))

scene.camera.position = (0.0, 3.2, 10.0)
scene.camera.rotation = (-15.0, 0.0, 0.0)

angle = 0.0


def update(scene: Scene, dt: float) -> None:
    global angle
    angle += dt
    import math

    for p, radius, speed in planets:
        a = angle * speed
        x = math.cos(math.radians(a)) * radius
        z = math.sin(math.radians(a)) * radius
        p.position = (x, 0.0, z)


scene.on_update(update)
scene.run(title="Simple - Solar System")

