# Simple — Pro‑Ready Python Game Engine


## Note - Simple is not tested under other OS except Windows
<p align="center">
<img width="150" height="200" alt="Simple 2" src="https://github.com/user-attachments/assets/15d755da-73f1-447a-b3b0-eeeb670e3213" />
</p>

<div align="center">

<div style="display:flex;flex-wrap:wrap;gap:14px;justify-content:center;align-items:center">

<div style="border-radius:999px;overflow:hidden;box-shadow:0 8px 24px rgba(168,213,194,0.12),0 4px 8px rgba(0,0,0,0.5),inset 0 2px 3px rgba(0,0,0,0.5),inset 0 -1px 1px rgba(255,255,255,0.1)">
  <img src="https://img.shields.io/badge/SIMPLE-Game_Engine-A8D5C2?style=for-the-badge&labelColor=1A1A1A" alt="SIMPLE Game Engine">
</div>

<div style="border-radius:999px;overflow:hidden;box-shadow:0 8px 24px rgba(183,201,226,0.10),0 4px 8px rgba(0,0,0,0.5),inset 0 2px 3px rgba(0,0,0,0.5),inset 0 -1px 1px rgba(255,255,255,0.1)">
  <img src="https://img.shields.io/badge/Languages-Python_%26_C%2B%2B-B7C9E2?style=for-the-badge&logo=python&logoColor=F2D16B&labelColor=1A1A1A" alt="Languages">
</div>

<div style="border-radius:999px;overflow:hidden;box-shadow:0 8px 24px rgba(176,196,217,0.10),0 4px 8px rgba(0,0,0,0.5),inset 0 2px 3px rgba(0,0,0,0.5),inset 0 -1px 1px rgba(255,255,255,0.1)">
  <img src="https://img.shields.io/badge/BUILD_SYSTEM-CMake-B0C4D9?style=for-the-badge&logo=cmake&logoColor=white&labelColor=1A1A1A" alt="CMake">
</div>

<div style="border-radius:999px;overflow:hidden;box-shadow:0 8px 24px rgba(195,212,230,0.10),0 4px 8px rgba(0,0,0,0.5),inset 0 2px 3px rgba(0,0,0,0.5),inset 0 -1px 1px rgba(255,255,255,0.1)">
  <img src="https://img.shields.io/badge/RENDERING-OpenGL_3.3-C3D4E6?style=for-the-badge&logo=opengl&logoColor=white&labelColor=1A1A1A" alt="OpenGL 3.3">
</div>

<div style="border-radius:999px;overflow:hidden;box-shadow:0 8px 24px rgba(214,194,232,0.12),0 4px 8px rgba(0,0,0,0.5),inset 0 2px 3px rgba(0,0,0,0.5),inset 0 -1px 1px rgba(255,255,255,0.1)">
  <img src="https://img.shields.io/badge/FEATURE-Visual_Editor-D6C2E8?style=for-the-badge&labelColor=1A1A1A" alt="Visual Editor">
</div>

<div style="border-radius:999px;overflow:hidden;box-shadow:0 8px 24px rgba(175,196,214,0.10),0 4px 8px rgba(0,0,0,0.5),inset 0 2px 3px rgba(0,0,0,0.5),inset 0 -1px 1px rgba(255,255,255,0.1)">
  <img src="https://img.shields.io/badge/pip_install-simple--game--engine-AFC4D6?style=for-the-badge&logo=pypi&logoColor=F2D16B&labelColor=1A1A1A" alt="pip install">
</div>

</div>

