from simple import Scene, Cube, config

scene = Scene()
scene.background = (0.04, 0.04, 0.06)

cube = Cube()
cube.texture = config.asset_path("checker.ppm")  # PPM (P3/P6) texture
cube.spin = (15, 45, 0)
cube.position = (0, 0, 0)

scene.add(cube)
scene.run(title="Simple - Textured Cube")
