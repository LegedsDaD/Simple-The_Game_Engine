from __future__ import annotations

import io
import json
import os
import time
import zipfile
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import streamlit as st


APP_TITLE = "Simple Web Editor"
PROJECT_EXT = ".sim"
PROJECT_FILE = "project.json"
SCENE_FILE = "scene.json"


@dataclass
class Transform:
    position: Tuple[float, float, float] = (0.0, 0.0, 0.0)
    rotation: Tuple[float, float, float] = (0.0, 0.0, 0.0)
    scale: Tuple[float, float, float] = (1.0, 1.0, 1.0)


@dataclass
class Entity:
    id: str
    type: str = "Cube"
    name: str = "Cube"
    transform: Transform = field(default_factory=Transform)
    color: Tuple[float, float, float] = (0.9, 0.2, 0.2)
    texture_ppm: str = ""


@dataclass
class SceneDoc:
    background: Tuple[float, float, float] = (0.08, 0.09, 0.12)
    camera_pos: Tuple[float, float, float] = (0.0, 0.0, 3.5)
    camera_rot: Tuple[float, float, float] = (0.0, 0.0, 0.0)
    camera_fov: float = 60.0
    entities: List[Entity] = field(default_factory=list)


def _now_id() -> str:
    return f"e_{int(time.time() * 1000)}"


def _project_paths(project_dir: Path) -> Dict[str, Path]:
    return {
        "project": project_dir / PROJECT_FILE,
        "scene": project_dir / SCENE_FILE,
        "assets": project_dir / "assets",
        "scripts": project_dir / "scripts",
        "exports": project_dir / "exports",
    }


def _safe_read_json(path: Path) -> Optional[Dict[str, Any]]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None


def _write_json(path: Path, payload: Dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=False), encoding="utf-8")


def _scene_to_dict(scene: SceneDoc) -> Dict[str, Any]:
    payload = asdict(scene)
    payload["entities"] = []
    for e in scene.entities:
        d = asdict(e)
        d["transform"] = asdict(e.transform)
        payload["entities"].append(d)
    return payload


def _scene_from_dict(data: Dict[str, Any]) -> SceneDoc:
    scene = SceneDoc()
    scene.background = tuple(data.get("background", scene.background))  # type: ignore[assignment]
    scene.camera_pos = tuple(data.get("camera_pos", scene.camera_pos))  # type: ignore[assignment]
    scene.camera_rot = tuple(data.get("camera_rot", scene.camera_rot))  # type: ignore[assignment]
    scene.camera_fov = float(data.get("camera_fov", scene.camera_fov))
    ents = []
    for raw in data.get("entities", []):
        t_raw = raw.get("transform", {}) if isinstance(raw, dict) else {}
        t = Transform(
            position=tuple(t_raw.get("position", (0.0, 0.0, 0.0))),  # type: ignore[arg-type]
            rotation=tuple(t_raw.get("rotation", (0.0, 0.0, 0.0))),  # type: ignore[arg-type]
            scale=tuple(t_raw.get("scale", (1.0, 1.0, 1.0))),  # type: ignore[arg-type]
        )
        ent = Entity(
            id=str(raw.get("id", _now_id())),
            type=str(raw.get("type", "Cube")),
            name=str(raw.get("name", "Cube")),
            transform=t,
            color=tuple(raw.get("color", (0.9, 0.2, 0.2))),  # type: ignore[arg-type]
            texture_ppm=str(raw.get("texture_ppm", "")),
        )
        ents.append(ent)
    scene.entities = ents
    return scene


def create_project(project_dir: Path, project_name: str) -> None:
    project_dir.mkdir(parents=True, exist_ok=True)
    p = _project_paths(project_dir)
    p["assets"].mkdir(exist_ok=True)
    p["scripts"].mkdir(exist_ok=True)
    p["exports"].mkdir(exist_ok=True)

    if not p["project"].exists():
        _write_json(
            p["project"],
            {
                "name": project_name,
                "engine": "Simple",
                "format": 1,
            },
        )

    if not p["scene"].exists():
        scene = SceneDoc()
        scene.entities.append(Entity(id=_now_id(), type="Cube", name="Cube"))
        _write_json(p["scene"], _scene_to_dict(scene))

    # Helpful runner script.
    run_py = project_dir / "run.py"
    if not run_py.exists():
        run_py.write_text(
            "\n".join(
                [
                    "from __future__ import annotations",
                    "",
                    "import json",
                    "from pathlib import Path",
                    "",
                    "from simple import Scene, Cube",
                    "",
                    "ROOT = Path(__file__).resolve().parent",
                    "scene_doc = json.loads((ROOT / 'scene.json').read_text(encoding='utf-8'))",
                    "",
                    "scene = Scene()",
                    "scene.background_color = tuple(scene_doc.get('background', (0.08, 0.09, 0.12)))",
                    "",
                    "for e in scene_doc.get('entities', []):",
                    "    if e.get('type') != 'Cube':",
                    "        continue",
                    "    cube = Cube()",
                    "    cube.name = e.get('name', 'Cube')",
                    "    t = e.get('transform', {})",
                    "    cube.position = tuple(t.get('position', (0, 0, 0)))",
                    "    cube.rotation = tuple(t.get('rotation', (0, 0, 0)))",
                    "    cube.scale = tuple(t.get('scale', (1, 1, 1)))",
                    "    cube.color = tuple(e.get('color', (0.9, 0.2, 0.2)))",
                    "    tex = e.get('texture_ppm') or ''",
                    "    if tex:",
                    "        cube.texture = tex",
                    "    scene.add(cube)",
                    "",
                    "scene.run()",
                    "",
                ]
            ),
            encoding="utf-8",
        )


