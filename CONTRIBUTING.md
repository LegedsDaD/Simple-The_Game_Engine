# Contributing

## Dev setup

Requirements:

- Python 3.9+
- CMake 3.20+
- A C++17 compiler

Install editable:

```bash
python -m pip install -U pip
python -m pip install -e .
```

## Building (Windows + MSYS2 MinGW)

```powershell
$env:CMAKE_GENERATOR = "MinGW Makefiles"
python -m pip install -e . --force-reinstall
```

## Running examples

```bash
python examples/rotating_cube.py
python examples/cube_arena_hud.py
```

## Style

- Keep the Python API beginner-friendly and stable.
- Keep the C++ core small and modular.
- Prefer additions that come with an example and docs update.

