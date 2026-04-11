from simple import Scene, Cube, config


scene = Scene()

player = Cube()
player.color = (0.2, 0.9, 0.7)
player.spin = (0, 0, 0)
scene.add(player)

scene.camera.position = (0.0, 1.5, 6.0)
scene.camera.rotation = (-10.0, 0.0, 0.0)


def update(scene: Scene, dt: float) -> None:
    speed = 2.5
    x, y, z = player.position
    if scene.key_down(config.KEY_W):
        z -= speed * dt
    if scene.key_down(config.KEY_S):
        z += speed * dt
    if scene.key_down(config.KEY_A):
        x -= speed * dt
    if scene.key_down(config.KEY_D):
        x += speed * dt
    player.position = (x, y, z)

    # Hold right mouse to orbit camera yaw/pitch.
    if scene.mouse_down(config.MOUSE_RIGHT):
        dx, dy = scene.mouse_delta()
        pitch, yaw, roll = scene.camera.rotation
        yaw += dx * 0.15
        pitch += dy * 0.15
        pitch = max(-80.0, min(80.0, pitch))
        scene.camera.rotation = (pitch, yaw, roll)


scene.on_update(update)
scene.run(title="Simple - Basic Game (WASD + RMB look)")

