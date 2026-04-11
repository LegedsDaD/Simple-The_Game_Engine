# API Reference

This describes the user-facing Python API in the `simple` package.

## `Scene`

Create a new scene:

```python
from simple import Scene
scene = Scene()
```

### Methods

- `add(obj)`  
  Adds an entity to the scene. `obj` is typically a `Cube`.

- `remove(obj)`  
  Removes an entity.

- `clear()`  
  Removes all entities.

- `run(width=900, height=600, title="Simple")`  
  Starts the engine loop. The loop runs until the window closes or `ESC` is pressed.

- `disable_branding()`  
  Disables the on-screen `Made with Simple` overlay. (Console still prints at startup.)

- `background: (r, g, b)`  
  Scene clear color (0..1). Example:
  ```python
  scene.background = (0.04, 0.04, 0.06)
  ```

- `time_seconds` (read-only)  
  Total elapsed time while the scene is running.

- `fps` (read-only)  
  Smoothed frames-per-second estimate.

- `frame_index` (read-only)  
  Monotonic frame counter.

- `draw_text(text, x=10, y=10, size=1.0, color=(1,1,1))`  
  Draws HUD/debug text in screen-space pixels (top-left origin).

- `draw_line3d(a, b, color=(1,1,1))`  
  Draws a world-space debug line segment for the current frame (useful for gizmos).

- `set_title(title)`  
  Sets the window title (while running).

- `set_vsync(enabled)`  
  Enables/disables vsync (while running).

- `screenshot(path)`  
  Saves the next rendered frame as a binary PPM (P6).

- `on_update(fn)`  
  Registers an update callback. `fn(scene, dt)` is called every frame before rendering.

### Input

These methods are available while the scene is running:

- `key_down(key)` -> `bool`
- `key_pressed(key)` -> `bool`
- `mouse_down(button)` -> `bool`
- `mouse_pressed(button)` -> `bool`
- `mouse_position()` -> `(x, y)`
- `mouse_delta()` -> `(dx, dy)`

Use constants from `simple.config`.

## `Cube`

```python
from simple import Cube
cube = Cube()
```

### Properties

- `position: (x, y, z)`
- `rotation: (x, y, z)` (degrees)
- `scale: (x, y, z)`
- `color: (r, g, b)` (0..1)
- `spin: (x, y, z)` degrees per second (default rotates around Y)
- `texture: str` path to a `.ppm` texture (P3 or P6). Empty string disables texturing.

## `config`

- `asset_path(name)`  
  Returns an absolute path to a file inside the installed `simple/assets/` directory.

## `Camera`

Access via `scene.camera`.

### Properties

- `position: (x, y, z)`
- `rotation: (pitch, yaw, roll)` (degrees; roll unused right now)
- `fov` (degrees)
- `near`, `far`
