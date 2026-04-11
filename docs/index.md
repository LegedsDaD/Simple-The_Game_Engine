# Simple Engine Documentation

Simple is a small but professional engine with a **Python API** and a **C++ core**.

## Overview

Simple focuses on:

- **Fast feedback:** open a window and render something immediately.
- **Low ceremony:** no manual shader compilation steps, no engine boilerplate in user code.
- **Performance where it matters:** update/render loop and rendering are in C++.
- **Extensibility:** add entities, add rendering features, and expose more systems via `pybind11`.

## Core Features

- OpenGL 3.3 core cube renderer with basic Phong lighting
- Scene graph (flat list of entities for now)
- `Cube` entity with transform + color + spin
- `Camera` with view + perspective projection
- Input (keyboard + mouse) via GLFW
- Branding overlay + console branding

## Philosophy

Simple isn’t trying to replace full engines. It aims to be:

- A clean foundation for small games, demos, and interactive animation
- A learning-friendly codebase with real architecture
- A base you can extend without rewriting everything

Next: `docs/getting_started.md`

## Editor

See `docs/editor.md`.
