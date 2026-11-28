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

Thanks to everyone supporting this project!

### ⭐ 142 Amazing Supporters

</div>

<table align="center" width="100%">
<tr>

<td align="center" width="20%">
  <a href="https://github.com/AlexOesTech">
    <img src="https://avatars.githubusercontent.com/u/257420406?v=4&size=120"
         width="90"
         height="90"
         alt="AlexOesTech" />
    <br/>
    <strong>@AlexOesTech</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/ChakraDev1999">
    <img src="https://avatars.githubusercontent.com/u/257418439?v=4&size=120"
         width="90"
         height="90"
         alt="ChakraDev1999" />
    <br/>
    <strong>@ChakraDev1999</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/Unclerog">
    <img src="https://avatars.githubusercontent.com/u/252560529?v=4&size=120"
         width="90"
         height="90"
         alt="Unclerog" />
    <br/>
    <strong>@Unclerog</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/EasierBot">
    <img src="https://avatars.githubusercontent.com/u/269893018?v=4&size=120"
         width="90"
         height="90"
         alt="EasierBot" />
    <br/>
    <strong>@EasierBot</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/GoodPHP">
    <img src="https://avatars.githubusercontent.com/u/22586552?v=4&size=120"
         width="90"
         height="90"
         alt="GoodPHP" />
    <br/>
    <strong>@GoodPHP</strong>
  </a>
</td>

</tr>
<tr>

<td align="center" width="20%">
  <a href="https://github.com/davishkar">
    <img src="https://avatars.githubusercontent.com/u/138203333?v=4&size=120"
         width="90"
         height="90"
         alt="davishkar" />
    <br/>
    <strong>@davishkar</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/LegedsDaD">
    <img src="https://avatars.githubusercontent.com/u/234332968?v=4&size=120"
         width="90"
         height="90"
         alt="LegedsDaD" />
    <br/>
    <strong>@LegedsDaD</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/bhavyakeerthi3">
    <img src="https://avatars.githubusercontent.com/u/255680099?v=4&size=120"
         width="90"
         height="90"
         alt="bhavyakeerthi3" />
    <br/>
    <strong>@bhavyakeerthi3</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/rahuloraj">
    <img src="https://avatars.githubusercontent.com/u/119727688?v=4&size=120"
         width="90"
         height="90"
         alt="rahuloraj" />
    <br/>
    <strong>@rahuloraj</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/pandasipra76-cell">
    <img src="https://avatars.githubusercontent.com/u/259558725?v=4&size=120"
         width="90"
         height="90"
         alt="pandasipra76-cell" />
    <br/>
    <strong>@pandasipra76-cell</strong>
  </a>
</td>

</tr>
<tr>

<td align="center" width="20%">
  <a href="https://github.com/Raj-glitch-max">
    <img src="https://avatars.githubusercontent.com/u/174995162?v=4&size=120"
         width="90"
         height="90"
         alt="Raj-glitch-max" />
    <br/>
    <strong>@Raj-glitch-max</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/Mutasem-mk4">
    <img src="https://avatars.githubusercontent.com/u/140179052?v=4&size=120"
         width="90"
         height="90"
         alt="Mutasem-mk4" />
    <br/>
    <strong>@Mutasem-mk4</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/Gledson-z">
    <img src="https://avatars.githubusercontent.com/u/201022241?v=4&size=120"
         width="90"
         height="90"
         alt="Gledson-z" />
    <br/>
    <strong>@Gledson-z</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/Fuckies">
    <img src="https://avatars.githubusercontent.com/u/191494293?v=4&size=120"
         width="90"
         height="90"
         alt="Fuckies" />
    <br/>
    <strong>@Fuckies</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/Sahil-Mansuri-15">
    <img src="https://avatars.githubusercontent.com/u/258580369?v=4&size=120"
         width="90"
         height="90"
         alt="Sahil-Mansuri-15" />
    <br/>
    <strong>@Sahil-Mansuri-15</strong>
  </a>
</td>

</tr>
<tr>

