# Architecture

Simple is split into two layers:

- **C++ core** (`cpp_core/`): windowing, OpenGL, input, entity/scene storage, engine loop
- **Python API** (`python_api/`): beginner-friendly wrappers around the core

The Python package is built from `python_api/` but installed as `simple/` inside the wheel.

## C++ Core Modules

- `window/`  
  GLFW window creation and context management.

- `input/`  
  GLFW callbacks -> per-frame state (down / pressed) for keys and mouse.

- `math/`  
  Minimal vector/matrix math used by transforms and camera projection.

- `scene/`  
  `Scene` owns entities. `Cube` is an `Entity` with transform + color + optional spin.

- `renderer/`  
  Minimal OpenGL 3.3 pipeline:
  - shader compilation
  - cube VAO/VBO
  - per-entity model matrix
  - camera view/projection
  - Phong-like lighting

- `branding/`  
  Generates a small triangle mesh for `Made with Simple` and draws it via a 2D UI shader.

- `bindings/`  
  `pybind11` module exposing `Scene`, `Cube`, `Transform`, input helpers, and `Camera`.

## Engine Flow

`Scene.run()` creates an `Engine`, which:

1. Creates a GLFW window and OpenGL context
2. Initializes input callbacks
3. Initializes the renderer + branding
4. Runs the game loop:
   - poll events
   - update entities
   - invoke optional Python callback
   - render scene
   - render debug lines + HUD overlay
   - render branding overlay (unless disabled)

## Tooling Layer

Simple also ships a small tooling layer in Python:

- `simple.tools.blueprint`: JSON “blueprint” format for data-driven scenes
- `simple.editor_runtime`: runs a blueprint-based project folder
- `simple.editor`: a lightweight editor UI to create/edit/play blueprints
