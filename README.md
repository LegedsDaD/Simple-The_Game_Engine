# Simple

Simple is a small, production-oriented game/animation engine:

- **Python-first API** (`import simple`)
- **C++/OpenGL 3.3 core** for rendering + the main loop
- A lightweight **editor** for `.sim` projects with Play-in-Editor

## Quick start (10 lines)

```python
from simple import Scene, Cube

scene = Scene()
cube = Cube()
scene.add(cube)
scene.run()
```

## What you get

- Rendering: lit 3D cubes (Phong-ish directional light), optional textures (`.ppm`)
- Scene system: `Scene` + entities (`Cube`)
- Camera: view + perspective projection
- Input: keyboard + mouse (GLFW)
- HUD: `scene.draw_text(...)`
- Debug gizmos: `scene.draw_line3d(...)`
- Screenshots: `scene.screenshot("frame.ppm")`
- Editor: create/open `.sim` projects, edit objects, Play, Auto Reload

## Install

### Pip (end users)

```bash
python -m pip install simple-game-engine
```

### From source (contributors)

```bash
python -m pip install -U pip
python -m pip install -e .
```

## Simple Editor

Run:

```bash
simple-editor
```

Build a standalone editor executable:

```bash
python -m pip install .[editor]
python tools/build_editor.py
```

## Examples

Run any example:

```bash
python examples/cube_arena_hud.py
python examples/textured_cube.py
python examples/pro_debug_hud.py
```

## Documentation

- Engine docs: `docs/index.md`
- Editor docs: `docs/editor.md`

## Release (PyPI Trusted Publisher)

- Tag `vX.Y.Z` to publish wheels + sdist via GitHub Actions.
- Setup details: `docs/getting_started.md`