<td align="center" width="20%">
  <a href="https://github.com/L1nkinPark">
    <img src="https://avatars.githubusercontent.com/u/175855131?v=4&size=120"
         width="90"
         height="90"
         alt="L1nkinPark" />
    <br/>
    <strong>@L1nkinPark</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/hitesh066">
    <img src="https://avatars.githubusercontent.com/u/181207931?v=4&size=120"
         width="90"
         height="90"
         alt="hitesh066" />
    <br/>
    <strong>@hitesh066</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/ahyanistheEmty">
    <img src="https://avatars.githubusercontent.com/u/156690076?v=4&size=120"
         width="90"
         height="90"
         alt="ahyanistheEmty" />
    <br/>
    <strong>@ahyanistheEmty</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/naksh-atra">
    <img src="https://avatars.githubusercontent.com/u/96780417?v=4&size=120"
         width="90"
         height="90"
         alt="naksh-atra" />
    <br/>
    <strong>@naksh-atra</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/ShinnAsukha">
    <img src="https://avatars.githubusercontent.com/u/50636585?v=4&size=120"
         width="90"
         height="90"
         alt="ShinnAsukha" />
    <br/>
    <strong>@ShinnAsukha</strong>
  </a>
</td>

</tr>
<tr>

<td align="center" width="20%">
  <a href="https://github.com/divyamprusty">
    <img src="https://avatars.githubusercontent.com/u/83948597?v=4&size=120"
         width="90"
         height="90"
         alt="divyamprusty" />
    <br/>
    <strong>@divyamprusty</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/7se7en72025">
    <img src="https://avatars.githubusercontent.com/u/218611947?v=4&size=120"
         width="90"
         height="90"
         alt="7se7en72025" />
    <br/>
    <strong>@7se7en72025</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/K-SuhasM">
    <img src="https://avatars.githubusercontent.com/u/107295251?v=4&size=120"
         width="90"
         height="90"
         alt="K-SuhasM" />
    <br/>
    <strong>@K-SuhasM</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/data-probe-1">
    <img src="https://avatars.githubusercontent.com/u/292077293?v=4&size=120"
         width="90"
         height="90"
         alt="data-probe-1" />
    <br/>
    <strong>@data-probe-1</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/Shrikant922">
    <img src="https://avatars.githubusercontent.com/u/167732283?v=4&size=120"
         width="90"
         height="90"
         alt="Shrikant922" />
    <br/>
    <strong>@Shrikant922</strong>
  </a>
</td>

</tr>
<tr>

<td align="center" width="20%">
  <a href="https://github.com/awejofficial">
    <img src="https://avatars.githubusercontent.com/u/108984247?v=4&size=120"
         width="90"
         height="90"
         alt="awejofficial" />
    <br/>
    <strong>@awejofficial</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/piracyiskey">
    <img src="https://avatars.githubusercontent.com/u/164041972?v=4&size=120"
         width="90"
         height="90"
         alt="piracyiskey" />
    <br/>
    <strong>@piracyiskey</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/andrefetch">
    <img src="https://avatars.githubusercontent.com/u/244600452?v=4&size=120"
         width="90"
         height="90"
         alt="andrefetch" />
    <br/>
    <strong>@andrefetch</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/yzsmp">
    <img src="https://avatars.githubusercontent.com/u/290584450?v=4&size=120"
         width="90"
         height="90"
         alt="yzsmp" />
    <br/>
    <strong>@yzsmp</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/Piyush-Prasad-PP">
    <img src="https://avatars.githubusercontent.com/u/91525106?v=4&size=120"
         width="90"
         height="90"
         alt="Piyush-Prasad-PP" />
    <br/>
    <strong>@Piyush-Prasad-PP</strong>
  </a>
</td>

</tr>
<tr>

<td align="center" width="20%">
  <a href="https://github.com/AMRITO-KUNDU">
    <img src="https://avatars.githubusercontent.com/u/158552346?v=4&size=120"
         width="90"
         height="90"
         alt="AMRITO-KUNDU" />
    <br/>
    <strong>@AMRITO-KUNDU</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/ZlGChoin">
    <img src="https://avatars.githubusercontent.com/u/153075948?v=4&size=120"
         width="90"
         height="90"
         alt="ZlGChoin" />
    <br/>
    <strong>@ZlGChoin</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/Manav-Arora4">
    <img src="https://avatars.githubusercontent.com/u/170600156?v=4&size=120"
         width="90"
         height="90"
         alt="Manav-Arora4" />
    <br/>
    <strong>@Manav-Arora4</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/Code2With-Pratik">
    <img src="https://avatars.githubusercontent.com/u/169572793?v=4&size=120"
         width="90"
         height="90"
         alt="Code2With-Pratik" />
    <br/>
    <strong>@Code2With-Pratik</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/pirmber">
    <img src="https://avatars.githubusercontent.com/u/201049843?v=4&size=120"
         width="90"
         height="90"
         alt="pirmber" />
    <br/>
    <strong>@pirmber</strong>
  </a>
</td>

</tr>
<tr>