[![PyPI Downloads](https://static.pepy.tech/personalized-badge/simple-game-engine?period=total&units=NONE&left_color=BLACK&right_color=GREEN&left_text=Downloads)](https://pepy.tech/projects/simple-game-engine)

[![RepoRanker](https://reporanker.com/badge/LegedsDaD/Simple-The_Game_Engine)](https://reporanker.com/repos/LegedsDaD/Simple-The_Game_Engine)

</div>


Simple is a fast, modern game/animation engine built for Python developers who want **real engine power** without the heavyweight setup. It’s designed to feel pro from day one:

- **Python-first workflow** (`import simple`) with a clean, friendly API
- **C++/OpenGL 3.3 core** for speed, rendering, and the main loop
- A lightweight **editor** for `.sim` projects with Play‑in‑Editor

## To Download the Standalone Editor , Follow the given Steps :
**Step 1** Download the OS specific .zip Click your OS [Windows](https://github.com/LegedsDaD/Simple-The_Game_Engine/releases/download/v1.1.1/SimpleEditor-windows.zip) , [Linux](https://github.com/LegedsDaD/Simple-The_Game_Engine/releases/download/v1.1.1/SimpleEditor-linux.zip) , [Macos](https://github.com/LegedsDaD/Simple-The_Game_Engine/releases/download/v1.1.1/SimpleEditor-macos.zip) and you should see the .zip file getting downloaded .

**Step 2** Locate the .zip file.

**Step 3** Extract the .zip file and open it , You will see the Application, under the "Internal" Folder, Run it and the Editor is Ready. 

## Quick start (10 lines)

```python
from simple import Scene, Cube

scene = Scene()
cube = Cube()
scene.add(cube)
scene.run()
```

## Why Simple

- **Ridiculously fast to start**: visible results in under 10 lines
- **Built for creators**: editor + runtime in the same ecosystem
- **Performance without the pain**: C++ core, Python simplicity
- **Small‑team friendly**: minimal setup, modern engine features

## What you get (out of the box)

- Rendering: lit 3D cubes (Phong-ish directional light), optional textures (`.ppm`)
- Scene system: `Scene` + entities (`Cube`)
- Camera: view + perspective projection
- Input: keyboard + mouse (GLFW)
- HUD: `scene.draw_text(...)`
- Debug gizmos: `scene.draw_line3d(...)`
- Screenshots: `scene.screenshot("frame.ppm")`
- Editor: create/open `.sim` projects, edit objects, Play, Auto Reload


THE EDITOR :-
<img width="1366" height="768" alt="Simple Editor" src="https://github.com/user-attachments/assets/1346ca1a-5109-42f0-917c-e8926d7a09ae" />

## Install (PyPI)

Version **1.1.1** is live:

```bash
pip install simple-game-engine
```

## From source (contributors)

```bash
python -m pip install -U pip
python -m pip install -e .
```

## Simple Editor

Run:

```bash
simple-editor
```

Build a standalone editor executable:

```bash
python -m pip install .[editor]
python tools/build_editor.py
```

## Examples

Run any example:

```bash
python examples/cube_arena_hud.py
python examples/textured_cube.py
python examples/pro_debug_hud.py
```

## Documentation

See [Documentation](https://github.com/LegedsDaD/Simple-The_Game_Engine/tree/main/docs) for more information of How to use.

## Community Engagement 

So Star 🌟 the project if you like it .


## People who liked Simple

<!-- STARGAZERS:START -->

<div align="center">

# ✨ Stargazers

**A huge thank you to everyone supporting this project!**

<br />

<table>
  <tr>
    <td align="center">
      <h2>⭐ 135</h2>
      <sub>TOTAL STARGAZERS</sub>
    </td>
  </tr>
</table>

<br />

</div>

<table align="center" width="100%">
<tr>

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/AlexOesTech">
                <img
                  src="https://avatars.githubusercontent.com/u/257420406?v=4&s=120"
                  width="85"
                  height="85"
                  alt="AlexOesTech"
                />
                <br />
                <sub><b>@AlexOesTech</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/ChakraDev1999">
                <img
                  src="https://avatars.githubusercontent.com/u/257418439?v=4&s=120"
                  width="85"
                  height="85"
                  alt="ChakraDev1999"
                />
                <br />
                <sub><b>@ChakraDev1999</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/Unclerog">
                <img
                  src="https://avatars.githubusercontent.com/u/252560529?v=4&s=120"
                  width="85"
                  height="85"
                  alt="Unclerog"
                />
                <br />
                <sub><b>@Unclerog</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/EasierBot">
                <img
                  src="https://avatars.githubusercontent.com/u/269893018?v=4&s=120"
                  width="85"
                  height="85"
                  alt="EasierBot"
                />
                <br />
                <sub><b>@EasierBot</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/GoodPHP">
                <img
                  src="https://avatars.githubusercontent.com/u/22586552?v=4&s=120"
                  width="85"
                  height="85"
                  alt="GoodPHP"
                />
                <br />
                <sub><b>@GoodPHP</b></sub>
              </a>
            </td>
            
</tr>
<tr>

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/davishkar">
                <img
                  src="https://avatars.githubusercontent.com/u/138203333?v=4&s=120"
                  width="85"
                  height="85"
                  alt="davishkar"
                />
                <br />
                <sub><b>@davishkar</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/LegedsDaD">
                <img
                  src="https://avatars.githubusercontent.com/u/234332968?v=4&s=120"
                  width="85"
                  height="85"
                  alt="LegedsDaD"
                />
                <br />
                <sub><b>@LegedsDaD</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/bhavyakeerthi3">
                <img
                  src="https://avatars.githubusercontent.com/u/255680099?v=4&s=120"
                  width="85"
                  height="85"
                  alt="bhavyakeerthi3"
                />
                <br />
                <sub><b>@bhavyakeerthi3</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/rahuloraj">
                <img
                  src="https://avatars.githubusercontent.com/u/119727688?v=4&s=120"
                  width="85"
                  height="85"
                  alt="rahuloraj"
                />
                <br />
                <sub><b>@rahuloraj</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/pandasipra76-cell">
                <img
                  src="https://avatars.githubusercontent.com/u/259558725?v=4&s=120"
                  width="85"
                  height="85"
                  alt="pandasipra76-cell"
                />
                <br />
                <sub><b>@pandasipra76-cell</b></sub>
              </a>
            </td>
            
</tr>
<tr>

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/Raj-glitch-max">
                <img
                  src="https://avatars.githubusercontent.com/u/174995162?v=4&s=120"
                  width="85"
                  height="85"
                  alt="Raj-glitch-max"
                />
                <br />
                <sub><b>@Raj-glitch-max</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/Mutasem-mk4">
                <img
                  src="https://avatars.githubusercontent.com/u/140179052?v=4&s=120"
                  width="85"
                  height="85"
                  alt="Mutasem-mk4"
                />
                <br />
                <sub><b>@Mutasem-mk4</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/Gledson-z">
                <img
                  src="https://avatars.githubusercontent.com/u/201022241?v=4&s=120"
                  width="85"
                  height="85"
                  alt="Gledson-z"
                />
                <br />
                <sub><b>@Gledson-z</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/Fuckies">
                <img
                  src="https://avatars.githubusercontent.com/u/191494293?v=4&s=120"
                  width="85"
                  height="85"
                  alt="Fuckies"
                />
                <br />
                <sub><b>@Fuckies</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/Sahil-Mansuri-15">
                <img
                  src="https://avatars.githubusercontent.com/u/258580369?v=4&s=120"
                  width="85"
                  height="85"
                  alt="Sahil-Mansuri-15"
                />
                <br />
                <sub><b>@Sahil-Mansuri-15</b></sub>
              </a>
            </td>
            
</tr>
<tr>

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/L1nkinPark">
                <img
                  src="https://avatars.githubusercontent.com/u/175855131?v=4&s=120"
                  width="85"
                  height="85"
                  alt="L1nkinPark"
                />
                <br />
                <sub><b>@L1nkinPark</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/hitesh066">
                <img
                  src="https://avatars.githubusercontent.com/u/181207931?v=4&s=120"
                  width="85"
                  height="85"
                  alt="hitesh066"
                />
                <br />
                <sub><b>@hitesh066</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/ahyanistheEmty">
                <img
                  src="https://avatars.githubusercontent.com/u/156690076?v=4&s=120"
                  width="85"
                  height="85"
                  alt="ahyanistheEmty"
                />
                <br />
                <sub><b>@ahyanistheEmty</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/naksh-atra">
                <img
                  src="https://avatars.githubusercontent.com/u/96780417?v=4&s=120"
                  width="85"
                  height="85"
                  alt="naksh-atra"
                />
                <br />
                <sub><b>@naksh-atra</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/ShinnAsukha">
                <img
                  src="https://avatars.githubusercontent.com/u/50636585?v=4&s=120"
                  width="85"
                  height="85"
                  alt="ShinnAsukha"
                />
                <br />
                <sub><b>@ShinnAsukha</b></sub>
              </a>
            </td>
            
</tr>
<tr>

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/divyamprusty">
                <img
                  src="https://avatars.githubusercontent.com/u/83948597?v=4&s=120"
                  width="85"
                  height="85"
                  alt="divyamprusty"
                />
                <br />
                <sub><b>@divyamprusty</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/7se7en72025">
                <img
                  src="https://avatars.githubusercontent.com/u/218611947?v=4&s=120"
                  width="85"
                  height="85"
                  alt="7se7en72025"
                />
                <br />
                <sub><b>@7se7en72025</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/K-SuhasM">
                <img
                  src="https://avatars.githubusercontent.com/u/107295251?v=4&s=120"
                  width="85"
                  height="85"
                  alt="K-SuhasM"
                />
                <br />
                <sub><b>@K-SuhasM</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/data-probe-1">
                <img
                  src="https://avatars.githubusercontent.com/u/292077293?v=4&s=120"
                  width="85"
                  height="85"
                  alt="data-probe-1"
                />
                <br />
                <sub><b>@data-probe-1</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/Shrikant922">
                <img
                  src="https://avatars.githubusercontent.com/u/167732283?v=4&s=120"
                  width="85"
                  height="85"
                  alt="Shrikant922"
                />
                <br />
                <sub><b>@Shrikant922</b></sub>
              </a>
            </td>
            
</tr>
<tr>

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/awejofficial">
                <img
                  src="https://avatars.githubusercontent.com/u/108984247?v=4&s=120"
                  width="85"
                  height="85"
                  alt="awejofficial"
                />
                <br />
                <sub><b>@awejofficial</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/piracyiskey">
                <img
                  src="https://avatars.githubusercontent.com/u/164041972?v=4&s=120"
                  width="85"
                  height="85"
                  alt="piracyiskey"
                />
                <br />
                <sub><b>@piracyiskey</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/andrefetch">
                <img
                  src="https://avatars.githubusercontent.com/u/244600452?v=4&s=120"
                  width="85"
                  height="85"
                  alt="andrefetch"
                />
                <br />
                <sub><b>@andrefetch</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/yzsmp">
                <img
                  src="https://avatars.githubusercontent.com/u/290584450?v=4&s=120"
                  width="85"
                  height="85"
                  alt="yzsmp"
                />
                <br />
                <sub><b>@yzsmp</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/Piyush-Prasad-PP">
                <img
                  src="https://avatars.githubusercontent.com/u/91525106?v=4&s=120"
                  width="85"
                  height="85"
                  alt="Piyush-Prasad-PP"
                />
                <br />
                <sub><b>@Piyush-Prasad-PP</b></sub>
              </a>
            </td>
            
</tr>
<tr>

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/AMRITO-KUNDU">
                <img
                  src="https://avatars.githubusercontent.com/u/158552346?v=4&s=120"
                  width="85"
                  height="85"
                  alt="AMRITO-KUNDU"
                />
                <br />
                <sub><b>@AMRITO-KUNDU</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/ZlGChoin">
                <img
                  src="https://avatars.githubusercontent.com/u/153075948?v=4&s=120"
                  width="85"
                  height="85"
                  alt="ZlGChoin"
                />
                <br />
                <sub><b>@ZlGChoin</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/Manav-Arora4">
                <img
                  src="https://avatars.githubusercontent.com/u/170600156?v=4&s=120"
                  width="85"
                  height="85"
                  alt="Manav-Arora4"
                />
                <br />
                <sub><b>@Manav-Arora4</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/Code2With-Pratik">
                <img
                  src="https://avatars.githubusercontent.com/u/169572793?v=4&s=120"
                  width="85"
                  height="85"
                  alt="Code2With-Pratik"
                />
                <br />
                <sub><b>@Code2With-Pratik</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/pirmber">
                <img
                  src="https://avatars.githubusercontent.com/u/201049843?v=4&s=120"
                  width="85"
                  height="85"
                  alt="pirmber"
                />
                <br />
                <sub><b>@pirmber</b></sub>
              </a>
            </td>
            
</tr>
<tr>

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/fraisasghar">
                <img
                  src="https://avatars.githubusercontent.com/u/223228391?v=4&s=120"
                  width="85"
                  height="85"
                  alt="fraisasghar"
                />
                <br />
                <sub><b>@fraisasghar</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/shaaravraghu">
                <img
                  src="https://avatars.githubusercontent.com/u/195157135?v=4&s=120"
                  width="85"
                  height="85"
                  alt="shaaravraghu"
                />
                <br />
                <sub><b>@shaaravraghu</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/binitkafle">
                <img
                  src="https://avatars.githubusercontent.com/u/257916351?v=4&s=120"
                  width="85"
                  height="85"
                  alt="binitkafle"
                />
                <br />
                <sub><b>@binitkafle</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/callmevanshh">
                <img
                  src="https://avatars.githubusercontent.com/u/143322008?v=4&s=120"
                  width="85"
                  height="85"
                  alt="callmevanshh"
                />
                <br />
                <sub><b>@callmevanshh</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/Allwyy08">
                <img
                  src="https://avatars.githubusercontent.com/u/154124348?v=4&s=120"
                  width="85"
                  height="85"
                  alt="Allwyy08"
                />
                <br />
                <sub><b>@Allwyy08</b></sub>
              </a>
            </td>
            
</tr>
<tr>

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/mauriciospark">
                <img
                  src="https://avatars.githubusercontent.com/u/60632158?v=4&s=120"
                  width="85"
                  height="85"
                  alt="mauriciospark"
                />
                <br />
                <sub><b>@mauriciospark</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/Jinwookaisel">
                <img
                  src="https://avatars.githubusercontent.com/u/283231218?v=4&s=120"
                  width="85"
                  height="85"
                  alt="Jinwookaisel"
                />
                <br />
                <sub><b>@Jinwookaisel</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/clementbouni-arch">
                <img
                  src="https://avatars.githubusercontent.com/u/237706224?v=4&s=120"
                  width="85"
                  height="85"
                  alt="clementbouni-arch"
                />
                <br />
                <sub><b>@clementbouni-arch</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/kimchannchon">
                <img
                  src="https://avatars.githubusercontent.com/u/67007450?v=4&s=120"
                  width="85"
                  height="85"
                  alt="kimchannchon"
                />
                <br />
                <sub><b>@kimchannchon</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/bishal-og">
                <img
                  src="https://avatars.githubusercontent.com/u/336500620?v=4&s=120"
                  width="85"
                  height="85"
                  alt="bishal-og"
                />
                <br />
                <sub><b>@bishal-og</b></sub>
              </a>
            </td>
            
</tr>
<tr>

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/marlone-prog">
                <img
                  src="https://avatars.githubusercontent.com/u/345758342?v=4&s=120"
                  width="85"
                  height="85"
                  alt="marlone-prog"
                />
                <br />
                <sub><b>@marlone-prog</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/pranishkoirala90394">
                <img
                  src="https://avatars.githubusercontent.com/u/334437461?v=4&s=120"
                  width="85"
                  height="85"
                  alt="pranishkoirala90394"
                />
                <br />
                <sub><b>@pranishkoirala90394</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/fmoorenoo">
                <img
                  src="https://avatars.githubusercontent.com/u/151165920?v=4&s=120"
                  width="85"
                  height="85"
                  alt="fmoorenoo"
                />
                <br />
                <sub><b>@fmoorenoo</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/leduc121">
                <img
                  src="https://avatars.githubusercontent.com/u/143080413?v=4&s=120"
                  width="85"
                  height="85"
                  alt="leduc121"
                />
                <br />
                <sub><b>@leduc121</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/abhigyan6">
                <img
                  src="https://avatars.githubusercontent.com/u/84132249?v=4&s=120"
                  width="85"
                  height="85"
                  alt="abhigyan6"
                />
                <br />
                <sub><b>@abhigyan6</b></sub>
              </a>
            </td>
            
</tr>
<tr>

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/Raph049">
                <img
                  src="https://avatars.githubusercontent.com/u/130841437?v=4&s=120"
                  width="85"
                  height="85"
                  alt="Raph049"
                />
                <br />
                <sub><b>@Raph049</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/SriramBharath-7">
                <img
                  src="https://avatars.githubusercontent.com/u/213016158?v=4&s=120"
                  width="85"
                  height="85"
                  alt="SriramBharath-7"
                />
                <br />
                <sub><b>@SriramBharath-7</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/codeby-Vishwajeet">
                <img
                  src="https://avatars.githubusercontent.com/u/280482873?v=4&s=120"
                  width="85"
                  height="85"
                  alt="codeby-Vishwajeet"
                />
                <br />
                <sub><b>@codeby-Vishwajeet</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/Abishek0070">
                <img
                  src="https://avatars.githubusercontent.com/u/221973912?v=4&s=120"
                  width="85"
                  height="85"
                  alt="Abishek0070"
                />
                <br />
                <sub><b>@Abishek0070</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/jy7lsna">
                <img
                  src="https://avatars.githubusercontent.com/u/121849188?v=4&s=120"
                  width="85"
                  height="85"
                  alt="jy7lsna"
                />
                <br />
                <sub><b>@jy7lsna</b></sub>
              </a>
            </td>
            
</tr>
<tr>

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/Prajyot-Desai">
                <img
                  src="https://avatars.githubusercontent.com/u/181592667?v=4&s=120"
                  width="85"
                  height="85"
                  alt="Prajyot-Desai"
                />
                <br />
                <sub><b>@Prajyot-Desai</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/samertall">
                <img
                  src="https://avatars.githubusercontent.com/u/52387110?v=4&s=120"
                  width="85"
                  height="85"
                  alt="samertall"
                />
                <br />
                <sub><b>@samertall</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/joao-g">
                <img
                  src="https://avatars.githubusercontent.com/u/253616805?v=4&s=120"
                  width="85"
                  height="85"
                  alt="joao-g"
                />
                <br />
                <sub><b>@joao-g</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/ryugacodesgit">
                <img
                  src="https://avatars.githubusercontent.com/u/349170142?v=4&s=120"
                  width="85"
                  height="85"
                  alt="ryugacodesgit"
                />
                <br />
                <sub><b>@ryugacodesgit</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/anshk1234">
                <img
                  src="https://avatars.githubusercontent.com/u/160382375?v=4&s=120"
                  width="85"
                  height="85"
                  alt="anshk1234"
                />
                <br />
                <sub><b>@anshk1234</b></sub>
              </a>
            </td>
            
</tr>
<tr>

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/darshanworkplace30">
                <img
                  src="https://avatars.githubusercontent.com/u/296192757?v=4&s=120"
                  width="85"
                  height="85"
                  alt="darshanworkplace30"
                />
                <br />
                <sub><b>@darshanworkplace30</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/Kukzze">
                <img
                  src="https://avatars.githubusercontent.com/u/91667682?v=4&s=120"
                  width="85"
                  height="85"
                  alt="Kukzze"
                />
                <br />
                <sub><b>@Kukzze</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/Juan-Miguel-alvarado">
                <img
                  src="https://avatars.githubusercontent.com/u/109107814?v=4&s=120"
                  width="85"
                  height="85"
                  alt="Juan-Miguel-alvarado"
                />
                <br />
                <sub><b>@Juan-Miguel-alvarado</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/donaldraph">
                <img
                  src="https://avatars.githubusercontent.com/u/62525712?v=4&s=120"
                  width="85"
                  height="85"
                  alt="donaldraph"
                />
                <br />
                <sub><b>@donaldraph</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/Rosy-Dev">
                <img
                  src="https://avatars.githubusercontent.com/u/258010841?v=4&s=120"
                  width="85"
                  height="85"
                  alt="Rosy-Dev"
                />
                <br />
                <sub><b>@Rosy-Dev</b></sub>
              </a>
            </td>
            
</tr>
<tr>

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/khalidabdifetah9">
                <img
                  src="https://avatars.githubusercontent.com/u/312366118?v=4&s=120"
                  width="85"
                  height="85"
                  alt="khalidabdifetah9"
                />
                <br />
                <sub><b>@khalidabdifetah9</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/NathanX23">
                <img
                  src="https://avatars.githubusercontent.com/u/201589790?v=4&s=120"
                  width="85"
                  height="85"
                  alt="NathanX23"
                />
                <br />
                <sub><b>@NathanX23</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/ineedfoundmyway">
                <img
                  src="https://avatars.githubusercontent.com/u/329826984?v=4&s=120"
                  width="85"
                  height="85"
                  alt="ineedfoundmyway"
                />
                <br />
                <sub><b>@ineedfoundmyway</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/gotkunal15">
                <img
                  src="https://avatars.githubusercontent.com/u/311084442?v=4&s=120"
                  width="85"
                  height="85"
                  alt="gotkunal15"
                />
                <br />
                <sub><b>@gotkunal15</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/petrosalex">
                <img
                  src="https://avatars.githubusercontent.com/u/19343014?v=4&s=120"
                  width="85"
                  height="85"
                  alt="petrosalex"
                />
                <br />
                <sub><b>@petrosalex</b></sub>
              </a>
            </td>
            
</tr>
<tr>

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/BhuwanJoshi-01">
                <img
                  src="https://avatars.githubusercontent.com/u/109661126?v=4&s=120"
                  width="85"
                  height="85"
                  alt="BhuwanJoshi-01"
                />
                <br />
                <sub><b>@BhuwanJoshi-01</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/Berserk-hub150">
                <img
                  src="https://avatars.githubusercontent.com/u/89993099?v=4&s=120"
                  width="85"
                  height="85"
                  alt="Berserk-hub150"
                />
                <br />
                <sub><b>@Berserk-hub150</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/ADITYA-KUMAR-2358">
                <img
                  src="https://avatars.githubusercontent.com/u/131487393?v=4&s=120"
                  width="85"
                  height="85"
                  alt="ADITYA-KUMAR-2358"
                />
                <br />
                <sub><b>@ADITYA-KUMAR-2358</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/sahitya1903">
                <img
                  src="https://avatars.githubusercontent.com/u/83616018?v=4&s=120"
                  width="85"
                  height="85"
                  alt="sahitya1903"
                />
                <br />
                <sub><b>@sahitya1903</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/CacheClown">
                <img
                  src="https://avatars.githubusercontent.com/u/171366273?v=4&s=120"
                  width="85"
                  height="85"
                  alt="CacheClown"
                />
                <br />
                <sub><b>@CacheClown</b></sub>
              </a>
            </td>
            
</tr>
<tr>

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/nopedal">
                <img
                  src="https://avatars.githubusercontent.com/u/84512230?v=4&s=120"
                  width="85"
                  height="85"
                  alt="nopedal"
                />
                <br />
                <sub><b>@nopedal</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/ampratapsingh">
                <img
                  src="https://avatars.githubusercontent.com/u/179601648?v=4&s=120"
                  width="85"
                  height="85"
                  alt="ampratapsingh"
                />
                <br />
                <sub><b>@ampratapsingh</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/ozrd">
                <img
                  src="https://avatars.githubusercontent.com/u/272019955?v=4&s=120"
                  width="85"
                  height="85"
                  alt="ozrd"
                />
                <br />
                <sub><b>@ozrd</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/nerfsaksham">
                <img
                  src="https://avatars.githubusercontent.com/u/325280059?v=4&s=120"
                  width="85"
                  height="85"
                  alt="nerfsaksham"
                />
                <br />
                <sub><b>@nerfsaksham</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/Armen5570">
                <img
                  src="https://avatars.githubusercontent.com/u/286051936?v=4&s=120"
                  width="85"
                  height="85"
                  alt="Armen5570"
                />
                <br />
                <sub><b>@Armen5570</b></sub>
              </a>
            </td>
            
</tr>
<tr>

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/DMS-Menula">
                <img
                  src="https://avatars.githubusercontent.com/u/186381241?v=4&s=120"
                  width="85"
                  height="85"
                  alt="DMS-Menula"
                />
                <br />
                <sub><b>@DMS-Menula</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/mzainulabideendev">
                <img
                  src="https://avatars.githubusercontent.com/u/325703180?v=4&s=120"
                  width="85"
                  height="85"
                  alt="mzainulabideendev"
                />
                <br />
                <sub><b>@mzainulabideendev</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/sarbatra3">
                <img
                  src="https://avatars.githubusercontent.com/u/352874139?v=4&s=120"
                  width="85"
                  height="85"
                  alt="sarbatra3"
                />
                <br />
                <sub><b>@sarbatra3</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/infinityRazor3">
                <img
                  src="https://avatars.githubusercontent.com/u/351104737?v=4&s=120"
                  width="85"
                  height="85"
                  alt="infinityRazor3"
                />
                <br />
                <sub><b>@infinityRazor3</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/sarang-devb">
                <img
                  src="https://avatars.githubusercontent.com/u/353216818?v=4&s=120"
                  width="85"
                  height="85"
                  alt="sarang-devb"
                />
                <br />
                <sub><b>@sarang-devb</b></sub>
              </a>
            </td>
            
</tr>
<tr>

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/akash3893">
                <img
                  src="https://avatars.githubusercontent.com/u/353268786?v=4&s=120"
                  width="85"
                  height="85"
                  alt="akash3893"
                />
                <br />
                <sub><b>@akash3893</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/ldsh-weilinlai">
                <img
                  src="https://avatars.githubusercontent.com/u/323045087?v=4&s=120"
                  width="85"
                  height="85"
                  alt="ldsh-weilinlai"
                />
                <br />
                <sub><b>@ldsh-weilinlai</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/gogozza11">
                <img
                  src="https://avatars.githubusercontent.com/u/273905449?v=4&s=120"
                  width="85"
                  height="85"
                  alt="gogozza11"
                />
                <br />
                <sub><b>@gogozza11</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/armenhar636-source">
                <img
                  src="https://avatars.githubusercontent.com/u/343832237?v=4&s=120"
                  width="85"
                  height="85"
                  alt="armenhar636-source"
                />
                <br />
                <sub><b>@armenhar636-source</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/atjos">
                <img
                  src="https://avatars.githubusercontent.com/u/65507292?v=4&s=120"
                  width="85"
                  height="85"
                  alt="atjos"
                />
                <br />
                <sub><b>@atjos</b></sub>
              </a>
            </td>
            
</tr>
<tr>

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/doom-cli">
                <img
                  src="https://avatars.githubusercontent.com/u/266218443?v=4&s=120"
                  width="85"
                  height="85"
                  alt="doom-cli"
                />
                <br />
                <sub><b>@doom-cli</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/kdbewn23">
                <img
                  src="https://avatars.githubusercontent.com/u/353790502?v=4&s=120"
                  width="85"
                  height="85"
                  alt="kdbewn23"
                />
                <br />
                <sub><b>@kdbewn23</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/lovesmesjhy3">
                <img
                  src="https://avatars.githubusercontent.com/u/353794131?v=4&s=120"
                  width="85"
                  height="85"
                  alt="lovesmesjhy3"
                />
                <br />
                <sub><b>@lovesmesjhy3</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/kdgbh23">
                <img
                  src="https://avatars.githubusercontent.com/u/353797010?v=4&s=120"
                  width="85"
                  height="85"
                  alt="kdgbh23"
                />
                <br />
                <sub><b>@kdgbh23</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/lartesh2">
                <img
                  src="https://avatars.githubusercontent.com/u/353804809?v=4&s=120"
                  width="85"
                  height="85"
                  alt="lartesh2"
                />
                <br />
                <sub><b>@lartesh2</b></sub>
              </a>
            </td>
            
</tr>
<tr>

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/lowlifecodezero">
                <img
                  src="https://avatars.githubusercontent.com/u/353807470?v=4&s=120"
                  width="85"
                  height="85"
                  alt="lowlifecodezero"
                />
                <br />
                <sub><b>@lowlifecodezero</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/web3wizzz">
                <img
                  src="https://avatars.githubusercontent.com/u/236838012?v=4&s=120"
                  width="85"
                  height="85"
                  alt="web3wizzz"
                />
                <br />
                <sub><b>@web3wizzz</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/dr1node">
                <img
                  src="https://avatars.githubusercontent.com/u/235500152?v=4&s=120"
                  width="85"
                  height="85"
                  alt="dr1node"
                />
                <br />
                <sub><b>@dr1node</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/rrsd2769">
                <img
                  src="https://avatars.githubusercontent.com/u/174997233?v=4&s=120"
                  width="85"
                  height="85"
                  alt="rrsd2769"
                />
                <br />
                <sub><b>@rrsd2769</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/henry9438">
                <img
                  src="https://avatars.githubusercontent.com/u/353799493?v=4&s=120"
                  width="85"
                  height="85"
                  alt="henry9438"
                />
                <br />
                <sub><b>@henry9438</b></sub>
              </a>
            </td>
            
</tr>
<tr>

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/braachcc">
                <img
                  src="https://avatars.githubusercontent.com/u/353682133?v=4&s=120"
                  width="85"
                  height="85"
                  alt="braachcc"
                />
                <br />
                <sub><b>@braachcc</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/andriymelnyk1997">
                <img
                  src="https://avatars.githubusercontent.com/u/46633744?v=4&s=120"
                  width="85"
                  height="85"
                  alt="andriymelnyk1997"
                />
                <br />
                <sub><b>@andriymelnyk1997</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/Professor-101">
                <img
                  src="https://avatars.githubusercontent.com/u/277202135?v=4&s=120"
                  width="85"
                  height="85"
                  alt="Professor-101"
                />
                <br />
                <sub><b>@Professor-101</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/Aurokrishnaa">
                <img
                  src="https://avatars.githubusercontent.com/u/191313144?v=4&s=120"
                  width="85"
                  height="85"
                  alt="Aurokrishnaa"
                />
                <br />
                <sub><b>@Aurokrishnaa</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/YashasHK-06">
                <img
                  src="https://avatars.githubusercontent.com/u/197676148?v=4&s=120"
                  width="85"
                  height="85"
                  alt="YashasHK-06"
                />
                <br />
                <sub><b>@YashasHK-06</b></sub>
              </a>
            </td>
            
</tr>
<tr>

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/yueffhjg">
                <img
                  src="https://avatars.githubusercontent.com/u/352319362?v=4&s=120"
                  width="85"
                  height="85"
                  alt="yueffhjg"
                />
                <br />
                <sub><b>@yueffhjg</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/spideythedev">
                <img
                  src="https://avatars.githubusercontent.com/u/221688867?v=4&s=120"
                  width="85"
                  height="85"
                  alt="spideythedev"
                />
                <br />
                <sub><b>@spideythedev</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/leaderfrank">
                <img
                  src="https://avatars.githubusercontent.com/u/19779854?v=4&s=120"
                  width="85"
                  height="85"
                  alt="leaderfrank"
                />
                <br />
                <sub><b>@leaderfrank</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/navadeep0508">
                <img
                  src="https://avatars.githubusercontent.com/u/199091183?v=4&s=120"
                  width="85"
                  height="85"
                  alt="navadeep0508"
                />
                <br />
                <sub><b>@navadeep0508</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/punit2911">
                <img
                  src="https://avatars.githubusercontent.com/u/144655592?v=4&s=120"
                  width="85"
                  height="85"
                  alt="punit2911"
                />
                <br />
                <sub><b>@punit2911</b></sub>
              </a>
            </td>
            
</tr>
<tr>

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/pa-ulander">
                <img
                  src="https://avatars.githubusercontent.com/u/1719300?v=4&s=120"
                  width="85"
                  height="85"
                  alt="pa-ulander"
                />
                <br />
                <sub><b>@pa-ulander</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/abinasharma001">
                <img
                  src="https://avatars.githubusercontent.com/u/83633679?v=4&s=120"
                  width="85"
                  height="85"
                  alt="abinasharma001"
                />
                <br />
                <sub><b>@abinasharma001</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/vyasanbmathew2008">
                <img
                  src="https://avatars.githubusercontent.com/u/285423314?v=4&s=120"
                  width="85"
                  height="85"
                  alt="vyasanbmathew2008"
                />
                <br />
                <sub><b>@vyasanbmathew2008</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/jamiejustcodes">
                <img
                  src="https://avatars.githubusercontent.com/u/306206816?v=4&s=120"
                  width="85"
                  height="85"
                  alt="jamiejustcodes"
                />
                <br />
                <sub><b>@jamiejustcodes</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/rudra-xi">
                <img
                  src="https://avatars.githubusercontent.com/u/164514144?v=4&s=120"
                  width="85"
                  height="85"
                  alt="rudra-xi"
                />
                <br />
                <sub><b>@rudra-xi</b></sub>
              </a>
            </td>
            
</tr>
<tr>

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/ThomasWack">
                <img
                  src="https://avatars.githubusercontent.com/u/264466934?v=4&s=120"
                  width="85"
                  height="85"
                  alt="ThomasWack"
                />
                <br />
                <sub><b>@ThomasWack</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/iyawnnn">
                <img
                  src="https://avatars.githubusercontent.com/u/151660400?v=4&s=120"
                  width="85"
                  height="85"
                  alt="iyawnnn"
                />
                <br />
                <sub><b>@iyawnnn</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/senoritekoti">
                <img
                  src="https://avatars.githubusercontent.com/u/319553613?v=4&s=120"
                  width="85"
                  height="85"
                  alt="senoritekoti"
                />
                <br />
                <sub><b>@senoritekoti</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/swarn007-byte">
                <img
                  src="https://avatars.githubusercontent.com/u/235354922?v=4&s=120"
                  width="85"
                  height="85"
                  alt="swarn007-byte"
                />
                <br />
                <sub><b>@swarn007-byte</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/freeopensourcesorftwarelover">
                <img
                  src="https://avatars.githubusercontent.com/u/354397807?v=4&s=120"
                  width="85"
                  height="85"
                  alt="freeopensourcesorftwarelover"
                />
                <br />
                <sub><b>@freeopensourcesorftwarelover</b></sub>
              </a>
            </td>
            
</tr>
<tr>

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/Ilakkiyaa2k8">
                <img
                  src="https://avatars.githubusercontent.com/u/190212610?v=4&s=120"
                  width="85"
                  height="85"
                  alt="Ilakkiyaa2k8"
                />
                <br />
                <sub><b>@Ilakkiyaa2k8</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/kalidevali">
                <img
                  src="https://avatars.githubusercontent.com/u/332364003?v=4&s=120"
                  width="85"
                  height="85"
                  alt="kalidevali"
                />
                <br />
                <sub><b>@kalidevali</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/alexandereyyey-prog">
                <img
                  src="https://avatars.githubusercontent.com/u/295306620?v=4&s=120"
                  width="85"
                  height="85"
                  alt="alexandereyyey-prog"
                />
                <br />
                <sub><b>@alexandereyyey-prog</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/nothingcodex">
                <img
                  src="https://avatars.githubusercontent.com/u/357257574?v=4&s=120"
                  width="85"
                  height="85"
                  alt="nothingcodex"
                />
                <br />
                <sub><b>@nothingcodex</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/Dark-Brain07">
                <img
                  src="https://avatars.githubusercontent.com/u/85172976?v=4&s=120"
                  width="85"
                  height="85"
                  alt="Dark-Brain07"
                />
                <br />
                <sub><b>@Dark-Brain07</b></sub>
              </a>
            </td>
            
</tr>
<tr>

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/Calyxia">
                <img
                  src="https://avatars.githubusercontent.com/u/316318074?v=4&s=120"
                  width="85"
                  height="85"
                  alt="Calyxia"
                />
                <br />
                <sub><b>@Calyxia</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/ehsaanullah0">
                <img
                  src="https://avatars.githubusercontent.com/u/225146296?v=4&s=120"
                  width="85"
                  height="85"
                  alt="ehsaanullah0"
                />
                <br />
                <sub><b>@ehsaanullah0</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/ayxanuser123">
                <img
                  src="https://avatars.githubusercontent.com/u/358381657?v=4&s=120"
                  width="85"
                  height="85"
                  alt="ayxanuser123"
                />
                <br />
                <sub><b>@ayxanuser123</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/SpolyCode">
                <img
                  src="https://avatars.githubusercontent.com/u/171841122?v=4&s=120"
                  width="85"
                  height="85"
                  alt="SpolyCode"
                />
                <br />
                <sub><b>@SpolyCode</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/perashanid">
                <img
                  src="https://avatars.githubusercontent.com/u/155494150?v=4&s=120"
                  width="85"
                  height="85"
                  alt="perashanid"
                />
                <br />
                <sub><b>@perashanid</b></sub>
              </a>
            </td>
            
</tr>
<tr>

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/royalpriest">
                <img
                  src="https://avatars.githubusercontent.com/u/88779808?v=4&s=120"
                  width="85"
                  height="85"
                  alt="royalpriest"
                />
                <br />
                <sub><b>@royalpriest</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/MerrickHayes">
                <img
                  src="https://avatars.githubusercontent.com/u/174679699?v=4&s=120"
                  width="85"
                  height="85"
                  alt="MerrickHayes"
                />
                <br />
                <sub><b>@MerrickHayes</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/Grish2063">
                <img
                  src="https://avatars.githubusercontent.com/u/215848097?v=4&s=120"
                  width="85"
                  height="85"
                  alt="Grish2063"
                />
                <br />
                <sub><b>@Grish2063</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/JayNguyen0505-es">
                <img
                  src="https://avatars.githubusercontent.com/u/192913383?v=4&s=120"
                  width="85"
                  height="85"
                  alt="JayNguyen0505-es"
                />
                <br />
                <sub><b>@JayNguyen0505-es</b></sub>
              </a>
            </td>
            

            <td align="center" width="20%" valign="top">
              <a href="https://github.com/mudassiralladatkhan">
                <img
                  src="https://avatars.githubusercontent.com/u/208343323?v=4&s=120"
                  width="85"
                  height="85"
                  alt="mudassiralladatkhan"
                />
                <br />
                <sub><b>@mudassiralladatkhan</b></sub>
              </a>
            </td>
            
</tr>
</table>

<div align="center">

<br />

*Every star makes a difference. Thank you for being part of this journey!*

</div>

<!-- STARGAZERS:END -->

