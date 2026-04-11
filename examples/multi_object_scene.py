from simple import Scene, Cube

scene = Scene()

colors = [
    (1.0, 0.3, 0.3),
    (0.3, 1.0, 0.3),
    (0.3, 0.6, 1.0),
    (1.0, 0.9, 0.3),
    (0.9, 0.3, 1.0),
]

for i, c in enumerate(colors):
    cube = Cube()
    cube.position = ((i - 2) * 1.2, 0.0, 0.0)
    cube.color = c
    cube.spin = (15 * (i + 1), 30 * (i + 1), 0)
    scene.add(cube)

scene.camera.position = (0.0, 1.2, 6.5)
scene.camera.rotation = (-10.0, 0.0, 0.0)
scene.run(title="Simple - Multi Object Scene")