<td align="center" width="20%">
  <a href="https://github.com/fraisasghar">
    <img src="https://avatars.githubusercontent.com/u/223228391?v=4&size=120"
         width="90"
         height="90"
         alt="fraisasghar" />
    <br/>
    <strong>@fraisasghar</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/shaaravraghu">
    <img src="https://avatars.githubusercontent.com/u/195157135?v=4&size=120"
         width="90"
         height="90"
         alt="shaaravraghu" />
    <br/>
    <strong>@shaaravraghu</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/binitkafle">
    <img src="https://avatars.githubusercontent.com/u/257916351?v=4&size=120"
         width="90"
         height="90"
         alt="binitkafle" />
    <br/>
    <strong>@binitkafle</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/callmevanshh">
    <img src="https://avatars.githubusercontent.com/u/143322008?v=4&size=120"
         width="90"
         height="90"
         alt="callmevanshh" />
    <br/>
    <strong>@callmevanshh</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/Allwyy08">
    <img src="https://avatars.githubusercontent.com/u/154124348?v=4&size=120"
         width="90"
         height="90"
         alt="Allwyy08" />
    <br/>
    <strong>@Allwyy08</strong>
  </a>
</td>

</tr>
<tr>

<td align="center" width="20%">
  <a href="https://github.com/mauriciospark">
    <img src="https://avatars.githubusercontent.com/u/60632158?v=4&size=120"
         width="90"
         height="90"
         alt="mauriciospark" />
    <br/>
    <strong>@mauriciospark</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/Jinwookaisel">
    <img src="https://avatars.githubusercontent.com/u/283231218?v=4&size=120"
         width="90"
         height="90"
         alt="Jinwookaisel" />
    <br/>
    <strong>@Jinwookaisel</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/clementbouni-arch">
    <img src="https://avatars.githubusercontent.com/u/237706224?v=4&size=120"
         width="90"
         height="90"
         alt="clementbouni-arch" />
    <br/>
    <strong>@clementbouni-arch</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/kimchannchon">
    <img src="https://avatars.githubusercontent.com/u/67007450?v=4&size=120"
         width="90"
         height="90"
         alt="kimchannchon" />
    <br/>
    <strong>@kimchannchon</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/bishal-og">
    <img src="https://avatars.githubusercontent.com/u/336500620?v=4&size=120"
         width="90"
         height="90"
         alt="bishal-og" />
    <br/>
    <strong>@bishal-og</strong>
  </a>
</td>

</tr>
<tr>

<td align="center" width="20%">
  <a href="https://github.com/marlone-prog">
    <img src="https://avatars.githubusercontent.com/u/345758342?v=4&size=120"
         width="90"
         height="90"
         alt="marlone-prog" />
    <br/>
    <strong>@marlone-prog</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/pranishkoirala90394">
    <img src="https://avatars.githubusercontent.com/u/334437461?v=4&size=120"
         width="90"
         height="90"
         alt="pranishkoirala90394" />
    <br/>
    <strong>@pranishkoirala90394</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/fmoorenoo">
    <img src="https://avatars.githubusercontent.com/u/151165920?v=4&size=120"
         width="90"
         height="90"
         alt="fmoorenoo" />
    <br/>
    <strong>@fmoorenoo</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/leduc121">
    <img src="https://avatars.githubusercontent.com/u/143080413?v=4&size=120"
         width="90"
         height="90"
         alt="leduc121" />
    <br/>
    <strong>@leduc121</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/abhigyan6">
    <img src="https://avatars.githubusercontent.com/u/84132249?v=4&size=120"
         width="90"
         height="90"
         alt="abhigyan6" />
    <br/>
    <strong>@abhigyan6</strong>
  </a>
</td>

</tr>
<tr>

<td align="center" width="20%">
  <a href="https://github.com/Raph049">
    <img src="https://avatars.githubusercontent.com/u/130841437?v=4&size=120"
         width="90"
         height="90"
         alt="Raph049" />
    <br/>
    <strong>@Raph049</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/SriramBharath-7">
    <img src="https://avatars.githubusercontent.com/u/213016158?v=4&size=120"
         width="90"
         height="90"
         alt="SriramBharath-7" />
    <br/>
    <strong>@SriramBharath-7</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/codeby-Vishwajeet">
    <img src="https://avatars.githubusercontent.com/u/280482873?v=4&size=120"
         width="90"
         height="90"
         alt="codeby-Vishwajeet" />
    <br/>
    <strong>@codeby-Vishwajeet</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/Abishek0070">
    <img src="https://avatars.githubusercontent.com/u/221973912?v=4&size=120"
         width="90"
         height="90"
         alt="Abishek0070" />
    <br/>
    <strong>@Abishek0070</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/jy7lsna">
    <img src="https://avatars.githubusercontent.com/u/121849188?v=4&size=120"
         width="90"
         height="90"
         alt="jy7lsna" />
    <br/>
    <strong>@jy7lsna</strong>
  </a>
