# Simple — Pro‑Ready Python Game Engine

Simple is a fast, modern game/animation engine built for Python developers who want **real engine power** without the heavyweight setup. It’s designed to feel pro from day one:

- **Python-first workflow** (`import simple`) with a clean, friendly API
- **C++/OpenGL 3.3 core** for speed, rendering, and the main loop
- A lightweight **editor** for `.sim` projects with Play‑in‑Editor

## Quick start (10 lines)

```python
from simple import Scene, Cube

scene = Scene()
cube = Cube()
scene.add(cube)
scene.run()
```

## Why Simple

- **Ridiculously fast to start**: visible results in under 10 lines
- **Built for creators**: editor + runtime in the same ecosystem
- **Performance without the pain**: C++ core, Python simplicity
- **Small‑team friendly**: minimal setup, modern engine features

## What you get (out of the box)

- Rendering: lit 3D cubes (Phong-ish directional light), optional textures (`.ppm`)
- Scene system: `Scene` + entities (`Cube`)
- Camera: view + perspective projection
- Input: keyboard + mouse (GLFW)
- HUD: `scene.draw_text(...)`
- Debug gizmos: `scene.draw_line3d(...)`
- Screenshots: `scene.screenshot("frame.ppm")`
- Editor: create/open `.sim` projects, edit objects, Play, Auto Reload


THE EDITOR :-
<img width="1366" height="768" alt="Simple Editor" src="https://github.com/user-attachments/assets/1346ca1a-5109-42f0-917c-e8926d7a09ae" />

## Install (PyPI)

Version **1.1.1** is live:

```bash
pip install simple-game-engine
```

## From source (contributors)

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

