from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import threading
from dataclasses import dataclass
from pathlib import Path
from tkinter import BOTH, END, LEFT, RIGHT, TOP, BOTTOM, X, Y, filedialog, messagebox, simpledialog, ttk
import tkinter as tk


@dataclass
class Project:
    root: Path

    @property
    def blueprint_path(self) -> Path:
        return self.root / "scene.simple.json"

    @property
    def assets_dir(self) -> Path:
        return self.root / "assets"


class EditorSettings:
    def __init__(self):
        self.path = Path.home() / ".simple_editor" / "settings.json"
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.data = {
            "recent_projects": [],
            "auto_reload": True,
            "default_projects_dir": str(Path.home() / "SimpleProjects"),
        }
        self.load()

    def load(self) -> None:
        try:
            if self.path.exists():
                self.data.update(json.loads(self.path.read_text(encoding="utf-8")))
        except Exception:
            pass

    def save(self) -> None:
        try:
            self.path.write_text(json.dumps(self.data, indent=2), encoding="utf-8")
        except Exception:
            pass

class GameRunner:
    def __init__(self, log_fn):
        self._proc: subprocess.Popen[str] | None = None
        self._log_fn = log_fn

    def running(self) -> bool:
        return self._proc is not None and self._proc.poll() is None

    def stop(self) -> None:
        if not self._proc:
            return
        try:
            self._proc.terminate()
        except Exception:
            pass
        self._proc = None

    def run(self, project_dir: Path) -> None:
        if self.running():
            self.stop()

        cmd = [sys.executable, "-m", "simple.editor.runtime", str(project_dir)]
        self._log_fn(f"$ {' '.join(cmd)}\n")
        self._proc = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            cwd=str(project_dir),
        )

        def _pump() -> None:
            assert self._proc and self._proc.stdout
            for line in self._proc.stdout:
                self._log_fn(line)
            rc = self._proc.wait()
            self._log_fn(f"\n[Process exited: {rc}]\n")

        threading.Thread(target=_pump, daemon=True).start()