</td>

</tr>
<tr>

<td align="center" width="20%">
  <a href="https://github.com/Prajyot-Desai">
    <img src="https://avatars.githubusercontent.com/u/181592667?v=4&size=120"
         width="90"
         height="90"
         alt="Prajyot-Desai" />
    <br/>
    <strong>@Prajyot-Desai</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/samertall">
    <img src="https://avatars.githubusercontent.com/u/52387110?v=4&size=120"
         width="90"
         height="90"
         alt="samertall" />
    <br/>
    <strong>@samertall</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/joao-g">
    <img src="https://avatars.githubusercontent.com/u/253616805?v=4&size=120"
         width="90"
         height="90"
         alt="joao-g" />
    <br/>
    <strong>@joao-g</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/ryugacodesgit">
    <img src="https://avatars.githubusercontent.com/u/349170142?v=4&size=120"
         width="90"
         height="90"
         alt="ryugacodesgit" />
    <br/>
    <strong>@ryugacodesgit</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/anshk1234">
    <img src="https://avatars.githubusercontent.com/u/160382375?v=4&size=120"
         width="90"
         height="90"
         alt="anshk1234" />
    <br/>
    <strong>@anshk1234</strong>
  </a>
</td>

</tr>
<tr>

<td align="center" width="20%">
  <a href="https://github.com/darshanworkplace30">
    <img src="https://avatars.githubusercontent.com/u/296192757?v=4&size=120"
         width="90"
         height="90"
         alt="darshanworkplace30" />
    <br/>
    <strong>@darshanworkplace30</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/Kukzze">
    <img src="https://avatars.githubusercontent.com/u/91667682?v=4&size=120"
         width="90"
         height="90"
         alt="Kukzze" />
    <br/>
    <strong>@Kukzze</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/Juan-Miguel-alvarado">
    <img src="https://avatars.githubusercontent.com/u/109107814?v=4&size=120"
         width="90"
         height="90"
         alt="Juan-Miguel-alvarado" />
    <br/>
    <strong>@Juan-Miguel-alvarado</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/donaldraph">
    <img src="https://avatars.githubusercontent.com/u/62525712?v=4&size=120"
         width="90"
         height="90"
         alt="donaldraph" />
    <br/>
    <strong>@donaldraph</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/Rosy-Dev">
    <img src="https://avatars.githubusercontent.com/u/258010841?v=4&size=120"
         width="90"
         height="90"
         alt="Rosy-Dev" />
    <br/>
    <strong>@Rosy-Dev</strong>
  </a>
</td>

</tr>
<tr>

<td align="center" width="20%">
  <a href="https://github.com/khalidabdifetah9">
    <img src="https://avatars.githubusercontent.com/u/312366118?v=4&size=120"
         width="90"
         height="90"
         alt="khalidabdifetah9" />
    <br/>
    <strong>@khalidabdifetah9</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/NathanX23">
    <img src="https://avatars.githubusercontent.com/u/201589790?v=4&size=120"
         width="90"
         height="90"
         alt="NathanX23" />
    <br/>
    <strong>@NathanX23</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/ineedfoundmyway">
    <img src="https://avatars.githubusercontent.com/u/329826984?v=4&size=120"
         width="90"
         height="90"
         alt="ineedfoundmyway" />
    <br/>
    <strong>@ineedfoundmyway</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/gotkunal15">
    <img src="https://avatars.githubusercontent.com/u/311084442?v=4&size=120"
         width="90"
         height="90"
         alt="gotkunal15" />
    <br/>
    <strong>@gotkunal15</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/petrosalex">
    <img src="https://avatars.githubusercontent.com/u/19343014?v=4&size=120"
         width="90"
         height="90"
         alt="petrosalex" />
    <br/>
    <strong>@petrosalex</strong>
  </a>
</td>

</tr>
<tr>

