from simple import Scene, Cube

scene = Scene()

cube = Cube()
cube.position = (0, 0, 0)
cube.spin = (0, 60, 0)  # degrees/sec

scene.add(cube)
scene.run()

