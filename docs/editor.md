# Simple Editor

Simple includes a lightweight **Python-made editor** that ships with the engine package.

The editor focuses on fast iteration for small games:

- Data-driven scene editing (`scene.simple.json`)
- Play the game immediately (Play-in-Editor launches the game window)
- Auto-reload on blueprint changes
- `.sim` project folders (self-contained)
- Built-in 2D pixel-art tool (exports textures you can use immediately)
- Object palette (Cube/Line + quick generators)
- Project window with search filters (`t:texture`, `t:script`, `t:blueprint`)
- Python game scripting (`game.py`) run by the editor runtime
- Scene View snapshot preview (F5) without embedding a 3D viewport

## Run the editor (from source install)

After installing the package:

```bash
simple-editor
```

## Project format

A Simple “project” is a folder ending with `.sim` containing:

- `scene.simple.json`
- `assets/` (textures you create in the editor)

The editor can create this file for you using the built-in template.

## Play-in-Editor

The editor runs your project using:

```bash
python -m simple.editor.runtime <project_dir>
```

This starts the engine window and renders the scene described by the blueprint.

## Texture paths

Blueprint textures support:

- Empty string: no texture (use `Cube.color`)
- `simple:<name>`: load a packaged asset from `simple/assets/`  
  Example: `simple:checker.ppm`
- Relative/absolute filesystem paths: loaded directly

## Keybinds

- `Ctrl+N`: New project
- `Ctrl+O`: Open project
- `Ctrl+S`: Save blueprint
- `Space`: Play
- `Esc`: Stop
- `Del`: Delete selected object
- `Enter`: Apply inspector changes
- `F5`: Snapshot (updates Scene View preview)

## Scene objects

- **Cube**: transform + color + optional `texture` + `spin`
- **Line3D**: debug/gizmo line (two endpoints + color)
- **Behaviors** (cube JSON field): `bob`, `orbit` (simple motion components)

## Art tab (2D)

The Art tab is a small pixel editor that saves `assets/<name>.ppm` into your `.sim` project.

Use the saved file as a cube texture by setting the cube `texture` to `assets/<name>.ppm`.