<td align="center" width="20%">
  <a href="https://github.com/BhuwanJoshi-01">
    <img src="https://avatars.githubusercontent.com/u/109661126?v=4&size=120"
         width="90"
         height="90"
         alt="BhuwanJoshi-01" />
    <br/>
    <strong>@BhuwanJoshi-01</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/Berserk-hub150">
    <img src="https://avatars.githubusercontent.com/u/89993099?v=4&size=120"
         width="90"
         height="90"
         alt="Berserk-hub150" />
    <br/>
    <strong>@Berserk-hub150</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/ADITYA-KUMAR-2358">
    <img src="https://avatars.githubusercontent.com/u/131487393?v=4&size=120"
         width="90"
         height="90"
         alt="ADITYA-KUMAR-2358" />
    <br/>
    <strong>@ADITYA-KUMAR-2358</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/sahitya1903">
    <img src="https://avatars.githubusercontent.com/u/83616018?v=4&size=120"
         width="90"
         height="90"
         alt="sahitya1903" />
    <br/>
    <strong>@sahitya1903</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/CacheClown">
    <img src="https://avatars.githubusercontent.com/u/171366273?v=4&size=120"
         width="90"
         height="90"
         alt="CacheClown" />
    <br/>
    <strong>@CacheClown</strong>
  </a>
</td>

</tr>
<tr>

<td align="center" width="20%">
  <a href="https://github.com/nopedal">
    <img src="https://avatars.githubusercontent.com/u/84512230?v=4&size=120"
         width="90"
         height="90"
         alt="nopedal" />
    <br/>
    <strong>@nopedal</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/ampratapsingh">
    <img src="https://avatars.githubusercontent.com/u/179601648?v=4&size=120"
         width="90"
         height="90"
         alt="ampratapsingh" />
    <br/>
    <strong>@ampratapsingh</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/ozrd">
    <img src="https://avatars.githubusercontent.com/u/272019955?v=4&size=120"
         width="90"
         height="90"
         alt="ozrd" />
    <br/>
    <strong>@ozrd</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/nerfsaksham">
    <img src="https://avatars.githubusercontent.com/u/325280059?v=4&size=120"
         width="90"
         height="90"
         alt="nerfsaksham" />
    <br/>
    <strong>@nerfsaksham</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/Armen5570">
    <img src="https://avatars.githubusercontent.com/u/286051936?v=4&size=120"
         width="90"
         height="90"
         alt="Armen5570" />
    <br/>
    <strong>@Armen5570</strong>
  </a>
</td>

</tr>
<tr>

<td align="center" width="20%">
  <a href="https://github.com/DMS-Menula">
    <img src="https://avatars.githubusercontent.com/u/186381241?v=4&size=120"
         width="90"
         height="90"
         alt="DMS-Menula" />
    <br/>
    <strong>@DMS-Menula</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/mzainulabideendev">
    <img src="https://avatars.githubusercontent.com/u/325703180?v=4&size=120"
         width="90"
         height="90"
         alt="mzainulabideendev" />
    <br/>
    <strong>@mzainulabideendev</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/sarbatra3">
    <img src="https://avatars.githubusercontent.com/u/352874139?v=4&size=120"
         width="90"
         height="90"
         alt="sarbatra3" />
    <br/>
    <strong>@sarbatra3</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/infinityRazor3">
    <img src="https://avatars.githubusercontent.com/u/351104737?v=4&size=120"
         width="90"
         height="90"
         alt="infinityRazor3" />
    <br/>
    <strong>@infinityRazor3</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/sarang-devb">
    <img src="https://avatars.githubusercontent.com/u/353216818?v=4&size=120"
         width="90"
         height="90"
         alt="sarang-devb" />
    <br/>
    <strong>@sarang-devb</strong>
  </a>
</td>

</tr>
<tr>

<td align="center" width="20%">
  <a href="https://github.com/akash3893">
    <img src="https://avatars.githubusercontent.com/u/353268786?v=4&size=120"
         width="90"
         height="90"
         alt="akash3893" />
    <br/>
    <strong>@akash3893</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/ldsh-weilinlai">
    <img src="https://avatars.githubusercontent.com/u/323045087?v=4&size=120"
         width="90"
         height="90"
         alt="ldsh-weilinlai" />
    <br/>
    <strong>@ldsh-weilinlai</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/gogozza11">
    <img src="https://avatars.githubusercontent.com/u/273905449?v=4&size=120"
         width="90"
         height="90"
         alt="gogozza11" />
    <br/>
    <strong>@gogozza11</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/armenhar636-source">
    <img src="https://avatars.githubusercontent.com/u/343832237?v=4&size=120"
         width="90"
         height="90"
         alt="armenhar636-source" />
    <br/>
    <strong>@armenhar636-source</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/atjos">
    <img src="https://avatars.githubusercontent.com/u/65507292?v=4&size=120"
         width="90"
         height="90"
         alt="atjos" />
    <br/>
    <strong>@atjos</strong>
  </a>
