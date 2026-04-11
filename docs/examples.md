# Examples

All examples are in `examples/`.

## 1) Rotating Cube

File: `examples/rotating_cube.py`

What it shows:

- Minimal scene setup
- A cube spinning using the built-in `spin` property

## 2) Multiple Objects

File: `examples/multi_object_scene.py`

What it shows:

- Multiple cubes in one scene
- Different colors and spin rates
- Adjusting camera position/rotation

## 3) Basic Interactive Scene

File: `examples/basic_game.py`

What it shows:

- Update callback via `scene.on_update(...)`
- Keyboard movement with `W/A/S/D`
- Mouse orbit camera (hold RMB and move)

## 4) Camera Orbit + Satellite

File: `examples/camera_orbit.py`

What it shows:

- Orbiting object logic in `on_update`
- RMB camera orbit controls

## 5) Procedural Grid Wave

File: `examples/grid_wave.py`

What it shows:

- Dozens of objects updated per-frame from Python
- Procedural animation + color mapping

## 6) Solar System

File: `examples/solar_system.py`

What it shows:

- Hierarchy-like motion (orbits) implemented at a high level
- Different angular velocities + sizes

## 7) Fly Camera

File: `examples/fly_camera.py`

What it shows:

- High-level camera controller (WASD + RMB look)
- A simple “world” of landmarks

## 8) Bouncing Cubes

File: `examples/bouncing_cubes.py`

What it shows:

- Many objects with per-object state (velocity)
- Simple collision with bounds

## 9) Color Pulse

File: `examples/color_pulse.py`

What it shows:

- Procedural material/color animation

## 10) Timeline Animation

File: `examples/timeline_animation.py`

What it shows:

- Cutscene-style keyframe/tween logic in pure Python
- Ease curves + staged animation

## 11) Cube Arena (Game)

File: `examples/cube_arena_game.py`

What it shows:

- A complete gameplay loop: spawn → chase → shoot → score → game over
- High-level game logic in `scene.on_update(...)` with per-entity state in Python
- Input-driven controls (WASD + mouse) and camera orbit

## 12) Textured Cube

File: `examples/textured_cube.py`

What it shows:

- Texture loading + sampling (PPM)
- Per-scene background color

## 13) Pro Debug HUD

File: `examples/pro_debug_hud.py`

What it shows:

- HUD text rendering (`scene.draw_text`)
- Frame timing (`scene.fps`, `scene.time_seconds`, `scene.frame_index`)

## 14) Pause + Step

File: `examples/pause_and_step.py`

What it shows:

- Pausing game logic
- Frame stepping (one-frame advance) for debugging

## 15) VSync Toggle + Dynamic Title

File: `examples/vsync_toggle.py`

What it shows:

- Runtime vsync switching (`scene.set_vsync`)
- Runtime title updates (`scene.set_title`)

## 16) Click Spawn (Textured)

File: `examples/click_spawn_textured.py`

What it shows:

- Input-driven spawning with a HUD counter
- Textured cubes using packaged assets (`config.asset_path`)

## 17) Cube Arena (HUD)

File: `examples/cube_arena_hud.py`

What it shows:

- Game + HUD overlay integrated (score/HP counters, instructions, FPS)
