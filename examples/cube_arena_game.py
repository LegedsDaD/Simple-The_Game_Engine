"""
Cube Arena (a small "real" game built with Simple)

Controls:
  - WASD: move
  - LMB: shoot
  - RMB + mouse: orbit camera
  - ESC: quit

Goal:
  Survive and score points by shooting incoming drones.
"""

from __future__ import annotations

import math
import random
from dataclasses import dataclass
from typing import List, Tuple

from simple import Cube, Scene, config


Vec3 = Tuple[float, float, float]


def v_add(a: Vec3, b: Vec3) -> Vec3:
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def v_sub(a: Vec3, b: Vec3) -> Vec3:
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def v_mul(a: Vec3, s: float) -> Vec3:
    return (a[0] * s, a[1] * s, a[2] * s)


def v_len(a: Vec3) -> float:
    return math.sqrt(a[0] * a[0] + a[1] * a[1] + a[2] * a[2])


def v_norm(a: Vec3) -> Vec3:
    l = v_len(a)
    if l < 1e-8:
        return (0.0, 0.0, 0.0)
    return (a[0] / l, a[1] / l, a[2] / l)


def clamp(x: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, x))


@dataclass
class Bullet:
    cube: Cube
    vel: Vec3
    life: float


@dataclass
class Drone:
    cube: Cube
    speed: float
    hp: int


scene = Scene()

# If you want to ship your own branding, disable engine overlay:
# scene.disable_branding()

# Camera: slightly top-down for readability; RMB lets the player orbit.
scene.camera.position = (0.0, 7.5, 10.5)
scene.camera.rotation = (-28.0, 0.0, 0.0)

# "Floor" tiles (purely visual; gives motion cues).
tiles: List[Cube] = []
for z in range(-6, 7):
    for x in range(-6, 7):
        t = Cube()
        t.scale = (0.48, 0.04, 0.48)
        t.spin = (0, 0, 0)
        t.position = (x * 1.05, -0.55, z * 1.05)
        # Checkerboard-ish palette
        if (x + z) % 2 == 0:
            t.color = (0.12, 0.12, 0.14)
        else:
            t.color = (0.08, 0.08, 0.10)
        scene.add(t)
        tiles.append(t)

# Player
player = Cube()
player.scale = (0.65, 0.65, 0.65)
player.color = (0.15, 0.95, 0.55)
player.spin = (0, 0, 0)
player.position = (0.0, 0.0, 0.0)
scene.add(player)

# Player state
player_hp = 5
score = 0

# Projectiles and enemies
bullets: List[Bullet] = []
drones: List[Drone] = []

# Arena
ARENA_R = 6.4

# Timers
time_s = 0.0
spawn_accum = 0.0
shoot_cooldown = 0.0


def spawn_drone() -> None:
    # Spawn on a ring around the arena.
    a = random.random() * math.tau
    r = ARENA_R + 1.2
    x = math.cos(a) * r
    z = math.sin(a) * r

    d = Cube()
    d.scale = (0.55, 0.55, 0.55)
    d.spin = (0, random.uniform(30, 120), 0)
    d.position = (x, 0.0, z)
    d.color = (0.95, 0.25, 0.25)
    scene.add(d)

    drones.append(
        Drone(
            cube=d,
            speed=random.uniform(1.1, 2.2),
            hp=2,
        )
    )


def shoot(from_pos: Vec3, dir_xz: Vec3) -> None:
    b = Cube()
    b.scale = (0.18, 0.18, 0.18)
    b.spin = (0, 0, 0)
    b.color = (1.0, 0.95, 0.4)
    b.position = (from_pos[0], 0.0, from_pos[2])
    scene.add(b)

    speed = 9.5
    vel = v_mul(v_norm(dir_xz), speed)
    bullets.append(Bullet(cube=b, vel=vel, life=1.6))


def remove_cube(c: Cube) -> None:
    scene.remove(c)


def end_game() -> None:
    # A minimal "game over": print and stop spawning/shooting by clearing update.
    print(f"Game Over! Score: {score}")
    scene.on_update(None)