</td>

</tr>
<tr>

<td align="center" width="20%">
  <a href="https://github.com/doom-cli">
    <img src="https://avatars.githubusercontent.com/u/266218443?v=4&size=120"
         width="90"
         height="90"
         alt="doom-cli" />
    <br/>
    <strong>@doom-cli</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/kdbewn23">
    <img src="https://avatars.githubusercontent.com/u/353790502?v=4&size=120"
         width="90"
         height="90"
         alt="kdbewn23" />
    <br/>
    <strong>@kdbewn23</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/lovesmesjhy3">
    <img src="https://avatars.githubusercontent.com/u/353794131?v=4&size=120"
         width="90"
         height="90"
         alt="lovesmesjhy3" />
    <br/>
    <strong>@lovesmesjhy3</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/kdgbh23">
    <img src="https://avatars.githubusercontent.com/u/353797010?v=4&size=120"
         width="90"
         height="90"
         alt="kdgbh23" />
    <br/>
    <strong>@kdgbh23</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/lartesh2">
    <img src="https://avatars.githubusercontent.com/u/353804809?v=4&size=120"
         width="90"
         height="90"
         alt="lartesh2" />
    <br/>
    <strong>@lartesh2</strong>
  </a>
</td>

</tr>
<tr>

<td align="center" width="20%">
  <a href="https://github.com/lowlifecodezero">
    <img src="https://avatars.githubusercontent.com/u/353807470?v=4&size=120"
         width="90"
         height="90"
         alt="lowlifecodezero" />
    <br/>
    <strong>@lowlifecodezero</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/web3wizzz">
    <img src="https://avatars.githubusercontent.com/u/236838012?v=4&size=120"
         width="90"
         height="90"
         alt="web3wizzz" />
    <br/>
    <strong>@web3wizzz</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/dr1node">
    <img src="https://avatars.githubusercontent.com/u/235500152?v=4&size=120"
         width="90"
         height="90"
         alt="dr1node" />
    <br/>
    <strong>@dr1node</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/rrsd2769">
    <img src="https://avatars.githubusercontent.com/u/174997233?v=4&size=120"
         width="90"
         height="90"
         alt="rrsd2769" />
    <br/>
    <strong>@rrsd2769</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/henry9438">
    <img src="https://avatars.githubusercontent.com/u/353799493?v=4&size=120"
         width="90"
         height="90"
         alt="henry9438" />
    <br/>
    <strong>@henry9438</strong>
  </a>
</td>

</tr>
<tr>

<td align="center" width="20%">
  <a href="https://github.com/braachcc">
    <img src="https://avatars.githubusercontent.com/u/353682133?v=4&size=120"
         width="90"
         height="90"
         alt="braachcc" />
    <br/>
    <strong>@braachcc</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/andriymelnyk1997">
    <img src="https://avatars.githubusercontent.com/u/46633744?v=4&size=120"
         width="90"
         height="90"
         alt="andriymelnyk1997" />
    <br/>
    <strong>@andriymelnyk1997</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/Professor-101">
    <img src="https://avatars.githubusercontent.com/u/277202135?v=4&size=120"
         width="90"
         height="90"
         alt="Professor-101" />
    <br/>
    <strong>@Professor-101</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/Aurokrishnaa">
    <img src="https://avatars.githubusercontent.com/u/191313144?v=4&size=120"
         width="90"
         height="90"
         alt="Aurokrishnaa" />
    <br/>
    <strong>@Aurokrishnaa</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/YashasHK-06">
    <img src="https://avatars.githubusercontent.com/u/197676148?v=4&size=120"
         width="90"
         height="90"
         alt="YashasHK-06" />
    <br/>
    <strong>@YashasHK-06</strong>
  </a>
</td>

</tr>
<tr>