class SimpleEditor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Editor")
        self.geometry("1100x700")

        self.settings = EditorSettings()
        self.project: Project | None = None
        self.runner = GameRunner(self.append_log)
        self._watch_timer = None
        self._watch_mtimes: dict[Path, float] = {}
        self._auto_reload = tk.BooleanVar(value=bool(self.settings.data.get("auto_reload", True)))

        self._bp_data: dict = {"cubes": [], "lines": []}

        self._build_ui()
        self._bind_keys()

    def _build_ui(self) -> None:
        top = ttk.Frame(self)
        top.pack(side=TOP, fill=X)

        ttk.Button(top, text="New (.sim)", command=self.new_project).pack(side=LEFT, padx=4, pady=4)
        ttk.Button(top, text="Open (.sim)", command=self.open_project).pack(side=LEFT, padx=4, pady=4)

        ttk.Separator(top, orient="vertical").pack(side=LEFT, fill=Y, padx=8)

        ttk.Button(top, text="Play (Space)", command=self.play).pack(side=LEFT, padx=4, pady=4)
        ttk.Button(top, text="Stop (Esc)", command=self.stop).pack(side=LEFT, padx=4, pady=4)
        ttk.Checkbutton(top, text="Auto Reload", variable=self._auto_reload, command=self._persist_settings).pack(
            side=LEFT, padx=8
        )

        ttk.Separator(top, orient="vertical").pack(side=LEFT, fill=Y, padx=8)

        ttk.Label(top, text="Add:").pack(side=LEFT, padx=(6, 2))
        self.add_choice = ttk.Combobox(top, state="readonly", values=["Cube", "Line3D", "Wall (voxels)"])
        self.add_choice.set("Cube")
        self.add_choice.pack(side=LEFT, padx=4, pady=4)
        ttk.Button(top, text="Add", command=self.add_from_palette).pack(side=LEFT, padx=4, pady=4)
        ttk.Button(top, text="Delete (Del)", command=self.delete_selected).pack(side=LEFT, padx=4, pady=4)

        ttk.Separator(top, orient="vertical").pack(side=LEFT, fill=Y, padx=8)
        ttk.Button(top, text="Open Blueprint", command=self.open_blueprint).pack(side=LEFT, padx=4, pady=4)
        ttk.Button(top, text="Save (Ctrl+S)", command=self.save_blueprint).pack(side=LEFT, padx=4, pady=4)

        self.tabs = ttk.Notebook(self)
        self.tabs.pack(side=TOP, fill=BOTH, expand=True)

        self.tab_scene = ttk.Frame(self.tabs)
        self.tab_art = ttk.Frame(self.tabs)
        self.tab_settings = ttk.Frame(self.tabs)
        self.tabs.add(self.tab_scene, text="Scene")
        self.tabs.add(self.tab_art, text="Art (2D)")
        self.tabs.add(self.tab_settings, text="Settings")

        self._build_scene_tab(self.tab_scene)
        self._build_art_tab(self.tab_art)
        self._build_settings_tab(self.tab_settings)

        bottom = ttk.Frame(self)
        bottom.pack(side=BOTTOM, fill=X)
        self.status = ttk.Label(bottom, text="No project opened.")
        self.status.pack(side=LEFT, padx=6, pady=4)

    def _build_scene_tab(self, root: ttk.Frame) -> None:
        mid = ttk.PanedWindow(root, orient="horizontal")
        mid.pack(side=TOP, fill=BOTH, expand=True)

        left = ttk.Frame(mid)
        mid.add(left, weight=1)

        ttk.Label(left, text="Outliner").pack(side=TOP, anchor="w", padx=6, pady=(6, 2))
        self.outliner = tk.Listbox(left, height=14)
        self.outliner.pack(side=TOP, fill=X, padx=6)
        self.outliner.bind("<<ListboxSelect>>", lambda e: self.refresh_inspector())

        insp = ttk.LabelFrame(left, text="Inspector (selected)")
        insp.pack(side=TOP, fill=BOTH, expand=True, padx=6, pady=6)

        self.fields: dict[str, tk.Entry] = {}

        def add_field(row: int, label: str, key: str) -> None:
            ttk.Label(insp, text=label).grid(row=row, column=0, sticky="w", padx=6, pady=4)
            ent = ttk.Entry(insp)
            ent.grid(row=row, column=1, sticky="ew", padx=6, pady=4)
            self.fields[key] = ent

        insp.columnconfigure(1, weight=1)
        add_field(0, "Type", "type")
        add_field(1, "Name", "name")
        add_field(2, "Position/A (x,y,z)", "pos_a")
        add_field(3, "Rotation/B (x,y,z)", "rot_b")
        add_field(4, "Scale (x,y,z)", "scale")
        add_field(5, "Color (r,g,b)", "color")
        add_field(6, "Texture path", "texture")
        add_field(7, "Spin (x,y,z)", "spin")
        add_field(8, "Behaviors (JSON)", "behaviors")

        tools = ttk.Frame(insp)
        tools.grid(row=9, column=0, columnspan=2, sticky="ew", padx=6, pady=(2, 6))
        ttk.Button(
            tools, text="+ Bob", command=lambda: self.add_behavior({"type": "bob", "amplitude": 0.5, "frequency": 1.8})
        ).pack(side=LEFT)
        ttk.Button(
            tools,
            text="+ Orbit",
            command=lambda: self.add_behavior({"type": "orbit", "center": [0, 0, 0], "radius": 2.2, "speed_deg_s": 45}),
        ).pack(side=LEFT, padx=6)
        ttk.Button(tools, text="Clear Behaviors", command=self.clear_behaviors).pack(side=LEFT, padx=6)

        ttk.Button(insp, text="Apply (Enter)", command=self.apply_inspector).grid(
            row=10, column=0, columnspan=2, sticky="ew", padx=6, pady=8
        )

        right = ttk.Frame(mid)
        mid.add(right, weight=2)

        self.right_tabs = ttk.Notebook(right)
        self.right_tabs.pack(side=TOP, fill=BOTH, expand=True, padx=6, pady=6)

        tab_view = ttk.Frame(self.right_tabs)
        tab_project = ttk.Frame(self.right_tabs)
        tab_log = ttk.Frame(self.right_tabs)
        self.right_tabs.add(tab_view, text="Scene View")
        self.right_tabs.add(tab_project, text="Project")
        self.right_tabs.add(tab_log, text="Log")

        view_top = ttk.Frame(tab_view)
        view_top.pack(side=TOP, fill=X, padx=6, pady=6)
        ttk.Button(view_top, text="Snapshot (F5)", command=self.snapshot).pack(side=LEFT)
        ttk.Button(view_top, text="Open game.py", command=self.open_game_script).pack(side=LEFT, padx=6)
        ttk.Button(view_top, text="New game.py", command=self.create_game_script).pack(side=LEFT, padx=6)

        self.preview_label = ttk.Label(tab_view, text="No preview yet. Click Snapshot while game is running.")
        self.preview_label.pack(side=TOP, fill=BOTH, expand=True, padx=6, pady=6)
        self._preview_img = None

        proj_top = ttk.Frame(tab_project)
        proj_top.pack(side=TOP, fill=X, padx=6, pady=6)
        ttk.Label(proj_top, text="Search:").pack(side=LEFT)
        self.asset_search = ttk.Entry(proj_top)
        self.asset_search.pack(side=LEFT, fill=X, expand=True, padx=6)
        self.asset_search.bind("<KeyRelease>", lambda e: self.refresh_assets())
        ttk.Button(proj_top, text="Refresh", command=self.refresh_assets).pack(side=LEFT, padx=6)

        self.asset_list = tk.Listbox(tab_project, height=12)
        self.asset_list.pack(side=TOP, fill=BOTH, expand=True, padx=6, pady=(0, 6))
        self.asset_list.bind("<Double-Button-1>", lambda e: self.use_selected_asset())

        ttk.Label(
            tab_project,
            text="Filters: t:texture / t:script / t:blueprint. Double-click a texture to apply to selected cube.",
        ).pack(side=TOP, anchor="w", padx=6, pady=(0, 6))

        ttk.Label(tab_log, text="Output / Log").pack(side=TOP, anchor="w", padx=6, pady=(6, 2))
        self.log = tk.Text(tab_log, wrap="word")
        self.log.pack(side=TOP, fill=BOTH, expand=True, padx=6, pady=(0, 6))

    def _build_art_tab(self, root: ttk.Frame) -> None:
        # A tiny pixel-art tool that exports PPM for immediate in-engine use.
        top = ttk.Frame(root)
        top.pack(side=TOP, fill=X, padx=6, pady=6)

        ttk.Label(top, text="Sprite name:").pack(side=LEFT)
        self.sprite_name = ttk.Entry(top, width=24)
        self.sprite_name.insert(0, "sprite")
        self.sprite_name.pack(side=LEFT, padx=6)

        ttk.Label(top, text="Color (#RRGGBB):").pack(side=LEFT)
        self.sprite_color = ttk.Entry(top, width=12)
        self.sprite_color.insert(0, "#ffffff")
        self.sprite_color.pack(side=LEFT, padx=6)

        ttk.Button(top, text="Pen", command=lambda: self._set_art_tool("pen")).pack(side=LEFT, padx=4)
        ttk.Button(top, text="Eraser", command=lambda: self._set_art_tool("eraser")).pack(side=LEFT, padx=4)
        ttk.Button(top, text="Clear", command=self._art_clear).pack(side=LEFT, padx=4)
        ttk.Button(top, text="Save to Project", command=self._art_save).pack(side=LEFT, padx=8)

        self._art_tool = "pen"
        self._art_w = 32
        self._art_h = 32
        self._art_pix = [(0, 0, 0, 0)] * (self._art_w * self._art_h)  # RGBA
        self._cell = 16

        self.art_canvas = tk.Canvas(root, bg="#202226", width=self._art_w * self._cell, height=self._art_h * self._cell)
        self.art_canvas.pack(side=TOP, padx=6, pady=6)
        self.art_canvas.bind("<B1-Motion>", self._art_paint)
        self.art_canvas.bind("<Button-1>", self._art_paint)
        self._art_redraw()

        ttk.Label(root, text="Tip: save, then set a cube texture to assets/<name>.ppm in the Scene tab.").pack(
            side=TOP, anchor="w", padx=6, pady=(0, 6)
        )

    def _build_settings_tab(self, root: ttk.Frame) -> None:
        box = ttk.LabelFrame(root, text="Editor Settings")
        box.pack(side=TOP, fill=X, padx=8, pady=8)

        ttk.Label(box, text="Default projects directory").grid(row=0, column=0, sticky="w", padx=6, pady=6)
        self.projects_dir = ttk.Entry(box)
        self.projects_dir.grid(row=0, column=1, sticky="ew", padx=6, pady=6)
        self.projects_dir.insert(0, str(self.settings.data.get("default_projects_dir", "")))
        ttk.Button(box, text="Browse", command=self._browse_projects_dir).grid(row=0, column=2, padx=6, pady=6)

        box.columnconfigure(1, weight=1)

        ttk.Button(root, text="Save Settings", command=self._persist_settings).pack(side=TOP, anchor="w", padx=8, pady=6)

    def _browse_projects_dir(self) -> None:
        folder = filedialog.askdirectory(title="Select default projects directory")
        if not folder:
            return
        self.projects_dir.delete(0, END)
        self.projects_dir.insert(0, folder)

    # ---- logging ----
    def append_log(self, text: str) -> None:
        def _ui() -> None:
            self.log.insert(END, text)
            self.log.see(END)

        self.after(0, _ui)

    # ---- project actions ----
    def set_project(self, root: Path) -> None:
        self.project = Project(root=root)
        self.status.configure(text=f"Project: {root}")
        self.append_log(f"[Opened project] {root}\n")
        self.load_blueprint_into_ui()
        self.start_watch()
        self.refresh_assets()

        # update recent list
        rec = [p for p in self.settings.data.get("recent_projects", []) if p != str(root)]
        rec.insert(0, str(root))
        self.settings.data["recent_projects"] = rec[:12]
        self._persist_settings()

    def new_project(self) -> None:
        default_dir = Path(str(self.settings.data.get("default_projects_dir", str(Path.home() / "SimpleProjects"))))
        default_dir.mkdir(parents=True, exist_ok=True)
        parent = filedialog.askdirectory(title="Select parent folder for new .sim project", initialdir=str(default_dir))
        if not parent:
            return
        name = simpledialog.askstring("Project Name", "Enter project name (folder will be <name>.sim):")
        if not name:
            return
        root = Path(parent) / f"{name}.sim"
        root.mkdir(parents=True, exist_ok=True)
        (root / "assets").mkdir(parents=True, exist_ok=True)

        try:
            import importlib.resources as res

            template = res.files("simple").joinpath("templates").joinpath("basic_project").joinpath("scene.simple.json")
            shutil.copyfile(str(template), str(root / "scene.simple.json"))
        except Exception as e:
            messagebox.showerror("Template error", f"Failed to create blueprint template:\n{e}")
            return

        self.set_project(root)

    def open_project(self) -> None:
        folder = filedialog.askdirectory(title="Open .sim project folder (contains scene.simple.json)")
        if not folder:
            return
        root = Path(folder)
        if root.suffix.lower() != ".sim":
            messagebox.showerror("Not a .sim project", "Choose a folder ending in .sim")
            return
        if not (root / "scene.simple.json").exists():
            messagebox.showerror("Not a project", "Folder must contain scene.simple.json")
            return
        (root / "assets").mkdir(parents=True, exist_ok=True)
        self.set_project(root)

    # ---- play controls ----
    def play(self) -> None:
        if not self.project:
            messagebox.showinfo("No project", "Create or open a project first.")
            return
        self.save_blueprint()
        self.runner.run(self.project.root)

    def stop(self) -> None:
        self.runner.stop()

    # ---- file watch / hot reload ----
    def start_watch(self) -> None:
        self._watch_mtimes.clear()
        if not self.project:
            return
        self._watch_mtimes[self.project.blueprint_path] = self.project.blueprint_path.stat().st_mtime
        if self._watch_timer is not None:
            self.after_cancel(self._watch_timer)
        self._watch_timer = self.after(250, self._watch_tick)

    def _watch_tick(self) -> None:
        try:
            if self.project and self._auto_reload.get() and self.runner.running():
                p = self.project.blueprint_path
                mt = p.stat().st_mtime
                if mt != self._watch_mtimes.get(p):
                    self._watch_mtimes[p] = mt
                    self.append_log("[Auto Reload] blueprint changed, restarting...\n")
                    self.runner.run(self.project.root)
        except Exception:
            pass
        self._watch_timer = self.after(250, self._watch_tick)

    # ---- blueprint UI ----
    def open_blueprint(self) -> None:
        if not self.project:
            return
        os.startfile(self.project.blueprint_path)  # type: ignore[attr-defined]

    def load_blueprint_into_ui(self) -> None:
        if not self.project:
            return
        try:
            data = json.loads(self.project.blueprint_path.read_text(encoding="utf-8"))
            data.setdefault("cubes", [])
            data.setdefault("lines", [])
            for c in data.get("cubes", []):
                c.setdefault("behaviors", [])
            self._bp_data = data
            self._refresh_outliner()
        except Exception as e:
            messagebox.showerror("Blueprint error", str(e))

    def save_blueprint(self) -> None:
        if not self.project:
            return
        try:
            self.project.blueprint_path.write_text(json.dumps(self._bp_data, indent=2), encoding="utf-8")
        except Exception as e:
            messagebox.showerror("Save error", str(e))

    def refresh_inspector(self) -> None:
        if not self.project:
            return
        sel = self._selected_item()
        if sel is None:
            for ent in self.fields.values():
                ent.delete(0, END)
            return

        kind, idx = sel
        if kind == "cube":
            c = self._bp_data.get("cubes", [])[idx]
            self._set_field("type", "Cube")
            self._set_field("name", c.get("name", "Cube"))
            self._set_field("pos_a", self._fmt_tuple(c.get("position", (0, 0, 0))))
            self._set_field("rot_b", self._fmt_tuple(c.get("rotation", (0, 0, 0))))
            self._set_field("scale", self._fmt_tuple(c.get("scale", (1, 1, 1))))
            self._set_field("color", self._fmt_tuple(c.get("color", (1, 1, 1))))
            self._set_field("texture", str(c.get("texture", "")))
            self._set_field("spin", self._fmt_tuple(c.get("spin", (0, 45, 0))))
            self._set_field("behaviors", json.dumps(c.get("behaviors", [])))
        else:
            l = self._bp_data.get("lines", [])[idx]
            self._set_field("type", "Line3D")
            self._set_field("name", l.get("name", f"Line{idx}"))
            self._set_field("pos_a", self._fmt_tuple(l.get("a", (0, 0, 0))))
            self._set_field("rot_b", self._fmt_tuple(l.get("b", (0, 0, 0))))
            self._set_field("scale", "")
            self._set_field("texture", "")
            self._set_field("spin", "")
            self._set_field("color", self._fmt_tuple(l.get("color", (1, 1, 1))))
            self._set_field("behaviors", "[]")

    def apply_inspector(self) -> None:
        sel = self._selected_item()
        if sel is None:
            return
        kind, idx = sel
        if kind == "cube":
            cubes = self._bp_data.get("cubes", [])
            c = cubes[idx]
            c["name"] = self._get_field("name")
            c["position"] = self._parse_tuple(self._get_field("pos_a"))
            c["rotation"] = self._parse_tuple(self._get_field("rot_b"))
            c["scale"] = self._parse_tuple(self._get_field("scale"))
            c["color"] = self._parse_tuple(self._get_field("color"))
            c["texture"] = self._get_field("texture")
            c["spin"] = self._parse_tuple(self._get_field("spin"))
            try:
                beh = json.loads(self._get_field("behaviors") or "[]")
                c["behaviors"] = beh if isinstance(beh, list) else []
            except Exception:
                c["behaviors"] = []
        else:
            lines = self._bp_data.get("lines", [])
            l = lines[idx]
            l["name"] = self._get_field("name") or l.get("name", f"Line{idx}")
            l["a"] = self._parse_tuple(self._get_field("pos_a"))
            l["b"] = self._parse_tuple(self._get_field("rot_b"))
            l["color"] = self._parse_tuple(self._get_field("color"))

        self._refresh_outliner(keep_selection=True)

    def add_from_palette(self) -> None:
        choice = self.add_choice.get()
        if choice == "Cube":
            self._add_cube()
        elif choice == "Line3D":
            self._add_line()
        elif choice.startswith("Wall"):
            self._add_wall()
        self._refresh_outliner(keep_selection=False)

    def _add_cube(self) -> None:
        cubes = self._bp_data.setdefault("cubes", [])
        cubes.append(
            {
                "name": f"Cube{len(cubes)}",
                "position": [0.0, 0.0, 0.0],
                "rotation": [0.0, 0.0, 0.0],
                "scale": [1.0, 1.0, 1.0],
                "color": [0.2, 0.6, 1.0],
                "texture": "",
                "spin": [0.0, 45.0, 0.0],
                "behaviors": [],
            }
        )

    def _add_line(self) -> None:
        lines = self._bp_data.setdefault("lines", [])
        lines.append({"name": f"Line{len(lines)}", "a": [-1.0, 0.0, 0.0], "b": [1.0, 0.0, 0.0], "color": [1, 1, 1]})

    def _add_wall(self) -> None:
        cubes = self._bp_data.setdefault("cubes", [])
        base = len(cubes)
        # A small voxel wall generator (iconic for quick level blockouts).
        for y in range(0, 4):
            for x in range(0, 8):
                cubes.append(
                    {
                        "name": f"Wall{base + y*8 + x}",
                        "position": [x - 3.5, y - 0.5, -4.0],
                        "rotation": [0.0, 0.0, 0.0],
                        "scale": [0.95, 0.95, 0.95],
                        "color": [0.8, 0.8, 0.9],
                        "texture": "simple:checker.ppm",
                        "spin": [0.0, 0.0, 0.0],
                    }
                )

    def delete_selected(self) -> None:
        sel = self._selected_item()
        if sel is None:
            return
        kind, idx = sel
        if kind == "cube":
            self._bp_data.get("cubes", []).pop(idx)
        else:
            self._bp_data.get("lines", []).pop(idx)
        self._refresh_outliner(keep_selection=False)
        self.refresh_inspector()

    # ---- Project / Assets ----
    def refresh_assets(self) -> None:
        self.asset_list.delete(0, END)
        if not self.project:
            return

        q = self.asset_search.get().strip()
        type_filter = None
        terms: list[str] = []
        for token in q.split():
            if token.startswith("t:"):
                type_filter = token[2:].lower()
            else:
                terms.append(token.lower())

        def kind(p: Path) -> str:
            ext = p.suffix.lower()
            if ext == ".ppm":
                return "texture"
            if ext == ".py":
                return "script"
            if ext == ".json":
                return "blueprint"
            return "other"

        # Always include project blueprint + game.py.
        bp = self.project.blueprint_path
        if bp.exists() and (not type_filter or type_filter == "blueprint"):
            self.asset_list.insert(END, f"{'blueprint':8}  {'project':7}  {bp.name}")
        gp = self.project.root / "game.py"
        if gp.exists() and (not type_filter or type_filter == "script"):
            self.asset_list.insert(END, f"{'script':8}  {'project':7}  {gp.name}")

        # Project assets directory
        if self.project.assets_dir.exists():
            for p in sorted(self.project.assets_dir.glob("*")):
                if not p.is_file():
                    continue
                k = kind(p)
                if type_filter and k != type_filter:
                    continue
                name = p.name.lower()
                if any(t not in name for t in terms):
                    continue
                self.asset_list.insert(END, f"{k:8}  {'project':7}  {p.name}")

        # Core packaged assets (read-only)
        try:
            import importlib.resources as res

            core_assets = res.files("simple").joinpath("assets")
            for entry in sorted(core_assets.iterdir(), key=lambda e: e.name):
                if not entry.is_file():
                    continue
                p = Path(str(entry))
                k = kind(p)
                if type_filter and k != type_filter:
                    continue
                name = p.name.lower()
                if any(t not in name for t in terms):
                    continue
                self.asset_list.insert(END, f"{k:8}  {'core':7}  {p.name}")
        except Exception:
            pass

    def _asset_path_from_row(self, row: str) -> Path | None:
        if not self.project:
            return None
        parts = row.split()
        if len(parts) < 3:
            return None
        scope = parts[1]
        fname = parts[2]
        if fname == "scene.simple.json":
            return self.project.blueprint_path
        if scope == "project":
            if fname == "game.py":
                return self.project.root / "game.py"
            return self.project.assets_dir / fname
        # core
        try:
            import importlib.resources as res

            return Path(str(res.files("simple").joinpath("assets").joinpath(fname)))
        except Exception:
            return None

    def use_selected_asset(self) -> None:
        if not self.project:
            return
        sel = self.asset_list.curselection()
        if not sel:
            return
        row = self.asset_list.get(sel[0])
        p = self._asset_path_from_row(row)
        if not p:
            return

        if p.suffix.lower() in (".py", ".json"):
            try:
                os.startfile(p)  # type: ignore[attr-defined]
            except Exception:
                pass
            return

        # Texture: apply to selected cube.
        item = self._selected_item()
        if not item or item[0] != "cube":
            return

        rel = ""
        try:
            rel = str(p.relative_to(self.project.root)).replace("\\", "/")
        except Exception:
            if p.name == "checker.ppm":
                rel = "simple:checker.ppm"
            else:
                rel = str(p)

        self.fields["texture"].delete(0, END)
        self.fields["texture"].insert(0, rel)
        self.apply_inspector()
        self.append_log(f"[Applied texture] {rel}\n")

    # ---- Scene View snapshot (from running game) ----
    def snapshot(self) -> None:
        if not self.project:
            return
        ipc = self.project.root / ".simple_ipc"
        ipc.mkdir(parents=True, exist_ok=True)
        req = ipc / "screenshot.request"
        out = ipc / "screenshot.ppm"
        req.write_text("1", encoding="utf-8")
        self.append_log("[Snapshot requested]\n")

        def _poll() -> None:
            if out.exists():
                try:
                    img = tk.PhotoImage(file=str(out))
                    self._preview_img = img
                    self.preview_label.configure(image=img, text="")
                except Exception as e:
                    self.preview_label.configure(text=f"Failed to load preview: {e}")
                return
            self.after(150, _poll)

        self.after(150, _poll)

    # ---- Python scripting (project/game.py) ----
    def create_game_script(self) -> None:
        if not self.project:
            messagebox.showinfo("No project", "Create/open a .sim project first.")
            return
        p = self.project.root / "game.py"
        if p.exists():
            messagebox.showinfo("Exists", "game.py already exists.")
            return
        p.write_text(
            "from __future__ import annotations\n\n"
            "# Optional hooks used by Simple Editor runtime.\n"
            "# def start(scene, objects_by_name):\n"
            "# def update(scene, dt, objects_by_name):\n\n"
            "def start(scene, objects_by_name):\n"
            "    # Called once before the window opens.\n"
            "    pass\n\n"
            "def update(scene, dt, objects_by_name):\n"
            "    # Called every frame.\n"
            "    # Example: objects_by_name['Player'].rotation = (0, scene.time_seconds*60, 0)\n"
            "    pass\n",
            encoding="utf-8",
        )
        self.append_log(f"[Created] {p}\n")
        self.refresh_assets()
        self.open_game_script()

    def open_game_script(self) -> None:
        if not self.project:
            return
        p = self.project.root / "game.py"
        if not p.exists():
            messagebox.showinfo("Missing", "No game.py in this project. Click New game.py.")
            return
        try:
            os.startfile(p)  # type: ignore[attr-defined]
        except Exception:
            pass

    # ---- Behaviors ----
    def add_behavior(self, beh: dict) -> None:
        try:
            cur = json.loads(self._get_field("behaviors") or "[]")
            if not isinstance(cur, list):
                cur = []
        except Exception:
            cur = []
        cur.append(beh)
        self.fields["behaviors"].delete(0, END)
        self.fields["behaviors"].insert(0, json.dumps(cur))

    def clear_behaviors(self) -> None:
        self.fields["behaviors"].delete(0, END)
        self.fields["behaviors"].insert(0, "[]")

    def _refresh_outliner(self, keep_selection: bool = False) -> None:
        sel = self._selected_item() if keep_selection else None
        self.outliner.delete(0, END)
        for i, c in enumerate(self._bp_data.get("cubes", [])):
            self.outliner.insert(END, f"Cube  {i:03d}  {c.get('name','Cube')}")
        for i, l in enumerate(self._bp_data.get("lines", [])):
            self.outliner.insert(END, f"Line  {i:03d}  {l.get('name', f'Line{i}')}")
        if sel is not None:
            kind, idx = sel
            if kind == "cube":
                self.outliner.select_set(idx)
            else:
                base = len(self._bp_data.get("cubes", []))
                self.outliner.select_set(base + idx)
        elif self.outliner.size() > 0:
            self.outliner.select_set(0)
        self.refresh_inspector()

    # ---- helpers ----
    def _selected_item(self) -> tuple[str, int] | None:
        sel = self.outliner.curselection()
        if not sel:
            return None
        index = int(sel[0])
        cubes = self._bp_data.get("cubes", [])
        if index < len(cubes):
            return ("cube", index)
        return ("line", index - len(cubes))

    def _set_field(self, key: str, value: str) -> None:
        e = self.fields[key]
        e.delete(0, END)
        e.insert(0, value)

    def _get_field(self, key: str) -> str:
        return self.fields[key].get().strip()

    @staticmethod
    def _fmt_tuple(v) -> str:
        try:
            return ", ".join(f"{float(x):g}" for x in v)
        except Exception:
            return "0, 0, 0"

    @staticmethod
    def _parse_tuple(s: str):
        parts = [p.strip() for p in s.replace("(", "").replace(")", "").split(",") if p.strip()]
        if len(parts) != 3:
            return [0.0, 0.0, 0.0]
        try:
            return [float(parts[0]), float(parts[1]), float(parts[2])]
        except Exception:
            return [0.0, 0.0, 0.0]

    # ---- keybinds ----
    def _bind_keys(self) -> None:
        self.bind("<Control-n>", lambda e: self.new_project())
        self.bind("<Control-o>", lambda e: self.open_project())
        self.bind("<Control-s>", lambda e: self.save_blueprint())
        self.bind("<Delete>", lambda e: self.delete_selected())
        self.bind("<Return>", lambda e: self.apply_inspector())
        self.bind("<Escape>", lambda e: self.stop())
        self.bind("<space>", lambda e: self.play())
        self.bind("<F5>", lambda e: self.snapshot())

    def _persist_settings(self) -> None:
        self.settings.data["auto_reload"] = bool(self._auto_reload.get())
        self.settings.data["default_projects_dir"] = self.projects_dir.get().strip()
        self.settings.save()

    # ---- art tool ----
    def _set_art_tool(self, tool: str) -> None:
        self._art_tool = tool

    def _art_redraw(self) -> None:
        self.art_canvas.delete("all")
        for y in range(self._art_h):
            for x in range(self._art_w):
                r, g, b, a = self._art_pix[y * self._art_w + x]
                if a == 0:
                    fill = "#000000"
                else:
                    fill = f"#{r:02x}{g:02x}{b:02x}"
                x0 = x * self._cell
                y0 = y * self._cell
                self.art_canvas.create_rectangle(x0, y0, x0 + self._cell, y0 + self._cell, outline="#2b2d31", fill=fill)

    def _art_clear(self) -> None:
        self._art_pix = [(0, 0, 0, 0)] * (self._art_w * self._art_h)
        self._art_redraw()

    def _parse_hex(self, s: str) -> tuple[int, int, int]:
        s = s.strip()
        if s.startswith("#"):
            s = s[1:]
        if len(s) != 6:
            return (255, 255, 255)
        try:
            return (int(s[0:2], 16), int(s[2:4], 16), int(s[4:6], 16))
        except Exception:
            return (255, 255, 255)

    def _art_paint(self, evt) -> None:
        x = int(evt.x // self._cell)
        y = int(evt.y // self._cell)
        if x < 0 or y < 0 or x >= self._art_w or y >= self._art_h:
            return
        idx = y * self._art_w + x
        if self._art_tool == "eraser":
            self._art_pix[idx] = (0, 0, 0, 0)
        else:
            r, g, b = self._parse_hex(self.sprite_color.get())
            self._art_pix[idx] = (r, g, b, 255)
        self._art_redraw()

    def _art_save(self) -> None:
        if not self.project:
            messagebox.showinfo("No project", "Create/open a .sim project first.")
            return
        name = self.sprite_name.get().strip() or "sprite"
        out = self.project.assets_dir / f"{name}.ppm"
        out.parent.mkdir(parents=True, exist_ok=True)

        # Save as P3 PPM (alpha is composited onto black).
        w, h = self._art_w, self._art_h
        lines = ["P3", f"{w} {h}", "255"]
        for y in range(h):
            row = []
            for x in range(w):
                r, g, b, a = self._art_pix[y * w + x]
                if a == 0:
                    row += ["0", "0", "0"]
                else:
                    row += [str(r), str(g), str(b)]
            lines.append(" ".join(row))
        out.write_text("\n".join(lines) + "\n", encoding="ascii")
        self.append_log(f"[Saved sprite] {out}\n")
        messagebox.showinfo("Saved", f"Saved sprite texture:\n{out}\n\nUse it as: assets/{name}.ppm")


def main() -> None:
    app = SimpleEditor()
    app.mainloop()


if __name__ == "__main__":
    main()