def update(scene: Scene, dt: float) -> None:
    global time_s, spawn_accum, shoot_cooldown, score, player_hp

    time_s += dt
    spawn_accum += dt
    shoot_cooldown = max(0.0, shoot_cooldown - dt)

    # Orbit camera with RMB.
    if scene.mouse_down(config.MOUSE_RIGHT):
        dx, dy = scene.mouse_delta()
        pitch, yaw, roll = scene.camera.rotation
        yaw += dx * 0.15
        pitch += dy * 0.15
        pitch = clamp(pitch, -75.0, 10.0)
        scene.camera.rotation = (pitch, yaw, roll)

    # Player movement.
    speed = 4.2
    px, py, pz = player.position
    mx = 0.0
    mz = 0.0
    if scene.key_down(config.KEY_W):
        mz -= 1.0
    if scene.key_down(config.KEY_S):
        mz += 1.0
    if scene.key_down(config.KEY_A):
        mx -= 1.0
    if scene.key_down(config.KEY_D):
        mx += 1.0
    move = v_norm((mx, 0.0, mz))
    px += move[0] * speed * dt
    pz += move[2] * speed * dt

    # Keep the player inside the arena.
    r = math.sqrt(px * px + pz * pz)
    if r > ARENA_R:
        px, _, pz = v_mul(v_norm((px, 0.0, pz)), ARENA_R)
    player.position = (px, py, pz)

    # Aim direction: forward in camera yaw, so shooting stays intuitive while orbiting.
    pitch, yaw, _ = scene.camera.rotation
    yaw_r = math.radians(yaw)
    aim = (math.sin(yaw_r), 0.0, -math.cos(yaw_r))

    # Shooting.
    if scene.mouse_pressed(config.MOUSE_LEFT) and shoot_cooldown <= 0.0:
        shoot_cooldown = 0.12
        shoot((px, 0.0, pz), aim)

    # Difficulty curve: spawn faster over time (caps).
    spawn_interval = max(0.35, 1.1 - time_s * 0.03)
    while spawn_accum >= spawn_interval:
        spawn_accum -= spawn_interval
        spawn_drone()

    # Update bullets.
    i = 0
    while i < len(bullets):
        b = bullets[i]
        b.life -= dt
        bx, by, bz = b.cube.position
        bx += b.vel[0] * dt
        bz += b.vel[2] * dt
        b.cube.position = (bx, by, bz)

        # Despawn if out of bounds or expired.
        if b.life <= 0.0 or (bx * bx + bz * bz) > (ARENA_R + 4.0) ** 2:
            remove_cube(b.cube)
            bullets.pop(i)
            continue
        i += 1

    # Update drones + collisions.
    di = 0
    while di < len(drones):
        d = drones[di]
        dx, dy, dz = d.cube.position

        to_player = v_sub((px, 0.0, pz), (dx, 0.0, dz))
        dirp = v_norm(to_player)
        dx += dirp[0] * d.speed * dt
        dz += dirp[2] * d.speed * dt
        d.cube.position = (dx, dy, dz)

        # Drone hits player.
        if v_len((dx - px, 0.0, dz - pz)) < 0.55:
            player_hp -= 1
            remove_cube(d.cube)
            drones.pop(di)
            print(f"Hit! HP: {player_hp}  Score: {score}")
            if player_hp <= 0:
                end_game()
                return
            continue

        # Bullet hits drone.
        hit = False
        bi = 0
        while bi < len(bullets):
            b = bullets[bi]
            bx, _, bz = b.cube.position
            if v_len((dx - bx, 0.0, dz - bz)) < 0.45:
                hit = True
                remove_cube(b.cube)
                bullets.pop(bi)
                d.hp -= 1
                if d.hp <= 0:
                    score += 10
                    remove_cube(d.cube)
                    drones.pop(di)
                    print(f"+10  Score: {score}")
                break
            bi += 1

        if hit:
            continue

        di += 1


print("Cube Arena: WASD move, LMB shoot, RMB orbit camera, ESC quit")
scene.on_update(update)
scene.run(title="Simple - Cube Arena")