<td align="center" width="20%">
  <a href="https://github.com/yueffhjg">
    <img src="https://avatars.githubusercontent.com/u/352319362?v=4&size=120"
         width="90"
         height="90"
         alt="yueffhjg" />
    <br/>
    <strong>@yueffhjg</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/spideythedev">
    <img src="https://avatars.githubusercontent.com/u/221688867?v=4&size=120"
         width="90"
         height="90"
         alt="spideythedev" />
    <br/>
    <strong>@spideythedev</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/leaderfrank">
    <img src="https://avatars.githubusercontent.com/u/19779854?v=4&size=120"
         width="90"
         height="90"
         alt="leaderfrank" />
    <br/>
    <strong>@leaderfrank</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/navadeep0508">
    <img src="https://avatars.githubusercontent.com/u/199091183?v=4&size=120"
         width="90"
         height="90"
         alt="navadeep0508" />
    <br/>
    <strong>@navadeep0508</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/punit2911">
    <img src="https://avatars.githubusercontent.com/u/144655592?v=4&size=120"
         width="90"
         height="90"
         alt="punit2911" />
    <br/>
    <strong>@punit2911</strong>
  </a>
</td>

</tr>
<tr>

<td align="center" width="20%">
  <a href="https://github.com/pa-ulander">
    <img src="https://avatars.githubusercontent.com/u/1719300?v=4&size=120"
         width="90"
         height="90"
         alt="pa-ulander" />
    <br/>
    <strong>@pa-ulander</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/abinasharma001">
    <img src="https://avatars.githubusercontent.com/u/83633679?v=4&size=120"
         width="90"
         height="90"
         alt="abinasharma001" />
    <br/>
    <strong>@abinasharma001</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/vyasanbmathew2008">
    <img src="https://avatars.githubusercontent.com/u/285423314?v=4&size=120"
         width="90"
         height="90"
         alt="vyasanbmathew2008" />
    <br/>
    <strong>@vyasanbmathew2008</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/jamiejustcodes">
    <img src="https://avatars.githubusercontent.com/u/306206816?v=4&size=120"
         width="90"
         height="90"
         alt="jamiejustcodes" />
    <br/>
    <strong>@jamiejustcodes</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/rudra-xi">
    <img src="https://avatars.githubusercontent.com/u/164514144?v=4&size=120"
         width="90"
         height="90"
         alt="rudra-xi" />
    <br/>
    <strong>@rudra-xi</strong>
  </a>
</td>

</tr>
<tr>

<td align="center" width="20%">
  <a href="https://github.com/ThomasWack">
    <img src="https://avatars.githubusercontent.com/u/264466934?v=4&size=120"
         width="90"
         height="90"
         alt="ThomasWack" />
    <br/>
    <strong>@ThomasWack</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/iyawnnn">
    <img src="https://avatars.githubusercontent.com/u/151660400?v=4&size=120"
         width="90"
         height="90"
         alt="iyawnnn" />
    <br/>
    <strong>@iyawnnn</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/senoritekoti">
    <img src="https://avatars.githubusercontent.com/u/319553613?v=4&size=120"
         width="90"
         height="90"
         alt="senoritekoti" />
    <br/>
    <strong>@senoritekoti</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/swarn007-byte">
    <img src="https://avatars.githubusercontent.com/u/235354922?v=4&size=120"
         width="90"
         height="90"
         alt="swarn007-byte" />
    <br/>
    <strong>@swarn007-byte</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/freeopensourcesorftwarelover">
    <img src="https://avatars.githubusercontent.com/u/354397807?v=4&size=120"
         width="90"
         height="90"
         alt="freeopensourcesorftwarelover" />
    <br/>
    <strong>@freeopensourcesorftwarelover</strong>
  </a>
</td>

</tr>
<tr>

<td align="center" width="20%">
  <a href="https://github.com/Ilakkiyaa2k8">
    <img src="https://avatars.githubusercontent.com/u/190212610?v=4&size=120"
         width="90"
         height="90"
         alt="Ilakkiyaa2k8" />
    <br/>
    <strong>@Ilakkiyaa2k8</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/kalidevali">
    <img src="https://avatars.githubusercontent.com/u/332364003?v=4&size=120"
         width="90"
         height="90"
         alt="kalidevali" />
    <br/>
    <strong>@kalidevali</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/alexandereyyey-prog">
    <img src="https://avatars.githubusercontent.com/u/295306620?v=4&size=120"
         width="90"
         height="90"
         alt="alexandereyyey-prog" />
    <br/>
    <strong>@alexandereyyey-prog</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/nothingcodex">
    <img src="https://avatars.githubusercontent.com/u/357257574?v=4&size=120"
         width="90"
         height="90"
         alt="nothingcodex" />
    <br/>
    <strong>@nothingcodex</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/Dark-Brain07">
    <img src="https://avatars.githubusercontent.com/u/85172976?v=4&size=120"
         width="90"
         height="90"
         alt="Dark-Brain07" />
    <br/>
    <strong>@Dark-Brain07</strong>
  </a>
</td>

</tr>
<tr>

