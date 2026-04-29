# Simple — Pro‑Ready Python Game Engine

<p align="center">
<img width="150" height="200" alt="Simple 2" src="https://github.com/user-attachments/assets/15d755da-73f1-447a-b3b0-eeeb670e3213" />
</p>

<div align="center">

<div style="display:flex;flex-wrap:wrap;gap:14px;justify-content:center;align-items:center">

<div style="border-radius:999px;overflow:hidden;box-shadow:0 8px 24px rgba(168,213,194,0.12),0 4px 8px rgba(0,0,0,0.5),inset 0 2px 3px rgba(0,0,0,0.5),inset 0 -1px 1px rgba(255,255,255,0.1)">
  <img src="https://img.shields.io/badge/SIMPLE-Game_Engine-A8D5C2?style=for-the-badge&labelColor=1A1A1A" alt="SIMPLE Game Engine">
</div>

<div style="border-radius:999px;overflow:hidden;box-shadow:0 8px 24px rgba(183,201,226,0.10),0 4px 8px rgba(0,0,0,0.5),inset 0 2px 3px rgba(0,0,0,0.5),inset 0 -1px 1px rgba(255,255,255,0.1)">
  <img src="https://img.shields.io/badge/Languages-Python_%26_C%2B%2B-B7C9E2?style=for-the-badge&logo=python&logoColor=F2D16B&labelColor=1A1A1A" alt="Languages">
</div>

<div style="border-radius:999px;overflow:hidden;box-shadow:0 8px 24px rgba(176,196,217,0.10),0 4px 8px rgba(0,0,0,0.5),inset 0 2px 3px rgba(0,0,0,0.5),inset 0 -1px 1px rgba(255,255,255,0.1)">
  <img src="https://img.shields.io/badge/BUILD_SYSTEM-CMake-B0C4D9?style=for-the-badge&logo=cmake&logoColor=white&labelColor=1A1A1A" alt="CMake">
</div>

<div style="border-radius:999px;overflow:hidden;box-shadow:0 8px 24px rgba(195,212,230,0.10),0 4px 8px rgba(0,0,0,0.5),inset 0 2px 3px rgba(0,0,0,0.5),inset 0 -1px 1px rgba(255,255,255,0.1)">
  <img src="https://img.shields.io/badge/RENDERING-OpenGL_3.3-C3D4E6?style=for-the-badge&logo=opengl&logoColor=white&labelColor=1A1A1A" alt="OpenGL 3.3">
</div>

<div style="border-radius:999px;overflow:hidden;box-shadow:0 8px 24px rgba(214,194,232,0.12),0 4px 8px rgba(0,0,0,0.5),inset 0 2px 3px rgba(0,0,0,0.5),inset 0 -1px 1px rgba(255,255,255,0.1)">
  <img src="https://img.shields.io/badge/FEATURE-Visual_Editor-D6C2E8?style=for-the-badge&labelColor=1A1A1A" alt="Visual Editor">
</div>

<div style="border-radius:999px;overflow:hidden;box-shadow:0 8px 24px rgba(175,196,214,0.10),0 4px 8px rgba(0,0,0,0.5),inset 0 2px 3px rgba(0,0,0,0.5),inset 0 -1px 1px rgba(255,255,255,0.1)">
  <img src="https://img.shields.io/badge/pip_install-simple--game--engine-AFC4D6?style=for-the-badge&logo=pypi&logoColor=F2D16B&labelColor=1A1A1A" alt="pip install">
</div>

</div>

[![PyPI Downloads](https://static.pepy.tech/personalized-badge/simple-game-engine?period=total&units=NONE&left_color=BLACK&right_color=GREEN&left_text=Downloads)](https://pepy.tech/projects/simple-game-engine)

</div>

## Goal - 100 stars for version `2.0.0` . Do star the project if tou like it .

Simple is a fast, modern game/animation engine built for Python developers who want **real engine power** without the heavyweight setup. It’s designed to feel pro from day one:

- **Python-first workflow** (`import simple`) with a clean, friendly API
- **C++/OpenGL 3.3 core** for speed, rendering, and the main loop
- A lightweight **editor** for `.sim` projects with Play‑in‑Editor

## To Download the Standalone Editor , Follow the given Steps :
**Step 1** Download the OS specific .zip Click your OS [Windows](https://github.com/LegedsDaD/Simple-The_Game_Engine/releases/download/v1.1.1/SimpleEditor-windows.zip) , [Linux](https://github.com/LegedsDaD/Simple-The_Game_Engine/releases/download/v1.1.1/SimpleEditor-linux.zip) , [Macos](https://github.com/LegedsDaD/Simple-The_Game_Engine/releases/download/v1.1.1/SimpleEditor-macos.zip) and you should see the .zip file getting downloaded .

**Step 2** Locate the .zip file.

**Step 3** Extract the .zip file and open it , You will see the Application, under the "Internal" Folder, Run it and the Editor is Ready. 

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

See [Documentation](https://github.com/LegedsDaD/Simple-The_Game_Engine/tree/main/docs) for more information of How to use.
