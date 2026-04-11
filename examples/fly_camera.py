from simple import Scene, Cube, config

scene = Scene()

# A few landmarks.
for i in range(10):
    c = Cube()
    c.position = ((i - 5) * 1.5, 0.0, -i * 2.0)
    c.color = (0.2 + i * 0.07, 0.6, 1.0 - i * 0.05)
    c.spin = (0, 0, 0)
    scene.add(c)

scene.camera.position = (0.0, 1.2, 4.0)
scene.camera.rotation = (0.0, 0.0, 0.0)


def update(scene: Scene, dt: float) -> None:
    # Mouse look (hold RMB).
    if scene.mouse_down(config.MOUSE_RIGHT):
        dx, dy = scene.mouse_delta()
        pitch, yaw, roll = scene.camera.rotation
        yaw += dx * 0.15
        pitch += dy * 0.15
        pitch = max(-85.0, min(85.0, pitch))
        scene.camera.rotation = (pitch, yaw, roll)

    # Simple WASD forward/back/strafe (relative to camera yaw only).
    import math

    pitch, yaw, _ = scene.camera.rotation
    yaw_r = math.radians(yaw)
    forward = (math.sin(yaw_r), 0.0, -math.cos(yaw_r))
    right = (math.cos(yaw_r), 0.0, math.sin(yaw_r))

    speed = 5.0
    x, y, z = scene.camera.position

    if scene.key_down(config.KEY_W):
        x += forward[0] * speed * dt
        z += forward[2] * speed * dt
    if scene.key_down(config.KEY_S):
        x -= forward[0] * speed * dt
        z -= forward[2] * speed * dt
    if scene.key_down(config.KEY_D):
        x += right[0] * speed * dt
        z += right[2] * speed * dt
    if scene.key_down(config.KEY_A):
        x -= right[0] * speed * dt
        z -= right[2] * speed * dt

    scene.camera.position = (x, y, z)


scene.on_update(update)
scene.run(title="Simple - Fly Camera (WASD + RMB look)")