<td align="center" width="20%">
  <a href="https://github.com/Calyxia">
    <img src="https://avatars.githubusercontent.com/u/316318074?v=4&size=120"
         width="90"
         height="90"
         alt="Calyxia" />
    <br/>
    <strong>@Calyxia</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/ehsaanullah0">
    <img src="https://avatars.githubusercontent.com/u/225146296?v=4&size=120"
         width="90"
         height="90"
         alt="ehsaanullah0" />
    <br/>
    <strong>@ehsaanullah0</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/ayxanuser123">
    <img src="https://avatars.githubusercontent.com/u/358381657?v=4&size=120"
         width="90"
         height="90"
         alt="ayxanuser123" />
    <br/>
    <strong>@ayxanuser123</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/SpolyCode">
    <img src="https://avatars.githubusercontent.com/u/171841122?v=4&size=120"
         width="90"
         height="90"
         alt="SpolyCode" />
    <br/>
    <strong>@SpolyCode</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/perashanid">
    <img src="https://avatars.githubusercontent.com/u/155494150?v=4&size=120"
         width="90"
         height="90"
         alt="perashanid" />
    <br/>
    <strong>@perashanid</strong>
  </a>
</td>

</tr>
<tr>

<td align="center" width="20%">
  <a href="https://github.com/royalpriest">
    <img src="https://avatars.githubusercontent.com/u/88779808?v=4&size=120"
         width="90"
         height="90"
         alt="royalpriest" />
    <br/>
    <strong>@royalpriest</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/MerrickHayes">
    <img src="https://avatars.githubusercontent.com/u/174679699?v=4&size=120"
         width="90"
         height="90"
         alt="MerrickHayes" />
    <br/>
    <strong>@MerrickHayes</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/Grish2063">
    <img src="https://avatars.githubusercontent.com/u/215848097?v=4&size=120"
         width="90"
         height="90"
         alt="Grish2063" />
    <br/>
    <strong>@Grish2063</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/mudassiralladatkhan">
    <img src="https://avatars.githubusercontent.com/u/208343323?v=4&size=120"
         width="90"
         height="90"
         alt="mudassiralladatkhan" />
    <br/>
    <strong>@mudassiralladatkhan</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/krishbuilds01">
    <img src="https://avatars.githubusercontent.com/u/129619885?v=4&size=120"
         width="90"
         height="90"
         alt="krishbuilds01" />
    <br/>
    <strong>@krishbuilds01</strong>
  </a>
</td>

</tr>
<tr>

<td align="center" width="20%">
  <a href="https://github.com/Aashritha-2005">
    <img src="https://avatars.githubusercontent.com/u/199344908?v=4&size=120"
         width="90"
         height="90"
         alt="Aashritha-2005" />
    <br/>
    <strong>@Aashritha-2005</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/arnavseth12">
    <img src="https://avatars.githubusercontent.com/u/241027327?v=4&size=120"
         width="90"
         height="90"
         alt="arnavseth12" />
    <br/>
    <strong>@arnavseth12</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/Sri99varsan">
    <img src="https://avatars.githubusercontent.com/u/98585195?v=4&size=120"
         width="90"
         height="90"
         alt="Sri99varsan" />
    <br/>
    <strong>@Sri99varsan</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/thanos-titan">
    <img src="https://avatars.githubusercontent.com/u/308982418?v=4&size=120"
         width="90"
         height="90"
         alt="thanos-titan" />
    <br/>
    <strong>@thanos-titan</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/amanda09486-sudo">
    <img src="https://avatars.githubusercontent.com/u/359854545?v=4&size=120"
         width="90"
         height="90"
         alt="amanda09486-sudo" />
    <br/>
    <strong>@amanda09486-sudo</strong>
  </a>
</td>

</tr>
<tr>

<td align="center" width="20%">
  <a href="https://github.com/Malick-Tammal">
    <img src="https://avatars.githubusercontent.com/u/63257939?v=4&size=120"
         width="90"
         height="90"
         alt="Malick-Tammal" />
    <br/>
    <strong>@Malick-Tammal</strong>
  </a>
</td>


<td align="center" width="20%">
  <a href="https://github.com/rodrigomourapinto">
    <img src="https://avatars.githubusercontent.com/u/174130487?v=4&size=120"
         width="90"
         height="90"
         alt="rodrigomourapinto" />
    <br/>
    <strong>@rodrigomourapinto</strong>
  </a>
</td>

</tr>
</table>

<div align="center">

*Made possible by this amazing community!*

</div>

<!-- STARGAZERS:END -->

