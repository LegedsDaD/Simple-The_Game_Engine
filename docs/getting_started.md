# Getting Started

## Requirements

- Python **3.9+**
- A C++17 toolchain
- CMake **3.20+**

Simple fetches dependencies during build:

- `pybind11` (bindings)
- `glfw` (windowing/input)

## Installation

From the project root (`simple/`):

```bash
python -m pip install -U pip
python -m pip install -e .
```

Install from PyPI:

```bash
python -m pip install simple-game-engine
```

This builds the C++ extension and installs the `simple` Python package.

## First program

Create `hello_simple.py`:

```python
from simple import Scene, Cube

scene = Scene()
cube = Cube()
scene.add(cube)
scene.run()
```

Run:

```bash
python hello_simple.py
```

You should see:

- A window with a lit, rotating cube
- A top-left overlay: `Made with Simple`
- Console output: `Running on Simple Engine`

Disable branding:

```python
scene.disable_branding()
```

## Running examples

```bash
python examples/rotating_cube.py
python examples/multi_object_scene.py
python examples/basic_game.py
```

## Run the editor

If installed from source:

```bash
simple-editor
```

The editor creates/open a project folder and lets you press **Play** to run it.

## Publishing (maintainers)

This repository is set up for PyPI **Trusted Publishing** from GitHub Actions.

1. On PyPI, add a Trusted Publisher for this repo/workflow: `.github/workflows/publish.yml`
2. Create a release tag:

```bash
git tag v0.1.1
git push origin v0.1.1
```

GitHub Actions will build wheels (Windows/macOS/Linux) and publish to PyPI.
