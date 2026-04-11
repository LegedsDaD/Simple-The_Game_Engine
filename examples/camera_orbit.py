from simple import Scene, Cube, config

scene = Scene()

target = Cube()
target.color = (1.0, 0.8, 0.2)
target.spin = (0, 20, 0)
scene.add(target)

satellite = Cube()
satellite.scale = (0.4, 0.4, 0.4)
satellite.color = (0.2, 0.7, 1.0)
satellite.spin = (0, 90, 0)
scene.add(satellite)

scene.camera.position = (0.0, 1.3, 6.0)
scene.camera.rotation = (-10.0, 0.0, 0.0)

orbit_yaw = 0.0
orbit_radius = 3.0


def update(scene: Scene, dt: float) -> None:
    global orbit_yaw

    # Hold RMB to orbit camera around the origin.
    if scene.mouse_down(config.MOUSE_RIGHT):
        dx, dy = scene.mouse_delta()
        pitch, yaw, roll = scene.camera.rotation
        yaw += dx * 0.15
        pitch += dy * 0.15
        pitch = max(-80.0, min(80.0, pitch))
        scene.camera.rotation = (pitch, yaw, roll)

    # Animate a "satellite" cube orbiting the target.
    orbit_yaw += 60.0 * dt
    import math

    x = math.cos(math.radians(orbit_yaw)) * orbit_radius
    z = math.sin(math.radians(orbit_yaw)) * orbit_radius
    satellite.position = (x, 0.2, z)


scene.on_update(update)
scene.run(title="Simple - Camera Orbit")