def zip_project(project_dir: Path) -> bytes:
    mem = io.BytesIO()
    with zipfile.ZipFile(mem, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for p in project_dir.rglob("*"):
            if p.is_dir():
                continue
            rel = p.relative_to(project_dir.parent)
            zf.write(p, rel.as_posix())
    return mem.getvalue()


def _vec3_inputs(label: str, value: Tuple[float, float, float], key: str, step: float = 0.1) -> Tuple[float, float, float]:
    c1, c2, c3 = st.columns(3)
    with c1:
        x = st.number_input(f"{label} X", value=float(value[0]), step=step, key=f"{key}_x")
    with c2:
        y = st.number_input(f"{label} Y", value=float(value[1]), step=step, key=f"{key}_y")
    with c3:
        z = st.number_input(f"{label} Z", value=float(value[2]), step=step, key=f"{key}_z")
    return (float(x), float(y), float(z))


def _color_inputs(label: str, value: Tuple[float, float, float], key: str) -> Tuple[float, float, float]:
    c1, c2, c3 = st.columns(3)
    with c1:
        r = st.slider(f"{label} R", 0.0, 1.0, float(value[0]), 0.01, key=f"{key}_r")
    with c2:
        g = st.slider(f"{label} G", 0.0, 1.0, float(value[1]), 0.01, key=f"{key}_g")
    with c3:
        b = st.slider(f"{label} B", 0.0, 1.0, float(value[2]), 0.01, key=f"{key}_b")
    return (float(r), float(g), float(b))


def main() -> None:
    st.set_page_config(page_title=APP_TITLE, layout="wide")
    st.title(APP_TITLE)
    st.caption("Build scenes in the browser, save as a `.sim` folder, then run with the Simple runtime.")

    if "project_dir" not in st.session_state:
        st.session_state.project_dir = ""
    if "scene" not in st.session_state:
        st.session_state.scene = SceneDoc()
    if "selected_entity_id" not in st.session_state:
        st.session_state.selected_entity_id = ""

    with st.sidebar:
        st.header("Project")
        base = st.text_input("Projects folder", value=str(Path.cwd()), help="Where `.sim` projects live.")
        name = st.text_input("Project name", value="MyGame")

        project_dir = Path(base).expanduser().resolve() / f"{name}{PROJECT_EXT}"
        st.text_input("Project path", value=str(project_dir), disabled=True)

        col_a, col_b = st.columns(2)
        with col_a:
            if st.button("Create / Open", use_container_width=True):
                create_project(project_dir, name)
                data = _safe_read_json(_project_paths(project_dir)["scene"])
                st.session_state.project_dir = str(project_dir)
                st.session_state.scene = _scene_from_dict(data or {})
                if st.session_state.scene.entities and not st.session_state.selected_entity_id:
                    st.session_state.selected_entity_id = st.session_state.scene.entities[0].id
        with col_b:
            if st.button("Save", use_container_width=True, disabled=not st.session_state.project_dir):
                pdir = Path(st.session_state.project_dir)
                _write_json(_project_paths(pdir)["scene"], _scene_to_dict(st.session_state.scene))
                st.toast("Saved scene.json")

        st.divider()
        st.subheader("Export")
        if st.session_state.project_dir:
            pdir = Path(st.session_state.project_dir)
            st.download_button(
                "Download project ZIP",
                data=zip_project(pdir),
                file_name=f"{pdir.name}.zip",
                use_container_width=True,
            )
        else:
            st.info("Create/Open a project to enable export.")

        st.divider()
        st.subheader("Run")
        st.code("python run.py", language="bash")
        st.caption("Run inside the `.sim` folder to play the scene using the native Simple runtime.")

    project_loaded = bool(st.session_state.project_dir)
    if not project_loaded:
        st.info("Create/Open a project from the sidebar to begin.")
        return

    scene: SceneDoc = st.session_state.scene

    tab_scene, tab_assets, tab_scripts = st.tabs(["Scene", "Assets", "Scripts"])

    with tab_scene:
        left, right = st.columns([0.35, 0.65], gap="large")

        with left:
            st.subheader("Hierarchy")
            types = ["Cube"]
            add_type = st.selectbox("Add object", types, index=0)
            if st.button("Add", use_container_width=True):
                ent = Entity(id=_now_id(), type=add_type, name=add_type)
                scene.entities.append(ent)
                st.session_state.selected_entity_id = ent.id

            if not scene.entities:
                st.caption("No objects in scene.")

            options = {f"{e.name}  ({e.type})": e.id for e in scene.entities}
            labels = list(options.keys())
            selected = st.selectbox(
                "Select",
                labels,
                index=max(0, labels.index(next((k for k, v in options.items() if v == st.session_state.selected_entity_id), labels[0]))),
            )
            st.session_state.selected_entity_id = options[selected]

            st.divider()
            st.subheader("Scene Settings")
            scene.background = _color_inputs("Background", scene.background, key="bg")
            scene.camera_pos = _vec3_inputs("Camera Pos", scene.camera_pos, key="cam_pos", step=0.1)
            scene.camera_rot = _vec3_inputs("Camera Rot (deg)", scene.camera_rot, key="cam_rot", step=1.0)
            scene.camera_fov = st.slider("Camera FOV", 30.0, 120.0, float(scene.camera_fov), 1.0)

        with right:
            st.subheader("Inspector")
            ent = next((e for e in scene.entities if e.id == st.session_state.selected_entity_id), None)
            if not ent:
                st.info("Select an object.")
            else:
                ent.name = st.text_input("Name", value=ent.name)
                ent.type = st.selectbox("Type", ["Cube"], index=0, disabled=True)
                ent.transform.position = _vec3_inputs("Position", ent.transform.position, key=f"{ent.id}_pos", step=0.1)
                ent.transform.rotation = _vec3_inputs("Rotation (deg)", ent.transform.rotation, key=f"{ent.id}_rot", step=1.0)
                ent.transform.scale = _vec3_inputs("Scale", ent.transform.scale, key=f"{ent.id}_scl", step=0.05)
                ent.color = _color_inputs("Color", ent.color, key=f"{ent.id}_col")
                ent.texture_ppm = st.text_input("Texture (.ppm path, optional)", value=ent.texture_ppm)

                col_del, col_dup = st.columns(2)
                with col_del:
                    if st.button("Delete", type="primary", use_container_width=True):
                        scene.entities = [e for e in scene.entities if e.id != ent.id]
                        st.session_state.selected_entity_id = scene.entities[0].id if scene.entities else ""
                        st.rerun()
                with col_dup:
                    if st.button("Duplicate", use_container_width=True):
                        dup = Entity(
                            id=_now_id(),
                            type=ent.type,
                            name=f"{ent.name} Copy",
                            transform=Transform(position=ent.transform.position, rotation=ent.transform.rotation, scale=ent.transform.scale),
                            color=ent.color,
                            texture_ppm=ent.texture_ppm,
                        )
                        scene.entities.append(dup)
                        st.session_state.selected_entity_id = dup.id
                        st.rerun()

            st.divider()
            st.subheader("Play")
            st.caption(
                "Streamlit can’t embed the native OpenGL runtime. Use the generated `run.py` inside your `.sim` folder to play."
            )

    with tab_assets:
        pdir = Path(st.session_state.project_dir)
        assets_dir = _project_paths(pdir)["assets"]
        st.subheader("Assets")
        st.caption("Drop `.ppm` textures into `assets/` and reference them by relative path in the Inspector.")
        st.code(str(assets_dir), language="text")
        files = sorted([p for p in assets_dir.rglob("*") if p.is_file()])
        if not files:
            st.info("No assets yet.")
        else:
            st.write("Files:")
            for p in files:
                st.text(p.relative_to(pdir).as_posix())

    with tab_scripts:
        pdir = Path(st.session_state.project_dir)
        scripts_dir = _project_paths(pdir)["scripts"]
        st.subheader("Scripts")
        st.caption("This is a lightweight project scripting area. You can import these scripts from `run.py`.")
        new_name = st.text_input("New script name", value="game.py")
        if st.button("Create script", use_container_width=False):
            target = scripts_dir / new_name
            if not target.suffix:
                target = target.with_suffix(".py")
            target.parent.mkdir(parents=True, exist_ok=True)
            if not target.exists():
                target.write_text(
                    "\n".join(
                        [
                            "from __future__ import annotations",
                            "",
                            "# Put your game logic here. Import it from run.py.",
                            "",
                        ]
                    ),
                    encoding="utf-8",
                )
                st.toast(f"Created {target.name}")
        files = sorted([p for p in scripts_dir.rglob("*.py") if p.is_file()])
        if not files:
            st.info("No scripts yet.")
        else:
            st.write("Scripts:")
            for p in files:
                st.text(p.relative_to(pdir).as_posix())


if __name__ == "__main__":
    # Streamlit runs this file via `streamlit run streamlit_app.py`.
    main()

